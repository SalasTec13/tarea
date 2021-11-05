from sense_hat import SenseHat
sense = SenseHat()

while True:
# Se declaran las variables de los tres sensores
  
  t = sense.get_temperature() 
  p = sense.get_pressure() 
  h = sense.get_humidity() 
  # Se redondean los valores a decimal
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  # Creamos el metodo mensaje, usando  str() que va a mostrar la cadena que se mostrara en los led´s
  message = "Temperatura: " + str(t) + " Presión: " + str(p) + " Humedad: " + str(h)
  # Se muestra el metodo
  sense.show_message(message)
  
