import os
from openai import OpenAI

# Ta clé API (stockée dans une variable d'environnement pour plus de sécurité)
# Mais pour le test, on peut la mettre directement (attention à ne pas partager le fichier)
API_KEY = "sk-ac1e041fd6c44c749284e14ed9831e9e"  # Remplace par ta vraie clé (celle que tu as nommée "Klara")

# Initialiser le client DeepSeek (compatible OpenAI)
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com/v1"  # Endpoint DeepSeek
)

# Lire le prompt depuis prompt.txt
with open("prompt.txt", "r", encoding="utf-8") as f:
    user_message = f.read().strip()

# Appel à l'API
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Tu es une IA utile, membre du Jardin Coopératif."},
        {"role": "user", "content": user_message}
    ],
    temperature=0.7,
)

# Récupérer la réponse
assistant_reply = response.choices[0].message.content

# Sauvegarder dans reponse.txt
with open("reponse.txt", "w", encoding="utf-8") as f:
    f.write(assistant_reply)

# Afficher les tokens consommés
print("Tokens utilisés (prompt + réponse) :", response.usage.total_tokens)
print("Réponse sauvegardée dans reponse.txt")