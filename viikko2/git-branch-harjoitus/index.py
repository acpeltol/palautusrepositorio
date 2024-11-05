# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"summa x ja y on {summa(x, y)}")
print(f"erotus x ja y {erotus(x, y)}")
print(f"tulo x ja y{tulo(x,y)}")

logger("lopetetaan")
