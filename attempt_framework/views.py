# from run import app
# # from patterns.structural_patterns import AppRoute
# #
# #
# #
# routes = {}
#
# class AppRoute:
#     def __init__(self, routes, url):
#         self.routes = routes
#         self.url = url
#         assert url not in self.routes, "Such route already exists."
#
#     def __call__(self, cls):
#         self.routes[self.url] = cls()
#
#
# # class AppRoute(path):
# #     assert path not in self.routes, "Such route already exists."
# #
# #     def wrapper(handler):
# #         self.routes[path] = handler
# #         return handler
# #
# #     return wrapper
#
# @Approute("/")
# class IndexHandler:
#     def get(self, req, response):
#         response.body = app.template("index.html", context={"name": "Главная", "title": "Главная страница"}).encode()
#
#     def post(self, req, response):
#         response.text = "Endpoint to create a index"
#
# #
# # @app.route("/")
# # class IndexHandler:
# #     def get(self, req, response):
# #         response.body = app.template("index.html", context={"name": "Главная", "title": "Главная страница"}).encode()
# #
# #     def post(self, req, response):
# #         response.text = "Endpoint to create a index"
# #
# #
# # @app.route("/about/")
# # class AboutHandler:
# #     def get(self, req, response):
# #         response.body = app.template("about.html", context={"name": "О нас", "title": "О нас"}).encode()
# #
# #
# # @app.route("/study_programs/")
# # class AboutHandler:
# #     def get(self, req, response):
# #         response.body = app.template("study-programs.html", context={"name": "О нас", "title": "О нас"}).encode()