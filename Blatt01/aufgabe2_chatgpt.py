from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_histogram(image, title):
    # Histogramme für RGB-Kanäle berechnen
    r, g, b = image.split()
    plt.figure(figsize=(10, 5))
    plt.suptitle(title)

    # Rotes Histogramm
    plt.subplot(1, 3, 1)
    plt.hist(np.array(r).flatten(), bins=256, color='red', alpha=0.6, range=(0, 255))
    plt.title("Red Channel")

    # Grünes Histogramm
    plt.subplot(1, 3, 2)
    plt.hist(np.array(g).flatten(), bins=256, color='green', alpha=0.6, range=(0, 255))
    plt.title("Green Channel")

    # Blaues Histogramm
    plt.subplot(1, 3, 3)
    plt.hist(np.array(b).flatten(), bins=256, color='blue', alpha=0.6, range=(0, 255))
    plt.title("Blue Channel")

    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    plt.show()

def invert_image(input_path, output_path):
    # Bild laden
    image = Image.open(input_path)
    image = image.convert("RGB")  # sicherstellen, dass das Bild im RGB-Format ist

    # Histogramm des Originalbildes anzeigen
    plot_histogram(image, "Original Image RGB Histogram")

    # Pixel invertieren
    inverted_image = Image.eval(image, lambda x: 255 - x)

    # Histogramm des invertierten Bildes anzeigen
    plot_histogram(inverted_image, "Inverted Image RGB Histogram")

    # Invertiertes Bild speichern
    inverted_image.save(output_path)
    print(f"Invertiertes Bild wurde gespeichert unter: {output_path}")

if __name__ == "__main__":
    # Prüfen, ob die Eingabeparameter vorhanden sind
    if len(sys.argv) != 3:
        print("Verwendung: python Blatt01\\aufgabe2_chatgpt.py Blatt01\\img\\kaktusmensch.png Blatt01\\img\\kaktusmensch1.png")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        invert_image(input_path, output_path)
