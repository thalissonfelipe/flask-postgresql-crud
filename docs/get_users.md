# List users

```
GET /api/v1/users
```

Returns a list of users.

## Parameters

* `limit` Limit the number of users returned. Optional.
* `order_by` Direction of response body ordering, can be name or age. Optional.
* `key=name` key-value pairs to filter response body according to its values. Optional.

## Body

No body required.

## HTTP Status

* `200` OK
* `500` Internal Error.

## Example 1

### Request

```
curl -X GET http://localhost:5000/api/v1/users
```

### Response

```json
[
    {
        "name": "name 1",
        "age": 20,
        "address": {
            "street": "street 1",
            "number": 100,
            "city": "city 1",
            "state": "state 1"
        }
    },
    {
        "name": "name 2",
        "age": 20,
        "address": {
            "street": "street 2",
            "number": 200,
            "city": "city 2",
            "state": "state 2"
        }
    }
]
```

## Example 2

### Request

```
curl -X GET http://localhost:5000/api/v1/users?age=20
```

### Response

```json
[
    {
        "name": "name 2",
        "age": 20,
        "address": {
            "street": "street 2",
            "number": 200,
            "city": "city 2",
            "state": "state 2"
        }
    }
]
```