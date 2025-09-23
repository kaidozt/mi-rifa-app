document.getElementById("purchaseForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const payment = document.getElementById("payment").value;

  const response = await fetch("/api/purchase", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, payment })
  });

  const result = await response.json();

  const messageDiv = document.getElementById("message");
  if (result.success) {
    messageDiv.textContent = "✅ Compra registrada. ¡Mucha suerte!";
    messageDiv.style.color = "#28a745";
  } else {
    messageDiv.textContent = "❌ Error: " + (result.error || "No se pudo registrar");
    messageDiv.style.color = "red";
  }
});
