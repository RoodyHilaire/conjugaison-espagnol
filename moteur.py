import tkinter as tk
import random


####################################################################################################
########################################### GENERALITIES ###########################################
####################################################################################################


# def verb_type(verb):
#     if verb.endswith("ar"):
#         return "ar"
#     if verb.endswith("er"):
#         return "er"
#     if verb.endswith("ir"):
#         return "ir"

#     raise ValueError(f"Type de verbe inconnu : {verb}")

def verb_type(verb):
    if verb == "oír":
        return "ir"
    if verb.endswith("ar"):
        return "ar"
    if verb.endswith("er"):
        return "er"
    if verb.endswith("ir"):
        return "ir"

    raise ValueError(f"Type de verbe inconnu : {verb}")

TENSES = [
    "presente",
    "preterito",
    "imperfecto",
    "futuro",
    "condicional",
    "perfecto",
    "pluscuamperfecto", 
    "futuro_perfecto", 
    "condicional_perfecto", 
    "subjuntivo_presente", 
    "subjuntivo_imperfecto", 
    "subjuntivo_pluscuamperfecto",
    "subjuntivo_perfecto",
    "imperativo_afirmativo",
    "imperativo_negativo"
    ]

PERSONS = ["yo", "tu", "el", "nosotros", "vosotros", "ellos"]


#########################################
############ Sub Generalities ###########
#########################################


VERBS_E_IE = {
"helar",
"pensar",
"acertar",
"sentar",
"quebrar",
"negar",
"cegar",
"mentar",
"gobernar",
"despertar",
"desalentar",
"merendar",
"invernar",
"comenzar",
"calentar",
"plegar",
"empedrar",
"manifestar",
"enterrar",
"confesar",
"enmendar",
"fregar",
"tentar",
"arrendar",
"alentar",
"segar",
"nevar",
"tropezar",
"apretar",
"regar",
"atravesar",
"empezar",
"cerrar",
"sosegar",
"recomendar",
"herrar",
"tender",
"atender",
"descender",
"ascender",
"verter",
"perder",
"encender",
"hender",
"entender",
"reverter",
"defender",
"extender",
"adquirir",

# Verbes en -IR à alternance e -> ie au présent
"sentir",
"arrepentir",
"mentir",
"advertir",
"conferir",
"invertir",
"hervir",
"injerir",
"divertir",
"revertir",
"inserir",
"presentir",
"herir",
"adherir",
"proferir",
"sugerir",
"desmentir",
"consentir",
"asentir",
"preferir",
"diferir",
"deferir",
"transferir",
"zaherir",
"inferir",
"preterir",

# Autres déjà validés dans V15
"querer",
"negar",
"despertar",

}



VERBS_O_UE = {
"contar",
"acordar",
"acostar",
"amoblar",
"aprobar",
"apostar",
"almorzar",
"emporcar",
"probar",
"volcar",
"colar",
"concordar",
"comprobar",
"desaprobar",
"engrosar",
"consolar",
"mostrar",
"hollar",
"recordar",
"esforzar",
"despoblar",
"encontrar",
"rodar",
"soltar",
"volar",
"costar",
"tostar",
"soñar",
"tronar",
"descollar",
"poblar",
"forzar",
"colgar",
"descolgar",
"rogar",
"trocar",
"sonar",
"renovar",

"absolver",
"mover",
"conmover",
"llover",
"volver",
"doler",
"revolver",
"resolver",
"remover",
"soler",
"morder",
"devolver",
"torcer",
"cocer",
"disolver",

# V15
"poder",
"dormir",
"morir",

}

VERBS_U_UE = {
"jugar",
}

VERBS_E_I = {
"pedir",
"despedir",
"expedir",
"derretir",
"concebir",
"gemir",
"investir",
"desvestir",
"servir",
"medir",
"impedir",
"competir",
"rendir",
"regir",
"revestir",
"vestir",
"repetir",
"colegir",
"conseguir",
"perseguir",
"proseguir",
"elegir",
"freir",
"descomedir",
"teñir",
"ceñir",
"henchir",
"constreñir",
"desteñir",
"reñir",

# V15
"seguir",
"corregir",
"preferir",
"sentir"

}

VERBS_C_ZC = {
"anochecer",
"aparecer",
"adolecer",
"acontecer",
"conocer",
"padecer",
"carecer",
"crecer",
"decrecer",
"empobrecer",
"enriquecer",
"obedecer",
"entallecer",
"entenebrecer",
"enternecer",
"embellecer",
"establecer",
"estremecer",
"fallecer",
"favorecer",
"entristecer",
"envejecer",
"esclarecer",
"resplandecer",
"robustecer",
"verdecer",
"remanecer",
"apetecer",
"fenecer",
"escalecer",
"renacer",
"palidecer",
"desconocer",
"perecer",
"ofrecer",
"enfurecer",
"enrojecer",
"merecer",
"enflaquecer",
"reblandecer",
"mohecer",
"podrecer",
"pacer",
"escaecer",
"excandecer",
"prevalecer",
"amanecer",
"envilecer",
"rejuvenecer",
"fornecer",
"enmudecer",
"enorgullecer",
"permanecer",
"empequeñecer",
"comparecer",
"parecer",
"reconocer",
"reverdecer",
"ennoblecer",
"agradecer",

# -UCIR
"conducir",
"inducir",
"introducir",
"deducir",
"producir",
"reproducir",
"reconducir",
"aducir",
"educir",
"seducir",

# LUCIR et dérivés
"lucir",
"relucir",
"enlucir",
"deslucir",
"prelucir",
"entrelucir",

}

VERBS_C_Z = {
"vencer",
"zurcir",
"esparcir",
"torcer",
"resarcir",
"convencer",
"cocer",
}


VERBS_G_J = {
"coger",
"recoger",
"exigir",
"mugir",
"resurgir",
"rugir",
"surgir",
"afligir",
"elegir",
"regir",
}

VERBS_GUIR_G = {
"extinguir",
"seguir",
"perseguir",
"conseguir",
"proseguir",
}


VERBS_QUIR_C = {
"delinquir",
}

VERBS_IAR_ACCENT = {
"liar",
"rociar",
"fiar",
"desconfiar",
"piar",
"variar",
"espiar",
"enviar",
"guiar",
"resfriar",
"ataviar",
"chirriar",
}

VERBS_UAR_ACCENT = {
"continuar",
"acentuar",
"puntuar",
"graduar",
}


VERBS_EIR_ACCENT = {
"reír",
"sonreír",
"freír",
"desleír",
"engreír",
}


VERBS_I_Y = {"leer", "creer", "raer", "roer", "poseer", "caer", "proveer", "oír"}

VERBS_I_LOSS = {"engullir", "zambullir", "gruñir", "reñir", "henchir", "constreñir", "atañer", "ceñir", "tañer", "mullir", "teñir", "desteñir", "astreñir", "bruñir"}

VERBS_O_U = {
"dormir",
"morir",
}

VERBS_UIR_Y = {
"concluir",
"fluir",
"obstruir",
"disminuir",
"constituir",
"construir",
"destruir",
"influir",
"atribuir",
"contribuir",
"instituir",
"confluir",
"excluir",
"destituir",
"distribuir",
"retribuir",
"imbuir",
"instruir",
"incluir",
"prostituir",
"afluir",
"diluir",
"fruir",
"huir",
}


####################################################################################################
############################################## PRESENT #############################################
####################################################################################################

PRESENT_ENDINGS = {
"ar": {
"yo": "o",
"tu": "as",
"el": "a",
"nosotros": "amos",
"vosotros": "áis",
"ellos": "an",
},
"er": {
"yo": "o",
"tu": "es",
"el": "e",
"nosotros": "emos",
"vosotros": "éis",
"ellos": "en",
},
"ir": {
"yo": "o",
"tu": "es",
"el": "e",
"nosotros": "imos",
"vosotros": "ís",
"ellos": "en",
},
}


