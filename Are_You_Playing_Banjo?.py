#Are You Playing Banjo?

#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!
#The function takes a name as its only argument, and returns one of the following strings:
#name + " plays banjo" 
#name + " does not play banjo"
#Names given are always valid strings.

def areYouPlayingBanjo(name):
    if "R" in name[0:1] or "r" in name[0:1]:
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
