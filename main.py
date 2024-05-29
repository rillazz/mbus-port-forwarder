import socket
import logging

logger = logging.getLogger("Server")


class Device:
    def __init__(self, host: str, port: int) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        logger.info(" [*] Opened Device Socket")
        self.bind()
        logger.info(" [*] Binded The Device")

    def bind(self) -> None:
        self.socket.listen(4)
        self.connection, self.address = self.socket.accept()
        self.connection.settimeout(30)


class Client(Device):
    def __init__(self, host: str, port: int, device_conn) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(4)
        logger.info(" [*] Opened Client Socket")
        while True:
            self.bind()
            logger.info(" [*] Binded The Client")
            self.work(device_conn)

    def bind(self) -> None:
        
        self.connection, self.address = self.socket.accept()
        self.connection.settimeout(30)

    def work(self, device_conn: socket.socket) -> None:
        logger.info(" [*] Running...")
        while True:
            data = self.connection.recv(2048)
            if data == b"":
                logger.info(" [*] Client Disconnected")
                break
            logger.info(" [*] Recieved Data")
            device_conn.send(data)
            response = device_conn.recv(2048)
            self.connection.send(response)
        self.connection.close()


class Server:
    def __init__(self) -> None:
        self.device = Device("localhost", 51111)
        self.client = Client("localhost", 52222, self.device.connection)


def main():
    logging.basicConfig(level="INFO")
    Server()


if __name__ == "__main__":
    main()
