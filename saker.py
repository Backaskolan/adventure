# coding: utf-8
class Sak:
    def __init__(self, namn, beskrivning):
        self.namn = namn
        self.beskrivning = beskrivning

    def __str__(self):
        return "{}:\n {}".format(self.namn, self.beskrivning)

class Inventarie(Sak):
    def __init__(self, namn, beskrivning, anvandning, upplockad):
        self.anvandning = anvandning
        self.upplockad = upplockad
        super().__init__(namn, beskrivning)

class Ficklampa(Inventarie):
    def __init__(self):
        super().__init__(
            namn = "Ficklampa",
            beskrivning = "En rostig ficklampa. Den känns lätt.",
            anvandning = "Den fungerar inte. Den verkar sakna ett batteri.",
            upplockad = False)

class Batteri(Inventarie):
    def __init__(self):
        super().__init__(
            namn = "Batteri",
            beskrivning = "Ett batteri. Verkar passa i en ficklampa...",
            anvandning = "Du har inget att använda det med.",
            upplockad = False)

class FicklampaMedBatteri(Inventarie):
    def __init__(self):
        super().__init__(
            namn="Ficklampa med batteri",
            beskrivning="En ficklampa. Lite sliten men i övrigt verkar den helt okej.",
            anvandning="Den fungerar! Nu kan du se var du går.",
            upplockad = True)