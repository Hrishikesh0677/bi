from xmlrpc.server import SimpleXMLRPCServer

def concatenate_strings(str1, str2):
    return str1 + str2

server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")
server.register_function(concatenate_strings, "concatenate")
server.serve_forever()
