# Pokédex
Programa para realizar consultas ya sea de numero o nombre correspondientes a Pokemones para visualizar sus datos principales.

Al abrir el programa nos despliegara una ventana completa en la cual tendremos una barra para ingresar datos y dos botones, uno para realizar la consulta con el contenido de la barra donde ingresaremos los datos y por ultimo un boton de salida para cerrar el programa.

Cuando se realiza una consulta en el programa se resguarda en una carpeta aparte llamada Pokedex archivos .JSON con los datos de la consulta realizada.

Para la ejecución del programa se requiere la instalacion de las bibliotecas tkinter, requests y PIL.


Proceso del programa y aprendizaje obtenido en este módulo.

El programa de la Pokédex fue realizado en el siguiente orden: Asignamos la clase PokedexApi de la cual obtendremos tanto los datos desde la página "https://pokeapi.co/api/v2/pokemon" como la verificación correspondiente a si el usuario ingresó ya sea un número o un nombre de pokémon para obtener los datos de pokémon como su número, nombre, tipos, altura y peso, al igual que al realizarse una consulta se resguardarán dichos datos como un archivo .json. Seguimos con la clase PokedexGUI iniciando con hacer que el programa se despliegue en pantalla completa y con ello hacemos la creación tanto del marco principal, titulo y botones mostrados en la interfaz para realizar dichas consultas, etiquetas para desplegar los datos en el orden solicitado, asignamos un botón de salida, creamos la instancia de la clase PokedexAPI y el bucle para realizar un numero finito de consultas controlado por el usuario, no olvidando que también asignamos la limpieza de los datos entre consultas para evitar visualizar el mensaje en futuras consultas disponibles. Declaramos los datos que se resguardaran como .json, las limpiezas entre mensajes de error y la ejecución como tal del programa.
En este módulo aprendí muchas cosas nuevas en este lenguaje de programación entre ellas lo principal seria el uso de distintas bibliotecas, la consulta de datos incluyendo imágenes como tal mediante una página externa, la validación de datos para evitar mal funcionamiento del programa, asignar una interfaz un tanto más amigable con el usuario, el resguardo de datos en la ejecución de un programa hacia una carpeta con archivos en terminación .json y principalmente el poder jugar con mi código con la elección de un tema el cual me trae muchos recuerdos de mi infancia.
