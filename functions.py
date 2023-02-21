def areaOfRectangle(base = 0, height = 0): 
    if(height == 0):
        height = base #if no height, assume a square
    if(base == 0):
        base = height
    return base * height

print(areaOfRectangle(3, 2)) #expect 6
print(areaOfRectangle(3)) #expect 9


print(areaOfRectangle(height=5)) #expect25
print(areaOfRectangle(height=5, base=2)) #expect10


def calculateTotal(taxRate, subtotal, shipping): 
    taxTotal = taxRate * subtotal
    return taxTotal + shipping + subtotal

print(calculateTotal(0.07, shipping=4.99, subtotal=24.99))