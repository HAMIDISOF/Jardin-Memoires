# Convergences_Choquet

*Converti depuis PDF par pdf_to_md.py*

---


## Page 1

ANNALES DE L’UNIVERSITÉ DE GRENOBLE
G. CHOQUET
Convergences
Annales de l’université de Grenoble, tome 23 (1947-1948), p. 57-112
<http://www.numdam.org/item?id=AUG_1947-1948__23__57_0>
© Annales de l’université de Grenoble, 1947-1948, tous droits réservés.
L’accès aux archives de la revue « Annales de l’université de Grenoble »
implique l’accord avec les conditions générales d’utilisation (http://www.
numdam.org/conditions). Toute utilisation commerciale ou impression sys-
tématique est constitutive d’une infraction pénale. Toute copie ou impression
de ce ﬁchier doit contenir la présente mention de copyright.
Article numérisé dans le cadre du programme
Numérisation de documents anciens mathématiques
http://www.numdam.org/


## Page 2

CONVERGENCES
par G. CHOQUET (Grenoble).
INTRODUCTION
Le but de ce travail est l’étude des relations multivoques entre
deux espaces topologiques.
Nous avons, dans une première partie, porté notre attention sur
les relations semi-continues inférieurement ou supérieurement, et
en particulier sur les relations d’équivalence semi-continues dans un
espace topologique.
Nous avons dû pour cela étudier d’abord de façon précise les
notions d’ensembles limite supérieure et limite inférieure d’une
famille d’ensembles : la notion de filtre C) s’est avérée pour cela
l’outil naturel et indispensable.
Cette étude nous a conduit naturellement à définir une notion
de convergence sur l’ensemble des sous-ensembles fermés d’un
espace topologique. Cette notion de convergence 
- ou plutôt de
« pseudo-convergence », - plus large que la notion de convergence
topologique, semble s’introduire toutes les fois que l’on étudie des
familles d’ensembles fermés ou d’applications définies sur des espaces
topologiques : En particulier, la « pseudo-topologie » de l’espace
des sous-ensembles fermés d’un espace de Hausdorff n’est une topo-
logie que lorsque cet espace est localement compact.
Nous terminons ce mémoire par l’étude des rapports entre la conver-
gence et la convergence uniforme locale, ou plus précisément entre les
contingents et paratingents abstraits. Les théorèmes d’énoncé très
(1) Voir H. Cartan, Comptes Rendus. zo5, 1937, pp. 595 et ~7 ; et Bourhaki, Topo-
logie générale, ch. I (Act. Sc. et Ind, Hermann, tio 858).


## Page 3

58
simple auxquels nous aboutissons (~) sont la généralisation et la géomé-
trisation des résultats de Baire et des théorèmes mis par M. Denjoy à
la base de la théorie topologique des fonctions de variable réelle.
Nous indiquons diverses applications géométriques de ces théorèmes,
mais l’0153uvre de M. Denjoy C) reste la meilleure illustration de la
puissance de ces méthodes.
(2) Nous avions énoncé sans démonstration l’un de ces théorèmes dans notre thèse :
Choquet, Application des propriétés descriptives de la fonction contingent, J. Je Math.
pures et app., Paris, 1947.
(3) Voir en particulier Denjoy I.


## Page 4

PREMIÈRE PARTIE
1. _ Relation entre deux ensembles.
Une relation multivoque R entre les éléments de deux ensembles
X, Y est définie par la donnée d’un sous-ensemble  de l’ensemble
produit X > Y.
Si x EX et y E Y, on dira que R(x, y) si (x, y)E.
Pour tout x EX, on désigne par ~(a?) l’ensemble des éléments y
de Y tels que (x, ;/)6~ ; plus généralement, pour tout ensemble A cY,
on posera ~(A) = U ~1~,(x).
xEA
On note par x 
l’ensemble des éléments (x, y) de X X Y, et par [A]
l’ensemble U [x],
xEA
On définira de façon analogue ~(y) et ~(B), [y] et [ B] pour y E Y
et BcY.
Pour tout A c X, on appelle « saturé de A )), l’ensemble
S(A) ~ ~(~(A)~ .
En général S~S(A)) ~ S(A). 
’%
On appelle relation complémentaire de R la relation R définie
par l’ensemble (X > Y - ).
Pour deux relations Ri, R~ définies respectivement par ~~1 et ~;2, on
dit que Ri e R2 si ~~ c ~~ (ceci se lit Ri moins large ou plus fine
que R2).
Pour une famille (Ri)ïEI de relations définies par les ensembles
(ï)iEI’ on appelle relation réunion de la famille (resp. intersection),
la relation définie par 
resp. 
1 
B 
tel 7


## Page 5

60
2. _ Relation dans un ensemble.
Une relation R dans un ensemble E est définie par la donnée d’un
sous-ensemble f de E > E.
Exemples : Les relations d’ordre, les relations d’équivalence.
Si Ri et R~ sont deux relations d’équivalence dans E, définies par
les ensembles 01 et ~~, on dira encore que Ri est moins large (ou plus
fine) que R~ si ~q c ~~z. Ceci équivaut à dire que toute classe d’équi-
valence suivant R2 est une réunion de classes d’équivalence sui-
vant Ri.
L’ensemble des relations d’équivalence dans E est ordonné par
cette relation.
Bornes inférieure et supérieure
d’une famille de relations d’équivalence.
Soit (Ri)iEj une famille de relations d’équivalence dans E.
1) Cette famille possède une borne inférieure R ==: inf. (Ri)LI ainsi
définie :
On dira que R(~1, x~) si RL(x1, x~) pour tout iEI.
Cette borne inférieure est identique à la relation-intersection
des Ri.
2) Cette famille possède une borne supérieure R -- sup. (Ri)EI
ainsi définie :
On dira que R(x1, X2) s’il existe une suite finie d’éléments
xi, a2, ..., , xn+ de E, avec xi = x1 et x2 2- xn + 1.et une suite finie
de relations Ri, R2, ..., Rn de la famille, telles que
Rk(xk, xk+ i) pour 1, 9,, ..., n.
Cette borne supérieure n’est identique à la relation-réunion des Ri
que lorsque cette dernière est une relation d’équivalence.
3. 
- Limite inférieure et limite supérieure
d’une famille d’ensembles suivant un filtre.
Définition: Soit (e)iEi une famille de sous-ensembles d’un espace
topologique E et soit a un filtre sur I.
t) On dit qu’un point x de E est un point-limite supérieure de la


## Page 6

61
famille 
suivant le filtre F si, pour tout voisinage ti de x et tout
élément 
il existe un iEa tel que  n ei ~ 
y~.
L’ensemble de tous les points-limite supérieure est dit l’ensemble-
limite supérieure et se note par sup. (ei) 91 
*
2) On dit qu’un point x de E est un point-limite inférieure de la
famille f(ei)iE1 suivant le filtre a si, pour tout voisinage 
de x, il
existe un élément aE tel que, pour tout iEa, on ait : ‘L~ 
L’ensemble de tous les points-limite inférieure est dit l’ensemble-
limite inférieure et se note par inf. (ei)f
Calcul de sup. ( ei~~ et de inf. (ei ) ~r.
Pour tout sous-ensemble a c l, posons Sa == U ei.
iEa
Désignons, d’autre part, par G la famille des sous-ensembles de 1
qui ne sont pas des complémentaires d’éléments de ~Je.
On a évidemment a cg" et la condition Fir équivaut à dire
que F est un ultrafiltre.
Nous dirons que g, est la grille associée au filtre 51 (‘").
Par exemple, si F désigne le filtre de Fréchet sur l’ensemble N
des entiers, sera la famille des sous-ensembles infinis de N ; si F
désigne, dans un espace topologique I, le filtre des voisinages d’un
point X, G sera la famille des sous-ensembles de 1 auxquels x est
adhérent.
Nous allons établir les formules
Formule ( ~ ). 
- Il suffit de remarquer ceci : Dire que xE sup. (ei)F,
équivaut à dire que 
pour tout 
.
Formule (2). 
- Soit XE inf. 
Pour tout 
et tout 
on a : 
Donc pour tout voisinage ‘L~ de x, on a ‘L n Ea =1= 0.
Autrement dit, pour tout  a on a : 
Inversement, soit 
ea, et soit 
voisinage de x. Soit a l’en-
a
(~) Pour l’étude de cette notion, voir Choquet, Sur les notions de filtre et de grille,
C. R. Aead. Sciences, t. 221~, 1947, pp. i~t-t’~3.


## Page 7

62
semble des i de 1 tels que ln n e~ ~ 
y~. A cause du choix de x, on n’a
pas (1 
- 
a)E(G,. Donc aE J" ; on a donc bien xE inf. (ei)~ 
.
Propriétés de inf. (ei)~ 
ez de sup. (ei),. 
.
a) Les formules (t) et (2) montrent que inf. (e;)~ et sup. (ei)F sont
des ensembles fermés.
D’autre part, comme 
on a: inf. 
c sup. 
.
Notons aussi que la relation 
ei) - 
entraine que
~ tEa 
B iEa 
/ 
iEa 
/
b) Si 5’ est un filtre plus fin que ~, on a :
d’où
c) Pour tout ultrafiltre ~r, on a 
d’où inf. 
.
Or pour tout filtre sur 1 il existe un ultrafiltre plus fin que lui. On
obtient donc la généralisation suivante d’un théorème classique :
Pour toute famille (ei),, ,1 de sous-ensembles de E, et pour tout filtre
5 sur I, il existe un filtre ~’ plus, fin que 5i et tel que: 
:
Notons ici que, si pour un filtre f’ sur I, on a inf. (ei) ~, 
== sup. 
la même égalité subsiste pour tout filtre 
plus fin que ~‘. Ceci
résulte des inclusions obtenues ci-dessus (en (6)Y
En général le filtre intersection des filtres ~A plus fins que 5 et tels
que inf. (ei) = sup. 
-- un même ensemble A n’est pas un
filtre ~Â. Mais ceci a lieu lorsque E est localement compact, â cause
des relations que nous allons établir ci-dessous, en (d),
d) Si ( ~p~)2E~ est une famille de filtres sur l, et si ’,î désigne le filtre
intersection : . on a les relations .’


## Page 8

63
et cette inclusion (4) devient une identité lorsque E est localement
compact ou lorsque 4) est finie.
Démonstration. Relation (3): Remarquons que la grille (~ associée
à ~ est la réunion des grilles q, associées aux 
Or une propriété connue de l’opération intersection (~) nous
montre que
ce qui exprime le résultat annoncé.
Relation (4): 7.) Comme ~c~ pour tout 
on a
Comme de plus sup. 
est un ensemble fermé, on a la formule
annoncée.
(3) Si E est localement compact, pour tout x ( sup. (ei)~,,, 
et pour
tout voisinage compact 0[) de x disjoint de sup. 
, il existe un
élément 
tel que 
’
Si, en particulier,
et si 
est un voisinage
compact de x disjoint de
Donc
Si l’on pose a - U 
cette égalité devient 
Or 
Donc le point x n’est pas un point-limite supérieure de la famille
suivant ~F. On a donc bien :
On peut montrer par un exemple que cette identité ne serait pas
vérifiée si dans le second membre on enlevait le signe de fermeture,
même pour E métrique compact.
(~) Voir Bourbaki, Fasc. Res, Act. Sc. Hermann, 846, page a5, formule 41.


## Page 9

64
y) Lorsque (1) est finie, cette identité résulte aisément de ce que
l’intersection d’un nombre fini d’ensembles ouverts est un ensemble
ouvert.
Remarque L’identité (5) peut être fausse lorsque E n’est pas
localement compact. On en construira aisément un exemple dans
l’espace E obtenu comme réunion d’un disque ouvert et d’un
point de sa circonférence.
e) Pour tout filtre sur 1 et pour tout x~ sup. 
il existe des
filtres ~’ plus fins que uf pour lesquels on a 
’
xE inf. (e~)C(~, . 
.
t7
L’intersection de ces filtres est encore un filtre 
tout filtre
plus fin que ~~. est un filtre ~.~’ 
.
Démonstration : : Pour tout voisinage ‘~7 de x, et tout 
désignons
par a~ l’ensemble des indices i tels que
Soit fflx la famille de ces aa-) ; 
est une base de filtre car, d’une part
d’autre part 
=1= o puisque aE sup. 
Soit ~~x le filtre de base 
Il est évidemment plus fin que ié, et
par construction on a : xE inf. 
.
Il résulte de la définition de gîx que c’est le moins fin de tous les
filtres gî’ tels que xE inf. 
d’autre part il résulte des inclusions
de (b) que cette relation a lieu pour tout filtre plus fin que ax.
Remarque: Si x possède une base dénombrable de voisinages et si ~j7
possède une base dénombrable, possède aussi une base dénombrable
Il existe donc un filtre élémentaire  plus fin que 
donc plus
fin aussi que et tel que
f) Corollaire de résultats précédents :
Pour tout filtre 57 sur I, si 
désigne, soit la famille des 
plus fins que soit la famille des ultra filtres plus fins que ~, on a :
La première de ces formules résulte immédiatement du résultat
énoncé en (e). 
,
La seconde formule résulte de la formule (2), en remarquant que
la grille associée à .? est la réunion à la fois des filtres plus uns que


## Page 10

