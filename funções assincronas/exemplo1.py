import asyncio

async def funcao1():
    print('entrando no sono...')
    await asyncio.sleep(3)
    print('saindo do sono...')

async def funcao2():
    print('rodando de forma independente!')

async def main():
    await asyncio.gather(funcao1(), funcao2())

if __name__ == '__main__':
    # Se a versão do seu Python for menor que 3.7, use o seguinte:
    #
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

    asyncio.run(main())
