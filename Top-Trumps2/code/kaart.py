import csv
import os

class Kaart:
    def __init__(self, naam, attr_list):
        self.naam = naam
        self.attr_list = attr_list

    def isgelijk(self, other, attr):
        if attr == 1:
            return self.attr_list[0] == other.attr_list[0]
        elif attr == 2:
            return self.attr_list[1] == other.attr_list[1]
        elif attr == 3:
            return self.attr_list[2] == other.attr_list[2]
        elif attr == 4:
            return self.attr_list[3] == other.attr_list[3]

    def isgroter(self, other, attr):
        if attr == 1:
            return self.attr_list[0] > other.attr_list[0]
        elif attr == 2:
            return self.attr_list[1] > other.attr_list[1]
        elif attr == 3:
            return self.attr_list[2] > other.attr_list[2]
        elif attr == 4:
            return self.attr_list[3] > other.attr_list[3]


# Is niet meer nodig wegens uit database halen.     (maar was simpel en beter om hier te doen, klein algoritme)
# PS:: Moet nog gefixt worden
#
path_dierencsv = os.path.join("Top-Trumps2", "assets", "Dieren_TopTrumps.csv")
path_dierencsv_V2 = "../assets/Dieren_TopTrumps.csv"

DECK_DIEREN_CSV = []
with open(path_dierencsv_V2, 'r') as csv_bestand:
    csv_lezer = csv.reader(csv_bestand)
    header = next(csv_lezer)
    attr1, attr2, attr3, attr4 = header[1], header[2], header[3], header[4]
    for rij in csv_lezer:
        attr_lijst = [float(rij[1]), float(rij[2]), float(rij[3]), float(rij[4])]
        dier = Kaart(rij[0], attr_lijst)
        DECK_DIEREN_CSV.append(dier)

sorted_attr1 = []
sorted_attr2 = []
sorted_attr3 = []
sorted_attr4 = []

for kaart in DECK_DIEREN_CSV:
    sorted_attr1.append(kaart.attr_list[0])
    sorted_attr2.append(kaart.attr_list[1])
    sorted_attr3.append(kaart.attr_list[2])
    sorted_attr4.append(kaart.attr_list[3])
sorted_attr1 = sorted(sorted_attr1)
sorted_attr2 = sorted(sorted_attr2)
sorted_attr3 = sorted(sorted_attr3)
sorted_attr4 = sorted(sorted_attr4)


def rank_kaart_attr(kaart, hoger_lager):
    waarde1, waarde2, waarde3, waarde4 = kaart.attr_list[0], kaart.attr_list[1], kaart.attr_list[2], kaart.attr_list[3]
    rank1 = sorted_attr1.index(waarde1)
    rank2 = sorted_attr2.index(waarde2)
    rank3 = sorted_attr3.index(waarde3)
    rank4 = sorted_attr4.index(waarde4)
    rank_list = [rank1, rank2, rank3, rank4]
    if hoger_lager:  # True==Hoger
        wanted_rank = max(rank_list)
    else:
        wanted_rank = min(rank_list)
    return rank_list.index(wanted_rank) + 1