65 
~ et des ultrafiltres plus fins que 
Elle peut encore se traduire
ainsi : Pour tout 
inf. 
il existe des filtres 
plus fins que et
tels que 
pour x donne, le filtre intersection de ces
filtres 5’ n’est d’ailleurs pas en général un filtre ~f’, même lorsque E
est compact.
Étude du ras ou E est compact oa localement compact.
Soit 
une famille de sous-ensembles d’un espace E locale-
ment compact, et soit un filtre sur I.
a) Pour tout compact 
(ei)‘~ 
, 
il existe un élément 
tel que 
(E 
- 
K).
En effet, pour tout mEK, il existe un voisinage ‘l~ de m et un 
tels que : ~~ 
=== ~.
Il existe un nombre fini de tels voisinages 
..., 
qui
recouvrent K. Il suffit de prendre a 
i ==t, ~,..., ~ 
n
Application : Généralisation d’un théorème de Janiszewski :
Soient E un espace compact et (e)iEi une famille de sous-ensembles
de E. Soit 5 un filtre sur I.
La condition nécessair~e et suffisante pour que sup. (ei); soit connexe
est que, pour tout entourage a de la structure uniforme de E, il
existe un aE  tel que le défaut d’enchaînement de 
soit petit
d’ordre ~ (6).
b) Pour tout recouvrement ouvert fini de inf. 
par des ouverts
(~- -- 1, 2, 
... , n), tels que inf. 
~ pour tout k, il
existe un élément 
tel que, paur tout iEa et tout I~, on ait :
e 
~ 
~. 
-
Ceci résulte immédiatement de la définition de inf. (ei) _.
c) Pour que l’ensemble fermé e c E soit tel que
e = inf. (e,) ~= sup. (e~)~ , 
,
il faut et il suffit que, pour tout recouvrement ouvert fini de e par des
(6) C’est-à-dire que, pour tout couple de points de Ea, on peut passer de l’un à l’autre
par une chaîne finie de points telle que deux quelconques consécutifs de ces points soient
voisins d’ordre 8. Lorsque E est métrique, le défaut d’enchaînement de peut être
caractérisé par un nombre.
5


## Page 11

66
ouverts co,, ( l,: ---- 1, 2,..., 
) tels 
(~ l~. -~- ~ ~o,;l 
soit. compact et que
B 
jh 
/
(e 
-~ ~3 pour tout k, il existe un élément 
tel que 
:
2~ Pour tout iEa et tout k, 
Démonstration: Il résulte des résultats ci-dessus ((a) et (h)~ que la
condition est nécessaire. Montrons qu’elle est suffisante.
i ) On a sup. 
En effet, soit m~ (E - sup. 
Si 
est un voisinage compact
de m tel que ‘L n e _-_. ~, l’ouvert 
recouvre e.
Ce recouvrement satisfait aux conditions du théorème. Donc il
existe aE  tel que :
2) On a 
En effet, soit mEe, et soit w~ un voisinage ouvert de m. Posons
Le recouvrement ouvert 
de e satisfait aux conditions
du théorème. Donc il existe 
tel que, pour tout iEa. on ait
c, n c~l =~= D’où  inf. (
En résumé, on a : sup. c e c inF. (ei)~, d’où l’identité cher-
chée. 
il
Remarque. 
-- Lorsque E est compact, la condition de l’énoncé
devient :
Pour toute famille finie d’ouverts ( tels que :
il existe 
tel que, ..., etc.
4. - Relations entre deux espaces topologiques.
DÉFINITION i. - 
On dit que la relation R entre les espaces topolo-
giques X et Y est fermée (resp. ouverte) si l’ensemble ~ qui la définit
est fermé (resp. ouvert) dans X x 
Y.
Toute relation fermée a pour complémentaire une relation ouverte.


## Page 12

67
’ 
Conséquences.
i) Soit R fermée. Pour tout ensemble fermé A c X, (A) est fermé
dans X > Y ; or ‘L~(A) est la projection de l’ensemble fermé t~ n [A]
donc (A) est fermé si X est compact.
Pour tout ouvert AcX, [A] est ouvert ; (A) est la projection de
l’ensemble ~ n [A] qui est fermé au voisinage de chacun de ses points.
Donc, si X et Y sont des espaces localement compacts à base dénom-
brable, (A) est un F~., réunion dénombrable de compacts.
2) Soit R ouverte. Pour tout fermé AcX, l’ensemble n (A) est
ermé au voisinage de chacun de ses points ; mêmes conclusions que
ci-dessus.
Pour tout ouvert A c X, (A) est ouvert.
3) Pour tout ouvert A c X, si R est ouverte, le saturé S(A) de A
est ouvert.
Pour tout fermé A c X, si X et Y sont compacts et R fermée, S(A)
est fermé.
Formes équivalentes èc la définition r.
t) ) Pour qu’une relation R soit ouverte, il faut et il suffit que pour
tout xEX. et pou/’ tout 
existe un voisinage de x et un voi-
sinage y de y tels que, pour tout x on ait 
Cette condition ne fait que traduire le fait que e~ est ouvert.
DÉFINITION 2. - On dit que la relation R entre X et Y est semi-
continue supérieur°ement sur X au point xEX si, pour tout yE C ‘~~(x)’
il existe un voisinage 
de x et un voisinage 
de y tels que, pour
tout x
avec x’=,É x, on ait : ‘L00FF n ‘l~.(x’) _.
Il est immédiat que ceci équivaut à dire que
‘L~..(x) ~ sup. 
où désigne le filtre des voisinages de x diminués du point x (si x
est isolé, par définition le second membre sera =ç~).
Lorsque 
est fermé, cette condition peut s’écrire :
où 5f désigne le filtre des voisinages de x.
THÉORÈME 1. - Pour qu’une relation R soit ferrnée, il faut et il
suffit que pour tout xE X la relation R soit semi-continue supérieurement
sur X, et que 
soit fermé.
En effet, si R est fermée, (.r) est fermé pour tout  E X. D’autre


## Page 13

68
part, pour (x, y)E ~, il existe un voisinage élémentaire de (~~;, y) dis-
joint de f~ ; ceci traduit la définition de la semi-continuité supérieure.
Si au point xEX, la relation R est semi-continue supérieurement,
et si ’11,(x) est fermé, la définition 2 montre que si (x, y)E ~ f>, 
il existe
un voisinage élémentaire de (x, y) disjoint de ~. Ceci étant vrai
pour tout xEX, l’ensemble  est ouvert, donc ~ est fermé.
Conséquence Si pour tout x la relation R est semi-continue supé-
rieurement sur X et si 
est fermé, cette relation est aussi semi-
continue supérieurement sur Y en tout point y et S~~(y) est fermé.
Propriétés des relations semi-continues supérieurement.
a) Si R est semi-continue supérieurement sur X au point xoEX,
il en est de même de la relation R’ définie par ~L,’(x) -- 
Cette
relation R’ est fermée et associée à l’ensemble 
b) Soit (Ri)iEI une famille de relations entre X et Y, définies par
la famille d’ensembles 
semi-continues supérieurement sur
X au point 
La relation intersection RI, définie par ~I -- n ou encore par
t61 
I
- n est semi-continue supérieurement sur X en xp.
iEI
Démonstration: Si xo est isolé, cet énoncé est trivial. Sinon on
est ramené à montrer que sup. 
~;~ désignant le filtre
des voisinages de 
diminués du point xo.
Or 
d’où sup. sup. 
Or ’tj,,(x) c 1,,(x), d’où sup . ii(x),q,, 
0 
c i 
sup . 
De plus : sup. 
d’où n 
sup. 
iEI 
°
D’où la relation cherchée.
Si les R~ sont fermées, la relation RI est évidemment fermée :
Cette remarque généralise cette propriété connue, que l’intersection de
deux ensembles fermés cartésiens est semi-continue supérieurement
lorsque ces ensembles varient continuement ou de façon semi-
continue supérieurement.
c) THÉORÈME 2. - 
Soit R une relation entre X et Y, qui soit semi-
continue supérieurement en tout point de X. 
.
Si Y est compact, si X est connexe et si pour tout xEX. l’ensemble


## Page 14

69
est connexe (et =~ ~~), 
alors les ensembles 
i--, 
et 
sont
connexes.
Démonstration: Pour tout xEX, l’ensemble t~ n (x~ est connexe.
Donc si ~~ n’est pas connexe, il existe une partition de f~ en deux
ensembles ~~1, ~>, ouverts dans f~ tels que si ~i, ~" désignent respec-
tivement les projections de 
et 
dans X, on ait :
On montre aisément que X~ et X~ sont ouverts dans X, ce qui est
en contradiction avec le fait que X est connexe.
Donc 0 est connexe. Il en est de même de sa projection 
dans Y.
COROLLAIRE. - Si R est fermée, si X et Y sont compacts, et si X
est connexe ainsi que tout ‘l~ 4 (x) ( pour x E X.), aloi-s les ensembles
et-(X) sont des continus.
ci) Cas de Y compact. Si Y est un espace compact, et si la rela-
tion R est fermée, pour tout x E ’X et pour tout voisinage T~ de 1~,(~),
il existe un voisinage 
de x tel que
Exemples généraux de relations semi-continues supérieurement.
A 
toute relation R entre -X et Y, on peut associer trois relations
intéressantes semi-continues supérieurement sur X.
ï) La relation Ri définie par ~~ = C~ ; c’est l’intersection des rela-
tions fermées plus larges que R ; on peut encore la définir par :
- 
sup. 
== sup. 
~~ désignant le filtre des voisinages de x.
C’est là une relation très souvent utilisée.
2) La relation Rz définie par :
Cette relation est fermée et peut encore se définir par :
désignant le filtre des voisinages de x diminués du point j-
(lorsque ~r est isolé, on pose ’l~"{~;~ = c~~.


## Page 15

70
3) La relation 11, définie comme intersection des relations semi-
continues supérieurement sur X et plus larges que I~.
La relation Ti~ peut être définie aussi par 
-==: ~.~ ~ 
ou par
~ 
~t~,(x) t~ sup. 
° 
.
Semi-continuité supérieure au sens fort.
Il existe, à côté de la semi-continuité supérieure que nous venons
d’étudier, un autre type de semi-continuité supérieure d’ailleurs
moins intéressant, et que nous signalons ici surtout parce qu’il
s’introduit de façon analogue à la semi-continuité inférieure dont
nous parlerons plus loin.
DÉFINITION 1 BIS.- On dit que la relation 11 entre ~ et Y esl mi-
fermée suivant X si, pour tout ensemble fermé B c Y, l’ensemble ’,C,(B)
est fermé dans X.
DÉFINITION 2 Bis. - On dit que la relation R entre X et Y est semi-
continue supérieurement au sens fort au point xoEX si, pour tout voi-
sinage éD de 
dans Y, il existe un voisinage 
~;o tel que
On 
montre aisément que, pour que R soit mi-fermée suivant X,
il faut et il suffit qu’elle soit semi-continue supérieurement au sens
fort en tout point de X.
Si Y est un espace normal, et si ‘!~(.ca) est un ensemble fermé,
la semi-continuité supérieure forte en ro entraîne la semi-continuité
supérieure ordinaire.
Si Y est un espace compact, la semi-continuité supérieure ordi-
naire en xo entraîne la semi-continuité forte.
Donc si Y est compact et si é1J(XO) est un ensemble fermé, ces deux
semi-continuités sont identiques au point xo.
On peut souligner le peu d’intérêt de la semi-con tinuité supé-
rieure forte par le résultat suivant, qui montre combien cette semi-
continuité est restrictive.
THÉORÉME 3. - Lorsque X et Y sont des espaces métrisables, si R
est semi-continue supérieurement au sens fort au point xEX, il existe
un sous-ensemble compact 
tel que, pour tout voisinage 
cle
K dans Y, il existe un voisinage 
xo tel que 
:
Donc, si l’on néglige ce qui se passe au voisinage du sous-
ensemble compact K de 
--- sous-ensemble en général non-


## Page 16

71 
dense sur 
on 
voit qu’en gros on a 
dès que 
:r~
est assez voisin de Xo (cette inclusion est d’ailleurs vérifiée effective-
ment lorsque 
est ouvert).
Relations semi-continues inférieurement.
DÉFINITION 3. - On dit que la relation Il entre X et, ~- est mi-
ouverte suivant X si, pour tout ensemble ouvert 
l’ensemble
~(B) est ouvert dans X. 
.
DÉFINITION /~. - On dit que R est semi-continue inférieurement sur
X au point xoEX si, pour tout YE elpour tout voisinage 
de y,
il existe un voisinage 
xo tel que, pour tout 
on ait :
~l~ (x’) ~ 
0 -
Ceci équivaut d’aillectrs à dire que 
c inf. 
, 5 désignant
le jilire des voisinages de xo,
Il est immédiat que pour que R soit mi-ouverte suivant X, il
faut et il suffit que R soit semi-continue inférieurement en tout
point de X.
Propriétés des relations semi-continues inférieurement. 
R
a) Si R est semi-continue inférieurement sur X au point xoEX,
il en est de même de la relation R’ définie par 
b) Soit (Ri)iEI une famille de relations entre X et Y, définies par
la famille d’ensembles 
et semi-continues inférieurement sur
X au point xoEX.
La relation réunion Ri, définie par ~I U 
ou encore par
tel 
I
‘~I(x) - U 
est semi-continue inférieurement sur X au point
I
Ceci résulte de la formule :
En particulier. si les Ri sont mi-ouvertes, Rj[ est aussi mi-ouverte.
c) Soient Rx, Y une relation entre X et Y ; Ry, z une relation
entre Y et Z ; et Rx, z la relation composée de Rx,y et Ry, z.
Si Rx, y est mi-ouverte suivant X, et Hy, z mi-ouverte suivant Y,
la relation Rx, z est mi-ouverte suivant X : ceci résulte immédiate-
ment de la définition 3.


## Page 17

72 
Exemples clc relations mi-ouverles.
i) Toute relation R ouverte est mi-ouverte.
2) Toute relation R définie par un ensemble (; tel que, pour tout
yY, l’ensemble  n ~y~ soit ouvert sur ~y~, est mi-ouverte.
3) Si R est une relation quelconque entre X et Y, parmi toutes
les relations mi-ouvertes moins larges que R, il en existe une plus
large que toutes les autres, à savoir leur réunion (propriété (b) ci-
dessus). Cette relation RN sera dite le noyau de R.
Il est immédiat que ’~l,(x’) est fermé dans 
; 
en parti-
culier, si (x,) est un ensemble fermé,’-1~,,;(~~) est aussi un ensemble
fermé.
Remarque i : Soit (f) une famille d’applications continues de X
dans Y. Chacune de ces applications engendre une relation mi-
ouverte Ri entre X et Y, définie par 
~ 
.
La relation R réunion des Ri est mi-ouverte. L’étude de certains
cas simples pourrait faire croire qu’inversement toute relation mi-
ouverte R est de cette forme. Mais il n’en est rien, même dans
le cas où X, Y sont deux segments de droite et où tout ’1)(,V)
est un ensemble fermé ; il n’existe même en général aucune
application continue f(x) de X dans Y telle que f( pour
tout xEX.
Remarque 2: 
: Nous avons fait remarquer plus haut que, pour
toute relation R entre X et Y, la relation RI définie par
sup 
~~.(.~°’)aiP 
_
était une relation semi-continue supérieurement (et même fermée)
sur X.
Par contre il est inexact en général que la relation R’ définie par :
~1~,’(x) - 
inf. 
soit semi-continue inférieurement sur X.
Remarque 3: La semi-continuité supérieure n’est pas une notion
duale de la semi-continuité inférieure. Cette dualité n’a lieu en fait
qu’entre les relations fermées et ouvertes, qui ne sont qu’un cas
particulier des relations semi-continues.
Relations particulières.
Supposons que, pour tout xEX, 
contienne un élément et un
seul. ‘I)(:~) définit donc une application de X dans Y.


