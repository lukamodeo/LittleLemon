- static content (index view):
http://localhost:8000/api/

- menu endpoints (Menu Items and Single Menu Item - authentication required):
http://localhost:8000/api/menu-items            (GET/POST)
http://localhost:8000/api/menu-items/<int:pk>   (GET/PUT/DELETE)

- table booking endpoint (Booking List - authentication required):
http://localhost:8000/api/booking/tables        (GET/POST)

- user registration (djoser native):
http://localhost:8000/auth/token/login/         (POST with Username and Password to get a Token)
http://localhost:8000/auth/token/logout/        (GET to destroy Token)

