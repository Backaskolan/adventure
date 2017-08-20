# coding: utf-8
from spelare import Spelare

class Handling():
    def __init__(self, metod, namn, snabbkommando, **kwargs):
        self.metod = metod
        self.namn = namn
        self.snabbkommando = snabbkommando
        self.kwargs = kwargs

    def __str__(self):
        return "| {} | {}".format(self.snabbkommando, self.namn)

class FlyttaNorr(Handling):
    def __init__(self):
        super().__init__(metod=Spelare.flytta_norr, namn="Gå norrut", snabbkommando="n")

class FlyttaSoder(Handling):
    def __init__(self):
        super().__init__(metod=Spelare.flytta_soder, namn="Gå söderut", snabbkommando="s")

class FlyttaOst(Handling):
    def __init__(self):
        super().__init__(metod=Spelare.flytta_ost, namn="Gå österut", snabbkommando="o")

class FlyttaVast(Handling):
    def __init__(self):
        super().__init__(metod=Spelare.flytta_vast, namn="Gå västerut", snabbkommando="v")

class VisaSaker(Handling):
    def __init__(self):
        super().__init__(metod=Spelare.visa_saker, namn="Visa dina saker", snabbkommando="i")

class PlockaUpp(Handling):
    def __init__(self, sak):
        super().__init__(metod=Spelare.plocka_upp, namn="Plocka upp {}".format(sak.namn), snabbkommando="p", sak=sak)

class Anvand(Handling):
    def __init__(self, sak):
        super().__init__(metod=Spelare.anvand, namn="Använd {}".format(sak.namn), snabbkommando="{}".format(sak.namn[0].lower()), sak=sak)

class Tillbaka(Handling):
    def __init__(self, rum):
        super().__init__(metod=Spelare.tillbaka, namn="Tillbaka", snabbkommando="t")

class Avsluta(Handling):
    def __init__(self):
        super().__init__(metod=Spelare.avsluta, namn="Avsluta", snabbkommando="q")