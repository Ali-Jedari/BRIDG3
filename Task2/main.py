from fileClass import *
def main():
    #filename = input("Enter the filename: ")

    try:
        fileIn = open("content.txt", mode="r")

    except OSError:
        print(f"Error: opening the file '{fileIn}' failed!")

        return

    try:
        fileOut = open("result.txt", mode="w")

    except OSError:
        print(f"Error: opening the file '{fileOut}' failed!")

        return


    file = File(fileIn, fileOut)
    file.process_file()

    fileIn.close()
    fileOut.close()


if __name__ == "__main__":
    main()