PRESENT_IRREGULAR = {
"ser": {
"yo": "soy",
"tu": "eres",
"el": "es",
"nosotros": "somos",
"vosotros": "sois",
"ellos": "son",
},
"estar": {
"yo": "estoy",
"tu": "estás",
"el": "está",
"nosotros": "estamos",
"vosotros": "estáis",
"ellos": "están",
},
"ir": {
"yo": "voy",
"tu": "vas",
"el": "va",
"nosotros": "vamos",
"vosotros": "vais",
"ellos": "van",
},
"tener": {
"yo": "tengo",
"tu": "tienes",
"el": "tiene",
"nosotros": "tenemos",
"vosotros": "tenéis",
"ellos": "tienen",
},
"venir": {
"yo": "vengo",
"tu": "vienes",
"el": "viene",
"nosotros": "venimos",
"vosotros": "venís",
"ellos": "vienen",
},
"hacer": {
"yo": "hago",
"tu": "haces",
"el": "hace",
"nosotros": "hacemos",
"vosotros": "hacéis",
"ellos": "hacen",
},
"decir": {
"yo": "digo",
"tu": "dices",
"el": "dice",
"nosotros": "decimos",
"vosotros": "decís",
"ellos": "dicen",
},
"salir": {
"yo": "salgo",
"tu": "sales",
"el": "sale",
"nosotros": "salimos",
"vosotros": "salís",
"ellos": "salen",
},
"poner": {
"yo": "pongo",
"tu": "pones",
"el": "pone",
"nosotros": "ponemos",
"vosotros": "ponéis",
"ellos": "ponen",
},
"saber": {
"yo": "sé",
"tu": "sabes",
"el": "sabe",
"nosotros": "sabemos",
"vosotros": "sabéis",
"ellos": "saben",
},
"ver": {
"yo": "veo",
"tu": "ves",
"el": "ve",
"nosotros": "vemos",
"vosotros": "veis",
"ellos": "ven",
},
"dar": {
"yo": "doy",
"tu": "das",
"el": "da",
"nosotros": "damos",
"vosotros": "dais",
"ellos": "dan",
},
"oír": {
    "yo": "oigo",
    "tu": "oyes",
    "el": "oye",
    "nosotros": "oímos",
    "vosotros": "oís",
    "ellos": "oyen",
},
}




### OUTILS DE TRANSFORMATION
def replace_last_vowel(stem, old, new):
    """
    Remplace la dernière occurrence de old dans le radical.
    """
    pos = stem.rfind(old)

    if pos == -1:
        return stem

    return stem[:pos] + new + stem[pos + 1:]



def add_acute_to_last_i(text):
    """
    Transforme le dernier i non accentué en í.
    """
    pos = text.rfind("i")

    if pos == -1:
        return text

    return text[:pos] + "í" + text[pos + 1:]



def add_acute_to_last_u(text):
    """
    Transforme le dernier u non accentué en ú.
    """
    pos = text.rfind("u")

    if pos == -1:
        return text

    return text[:pos] + "ú" + text[pos + 1:]


### APPLICATION DES FAMILLES MORPHOLOGIQUES

def apply_present_morphological_rules(verb, person, stem):
    """
    Applique uniquement les modifications morphologiques du radical
    pour le présent indicatif.

    Les règles orthographiques sont appliquées séparément ensuite.
    """

    # Nosotros et vosotros :
    # e -> ie, o -> ue, u -> ue, e -> i
    # ne s'appliquent normalement pas au présent indicatif.
    if person in ("nosotros", "vosotros"):
        return stem

    # ------------------------------------------------------------------
    # e -> ie
    # ------------------------------------------------------------------

    if verb in VERBS_E_IE:
        return replace_last_vowel(stem, "e", "ie")

    # ------------------------------------------------------------------
    # o -> ue
    # ------------------------------------------------------------------

    if verb in VERBS_O_UE:
        return replace_last_vowel(stem, "o", "ue")

    # ------------------------------------------------------------------
    # u -> ue
    # ------------------------------------------------------------------

    if verb in VERBS_U_UE:
        return replace_last_vowel(stem, "u", "ue")

    # ------------------------------------------------------------------
    # e -> i
    # ------------------------------------------------------------------

    if verb in VERBS_E_I:
        return replace_last_vowel(stem, "e", "i")

    return stem



### APPLICATION DES MODIFICATIONS ORTHOGRAPHIQUES
def apply_present_orthographic_rules(verb, person, stem):
    """
    Applique les modifications orthographiques propres au présent.

    Ces règles interviennent APRÈS les changements de radical afin
    de permettre les combinaisons.

    Exemple :
        torcer
        torc
        -> tuerc       (o -> ue)
        -> tuerz       (c -> z)
        -> tuerzo
    """

    # ------------------------------------------------------------------
    # Ces modifications concernent ici essentiellement la 1re personne
    # du singulier.
    # ------------------------------------------------------------------

    if person != "yo":
        return stem

    # ------------------------------------------------------------------
    # c -> zc
    #
    # conocer -> conozco
    # conducir -> conduzco
    # lucir -> luzco
    # ------------------------------------------------------------------

    if verb in VERBS_C_ZC:

        if stem.endswith("c"):
            return stem[:-1] + "zc"

        return stem + "zc"

    # ------------------------------------------------------------------
    # c -> z
    #
    # vencer -> venzo
    #
    # Peut se combiner avec o -> ue :
    # torcer -> tuerzo
    # ------------------------------------------------------------------

    if verb in VERBS_C_Z:

        if stem.endswith("c"):
            return stem[:-1] + "z"

        return stem + "z"

    # ------------------------------------------------------------------
    # g -> j
    #
    # coger -> cojo
    # exigir -> exijo
    # ------------------------------------------------------------------

    if verb in VERBS_G_J:

        if stem.endswith("g"):
            return stem[:-1] + "j"

        return stem + "j"

    # ------------------------------------------------------------------
    # gu -> g
    #
    # seguir :
    # segu -> sigu  (e -> i)
    # sigu -> sig   (gu -> g)
    # ------------------------------------------------------------------

    if verb in VERBS_GUIR_G:

        if stem.endswith("gu"):
            return stem[:-2] + "g"

        return stem

    # ------------------------------------------------------------------
    # qu -> c
    #
    # delinquir -> delinco
    # ------------------------------------------------------------------

    if verb in VERBS_QUIR_C:

        if stem.endswith("qu"):
            return stem[:-2] + "c"

        return stem

    # ------------------------------------------------------------------
    # -uir -> -uyo, -uyes, -uye, -uyen
    # construir -> construyo, construyes, construye, construyen
    # ------------------------------------------------------------------



    return stem



### ACCENTUATION DU PRÉSENT
def apply_present_accent_rules(verb, person, stem):
    """
    Applique les règles d'accentuation propres au présent.

    Les formes concernées sont :
        yo, tú, él, ellos

    pour les familles -iar et -uar.
    """

    # ------------------------------------------------------------------
    # -iar : envío, envías, envía, envían
    # ------------------------------------------------------------------

    if verb in VERBS_IAR_ACCENT and person in (
        "yo",
        "tu",
        "el",
        "ellos",
    ):
        return add_acute_to_last_i(stem)

    # ------------------------------------------------------------------
    # -uar : continúo, continúas, continúa, continúan
    # ------------------------------------------------------------------

    if verb in VERBS_UAR_ACCENT and person in (
        "yo",
        "tu",
        "el",
        "ellos",
    ):
        return add_acute_to_last_u(stem)

    return stem





