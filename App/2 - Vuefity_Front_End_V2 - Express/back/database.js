// importando o Sequelize. 

const Sequelize = require("sequelize");
// cont dbconfig = require('../config/dataset'); // Exemplo de importação de arquivo de configuração. 


// configurando linguagem e senha acesso ao banco de dados. 
// em caso de arquivo de configuração importado : ↓ 
// const connection = new Sequelize(dbconfig);
// module.exports = connection; // caso nescessario exportar e usar em outra parte do programa. 
const sequelize = new Sequelize("exemplo", "root", "0101", { //conectando ao banco de dados. 
  host: "localhost",
  dialect: "mysql",
});

// Status de acesso ao banco. 

sequelize.authenticate()
  .then(() => {
    console.log("Pew de mais");
  })
  .catch((err) => {
    console.log("Errou", err);
  });



// CRUD -----------------------------------------------------------------------------------------------------------------
// criando uma table. 
const banco_de_dados = sequelize.define("Tabela_02", { //Nome da tabela. 
  coluna_01: { // nome da coluna. 
    type: Sequelize.INTEGER,
  },
  coluna_02: {
    type: Sequelize.STRING,
  }
});
// banco_de_dados.sync({force:true}) // Sincronizando tabela acima ↑

//inserindo dados. Na tabela banco_de_dados ↑ 
banco_de_dados.create({
  coluna_01: "1231321",
  coluna_02: "chora ou nem",
})



// module.exports = sequelize;



