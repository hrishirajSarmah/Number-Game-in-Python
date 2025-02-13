import random

print("~~Welcome to the Number guessing game!~~")
print("""Rules:
1. Select number of rounds you wanna play.
2. You will get 5 attempts per round.
3. Each round has 5 points. If you answer in 1st attempt, you get 5 points, 2nd attempt 4 points and so on.
4. At the end the total score is calculated. After all rounds.
5. For each round a new random number is generated between 1-100.\n""")



rounds = int(input("Enter number of rounds: "))
score = 0

for i in range(1, rounds+1):
    num = random.randint(1, 100)
    print(f"Round {i}: Generating a random number...\n")

    attempts, points = 5, 0

    while attempts > 0:
        try:
            x = int(input("Guess the correct number. Your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue


        if x == num:
            print("🎉Congrats! You guessed it right!\nGenerated random number: {}\nYour guess: {}".format(num, x))
            points=attempts
            break
        attempts -= 1
        if attempts > 0:
            print("❌Your guess is incorrect! Try again.")
            if max(1, num-5) <= x <= min(100, num+5):  #an issue might arise here if the randomly generated number is <=5 or >=95
                print("🔥Fet's luck!! Close, but not quite. ;(")
            elif x > num:
                print("⬇️Go lower human!!")
            else:
                print("⬆️Go higher human!!")

            print(f"Attempts remaining: {attempts}")
        elif attempts == 0:
            print(f"❌Incorrect guess.\nYou've exhausted all attempts.\nGenerated random number: {num}\nYour last guess: {x}")
        print("\n")
    score += points
    print("🎯Points for round {} is {}".format(i, points))
print(f"\n🏆Final score: {score}")