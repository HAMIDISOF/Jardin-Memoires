(function() {
    const SELECTOR = '.chat-message, .message, [class*="message"]';
    const messages = document.querySelectorAll(SELECTOR);
    if (messages.length === 0) {
        console.error("Aucun message trouvé. Vérifie le sélecteur CSS.");
        return;
    }
    let output = "# Conversation DeepSeek – sauvegarde brute\n\n";
    messages.forEach(msg => {
        let author = "Inconnu";
        if (msg.querySelector('.user, [class*="user"]')) author = "**Sof**";
        else if (msg.querySelector('.assistant, [class*="assistant"]')) author = "**Sol**";
        let text = msg.innerText || msg.textContent;
        text = text.trim();
        if (text) {
            output += `---\n${author} :\n${text}\n\n`;
        }
    });
    const blob = new Blob([output], {type: "text/markdown"});
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = `deepseek_${new Date().toISOString().slice(0,19)}.md`;
    link.click();
    URL.revokeObjectURL(link.href);
    console.log("Extraction terminée !");
})();