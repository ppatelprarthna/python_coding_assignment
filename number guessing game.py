import random

def main():
    print("Welcome to the number guesing game")
    
    #generate a random number between 1- 50
    
    number= random.randint(1,50)
    
    attempts = 0
    max_attempts= 5
    
    while attempts < max_attempts: 
        
        #get user input for the guess
        try: 
           userNum = int(input("Please guess a number between 1-50 ")) 
           response = number_guessing_game(userNum, number)
           print(response)
           if response == "You got  it correct! Congratulations":
                break
           attempts += 1

        except ValueError:
           print("Invalid  input! Please enter a valid number. ")

    else:
       print(f"You have reached the max attempt. The correct answer is {number}")    
 

def number_guessing_game(userNum,number):
            #check if the guess is correct       
            if userNum == number:
                message ="You got it correct! congratuliations "
                
            elif userNum > number:
                message = "Too High, try again"
            
            else:    
                 message= "Too low, try again"
           
            return(message)  

if __name__ == "__main__":
    main()

