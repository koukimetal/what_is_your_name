**Set Up**

* $ docker build -t whatis .
* $ docker run -p 5000:5000 whatis
* Access http://localhost:5000

**Shut Down**

* $ docker ps # Find CONTAINER ID
* $ docker stop <CONTAINER ID>
