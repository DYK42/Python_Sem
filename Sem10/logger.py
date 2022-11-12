from datetime import datetime


def log_by_msg(message):
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(
            f'{datetime.now().strftime("%Y.%m.%d %H:%M:%S")}, {str(message.chat.first_name)}, {str(message.chat.last_name)}, {str(message.text)}\n')
        file.close()

