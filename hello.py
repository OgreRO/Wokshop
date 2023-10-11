
#English language
def hello():
print("Hello, world!")

#Slovak language
def slovak():
pring("Ahoj")

#Main function
def main():
if sys.argv[1] == "sk":
slovak()
else:
hello()