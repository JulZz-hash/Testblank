import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
from save_system import save_game, load_game
from npc_interactions import interact_with_npc, NPCS, automatic_npc_actions
from events import generate_random_event
from dynamic_quests import generate_random_quest

def main():
    print("\n🌌 Willkommen zurück in der Galaxis...")

    # Spiel laden oder neu starten
    choice = input("Möchtest du ein neues Spiel starten oder einen Spielstand laden? (neu/laden): ").lower()
    if choice == "laden":
        player, npcs = load_game()
        if not player:
            print("Ein neues Spiel wird gestartet.")
            player = {"species": "Mensch", "credits": 100, "inventory": []}
            npcs = NPCS
    else:
        player = {"species": "Mensch", "credits": 100, "inventory": []}
        npcs = NPCS

    while True:
        # Automatische NPC-Aktionen
        automatic_npc_actions(npcs)

        # Hauptmenü
        print("\nWas möchtest du tun?")
        print("1. Mit einem NPC interagieren")
        print("2. Ein zufälliges Ereignis erleben")
        print("3. Eine Quest starten")
        print("4. Spiel speichern")
        print("5. Spiel beenden")
        choice = input("> ")

        if choice == "1":
            print("\nWähle einen NPC:")
            for npc_name in npcs.keys():
                print(f"- {npc_name}")
            npc_name = input("> ")
            interact_with_npc(npc_name)
        elif choice == "2":
            event = generate_random_event()
            print(f"\n⚡ Ereignis: {event}")
        elif choice == "3":
            quest = generate_random_quest()
            print(f"\n🌀 Quest: {quest['description']}")
            print(f"Belohnung: {quest['reward']} Credits | Schwierigkeit: {quest['difficulty'].capitalize()}")
        elif choice == "4":
            save_game(player, npcs)
        elif choice == "5":
            print("🚀 Möge die Macht mit dir sein. Bis zum nächsten Mal!")
            break
        else:
            print("❌ Ungültige Wahl. Versuch es erneut