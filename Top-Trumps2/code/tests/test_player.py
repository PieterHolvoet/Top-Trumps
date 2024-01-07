from pl.player import Player
import pytest

@pytest.fixture
def player_with_deck():
    deck = ['Card1', 'Card2', 'Card3']
    return Player(deck)

def test_aantal_kaarten(player_with_deck):
    assert player_with_deck.aantal_kaarten() == 3

def test_pak_bovenste_kaart(player_with_deck):
    assert player_with_deck.pak_bovenste_kaart() == 'Card1'

def test_kaart_toevoegen_deck(player_with_deck):
    initial_count = player_with_deck.aantal_kaarten()
    player_with_deck.kaart_toevoegen_deck('NewCard')
    assert player_with_deck.aantal_kaarten() == initial_count + 1
    assert 'NewCard' in player_with_deck.deck

def test_kaart_verwijderen_deck(player_with_deck):
    initial_count = player_with_deck.aantal_kaarten()
    card_to_remove = player_with_deck.pak_bovenste_kaart()
    player_with_deck.kaart_verwijderen_deck(card_to_remove)
    assert player_with_deck.aantal_kaarten() == initial_count - 1
    assert card_to_remove not in player_with_deck.deck

def test_bonus_krijgen(player_with_deck):
    bonus_cards = ['BonusCard1', 'BonusCard2']
    initial_count = player_with_deck.aantal_kaarten()
    player_with_deck.bonus_krijgen(bonus_cards)
    assert player_with_deck.aantal_kaarten() == initial_count + len(bonus_cards)
    for card in bonus_cards:
        assert card in player_with_deck.deck


def test_battle_andere_speler_hoger(player_with_deck):
    other_deck = ['Card4', 'Card5', 'Card6']
    other_player = Player(other_deck)

    attr = 2
    bonus = ['BonusCard1', 'BonusCard2']
    bool_hoger_lager = True

    initial_player_deck_size = player_with_deck.aantal_kaarten()
    initial_other_deck_size = other_player.aantal_kaarten()

    result = player_with_deck.battle_andere_speler(other_player, attr, bonus, bool_hoger_lager)

    assert result == 1  # Player should win
    assert player_with_deck.aantal_kaarten() == initial_player_deck_size + 2
    assert other_player.aantal_kaarten() == initial_other_deck_size - 2

def test_battle_andere_speler_lager(player_with_deck):
    other_deck = ['Card4', 'Card5', 'Card6']
    other_player = Player(other_deck)

    attr = 4
    bonus = ['BonusCard1', 'BonusCard2']
    bool_hoger_lager = False

    initial_player_deck_size = player_with_deck.aantal_kaarten()
    initial_other_deck_size = other_player.aantal_kaarten()

    result = player_with_deck.battle_andere_speler(other_player, attr, bonus, bool_hoger_lager)

    assert result == -1  # Computer should win
    assert player_with_deck.aantal_kaarten() == initial_player_deck_size - 2
    assert other_player.aantal_kaarten() == initial_other_deck_size + 2


