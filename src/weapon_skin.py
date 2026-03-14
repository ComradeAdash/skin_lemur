# A simple weapon class to take in user queries through discord commands
# we define how to parse through inputs here and return the json response into something
# the discord bot can display

# Issues - skins that dont exist such as AWP asiimov fn (they only come in ft) create a mismatch

import re
import steam_skins
from rapidfuzz import process, fuzz # rapid fuzz helps process user queries

class Weapon_skin:

    def __init__(self):
        self.wear_map =  {
            "ft": "(Field Tested)",
            "mw": "(Minimal Wear)",
            "fn": "(Factory New)",
            "bs": "(Battle Scarred)",
            "ww": "(Well Worn)"
            }

        self.skin_array = steam_skins.get_all_skin_names(steam_skins.skin_names_url)
        self.norm_skin_array = [self.normalize(skin) for skin in self.skin_array]

    def normalize(self,input):
        for abbr, full in self.wear_map.items():
            input = re.sub(rf"\b{abbr}\b", full, input)
        input = input.lower()
        input = re.sub(r"[^a-z0-9\s]", "", input)
        input = re.sub(r"\s+", " ", input).strip()

        return input

    # taking in a user input query, normalizing it, and checking for the skin
    # returns the matched skin name from the CS2 item json data

    #intended input ex) "ak47 redline fn"
    def search_skin(self,user_query):
        best_match = None
        best_score = 0
    
        # parse the input down
        norm_input = self.normalize(user_query)
        print(norm_input)

        for i,skin in enumerate(self.norm_skin_array):
             score = fuzz.token_sort_ratio(norm_input, skin)
             
             if score > best_score:
                best_score = score
                best_match = self.skin_array[i]

        return best_match

# skin = Weapon_skin()
# print(skin.search_skin("awp gungnir fn"))