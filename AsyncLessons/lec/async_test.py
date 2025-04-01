import asyncio


class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def __enter__(self):
        print('вход в контекст')
        
    def __exit__(self, ext_type, exc, tb):
        print('выход из контекста')
    
    async def __aenter__(self):
        print('вход в асинх контекст')
    
    async def __aexit__(self, exc_type, exc, tb):
        print('выход из асинх контекста')
    
async def main():
    async with Connection('localhost', 8080) as c:
        print(c.host, c.port)
    
    with Connection('localhost', 8080) as c:
        pass


asyncio.run(main())  # noqa: F821
