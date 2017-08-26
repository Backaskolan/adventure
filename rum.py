# coding: utf-8
import saker, handlingar, karta

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
    def beskrivning(self):
        return "Vad vill du använda?"

    def mojliga_handlingar(self, spelare):
        mojliga_anvandningar = []
        for sak in spelare.saker:
            if sak.upplockad:
                mojliga_anvandningar.append(handlingar.Anvand(sak))
        mojliga_anvandningar.append(handlingar.Tillbaka(spelare.tidigare_position))
        return mojliga_anvandningar

    def modifiera_spelare(self, spelare):
        pass

class StartRum(Rum):
    def beskrivning(self):
        return """
        En vacker glänta i skogen. 
        Härifrån går det stigar till norr, öster och söder.
        """

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
        self.beskrivning_txt = """
        Här är skogen tät och mörk. Du vågar inte gå vidare.
        Den vackra gläntan ligger norrut.
        """

    def beskrivning(self):
        return self.beskrivning_txt
    def modifiera_spelare(self, spelare):
        pass


class SlutRum(Rum):
    def __init__(self, x, y):
        super().__init__(x, y)

    def beskrivning(self):
        return """
        Skogen öppnar sig och du kliver ut i din egen bakgård. Äntligen hemma!
        """

    def modifiera_spelare(self, spelare):
        spelare.hemma = True

class FicklampaRum(HittaSakRum):
    def __init__(self, x, y):
        super().__init__(x, y, saker.Ficklampa())

    def beskrivning(self):
        if not self.sak.upplockad:
            return """
            En bit in i skogen ligger en gammal FICKLAMPA vid en sten.
            En stig leder söderut.
            """
        else:
            return """
                En sten mitt i skogen. En stig leder söderut.
            """            

class BatteriRum(HittaSakRum):
    def __init__(self, x, y):
        super().__init__(x, y, saker.Batteri())

    def beskrivning(self):
        if not self.sak.upplockad:    
            return """
            Mitt i skogen växer ett stort gammalt träd. I trädets bark sitter det ett BATTERI.
            Stigen leder västerut tillbaka till gläntan.
            """
        else:
            return """
                Mitt i skogen växer ett stort gammalt träd. Det ser ut som det suttit något i barken nyligen.
                Stigen leder västerut tillbaka till gläntan.
            """