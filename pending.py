##project:1 return how many words in sentences

##name=input("enter the words")
##name2={}
##for i in name:
##    if i in name2:
##        name2[i]+=1
##    else:
##        name2[i]=1
##for x,y in name2.items():
##    print(f"{x}-{y}")
##
##        
  
##next permutation:
##nums=[1,2,3]
##nums.remove(3)
##print(nums)
##nums.insert(1,3)
##print(nums)

## project:BMI calucator 
##weight=float(input("enter the  weight in kg"))
##height=float(input("enter the height in meter"))
##BMI=weight/height**2
##print(BMI)
##if BMI< 18.25:
##    print("under weight")
##elif BMI< 50:
##    print("healthy weight")
##else:
##    print("over weight")


##project:quiz game

player=input("do you want to play the game")
if player !="yes":
    quit()
print("ok lets play")
score=0
question=input("1. Who developed Python Programming Language?")
if question.lower()=="Guido van Rossum":
    print("correct")
    score+=1
else:
    print("incorrect")

    
