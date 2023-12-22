import cv2
import os
import numpy as np

def draw_dashed_line(image, start_point, end_point, color, thickness, dash_length, space_length):
    x1, y1 = start_point
    x2, y2 = end_point
    dx = x2 - x1
    dy = y2 - y1
    distance = max(abs(dx), abs(dy))
    dx = dx / distance if distance != 0 else 0
    dy = dy / distance if distance != 0 else 0

    for i in range(int(distance / (dash_length + space_length))):
        x_start = int(x1 + i * (dash_length + space_length) * dx)
        y_start = int(y1 + i * (dash_length + space_length) * dy)
        x_end = int(x1 + (i + 1) * dash_length * dx)
        y_end = int(y1 + (i + 1) * dash_length * dy)
        cv2.circle(image, (x_start, y_start), 2, color, thickness)
        #cv2.line(image, (x_start, y_start), (x_end, y_end), color, thickness)

def unisci_e_traccia_linee(fronte_path, retro_path, output_path):
    # Carica le immagini
    fronte = cv2.imread(fronte_path)
    retro = cv2.imread(retro_path)

    # Ridimensiona le immagini se hanno dimensioni diverse
    """altezza_fronte, larghezza_fronte, _ = fronte.shape
    altezza_retro, larghezza_retro, _ = retro.shape

    if altezza_fronte != altezza_retro or larghezza_fronte != larghezza_retro:
        altezza_max = max(altezza_fronte, altezza_retro)
        larghezza_max = max(larghezza_fronte, larghezza_retro)

        fronte = cv2.resize(fronte, (larghezza_max, altezza_max))
        retro = cv2.resize(retro, (larghezza_max, altezza_max))

    # Rendi le immagini quadrate
    altezza, larghezza, _ = fronte.shape

    if altezza > larghezza:
        fronte = cv2.resize(fronte, (altezza, altezza))
        retro = cv2.resize(retro, (altezza, altezza))
    elif larghezza > altezza:
        fronte = cv2.resize(fronte, (larghezza, larghezza))
        retro = cv2.resize(retro, (larghezza, larghezza))
"""
    fronte = cv2.resize(fronte, (1000, 1000))
    retro = cv2.resize(retro, (1000, 1000))
    # Unisci le due immagini
    album_united = cv2.hconcat([fronte, retro])

    # Espandi le dimensioni dell'immagine risultante
    altezza, larghezza, _ = album_united.shape
    bordo = altezza//8  # Larghezza del bordo esterno

    album_united_expanded = 255 * np.ones((altezza + 2 * bordo, larghezza, 3), dtype=np.uint8)
    album_united_expanded[bordo:bordo + altezza, :] = album_united

    # Disegna le linee attorno all'album
    spessore_linea = 5

    # Linea superiore
    """cv2.line(album_united_expanded, (0, 0), (larghezza + 2 * bordo, 0), (0, 255, 0), spessore_linea)
    # Linea inferiore
    cv2.line(album_united_expanded, (0, altezza + 2 * bordo), (larghezza + 2 * bordo, altezza + 2 * bordo), (0, 255, 0), spessore_linea)
    # Linea sinistra
    cv2.line(album_united_expanded, (0, 0), (0, altezza + 2 * bordo), (0, 255, 0), spessore_linea)
    # Linea destra
    cv2.line(album_united_expanded, (larghezza + 2 * bordo, 0), (larghezza + 2 * bordo, altezza + 2 * bordo), (0, 255, 0), spessore_linea)
    """
    d = larghezza//25
    h = altezza//10
    lunghezza_trattino = 10
    spaziatura_trattino = 10
    draw_dashed_line(album_united_expanded, (larghezza//2, bordo), (larghezza//2 + d, bordo - h), (0,0,0), spessore_linea,lunghezza_trattino, spaziatura_trattino)
    draw_dashed_line(album_united_expanded, (larghezza//2 + d, bordo - h), (larghezza-d,bordo - h), (0,0,0), spessore_linea, lunghezza_trattino, spaziatura_trattino)
    draw_dashed_line(album_united_expanded, (larghezza-d,bordo - h), (larghezza, bordo), (0,0,0), spessore_linea, lunghezza_trattino, spaziatura_trattino)
    
    h2 = altezza + 2 * bordo
    draw_dashed_line(album_united_expanded, (larghezza//2, h2-bordo), (larghezza//2 + d, h2- (bordo - h)), (0,0,0), spessore_linea,lunghezza_trattino, spaziatura_trattino)
    draw_dashed_line(album_united_expanded, (larghezza//2 + d, h2-(bordo - h)), (larghezza-d,h2-(bordo - h)), (0,0,0), spessore_linea, lunghezza_trattino, spaziatura_trattino)
    draw_dashed_line(album_united_expanded, (larghezza-d,h2-(bordo - h)), (larghezza, h2-bordo), (0,0,0), spessore_linea, lunghezza_trattino, spaziatura_trattino)
    
    
    cv2.imwrite(output_path, album_united_expanded)

if __name__ == "__main__":

    # Apri cartella e leggi tutte le immagini
    for image in os.listdir("Copertine"):
        print(image)
        if image.endswith("_fronte.jpg"):
            fronte_path = f"Copertine/{image}"
            retro_path = f"Copertine/{image[:-11]}_retro.jpg"
            output_path = f"CopertineFinali/{image[:-11]}.jpg"
        elif image.endswith("_retro.jpg"):
            continue
        else:
            fronte_path = f"Copertine/{image}"
            retro_path = f"Copertine/{image}"
            output_path = f"CopertineFinali/{image}"

        unisci_e_traccia_linee(fronte_path, retro_path, output_path)
