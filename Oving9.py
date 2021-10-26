from Oving8b import MultipleChoise


class Spiller:

    def __init__(self, navn):
        self.navn = navn
        self.korrekte_svar = 0

    def riktig_svar(self):
        self.korrekte_svar += 1

extra = [
    ["Slutter dagen i dag på 'g'", 0, ["Ja", "Nei"]]
]

def less_fil():
    Sporsmaal: list[MultipleChoise] = []
    with open("sporsmaalsfil.txt", encoding="utf-8") as f:
        for line in f.readlines():
            TreDeler = line.split(":")
            sporsmaal = TreDeler[0].strip() 
            fasit = int(TreDeler[1].strip())
            alternativ = TreDeler[2].strip()[1:-1].split(", ") 
            Sporsmaal.append(
                MultipleChoise(
                    sporsmaal,
                    alternativ,
                    fasit
                )
            )
    for sporsmaal in extra:
        [sporsmaal, fasit, alternativ] = sporsmaal
        Sporsmaal.append(
            MultipleChoise(
                    sporsmaal,
                    alternativ,
                    int(fasit)
                )
            )
    return Sporsmaal




if __name__ == "__main__":
    spillere = (
        Spiller(input("Navn på spiller 1: ")),
        Spiller(input("Navn på spiller 2: ")),
        )
    
    for sporsmaal in less_fil():
        print(f"\n\n{sporsmaal}")
        spiller_svar = {}
        for spiller in spillere:
            spiller_svar[spiller.navn] = sporsmaal.sjekk_svar(input(f"Velg et svaralternativ for {spiller.navn}: "))
            if spiller_svar[spiller.navn]:
                spiller.riktig_svar()
        print(f"\nKorrekt svar: {sporsmaal.answer}\n")
        for spiller in spillere:
            print(f"{spiller.navn}: {'Korrekt' if spiller_svar[spiller.navn] else 'Feil'}")

    for spiller in spillere:
        print(f"\nSpiller {spiller.navn} hadde {spiller.korrekte_svar} riktig(e) svar")



