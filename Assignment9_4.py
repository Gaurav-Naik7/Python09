import os
import hashlib

def main():

    name1=input("Enter first file name ")
    name2=input("Enter second file name ")


    if os.path.exists(name1):
        if os.path.exists(name2):

            hx1 = hashlib.md5()
            hx2 = hashlib.md5()

            hx1.update(open(name1, "rb").read())
            hx2.update(open(name2, "rb").read())

            if hx1.hexdigest()==hx2.hexdigest():
                print("Success")

            else:
                print("Failure")

        else:
            print("Second file does not exist")

    else:
        print("First file does not exist")

if __name__=="__main__":
    main()
