# Create an user

```
PUT /api/v1/users/:id
```

Updates an user by id if its exists.

## Parameters

* `id` The user's id.

## Body

* `name` The user's name. Optional.
* `age` The user's age. Optional.
* `address` The user's address. This property is a json and must have the following properties: `street`, `number`, `city` and `state`. Optional.

## HTTP Status

* `204` No Content
* `400` Invalid JSON.
* `500` Internal Error.

## Example

### Request

```
curl --header "Content-Type: application/json" \
     --request PUT \
     --data '{"name":"name1","age":20'}' \
     http://localhost:5000/api/v1/users/1
```

### Response

Reply with HTTP status and corresponding message.