# Delete one user

```
DELETE /api/v1/users/:id
```

Deletes an user by id if it exists.

## Parameters

* `id` The user's id.

## Body

No body required.

## HTTP Status

* `204` No Content.
* `404` User not found.
* `500` Internal Error.

## Example

### Request

```
curl -X DELETE http://localhost:5000/api/v1/users/1
```

### Response

Reply with HTTP status and corresponding message.