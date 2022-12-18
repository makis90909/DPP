def even_number(i = 0):
    while True:
        i += 2
        yield i

if (__name__ == "__main__"):
    x = even_number()
    for i in range(10):
        print(next(x))