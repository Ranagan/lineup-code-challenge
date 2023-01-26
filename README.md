## To run:

You need to have docker installed & preferably docker-compose

Once running you can visit http://localhost:3000/1/ to see user details from the API

### Start the server
```shell
make up
```

### Rebuild:
```shell
make build
```

### Shut down:
```shell
make down
```

### Run tests:
```shell
make test
```

## If you do not use docker-compose
```shell
# Start Python server
docker build -t lineup:latest .
docker run -it -p 8000:8000 lineup:latest

# Start react server
cd frontend
npm install
npm start
```