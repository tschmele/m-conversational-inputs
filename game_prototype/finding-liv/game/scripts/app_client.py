import selectors
import socket
import sys
import traceback

import game.scripts.libclient as libclient

class Client():

    def __init__(self, host='127.0.0.1', port=5000):
        self.HOST = host
        self.PORT = port
        self.sel = selectors.DefaultSelector()


    def create_request(self, value):
        return dict(
            type = 'text/json',
            encoding = 'utf-8',
            content = dict(value=value)
        )


    def start_connection(self, request):
        addr = (self.HOST, self.PORT)
        print(f"Starting connection to {addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = libclient.Message(self.sel, sock, addr, request)
        self.sel.register(sock, events, data=message)


    def loop(self, value):
        request = self.create_request(value)
        self.start_connection(request)
        result = None

        try:
            while True:
                events = self.sel.select(timeout=1)
                for key, mask in events:
                    message = key.data
                    try:
                        result = message.process_events(mask)
                        if result != None:
                            break
                    except Exception:
                        print(
                            f"Main: Error: Exception for {message.addr}:\n"
                            f"{traceback.format_exc()}"
                        )
                        message.close()
                # Check for a socket being monitored to continue.
                if not self.sel.get_map():
                    break
        except KeyboardInterrupt:
            print("Caught keyboard interrupt, exiting")
        finally:
            return result
        

    def close_socket(self):
        self.sel.close()