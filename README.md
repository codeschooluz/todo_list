# todo_list
project


# Endpoints

## GET /todo_list

Request:

```bash
curl -X GET http://localhost:8080/get
```

Response:

```json
[
  {
    "id": 1,
    "title": "test",
    "description": "test",
    "status": "test",
    "created_at": "2021-05-31T15:00:00Z",
    "updated_at": "2021-05-31T15:00:00Z"
  }
]
```

## POST /add

Request:

```bash
curl -X POST http://localhost:8080/add -d '{"title":"test","description":"test"}' -H "Content-Type: application/json"
```

Response:

```json
{
  "id": 1,
  "title": "test",
  "description": "test",
  "status": "test",
  "created_at": "2021-05-31T15:00:00Z",
  "updated_at": "2021-05-31T15:00:00Z"
}
```