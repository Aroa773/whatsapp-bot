const venom = require('venom-bot');

venom
  .create({
    session: 'whatsapp-bot', // este nombre puede ser cualquiera, ¡pero debe estar!
    multidevice: true, // usa el nuevo sistema de WhatsApp Web
    headless: false // para que puedas ver el navegador
  })
  .then((client) => start(client))
  .catch((err) => {
    console.error('❌ Error al iniciar el bot:', err);
  });

function start(client) {
  client.onMessage((message) => {
    if (message.body === 'hola' && message.isGroupMsg === false) {
      client.sendText(message.from, '¡Hola! ¿En qué puedo ayudarte?');
    }
  });
}


