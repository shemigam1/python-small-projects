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
    print("Wrong! try again... its central processing unit")

answer = input("what is a bad hacker called? ")
answer = answer.lower()
if answer == 'black hat hacker':
    print('correct, 10 points to Gryffndor!')
else:
    print("Wrong! try again... its black hat hacker")

answer = input("who created the linux kernel? ")
answer = answer.lower()
if answer == 'linus torvalds':
    print('correct, 10 points to Gryffndor!')
else:
    print("Wrong! try again... linus torvalds")
