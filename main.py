import smtplib
from email.message import EmailMessage
from tkinter import *


def send_email():
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

    sever = None

    try:
        server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
        server.login(sender_email, password)
        server.send_message(msg)
        result_label.config(text="Письмо отправлено")
    except Exception as e:
        result_label.config(f"Произошла ошибка: {e}")
    finally:
        if server:
            server.quit()

window = Tk()
window.title("Отправка E-mail")
window.geometry("500x300")

Label(text="Отправитель:").grid(row=0, column=0, sticky=W)
sender_email_entry = Entry()
sender_email_entry.grid(row=0, column=1, sticky=W)

Label(text="Получатель:").grid(row=1, column=0, sticky=W)
password_entry = Entry()
password_entry.grid(row=1, column=1, sticky=W)

Label(text="Пароль приложения:").grid(row=2, column=0, sticky=W)
recepient_email_entry = Entry()
recepient_email_entry.grid(row=2, column=1, sticky=W)

Label(text="Тема письма:").grid(row=3, column=0, sticky=W)
subject_entry = Entry()
subject_entry.grid(row=3, column=1, sticky=W)

Label(text="Сообщение:").grid(row=4, column=0, sticky=W)
body_text_entry = Text(width=45, height=10)
body_text_entry.grid(row=4, column=1, sticky=W)

Button(text="Отправить письмо", command=send_email).grid(row=5, column=1, sticky=W)

result_label = Label(text="")
result_label.grid(row=6, column=1, sticky=W)

window.mainloop()