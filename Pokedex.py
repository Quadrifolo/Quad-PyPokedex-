import tkinter as tk
import pypokedex
import PIL.Image
import PIL.ImageTk
import urllib3
from io import BytesIO

# pokemon = pypokedex.get(name="charmander")
# print(pokemon.dex)
# print(pokemon.name)
# print(pokemon.abilities)

# Geometry For Window
window = tk.Tk()
window.geometry("700x600")
window.title("Quad Pokedex Tutorial")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Quad Python Pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial, 20"))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_abilities = tk.Label(window)
pokemon_abilities.config(font=("Arial", 10))
pokemon_abilities.pack(padx=10, pady=10)

pokemon_BaseStats = tk.Label(window)
pokemon_BaseStats.config(font=("Arial", 10))
pokemon_BaseStats.pack(padx=10, pady=10)

pokemon_moves = tk.Label(window)
pokemon_moves.config(font=("Arial", 10))
pokemon_moves.pack(padx=10, pady=10)


# FUNCTION


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    # Retrieves Images being used by Pokemon
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    # Processing of the image locally
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    # Fields that appear on the GUI and how they are formatted
    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())
    pokemon_abilities.config(text=f"{pokemon.abilities}".title())
    pokemon_BaseStats.config(text=f"{pokemon.base_stats}".title())
    pokemon_moves.config(text=(move.name for move in pokemon.moves).title())


# Text Label Config
label_id_name = tk.Label(window, text="Enter ID or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

# Text Settings
text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

# Button Config
btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()
