## 🎮 DUST-MIGHTY
Users can log activities such as reading, exercising, and studying in "10-minute blocks" to earn points and visualize their progress in real-time.

### 🚀 run fastapi
```bash
uv run fastapi dev app/main.py
```

### 👉 alembic update
```bash
uv run alembic revision --autogenerate -m "message"
uv run alembic upgrade head
```

### 1. Dependency Injection Strategy
We utilize FastAPI's `Annotated` pattern to maintain a clean and type-safe DI system.

* **Global Dependencies (`app/core/deps.py`)**
    * Contains `DBSession` and `CurrentUser`.
    * Centralized here to prevent **circular imports** when multiple services require authentication or DB access.
* **Domain Service Dependencies (Service-specific)**
    * Defined at the bottom of each service file  
    `AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]`.