# Create an user

```
POST /api/v1/users
```

Creates an user in the database and returns the user created.

## Parameters

No parameters required.

## Body

* `name` The user's name.
* `age` The user's age.
* `address` The user's address. This property is a json and must have the following properties: `street`, `number`, `city` and `state`.

## HTTP Status

* `201` Created
* `400` Invalid JSON.
* `400` Missing name parameter.
* `400` Missing age parameter
* `400` Missing address parameter.
* `400` Missing address.street parameter.
* `400` Missing address.number parameter.
* `400` Missing address.city parameter.
* `400` Missing address.state parameter.
* `500` Internal Error.

## Example

### Request

```
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{ \
                "name":"name", \
                "age":10', \
                "address": { \
                    "street": "street", \
                    "number": 10, \
                    "city": "city", \
                    "state": "state" \
                } \
            }' \
     http://localhost:5000/api/v1/users
```

### Response

```json
{
    "id": 1,
    "name": "name",
    "age": 10,
    "address": {
        "street": "street",
        "number": 10,
        "city": "city",
        "state": "state"
    }
}
```