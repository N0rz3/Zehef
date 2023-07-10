@echo off

color 0A     
echo Installation requirements                                                                           
                                                                                                                                                                             
pip install httpx
pip install holehe
pip install argparse
pip install datetime
pip install pwnedpasswords
pip install scrape-search-engine
pip install requests

if %errorlevel% equ 0 (
    echo [+] Installation successful
) else (
    echo [-] Installation failed
)
pause