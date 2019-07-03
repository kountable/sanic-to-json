from routes import acp_v1

# print bluepint metadata version
print(acp_v1.name, acp_v1.version, acp_v1.__doc__)

# print endpoints with doc strings
for route in acp_v1.__dict__["routes"]:
    print(route[1])
    print(route[0].__doc__)
