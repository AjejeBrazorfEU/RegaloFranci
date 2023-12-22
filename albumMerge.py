import cv2
import os
import numpy as np


def unisci_immagini(pics, output_path):
    # Carica tutte le immagini

    images = []
    for pic in pics:
        if os.path.exists(pic):
            images.append(cv2.imread(pic))

    while len(images) < 6:
        images.append(255 * np.ones(images[0].shape, dtype=np.uint8))

    # Metti le prime quattro immagini una sotto l'altra
    album = cv2.vconcat([images[0], images[1], images[2], images[3]])

    # Ruota di 180 gradi le ultime due immagini
    images[4] = cv2.rotate(images[4], cv2.ROTATE_90_CLOCKWISE)
    images[5] = cv2.rotate(images[5], cv2.ROTATE_90_CLOCKWISE)

    # Metti le ultime due immagini una sotto l'altra
    # Prima però bisogna aggiungere del padding per farle combaciare con le prime quattro
    altezza, larghezza, _ = images[4].shape
    bordo = (album.shape[1] - larghezza) // 2
    print(bordo)
    images[4] = cv2.copyMakeBorder(images[4], bordo*2//3, bordo * 4//3,bordo//2, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    images[5] = cv2.copyMakeBorder(images[5], 0, bordo*2//3,bordo//2,0, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    album2 = cv2.vconcat([images[4], images[5]])

    # Salva le immagini prima di unirle
    cv2.imwrite("album1.png", album)
    cv2.imwrite("album2.png", album2)
    # Unisci le due immagini
    print(album.shape, album2.shape)
    album_united = cv2.hconcat([album, album2])

    # Salva l'immagine risultante
    cv2.imwrite(output_path, album_united)

if __name__ == "__main__":
    # Apri cartella e leggi tutte le immagini
    pics = []
    j = 0
    for image in os.listdir("CopertineFinali"):
        output_path = f"CopertineFinaliUnite/album_united{j}.png"
        print(image)
        j+=1
    
        pics.append('CopertineFinali/' + image)
        if j % 6 == 0:
            unisci_immagini(pics, output_path)
            pics = []
    unisci_immagini(pics, output_path)