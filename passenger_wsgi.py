from main import app  # Replace 'main' with your actual script name
from fastapi.middleware.wsgi import WSGIMiddleware

# Wrap FastAPI app with WSGI middleware
app = WSGIMiddleware(app)
# .