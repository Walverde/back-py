const Sequelize = require("sequelize");

function GroupsModel(sequelize) {
  const Groups = sequelize.define("Groups", {
    id: {
      primaryKey: true,
      autoIncrement: true,
      type: Sequelize.INTEGER,
    },
    name: Sequelize.STRING,
  });
  return Groups;
}

module.exports = GroupsModel;
