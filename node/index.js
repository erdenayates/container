const express = require('express');
const mysql = require('mysql');
const app = express();
const port = 3000;

const connection = mysql.createConnection({
  host: 'mysql',
  user: 'root',
  password: 'password',
  database: 'information_schema'
});

app.get('/', (req, res) => {
  connection.query('SELECT * FROM CHARACTER_SETS', (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

app.listen(port, () => {
  console.log(`Node app listening at http://localhost:${port}`);
});

