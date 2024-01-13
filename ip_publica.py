from requests import get
import time
from email.message import EmailMessage
import ssl
import smtplib
from passw import contraseña, mail, mail_receptor


    # Guardar ip dentro de txt
    # Meter timer cada 3hs
    # Comparar contenido de txt con lo que me devuelva la ejecucion de .py
    # Si no cambio -> no hago nada, ejecuto timer
    # Si cambio -> reemplazarlo en el txt y enviar mail con ip nueva

def timer():
    public_ip = get("http://api.ipify.org").text
    print(public_ip)
    with open('ip2.txt', 'r+') as file:
        content = (file.readline()) 
        if content == public_ip:
            print("Es igual")
        else:
            file.seek(0)
            file.truncate()
            file.write(public_ip)

            email_emisor = mail
            email_pass = contraseña
            email_receptor = mail_receptor
            asunto = 'cambio de ip'
            message = f"""Our IP recently changed, this is the new one: {public_ip}"""

            em = EmailMessage()
            em['From'] = email_emisor
            em['to'] = email_receptor
            em['Subject'] = asunto
            em.set_content(message)
            contexto = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=contexto) as smtp:
                smtp.login(email_emisor, email_pass)
                smtp.sendmail(email_emisor,email_receptor,em.as_string())

            
    time.sleep(3)
    timer()


  
