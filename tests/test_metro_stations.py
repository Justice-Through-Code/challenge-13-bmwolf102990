'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DO NOT EDIT THIS FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

import io
from unittest import mock, TestCase

from metro_stations import SubwayStation, BusStation


class TestStationClasses(TestCase):
    def setUp(self) -> None:
        # Runs before every test case
        super().setUp()

        self.subway = SubwayStation(
            '14th Street', '14th street and 7th avenue', ['1', '2', '3', 'L']
        )
        self.bus_station = BusStation(
            'NYC Megabus Stop', '34th street and 12th avenue', ['Boston', 'DC', 'Philly']
        )

    def test_subway_constructor(self):
        self.assertEqual(['1', '2', '3', 'L'], self.subway.lines)
        self.assertEqual('14th street and 7th avenue', self.subway.location)
        self.assertEqual('14th Street', self.subway.station_name)

    def test_bus_station_constructor(self):
        self.assertEqual(['Boston', 'DC', 'Philly'], self.bus_station.routes)
        self.assertEqual('34th street and 12th avenue', self.bus_station.location)
        self.assertEqual('NYC Megabus Stop', self.bus_station.station_name)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_subway_show_info(self, mock_stdout):
        self.subway.show_info()

        info = mock_stdout.getvalue()

        self.assertIn('14th Street', info)
        self.assertIn('14th street and 7th avenue', info)
        self.assertIn('open', info.lower())
        self.assertIn('1', info)
        self.assertIn('2', info)
        self.assertIn('3', info)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bus_station_show_info(self, mock_stdout):
        self.bus_station.show_info()

        info = mock_stdout.getvalue()

        self.assertIn('NYC Megabus Stop', info)
        self.assertIn('34th street and 12th avenue', info)
        self.assertIn('open', info.lower())
        self.assertIn('Boston', info)
        self.assertIn('DC', info)
        self.assertIn('Philly', info)

        self.bus_station.close_station()
        self.bus_station.show_info()
        info = mock_stdout.getvalue()

        self.assertIn('closed', info.lower())

    def test_close_station(self):
        self.bus_station.close_station()
        self.assertEqual(False, self.bus_station.is_open)

    def test_open_station(self):
        self.subway.open_station()
        self.assertEqual(True, self.subway.is_open)