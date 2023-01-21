# Розробити сокет-сервер з бібліотекою asyncio.


import asyncio

print('--- Task 2. Server ---')


# СЕРВЕР.
class EchoServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        print("I'm server:))")

    # Створюю з’єднання
    def connection_made(self, transport):
        address = transport.get_extra_info('peername')

        print(f'Connection from {address}')
        self.transport = transport

    def data_received(self, data):
        message = data.decode()

        print(f'It was received: {message}')

        print(f'It was sent: {message}')
        self.transport.write(data)

        print('Close the client socket.')
        print("---------------------------")
        self.transport.close()


# Створюю цикл подій, що буде чекати нових з’єднань.
async def main():
    loop = asyncio.get_running_loop()
    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())
