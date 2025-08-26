from flask import Flask, render_template, jsonify
import threading
import sniffer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/packets")
def get_packets():
    return jsonify(sniffer.packets)

if __name__ == "__main__":
    # Start sniffer in background thread
    t = threading.Thread(target=sniffer.start_sniffing, daemon=True)
    t.start()

    app.run(debug=True)
