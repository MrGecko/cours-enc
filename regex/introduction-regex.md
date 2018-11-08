
# Introduction

Imaginez le scénario suivant : on vous a donné la tâche de vérifier la qualité
d'une collection de textes, mettons les thèses de l'école des dix dernières
années au format numérique, dans le but de les publier sur un site dédié.
Vous remarquez rapidement que malgré l'utilisation de correcteurs ortographiques
il reste bon nombre d'erreurs et de coquilles au sein des textes. Celle qui vous
semble revenir le plus souvent est le cas des "mots doublés" comme "ceci ceci".

Il est vrai que le processus d'écriture de tels travaux nécessite beaucoup de corrections,
de réecritures et de reformulations entrainant quasi inévitablement ce genre d'erreur.

Dans notre scénario, vous avez la chance de récupérer les sources de thèses
au format TEI. Votre mission, si vous l'acceptez, est de créer une solution qui :
* accepte n'importe quel nombre de fichier en entrée, détecte chaque ligne dans chaque fichier où se trouve un mot doublé et affiche le nom du fichier en regard de la ligne fautive.
* détecte même les cas où deux mots doublés sont séparés par un retour à la ligne
* détecte même les cas où la casse des deux mots diffère (exemple en début de ligne: "Votre votre")
* détecte les cas où les mots sont séparés par des balises: "<em>très</em> très important"


C'est un exercice à priori fastidieux qui vous demanderait de nombreuses heures de relecture !
Il s'agit nénamoins de cas problématiques qui doivent bien être résolus avant la publication
des textes.

Les expressions régulières, ou regex (regular expressions), sont un outils puissant et flexible
vous permettant de maîtriser le contenu de vos données textuelles grâce à des capacités
de groupement, de suppression, d'ajout et de remplacement de motifs.

Une expression régulière peut être aussi simple qu'une recherche de mot dans votre éditeur de texte préféré
mais aussi puissante que les fonctionnalités offertes par un outils expert dans l'analyse textuelle.

# Au quotidien

S'il y a peu de chance que l'on vous demande de publier les thèses de l'école, il reste, au quotidien, de nombreux cas de bien moindre envergure
où les expressions régulières excellent et permettent de ne pas avoir à parcourir des milliers de lignes de texte manuellement.
Imaginez plutôt : vous arrivez à la fin de la rédaction de votre mémoire en TEI (au bas mot 500 pages) et ce n'est qu'à ce moment-là que vous réalisez
votre erreur quant à l'utilisation de balises <b> pour mettre en valeur des dates dans votre texte.
Vous étiez bien au courant qu'il ne s'agissait pas de la balise la plus adéquate mais vous avez laissé de côté le problème jusqu'au dernier moment.
Désormais, vous aimeriez bien remplacer ces balises par des balises <date>.

Hélas vous vous rendez bien vite compte qu'il vous est impossible d'utiliser la recherche textuelle de votre éditeur de texte :
et pour cause, de nombreux autres segments de votre textes sont entourés de balises <b> et ce de manière tout à fait légitime car ils respectent
la sémantique de <b> et n'ont rien à voir avec les dates incriminées.
Autant de faux positifs qui vous rendent la tâche de correction aussi peu excitante que laborieuse !

L'expression régulière que vous pouvez utiliser pour vous sortir de ce guêpier est la suivante (https://regex101.com/r/TC6GEB/1) :
```
s/<b>([0-9]{4})<\/b>/<date>$1</date>/gmi
```

Ce n'est pas la complexité d'une tâche qui la rend fastidieuse, c'est bien souvent la répétitivé induite par la taille du corpus à traiter mais aussi la présence de cas particuliers que l'on ne s'attendait pas à trouver.

Les expressions régulières forment un langage en soi. Nous verrons par la suite sa grammaire et comment fonctionne sa syntaxe puis nous apprendrons comment lire une expression, avant de nous atteler à notre tour à en composer.

---
noms de fichier, des globs/wildcard
---
Les regex ne sont pleinement exploitables que lorsqu'elles sont utilisées conjointement à des langages de programmation ou des outils spécialisés.
Aussi, ce ne sont pas les expressions régulières qui s'occuperont de parcourir les dossiers sur vos disques durs puis d'ouvrir les fichiers un par un.
Ce n'est pas leur rôle. Les expressions régulières s'attachent à traiter du texte et ne s'occupent que de cela.

Nous verrons par la suite comment les utiliser au sein d'outils comme Oxygen, Python mais aussi directement dans un terminal.

Enfin, le but de ce cours n'est pas de vous donner clef en main toute une suite d'expressions régulières mais de vous initier à l'esprit de rédaction et de lecture de ces dernières.
