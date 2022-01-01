import wmi
import typing


class WindowsNetworkConfigurationHandler:

    def __init__(self, network_id: str):
        """
        Hanlder to read and modify network connections on windows.
        :param id: InterfaceIndex that identifies a specific connection.
        """
        self.network_id = network_id

    @staticmethod
    def get_connection_names() -> typing.Dict[str, str]:
        """
        Returns a dictionary {network_name:network_id} of available network connections. The id can be used to
        instantiate this class with a specific connection
        :return: dictionary {network_name:network_id} of available network connections.
        """
        network_adapters = wmi.WMI().Win32_NetworkAdapter()

        # only networks with given net connection id are relevant
        # The python wrapper for wmi unfortunately does not allow for a Null-Filtering
        network_adapters = [adapter for adapter in network_adapters if adapter.netconnectionid is not None]

        # network_id is the InterfaceIndex and network_name the NetconnectioId
        return {adapter.netconnectionid: adapter.interfaceindex for adapter in network_adapters}
