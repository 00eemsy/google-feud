### hi and welcome to my README !! ###

## DESCRIPTION ##
> this project is based off of the popular online game "Google Feud" **(https://googlefeud.com/)**, that is inspired by the autocomplete function of the Google search engine. in the game, the player fills in the blanks of partial search queries to find most common autocomplete suggestions for that partial search query.

a successful attempt: 
![](https://github.com/00eemsy/google-feud/blob/main/success.gif)

a failed attempt:
![](https://github.com/00eemsy/google-feud/blob/main/fail.gif)

> i took inspiration from this game and recreated it with PyTrends, a Python library which makes accessing the Google Trends API easier. although not 100% the same, i used its related queries function to find the top related queries to certain keywords. 

## INSTRUCTIONS ##
> delete the prompt text & type in what you believe to be the top related query given the keyword into the entry box. -> press the guess button -> continue until you lose or win

## MY FILES ##
**gf_data.py**
- purpose: organize PyTrends data and convert into accessible/readable lists
- contains: clean_data, mlist_set_up, console_list_set_up

**gf_metrics.py**
- purpose: hold Metrics class for its globally accessible variables
- contains: class Metrics

**gf_tk.py**
- purpose: 1. set up tkinter gui, 2. create functions that interact/update these gui elements to run game successfully
- contains: tkinter window set up, print_to_tkinter, check_if_winning, guessing

## MISC ##
> have questions? noticed bugs? suggestions? please reach out at **eyu@reed.edu**
