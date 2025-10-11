"""
License: MIT
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"

def sort_list(items, ascending=True, remove_duplicates =False):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    # Si se solicita, eliminar duplicados antes de ordenar
    if remove_duplicates:
        items = list(set(items))

    return sorted(items, reverse=(not ascending), nuevo)

if __name__ == "__main__":
    # Argumentos por defecto
    remove_duplicates = False

    # Parseo simple de argumentos
    args = sys.argv[1:]

    # Comprobar si se pasa --unique
    if "--unique" in args:
        remove_duplicates = True
        args.remove("--unique")

    filename = DEFAULT_FILENAME
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("Se debe indicar el fichero como primer argumento")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        word_list = [33]
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(sort_list(word_list, remove_duplicates=remove_duplicates))

