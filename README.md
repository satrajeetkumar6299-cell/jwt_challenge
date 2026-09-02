# Flask JWT + OOP + Blueprints

This version uses one hardcoded user and no database.

## Hardcoded login

```text
Email: gautam@gmail.com
Password: 123456
```

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

## Login

POST `/auth/login`

```json
{
  "email": "gautam@gmail.com",
  "password": "123456"
}
```

Use the returned JWT as a Bearer Token for `/auth/me` and `/tasks`.

## Vercel

The included `vercel.json` routes requests to `app.py`.

Tasks are stored in an in-memory Python list. They are not persistent on
Vercel and can disappear when a serverless instance restarts.
