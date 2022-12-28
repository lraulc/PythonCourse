# BAD PRACTICE - DO NOT ACCESS USING GLOBAL, AVOID AS MUCH AS POSSIBLE
message = "a"

def greet(name):
    global message
    message = 'b'

print(message)