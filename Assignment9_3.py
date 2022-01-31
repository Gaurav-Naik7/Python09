import os
from sys import *

def main():

    fd=open(argv[1],"x")

    print(argv[1]," file was created")

    if os.path.exists(argv[2]):

        fd1=open(argv[2],"r")

        data=fd1.read()

        data1=fd.write(data)

        print("Data is sucessfully copied in new file")

    else:
        print("There is no such file")


if __name__=="__main__":
    main()
