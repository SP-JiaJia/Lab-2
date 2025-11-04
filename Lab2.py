print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    #print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    return [float(i) for i in input().split(",")]

def calc_average_temp(temp_list):
    #print("calc_average")
    return sum(temp_list)/len(temp_list)

def sort_temp(temp_list):
    return sorted(temp_list)

def cal_min_max_temp(temp_list):
    return [min(temp_list), max(temp_list)]

def cal_median_temp(temp_list):
    #print(temp_list)
    if(len(temp_list)%2): #if list is odd in length
        return temp_list[int(len(temp_list)/2)]
    else:
        index=int(len(temp_list)/2) 
        return (temp_list[index]+temp_list[index-1])/2 #need to minus 1 as list index starts from 0

List = get_user_input()
print(calc_average_temp(List))
sorted_list=sort_temp(List)
print(cal_min_max_temp(sorted_list))
print(cal_median_temp(sorted_list))

def main():
    print("Here is the main program")

if __name__ == "main":
    main()