from datetime import datetime

from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

AGENDA_EVENT = {
    "1": {
        "event_id": "1",
        "user_id": "1",
        "event_name": "Entrega do Trabalho de BD",
        "event_description": "Entrega do documento do e apresentação.",
        "event_date": "2023-03-16 13:30:00",
        "timestamp": get_timestamp(),
    },
    "2": {
        "event_id": "2",
        "user_id": "1",
        "event_name": "SBGames",
        "event_description": "Evento de jogos onde vou apresentar o 'Coelho Pula-Pula'.",
        "event_date": "2023-04-16 13:30:00",
        "timestamp": get_timestamp(),
    },
    "3": {
        "event_id": "3",
        "user_id": "1",
        "event_name": "Dentista",
        "event_description": "Consulta no posto lá do São Raimundo.",
        "event_date": "2023-05-16 13:30:00",
        "timestamp": get_timestamp(),
    },
    "4": {
        "event_id": "4",
        "user_id": "2",
        "event_name": "Dia de limpar a casa",
        "event_description": "Arrumar a sala e a cozinha.",
        "event_date": "2023-03-16 13:30:00",
        "timestamp": get_timestamp(),
    },
    "5": {
        "event_id": "5",
        "user_id": "2",
        "event_name": "Partida de futebol",
        "event_description": "Partida depois da aula na rua atrás de casa.",
        "event_date": "2023-04-16 13:30:00",
        "timestamp": get_timestamp(),
    },
    "6": {
        "event_id": "6",
        "user_id": "2",
        "event_name": "Profa final",
        "event_description": "Final de redes, vai cair a camada de enlace.",
        "event_date": "2023-05-16 13:30:00",
        "timestamp": get_timestamp(),
    },
    "7": {
        "event_id": "7",
        "user_id": "3",
        "event_name": "Apresentação no teatro",
        "event_description": "O coral jovem vai cantar Halo no teatro, não posso perder kkk.",
        "event_date": "2023-03-16 13:30:00",
        "timestamp": get_timestamp(),
    },
    "8": {
        "event_id": "8",
        "user_id": "3",
        "event_name": "Aula de piano",
        "event_description": "Vamos aprender a transpor escalas, não posso esquecer a partitura.",
        "event_date": "2023-04-16 13:30:00",
        "timestamp": get_timestamp(),
    },
    "9": {
        "event_id": "9",
        "user_id": "3",
        "event_name": "Episódio final de TLFU",
        "event_description": "Vou assistir na casa da Fernanda.",
        "event_date": "2023-05-16 13:30:00",
        "timestamp": get_timestamp(),
    },
}

def read_all():
    return list(AGENDA_EVENT.values())

def create(event):
    event_id = event.get("event_id")
    user_id = event.get("user_id")
    event_name = event.get("event_name")
    event_description = event.get("event_description")
    event_date = event.get("event_date")
    timestamp = get_timestamp()

    if event_id and event_id not in AGENDA_EVENT:
        AGENDA_EVENT[event_id] = {
            "event_id": event_id,
            "user_id": user_id,
            "event_name": event_name,
            "event_description": event_description,
            "event_date": event_date,
            "timestamp": timestamp,
        }
        return AGENDA_EVENT[event_id], 201
    else:
        abort(404, f"Event with the title '{event_name}' already exists")

def read_one(event_id):
    if event_id in AGENDA_EVENT:
        return AGENDA_EVENT[event_id]
    else:
        abort(404, f"Event not found :(")

def update(event_id, event):
    if event_id in AGENDA_EVENT:
        AGENDA_EVENT[event_id]["event_name"] = event.get("event_name", AGENDA_EVENT[event_id]["event_name"])
        AGENDA_EVENT[event_id]["user_description"] = event.get("event_description", AGENDA_EVENT[event_id]["event_description"])
        AGENDA_EVENT[event_id]["user_date"] = event.get("event_date", AGENDA_EVENT[event_id]["event_date"])
        AGENDA_EVENT[event_id]["timestamp"] = get_timestamp()
        return AGENDA_EVENT[event_id]
    else:
        abort(404, f"Event not found :(")

def delete(event_id):
    if event_id in AGENDA_EVENT:
        event_name = AGENDA_EVENT[event_id]["event_name"]
        del AGENDA_EVENT[event_id]
        return make_response(f"Event with title '{event_name}' successfully deleted.", 200)
    else:
        abort(404, f"User not found:(")