test = {   'name': 'q1_5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> 'decade' in df_with_decade.columns\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> to_decade(1943) == 1940\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> to_decade(1500) == 1500\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> df_with_decade.get('decade').loc[30409] == 1990\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}