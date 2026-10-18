
import random
import streamlit as st
import moteur
from pathlib import Path
import base64

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Spanish Conjugation Trainer",
    page_icon="🇪🇸",
    layout="centered",
    initial_sidebar_state="expanded",
)

COLORS = {
    "background": "#F7F2E8",
    "surface": "#FFFFFF",
    "terracotta": "#B9573F",
    "terracotta_dark": "#93432F",
    "green": "#287D52",
    "red": "#B84242",
    "text": "#302E2B",
    "muted": "#77716A",
    "border": "#E8DED0",
}

TENSE_LABELS = {
    "presente": "Présent",
    "preterito": "Prétérit",
    "imperfecto": "Imparfait",
    "futuro": "Futur",
    "condicional": "Conditionnel",
    "subjuntivo_presente": "Subjonctif présent",
    "subjuntivo_imperfecto": "Subjonctif imparfait",
    "subjuntivo_futuro": "Subjonctif futur",
    "perfecto": "Passé composé",
    "pluscuamperfecto": "Plus-que-parfait",
    "futuro_perfecto": "Futur antérieur",
    "condicional_perfecto": "Conditionnel passé",
    "subjuntivo_perfecto": "Subjonctif passé",
    "subjuntivo_pluscuamperfecto": "Subjonctif plus-que-parfait",
    "imperativo_afirmativo": "Impératif affirmatif",
    "imperativo_negativo": "Impératif négatif",
}

PRONOMINAL_VERBS = [
    "llamarse",
    "levantarse",
    "acostarse",
    "despertarse",
    "ducharse",
    "lavarse",
    "vestirse",
    "sentarse",
    "quedarse",
    "irse",
    "sentirse",
    "divertirse",
]

VERB_TYPE_OPTIONS = {
    "Tous les verbes": "tous",
    "Verbes simples": "simples",
    "Verbes pronominaux": "pronominaux",
}


# ============================================================
# STYLE
# ============================================================

