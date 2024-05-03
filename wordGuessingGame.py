import random
print("enter your name")
name=input()
words=['rainbow','sky','heaven','forest','mountain','valley','waterfall','sea','ocean']
word=random.choice(words)
chance=7
print("start guessing the word",name,"you have 7 chances")
guesses=''
while chance>=0:
    chance-=1
    failed=0
    for i in word:
        if i in guesses:
            print(i,"\n")
        else:
            print('__',"\n")
            failed+=1
    if failed==0:
      print("You correctly guessed the word")
    print("Your next guess")  
    guess=input()
    print("....STARTING....")
    guesses+=guess

    

           