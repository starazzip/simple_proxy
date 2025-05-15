import base64
import os
from dotenv import load_dotenv
from proxy.http.parser import HttpParser
from proxy.http.proxy import HttpProxyBasePlugin

load_dotenv()

class AuthPlugin(HttpProxyBasePlugin):
    def before_upstream_connection(self, request: HttpParser) -> bool:
        username = os.getenv("PROXY_USERNAME")
        password = os.getenv("PROXY_PASSWORD")
        expected_token = base64.b64encode(f"{username}:{password}".encode()).decode()

        if not request.has_header(b'Proxy-Authorization'):
            self.deny()
            return True

        auth_header = request.header(b'Proxy-Authorization')

        if not auth_header.startswith(b'Basic '):
            self.deny()
            return True

        received_token = auth_header[len(b'Basic '):].decode()

        if received_token != expected_token:
            self.deny()
            return True

        return False

    def deny(self):
        self.client.queue(
            b'HTTP/1.1 407 Proxy Authentication Required\r\n'
            b'Proxy-Authenticate: Basic realm="proxy.py"\r\n'
            b'Content-Length: 0\r\n\r\n'
        )
        self.client.flush()
        self.client.connection.close()
