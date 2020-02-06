"""Импорт модуля, который делает запрос на сайт."""
from website_alive import make_request as mr


def site_response(site):
    """Фукнция, которая на вход принимает URL и проверяет status_code."""
    response = mr.site_request(site)
    if response.status_code == 200:
        return True
    return False
