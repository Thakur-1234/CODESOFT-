def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        print("Not defined!!!!!!!") 
    else:
        return x/y
def main():
    while True:
        print("For backing the caculator press x")
        choice=input("Choose operation(+,-,*,/): ")
        if choice=='x' or choice=='X':
            break
        else:
            x=float(input("Enter first number: "))
            y=float(input("Enter secnd number: "))
            if choice=='+':
                print("Result=",add(x,y))
            elif choice=='-':
                print("Reult=",sub(x,y))    
            elif choice=='*':
                print("Result=",mul(x,y))    
            elif choice=='/':
                print("Rsult=",div(x,y))
            else:
                print("Error!!, Enter valid  operation")    
if __name__=="__main__":
    main()

