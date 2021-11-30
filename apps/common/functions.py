import functools
from decimal import Decimal, ROUND_HALF_UP

from django.db import connection

from rest_framework.response import Response

def round_decimal(value, prec=2):
    number_format = '0.' + '0' * prec
    return value.quantize(Decimal(number_format), rounding=ROUND_HALF_UP)

"""
Retorna los datos obtenidos del procedure filtrado con filters
"""
def get_data_procedure(procedure, params=(), filters=[]):
    data = []
    query = 'select * from {}()'.format(procedure)
    values = []

    if filters:
        query = '{} where {}'.format(query, ' and '.join(map(lambda e: '{field} {operator} %s'.format(**e), filters)))
        values += map(lambda e: e['value'], filters)

    with connection.cursor() as cursor:
        cursor.execute(query, values)
        columns = [col[0] for col in cursor.description]
        for row in cursor.fetchall():
            row = dict(zip(columns, row))
            data.append(row)

    return data

"""
Convierte los query params definidos en fields en un dict(field: nombre del campo, operator, value: valor del query param)
ej.
['campo', 'otro'] => [{field: 'campo', operator: '=', value: ''}, {field: 'otro', operator: '=', value: ''}]
['campo__gte', 'otro__icontains'] => [{field: 'campo', operator: '>=', value: ''}, {field: 'otro', operator: 'ilike', value: ''}]
"""
def get_filters_request(request, fields):
    filters = []
    operators = {'exact': '=', 'icontains': 'ilike', 'gte': '>=', 'lte': '<='}
    for field in fields:
        value = request.query_params.get(field, None)
        lookup = 'exact'
        if field.find('__') >= 0:
            field, lookup = field.split('__')
        if value not in (None, ''):
            operator = operators[lookup]
            if operator == 'ilike':
                value = ' {} '.format(value.strip()).replace(' ', '%')
            filter_obj = {'field': field, 'operator': operator, 'value': value}
            filters.append(filter_obj)
    return filters

"""
Decorador para retornar el Response de la llamada de un procedure
"""
def reporte_procedure(procedure):
    def wrapper_args(function):
        @functools.wraps(function)
        def wrapper_function(*args, **kwargs):
            view = args[0]
            request = args[1]
            filters = function(*args, **kwargs)
            filters = get_filters_request(request, filters)
            data = get_data_procedure(procedure, filters=filters)
            page = view.paginate_queryset(data)
            if page is not None:
                return view.get_paginated_response(page)
            return Response(data)
        return wrapper_function
    return wrapper_args