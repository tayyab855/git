# This is a simple Python program

# Function to greet the user
def greet(name):
    print(f"Hello, {name}! Welcome to Python programming.")

# Loop that asks for user input and calls the greet function
while True:
    user_name = input("Enter your name (or type 'exit' to quit): ")
    
    if user_name.lower() == 'exit':
        print("Goodbye!")
        break
    
    greet(user_name)

