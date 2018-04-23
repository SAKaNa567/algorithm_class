def merge_sort(List):
    if len(List) <= 1:
        return List

    mid = len(List) /2
    left = List[:mid]
    right = List[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    if left:
        sorted_list.extend(left[left_index:])
    if right:
        sorted_list.extend(right[right_index:])

    return sorted_list

if __name__ == '__main__':
    l = [6,3,1]
    l = merge_sort(l)
    print l
