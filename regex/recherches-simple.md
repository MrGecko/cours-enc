
** La recherche textuelle **

# Que cherche-t-on ?

Qu'est-ce qu'une recherche textuelle ?
Nous recherchons implicitement des mots que nous souhaitons retrouver ou des morceaux de mots, comme des suffixes ou des terminaisons que nous savons incorrectes. C'est grâce à notre connaissance de la langue française et de sa grammaire que nous sommes capables de distinguer ce qui est fait parti de l'ensemble des mots et ce qui n'est que ponctuation.

Implicitement, nous comprenons que ces suites de caractères séparés par des espaces forment des ensembles indépendants et ont une signification propre.
Nous avons connaissance du concept de phrase séparés par des signes de ponctuation, là où, par défaut, la machine ne voit qu'une très longue succession de caractères variés.

Votre éditeur de texte est capable d'ouvrir des textes en anglais, en français ou dans n'importe quelle langue tant que son concepteur lui a permis de représenter à l'écran les différentes lettres ou idéogrammes.
Mais l'éditeur de texte ne connait pas le concept de grammaire pour autant (nous ne parlons pas ici du cas des correcteurs) : il ne fait qu'afficher cette suite continue de caractères contenus dans le fichier.

Demander à la machine de rechercher du texte revient alors à lui demander de chercher **caractère par caractère** si deux mots ou deux terminaisons sont constitués des mêmes éléments.
Vous lui demandez de chercher un mot ? Il va tout de même regarder parmis les espaces et les signes de ponctuation, parce que tant qu'il n'a pas testé, il ne peut pas savoir.
Là où notre oeil ne semble ne pas s'arrêter, la machine appliquera assidûment son algorithme, sans à priori.

# Le concept de classification

La plupart des problèmes que nous souhaitons voir automatiser par une machine sont des problèmes de **classification**. Comprenez par le concept classe l'ensemble comprenant les résultats correspondant à ce que l'on cherche et ceux qui ne correspondent pas.
Les résultats correspondant formant un ensemble et le reste des résultats en formant un autre. Ces deux ensembles, disjoints, sont représentés dans le cas d'une recherche textuelle par des mots surlignés de couleur vive mais aussi par le reste du texte, c'est-à-dire l'ensemble ordonné des caractères qui ne répondent pas au critère de recherche.  
En cherchant un mot dans un texte, vous n'avez pas seulement trouvé la suite de caractères correspondant à ce mot, vous avez trouvé l'ensemble des suites de caractères correspondant à ce mot (il peut en effet être présent plusieurs fois dans le texte !) mais aussi l'ensemble des caractères ne correspondant pas à ce que vous cherchiez.
Il s'agit-là d'une opération de classification : chaque élément (dans notre cas des suites de caractère) de l'ensemble du texte sera classé soit d'un côté soit de l'autre.

Utiliser des expressions régulières demande de bien saisir la notion d'ensemble de résultats : ceux qui répondent à votre question d'une part et ceux qui à priori ne vous sont d'aucun intérêt.

# Les classes de caractères

Nous savons aisemment découper l'ensemble des signes composant nos langues modernes. Nous donnons le nom de ponctuation à une liste finie de caractères,
le noms de lettres à un autre ensemble. Il existe également l'ensemble des chiffres, à ne pas confondre avec l'ensemble des nombres, tout comme l'ensemble des majuscules ne peut être confondu avec celui des lettres minuscules.
Cela est encore plus vrai lorsque l'on doit représenter le sujet de sa recherche de manière numérique : les caractères diffèrent entre un "a" et un "A" et ont bien deux emplacemnts distincts dans les tables de codage des caractères.

Les expressions régulières permettent de définir des ensembles de caractères (appelés classes de caractères) personnalisables : vous pouvez créer un ensemble comportant un caractère de votre choix, deux caractères, mélanger de la ponctuation, ajouter un arobase ou des chiffres.

Les éléments d'une classe de caractères sont notés entre crochets [ ].
L'ordre des éléments dans une classe de caractères n'a pas d'importance

