import math

def area_paramter_diagonal(hight , width):
    area = hight * width
    parameter = 2 * (width + hight)
    diagonal = (width**2 + hight*2)

    return{
        "area": area,
        "parameter" : parameter,
        "diagonal":diagonal
    }

result = area_paramter_diagonal(12.5,58.2)

print(result)