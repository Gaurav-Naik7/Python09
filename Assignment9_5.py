import os

def main():
    name=input("Enter file name  ")
    word=input("Enter one string ")

    if os.path.exists(name):

        fd=open(name,"r")

        data=fd.read()

        occurence=data.count(word)

        print("Number of time the string occurs is: ",occurence)

    else:
        print("There is no such file")

if __name__=="__main__":
    main()
