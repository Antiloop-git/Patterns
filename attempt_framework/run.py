from wsgiref.simple_server import make_server
from my_framework.main import Framework
from patterns.сreational_patterns import Engine, Category

import views

app = Framework(templates_dir="templates")
site = Engine()


@app.route("/")
class IndexHandler:
    @staticmethod
    def get(request, response):
        response.body = app.template("index.html", context={"name": "Главная", "title": "Главная страница"}).encode()

    @staticmethod
    def post(req, response):
        response.text = "Endpoint to create a index"


@app.route("/about/")
class AboutHandler:
    def get(self, request, response):
        response.body = app.template("about.html", context={"name": "О нас", "title": "О нас"}).encode()


@app.route("/study_programs/")
class StudyHandler:
    def get(self, request, response):
        response.body = app.template("study_programs.html", context={"name": "Программы обучения", "title": "Программы обучения"}).encode()


@app.route("/create_category/")
class CreateCategoryHandler:
    def get(self, request, response):
        response.body = app.template("Create_Category.html", context={"name": "Создать категорию", "title": "Создать категорию"}).encode()

    def post(self, request, response):
        print(request)
        print(request.POST['name'])

        data = request.params
        print(data, type(data))

        # name = data['name']
        # name = site.decode_value(name)

        name = request.POST['name']

        all = request.GET.items()
        all = list(all)

        print(f"all: {all}")

        try:
            category_id = request.params['category_id']
        except:
            category_id = None


        # category_id = data.get('category_id')


        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)

        site.categories.append(new_category)

        # template = self.system.render_template('index.html', self.get_context())
        # return response(template, content_type='text/html')
        response.body = app.template("index.html", context={"objects_list": "site.categories"}).encode()

        # response.body = app.template("index.html", context={"name": "Программы обучения", "title": "Программы обучения"}).encode()



#
# @app.route("/template")
# def template_handler(req, response):
#     response.body = app.template("index.html", context={"name": "Alcazar", "title": "Best Framework"}).encode()
#
#
# @app.route("/book")
# class BooksResource:
#     def get(self, req, response):
#         response.text = "Books Page"
#
#
# @app.route("/home")
# def home(request, response):
#     response.text = "Привет! Это домашняя страница"
#
#
# @app.route("/about")
# def about(request, response):
#     response.text = "Привет! Это страница О НАС!"
#
#
# @app.route("/hello/{name}")
# def greeting(request, response, name):
#     response.text = f"Hello, {name}"
#
#
# @app.route("/tell/{age:d}")
# def greeting(request, response, age):
#     response.text = f"age, {age}"


with make_server('', 8088, app) as httpd:
    print("Запуск на порту 8088...")
    httpd.serve_forever()

#
# snail/exceptions.py  # Исключения
# snail/middleware.py  # Промежуточные слои
# snail/request.py  # Класс запросов
# snail/response.py  # Класс ответов
# snail/urls.py  # Роутинг
# snail/view.py  # Представления
