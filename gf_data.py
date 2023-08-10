from pytrends.request import TrendReq
from gf_metrics import *

'''
🏳️ CLEAN_DATA:

- WHAT it does: uses PyTrends data for related queries for the given keyword and converts into dictionary
- HOW it does it: PyTrends data in temp_dict -> cleans up dictionary -> transfers into list to split via " " -> cleans up list -> place values into new dict by ranking
- arguments: none | return values: top_dict (dictionary containing top queries from PyTrends results)

'''
def clean_data(): 
    pytrend = TrendReq(hl='en-US')

    kw0 = metrics.keyword # the key word for the search
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    kw_list = pytrend.build_payload(kw_list=[kw0])
    temp_dict = pytrend.related_queries()

    # has the strangest format -> i.e. {Stray Kids: {top: query value ..., rising:...}} -> need to clean it up
    del temp_dict[kw0]["rising"] # keeps only top entries, deletes rising ones

    # convert value into string
    temp_str = str(temp_dict[kw0]["top"])

    # space splicing into list
    temp_list = temp_str.split()

    # delete "query" and "value" (more weird pytrends formatting)
    for i in range(0,2):
        del temp_list[0]

    # then make a new dictionary
    top_dict = {}
    key = True
    value = False
    dict_key = ""
    dict_str = ""

    for i in range(0,len(temp_list)):
        if temp_list[i][0] in alphabet: # double checking if it's the search results!
            key = False
            value = True

        if key and not value: # the rankings! (it's a key, i.e. 0, 1, etc...)
            dict_key = temp_list[i]
            top_dict[temp_list[i]] = ""
            key = False
            value = True
        elif value and not key: # the kw/search results! suggestions
            dict_str += temp_list[i] + " "

            # then marking it so u know to ignore the 0-100 scores google gives
            value = False
            key = False
        else: # ignore the 0-100 scores google gives
            top_dict[dict_key] = dict_str
            dict_str = ""
            key = True

    return top_dict

'''
🏳️ MLIST_SET_UP:

- WHAT it does: takes the dictionary and sets up a "masterlist" to keep all of the search results
- HOW it does it: traverses through dict -> double checks it's in english -> otherwise appends it to the masterlist
- arguments: dictionary (top_dict) | return values: mlist (list of all of the search results)

'''
def mlist_set_up(dictionary):

    mlist = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'] # to verify everything's in eng

    # turning the dictionary into a list for easier access/manipulation (random access hehe)
    for i in dictionary:
        mlist.append(dictionary[i])

        # bc the hl (home language) function of pytrends doesn't seem to work 100% of the time
        notEng = True
        count = 0

        while notEng and count < len(alphabet):
            if alphabet[count] in dictionary[i]:
                notEng = False
            else:
                count += 1

        if notEng:
            mlist.pop() # bye bye sorry foreign language search result :)
    
    mlist.pop() # making sure further items don't go out of range elsewhere 

    return mlist


'''
🏳️ CONSOLE_LIST_SET_UP:

- WHAT it does: takes the mlist and makes a client-facing version (underscores, etc.) that's also easier to manipulate (each word individually)
- HOW it does it: traverses through mlist -> adds each word of a search result into console_list -> replaces the non-keywords with _s
- arguments: mlist (list of all of the search results) | return values: console_list (list that's client facing [includes underscores, etc.])

'''
def console_list_set_up(mlist):    
    console_list = []

    # loading search result words into console_list
    for i in range(0,len(mlist)):
        temp_list = mlist[i].split() # splits entire search result into individual words

        for item in temp_list:
            console_list.append(item.strip()) # adds to console list, also strips bc PyTrends has formatting issues (...)

    # editing the console_list so that the keyword -> ____
    for i in range(0,len(console_list)):
        if metrics.keyword.lower() != console_list[i]: # not the keyword
            console_list[i] = "_" * len(console_list[i]) # replaces it w underscores

    return console_list