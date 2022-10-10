# Food-Order-System

## Models

- Food
    - id (number tentatively, will change to UUID later)
    - name (char)
    - price (char)
    - description (char)
    - photo (but will not be implemented right now)
    - 
- MenuFoodItem
  - id
  - Food
  - stock

- Menu
  - id
  - List [MenuFoodItem]

- Order
    - id
    - client_name
    - client_phone
    - client_email
    - List [OrderItem]
    - total_charge
    - status
    - location/address

- OrderItem
    - id
    - Food
    - quantity

----
## Business UseCases

- CRUD on Food
- Adding and Removing Food from Menu
- Placing an Order