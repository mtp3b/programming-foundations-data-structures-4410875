#DOES NOT WORK, refer to 04_06e for answer
def has_unique_characters(data):
    data_set = set(data)
    data_list = list(data)
    x = 0
    for letter in data_list:
        if letter in data_set:
            x = x + 1


    return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
