# Deploy with Docker Compose

This project is prepared to run with Docker Compose (Postgres + FastAPI web service).

1) Copy the example env and edit secrets:

```bash
cp .env.example .env
# Edit .env to set a secure POSTGRES_PASSWORD
```

2) Build and start services:

```bash
docker compose up --build -d
```

3) Check logs:

```bash
docker compose logs -f web
```

4) The API will be available at `http://<host-ip>:8000` and the OpenAPI docs at `/docs`.

Notes:
- `DATABASE_URL` inside the container is set to connect to the `db` service.
- If deploying to a cloud server or DigitalOcean, run the same `docker compose` commands there.
- For production you should:
  - Use a secure password and do not commit `.env` to the repo.
  - Use a managed Postgres or separate volume backups for the DB.
  - Put the app behind a TLS-terminating reverse proxy (nginx, Caddy, or cloud load balancer).
