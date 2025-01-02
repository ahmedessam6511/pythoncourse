def read_second_last_line(file_name): 
    
    # ls = []
    # f.seek(0,0)
    # # lines_count = len(f.readlines())
    # # f.seek(0,0)
    # for line in f.readlines():
    #     line = line.strip()
    #     if line == "":
    #         pass
    #     else:
    #         ls.append(line)
    # return ls[-2]
    
    # f = open(file_name, "r")
    # ls =  f.readlines()

    # for i in range(len(ls)):
    #     ls[i] = ls[i].strip()
        
    # if len(ls) == 0:
    #     return ""
    # elif len(ls) == 1:
    #     return ls[-1]
    # else:
    #     return ls[-2]

    with open(file_name, 'r') as file:
        lines = file.readlines()

        lines = "['Hello everyone!!\n', 'Welcome to the Robogarden Course.\n', 'Hope you understand your lessons well.\n']"
        ls = lines[1:-1]
        print(ls)
        # if len(lines) < 2:
        #     return None  # or raise an error if you prefer
        # return lines[-2].strip()
    

# ['Hello everyone!!\n', 'Welcome to the Robogarden Course.\n', 'Hope you understand your lessons well.\n']

def main(): 

    data = read_second_last_line('test.txt') 

    print(data) 

    return data

  

main() 