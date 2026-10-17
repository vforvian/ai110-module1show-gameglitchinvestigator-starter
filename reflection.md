# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
For the first few attempts, it seemed to be running fine as it kept giving "Go LOWER!" message but as I eventually reached 1, it gave the same message which is when I noticed that there's a bug since 1 is the lowest possible result. As I had more attempts left, I tried out negative number but it still returned "Go LOWER!" message. With new game with new number, it game "Go HIGHER" message with the highest value of 100, and even for a number greater than 100. After the "Game over" message, I pressed "New Game" button and the game over message didn't disappear, nor it took in new inputs.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The hint was off; it only gave "Go LOWER!" messag for my trial even when it reached the lowest number.
"Go HIGHER!" hint appeared with the highest number. The function related to the hint seems off.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|      Input      | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|-----------------|-------------------|-----------------|------------------------|-------------------------|
|   guess of 1    | "Go HIGHER" hint  | "Go LOWER" hint |         none           |   app.py, check_guess   | 
|  guess of 100   | "Go LOWER" hint   | "Go HIGHER" hint|         none           |   app.py, check_guess   | 
|press "New Game" |"New game started."|no new game but  |         none           |   app.py, new_game or   |
|after "Game over"| & fresh attempts  |new attempts     |                        |     session_state       |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It pointed out that when the player runs out attempts, the session state gets lost and that was cause of the new game bug.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
It wasn't exactly the result of interaction with Claude Code, but with the auto fill on the code, as I was fixing the bug on high/low hint, it was trying to suggest putting the lines of code under same condition but both so I ignored it and only made the changes that was needed.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tried out different situations after the fix.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran both manual of differnt situations that it initially had bugs and pytest. There were initially multiple bugs and even though the instruction asked to fix 2 bugs, I was quite annoyed by how the game still wasn't working properly and eneded up fixing all that Claude and I detected. There was an additional hurdle for running pytest because of having dual messages for the hints but was able to make some changes and have it pass the test.
- Did AI help you design or understand any tests? How?
Absolutely. It helps me with running the test by suggest all possible outcomes and situations to get them. Also, with running them a lot faster than I can manually do.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
When the streamlit reruns, it actually runs app.py file all again. However, with session_state, it keeps the value between reruns. Through that, we were able to see the history of our input values through Developer Debug Info.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
How I attached the specific file as I had the idea of where the bug could've been located and collaborate with Claude to detect that bug and even additional ones. In addition, I always to prefer checking them myself before letting Claude make any changes so will continue to go that way.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Claude actually found more bugs that I did through manual testing. I wouldn't necessarily consider it bad but it kind of went too far ahead of how I wanted to follow through the instruction step-by-step.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
Instead of giving a general and broad prompts to let the AI do all the work, I honestly gained more confidence is the quality of the result by somewhat figuring out with it together.