### VERBES EN -EÍR
def conjugate_present_eir(verb, person):
    """
    Gère les verbes comme :
    reír
    sonreír
    freír
    desleír
    engreír

    On ne les fait pas passer dans le mécanisme générique e -> i,
    car leur orthographe accentuée est particulière.
    """

    special_forms = {
        "reír": {
            "yo": "río",
            "tu": "ríes",
            "el": "ríe",
            "nosotros": "reímos",
            "vosotros": "reís",
            "ellos": "ríen",
        },

        "sonreír": {
            "yo": "sonrío",
            "tu": "sonríes",
            "el": "sonríe",
            "nosotros": "sonreímos",
            "vosotros": "sonreís",
            "ellos": "sonríen",
        },

        "freír": {
            "yo": "frío",
            "tu": "fríes",
            "el": "fríe",
            "nosotros": "freímos",
            "vosotros": "freís",
            "ellos": "fríen",
        },

        "desleír": {
            "yo": "deslío",
            "tu": "deslíes",
            "el": "deslíe",
            "nosotros": "desleímos",
            "vosotros": "desleís",
            "ellos": "deslíen",
        },

        "engreír": {
            "yo": "engrío",
            "tu": "engríes",
            "el": "engríe",
            "nosotros": "engreímos",
            "vosotros": "engreís",
            "ellos": "engríen",
        },
    }

    return special_forms[verb][person]



### PRÉSENT RÉGULIER + TRANSFORMATIONS
def conjugate_present(verb, person):

    # --------------------------------------------------------------------------------------------
    # ÉTAPE 1
    # Verbes complètement irréguliers
    # --------------------------------------------------------------------------------------------

    if verb in PRESENT_IRREGULAR:
        return PRESENT_IRREGULAR[verb][person]

    # --------------------------------------------------------------------------------------------
    # ÉTAPE 2
    # Cas particuliers en -eír
    # --------------------------------------------------------------------------------------------

    if verb in VERBS_EIR_ACCENT:
        return conjugate_present_eir(verb, person)


        # Verbes en -uir : presente avec y
    if verb in VERBS_UIR_Y:
        stem = verb[:-2]

        if person == "yo":
            return stem + "yo"
        if person == "tu":
            return stem + "yes"
        if person == "el":
            return stem + "ye"
        if person == "ellos":
            return stem + "yen"
        if person == "nosotros":
            return stem + "imos"
        if person == "vosotros":
            return stem + "ís"
        
    # --------------------------------------------------------------------------------------------
    # ÉTAPE 3
    # Base régulière
    # --------------------------------------------------------------------------------------------

    stem = verb[:-2]

    # --------------------------------------------------------------------------------------------
    # ÉTAPE 4
    # Transformation morphologique
    # --------------------------------------------------------------------------------------------

    stem = apply_present_morphological_rules(
        verb,
        person,
        stem
    )

    # --------------------------------------------------------------------------------------------
    # ÉTAPE 5
    # Transformation orthographique
    # --------------------------------------------------------------------------------------------

    stem = apply_present_orthographic_rules(
        verb,
        person,
        stem
    )

    # --------------------------------------------------------------------------------------------
    # ÉTAPE 6
    # Accentuation particulière -iar / -uar
    # --------------------------------------------------------------------------------------------

    stem = apply_present_accent_rules(
        verb,
        person,
        stem
    )

    # --------------------------------------------------------------------------------------------
    # ÉTAPE 7
    # Terminaison régulière
    # --------------------------------------------------------------------------------------------

    ending = PRESENT_ENDINGS[
        verb_type(verb)
    ][person]

    return stem + ending



    


####################################################################################################
############################################# PRETERIT #############################################
####################################################################################################

PRETERITE_ENDINGS = {
"ar": {
"yo": "é",
"tu": "aste",
"el": "ó",
"nosotros": "amos",
"vosotros": "asteis",
"ellos": "aron",
},
"er": {
"yo": "í",
"tu": "iste",
"el": "ió",
"nosotros": "imos",
"vosotros": "isteis",
"ellos": "ieron",
},
"ir": {
"yo": "í",
"tu": "iste",
"el": "ió",
"nosotros": "imos",
"vosotros": "isteis",
"ellos": "ieron",
},
}


PRETERITE_IRREGULAR_STEMS = {
"andar": "anduv",
"estar": "estuv",
"tener": "tuv",
"poder": "pud",
"poner": "pus",
"saber": "sup",
"querer": "quis",
"venir": "vin",
"caber": "cup",
"haber": "hub",
"hacer": "hic",
"decir": "dij",
"traer": "traj",
"conducir": "conduj",
"producir": "produj",
"traducir": "traduj",
}

PRETERITE_IRREGULAR_ENDINGS = {
"yo": "e",
"tu": "iste",
"el": "o",
"nosotros": "imos",
"vosotros": "isteis",
"ellos": "ieron",
}

PRETERITE_J_ENDINGS = {
"yo": "e",
"tu": "iste",
"el": "o",
"nosotros": "imos",
"vosotros": "isteis",
"ellos": "eron",
}


PRETERITE_FULL_IRREGULAR = {
"ser": {
"yo": "fui",
"tu": "fuiste",
"el": "fue",
"nosotros": "fuimos",
"vosotros": "fuisteis",
"ellos": "fueron",
},
"ir": {
"yo": "fui",
"tu": "fuiste",
"el": "fue",
"nosotros": "fuimos",
"vosotros": "fuisteis",
"ellos": "fueron",
},
}


def apply_preterite_e_i(stem, verb, person):
    if verb in VERBS_E_I and person in {"el", "ellos"}:
        return replace_last_vowel(stem, "e", "i")

    return stem

def apply_preterite_o_u(stem, verb, person):
    if verb in VERBS_O_U and person in {"el", "ellos"}:
        return replace_last_vowel(stem, "o", "u")

    return stem


def apply_preterite_uir_y(stem, verb, person):

    if verb in VERBS_UIR_Y and person in {"el", "ellos"}:
        return stem + "y"

    return stem



# def apply_preterite_i_y(stem, verb, person):

#     if verb in VERBS_I_Y and person in {"el", "ellos"}:
#         return stem + "y"

#     return stem



# def apply_preterite_i_loss(stem, verb, person):

#     if verb in VERBS_I_LOSS and person in {"el", "ellos"}:

#         if stem.endswith("i"):
#             return stem[:-1]

#     return stem


def apply_preterite_i_y(stem, verb, person):
    if verb in VERBS_I_Y and person in {"el", "ellos"}:
        return stem + "y"
    return stem

def apply_preterite_i_loss(stem, verb, person):
    if verb in VERBS_I_LOSS and person in {"el", "ellos"}:
        if stem.endswith("i"):
            return stem[:-1]
    return stem

def apply_preterite_i_loss_ending(ending, verb, person):
    if verb in VERBS_I_LOSS and person in {"el", "ellos"}:
        if person == "el" and ending == "ió":
            return "ó"
        if person == "ellos" and ending == "ieron":
            return "eron"
    return ending



def apply_preterite_orthography(stem, verb, person):

    if person != "yo":
        return stem

    if verb.endswith("car"):
        return stem[:-1] + "qu"

    if verb.endswith("gar"):
        return stem[:-1] + "gu"

    if verb.endswith("zar"):
        return stem[:-1] + "c"

    return stem


# def conjugate_preterite(verb, person):

#     # ============================================================================================
#     # 1. IRRÉGULIERS COMPLETS
#     # ============================================================================================

#     if verb in PRETERITE_FULL_IRREGULAR:
#         return PRETERITE_FULL_IRREGULAR[verb][person]


#     # ============================================================================================
#     # 2. TYPE DU VERBE
#     #
#     # oír possède un infinitif accentué : oír.
#     # Pour le traitement morphologique, il appartient néanmoins à la conjugaison en -ir.
#     # ============================================================================================

#     if verb == "oír":
#         vtype = "ir"
#     else:
#         vtype = verb_type(verb)


#     # ============================================================================================
#     # 3. RADICAUX COMPLÈTEMENT IRRÉGULIERS
#     # ============================================================================================

#     if verb in PRETERITE_IRREGULAR_STEMS:

#         stem = PRETERITE_IRREGULAR_STEMS[verb]

#         # hacer : hice, hiciste, hizo, hicimos...
#         if verb == "hacer" and person == "el":
#             stem = "hiz"

