#OPTION1
def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    return sorted_list[1]

#OPTION2 - lesser time complexity
def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    smallest = float('inf') #start with the highest possible value
    second_smallest = float('inf') #start with the highest possible value
    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest

print(find_second_smallest_v2([5, 8, 3, 2, 6]))
