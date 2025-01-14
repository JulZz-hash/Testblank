import streamlit as st
# Globale Variablen für den aktuellen Spielstatus
if "player" not in st.session_state:
    st.session_state["player"] = {"species": "Mensch", "credits": 100, "inventory": []}
if "npcs" not in st.session_state:
    st.session_state["npcs"] = NPCS

# Seitenkopf
st.title("🌌 Star Wars Story Game")
st.sidebar.header("Spieloptionen")

# Spiel laden oder neu starten
if st.sidebar.button("Spielstand laden"):
    player, npcs = load_game()
    if player:
        st.session_state["player"] = player
        st.session_state["npcs"] = npcs
        st.success("💾 Spielstand erfolgreich geladen!")
    else:
        st.warning("❌ Kein gespeicherter Spielstand gefunden.")
if st.sidebar.button("Spiel speichern"):
    save_game(st.session_state["player"], st.session_state["npcs"])
    st.success("💾 Spiel gespeichert!")

# Automatische NPC-Aktionen
automatic_npc_actions(st.session_state["npcs"])

# Hauptmenü
st.header("🌀 Was möchtest du tun?")
options = [
    "Mit einem NPC interagieren",
    "Ein zufälliges Ereignis erleben",
    "Eine Quest starten",
]
choice = st.radio("Wähle eine Aktion:", options)

if choice == "Mit einem NPC interagieren":
    npc_name = st.selectbox("Wähle einen NPC:", list(st.session_state["npcs"].keys()))
    if st.button("Interagieren"):
        interact_with_npc(npc_name)

elif choice == "Ein zufälliges Ereignis erleben":
    if st.button("Ereignis generieren"):
        event = generate_random_event()
        st.write(f"⚡ **Ereignis:** {event}")

elif choice == "Eine Quest starten":
    if st.button("Quest generieren"):
        quest = generate_random_quest()
        st.write(f"🌀 **Quest:** {quest['description']}")
        st.write(f"**Belohnung:** {quest['reward']} Credits | **Schwierigkeit:** {quest['difficulty'].capitalize()}")

# Spielerstatus anzeigen
st.sidebar.subheader("Spielerstatus")
st.sidebar.write(f"**Spezies:** {st.session_state['player']['species']}")
st.sidebar.write(f"**Credits:** {st.session_state['player']['credits']}")
st.sidebar.write(f"**Inventar:** {', '.join(st.session_state['player']['inventory']) if st.session_state['player']['inventory'] else 'Leer'}")

NPCS = {
    "Jabba the Hutt": {"relationship": 0, "greeting": "Ho ho ho! Was willst du von Jabba?"},
    "Imperialer Offizier": {"relationship": 0, "greeting": "Was führt dich hierher, Bürger?"},
    "Schmuggler-Kapitän": {"relationship": 0, "greeting": "Was kann ich für dich tun, Freund?"},
}

def adjust_relationship(npc_name, amount):
    """Ändert den Beziehungsstatus eines NPCs."""
    if npc_name in NPCS:
        NPCS[npc_name]["relationship"] += amount
        return f"🔄 Beziehung zu {npc_name} verändert: {NPCS[npc_name]['relationship']}"
    return "❌ NPC nicht gefunden."

def interact_with_npc(npc_name):
    """Interagiere mit einem NPC und wähle eine Dialogoption."""
    if npc_name not in NPCS:
        return "❌ Dieser NPC existiert nicht."

    npc = NPCS[npc_name]
    result = [f"💬 **{npc_name}:** {npc['greeting']}", f"Beziehungsstatus: {npc['relationship']}"]
    options = {
        "Höflich sein (+10 Beziehung)": 10,
        "Fordernd sein (-10 Beziehung)": -10,
        "Angriff (-50 Beziehung)": -50,
    }
    selected_action = st.radio("Wähle eine Aktion:", list(options.keys()))
    if st.button("Bestätigen"):
        change = options[selected_action]
        result.append(adjust_relationship(npc_name, change))
    return "\n".join(result)

def automatic_npc_actions(npcs):
    """Automatische Aktionen der NPCs basierend auf ihrer Beziehung."""
    for npc_name, npc_data in npcs.items():
        if npc_data["relationship"] < -30:
            st.sidebar.warning(f"⚠️ {npc_name} hat negative Absichten!")
        elif npc_data["relationship"] > 50:
            st.sidebar.success(f"✨ {npc_name} bietet dir Hilfe an!")
            
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

def load_game():
    """Lädt den gespeicherten Spielstatus."""
    try:
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)
            return data["player"], data["npcs"]
    except FileNotFoundError:
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

