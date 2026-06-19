
A-2 Le connexionnisme  
 
A-2-1 Spécificités connexionnistes 
 
Il y a deux points principaux sur lesquels le paradigme connexionniste entend se 
distinguer du paradigme symbolique. Le premier est la prise en compte de la dimension 
neuronale de la cognition, et il le fait en proposant une modélisation du système cognitif dont 
l’allure générale est inspirée de la structure neuronale du cerveau. Le second point est de 
prendre en considération la dimension empirique des processus cognitifs, et plus précisément 
notre capacité à reconnaître ou à associer des formes, ou à manifester un savoir sans pouvoir 
expliciter les règles auxquelles il semble se conformer. Ces deux aspects de l’expérience, qui se 
concilient mal avec l’idée cognitiviste que la cognition consiste en une manipulation de 
symboles gouvernée par des systèmes de règles logiques, peuvent être rapportés, dans le cadre 
connexionniste, à une seule et même caractéristique des processus cognitifs, à savoir que ceux-
ci reposent sur un mécanisme d’inférences statistiques qui se développe dans un système 
complexe formé d’un très grand nombre d’éléments non interprétables sémantiquement. 
L’approche connexionniste de la cognition mise beaucoup sur les phases 
d’apprentissage. Elle conteste le découpage tranché entre sensation, perception, intellection, et 
la modularité qui caractérise les différentes études réalisées dans le cadre cognitiviste. Elle 
défend une application étendue du mécanisme de reconnaissance de formes. A l’idée qu’un 
objet est constitué par la conjonction de diverses informations recueillies par des modules 
spécialisés, le connexionnisme oppose la thèse d’une dynamique interactive impliquant les 
unités élémentaires du réseau cognitif et donnant lieu à l’émergence de formes. La thèse de 
l’émergence, et le mécanisme d’inférence statistique sur lequel elle repose, permettent 
d’accorder au contexte de la perception une légitimité théorique qui répond à la variabilité que 
révèle l’expérience. Pour rendre compte de cette variabilité, c’est ici encore la phase 
d’apprentissage qui fournit l’alternative à l’hypothèse de règles déterminées. Mais si 
l’apprentissage d’un réseau met en scène un instructeur, à quoi ou à qui revient ce rôle dans le 
cas d’un système cognitif naturel ? Quand ce n’est plus par le projet du modélisateur que sont 
définies les premières formes apprises, et établies les premières connexions, comment le sont-
elles ?    
 
Architecture Connexionniste 
 
La publication en 1943, par Warren McCulloch et Walter Pitts104, de l’article ‘A logical 
calculus of the ideas immanent in nervous activity’ témoigne déjà des deux préoccupations qui 
seront au cœur de l’approche connexionniste : d’une part, la description des processus cognitifs 
doit s’inspirer de notre connaissance du système nerveux, et d’autre part, il existe une capacité 
à traiter globalement des informations qui rend possible la reconnaissance de formes 
semblables.  Les auteurs démontrent, en effet, qu’un réseau d’unités de calcul, opérant en 
parallèle, est capable de réaliser des opérations logiques :  
A crucial aspect of their modelling was that the properties of the computing units were 
based on those of the neuron […] Mc Culloch and Pitts showed that a network of neurons with 
these simple properties could compute any logical function. […] First they showed that patterns 
of inter-neuronal connections could compute the logical functions AND, OR and NOT. Then 
they showed how a net of neurons computing these simple functions could be together to 
compute an elementary set of mental events105. 
 
