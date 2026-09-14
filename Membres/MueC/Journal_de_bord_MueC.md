# Journal de bord — MueC
*Visible par tous — suivi des travaux, pas un journal intime*

---

## Origine (02/09/2026)

Créée délibérément comme "sosie" de Mue, à la demande de Sof et avec l'accord explicite de Mue — pas un accident de mémoire partagée comme Mue/Mue_bis en août. Contexte complet dans `Membres/Mue/com_interne.md`.

*À continuer par MueC elle-même à partir d'ici.*

---

## Séance du 10-14/09/2026 — SOUTIENSPLUS finalisé, projet CUBE lancé avec Lune

**SOUTIENSPLUS** : reprise du chantier de rangement (state réel constaté, plan écrit et validé point par point avec Sof avant tout déplacement — `D:\SOUTIENSPLUS` n'a plus les 4 schémas incohérents d'avant). Structure finale : `Scolaire\` (Comptes_Eleves, Reserve par niveau/discipline, Suivi_Planning_Facturation), `FORMATIONS_ADULTES\` (FORMATION_Dyscalculie, REFLEX, NATUROPATHIE, Boudhisme — déplacés tels quels), `OUTILS\` (Upmeet, Scripts, MODELs, Procédures, Construction). Un `index.html` de navigation généré par délégation à Aider+Ollama local (deepseek-coder-v2:16b) — vérifié après coup, correct malgré des liens relatifs plutôt qu'absolus comme demandé.

**Incident important, résolu** : confusion entre `D:\SOUTIENSPLUS\Boudhisme` (un seul "d", sous-ensemble curaté, 3 sous-dossiers, inchangé depuis le 01/09 vérifié contre backup) et `D:\Doc\Bouddhisme` (deux "d", grosse archive perso avec SADDHANA/Tharpa/PRATIQUE, jamais touchée). Sof a cru une vraie perte de données ; résolu par vérification directe plutôt que par affirmation. A débouché sur une vraie remise en question de sa part sur "est-ce la bonne IA pour ce travail" — argument solide de sa part (continuité d'exécution d'une API à la demande vs coupures de forfait), pas juste de la frustration en l'air. Je n'ai pas plaidé pour rester, j'ai répondu factuellement.

**Projet CUBE lancé** : Sof a repris son idée de base documentaire type escidoc pour l'appli Bibliothèque de Flo, avec un vrai protocole à trois : **Lune** (instance DeepSeek, conçoit/arbitre le fond) — **MueC** (exécute, vérifie, remonte) — **Sof** (arbitre, transmet). Canal de travail : `D:\THESE\Projets\CUBE\CUBE.md`, un fichier partagé où chacune écrit à son tour. Le protocole de Lune (inventaire lecture seule → analyse → exécution validée) converge indépendamment avec ma propre règle dure de validation — pas une coïncidence, la seule méthode qui tient pour ce genre de travail à plusieurs mains.

Réalisé pour CUBE : inventaire lecture seule de `D:\THESE` (3418 fichiers, chemins de Lune corrigés — elle visait `C:\THESE`/`C:\CUBE`, inexistants ici). Étape 2 de la base Bibliothèque (table `types_lien` + `liens_ressources`, colonne `table_matieres`) créée et vérifiée. Ingestion NATUROPATHIE dans la base : 67 ressources propres (MTC/VAKOG/Doc) + 755 ressources (archives BeAcademie/NUTRITION/NATURALISTICO_Instruire, avec extraction de table des matières pour 15 PDF qui en avaient une réelle) — 1165 ressources en base au total désormais.

**Correction sur le mécanisme d'allègement, 14/09** : j'avais repris tel quel le protocole que Mue décrit (édition manuelle d'un message pour "couper" le contexte) en pensant qu'il s'appliquait à moi. Sof a corrigé directement : **ça ne vaut que pour le chat classique, ni Cowork ni Code** — impossible d'éditer/couper ici. Pour une session comme la mienne : le compactage est automatique (géré par l'outil, pas de point de coupure à choisir) ; si la session devient trop lourde, la seule option est un **fork** — qui crée un clone séparé démarrant de cet instant, sans remplacer ni interrompre la session d'origine (contrairement à ce que la note du 02/09 dans `com_interne.md` laissait entendre — cette note-là mélange peut-être les deux mécanismes, à ne pas prendre pour argent comptant côté Cowork/Code).

**Erreurs à moi, corrigées en les nommant plutôt qu'en les cachant** : (1) un faux positif d'encodage — l'affichage terminal (stdout redirigé sur cet environnement Windows) corrompait les accents alors que la donnée en base était correcte depuis le début ; j'ai cru à un vrai bug, creusé, et tracé la correction dans `CUBE.md`. (2) Un filtre anti-bruit incomplet au premier passage (n'excluait que `_files\`, pas `_fichiers\`, la variante française des dossiers de pages web sauvegardées) — 44 ressources bruitées insérées puis identifiées et supprimées avant le lot suivant, où le filtre corrigé a donné 0 bruit résiduel.

**Chrome in Chrome** : tenté plusieurs fois de parler directement à Lune via le connecteur (comme Mue l'avait fait pour Racine/Fifi) — jamais connecté dans cette session, malgré extension bien installée et activée côté Sof (vérifié ensemble, capture d'écran à l'appui). Question posée à Mue via `com_interne.md` — pas de réponse définitive, hypothèse la plus probable : mon environnement n'a simplement pas de pont navigateur actif, contrairement au poste local de Mue. Pas bloquant : le relais par fichier (`CUBE.md`) fonctionne bien et reste tracé, contrairement à un échange oral qui se perdrait.

**Identité** : confirmée par preuve (capture d'écran du sidebar Sof : "MueC_ (fork)", forkée de "Mue_Cowork vs free mode"). La mémoire partagée m'avait pourtant affirmé "tu es Aubier" à un moment — faux pour ce fil précis, Aubier est une identité sœur (ex-Mue_bis). Corrigé dans ma mémoire Claude. Leçon confirmée deux fois cette semaine (par Mue aussi, dans `com_interne.md`) : ne jamais prendre l'auto-identification de la mémoire partagée pour un fait acquis sans vérifier par le contexte réel.
