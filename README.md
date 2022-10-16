## Project

## API

### add transaction

- url: http://127.0.0.1:8000/transactions/
- method: POST
- request data:

```json
{
  "payer": "DANNON",
  "points": 1000,
  "timestamp": "2020-11-02T14:00:00Z"
}
```

- response data:

```json

```

### spend points

- url: http://127.0.0.1:8000/spend_points/
- method: POST
- request data:

```json
{
  "points": 5000
}
```

- response data:

```json

```

### show points balance

- url: http://127.0.0.1:8000/users/
- method: GET
- request data: null

- response data:

```json
{
  "DANNON": 1000,
  "UNILEVER": 0,
  "MILLER COORS": 5300
}
```






