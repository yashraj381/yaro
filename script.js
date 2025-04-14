async function askYaro() {
    const input = document.getElementById("userInput").value;
    const response = await fetch("https://yaro-assistant.replit.app/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input })
    });

    const data = await response.json();
    document.getElementById("yaroReply").innerText = data.reply || "कोई जवाब नहीं मिला।";
}
