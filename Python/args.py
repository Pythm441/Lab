def sum(*nums):
    result = 0
    for num in nums:
        result += num

    return result

x = sum(2 + 2 + 2)
print(x)