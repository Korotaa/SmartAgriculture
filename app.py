from flask import Flask, render_template, jsonify
from time import sleep
from datetime import date
import math
import random

#from pressureSensor import PressureSensor
#from flowSensor import FlowSensor

FLOW_GPIOPIN = 13

app = Flask(__name__)
pressureSensor = PressureSensor()
flowSensor = FlowSensor()

flowSensor.setup()

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/sensorReadings")
def getSensorReadings():
    #Read Pressure
    pressureSensor.pressureReadings()
    pressurInbar = pressureSensor.getPressureInBar()
    pressureInHPa = pressureSensor.getPressureInHPa()
    pressureInMPa = pressureSensor.getPressureInMPa()

    #Read Flow rate
    flowRate = flowSensor.getFlowRate()

    temperature = random.uniform(10, 30)
    pressure = random.randint(0, 1)
    #print(pressure)
    humidity = random.uniform(10, 30)
    altitude = random.randint(0, 1)

    #Send an email when we have a leakage
    
    return jsonify(
        {
            "status": "OK",
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity,
            "altitude": altitude
        }
    )
    
if __name__ == "__main__" :
    app.run(debug=True, host="0.0.0.0")
