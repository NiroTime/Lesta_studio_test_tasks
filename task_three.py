# Мне кажется невозможно выбрать идеальную сортировку имея те даннные,
# что представленны в тз, в тех задачах с которыми я сталкивался до сих пор,
# принципиальной разницы между встроенной сортировкой, быстрой, или слиянием
# не было принципиальной разницы в скорости, но в качестве кода я всё же выберу
# cортировку слиянием, потому что в тз, не сказанно ничего про доп память.


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if (left_list_index < left_list_length
                and right_list_index < right_list_length):
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

