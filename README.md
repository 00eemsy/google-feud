## 👩🏻‍💻 DESCRIPTION
Welcome to `google feud 🔍`, a game that asks you to embody your inner Google autocomplete and fill in the blanks for the most common autocomplete suggestions of a certain prompt! This project was heavily inspired by the popular online game, [**Google Feud**](https://googlefeud.com/).

I recreated the game with the [**Pytrends API**](https://pypi.org/project/pytrends/), an API that connects to Google Trends for stats on top queries, related queries, etc. with the data from this API, this game was born. And to beautify the project, I used [**Tkinter**](https://docs.python.org/3/library/tkinter.html), a Python GUI.

This project was a result of a penchant to learn about what makes software _software_ in this day and age. My university's curriculum is heavily concepts-based, which is definitely necessary and important information, but I was curious about how to translate that theoretical knowledge into practice. Enjoy my little experiment!

⬇️ Opening still of `google feud`
![](./visuals/opening-still.png)
<br>

## 💡 INSTRUCTIONS 
* Delete the prompt in the query box
* Using the length of the underscored prompts, type in your guess for the top-most related query for _x_ prompt
* Press the "guess" button
* If you are wrong, your "errors" count will go up by one. If you are right, your "score" will go up by one and you'll see that prompt filled in on your screen. 
* Continue guessing! Too many errors and your game will end; if you fill in every blank on the screen, you win!

### Other Details 🌟
* To customize the prompt, go into `gf_metrics.py` and replace the string value of the `self.keyword` variable. It must be a singular word only; **multiple words cause the prompts to populate incorrectly.**
![](./visuals/keyword.gif)

##  📦 INSTALLING AND RUNNING 
1. From [00eemsy/google-feud](https://github.com/00eemsy/google-feud), download the following files:
    * `gf_data.py` (Utilizes the Pytrend API's query data and makes it more comprehensible)
    * `gf_metrics.py` (Stores global variables)
    * `gf_tk.py` (Runs the game mechanics and GUI)
    * `gf.png` (Google Feud logo, used in the GUI)
2. Using your preferred console, type the following:
```
python3 gf_tk.py
```
This will redirect you to a pop-up window 
<br>
* Sometimes Pytrends return this error:
```
pytrends.exceptions.TooManyRequestsError: The request failed: Google returned a response with code 429
```
 Completely normal! Sometimes Google Trends is overwhelmed by requests, just run the above console entry again.


## 🎮 DEMOS 
_A successful attempt_
![](./visuals/success.gif)

_A failed attempt_
![](./visuals/fail.gif)

_Winning the game_
![](./visuals/win.gif)
