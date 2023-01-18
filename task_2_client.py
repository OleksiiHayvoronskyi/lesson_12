# Розробити сокет-сервер з бібліотекою asyncio.
# Сервер має приймати два числа і виконувати над ними прості арифметичні
# функції: додаваня, віднімання, множення - з використанням користувацьких
# функцій, які працюють в асинхронному режимі.

import asyncio, socket

print('--- Task 2. Client ---')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('lockalhost', 8888))
sock.send(b'2 + 2')
sock.close()