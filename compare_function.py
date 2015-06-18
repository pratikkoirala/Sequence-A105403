from sets import Set
def compare(list1, list2):
    list_1 = Set(list1)
    list_2 = Set(list2)
    if len(list_1 & list_2) >= 2:
        return True
    else:
        return False

