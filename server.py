from flask import Flask, request, jsonify
import threading
import argparse
import subprocess
import socket

app = Flask(__name__)
private_ip = socket.gethostbyname(socket.gethostname())


@app.route('/', methods=['GET', 'POST'])
def handler():
    if request.method == 'GET':
        return private_ip

    elif request.method == 'POST':
        try:
            subprocess.Popen(["python3", "stress_cpu.py"])
        except:
            print("something wrong")
        return "stress testing starated on: " + private_ip


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='mp1 part2')
    parser.add_argument('-p', '--port', type=int, default=8082, help='Port number')
    args = parser.parse_args()

    app.run(port=args.port)
