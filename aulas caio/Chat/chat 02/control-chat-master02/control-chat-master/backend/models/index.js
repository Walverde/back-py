const Sequelize = require("sequelize");
const UserModel = require("./users.model");

let sequelize = new Sequelize("vueDatabase", "vueUser", "vueP4ssw@rd", {
  host: "helloiot.com.br",
  dialect: "mysql",
});

sequelize
  .authenticate()
  .then(() => {
    console.log("Banco de dados Ok");
  })
  .catch((err) => {
    console.log("Banco de dados Fail", err);
  });

let Users = UserModel(sequelize);

sequelize.Users = Users;
module.exports = sequelize;
