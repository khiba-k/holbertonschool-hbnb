
# holbertonschool-hbnb

Creating our very own web application, HBnB Evolution, modeled after AirBnB using Python and Flask!


## Building the Docker Image
To build the Docker image, run the following command from the root directory of your application:

```Bash

docker build -t my-flask-app
```

## Running the Container
To run the container, use:

```Bash

docker run -d -p 5000:5000 -v /path/to/host/data:/app/data -e APP_PORT=5000 --name my-flask-container my-flask-app Replace /path/to/host/data
```
with the path on your host machine where you want to store persistent data

## Accessing the Application
Open your web browser and navigate to

```

http://localhost:5000
```

## Overriding the Port
To override the default port, use the -e flag:

```Bash

docker run -d -p 8080:8080 -v /path/to/host/data:/app/data -e APP_PORT=8080 --name my-flask-container my-flask-app
```
This will run the application on port 8080

## Persistent Data Storage
The

```Bash

-v /path/to/host/data:/app/data
```
option in the docker run command ensures that the data directory in the container is mapped to a directory on the host system, allowing data to persist across container restarts


## Authors

- [@Khiba Koenane](https://github.com/khiba-k)
- [@Kamohelo Koali](https://github.com/KamoheloKoali)
- [@Langa Hoohlo](https://github.com/Langahoohlo)
- [@Mthawelanga Matross](https://github.com/Matross-20)
- [@Lebohang Motaung](https://github.com/Lebohang1983)
- [@Pheello Ntlele](https://github.com/Ntlele)

