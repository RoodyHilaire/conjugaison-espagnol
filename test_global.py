from moteur import conjugate

####################################################################################################
############################################### TEST ###############################################
####################################################################################################

def test(expected, verb, tense, person):

    result = conjugate(verb, tense, person)

    if result != expected:
        print(
            f"ERREUR : {verb} / {tense} / {person} "
            f"=> obtenu '{result}', attendu '{expected}'"
        )
        return False

    return True

def run_global_tests():

    tests = [

        # ----------------------------------------------------
        # PRESENT REGULIER
        # ----------------------------------------------------

        ("hablo", "hablar", "presente", "yo"),
        ("hablas", "hablar", "presente", "tu"),
        ("habla", "hablar", "presente", "el"),
        ("hablamos", "hablar", "presente", "nosotros"),
        ("habláis", "hablar", "presente", "vosotros"),
        ("hablan", "hablar", "presente", "ellos"),

        ("como", "comer", "presente", "yo"),
        ("comes", "comer", "presente", "tu"),
        ("come", "comer", "presente", "el"),
        ("comemos", "comer", "presente", "nosotros"),
        ("coméis", "comer", "presente", "vosotros"),
        ("comen", "comer", "presente", "ellos"),

        ("vivo", "vivir", "presente", "yo"),
        ("vives", "vivir", "presente", "tu"),
        ("vive", "vivir", "presente", "el"),
        ("vivimos", "vivir", "presente", "nosotros"),
        ("vivís", "vivir", "presente", "vosotros"),
        ("viven", "vivir", "presente", "ellos"),

        # ----------------------------------------------------
        # PRESENT STEM CHANGE
        # ----------------------------------------------------

        ("pienso", "pensar", "presente", "yo"),
        ("piensas", "pensar", "presente", "tu"),
        ("piensa", "pensar", "presente", "el"),
        ("pensamos", "pensar", "presente", "nosotros"),
        ("pensáis", "pensar", "presente", "vosotros"),
        ("piensan", "pensar", "presente", "ellos"),

        ("puedo", "poder", "presente", "yo"),
        ("puedes", "poder", "presente", "tu"),
        ("puede", "poder", "presente", "el"),
        ("podemos", "poder", "presente", "nosotros"),
        ("podéis", "poder", "presente", "vosotros"),
        ("pueden", "poder", "presente", "ellos"),

        ("pido", "pedir", "presente", "yo"),
        ("pides", "pedir", "presente", "tu"),
        ("pide", "pedir", "presente", "el"),
        ("pedimos", "pedir", "presente", "nosotros"),
        ("pedís", "pedir", "presente", "vosotros"),
        ("piden", "pedir", "presente", "ellos"),

        ("juego", "jugar", "presente", "yo"),
        ("juegas", "jugar", "presente", "tu"),
        ("juega", "jugar", "presente", "el"),
        ("jugamos", "jugar", "presente", "nosotros"),
        ("jugáis", "jugar", "presente", "vosotros"),
        ("juegan", "jugar", "presente", "ellos"),

        # ----------------------------------------------------
        # PRESENT IRREGULIERS
        # ----------------------------------------------------

        ("soy", "ser", "presente", "yo"),
        ("eres", "ser", "presente", "tu"),
        ("es", "ser", "presente", "el"),
        ("somos", "ser", "presente", "nosotros"),
        ("sois", "ser", "presente", "vosotros"),
        ("son", "ser", "presente", "ellos"),

        ("tengo", "tener", "presente", "yo"),
        ("tienes", "tener", "presente", "tu"),
        ("tiene", "tener", "presente", "el"),
        ("tenemos", "tener", "presente", "nosotros"),
        ("tenéis", "tener", "presente", "vosotros"),
        ("tienen", "tener", "presente", "ellos"),

        ("vengo", "venir", "presente", "yo"),
        ("vienes", "venir", "presente", "tu"),
        ("viene", "venir", "presente", "el"),
        ("venimos", "venir", "presente", "nosotros"),
        ("venís", "venir", "presente", "vosotros"),
        ("vienen", "venir", "presente", "ellos"),

        # ----------------------------------------------------
        # PRETERITO REGULIER
        # ----------------------------------------------------

        ("hablé", "hablar", "preterito", "yo"),
        ("hablaste", "hablar", "preterito", "tu"),
        ("habló", "hablar", "preterito", "el"),
        ("hablamos", "hablar", "preterito", "nosotros"),
        ("hablasteis", "hablar", "preterito", "vosotros"),
        ("hablaron", "hablar", "preterito", "ellos"),
        ("compraron", "comprar", "preterito", "ellos"),

        ("comí", "comer", "preterito", "yo"),
        ("comiste", "comer", "preterito", "tu"),
        ("comió", "comer", "preterito", "el"),
        ("comimos", "comer", "preterito", "nosotros"),
        ("comisteis", "comer", "preterito", "vosotros"),
        ("comieron", "comer", "preterito", "ellos"),

        # ----------------------------------------------------
        # PRETERITO IRREGULIER
        # ----------------------------------------------------

        ("tuve", "tener", "preterito", "yo"),
        ("tuviste", "tener", "preterito", "tu"),
        ("tuvo", "tener", "preterito", "el"),
        ("tuvimos", "tener", "preterito", "nosotros"),
        ("tuvisteis", "tener", "preterito", "vosotros"),
        ("tuvieron", "tener", "preterito", "ellos"),

        ("pude", "poder", "preterito", "yo"),
        ("pudiste", "poder", "preterito", "tu"),
        ("pudo", "poder", "preterito", "el"),
        ("pudimos", "poder", "preterito", "nosotros"),
        ("pudisteis", "poder", "preterito", "vosotros"),
        ("pudieron", "poder", "preterito", "ellos"),

        ("hice", "hacer", "preterito", "yo"),
        ("hiciste", "hacer", "preterito", "tu"),
        ("hizo", "hacer", "preterito", "el"),
        ("hicimos", "hacer", "preterito", "nosotros"),
        ("hicisteis", "hacer", "preterito", "vosotros"),
        ("hicieron", "hacer", "preterito", "ellos"),

        ("dije", "decir", "preterito", "yo"),
        ("dijiste", "decir", "preterito", "tu"),
        ("dijo", "decir", "preterito", "el"),
        ("dijimos", "decir", "preterito", "nosotros"),
        ("dijisteis", "decir", "preterito", "vosotros"),
        ("dijeron", "decir", "preterito", "ellos"),

        ("vine", "venir", "preterito", "yo"),
        ("viniste", "venir", "preterito", "tu"),
        ("vino", "venir", "preterito", "el"),
        ("vinimos", "venir", "preterito", "nosotros"),
        ("vinisteis", "venir", "preterito", "vosotros"),
        ("vinieron", "venir", "preterito", "ellos"),

        ("fui", "ser", "preterito", "yo"),
        ("fuiste", "ser", "preterito", "tu"),
        ("fue", "ser", "preterito", "el"),
        ("fuimos", "ser", "preterito", "nosotros"),
        ("fuisteis", "ser", "preterito", "vosotros"),
        ("fueron", "ser", "preterito", "ellos"),

        # ----------------------------------------------------
        # PRETERITO STEM CHANGE IR
        # ----------------------------------------------------

        ("pedí", "pedir", "preterito", "yo"),
        ("pediste", "pedir", "preterito", "tu"),
        ("pidió", "pedir", "preterito", "el"),
        ("pedimos", "pedir", "preterito", "nosotros"),
        ("pedisteis", "pedir", "preterito", "vosotros"),
        ("pidieron", "pedir", "preterito", "ellos"),

        ("dormí", "dormir", "preterito", "yo"),
        ("dormiste", "dormir", "preterito", "tu"),
        ("durmió", "dormir", "preterito", "el"),
        ("dormimos", "dormir", "preterito", "nosotros"),
        ("dormisteis", "dormir", "preterito", "vosotros"),
        ("durmieron", "dormir", "preterito", "ellos"),

        # ----------------------------------------------------
        # PRETERITO ORTHOGRAPHIQUE
        # ----------------------------------------------------

        ("empecé", "empezar", "preterito", "yo"),
        ("busqué", "buscar", "preterito", "yo"),
        ("llegué", "llegar", "preterito", "yo"),

        # ----------------------------------------------------
        # PRETERITO Y
        # ----------------------------------------------------

        ("leyó", "leer", "preterito", "el"),
        ("leyeron", "leer", "preterito", "ellos"),

        ("cayó", "caer", "preterito", "el"),
        ("cayeron", "caer", "preterito", "ellos"),

        ("oyó", "oír", "preterito", "el"),
        ("oyeron", "oír", "preterito", "ellos"),

        ("construyó", "construir", "preterito", "el"),
        ("construyeron", "construir", "preterito", "ellos"),

        # ====================================================
        # V5 - IMPERFECTO REGULIER
        # ====================================================

        ("hablaba", "hablar", "imperfecto", "yo"),
        ("hablabas", "hablar", "imperfecto", "tu"),
        ("hablaba", "hablar", "imperfecto", "el"),
        ("hablábamos", "hablar", "imperfecto", "nosotros"),
        ("hablabais", "hablar", "imperfecto", "vosotros"),
        ("hablaban", "hablar", "imperfecto", "ellos"),

        ("comía", "comer", "imperfecto", "yo"),
        ("comías", "comer", "imperfecto", "tu"),
        ("comía", "comer", "imperfecto", "el"),
        ("comíamos", "comer", "imperfecto", "nosotros"),
        ("comíais", "comer", "imperfecto", "vosotros"),
        ("comían", "comer", "imperfecto", "ellos"),

        ("vivía", "vivir", "imperfecto", "yo"),
        ("vivías", "vivir", "imperfecto", "tu"),
        ("vivía", "vivir", "imperfecto", "el"),
        ("vivíamos", "vivir", "imperfecto", "nosotros"),
        ("vivíais", "vivir", "imperfecto", "vosotros"),
        ("vivían", "vivir", "imperfecto", "ellos"),

        # ====================================================
        # V5 - IMPERFECTO STEM-CHANGE : AUCUN CHANGEMENT
        # ====================================================

        ("pensaba", "pensar", "imperfecto", "yo"),
        ("pensabas", "pensar", "imperfecto", "tu"),
        ("pensábamos", "pensar", "imperfecto", "nosotros"),
        ("pensabais", "pensar", "imperfecto", "vosotros"),
        ("pensaban", "pensar", "imperfecto", "ellos"),

        ("podía", "poder", "imperfecto", "yo"),
        ("podías", "poder", "imperfecto", "tu"),
        ("podíamos", "poder", "imperfecto", "nosotros"),
        ("podíais", "poder", "imperfecto", "vosotros"),
        ("podían", "poder", "imperfecto", "ellos"),

        ("pedía", "pedir", "imperfecto", "yo"),
        ("pedías", "pedir", "imperfecto", "tu"),
        ("pedíamos", "pedir", "imperfecto", "nosotros"),
        ("pedíais", "pedir", "imperfecto", "vosotros"),
        ("pedían", "pedir", "imperfecto", "ellos"),

        # ====================================================
        # V5 - IMPERFECTO IRREGULIERS
        # ====================================================

        ("era", "ser", "imperfecto", "yo"),
        ("eras", "ser", "imperfecto", "tu"),
        ("era", "ser", "imperfecto", "el"),
        ("éramos", "ser", "imperfecto", "nosotros"),
        ("erais", "ser", "imperfecto", "vosotros"),
        ("eran", "ser", "imperfecto", "ellos"),

        ("iba", "ir", "imperfecto", "yo"),
        ("ibas", "ir", "imperfecto", "tu"),
        ("iba", "ir", "imperfecto", "el"),
        ("íbamos", "ir", "imperfecto", "nosotros"),
        ("ibais", "ir", "imperfecto", "vosotros"),
        ("iban", "ir", "imperfecto", "ellos"),

        ("veía", "ver", "imperfecto", "yo"),
        ("veías", "ver", "imperfecto", "tu"),
        ("veía", "ver", "imperfecto", "el"),
        ("veíamos", "ver", "imperfecto", "nosotros"),
        ("veíais", "ver", "imperfecto", "vosotros"),
        ("veían", "ver", "imperfecto", "ellos"),

        # ====================================================
        # TESTS SUPPLEMENTAIRES - V5
        # Verbes avec plusieurs e / o dans le radical
        # ====================================================

        # ----------------------------------------------------
        # REPETIR - PRESENT
        # ----------------------------------------------------

        ("repito", "repetir", "presente", "yo"),
        ("repites", "repetir", "presente", "tu"),
        ("repite", "repetir", "presente", "el"),
        ("repetimos", "repetir", "presente", "nosotros"),
        ("repetís", "repetir", "presente", "vosotros"),
        ("repiten", "repetir", "presente", "ellos"),

        # ----------------------------------------------------
        # REPETIR - PRETERITO
        # ----------------------------------------------------

        ("repetí", "repetir", "preterito", "yo"),
        ("repetiste", "repetir", "preterito", "tu"),
        ("repitió", "repetir", "preterito", "el"),
        ("repetimos", "repetir", "preterito", "nosotros"),
        ("repetisteis", "repetir", "preterito", "vosotros"),
        ("repitieron", "repetir", "preterito", "ellos"),

        # ----------------------------------------------------
        # ELEGIR - PRESENT
        # ----------------------------------------------------

        ("elijo", "elegir", "presente", "yo"),
        ("eliges", "elegir", "presente", "tu"),
        ("elige", "elegir", "presente", "el"),
        ("elegimos", "elegir", "presente", "nosotros"),
        ("elegís", "elegir", "presente", "vosotros"),
        ("eligen", "elegir", "presente", "ellos"),

        # ----------------------------------------------------
        # ELEGIR - PRETERITO
        # ----------------------------------------------------

        ("elegí", "elegir", "preterito", "yo"),
        ("elegiste", "elegir", "preterito", "tu"),
        ("eligió", "elegir", "preterito", "el"),
        ("elegimos", "elegir", "preterito", "nosotros"),
        ("elegisteis", "elegir", "preterito", "vosotros"),
        ("eligieron", "elegir", "preterito", "ellos"),

        # ----------------------------------------------------
        # PREFERIR - PRESENT
        # ----------------------------------------------------

        ("prefiero", "preferir", "presente", "yo"),
        ("prefieres", "preferir", "presente", "tu"),
        ("prefiere", "preferir", "presente", "el"),
        ("preferimos", "preferir", "presente", "nosotros"),
        ("preferís", "preferir", "presente", "vosotros"),
        ("prefieren", "preferir", "presente", "ellos"),

        # ----------------------------------------------------
        # PREFERIR - PRETERITO
        # ----------------------------------------------------

        ("preferí", "preferir", "preterito", "yo"),
        ("preferiste", "preferir", "preterito", "tu"),
        ("prefirió", "preferir", "preterito", "el"),
        ("preferimos", "preferir", "preterito", "nosotros"),
        ("preferisteis", "preferir", "preterito", "vosotros"),
        ("prefirieron", "preferir", "preterito", "ellos"),

        # ----------------------------------------------------
        # DORMIR - PRESENT
        # ----------------------------------------------------

        ("duermo", "dormir", "presente", "yo"),
        ("duermes", "dormir", "presente", "tu"),
        ("duerme", "dormir", "presente", "el"),
        ("dormimos", "dormir", "presente", "nosotros"),
        ("dormís", "dormir", "presente", "vosotros"),
        ("duermen", "dormir", "presente", "ellos"),

        # ----------------------------------------------------
        # DORMIR - PRETERITO
        # ----------------------------------------------------

        ("dormí", "dormir", "preterito", "yo"),
        ("dormiste", "dormir", "preterito", "tu"),
        ("durmió", "dormir", "preterito", "el"),
        ("dormimos", "dormir", "preterito", "nosotros"),
        ("dormisteis", "dormir", "preterito", "vosotros"),
        ("durmieron", "dormir", "preterito", "ellos"),

        # ----------------------------------------------------
        # SENTIR - PRESENT
        # ----------------------------------------------------

        ("siento", "sentir", "presente", "yo"),
        ("sientes", "sentir", "presente", "tu"),
        ("siente", "sentir", "presente", "el"),
        ("sentimos", "sentir", "presente", "nosotros"),
        ("sentís", "sentir", "presente", "vosotros"),
        ("sienten", "sentir", "presente", "ellos"),

        # ----------------------------------------------------
        # SENTIR - PRETERITO
        # ----------------------------------------------------

        ("sentí", "sentir", "preterito", "yo"),
        ("sentiste", "sentir", "preterito", "tu"),
        ("sintió", "sentir", "preterito", "el"),
        ("sentimos", "sentir", "preterito", "nosotros"),
        ("sentisteis", "sentir", "preterito", "vosotros"),
        ("sintieron", "sentir", "preterito", "ellos"),

        # ----------------------------------------------------
        # MORIR - PRESENT
        # ----------------------------------------------------

        ("muero", "morir", "presente", "yo"),
        ("mueres", "morir", "presente", "tu"),
        ("muere", "morir", "presente", "el"),
        ("morimos", "morir", "presente", "nosotros"),
        ("morís", "morir", "presente", "vosotros"),
        ("mueren", "morir", "presente", "ellos"),

        # ----------------------------------------------------
        # MORIR - PRETERITO
        # ----------------------------------------------------

        ("morí", "morir", "preterito", "yo"),
        ("moriste", "morir", "preterito", "tu"),
        ("murió", "morir", "preterito", "el"),
        ("morimos", "morir", "preterito", "nosotros"),
        ("moristeis", "morir", "preterito", "vosotros"),
        ("murieron", "morir", "preterito", "ellos"),

        # ----------------------------------------------------
        # CONSEGUIR - PRESENT
        # ----------------------------------------------------

        ("consigo", "conseguir", "presente", "yo"),
        ("consigues", "conseguir", "presente", "tu"),
        ("consigue", "conseguir", "presente", "el"),
        ("conseguimos", "conseguir", "presente", "nosotros"),
        ("conseguís", "conseguir", "presente", "vosotros"),
        ("consiguen", "conseguir", "presente", "ellos"),

        # ----------------------------------------------------
        # CONSEGUIR - PRETERITO
        # ----------------------------------------------------

        ("conseguí", "conseguir", "preterito", "yo"),
        ("conseguiste", "conseguir", "preterito", "tu"),
        ("consiguió", "conseguir", "preterito", "el"),
        ("conseguimos", "conseguir", "preterito", "nosotros"),
        ("conseguisteis", "conseguir", "preterito", "vosotros"),
        ("consiguieron", "conseguir", "preterito", "ellos"),

        # ----------------------------------------------------
        # MEDIR - PRESENT / PRETERITO
        # ----------------------------------------------------

        ("mido", "medir", "presente", "yo"),
        ("mides", "medir", "presente", "tu"),
        ("mide", "medir", "presente", "el"),
        ("medimos", "medir", "presente", "nosotros"),
        ("medís", "medir", "presente", "vosotros"),
        ("miden", "medir", "presente", "ellos"),

        ("medí", "medir", "preterito", "yo"),
        ("mediste", "medir", "preterito", "tu"),
        ("midió", "medir", "preterito", "el"),
        ("medimos", "medir", "preterito", "nosotros"),
        ("medisteis", "medir", "preterito", "vosotros"),
        ("midieron", "medir", "preterito", "ellos"),



        ### FUTURO

        ("hablaré", "hablar", "futuro", "yo"),
        ("hablarás", "hablar", "futuro", "tu"),
        ("hablará", "hablar", "futuro", "el"),
        ("hablaremos", "hablar", "futuro", "nosotros"),
        ("hablaréis", "hablar", "futuro", "vosotros"),
        ("hablarán", "hablar", "futuro", "ellos"),

        ("comeré", "comer", "futuro", "yo"),
        ("viviré", "vivir", "futuro", "yo"),

        ("tendré", "tener", "futuro", "yo"),
        ("tendrás", "tener", "futuro", "tu"),
        ("tendrá", "tener", "futuro", "el"),
        ("tendremos", "tener", "futuro", "nosotros"),
        ("tendréis", "tener", "futuro", "vosotros"),
        ("tendrán", "tener", "futuro", "ellos"),

        ("vendré", "venir", "futuro", "yo"),
        ("pondré", "poner", "futuro", "yo"),
        ("saldré", "salir", "futuro", "yo"),
        ("podré", "poder", "futuro", "yo"),
        ("sabré", "saber", "futuro", "yo"),
        ("querré", "querer", "futuro", "yo"),
        ("haré", "hacer", "futuro", "yo"),
        ("diré", "decir", "futuro", "yo"),

        ("hablaría", "hablar", "condicional", "yo"),
        ("hablarías", "hablar", "condicional", "tu"),
        ("hablaría", "hablar", "condicional", "el"),
        ("hablaríamos", "hablar", "condicional", "nosotros"),
        ("hablaríais", "hablar", "condicional", "vosotros"),
        ("hablarían", "hablar", "condicional", "ellos"),

        ("comería", "comer", "condicional", "yo"),
        ("viviría", "vivir", "condicional", "yo"),

        ("tendría", "tener", "condicional", "yo"),
        ("tendrías", "tener", "condicional", "tu"),
        ("tendría", "tener", "condicional", "el"),
        ("tendríamos", "tener", "condicional", "nosotros"),
        ("tendríais", "tener", "condicional", "vosotros"),
        ("tendrían", "tener", "condicional", "ellos"),

        ("vendría", "venir", "condicional", "yo"),
        ("pondría", "poner", "condicional", "yo"),
        ("saldría", "salir", "condicional", "yo"),
        ("podría", "poder", "condicional", "yo"),
        ("sabría", "saber", "condicional", "yo"),
        ("querría", "querer", "condicional", "yo"),
        ("haría", "hacer", "condicional", "yo"),
        ("diría", "decir", "condicional", "yo"),

        ### Perfecto
        ("he hablado", "hablar", "perfecto", "yo"),
        ("has hablado", "hablar", "perfecto", "tu"),
        ("ha hablado", "hablar", "perfecto", "el"),
        ("hemos hablado", "hablar", "perfecto", "nosotros"),
        ("habéis hablado", "hablar", "perfecto", "vosotros"),
        ("han hablado", "hablar", "perfecto", "ellos"),

        ("he comido", "comer", "perfecto", "yo"),
        ("has comido", "comer", "perfecto", "tu"),
        ("ha comido", "comer", "perfecto", "el"),
        ("hemos comido", "comer", "perfecto", "nosotros"),
        ("habéis comido", "comer", "perfecto", "vosotros"),
        ("han comido", "comer", "perfecto", "ellos"),

        ("he vivido", "vivir", "perfecto", "yo"),
        ("has vivido", "vivir", "perfecto", "tu"),
        ("ha vivido", "vivir", "perfecto", "el"),
        ("hemos vivido", "vivir", "perfecto", "nosotros"),
        ("habéis vivido", "vivir", "perfecto", "vosotros"),
        ("han vivido", "vivir", "perfecto", "ellos"),

        ("he hecho", "hacer", "perfecto", "yo"),
        ("has dicho", "decir", "perfecto", "tu"),
        ("ha visto", "ver", "perfecto", "el"),
        ("hemos escrito", "escribir", "perfecto", "nosotros"),
        ("habéis puesto", "poner", "perfecto", "vosotros"),
        ("han vuelto", "volver", "perfecto", "ellos"),
        ("he abierto", "abrir", "perfecto", "yo"),
        ("has roto", "romper", "perfecto", "tu"),
        ("ha muerto", "morir", "perfecto", "el"),
        ("hemos cubierto", "cubrir", "perfecto", "nosotros"),


        #plus que parfait
        ("había hablado", "hablar", "pluscuamperfecto", "yo"),
        ("habías hablado", "hablar", "pluscuamperfecto", "tu"),
        ("había hablado", "hablar", "pluscuamperfecto", "el"),
        ("habíamos hablado", "hablar", "pluscuamperfecto", "nosotros"),
        ("habíais hablado", "hablar", "pluscuamperfecto", "vosotros"),
        ("habían hablado", "hablar", "pluscuamperfecto", "ellos"),

        ("había comido", "comer", "pluscuamperfecto", "yo"),
        ("habías comido", "comer", "pluscuamperfecto", "tu"),
        ("había comido", "comer", "pluscuamperfecto", "el"),
        ("habíamos comido", "comer", "pluscuamperfecto", "nosotros"),
        ("habíais comido", "comer", "pluscuamperfecto", "vosotros"),
        ("habían comido", "comer", "pluscuamperfecto", "ellos"),

        ("había vivido", "vivir", "pluscuamperfecto", "yo"),
        ("habías vivido", "vivir", "pluscuamperfecto", "tu"),
        ("había vivido", "vivir", "pluscuamperfecto", "el"),
        ("habíamos vivido", "vivir", "pluscuamperfecto", "nosotros"),
        ("habíais vivido", "vivir", "pluscuamperfecto", "vosotros"),
        ("habían vivido", "vivir", "pluscuamperfecto", "ellos"),

        ### Participes irréguliers

        ("había hecho", "hacer", "pluscuamperfecto", "yo"),
        ("habías dicho", "decir", "pluscuamperfecto", "tu"),
        ("había visto", "ver", "pluscuamperfecto", "el"),
        ("habíamos escrito", "escribir", "pluscuamperfecto", "nosotros"),
        ("habíais puesto", "poner", "pluscuamperfecto", "vosotros"),
        ("habían vuelto", "volver", "pluscuamperfecto", "ellos"),
        ("había abierto", "abrir", "pluscuamperfecto", "yo"),
        ("habías roto", "romper", "pluscuamperfecto", "tu"),
        ("había muerto", "morir", "pluscuamperfecto", "el"),
        ("habíamos cubierto", "cubrir", "pluscuamperfecto", "nosotros"),


        ### futuro perfecto
        ("habré hablado", "hablar", "futuro_perfecto", "yo"),
        ("habrás hablado", "hablar", "futuro_perfecto", "tu"),
        ("habrá hablado", "hablar", "futuro_perfecto", "el"),
        ("habremos hablado", "hablar", "futuro_perfecto", "nosotros"),
        ("habréis hablado", "hablar", "futuro_perfecto", "vosotros"),
        ("habrán hablado", "hablar", "futuro_perfecto", "ellos"),

        ("habré comido", "comer", "futuro_perfecto", "yo"),
        ("habrás comido", "comer", "futuro_perfecto", "tu"),
        ("habrá comido", "comer", "futuro_perfecto", "el"),
        ("habremos comido", "comer", "futuro_perfecto", "nosotros"),
        ("habréis comido", "comer", "futuro_perfecto", "vosotros"),
        ("habrán comido", "comer", "futuro_perfecto", "ellos"),

        ("habré vivido", "vivir", "futuro_perfecto", "yo"),
        ("habrás vivido", "vivir", "futuro_perfecto", "tu"),
        ("habrá vivido", "vivir", "futuro_perfecto", "el"),
        ("habremos vivido", "vivir", "futuro_perfecto", "nosotros"),
        ("habréis vivido", "vivir", "futuro_perfecto", "vosotros"),
        ("habrán vivido", "vivir", "futuro_perfecto", "ellos"),

        ### Participes irréguliers

        ("habré hecho", "hacer", "futuro_perfecto", "yo"),
        ("habrás dicho", "decir", "futuro_perfecto", "tu"),
        ("habrá visto", "ver", "futuro_perfecto", "el"),
        ("habremos escrito", "escribir", "futuro_perfecto", "nosotros"),
        ("habréis puesto", "poner", "futuro_perfecto", "vosotros"),
        ("habrán vuelto", "volver", "futuro_perfecto", "ellos"),
        ("habré abierto", "abrir", "futuro_perfecto", "yo"),
        ("habrás roto", "romper", "futuro_perfecto", "tu"),
        ("habrá muerto", "morir", "futuro_perfecto", "el"),
        ("habremos cubierto", "cubrir", "futuro_perfecto", "nosotros"),

        ### condicional perfecto
        ("habría hablado", "hablar", "condicional_perfecto", "yo"),
        ("habrías hablado", "hablar", "condicional_perfecto", "tu"),
        ("habría hablado", "hablar", "condicional_perfecto", "el"),
        ("habríamos hablado", "hablar", "condicional_perfecto", "nosotros"),
        ("habríais hablado", "hablar", "condicional_perfecto", "vosotros"),
        ("habrían hablado", "hablar", "condicional_perfecto", "ellos"),

        ("habría comido", "comer", "condicional_perfecto", "yo"),
        ("habrías comido", "comer", "condicional_perfecto", "tu"),
        ("habría comido", "comer", "condicional_perfecto", "el"),
        ("habríamos comido", "comer", "condicional_perfecto", "nosotros"),
        ("habríais comido", "comer", "condicional_perfecto", "vosotros"),
        ("habrían comido", "comer", "condicional_perfecto", "ellos"),

        ("habría vivido", "vivir", "condicional_perfecto", "yo"),
        ("habrías vivido", "vivir", "condicional_perfecto", "tu"),
        ("habría vivido", "vivir", "condicional_perfecto", "el"),
        ("habríamos vivido", "vivir", "condicional_perfecto", "nosotros"),
        ("habríais vivido", "vivir", "condicional_perfecto", "vosotros"),
        ("habrían vivido", "vivir", "condicional_perfecto", "ellos"),

        ### Participes irréguliers

        ("habría hecho", "hacer", "condicional_perfecto", "yo"),
        ("habrías dicho", "decir", "condicional_perfecto", "tu"),
        ("habría visto", "ver", "condicional_perfecto", "el"),
        ("habríamos escrito", "escribir", "condicional_perfecto", "nosotros"),
        ("habríais puesto", "poner", "condicional_perfecto", "vosotros"),
        ("habrían vuelto", "volver", "condicional_perfecto", "ellos"),
        ("habría abierto", "abrir", "condicional_perfecto", "yo"),
        ("habrías roto", "romper", "condicional_perfecto", "tu"),
        ("habría muerto", "morir", "condicional_perfecto", "el"),
        ("habríamos cubierto", "cubrir", "condicional_perfecto", "nosotros"),

        ### subjuntivo
        ("hable", "hablar", "subjuntivo_presente", "yo"),
        ("hables", "hablar", "subjuntivo_presente", "tu"),
        ("hable", "hablar", "subjuntivo_presente", "el"),
        ("hablemos", "hablar", "subjuntivo_presente", "nosotros"),
        ("habléis", "hablar", "subjuntivo_presente", "vosotros"),
        ("hablen", "hablar", "subjuntivo_presente", "ellos"),

        ("coma", "comer", "subjuntivo_presente", "yo"),
        ("comas", "comer", "subjuntivo_presente", "tu"),
        ("coma", "comer", "subjuntivo_presente", "el"),
        ("comamos", "comer", "subjuntivo_presente", "nosotros"),
        ("comáis", "comer", "subjuntivo_presente", "vosotros"),
        ("coman", "comer", "subjuntivo_presente", "ellos"),

        ("viva", "vivir", "subjuntivo_presente", "yo"),
        ("vivas", "vivir", "subjuntivo_presente", "tu"),
        ("viva", "vivir", "subjuntivo_presente", "el"),
        ("vivamos", "vivir", "subjuntivo_presente", "nosotros"),
        ("viváis", "vivir", "subjuntivo_presente", "vosotros"),
        ("vivan", "vivir", "subjuntivo_presente", "ellos"),

        ### Changements de radical

        ("piense", "pensar", "subjuntivo_presente", "yo"),
        ("pensemos", "pensar", "subjuntivo_presente", "nosotros"),

        ("pueda", "poder", "subjuntivo_presente", "yo"),
        ("podamos", "poder", "subjuntivo_presente", "nosotros"),

        ("pida", "pedir", "subjuntivo_presente", "yo"),
        ("pidamos", "pedir", "subjuntivo_presente", "nosotros"),

        ### Irréguliers

        ("sea", "ser", "subjuntivo_presente", "yo"),
        ("seamos", "ser", "subjuntivo_presente", "nosotros"),

        ("esté", "estar", "subjuntivo_presente", "yo"),
        ("estemos", "estar", "subjuntivo_presente", "nosotros"),

        ("vaya", "ir", "subjuntivo_presente", "yo"),
        ("vayamos", "ir", "subjuntivo_presente", "nosotros"),

        ("tenga", "tener", "subjuntivo_presente", "yo"),
        ("tengamos", "tener", "subjuntivo_presente", "nosotros"),

        ("venga", "venir", "subjuntivo_presente", "yo"),
        ("vengamos", "venir", "subjuntivo_presente", "nosotros"),

        ("haga", "hacer", "subjuntivo_presente", "yo"),
        ("hagamos", "hacer", "subjuntivo_presente", "nosotros"),

        ("diga", "decir", "subjuntivo_presente", "yo"),
        ("digamos", "decir", "subjuntivo_presente", "nosotros"),

        ("salga", "salir", "subjuntivo_presente", "yo"),
        ("salgamos", "salir", "subjuntivo_presente", "nosotros"),

        ("ponga", "poner", "subjuntivo_presente", "yo"),
        ("pongamos", "poner", "subjuntivo_presente", "nosotros"),

        ("sepa", "saber", "subjuntivo_presente", "yo"),
        ("sepamos", "saber", "subjuntivo_presente", "nosotros"),

        ("vea", "ver", "subjuntivo_presente", "yo"),
        ("veamos", "ver", "subjuntivo_presente", "nosotros"),

        ("dé", "dar", "subjuntivo_presente", "yo"),
        ("demos", "dar", "subjuntivo_presente", "nosotros"),


        ### Subjuntivo imperfecto

        ("compráramos", "comprar", "subjuntivo_imperfecto", "nosotros"),

        ("hablara", "hablar", "subjuntivo_imperfecto", "yo"),
        ("hablaras", "hablar", "subjuntivo_imperfecto", "tu"),
        ("hablara", "hablar", "subjuntivo_imperfecto", "el"),
        ("habláramos", "hablar", "subjuntivo_imperfecto", "nosotros"),
        ("hablarais", "hablar", "subjuntivo_imperfecto", "vosotros"),
        ("hablaran", "hablar", "subjuntivo_imperfecto", "ellos"),

        ("comiera", "comer", "subjuntivo_imperfecto", "yo"),
        ("comiéramos", "comer", "subjuntivo_imperfecto", "nosotros"),
        ("comieran", "comer", "subjuntivo_imperfecto", "ellos"),

        ("viviera", "vivir", "subjuntivo_imperfecto", "yo"),
        ("viviéramos", "vivir", "subjuntivo_imperfecto", "nosotros"),
        ("vivieran", "vivir", "subjuntivo_imperfecto", "ellos"),

        ("tuviera", "tener", "subjuntivo_imperfecto", "yo"),
        ("tuviéramos", "tener", "subjuntivo_imperfecto", "nosotros"),
        ("tuvieran", "tener", "subjuntivo_imperfecto", "ellos"),

        ("estuviera", "estar", "subjuntivo_imperfecto", "yo"),
        ("fuera", "ser", "subjuntivo_imperfecto", "yo"),
        ("fuéramos", "ser", "subjuntivo_imperfecto", "nosotros"),

        ("hiciera", "hacer", "subjuntivo_imperfecto", "yo"),
        ("hiciéramos", "hacer", "subjuntivo_imperfecto", "nosotros"),

        ("dijera", "decir", "subjuntivo_imperfecto", "yo"),
        ("dijéramos", "decir", "subjuntivo_imperfecto", "nosotros"),

        ("pudiera", "poder", "subjuntivo_imperfecto", "yo"),
        ("pudiéramos", "poder", "subjuntivo_imperfecto", "nosotros"),

        ("pidiera", "pedir", "subjuntivo_imperfecto", "yo"),
        ("pidiéramos", "pedir", "subjuntivo_imperfecto", "nosotros"),

        ("durmiera", "dormir", "subjuntivo_imperfecto", "yo"),
        ("durmiéramos", "dormir", "subjuntivo_imperfecto", "nosotros"),

        ("leyera", "leer", "subjuntivo_imperfecto", "yo"),
        ("leyéramos", "leer", "subjuntivo_imperfecto", "nosotros"),

        ("trajera", "traer", "subjuntivo_imperfecto", "yo"),
        ("trajéramos", "traer", "subjuntivo_imperfecto", "nosotros"),

        ("condujera", "conducir", "subjuntivo_imperfecto", "yo"),
        ("condujéramos", "conducir", "subjuntivo_imperfecto", "nosotros"),

        ("siguiera", "seguir", "subjuntivo_imperfecto", "yo"),
        ("siguiéramos", "seguir", "subjuntivo_imperfecto", "nosotros"),

        ("eligiera", "elegir", "subjuntivo_imperfecto", "yo"),
        ("eligiéramos", "elegir", "subjuntivo_imperfecto", "nosotros"),

        ("viniera", "venir", "subjuntivo_imperfecto", "yo"),
        ("viniéramos", "venir", "subjuntivo_imperfecto", "nosotros"),

        ("quisiera", "querer", "subjuntivo_imperfecto", "yo"),
        ("quisiéramos", "querer", "subjuntivo_imperfecto", "nosotros"),

        ("supiera", "saber", "subjuntivo_imperfecto", "yo"),
        ("supiéramos", "saber", "subjuntivo_imperfecto", "nosotros"),

        ### Subjuntivo pluscaumperfecto
        ("hubiera hablado", "hablar", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubieras hablado", "hablar", "subjuntivo_pluscuamperfecto", "tu"),
        ("hubiera hablado", "hablar", "subjuntivo_pluscuamperfecto", "el"),
        ("hubiéramos hablado", "hablar", "subjuntivo_pluscuamperfecto", "nosotros"),
        ("hubierais hablado", "hablar", "subjuntivo_pluscuamperfecto", "vosotros"),
        ("hubieran hablado", "hablar", "subjuntivo_pluscuamperfecto", "ellos"),

        ("hubiera comido", "comer", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos comido", "comer", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera vivido", "vivir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos vivido", "vivir", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera hecho", "hacer", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos hecho", "hacer", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera dicho", "decir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubieran dicho", "decir", "subjuntivo_pluscuamperfecto", "ellos"),

        ("hubiera visto", "ver", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos visto", "ver", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera puesto", "poner", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubieran puesto", "poner", "subjuntivo_pluscuamperfecto", "ellos"),

        ("hubiera vuelto", "volver", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos vuelto", "volver", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera abierto", "abrir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubieran abierto", "abrir", "subjuntivo_pluscuamperfecto", "ellos"),

        ("hubiera roto", "romper", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos roto", "romper", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera muerto", "morir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubieran muerto", "morir", "subjuntivo_pluscuamperfecto", "ellos"),

        ("hubiera cubierto", "cubrir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos cubierto", "cubrir", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera escrito", "escribir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos escrito", "escribir", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera pedido", "pedir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubieran pedido", "pedir", "subjuntivo_pluscuamperfecto", "ellos"),

        ("hubiera dormido", "dormir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos dormido", "dormir", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera leído", "leer", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos leído", "leer", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera traído", "traer", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos traído", "traer", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera conseguido", "conseguir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos conseguido", "conseguir", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera preferido", "preferir", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubieran preferido", "preferir", "subjuntivo_pluscuamperfecto", "ellos"),

        ("hubiera sido", "ser", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubiéramos sido", "ser", "subjuntivo_pluscuamperfecto", "nosotros"),

        ("hubiera estado", "estar", "subjuntivo_pluscuamperfecto", "yo"),
        ("hubieran estado", "estar", "subjuntivo_pluscuamperfecto", "ellos"),

        ### Subjuntivo_perfecto
        ("haya hablado", "hablar", "subjuntivo_perfecto", "yo"),
        ("hayas hablado", "hablar", "subjuntivo_perfecto", "tu"),
        ("haya hablado", "hablar", "subjuntivo_perfecto", "el"),
        ("hayamos hablado", "hablar", "subjuntivo_perfecto", "nosotros"),
        ("hayáis hablado", "hablar", "subjuntivo_perfecto", "vosotros"),
        ("hayan hablado", "hablar", "subjuntivo_perfecto", "ellos"),

        ("haya comido", "comer", "subjuntivo_perfecto", "yo"),
        ("hayamos comido", "comer", "subjuntivo_perfecto", "nosotros"),

        ("haya vivido", "vivir", "subjuntivo_perfecto", "yo"),
        ("hayamos vivido", "vivir", "subjuntivo_perfecto", "nosotros"),

        ("haya hecho", "hacer", "subjuntivo_perfecto", "yo"),
        ("hayamos hecho", "hacer", "subjuntivo_perfecto", "nosotros"),

        ("haya dicho", "decir", "subjuntivo_perfecto", "yo"),
        ("hayan dicho", "decir", "subjuntivo_perfecto", "ellos"),

        ("haya visto", "ver", "subjuntivo_perfecto", "yo"),
        ("hayamos visto", "ver", "subjuntivo_perfecto", "nosotros"),

        ("haya puesto", "poner", "subjuntivo_perfecto", "yo"),
        ("hayan puesto", "poner", "subjuntivo_perfecto", "ellos"),

        ("haya vuelto", "volver", "subjuntivo_perfecto", "yo"),
        ("hayamos vuelto", "volver", "subjuntivo_perfecto", "nosotros"),

        ("haya abierto", "abrir", "subjuntivo_perfecto", "yo"),
        ("hayan abierto", "abrir", "subjuntivo_perfecto", "ellos"),

        ("haya roto", "romper", "subjuntivo_perfecto", "yo"),
        ("hayamos roto", "romper", "subjuntivo_perfecto", "nosotros"),

        ("haya muerto", "morir", "subjuntivo_perfecto", "yo"),
        ("hayan muerto", "morir", "subjuntivo_perfecto", "ellos"),

        ("haya cubierto", "cubrir", "subjuntivo_perfecto", "yo"),
        ("hayamos cubierto", "cubrir", "subjuntivo_perfecto", "nosotros"),

        ("haya escrito", "escribir", "subjuntivo_perfecto", "yo"),
        ("hayamos escrito", "escribir", "subjuntivo_perfecto", "nosotros"),

        ("haya pedido", "pedir", "subjuntivo_perfecto", "yo"),
        ("hayan pedido", "pedir", "subjuntivo_perfecto", "ellos"),

        ("haya dormido", "dormir", "subjuntivo_perfecto", "yo"),
        ("hayamos dormido", "dormir", "subjuntivo_perfecto", "nosotros"),

        ("haya leído", "leer", "subjuntivo_perfecto", "yo"),
        ("hayamos leído", "leer", "subjuntivo_perfecto", "nosotros"),

        ("haya traído", "traer", "subjuntivo_perfecto", "yo"),
        ("hayamos traído", "traer", "subjuntivo_perfecto", "nosotros"),

        ("haya conseguido", "conseguir", "subjuntivo_perfecto", "yo"),
        ("hayamos conseguido", "conseguir", "subjuntivo_perfecto", "nosotros"),

        ("haya preferido", "preferir", "subjuntivo_perfecto", "yo"),
        ("hayan preferido", "preferir", "subjuntivo_perfecto", "ellos"),

        ("haya sido", "ser", "subjuntivo_perfecto", "yo"),
        ("hayamos sido", "ser", "subjuntivo_perfecto", "nosotros"),

        ("haya estado", "estar", "subjuntivo_perfecto", "yo"),
        ("hayan estado", "estar", "subjuntivo_perfecto", "ellos"),

        ### Imperativo affirmativo y negativo
        ("habla", "hablar", "imperativo_afirmativo", "tu"),
        ("hable", "hablar", "imperativo_afirmativo", "el"),
        ("hablemos", "hablar", "imperativo_afirmativo", "nosotros"),
        ("hablad", "hablar", "imperativo_afirmativo", "vosotros"),
        ("hablen", "hablar", "imperativo_afirmativo", "ellos"),

        ("come", "comer", "imperativo_afirmativo", "tu"),
        ("coma", "comer", "imperativo_afirmativo", "el"),
        ("comamos", "comer", "imperativo_afirmativo", "nosotros"),
        ("comed", "comer", "imperativo_afirmativo", "vosotros"),
        ("coman", "comer", "imperativo_afirmativo", "ellos"),

        ("vive", "vivir", "imperativo_afirmativo", "tu"),
        ("viva", "vivir", "imperativo_afirmativo", "el"),
        ("vivamos", "vivir", "imperativo_afirmativo", "nosotros"),
        ("vivid", "vivir", "imperativo_afirmativo", "vosotros"),
        ("vivan", "vivir", "imperativo_afirmativo", "ellos"),

        ("piensa", "pensar", "imperativo_afirmativo", "tu"),
        ("piense", "pensar", "imperativo_afirmativo", "el"),
        ("pensemos", "pensar", "imperativo_afirmativo", "nosotros"),
        ("pensad", "pensar", "imperativo_afirmativo", "vosotros"),
        ("piensen", "pensar", "imperativo_afirmativo", "ellos"),

        ("puede", "poder", "imperativo_afirmativo", "tu"),
        ("pueda", "poder", "imperativo_afirmativo", "el"),
        ("podamos", "poder", "imperativo_afirmativo", "nosotros"),
        ("poded", "poder", "imperativo_afirmativo", "vosotros"),
        ("puedan", "poder", "imperativo_afirmativo", "ellos"),

        ("pide", "pedir", "imperativo_afirmativo", "tu"),
        ("pida", "pedir", "imperativo_afirmativo", "el"),
        ("pidamos", "pedir", "imperativo_afirmativo", "nosotros"),
        ("pedid", "pedir", "imperativo_afirmativo", "vosotros"),
        ("pidan", "pedir", "imperativo_afirmativo", "ellos"),

        ("ten", "tener", "imperativo_afirmativo", "tu"),
        ("tenga", "tener", "imperativo_afirmativo", "el"),
        ("tengamos", "tener", "imperativo_afirmativo", "nosotros"),
        ("tened", "tener", "imperativo_afirmativo", "vosotros"),
        ("tengan", "tener", "imperativo_afirmativo", "ellos"),

        ("ven", "venir", "imperativo_afirmativo", "tu"),
        ("venga", "venir", "imperativo_afirmativo", "el"),
        ("vengamos", "venir", "imperativo_afirmativo", "nosotros"),
        ("venid", "venir", "imperativo_afirmativo", "vosotros"),
        ("vengan", "venir", "imperativo_afirmativo", "ellos"),

        ("di", "decir", "imperativo_afirmativo", "tu"),
        ("diga", "decir", "imperativo_afirmativo", "el"),
        ("digamos", "decir", "imperativo_afirmativo", "nosotros"),
        ("decid", "decir", "imperativo_afirmativo", "vosotros"),
        ("digan", "decir", "imperativo_afirmativo", "ellos"),

        ("haz", "hacer", "imperativo_afirmativo", "tu"),
        ("haga", "hacer", "imperativo_afirmativo", "el"),
        ("hagamos", "hacer", "imperativo_afirmativo", "nosotros"),
        ("haced", "hacer", "imperativo_afirmativo", "vosotros"),
        ("hagan", "hacer", "imperativo_afirmativo", "ellos"),

        ("ve", "ir", "imperativo_afirmativo", "tu"),
        ("vaya", "ir", "imperativo_afirmativo", "el"),
        ("vayamos", "ir", "imperativo_afirmativo", "nosotros"),
        ("id", "ir", "imperativo_afirmativo", "vosotros"),
        ("vayan", "ir", "imperativo_afirmativo", "ellos"),

        ("pon", "poner", "imperativo_afirmativo", "tu"),
        ("ponga", "poner", "imperativo_afirmativo", "el"),
        ("pongamos", "poner", "imperativo_afirmativo", "nosotros"),
        ("poned", "poner", "imperativo_afirmativo", "vosotros"),
        ("pongan", "poner", "imperativo_afirmativo", "ellos"),

        ("sal", "salir", "imperativo_afirmativo", "tu"),
        ("salga", "salir", "imperativo_afirmativo", "el"),
        ("salgamos", "salir", "imperativo_afirmativo", "nosotros"),
        ("salid", "salir", "imperativo_afirmativo", "vosotros"),
        ("salgan", "salir", "imperativo_afirmativo", "ellos"),

        ("sé", "ser", "imperativo_afirmativo", "tu"),
        ("sea", "ser", "imperativo_afirmativo", "el"),
        ("seamos", "ser", "imperativo_afirmativo", "nosotros"),
        ("sed", "ser", "imperativo_afirmativo", "vosotros"),
        ("sean", "ser", "imperativo_afirmativo", "ellos"),

        ("no hables", "hablar", "imperativo_negativo", "tu"),
        ("no hable", "hablar", "imperativo_negativo", "el"),
        ("no hablemos", "hablar", "imperativo_negativo", "nosotros"),
        ("no habléis", "hablar", "imperativo_negativo", "vosotros"),
        ("no hablen", "hablar", "imperativo_negativo", "ellos"),

        ("no comas", "comer", "imperativo_negativo", "tu"),
        ("no comamos", "comer", "imperativo_negativo", "nosotros"),
        ("no vivas", "vivir", "imperativo_negativo", "tu"),
        ("no vivamos", "vivir", "imperativo_negativo", "nosotros"),

        ("no tengas", "tener", "imperativo_negativo", "tu"),
        ("no vengas", "venir", "imperativo_negativo", "tu"),
        ("no digas", "decir", "imperativo_negativo", "tu"),
        ("no hagas", "hacer", "imperativo_negativo", "tu"),
        ("no vayas", "ir", "imperativo_negativo", "tu"),
        ("no pongas", "poner", "imperativo_negativo", "tu"),
        ("no salgas", "salir", "imperativo_negativo", "tu"),
        ("no seas", "ser", "imperativo_negativo", "tu"),

        ("no pidas", "pedir", "imperativo_negativo", "tu"),
        ("no duermas", "dormir", "imperativo_negativo", "tu"),
        ("no pienses", "pensar", "imperativo_negativo", "tu"),
        ("no puedas", "poder", "imperativo_negativo", "tu"),



        ("hablo", "hablar", "presente", "yo"),
        ("comes", "comer", "presente", "tu"),
        ("vivimos", "vivir", "presente", "nosotros"),

        # --- e → ie ---
        ("pienso", "pensar", "presente", "yo"),
        ("piensas", "pensar", "presente", "tu"),
        ("piensa", "pensar", "presente", "el"),
        ("pensamos", "pensar", "presente", "nosotros"),
        ("pensáis", "pensar", "presente", "vosotros"),
        ("piensan", "pensar", "presente", "ellos"),

        # --- o → ue ---
        ("puedo", "poder", "presente", "yo"),
        ("puedes", "poder", "presente", "tu"),
        ("puede", "poder", "presente", "el"),
        ("podemos", "poder", "presente", "nosotros"),
        ("podéis", "poder", "presente", "vosotros"),
        ("pueden", "poder", "presente", "ellos"),

        # --- u → ue ---
        ("juego", "jugar", "presente", "yo"),
        ("jugamos", "jugar", "presente", "nosotros"),

        # --- e → i ---
        ("pido", "pedir", "presente", "yo"),
        ("pides", "pedir", "presente", "tu"),
        ("pide", "pedir", "presente", "el"),
        ("pedimos", "pedir", "presente", "nosotros"),
        ("pedís", "pedir", "presente", "vosotros"),
        ("piden", "pedir", "presente", "ellos"),

        # --- e → ie + e → i ---
        ("siento", "sentir", "presente", "yo"),
        ("sientes", "sentir", "presente", "tu"),
        ("siente", "sentir", "presente", "el"),
        ("sentimos", "sentir", "presente", "nosotros"),
        ("sentís", "sentir", "presente", "vosotros"),
        ("sienten", "sentir", "presente", "ellos"),

        # --- o → ue + o → u ---
        ("duermo", "dormir", "presente", "yo"),
        ("duermes", "dormir", "presente", "tu"),
        ("duerme", "dormir", "presente", "el"),
        ("dormimos", "dormir", "presente", "nosotros"),
        ("dormís", "dormir", "presente", "vosotros"),
        ("duermen", "dormir", "presente", "ellos"),

        # --- e → i + g → j ---
        ("elijo", "elegir", "presente", "yo"),
        ("eliges", "elegir", "presente", "tu"),
        ("elige", "elegir", "presente", "el"),
        ("elegimos", "elegir", "presente", "nosotros"),
        ("elegís", "elegir", "presente", "vosotros"),
        ("eligen", "elegir", "presente", "ellos"),

        ("rijo", "regir", "presente", "yo"),
        ("riges", "regir", "presente", "tu"),
        ("rige", "regir", "presente", "el"),
        ("regimos", "regir", "presente", "nosotros"),
        ("regís", "regir", "presente", "vosotros"),
        ("rigen", "regir", "presente", "ellos"),

        # --- e → i + gu → g ---
        ("sigo", "seguir", "presente", "yo"),
        ("sigues", "seguir", "presente", "tu"),
        ("sigue", "seguir", "presente", "el"),
        ("seguimos", "seguir", "presente", "nosotros"),
        ("seguís", "seguir", "presente", "vosotros"),
        ("siguen", "seguir", "presente", "ellos"),

        ("consigo", "conseguir", "presente", "yo"),
        ("consigues", "conseguir", "presente", "tu"),
        ("consigue", "conseguir", "presente", "el"),
        ("conseguimos", "conseguir", "presente", "nosotros"),
        ("conseguís", "conseguir", "presente", "vosotros"),
        ("consiguen", "conseguir", "presente", "ellos"),

        # --- e → ie + g → gu ---
        ("riego", "regar", "presente", "yo"),
        ("riegas", "regar", "presente", "tu"),
        ("riega", "regar", "presente", "el"),
        ("regamos", "regar", "presente", "nosotros"),
        ("regáis", "regar", "presente", "vosotros"),
        ("riegan", "regar", "presente", "ellos"),

        # --- o → ue + c → z ---
        ("tuerzo", "torcer", "presente", "yo"),
        ("tuerces", "torcer", "presente", "tu"),
        ("tuerce", "torcer", "presente", "el"),
        ("torcemos", "torcer", "presente", "nosotros"),
        ("torcéis", "torcer", "presente", "vosotros"),
        ("tuercen", "torcer", "presente", "ellos"),

        ("cuezo", "cocer", "presente", "yo"),
        ("cueces", "cocer", "presente", "tu"),
        ("cuece", "cocer", "presente", "el"),
        ("cocemos", "cocer", "presente", "nosotros"),
        ("cocéis", "cocer", "presente", "vosotros"),
        ("cuecen", "cocer", "presente", "ellos"),

        # --- c → zc ---
        ("conozco", "conocer", "presente", "yo"),
        ("conoces", "conocer", "presente", "tu"),
        ("conoce", "conocer", "presente", "el"),
        ("conocemos", "conocer", "presente", "nosotros"),
        ("conocéis", "conocer", "presente", "vosotros"),
        ("conocen", "conocer", "presente", "ellos"),

        # --- -ucir : c → zc ---
        ("conduzco", "conducir", "presente", "yo"),
        ("conduces", "conducir", "presente", "tu"),
        ("conduce", "conducir", "presente", "el"),
        ("conducimos", "conducir", "presente", "nosotros"),
        ("conducís", "conducir", "presente", "vosotros"),
        ("conducen", "conducir", "presente", "ellos"),

        # --- qu → c ---
        ("delinco", "delinquir", "presente", "yo"),
        ("delinques", "delinquir", "presente", "tu"),
        ("delinque", "delinquir", "presente", "el"),
        ("delinquimos", "delinquir", "presente", "nosotros"),
        ("delinquís", "delinquir", "presente", "vosotros"),
        ("delinquen", "delinquir", "presente", "ellos"),

        # --- -iar : accentuation ---
        ("envío", "enviar", "presente", "yo"),
        ("envías", "enviar", "presente", "tu"),
        ("envía", "enviar", "presente", "el"),
        ("enviamos", "enviar", "presente", "nosotros"),
        ("enviáis", "enviar", "presente", "vosotros"),
        ("envían", "enviar", "presente", "ellos"),

        # --- -uar : accentuation ---
        ("continúo", "continuar", "presente", "yo"),
        ("continúas", "continuar", "presente", "tu"),
        ("continúa", "continuar", "presente", "el"),
        ("continuamos", "continuar", "presente", "nosotros"),
        ("continuáis", "continuar", "presente", "vosotros"),
        ("continúan", "continuar", "presente", "ellos"),

        # --- -eír : formes spéciales ---
        ("río", "reír", "presente", "yo"),
        ("ríes", "reír", "presente", "tu"),
        ("ríe", "reír", "presente", "el"),
        ("reímos", "reír", "presente", "nosotros"),
        ("reís", "reír", "presente", "vosotros"),
        ("ríen", "reír", "presente", "ellos"),

        # --- irréguliers complets ---
        ("soy", "ser", "presente", "yo"),
        ("eres", "ser", "presente", "tu"),
        ("es", "ser", "presente", "el"),
        ("somos", "ser", "presente", "nosotros"),
        ("sois", "ser", "presente", "vosotros"),
        ("son", "ser", "presente", "ellos"),

        ("voy", "ir", "presente", "yo"),
        ("vas", "ir", "presente", "tu"),
        ("va", "ir", "presente", "el"),
        ("vamos", "ir", "presente", "nosotros"),
        ("vais", "ir", "presente", "vosotros"),
        ("van", "ir", "presente", "ellos"),


        # AR

        ("hablé", "hablar", "preterito", "yo"),
        ("hablaste", "hablar", "preterito", "tu"),
        ("habló", "hablar", "preterito", "el"),
        ("hablamos", "hablar", "preterito", "nosotros"),
        ("hablasteis", "hablar", "preterito", "vosotros"),
        ("hablaron", "hablar", "preterito", "ellos"),

        # ER

        ("comí", "comer", "preterito", "yo"),
        ("comiste", "comer", "preterito", "tu"),
        ("comió", "comer", "preterito", "el"),
        ("comimos", "comer", "preterito", "nosotros"),
        ("comisteis", "comer", "preterito", "vosotros"),
        ("comieron", "comer", "preterito", "ellos"),

        # IR

        ("viví", "vivir", "preterito", "yo"),
        ("viviste", "vivir", "preterito", "tu"),
        ("vivió", "vivir", "preterito", "el"),
        ("vivimos", "vivir", "preterito", "nosotros"),
        ("vivisteis", "vivir", "preterito", "vosotros"),
        ("vivieron", "vivir", "preterito", "ellos"),

        # SER / IR

        ("fui", "ser", "preterito", "yo"),
        ("fuiste", "ser", "preterito", "tu"),
        ("fue", "ser", "preterito", "el"),
        ("fuimos", "ser", "preterito", "nosotros"),
        ("fuisteis", "ser", "preterito", "vosotros"),
        ("fueron", "ser", "preterito", "ellos"),

        ("fui", "ir", "preterito", "yo"),
        ("fuiste", "ir", "preterito", "tu"),
        ("fue", "ir", "preterito", "el"),
        ("fuimos", "ir", "preterito", "nosotros"),
        ("fuisteis", "ir", "preterito", "vosotros"),
        ("fueron", "ir", "preterito", "ellos"),

        # RADICALES IRREGULARES

        # andar

        ("anduve", "andar", "preterito", "yo"),
        ("anduviste", "andar", "preterito", "tu"),
        ("anduvo", "andar", "preterito", "el"),
        ("anduvimos", "andar", "preterito", "nosotros"),
        ("anduvisteis", "andar", "preterito", "vosotros"),
        ("anduvieron", "andar", "preterito", "ellos"),

        # estar

        ("estuve", "estar", "preterito", "yo"),
        ("estuviste", "estar", "preterito", "tu"),
        ("estuvo", "estar", "preterito", "el"),
        ("estuvimos", "estar", "preterito", "nosotros"),
        ("estuvisteis", "estar", "preterito", "vosotros"),
        ("estuvieron", "estar", "preterito", "ellos"),

        # tener

        ("tuve", "tener", "preterito", "yo"),
        ("tuviste", "tener", "preterito", "tu"),
        ("tuvo", "tener", "preterito", "el"),
        ("tuvimos", "tener", "preterito", "nosotros"),
        ("tuvisteis", "tener", "preterito", "vosotros"),
        ("tuvieron", "tener", "preterito", "ellos"),

        # poder

        ("pude", "poder", "preterito", "yo"),
        ("pudiste", "poder", "preterito", "tu"),
        ("pudo", "poder", "preterito", "el"),
        ("pudimos", "poder", "preterito", "nosotros"),
        ("pudisteis", "poder", "preterito", "vosotros"),
        ("pudieron", "poder", "preterito", "ellos"),

        # poner

        ("puse", "poner", "preterito", "yo"),
        ("pusiste", "poner", "preterito", "tu"),
        ("puso", "poner", "preterito", "el"),
        ("pusimos", "poner", "preterito", "nosotros"),
        ("pusisteis", "poner", "preterito", "vosotros"),
        ("pusieron", "poner", "preterito", "ellos"),

        # saber

        ("supe", "saber", "preterito", "yo"),
        ("supiste", "saber", "preterito", "tu"),
        ("supo", "saber", "preterito", "el"),
        ("supimos", "saber", "preterito", "nosotros"),
        ("supisteis", "saber", "preterito", "vosotros"),
        ("supieron", "saber", "preterito", "ellos"),

        # querer

        ("quise", "querer", "preterito", "yo"),
        ("quisiste", "querer", "preterito", "tu"),
        ("quiso", "querer", "preterito", "el"),
        ("quisimos", "querer", "preterito", "nosotros"),
        ("quisisteis", "querer", "preterito", "vosotros"),
        ("quisieron", "querer", "preterito", "ellos"),

        # venir

        ("vine", "venir", "preterito", "yo"),
        ("viniste", "venir", "preterito", "tu"),
        ("vino", "venir", "preterito", "el"),
        ("vinimos", "venir", "preterito", "nosotros"),
        ("vinisteis", "venir", "preterito", "vosotros"),
        ("vinieron", "venir", "preterito", "ellos"),

        # caber

        ("cupe", "caber", "preterito", "yo"),
        ("cupiste", "caber", "preterito", "tu"),
        ("cupo", "caber", "preterito", "el"),
        ("cupimos", "caber", "preterito", "nosotros"),
        ("cupisteis", "caber", "preterito", "vosotros"),
        ("cupieron", "caber", "preterito", "ellos"),

        # haber

        ("hube", "haber", "preterito", "yo"),
        ("hubiste", "haber", "preterito", "tu"),
        ("hubo", "haber", "preterito", "el"),
        ("hubimos", "haber", "preterito", "nosotros"),
        ("hubisteis", "haber", "preterito", "vosotros"),
        ("hubieron", "haber", "preterito", "ellos"),

        # hacer

        ("hice", "hacer", "preterito", "yo"),
        ("hiciste", "hacer", "preterito", "tu"),
        ("hizo", "hacer", "preterito", "el"),
        ("hicimos", "hacer", "preterito", "nosotros"),
        ("hicisteis", "hacer", "preterito", "vosotros"),
        ("hicieron", "hacer", "preterito", "ellos"),

        # RADICALES EN J

        # decir

        ("dije", "decir", "preterito", "yo"),
        ("dijiste", "decir", "preterito", "tu"),
        ("dijo", "decir", "preterito", "el"),
        ("dijimos", "decir", "preterito", "nosotros"),
        ("dijisteis", "decir", "preterito", "vosotros"),
        ("dijeron", "decir", "preterito", "ellos"),

        # traer

        ("traje", "traer", "preterito", "yo"),
        ("trajiste", "traer", "preterito", "tu"),
        ("trajo", "traer", "preterito", "el"),
        ("trajimos", "traer", "preterito", "nosotros"),
        ("trajisteis", "traer", "preterito", "vosotros"),
        ("trajeron", "traer", "preterito", "ellos"),

        # conducir

        ("conduje", "conducir", "preterito", "yo"),
        ("condujiste", "conducir", "preterito", "tu"),
        ("condujo", "conducir", "preterito", "el"),
        ("condujimos", "conducir", "preterito", "nosotros"),
        ("condujisteis", "conducir", "preterito", "vosotros"),
        ("condujeron", "conducir", "preterito", "ellos"),

        # producir

        ("produje", "producir", "preterito", "yo"),
        ("produjiste", "producir", "preterito", "tu"),
        ("produjo", "producir", "preterito", "el"),
        ("produjimos", "producir", "preterito", "nosotros"),
        ("produjisteis", "producir", "preterito", "vosotros"),
        ("produjeron", "producir", "preterito", "ellos"),

        # traducir

        ("traduje", "traducir", "preterito", "yo"),
        ("tradujiste", "traducir", "preterito", "tu"),
        ("tradujo", "traducir", "preterito", "el"),
        ("tradujimos", "traducir", "preterito", "nosotros"),
        ("tradujisteis", "traducir", "preterito", "vosotros"),
        ("tradujeron", "traducir", "preterito", "ellos"),

        # e → i

        # pedir

        ("pedí", "pedir", "preterito", "yo"),
        ("pediste", "pedir", "preterito", "tu"),
        ("pidió", "pedir", "preterito", "el"),
        ("pedimos", "pedir", "preterito", "nosotros"),
        ("pedisteis", "pedir", "preterito", "vosotros"),
        ("pidieron", "pedir", "preterito", "ellos"),

        # sentir

        ("sentí", "sentir", "preterito", "yo"),
        ("sentiste", "sentir", "preterito", "tu"),
        ("sintió", "sentir", "preterito", "el"),
        ("sentimos", "sentir", "preterito", "nosotros"),
        ("sentisteis", "sentir", "preterito", "vosotros"),
        ("sintieron", "sentir", "preterito", "ellos"),

        # servir

        ("serví", "servir", "preterito", "yo"),
        ("serviste", "servir", "preterito", "tu"),
        ("sirvió", "servir", "preterito", "el"),
        ("servimos", "servir", "preterito", "nosotros"),
        ("servisteis", "servir", "preterito", "vosotros"),
        ("sirvieron", "servir", "preterito", "ellos"),

        # vestir

        ("vestí", "vestir", "preterito", "yo"),
        ("vestiste", "vestir", "preterito", "tu"),
        ("vistió", "vestir", "preterito", "el"),
        ("vestimos", "vestir", "preterito", "nosotros"),
        ("vestisteis", "vestir", "preterito", "vosotros"),
        ("vistieron", "vestir", "preterito", "ellos"),

        # o → u

        # dormir

        ("dormí", "dormir", "preterito", "yo"),
        ("dormiste", "dormir", "preterito", "tu"),
        ("durmió", "dormir", "preterito", "el"),
        ("dormimos", "dormir", "preterito", "nosotros"),
        ("dormisteis", "dormir", "preterito", "vosotros"),
        ("durmieron", "dormir", "preterito", "ellos"),

        # morir

        ("morí", "morir", "preterito", "yo"),
        ("moriste", "morir", "preterito", "tu"),
        ("murió", "morir", "preterito", "el"),
        ("morimos", "morir", "preterito", "nosotros"),
        ("moristeis", "morir", "preterito", "vosotros"),
        ("murieron", "morir", "preterito", "ellos"),

        # -UIR → Y

        # construir

        ("construí", "construir", "preterito", "yo"),
        ("construiste", "construir", "preterito", "tu"),
        ("construyó", "construir", "preterito", "el"),
        ("construimos", "construir", "preterito", "nosotros"),
        ("construisteis", "construir", "preterito", "vosotros"),
        ("construyeron", "construir", "preterito", "ellos"),

        # destruir

        ("destruí", "destruir", "preterito", "yo"),
        ("destruiste", "destruir", "preterito", "tu"),
        ("destruyó", "destruir", "preterito", "el"),
        ("destruimos", "destruir", "preterito", "nosotros"),
        ("destruisteis", "destruir", "preterito", "vosotros"),
        ("destruyeron", "destruir", "preterito", "ellos"),

        # huir

        ("huí", "huir", "preterito", "yo"),
        ("huiste", "huir", "preterito", "tu"),
        ("huyó", "huir", "preterito", "el"),
        ("huimos", "huir", "preterito", "nosotros"),
        ("huisteis", "huir", "preterito", "vosotros"),
        ("huyeron", "huir", "preterito", "ellos"),

        # i → y

        # leer

        ("leí", "leer", "preterito", "yo"),
        ("leíste", "leer", "preterito", "tu"),
        ("leyó", "leer", "preterito", "el"),
        ("leímos", "leer", "preterito", "nosotros"),
        ("leísteis", "leer", "preterito", "vosotros"),
        ("leyeron", "leer", "preterito", "ellos"),

        # creer

        ("creí", "creer", "preterito", "yo"),
        ("creíste", "creer", "preterito", "tu"),
        ("creyó", "creer", "preterito", "el"),
        ("creímos", "creer", "preterito", "nosotros"),
        ("creísteis", "creer", "preterito", "vosotros"),
        ("creyeron", "creer", "preterito", "ellos"),

        # caer

        ("caí", "caer", "preterito", "yo"),
        ("caíste", "caer", "preterito", "tu"),
        ("cayó", "caer", "preterito", "el"),
        ("caímos", "caer", "preterito", "nosotros"),
        ("caísteis", "caer", "preterito", "vosotros"),
        ("cayeron", "caer", "preterito", "ellos"),

        # oír

        ("oí", "oír", "preterito", "yo"),
        ("oíste", "oír", "preterito", "tu"),
        ("oyó", "oír", "preterito", "el"),
        ("oímos", "oír", "preterito", "nosotros"),
        ("oísteis", "oír", "preterito", "vosotros"),
        ("oyeron", "oír", "preterito", "ellos"),

        # PERT / disparition du i

        # reñir

        ("reñí", "reñir", "preterito", "yo"),
        ("reñiste", "reñir", "preterito", "tu"),
        ("riñó", "reñir", "preterito", "el"),
        ("reñimos", "reñir", "preterito", "nosotros"),
        ("reñisteis", "reñir", "preterito", "vosotros"),
        ("riñeron", "reñir", "preterito", "ellos"),

        # teñir

        ("teñí", "teñir", "preterito", "yo"),
        ("teñiste", "teñir", "preterito", "tu"),
        ("tiñó", "teñir", "preterito", "el"),
        ("teñimos", "teñir", "preterito", "nosotros"),
        ("teñisteis", "teñir", "preterito", "vosotros"),
        ("tiñeron", "teñir", "preterito", "ellos"),

        # ceñir

        ("ceñí", "ceñir", "preterito", "yo"),
        ("ceñiste", "ceñir", "preterito", "tu"),
        ("ciñó", "ceñir", "preterito", "el"),
        ("ceñimos", "ceñir", "preterito", "nosotros"),
        ("ceñisteis", "ceñir", "preterito", "vosotros"),
        ("ciñeron", "ceñir", "preterito", "ellos"),

        # gruñir

        ("gruñí", "gruñir", "preterito", "yo"),
        ("gruñiste", "gruñir", "preterito", "tu"),
        ("gruñó", "gruñir", "preterito", "el"),
        ("gruñimos", "gruñir", "preterito", "nosotros"),
        ("gruñisteis", "gruñir", "preterito", "vosotros"),
        ("gruñeron", "gruñir", "preterito", "ellos"),

        # ORTHOGRAPHE -CAR → QU

        ("busqué", "buscar", "preterito", "yo"),
        ("buscaste", "buscar", "preterito", "tu"),
        ("buscó", "buscar", "preterito", "el"),
        ("buscamos", "buscar", "preterito", "nosotros"),
        ("buscasteis", "buscar", "preterito", "vosotros"),
        ("buscaron", "buscar", "preterito", "ellos"),

        ("toqué", "tocar", "preterito", "yo"),
        ("expliqué", "explicar", "preterito", "yo"),

        # ORTHOGRAPHE -GAR → GU

        ("llegué", "llegar", "preterito", "yo"),
        ("llegaste", "llegar", "preterito", "tu"),
        ("llegó", "llegar", "preterito", "el"),
        ("llegamos", "llegar", "preterito", "nosotros"),
        ("llegasteis", "llegar", "preterito", "vosotros"),
        ("llegaron", "llegar", "preterito", "ellos"),

        ("pagué", "pagar", "preterito", "yo"),
        ("entregué", "entregar", "preterito", "yo"),

        # ORTHOGRAPHE -ZAR → C

        ("empecé", "empezar", "preterito", "yo"),
        ("empezaste", "empezar", "preterito", "tu"),
        ("empezó", "empezar", "preterito", "el"),
        ("empezamos", "empezar", "preterito", "nosotros"),
        ("empezasteis", "empezar", "preterito", "vosotros"),
        ("empezaron", "empezar", "preterito", "ellos"),

        ("lancé", "lanzar", "preterito", "yo"),
        ("crucé", "cruzar", "preterito", "yo"),

        # COMBINAISON e → i + g → j

        ("elegí", "elegir", "preterito", "yo"),
        ("elegiste", "elegir", "preterito", "tu"),
        ("eligió", "elegir", "preterito", "el"),
        ("elegimos", "elegir", "preterito", "nosotros"),
        ("elegisteis", "elegir", "preterito", "vosotros"),
        ("eligieron", "elegir", "preterito", "ellos"),

        # COMBINAISON e → i + gu → g

        ("seguí", "seguir", "preterito", "yo"),
        ("seguiste", "seguir", "preterito", "tu"),
        ("siguió", "seguir", "preterito", "el"),
        ("seguimos", "seguir", "preterito", "nosotros"),
        ("seguisteis", "seguir", "preterito", "vosotros"),
        ("siguieron", "seguir", "preterito", "ellos"),

        # conseguir

        ("conseguí", "conseguir", "preterito", "yo"),
        ("conseguiste", "conseguir", "preterito", "tu"),
        ("consiguió", "conseguir", "preterito", "el"),
        ("conseguimos", "conseguir", "preterito", "nosotros"),
        ("conseguisteis", "conseguir", "preterito", "vosotros"),
        ("consiguieron", "conseguir", "preterito", "ellos"),

        # VÉRIFICATION DES PERSONNES SANS MODIFICATION

        # sentir

        ("sentí", "sentir", "preterito", "yo"),
        ("sentiste", "sentir", "preterito", "tu"),
        ("sentimos", "sentir", "preterito", "nosotros"),
        ("sentisteis", "sentir", "preterito", "vosotros"),

        # dormir

        ("dormí", "dormir", "preterito", "yo"),
        ("dormiste", "dormir", "preterito", "tu"),
        ("dormimos", "dormir", "preterito", "nosotros"),
        ("dormisteis", "dormir", "preterito", "vosotros"),

        # leer

        ("leí", "leer", "preterito", "yo"),
        ("leíste", "leer", "preterito", "tu"),
        ("leímos", "leer", "preterito", "nosotros"),
        ("leísteis", "leer", "preterito", "vosotros"),

        # oír

        ("oí", "oír", "preterito", "yo"),
        ("oíste", "oír", "preterito", "tu"),
        ("oímos", "oír", "preterito", "nosotros"),
        ("oísteis", "oír", "preterito", "vosotros"),


        ("hablaba", "hablar", "imperfecto", "yo"),
        ("hablabas", "hablar", "imperfecto", "tu"),
        ("hablaba", "hablar", "imperfecto", "el"),
        ("hablábamos", "hablar", "imperfecto", "nosotros"),
        ("hablabais", "hablar", "imperfecto", "vosotros"),
        ("hablaban", "hablar", "imperfecto", "ellos"),

        ("trabajaba", "trabajar", "imperfecto", "yo"),
        ("trabajabas", "trabajar", "imperfecto", "tu"),
        ("trabajaba", "trabajar", "imperfecto", "el"),
        ("trabajábamos", "trabajar", "imperfecto", "nosotros"),
        ("trabajabais", "trabajar", "imperfecto", "vosotros"),
        ("trabajaban", "trabajar", "imperfecto", "ellos"),

        ("estudiaba", "estudiar", "imperfecto", "yo"),
        ("estudiabas", "estudiar", "imperfecto", "tu"),
        ("estudiaba", "estudiar", "imperfecto", "el"),
        ("estudiábamos", "estudiar", "imperfecto", "nosotros"),
        ("estudiabais", "estudiar", "imperfecto", "vosotros"),
        ("estudiaban", "estudiar", "imperfecto", "ellos"),

        #IMPARFAIT — VERBES RÉGULIERS -ER

        ("comía", "comer", "imperfecto", "yo"),
        ("comías", "comer", "imperfecto", "tu"),
        ("comía", "comer", "imperfecto", "el"),
        ("comíamos", "comer", "imperfecto", "nosotros"),
        ("comíais", "comer", "imperfecto", "vosotros"),
        ("comían", "comer", "imperfecto", "ellos"),

        ("bebía", "beber", "imperfecto", "yo"),
        ("bebías", "beber", "imperfecto", "tu"),
        ("bebía", "beber", "imperfecto", "el"),
        ("bebíamos", "beber", "imperfecto", "nosotros"),
        ("bebíais", "beber", "imperfecto", "vosotros"),
        ("bebían", "beber", "imperfecto", "ellos"),

        ("aprendía", "aprender", "imperfecto", "yo"),
        ("aprendías", "aprender", "imperfecto", "tu"),
        ("aprendía", "aprender", "imperfecto", "el"),
        ("aprendíamos", "aprender", "imperfecto", "nosotros"),
        ("aprendíais", "aprender", "imperfecto", "vosotros"),
        ("aprendían", "aprender", "imperfecto", "ellos"),

        #IMPARFAIT — VERBES RÉGULIERS -IR

        ("vivía", "vivir", "imperfecto", "yo"),
        ("vivías", "vivir", "imperfecto", "tu"),
        ("vivía", "vivir", "imperfecto", "el"),
        ("vivíamos", "vivir", "imperfecto", "nosotros"),
        ("vivíais", "vivir", "imperfecto", "vosotros"),
        ("vivían", "vivir", "imperfecto", "ellos"),

        ("escribía", "escribir", "imperfecto", "yo"),
        ("escribías", "escribir", "imperfecto", "tu"),
        ("escribía", "escribir", "imperfecto", "el"),
        ("escribíamos", "escribir", "imperfecto", "nosotros"),
        ("escribíais", "escribir", "imperfecto", "vosotros"),
        ("escribían", "escribir", "imperfecto", "ellos"),

        ("abría", "abrir", "imperfecto", "yo"),
        ("abrías", "abrir", "imperfecto", "tu"),
        ("abría", "abrir", "imperfecto", "el"),
        ("abríamos", "abrir", "imperfecto", "nosotros"),
        ("abríais", "abrir", "imperfecto", "vosotros"),
        ("abrían", "abrir", "imperfecto", "ellos"),

        #SER

        ("era", "ser", "imperfecto", "yo"),
        ("eras", "ser", "imperfecto", "tu"),
        ("era", "ser", "imperfecto", "el"),
        ("éramos", "ser", "imperfecto", "nosotros"),
        ("erais", "ser", "imperfecto", "vosotros"),
        ("eran", "ser", "imperfecto", "ellos"),

        #IR

        ("iba", "ir", "imperfecto", "yo"),
        ("ibas", "ir", "imperfecto", "tu"),
        ("iba", "ir", "imperfecto", "el"),
        ("íbamos", "ir", "imperfecto", "nosotros"),
        ("ibais", "ir", "imperfecto", "vosotros"),
        ("iban", "ir", "imperfecto", "ellos"),

        #VER

        ("veía", "ver", "imperfecto", "yo"),
        ("veías", "ver", "imperfecto", "tu"),
        ("veía", "ver", "imperfecto", "el"),
        ("veíamos", "ver", "imperfecto", "nosotros"),
        ("veíais", "ver", "imperfecto", "vosotros"),
        ("veían", "ver", "imperfecto", "ellos"),

        #VÉRIFICATION DES VERBES IRRÉGULIERS DU PRÉSENT
        #Ils doivent rester réguliers à l'imparfait.

        ("pensaba", "pensar", "imperfecto", "yo"),
        ("pensábamos", "pensar", "imperfecto", "nosotros"),
        ("pensaban", "pensar", "imperfecto", "ellos"),

        ("podía", "poder", "imperfecto", "yo"),
        ("podíamos", "poder", "imperfecto", "nosotros"),
        ("podían", "poder", "imperfecto", "ellos"),

        ("pedía", "pedir", "imperfecto", "yo"),
        ("pedíamos", "pedir", "imperfecto", "nosotros"),
        ("pedían", "pedir", "imperfecto", "ellos"),

        ("sentía", "sentir", "imperfecto", "yo"),
        ("sentíamos", "sentir", "imperfecto", "nosotros"),
        ("sentían", "sentir", "imperfecto", "ellos"),

        ("dormía", "dormir", "imperfecto", "yo"),
        ("dormíamos", "dormir", "imperfecto", "nosotros"),
        ("dormían", "dormir", "imperfecto", "ellos"),

        ("construía", "construir", "imperfecto", "yo"),
        ("construíamos", "construir", "imperfecto", "nosotros"),
        ("construían", "construir", "imperfecto", "ellos"),

        ("conocía", "conocer", "imperfecto", "yo"),
        ("conocíamos", "conocer", "imperfecto", "nosotros"),
        ("conocían", "conocer", "imperfecto", "ellos"),

        ("elegía", "elegir", "imperfecto", "yo"),
        ("elegíamos", "elegir", "imperfecto", "nosotros"),
        ("elegían", "elegir", "imperfecto", "ellos"),


        ("hablaré", "hablar", "futuro", "yo"), 
        ("hablarás", "hablar", "futuro", "tu"), 
        ("hablará", "hablar", "futuro", "el"), 
        ("hablaremos", "hablar", "futuro", "nosotros"), 
        ("hablaréis", "hablar", "futuro", "vosotros"), 
        ("hablarán", "hablar", "futuro", "ellos"),

        ("comeré", "comer", "futuro", "yo"), 
        ("comerás", "comer", "futuro", "tu"), 
        ("comerá", "comer", "futuro", "el"), 
        ("comeremos", "comer", "futuro", "nosotros"), 
        ("comeréis", "comer", "futuro", "vosotros"), 
        ("comerán", "comer", "futuro", "ellos"),

        ("viviré", "vivir", "futuro", "yo"), 
        ("vivirás", "vivir", "futuro", "tu"), 
        ("vivirá", "vivir", "futuro", "el"), 
        ("viviremos", "vivir", "futuro", "nosotros"), 
        ("viviréis", "vivir", "futuro", "vosotros"), 
        ("vivirán", "vivir", "futuro", "ellos"),

        #Les 12 radicaux irréguliers

        ("tendré", "tener", "futuro", "yo"), 
        ("tendrás", "tener", "futuro", "tu"), 
        ("tendrá", "tener", "futuro", "el"), 
        ("tendremos", "tener", "futuro", "nosotros"), 
        ("tendréis", "tener", "futuro", "vosotros"), 
        ("tendrán", "tener", "futuro", "ellos"),

        ("vendré", "venir", "futuro", "yo"), 
        ("vendrás", "venir", "futuro", "tu"), 
        ("vendrá", "venir", "futuro", "el"), 
        ("vendremos", "venir", "futuro", "nosotros"), 
        ("vendréis", "venir", "futuro", "vosotros"), 
        ("vendrán", "venir", "futuro", "ellos"),

        ("pondré", "poner", "futuro", "yo"), 
        ("pondrás", "poner", "futuro", "tu"), 
        ("pondrá", "poner", "futuro", "el"), 
        ("pondremos", "poner", "futuro", "nosotros"), 
        ("pondréis", "poner", "futuro", "vosotros"), 
        ("pondrán", "poner", "futuro", "ellos"),

        ("saldré", "salir", "futuro", "yo"), 
        ("saldrás", "salir", "futuro", "tu"),
        ("saldrá", "salir", "futuro", "el"), 
        ("saldremos", "salir", "futuro", "nosotros"), 
        ("saldréis", "salir", "futuro", "vosotros"), 
        ("saldrán", "salir", "futuro", "ellos"),

        ("podré", "poder", "futuro", "yo"), 
        ("podrás", "poder", "futuro", "tu"), 
        ("podrá", "poder", "futuro", "el"), 
        ("podremos", "poder", "futuro", "nosotros"), 
        ("podréis", "poder", "futuro", "vosotros"), 
        ("podrán", "poder", "futuro", "ellos"),

        ("sabré", "saber", "futuro", "yo"), 
        ("sabrás", "saber", "futuro", "tu"), 
        ("sabrá", "saber", "futuro", "el"), 
        ("sabremos", "saber", "futuro", "nosotros"), 
        ("sabréis", "saber", "futuro", "vosotros"), 
        ("sabrán", "saber", "futuro", "ellos"),

        ("querré", "querer", "futuro", "yo"), 
        ("querrás", "querer", "futuro", "tu"), 
        ("querrá", "querer", "futuro", "el"), 
        ("querremos", "querer", "futuro", "nosotros"), 
        ("querréis", "querer", "futuro", "vosotros"), 
        ("querrán", "querer", "futuro", "ellos"),

        ("haré", "hacer", "futuro", "yo"),
        ("harás", "hacer", "futuro", "tu"), 
        ("hará", "hacer", "futuro", "el"), 
        ("haremos", "hacer", "futuro", "nosotros"), 
        ("haréis", "hacer", "futuro", "vosotros"), 
        ("harán", "hacer", "futuro", "ellos"),

        ("diré", "decir", "futuro", "yo"), 
        ("dirás", "decir", "futuro", "tu"), 
        ("dirá", "decir", "futuro", "el"), 
        ("diremos", "decir", "futuro", "nosotros"), 
        ("diréis", "decir", "futuro", "vosotros"), 
        ("dirán", "decir", "futuro", "ellos"),

        ("habré", "haber", "futuro", "yo"), 
        ("habrás", "haber", "futuro", "tu"), 
        ("habrá", "haber", "futuro", "el"), 
        ("habremos", "haber", "futuro", "nosotros"), 
        ("habréis", "haber", "futuro", "vosotros"), 
        ("habrán", "haber", "futuro", "ellos"),

        ("cabré", "caber", "futuro", "yo"), 
        ("cabrás", "caber", "futuro", "tu"), 
        ("cabrá", "caber", "futuro", "el"), 
        ("cabremos", "caber", "futuro", "nosotros"), 
        ("cabréis", "caber", "futuro", "vosotros"), 
        ("cabrán", "caber", "futuro", "ellos"),

        ("valdré", "valer", "futuro", "yo"), 
        ("valdrás", "valer", "futuro", "tu"), 
        ("valdrá", "valer", "futuro", "el"), 
        ("valdremos", "valer", "futuro", "nosotros"), 
        ("valdréis", "valer", "futuro", "vosotros"), 
        ("valdrán", "valer", "futuro", "ellos"),

        #2. Conditionnel — condicional Verbes réguliers

        ("hablaría", "hablar", "condicional", "yo"), ("hablarías", "hablar", "condicional", "tu"), ("hablaría", "hablar", "condicional", "el"), ("hablaríamos", "hablar", "condicional", "nosotros"), ("hablaríais", "hablar", "condicional", "vosotros"), ("hablarían", "hablar", "condicional", "ellos"),

        ("comería", "comer", "condicional", "yo"), ("comerías", "comer", "condicional", "tu"), ("comería", "comer", "condicional", "el"), ("comeríamos", "comer", "condicional", "nosotros"), ("comeríais", "comer", "condicional", "vosotros"), ("comerían", "comer", "condicional", "ellos"),

        ("viviría", "vivir", "condicional", "yo"), ("vivirías", "vivir", "condicional", "tu"), ("viviría", "vivir", "condicional", "el"), ("viviríamos", "vivir", "condicional", "nosotros"), ("viviríais", "vivir", "condicional", "vosotros"), ("vivirían", "vivir", "condicional", "ellos"),

        # Radicaux irréguliers

        ("tendría", "tener", "condicional", "yo"), ("tendrías", "tener", "condicional", "tu"), ("tendría", "tener", "condicional", "el"), ("tendríamos", "tener", "condicional", "nosotros"), ("tendríais", "tener", "condicional", "vosotros"), ("tendrían", "tener", "condicional", "ellos"),

        ("vendría", "venir", "condicional", "yo"), ("vendrías", "venir", "condicional", "tu"), ("vendría", "venir", "condicional", "el"), ("vendríamos", "venir", "condicional", "nosotros"), ("vendríais", "venir", "condicional", "vosotros"), ("vendrían", "venir", "condicional", "ellos"),

        ("pondría", "poner", "condicional", "yo"), ("pondrías", "poner", "condicional", "tu"), ("pondría", "poner", "condicional", "el"), ("pondríamos", "poner", "condicional", "nosotros"), ("pondríais", "poner", "condicional", "vosotros"), ("pondrían", "poner", "condicional", "ellos"),

        ("saldría", "salir", "condicional", "yo"), ("saldrías", "salir", "condicional", "tu"), ("saldría", "salir", "condicional", "el"), ("saldríamos", "salir", "condicional", "nosotros"), ("saldríais", "salir", "condicional", "vosotros"), ("saldrían", "salir", "condicional", "ellos"),

        ("podría", "poder", "condicional", "yo"), ("podrías", "poder", "condicional", "tu"), ("podría", "poder", "condicional", "el"), ("podríamos", "poder", "condicional", "nosotros"), ("podríais", "poder", "condicional", "vosotros"), ("podrían", "poder", "condicional", "ellos"),

        ("sabría", "saber", "condicional", "yo"), ("sabrías", "saber", "condicional", "tu"), ("sabría", "saber", "condicional", "el"), ("sabríamos", "saber", "condicional", "nosotros"), ("sabríais", "saber", "condicional", "vosotros"), ("sabrían", "saber", "condicional", "ellos"),

        ("querría", "querer", "condicional", "yo"), ("querrías", "querer", "condicional", "tu"), ("querría", "querer", "condicional", "el"), ("querríamos", "querer", "condicional", "nosotros"), ("querríais", "querer", "condicional", "vosotros"), ("querrían", "querer", "condicional", "ellos"),

        ("haría", "hacer", "condicional", "yo"), ("harías", "hacer", "condicional", "tu"), ("haría", "hacer", "condicional", "el"), ("haríamos", "hacer", "condicional", "nosotros"), ("haríais", "hacer", "condicional", "vosotros"), ("harían", "hacer", "condicional", "ellos"),

        ("diría", "decir", "condicional", "yo"), ("dirías", "decir", "condicional", "tu"), ("diría", "decir", "condicional", "el"), ("diríamos", "decir", "condicional", "nosotros"), ("diríais", "decir", "condicional", "vosotros"), ("dirían", "decir", "condicional", "ellos"),

        ("habría", "haber", "condicional", "yo"), ("habrías", "haber", "condicional", "tu"), ("habría", "haber", "condicional", "el"), ("habríamos", "haber", "condicional", "nosotros"), ("habríais", "haber", "condicional", "vosotros"), ("habrían", "haber", "condicional", "ellos"),

        ("cabría", "caber", "condicional", "yo"), ("cabrías", "caber", "condicional", "tu"), ("cabría", "caber", "condicional", "el"), ("cabríamos", "caber", "condicional", "nosotros"), ("cabríais", "caber", "condicional", "vosotros"), ("cabrían", "caber", "condicional", "ellos"),

        ("valdría", "valer", "condicional", "yo"), ("valdrías", "valer", "condicional", "tu"), ("valdría", "valer", "condicional", "el"), ("valdríamos", "valer", "condicional", "nosotros"), ("valdríais", "valer", "condicional", "vosotros"), ("valdrían", "valer", "condicional", "ellos"),

        # 3. Futur antérieur — futuro_perfecto -Participes réguliers

        ("habré hablado", "hablar", "futuro_perfecto", "yo"), ("habrás hablado", "hablar", "futuro_perfecto", "tu"), ("habrá hablado", "hablar", "futuro_perfecto", "el"), ("habremos hablado", "hablar", "futuro_perfecto", "nosotros"), ("habréis hablado", "hablar", "futuro_perfecto", "vosotros"), ("habrán hablado", "hablar", "futuro_perfecto", "ellos"),

        ("habré comido", "comer", "futuro_perfecto", "yo"), ("habrás comido", "comer", "futuro_perfecto", "tu"), ("habrá comido", "comer", "futuro_perfecto", "el"), ("habremos comido", "comer", "futuro_perfecto", "nosotros"), ("habréis comido", "comer", "futuro_perfecto", "vosotros"), ("habrán comido", "comer", "futuro_perfecto", "ellos"),

        ("habré vivido", "vivir", "futuro_perfecto", "yo"), ("habrás vivido", "vivir", "futuro_perfecto", "tu"), ("habrá vivido", "vivir", "futuro_perfecto", "el"), ("habremos vivido", "vivir", "futuro_perfecto", "nosotros"), ("habréis vivido", "vivir", "futuro_perfecto", "vosotros"), ("habrán vivido", "vivir", "futuro_perfecto", "ellos"),

        # Participes irréguliers courants

        ("habré hecho", "hacer", "futuro_perfecto", "yo"), ("habrá dicho", "decir", "futuro_perfecto", "el"), ("habremos puesto", "poner", "futuro_perfecto", "nosotros"), ("habrán visto", "ver", "futuro_perfecto", "ellos"), ("habré escrito", "escribir", "futuro_perfecto", "yo"), ("habrás abierto", "abrir", "futuro_perfecto", "tu"), ("habrá vuelto", "volver", "futuro_perfecto", "el"), ("habremos roto", "romper", "futuro_perfecto", "nosotros"), ("habréis muerto", "morir", "futuro_perfecto", "vosotros"), ("habrán resuelto", "resolver", "futuro_perfecto", "ellos"), ("habré cubierto", "cubrir", "futuro_perfecto", "yo"),

        #4. Conditionnel passé — condicional_perfecto - Participes réguliers

        ("habría hablado", "hablar", "condicional_perfecto", "yo"), ("habrías hablado", "hablar", "condicional_perfecto", "tu"), ("habría hablado", "hablar", "condicional_perfecto", "el"), ("habríamos hablado", "hablar", "condicional_perfecto", "nosotros"), ("habríais hablado", "hablar", "condicional_perfecto", "vosotros"), ("habrían hablado", "hablar", "condicional_perfecto", "ellos"),

        ("habría comido", "comer", "condicional_perfecto", "yo"), ("habrías comido", "comer", "condicional_perfecto", "tu"), ("habría comido", "comer", "condicional_perfecto", "el"), ("habríamos comido", "comer", "condicional_perfecto", "nosotros"), ("habríais comido", "comer", "condicional_perfecto", "vosotros"), ("habrían comido", "comer", "condicional_perfecto", "ellos"),

        ("habría vivido", "vivir", "condicional_perfecto", "yo"), ("habrías vivido", "vivir", "condicional_perfecto", "tu"), ("habría vivido", "vivir", "condicional_perfecto", "el"), ("habríamos vivido", "vivir", "condicional_perfecto", "nosotros"), ("habríais vivido", "vivir", "condicional_perfecto", "vosotros"), ("habrían vivido", "vivir", "condicional_perfecto", "ellos"),

        # Participes irréguliers courants

        ("habría hecho", "hacer", "condicional_perfecto", "yo"), ("habría dicho", "decir", "condicional_perfecto", "yo"), ("habrías puesto", "poner", "condicional_perfecto", "tu"), ("habría visto", "ver", "condicional_perfecto", "el"), ("habríamos escrito", "escribir", "condicional_perfecto", "nosotros"), ("habríais abierto", "abrir", "condicional_perfecto", "vosotros"), ("habrían vuelto", "volver", "condicional_perfecto", "ellos"), ("habría roto", "romper", "condicional_perfecto", "yo"), ("habríamos muerto", "morir", "condicional_perfecto", "nosotros"), ("habrían resuelto", "resolver", "condicional_perfecto", "ellos"), ("habría cubierto", "cubrir", "condicional_perfecto", "yo"),




        
    ]

    errors = 0

    for expected, verb, tense, person in tests:
        if not test(expected, verb, tense, person):
            errors += 1

    print("=" * 70)
    print("TESTS DU MOTEUR DE CONJUGAISON V15")
    print("=" * 70)
    print()
    print(f"Tests effectués : {len(tests)}")
    print(f"Erreurs : {errors}")
    print()

    if errors == 0:
        print("TOUS LES TESTS SONT PASSÉS.")
        print("Le moteur V15 est prêt.")
    else:
        print("DES TESTS ONT ÉCHOUÉ.")
        print("L'interface ne sera pas lancée.")

    print("=" * 70)

    return errors == 0





if __name__ == "__main__":
    success = run_global_tests()
    raise SystemExit(0 if success else 1)
