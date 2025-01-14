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
            
            NPCS = {
    "Jabba the Hutt": {"relationship": 0, "greeting": "Ho ho ho! Was willst du von Jabba?"},
    "Imperialer Offizier": {"relationship": 0, "greeting": "Was führt dich hierher, Bürger?"},
    "Schmuggler-Kapitän": {"relationship": 0, "greeting": "Was kann ich für dich tun, Freund?"},
}

def adjust_relationship(npc_name, amount):
    """Ändert den Beziehungsstatus eines NPCs."""
    if npc_name in NPCS:
        NPCS[npc_name]["relationship"] += amount
        print(f"🔄 Beziehung zu {npc_name} verändert: {NPCS[npc_name]['relationship']}")
    else:
        print("❌ NPC nicht gefunden.")

def interact_with_npc(npc_name):
    """Interagiere mit einem NPC und wähle eine Dialogoption."""
    if npc_name not in NPCS:
        print("❌ Dieser NPC existiert nicht.")
        return

    npc = NPCS[npc_name]
    print(f"\n💬 {npc_name}: {npc['greeting']}")
    print("Beziehungsstatus:", npc["relationship"])
    print("\nWähle eine Aktion:")
    print("1. Höflich sein (+10 Beziehung)")
    print("2. Fordernd sein (-10 Beziehung)")
    print("3. Angriff (-50 Beziehung)")

    choice = input("> ")
    if choice == "1":
        adjust_relationship(npc_name, 10)
        print(f"{npc_name} lächelt zufrieden.")
    elif choice == "2":
        adjust_relationship(npc_name, -10)
        print(f"{npc_name} schaut dich misstrauisch an.")
    elif choice == "3":
        adjust_relationship(npc_name, -50)
        print(f"{npc_name} ist jetzt feindlich gesinnt!")
    else:
        print("❌ Ungültige Wahl.")

def automatic_npc_actions(npcs):
    """Automatische Aktionen der NPCs basierend auf ihrer Beziehung."""
    for npc_name, npc_data in npcs.items():
        if npc_data["relationship"] < -30:
            print(f"⚠️ {npc_name} hat negative Absichten. Er plant etwas gegen dich!")
        elif npc_data["relationship"] > 50:
            print(f"✨ {npc_name} bietet dir Hilfe oder Belohnungen an.")
            
            import json

SAVE_FILE = "savegame.json"

def save_game(player, npcs):
    """Speichert den aktuellen Spielstatus."""
    data = {
        "player": player,
        "npcs": npcs
    }
    with open(SAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print("💾 Spiel gespeichert!")

def load_game():
    """Lädt den gespeicherten Spielstatus."""
    try:
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)
            print("💾 Spielstand geladen!")
            return data["player"], data["npcs"]
    except FileNotFoundError:
        print("❌ Kein gespeicherter Spielstand gefunden.")
        return None, None
        
        import random

ACTORS = ["ein Sith-Lord", "eine Jedi-Meisterin", "ein Kopfgeldjäger", "eine imperiale Wache", "ein Droidenhändler"]
ACTIONS = ["greift dich an", "bittet um Hilfe", "verkauft dir seltene Gegenstände", "enthüllt dir geheime Informationen", "stellt dir eine Falle"]
LOCATIONS = ["in einer verlassenen Raumstation", "auf einem belebten Marktplatz", "in den dunklen Gassen von Coruscant", "in einer Cantina", "in einer geheimen Basis"]

def generate_random_event():
    """Erstellt ein zufälliges Ereignis basierend auf modularen Bausteinen."""
    actor = random.choice(ACTORS)
    action = random.choice(ACTIONS)
    location = random.choice(LOCATIONS)
    return f"{actor} {action} {location}."
    
    import random

QUEST_OBJECTIVES = ["eine Geisel retten", "einen gestohlenen Droiden finden", "einen Sith-Lord besiegen", "einen Schmuggelauftrag durchführen"]
LOCATIONS = ["auf Tatooine", "in einer Cantina auf Coruscant", "in einer alten Jedi-Ruine", "auf einem imperialen Sternzerstörer"]
REWARDS = [100, 200, 300, 500]
DIFFICULTY = ["einfach", "mittel", "schwer", "extrem"]

def generate_random_quest():
    """Erstellt eine zufällige Quest."""
    objective = random.choice(QUEST_OBJECTIVES)
    location = random.choice(LOCATIONS)
    reward = random.choice(REWARDS)
    difficulty = random.choice(DIFFICULTY)
    return {
        "description": f"{objective} {location}.",
        "reward": reward,
        "difficulty": difficulty
    }