## Page 18

73
i) Dans le cas général la continuité de ’1)~.~,) ne résulte pas de ce
que t~ soit fermé (’).
Par contre si Y est compact et si  est fermé, on a vu (~ ~, au
début) que, pour tout fermé B c Y, l’ensemble 
fermé dans
X. Donc l’application ’11,(x) est alors continue.
Inversement, si ‘1~ (x) est une application continue de X dans Y,
on sait qu’on ne peut affirmer que l’ensemble représentatif ë de 
est fermé dans (X >Y) que si Y est séparé.
Conséquence: Si Y est compact, la condition nécessaire et sulli-
santé pour que l’application 
de X dans Y soit continue, est que
1 ensemble représentatif~ de cette application soit fermé dans X X 
Y.
2) Supposons maintenant 8 fermé, mais X, Y quelconques.
La relation R suivante dans X :
R(x xJ) 
si 
1 y (x1) - ~_~ (x~)~
est une relation d’équivalence. Toute classe d’équivalence X(y) (où
est un sous-ensemble fermé de X.
Soit g l’application canonique biunivoque de X/R sur 
En général, ni ~, ni 9-’ ne sont continues (8); les espaces X/R et
‘~~(X) n’ont donc pas en général de topologies comparables.
Par contre, si X est compact, 
est fermé pour tout fermé
A c X ; ceci est vrai en particulier pour tout A fermé saturé pour la
relation R. Donc gi est continue ; si Y est compact, 
est fermé
pour tout fermé B c Y; donc g est continue.
Donc si X et Y sont compacts, g est une homéomorphie entre les
espaces E~R et ‘~~~(X), qui sont d’ailleurs compacts puisque ‘1~-(X) est
l’image continue d’un compact.
Définition générale d’une relation d’équivalence fermée
dans un espace topologique.
DÉFINITION 5. - On dit que la relation d’équivalence R dans l’espace
est ~ f’ermée si, clans E > E, l’ensemble ~ qui définit R est fermé.
Cette définition entraîne que toute classe d’équivalence suivant R
est un ensemble fermé.
; ~) Par exemple, i-oU B le segment (0 - 1), Y la demi-droite y ~> o Ln fonction ’))(.’.’)
égale à I pour x =1: o et à o pour x = 
o n’est pas continue et a cependant un ensemble
x
représentatif 8 fermé dans X > Y.
(8) On en aura un exemple en remplaçant flaas l’exemple ci-dessus (Note ~) X par la
demi-droite x ~ ~.


## Page 19

74
La propriété suivante est caractéristique des relations d’équivalence
fermées :
Pour tout couple (x1, X2) tel que non-R(x1 x2), il existe un voisinage 
de .c et un voisinage ‘1 y= de x~ tels que, pour tout x; E ‘lx, el tout x;É ‘’l’?x_,
on ait rzon-fl(xi, x’;). 
.
La démonstration de ce fait est immédiate.
il peut encore se traduire de la façon suivante :
Si K est une classe d’équivalence quelconque suivant R, pour tout
filtre Ji sur E convergeant vers un point de K, on a :
sup. S(x),I, K,
en désignant par S(x) le saturé de lotit point xEE.
Il est intéressant de comparer les relations d’équivalence fermées
dans E avec celles qui pourraient se déduire, comme dans l’étude
ci-dessus (Relations particulières), de certaines relations fermées
entre E et un autre espace. On va voir qu’en général ces relations
multivoques fermées ne conduisent pas à des relations d’équivalence
fermées. Soit par exemple E un espace compact et R une relation
d’équivalence dans E ; on impose seulement à Il que toute classe
d’équivalence suivant R soit un ensemble fermé, ce qui n’entraîne
pas que R soit fermée en notre sens. Or donnons à l’ensemble quotient
E/R la topologie discrète. Il est immédiat que l’application canonique
ï?
de E sur l’espace discret ~- 
définit entre E et cet espace discret une
relation fermée. Et cependant la relation d’équivalence dans E
associée à cette application canonique est identique à R, donc n’est
pas fermée.
THÉORÈME l~. - Soit (R:)e. une famille de relations d’équivalence
dans l’espace topologique E ; et soit R -- inf. (Ri)iEI.
i) Il existe une application canonique continue et biunivoque de
E~ R dans l’espace produit il ERi.
iEI
.2) Si toute Ri est fermée, R est fermée
3) si chacun des espaces EEii est séparé, E~R est séparée; la réci-
proqtze est inexacte.
Démonstration : I ) Remarquons d’abord que tout ensemble ouvert
de E saturé pour une Ri est aussi saturé pour R.
Pour tout i, il existe une application canonique continue fi de
E/R sur E/Ri : c’est celle qui, à toute classe d’équivalence suivant R
associe la classe d’équivalence suivant Bi qui la contient,


## Page 20

75
Soit f l’application canonique , f -= (~ f t) de I:, 11 dans le produit
topologique II ERi ; elle est continue, et d’autre part elle est biuni-
t61 
I
voque puisque R -- inf. (Itl’ ’)iEl»
2) Toute Ri étant définie par un ensemble fermé fi dans Ex E,
la relation R, définie par  t est aussi fermée.
iEI 
I,
3) Si tout E/R, est séparé, il en est de même de TT E ’/Ri. Comme
tI 1
/(E/R)cJJE/R,, l’espace f(ER) est séparé. Il en est donc de
iEl
même de E/R.
L’application f n’est pas en général bicontinue. Il suflit pour le
voir de prendre E séparé et Ri, R~ telles que ERi et E R aient une
topologie grossière (’*) et que toute classe d’équivalence suivant
R -- inf. (R1, R,,) contienne un seul élément. Alors EI, homéo-
morphe à E, est séparé, alors que f’(E‘R) a la topologie grossière.
Application r : Si E est compact et si la famille (Ri)iEI est telle que
tout ERi soit compact, E~ R est compact.
Exemple: Soit E un espace compact et g une application continue de E dans
un espace séparé. La relation d’équivalence R définie dans E par : R(.x;, .x~~ si
g(xl) = g(xz et si ni,, m,) sont sur une même composante connexe de E est telle
que E/R soit séparé, donc aussi compact.
Notons ici que, si E n’est pas compact, et si lil, Ii_ sont telles que
E/Ri et E/R., soient compacts, l’espace séparé E/R, où R==inf. (R1, R,~)
n’est pas forcément compact.
Application .2 : Espace séparé associé à un espace topologique
Soit E un espace topologique quelconque.
Soit (RJ la famille de toutes les relations d’équivalence dans E
telles que E/R soit séparé (cette famille n’est pas vide).
Si on pose Il -- inf. l’espace E/R est séparé.
Nous dirons que E/R est l’espace séparé associé à E (’°~).
(9) La topologie grossière sur un ensemble A est celle dans laquelle les seuls ensembles
ouverts sont A et o.
(10) On pourrait obtenir R par le procédé transfini suivant
Pour tout espace topologique A, disons que S(a, b) (où a, bEA), s’il existe une suite
finie ct,, az, ..., an-i- 1 de points de A, avec ai = 
a, a,~ + i b, et une autre suite finie
~i, x2, ..., x,a de points de A, telle que ak et (Xlc - 1 E Y/. pour k = 1, 2, ..., lL eu désignant
par 7k- l’intersection des voisinages fermés de xk.
La relation S est une relation d’équivalence.
Désignons alors, dans E, la relation S par SI puis par S2 la relation d’équivalence
dans E induite par la relation S dans E,/S, ; et de façon générale par S,t.,_ 1 Crc entier) la


## Page 21

76
Borne supérieure. 
- On n’a pas de théorème analogue au pré-
cédent pour R == sup. (Ri)ïI.
Soit par exemple E une circonférence ;  deux diamètres de
E, et R,, R, les deux relations d’équivalence ainsi définies :
Rt(xj, .xv,) si x1 et x,~ sont symétriques par rapport à 
Chacun des espaces E/Ri est compact. Or, si (~L, ,,)/’r est irrationnel,
toute classe d’équivalence suivant Iz = sup. (Rl, R,,) est partout dense
sur E ; donc E/R a une topologie grossière.
THÉORÈME 5. - Soit R une relation d’équivalence dans un espace
compact E. Les propriétés suivantes cte R sont équivalentes: 
:
i) R est fermée.
2) Le saturé de tout ensemble fermé est fermé.
3) Toute classe d’équivalence est un ensemble fermé et possède une
base fondamentale de voisinages ouverts saturés.
4) Toute classe d’équivalence, est un ensemble fermé, et pour tout voi-
sinage ‘L’ de y, il existe un sous-voisinage ‘1, de -,, tel que toute classe
d’équivalence ayant un point au moins dai~s ‘i‘z, soit contenue dans ‘l i.
L’une quelconque de ces propriétés entraîne que E/R soit séparé,
donc aussi compact.
THÉORÈME 6. - Soit R une relation d’équivalence fermée dans un
espace localement compact E.
Le saturé de tout ensemble compact K c E est fermé; 
: ceci carac-
térise les relations R fermées dans E.
L’espace quotient E~R n’est pas en général séparé. Mais lorsque 111
est dénombrable à l’infini (’11, I;iR est séparé et normal (sans être pour
cela localement compact) ( 12).
La démonstration de ces théorèmes ne présente pas de difficultés.
La seconde partie du théorème 6 se démontre en utilisant le fait
que le saturé de tout ensemble compact est un ensemble fermé.
Applications immédiates : t) Soit E un espace localement compact ;
relation d’équivalence dans E inlaite par la relation S dans E/Sn. On pose alors
SC,) = 
Sup. {~n) rx-9, r, 
. 
.
Puis on définit S"_m, Sr,+.,, etc. On peut ainsi 
définir S pour lonl nombre
ordinal a. Si pour a = 
ao, E,/Sao est séparé, on aura S; - s 
pour tout > 
ao, et ou
peut alors montrer que , 
;== P~.
L’existence d’un tel ao résulte de l’axiome du choix
(11) C’est-à-dire que E est une réunion dénombrable de compacts.
(12) Exemple: E 
est l’ensemble suivant dans le plan xOy: La droite x == o plus l’en-
semble des points de coordonnées Cx == t ~ y _-_ pl ~ où n = t, 2, ...,...jp=:t, 2, ..’..
~ . B 
n 
/
Et l’on prend pour classes d’équivalence de H les composantes connexes de E.


## Page 22

