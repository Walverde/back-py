let express = require("express");
let sequelize = require("./models");
const UserRoute = require("./routes/users.route");
const AuthRoute = require("./routes/auth.route");
const cors = require("cors");

require("./models");

let app = express();

app.use(express.json());
app.use(
  cors({
    exposedHeaders: "token",
  })
);
app.use("/users", UserRoute);
app.use("/", AuthRoute);

console.log("Servidor Startado");
module.exports = app;
