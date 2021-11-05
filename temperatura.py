from sense_hat import SenseHat
sense = SenseHat()

while True:
# Toma lecturas de los tres sensores
  
  t = sense.get_temperature() # temperatura
  p = sense.get_pressure() # presión
  h = sense.get_humidity() # humedad
  # Redondea los valores a un lugar decimal
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  # Crea el mensaje
  # str() convierte el valor en una cadena de caracteres, para que pueda ser concatenado
  message = "Temperatura: " + str(t) + " Presión: " + str(p) + " Humedad: " + str(h)
  # Muestra el mensaje
  sense.show_message(message)
  
