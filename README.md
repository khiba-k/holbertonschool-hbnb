# holbertonschool-hbnb

Creating our very own web application, HBnB Evolution, modeled after AirBnB using Python and Flask!

<h3><b>Documentation</b></h3>

<h4>Building the Docker Image</h4>

To build the Docker image, run the following command from the root directory of your application:

<p>docker build -t my-flask-app .</b>

<h4>Running the Container</h4>

<b>To run the container, use:</b>
<b>
docker run -d -p 5000:5000 -v /path/to/host/data:/app/data -e APP_PORT=5000 --name my-flask-container my-flask-app
Replace /path/to/host/data with the path on your host machine where you want to store persistent data.
</b>

<h4>Accessing the Application</h4>

Open your web browser and navigate to http://localhost:5000.

<h4>Overriding the Port</h4>

<b>To override the default port, use the -e flag:</b>

<b>
    docker run -d -p 8080:8080 -v /path/to/host/data:/app/data -e APP_PORT=8080 --name my-flask-container my-flask-app
    This will run the application on port 8080.
</b>

<h4>Persistent Data Storage</h4>

<b>
    The -v /path/to/host/data:/app/data option in the docker run command ensures that the data directory in the container is mapped to a directory on the host system, allowing data to persist across container restarts
</b>
