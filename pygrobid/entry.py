from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

grobid = gateway.entry_point.getEngine()