st.markdown(
    f"""
    <style>
    
    /* Texte des KPI : lisible sur fond blanc */
    div[data-testid="stMetric"] {{
        background-color: #FFFFFF !important;
        border: 1px solid #E8DED0;
        border-radius: 12px;
        padding: 1rem;
    }}

    div[data-testid="stMetric"] label,
    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricLabel"] p,
    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] div {{
        color: #302E2B !important;
    }}

    /* Boutons : texte clair, y compris Question suivante */
    .stButton > button,
    .stFormSubmitButton > button,
    button[kind="primaryFormSubmit"] {{
        background-color: #B9573F !important;
        color: #FFFFFF !important;
        border: 1px solid #93432F !important;
        border-radius: 10px;
        font-weight: 600;
    }}

    /* Conserver le texte blanc au survol */
    .stButton > button:hover,
    .stFormSubmitButton > button:hover,
    button[kind="primaryFormSubmit"]:hover {{
        background-color: #93432F !important;
        color: #FFFFFF !important;
        border-color: #93432F !important;
    }}

    /* Corriger également le texte interne des boutons */
    .stButton > button *,
    .stFormSubmitButton > button *,
    button[kind="primaryFormSubmit"] * {{
        color: #FFFFFF !important;
    }}

    .stApp {{
        background-color: {COLORS["background"]};
        color: {COLORS["text"]};
    }}

    [data-testid="stHeader"] {{
        background-color: transparent;
    }}

    .main .block-container {{
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    .app-subtitle {{
        color: {COLORS["muted"]};
        font-size: 1rem;
        margin-top: -0.6rem;
        margin-bottom: 1.8rem;
    }}

    .exercise-card {{
        background: {COLORS["surface"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 18px;
        padding: 1.7rem;
        margin: 1rem 0;
        text-align: center;
    }}

    .exercise-type {{
        color: {COLORS["terracotta"]};
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }}

    .exercise-verb {{
        font-size: 2.2rem;
        font-weight: 750;
        margin: 0.4rem 0 1rem 0;
        color: {COLORS["text"]};
    }}

    .exercise-detail {{
        font-size: 1.05rem;
        margin: 0.35rem 0;
    }}

    .stButton > button,
    .stFormSubmitButton > button {{
        border-radius: 10px;
        min-height: 2.8rem;
        font-weight: 600;
    }}

    div[data-testid="stMetric"] {{
        background: {COLORS["surface"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 12px;
        padding: 1rem;
    }}

    div[data-testid="stProgressBar"] > div > div {{
        background-color: {COLORS["terracotta"]};
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FONCTIONS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
SOUND_CORRECT = BASE_DIR / "assets" / "positive.wav"
SOUND_INCORRECT = BASE_DIR / "assets" / "negative.wav"


def play_sound(sound_path):
    """Joue un son dans le navigateur à partir d'un fichier local."""
    if not sound_path.exists():
        return

    audio_bytes = sound_path.read_bytes()
    encoded_audio = base64.b64encode(audio_bytes).decode("utf-8")

    st.markdown(
        f"""
        <audio autoplay>
            <source
                src="data:audio/wav;base64,{encoded_audio}"
                type="audio/wav"
            >
        </audio>
        """,
        unsafe_allow_html=True,
    )




def label_tense(tense):
    return TENSE_LABELS.get(
        tense,
        tense.replace("_", " ").capitalize()
    )


def generate_question(verb_type, selected_tense):
    """Crée une nouvelle question selon les filtres sélectionnés."""

    if verb_type == "simples":
        candidates = [
            (verb, False) for verb in moteur.ALL_VERBS
        ]
    elif verb_type == "pronominaux":
        candidates = [
            (verb, True) for verb in PRONOMINAL_VERBS
        ]
    else:
        candidates = (
            [(verb, False) for verb in moteur.ALL_VERBS]
            + [(verb, True) for verb in PRONOMINAL_VERBS]
        )

    if not candidates:
        raise ValueError("Aucun verbe disponible.")

    verb, is_pronominal = random.choice(candidates)
    person = random.choice(moteur.PERSONS)

    if selected_tense == "Tous les temps":
        tense = random.choice(moteur.TENSES)
    else:
        tense = selected_tense

    if is_pronominal:
        expected = moteur.conjugate_pronominal(
            verb, tense, person
        )
    else:
        expected = moteur.conjugate(
            verb, tense, person
        )

    return {
        "verb": verb,
        "is_pronominal": is_pronominal,
        "person": person,
        "tense": tense,
        "expected": expected,
        "answered": False,
        "feedback": None,
    }


def reset_session():
    """Réinitialise le score et prépare une nouvelle question."""
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.question = generate_question(
        st.session_state.verb_type,
        st.session_state.selected_tense,
    )
    st.session_state.answer = ""


def submit_answer():
    """Valide la réponse ou passe à la question suivante."""

    question = st.session_state.question

    # Si la réponse précédente était correcte,
    # la prochaine validation passe à l'exercice suivant.
    if question["answered"]:
        st.session_state.question = generate_question(
            st.session_state.verb_type,
            st.session_state.selected_tense,
        )
        st.session_state.answer = ""
        return

    answer = st.session_state.answer.strip().casefold()

    if not answer:
        st.session_state.feedback_message = (
            "Écris d'abord une réponse."
        )
        st.session_state.feedback_type = "warning"
        return

    st.session_state.total += 1

    if answer == question["expected"].casefold():
        st.session_state.score += 1
        question["answered"] = True
        question["feedback"] = "correct"

        st.session_state.feedback_message = (
            f"¡Muy bien! Bonne réponse : {question['expected']}"
        )
        st.session_state.feedback_type = "success"
        play_sound(SOUND_CORRECT)

    else:
        # On garde la même question pour permettre une nouvelle tentative.
        question["feedback"] = "incorrect"

        st.session_state.feedback_message = (
            "Pas tout à fait. Essaie encore !"
        )
        st.session_state.feedback_type = "error"
        play_sound(SOUND_INCORRECT)


# ============================================================
# INITIALISATION DE LA SESSION
# ============================================================

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.verb_type = "tous"
    st.session_state.selected_tense = "Tous les temps"
    st.session_state.question = generate_question(
        st.session_state.verb_type,
        st.session_state.selected_tense,
    )
    st.session_state.answer = ""
    st.session_state.feedback_message = ""
    st.session_state.feedback_type = ""


# ============================================================
# EN-TÊTE
# ============================================================

st.title("🇪🇸 Spanish Conjugation Trainer")

st.markdown(
    '<div class="app-subtitle">'
    "Entraîne-toi à conjuguer les verbes espagnols, "
    "des temps simples aux temps composés."
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# FILTRES
# ============================================================

st.sidebar.header("⚙️ Paramètres des exercices")

verb_type_label = st.sidebar.selectbox(
    "Type de verbes",
    options=list(VERB_TYPE_OPTIONS.keys()),
    index=list(VERB_TYPE_OPTIONS.values()).index(
        st.session_state.verb_type
    ),
)

new_verb_type = VERB_TYPE_OPTIONS[verb_type_label]

tense_labels = ["Tous les temps"] + [
    label_tense(tense) for tense in moteur.TENSES
]

tense_to_code = {
    label_tense(tense): tense
    for tense in moteur.TENSES
}

tense_label_to_show = st.sidebar.selectbox(
    "Temps verbal",
    options=tense_labels,
    index=(
        tense_labels.index(st.session_state.selected_tense)
        if st.session_state.selected_tense in tense_labels
        else 0
    ),
)

new_selected_tense = (
    "Tous les temps"
    if tense_label_to_show == "Tous les temps"
    else tense_to_code[tense_label_to_show]
)

# Un changement de filtre crée une nouvelle question.
if (
    new_verb_type != st.session_state.verb_type
    or new_selected_tense != st.session_state.selected_tense
):
    st.session_state.verb_type = new_verb_type
    st.session_state.selected_tense = new_selected_tense
    st.session_state.question = generate_question(
        new_verb_type,
        new_selected_tense,
    )
    st.session_state.answer = ""
    st.session_state.feedback_message = ""
    st.session_state.feedback_type = ""
    st.rerun()

st.sidebar.divider()

st.sidebar.caption(
    "Conseil : commence par un seul temps verbal, "
    "puis élargis progressivement les exercices."
)

if st.sidebar.button("🔄 Recommencer la session", use_container_width=True):
    reset_session()
    st.session_state.feedback_message = ""
    st.session_state.feedback_type = ""
    st.rerun()


# ============================================================
# PROGRESSION
# ============================================================

score = st.session_state.score
total = st.session_state.total
accuracy = score / total * 100 if total else 0

metric1, metric2, metric3 = st.columns(3)

metric1.metric("Réussites", score)
metric2.metric("Tentatives", total)
metric3.metric("Précision", f"{accuracy:.0f}%")

st.progress(accuracy / 100)

st.caption("La précision correspond aux réponses correctes sur les tentatives.")


# ============================================================
# CARTE DE L'EXERCICE
# ============================================================

question = st.session_state.question

verb_type_text = (
    "Verbe pronominal"
    if question["is_pronominal"]
    else "Verbe simple"
)

st.markdown(
    f"""
    <div class="exercise-card">
        <div class="exercise-type">{verb_type_text}</div>
        <div class="exercise-verb">{question["verb"]}</div>
        <div class="exercise-detail">
            <strong>Temps :</strong> {label_tense(question["tense"])}
        </div>
        <div class="exercise-detail">
            <strong>Personne :</strong> {question["person"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SAISIE ET VALIDATION
# ============================================================

if question["answered"]:
    st.success(
        f"✓ {st.session_state.feedback_message}"
    )
    st.info("Appuie sur le bouton ci-dessous ou sur Entrée pour continuer.")

elif question["feedback"] == "incorrect":
    st.error(st.session_state.feedback_message)

elif st.session_state.feedback_type == "warning":
    st.warning(st.session_state.feedback_message)


button_label = (
    "Question suivante →"
    if question["answered"]
    else "Valider la réponse"
)

with st.form("answer_form", clear_on_submit=False):
    st.text_input(
        "Ta conjugaison en espagnol",
        key="answer",
        placeholder="Écris la forme conjuguée…",
        disabled=question["answered"],
    )

    st.form_submit_button(
        button_label,
        on_click=submit_answer,
        use_container_width=True,
    )


# ============================================================
# AIDE
# ============================================================

with st.expander("💡 Comment jouer ?"):
    st.markdown(
        """
        1. Observe le verbe, le temps et la personne.
        2. Écris la conjugaison en espagnol.
        3. Appuie sur **Entrée** pour valider.
        4. Si ta réponse est incorrecte, essaie de nouveau.
        5. Si elle est correcte, passe à la question suivante.
        6. Utilise les filtres à gauche pour choisir les temps
           et les types de verbes.

        Les accents espagnols comptent : par exemple, **hablé**
        et **hable** ne sont pas la même forme.
        """
    )
