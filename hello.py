import sys

#English language
def hello():
print("Hello")

#French language
def french():
pring("Bonjour!")

#Slovak language
def slovak():
pring("Ahoj")

#Main function with if
def main():
if sys.argv[1] == "fr":
    french()
else if sys.argv[1] == "sk":
    slovak()
else:
    hello()
