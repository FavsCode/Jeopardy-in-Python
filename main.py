"""main.py - The main entry point of the program."""


def main() -> None:
    teams = None
    while teams not in range(2, 7):
        try:
            teams = int(input("How many teams would you like to play with? "))
        except TypeError:
            continue

    if teams != None:
        # Importing gui creates and configures the Tk root window, so it has to be imported after the prompt
        import gui

        gui.open_scoreboard(teams)
        gui.root.mainloop()


if __name__ == "__main__":
    main()
