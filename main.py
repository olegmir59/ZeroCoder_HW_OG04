print("Это программадля подсчета площади прямоугольника")

def quadrat(a,b):
    if a > 0 and b > 0:
        return a*b
    else:
        return "Площадь получилась отрицательная!"


print(quadrat(23,-7))

print(quadrat(23,7))
