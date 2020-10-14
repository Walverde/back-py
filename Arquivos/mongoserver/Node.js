const mongoose = require("mongoose")

//configurando o mongoose
mongoose.Promise = global.Promise;
mongoogse.conncect ("mongodb://localhost/Bancozero", {
    userMongoClient: true
}).then(() => {
    console.log("Conectado")
}).catch((err)=> {
    console.log("Houve um erro: " +err)
})