import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def enviar_correos(receiver_email):
    port = 587  # For starttls
    smtp_server = "smtp.office365.com"
    subject = "Obtención de metadatos y valores Hash de PDFS"
    body = "Pía"
    sender_email = "Pruebasdeciberseguridad@outlook.com"
    password = "Pruebacontra9"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Bcc"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    filename = ["Obtencion_hash.txt", "Metadatos.txt"]

    for i in filename:

        with open(i, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {i}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    os.system ("cls")
    print("El correo ha sido enviado exitosamente")