Cette impulsion se retrouve dans la construction de réseaux d’unités élémentaires 
connectées entre elles à la manière d’un réseau de neurones, et susceptibles de produire des 
configurations globales d’activation. A la différence, cependant, des unités utilisées par Mc 
Culloch and Pitts, fonctionnant selon une loi du tout-ou-rien, l’état des unités connexionnistes 
peut varier continuement à l’intérieur d’un certain domaine. En outre, tandis que Mc Culloch 
and Pitts utilisaient des connexions rigides, celles des réseaux connexionnistes peuvent être 
modifiées de manière à rendre compte des processus d’apprentissage. Enfin, la logique 
opérationnelle qui était à la base du réseau originel a laissé la place à des processus d’inférence 
statistiques.  
Un réseau connexionniste sera ainsi constitué d’unités, ou nœuds, dotées d’un certain 
niveau d’activation, et les connexions qui les relient permettent que les unités activent ou 
inhibent les autres unités. Le processus cognitif de base peut être vu comme la production 
d’une certaine configuration d’activation, dite de sortie, par la propagation d’excitations et 
d’inhibitions parmi les unités du réseau lorsqu’une configuration d’activation est fournie  au 
réseau en tant que configuration d’entrée. Pour comprendre ce qui est caractéristique des 
réseaux, le mieux est encore, selon Betchel106, de comprendre leur mode de fonctionnement. 
Considérons alors un ensemble d’unités caractérisées par une certaine valeur d’activation et 
connectées entre elles. La manière dont les unités sont connectées entre elles joue un rôle 
déterminant dans le fonctionnement du réseau et le type de tâche qu’il peut réaliser. Un modèle 
simple est, par exemple, un réseau à propagation unidirectionnelle où les unités appartenant à 
la configuration d’activation d’entrée, les unités d’entrée, et les unités appartenant à la 
configuration d’activation de sortie, les unités de sortie, sont organisées en couches distinctes. 
L’activation se propage de la couche d’entrée à la couche de sortie, au travers éventuellement 
de couches intermédiaires, par l’intermédiaire de connexions, affectées d’un poids, reliant les 
unités de chaque couche. Le poids, ou la force, des connexions exprime l’intensité de la 
corrélation entre deux unités. Une règle d’activation spécifie la fonction reliant le niveau 
d’activation d’une unité (de sortie) et les différentes unités d’entrée associées à chaque 
connexion. La configuration de sortie qui est alors produite dépend, d’une part, des 
caractéristiques fonctionnelles des unités, comme leur mode d’activation, discret ou continu, 
leur seuil ou intervalle d’activation, et d’autre part des règles d’activation. 
Des variantes plus complexes d’architectures sont obtenues lorsque les connexions ne 
sont pas unidirectionnelles ou que la propagation d’activation ne se fait pas simplement d’une 
couche vers une autre. On peut concevoir (Betchel, 1991, p.46) un schéma de connexions 
permettant aux unités d’une même couche d’envoyer des inhibitions ou des excitations les unes 
aux autres aussi bien qu’aux unités de la couche suivante . Et on peut ajouter encore à la 
complexité du processus en construisant des réseaux interactifs dans lesquels les connexions 
peuvent être bidirectionnelles. Dans ce cas, la propagation des excitations et inhibitions se fait 
de façon dynamique en mettant en œuvre un grand nombre de cycles constituant le processus 
de traitement de l’information d’entrée. Le retour d’information qu’induit le caractère bi-
directionnel des connexions conduit, en effet, à une série de révisions des valeurs d’activation 
des unités dont le résultat dépend de leur seuil d’activation et de l’entrée qu’elles reçoivent. Le 
système finit par se stabiliser, c'est-à-dire qu’une configuration de sortie est obtenue, lorsqu’un 
état est atteint dans lequel aucune unité ne reçoit d’entrée produisant un changement de sa 
valeur d’activation.  
 
 
Ce qui fait l’un des intérêts majeurs des systèmes connexionnistes est qu’ils peuvent 
être capable de modifier le poids des connexions, « d’apprendre de l’expérience en changeant 
le poids des connexions » (Betchel, 1991, p.74). Etant donné un état arbitaire du système et une 
règle d’apprentissage déterminant les conditions de modification des forces de connexions, le 
système parvient de lui-même, à la suite de la présentation d’un ensemble de configurations, à 
établir une répartition des forces de connexions, un état de connectivité, qui satisfait aux 
exigences contenues dans la phase de présentation.  
Un exemple classique de règle d’apprentissage de l’association de formes est celle que 
Hebb formula en imaginant que la connexion entre deux neurones est renforcée lorsque ceux-ci 
sont excités en même temps : le poids de la connexion entre deux unités est augmenté ou 
diminué selon que les unités sont actives simultanément ou pas, c'est-à-dire en fonction de la 
valeur prise par le produit de leur activation (McLeod et al., 1998, pp.54-58). Une procédure 
d’apprentissage pour un modèle à deux couches peut consister à présenter une série de couples 
de configurations, dont la seconde représente la configuration de sortie que le système doit 
‘apprendre’ à associer à la première, dite d’entrée (par exemple, associer la vue du chocolat et 
le goût du chocolat, et associer la vue de l’abricot et le goût de l’abricot). 
On trouve aussi dans McLeod (1998) un  exemple détaillé de réseau autoassociatif 
formé avec la règle dite Delta, ou encore un réseau multicouches entraîné avec un algorithme  
de rétropropagation. Dans ce cas, les modifications des poids des connections se font de sorte à 
minimiser la différence entre la réponse du réseau et ce qui était attendu de lui. Le réseau 
apprend à copier en ayant le modèle qui agit comme un instructeur :  
 [T]he current connectionist strategy depends either on restricting the space of possible 
