print("Login Page")
while(1):
    print("Do you have an account already? (y/n)")
    res=input()
    if(res=='y' or res=='Y'):
        email=input("Please enter your email: ")
        password=input("Please enter your password: ")
        if (email=="msaha2245@gmail.com" and password=="test"):
            print("Logged in Successfully")
            break
        else:
            print("Enter correct user details")
    else:
        name=input("Please enter your name:  ")
        email=input("Please enter your email: ")
        password=input("Please enter your password: ")
        print("Account created Successfully")
        break