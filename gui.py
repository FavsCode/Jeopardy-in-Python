import tkinter as tk


def open_scoreboard() -> None:
    """A function to open the scoreboard of Jeopardy!"""
    # Create a secondary window linked to the main root window

    scoreboard = tk.Toplevel(root)
    scoreboard.title("Scoreboard")
    scoreboard.geometry("640x360")
    scoreboard.attributes("-topmost", True)

    # Add widgets to the scoreboard by passing it as the parent

    for row in range(2):
        scoreboard.rowconfigure(row, weight=1)
        for column in range(3):
            scoreboard.columnconfigure(column, weight=1)
            if row == 0:
                label = tk.Label(
                    scoreboard,
                    background="#060ce9",
                    borderwidth=4,
                    relief="solid",
                    font=("Bahnschrift SemiBold Condensed", 35, "bold"),
                    fg="#E5E5E5",
                    text=f"Team {row + 1 + column}\n0",  # So row 0, column one would be is 2
                )
            else:
                label = tk.Label(
                    scoreboard,
                    background="#060ce9",
                    borderwidth=4,
                    relief="solid",
                    font=("Bahnschrift SemiBold Condensed", 35, "bold"),
                    fg="#E5E5E5",
                    text=f"Team {row + 1 + column + 2}\n0",  # So row 1, column one would be is 5
                )
    
            label.grid(row=row, column=column, sticky="nsew")


root = tk.Tk()

# Setting the main window properties

root.title("Jeopardy! in Python")
root.configure(background="#060ce9")
root.state("zoomed")

# Adding the headers

root.rowconfigure(0, weight=1)  # Configuring the header row beforehand

for i in range(6):
    # Stretch the grid into proportion by ensuring all extra column space is allocated to the widgets
    root.columnconfigure(i, weight=1)

    label = tk.Label(
        root,
        background="#060ce9",
        borderwidth=4,
        relief="solid",
        font=("Bahnschrift SemiBold Condensed", 35),
        fg="#D9D9D9",
        text=i + 1,
    )
    label.grid(row=0, column=i, sticky="nsew")

# Making the grid and the labels

for row in range(1, 6):  # Starting on row 1! (0, 1, 2...)
    # Stretch the grid into proportion by ensuring all extra column space is allocated to the widgets
    root.rowconfigure(row, weight=1)
    for column in range(6):
        label = tk.Label(
            root,
            background="#060ce9",
            borderwidth=3,
            relief="solid",
            font=("Bahnschrift SemiBold Condensed", 70, "bold"),
            fg="#E1B530",
            text=f"${(row) * 200}",  # So row 0 is $200 and so on...
        )
        label.grid(row=row, column=column, sticky="nsew")

open_scoreboard()
root.mainloop()
