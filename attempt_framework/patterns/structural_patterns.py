# # from time import time
#
#
#
#
# class AppRoute:
#     def __init__(self, routes, url):
#         '''
#         Сохраняем значение переданного параметра
#         '''
#         self.routes = routes
#         self.url = url
#
#     def __call__(self, cls):
#         '''
#         Сам декоратор
#         '''
#         self.routes[self.url] = cls()
#
#
# #
# # def route(self, path):
# #     assert path not in self.routes, "Such route already exists."
# #
# #     def wrapper(handler):
# #         self.routes[path] = handler
# #         return handler
# #
# #     return wrapper
# #
# #
# #
# # # структурный паттерн - Декоратор
# # class AppRoute:
# #     def __init__(self, routes, url):
# #         self.routes = routes
# #         self.url = url
# #         assert url not in self.routes, "Such route already exists."
# #
# #     def wrapper(self, cls):
# #         self.routes[self.urlurl] = cls
# #         return handler
# #
# #     return wrapper
# #
# # class AppRoute:
# #     def __init__(self, routes, url):
# #         '''
# #         Сохраняем значение переданного параметра
# #         '''
# #         self.routes = routes
# #         self.url = url
# #
# #     def __call__(self, cls):
# #         '''
# #         Сам декоратор
# #         '''
# #         self.routes[self.url] = cls()
# #
# #
# # # # структурный паттерн - Декоратор
# # # class Debug:
# # #
# # #     def __init__(self, name):
# # #
# # #         self.name = name
# # #
# # #     def __call__(self, cls):
# # #         '''
# # #         сам декоратор
# # #         '''
# # #
# # #         # это вспомогательная функция будет декорировать каждый отдельный метод класса, см. ниже
# # #         def timeit(method):
# # #             '''
# # #             нужен для того, чтобы декоратор класса wrapper обернул в timeit
# # #             каждый метод декорируемого класса
# # #             '''
# # #             def timed(*args, **kw):
# # #                 ts = time()
# # #                 result = method(*args, **kw)
# # #                 te = time()
# # #                 delta = te - ts
# # #
# # #                 print(f'debug --> {self.name} выполнялся {delta:2.2f} ms')
# # #                 return result
# # #
# # #             return timed
# # #
# # #         return timeit(cls)
