import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

files = os.listdir(os.path.join(dir_path, "raw_txt"))
del files[40] # supprimer l'élément marqueur des raccourcis tex

# total
lines = 0
words = 0
characters = 0
equation = 0

for file in files:
    with open(os.path.join(dir_path, "raw_txt", file)) as infile:
        
        for line in infile:
            wordslist = line.split()
            lines= lines + 1
            words = words + len(wordslist)
            characters += sum(len(word) for word in wordslist)
            equation += line.count("\[")
            equation += line.count("&")
            equation += line.count("$") / 2 # calcul un peu faussé car des fois y'a des $$ $$ et non de simples $ $, mais on veut juste une estimation
            equation += line.count("\\begin\{equation\}")
        
        # oops if len(infile) == 1: equation += 1 si une seule ligne, pas compté mais on sait qu'il n'y en a qu'une quinzaine
print(lines)
print(words)
print(characters)
print(equation)