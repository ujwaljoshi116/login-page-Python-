import os
def practical():
    print("welcome to login form")
    print("3 to exit")
    c=int(input("1--new user\n2--login\n3--exit\n"))
    print("----------"*10)

    if c==1:
        name  = input("Enter Your name: ")
        username = input("Enter Your username : ")
        password = input("Enter Your password : ")

        PersonalFile = "username"+username+password+".txt"
        with open(PersonalFile, 'w')as pf:
            pf.write(name)
            print(PersonalFile+ " CREATED")
        
    elif c==2:
        login = input("Enter Your login : ")
        pwd = input("Enter Your password : ")
        PersonalFile = "login"+login+pwd+".txt"
        if os.path.exists(PersonalFile):
            print("login Successfull")
            print("Thank you for using this login form")
        else :
            print("Login Unsucessful\nPlease try again!!!!!!!")
            print("----------"*10)

            practical()
    elif c==3:
        exit(0)

    else:
        print("-"*10)
        print("You have selected an invalid term,SELECT AGAIN!!")
        print("-"*10)
        practical()

        
practical()
          

    
