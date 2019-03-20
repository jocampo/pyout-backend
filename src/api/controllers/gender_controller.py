from http.server import BaseHTTPRequestHandler
from src.api.model.Dummy import Dummy
import jsonpickle


class GenderController(BaseHTTPRequestHandler):

    def do_GET(self):
        """Returns all genders from the database"""
        response_object = Dummy("Peru", "LMO", "Lima", 100, 200)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(jsonpickle.encode(response_object, unpicklable=False))
        return
