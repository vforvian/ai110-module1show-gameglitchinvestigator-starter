# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [you have a limited number of attempts to find a secret number, with "higher/lower" hints after each guess] Describe the game's purpose.
- [Hints backwards: A guess of 1 said "Go LOWER!" and a guess of 100 said "Go HIGHER!". (The messages in check_guess were swapped.)/ Inconsistent hints: On even-numbered attempts, the secret was turned into text, so "9" > "50" came out True./ No range check: Negative numbers and numbers over 100 were accepted, and the banner always said 1–100.
New Game stuck after Game Over: status stayed "lost", so the game stopped every time the page reloaded.] Detail which bugs you found.
- [swapped the hint messages in check_guess, so a high guess says "Go LOWER!" and a low guess says "Go HIGHER!"/ removed the code that turned the secret into text on even attempts, so hints are the same on every attempt/ added a range check to parse_guess, so guesses outside the difficulty's range are rejected/ changed the banner to show the difficulty's real range instead of always "1 to 100"/ made New Game reset the status, attempts, score, history, and secret, so you can play again after Game Over/ moved the game logic from app.py into logic_utils.py and imported it in app.py/ updated the tests to match the new check_guess output and added tests for hints and range checks.] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User makes a guess and enters "50"
2. Press "Submit Guess" with "Show hint" box checked
3. Get a hint that says "Go HIGHER!"
4. User makes a new guess of "75" and score updates after each guess
5. Game ends after the correct guess, or after the user runs out of the attempts

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
(.venv) (base) Mac:ai110-module1show-gameglitchinvestigator-starter vians$ python3.13 -m pytest
================================================================================================================================= test session starts =================================================================================================================================
platform darwin -- Python 3.13.14, pytest-9.1.1, pluggy-1.7.0
rootdir: /Users/vians/ai110-module1tinker-playlistchaos-starter/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 11 items                                                                                                                                                                                                                                                                    

tests/test_game_logic.py ...........                                                                                                                                                                                                                                            [100%]

================================================================================================================================= 11 passed in 0.01s ==================================================================================================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
