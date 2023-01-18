# Розробити сокет-сервер з бібліотекою asyncio.
# Сервер має приймати два числа і виконувати над ними прості арифметичні
# функції: додаваня, віднімання, множення - з використанням користувацьких
# функцій, які працюють в асинхронному режимі.

import asyncio, socket

print('--- Task 2. Server ---')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8888))
sock.listen(5)
sock.setblocking(False)

while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print('no client')
    except KeyboardInterrupt:
        break
    else:
        client.setblocking(True)
        result = client.recv(1024)
        client.close()
        print('Message', result.decode('utf-8'))
        print(sum(result))