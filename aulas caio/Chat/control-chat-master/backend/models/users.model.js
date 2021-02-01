const Sequelize = require("sequelize");

function UserModel(sequelize) {
  const Users = sequelize.define("Users", {
    id: {
      primaryKey: true,
      autoIncrement: true,
      type: Sequelize.INTEGER,
    },
    name: Sequelize.STRING,
    email: Sequelize.STRING,
    password: Sequelize.STRING,
  });
  return Users;
}

module.exports = UserModel;