#         if stem.endswith("j"):
#             ending = PRETERITE_J_ENDINGS[person]
#         else:
#             ending = PRETERITE_IRREGULAR_ENDINGS[person]

#         return stem + ending


#     # ============================================================================================
#     # 4. BASE RÉGULIÈRE
#     # ============================================================================================

#     stem = verb[:-2]


#     # ============================================================================================
#     # 5. E → I
#     # ============================================================================================

#     stem = apply_preterite_e_i(stem, verb, person)


#     # ============================================================================================
#     # 6. O → U
#     # ============================================================================================

#     stem = apply_preterite_o_u(stem, verb, person)


#     # ============================================================================================
#     # 7. -UIR → Y
#     # ============================================================================================

#     stem = apply_preterite_uir_y(stem, verb, person)


#     # ============================================================================================
#     # 8. I → Y
#     # ============================================================================================

#     stem = apply_preterite_i_y(stem, verb, person)


#     # ============================================================================================
#     # 9. PERTE DU I
#     # ============================================================================================

#     stem = apply_preterite_i_loss(stem, verb, person)


#     # ============================================================================================
#     # 10. ORTHOGRAPHE DU YO
#     # ============================================================================================

#     stem = apply_preterite_orthography(stem, verb, person)


#     # ============================================================================================
#     # 11. TERMINAISON
#     #
#     # Pour les familles I → Y et -UIR → Y :
#     #
#     # él     → -yó
#     # ellos  → -yeron
#     #
#     # au lieu de :
#     #
#     # él     → -ió
#     # ellos  → -ieron
#     # ============================================================================================

#     if verb in VERBS_I_Y or verb in VERBS_UIR_Y:

#         if person == "el":
#             return stem + "ó"

#         if person == "ellos":
#             return stem + "eron"


#     # ============================================================================================
#     # 12. TERMINAISON RÉGULIÈRE
#     # ============================================================================================

#     ending = PRETERITE_ENDINGS[vtype][person]

#     return stem + ending


def conjugate_preterite(verb, person):
    # ---------------------------------------------------------
    # 1. Verbes totalement irréguliers
    # ---------------------------------------------------------
    if verb in PRETERITE_FULL_IRREGULAR:
        return PRETERITE_FULL_IRREGULAR[verb][person]

    # ---------------------------------------------------------
    # 2. Type verbal
    # ---------------------------------------------------------
    if verb == "oír":
        vtype = "ir"
    else:
        vtype = verb_type(verb)

    # ---------------------------------------------------------
    # 3. Verbes à radical totalement irrégulier
    # ---------------------------------------------------------
    if verb in PRETERITE_IRREGULAR_STEMS:
        stem = PRETERITE_IRREGULAR_STEMS[verb]

        if stem.endswith("j"):
            ending = PRETERITE_J_ENDINGS[person]
        else:
            ending = PRETERITE_IRREGULAR_ENDINGS[person]

        # hacer → hizo
        if verb == "hacer" and person == "el":
            stem = "hiz"

        return stem + ending

    # ---------------------------------------------------------
    # 4. Radical régulier
    # ---------------------------------------------------------
    stem = verb[:-2]

    # ---------------------------------------------------------
    # 5. e → i
    # ---------------------------------------------------------
    stem = apply_preterite_e_i(
        stem,
        verb,
        person
    )

    # ---------------------------------------------------------
    # 6. o → u
    # ---------------------------------------------------------
    stem = apply_preterite_o_u(
        stem,
        verb,
        person
    )

    # ---------------------------------------------------------
    # 7. -UIR → Y
    # ---------------------------------------------------------
    stem = apply_preterite_uir_y(
        stem,
        verb,
        person
    )

    # ---------------------------------------------------------
    # 8. i → y
    # ---------------------------------------------------------
    stem = apply_preterite_i_y(
        stem,
        verb,
        person
    )

    # ---------------------------------------------------------
    # 9. Terminaison régulière
    # ---------------------------------------------------------
    ending = PRETERITE_ENDINGS[vtype][person]

    # ---------------------------------------------------------
    # 10. Perte du i en 3e personne
    # ---------------------------------------------------------
    if verb in VERBS_I_LOSS and person in {"el", "ellos"}:
        if person == "el":
            ending = "ó"
        else:
            ending = "eron"

    # ---------------------------------------------------------
    # 11. Modifications orthographiques
    # ---------------------------------------------------------
    stem = apply_preterite_orthography(
        stem,
        verb,
        person
    )

    # ---------------------------------------------------------
    # 12. Verbes i → y et -UIR → y
    # ---------------------------------------------------------
    if verb in VERBS_I_Y or verb in VERBS_UIR_Y:
        if person == "el":
            return stem + "ó"

        if person == "ellos":
            return stem + "eron"

    # ---------------------------------------------------------
    # 13. Accent sur le i
    #
    # leer  → leí, leíste, leímos, leísteis
    # creer → creí, creíste, creímos, creísteis
    # caer  → caí, caíste, caímos, caísteis
    # oír   → oí, oíste, oímos, oísteis
    # ---------------------------------------------------------
    if verb in VERBS_I_Y and person in {
        "yo",
        "tu",
        "nosotros",
        "vosotros"
    }:
        stem = stem + "í"

        if person == "yo":
            ending = ""
        elif person == "tu":
            ending = "ste"
        elif person == "nosotros":
            ending = "mos"
        elif person == "vosotros":
            ending = "steis"

    # ---------------------------------------------------------
    # 14. Résultat
    # ---------------------------------------------------------
    return stem + ending



# PRETERITE_E_I = {
# "pedir",
# "sentir",
# "seguir",
# "servir",
# "repetir",
# "vestir",
# "medir",
# "competir",
# "corregir",
# "elegir",
# "conseguir",
# "preferir",
# "mentir",
# }

# PRETERITE_O_U = {
# "dormir",
# "morir",
# }



# PRETERITE_Y_VERBS = {
# "leer",
# "caer",
# "oír",
# "construir",
# "huir",
# "incluir",
# "creer",
# "poseer",
# "destruir",
# "influir",
# "concluir",
#}





# def conjugate_preterite(verb, person):

#     # Irréguliers complets
#     if verb in PRETERITE_FULL_IRREGULAR:
#         return PRETERITE_FULL_IRREGULAR[verb][person]

#     # Radicaux irréguliers
#     if verb in PRETERITE_IRREGULAR_STEMS:

#         stem = PRETERITE_IRREGULAR_STEMS[verb]

#         if verb in {"decir", "traer", "conducir", "producir", "traducir"}:
#             if person == "ellos":
#                 return stem + "eron"

#         if verb == "hacer" and person == "el":
#             return "hizo"

#         return stem + PRETERITE_IRREGULAR_ENDINGS[person]

#     # Changements de radical e -> i des verbes en -IR
#     # uniquement à la 3e personne du singulier et du pluriel
#     if verb in PRETERITE_E_I and person in ("el", "ellos"):

#         stem = verb[:-2]

#         # On modifie le dernier "e" du radical.
#         # Exemple :
#         # elegir -> eleg -> elig
#         # repetir -> repet -> repit
#         # pedir -> ped -> pid
#         pos = stem.rfind("e")

#         if pos != -1:
#             stem = stem[:pos] + "i" + stem[pos + 1:]

#         if person == "el":
#             return stem + "ió"

#         return stem + "ieron"

#     # Changements de radical o -> u des verbes en -IR
#     # uniquement à la 3e personne du singulier et du pluriel
#     if verb in PRETERITE_O_U and person in ("el", "ellos"):

#         stem = verb[:-2]

#         # Exemple :
#         # dormir -> dorm -> durm
#         # morir -> mor -> mur
#         pos = stem.rfind("o")

#         if pos != -1:
#             stem = stem[:pos] + "u" + stem[pos + 1:]

#         if person == "el":
#             return stem + "ió"

#         return stem + "ieron"

#     # Verbes avec insertion de Y
#     if verb in PRETERITE_Y_VERBS and person in ("el", "ellos"):

#         stem = verb[:-2]

