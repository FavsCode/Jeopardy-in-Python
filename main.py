"""main.py - The main entry point of the program."""
import gui


def main() -> None:
    gui.open_scoreboard()
    gui.root.mainloop()

if __name__ == '__main__':
    main()