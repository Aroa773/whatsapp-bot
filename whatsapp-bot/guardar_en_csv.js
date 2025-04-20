const fs = require("fs");
const path = require("path");

function guardarEnCSV(nombre, numero, mensaje, fecha) {
  const ruta = path.join(__dirname, "../datos_whatsapp.csv");
  const fila = `"${nombre}","${numero}","${mensaje.replace(/"/g, '""')}","${fecha}"\n`;

  // Si el archivo no existe, añade la cabecera
  if (!fs.existsSync(ruta)) {
    const cabecera = `"Remitente","Número","Mensaje","Fecha"\n`;
    fs.writeFileSync(ruta, cabecera);
  }

  // Añadir el mensaje al CSV
  fs.appendFileSync(ruta, fila);
}

module.exports = { guardarEnCSV };