Exemples :
la lettre a minuscule : ```[a]```
les lettres minuscles : ```[abcdefghijklmnopqrstuvwxyz]``` ou bien ```[a-z]```
les chiffres : ```[0213465987]``` ou bien ```[0-9]```
Les caractères a,b,d,1,2,3 : ```[a1b23d]```
L'ensemble des lettres minuscules et majuscules : ```[a-zA-Z]```
Un certain ensemble de caractères de ponctuation : ```[,;!]```

Il existe un certain nombres de raccourcis qui n'utilisent pas de crochets pour des classes usuelles :
* ```\d``` : les chiffres
* ```\D``` : l'ensemble des caractères qui ne sont pas dans \d
* ```\w``` : l'ensemble des caractères que l'ont peut trouver dans un mot (équivaut à * ```[a-zA-Z0-9_]```)
* ```\W``` : l'ensemble des caractères qui ne sont pas dans \w
* ```\s``` : l'ensemble des caractères qui représentent des espaces (espace, tabulation, retour à la ligne, retour chariot, tabulation verticale...)
* ```\S``` : le complémentaire de \s

---
**Exercice 1**

https://regex101.com/

Déterminer les classes de caractères couvrant entièrement les cas suivants :
1. > Bonjour !
2. > Cé tro bi1 comme exercice

Déterminer la classe de caractères pour qui correspond à tous les nombres (romains ou non) suivant, mais pas au reste de l'expression :
3. > XIIIème siècle
4. > Du XIVème (14ème) au XIXème (19ème) siècle

---

# Le concept de motif

Si rechercher un mot avec l'outil de recherche classique est une tâche courante et semble-t-il maîtrisée pour l'utilisateur occasionnel d'un traitement de texte, il faut tout de même noter que des faux-positifs sont bien souvents surlignés et mis sur le même pied d'égalité avec le reste des résultats.

**Exercice 2**

https://goo.gl/srx4wT

> Robert est venu au château par chariot. Nous avons apporté son chat et Robert est venu ensuite avec ses achats de la semaine.

1. Quel est le résultat d'une recherche sur le mot chat avec un éditeur de texte ?
2. À la lecture comment arrivez-vous à la conclusion que seul le premier résultat est pertinent ? Qu'est-ce qui le sépare du second résultat ?

Pour chercher la suite de caractères ```chat``` en avec une expression régulière, on écrit tout simplement la regex ```chat```, sans crochets. Il s'agit de la forme la plus simple pour une expression régulière.

3. Que se passe-t-il si on cherche avec la regex ```[chat]``` ?

Pour exprimer la notion de mot telle que nous la connaissons, nous pouvons par exemple décider que *chat* est un mot à partir du moment où il est précédé et suivi d'un espace :
``` \schat\s ```

4. Que se passerait-t-il dans le cas où le mot chat apparaîtrait en fin de phrase, donc suivi d'un point ?

Nous avons formé ici un motif d'expression régulière qui peut sémantiquement être découpé en plusieurs parties : l'espace de début, les caractères du mot chat, l'espace de fin.
5. De combien de caractères est composé le motif (attention au piège) ?

Les motifs permettent de spécifier *caractère par caractère* le sujet de notre recherche.
Ils sont la plupart du temps accompagnés de métacaractères servant à exprimer une quantification, une construction de groupes ou des ancres permettant de sélectionner plus finement les expressions recherchées.

## Les quantificateurs

Intéressons-nous à la recherche de la lettre **m** doublée dans un texte.
L'expression régulière ```m``` permet certes de repérer toutes les lettres **m** au sein d'un texte, mais elle ne fait pas la distinction entre les **m** isolés et les **m** doublés.
En effet, si une classe de caractère peut contenir plusieurs éléments, écrire ```[a-z]``` ne cherchera que les **suites composées d'une seule lettre minuscule**.

Autrement dit, appliquer l'expression régulière ```m``` au texte **J'ai été surpris par son attitude, et notamment par son cynisme.** fera ressortir les deux **m** de **notamment** comme deux résultats distincts.

