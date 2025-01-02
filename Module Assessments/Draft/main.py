from math import pi, pow
def main():  

    radius = 4.0  

  

    ## type your code below 
    def calc_circle_area(r):
        
        area= pi*(pow(r,2))

    ############ 

        return area 

  

    # Example usage  

    result = calc_circle_area(radius)  

    print("The answer is:", result)  

    return result  

  

main() 