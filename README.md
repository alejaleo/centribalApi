Presentación y descripción del proyecto back artículos y pedidos para centribal.
Por: Alejandra león

Tecnologías utilizadas
• El proyecto back fue desarrollado en python 3.11.3 Django 5.0.6, mySql y Docker

Descripción del proyecto 
El proyecto es una REST API para una aplicación de gestión de artículos y pedidos
• Artículos: se puede crear nuevos artículos, editarlos y eliminarlos 
• Pedidos: se pueden crear nuevos pedidos adjuntando los artículos ya creados, editarlos y eliminarlos.

Pasos
1- activar el entorno virtual de python en consola con el comando “myenv\Scripts\activate”
2- se crea el contenedor de docker con el comando “docker-compose build”
3- se sube el contenedor con el comando “docker-compose up”
4- importar el archivo “apiCentribal.postman_collection” en postman que se encuentra en la carpeta principal de centribalApi.
5-para visualizar desde el navegador debe ingresar a “http://localhost:8000/articles/” o a “http://localhost:8000/orders/ ”
6- Para realizar pruebas unitarias ingresar el comando “pytest-v”
