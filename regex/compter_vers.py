import re
import sys

# le nom du fichier à analyser et passé en paramètre du programme
filename = sys.argv[1]
div_type =  sys.argv[2]

# lecture du fichier
with open(filename) as f:
    lines = f.readlines()
# on recompose le texte en une seule variable
txt = "".join(lines)

# on récupére le contenu de la balise <div>
contenu_div = re.findall("(?<=%s\">\n)((?:.|\n)*?)<\/div>" % div_type, txt)

# on récupère les vers
if len(contenu_div) > 0:
    vers = re.findall("<l>(.*)</l>", contenu_div[0])
    # afficher le nombre de vers
    print(filename, len(vers))

    # on écrit le contenu des vers dans un second fichier
    with open(filename + ".%s.txt" % div_type, 'w') as fo:
        fo.writelines("\n".join(vers))
