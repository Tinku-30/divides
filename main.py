def divide(nums):
    result = []
    for i in range(nums):
        if i%3 == 0 and i%5 == 0:
            result.append(i)

    return result




nums = int(input("enter any number: "))
result = divide(nums)
print(result)