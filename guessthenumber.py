secret = 6

guess = 0

while guess != secret:

    guess = int(input("enter the number: "))

    if guess < secret:
        print("too small")

    elif guess > secret:
        print("too big")

    else:
        print("correct")