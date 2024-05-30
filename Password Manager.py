pwd = input("What is the master password? ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:", passw)

def add():
    Name = input("Account Name: ")
    Password = input("Account Password: ")

    with open("passwords.txt", "a") as f:
        f.write(f"{Name} | {Password}\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add/q to quit): ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("Invalid selection.")
        continue