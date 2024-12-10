import random
def get_comp_choice():
    return random.choice(['rock','paper','scissors'])
def compute_winner(user_choice,comp_choice):
    if user_choice==comp_choice:
        print("Tie....")
    elif(user_choice=='rock' and comp_choice=='scissors') or (user_choice=='paper' and comp_choice=='rock')or (user_choice=='scissors' and comp_choice=='paper') :
        return "win" 
    else:
        return "lose"
def result_dislay(user_choice,computer_choice,result):
    print("You choose:",user_choice)   
    print("Computer choose:",computer_choice)
    if result=="win":
        print("You win!!")
    elif result=="lose":
        print("you lose!!")  
    else:
        print("It's a tie!!!!") 
def main():
    user_score,computer_score=0,0  
    while True:
        user_choice=input("Enter your choice (rock,paper,scisors),& type 'quit' for backing the game: ").lower()   
        if user_choice=="quit":
            print("Thank you for playing...")  
            print("Final score:\n You:",user_score,"computer:",computer_score)  
            break
        if user_choice not in ['rock','paper','scissors']:
            print("Invalid choice!!!!!!!")  
            continue
        comp_choice=get_comp_choice()
        result=compute_winner(user_choice,comp_choice)
        if result=="win":
            user_score+=1
        elif result=="lose":
            computer_score+=1
        result_dislay(user_choice,comp_choice,result)   
        print("Current score:\nYou:", user_score,"Computer:",computer_score) 
if __name__=="__main__":
    print("Welcome to Rock-Paper-Scisssors game....")
    main()      
