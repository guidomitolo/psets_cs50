while True:
    number = input("Number: ")
    if number.isdigit():
            break

# Validating card number

second_last = [int(n)*2 for n in number[-2::-2]]
digits_to_sum = [int(n) for x in second_last for n in str(x)]
non_multiplied = [int(n) for n in number[-1::-2]]
to_validate = sum(digits_to_sum)+sum(non_multiplied)

if to_validate % 10 != 0:
    print('INVALID')
    exit(1)

# Checking vendor

if len(number) == 15 and int(number[0:2]) == 34 or int(number[0:2]) == 37:
        print('AMERICAN EXPRESS')
        exit(0)

if len(number) == 16 and 50 < int(number[0:2]) < 56:
        print('MASTERCARD')
        exit(0)

if len(number) == 13 or len(number) == 16 and int(number[0]) == 4:
        print('VISA')
        exit(0)

