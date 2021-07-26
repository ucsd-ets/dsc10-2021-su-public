test = {   'name': 'q1_7',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> 'continent' in df.columns\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> df.get('continent').loc[31356:]\n"
                                               'id\n'
                                               '31356           Africa\n'
                                               '30409           Africa\n'
                                               '30410           Europe\n'
                                               '31357           Europe\n'
                                               '30414    North America\n'
                                               'Name: continent, dtype: object',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> df.index.name\n'id'", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
