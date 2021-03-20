# Get one user

```
GET /api/v1/users/:id
```

Returns an user by id if it exists.

## Parameters

* `id` The user's id.

## Body

No body required.

## HTTP Status

* `200` OK
* `404` User not found.
* `500` Internal Error.

## Example

### Request

```
curl -X GET http://localhost:5000/api/v1/users/1
```

### Response

```json
{
    "name": "name 1",
    "age": 20,
    "address": {
        "street": "street 1",
        "number": 100,
        "city": "city 1",
        "state": "state 1"
    }
}
```