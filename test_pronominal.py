
import unittest

from moteur import conjugate_pronominal


class TestConjugaisonPronominale(unittest.TestCase):

    # --------------------------------------------------------
    # PRESENT DE L'INDICATIF
    # --------------------------------------------------------

    def test_presente_regular(self):
        self.assertEqual(
            conjugate_pronominal("levantarse", "presente", "yo"),
            "me levanto"
        )
        self.assertEqual(
            conjugate_pronominal("levantarse", "presente", "tu"),
            "te levantas"
        )
        self.assertEqual(
            conjugate_pronominal("levantarse", "presente", "el"),
            "se levanta"
        )
        self.assertEqual(
            conjugate_pronominal("levantarse", "presente", "nosotros"),
            "nos levantamos"
        )
        self.assertEqual(
            conjugate_pronominal("levantarse", "presente", "vosotros"),
            "os levantáis"
        )
        self.assertEqual(
            conjugate_pronominal("levantarse", "presente", "ellos"),
            "se levantan"
        )

    def test_presente_stem_change(self):
        self.assertEqual(
            conjugate_pronominal("acostarse", "presente", "tu"),
            "te acuestas"
        )
        self.assertEqual(
            conjugate_pronominal("vestirse", "presente", "yo"),
            "me visto"
        )
        self.assertEqual(
            conjugate_pronominal("vestirse", "presente", "nosotros"),
            "nos vestimos"
        )

    # --------------------------------------------------------
    # TEMPS DU PASSE
    # --------------------------------------------------------

    def test_preterito(self):
        self.assertEqual(
            conjugate_pronominal("levantarse", "preterito", "yo"),
            "me levanté"
        )
        self.assertEqual(
            conjugate_pronominal("levantarse", "preterito", "ellos"),
            "se levantaron"
        )

    def test_imperfecto(self):
        self.assertEqual(
            conjugate_pronominal("levantarse", "imperfecto", "yo"),
            "me levantaba"
        )
        self.assertEqual(
            conjugate_pronominal("levantarse", "imperfecto", "nosotros"),
            "nos levantábamos"
        )

    # --------------------------------------------------------
    # TEMPS COMPOSES
    # --------------------------------------------------------

    def test_perfecto(self):
        self.assertEqual(
            conjugate_pronominal("levantarse", "perfecto", "yo"),
            "me he levantado"
        )
        self.assertEqual(
            conjugate_pronominal("vestirse", "perfecto", "el"),
            "se ha vestido"
        )

    def test_pluscuamperfecto(self):
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "pluscuamperfecto", "yo"
            ),
            "me había levantado"
        )

    def test_futuro_perfecto(self):
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "futuro_perfecto", "yo"
            ),
            "me habré levantado"
        )

    def test_condicional_perfecto(self):
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "condicional_perfecto", "yo"
            ),
            "me habría levantado"
        )

    def test_subjuntivo_compuesto(self):
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "subjuntivo_perfecto", "yo"
            ),
            "me haya levantado"
        )
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "subjuntivo_pluscuamperfecto", "yo"
            ),
            "me hubiera levantado"
        )

    # --------------------------------------------------------
    # SUBJONCTIF SIMPLE
    # --------------------------------------------------------

    def test_subjuntivo_presente(self):
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "subjuntivo_presente", "yo"
            ),
            "me levante"
        )
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "subjuntivo_presente", "tu"
            ),
            "te levantes"
        )

    def test_subjuntivo_imperfecto(self):
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "subjuntivo_imperfecto", "yo"
            ),
            "me levantara"
        )

    # --------------------------------------------------------
    # IMPERATIF AFFIRMATIF : ACCENTS ET PRONOMS ATTACHES
    # --------------------------------------------------------

    def test_imperativo_afirmativo_levantarse(self):
        expected = {
            "tu": "levántate",
            "el": "levántese",
            "nosotros": "levantémonos",
            "vosotros": "levantaos",
            "ellos": "levántense",
        }

        for person, result in expected.items():
            with self.subTest(person=person):
                self.assertEqual(
                    conjugate_pronominal(
                        "levantarse", "imperativo_afirmativo", person
                    ),
                    result
                )

    def test_imperativo_afirmativo_otros_verbos(self):
        self.assertEqual(
            conjugate_pronominal(
                "acostarse", "imperativo_afirmativo", "tu"
            ),
            "acuéstate"
        )
        self.assertEqual(
            conjugate_pronominal(
                "ponerse", "imperativo_afirmativo", "tu"
            ),
            "ponte"
        )
        self.assertEqual(
            conjugate_pronominal(
                "vestirse", "imperativo_afirmativo", "vosotros"
            ),
            "vestíos"
        )

    def test_imperativo_afirmativo_irse(self):
        expected = {
            "tu": "vete",
            "el": "váyase",
            "nosotros": "vámonos",
            "vosotros": "idos",
            "ellos": "váyanse",
        }

        for person, result in expected.items():
            with self.subTest(person=person):
                self.assertEqual(
                    conjugate_pronominal(
                        "irse", "imperativo_afirmativo", person
                    ),
                    result
                )

    # --------------------------------------------------------
    # IMPERATIF NEGATIF
    # --------------------------------------------------------

    def test_imperativo_negativo(self):
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "imperativo_negativo", "tu"
            ),
            "no te levantes"
        )
        self.assertEqual(
            conjugate_pronominal(
                "levantarse", "imperativo_negativo", "nosotros"
            ),
            "no nos levantemos"
        )
        self.assertEqual(
            conjugate_pronominal(
                "ponerse", "imperativo_negativo", "tu"
            ),
            "no te pongas"
        )

    # --------------------------------------------------------
    # VALIDATION DES ENTREES
    # --------------------------------------------------------

    def test_reject_non_pronominal_verb(self):
        with self.assertRaises(ValueError):
            conjugate_pronominal("levantar", "presente", "yo")

    def test_reject_unknown_person(self):
        with self.assertRaises(ValueError):
            conjugate_pronominal("levantarse", "presente", "unknown")

    
    def test_despertarse_presente(self):
        self.assertEqual(
            conjugate_pronominal("despertarse", "presente", "yo"),
            "me despierto"
        )
        self.assertEqual(
            conjugate_pronominal("despertarse", "presente", "tu"),
            "te despiertas"
        )
        self.assertEqual(
            conjugate_pronominal("despertarse", "presente", "nosotros"),
            "nos despertamos"
        )

    def test_sentarse_presente(self):
        self.assertEqual(
            conjugate_pronominal("sentarse", "presente", "yo"),
            "me siento"
        )
        self.assertEqual(
            conjugate_pronominal("sentarse", "presente", "tu"),
            "te sientas"
        )

    def test_dormirse_presente(self):
        self.assertEqual(
            conjugate_pronominal("dormirse", "presente", "yo"),
            "me duermo"
        )
        self.assertEqual(
            conjugate_pronominal("dormirse", "presente", "tu"),
            "te duermes"
        )
        self.assertEqual(
            conjugate_pronominal("dormirse", "presente", "nosotros"),
            "nos dormimos"
        )

    def test_divertirse_presente(self):
        self.assertEqual(
            conjugate_pronominal("divertirse", "presente", "yo"),
            "me divierto"
        )
        self.assertEqual(
            conjugate_pronominal("divertirse", "presente", "ellos"),
            "se divierten"
        )

    def test_llamarse_presente(self):
        self.assertEqual(
            conjugate_pronominal("llamarse", "presente", "yo"),
            "me llamo"
        )
        self.assertEqual(
            conjugate_pronominal("llamarse", "presente", "el"),
            "se llama"
        )

    def test_ducharse_presente(self):
        self.assertEqual(
            conjugate_pronominal("ducharse", "presente", "yo"),
            "me ducho"
        )
        self.assertEqual(
            conjugate_pronominal("ducharse", "presente", "nosotros"),
            "nos duchamos"
        )

    def test_banarse_presente(self):
        self.assertEqual(
            conjugate_pronominal("bañarse", "presente", "yo"),
            "me baño"
        )
        self.assertEqual(
            conjugate_pronominal("bañarse", "presente", "ellos"),
            "se bañan"
        )

    def test_ponerse_presente(self):
        self.assertEqual(
            conjugate_pronominal("ponerse", "presente", "yo"),
            "me pongo"
        )
        self.assertEqual(
            conjugate_pronominal("ponerse", "presente", "tu"),
            "te pones"
        )

    def test_arrepentirse_presente(self):
        self.assertEqual(
            conjugate_pronominal("arrepentirse", "presente", "yo"),
            "me arrepiento"
        )
        self.assertEqual(
            conjugate_pronominal("arrepentirse", "presente", "nosotros"),
            "nos arrepentimos"
        )

    def test_despertarse_imperativo_afirmativo(self):
        self.assertEqual(
            conjugate_pronominal(
                "despertarse", "imperativo_afirmativo", "tu"
            ),
            "despiértate"
        )

    def test_sentarse_imperativo_afirmativo(self):
        self.assertEqual(
            conjugate_pronominal(
                "sentarse", "imperativo_afirmativo", "tu"
            ),
            "siéntate"
        )

    def test_dormirse_imperativo_afirmativo(self):
        self.assertEqual(
            conjugate_pronominal(
                "dormirse", "imperativo_afirmativo", "tu"
            ),
            "duérmete"
        )

    def test_divertirse_imperativo_afirmativo(self):
        self.assertEqual(
            conjugate_pronominal(
                "divertirse", "imperativo_afirmativo", "tu"
            ),
            "diviértete"
        )

    def test_despertarse_imperativo_negativo(self):
        self.assertEqual(
            conjugate_pronominal(
                "despertarse", "imperativo_negativo", "tu"
            ),
            "no te despiertes"
        )

    def test_sentarse_imperativo_negativo(self):
        self.assertEqual(
            conjugate_pronominal(
                "sentarse", "imperativo_negativo", "tu"
            ),
            "no te sientes"
        )

    def test_dormirse_imperativo_negativo(self):
        self.assertEqual(
            conjugate_pronominal(
                "dormirse", "imperativo_negativo", "tu"
            ),
            "no te duermas"
        )


def run_pronominal_tests():
    import unittest

    suite = unittest.defaultTestLoader.loadTestsFromModule(
        __import__(__name__)
    )

    result = unittest.TextTestRunner(verbosity=2).run(suite)

    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_pronominal_tests()
    raise SystemExit(0 if success else 1)


# if __name__ == "__main__":
#     unittest.main(verbosity=2)
