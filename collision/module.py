def isCorrectRect(rectangle): #функция проверяет, может ли быть такой прямоугольник
    if(rectangle[0][0] < rectangle[1][0] and rectangle[0][1] < rectangle[1][1]):
        return True
    else:
        return False
