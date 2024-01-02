from tkinter import *
from PIL import ImageTk, Image

from gf_metrics import *
from gf_data import *

# regular set up (same in console ver.)
keyword = metrics.keyword.lower()
dict = clean_data()
m = mlist_set_up(dict)
c = console_list_set_up(m)

# setting up the Tkinter window
root = Tk()
root.title("PyTrends Google Feud")

# and frames (so the logo png size doesn't mess up the column spacing)
logoFrame = LabelFrame(root, borderwidth=0) # holds Google Feud img, entry box, blank label
guessFrame = LabelFrame(root, borderwidth=0) # holds all of the labels for search results
metricsFrame = LabelFrame(root,borderwidth=0) # holds the score, spacer label, the # of errors

# adding in the Google Feud logo :)
logo = Image.open("gf.png") # credit: from https://googlefeud.com/ !!! 
logo = logo.resize((500,95)) # halving the dimensions
logo = ImageTk.PhotoImage(logo)

logoLabel = Label(logoFrame, image=logo)
logoLabel.grid(row=0) # putting it at the top of the logoFrame

# entry box for guessing!
myEntry = Entry(logoFrame, font="Monaco 12")
myEntry.insert(0, 'what is the top related query for "' + str(metrics.keyword) + '"?: (delete me)') # puts text there as a prompt
myEntry.grid(row=1, sticky=W+E) # sticky to make it span across the row

# blank for spacing
blankLabel = Label(logoFrame)
blankLabel.grid(row=2)

# metrics
scoreLabel = Label(metricsFrame, text="score: " + str(metrics.score), font="Monaco") # accessing via the class variables
scoreLabel.grid(row=0,column=0)

blankLabel01 = Label(metricsFrame, text="  |  ") # spacer label
blankLabel01.grid(row=0,column=1)

errorsLabel = Label(metricsFrame, text="errors: " + str(metrics.errors), font="Monaco")
errorsLabel.grid(row=0,column=2)

# a million labels for our guesses :)
label1 = Label(guessFrame, font="Monaco")
label1.grid(row=0,column=0)

label2 = Label(guessFrame, font="Monaco")
label2.grid(row=1,column=0)

label3 = Label(guessFrame, font="Monaco")
label3.grid(row=2,column=0)

label4 = Label(guessFrame, font="Monaco")
label4.grid(row=3,column=0)

label5 = Label(guessFrame, font="Monaco")
label5.grid(row=4,column=0)

label6 = Label(guessFrame, font="Monaco")
label6.grid(row=0,column=1)

label7 = Label(guessFrame, font="Monaco")
label7.grid(row=1,column=1)

label8 = Label(guessFrame, font="Monaco")
label8.grid(row=2,column=1)

label9 = Label(guessFrame, font="Monaco")
label9.grid(row=3,column=1)

label10 = Label(guessFrame, font="Monaco")
label10.grid(row=4,column=1)

label11 = Label(guessFrame, font="Monaco")
label11.grid(row=0,column=2)

label12 = Label(guessFrame, font="Monaco")
label12.grid(row=1,column=2)

label13 = Label(guessFrame, font="Monaco")
label13.grid(row=2,column=2)

label14 = Label(guessFrame, font="Monaco")
label14.grid(row=3,column=2)

label15 = Label(guessFrame, font="Monaco")
label15.grid(row=4,column=2)

label16 = Label(guessFrame, font="Monaco")
label16.grid(row=0,column=3)

label17 = Label(guessFrame, font="Monaco")
label17.grid(row=1,column=3)

label18 = Label(guessFrame, font="Monaco")
label18.grid(row=2,column=3)

label19 = Label(guessFrame, font="Monaco")
label19.grid(row=3,column=3)

label20= Label(guessFrame, font="Monaco")
label20.grid(row=4,column=3)

label21 = Label(guessFrame, font="Monaco")
label21.grid(row=0,column=4)

label22 = Label(guessFrame, font="Monaco")
label22.grid(row=1,column=4)

label23 = Label(guessFrame, font="Monaco")
label23.grid(row=2,column=4)

label24 = Label(guessFrame, font="Monaco")
label24.grid(row=3,column=4)

# packing the frames now (gridding's usually the better option but the frames hold everything in an organized fashion soo)
logoFrame.pack()
guessFrame.pack()

# blank for spacing pt.2
blankLabel2 = Label(root) # not in a frame!! just putting it between guessFrame, the button, and metricsFrame
blankLabel2.pack()

# guess button
myButton = Button(root, text="guess", command= lambda: guessing(myEntry.get(), m, c), font="Monaco") # again, not in a frame! also connects to guessing function below (using the input from myEntry as a guess)
myButton.pack()

# blank for spacing pt.3
blankLabel3 = Label(root)
blankLabel3.pack()

