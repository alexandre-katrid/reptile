import os
from unittest import TestCase
from reptile.bands import DataSource, Report


class GridTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.datasource = DataSource(
            [
                {
                    'id': i,
                    'name': 'Product %s' % i,
                    'price': i * 10.01,
                    'group_name': 'Group %s' % ((i - 1) // 10 + 1),
                }
                for i in range(1, 61)
            ]
        )
