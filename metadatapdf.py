from PyPDF2 import PdfFileReader, PdfFileWriter
import os 
import pickle

def printMeta(ruta):
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                ext=name.lower().rsplit(".",1) [-1]
                if ext in ["pdf"]:
                    print("[+] Metadata for file: %s " %(ruta+os.path.sep+name))
                    pdfFile = PdfFileReader(open(ruta+os.path.sep+name, "rb"))
                    docInfo = pdfFile.getDocumentInfo()
                    print("Tipo: ", type(docInfo))
                    for metaItem in docInfo:
                        Info = "[+] " + metaItem + ":" + docInfo[metaItem] 
                        file1 = open("Metadatos.txt", "a")
                        file1.write(Info + "\n")
                        file1.close 
