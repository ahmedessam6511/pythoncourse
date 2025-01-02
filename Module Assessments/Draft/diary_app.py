import datetime

if __name__ == "__main__":
    try:
        file = open("diary.txt", "r+")
        data = file.read()
        print("Your Previous entries: ", data)
        in1 = int(input("Enter 1 for adding timestamp: "))
        if in1 == 1:
            # file.seek(0,0)
            file.write(str(datetime.datetime.now()))
            

        else:
            pass
    except FileNotFoundError:
        print("File not Found!")
    except PermissionError:
        print("Permission denied!")
    except ValueError:
        print("Value entered not a number!")
    except ModuleNotFoundError:
        print("Module not found!")

    else:
        print("Code excuted well")