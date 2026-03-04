lista1= ['luci','anxo','luis','diego']; lista2=[30,2,7,0.1]
def lista_materiales_tamaños(nombres,tamaños):
    print('-'*30)
    print(f"{'MATERIALES':<15} | {'TAMAÑO':<15}") #guardamos15 huecos para los no,bres y 10 para los tamaños y los dividimos con una ralla
    print('-'*30)
    for i in range(len(nombres)):
        print(f"{nombres[i]:<15} | {tamaños[i]:<10}")
lista_materiales_tamaños(lista1,lista2)