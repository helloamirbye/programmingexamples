#Date:      1402.5.5
#Program:   Check User Input
#Teacher:   Soroush Joudaki
#Academy:   Montazemi
#Programer: Amir Bagherzade


"""
1. gereftane name karbar
2. gereftane charactere controli va barresi
3. baressi inke tedadesh 8tast ya na
4. baressi inke adad tosh hast ya na
5. baressi inke horofe kochick tosh hast ya na
6. baressi inke horofe bozorg tosh hast ya na
7. baressi key vorodi karbar ba liste validkeys be onvane Data Base
8. soal az karbar baraye tamayol be ezafe kardane valid key jadid
9. soal az karbar baraye edame barname ya tamam shodanesh

"""


#--------------------------------------Libraries----------------------------------# 

import os


#--------------------------------------DataBase----------------------------------# 

validKeys=["S45E29tb","5kdI4i3V","77vV33Ee"] #Data Base List
charCheck="#" #Charactere Controli Khaste shode da inja "#" mibashad

#--------------------------------------Functions----------------------------------# 
def UserName():
    os.system('cls')
    global userName
    userName = input("Enter your name:") # gereftane name karbar
    if userName == "":
        userName = "Guest"
    os.system('cls')


def ContorlChar():
    charUser = input("Enter your control character:") #gereftane charactere controli va barresi
    if charCheck == charUser:
        pass
        os.system('cls')
    else:
        os.system('cls')
        print("The control character entered is incorrect!")
        ContorlChar()


#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#


def GetInput(): #barresi vorodie karbar
    keyUser = input("Enter your login key:")
    
    keyUser = CountChar(keyUser)
    keyUser = HaveNum(keyUser,0)
    keyUser = HaveLower(keyUser,0)
    keyUser = HaveUpper(keyUser,0)

    os.system('cls')
    return keyUser


def CountChar(stCount): #baressi inke tedadesh 8tast ya na
    if len(stCount) == 8:
        return stCount
    else:
        os.system('cls')
        print("The input length is not correct! It should be 8 characters")
        return GetInput()
  

def HaveNum(stNum,n): #baressi inke adad tosh hast ya na
    if n == (len(stNum)-1) and stNum[n].isnumeric() == False:
        os.system('cls')
        print("Your entry does not have a number!")
        stNum = GetInput()
        return stNum
    elif stNum[n].isnumeric():
        return stNum
    else:
        stNum = HaveNum(stNum,n+1)
        return stNum

def HaveLower(stLow,n): #baressi inke horofe kochick tosh hast ya na
    if n == (len(stLow)-1) and stLow[n].islower() == False: 
        os.system('cls')
        print("Your entry does not contain a lowercase character!")
        stLow = GetInput()
        return stLow
    elif stLow[n].islower():
        return stLow
    else:
        stLow = HaveLower(stLow,n+1)
        return stLow

def HaveUpper(stUp,n): #baressi inke horofe bozorg tosh hast ya na
    if n == (len(stUp)-1) and stUp[n].isupper() == False:
        os.system('cls')
        print("Your entry does not contain an uppercase character!")
        stUp = GetInput()
        return stUp
    elif stUp[n].isupper():
        return stUp
    else:
        stUp = HaveUpper(stUp,n+1)
        return stUp
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#

def CheckKeyUserWithDB(st): #barresi key vorodie karbar ba DataBase
    if st in validKeys:
        os.system('cls')
        return st
    
    else:
        os.system('cls')
        print("Your input key does not match the database keys!")
        st = GetInput()
        return st


#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#


def MainProgram(): #daryafte va barresi vorodi karbar va ehyanan vorode key jadid be data base
    UserName()
    ContorlChar()

    CheckInput = GetInput()
    CheckInput = CheckKeyUserWithDB(CheckInput)#################################    ERROR LOGIC     !!!!!!!!!!!!!!!!!!!!!!
    
    print(f"Welcome Dear {userName}")
    print("--------------------------\n")
    ch = input("Do you want to enter a new key? (y/n)").lower()
    if ch == 'y':
        NewKeyUser = GetInput()
        validKeys.append(NewKeyUser)
        os.system('cls')
        print("Dear {},\nYour new key has been successfully added to the database.\n".format(userName))
        print(validKeys)


def MyProgram(): #baraye barresi inke karbar mikhad barname edame peida kone ya na
    MainProgram()
    choose = input("Do you want to log out? (y/n)").lower()
    if choose == 'n':
        MyProgram()
    else:
        os.system('cls')
        print("Logout...")
        print("Good Luck.")

#------------------------------------End_Functions--------------------------------# 

#------------------------------------MAIN_PROGRAM--------------------------------# 

MyProgram()

