'''
1 - Perform a Task
2 - Return a value
'''
def greet(name):
    print(f"Hi {name}")
    
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("New name")

# Creates and writes to a document called "content.txt"
file = open("NameFile.txt", "w")
file.write(message)
