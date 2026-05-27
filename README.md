Merlin is a lightweight, interactive Terminal User Interface (TUI) designed for micro-logging and daily journaling. Built completely in Python using the native "curses" library, it allows you to quickly log thoughts, stamp timestamps, and categorize entries using semantic color tags without your fingers ever leaving the home row.

Key Features:

    1. Smart In-Line Formatting: Expressive shorthand color tokens (`#r` for red, `#g`
    for green, etc.).
    2. Hybrid Storage Architecture: Automatically adheres to modern Linux XDG
    specifications (`~/.local/share`) but locks into a completely isolated standalone
    portable mode if a local `/data` directory is detected.

Merlin can be installed or not, the only difference between those options is
that installing it allows you to open it by just calling "merlin" in the terminal
and the portable way requires you to navigate to "merlin.py".

  Installation:

    1. Unzip Merlin.zip and place the resulting folder where you want the program to
    be installed.
    2. Open the terminal in the folder and give permissions to "setup.sh" and run it:
        -> chmod +x setup.sh
        -> ./setup.sh
    3. Open the program:
        -> merlin

  Portable usage:

    1. Unzip Merlin.zip and place the resulting folder where you want the program to
    be used.
    2. Open the terminal in the folder and give permissions to "merlin.py":
        -> chmod +x merlin.py
    3. Open the program:
        -> python3 merlin.py

Developer comment: I made the program with AI's help just to take quick notes at
university and kill some time, if you like it I hope you enjoy it.
