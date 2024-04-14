if __name__ == '__main__':
    import sys; sys.dont_write_bytecode = True
    from lib.helpers import show_banner; show_banner()
    import asyncio
    from main import main; asyncio.run(main())