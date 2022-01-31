import os

def main():
    name=input("Enter file name  ")

    if os.path.exists(name):

        #print(name," file exists in the current directory")

        fd=open(name,"r")

        data=fd.read()

        print("Data in File is: ",data)

    else:
        print("There is no such file")

if __name__=="__main__":
    main()
