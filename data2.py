def piramida(tinggi):
    for i in range(1, tinggi + 1):
        spasi = ' ' * (tinggi - i)
        bintang = '*' * (2 * i - 1)
        print(spasi + bintang)


piramida(5)