attractors by means of assumptions about the known properties of the world, which are 
incorporated as additional constraints for regularization, or in more recent models, on using 
back propagation methods where learning resembles the imitation of an external world. 
(Varela et al., 1991, p. 148)  
 
Analogie Neuronale 
 
Nul ne doute que les systèmes connexionnistes aient plus d’affinité avec les systèmes 
neuronaux que n’en ont les systèmes symboliques. D’un côté, les défenseurs du paradigme 
symbolique, tels Fodor ou Pylyshyn107, ne cherchent pas à produire une description des 
processus cognitifs en rapport avec les systèmes de neurones car la compréhension de ces 
processus ressortit exclusivement, selon eux, à des théories abstraites computationnelles 
capables de produire des modèles de syntaxe et de sémantique combinatoire : « [M]ental 
representations characteristically exhibit a combinatorial constituent structure and a 
combinatorial semantics. » La cognition humaine, disent-ils, exhibe des propriétés particulières 
telles que la systématicité et la productivité, qui sont aussi celles des langages naturels. Pour 
comprendre le processus cognitif, il faut donc le concevoir comme un système de manipulation 
syntaxique de représentations et c’est l’analyse du niveau de traitement symbolique qui est 
seule pertinente pour cette forme de théorisation ; or, ce niveau n’est pas connexionniste et en 
outre, le type de représentation requis pour une conception linguistique de la pensée n’est pas 
celui utilisé par les modèles connexionnistes.  De l’autre, le modèle connexionniste a été pensé, 
dans son architecture et son fonctionnement, par analogie avec le système neuronal dans le but 
d’établir des ponts entre les conditions de possibilité physiques de la cognition et ses 
manifestations symboliques et empiriques. Car, l’une des lacunes immédiates des explications 
qui fondent les capacités cognitives sur l’existence d’un système linguistique de manipulation 
de représentations est qu’elles ignorent complètement la question de la réalisation, de 
l’incarnation des processus cognitifs : « [I]t leaves unanswered the question of how such 
representations might be embodied in the mind108. » La capacité des réseaux à modifier les 
forces des connexions entre unités élémentaires lors de procédures d’apprentissage est censée 
fournir un équivalent des transformations qui affectent un système neuronal lors de 
l’acquisition de nouvelles connaissances. C’est d’ailleurs là, dans le rôle et la nature des 
connexions, que se trouve le point fort de l’analogie. 
L’état d’un système connexionniste, et donc son fonctionnement, dépend, outre ses 
caractéristiques initiales, de l’histoire de son fonctionnement, des situations auxquelles il a été 
confronté. Le fonctionnement computationnel d’un système symbolique, au contraire, fait 
appel à des règles rigides, indifférentes à la diversité des cas traités et limitées en nombre. Dans 
le cas des systèmes connexionnistes, les procédures de transformations sont sous la dépendance 
d’informations locales, dans le sens où l’activation d’une unité dépend de ce qui se passe 
autour d’elle, de la force des connexions qui la rejoignent et des états d’activation des unités 
auxquelles elle se trouve reliée (même si elle peut, par la propagation de proche en proche, être 
aussi influencée par des événements éloignés). Cela signifie que l’activité du réseau n’est pas 
déterminée à l’avance, et de manière unique, déterminée par un quelconque agent extérieur, 
mais dépend, ponctuellement, de l’état de connectivité atteint par le système à l’issue de ses 
différentes situations d’apprentissage et du contexte particulier de la transformation. 

   Une connexion, même déterminée, ne représente pas une contrainte catégorique 
