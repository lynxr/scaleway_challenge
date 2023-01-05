
# Write a script/function to remove duplicate datas from a list
# We do not need to order the targeted list


def de_duplicate(lst):
    """
    function which removes duplicates from collection
    :param lst: collection
    :return: de-duplicated list
    """
    result = []
    for elem in lst:
        if elem not in result:
            result.append(elem)
    return result


def de_duplicate_list_comprehension(lst):
    """
    Same function as `de_duplicate` but uses list comprehension
    :param lst: collection
    :return: de-duplicated list
    """
    result = []
    [result.append(x) for x in lst if x not in result]
    return result
