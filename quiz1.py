import random
import os

login_status = False
login_user = ""

def registration():
    """Register a new user."""
    name = input("Enter name: ")
    username = input("Enter username: ")
    pwd = input("Enter password: ")
    score = 0

    # Append user info to registration file
    with open("registration.txt", "a") as file:
        file.write(f"{username},{score}\n")

    # Append login details to login file
    with open("login_details.txt", "a") as file:
        file.write(f"{username},{pwd}\n")

    print("Registration successful!")


def login_users():
    """Login a user."""
    global login_status, login_user
    en = input("Enter your username: ")
    users = []
    uspw = {}

    # Load login details
    if not os.path.exists("login_details.txt"):
        print("No users registered yet.")
        return None

    with open("login_details.txt", "r") as file:
        log = file.readlines()
        for i in log:
            u, p = i.strip().split(",")
            users.append(u)
            uspw[u] = p

    if en in users:
        while not login_status:
            pw = input("Enter PASSWORD: ")
            if pw == uspw[en]:
                print(f"Welcome {en}!")
                login_status = True
                login_user = en
                return en
            else:
                print("Wrong password. Try again.")
    else:
        print("USER NOT REGISTERED")
        choice = input("Do you want to register? (y/n): ").lower()
        if choice == "y":
            registration()
        else:
            exit()


def attempt_quiz(username):
    """Allow the user to attempt the quiz."""
    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "What is 5 + 3?", "options": ["5", "8", "10", "15"], "answer": "8"},
        {"question": "Which is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"], "answer": "Blue Whale"}
    ]

    # Select a random question
    

    # Check if the answer is correct
    game_over=False
    score=0
    while(game_over!=True):
            rand = random.choice(questions)
            print("\nQuestion:", rand["question"])
            print("Options:", ", ".join(rand["options"]))
            ans = input("Enter your answer: ").title()
            if ans == rand["answer"]:
                print("Correct!")
                score+=1
                update_score(username, score)

            else:
                print("ooppss! Wrong Answer")
                game_over=True
                print(f"Your total score is: {score}")

   
   


def update_score(username, points):
    """Update the user's score."""
    if not os.path.exists("registration.txt"):
        print("User data not found.")
        return

    with open("registration.txt", "r") as file:
        lines = file.readlines()

    with open("registration.txt", "w") as file:
        for line in lines:
            user, score = line.strip().split(",")
            if user == username:
                score = int(score) + points
            file.write(f"{user},{score}\n")


def show_profile(username):
    """Show the profile of the logged-in user."""
    if not os.path.exists("registration.txt"):
        print("User data not found.")
        return

    with open("registration.txt", "r") as file:
        for line in file:
            user, score = line.strip().split(",")
            if user == username:
                print(f"Profile of {user}:")
                print(f"Score: {score}")
                return


def main():
    print("Welcome to the Quiz App!")
    while True:
        print("\n1. LET'S PLAY")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            act = input("Do you want to login or register? (login/register): ").lower()
            if act == "login":
                username = login_users()
                if username:
                    attempt_quiz(username)
            elif act == "register":
                registration()
                username = login_users()
                if username:
                    attempt_quiz(username)
            else:
                print("Invalid choice!")
        elif choice == "2":
            username = login_users()
            if username:
                while True:
                    print("\n1. Attempt Quiz")
                    print("2. Show Profile")
                    print("3. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        attempt_quiz(username)
                    elif user_choice == "2":
                        show_profile(username)
                    elif user_choice == "3":
                        print("Logging out...")
                        login_status = False
                        break
                    else:
                        print("Invalid choice! Try again.")
        elif choice == "3":
            print("Thank you for using the Quiz App!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
