# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")
print(f"{tulo(x,y)}")

logger("lopetetaan")
