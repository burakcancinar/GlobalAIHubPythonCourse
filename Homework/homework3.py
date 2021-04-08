username = "Python"
password = "admin"
loginName = input("Username: ")
loginPassword= input("Password: ")
if loginName == username and loginPassword != password:
    print("Wrong password!")
elif loginName != username and loginPassword == password:
    print("Wrong Username!")
elif loginName != username and loginPassword != password:
    print("Wrong username and password!")
else:
    print("Login successful")