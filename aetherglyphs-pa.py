# The aetherglyphs dictionary!!! It's in the A-Z order. None of this is case sensitive.
#It's set up like [letter, line 1, line 2, line 3, line 4, line 5 ]
aetherDictionary = {
    "a": ["------","-■■---","-■-■--","--■■--","------"],
    "b": ["-■■--", "---■-","■■---","---■-","-■■--"],
    "c": ["--■■■--","-■---■-","---■---","-■-■-■-","---■---"],
    "d": ["-■■---","--■-■-","--■-■-","--■-■-","-■■---"],
    "e": ["-----","■■---","■-■-■","-■■--","-----"],
    "f": ["--■■-","-----","■-■■■","-----","-■---"],
    "g": ["---■■----","---■-■---","-■-----■-","---■-■---","----■■---",],
    "h": ["------","■■-■■-","■-■-■-","-■-■--","------"],
    "i": ["-■■---","-■-■--","---■■-","------","--■---"],
    "j": ["-■■--","---■-","---■-","---■-","-■---"],
    "k": ["--■■---","-■-■---","-■■-■■-","---■-■-","---■■--"],
    "l": ["---------","---■-■---","-■-■■■-■-","----■----","---------",],
    "m": ["---■---","-■---■-","---■---","--■-■--","---■---"],
    "n": ["--■■■--","-■---■-","-■-■-■-","-■--■--","-■-----"],
    "o": ["-------","---■■--","-■-■-■-","----■■-","-------"],
    "p": ["-■----","-■-■--","-■-■--","-■-■--","---■--"],
    "q": ["-■-----","--■■■--","--■-■--","--■■■--","-----■-"],
    "r": ["---■---","--■-■--","-------","-■■-■■-","---■---"],
    "s": ["-------","-■--■--","--■--■-","-■--■--","-------"],
    "t": ["---■---","---■---","-■-■-■-","---■---","---■---"],
    "u": ["--■--","-----","-■■--","-■-■-","--■■-"],
    "v": ["--■--","-----","-■■--","-■-■-","--■■-"],
    "w": ["---■----","--■■-■--","-■--■■■-","--■■-■--","---■----"],
    "x": ["---■---","-■---■-","--■-■--","-■---■-","---■---"],
    "y": ["--■■---","-■-----","-■-■-■-","-----■-","---■■--"],
    "z": ["-------","--■--■-","-■--■--","--■--■-","-------"],
    " ": ["--","--","--","--","--"]
}

print("--== AETHERGLYPHS TO PROJECT ARRHYTHMIA ==--")
#python is case sensitive :(
text = str(input("Please enter the aetherglyphs to be turned into text!!!")).lower()
#AetherOutput variable stores the final output. We start with line height and cspace
# <size=10><line-height=4><cspace=-0.25em>
aetherOutput = '<size=10><line-height=4><cspace=-0.25em>'

for row in range (1,6):
    for i in text:
        glyphLayer = aetherDictionary[i][row].replace("-","<alpha=#00>■<alpha=#ff>")
        aetherOutput = "".join([aetherOutput,glyphLayer])
    aetherOutput = "".join([aetherOutput," <br>"])
print("--- All done! :) ---")
print(aetherOutput)
    
