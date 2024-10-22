volume = 1.44 * (2 ** 20)
pages = 100
strings = 50
symbols = 25
v_symbols = 4

count = int(volume // (v_symbols * symbols * strings * pages))

print("Количество книг, помещающихся на дискету:", count)
