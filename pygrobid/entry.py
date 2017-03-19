from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

grobid = gateway.entry_point.getEngine()

class Grobid():

    def __init__(self):
        self._gateway = JavaGateway()
        self._grobid_engine = gateway.entry_point.getEngine()
