# The aetherglyphs dictionary!!! It's in the A-Z order. None of this is case sensitive.
#It's set up like [letter, line 1, line 2, line 3, line 4, line 5 ]
aetherDictionary = [
    ["a","------","-■■---","-■-■--","--■■--","------"],
    ["b","-■■--","---■-","■■---","---■-","-■■--"],
    ["c","--■■■--","-■---■-","---■---","-■-■-■-","---■---"],
    ["d","-■■---","--■-■-","--■-■-","--■-■-","-■■---"],
    ["e","-----","■■---","■-■-■","-■■--","-----"],
    ["f","--■■-","-----","■-■■■","-----","-■---"],
    ["g","---■■----","---■-■---","-■-■■■-■-","---■-■---","----■■---",],
    ["h","------","■■-■■-","■-■-■-","-■-■--","------"],
    ["i","-■■---","-■-■--","---■■-","------","--■---"],
    ["j","-■■--","---■-","---■-","---■-","-■---"],
    ["k","--■■---","-■-■---","-■■-■■-","---■-■-","---■■--"],
    ["l","---------","---■-■---","-■-■■■-■-","----■----","---------",],
    ["m","---■---","-■---■-","---■---","--■-■--","---■---"],
    ["n","--■■■--","-■---■-","-■-■-■-","-■--■--","-■-----"],
    ["o","-------","---■■--","-■-■-■-","---■■--","-------"],
    ["p","-■----","-■-■--","-■-■--","-■-■--","---■--"],
    ["q","-■-----","--■■■--","--■-■--","--■■■--","-----■-"],
    ["r","---■---","--■-■--","-------","-■■-■■-","---■---"],
    ["s","-------","-■--■--","--■--■-","-■--■--","-------"],
    ["t","---■---","---■---","-■-■-■-","---■---","---■---"],
    ["u","--■--","-----","-■■--","-■-■-","--■■-"],
    ["v","--■--","-----","-■■--","-■-■-","--■■-"],
    ["w","---■----","--■■-■--","-■--■■■-","--■■-■--","---■----"],
    ["x","-------","-------","-------","-------","-------"],
    ["y","--■■---","-■-----","-■-■-■-","-----■-","---■■--"],
    ["z","-------","--■--■-","-■--■--","--■--■-","-------"],
    [" ","--","--","--","--","--"], 
    ]

print("--== AETHERGLYPHS TO SOUNDODGER 2 ==--")
#python is case sensitive :(
text = str(input("Please enter the aetherglyphs to be turned into text!!!")).lower()
#AetherOutput variable stores the final output. We start with line height and cspace
lHeight = int(input("Please enter the size of the text!"))
aetherOutput = f'<size={lHeight}><line-height={lHeight*1.7}><cspace=-0.15em>'
for row in range (1,6):
    for i in text:
        active = True
        while active == True:
            for j in range(0,len(aetherDictionary)+1):
                if aetherDictionary[j][0] == i: #If the letter matches the letter
                    letter = aetherDictionary[j] # Set the letter to the letter
                    active = False
                    break
                else:
                    continue #Keep checking :/
        glyphLayer = letter[row].replace("-","<alpha=#00>■<alpha=#ff>")
        aetherOutput = "".join([aetherOutput,glyphLayer])
    aetherOutput = "".join([aetherOutput," <br>"])
print("--- All done! :) ---")
print(aetherOutput)
    