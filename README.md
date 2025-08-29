# KamGrow Pharma (Django)

A clean, production-ready starter for an online pharmacy:
- Product catalog with categories & manufacturers
- Search, product detail, prescription-required flag
- Add to cart, checkout (COD placeholder), order records
- Upload prescription (image/pdf)
- REST API: `/api/catalog/products/`, `/api/catalog/categories/`
- Bootstrap 5 UI with your logo

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ — visit /admin to add Categories & Products.
Upload prescriptions at /prescriptions/upload/.
API at /api/catalog/products/ and /api/catalog/categories/.

### Notes
- Change SECRET_KEY and DEBUG in `.env` or env vars before production.
- Static files served from `static/`. Collected to `staticfiles/` in production.
- SQLite by default; switch DB in `settings.py` for Postgres/MySQL.
