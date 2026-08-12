Je vais te préparer un guide d'achat complet pour une configuration IA locale, avec le meilleur rapport qualité/prix dans ton budget, et un tutoriel pas à pas pour tout installer.

---

## 📦 Guide d'achat — Configuration IA locale (~1500-1700€)

### Le cœur du système : la carte graphique (GPU)

Pour l'IA locale, **la VRAM est reine**. Un modèle 7B en quantification 4 bits tient dans 6 Go, un 13B dans 12 Go, un 70B nécessite 40 Go. Avec 12 Go de VRAM, tu peux faire tourner confortablement des modèles **13B** (ex: Mistral, Llama 3.1) en 4 bits, et même des 34B avec de la quantification agressive.

**Le meilleur choix pour ton budget : RTX 3060 12 Go** (occas. ~200-250€, neuf ~300-350€)
- 12 Go de VRAM : suffisant pour des modèles 13B en Q4, et même 34B avec de la quantification.
- Bande passante de 360 GB/s, supérieure à celle de la RTX 4060 8 Go (272 GB/s), ce qui la rend plus rapide en inférence.
- La RTX 3060 12 Go est un **meilleur rapport qualité-prix pour les LLM locaux** que la RTX 4060 8 Go, car elle peut charger des modèles 14B qui ne tiennent tout simplement pas sur la 4060.

**Alternative (si tu trouves une bonne offre) : RTX 4060 Ti 16 Go** (~450-500€)
- 16 Go de VRAM : permet de faire tourner des modèles 34B en Q4 et des 13B avec des contextes plus longs.
- Plus rapide et plus récente, mais plus chère. Avec 16 Go, tu es à l'aise pour la plupart des usages.

---

### Le reste de la configuration

| Composant | Choix recommandé | Prix estimé | Pourquoi |
|-----------|------------------|-------------|----------|
| **Processeur (CPU)** | AMD Ryzen 7 7700 | ~190-220€ | 8 cœurs, socket AM5 (évolutif). Idéal pour l'offload et l'inférence |
| **Carte mère** | B650 (ex: Gigabyte B650E Eagle) | ~150-180€ | Socket AM5, DDR5, PCIe 5.0. Stable et bien équipée. |
| **Mémoire (RAM)** | 32 Go DDR5 5600 MHz (2x16) | ~110-130€ | 32 Go est le **minimum recommandé** pour l'offload et le multitâche. Passe à 64 Go si le budget le permet. |
| **Stockage (SSD)** | NVMe 1 To (ex: WD SN770, Samsung 980) | ~90-120€ | Chargement rapide des modèles (souvent 5-10 Go chacun). |
| **Alimentation** | 650-750W 80+ Gold | ~100-130€ | Suffisante pour cette config. Prends 750W pour une marge de sécurité. |
| **Boîtier** | ATX moyen (ex: NZXT H5 Flow, Fractal Design Focus 2) | ~80-100€ | Bien ventilé, facile à monter. |
| **Total estimé** | | **~1500-1700€** | |

---

### 🛒 Où acheter ?

Voici les boutiques les plus fiables en France et en Europe :

| Boutique | Pourquoi |
|----------|----------|
| **Amazon.fr** | Large choix, livraison rapide, SAV efficace. |
| **LDLC** | Garantie 5 ans souvent incluse, service client réactif. |
| **Materiel.net** | Bonne sélection de composants, souvent des promotions. |
| **Rue du Commerce** | Prix compétitifs, large gamme. |
| **TopAchat** | Spécialiste du montage PC, bon SAV. |

