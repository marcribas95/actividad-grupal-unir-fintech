"""
License: MIT
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"

def sort_list(items, ascending=True):
    """Ordena una lista de palabras en orden ascendente o descendente."""
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    return sorted(items, reverse=not ascending)


def count_words(items):
    """Cuenta cuántas palabras hay en la lista."""
    if not isinstance(items, list):
        raise RuntimeError(f"No puede contar elementos de {type(items)}")
    return len(items)


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("Se debe indicar el fichero como primer argumento.")
        print(f"Ejemplo: python {sys.argv[0]} words.txt")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero: {filename}")
    file_path = os.path.join(".", filename)

    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                palabra = line.strip()
                if palabra:
                    word_list.append(palabra)
    else:
        print(f"El fichero {filename} no existe, se usarán palabras por defecto.")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print("\nLista ordenada:")
    print(sort_list(word_list))

    print("\nNúmero total de palabras:")
    print(count_words(word_list))
