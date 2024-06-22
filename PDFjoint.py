from os import *
import datetime
from PyPDF2 import PdfMerger


def Banner():
    banner = """
  ____  ____  _____ _       _       _    
 |  _ \|  _ \|  ___(_) ___ (_)_ __ | |_  
 | |_) | | | | |_  | |/ _ \| | '_ \| __| 
 |  __/| |_| |  _| | | (_) | | | | | |_  
 |_|   |____/|_|  _/ |\___/|_|_| |_|\__| 
                 |__/                    
    """
    sottotitolo = "© A.Monti 2024\n"
    utilizzo = """Usage:
1) Rename the files that are to be merged like this: 00.pdf, 01.pdf, 02.pdf... etc.
2) Place them in the folder that contains PDFjoint.exe
3) Start PDFjoint.exe
CTRL+c to exit"""
    print(banner)
    print(sottotitolo)
    print(utilizzo)

def Controllo_nome(nome):
    nome_iniz = nome[0:-4]
    if nome.endswith(".pdf") and nome_iniz.isnumeric():
        return True
    else:
        return False

def Nome_file():
    now = datetime.datetime.now()
    return f"PJ_{now.day}_{now.month}_{now.year}_{now.hour}_{now.minute}.pdf"

Banner()

x = [a for a in listdir() if Controllo_nome(a)]

if not x:
    print("\nThere are no files to join")
    input("Press a key to exit...")
    exit()

nome_file = input("\nEnter the name of the final file >>> ")

if nome_file == "":
    nome_file = Nome_file() 
else:
    nome_file = nome_file + ".pdf"

print("\nFiles to join")
for i in range(0, len(x)):
    print(f"File {i+1}: {x[i]}")

while True:
    scelta = input("\nPress return to merge or 0 to exit >>> ")

    if scelta == "0":
        exit()
    if scelta == "":
        merger = PdfMerger()
        for pdf in x:
            merger.append(pdf)
        merger.write(nome_file)
        merger.close()
        exit()

