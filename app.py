from flask import Flask, render_template, jsonify
import threading
import sniffer

app = Flask(__name__)

# Start sniffing in background thread (set iface here)
threading.Thread(target=sniffer.start_sniffing, args=("Wi-Fi",), daemon=True).start()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/packets")
def get_packets():
    return jsonify(sniffer.packets[-20:])  # last 20 packets

if __name__ == "__main__":
    app.run(debug=True)
