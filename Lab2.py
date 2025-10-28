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
    return [int(temp_list[0]), int(temp_list[-1])]

List = get_user_input()
print(calc_average_temp(List))
sorted_list=sort_temp(List)
print(cal_min_max_temp(sorted_list))