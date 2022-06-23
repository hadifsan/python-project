
secret_word = "rengoku"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("Guess who died in Mugen Train Movies")
print("Do you want to play?")
answer = input("yes or no: ")
if answer == "yes":
    while guess != secret_word and not(out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
        else:
            out_of_guesses = True
elif answer == "no":
    print("come back later")

else:
    print("please enter yes or no only")

if out_of_guesses:
    print("Out of guesses, you lose!")

else:
    print("You win!")