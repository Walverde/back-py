const jwt = require("jsonwebtoken");

function requireToken(req, res, next) {
  let { token } = req.headers;
  jwt.verify(token, "Chave Secreta", function (err, decoded) {
    if (err) return res.status(401).json({ msg: "Token invalido" });
    next();
  });
}
module.exports = requireToken;
