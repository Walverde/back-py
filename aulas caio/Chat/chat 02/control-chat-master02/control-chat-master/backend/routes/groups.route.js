const express = require("express");
const route = express.Router();
const { Groups, Users } = require("../models");
//const sequelize = require("../models");
//const Groups = sequelize.Groups;
const requireToken = require("../middleware/auth");

route.use(requireToken);
route.get("/", function (req, res) {
  Groups.findAll({ where: { "$Users.id$": req.userId }, include: Users })
    .then((result) => {
      res.json(result);
    })
    .catch((err) => {
      res.status(500).json(err);
    });
});
route.post("/", function (req, res) {
  Groups.crete(req.body)
    .then((result) => {
      res.json(result);
    })
    .catch((err) => {
      res.status(500).json(err);
    });
});
route.put("/:id", function (req, res) {});
route.delete("/:id", function (req, res) {});

module.exports = route;
