def terjemahkan(kata):
    terjemahan = ""
    for huruf in kata:
        if huruf.lower() in "aeiou":
            if huruf.isupper():
                terjemahan = terjemahan + "G"
            else:
                terjemahan = terjemahan + "g"
        else:
            terjemahan = terjemahan + huruf
    return terjemahan

print(terjemahkan(input("Masukkan sebuah kata: ")))

