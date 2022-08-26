from gpiozero import Button, LED
from time import sleep
import random

led = LED(17)

#introduces the game and gets player names.
print("Get ready to play a reaction game. Once both players have entered their name, the game will start.\nThe first player to hit their button when the light turns on wins!")

user_1 = input("\nWho is player one? ")
user_2 = input("\nWho is player two? ")

#defines the funtion that runs the game

def gameOn():
    print("\nGame on!")
    button_1 = Button(2)
    button_2 = Button(3)


    time = random.uniform(5, 10)
    sleep(time)
    led.on()
    
    while True: 
        '''if button_1.is_pressed and is_lit != True:
            print("Foul called on " + user_1)
            break
        if button_2.is_pressed and is_lit != True:
            print("Foul called on " + user_2)
            break'''
        if button_1.is_pressed:
            print("\n" + user_1 +" wins!")
            break
        if button_2.is_pressed:
            print("\n" + user_2  +" wins!")
            break
       

    
#starts the game        
game_choice = input("\nAre you ready?? y/n ")
if game_choice == "y":
    gameOn()
    
#How can I wrap this in a function that repeats?
#How can I keep playing games and record scores across multiple games? 
led.off()