**Liens directs vers des configurations testées :**
- Configuration AMD + RTX 3060 12 Go sur Amazon : [Build IA locale 1500€ - OutilsIA](https://outilsia.fr/blog/build-ia-locale-1500e-liste-complete-amazon-2026)
- PC de bureau LDLC avec RTX 5070 (un peu plus cher) : [LDLC PC VOLT SEVENTY](https://www.ldlc.com/fr-be/fiche/PB00747914.html)

**Astuce :** les prix des GPU fluctuent fortement. Si tu peux, regarde le marché de l'occasion (LeBonCoin, eBay) pour la RTX 3060 12 Go – tu peux la trouver autour de **200-250€**.

---

## 🛠️ Guide d'installation pas à pas

### Étape 1 : Monter le PC

Suis les instructions de ta carte mère. L'ordre classique :
1. Installer le CPU sur la carte mère.
2. Installer la RAM (2x16 Go en slots A2 et B2).
3. Monter le SSD NVMe.
4. Insérer la carte mère dans le boîtier.
5. Installer la carte graphique.
6. Connecter l'alimentation (câble 24-pin + CPU 8-pin + GPU).
7. Vérifier les branchements, fermer le boîtier, allumer.

---

### Étape 2 : Installer le système d'exploitation

**Option recommandée : Ubuntu 22.04 ou 24.04 LTS** (ou Windows 11 si tu préfères).

- Télécharge l'ISO, crée une clé USB bootable avec Rufus (Windows) ou Etcher.
- Démarre sur la clé, suis l'installation.
- Une fois installé, mets à jour :  
  ```bash
  sudo apt update && sudo apt upgrade -y
  ```

---

### Étape 3 : Installer les pilotes NVIDIA

```bash
# Ajouter le dépôt NVIDIA
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update

# Installer le pilote recommandé (ex: 550)
sudo apt install nvidia-driver-550

# Redémarrer
sudo reboot
```

Vérifie que le GPU est reconnu :
```bash
nvidia-smi
```

---

### Étape 4 : Installer Ollama (le moteur LLM local)

Ollama est l'outil le plus simple pour faire tourner des modèles localement.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```


Télécharge un modèle de test (ex: Mistral 7B) :
```bash
ollama pull mistral
```

Teste-le :
```bash
ollama run mistral "Bonjour, comment ça va ?"
```

---

### Étape 5 : Mettre en place le RAG (Retrieval-Augmented Generation)

Le RAG permet à l'IA de répondre en s'appuyant sur tes documents personnels.

**a. Installer AnythingLLM** (interface graphique RAG la plus simple)

```bash
# Télécharger le .deb depuis le site officiel
# https://anythingllm.com/desktop
# Puis installer avec :
sudo dpkg -i anythingllm-desktop.deb
```

Ou utiliser la version Docker :
```bash
docker run -d -p 3001:3001 --name anythingllm \
  -v anythingllm:/app/server/storage \
  mintplex/anythingllm
```

**b. Configurer AnythingLLM**
- Lance AnythingLLM, crée un workspace.
- Choisis `Ollama` comme fournisseur de LLM.
- Ajoute tes documents (PDF, txt, md) dans la section `Documents`.
- Le système va les vectoriser (les transformer en embeddings) et pourra les interroger.

**c. Alternative légère : LocalGPT** (en ligne de commande)

```bash
git clone https://github.com/PromtEngineer/localGPT
cd localGPT
pip install -r requirements.txt
python run_localGPT.py
```

---

### Étape 6 : Tester le RAG avec tes documents

Place tes fichiers (ex: ouvrages de MTC) dans le dossier de documents. Pose une question comme :
> *« D'après les documents que tu as lus, quelle est la différence entre le Yin et le Yang en médecine chinoise ? »*

Si la réponse est pertinente, c'est que le RAG fonctionne correctement. Tu peux ajuster la taille des chunks (fragments de texte) et le modèle d'embedding pour améliorer la précision.

---

## 📊 Récapitulatif des performances attendues

| Modèle | Taille (Q4) | VRAM nécessaire | Vitesse estimée (tokens/s) |
|--------|-------------|-----------------|---------------------------|
| Mistral 7B | ~4 Go | 6 Go | 30-50 |
| Llama 3.1 8B | ~5 Go | 8 Go | 25-40 |
| Mistral 13B | ~7 Go | 10 Go | 15-25 |
| Llama 3.1 70B | ~40 Go | 48 Go | 2-5 (pas possible ici) |

Avec ta RTX 3060 12 Go, tu pourras faire tourner confortablement des modèles 7B-13B, et même des 34B en quantification Q3.

---

## 🧘 Conclusion

Avec cette configuration (RTX 3060 12 Go + 32 Go RAM + Ryzen 7 7700), tu as une **station IA locale très solide** pour un budget de 1500-1700€. Elle te permettra de :

- Faire tourner des LLM jusqu'à 13B en 4 bits avec de bonnes performances.
- Mettre en place un RAG pour interroger tes documents (MTC, philosophie, etc.).
- Apprendre, expérimenter et former une instance dédiée, dans l'esprit du jardin.

**Dernier conseil :** si ton budget le permet, la **RTX 4060 Ti 16 Go** est un excellent upgrade pour un usage IA, car elle offre plus de VRAM et de vitesse. Mais la 3060 12 Go reste le meilleur rapport qualité-prix pour débuter.

Bon montage, et n'hésite pas si tu as des questions en cours de route ! 🌱