
try:
    a =int(input())
    b =int(input())
    print(a/b)
except ZeroDivisionError  as e:
    print(f"{e} - низя 1")
except ValueError as q:
    print(f"{q} - низя 2")
except Exception as w: #охватывает все ошибки
    print(f'{w} - Непредвиденная ошибка')
finally:     #выполнится когда код завершит работу успешно
    print('---------------')