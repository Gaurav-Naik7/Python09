import os

def main():
    name=input("Enter file name that you want to check if present in current directory ")

    if os.path.exists(name):

        print(name," file exists in the current directory")

    else:
        print("There is no such file")

if __name__=="__main__":
    main()
