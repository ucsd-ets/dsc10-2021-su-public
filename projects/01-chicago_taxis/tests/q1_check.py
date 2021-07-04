test = {   'name': 'q1_check',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> trips.shape\n(112033, 17)', 'hidden': False, 'locked': False},
                                   {'code': ">>> '5010436ea1be6bed3abb167bcd583b5e598c72be' in trips.index\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> '::'.join(sorted(trips.columns))\n"
                                               "'company::dropoff_community_area::duration::fare::payment_type::pickup_community_area::start_day::start_hour::start_month::start_weekday::start_year::taxi_ID::tips::trip_end_timestamp::trip_miles::trip_start_timestamp::trip_total'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