# more packing
metricsFrame.pack()

# winLoseLabel to tell me once i lose or win
win_statement = "YOU WON :)!"
lose_statement = "YOU LOST, BEST LUCK NEXT TIME :,)!"

winLoseLabel = Label(root,text="", font="Monaco 20") # no text rn bc it updates to win/lose statement when those conditions are met
winLoseLabel.pack()


'''
🏳️ PRINT_TO_TKINTER:

- WHAT it does: takes the mlist and makes a client-facing version (underscores, etc.) that's also easier to manipulate (each word individually)
- HOW it does it: 
- arguments: mlist (list of all of the search results), console_list (list that's client facing [includes underscores, etc.]) | return values: none, but updates the tkinter window

'''
def print_to_tkinter(mlist, console_list):
    
    clist_count = 0 # to traverse the console_list (which bc of it's word by word format, requires a dif traversal variable)
    count = 0 # to continue through the while loop and traverse the mlist

    # list of labels to use to update the labels above!!!
    label_list = [label1,label2,label3,label4,label5,label6,label7,label8,label9,label10,label11,label12,label13,label14,label15,label16,label17,label18,label19,label20,label21,label22,label23,label24]

    while count < len(mlist) and clist_count < len(console_list): 

        temp_str = "🔍 " + str(count + 1) + ". " # adding some cute formatting at the beginning of the string

        labelName = label_list[count] # accessing list to get a label to config later

        temp_list = mlist[count].split() # split it up!! (to get a sense of how many items in the console_list i need to traverse lol)

        temp_count = 0

        while temp_count < len(temp_list):
            temp_str += console_list[clist_count] + " " # just add the console_list values to the string
            clist_count += 1
            temp_count += 1

        labelName.config(text=temp_str) # update the label's text

        count += 1

    scoreLabel.config(text="score: " + str(metrics.score)) # update the score
    errorsLabel.config(text="errors: " + str(metrics.errors)) # update the errors

'''
🏳️ CHECK_IF_WINNING:

- WHAT it does: checks whether the game has been won or lost
- HOW it does it: goes through console list to find _s -> if none, win -> but if 5 errors, lose -> shows a message accordingly
- arguments: console_list (list that's client facing [includes underscores, etc.]) | return values: none, but 

'''
def check_if_winning(console_list):
    global winning # need all of this from the outside world (outside of this function)
    global win_statement 
    global lose_statement

    underscore_detected = False 

    for i in console_list:
        if "_" in i:
            underscore_detected = True # basically haven't won

    if not underscore_detected: # bc answered everything, win
        winning = True

    if winning or metrics.errors == 5:
        myButton.config(state=DISABLED) # turns off the ability to press the button (won't run guessing/print_to_tkinter)

        if winning:
            winLoseLabel.config(text=win_statement, fg="#50C878")
        else: # if too many errors
            winLoseLabel.config(text=lose_statement, fg="#FF033E")

'''
🏳️ GUESSING:

- WHAT it does: takes a guess from the entry box and checks whether its in any of the search results, awards points/error points accordingly
- HOW it does it: traverses mlist -> checks if in that search result -> adds to score if not alr answered -> if not in any of mlist then add to errors -> calls print_to_tkinter and check_if_winning to update window accordingly
- arguments: guess (from the myEntry box), mlist (list of all of the search results), console_list (list that's client facing [includes underscores, etc.]) | return values: none, but updates console_list (via global variable c)

'''
def guessing(guess, mlist, console_list):
    global c # need this bc button commands don't return values :(
    hit = False # to check whether the guess didn't have a singular hit
    clist_count = 0

    for i in range(0,len(mlist)): # traversing through mlist bc will need to use mlist for the temp_list and word detection

        temp_list = mlist[i].split() # for easier traversal!

        if guess.lower() in mlist[i]: # it's a hit (correct guess)
            hit = True
            
            for n in range(0,len(temp_list)): # use a split() and an extra list to find specifically where it is (if there's multiple words in that query)

                if guess.lower() in temp_list[n] and console_list[clist_count] != guess.lower(): # if it's a hit and this hasn't alr been answered ... (console_list still has a blank there and not the actual word)
                    console_list[clist_count] = guess.lower()

                    metrics.score += 1 # adding to score

                else:
                    console_list[clist_count] = temp_list[n] # fill in the rest of the search result but do not reward points !!

                clist_count += 1 # keeps updating so can access console list properly

        else: # it's a miss
            clist_count += len(temp_list) # update count accordingly

    if not hit: # guess was completely wrong
        metrics.errors += 1

    c = console_list # updates console list!

    print_to_tkinter(mlist,console_list)
    check_if_winning(c)

# def main():
winning = False # for check_if_winning
print_to_tkinter(m,c) # setting up the labels/etc.!

root.mainloop()
