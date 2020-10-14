const express = require ("express");
const app = express();
const path = require('path');
const cors = require('cors');
// const vue = require('express-vue');
// importando bibliotecas, e instanciando em em suas respstivas vatiaveis ↑
const Sequelize = require("sequelize");
// import dbconfig from  ("../confi/confisql");
const dbconfig = require("./confi/confisql");
const connection = new Sequelize(dbconfig);
// importando arquivo de configuração sequelise, e instanciando em app ↑

// Status de autenticação com o servidor (Conecção) ---------Connecting----------------------------------
connection.authenticate()
  .then(() => {
    console.log("Pew de mais");
  })
  .catch((err) => {
    console.log("Errou", err);
  });

// Rotas

app.get('/', (req, res) => {
    res.json({
        message: 'Behold The MEVN Stack!'
    });
});

app.get('/cad', function (req, res){
    res.send('Rota de cadrastro de posts')
})

app.post('/messages', (req, res) => {
    console.log(req.body);
    messages.create(req.body).then((message) => {
        res.json(message);
    }).catch((error) => {
        res.status(500);
        res.json(error);
    });
});






// iniciando o servidor na porta ↓ ---------------------------fim ------------------------------------
const port = process.env.PORT || 4000;
app.listen(port, () => {
    console.log(`listening on ${port}`);
});