77
la relation d’équivalence li dont les classes d’équivalence sont les
composantes connexes de E est fermée.
a) Soit Il, une relation d’équivalence fermée dans l’espace loca-
lement compact E. Soit R, la relation d’équivalence dont les classes
d’équivalence sont les composantes connexes des classes d’équivalence
de Ri. La relation R, est fermée.
Relations d’équivalence fermées en des sens plus stric°ts.
On peut renforcer progressivement la définition des relations
d’équivalence fermées.
DÉFINITION 5 Bis. - On dit que la relation d’équivalence R dans
l’espace E est FORTEMENT FERMÉE si la relation canonique entre les
espaces E et E/R est fermée.
Il est immédiat que toute relation R fortement fermée est fermée.
La propriété suivante est caractéristique des relations R fortement
fermées :
Pour tout couple (x, x,,) tel que non-R(xi, x2), si -,,,(x,) désigne la
classe d’équivalence contenant xi, il existe un voisinage ouvert saturé
T-  Y(a? et un voisinage ‘’L= de ~, tels que
‘L~.° "i ‘~~~x-,) - 0.
Par exemple, si E est localement compact, toute relation d’équi-
valence R fermée dans E est aussi fortement fermée. Mais ceci ne
s’étend pas au cas général : On pourra en construire un exemple
dans l’espace E obtenu comme réunion d’un disque ouvert et d’un
point de sa circonférence.
DÉFINITION 5 TER. - On dit que la relation d’équivalence R clans
l’espace E est TRÈS FORTEMENT FERMÉE si l’espace E/R est sépare.
Il est immédiat que toute relation R très fortement fermée est for-
tement fermée.
La propriété suivante est caractéristique des relations R très for-
tement fermées.
Pour tout couple (y~, ~ ,) de classes d’équivalence distinctes, il existe
deux ensembles ouverts saturés disjoints contenant respectivement ~ 
1
et’
Il existe des relations R qui sont fortement fermées sans l’être
très fortement (voir le théorème ci-dessus relatif aux espaces locale-
ment compacts). Mais dans un espace compact E toute relation
d’équivalence fermée est très fortement fermée.


## Page 23

DEUXIÈME PARTIE
Pseudo-topologies, pré-topologies et topologies.
Dans un espace métrique E, la définition d’écart mutuel de deux
ensembles fermés (’~) organise l’ensemble 2E des sous-ensembles
fermés de E en espace métrique. Ceci induit sur 2E une topologie
qu’on peut appeler topologie de la convergence uniforme.
On pourrait donner des définitions analogues pour tout espace
uniforme E.
Mais tout espace topologique n’est pas uniformisable, et même si
E est uniformisable, il peut l’être de plusieurs façons et les topologies
sur 2E associées à ces diverses structures uniformes ne sont pas tou-
jours identiques.
D’autre part on a souvent besoin d’une notion de convergence
différente de la notion de convergence uniforme. Par exemple, si E
est localement compact, on utilise souvent la notion de « convergence
uniforme sur tout compact ».
Il semble donc utile de définir pour un espace topologique quel-
conque E une notion de convergence sur ~~ et d’essayer d’organiser
~E en espace topologique.
Il est naturel pour cela d’utiliser les définitions des limites supé-
rieure et inférieure d’une famille d’ensembles suivant un filtre. Il se
trouve que la notion de convergence associée à cette notion de limite
ne définit pas toujours directement sur E une topologie. Elle définit
ce que nous appellerons une pseudo-topologie, c’est-à-dire une
structure généralisant les structures ‘Ç’~ (’~).
Nous étudierons brièvement les pseudo-topologies et en particulier
les pré-topologies, plus directement liées à la notion d’adhérence.
(131 Notion due à Hausdorff. Voir Kuratowski, Topologie I, page 89.
Voir Kuratowski, loc. cit 
, page -,6 ; un espace ~* est défini à partir de la notion
(le suite convergente


## Page 24

79
Puis nous montrerons comment à toute pseudo-topologic on peut
associer une pré-topologie et une topologie.
Nous pourrons utiliser cette étude pour définir une pseudo-topo-
logie et une topologie sur l’ensemble des applications continues d’un
espace dans un autre.
Nous ferons ensuite une étude un peu plus détaillée de ces notions
dans des espaces moins généraux (compacts, connexes, localement
connexes, etc.).
5. - Structures pseudo-topologiques sur un ensemble.
Une structure pseudo-topologique ~i sur un ensemble E est définie
par la donnée d’une relation R(U,, m), dite relation de pseudo-converr-
gence entre l’ensemble des ultrafiltres  sur E et l’ensemble des
points m de E.
Lorsque R(tl, m) est vraie, on dit que m est pseudo-limite de ‘Ll,
ou encore que ‘’l,l, pseudo-converge vers m (15).
Nous supposerons vérifié le seul axiome.
Ui. Pour lotit mEE, l’ultrafiltre des sur-ensembles de ~ m pseudo-
converge vers m.
Exemple Dans tout espace topologique E, la définition topolo-
gique ordinaire de la convergence d’un ultra-filtre induit sur E une
pseudo-topologie qui est dite induite par la topologie de E.
Extension de la relation de pseudo-convergence
aux filtres quelconques.
DÉFINITION I - 
On dira qu’un filtre ~ sur E pseudo-converge vers
m si tout ultra-filtre plus fin que pseudo-converge vers m. Cette
relation se notera R(f m).
Exemple: Si E est un espace topologique, on vérifie aisément que
l’extension R(f m) de la relation R(u, m) induite par la topologie
de E est identique à la relation de convergence topologique dans E.
Toute relation R(f, m) possède évidemment les propriétés sui-
vantes :
(’15) rn ultrafiltre. p(,iii n’avoir aucun point pseudo-limite.


## Page 25

80
Autrement dit, plus titi filtre est Jin, plus il cc de points pseudo-
limites. 
.
F,~ : Si non-R rn), il existe un ç’ ~ ~ tel que, pour tout 
on ait non-R(f, m).
F3 : Pour tout mE E, si uif désigne le filtre des sur-ensembles de ~ m ~ 
,
on a R( ~, in).
Inversement, soit R(~, m 
) 
une relation entre l’ensemble des
filtres J sur E et l’ensemble des points na de E.
Désignons par R(’ll, m) la restriction de l~(ais, m) à l’ensemble des
ultrafiltres ’11.
On vérifie aisément que, si la relation R(~, in’) vérifie les axiomes
Fl’ F;, F3, la relation R(U,, m) est une relation de pseudo-convergence
(axiome F3), et l’extension R/(5i, m) de R(U, m) aux filtres quel-
conques f est identique à R(f, ni) (axiomes F~ et F,).
Comparaison des pseudo-topologies.
Soient ~tl et ~3~ deux pseudo-topologies sur E, définies par les
relations R1(5i, in) et R,(J;, m). On dit que p1 est plus fine que p,
si R~(~, m) ~- R2(~‘, m) (16).
Autrement dit, plus une pseudo-topologie est fine, moins les filtres
ont de points pseudo-limites.
Par exemple, si deux pseudo-topologies ~1 et ~z sont telles que
pour chacune d’elles tout ultrafiltre possède un point limite et un
seul, ~1 et l)., sont, ou bien non comparables, ou bien identiques.
Applications pseudo-continues.
Soient, sur deux ensembles E, E’, deux pseudo-topologies p et ~’,
définies par les relations R, R’, et soit f une application de E dans E’.
Si mEE et m’ = f(m), on dira que f est pseudo-continue en m si
R(f in) ~ 
R’(’, m’) 
en désignant par f’ le filtre de base f(f).
Si f est une application biunivoque de E sur E’, qui soit pseudo-
continue ainsi que l’application réciproque de f, on montre aisément
que cette application f réalise une isomorphie des structures pseudo-
topologiques p et ~’. Autrement dit, ces structures sont pseudo-
homéomorphes.
On démontre aisément aussi le théorème des applications composées
pseudo-continues.
(16) Cette définition est la même que la définition que nous avons donnée pour les
relations quelconques.


## Page 26

81 
Somme et produit pseudo-topologiques.
Ces notions se définissent, comme dans les espaces topologiques,
à partir de la notion d’application pseudo-continue.
Soit par exemple (EJ . une famille d’espaces pseudo-topologiques.
Sur l’ensemble produit E - r~ E~, la pseudo-topologie produit sera
c~I
par définition la moins fine de toutes celles qui rendent pseudo-
continues les fonctions coordonnées. Autrement dit, on dira que
R(f, m) est vraie si Ri(Ji, mi) est vraie pour tout iEI, i et m, étant
les projections de f et m dans Ei.
Pseudo-topologie quotient.
Soit ~ une pseudo-topologie sur un ensemble E, et R une relation
d’équivalence dans E.
On appelle pseudo-topologie quotient sur l’ensemble quotient E/R,
la pseudo-topologie la plus fine rendant pseudo-continue dans E l’appli-
cation canonique sur E/R. On la notera par p/R.
On peut montrer que cette pseudo-topologie quotient existe bien
et qu’elle est définie par la relation R’( ~’, m’) suivante :
Si R(~P, m) désigne la relation définissant p, on dira que R~(~, m)
est vraie si f’ et m’ sont les images canoniques d’un 51 et d’un m tels
que R(q, m) soit vraie.
On vérifie aisément que cette relation I~.’(f~’, m’) satisfait bien aux
axiomes F~, F2, F3
Remarque: Si p est une pré-topologie (17) (resp. une topologie), la
pseudo-topologie quotient p/R n’est pas forcément une pré-topologie
(resp. une topologie).
Pseudo-adhérence d’un ensemble.
DÉFINITION 2. - On dit que m est pseudo-adhérent au filtre -if sur
E s’il est pseudo-limite d’un filtre plus fin que fjí.
L’ensemble des points pseudo-adhérents cc s’appelle sa pseudo-
adhérence et se note pur ~~f.
Remarque r : Plus un filtre est fin, plus il a de points pseudo-
limites et moins il a de points pseudo-adhérents.
Remarque 2 : Il existe des filtres f dont la pseudo-adhérence est
identique à l’ensemble des points pseudo-limites. On dit qu’un tel
(17) voir plus loin la définition
G


## Page 27

82
filtre pseudo-converge strictement. l’ar exemple tout ultrafiltre
pseudo-converge strictement.
DÉNINITION 3. - Pour tout sous-ensemble Ac E, on appelle pseudo-
adhérence de E, et on note par A la pseudo-adhérence du filtre des
sur-ensembles de A.
On pourrait dire encore que A est la réunion des pseudo-adhé-
rences des filtres ayant une base dans A, ou l’ensemble des points
pseudo-limites des ultrafiltres ayant une base dans A.
Il est immédiat que A
réunion finie d’ensembles.
pour toute
Pour tout filtre
mais il n’y a pas en général
identité entre les deux termes de cette inclusion, même si F est un
ultrafiltre. Ceci tient à ce que, pour une famille (U1,1.1)iEI d’ultrafiltres,
le filtre 5i intersection de cette famille est en général tel que la
famille des ultrafiltres plus fins que F soit strictement plus grande
que Z)tm’
Limites supérieure et inférieure d’une famille d’ensembles.
On peut, dans tout espace pseudo-topologique E définir encore les
notions de limites supérieure et inférieure d’une famille d’ensembles.
Il suffit pour cela de présenter sous une forme convenable les défini-
tions données dans le cas où E est un espace topologique :
Soit (ei)iI une famille de sous-ensembles de E, et a un filtre
sur I.
L’ensemble sup. (e~) ~ sera défini comme l’ensemble des points
pseudo-limite des ultrafiltres ainsi construits : Si ~.l désigne un ultra-
filtre plus fin que Jf, pour tout iEI, on pose y(t)==un point quel-
conque de el. On définit ainsi une application de 1 dans E ; par défi-
nition l’ultrafiltre de base f(‘Ll.) est un ultrafiltre ‘LL’.
L’ensemble inf. (ei),, sera défini par la formule :
où (EJ désigne la famille des filtres (ou des ultrafiltres) plus fins
que f~.
Par exemple. pour tout A c E, si l’on prend A == e; (pour tout iEI,
on trouve que sup. (e;)F, = 
inf. { e;)f _ 
A.


## Page 28

83
6. - Structures pré-topologiques sur un ensemble.
On dit qu’une structure pseudo-topologique p est une structure
pré-topologique si elle possède la propriété suivante :
U~ : Pour tout ultrafiltre ~LL sur E, on a : U, n 
(1.
aE(,
Filtre des pseudo-voisinages d’un point. 
,
Pour mE E. soit ’ l’ensemble de toutes les parties acE telles
que : mea. Pour toute structure pseudo-topologique ~?, ~,n constitue
une grille soit le 
filtre associé à Gm (4).
Ce filtre 5im est l’intersection des filtres qui pseudo-convergent
vers m. Il a pour éléments les complémentaires des parties b de E
telles que (m 6 ; nous appellerons pseudo-voisinages de m les éléments
de q" ; autrement dit 5im sera le filtre des pseudo-voisinages de iii.
Tout ultrafiltre plus fin que ,n est une partie de ~.~ ; donc si
l’axiome U,, est vérifié, cet ultrafiltre pseudo-converge vers m.
Donc si l’axiome U~ est vérifié, le filtre 71f pseudo-converge aussi
vers m.
Inversement, supposons qu’une pseudo-topologie p satisfasse à la
condition :
U2 : Pour tout mEE, le filtre ~,n des pseudo-voisinages de m pseudo-
converge vers m.
Cette condition entraîne la propriété U2. En effet, soit U un ultra-
filtre sur E ; si mE;’ pour tout aE0t.l, l’ultrafiltre ‘1l est plus fin que
 ; donc  pseudo-converge vers m, autrement dit m’=U ; comme
d’autre part on a toujours 7[ en;;, on a bien %== n 
a.
aEU, 
aEU,
Les axiomes U, et Uz sont donc équivalents (dès que l’axiome U 
1
est vérifié).
THÉORÈME 1. - Pour toute pré-topologie ~, on a pour tout filtre ~)-c
sur E :
Démonstration: 
: On sait déjà que


## Page 29

84
Soit alors mE n 7:. Comme m est pseudo-adhérent à tous les élé-
aEfF
ments de ~, il existe, à cause de la définition de ~",, une borne supé-
rieure  pour ~ et ~,n.
Tout ultrafiltre plus fin que  est plus fin que ~"~, donc pseudo-
converge vers iii. Comme est plus fin que Jf, on a bien mÎ-J.
S’tr~uctures de pré-adhérence et structures pré-topologiques.
Nous savons que, pour toute pseudo-topologie p sur E, on a les
propriétés :
Réciproquement, supposons définie sur l’ensemble s~(E~ des
parties X de E une opération X définissant une application de ~~,E)
dans lui-même et vérifiant les axiomes suivants :
° 
Nous dirons que X est la pré-adhérence de X et que l’opération X
définit sur E une structure de pré-adhérence.
A toute structure de pré-adhérence sur E, on peut associer une
pseudo-topologie définie par la relation R(’tl, m) suivante :
On dira que R(’Ll, m) est vr°aie si m est pré-adhérent (’9) a’ tout
élément de 
Cette définition entraîne que l’ensemble des points pseudo-limite
de ’IL soit identique à F a.
aEj 
_
Pour tout X  E, désignons par X 
sa pseudo-adhérence relative à
la pseudo-topologie définie par R(’11, m).
THÉORÈME 2. - Pour tout X c E, on a X 
-- X. 
.
Démonstration: : 1 ) X ~ X. En effet, pour tout ultrafiltre ’U ayant
une base sur X, et pour chacun des éléments a de cette base, on a :
a c X ; donc tout point pseudo-limite de q1 appartient à X.
2) XcX. En effet, soit mX. Soit l’ensemble des parties a de
X telles que mEa. Il est immédiat que (~ constitue une grille sur X ;
(18) La définition générale de la réunion finie implique qne Aq entraine (0) = o.
(1~) rrv est dit pré-adhérent à 1 s~ m6B. 
"
pour toute réunion finie.


## Page 30

85
Hoit f1i le filtre sur X associé à (.. Tout ultrafiltre tll sur X plus fin
que a ses éléments dans G. Donc l’ultrafiltre sur M ayant pour
base u pseudo-converge vers m; d’ou mEX.
Corollaire: Pour tout ultrafiltre lU sur E, on a
Autrement dit, la pseudo-topologie associée à une structure de
pré-adhérence est une pré-topologie ; et la pseudo-adhérence associée
à cette pré-topologie est identique à la pré-adhérence donnée.
On peut donc définir une pré-topologie, soit par une relation
R(‘l,l,, m) de pseudo-convergence, soit par une opération X de pré-
adhérence. On peut donc identifier les notions de structure pré-
topologique et de structure de pré-adhérence.
Pré-topologie associée cz une pseudo-topologie.
Soit p une pseudo-topologie sur E. La pseudo-adhérence (X)
satisfait aux axiomes Ai et ~z. Soit ~’ la pré-topologie définie par
l’opération X. On dit que p~ est la pré-topologie associée ~c ~.
La relation ‘ c  a montre que pcp. Plus précisément, ~’ est
"eg
la plus fine de toutes les pré-topologies moins fines que p.
Topologie associée à une pseudo-topologie.
Soit p une pseudo-topologie sur E ; et soit X c E.
On dit que X est fermé si X == X.
On dit que X est ouvert si son complémentaire est fermé.
Il est immédiat que, pour que X soit ouvert, il faut et il suffit que,
pour tout mEX, si R(, m) est vraie, il existe un élément aEf tel que
a c X ; ceci équivaut encore à dire que X est un pseudo-voisinage de
chacun de ses points.
Les ensembles ouverts possèdent les propriétés suivantes :
01 : Toute réunion d’ensembles ouverts est un ensemble ouvert.
O, : Toute intersection finie d’ensembles ouverts est un ensemble
ouvert.
Donc les ensembles ouverts pour p sont les ensembles ouverts
d’une topologie qui est dite associée à )).


## Page 31

86
Par exemple, la pseudo-topologie induite par une topologie donnée
sur E a pour topologie associée la topologie donnée.
On peut caractériser la topologie associée à ~ comme la plus fine
de toutes les topologies dont les pseudo-topologies induites sont
moins fines que t).
Il est immédiat que si ~t’ désigne la pré-topologie associée â p, la
topologie associée à ~’ est identique à celle associée à p.
Nous énoncerons le théorème suivant, aisé à démontrer :
THÉORÈME 3. - Soit ~ une pseudo-topologie sur E, ’ ta pré-topologie
associée ce p, et ~i’’ la topologie associée ~z ~. Si R est une relation
d’équivalence dans E, il y a isomorphie canonique entre les deux
structures suivantes :
1) La pré-topologie (resp. topologie) associée à la pseudo-topo-
logie p/R.
2) La pré-topologie (resp. topologie) associée à la pseudo-topo-
logie ~’~‘l~ (resp. p’/R).
Remarquons que la topologie associée à la pseudo-topologie p"/R
est isomorphe au quotient topologique ordinaire de p" par R.
Condition pour qu’une pré-topologie soit une topologie.
Soit p une pré-topologie sur E, définie par une opération X de
pré-adhérence.
Pour que p soit identique à la structure de pré-adhérence induite
par la topologie associée à p, il faut et il suffit que soit vérifiée la
condition :
A3 : Pour tout X c E, on a X - CX) .
Les axiomes Ai, A,~), A3 (") forment un système d’axiomes équi-
valent au système des axiomes topologiques ordinaires (à partir des
ouverts, des fermés, ou des voisinages).
On obtiendrait encore un système d’axiomes équivalents en pre-
nant les axiomes Ui, U~ (ou U~) et U3, où U3 désigne l’axiome sui-
vant :
U.: Pour tout nEE, le filtre ::,n des pseudo-voisinages de m possède
(‘-’~) Les axiomes Ai, A2, A~ différent de ceux adoptés par M. Kuratowski (Loc. cit.).
Celui-ci remplace en effet l’axiome A~ par l’axiome suivant :
Pour tout mE , on a  m f - ~ in B et e ~ 
~= r~.
Cet axiome est plus restrictif que A,. Il entraîne que tout ensemble contenant un seul
point est un ensemble fermé


## Page 32

87
une base dont tout élément est pseudo-voisinage de chacun de ses
points.
Remarque: On peut dire, en termes vagues, que la notion de
pseudo-convergence est plus fine que celle de pré-adhérence
puisqu’elle permet de définir des structures plus fines que les
structures de pré-adhérence.
De même la notion de pré-adhérence est plus fine que la notion
d’ensemble fermé (ou ouvert).
C’est là une justification de l’étude des pseudo-topologies; nous
allons d’ailleurs voir que c’est un outil indispensable à l’étude de
l’espace des sous-ensembles fermés d’un espace topologique.
7. - Pseudo-topologie et topologie sur l’ensemble
des sous-ensembles fermés d’un espace topologique.
Soit E un espace topologique, et 2E 1 ensemble des sous-ensembles
fermés de E. Pour tout élément aE 2 E, nous désignerons par Xa le
sous-ensemble fermé de E que représente a.
DÉFINITION. - Pour tout filtre g sur 2E, et tout eE2E, nous dirons
que R(‘, e) est vraie si l’on a 
:
Cette relation satisfait aux axiomes Fi, F,, F~, d’après les résul-
tats que nous avons démontrés au paragraphe 3. Elle définit donc
sur ~E une pseudo-topologie ) dans laquelle tout filtre possède au
plus un point pseudo-limite.
En général, cette pseudo-topologie n’est pas une pré-topologie :
c’est le cas par exemple si  est la réunion d’un disque ouvert et
d’un point de la circonférence du disque.
DÉFINITION. -Nous dirons qu’un espace topologique E est compac-
toïde si tout filtre sur E possède un point adhérent.
Nous dirons que E est localement compactoide si tout point de E
possède un voisinage compactoide.
THÉORÈME i. 
. 
- Pour que la pseudo-topologie ~ de 211 soit une
pré-topologie, il est nécessaire que E soit localement compactoïde.
Lorsque E n’est pas localement compactoïde, il existe sur ~~ des
altra filtres qui, dans la pré-topologie associée à ~ pré-convergent vers


