from unittest import TestCase

from src.system_layer.windows_network_configuration_handler import WindowsNetworkConfigurationHandler


class TestWindowsNetworkConnectionHandler(TestCase):

    def test_get_connection_names(self):
        # given

        # when
        connection_names: dict = WindowsNetworkConfigurationHandler.get_connection_names()

        # then
        self.assertTrue(len(connection_names) > 0, "No connections found!")
        self.assertEqual(len(connection_names.values()), len(set(connection_names.values())), "duplicate id!")
        self.assertEqual(len(connection_names.keys()), len(set(connection_names.keys())), "duplicate connection names!")
