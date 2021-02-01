const Sequelize = require("sequelize");

function MessagesModel(sequelize) {
  const Messages = sequelize.define("Messages", {
    id: {
      primaryKey: true,
      autoIncrement: true,
      type: Sequelize.INTEGER,
    },
    name: Sequelize.STRING,
    text: Sequelize.TEXT,
  });
  return Messages;
}

module.exports = MessagesModel;
