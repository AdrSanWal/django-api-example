# django-api-example

Ejemplo de REST API CRUD con Django Rest Framework para desplegar con Docker.

Instrucciones:
=

1º Clona el repositorio en alguna carpeta:

    git clone https://github.com/AdrSanWal/django-api-example.git


2º Ejecuta docker-compose:

  Dentro de la carpeta django-api-example:

    docker-compose up -d
    
3º Rellena la base de datos con unos cuantos ejemplos:
  
  docker exec django python3 filmsapi/manage.py loaddata data.json
  
Puedes consultar la api en http://localhost:8000/api/
