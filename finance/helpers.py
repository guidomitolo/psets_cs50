import os
import requests
import urllib.parse
import smtplib
from cs50 import SQL
import base64
from base64 import b64encode

from flask import redirect, render_template, request, session
from functools import wraps

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        response = requests.get(f"https://cloud-sse.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}")
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def notify(username, user_email, cash):

    db = SQL("sqlite:///finance.db")
    adm = db.execute("SELECT * FROM adm;")

    sender = adm[0]['email']
    password = base64.b64decode(adm[0]['coded_pass']).decode("utf-8")

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender, password)

        subject='CASH OUT - DIGITAL BROKERS'
        body = f'Dear {username},\n\nThe total value of your holdings, up to {cash}, have been transfered to you.\n\nThanks for using Digital Brokers'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(sender, f"{user_email}", msg)

def create_bars(time, total):

    bytes_image_bars = io.BytesIO()

    matplotlib.use('Agg')
    fig = plt.figure()
    ax = plt.axes()
    ax.bar(time,total)
    plt.ylim(5000,15000)
    plt.xticks(rotation=45,rotation_mode="anchor", ha="right")
    plt.tight_layout()

    plt.savefig(bytes_image_bars, format='png')
    bytes_image_bars.seek(0)

    canvas = FigureCanvas(fig)
    canvas.print_png(bytes_image_bars)

    plot_bars= b64encode(bytes_image_bars.getvalue()).decode('ascii')
    bytes_image_bars.seek(0)
    plt.close()
    
    return plot_bars

def create_cake(sizes, labels):

    bytes_image_cake = io.BytesIO()
    matplotlib.use('Agg')

    fig = plt.figure()
    ax = plt.axes()
    ax.pie(sizes, labels=labels)
    ax.axis('equal')
    plt.tight_layout()

    plt.savefig(bytes_image_cake, format='png')
    bytes_image_cake.seek(0)

    canvas = FigureCanvas(fig)
    canvas.print_png(bytes_image_cake)

    plot_cake= b64encode(bytes_image_cake.getvalue()).decode('ascii')
    bytes_image_cake.seek(0)
    plt.close()

    return plot_cake

