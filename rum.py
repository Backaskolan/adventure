# coding: utf-8
import saker, handlingar, karta
clear_screen = "\033[H\033[J"

class Rum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def beskrivning(self):
        raise NotImplementedError()

    def modifiera_spelare(self, spelare):
        raise NotImplementedError()

    def mojliga_flyttar(self):
        flyttar = []
        if karta.rum_finns(self.x, self.y - 1):
            flyttar.append(handlingar.FlyttaNorr())
        if karta.rum_finns(self.x, self.y + 1):
            flyttar.append(handlingar.FlyttaSoder())
        if karta.rum_finns(self.x + 1, self.y):
            flyttar.append(handlingar.FlyttaOst())
        if karta.rum_finns(self.x - 1, self.y):
            flyttar.append(handlingar.FlyttaVast())
        
        return flyttar

    def mojliga_handlingar(self):
        mojliga_handlingar = self.mojliga_flyttar()
        mojliga_handlingar.append(handlingar.VisaSaker())
        mojliga_handlingar.append(handlingar.Avsluta())
        return mojliga_handlingar

class AnvandRum(Rum):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.beskrivning_text = clear_screen + '\n| Saker att använda:\n'
        super().__init__(x, y)

    def beskrivning(self):
        return self.beskrivning_text

    def mojliga_handlingar(self, spelare):
        mojliga_anvandningar = []
        if len(spelare.saker) == 0:
            print('(Du har inga saker.)\n')
        else:
            for sak in spelare.saker:
                if sak.upplockad:
                    mojliga_anvandningar.append(handlingar.Anvand(sak))
        
        mojliga_anvandningar.append(handlingar.Tillbaka(spelare.tidigare_position))
        return mojliga_anvandningar

    def modifiera_spelare(self, spelare):
        pass

class StartRum(Rum):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.beskrivning_text = clear_screen + '\n| GLÄNTA' '\n| En vacker glänta mitt i skogen.' '\n| Fåglar sjunger och solen strålar genom löven.\n'
        super().__init__(x, y)
    
    def beskrivning(self):
        return self.beskrivning_text

    def modifiera_spelare(self, spelare):
        #Här händer inget med spelaren
        pass

class HittaSakRum(Rum):
    def __init__(self, x, y, sak):
        self.sak = sak
        super().__init__(x, y)

    def modifiera_spelare(self, spelare):
        pass

    def mojliga_handlingar(self):
        mojliga_handlingar = super().mojliga_handlingar()
        if not self.sak.upplockad:
            mojliga_handlingar.insert(0, handlingar.PlockaUpp(self.sak))
            return mojliga_handlingar
        else:
            return mojliga_handlingar

class MorktRum(Rum):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.beskrivning_text = clear_screen +'\n| MÖRKA SKOGEN' '\n| Här är skogen tät och mörk. Du vågar inte gå vidare.\n'

    def beskrivning(self):
        return self.beskrivning_text
    def modifiera_spelare(self, spelare):
        pass


class SlutRum(Rum):
    def __init__(self, x, y):
        self.beskrivning_text = clear_screen + '\n| HEMMA!' '\n| Skogen öppnar sig och du kliver ut i din egen bakgård.\n'
        super().__init__(x, y)

    def beskrivning(self):
        return self.beskrivning_text

    def modifiera_spelare(self, spelare):
        spelare.hemma = True

class FicklampaRum(HittaSakRum):
    def __init__(self, x, y):
        super().__init__(x, y, saker.Ficklampa())

    def beskrivning(self):
        if not self.sak.upplockad:
            self.beskrivning_text = clear_screen + '\n| SKOGEN' '\n| En bit in i skogen ligger en gammal FICKLAMPA vid en sten.\n'
        else:
            self.beskrivning_text = clear_screen + '\n| SKOGEN' '\n| En sten mitt i skogen.\n'
        return self.beskrivning_text

class BatteriRum(HittaSakRum):
    def __init__(self, x, y):
        super().__init__(x, y, saker.Batteri())

    def beskrivning(self):
        if not self.sak.upplockad:    
            return clear_screen + '\n| SKOGEN' '\n| Mitt i skogen växer ett stort gammalt träd.' '\n| I trädets bark sitter det ett BATTERI.\n'
        else:
            return clear_screen + '\n| SKOGEN' '\n| Mitt i skogen växer ett stort gammalt träd.' '\n| Det ser ut som det suttit något i barken nyligen.\n'