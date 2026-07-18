<div align="center">

# ⌨️ Typing Speed Tester

### *How fast can your fingers really go?*

```
 _____          _             ___                  _   _____       _
|_   _|  _ _ __(_)_ _  __ _  / __|_ __  ___ ___ __| | |_   _|__ __| |_ ___ _ _
  | || || | '_ \ | ' \/ _` | \__ \ '_ \/ -_) -_) _` |   | |/ -_|_-<  _/ -_) '_|
  |_| \_, | .__/_|_||_\__, | |___/ .__/\___\___\__,_|   |_|\___/__/\__\___|_|
      |__/|_|         |___/      |_|
```

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Colorama-Enabled-FFD43B?style=for-the-badge)
![Modes](https://img.shields.io/badge/Modes-Difficulty%20%7C%20Category-6E44FF?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-Terminal-000000?style=for-the-badge&logo=windowsterminal&logoColor=white)
![Status](https://img.shields.io/badge/Status-Practice%20Project-orange?style=for-the-badge)

</div>

---

## ✨ Overview

**Typing Speed Tester** is a colorful, terminal-based typing test that measures your **WPM**, **CPM**, and **accuracy** against curated passages. Choose a **difficulty** or a **topic category**, type out the passage as fast and accurately as you can, and get an instant performance breakdown.

## 🎨 Preview

```
 _____          _             ___                  _   _____       _
|_   _|  _ _ __(_)_ _  __ _  / __|_ __  ___ ___ __| | |_   _|__ __| |_ ___ _ _
  | || || | '_ \ | ' \/ _` | \__ \ '_ \/ -_) -_) _` |   | |/ -_|_-<  _/ -_) '_|
  |_| \_, | .__/_|_||_\__, | |___/ .__/\___\___\__,_|   |_|\___/__/\__\___|_|
      |__/|_|         |___/      |_|

==============================================
               MAIN MENU
==============================================
  [1] Select Difficulty (Easy / Medium / Hard)
  [2] Select Category
  [3] Exit
Enter your choice: 1

==========================
      DIFFICULTY MENU
==========================
  [1] Easy
  [2] Medium
  [3] Hard
==========================
Select difficulty: 1

I wake up early every day to see the sun come up. The morning air is
cool and fresh. I like to sit by the window with a warm cup of tea.

Enter the above passage:I wake up early every day to see the sun come up.

  WPM :42
  CPM :210
  ACCURACY :97%
Press enter to continue...
```

## 🧩 Features Explained

<div align="center">

| Feature | How it works |
|:---|:---|
| 🎚️ **Difficulty Mode** | Pick **Easy**, **Medium**, or **Hard** — each pulls passages from its own dedicated text file. |
| 🗂️ **Category Mode** | Pick from **6 topics** — General Knowledge, History, Literature, Programming, Quotes, Science — each with its own passage pool. |
| 🔁 **Sequential Passages** | Passages are served **in order, not repeated back-to-back** — each mode/category tracks its own position and cycles through once you've seen them all. |
| ⏱️ **Live Timer** | A high-resolution timer starts the moment the passage is shown and stops the instant you hit Enter. |
| ⚡ **WPM Calculation** | Words per minute is derived from your typed character count (`chars ÷ 5`) divided by the elapsed time. |
| 🔤 **CPM Calculation** | Characters per minute is calculated directly from how many characters you typed in the time taken. |
| 🎯 **Accuracy Scoring** | Your input is compared character-by-character against the original passage to compute a percentage accuracy score. |
| 🖍️ **Colorized Interface** | Menus, passages, and results are all styled with `colorama` for a clean, readable experience. |
| 🧾 **Wrapped Passage Display** | Passages are word-wrapped to a readable width instead of spilling across the terminal in one long line. |
| 🖥️ **Auto Screen Clear** | The screen clears between menus and passages, keeping each step focused and clutter-free. |
| 🔂 **Continuous Play Loop** | After each test you return to the main menu — take test after test without restarting the script. |

</div>

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- `colorama` package

### Installation

```bash
git clone https://github.com/vineetgaira/Typing-Speed-Tester.git
cd Typing-Speed-Tester
pip install -r requirements.txt
```

### Run it

```bash
python main.py
```

## 🕹️ How to Play

1. From the **Main Menu**, choose **[1] Select Difficulty** or **[2] Select Category**.
2. Pick a difficulty (**Easy / Medium / Hard**) or a category (**General / History / Literature / Programming / Quotes / Science**).
3. A passage is displayed — read it carefully!
4. Type out the passage exactly as shown, then press **Enter**.
5. Instantly see your **WPM**, **CPM**, and **Accuracy** for that run.
6. Press Enter to return to the menu and try another passage, or choose **[3] Exit** to quit.

## 📊 Understanding Your Results

```
WPM (Words Per Minute)   →  (characters typed ÷ 5) ÷ minutes elapsed
CPM (Characters Per Min) →  characters typed ÷ minutes elapsed
Accuracy                 →  (matched characters ÷ total typed) × 100
```

## 🗂️ Project Structure

```
Typing-Speed-Tester/
├── main.py                      # Entry point — launches the game loop
├── requirements.txt               # Project dependencies
├── src/
│   ├── game.py                      # Main game loop & menu navigation
│   ├── display.py                     # Banner, menus, passage & result rendering
│   ├── passage.py                       # Passage loading, indexing & rotation logic
│   ├── typing.py                          # Captures the user's typed input
│   ├── statistics.py                        # WPM / CPM / accuracy / error calculations
│   ├── timer.py                                # Test start/stop & elapsed time tracking
│   ├── utils.py                                  # Screen clearing & "press enter" pause
│   └── constants.py                                # Time limit constants
└── passage/
    ├── difficulty/                                   # easy.txt · medium.txt · hard.txt
    └── category/                                       # general · history · literature ·
                                                            # programming · quotes · science
```

## 🧠 How Passage Rotation Works

Each difficulty level and category keeps track of its **own position pointer**. Every time you request a passage, the tester serves the next one in sequence (wrapping back to the start once the list is exhausted), so you won't see the same passage twice in a row:

```
position = current_index % total_passages_in_file
serve passages[position]
current_index += 1
```

## 🛠️ Built With

- 🐍 **Python** — core game logic, timing & statistics
- 🎨 **Colorama** — cross-platform colored terminal text
- 📄 **textwrap (stdlib)** — clean passage word-wrapping
- ⏱️ **time (stdlib)** — high-resolution performance timing
- 📁 **pathlib (stdlib)** — reading passage files from disk

## 📈 Roadmap

- [ ] Save and display **best scores** (the `show_best_score()` hook is already stubbed in)
- [ ] Add a countdown/time-limit mode using `MIN_TIME` / `MAX_TIME`
- [ ] Random passage mode instead of purely sequential
- [ ] Highlight mistakes inline (character-by-character diff)
- [ ] Track and graph typing progress over multiple sessions
- [ ] Add unit tests for statistics calculations

## ⚠️ Disclaimer

This is a **practice project** built for learning Python fundamentals — file I/O, modular architecture, timing, and building a real-time feedback loop in a CLI.

## 📄 License

Open source — free to use, learn from, and build upon.

---

<div align="center">

Made with 🐍 Python — *type fast, type true.* ⌨️

</div>
