#!/usr/bin/env python3

from random import randint
from hermes_python.hermes import Hermes

def greet (hermes, message):
    sentences = [
        "Schön, dass du da bist.",
        "Ich habe mich schon gefragt, wo du bleibst.",
        "Willkommen zurück",
        "Ich grüße dich",
        "Ich hoffe, du hattest Spaß",
        "Toll! Erzähl mir von deinem Tag!",
        "Ich habe hier auf dich gewartet",
        "Ich bin froh, dass du wieder zurück bist."
        ]

    generated_int = randint(0, len(sentences)-1)
    msg = sentences[generated_int]

    hermes.publish_end_session(message.session_id, msg)

with Hermes("localhost:1883") as h:
    h \
        .subscribe_intent("tierlord:Heimkommen", greet) \
        .start()