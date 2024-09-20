import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Listează extensiile pe care dorești să le instalezi
packages = [
    "numpy",
    "pandas",
    "matplotlib",
    "reportlab",
    "requests",
    "beautifulsoup4",
    # Adaugă aici alte extensii dorite
]

for package in packages:
    install(package)

print("Toate extensiile au fost instalate cu succes!")
