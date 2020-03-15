from .__module__ import Client, Server

if __name__ == '__main__':
    await Server()
else:
    return await Client()

