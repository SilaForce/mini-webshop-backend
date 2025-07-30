# Mini Web Shop Backend

This is the backend for the Mini Web Shop project. It is designed to handle user authentication, product management, and database interactions.

### Backend url

https://mini-webshop-backend-2ps2.onrender.com

## Setup Instructions

1. Clone the repository:

   ```
   git clone <repository-url>
   cd mini-webshop-backend
   ```

2. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python app/main.py
   ```

## Usage

- The application provides endpoints for user authentication and product management.
- Refer to the `app/routes/auth.py` and `app/routes/products.py` files for available routes and their usage.