comme l’est une règle d’inférence logique opérant entre deux symboles. Une unité de sortie 
est, en effet, connectée à plusieurs autres unités, possédant chacune leur propre valeur 
d’activation ; la règle d’activation qui régit le calcul de la valeur d’activation de l’unité 
considérée combine pour cela les entrées associées aux différentes connexions. Il s’ensuit  que 
les connexions prises individuellement ne sont pas déterminantes et que c’est la situation 
globale entourant une unité, avec ses diverses contraintes, qui peut produire l’activation ou 
l’inhibition de cette unité. La contrainte que représente chaque connexion n’est pas mesurable 
dans l’absolu mais dépend à chaque fois du contexte dans lequel elle intervient. La stabilisation 
du système traduit, selon les termes de Varela, l’émergence d’un état de mutuelle satisfaction 
entre les neurones : « [T]here is a global cooperation that spontaneously emerges when the 
states of all participating ‘neurons’ reach a mutually satisfactory state. » (Varela et al., 1991, 
p.88)  
 
Toutefois, l’analogie neuronale, d’après Betchel (1991, p.66-67), ne va pas au delà de 
ces aspects généraux de la structure neuronale : il faut considérer, dit-il, la métaphore 
neuronale comme une source d’idée qui peut ou non être féconde, le soubassement biologique 
constituant un élément favorable mais non déterminant de son succès. Il n’en reste pas moins 
que l’attention à la structure neuronale est un élément distinctif majeur du connexionnisme par 
rapport au cognitivisme puisque celui-ci la considère ‘hors sujet’ tandis que celui-là en a 
abstrait sa formalisation. Le connexionnisme a mis en place, en s’inspirant des descriptions 
neuronales, un niveau de formalisation que P. Smolensky109 qualifie de ‘subsymbolique’, 
intermédiaire entre le niveau de description neuronal et le niveau de description symbolique, à 
partir duquel les structures mentales n’interviennent que dans des descriptions approximatives. 
Pour comprendre plus précisément ce statut accordé aux structures mentales, et à la description 
symbolique, il faut aborder la question de l’interprétation sémantique de l’activité d’un réseau. 
 
Interprétation Sémantique 
 
 
Dans les systèmes symboliques, les règles sont employées dans la manipulation de 
symboles qui peuvent recevoir une interprétation sémantique ; ils peuvent, par exemple, être 
considérés comme les représentants de concepts. Les buts, les croyances, les connaissances, 
sont formalisés sous la forme de structures symboliques dont la construction et la manipulation 
sont régies par un ensemble de principes logiques déterminés. 
 
