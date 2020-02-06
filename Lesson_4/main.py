"""Импорт модуля, который проверяет status_code."""
from website_alive import check_response as cr


URL = input()
if cr.site_response(URL):
    print("Website available")
else:
    print("Website isn't available")
