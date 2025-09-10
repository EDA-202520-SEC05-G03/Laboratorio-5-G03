def newlist():
    newlist = {
        "first": None,
        "last": None,
        "size" : 0
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node ["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    
def add_last(my_list, element):
    size = my_list["size"]
    my_list["elements"].insert(size, element)
    my_list["size"] += 1    
    
def first_element(my_list):
    return my_list["elements"] [0]    
    
def size(my_list):
    return my_list["size"]  

def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    size = my_list["size"]
    return my_list["elements"] [size - 1]

def delete_element(my_list, pos):
    size = my_list["size"]
    if pos >= 0 and pos < size:
        element = my_list["elements"].pop(pos)
        my_list["size"] -= 1
        return element
    return None

def remove_first(my_list):
    if my_list["size"] > 0:
        element = my_list["elements"].pop(0)
        my_list["size"] -= 1
        return element
    return None

def remove_last(my_list):
    if my_list["size"] > 0:
        size = my_list["size"]
        element = my_list["elements"].pop(size - 1)
        my_list["size"] -= 1
        return element
    return None

def insert_element(my_list, element, pos):
    size = my_list["size"]
    if pos >= 0 and pos <= size:
        my_list["elements"].insert(pos, element)
        my_list["size"] += 1
        return True
    return False

def change_info(my_list, pos, new_element):
    size = my_list["size"]
    if pos >= 0 and pos < size:
        my_list["elements"][pos] = new_element
        return True
    return False

def exchange(my_list, pos1, pos2):
    size = my_list["size"]
    if pos1 >= 0 and pos1 < size and pos2 >= 0 and pos2 < size:
        temp = my_list["elements"][pos1]
        my_list["elements"][pos1] = my_list["elements"][pos2]
        my_list["elements"][pos2] = temp
        return True
    return False

def sub_list(my_list, start_pos, end_pos):
    size = my_list["size"]
    if start_pos >= 0 and start_pos < size and end_pos >= 0 and end_pos < size and start_pos <= end_pos:
        new_lst = newlist()
        for i in range(start_pos, end_pos + 1):
            add_last(new_lst, my_list["elements"][i])
        return new_lst
    return None

def cmp_function(element1, element2):
    if element1 == element2:
        return 0
    elif element1 < element2:
        return -1
    else:
        return 1  

def selection_sort(my_list, cmp_function):
    size = my_list["size"]
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if not cmp_function(my_list["elements"][j], my_list["elements"][min_index]):
                min_index = j
        if min_index != i:
            exchange(my_list, i, min_index)