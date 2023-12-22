from docx import Document
from docx.shared import Cm
import cv2
import docx
import os
from docx2pdf import convert
import time

def crea_documento_word_immagini(immagini, percorso_output):
    # Crea un nuovo documento Word
    doc = Document()

    # Imposta il layout del documento su A4
    doc.sections[0].start_type
    section = doc.sections[0]
    section.start_type
    # Convert in cm
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(1.27)
    section.right_margin = Cm(1.27)
    section.top_margin = Cm(1.27)
    section.bottom_margin = Cm(1.27)

    # Aggiungi le immagini al documento
    for img_path in immagini:
        doc.add_picture(img_path, width=Cm(18))

    # Salva il documento
    doc.save(percorso_output)

if __name__ == "__main__":
    immagini = []
    for images in os.listdir('CopertineFinaliUnite'):    
        immagini.append(f"CopertineFinaliUnite/{images}")
    documento_output = "documento_word_con_immagini.docx"

    crea_documento_word_immagini(immagini, documento_output)

    # Sleeps for 2 seconds
    time.sleep(2)
    convert(documento_output)