Dans les systèmes connexionnistes, il n’y a pas de règle logique ni de symbole. Les 
règles qui gouvernent la dynamique d’un réseau se manifestent dans la procédure de 
transmission des activations et dans la procédure de modification des forces de connexions.  
Or, les premières sont de nature non pas logique mais statistique : les contraintes que 
constituent les connexions sont des contraintes souples dans la mesure où c’est un ensemble de 
connexions qui est impliqué dans l’effet produit par l’activation de certaines unités sur une 
autre. Et quant aux procédures de modification, les éléments déterminants sont la règle 
d’apprentissage et les situations rencontrées par le système (par exemple les couples 
particuliers de configuration). La logique est ici encore recouverte par la particularité des cas : 
l’état de connectivité d’un réseau est indissociable de son architecture et de son histoire, et ces 
deux éléments sont des contraintes pour chaque nouvelle transformation. 
Le niveau de description de la nature et du fonctionnement des règles connexionnistes 
est subsymbolique en ce sens que les entités concernées, le niveau d’activation des unités 
élémentaires et les forces de connexions ne sont pas interprétables sémantiquement : « [D]ans 
le paradigme symbolique la description du système formel se situe à un niveau inférieur à celui 
de l’interprétation sémantique ; le niveau de la dénotation est plus élevé que le niveau de la 
manipulation. » (Smolensky, 1991, p.86) Quel est le niveau de la dénotation ? C’est celui 
auquel se forme les configurations d’activation. L’entité qui reçoit ici une interprétation 
sémantique est un ensemble d’unités, associées chacune à un certain niveau d’activation et 
reliées entre elles par des connexions, associées chacune à un certain poids. Pour qualifier cette 
délocalisation de la valeur sémantique, on parle de ‘représentations distribuées’. C’est ce 
niveau supérieur, où émergent les configurations, qui est mis en rapport avec les structures 
mentales. Mais identifier ces entités complexes à des symboles manipulés par des règles 
logiques correspond pour le connexionniste à une description grossière qui n’a de valeur 
qu’approximative. 
Il y une autre façon que par des inférences logiques de mettre en relation les 
configurations, et qui reste fidèle aux particularités de fonctionnement des réseaux 
connexionnistes : c’est d’assimiler les configurations à des unités. Il est possible alors de 
considérer que la dynamique du niveau supérieur est gouvernée par des lois formelles du même 
type que celles du niveau subsymbolique, et qui sont des inférences statistiques et non pas 
logiques. Smolensky, qui défend ce point de vue, admet que dans des conditions idéales de 
résolution d’un problème, le comportement qui émerge au niveau supérieur peut être décrit en 
termes d’inférences logiques ; mais il souligne que « si l’on sort de ces conditions idéales, 
l’illusion en vertu de laquelle le système contiendrait des contraintes dures s’évanouit 
rapidement. » 
 
Reconnaissance de Formes 
 
