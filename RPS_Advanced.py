# This app is actually a rock paper scissors game.
# Users have the opportunity to play with each other up to 5 times and in each period, either one person wins or they are tied.
# At the end of the game, the number of wins of the first player and the number of wins of the second player are displayed, and if they are equal 
# in a period, nothing is added to the score of any of them, and if the number of wins is
# also equal at the end of the game, again are not displayed and the words "You have tied" appear on the screen.
p1_win=0
p2_win=0
for RPS in range(5):
    print("iritation ", RPS+1, ":")
    p1=input("enter the type of your game as the first person:")
    if (p1!= "r" and p1!="p" and p1!="s") :
        print("the data is not correct; try again! ")
        exit()
    p2=input("enter the type of your game as the second person:")
    if (p2!= "r" and p2!="p" and p2!="s"):
        print("the data is not correct; try again! ")
        exit()
    
    if(p1=="r" and p2=="p"):
        print("p2 won")
        p2_win+=1
    elif(p1=="p" and p2=="r"):
        print("p1 won")
        p1_win+=1
    elif(p1=="r" and p2=="s"):
        print("p1 won")
        p1_win+=1
    elif(p1=="s" and p2=="r"):
        print("p2 won")
        p2_win+=1
    elif(p1=="p" and p2=="s"):
        print("p2 won")
        p2_win+=1
    elif(p1=="s" and p2=="p"):
        print("p1 won")
        p1_win+=1
    elif(p1==p2):
        print("You are equal")

print("p1 has won  ", p1_win, " times. And p2 has won  ", p2_win," times.")
if p1_win==p2_win:
    print("You are equal")
print("The game finished")