const express = require("express");
const route = express.Router();
const { Users } = require("../models");
const requireToken = require("../middleware/auth");

route.use(requireToken);
route.get("/", function (req, res) {
  Users.findAll({ attributes: { exclude: ["password"] } })
    .then((result) => {
      if (!result) return res.json([]);
      return res.json(result);
    })
    .catch((err) => {
      console.log(err);
      res.status(500).json({ msg: err });
    });
});

route.get("/:id", function (req, res) {
  Users.findOne({
    where: { id: req.params.id },
    attributes: { exclude: ["password"] },
  })
    .then((result) => {
      if (!result) return res.json({});
      return res.json(result);
    })
    .catch((err) => {
      console.log(err);
      res.status(500).json({ msg: err });
    });
});

route.post("/", function (req, res) {
  Users.create(req.body)
    .then((result) => {
      res.json(result);
    })
    .catch((err) => {
      console.log(err);
      res.status(500).json({ msg: err });
    });
});

route.put("/:id", function (req, res) {
  Users.update(req.body, { where: { id: req.params.id } })
    .then((result) => {
      res.json(result);
    })
    .catch((err) => {
      console.log(err);
      res.status(500).json({ msg: err });
    });
});
route.delete("/:id", function (req, res) {
  Users.destroy({ where: { id: req.params.id } })
    .then((result) => {
      res.json(result);
    })
    .catch((err) => {
      console.log(err);
      res.status(500).json({ msg: err });
    });
});

module.exports = route;
