def main():
  
  def suma(num1, num2):
    return num1 + num2

  def resta(num1, num2):
    return num1 - num2

  def multiplicacion(num1, num2):
    return num1 * num2

  def division(num1, num2):
    return num1 / num2

  def potencia(num1, num2):
    return num1 ** num2

  print("Bienvenid@")
  print("---Esta calculadora calcula operaciones SOLO de izquierda a derecha---")
  print("---Por ejemplo: 1 + 4 * 5")
  print("---Esto nos dará: 25")
  print("---Ya que no obedece la jerarquía matemática---")
  print("---Para salir, escriba 'salir'---")

  while True:

    try:

      operacion = ""
      operacion = input("Ingrese la operacion que desea realizar: ")
  
      if operacion == "salir":
        break;
    
      simbolos = []
      numeros = []
    
      #-----------------SEPARAMOS
      numero_temporal = " "
      for n in operacion:
        if n in ["+", "-", "*", "/", "^"]:
          simbolos.append(n)
          if numero_temporal !=" ":
            numeros.append(float(numero_temporal))
            numero_temporal = " "
        elif n == " ":
          continue
        else:
          numero_temporal += n
  
      
    
      if numero_temporal != " ":
        numeros.append(float(numero_temporal))
    
      #----------------------INICIALIZACION
    
      resultado = numeros[0]
    
      #----------------------OPERACIONES
    
      for i in range(len(simbolos)):
        if simbolos[i] == "+":
          resultado = suma(resultado, numeros[i+1])
        elif simbolos[i] == "-":
          resultado = resta(resultado, numeros[i+1])
        elif simbolos[i] == "*":
          resultado = multiplicacion(resultado, numeros[i+1])
        elif simbolos[i] == "/":
          resultado = division(resultado, numeros[i+1])
        elif simbolos[i] == "^":
          resultado = potencia(resultado, numeros[i+1])
    
      #-----------------IMPRIMIMOS RESULTADO FINAL
      print(resultado)
    except (SyntaxError, NameError, ZeroDivisionError, ValueError):
      print("Error en la entrada. Inténtelo de nuevo.")

      #Try y Except:Para evitar que el programa se detenga al ingresar un valor no válido. Créditos a Ariel Cruz

if __name__=="__main__":
  main()