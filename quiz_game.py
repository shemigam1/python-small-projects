# welcome the user
print("Welcome to the Glaidator Areana!")
# collect user input
playing = input("Will you proceed? ")
playing = playing.lower()
# print(playing)
if (playing != 'yes'):
    quit()

print("Let the games begin!")

answer = input("what does cpu stand for? ")
answer = answer.lower()
if answer == 'central processing unit':
    print('correct, 10 points to Gryffndor!')
else:
    print("Wrong! try again")
