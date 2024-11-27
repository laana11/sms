import smtplib
from email.message import EmailMessage

sender_email = "kamlaana@yandex.ru"
recipient_mail = "laa_na@mail.ru"
password = "lvchlndubmrvxfht"
subject = "Проверка связи"
body = "Привет! Это проверка связи из программы"

msg = EmailMessage()
msg.set_content(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_mail

try:
    server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    server.login(sender_email, password)
    server.send_message(msg)
    print("Письмо отправлено")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    if server:
        server.quit()