const express = require('express')
const path = require('path')

const app = express();
app.use(express.urlencoded({extended: true}))
const bport = 3000
const fport = 5173

// GET POST handling
app.post('/', function (req, res) {
  console.log('Hello, world!')
  res.redirect(`http://localhost:${fport}/`)
});

app.get('/', function(req, res) {
  res.redirect(`http://localhost:${fport}/`)
})


// Server start
app.listen(bport, function(req, res) {
  console.log(`Server running\n\tbackend host: http:/localhost:${bport}\n\tfrontend host: http:/localhost:${fport}`)
});