import pywhatkit
from number import mobiles

msg = ""
time_hour = 8
time_min = 27
for i in mobiles:

    pywhatkit.sendwhatmsg(i,msg, time_hour, time_min, 32, True, 3)
    time_min = time_min + 1
    if (time_min >= 60 ):
        time_hour = time_hour + 1
        time_min = 0




# msg = "¿Te apasiona la tecnología y quieres aprender a crear aplicaciones web con Python? \n Este webinar gratuito está especialmente diseñado para chicas de la FISI de todas las especialidades.\nEn este taller aprenderás: Fundamentos de Python, Desarrollo web con Django y APIs con Django REST Framework.\nNo necesitas experiencia previa en Python, aquí te guiaremos desde cero.\nFechas: Sábados 6, 13, 20 y 27 de abril.\nHora: 06:00 p.m.\nLugar: Laboratorio de la FISI (por asignar) y vía Zoom para quienes no puedan asistir de forma presencial.\nInscripciones:  https://forms.gle/hZ57ipwP1A7Zapo56 \nInstructor: Jorge Jesús de la Base 22\nSi ya te inscribiste omite el mensaje, por favor. Gracias."