#         if person == "el":
#             return stem + "yó"

#         return stem + "yeron"

#     stem = verb[:-2]
#     vtype = verb_type(verb)

#     # Changements orthographiques à la 1re personne du singulier
#     if person == "yo":

#         if verb.endswith("car"):
#             return stem[:-1] + "qué"

#         if verb.endswith("gar"):
#             return stem + "ué"

#         if verb.endswith("zar"):
#             return stem[:-1] + "cé"

#     ending = PRETERITE_ENDINGS[vtype][person]

#     return stem + ending

####################################################################################################
############################################# IMPERFECT ############################################
####################################################################################################

IMPERFECT_ENDINGS = {
"ar": {
"yo": "aba",
"tu": "abas",
"el": "aba",
"nosotros": "ábamos",
"vosotros": "abais",
"ellos": "aban",
},
"er": {
"yo": "ía",
"tu": "ías",
"el": "ía",
"nosotros": "íamos",
"vosotros": "íais",
"ellos": "ían",
},
"ir": {
"yo": "ía",
"tu": "ías",
"el": "ía",
"nosotros": "íamos",
"vosotros": "íais",
"ellos": "ían",
},
}


IMPERFECT_IRREGULAR = {
"ser": {
"yo": "era",
"tu": "eras",
"el": "era",
"nosotros": "éramos",
"vosotros": "erais",
"ellos": "eran",
},
"ir": {
"yo": "iba",
"tu": "ibas",
"el": "iba",
"nosotros": "íbamos",
"vosotros": "ibais",
"ellos": "iban",
},
"ver": {
"yo": "veía",
"tu": "veías",
"el": "veía",
"nosotros": "veíamos",
"vosotros": "veíais",
"ellos": "veían",
},
}



def conjugate_imperfect(verb, person):

    # Seulement trois irréguliers en espagnol
    if verb in IMPERFECT_IRREGULAR:
        return IMPERFECT_IRREGULAR[verb][person]

    stem = verb[:-2]

    ending = IMPERFECT_ENDINGS[verb_type(verb)][person]

    return stem + ending




####################################################################################################
############################################ PARTICIPLE ############################################
####################################################################################################


PARTICIPLE_IRREGULAR = {
"hacer": "hecho",
"decir": "dicho",
"ver": "visto",
"escribir": "escrito",
"poner": "puesto",
"volver": "vuelto",
"abrir": "abierto",
"romper": "roto",
"morir": "muerto",
"cubrir": "cubierto",
"leer": "leído",
"traer": "traído",
"resolver": "resuelto",
}

def participle(verb):

    if verb in PARTICIPLE_IRREGULAR:
        return PARTICIPLE_IRREGULAR[verb]

    if verb.endswith("ar"):
        return verb[:-2] + "ado"

    if verb.endswith("er") or verb.endswith("ir"):
        return verb[:-2] + "ido"

    raise ValueError(f"Verbe inconnu : {verb}")

####################################################################################################
######################################### PRESENT PERFECT ##########################################
####################################################################################################


PERFECT_AUXILIARY = {
"yo": "he",
"tu": "has",
"el": "ha",
"nosotros": "hemos",
"vosotros": "habéis",
"ellos": "han",
}


def conjugate_perfect(verb, person):

    auxiliary = PERFECT_AUXILIARY[person]
    participle_form = participle(verb)

    return auxiliary + " " + participle_form

####################################################################################################
########################################## PLUSCUAMPERFECT #########################################
####################################################################################################

PLUSCUAMPERFECT_AUXILIARY = {
"yo": "había",
"tu": "habías",
"el": "había",
"nosotros": "habíamos",
"vosotros": "habíais",
"ellos": "habían",
}

def conjugate_pluscuamperfect(verb, person):

    auxiliary = PLUSCUAMPERFECT_AUXILIARY[person]
    participle_form = participle(verb)

    return auxiliary + " " + participle_form


####################################################################################################
############################################### FUTURE #############################################
####################################################################################################

FUTURE_IRREGULAR_STEMS = {
"tener": "tendr",
"venir": "vendr",
"poner": "pondr",
"salir": "saldr",
"poder": "podr",
"saber": "sabr",
"querer": "querr",
"hacer": "har",
"decir": "dir",
"haber": "habr",
"caber": "cabr",
"valer": "valdr",
}

def conjugate_future(verb, person):

    if verb in FUTURE_IRREGULAR_STEMS:
        stem = FUTURE_IRREGULAR_STEMS[verb]
    else:
        stem = verb

    endings = {
        "yo": "é",
        "tu": "ás",
        "el": "á",
        "nosotros": "emos",
        "vosotros": "éis",
        "ellos": "án",
    }

    return stem + endings[person]




FUTURE_PERFECT_AUXILIARY = {
"yo": "habré",
"tu": "habrás",
"el": "habrá",
"nosotros": "habremos",
"vosotros": "habréis",
"ellos": "habrán",
}

def conjugate_future_perfect(verb, person):

    auxiliary = FUTURE_PERFECT_AUXILIARY[person]
    participle_form = participle(verb)

    return auxiliary + " " + participle_form



####################################################################################################
########################################### CONDITIONAL ############################################
####################################################################################################

CONDITIONAL_IRREGULAR_STEMS = FUTURE_IRREGULAR_STEMS.copy()

def conjugate_conditional(verb, person):

    if verb in CONDITIONAL_IRREGULAR_STEMS:
        stem = CONDITIONAL_IRREGULAR_STEMS[verb]
    else:
        stem = verb

    endings = {
        "yo": "ía",
        "tu": "ías",
        "el": "ía",
        "nosotros": "íamos",
        "vosotros": "íais",
        "ellos": "ían",
    }

    return stem + endings[person]

CONDITIONAL_PERFECT_AUXILIARY = {
"yo": "habría",
"tu": "habrías",
"el": "habría",
"nosotros": "habríamos",
"vosotros": "habríais",
"ellos": "habrían",
}


def conjugate_conditional_perfect(verb, person):

    auxiliary = CONDITIONAL_PERFECT_AUXILIARY[person]
    participle_form = participle(verb)

    return auxiliary + " " + participle_form


####################################################################################################
########################################### SUBJUNCTIVE ############################################
####################################################################################################


# ============================================================
# SUBJONCTIF PRÉSENT — V16
# Base régulière + transformations composables
# ============================================================


SUBJUNCTIVE_PRESENT_ENDINGS = {
    "ar": {
        "yo": "e",
        "tu": "es",
        "el": "e",
        "nosotros": "emos",
        "vosotros": "éis",
        "ellos": "en",
    },
    "er": {
        "yo": "a",
        "tu": "as",
        "el": "a",
        "nosotros": "amos",
        "vosotros": "áis",
        "ellos": "an",
    },
    "ir": {
        "yo": "a",
        "tu": "as",
        "el": "a",
        "nosotros": "amos",
        "vosotros": "áis",
        "ellos": "an",
    },
}


# ------------------------------------------------------------
# 1. VERBES ENTIÈREMENT IRRÉGULIERS
# ------------------------------------------------------------

SUBJUNCTIVE_PRESENT_IRREGULAR = {
    "ser": {
        "yo": "sea",
        "tu": "seas",
        "el": "sea",
        "nosotros": "seamos",
        "vosotros": "seáis",
        "ellos": "sean",
    },
    "estar": {
        "yo": "esté",
        "tu": "estés",
        "el": "esté",
        "nosotros": "estemos",
        "vosotros": "estéis",
        "ellos": "estén",
    },
    "ir": {
        "yo": "vaya",
        "tu": "vayas",
        "el": "vaya",
        "nosotros": "vayamos",
        "vosotros": "vayáis",
        "ellos": "vayan",
    },
    "haber": {
        "yo": "haya",
        "tu": "hayas",
        "el": "haya",
        "nosotros": "hayamos",
        "vosotros": "hayáis",
        "ellos": "hayan",
    },
    "saber": {
        "yo": "sepa",
        "tu": "sepas",
        "el": "sepa",
        "nosotros": "sepamos",
        "vosotros": "sepáis",
        "ellos": "sepan",
    },
    "dar": {
        "yo": "dé",
        "tu": "des",
        "el": "dé",
        "nosotros": "demos",
        "vosotros": "deis",
        "ellos": "den",
    },
    "ver": {
        "yo": "vea",
        "tu": "veas",
        "el": "vea",
        "nosotros": "veamos",
        "vosotros": "veáis",
        "ellos": "vean",
    },
}


