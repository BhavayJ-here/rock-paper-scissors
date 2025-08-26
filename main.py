import random
k=0
def play():
    
    n=input("wanna play more?") 
    if n[0]=="y": 
        game()
    else:
        print("thanks for playing, your total score was",k)
        exit()




def game():
    z=["rock","paper","scissors"]
    v=random.choice(z)
    global k
    
    x=input("rock,paper,scissors?")
    if x[0]=="r":
        x="rock"
    if x[0]=="s":
        x="scissors"
    if x[0]=="p":
        x="paper"
    if x==v:
        print("draw")
        print("the computer had chosen",v)
        k=k+0
        play()
    c={"rock":"paper","paper":"scissors","scissors":"rock"}
    if c.get(v)==x:
        print("won")
        k=k+1
        print("the computer had chosen",v)
        play()
    else:
        print("lose")
        k=k-1
        print("the computer had chosen",v)
        play()
game()
    
    


    
