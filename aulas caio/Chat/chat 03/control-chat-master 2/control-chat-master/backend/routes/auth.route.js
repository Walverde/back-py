const express = require("express");
const route = express.Router();
const jwt = require("jsonwebtoken");
const { Users } = require("../models");

route.post("/login", (req, res) => {
  let { email, password } = req.body;
  Users.findOne({ where: { email, password } })
    .then((result) => {
      if (!result) {
        return res.status(500).json({ msg: "Usuário não encontrado" });
      }
      let token = jwt.sign({ id: result.id }, "Chave Secreta");
      res.set("token", token);
      res.json(result);
    })
    .catch((err) => {
      res.json(err);
    });
});

module.exports = route;