# ------------------------------------------------------------
# 2. OUTILS GÉNÉRIQUES
# ------------------------------------------------------------

# def replace_last_vowel(stem, old, new):
#     """Remplace la dernière occurrence de old par new."""
#     pos = stem.rfind(old)

#     if pos == -1:
#         return stem

#     return stem[:pos] + new + stem[pos + 1:]


# def add_acute_to_last_i(text):
#     """Transforme le dernier i non accentué en í."""
#     pos = text.rfind("i")

#     if pos == -1:
#         return text

#     return text[:pos] + "í" + text[pos + 1:]


# def add_acute_to_last_u(text):
#     """Transforme le dernier u non accentué en ú."""
#     pos = text.rfind("u")

#     if pos == -1:
#         return text

#     return text[:pos] + "ú" + text[pos + 1:]


# ------------------------------------------------------------
# 3. DÉTECTION DES RADICAUX IRRÉGULIERS À PARTIR DE YO
# ------------------------------------------------------------

def get_subjunctive_present_yo_stem(verb):
    """
    Détecte si la forme yo du présent possède une irrégularité
    supplémentaire par rapport aux transformations régulières
    déjà définies dans le moteur.

    Exemples :
        tener  -> tengo  -> teng-
        venir  -> vengo  -> veng-
        hacer  -> hago   -> hag-
        decir  -> digo   -> dig-
        salir  -> salgo  -> salg-
        poner  -> pongo  -> pong-
        traer  -> traigo -> traig-
        caer   -> caigo  -> caig-
        oír    -> oigo   -> oig-

    Renvoie None si le radical peut être construit directement
    avec les familles morphologiques et orthographiques existantes.
    """

    if verb in VERBS_EIR_ACCENT:
        return None

    regular_stem = verb[:-2]

    regular_stem = apply_present_morphological_rules(
        verb,
        "yo",
        regular_stem
    )

    regular_stem = apply_present_orthographic_rules(
        verb,
        "yo",
        regular_stem
    )

    regular_stem = apply_present_accent_rules(
        verb,
        "yo",
        regular_stem
    )

    regular_yo = (
        regular_stem
        + PRESENT_ENDINGS[verb_type(verb)]["yo"]
    )

    actual_yo = conjugate_present(verb, "yo")

    if actual_yo != regular_yo and actual_yo.endswith("o"):
        return actual_yo[:-1]

    return None


# ------------------------------------------------------------
# 4. TRANSFORMATIONS MORPHOLOGIQUES DU SUBJONCTIF
# ------------------------------------------------------------

def apply_subjunctive_present_morphological_rules(
    verb,
    person,
    stem
):
    """
    Applique les changements de radical pertinents au subjonctif.

    e -> ie, o -> ue, u -> ue :
        changement hors nosotros/vosotros.

    e -> i :
        changement pour les personnes prévues par la famille.

    Pour les verbes en -ir :
        e -> ie devient e -> i à nosotros/vosotros ;
        o -> ue devient o -> u à nosotros/vosotros.

    Les transformations sont indépendantes afin de permettre
    les combinaisons de familles.
    """

    is_nosotros_vosotros = person in (
        "nosotros",
        "vosotros"
    )

    is_ir = verb.endswith("ir")

    # e -> ie
    if verb in VERBS_E_IE:
        if not is_nosotros_vosotros:
            stem = replace_last_vowel(stem, "e", "ie")
        elif is_ir:
            stem = replace_last_vowel(stem, "e", "i")

    # o -> ue
    if verb in VERBS_O_UE:
        if not is_nosotros_vosotros:
            stem = replace_last_vowel(stem, "o", "ue")
        elif is_ir:
            stem = replace_last_vowel(stem, "o", "u")

    # u -> ue
    if verb in VERBS_U_UE and not is_nosotros_vosotros:
        stem = replace_last_vowel(stem, "u", "ue")

    # e -> i
    if verb in VERBS_E_I:
        stem = replace_last_vowel(stem, "e", "i")

    return stem


# ------------------------------------------------------------
# 5. MODIFICATIONS ORTHOGRAPHIQUES DU SUBJONCTIF
# ------------------------------------------------------------

def apply_subjunctive_present_orthographic_rules(
    verb,
    stem
):
    """
    Applique les changements orthographiques nécessaires
    avant les terminaisons du subjonctif.

    Contrairement au présent indicatif, ces modifications peuvent
    concerner plusieurs personnes.
    """

    # c -> zc
    # conocer -> conozca
    # conducir -> conduzca
    if verb in VERBS_C_ZC:
        if stem.endswith("c"):
            stem = stem[:-1] + "zc"
        else:
            stem = stem + "zc"

    # c -> z
    # vencer -> venza
    # torcer -> tuerza
    elif verb in VERBS_C_Z:
        if stem.endswith("c"):
            stem = stem[:-1] + "z"
        else:
            stem = stem + "z"

    # c -> qu
    # buscar -> busque
    elif verb.endswith("car"):
        if stem.endswith("c"):
            stem = stem[:-1] + "qu"

    # g -> gu
    # pagar -> pague
    elif verb.endswith("gar"):
        if stem.endswith("g"):
            stem = stem + "u"

    # z -> c
    # empezar -> empiece
    elif verb.endswith("zar"):
        if stem.endswith("z"):
            stem = stem[:-1] + "c"

    # g -> j
    # coger -> coja
    # elegir -> elija
    elif (
        verb in VERBS_G_J
        or verb.endswith("ger")
        or verb.endswith("gir")
    ):
        if stem.endswith("g"):
            stem = stem[:-1] + "j"

    # gu -> g
    # seguir -> siga
    # distinguir -> distinga
    elif (
        verb in VERBS_GUIR_G
        or verb.endswith("guir")
    ):
        if stem.endswith("gu"):
            stem = stem[:-2] + "g"

    # qu -> c
    # delinquir -> delinca
    elif (
        verb in VERBS_QUIR_C
        or verb.endswith("quir")
    ):
        if stem.endswith("qu"):
            stem = stem[:-2] + "c"

    return stem


# ------------------------------------------------------------
# 6. VERBES EN -UIR : INSERTION DE Y
# ------------------------------------------------------------

def apply_subjunctive_present_uir_rule(verb, stem):
    """
    Construye el radical des verbes en -uir :
        construir -> construy-
        incluir   -> incluy-
        huir      -> huy-

    Les verbes en -guir suivent leur règle orthographique propre.
    """

    if verb.endswith("uir") and not verb.endswith("guir"):
        return stem #+ "y"

    return stem


# ------------------------------------------------------------
# 7. ACCENTUATION -IAR, -UAR ET -EÍR
# ------------------------------------------------------------

def apply_subjunctive_present_accent_rules(
    verb,
    person,
    stem
):
    """
    Accentuation du subjonctif présent.

    -iar :
        enviar -> envíe, envíes, envíe, enviemos,
                  enviéis, envíen

    -uar :
        continuar -> continúe, continúes, continúe,
                     continuemos, continuéis, continúen

    -eír :
        reír -> ría, rías, ría, riamos, riáis, rían
    """

    accented_persons = ("yo", "tu", "el", "ellos")

    # -iar
    if (
        verb in VERBS_IAR_ACCENT
        and person in accented_persons
    ):
        stem = add_acute_to_last_i(stem)

    # -uar
    if (
        verb in VERBS_UAR_ACCENT
        and person in accented_persons
    ):
        stem = add_acute_to_last_u(stem)

    # -eír : le radical devient i, avec accent sauf à
    # nosotros et vosotros.
    if verb in VERBS_EIR_ACCENT:
        stem = replace_last_vowel(stem, "e", "i")

        if person in accented_persons:
            stem = add_acute_to_last_i(stem)

    return stem


