import pymongo
import json

# Conexión a la base de datos
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Proyecto-MongoDB-Anime"]
collection = db["anime"]

# Cargar datos desde el archivo JSON
with open('C:\Users\Dani\Desktop\1-ASIR\BBDD\Proyecto-MongoDB-main\data.json', 'r') as file:
    data = json.load(file)
    collection.insert_many(data)  # Insertar datos en MongoDB

def insertar_anime():
    print("\nINSERTAR ANIME")
    studio = input("Estudio: ")
    genres = input("Géneros (separados por comas): ").split(", ")
    description = input("Descripción: ")
    title = input("Título: ")
    start_date = input("Fecha de inicio (formato: MMM D, YYYY, HH:MM (JST)): ")

    anime = {
        "studio": studio,
        "genres": genres,
        "description": description,
        "title": {"text": title},
        "start_date": start_date
    }

    collection.insert_one(anime)
    print("Anime insertado correctamente.")

def eliminar_anime():
    print("\nELIMINAR ANIME")
    title = input("Introduce el título del anime que deseas eliminar: ")
    result = collection.delete_one({"title.text": title})
    if result.deleted_count > 0:
        print("Anime eliminado correctamente.")
    else:
        print("El anime no se encontró.")

def modificar_anime():
    print("\nMODIFICAR ANIME")
    title = input("Introduce el título del anime que deseas modificar: ")
    new_title = input("Nuevo título (dejar en blanco si no se desea modificar): ")
    new_description = input("Nueva descripción (dejar en blanco si no se desea modificar): ")

    update_fields = {}
    if new_title:
        update_fields["title.text"] = new_title
    if new_description:
        update_fields["description"] = new_description

    if update_fields:
        collection.update_one({"title.text": title}, {"$set": update_fields})
        print("Anime modificado correctamente.")
    else:
        print("No se realizaron modificaciones.")

def consultar_anime():
    print("\nCONSULTAR ANIME")
    title = input("Introduce el título del anime que deseas consultar: ")
    anime = collection.find_one({"title.text": title})
    if anime:
        print("Información del anime:")
        print("Título:", anime["title"]["text"])
        print("Estudio:", anime["studio"])
        print("Descripción:", anime["description"])
        print("Fecha de inicio:", anime["start_date"])
        print("Géneros:", ", ".join(anime["genres"]))
    else:
        print("El anime no se encontró.")