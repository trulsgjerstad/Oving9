from __future__ import annotations

import re
from pathlib import Path

class MultipleChoise:

    def __init__(self, question, alternatives, answer):
        self.question = question
        self.answer = alternatives[answer]
        self.alternatives = alternatives
        
    def __repr__(self) -> str:
        return f"<MultipleChoise {self.question}>"

    def __str__(self):
        return f"{self.question}\n" + "\n".join(
            [
                f"    {index + 1}: {alternative}"
                for index, alternative in enumerate(self.alternatives)
            ]
        )

    def sjekk_svar(self, answer):
        if answer is None or answer == "" or int(answer) < 1 or int(answer) > len(self.alternatives):
            print(f"{answer} er ikke gyldig!")
            return False

        return self.answer == (self.alternatives[int(answer) -1])

#print(question.sjekk_svar(input(question)))

liste = [
    MultipleChoise(
        question="Den delen av en datamaskin som kjører programmet kalles?",
        alternatives=["RAM", "Harddisk", "CPU", "Sekundærlager"],
        answer=2
    ),
    MultipleChoise(
        question="En ___ er nok minne til å lagre en bokstav eller et lite heltall",
        alternatives=["bit", "byte", "bryter", "transistor"],
        answer=1
    ),
]

"""for element in liste:
    def ask_qestion():
        print(f"{element}\n")
        answer = input("Svar: ")
        if element.sjekk_svar(answer):
            print("RIKTIG!\n")
        else:
            print("FEIL!\n")
            ask_qestion()
    ask_qestion()"""
