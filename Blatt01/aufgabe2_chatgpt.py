from PIL import Image
import sys

def invert_image(input_path, output_path):
    # Bild laden
    image = Image.open(input_path)
    image = image.convert("RGB")  # sicherstellen, dass das Bild im RGB-Format ist

    # Pixel invertieren
    inverted_image = Image.eval(image, lambda x: 255 - x)

    # Invertiertes Bild speichern
    inverted_image.save(output_path)
    print(f"Invertiertes Bild wurde gespeichert unter: {output_path}")

if __name__ == "__main__":
    # Prüfen, ob die Eingabeparameter vorhanden sind
    if len(sys.argv) != 3:
        print("Verwendung: python Blatt01\aufgabe2_chatgpt.py Blatt01\\img\\kaktusmensch.png Blatt01\\img\\kaktusmensch1.png")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        invert_image(input_path, output_path)
