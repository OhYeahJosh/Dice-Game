import random 
import os 
  
os.system('clear') 
def rolling(): 
    #variable declare to be used  
    countWin = 0 
    countLoss = 0 
    #outer while loop for taking user entry 
    while True: 
        input("Press <Enter> to role the dice.<Ctrl-c> to quit.") 
        #inner while loop for other number you keep rolling until you win or lose. 
        while True: 
             
            d1 = random.randint(1, 6) 
            d2 = random.randint(1, 6) 
             
            if d1 == 1: 
                print(""" 
                ╔═══════╗ 
                ║ ║ 
                ║ * ║ 
                ║ ║ 
                ╚═══════╝""") 
                 
             
            if d1 == 2: 
                print(""" 
                ╔═══════╗ 
                ║ * ║ 
                ║ ║ 
                ║ * ║ 
                ╚═══════╝""") 
             
             
            if d1 == 3: 
                print(""" 
                ╔═══════╗ 
                ║ * ║ 
                ║ * ║ 
                ║ * ║ 
                ╚═══════╝""") 
             
             
            if d1 == 4: 
                print(""" 
                ╔═══════╗ 
                ║ * * ║ 
                ║ ║ 
                ║ * * ║ 
                ╚═══════╝""") 
             
             
            if d1 == 5: 
                print(""" 
                ╔═══════╗ 
                ║ * * ║ 
                ║ * ║ 
                ║ * * ║ 
                ╚═══════╝""") 
             
             
            if d1 == 6: 
                print(""" 
                ╔═══════╗ 
                ║ * * ║ 
                ║ * * ║ 
                ║ * * ║ 
                ╚═══════╝""") 
             
            if d2 == 1: 
                print(''' 
                ╔═══════╗ 
                ║ ║ 
                ║ * ║ 
                ║ ║ 
                ╚═══════╝''') 
             
             
            if d2 == 2: 
                print(""" 
                ╔═══════╗ 
                ║ * ║ 
                ║ ║ 
                ║ * ║ 
                ╚═══════╝""") 
             
             
            if d2 == 3: 
                print(""" 
                ╔═══════╗ 
                ║ * ║ 
                ║ * ║ 
                ║ * ║ 
                ╚═══════╝""") 
             
             
            if d2 == 4: 
                print(""" 
                ╔═══════╗ 
                ║ * * ║ 
                ║ ║ 
                ║ * * ║ 
                ╚═══════╝""") 
             
             
            if d2 == 5: 
                print(""" 
                ╔═══════╗ 
                ║ * * ║ 
                ║ * ║ 
                ║ * * ║ 
                ╚═══════╝""") 
             
             
            if d2 == 6: 
                print(""" 
                ╔═══════╗ 
                ║ * * ║ 
                ║ * * ║ 
                ║ * * ║ 
                ╚═══════╝""") 
             
            #print total wins 
            print('Total Win '+str(countWin)) 
            #print total loss 
            print('Total Loss '+str(countLoss)) 
            #if sum is 7 or 11 then print win and break the loop  
            if d1 + d2 == 7 or d1 + d2 == 11: 
                print("YOU WIN!") 
                #increment win count  
                countWin = countWin + 1 
                #break loop 
                break 
            #if sum is 2  3 or 12 then print loss and break the loop 
            elif d1 + d2 == 2 or d1 + d2 == 3 or d1 + d2 == 12: 
                print("YOU LOSE!") 
                #increment loss count  
                countLoss = countLoss + 1 
                break 
            #if any other number you keep rolling until you win or lose. continue inner while loop  
            else: 
                continue 
             
         
  
rolling() 
 
