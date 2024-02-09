import random

# Definición de las opciones disponibles
options = ('piedra', 'papel', 'tijera')

# Contadores para el número de victorias del ordenador y del usuario
computer_wins = 0
user_wins = 0

# Contador de rondas
rounds = 1

# Función para obtener la opción del usuario
def obtener_opcion_usuario():
  while True:
    # Solicitar la opción al usuario
    user_option = input('piedra, papel o tijera (escribe "salir" para terminar) => ').lower()
    if user_option == "salir":
      return None  # Retorna None si el usuario desea salir del juego
    elif user_option not in options:
      print('Esa opción no es válida. Por favor, intenta de nuevo.')
    else:
      return user_option  # Retorna la opción válida del usuario

# Función para imprimir el resultado de la ronda
def imprimir_resultado(user_option, computer_option):
  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  if user_option == computer_option:
    print('Empate!')
    return 'empate'  # Retorna 'empate' si hay un empate
  elif (user_option == 'piedra' and computer_option == 'tijera') or \
      (user_option == 'papel' and computer_option == 'piedra') or \
      (user_option == 'tijera' and computer_option == 'papel'):
    print(f'{user_option} gana a {computer_option}')
    print('Usuario gana!')
    return 'user'  # Retorna 'user' si el usuario gana
  else:
    print(f'{computer_option} gana a {user_option}')
    print('Computadora gana!')
    return 'computer'  # Retorna 'computer' si la computadora gana

# Bucle principal del juego
while True:

  # Imprimir el encabezado de la ronda
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  # Imprimir el número de victorias del ordenador y del usuario
  print('computer_wins', computer_wins)
  print('user_wins', user_wins)

  # Obtener la opción del usuario
  user_option = obtener_opcion_usuario()
  if user_option is None:
    break  # Salir del bucle si el usuario desea salir del juego

  # Incrementar el número de rondas
  rounds += 1

  # Generar la opción del ordenador
  computer_option = random.choice(options)

  # Determinar el resultado de la ronda e incrementar el contador de victorias correspondiente
  ganador = imprimir_resultado(user_option, computer_option)
  if ganador == 'user':
    user_wins += 1
  elif ganador == 'computer':
    computer_wins += 1

  # Verificar si hay un ganador
  if computer_wins == 2:
    print('El ganador es la computadora')
    break

  if user_wins == 2:
    print('El ganador es el usuario')
    break