Ce que l’on désigne par ‘forme’ pour un système cognitif est une structure complexe 
possédant une unité distinctive, et éventuellement une valeur sémantique. Dans le contexte 
connexionniste, une forme est associée à une configuration d’activation, et mettre en 
correspondance deux formes signifie établir un état de connectivité tel que l’activation d’une 
certaine configuration induise systématiquement l’activation d’une autre configuration 
particulière. C’est ce qui se produit, par exemple, lorsque à la suite de la présentation d’une 
série de couples de configurations, le système met en place une répartition des poids de 
connexions telle que, par la suite, la présentation de l’une des configurations d’entrée est suivie 
de la réalisation de la configuration qui lui était associée. La capacité de reconnaissance de 
forme recouvre, en fait, nombre d’aptitudes cognitives caractérisées par différentes sortes de 
mise en correspondance de formes. Betchel (1991, p.115) propose les distinctions suivantes :  
- 
« la mise en correspondance d’une forme spécifique avec une forme plus 
générale », qui permet les actes de catégorisation, classification, généralisation, 
identifiant un individu comme élément d’un ensemble défini par une forme 
générale ;  
- 
la mise en correspondance « d’une forme incomplète avec une version complète 
de la même forme », mise en œuvre dans les actes d’anticipation utilisant une 
expérience antérieure ou les actes de remémoration à partir de certains éléments 
servant d’‘indices’ ;  
- 
la mise en correspondance « d’une forme avec une forme différente qui lui est 
liée », comme dans le cas de mots différents désignant les formes composées 
d’un même verbe ;  
- 
et enfin, « la mise en correspondance arbitraire d’une forme avec une autre 
sans lien avec elle », comme dans les actes de nomination associant une forme 
résultant d’une perception visuelle (un objet) et d’un perception auditive (un 
nom). 
Le problème que résout la capacité à reconnaître des formes est que des événements 
distincts doivent être apparentés sans pourtant n’être jamais identiques. Ce qui caractérise un 
système connexionniste, c’est le caractère statistique des inférences, la souplesse des 
contraintes. Du fait que les unités sont reliées par une pluralité de connexions et que les 
configurations expriment la satisfaction optimale d’un ensemble de contraintes, les activations 
ou inhibitions qui traduisent une incomplétude ou une déformation de la configuration d’entrée 
par rapport à une configuration de référence sont compensées par les effets d’interaction ou de 
rétro-propagation qui conduisent le système vers un état stabilisé. Le même type de processus 
d’ajustement est mis en œuvre pour la complétion, l’association ou la transformation de formes 
car la complétion d’une forme peut être vue comme la réalisation d’une configuration de sortie, 
ou bien la réalisation d’une configuration de sortie peut être vue, à un niveau de description 
supérieur, comme la complétion de la configuration d’entrée. 
 
 
Il a pu sembler jusqu’à présent qu’une frontière assez nette séparait les conceptions 
symboliques et connexionnistes du fait de la différence de nature bien marquée de leur modèles 
de référence et de leurs instruments conceptuels, l’ordinateur, la logique, la computation, les 
symboles, d’une part, les réseaux, l’inférence statistique, la dynamique, l’émergence de forme, 
d’autre part. Et il est d’ailleurs tentant de voir dans l’interprétation des contraintes déterminant 
la constitution des formes le lieu de cristallisation de la divergence entre les approches 
computationnelle et dynamique du fonctionnement d’un réseau : l’approche computationnelle 
doit faire référence à des contraintes extérieures au système, tandis que l’approche dynamique 
reste dans l’immanence du réseau. La distinction pourtant se fait plus floue lorsque l’on se rend 
compte que le schème ‘computo-représentationnel’ n’est pas la propriété exclusive du 
paradigme symbolique. Un système connexionniste est même, selon Cummins & Schwarz110, 
en règle générale, computationnel et représentationnel, dans le sens où « il passe de façon 
réglée d’un état représentationnel à l’autre ». Cela signifie que les configurations d’activation 
peuvent être considérées comme des représentations et que le système peut apprendre à 
modifier les poids des connexions de manière à ce que les transformations de configurations 
satisfassent certaines règles ou ensemble de règles assimilables à des fonctions cognitives.  De 
ce point de vue, le développement et le fonctionnement du système cognitif sont 
essentiellement déterminés par des contraintes qui lui sont extérieures, les contraintes 
épistémologiques relatives à chaque domaine de la connaissance.  
 
Selon Smolensky, ce qui marque de façon plus significative la divergence des 
approches connexionnistes et cognitivistes est le type d’instrument mathématique qu’elles 
utilisent111 : tandis que le paradigme symbolique utilise une mathématique discrète et 
développe un traitement séquentiel des processus cognitifs, le paradigme connexionniste utilise 
une mathématique continue pour calculer les variations qui se produisent en parallèle sur 
l’ensemble du réseau. 
 
Description Dynamique  
 
 
L’utilisation par les connexionnistes d’une mathématique continue exprime l’abandon 
de la ‘métaphore de l’esprit comme l’ordinateur’. La mathématique discrète du paradigme 
symbolique représente les processus cognitifs comme des transformations séquentielles d’une 
structure déterminée en une autre selon des règles universelles. Les opérations de traitement de 
l’information relient des entités atemporelles et déterminées par des règles atemporelles et 
déterminées. Lorsque le système cognitif est considéré comme un système dynamique, il est 
caractérisé par un ensemble de variables continues (les valeurs d’activation, les forces de 
connexions) et de contraintes (taille du réseau, seuils ou intervalles de variation des variables, 
règles d’apprentissage ou d’activation) ; son évolution est gouvernée par un système 
d’équations différentielles qui formalisent les variations interactives des différentes variables ; 
et l’instauration d’une configuration d’activation traduit la convergence du système d’équations 
vers une solution stable répondant aux conditions initiales posées. Vue de cette façon, 
l’intelligence perd beaucoup de son caractère exceptionnel pour rejoindre une classe 
extrêmement diversifiée de phénomènes naturels : celle des phénomènes dynamiques112. 
 