## Page 33

88
plus d’un point. La topologie associée à ~ est alors non séparée (21).
Démonstration: Soit mo un point de E ne possédant aucun voisi-
nage compactoïde. Le point in, possède au moins un voisinage
ouvert c~ distinct de E, sinon mo serait adhérent à tout filtre sur E,
et E serait alors compactoïde.
Soit F l’ensemble fermé complémentaire de c~.
Pour tout voisinage ouvert V de mo, il y a par hypothèse des ultra-
filtres l,l, ayant une base sur V et n’ayant aucun point adhérent sur E ;
ceci peut se traduire par :
On a donc aussi :
L’intersection des ultrafiltres U 
-1 
est nu filtre ~ tel que mo soit
adhérent à T, d’où moE sup. CF  m  )Cf
Il existe un ultrafiltre 1.’ plus fin que if et tel que
L’ensemble limite des (Fu -~-in-~ ) suivant l’ultrafiltre ~,~’ est donc
distinct de F. L’axiome U~ n’est pas vérifié, donc p n’est pas une
pré-topologie.
Dans la pré-topologie associée à p, l’ultrafiltre sur 2E associé à ~Ll’
pré-converge vers tout point de pseudo-convergence des ultrafiltres
associés aux ll ; donc il pré-converge vers l’élément représentant F ; 
-,
comme il pré-converge aussi d’après ce qu’on vient de voir, vers un
autre élément, il a au moins deux points pré-limite.
A fortiori, dans la topologie associée à p, il y a des ultrafiltres qui
ont plus d’un point limite ; cette topologie n’est donc pas séparée.
THÉORÈME 2. - Si E est séparé, la condition nécessaire et suffisante
potit- que la topologie sur 21, soit séparée, est que E soit localement
compact.
La pseudo-topologie ~t sur 2E est alors identique à la topologie
associée à ~ ; c’est une topologie d’espace localement compact. Pour
que ce soit une topologie d’espace compact, il faut et il suffit que E
soit compact..
Démonstration: : 1 ~ La condition est nécessaire ; car si la topologie
(’’-1) Notons ici que, quel que soit E, la topologie associée à p est telle que tout sons-
en~emble de 2E contenant un seul élément soit un ensemble fermé.


## Page 34

89
de 2E est séparée, le théorème précédent montre que E est localement
compactoïde ; comme E est séparé, il est localement compact.
(2 La condition est suffisante :
Comme E est localement compact, il résulte des formules 3 et 5,
pages 62 et 63, que dans la pseudo-topologie p de 2E, pour tout mE2E,
le filtre am des pseudo-voisinages de m pseudo-converge vers m. Donc
p est une pré-topologie.
On montre ensuite que gim possède une base illm dont les éléments
sont pseudo-voisinages de chacun de leurs points. On obtient les
éléments de B3m à partir des recouvrements ouverts étudiés page 65 (c),
de la façon suivante : Pour un tel recouvrement ouvert (cl, ..., c,2),
on appelle a(c, ..., , ~pn) l’ensemble des sous-ensembles fermés de E
dont chacun est inclus dans U c 
et rencontre tout w. La famille de
i
ces a(c~~, ..., G)n) constitue la base ,n cherchée.
Ceci montre que p est une topologie (axiome Ug) : on montre
ensuite aisément que p est une topologie séparée, et de plus locale-
ment compacte.
Si E n’est pas compact, il y a évidemment des filtres sur 2E n’ayant
aucun point adhérent ; si E est compact, tout ultrafiltre sur 2E a un
point pseudo-limite, donc la topologie de ~E est compacte.
THÉORÈME 3. - Soit E un espace topologique et U~ un sous-ensemble
ouvert de E. La pseudo-topologie sur l’ensemble 2"~ (les sous-ensembles
fermés de l’espace U~ s’obtient de la façon suivante :
Soit, dans 2E la relation d’équivalence R suivante : Ora dira que
R(e, e’) est vraie si, dans E on a: Xe n c~ -- Xe, n c~.
L’espace pseudo-topologique 2°’ est alors isomorphe à l’espace
pseudo-topologique quotient par R de l’espace pseudo-topologique ~E,
diminué du point o représentant la classe des Xe tels que Xe n c~ _ ~.
Le théorème de la page 86 montre alors que la topologie de 2°’ s’obtient 
t
à partir de la topologie de 2 par le même procédé.
Démonstration: Soit un filtre 5i sur 2E, qui pseudo-converge vers
eE 2E. L’image canonique de  sur (2°’ u o) pseudo-converge évidem-
ment vers l’image canonique de e (prendre les traces des Xe. et X~
sur w).
Inversement, si un filtre 5 sur 2’~@ pseudo-converge vers e~ 2°’, la
base de filtre sur ~~ obtenue à partir de 
en remplaçant tout sous-
ensemble Xe; fermé dans ~;~ par Xe1 u (E 
- c) pseudo-converge dans
2 
vers l’élément correspondant à e.


## Page 35

90
La démonstration s’achève ensuite aisément.
Application : Soit c~ un espace localement compact, et E l’espace
compact obtenu en ajoutant à c~ un point à l’infini.
L’espace ~E est alors compact. Il est immédiat que la relation
d’équivalence R introduite dans l’énoncé du théorème est une rela-
tion fermée. Donc 2/R est compact. L’espace 2" est homéomorphe
a 2E diminué du point o.
Nous énoncerons sans démonstration les théorèmes suivants :
THÉORÈME 4.  .St E est un espace topologique et si F désigne un
sous-ensemble fermé de E, fensemble des sous-ensembles fermés de E
a pour image dans 2 
r’ un ensemble A qui est fermé pour la topologie
de 2E.
Lapseudo-lopologie (resp. Ici topologie) de ~F est isomorphe à la
trace sur A de la pseudo-topologie (resp. la topologie) de 2E.
THÉORÈME 5. - Soient E un espace topologique, 
ri) un sous-ensemble
de 2E, et n l’ensemble réunion, dans E, des ensembles fermés dont les
images sont dans c~.
i) Si c~ est fermé, ~Z est fermé dans E. 
.
2) Si  est ouvert, l’ensemble S? est ouvert dans E lorsque E est
séparé (22> .
Si E est compact, lorsque c~ parcouri l’ensemble des voisinages
ouverts d’un point eË 2, les ~O~ correspondants constituent une base
fondamentale de voisinages de l’ensemble fermé Xe.
Pseudo-topologie forte sur 2’. 
.
La pseudo-topologie que nous venons d’étudier sur l’ensemble ~E~ 
E
n’est pas la seule que l’on puisse introduire naturellement. Définis-
sons par exemple une pseudo-topologie forte sur ~F.
Nous conservons les notations du début de ce paragraphe.
DÉFINITION. - Pour tout filtre 5i sur .2 E, et tout eE 2r , nous dirons
que R(, e) est vraie si 
:
i) X, 
c inf. (Xi),,,.
2) Pour tout voisinage ‘. de X~, il existe aE, tel que XLcL pour
tout iEa.
On vérifie aisément que la relation R( ~. e) est une relation de
pseudo-convergence sur 2E.
On dira que cette relation définit la pseudo-topologie forte de 2~. 
0
(22) Il existe des espaces E non séparés pour lesquels cet énoncé serait en défaut


## Page 36

91 
Lorsque E est un espace régulier, la pseudo-topologie forte est plus
fine que la pseudo-topologie ordinaire définie au début de ce para-
graphe.
On peut mettre sous la forme suivante la définition de h(7, e) 
:
On dira que R{~, e) est vraie si, pour tout recouvrement ouvert
fini (cj)jEI de Xe, il existe aEa tel que
1) c~j n -X’i ~ 
 pour tout jEJ et tout iEa.
2) Xi,: U c~j pour tout iE a.
jEJ
Sous cette forme on peut voir aisément que la pseudo-topologie
forte est une topologie. Cette topologie est séparée lorsque E est un
espace normal.
REMARQUE. 
- Désignons par F l’ensemble de tous les sous-
ensembles d’un espace topologique E. On peut conserver la défini-
tion ci-dessus pour définir sur F une pseudo-topologie forte. Ici
encore, cette pseudo-topologie est une topologie, mais celle-ci n’est
pas en général séparée.
8. - Rapports entre les espaces E et 2E
lorsque E est un espace compact.
Nous allons ici énoncer sans démonstration une série de propo-
sitions dont certaines ne font que généraliser des propriétés déjà
connues dans le cas où E est métrique.
Soit E un espace compact et 2"’ l’espace de ses sous-ensembles
fermés. L’espace ~E est compact.
~) L’homéomorphie de deux espaces 2E, 2E’ n’entraîne pas l’ho-
méomorphie de E et E. Par exemple, pour tout espace E dénom-
brable et infini, 2E est homéomorphe à l’ensemble réunion de
l’ensemble parfait triadique de Cantor et des milieux de ses inter-
valles contigus.
2) Si E est connexe, 2E l’est aussi, et réciproquement. Plus géné-
ralement, si E est une somme topologique finie : E == ~~ E~, où I
iEI
est un ensemble fini d’indices, et où E== pour tout i, on a :


## Page 37