Il est évidemment possible d'utiliser l'expression ```mm``` pour trouver deux **m** accolés. Mais qu'en est-il du cas où le caractère que l'on recherche n'est pas connu par avance ?

Par exemple, comment rechercher toutes les dates ?

Il est possible d'écrire ```[0-9][0-9][0-9][0-9]``` mais ce n'est pas très pratique, surtout au sein d'expressions régulières imposantes.
Il est alors possible d'écrire ```[0-9]{4}``` où **{4}** ne fera pas parti du motif recherché : il s'agit d'un quantificateur signifiant **le caractère (ou un parmi la classe s'il s'agit d'une classe) précédent répété quatre fois**

Écrire ```[0-9]{4}``` permet donc de mettre en valeur touts les chaînes de caractères comprenant une suite de quatre caractères compris entre 0 et 9.
*Ex:* 0000, 1234, 2018, 9900, 9999

Autres exemples :
* En fournissant deux bornes on peut trouver les nombre composés de deux à quatre caractères ```[0-9]{2,4}```
* En fournissant seulement la première borne on peut trouver les nombres composés d'au minimum trois caractères ```[0-9]{3,}```.

Les quantifieurs les plus utilisés sont les suivants :
* L'étoile ```*``` (aussi appelée joker ou wildcard) permet de répéter **zéro ou plus** le motif précédent :
```[A-Z]{4}[0-9]*``` permet de sélectionner les expressions composées de quatre lettres majuscules suivies ou non d'un seul chiffre
* Le point d'interrogation ```?``` permet de répéter **zéro ou une fois** le motif précédent :
```<\/?b>``` permet de sélectionner à la fois les balises <b> et les balises </b>
* Le signe plus ```+``` permet de répéter **une fois ou plus** le motif précédent :
```[A-Z][a-z]+``` permet de sélectionner une expression composée d'une lettre majuscule suivie d'au moins une lettre minuscule

**Exercice 3**

https://goo.gl/yDjnak

>Les églises du 13ème et du 14ème siècles ont été le plus lourdement impactées par le séisme de la nuit dernière. Ce n'est qu'au 15ème siècle que la composition du mortier s'est significativement améliorée, grâce à l'adjonction de ... et de ... en proportion d'un cinquième. Paris 2012, 13 Rue du Souffle. Édition Dunod @AEF20120901BCG.

1. Sélectionner grâce à une regex les références à des siècles (en gardant -ème)
2. Sachant que le numéro d'édition commence toujours par @ suivi de trois lettres majuscules puis d'une date au format annéeemoisjour, comment récupérer le numéro d'édition du texte précédent ? Ne pas se soucier d'avoir une date cohérente.

3. Sélectionner tous les mots commençant par une majuscules

## Les ancres de début et de fin de ligne

* ```^Elles``` permet de sélectionner les mots **Elles** uniquement s'ils se trouvent en début de ligne
* ```Monsieur !$``` permet de sélectionner les expressions **Monsieurs !** uniquement s'ils se trouvent en début de ligne
* ```^Monsieur !$``` permet de sélectionner les expressions **Monsieurs !** uniquement s'ils se trouvent à la fois en début de ligne et en fin de ligne, **c'est-à-dire les lignes ne comportant que le texte Monsieur !**


## Les groupes de motifs

Les motifs peuvent être groupés au sein d'une même expression régulière en utilisant des parenthèses :
1.  ```Édition ([A-Z][a-z]+)``` permet ainsi de définir un groupe sélectionnant le nom de chaque édition présente dans le texte.
2. ```(Édition) ([A-Z][a-z]+)``` permet de définir deux groupes sélectionnant :
 * Le terme **Édition** lorsqu'il est suivi d'un nom d'édition et ce pour chaque édition
 * Le nom de l'édition seule pour chaque édition

** Exercice 4 **
1. Écrire l'expression régulière permettant de sélectionner dans deux groupes distincts 1) le nom d'une maison d'édition 2) le numéro de l'édition.

### La répétition de groupes
### Les sous-groupes

# La substitution
