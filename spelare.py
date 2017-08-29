# coding: utf-8
import saker, karta, rum

class Spelare():
    def __init__(self):
        self.tidigare_position = ()
        self.saker = []
        self.position_x, self.position_y = karta.startposition
        self.hemma = False

    def utfor_handling(self, handling, **kwargs):
        handling_metod = getattr(self, handling.metod.__name__)
        if handling_metod:
            handling_metod(**kwargs)

    def plocka_upp(self, sak):
        self.saker.append(sak)
        sak.upplockad = True
        print(rum.clear_screen + '\n| Plockade upp {}'.format(sak.namn))

    def visa_saker(self):
        # if len(self.saker) == 0:
        #     print("Du har inga saker.")
        # else:
        #     # for sak in self.saker:
        #     #     print(sak, '\n')
        self.tidigare_position = (self.position_x, self.position_y)
        self.position_x = 3
        self.position_y = 0

    def tillbaka(self):
        self.position_x = self.tidigare_position[0]
        self.position_y = self.tidigare_position[1]

    def anvand(self, sak):
        if sak.namn == "Batteri":
            for inventarie in self.saker:
                if inventarie.namn == "Ficklampa":
                    sak.anvandning = "Du stoppar in batteriet i ficklampan. Det passar perfekt."
                    self.saker.clear()
                    self.saker.append(saker.FicklampaMedBatteri())
        elif sak.namn == "Ficklampa med batteri" and self.tidigare_position == (1, 2):
            sak.anvandning = "\n| Du tänder ficklampan och låter strålen lysa upp den mörka skogen."
            karta.rum_finns(1, 2).beskrivning_text = rum.clear_screen + '\n| MÖRKA SKOGEN' '\n| Du lyser med ficklampan genom mörkret och ser en stig som leder västerut.\n'
            karta._karta[(0, 2)] = rum.SlutRum(0, 2)
        print("""{}""".format(sak.anvandning))

    def flytta(self, dx, dy):
        self.position_x += dx
        self.position_y += dy
        #print(karta.rum_finns(self.position_x, self.position_y).beskrivning())

    def flytta_norr(self):
        self.flytta(dx=0, dy=-1)

    def flytta_soder(self):
        self.flytta(dx=0, dy=1)

    def flytta_ost(self):
        self.flytta(dx=1, dy=0)

    def flytta_vast(self):
        self.flytta(dx=-1, dy=0)

    def avsluta(self):
        print("\n| Tack för att du spelade!")
        exit()