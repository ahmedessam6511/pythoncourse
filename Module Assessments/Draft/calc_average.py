def calc_avg(ls):
    return  sum(ls)/len(ls)

if __name__ == "__main__":
    ls = [1,2,3,4,5]
    if len(ls) != 0:
        try:
            print("Average = " , calc_avg(ls)) 
        except:
            print("Error!!!")
        
    else:
        print("List is empty!!")