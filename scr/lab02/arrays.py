def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("the array cannot be empty")
    min_val = nums[0]
    max_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return (min_val, max_val)


print("min_max: ")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
try:
    print(min_max([]))
except Exception as e:
    print(f"ValueErorre: {e}\n")


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums


print("unique_sorted: ")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]), "\n")


def flatten(mat: list[list | tuple]) -> list:
    result = []
    for item in mat:
        if not isinstance(item, (list, tuple)):
            raise TypeError("ab is not list or tuple")
        for element in item:
            if isinstance(element, (list, tuple)):
                result.extend(flatten([element]))
            else:
                result.append(element)
    return result


print("flatten: ")
print(flatten([[1, 2], [3, 4]]))
print(flatten([([1, 2], (3, 4, 5))]))
print(flatten([[1], [], [2, 3]]))
try:
    print(flatten([[1, 2], "ab"]))
except Exception as e:
    print(f"TybeErorre: {e}")
