import sys
import antlr

def main(argv):
  antlr.main(argv)
  lista_cuadruplos = antlr.rules.cuadruplos
  memoria = antlr.rules.memoria
  
  i = 1
  print("___CUADRUPLOS___")
  while(lista_cuadruplos):
    contador = lista_cuadruplos[0]['cont']
    operacion = lista_cuadruplos[0]['op']
    izquierdo = lista_cuadruplos[0]['izq']
    derecho = lista_cuadruplos[0]['der']
    resultado = lista_cuadruplos[0]['res']

    # Sacar los datos e ir metiendo los valores a memoria

    if (operacion == '1'):
      print(str(i)+": " + "PRINT" + "\t_\t_\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]

      print(valorRes[0])
    elif (operacion == '2'):
      print(str(i)+": " + izquierdo + "\t" + "SUMA" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) + int(valorDer[0])

      # print(pedazoMemoriaResultado)

    elif (operacion == '3'):
      print(str(i)+": " + izquierdo + "\t" + "RESTA" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) - int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '4'):
      print(str(i)+": " + izquierdo + "\t" + "MULTIPLICACION" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) * int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '5'):
      print(str(i)+": " + izquierdo + "\t" + "DIVISION" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) / int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '6'):
      print(str(i)+": " + izquierdo + "\t" + "MODULO" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) % int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '7'):
      print(str(i)+": " + izquierdo + "\t" + "MAYOR" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) > int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '8'):
      print(str(i)+": " + izquierdo + "\t" + "MENOR" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) < int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '9'):
      print(str(i)+": " + izquierdo + "\t" + "MAYORIGUAL" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) >= int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '10'):
      print(str(i)+": " + izquierdo + "\t" + "MENORIGUAL" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) <= int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '11'):
      print(str(i)+": " + resultado + "\t" + "ASIGNACION" + "\t_\t" + izquierdo)
      # Sacar tipo y localidad de resultado y valor a asignar
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)

      # print(res, izq)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]

      # print(pedazoMemoriaResultado, pedazoMemoriaIzquierdo)

      # Sacar valor de memoria
      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]

      # print(valorRes, valorIzq)

      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = valorIzq[0]

      # print(pedazoMemoriaResultado)

    elif (operacion == '12'):
      print(str(i)+": " + izquierdo + "\t" + "EQUAL" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) == int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '13'):
      print(str(i)+": " + izquierdo + "\t" + "NOTEQUAL" + "\t" + derecho + "\t" + resultado)
      res = sacaTipoYLocalidad(resultado)
      izq = sacaTipoYLocalidad(izquierdo)
      der = sacaTipoYLocalidad(derecho)

      pedazoMemoriaResultado = getattr(memoria, res[0])[res[1]]
      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]
      pedazoMemoriaDerecho = getattr(memoria, der[0])[der[1]]

      valorRes = [pedazoMemoriaResultado[value] for value in pedazoMemoriaResultado if int(resultado) == value]
      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]
      valorDer = [pedazoMemoriaDerecho[value] for value in pedazoMemoriaDerecho if int(derecho) == value]

      # print(valorRes, valorIzq, valorDer)
      
      for item in pedazoMemoriaResultado.items():
        if (item[1] == valorRes[0]):
          pedazoMemoriaResultado[item[0]] = int(valorIzq[0]) != int(valorDer[0])

      # print(pedazoMemoriaResultado)
    elif (operacion == '14'):
      print(str(i)+": " + "GOTO " + "\t_\t_\t" + resultado)
      # BRINCAR AL CUADRUPLO: resultado
    elif (operacion == '15'):
      print(str(i)+": " + "GOTOF "+ "\t" + izquierdo + "\t_\t" + resultado)
      izq = sacaTipoYLocalidad(izquierdo)

      pedazoMemoriaIzquierdo = getattr(memoria, izq[0])[izq[1]]

      valorIzq = [pedazoMemoriaIzquierdo[value] for value in pedazoMemoriaIzquierdo if int(izquierdo) == value]

      print(valorIzq)

      if (valorIzq[0] == False):
        print("hi")
        # BRINCAR AL CUADRUPLO: resultado
    else:
      print(operacion)

    lista_cuadruplos.pop(0)
    i = i + 1

def sacaTipoYLocalidad(variable):
  if (1000 <= int(variable) < 9000):
    tipo = 'int'
    if (1000 <= int(variable) < 3000):
      localidad = 'global'
    elif (3000 <= int(variable) < 5000):
      localidad = 'local'
    elif (5000 <= int(variable) < 7000):
      localidad = 'temporal'
    elif (7000 <= int(variable) < 9000):
      localidad = 'constante'
  elif (9000 <= int(variable) < 17000):
    tipo = 'float'
    if (9000 <= int(variable) < 11000):
      localidad = 'global'
    elif (11000 <= int(variable) < 13000):
      localidad = 'local'
    elif (13000 <= int(variable) < 15000):
      localidad = 'temporal'
    elif (15000 <= int(variable) < 17000):
      localidad = 'constante'
  elif (17000 <= int(variable) < 25000):
    tipo = 'string'
    if (17000 <= int(variable) < 19000):
      localidad = 'global'
    elif (19000 <= int(variable) < 21000):
      localidad = 'local'
    elif (21000 <= int(variable) < 23000):
      localidad = 'temporal'
    elif (23000 <= int(variable) < 25000):
      localidad = 'constante'
  elif (25000 <= int(variable) < 31000):
    tipo = 'bool'
    if (25000 <= int(variable) < 27000):
      localidad = 'global'
    elif (27000 <= int(variable) < 29000):
      localidad = 'local'
    elif (29000 <= int(variable) < 31000):
      localidad = 'temporal'
    elif (31000 <= int(variable) < 33000):
      localidad = 'constante'
  
  return [tipo, localidad]

if __name__ == '__main__':
  main(sys.argv)