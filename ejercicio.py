import json


repetidos = [1,2,3,"1","2","3",3,4,5] 
# 1. Genere una lista con los valores no repetidos de la lista ‘repetidos’. 
sin_repetir = []

for elemento in repetidos:
    if elemento not in sin_repetir:
        sin_repetir.append(elemento)
print(sin_repetir)



# 2. Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’ 
r = [1,"5",2,"3"] 

listComun = []

for elemento in repetidos:
    if elemento in r:
        listComun.append(elemento)

print(listComun) 


# 3. Transforme ‘d_str’ en un diccionario. 
d_str = '{"valor":125.3,"codigo":123}'
print(f'antes{d_str}')
dicc = json.loads(d_str)
print(f'Despues{dicc}')