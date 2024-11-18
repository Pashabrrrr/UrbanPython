
def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    x = 0
    y = 0
    b = ""
    d = ""

    b = sender[len(sender)-3: len(sender)]
    if b == "com" or b == "net" or b == ".ru":
        x = x + 1
    if sender.find("@") != -1:
        x = x + 1

    d = recipient[len(recipient)-3: len(recipient)]
    if d == "com" or d == "net" or d == ".ru":
        y = y + 1
    if recipient.find("@") != -1:
        y = y + 1

    if x != 2 or y != 2:
        print(f"Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient)
    elif recipient == sender:
        print("Невозможно отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient)

send_email("Добрый день", "example@gmail.com")
send_email("Проверка отправки с нестандартного адреса", "fan@mail.ru", sender = "urban.test@gmail.com")
send_email("Проверка неправильного адреса", "mailmail.ru")
