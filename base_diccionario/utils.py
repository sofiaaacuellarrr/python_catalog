import json

DB_LOAD = "./base_diccionario/datos.json"


def read_db():
    with open(DB_LOAD, "r", encoding="utf-8") as file:
        saved_dict = json.load(file)

    return saved_dict


def save_db(dictionary):
    with open(DB_LOAD, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, ensure_ascii=False)
        