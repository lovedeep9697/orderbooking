# Order Booking

## Overview
Order Booking is a Django-based trade engine designed to process and manage order booking efficiently. The system executes trades at 1-second intervals using a Django management command, ensuring accurate order matching and execution.

## Features
- Login/Signup
- Order Book view
- Order placement
- Trade execution: Order matching engine to match trades

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/lovedeep9697/orderbooking.git
   cd orderbooking
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```

## Usage

### Running the Trade Engine
Execute the following command to start the trade engine:
```sh
python3 manage.py start_matching_engine
```

## API Details

### Authentication
1. **Login**
   - `POST /api/token`
     - Body: `{username, password}`
   - `POST /api/token/refresh`
     - Body: `{refresh_token}`

2. **Signup**
   - `POST /api/users/register`
     - Body: `{username, email, password}`

### Orders
3. **View all orders**
   - `GET /api/orderbook/orders` (Retrieve all orders)
   - `GET /api/order?username=` (Retrieve orders for a specific user)

4. **Place an order**
   - `POST /api/orderbook/orders`
     - Body: `{price, token, quantity, order_type}`

### Trades
5. **View trades**
   - `GET /api/orderbook/trades?username=` (Retrieve trades for a specific user)


