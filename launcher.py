
from test import run_all_tests


if __name__ == "__main__":
    success = run_all_tests()

    if success:
        import tkinter as tk
        from interface import ConjugationTrainer

        root = tk.Tk()
        app = ConjugationTrainer(root)
        root.mainloop()
    else:
        print("Interface non lancée : tests échoués.")



