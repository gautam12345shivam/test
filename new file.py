##Answer 1

# import datetime


# Date = input("Enter a date (MM DD YYYY): ")



# date_object = datetime.datetime.strptime(Date, "%m %d %Y")

# Day_name = date_object.strftime("%A").upper()

# print(Day_name)


## Answer 2

# x = int(input("Enter num: ")) 
# if 1 < x < 11:
    
#     for i in range(0, x):  
#          print(i ** 2) 


##Answer 3

def swap_case(s):
    return s.swapcase()
 
if __name__ =='__main__':
    s = input("Enter a string: ")
    result = swap_case(s)
    print(result)


