def contar_digitos(numero):
    if numero < 10:
        return 1
    return 1 + contar_digitos(numero // 10)


print(contar_digitos(12345))  
print("********************************************************************************************")
#********************************************************************************************

def soma_lista(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista(lista[1:])


print(soma_lista([1, 2, 3, 4, 5]))  
print("********************************************************************************************")
#********************************************************************************************

def verificar_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    return verificar_palindromo(palavra[1:-1])


print(verificar_palindromo("radar")) 
print(verificar_palindromo("python"))  
print("********************************************************************************************")
#********************************************************************************************

def desenhar_triangulo(n, linha=1):
    if linha > n:
        return
    print('*' * linha)
    desenhar_triangulo(n, linha + 1)


desenhar_triangulo(8)

