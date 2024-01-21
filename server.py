from flask import Flask, request, jsonify
import threading
import argparse
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handler():
    private_ip = socket.gethostbyname(socket.gethostname())

    if request.method == 'GET':
        return private_ip

    elif request.method == 'POST':
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "stress testing starated on " + private_ip


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='mp1 part2')
    parser.add_argument('-p', '--port', type=int, default=8082, help='Port number')
    args = parser.parse_args()

    app.run(port=args.port)
