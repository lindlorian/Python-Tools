import socket
import requests
from bs4 import *
from Networking import Constants


class ScanNetworkForWebPortal:

    @staticmethod
    def set_headers():

        headers = {
            "User-Agent": Constants.DEFAULT_USER_AGENT,
            "Referer": Constants.DEFAULT_REFERRER
        }

        return headers

    @staticmethod
    def get_host_network():

        # Get the current ip address. This will be used to determine
        # the ip address subnet that will be scanned
        # Get the ip address range for the current network. This is usually
        # 192.168.x.x or 10.0.x.x
        # Only scan networks you have permission to scan!!!

        ip = socket.gethostbyname(socket.gethostname())
        host_network = ip.rsplit('.', 1)  # Discard the assigned ip because we don't need it

        return host_network[0]

    def send_request_and_check_output(self, host, start_endpoint=int(), end_endpoint=int(), directory="", timeout=int(), schema=""):

        discovered = []

        addresses = self.set_ip_scan_list(start=start_endpoint
                                          , end=end_endpoint
                                          , host=host)

        for address in addresses:

            headers = self.set_headers()
            url = str(schema + address + directory)  # e.g. "http://192.168.1.1/"

            try:

                r = requests.get(url, headers=headers, timeout=timeout)
                BeautifulSoup(r.text, "html.parser")
                discovered.append(url)
                print("#")

            # The exceptions that could occur are numerous and instead of trying to handle all of them
            # use a generic except clause. The code should only care about the scenario when something
            # doesn't cause an error or does not return empty.

            except:

                print("...")
                continue

        if len(discovered) != 0:

            results = Constants.DISCOVERED_PORTALS_TEXT % discovered

        else:

            results = Constants.NO_RESULTS_TEXT

        print(results)

        return results

    def set_ip_scan_list(self, start, end, host=""):

        address_list = []

        # Ensure the start ip and end ip are within the valid range

        if not (start >= 0 or end >= 254):

            raise Exception(Constants.ADDRESS_OUT_OF_BOUNDS_TEXT)

        if host == "":

            host = self.get_host_network()

        for end_point in range(start, end):

            address_list.append(host + "." + str(end_point))

        return address_list


if __name__ == "__main__":
    scanner = ScanNetworkForWebPortal()
    report = scanner.send_request_and_check_output(host=Constants.DEFAULT_HOST
                                                   , directory=Constants.DEFAULT_SEARCH_DIRECTORY
                                                   , start_endpoint=Constants.DEFAULT_START_ENDPOINT
                                                   , end_endpoint=Constants.DEFAULT_END_ENDPOINT
                                                   , timeout=Constants.DEFAULT_TIMEOUT
                                                   , schema=Constants.DEFAULT_SCHEMA)
