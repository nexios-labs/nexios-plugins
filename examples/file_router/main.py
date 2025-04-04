from nexios import get_application

from nexios_plugins import FileRouterPlugin

app = get_application()

FileRouterPlugin(app, config={"root": "routes"})
