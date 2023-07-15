@echo off

color 0A     
echo Installation requirements                                                                           
                                                                                                                                                                             
pip install httpx==0.24.1
pip install holehe==1.61
pip install argparse==1.4.0
pip install datetime==5.1
pip install pwnedpasswords==2.0.0
pip install scrape-search-engine==0.2.2
pip install requests==2.31.0

if %errorlevel% equ 0 (
    echo [+] Installation successful
) else (
    echo [-] Installation failed
)
pause
