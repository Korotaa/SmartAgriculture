from flask import Flask, render_template, jsonify
from pressureSensor import PressureSensor
from flowSensor import FlowSensor

app = Flask(__name__)

pressureModule = PressureSensor()
flowModule = FlowSensor()

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/sensorReadings")
def getSensorReadings():
    psi, bar, Mpa, HPa = pressureModule.pressureReadings()
    flow = flowModule.flowReadings()
    
    return jsonify(
        {
            "status" : "ok",
            "Pressure" : HPa,
            "flow"     : flow
        }
    )
    
if __name__ == "__main__" :
    app.run(debug=True, host="0.0.0.0")