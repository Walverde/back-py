file = open ('abcd.txt') #Apenas Ler o Arquivo
#file = open ('abcd.txt', 'w+') #Cria um arquivo com o Nome e/ousobrescreve o que que ja tem

#file.write('Linha 56465 1\n')
#file.write('Linha 56165165  2\n')
#file.write('Linha 561651651651 3\n')

file.seek(35,0) #move o curso para aposiçao inicial para poder ler o arquivo
print('Lendo linhas:')
print(file.read())
print('#############')
#file.seek(0,0)
#print(file.readline(), end='')
#print(file.readline(),end='')
#print(file.readline(),end='')
#print('#############')
#print(file.readlines())
#print('#############')
#file.seek(0,0)
#for Linha in file.readlines():
#    print(Linha)
file.close()