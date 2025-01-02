# import os
# os.rename("first.txt","third.txt")  ## rename an existing file 

# os.remove("hello.txt") # remove an existing file

# os.mkdir(dirname): creates a new directory inside the current directory with the name, dirname.
# os.chdir(path_new_dir): changes the current directory to another directory with the path, path_new_dir.
# os.rmdir(dirpath): removes the directory with the path, dirpath. The content of the directory must first be removed before removing the directory itself.
# os.getcwd(): returns the current working directory.
def conv_degree_to_percentage(degree,total_degree): 

    assert (degree>=0 and total_degree>=0), "Your course degree or total degree is below zero" 

    return (degree/total_degree)*100 



if __name__ == "__main__":
    print("h")


    # os.rename("text.txt", "r")

    # file = open("textt.txt", "r")
    # data = file.read()
    # print(data)
    # print(len(data))
    # 

    # file.write("AGAIN\nAGAIn")

    # current_pose=file.tell() 

    # print(current_pose)

    # # file.seek(0,0)

    # print(current_pose)
    # # file.write("Second\nSEcond")

    # print(len(file.readlines()))
    # print(file.readlines())
    # ls = file.readlines()
    # print(ls)
    # print("___")
    # for line in file.readlines():
    #     print("___")
    #     print(line)

    # print("___")
    # print(file.read(10))

    
    # file.close()
    # print(file.name)
    # print(file.mode)
    # print(file.closed)