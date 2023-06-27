import tkinter as tk
import requests
import json
import os
from PIL import Image, ImageTk
import io


class PokedexAPI:
    #Asignamos la url de la página de donde obtendremos los datos Pokémon
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon"

    def search_pokemon(self, value):
        # Verificar si se ingresó un número o un nombre de Pokémon
        if not value:
            raise ValueError("Ingrese un número o nombre de Pokémon.")

        if value.isdigit():
            # Si se ingresó un número, obtener los datos del Pokémon por su ID
            pokemon_id = int(value)
            if pokemon_id <= 0:
                raise ValueError("El número de Pokémon debe ser un entero positivo.")
            response = requests.get(f"{self.base_url}/{pokemon_id}")
        else:
            # Si se ingresó un nombre, obtener los datos del Pokémon por su nombre
            response = requests.get(f"{self.base_url}/{value.lower()}")

        # Verificar si se encontró el Pokémon
        if response.status_code == 404:
            raise ValueError("No se encontró el Pokémon.")

        # Obtener los datos del Pokémon en formato JSON
        pokemon_data = response.json()
        return pokemon_data


class PokedexGUI:
    # Hacemos que la ventana sea desplegada completamente
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokedex")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#F5E1A4")

        # Creación del marco principal de la interfaz gráfica
        main_frame = tk.Frame(self.root, bg="#BDB76B", bd=5)  # Marco principal con color de fondo y borde
        main_frame.pack(expand=True, padx=20, pady=40)  # Empaquetar el marco con opciones de expansión y relleno

        # Etiqueta de título
        title_label = tk.Label(main_frame, text="Pokédex", font=("Arial", 24, "bold"), bg="#BDB76B", fg="#4D4C47")
        title_label.pack(pady=10)  # Empaquetar la etiqueta con relleno vertical

        # Etiqueta para solicitar al usuario que ingrese el número o nombre del Pokémon
        label = tk.Label(main_frame, text="Ingrese el número o nombre del Pokémon:", font=("Arial", 12, "bold"),
                        bg="#BDB76B", fg="#4D4C47")
        label.pack()  # Empaquetar la etiqueta

        # Entrada para que el usuario ingrese el número o nombre del Pokémon
        self.entry1 = tk.Entry(main_frame, font=("Arial", 12))
        self.entry1.pack()  # Empaquetar la entrada

        # Botón de búsqueda
        button1 = tk.Button(main_frame, text="Buscar", font=("Arial", 12, "bold"), command=self.search_pokemon,
                            bg="#4D4C47", fg="#F5E1A4")
        button1.pack(pady=10)  # Empaquetar el botón con relleno vertical

        # Etiqueta para mostrar el número del Pokémon buscado
        self.number_label = tk.Label(main_frame, text="", font=("Arial", 12), bg="#BDB76B", fg="#4D4C47")
        self.number_label.pack()  # Empaquetar la etiqueta

        # Etiqueta para mostrar el nombre del Pokémon buscado
        self.name_label = tk.Label(main_frame, text="", font=("Arial", 16, "bold"), bg="#BDB76B", fg="#4D4C47")
        self.name_label.pack()  # Empaquetar la etiqueta

        # Etiqueta para mostrar la imagen del Pokémon buscado
        self.image_label = tk.Label(main_frame)
        self.image_label.pack(pady=10)  # Empaquetar la etiqueta con relleno vertical

        # Etiqueta para mostrar los tipos del Pokémon buscado
        self.types_label = tk.Label(main_frame, text="", font=("Arial", 12), bg="#BDB76B", fg="#4D4C47")
        self.types_label.pack()  # Empaquetar la etiqueta

        # Etiqueta para mostrar la altura del Pokémon buscado
        self.height_label = tk.Label(main_frame, text="", font=("Arial", 12), bg="#BDB76B", fg="#4D4C47")
        self.height_label.pack()  # Empaquetar la etiqueta

        # Etiqueta para mostrar el peso del Pokémon buscado
        self.weight_label = tk.Label(main_frame, text="", font=("Arial", 12), bg="#BDB76B", fg="#4D4C47")
        self.weight_label.pack()  # Empaquetar la etiqueta

        # Botón de salida
        exit_button = tk.Button(self.root, text="Salir", font=("Arial", 12, "bold"), command=self.root.quit,
                                bg="#4D4C47", fg="#F5E1A4")
        exit_button.pack(side="bottom", pady=20)  # Empaquetar el botón en la parte inferior de la interfaz con relleno inferior

        # Etiqueta para mostrar mensajes de error
        self.error_label = tk.Label(self.root, text="", fg="#FF0000", bg="#F5E1A4")
        self.error_label.pack(pady=10)  # Empaquetar la etiqueta con relleno vertical

        # Creación de una instancia de la clase PokedexAPI
        self.pokedex_api = PokedexAPI()

    #Método para ejecutar el bucle principal de la interfaz gráfica
    def run(self):
        self.root.mainloop()  # Iniciar el bucle principal de la GUI

    def search_pokemon(self):
        try:
            value = self.entry1.get().strip()
            # Obtener los datos del Pokémon desde la API
            pokemon_data = self.pokedex_api.search_pokemon(value)

            number = pokemon_data["id"]
            name = pokemon_data["name"]
            types = [t["type"]["name"] for t in pokemon_data["types"]]
            image_url = pokemon_data["sprites"]["front_default"]
            response_image = requests.get(image_url)
            image_data = response_image.content
            height = pokemon_data["height"] / 10
            weight = pokemon_data["weight"] / 10

            # Limpiar los datos anteriores y mostrar los nuevos datos del Pokémon
            self.clear_data()
            self.clear_error_message()

            self.number_label.config(text=f"Número: {number}")
            self.name_label.config(text=f"Nombre: {name}")
            self.types_label.config(text=f"Tipos: {', '.join(types)}")
            self.height_label.config(text=f"Altura: {height} m")
            self.weight_label.config(text=f"Peso: {weight} kg")

            # Mostrar la imagen del Pokémon
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

            # Guardar los datos del Pokémon en un archivo JSON
            pokemon_info = {
                "number": number,
                "name": name,
                "types": types,
                "height": height,
                "weight": weight,
                "image_url": image_url
            }
            self.save_to_json(pokemon_info, name.lower())

        # Capturar una excepción si se produce un ValueError
        except ValueError as e:
            self.clear_data()  # Limpiar los datos de la interfaz
            self.show_error_message(str(e))  # Mostrar un mensaje de error

        # Capturar cualquier otra excepción
        except Exception as e:
            self.clear_data()  # Limpiar los datos de la interfaz
            self.show_error_message(str(e))  # Mostrar un mensaje de error

    def clear_data(self):
        # Limpiar los datos del Pokémon en la interfaz
        self.number_label.config(text="")
        self.name_label.config(text="")
        self.types_label.config(text="")
        self.height_label.config(text="")
        self.weight_label.config(text="")
        self.image_label.config(image="")

    def show_error_message(self, message):
        # Mostrar un mensaje de error en la interfaz
        self.error_label.config(text=message)

    def clear_error_message(self):
        # Limpiar el mensaje de error en la interfaz
        self.error_label.config(text="")

    def save_to_json(self, data, filename):
        # Guardar los datos del Pokémon en un archivo JSON
        directory = "pokedex"
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, f"{filename}.json")
        with open(file_path, "w") as file:
            json.dump(data, file)


pokedex_gui = PokedexGUI()
pokedex_gui.run()
