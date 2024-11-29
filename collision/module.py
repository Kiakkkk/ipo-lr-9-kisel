class RectCorrectError(Exception): #исключение(ошибка) при неправильном вводе координат
    def __init__(self, num):
        super().__init__(f"{num}й прямоугольник некоректный")

def isCorrectRect(rectangle): #функция проверяет, может ли быть такой прямоугольник
    if(rectangle[0][0] < rectangle[1][0] and rectangle[0][1] < rectangle[1][1]):
        return True
    else:
        return False
    
def isCollisionRect(fir_rect, sec_rect):#функция проверяет наличие пересечений двух прямоугольников
    if isCorrectRect(fir_rect) and isCorrectRect(sec_rect): #если ввод корректный
        if min(sec_rect[0][0], sec_rect[1][0]) < max(fir_rect[0][0], fir_rect[1][0]) and min(fir_rect[0][1], fir_rect[1][1]) < max(fir_rect[0][1], fir_rect[1][1]):
            return True #если пересекаются
        else:
            return False #если не пересекаются
    elif(not isCorrectRect(fir_rect)): #если 1 прямоугольник некорректный
        raise RectCorrectError(1)
    elif (not isCorrectRect(sec_rect)): #если 2 прямоугольник некорректный
        raise RectCorrectError(2)
