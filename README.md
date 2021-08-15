# izba-docs-api

Documents viewer API.

## Configuration

Configuration for the development / production environment is done using environment variables.

These variables can be passed either in an .env file or using Doppler-like tools. Required set of variables for each enviromnent is listed below.

### Development

Set of environment variables required by development docker-compose file (see `docker-compose.dev.yml`).

| Name | Extra info |
|---|---|
| DJ_ALLOWED_HOSTS | `ALLOWED_HOSTS` (Django `settings.py`) |
| DJ_CORS_ORIGIN_WHITELIST | `CORS_ORIGIN_WHITELIST` (Django `settings.py`) |
| DJ_SECRET_KEY | `SECRET_KEY` (Django `settings.py`) |
| GIT_USER_EMAIL | `user.email` for `git config --global` |
| GIT_USER_NAME | `user.name` for `git config --global` |
| POSTGRES_DB | Database name for PostgreSQL image |
| POSTGRES_PASSWORD | Superuser password for PostgreSQL image |
| POSTGRES_USER | Superuser name for PostgreSQL image |

### Production

Set of environment variables required by production docker-compose file (see `docker-compose.yml`).

| Name | Extra info |
|---|---|
| COMPOSE_APP_PORT | `app` service port (`docker-compose.yml`) |
| COMPOSE_WEB_API_HOST | `web` service api host (`docker-compose.yml`, `VUE_APP_API_HOST` in `Dockerfile`) |
| COMPOSE_WEB_PORT | `web` service port (`docker-compose.yml`) |
| DJ_ALLOWED_HOSTS | `ALLOWED_HOSTS` (Django `settings.py`) |
| DJ_SECRET_KEY | `SECRET_KEY` (Django `settings.py`) |
| POSTGRES_DB | Database name for PostgreSQL image |
| POSTGRES_PASSWORD | Superuser password for PostgreSQL image |
| POSTGRES_USER | Superuser name for PostgreSQL image |