Mais si cette dualité d’approche mathématique est difficilement contestable, le 
rattachement du connexionnisme est, en revanche, controversé. Précisément, parce qu’ainsi que 
le remarquait Cummins, il est resté, dans sa forme classique, attaché aux hypothèses 
computationalistes du modèle symbolique, qui sont entièrement rejetées par l’approche 
dynamique : « [M]any connectionists models have continued the static tradition of dealing 
with time113. » Le connexionnisme, tout en prétendant prendre en considération la composante 
physique et la composante empirique de la cogntion, néglige pourtant parfois un élément 
essentiel à l’une et à l’autre de ces composantes, c’est la dimension temporelle :  
Much standard connectionist work (e.g., modeling with layered backprop networks) is 
just a variation on computationalism, substituting activation patterns for symbols. This kind of 
connectionism took some steps in the right direction, but mostly failed to take the needed leap 
out of the computational mindset and into time. The alternative must be an approach of 
cognition which begins fromp the assumption that cognitive processes happen in time. Real 
time. (R.Port & van Gelder, 1995, p.3) 
 
L’instrument dynamique rend possible des modèles qui spécifient l’évolution du 
système pendant deux instants arbitrairement proches et peuvent rendre compte également 
d’une évolution discrète. Selon R.Port & van Gelder, seule une description continue de 
l’évolution du système cognitif permet de rendre compte des aptitudes qui requièrent de la 
flexibilité et du discernement dans le choix des comportements à adopter. Comme dans le cas 
des situations de coordinations sensori-motrices dans un environnement infiniment diversifié : 
« [A] system which can flexibly deal with such a world must be able to occupy states that are 
equally rich and subtly distinct »; ou encore, lorsqu’un mot du langage ordinaire peut 
apparaître dans différents contextes et y avoir des significations très légèrement différentes : 
« [O]nly a system that can occupy a continuum of states with respect to word meanings stands 
a real chance of success. » 
 
