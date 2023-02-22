def sum(numbers):
    totalSum = 0

    for i in range(0,len(numbers)):
        totalSum += numbers[i]
    return totalSum

def product(numbers):
    totalProduct = 1
    
    for i in range(0,len(numbers)):
        totalProduct *= numbers[i]
    return totalProduct
