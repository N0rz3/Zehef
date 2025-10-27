if __name__ == '__main__':
    import sys; sys.dont_write_bytecode = True
    import os

    # Ensure UTF-8 is used for stdio on Windows to avoid UnicodeEncodeError
    # when printing characters like emoji to the console (cp1252 default).
    # Try multiple approaches for compatibility across Python versions.
    try:
        # Prefer the Python 3.7+ reconfigure API
        if hasattr(sys.stdout, 'reconfigure'):
            try:
                sys.stdin.reconfigure(encoding='utf-8')
            except Exception:
                pass
            try:
                sys.stdout.reconfigure(encoding='utf-8')
            except Exception:
                pass
            try:
                sys.stderr.reconfigure(encoding='utf-8')
            except Exception:
                pass
        else:
            # Fall back to environment variable which is respected by Python
            os.environ.setdefault('PYTHONIOENCODING', 'utf-8')
            os.environ.setdefault('PYTHONUTF8', '1')
    except Exception:
        # Best-effort; if this fails we'll still continue and handle errors elsewhere
        pass

    from lib.helpers import show_banner; show_banner()
    import asyncio
    from main import main; asyncio.run(main())