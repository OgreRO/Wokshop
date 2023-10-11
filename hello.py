import sys

#English language
def hello():
print("Hello, world!")

#French language
def french():
pring("Bonjour!")

#Main function with if
def main():
if sys.argv[1] == "fr":
french()
else:
hello()