print("Это программадля подсчета площади прямоугольника")

def quadrat(a):
   return a*a


def not_quadrat(a,b):
    if a > 0 and b > 0:
        return a*b
    else:
        return "Площадь получилась отрицательная!"


print(quadrat(17))

print(not_quadrat(23,7))

