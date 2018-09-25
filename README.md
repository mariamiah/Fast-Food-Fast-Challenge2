[![Build Status](https://travis-ci.org/mariamiah/Fast-Food-Fast-Challenge2.svg?branch=develop)](https://travis-ci.org/mariamiah/Fast-Food-Fast-Challenge2)
# Fast-Food-Fast-API

Fast-Food-Fast is a food delivery service app for a restaurant.

## Installations
Clone this repository onto your local machine by using the command below:
```
git clone https://github.com/mariamiah/Fast-Food-Fast-Challenge2.git
```

## Usage

All responses will have the form
```json
{
    "data":"Mixed type holding the content of the response",
    "message":"Description of what happened"
}
```
Subsequent response definitions will only detail the expected value of `data fields`

### Get all orders
**Definition**

`GET/orders`

**Responses**

- `200 OK ` on success 

```json
[
    {
        "order_id": 1,
        "name":"Veggie Burger",
        "order_type":"take away",
        "client_name":"Susan"
    },
    {
        "order_id": 2,
        "name":"Hot dog",
        "order_type":"dine in",
        "client_name":"Mark"
    }
]
```
### Place a new order

**Definition**

`POST/orders`

**Arguments**

- `"name":string` name of fast-food you wish to order
- `"order_type:string` whether you would like to take away or dine in
- `"client_name":string` the name of the client placing the order

**Response**
- `201 Created` on success
```json

    {
        "name":"Meat Samosas",
        "order_type":"take away",
        "client_name":"maria"
    }
```
## Fetch a specific order
`GET/orders/<orderId>`
**Response**
-`404 Not Found` if the specific order doesnot exist
-`200 OK` on success
```json
{
        "order_id": 2,
        "name":"Hot dog",
        "order_type":"dine in",
        "client_name":"Mark"
    }
```
## Update the status of an order
**Definition**

`PUT/order/<orderId>`

**Response**

-`404 Not Found` if the order doesnot exist

-`201 Created` on sucess
