import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, notify, create_bars, create_cake
import datetime

from email_validator import validate_email, EmailNotValidError

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():

    """Show portfolio of stocks"""

    records = db.execute('select symbol, name, sum(shares) from records WHERE id_user = :id GROUP by symbol HAVING sum(shares) != 0',id=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    user = db.execute("SELECT username, email FROM users WHERE id = :id", id=session["user_id"])

    total_assets = 0

    # the price is updated for each records query
    for item in records:
        item['current_price'] = usd(lookup(item['symbol'])['price'])
        item['total'] = usd(lookup(item['symbol'])['price'] * item['sum(shares)'])
        item['query_time'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_assets = total_assets + lookup(item['symbol'])['price'] * item['sum(shares)']

    balance = cash[0]['cash'] + total_assets

    sizes = [float(dictionary['total'].replace('$','').replace(',','')) for dictionary in records] + [cash[0]['cash']]
    labels = [dictionary['symbol'] for dictionary in records] + ['CASH']

    db.execute("INSERT INTO holdings (id_user, timestamp, total) VALUES (:id_user, :timestamp, :total)", 
        id_user=session["user_id"],
        timestamp=datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        total=balance)

    holdings = db.execute('SELECT timestamp, total from holdings WHERE id_user = :id',id=session["user_id"])

    time = [dictionary['timestamp'] for dictionary in holdings]
    total = [round(dictionary['total'],2) for dictionary in holdings]
    
    """show price holdings variation with bar graph"""
    """show composition of assets with cake"""
    if balance != 0:
        cake = create_cake(sizes, labels)
        bars = create_bars(time[-10:-1], total[-10:-1])
        return render_template('index.html', 
                    rows=records, 
                    total_cash= usd(cash[0]['cash']),
                    balance= usd(balance),
                    user=user[0]['username'],
                    plot_bars=bars,
                    plot_cake=cake)
    else:
        return render_template('index.html', 
            rows=records, 
            total_cash= usd(cash[0]['cash']),
            balance= usd(balance),
            user=user[0]['username'])


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        ticker = lookup(request.form.get("symbol"))

        if ticker == None:
            flash('Ticker doesn\'t exist')
            return render_template("buy.html")

        query = db.execute("SELECT cash FROM users WHERE id = :id",
            id=session["user_id"])

        if (int(request.form.get("shares"))*ticker['price']) > query[0]['cash']:
            flash('You don\'t have enough cash')
            return render_template("buy.html")
        else:
            db.execute("INSERT INTO records (id_user, symbol, name, shares, price, time_stamp) VALUES (:id_user, :symbol, :name, :shares, :price, :time_stamp)", 
                id_user=session["user_id"], 
                symbol=ticker['symbol'], 
                name=ticker['name'], 
                shares=int(request.form.get("shares")), 
                price=(int(request.form.get("shares"))*ticker['price']), 
                time_stamp=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            
            db.execute("UPDATE users SET cash = :cash WHERE id = :id", 
                cash=query[0]['cash'] - (int(request.form.get("shares"))*ticker['price']),
                id=session["user_id"])
        
        flash('You have bought {0} shares of {1} with USD {2}'.format(request.form.get("shares"), ticker['name'],int(request.form.get("shares"))*ticker['price']))
        return redirect(url_for('index'))

    else:
        user = db.execute("SELECT username FROM users WHERE id = :id", id=session["user_id"])
        return render_template("buy.html",
            user=user[0]['username'])

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    records = db.execute('select symbol, shares, price, time_stamp from records WHERE id_user = :id',id=session["user_id"])
    
    for item in records:
        item['price'] = usd(item['price'])
    
    user = db.execute("SELECT username FROM users WHERE id = :id", id=session["user_id"])

    return render_template("history.html", 
        rows=records,
        user=user[0]['username'])

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash('Invalid username and/or password')
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect(url_for('index'))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        ticker = lookup(request.form.get("symbol"))

        if ticker == None:
            flash('Symbol doesn\'t exist')
            return render_template("quote.html")
        else:
            return render_template("quoted.html", message='A share of {0} ({1}) costs ({2})'.format(ticker['name'],ticker['symbol'],usd(ticker['price'])))
    else:
        user = db.execute("SELECT username FROM users WHERE id = :id", id=session["user_id"])
        return render_template("quote.html",
            user=user[0]['username'])

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Ensure password is confirmed
        if request.form.get("password") != request.form.get("confirmation"):
            flash('Passwords don\'t match')
            return render_template("register.html")
               
        # Query database for username and password
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                        username=request.form.get("username"))

        # Ensure username does not exist and password is correct
        # if there is a row, there is a username
        if len(rows) == 1:
            flash('User already exists')
            return render_template("register.html")

        # if everything is fine, insert new record
        db.execute("INSERT INTO users (username,email,hash) VALUES (:username, :email, :hash)", 
            username=request.form.get("username"),
            email=request.form.get("email"),
            hash=generate_password_hash(request.form.get("password")))

        # get registered users
        rows = db.execute("SELECT * FROM users")

        # Remember which user has just registered
        session["user_id"] = rows[-1]["id"]

        # Redirect user to home page
        flash(f'You have successfully registered! Welcome {rows[-1]["username"]} to Digital Brokers')
        return redirect(url_for('index'))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":

        ticker = lookup(request.form.get("symbol"))

        query = db.execute("SELECT cash FROM users WHERE id = :id",
            id=session["user_id"])

        records = db.execute("SELECT sum(shares) FROM records WHERE id_user = :id_user AND symbol = :symbol",
            id_user=session["user_id"], symbol=ticker['symbol'])

        if (int(request.form.get("shares"))) > records[0]['sum(shares)']:
            flash('You are trying to sell too many shares')
            return redirect(url_for('sell'))
        else:
            residue = (int(request.form.get("shares"))) * ticker['price']
            db.execute("INSERT INTO records (id_user, symbol, name, shares, price, time_stamp) VALUES (:id_user, :symbol, :name, :shares, :price, :time_stamp)", 
                id_user=session["user_id"], 
                symbol=ticker['symbol'], 
                name=ticker['name'], 
                shares= int(request.form.get("shares")) * -1, 
                price= ticker['price'], 
                time_stamp=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            
            db.execute("UPDATE users SET cash = :cash WHERE id = :id", 
                cash=query[0]['cash'] + residue,
                id=session["user_id"])
        
        flash('You have sold {0} share(s) of {1} at USD {2} total'.format(request.form.get("shares"), ticker['name'],int(request.form.get("shares"))*ticker['price']))
        return redirect(url_for('index'))

    else:
        user = db.execute("SELECT username FROM users WHERE id = :id", id=session["user_id"])
        query = db.execute("SELECT symbol FROM records WHERE id_user = :id_user", id_user=session["user_id"])
        return render_template("sell.html",
            user=user[0]['username'], 
            tickers= list(set([query[x]['symbol'] for x in range(len(query))])))

@app.route("/account")
@login_required
def account():

    user = db.execute("SELECT username, email FROM users WHERE id = :id", id=session["user_id"])
    return render_template("account.html",
        user=user[0]['username'],
        email=user[0]['email'])

@app.route("/account_email", methods=["GET", "POST"])
@login_required
def account_email():

    """Edit email."""
    if request.method == "POST":

        user = db.execute("SELECT username, email FROM users WHERE id = :id", id=session["user_id"])
 
        email = request.form.get("email") 

        try:
            # Validate.
            valid = validate_email(email)

            # Update with the normalized form.
            email = valid.email

            db.execute("UPDATE users SET email = :email WHERE id = :id;",
                email=email,
                id=session["user_id"])

            flash('You have successfully changed your email!')
            return render_template("account.html",
                    user=user[0]['username'],
                    email=user[0]['email'])

        except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
            flash(str(e))
            return render_template("account.html",
                    user=user[0]['username'],
                    email=user[0]['email'])

    else:
        user = db.execute("SELECT username, email FROM users WHERE id = :id", id=session["user_id"])
        return render_template("account.html",
            user=user[0]['username'],
            email=user[0]['email'])

@app.route("/account_pass", methods=["GET", "POST"])
@login_required
def account_pass():

    """Edit password"""
    if request.method == "POST":

        user = db.execute("SELECT username, email FROM users WHERE id = :id", id=session["user_id"])

        # Ensure password is confirmed
        if request.form.get("pass") != request.form.get("confirm"):
            flash('New passwords don\'t match')
            return render_template("account.html",user=user[0]['username'])

        else:
            db.execute("UPDATE users SET hash = :hash WHERE id = :id;",
                            hash=generate_password_hash(request.form.get("pass")),
                            id=session["user_id"])

            flash('You have successfully changed password!')
            return render_template("account.html",user=user[0]['username'])

    else:
        user = db.execute("SELECT username, email FROM users WHERE id = :id", id=session["user_id"])
        return render_template("account.html",
            user=user[0]['username'],
            email=user[0]['email'])

@app.route("/account_cash", methods=["GET", "POST"])
@login_required
def account_cash():

    """Input cash"""
    if request.method == "POST":

        user = db.execute("SELECT username, email, cash FROM users WHERE id = :id", id=session["user_id"])

        if int(request.form.get("cash")) > 10000:
            flash('Invalid amount - exceeds legal restrictions')
            return render_template("account.html",user=user[0]['username'])

        elif int(request.form.get("cash")) <= 0:
            flash('Not enough cash')
            return render_template("account.html",user=user[0]['username'])

        else:
            # Update username and password
            db.execute("UPDATE users SET cash = :cash WHERE id = :id;",
                            cash=user[0]['cash']+int(request.form.get("cash")),
                            id=session["user_id"])

            flash('Credited Cash')
            return render_template("account.html",user=user[0]['username'])

    else:
        user = db.execute("SELECT username, email FROM users WHERE id = :id", id=session["user_id"])
        return render_template("account.html",
            user=user[0]['username'],
            email=user[0]['email'])


@app.route("/cash_out")
@login_required
def cash_out():
    """Cash out assets"""
  
    records = db.execute('select symbol, name, sum(shares) from records WHERE id_user = :id GROUP by symbol HAVING sum(shares) != 0',id=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    user = db.execute("SELECT username FROM users WHERE id = :id", id=session["user_id"])
    
    total_shares = 0
    for item in records:
        total_shares = total_shares + lookup(item['symbol'])['price'] * item['sum(shares)']

    balance = cash[0]['cash'] + total_shares
    no_shares = sum([records[item]['sum(shares)'] for item in range(len(records))])

    if balance == 0:
        flash('You have just collected all your holdings')
        return redirect(url_for('index'))
    else:
        return render_template("cash_out.html",
            user=user[0]['username'],
            total_cash= usd(cash[0]['cash']),
            total_shares=usd(total_shares),
            shares=no_shares,
            balance= usd(balance))

@app.route('/button')
def button():

    records = db.execute('select symbol, name, sum(shares) from records WHERE id_user = :id GROUP by symbol HAVING sum(shares) != 0',id=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    user = db.execute("SELECT id, username, email FROM users WHERE id = :id", id=session["user_id"])
    
    total = 0
    for item in records:
        total = total + lookup(item['symbol'])['price'] * item['sum(shares)']
    total = total + cash[0]['cash']

    db.execute("INSERT INTO cash_out (id_user, username, time_stamp, total_collected) VALUES (:id_user, :username, :time_stamp, :total_collected)", 
        id_user=user[0]['id'],
        username=user[0]['username'],
        time_stamp=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        total_collected=total)
    
    db.execute('DELETE FROM records WHERE id_user = :id_user', id_user=session["user_id"])
    db.execute('DELETE FROM holdings WHERE id_user = :id_user', id_user=session["user_id"])
    db.execute('UPDATE users SET cash = 0 WHERE id = :id;', id=session["user_id"])

    notify(user[0]['username'],user[0]['email'],usd(total))

    return redirect(url_for('cash_out'))

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
