# a=[1,2,3]
# b=[4,5]
# a.extend(b)
# print(a)


# print(2**3)
# print(2^3)


# a=[0,1,2,31]
# b=a[1::-1]
# print(b)



def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = 0
    for num in nums:
        actual_sum += num
    missing_number = expected_sum - actual_sum
    return missing_number

# Test the function
nums = [3, 7, 1, 2, 8, 4, 5]
print("Missing number:", find_missing_number(nums))