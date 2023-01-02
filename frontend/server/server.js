const jsonServer = require('json-server');
const middleware = jsonServer.defaults();
const server = jsonServer.create();

server.use(middleware);
server.use(jsonServer.bodyParser);

const testsData = require('./data/tests');

server.get('/api/tests', (req, res, next) => {
  res.status(200).send(testsData);
});

server.listen(3000, () => {
  console.log('JSON server listening on port 3000');
});