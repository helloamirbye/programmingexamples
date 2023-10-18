username="guest"
stDomain=tuple((".com",".org",".net",".gov",".co",".ir"))

def program():
    
    email=input("please enter youre email: ")
    emailSplit = email.split("@")
    
    if email.count("@")==1 and emailSplit[0] != "" and emailSplit[1] !="" and emailSplit[1].endswith(stDomain) :
        index=email.find("@")
        global username
        username=email[:index]
        passwordCheck()
    else:
        print("Your email is incorrect")
        program()
    

def passwordCheck():
    validkeys=["1212AmiR","pArHam13","098ALi23"]
    lowerChar=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upperChar=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    password=input("please enter your password:")
    if len(password) == 8:
        if password[0].isdigit() == True or password[1].isdigit() == True or password[2].isdigit() == True or password[3].isdigit() == True or password[4].isdigit() == True or password[5].isdigit() == True or password[6].isdigit() == True or password[7].isdigit() == True:
            if password[0] in lowerChar or password[1] in lowerChar or password[2] in lowerChar or password[3] in lowerChar or password[4] in lowerChar or password[5] in lowerChar or password[6] in lowerChar or password[7] in lowerChar:
                if password[0] in upperChar or password[1] in upperChar or password[2] in upperChar or password[3] in upperChar or password[4] in upperChar or password[5] in upperChar or password[6] in upperChar or password[7] in upperChar:
                    if password in validkeys:
                        print("Welcome Dear {}".format(username))
                        print("List of Password in DataBase: {}".format(validkeys))
                        chUser=input("are you want add new password to DB?(y/n)").lower()
                        if chUser == "y":
                            newpassword=input("enter new password:")
                            validkeys.append(newpassword)
                            print("Dear {}\nYour new password has been added :)".format(username))
                            print("List of Password in DataBase: {}".format(validkeys))
                        else:
                            print("You are out ):")
                    else:
                        print("The password is wrong")
                        passwordCheck()
                else:
                    print("There are no capital letters in your password")
                    passwordCheck()
            else:
                print("There are no lowercase letters in your password")
                passwordCheck()
        else:
            print("There is no number in your password")
            passwordCheck()
    else:
        print("Your password must be eight characters")
        passwordCheck()




program()