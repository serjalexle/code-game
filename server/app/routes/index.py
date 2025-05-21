from app.routes.auth_route import auth_router
from app.routes.logs_route import logs_router


APP_ROUTES = [
    auth_router,
    logs_router,
]