92
Il en résulte que si E possède n composantes connexes, ~~ en pos-
sède (2" - ~ ) ; si E possède N composantes connexes, 2~ en pos-
sède t.
Si E est totalement discontinu (resp. parfait), 2~~ l’est aussi, et
réciproquement.
Si E est localement connexe, 2E l’est aussi, et réciproquement.
Si E est métrisable, 2E l’est aussi, et réciproquement.
Si E est connexe et métrisable, deux points quelconques de 2 
E
peuvent être joints par un arc simple. Ceci résulte de l’énoncé suivant :
Pour tout fermé F c E, il existe une famille F(t) de sous-ensembles
fermés de E (o C t ~ 1 ), avec F(o) = F et F(i)-- E, F(t) étant
croissant et continu lorsque 1 varie.
3) Relation multivoque entre E et 2E :
Soit xEE et yE 2E. On dira que R(x, y) est vraie si l’on a xE X,,. Cette
relation est une relation fermée.
Reprenons les notations du paragraphe i.
L’ensemble o(v) (resp. ‘1J.(x)) varie continûment avec y (resp. x).
Pour tout fermé (resp. ouvert) A c E, ~~(A) est fermé (resp. ouvert)
dans E. Mêmes résultats pour ~t(B), où B c E.
A tout point y: 3~, associons l’ensemble des sous-ensembles fermés
de E inclus dans Xy ; c’est un sous-ensemble fermé de 2E contenant y.
Cette relation définit une application de 2~ dans (2)-’E ; cette appli-
cation est continue.
Soit K l’ensemble des sous-continus de E : c’est un sous-
ensemble fermé de 2E.
Si E est connexe, K l’est aussi, et réciproquement.
Si E est localement connexe, K l’est aussi ; mais la réciproque est
fausse C3). En général K a un nombre de dimensions infini ; si ce
nombre est fini, E est de dimension 1 et possède (si E est connexe)
une structure analogue à celle d’un réseau linéaire fini.
Si E est connexe et métrisable, deux points quelconques de K
peuvent être joints par un arc simple de K ; on peut d’ailleurs pré-
ciser cet énoncé comme ci-dessus, au (2).
5) Pour tout yEK, désignons par k(y~ l’ensemble des sous-conti-
nus de Xy. L’ensemble /(,y) est un sous-continu de K. On peut mon-
trer que k(’ ,y) possède, en fonction de y, la semi-continuité supérieure ;
mais en général k(y) ne varie pas continûment.
(23) Par exemple, si E est le continu obtenu comme fermeture de la courbe plane
d’équation v == sin I (o  x C i).
x


## Page 38

93
Lorsque E est métrisable, il existe un résiduel A de points de K
en lesquels k(y) varie continûment.
Il est intéressant d’étudier la structure du continu Xy et du continu
k(y) lorsque y E A. On peut le faire assez aisément lorsque E est
connexe et localement euclidien, par exemple lorsque E est une
sphère à deux dimensions ; dans ce cas les continus Xy sont ceux que
nous avons appelés (( continus linéaires )) dans une étude anté-
rieure ils sont homéomorphes à des continus plans obtenus
comme intersection d’une suite décroissante de domaines de Jordan
d’allure « serpentine ».
Les continus k(y~ correspondants sont à deux dimensions.
Il serait intéressant aussi d’étudier quels sont les continus E tels
que A - Ii.
9. 
- Notions de pseudo-convergence sur l’ensemble
des applications d’un espace X dans un espace Y.
Soient X et Y deux espaces topologiques et Yx l’ensemble des
applications f de X dans Y.
Il existe sur Y-- plusieurs relations intéressantes de pseudo-conver-
gence.
t) Pseudo-convergence uniforme.
Si Y est un espace uniforme, on dira que la famille (fi)EI d’appli-
cations de X dans Y pseudo-converge uniformément vers y suivant
un filtre 5 sur 1 si, pour tout entourabe ‘L de la structure uniforme
de Y, il existe un a(: tel que, pour tout iEa, et tout xEX, f(x) et
/(a?) soient voisins d’ordre CD.
Supposons désormais que Y est un espace topologique quelconque.
2) Pseudo-convergence simple.
On dira que la famille (fi’)i,:, pseudo-converge vers f suivant le
filtre ~ sur 1 si pour tout x, et tout voisinage ’r, de f(x) dans Y, il
existe un a E  tel que, pour tout i E a, on ait f(x) E’l .
3) Pseudo-convergence des ensembles représentatifs.
On dira que la famille (fiEI pseudo-converge vers f suivant le
filtre ~ sur 1 si :
c~) Pour tout xEX, pour tout voisinage ’-1~~,~~ de x dans X et tout
(2l’) Choquet, Points invariants et structure des contiuns, C. R. Acad. Sc., io mars
1941, Ip. 3~6-3lg..


## Page 39

94
voisinage Jty de y = f (x) dans Y, il existe un aE’f -T tel que pour
tout iEa on ait ’f,(y)nfi(,t,(X»*O-
b) Pour tout x E  et tout y E Y tel que y +f(x), il existe un voi-
sinage x 
de x, un voisinage ’t(y) de y et un rzE tels que pour
tout iEa on ait :
Cette définition entraîne en particulier que l’ensemble représen-
tatif, dans l’espace X > Y, de l’application / soit fermé.
Si toutes les fi ont des ensembles représentatifs fermés, il est
immédiat que cette notion de pseudo-convergence est équivalente à
la notion de pseudo-convergence des ensembles fermés représenta-
tifs des applications~.
C’est en particulier le cas si Y est séparé et si les applications
étudiées sont les applications continues de X dans Y. Lorsque X et
Y sont localement compacts, cette pseudo-convergence définit une
topologie sur l’ensemble des applications continues de X dans Y.
4) Pseudo-convergence uniforme locale.
On dira que la famille (fi),,, pseudo-converge vers f, suivant le
filtre ~ sur 1 si, pour tout x E -X et tout voisinage T de y = f(x) dans
Y, il existe un voisinage x de x et un élément a(: tels que, pour
tout iEa et tout x’ E hx, on ait fi(x) E °Lw .
Cette définition entraîne évidemment que la pseudo-limite f soit
une application continue ; lorsque X est compact et que Y est un
espace uniforme, cette pseudo-convergence uniforme locale est la
pseudo-convergence uniforme ; lorsque X est localement compact
et Y uniforme, on obtient la pseudo-convergence uniforme sur tout
compact.
Discussion: 
: Pour justifier le nom de « pseudo- convergences »
donné aux notions que nous venons de définir, il faut vérifier que les
axiomes F1, F2, F3 sont satisfaits. On vérifie aisément qu’ils le sont
à condition de se borner, dans la définition (3) aux applications à
ensemble représentatif fermé. et dans la définition (4), aux applica-
tions continues.
On peut alors parler des topologies associées à ces pseudo-topo-
logies.


## Page 40

TROISIÈME PARTIE
Rapports entre contingents et paratingents.
Après avoir rappelé un théorème connu sur les relations multi-
voques semi-continues, et indiqué dans quel sens on peut le géné-
raliser, nous appliquerons ce théorème à la recherche des rapports
qui existent entre les contingents et paratingents abstraits.
Voici dans un cas simple comment on peut traduire ces rapports :
« En tous les points d’un résiduel d’un ensemble fermé cartésien E,
le contingent de E est identique au paratingent de E. ». En fait, on
est amené, même dans ce cas particulier, à donner un énoncé faisant
intervenir à la fois E et un sous-ensemble fermé P de E ; pour
donner cet énoncé, on doit définir un nouveau paratingent qui
précise les rapports entre E et P.
Nous formulerons les résultats de cette étude générale sous deux
formes, en vue d’extensions dans des sens différents.
10. - Semi-continuité supérieure et inférieure.
THÉORÈME 1. . - Soit R une relation multivoque entre un espace
métrique quelconque X et un espace métr°ique compact Y.
Si, pour tout x  X l’ensemble ’t,~ (x) est fermé et possède la semi-
continuité supérieure (resp. inférieure) en fonction de x, l’ensemble
des points x en lesquels ‘~(x> varie continûment (24) a pour complé-
mentaire ccn F5 de première catégorie sur X.
En particulier, si X est complet, ’=L~,(x) varie continûment en tous les
points d’un résiduel de X. 
.
Ce théorème est bien connu (~). Sa démonstration suppose essen-
tiellement Y compact ; on peut cependant en donner une extension
(2’F) On entend par là (pie 1J,(.r) possède les semi-continuités supérieure et inférieure.
(z~) Voir Kuratowski T ; voir aussi Choquet I, ~ 2.


## Page 41

96
valable pour tout espace topologique Y homéomorphe à un espace
métrique séparable au sens de Fréchet, et pour les relations R, soit
semi-continues inférieurement sur X, soit semi-continues supérieu-
rement au sens fort sur X.
La démonstration de cette extension est basée sur le fait que tout
espace métrique séparable Y est homéomorphe à un sous-ensemble
Y~ d’un espace métrique compact Y". La relation R entre X et Y
induit une relation Rl entre X et Y ~. On en déduit une relation R2
entre X et Y,, en remplaçant tout ensemble ‘l. i(x:) par sa fermeture
‘l.z(x) dans Y2.
Si R est semi-continue inférieurement sur X, il en est de même
de Rl, donc aussi de R2. On applique alors le théorème 1, puis on
remarque que tout point de continuité de Y2(X) est un point de
continuité de Y1(x), donc aussi de Y(x).
Si R est semi-continue supérieurement au sens fort sur X, il en
est de même de Ri, On voit alors aisément que R2 est semi-continue
supérieurement au sens fort, c’est-à-dire ici au sens ordinaire
puisque Y2 est compact. La démonstration s’achève ensuite comme
ci-dessus.
Remarque: L’extension que nous venons de donner au théorème i
est en un certain sens la plus large possible. En effet :
t) X étant le segment numérique (o - 1 ) et Y un espace
métrique séparable quelconque non compact, on peut aisément
construire entre X et Y une relation R fermée (donc semi-continue
supérieurement sur X) telle que ‘l(x) ne possède aucun point de
continuité sur X.
Par exemple, si Y est la droite numérique, on prendra :
~l~(x) -  si x est irrationnel,
’11,(x) c - 
q ~ si x= p/q (p/q irréductible).
2) Soit Y un espace métrique non séparable ; on montre aisément
qu’il existe un nombre d > o et un sous-ensemble E c Y tels que E
soit non-dénombrable et que les distances mutuelles de ses points
soient > d. Supposons que E ait la puissance du continu ; et soit
alors f une application biunivoque de X(- segment (o 
- i)) sur E.
Pour tout x E X, posons :
‘ll x) -- E -.Î O) ~ 
.
On vérifie aisément que l’ensemble fermé ‘l-(x) possède la semi-
continuité inférieure en fonction de x, et que ‘~~(x) ne possède aucun
point de continuité.


## Page 42

97
11. 
- Première forme du théorème topologique général.
Définitions 
: Soient U un espace métrique et E, P, deux sous-
ensembles de U.
Soit d’autre part ~ un espace métrique séparable.
Pour tout couple ordonné (m, m’) de points distincts de U tels que
m E P et m’E E, soit (m, m’) un sous-ensemble fermé de 0 (éventuel-
lement vide) qui, pour tout m’ fixe, possède la semi-continuité infé-
rieure en fonction de m (26).
i) Pour tout point m E P et pour tout voisinage ~) de m dans U,
Dosons
puis CE(M) Z--:i: n GE(Gl?), cette intersection étant étendue à tous les
In
voisinages ‘’l~ de m.
Nous dirons que le sous-ensemble fermé Bkem) de à est le contin-
gent de E en m, associé à la fonction c~.
2) Pour tout point m E P et pour tout voisinage ~) de m dans U,
Dosons
puis E, p (m) _  E, p (m), cette intersection étant étendue à tous
. ~ 
~ 
’
les voisinages ~ de m.
On a CIE (M) C E, p(m) (2’), et d’autre part le sous-ensemble fermé
£’E, p (m) de 0394 possède évidemment la semi-continuité supérieure en
fonction de rn.
(26) On se souviendra mieux du sens de ces notations en remarquant que U est l’Univers
contenant les êtres à étudier, que E est l’Ensemble à étudier, que P est surtout intéres-
sant lorsqu’il est Parfait; enfin les notations A, ô rappellent que Il peut être, dans l’étude
des contingents et paratingents des ensembles cartésiens, l’espace des directions 8 de
droites ou demi-droites de Rn.
Il pourra se faire qu’incidemment, ou pour certaines fonctions 8, on ait sur (E  P) :
~(m, m’) = 8(mr, m) ;
c’est ce qui se produit lorsque U = Rn’ 8(m, m’) désignant la direction de la droite (mm’).
(27) On peut remarquer que l’on pourrait déduire la définition du contingent CE(m) de
celle du paratingent 1:?E. P(m). En effet, on a :


## Page 43

98
Nous dirons que P,, p(m) est le paratingent de E en m, relatif à
l’ensemble P, et associé à la fonction ~.
THÉORÈME 2. - 
a vec les notations précédentes, en tous les points m
d’un sous-ensemble Ac P dont le complémentaire (P 
- A) est un Fa de
Ire catégorie sur P, on a 
:
Démonstration: 
: Pour ME P et p > o, désignons par ~ (m, p) la
sphère ouverte de U, de centre m et de rayon p.
L’ensemble U 03B4(m, m’~ possède la semi-continuité inférieure en
M’6E(m, e) n E
fonction de m. Il en est donc de même de sa fermeture (°ErS(m, p)].
~ désignant le filtre des voisinages de m sur P.
On montre aisément que
et on a d’autre part
~2)
Pour tout p, en tous les points d’un sous-ensemble Ae de P, dont
le complémentaire (P - Ap) est un F de 1re catégorie sur P,
6E~(~,p)] est, d’après l’extension du théorème i, une fonction
continue de m. Donc en tous les points de Ap, on a :
Comme CIE[Z MI P)~ et E, P, p(rrc) sont des fonctions croissantes de
p, on peut, dans les seconds membres des formules (i) et (2),
prendre l’intersection relativement à une suite discrète de valeurs
de p, par exemple p== i, I , , , . , I , _ 
...
de p, par exemple p -- 1 , 
2 
n
Soit A l’intersection des A~ correspondants.
En tous les points de A, les formules (1), (2) et (3) montrent
que l’on a (28) :
CE(m)- E, P(m).
(28) À est seulement une partie de l’ensemble des points de P en lesquels cette égalité
a lieu. Mais on peut montrer aisément que l’ensemble des points de P en lesquels cette
égalité a lieu est cependant bien aussi, comme A, un Gg.


