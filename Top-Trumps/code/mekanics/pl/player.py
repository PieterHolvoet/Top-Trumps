class Player:
    def __init__(self, deck):
        self.deck = deck

    def aantal_kaarten(self):
        return len(self.deck)

    def pak_bovenste_kaart(self):
        kaart = self.deck[0]
        return kaart

    def kaart_toevoegen_deck(self, kaart):
        self.deck.append(kaart)
        return

    def kaart_verwijderen_deck(self, kaart):
        self.deck.remove(kaart)
        return

    def bonus_krijgen(self, kaarten):
        for kaart in kaarten:
            self.kaart_toevoegen_deck(kaart)

    def battle_andere_speler(self, other, attr, bonus, bool_hoger_lager):
        eigen_kaart, andere_kaart = self.pak_bovenste_kaart(), other.pak_bovenste_kaart()
        if bool_hoger_lager:
            if eigen_kaart.isgroter(andere_kaart, attr):
                self.kaart_verwijderen_deck(eigen_kaart)
                self.kaart_toevoegen_deck(eigen_kaart)
                self.kaart_toevoegen_deck(andere_kaart)
                other.kaart_verwijderen_deck(andere_kaart)
                self.bonus_krijgen(bonus)
                print("Player is gewonnen")
                print(f"PlayerRes: {len(self.deck)}     ComRes:{len(other.deck)}")
                return 1
            else:
                self.kaart_verwijderen_deck(eigen_kaart)
                other.kaart_verwijderen_deck(andere_kaart)
                other.kaart_toevoegen_deck(andere_kaart)
                other.kaart_toevoegen_deck(eigen_kaart)
                other.bonus_krijgen(bonus)
                print("Com is gewonnen")
                print(f"PlayerRes: {len(self.deck)}     ComRes:{len(other.deck)}")
                return -1
        else:
            if eigen_kaart.isgroter(andere_kaart, attr):
                self.kaart_verwijderen_deck(eigen_kaart)
                other.kaart_verwijderen_deck(andere_kaart)
                other.kaart_toevoegen_deck(andere_kaart)
                other.kaart_toevoegen_deck(eigen_kaart)
                other.bonus_krijgen(bonus)
                print("Com is gewonnen")
                print(f"PlayerRes: {len(self.deck)}     ComRes:{len(other.deck)}")
                return -1
            else:
                self.kaart_verwijderen_deck(eigen_kaart)
                self.kaart_toevoegen_deck(eigen_kaart)
                self.kaart_toevoegen_deck(andere_kaart)
                other.kaart_verwijderen_deck(andere_kaart)
                self.bonus_krijgen(bonus)
                print("Player is gewonnen")
                print(f"PlayerRes: {len(self.deck)}     ComRes:{len(other.deck)}")
                return 1

    def is_niet_einde(self, other):
        if self.deck and other.deck:
            return True
        else:
            return False
