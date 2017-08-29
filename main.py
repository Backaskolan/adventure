#!/usr/bin/env python3
# coding: utf-8
import karta
from spelare import Spelare

def spela():
    karta.ladda_rum()
    spelare = Spelare()
    while not spelare.hemma:
        rum = karta.rum_finns(spelare.position_x, spelare.position_y)
        print(rum.beskrivning())
        rum.modifiera_spelare(spelare)
        if not spelare.hemma:
            if rum.x == 3:
                mojliga_handlingar = rum.mojliga_handlingar(spelare)
            else:
                mojliga_handlingar = rum.mojliga_handlingar()
            for handling in mojliga_handlingar:
                print(handling)
            handling_input = input("\nVad vill du göra? ")
            for handling in mojliga_handlingar:
                if handling_input == handling.snabbkommando:
                    spelare.utfor_handling(handling, **handling.kwargs)
                    break

if __name__ == "__main__":
    spela()