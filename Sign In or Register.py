import json

#This will read a json file which have dictionary in it of username and passwords

username_Password = dict(json.load(open('Username.json')))
# print (registerOrLogin)


#This is Very Confusing Loop :(
OK = 0
while (OK < 1):
    #It will take input from user wether They want to register or sign in
    registerOrLogin=input('Sign In Or Register : ')
    registerOrLogin = registerOrLogin.lower()
    
    #Condition if user input register and take input of newusername
    if registerOrLogin == "register":
        newUsername = input("Enter UserName (small letters) : ")
        #Condition if user name already exist print already exist and restart loop
        if newUsername in username_Password:
            print ("Username : ", newUsername , "Already exist")
            time.sleep(2)
            clear_output()
            continue
        #Else will take input from user of newPassword
        else:
            newPassword = input('Enter Passeword : ')
            #it will Append new username and password to dictionary
            username_Password[newUsername] = newPassword
            #it will save dictionary back to json file and prints Registration SucessFull
            j = json.dumps(username_Password)
            with open('Username.json', 'w') as f:
                f.write(j)
                f.close()
            print ('Registration Successfull')
#Loop will run again
    #if user enter Sign In it will take input of username which already exist
    elif registerOrLogin == "sign in":
        username = input('Enter Your UserName : ')
        #if User name exist it will take input for password
        if username in username_Password:
            password = input('Enter Your Password : ')
            #if password is correct it will print login Succes ful
            if password == username_Password[username]:
                print('Login Succesful')
                break
            #If password is wrong it will print invalid password
            else:
                print ('Invalid Password')
                time.sleep(2)
                clear_output()
                continue
        #If username is wrong it will print invalid username
        else:
            print('Invalid Username')
            time.sleep(2)
            clear_output()
            continue