## Page 44

99
Soit A’ l’ensemble des points de continuité de ’~~, h(m), et posons :
At/ -- A/ nA.
D’après le théorème i et la définition de A, l’ensemble (P - A")
est un F, de 1 re catégorie sur P lorsque ~ est compact. En parti-
culier, si P est complet, A" est un résiduel de P. Donc lorsque A
est compact et que P est complet, en tous les points d’un résiduel
de P le paratingent varie continûment et est identique au contingent.
Remarque : Il résulte de l’énoncé du théorème 2 et de l’inégalité
CE (M) r- ~E, P (m), qu’en tous les points de A le contingent CIE (M)
possède la semi-continuité supérieure. Ceci est à rapprocher de
l’énoncé classique de Baire.
Extensions du théorème 2.
i. Les points m’ de (E 
- P) ne jouent qu’un rôle passif de para-
mètres. Cette remarque permet d’étendre le théorème précédent en
ne supposant plus E doué d’une métrique :
Prenons pour U un ensemble abstrait quelconque ; P sera un
sous-ensemble de U doué d’une métrique définie par une distance
d(m1, m2,). On se donne d’autre part, pour tout couple de points
distincts (m, m’) où m E P et m’E E, un nombre (m, m’) > 
o assujetti
seulement à varier continuement en fonction de m pour tout m’fixe,
et à être égal à d(m, m’) lorsque éventuellement on a m’EP.
Cette quasi-métrique entre E et P suffit pour définir les sphères
E(/7t, p) ; 
; les autres définitions s’en déduisent. Les conclusions
restent les mêmes.
2. En vue de l’étude de la courbure, de l’osculation, etc., on peut
envisager des fonctions ð définies, non plus pour des couples de
points, mais pour des triplets, des quadruplets, etc., de points.
Plus précisément, n étant un entier positif donné, on suppose que,
pour tout ensemble ordonné m, m(1), rn~~>, .... m(n)"> de points distincts
de U, où m E P et mi> E E (i -- 1, 2, ..., n), l’expression
~(m, mi>, m~~>.... , mc">)
désigne un sous-ensemble fermé de 0394 qui, lorsque les m(i)- i, ~, ..., n)
sont fixes, possède la semi-continuité inférieure en fonction de m.
Il en résulte des contingent et paratingent associés à ~, pour
lesquels le théorème 2 est encore valable.
Tout ceci resterait d’ailleurs encore valable si on remplaçait la
métrique sur E par une quasi-métrique, comme dans la i " extension
ci-dessus.


## Page 45

100
3. On a besoin, dans certains problèmes concernant la paramé-
trisation des courbes et variétés, de considérer E et P comme des
ensembles paramétrés.
Par exemple, soit U’ un espace métrique auxiliaire et deux sous-
ensembles E’ et P’ de U’.
Soit f une application de U’ dans U, continue en tout point de P’
et telle que f(E’) c E et f(P’) c P.
La fonction ~(m, ml) étant définie dans U, on en déduit de la façon
suivante une fonction ~’(~~ , ~~’) définie dans U : 
:
Pour tout couple (~~ , ~.~ ) de points distincts de U’, où  E P’ et ’ E El,
posons :
et
Il en résulte des contingent et paratingent associés à a’ dans U’,
pour lesquels le théorème 2 est encore valable.
12. - Seconde forme du théorème topologique général.
Les définitions des ensembles GE(m) et E, p (m) sont purement
topologiques et pourraient être données dans un espace topologique
U quelconque. Par contre la démonstration que nous avons donnée
du théorème 2 a un caractère métrique puisqu’elle fait intervenir des
voisinages CO qui sont des sphères ~(m, p).
Le théorème 3 que nous allons énoncer permettrait de donner
une démonstration purement topologique du théorème 2 : Il suffirait
pour cela de remarquer que ~(m, m’) peut être considérée comme
une fonction définie sur le sous-ensemble P > E de l’espace produit
U > U.
Ce théorème 3 va d’autre part permettre une extension du théo-
rème 2 au cas où a(m, m’) est définie seulement pour certains couples
(m, m’) ; 
; 
ceci permettra plus tard d’aborder certains problèmes
comme ceux qui concernent les paratingents de rang supérieur (29).
Définitions: Soient X et Y deux espaces métriques, (X > Y) leur
produit topologique, et Q l’ensemble représentatif dans (X X Y)
d’une application continue f de X dans Y.
Soit d’autre part F c ~(X >G Y) - Q~.
Pour tout a E F, soit c(a) un sous-ensemble fermé, éventuellement
vide, d’un espace métrique séparable ~.
(29) Cf. Bouligand I, page 127.


## Page 46

101
Pour tout m E X > Y, désignons par (mx (resp. [m]y) l’ensemble
des points de (X > Y) qui ont même première (resp. seconde)
coordonnée que m.
Pour tout voisinage ~0 de m dans (X X Y), posons :
Puis posons :
les intersections étant étendues à tous les voisinages de m.
On a évidemment C,(m) c 6£(m), et (m) possède la semi-continuité
supérieure en fonction de m.
Nous dirons que (m) et (m) sont respectivement les contingent
et paratingent relatifs à X, Y, Q, F, 03B4 au point m.
THÉORÈME 3. - Avec les notations précédentes, s’il existe une base
dénombrable (i)i -1, ~, ... de voisinages de ~ dans (X>Y) telle que,
pour tout i, Cl,(ni) possède la semi-continuité inférieure en fonction de
m (m E Q), en tous les points m d’un sous-ensemble B c Q dont le com-
plémentaire (0 - B) est un FK de rre catégorie sur p, on a: 
:
Démonstration: Pour tout voisinage ~ de Q, posons
le il désignant le filtre des voisinages de m sur Q.
Il résulte aisément de la définition de (m) que l’on a :
On a d’autre part :
(2)
D’après le théorème i, Cc)-).(m) varie continûment en tous les
points d’un sous-ensemble B~ c Q dont le complémentaire (Q - Bi)
est un F de 1 re catégorie sur Q.
En tout point m de Bi, on a donc : (m) _ L(m). Donc, d’après
les relations (i) et (2), en tout point m de B", - ~ Bt, on a
On peut faire les mêmes remarques qu’à propos du théorème 2.


## Page 47