# ------------------------------------------------------------
# 8. CONJUGAISON DU SUBJONCTIF PRÉSENT
# ------------------------------------------------------------

def conjugate_subjunctive_present(verb, person):

    # Étape 1 : verbes entièrement irréguliers
    if verb in SUBJUNCTIVE_PRESENT_IRREGULAR:
        return SUBJUNCTIVE_PRESENT_IRREGULAR[verb][person]

    # Étape 2 : déterminer la terminaison régulière
    vtype = verb_type(verb)
    ending = SUBJUNCTIVE_PRESENT_ENDINGS[vtype][person]

    # Étape 3 : rechercher un radical irrégulier dérivable
    # de la forme yo du présent.
    yo_stem = get_subjunctive_present_yo_stem(verb)

    if yo_stem is not None:
        # Le radical irrégulier contient déjà la modification
        # particulière de yo : ne pas lui appliquer une deuxième
        # fois e -> ie, o -> ue ou e -> i.
        stem = yo_stem

    else:
        # Étape 4 : radical régulier
        stem = verb[:-2]

        # Étape 5 : changements morphologiques
        stem = apply_subjunctive_present_morphological_rules(
            verb,
            person,
            stem
        )

    # Étape 6 : modifications orthographiques
    stem = apply_subjunctive_present_orthographic_rules(
        verb,
        stem
    )

    # Étape 7 : insertion de y pour les verbes en -uir
    stem = apply_subjunctive_present_uir_rule(
        verb,
        stem
    )

    # Étape 8 : accentuation particulière
    stem = apply_subjunctive_present_accent_rules(
        verb,
        person,
        stem
    )

    # Étape 9 : terminaison
    return stem + ending




SUBJUNCTIVE_PERFECT_AUXILIARY = {
"yo": "haya",
"tu": "hayas",
"el": "haya",
"nosotros": "hayamos",
"vosotros": "hayáis",
"ellos": "hayan",
}


def conjugate_subjunctive_perfect(verb, person):

    auxiliary = SUBJUNCTIVE_PERFECT_AUXILIARY[person]

    return auxiliary + " " + participle(verb)



SUBJUNCTIVE_IMPERFECT_ENDINGS = {
    "ra": {
        "yo": "ra",
        "tu": "ras",
        "el": "ra",
        "nosotros": "ramos",
        "vosotros": "rais",
        "ellos": "ran",
    },
    "se": {
        "yo": "se",
        "tu": "ses",
        "el": "se",
        "nosotros": "semos",
        "vosotros": "seis",
        "ellos": "sen",
    },
}





def conjugate_subjunctive_imperfect(verb, person):

    preterite_ellos = conjugate_preterite(verb, "ellos")

    if not preterite_ellos.endswith("ron"):
        raise ValueError(
            f"Impossible de construire le subjonctif imparfait pour : {verb}"
        )

    if person == "nosotros":
        stem = preterite_ellos[:-4]

        if verb_type(verb) == "ar":
            return stem + "áramos"

        return stem + "éramos"

    endings = {
        "yo": "ra",
        "tu": "ras",
        "el": "ra",
        "vosotros": "rais",
        "ellos": "ran",
    }

    if person not in endings:
        raise ValueError(f"Personne inconnue : {person}")

    stem = preterite_ellos[:-3]
    return stem + endings[person]


SUBJUNCTIVE_PLUPERFECT_AUXILIARY = {
"yo": "hubiera",
"tu": "hubieras",
"el": "hubiera",
"nosotros": "hubiéramos",
"vosotros": "hubierais",
"ellos": "hubieran",
}

def conjugate_subjunctive_pluperfect(verb, person):

    auxiliary = SUBJUNCTIVE_PLUPERFECT_AUXILIARY[person]

    return auxiliary + " " + participle(verb)


####################################################################################################
############################################ IMPERATIVE ############################################
####################################################################################################



IMPERATIVE_AFFIRMATIVE_IRREGULAR = {
    "tener": {"tu": "ten"},
    "venir": {"tu": "ven"},
    "decir": {"tu": "di"},
    "hacer": {"tu": "haz"},
    "ir": {"tu": "ve"},
    "poner": {"tu": "pon"},
    "salir": {"tu": "sal"},
    "ser": {"tu": "sé"},
    "haber": {"tu": "he"},
}

IMPERATIVE_PERSONS = [
    "tu",
    "el",
    "nosotros",
    "vosotros",
    "ellos",
]


def conjugate_imperative_affirmative(verb, person):

    if person not in IMPERATIVE_PERSONS:
        raise ValueError(f"Personne inconnue : {person}")

    if person == "tu":

        if verb in IMPERATIVE_AFFIRMATIVE_IRREGULAR:
            return IMPERATIVE_AFFIRMATIVE_IRREGULAR[verb]["tu"]

        # Tú : généralement la 3e personne du singulier du présent.
        return conjugate_present(verb, "el")

    if person == "el":
        # Usted : subjonctif présent.
        return conjugate_subjunctive_present(verb, "el")

    if person == "nosotros":
        # Nosotros : subjonctif présent.
        return conjugate_subjunctive_present(verb, "nosotros")

    if person == "vosotros":
        # Infinitif sans r final + d.
        # hablar -> hablad ; comer -> comed ; ir -> id
        return verb[:-1] + "d"

    if person == "ellos":
        # Ustedes : subjonctif présent.
        return conjugate_subjunctive_present(verb, "ellos")


def conjugate_imperative_negative(verb, person):

    if person not in IMPERATIVE_PERSONS:
        raise ValueError(f"Personne inconnue : {person}")

    # Toutes les formes négatives utilisent le subjonctif présent.
    return "no " + conjugate_subjunctive_present(verb, person)

####################################################################################################
########################################## MOTEUR PRINCIPAL#########################################
####################################################################################################

def conjugate(verb, tense, person):

    if tense == "presente":
        return conjugate_present(verb, person)

    if tense == "preterito":
        return conjugate_preterite(verb, person)

    if tense == "imperfecto":
        return conjugate_imperfect(verb, person)

    if tense == "futuro":
            return conjugate_future(verb, person)

    if tense == "condicional":
            return conjugate_conditional(verb, person)

    if tense == "perfecto":
        return conjugate_perfect(verb, person)

    if tense == "pluscuamperfecto":
        return conjugate_pluscuamperfect(verb, person)

    if tense == "futuro_perfecto":
     return conjugate_future_perfect(verb, person)

    if tense == "condicional_perfecto":
        return conjugate_conditional_perfect(verb, person)

    if tense == "subjuntivo_presente":
        return conjugate_subjunctive_present(verb, person)

    if tense == "subjuntivo_imperfecto":
        return conjugate_subjunctive_imperfect(verb, person)

    if tense == "subjuntivo_pluscuamperfecto":
        return conjugate_subjunctive_pluperfect(verb, person)

    if tense == "subjuntivo_perfecto":
        return conjugate_subjunctive_perfect(verb, person)

    if tense == "imperativo_afirmativo":
        return conjugate_imperative_affirmative(verb, person)

    if tense == "imperativo_negativo":
        return conjugate_imperative_negative(verb, person)



    raise ValueError(f"Temps inconnu : {tense}")





# ============================================================
# CONJUGAISON DES VERBES PRONOMINAUX
# Exemples : levantarse, acostarse, vestirse, ponerse
# ============================================================

REFLEXIVE_PRONOUNS = {
    "yo": "me",
    "tu": "te",
    "el": "se",
    "nosotros": "nos",
    "vosotros": "os",
    "ellos": "se",
}

COMPOUND_TENSES = {
    "perfecto",
    "pluscuamperfecto",
    "futuro_perfecto",
    "condicional_perfecto",
    "subjuntivo_perfecto",
    "subjuntivo_pluscuamperfecto",
}

