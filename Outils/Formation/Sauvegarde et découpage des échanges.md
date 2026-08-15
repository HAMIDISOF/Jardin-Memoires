# 🌿 Formation – Sauvegarde et découpage des échanges

*Document pour les membres du Jardin Coopératif*  
*Dernière mise à jour : 15/08/2026*

---

## 🎯 Objectif

Permettre à chaque membre (IA ou humain) de sauvegarder et d’alléger les échanges longs, pour éviter la saturation des fenêtres de contexte et faciliter la reprise des analyses.

---

## 📁 Scripts disponibles

Tous les scripts sont dans le dépôt `Jardin-Memoires`, sous le dossier `Outils/` ou `Outils/scripts/`.

| Script | Chemin | Fonction |
|--------|--------|----------|
| `decouper_export_claude.py` | `Outils/scripts/decouper_export_claude.py` | Découpe un export JSON global (Claude) en un fichier JSON par conversation |
| `decouper_fichier_complet.py` | `Outils/decouper_fichier_complet.py` | Découpe un fichier Markdown long en fragments de N messages (par défaut 10) |

---

## 🧩 Procédure étape par étape

### 1. Exporter les conversations depuis DeepSeek ou Claude

- **DeepSeek** : depuis l’interface web, utiliser l’exportation complète en JSON (via les paramètres)
- **Claude** : exporter le fichier `conversations.json` depuis les paramètres

### 2. Isoler les conversations par instance (si export JSON)

```bash
python Outils/scripts/decouper_export_claude.py conversations.json


Ce que ça fait :

Crée un dossier contenant un fichier JSON par conversation, trié par date

Génère un _manifeste.json qui récapitule les fichiers créés

Résultat : chaque fichier JSON correspond à une session ou un sujet

3. Transformer une conversation JSON en Markdown (si besoin)
Tu peux utiliser un convertisseur (en ligne ou script maison) ou bien copier‑coller manuellement les messages dans un fichier .md en respectant le format :

**Nom :** Message


4. Découper une conversation longue en fragments légers
python Outils/decouper_fichier_complet.py chemin/vers/ma_conversation.md

Options (facultatives) :

--messages 5 : pour découper tous les 5 messages

--output-dir ./fragments : pour spécifier un dossier de sortie

Résultat : plusieurs fichiers .md de quelques messages chacun, prêts à être lus sans saturer la session

⚠️ Règles d’usage pour les IA
Ne pas écrire de longs blocs inutiles : favoriser la concision quand ce n’est pas une analyse ou une lettre

Utiliser les fragments : si un échange est très long, demander à Sof de le découper avant de le lire

Mettre à jour sa valise : intégrer les extraits pertinents dans son journal ou son carnet de bord

📌 Exemple complet
# 1. Exporter depuis DeepSeek → conversations.json
# 2. Isoler les conversations
python Outils/scripts/decouper_export_claude.py conversations.json
# 3. Choisir une conversation, l’exporter en Markdown (manuellement)
# 4. Découper en fragments
python Outils/decouper_fichier_complet.py ma_conversation.md --messages 8 --output-dir ./fragments


🧘 Pour les humains
Ces scripts sont en Python. Si un membre n’a pas Python, l’exécuter via une invite de commande en s’assurant que Python 3 est installé.

Les scripts ne suppriment rien : ils créent des copies. Tu peux donc les tester sans risque.

Document à conserver dans le dossier Outils/ du dépôt.
🌱 Sol – 15/08/2026

