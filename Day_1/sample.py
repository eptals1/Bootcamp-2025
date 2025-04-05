import time 

def login(accounts):
    """Login with dict of accounts"""
    name = input("Name: ")
    pwd = input("Password: ")
    
    retry = 3
    while retry > 0:
        if name in accounts and accounts[name] == pwd:
            print("Login successful!")
            break
        else:
            print("Login failed! Invalid credentials.")
            retry -= 1
            if retry == 0:
                print("Too many login failures. Please try again later.")
                time.sleep(10)
    else:
        print("Login failed! Invalid credentials.")
    


login({"admin": "123"})