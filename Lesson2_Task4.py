string = input("Введите строку из нескольких слов, разделённых пробелами: ")
list_s = string.split()
for n, s in enumerate(list_s, 1):
    print(n, s[:10])