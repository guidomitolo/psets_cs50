while True:
    height = input("Height: ")
    if height.isdigit():
        if 0 < int(height) < 9:
            height = int(height)
            break

print(height)

for levels in range(height):
    for spaces in range(height-(levels+1)):
        print(" ",end='')
    for bricks in range(levels+1):
        print("#",end='')
    for center in range(2):
        print(" ",end='')
    for bricks in range(levels+1):
        print("#",end='')
    print()