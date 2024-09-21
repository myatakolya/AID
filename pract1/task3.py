def task_3():
    string = input("Введите строку: ").lower()
    leters='аоуэыяёеюи'
    for i in leters:
        counter = string.count(i)
        for k in range(counter,0,-1):
            if str(i*k) in string:
                string=string.replace(i*k,i)
    return string
print(task_3())