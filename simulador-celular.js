// simulador-celular.js
const express = require('express');
const app = express();
const PORT = 21337;

app.get('/trigger/linterna-on', (req, res) => {
  console.log('💡 ¡Simulación: se prendería la linterna!');
  res.send('Simulación OK');
});

app.get('/trigger/linterna-off', (req, res) => {
  console.log('💡 ¡Simulación: se apagaria la linterna!');
  res.send('Simulación OK');
});


app.listen(PORT, () => {
  console.log(`Servidor SIMULADOR escuchando en http://localhost:${PORT}`);
});
