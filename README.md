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
  - [Food]
  - stock

- Menu (Singleton)
  - id
  - List [MenuFoodItem] 1 - *

- Order
    - id
    - client_name
    - client_phone
    - client_email
    - List [OrderItem] * - 1
    - total_charge
    - status
    - location/address

- OrderItem
    - id
    - [Order] 1 - *
    - quantity

----
## Business UseCases

- CRUD on Food
- Adding and Removing Food from Menu
- Placing an Order
- Settling an Order