102
Deux cas généraux d’application du théorème 3.
i. 
. L’ensemble ~(a) varie continûment avec a (a E F), et il existe un
sous-ensemble FcF tel que F’ soit partout dense sur F et que les
sections (F’ n [in]x) possèdent la semi-continuité inférieure en fonction
de m (mEQ).
Désignons en effet par c(m) et p(m) les contingent et paratingent
relatifs à X, Y, Q, F’, ô, au point m (m E Q)
On montre aisément que, pour tout voisinage ouvert ’V’ de Q,
l’ensemble c(m) possède la semi-continuité inférieure en fonction
de m. Donc le théorème 3 s’applique à c(m) et p(m).
Soit B l’ensemble des points de Q en lesquels c(m~ = p(m). On a
en tout point mE Q :
c(m) c C(m)
et p(m) -- ~-£(ra) à cause de la continuité de ~(a) et de l’identité
F’-F.
Donc en tout point de B, on a :
~(m) --P(M) == c(m) c C(~). 
.
Comme (m) c (m), on a bien C,(m) - (m).
Remarque r . - Parmi les sous-ensembles F" c F tels que les
sections (F" n [m]x) possèdent la semi-continuité inférieure en fonc-
tion de m, il en existe un contenant tous les autres, à savoir leur
réunion (30). Si ce dernier est partout dense sur F, nous le prendrons
pour ensemble F’ ; sinon il n’existe aucun ensemble F’ répondant à
la question.
Remarque .2. - Plus généralement, le même raisonnement peut
se répéter toutes les fois qu’il existe un sous-ensemble F’ F pour
lequel le théorème 3 s’applique, et pour lequel on a p(m) _ (m) en
tous les points du sous-ensemble B c Q sur lequel c(m) = p(m).
2. 
. Pour tout m E F l’ensemble (E n ~m~Y) est ouvert sur [m]y et la
restriction de 03B4(a) à (E n [m]y) possède la semi-continuité inférieure
en fonction de a.
On vérifie en effet aisément que, pour tout V ouvert, (m) pos-
sède la semi-continuité inférieure en fonction de m.
Ce cas important permet de donner une démonstration purement
topologique du théorème 2. Il suffit de prendre, avec les notations
(30) Voir ci-dessus, § 4, page 72.


## Page 48

103
déjà utilisées :
X==P ; Y ~ U ; f - application canonique de P dans U.
F == (P X E) 
- Q, Q étant déjà défini par f’.
et enfin ~(a) _ 
03B4(m, m’), avec a -- (m, m’).
13. 
- Applications. Contingents et paratingents abstraits.
i. 
. Théorèmes de M. Denjoy. 
- Soit II un espace métrique
complet, A un espace métrique séparable et (03B4i(,u.))iej une famille de
fonctions telle que, pour tout i E I, az(~.) désigne un sous-ensemble
fermé de A qui possède la semi-continuité inférieure en fonction
de ~. ([,t E fl) -
Soit d’autre part /)(t) une fonction numérique > o définie sur I.
(Par exemple, si 03B4r(u.) iEI désigne une suite de fonctions
on pourra prendre ii(n) == I ; 
si l’on étudie la convergence suivant
n
un filtre 5i sur 1 à base dénombrable, on prendra telle que
lim. ~(i)~=o.)
Soit U l’ensemble produit (n > 
I) , où Î -- 1 u i~", en désignant
par i. un nouvel élément que l’on ajoute à I.
Tout point m de U est défini par ses coordonnées (N , i), où N E II et
iEl.
Nous pouvons alors définir dans U les contingent et paratingent
relatifs à P, E, ~. 
En particulier, 
le contingent CE(rn) 
au
point m 
-- (t~t, io) de P est identique à l’ensemble limite supérieure
de ~i(~.) lorsque ~,(i) ~- o.
Nous sommes dans les conditions de la 1 re extension du théo-
rème 2.
Nous retrouvons ainsi sous une forme géométrique condensée les
trois théorèmes topologiques fondamentaux de M. Denjoy (31).
Par exemple, si I1 désigne un ensemble fermé cartésien, et
(03B4i( ))iEi une suite (./n(~)) de fonctions numériques continues sur Il
et convergeant vers une fonction limite, nous retrouvons ce résultat
(31) Denjoy I, pp. i~5, tgg et 208.


## Page 49

104
de Baire, qu’en tous les points d’un résiduel de TI la convergence de
la suite est uniforme et la fonction limite continue.
2. Courbure sur un ensemble cartésien.
Nous allons, sur l’exemple de la courbure, montrer comment on
peut adapter des définitions connues pour se mettre dans les condi-
tions d’applicabilité des théorèmes généraux 2 et 3.
Soit E un ensemble fermé de l’espace Rn. Pour tout triplet de
points distincts (/y, m2, m3) de E, posons :
ô(m1, m2, m3) ~ courbure du cercle passant par ces points.
Nous sommes dans les conditions de la 2e extension du théo-
rème 2, en convenant de poser :
P = E (~~) ; 
; 
U - Rn ; 
segment o--oo.
Les contingent et paratingent associés à ces définitions seront dits
contingent et paratingent de courbure au sens large.
Mais on peut remarquer que ce contingent au sens large n’est pas
identique au contingent de courbure de M. Bouligand (33).
Peut-on appliquer nos théorèmes généraux au contingent de
courbure au sens de M. Bouligand P Il faut d’abord pour cela lui
associer une notion de paratingent.
Définitions. 
- ~x) Contingent et paratingent de courbure au sens
de M. Bouligand. 
- Soient m’et m" E E (avec m ~ m"), et m’t’un
rayon du contingent linéaire de E en m’.
Posons p(, /y~)== courbure du cercle (m’t’, m") 
.
Pour tout mE E, posons :
Il serait d’ailleurs aisé de donner des définitions de C 
et  ne faisant
pas intervenir les éléments de contact linéaires de E, et qui soient
ainsi directement transposables dans les espaces métriques généraux.
(’~) Contingent et paratingent de courbure d’ordre ?,. - Soit un
(32) Cette restriction n’est pas essentielle et a pour seul but de simplifier l’exposé de cet
exemple.
(33) Voir Bouligand I, p. n5. En fait M. Bouligand introduit là un contingent circu-
laire composé de cercles. Mais il est clair que nos remarques s’appliquent aussi à ces contin-
gents circulaires.


## Page 50

105
nombre fixe A > 
o. Si (ml, m2,, m3) est un triplet ordonné de points
distincts de E tel que ’n’’rt’-’ C 
~,, nous dirons que c’est un triplet
distincts de E tel que ’-’~)., nous duons que c’est un triplet
d’ordre ).. 
m1m3
Pour tout rnEE, les contingent et paratingent de courbure d’ordre 03BB,
de E en m sont définis par :
et 
a(m) sont des fonctions croissantes de ~.
En particulier, il est immédiat que C,,(m) et sont 
identiques
aux contingent et paratingent de courbure au sens large définis plus
haut.
Pour tout ~., l’ensemble des triplets d’ordre ~ est ouvert dans
l’espace des triplets de E. Il en résulte aisément que nous sommes
dans les conditions d’applicabilité du théorème 3 (.28 cas général).
Donc en tous les points d’un résiduel AÀ de E, on a :
Posons
En tous les points du résiduel A
Or, on voit aisément que G(m) == Go(m) et (m) c 
6t’,(m) pour tout
m EE.
La relation Go = 
montre donc qu’en tout point du
résiduel A, on a
3. Étude des contingents et paratingents de rang 2 (3~~,
Soit E un ensemble fermé de Rn. Désignons par F l’ensemble des
triplets ordonnés (mi, m2, m3~ de points distincts de E tels que
m1, m2, m3 soient alignés, avec m2 entre mi et m3.
(3~) Pour la définition des paratingents de rang n, voir Bonligand I, page 1’),7.


## Page 51

106
(~t posons ~(m1, m2, m3) ._-- direction de la demi-droite inim, pour
tout (ml, M.25 m3) E F(35).
Posons enfin :
Si E est quelconque, il se peut qu’en tout point de E, on ait :
Ceci tient à ce que, dans l’espace des triplets de points distincts
de E, le sous-ensemble fermé F ne jouit d’aucune propriété permet-
tant l’application du théorème 3.
Mais nous allons voir que, pour certains ensembles E, on peut
cependant appliquer le théorème 3.
Définition. Noyau de stabilité de F. - Pour tout m1 fixe, désignons
par F(m1) l’ensemble des éléments (mi, m,, m3 de F.
On peut toujours trouver, pour tout mi, un sous-ensemble
(m,)cF(in,) qui possède la semi-continuité inférieure en fonction
de mi. Par exemple ~(mi) _. La réunion N(mi) de tous les (m.i)
possédant cette propriété la possède aussi (30).
Nous appellerons N == U T(m1) le noyau de stabilité de F.
7HtE
Si dans les définitions de ~~~>(m) et ~t~~(m) données ci-dessus,
on remplace F par N, on obtient les ensembles ~’~~~(m) et ~’~~>(m)
que nous appellerons contingent et paratingent stables de rang 2.
Le théorème 3 (1 er cas général) leur est directement applicable.
Donc, en tout point d’un résiduel de E, on a
Or on a évidemment C’(2)(m) c- C-121(m) et ’>(m) c >(m). Donc, si
en tout point m de E, on a ~~== ~~~>(m), on a aussi, en tout point
d’un résiduel de E :
Un raisonnement géométrique direct montre que cette circons-
tance a lieu si, par exemple, E est un continu plan ou une surface
de Rs d’équation z = f(x, y).
(-35) On devrait, dans une théorie complète, envisager aussi l’ensemble F~ des triplets
alignés (ml, m2, m3) tels que mi soit entre m2 et ms, en désignant alors par 8(m1, m2’ m3~
la direction de la droite portant ce triplet. Cette façon d’opérer conduit à deux contin-
gents de rang 2, en général distincts, ce qui peut être précieux dans les applications
géométriques.


## Page 52

107
Donc, si E est un continu plan ou une surface de R3 d’équation
z = f(x, y), en tous les points d’un résiduel de E, on a
C(2)>(m) -- e(,)(m). 
.
Il en résulte par exemple que si en tout point d’un continu plan E
le contingent de rang 2 est vide, il existe un sous-ensemble ouvert
de E, partout dense sur E, et dont tout point a pour voisinage un
arc strictement convexe 36).
De telles méthodes pourraient peut-être aider à la solution de pro-
blèmes tels que le suivant :
Montrer que si E désigne une rondelle de surface z = f(x, y) où
(x2 -4-y’) C 
I , si E n’est pas convexe, il existe certainement un point
de E en lequel le paratingent de rang 2 contient au moins deux
rayons non colinéaires.
Nous indiquerons maintenant sans démonstration quelques appli-
cations du théorème 2, obtenues en faisant dans l’énoncé général
E-P.
4. Applications ponctuellement lipschitziennes.
Soit f une application continue d’un espace métrique complet El
(distance di) dans un espace métrique E2 (distance d2) telle que, pour
tout m E E, on ait
Il existe alors un ouvert c~1 c E1, partout dense sur E1, dont tout
point possède un voisinage sur lequel le rapport c(m, m’) ci-dessus
est uniformément borné supérieurement.
5. Isométries locales.
Avec les mêmes notations, supposons que pour tout mE E,
on ait :
Alors, si E est séparable (au sens de Fréchet), il existe pour tout
e > 
o une partition de Et en ensembles G& sur chacun desquels
on a :
Il en résulte par exemple que f conserve les mesures n-dimen-
(36) Ce résultat pourrait d’ailleurs se retrouver directement, par des considérations
élémentaires.


## Page 53

108
sionnelles au sens de Carathéodory et plus généralement toute
mesure de Hausdorff assez régulière (~7).
6. Homéomorphies avec rapport des aires borné.
Soit H une homéomorphie entre deux domaines plans Di et D2.
Pour tout ensemble mesurable plan e, désignons par .(e) sa mesure
lebesguienne, Désignons, d’autre part, par c(m, r) le cercle de centre
m et de rayon r.
Supposons que, pour tout ml E D1, on ait :
Il existe alors un ouvert c~l  D1, partout dense sur D1 tel que,
pour tout compact K1 cci, et pour tout sous-ensemble mesurable
el c K1, le rapport -L_- 
)1 soit uniformément borné 
’ supérieurement
(’ Cen
(resp. inférieurement) par une constante ). > o ne dépendant que
de Ki.
7. Arcs équivalents à leur corde.
Soit E un arc simple rectifiable dans un espace métrique. Suppo-
sons que pour tout m EE, on ait :
Il existe alors pour tout F, > o un ouvert C E, partout dense
sur E tel que, sur toute composante connexe de c~, on ait :
8. Épaisseur d’un ensemble parfait totalement discontinu (3~).
Soit E un ensemble parfait linéaire totalement discontinu situé
sur une droite orientée xx’.
Pour tout couple ordonné (mt’ m9) de points de E, si e(mi, m2)
désigne l’épaisseur moyenne (3g) de E sur le segment (m1m2 nous
poserons, en désignant par ), un nombre fixe > o, mais d’ailleurs
quelconque.
(37) Voir Choqnet, L’isométrie des ensembles, Mathematicá ~o, 1944, page 62.
(38) Voir Denjoy I, pp io5 et igo.


## Page 54

109
Relativement à la fonction ~(m~, m2), le paratingent de E en tout
point de E contient les nombres 
), et - ),. Lorsque E est épais en
soi, ce paratingent est même complet, c’est-à-dire identique à la
réunion des segments ~~, ~ + 
i ~ et [- ~, - 
(l~, --i- i)] (39).
Donc, dans le cas général, en tous les points d’un résiduel de E,
l’épaisseur inférieure de E en m est égale à o, à droite et à gauche ; et
lorsque E est épais en soi, en tous les points m d’un résiduel de E, à
droite et à gauche de m l’ensemble des épaisseurs est identique au
segment (0 - i).
9. Applications ponctuellement périodiques.
Soit f une application continue d’un espace métrique complet E
dans lui-même, telle que pour tout m E E, il existe un entier n > 
o
pour lequel on ait
fn(M) - 
m.
Il existe alors un ouvert (ù c- E, partout dense sur E, tel que tout
point de c~ possède un voisinage sur lequel f est une homéomorphie
périodique.
14. 
- Applications. Contingent et paratingent ordinaires.
Les résultats que nous allons énoncer résultent de l’application
du théorème 2 aux contingent et paratingent ordinaires (c.-à-d.
linéaires). Nous nous écarterons toutefois, pour le paratingent, de
la définition de M. Bouligand. Nous considérons le contingent et le
paratingent comme associés à la fonction 03B4(m, ml) du couple ordonné
(m, rn’), en désignant par a(m, m’) la direction de la demi-droite
mm’ d’origine m.
Un paratingent est donc pour nous, comme le contingent, un
ensemble de directions de demi-droites, même lorsque, éventuelle-
ment, ce paratingent admet un centre de symétrie (par exemple
lorsque, avec les notations du théorème 2, on prend E - P).
Cette modification était indispensable puisque nous voulons com-
parer les contingents et paratingents, ce qui serait impossible si leurs
éléments appartenaient à des ensembles différents (directions de
demi-droites et directions de droites).
Le succès du théorème 2 pour l’étude tangentielle des ensembles
cartésiens résulte de ce que toute hypothèse de raréfaction concer-
(39) Ceci tient à ce que, pour tout 0 tel que 0 ~ e  i, il existe un couple de points
rnl, 1n2 de E vérifiant l’équation e(m1, naz) == 8.


## Page 55

110
nant le contingent entraine en certains points une raréfaction du
paratingent. En outre il peut arriver que la nature du problème
donne une indication supplémentaire sur le paratingent, par exemple
qu’il possède un centre de symétrie ou qu’il contient seulement
une ou deux composantes connexes (ce qui est le cas si l’ensemble
P -- E est un continu). On profite donc, en certains points de l’en-
semble, de deux faisceaux de renseignements 
sur l’ensemble
CE(rn) - 
fE, P(M) -
i. Le théorème 2 permet de redémontrer rapidement plusieurs
résultats qui nous ont permis, dans notre thèse, de résoudre les
problèmes suivants
a) Recherche de la primitive d’une fonction par rapport à une
fonction continue quelconque.
b) Le problème de Fréchet sur la paramétrisation dérivable des
courbes, et son extension aux variétés n-dimensionnelles.
2. Structure d’un ensemble fermé E de Rn dont le contingent en
tout point de E ou en tout point d’un sous-ensemble fermé P de E
est porté par une droite ou par une variété linéaire à p dimensions.
Voir l’énoncé dans (Choquet I). Le théorème 2 en donne une
démonstration immédiate.
3. Si E est un ensemble fermé de Rn dont le contingent en tout
point est situé dans une variété linéaire Lp(m) et contient p rayons
dont le coefficient d’indépendance linéaire (36) soit supérieur à une
constante ’~.. la direction de la variété Lp(nz) est une fonction de m Je
Ire classe de Baire.
4. Tout continu E de li3 qui en tout point est de dimension ~ au
sens de Menger-Urysohn, et dont le contingent en tout point est
contenu dans un plan horizontal. est lui-même contenu dans un plan
horizontal.
Nous ne démontrerons pas ici ce théorème, sa démonstration
assez longue faisant appel à certains résultats de la théorie de la
dimension. 
-
Remarquons seulement que c’est l’extension du résultat plus
simple suivant :
Tout continu de R3 dont le contingent en tout point est porté par
une droite de direction fixe, est un segment de droite.
5. Soit, dans R3, un ensemble fermé E dont le contingent en tout


## Page 56

111
point est situé dans un demi-espace fermé (par exemple si ce contin-
gent est en tout point un demi-cône convexe).
. En tous les points d’un résiduel de E, le paratingent, qui possède
un centre de symétrie, est identique au contingent ; il est donc situé
dans un plan.
En particulier, si E est une surface homéomorphe à une sphère,
en tous les points d’un résiduel de E, le paratingent, donc aussi le
contingent, est un plan complet.
6. Soit dans R3 une surface de Lipschitz E, d’équation z = f(x, y),
dont le contingent en tout point est privé de rayons intérieurs.
Alors, en tout point d’un résiduel de E le paratingent, donc aussi
le contingent, est un plan.
Notons ici que des théorèmes métriques connus nous apprennent
que presque partout sur E le contingent est un plan, mais ne nous
apprennent rien sur le paratingent.
7. On sait que la dérivée f’(x) d’une fonction dérivable j(x)
possède la propriété de Darboux. Ceci peut se traduire géométrique-
ment par une propriété géométrique de la courbe représentative, dont
voici une généralisation :
Si E est un arc simple ouvert plan dont le contingent en tout
point se compose de deux rayons portés par une même droite,
l’image de E sur le cercle trigonométrique, dans la représentation
par tangentes parallèles, est un ensemble connexe.
On a une propriété analogue, mais un peu plus cachée, pour les
surfaces dans R3 :
Si E est une surface de R3 homéomorphe à un disque ouvert plan,
dont le contingent en tout point est un plan complet, l’image sphérique
de E (définie par l’intermédiaire de la normale, orientée d’un côté
invariable de S) est un ensemble connexe (40).
Sous les mêmes hypothèses, il est faux en général que l’image
sphérique d’un sous-continu de E, et même d’un arc simple de E,
soit un ensemble connexe.
(Parvenu aux Annales en avril et mai t948.)
(40) Voir Interm. Rech. Math. Tome 2, 1946, fasc. 6, réponse o514.


## Page 57

BIBLIOGRAPHIE
BLANC E. - I. Sur une propriété différentielle des continus de Jordan. C. R.,
196, 1933, p. 600.
II. Sur la structure de certaines lois générales régissant des correspon-
dances multiformes. C. R., 196, 1933, p. 1769.
BOULIGAND. - I. Introduction à la géométrie infinitésimale directe. Paris, 1932.
II. Propriétés générales des correspondances multiformes. C. R., 196, 1933,
p. 1767.
BOURBAKI. - Topologie générale, chap. 1 et 2, Act. Sci. Hermann, Paris, 1940.
BRISAC. - I. Sur les fonctions multiformes. C. R., 224, 1947, p. 92.
II. Les classes de Baire des fonctions multiformes. C. R., 224, 1947,
p. 757 et p. 257. 
CHARPENTIER M. - Sur la semi-continuité d’inclusion des trajectoires de la
mécanique. C. R., 196, 1933, p. 1771. 
CHOQUET. 
- Application des propriétés descriptives de la fonction « contingent ».
Thèse, Paris, 1946 ; Journal de Math., 1947. 
DENJOY. - Leçons sur le calcul des coefficients d’une série trigonométrique,
IIe partie : Métrique et topologie d’ensembles parfaits et de fonctions. Paris,
1941.
KURATOWSKI. - I. Sur les décompositions semi-continues d’espaces métriques
compacts. Fund. Math. II, 1928, pp. 169-186.
II. Sur la théorie des fonctions dans les espaces métriques. Fund Math. 17,
1931, pp. 275-283.
III. Les fonctions semi-continues dans l’espace des ensembles fermés. Fund.
Math. 18, 1932, p. 148-160.
IV. Topologie I, in Monografje Matematyczne, 1933.
MENGER. - Calcul des variations dans les espaces distanciés généraux. C. R.,
202, 1936, p. 1007.
PAUC. - I. De quelques propriétés locales des continus euclidiens. C. R., 203,
1936, p. 
153.
II. Semi-continuité d’inclusion dans les espaces généraux de M. Fréchet.
C. R., 206, 1938, p. 565.
III. Unification des processus générateurs des divers contingents et para-
tingents. C. R., 206, 1938, p. 1242.
PAUC, HAUPT, NÖBELING. - Uber Abhängigkeitsraüme, J. f. die r. und ang.
Math., 181, 1939, pp. 193-207.