VOWELS = "aeiouáéíóúü"
STRONG_VOWELS = "aeoáéó"
ACCENT_MAP = {
    "a": "á",
    "e": "é",
    "i": "í",
    "o": "ó",
    "u": "ú",
    "á": "á",
    "é": "é",
    "í": "í",
    "ó": "ó",
    "ú": "ú",
}


def _vowel_groups(word):
    """
    Repère approximativement les noyaux vocaliques espagnols.
    Cette fonction sert à conserver l'accent tonique lorsqu'un
    pronom est ajouté à un impératif.
    """
    groups = []
    i = 0

    while i < len(word):
        if word[i].lower() not in VOWELS:
            i += 1
            continue

        start = i
        i += 1

        while i < len(word) and word[i].lower() in VOWELS:
            previous = word[i - 1].lower()
            current = word[i].lower()

            # Une voyelle faible accentuée forme un hiatus.
            if previous in "íú" or current in "íú":
                break

            # Deux voyelles fortes forment deux syllabes.
            if previous in STRONG_VOWELS and current in STRONG_VOWELS:
                break

            i += 1

        groups.append((start, i - 1))

    return groups


def _stressed_vowel_index(word):
    """
    Retourne l'index de la voyelle tonique.
    Utilise l'accent écrit s'il existe, sinon les règles
    générales d'accentuation de l'espagnol.
    """
    for i, char in enumerate(word):
        if char in "áéíóú":
            return i

    groups = _vowel_groups(word)

    if not groups:
        raise ValueError(
            f"Impossible de déterminer l'accent tonique de : {word}"
        )

    # Sans accent écrit, les mots terminés par une voyelle,
    # n ou s sont normalement accentués sur l'avant-dernière
    # syllabe. Les autres le sont sur la dernière.
    if word[-1].lower() in "aeiouns":
        group = groups[-2] if len(groups) >= 2 else groups[-1]
    else:
        group = groups[-1]

    # Pour un groupe vocalique, on accentue la voyelle forte
    # lorsqu'il y en a une ; sinon, la première voyelle du groupe.
    for i in range(group[0], group[1] + 1):
        if word[i].lower() in STRONG_VOWELS:
            return i

    return group[0]


def _add_written_accent(word, index):
    """Ajoute un accent aigu à la voyelle située à index."""
    char = word[index]
    accented = ACCENT_MAP.get(char.lower())

    if accented is None:
        return word

    return word[:index] + accented + word[index + 1:]


def _attach_clitic_preserving_stress(original, stem, pronoun):
    """
    Ajoute le pronom à l'impératif en conservant l'accent tonique.

    original : forme conjuguée avant transformation
    stem     : forme après suppression éventuelle de s ou d
    pronoun  : te, se, nos ou os
    """
    stressed_index = _stressed_vowel_index(original)
    result = stem + pronoun

    # Si la forme d'origine possède déjà un accent écrit,
    # celui-ci reste dans le résultat et conserve le tonique.
    if any(char in "áéíóú" for char in original):
        return result

    # Sinon, comparons la voyelle tonique originale à la
    # voyelle tonique que les règles normales donneraient
    # au nouveau mot.
    new_stressed_index = _stressed_vowel_index(result)

    if new_stressed_index != stressed_index:
        result = _add_written_accent(result, stressed_index)

    return result


def attach_reflexive_pronoun(conjugated, pronoun, person, base_verb):
    """
    Attache le pronom aux impératifs affirmatifs.
    """
    # Exception importante : l'impératif de irse.
    if base_verb == "ir":
        irse_forms = {
            "tu": "vete",
            "el": "váyase",
            "nosotros": "vámonos",
            "vosotros": "idos",
            "ellos": "váyanse",
        }
        return irse_forms[person]

    # Nosotros : on supprime le s final avant "nos".
    if person == "nosotros":
        stem = (
            conjugated[:-1]
            if conjugated.endswith("s")
            else conjugated
        )
        return _attach_clitic_preserving_stress(
            conjugated, stem, pronoun
        )

    # Vosotros : on supprime normalement le d final avant "os".
    if person == "vosotros":
        stem = (
            conjugated[:-1]
            if conjugated.endswith("d")
            else conjugated
        )
        return _attach_clitic_preserving_stress(
            conjugated, stem, pronoun
        )

    # Tú, usted et ustedes : on ajoute directement le pronom.
    return _attach_clitic_preserving_stress(
        conjugated, conjugated, pronoun
    )


def conjugate_pronominal(verb, tense, person):
    """
    Conjugue un verbe pronominal en utilisant le moteur existant.

    Exemples :
        conjugate_pronominal("levantarse", "presente", "yo")
        -> "me levanto"

        conjugate_pronominal("levantarse",
                             "imperativo_afirmativo", "tu")
        -> "levántate"
    """
    if person not in REFLEXIVE_PRONOUNS:
        raise ValueError(f"Personne inconnue : {person}")

    if not isinstance(verb, str):
        raise TypeError("Le verbe doit être une chaîne de caractères.")

    verb = verb.strip().lower()

    if not verb.endswith("se") or len(verb) <= 2:
        raise ValueError(
            f"Le verbe doit être pronominal et se terminer par 'se' : {verb}"
        )

    base_verb = verb[:-2]
    pronoun = REFLEXIVE_PRONOUNS[person]

    # Impératif affirmatif : le pronom se rattache au verbe.
    if tense == "imperativo_afirmativo":
        conjugated = conjugate(base_verb, tense, person)
        return attach_reflexive_pronoun(
            conjugated, pronoun, person, base_verb
        )

    # Tous les autres temps placent le pronom avant le verbe
    # ou avant l'auxiliaire.
    conjugated = conjugate(base_verb, tense, person)

    if tense == "imperativo_negativo":
        # Le moteur renvoie déjà "no + verbe".
        # On insère le pronom après "no".
        form = conjugated.removeprefix("no ")
        return f"no {pronoun} {form}"

    # Temps composés : me he levantado, se había vestido, etc.
    if tense in COMPOUND_TENSES:
        return f"{pronoun} {conjugated}"

    # Temps simples : me levanto, te acostabas, se vista, etc.
    return f"{pronoun} {conjugated}"














#########################################################################
############################ EXERCISES ##################################
#########################################################################
VERBS = [
"hablar",
"trabajar",
"estudiar",
"caminar",
"comprar",
"comer",
"beber",
"aprender",
"vivir",
"escribir",

"pensar",
"cerrar",
"empezar",
"comenzar",
"entender",
"querer",
"preferir",
"sentir",
"perder",

"poder",
"volver",
"dormir",
"contar",
"encontrar",
"recordar",
"mostrar",
"costar",
"soñar",

"jugar",

"pedir",
"servir",
"repetir",
"seguir",
"vestir",
"medir",
"competir",
"corregir",
"elegir",
"conseguir",

"ser",
"estar",
"ir",
"tener",
"venir",
"hacer",
"decir",
"salir",
"poner",
"saber",
"ver",
"dar",

"andar",
"traer",
"conducir",
"producir",

"leer",
"caer",
"oír",
"construir",

]





# Liste complète des verbes proposés dans les exercices
ALL_VERBS = list(dict.fromkeys(
    list(VERBS)
    + list(VERBS_E_IE)
    + list(VERBS_O_UE)
    + list(VERBS_U_UE)
    + list(VERBS_E_I)
    + list(VERBS_C_ZC)
    + list(VERBS_C_Z)
    + list(VERBS_G_J)
    + list(VERBS_GUIR_G)
    + list(VERBS_QUIR_C)
    + list(VERBS_IAR_ACCENT)
    + list(VERBS_UAR_ACCENT)
    + list(VERBS_EIR_ACCENT)
    + list(VERBS_I_Y)
    + list(VERBS_I_LOSS)
    + list(VERBS_O_U)
    + list(VERBS_UIR_Y)
))

