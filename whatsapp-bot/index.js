const guardarEnCSV = require('./guardar_en_csv');
const venom = require('venom-bot');
const { GoogleSpreadsheet } = require('google-spreadsheet');
const creds = require('./credenciales-google.json');

const SHEET_ID = '16ZMWnRrzvD_RCN3xSEp4RCDD7f6m3bfu3nNW4-UA-uc';

async function guardarEnSheets(nombre, numero, mensaje, fecha) {
  const doc = new GoogleSpreadsheet(SHEET_ID);

  await doc.useServiceAccountAuth(creds);
  await doc.loadInfo();

  const sheet = doc.sheetsByIndex[0]; // primera hoja
  await sheet.addRow({
    Nombre: nombre,
    Numero: numero,
    Mensaje: mensaje,
    Fecha: fecha,
  });

  console.log('✅ Mensaje guardado en Google Sheets');
}

venom
  .create({
    session: 'whatsapp-bot',
    multidevice: true
  })
  .then((client) => start(client));

function start(client) {
  client.onMessage(async (message) => {
    if (!message.isGroupMsg && message.body) {
      const nombre = message.notifyName || 'Desconocido';
      const numero = message.from;
      const texto = message.body;
      const fecha = new Date().toLocaleString();
  
      guardarEnSheets(nombre, numero, texto, fecha);
      guardarEnCSV(nombre, numero, texto, fecha);
    }
  });