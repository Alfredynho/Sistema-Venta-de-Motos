**DEVZONE** Backend Proyecto USMOTOS
### Tecnologías

  * [Django](https://www.djangoproject.com/)
  * [Admin LTE Template](http://semantic-ui.com/)

### Commercial Support

# Crear Base de Datos en postgres

  - `sudo su postgres`
  - `psql -c "DROP DATABASE usm_app"`
  - `psql -c "DROP USER usm_user"`
  - `psql -c "CREATE USER usm_user WITH NOCREATEDB NOCREATEUSER ENCRYPTED PASSWORD 'XXXYYYZZZ'"`
  - `psql -c "CREATE DATABASE usm_app WITH OWNER usm_user"`


DEVZONE es soportado por [@alfredynho](alfredynho.cg@gmail.com).

