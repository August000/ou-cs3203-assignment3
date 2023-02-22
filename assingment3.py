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
    
def reverseOrder(numbers):
    return list(reversed(numbers))
    
numbers = []

print("insert five numbers to be used in the operations")

for i in range(0,5):
   letter = int(input())
   numbers.append(letter)
   
print(numbers)
print(sum(numbers))
print(product(numbers))
print(reverseOrder(numbers))
