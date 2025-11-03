import argparse

parser = argparse.ArgumentParser()
parser.add_argument("IP")
parser.add_argument("--port", "-p", default = 2500)
args = parser.parse_args()

print("serverIP:", args.IP)
print("port:", args.port)
