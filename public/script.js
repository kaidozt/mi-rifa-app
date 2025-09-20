document.getElementById("compraForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    nombre: e.target.nombre.value,
    email: e.target.email.value,
    metodo_pago: e.target.metodo_pago.value,
    cantidad: parseInt(e.target.cantidad.value)
  };

  const res = await fetch("/api/purchase", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const json = await res.json();
  alert(json.mensaje || "Error en la compra");
});