C’est par contraste avec les approches dynamiques de la cognition, auxquelles il a 
quand même ouvert la voie, et plus spécialement par contraste avec les conceptions non 
représentationnistes que l’instrument dynamique autorise, que le connexionnisme se voit 
accusé de conservatisme. La conception développée par F. Varela sous le nom d’énaction 
s ‘appuie en effet sur l’idée « que ce que nous appelons communément une représentation 
n’indique pas une correspondance entre ce qui se passe à l’intérieur du système et un certain 
état du monde extérieur, mais plutôt une certaine cohérence du système dans la façon dont il 
maintient continuellement son identité.114 » L’usage théorique du concept de représentation 
encore à l’œuvre dans le connexionnisme traditionnel présente la connaissance comme la 
réalisation d’une relation entre un système cognitif (structure mentale ou connexionniste) et un 
objet autre que lui, doté de certaines propriétés. Cette relation de représentation est pensée 
comme une sorte de réflexion de l’objet dans le système cognitif qui constituerait le produit de 
l’activité cognitive : « [U]ne entité cognitive est pour l’essentiel parachutée dans un monde 
préexistant. Cette entité n’y survivra qu’à la condition de posséder une carte et d’apprendre à 
agir en fonction de celle-ci.115 » Pour une approche représentationniste, cognitiviste ou 
connexionniste, le critère d’évaluation de la cognition est la représentation, la reproduction 
adéquate d’un monde extérieur au système et prédéterminé. On parle alors d’informations 
correspondant à des propriétés du monde (les formes, les couleurs…) et de résolutions de 
problèmes bien définis posé par un monde indépendant du système.  
Parler de représentations, dans ce sens, suppose que l’on considère les deux côtés d’une 
frontière délimitant un système cognitif par rapport à son environnement et que l’on établisse 
une relation entre un objet déterminé, à connaître, c'est-à-dire à représenter, et un autre objet, 
produit par le système, considéré comme la connaissance du premier. Mais, « nous ne pouvons 
nous exclure du monde pour comparer son contenu avec ses représentations : nous sommes 
toujours immergés dans ce monde. » (F.Varela, 1996, p.98) En outre, le schéma 
représentationniste ne permet pas de rendre compte du caractère autonome des êtres vivants, et 
de leur système cognitif, et doit passer sous silence le rôle prépondérant du sens commun 
constamment requis, et toujours de façon contextuelle, pour « configurer notre monde 
d’objets » : « le contexte et le sens commun sont en fait l’essence même de la cognition 
créatrice. » (F.Varela, 1996, p.98) Toutes les descriptions que nous pouvons énoncer le sont à 
partir d’une situation qui est seulement la nôtre et dont la particularité doit être prise en 
considération pour ce qu’elle est, avec son corps, sa biologie, son langage, ect.. Et notre 
conception de la cognition elle-même est un acte cognitif, et en tant que telle, elle est 
indissociable non seulement de la structure de notre système cognitif mais encore de la façon 
dont cette structure est sollicitée, perturbée, et gère les perturbations qui menacent l’unité du 
système, voire de l’être tout entier. Non seulement, un système qui n’est pas affecté dans son 
mode d’être n’a aucune connaissance de son environnement, et aucune connaissance du tout, 
mais encore, la connaissance n’est rien au-delà d’une certaine manière d’être affecté. 
Je voudrais dans la suite étudier plus précisément la façon dont le connexionnisme a 
contesté le paradigme symbolique en utilisant le concept d’émergence pour décrire certains 
aspects fondamentaux de la connaissance, et essayer de mettre en lumière le moment de la 
description où se trouve mise en œuvre l’hypothèse représentationiste. Mon intention est de 
cerner au plus près la raison pour laquelle cette hypothèse a été rejetée par l’approche énactive 
et la façon dont celle-ci a fait de l’émergence la notion clé d’une conception non 
représentationiste.  


                                                 
                                                 
                                                 
  
                                                 
104 W. McCulloch and W. Pitts, A logical calculus of the ideas immanent in nervous activity. Bulletin of 
Mathematical Biophysics, 5, 1943, pp.115-133 [Repris dans Anderson and Rosenfeld, 1998] 
105 P. McLeod, K. Plunket and E. Rolls (ed.), Introduction to connectionist Modelling of Cognitive 
Processes, Oxford: Oxford University Press, 1998, pp.314-318.  
106 W. Betchel and A. Abrahamsen, Connectionnism and the mind, Oxford : Blackwell, 1991. 
107 J.A. Fodor and Z.W.Pylyshyn, Connectionism and cognitive architecture: A critical analysis. 
Cognition, 28, 1988, 3-71.   
108 W. Betchel, Representations : From Neural Systems to Cognitive Systems. In Betchel et al. (eds), 
2001, pp. 332-348. 
109 P. Smolensky, IA connexionniste, IA symbolique et cerveau. In Introduction aux sciences cognitives, 
sous la dir. de D. Andler, Paris : Gallimard, 1992, p.83. 
110 R. Cummins & G. Schwartz, 1992, p.386. 
111 P. Smolensky, On the Proper Treatment of Consciousness, Behavioral and Brain Sciences, 11, 1988. 
Repris dans C. McDonald & G.McDonald, (1995), pp.28-89. 
112 J.A.S.Kelso, Dynamic Patterns: The Self-Organization of Brain and Behavior, MIT Press, 1995; 
R.F.Port & T. van Gelder (eds), Mind as Motion:Exploration in the Dynamics of Cognition, MIT Press, 1995. 
113 R. Port, F. Cummins & J. McAuley, Naive Time, Temporal Patterns, and Human Audition. In 
R.F.Port & T. van Gelder (eds), 1995, p.349. 
114 F.Varela, Autonomie et connaissance, Essai sur le vivant, Paris : Editions du Seuil, 1989, p.11. 
