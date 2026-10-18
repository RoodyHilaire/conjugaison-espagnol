from test_global import run_global_tests
from test_pronominal import run_pronominal_tests


def run_all_tests():
    print("\n" + "=" * 70)
    print("ÉTAPE 1 : TESTS GÉNÉRAUX")
    print("=" * 70)

    success_global = run_global_tests()

    print("\n" + "=" * 70)
    print("ÉTAPE 2 : TESTS PRONOMINAUX")
    print("=" * 70)

    success_pronominal = run_pronominal_tests()

    success = success_global and success_pronominal

    print("\n" + "=" * 70)
    if success:
        print("TOUS LES TESTS ONT RÉUSSI.")
    else:
        print("AU MOINS UN GROUPE DE TESTS A ÉCHOUÉ.")
    print("=" * 70)

    return success


if __name__ == "__main__":
    raise SystemExit(0 if run_all_tests() else 1)
