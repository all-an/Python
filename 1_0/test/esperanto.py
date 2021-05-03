s = input("Type your text: ")

a1 = ("ũ",'\u016d')
a2 = ("Ũ",'\u016C') 

for r in (a1,a2):
    s = s.replace(*r)

arquivo = open("texto.txt","w")
arquivo.write(s)
arquivo.close()
print(''.join(s))
