s = input("Type your text: ")

a1 = ("ã",'\u0101')
a2 = ("Ã",'\u0100')
a3 = ("ẽ",'\u0113')
a4 = ("Ẽ",'\u0112')
a5 = ("ĩ",'\u012b')
a6 = ("Ĩ",'\u012a')
a7 = ("õ",'\u014d')
a8 = ("Õ",'\u014c')
a9 = ("ũ",'\u016b')
a10 = ("Ũ",'\u016a')
a11 = ("`",'\u02bb')
 

for r in (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11):
    s = s.replace(*r)

arquivo = open("texto.txt","w")
arquivo.write(s)
arquivo.close()
print(''.join(s))
