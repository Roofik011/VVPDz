import math

def calculate_hypotenuse(a, b):
    # Вычисляем гипотенузу по теореме Пифагораprint("")
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

if __name__ == "__main__":
    import sys
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    
    # Вычисляем гипотенузу
    hypotenuse = calculate_hypotenuse(a, b)
    
    # Печатаем результат
    print(f"Гипотенуза: {hypotenuse}")