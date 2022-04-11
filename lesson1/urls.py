from datetime import date, datetime
from views import Index, About, Contacts


# front controller
def secret_front(request):
    request['data'] = date.today()


def other_front(request):
    request['key'] = 'key'


def report_data_of_run(request):
    request['var_report_data_of_run'] = datetime.now()


fronts = [secret_front, other_front, report_data_of_run]


routes = {
    '/': Index(),
    '/about/': About(),
    '/contacts/': Contacts(),
}
