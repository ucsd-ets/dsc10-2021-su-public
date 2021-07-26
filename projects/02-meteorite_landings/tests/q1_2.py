test = {   'name': 'q1_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> df_with_geolocation.shape[0]\n38401', 'hidden': False, 'locked': False},
                                   {   'code': '>>> def geolocation_are_all_strings():\n'
                                               "...     return np.all(df_with_geolocation.get('GeoLocation').apply(lambda x: isinstance(x, str)));\n"
                                               '>>> \n'
                                               '>>> geolocation_are_all_strings()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
