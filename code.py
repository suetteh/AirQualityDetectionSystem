'''
pseudo code

# define a function to calculate air quality
def calculate_air_quality():
    # Define input variables: pm2_5, tvoc, co, no2, temperature,humidity
    # Define output variables: api, tci, iaq

    # Define fuzzy membership functions for inputs and outputs
    # Define complex rules
    # Define a control system

    # Create a loop to get sensor decect inputs
    while True:


# Prompt the sensor decect for input
# Check if the inputs are within valid ranges
# Set the input values for the fuzzy system
# Compute the fuzzy output values and display the results


# Call the function
calculate_air_quality()
'''

from skfuzzy import control as ctrl
import numpy as np #statistics
import skfuzzy as fuzz
import tkinter as tk
from tkinter import messagebox

# Define the function that will be called when the "Calculate" button is pressed
def calculate():
    try:
        # inputs: pm2_5, tvoc, co, no2, temperature,humidity
        pm2_5 = ctrl.Antecedent(np.arange(0, 301, ), 'pm2_5')
        tvoc = ctrl.Antecedent(np.arange(0, 10001, 1), 'tvoc')
        co = ctrl.Antecedent(np.arange(0, 91, 1), 'co')
        no2 = ctrl.Antecedent(np.arange(0, 201, 1), 'no2')
        temperature = ctrl.Antecedent(np.arange(-15, 41, 1), 'temperature')
        humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
        api = ctrl.Consequent(np.arange(0, 11, 0.2), 'api')
        tci = ctrl.Consequent(np.arange(0, 11, 0.2), 'tci')
        iaq = ctrl.Consequent(np.arange(0, 11, 0.2), 'iaq')

        # membership function
        pm2_5['low'] = fuzz.trimf(pm2_5.universe, [0, 0, 25])
        pm2_5['moderate'] = fuzz.trimf(pm2_5.universe, [20, 35, 50])
        pm2_5['high'] = fuzz.trimf(pm2_5.universe, [40, 70, 100])
        pm2_5['very high'] = fuzz.trimf(pm2_5.universe, [80, 190, 300])

        tvoc['low'] = fuzz.trimf(tvoc.universe, [0, 0, 300])
        tvoc['moderate'] = fuzz.trimf(tvoc.universe, [240, 620, 1000])
        tvoc['high'] = fuzz.trimf(tvoc.universe, [800, 1900, 3000])
        tvoc['very high'] = fuzz.trimf(tvoc.universe, [2400, 6200, 10000])

        co['low'] = fuzz.trimf(co.universe, [0, 0, 10])
        co['moderate'] = fuzz.trimf(co.universe, [8, 19, 30])
        co['high'] = fuzz.trimf(co.universe, [24, 37, 50])
        co['very high'] = fuzz.trimf(co.universe, [40, 65, 90])

        no2['low'] = fuzz.trimf(no2.universe, [0, 0, 40])
        no2['moderate'] = fuzz.trimf(no2.universe, [32, 56, 80])
        no2['high'] = fuzz.trimf(no2.universe, [64, 92, 120])
        no2['very high'] = fuzz.trimf(no2.universe, [96, 148, 200])

        temperature['low'] = fuzz.trimf(temperature.universe, [-15, -15, 20])
        temperature['moderate'] = fuzz.trimf(temperature.universe, [16, 20, 24])
        temperature['high'] = fuzz.trimf(temperature.universe, [19, 26, 32])
        temperature['very high'] = fuzz.trimf(temperature.universe, [26, 33, 40])

        humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 40])
        humidity['moderate'] = fuzz.trimf(humidity.universe, [32, 46, 60])
        humidity['high'] = fuzz.trimf(humidity.universe, [48, 64, 80])
        humidity['very high'] = fuzz.trimf(humidity.universe, [64, 82, 100])

        api['good'] = fuzz.trimf(api.universe, [0, 2, 4])
        api['moderate'] = fuzz.trimf(api.universe, [3.2, 4.6, 6])
        api['unhealthy'] = fuzz.trimf(api.universe, [4.8, 6.4, 8])
        api['hazardous'] = fuzz.trimf(api.universe, [6.4, 8.2, 10])

        tci['good'] = fuzz.trimf(tci.universe, [0, 0, 4])
        tci['moderate'] = fuzz.trimf(tci.universe, [3.2, 4.6, 6])
        tci['unhealthy'] = fuzz.trimf(tci.universe, [4.8, 6.4, 8])
        tci['hazardous'] = fuzz.trimf(tci.universe, [6.4, 8.2, 10])

        iaq['excellent'] = fuzz.trimf(iaq.universe, [0, 0, 4])
        iaq['good'] = fuzz.trimf(iaq.universe, [3.2, 4.6, 6])
        iaq['unhealthy'] = fuzz.trimf(iaq.universe, [4.8, 6.4, 8])
        iaq['hazardous'] = fuzz.trimf(iaq.universe, [6.4, 8.2, 10])

        # graph
        pm2_5.view()
        tvoc.view()
        co.view()
        no2.view()
        temperature.view()
        humidity.view()
        api.view()
        tci.view()
        iaq.view()

        # Define complex rules
        #####################################################################################################################
        ##RULES for pm2.5,tvoc,co and no2
        # generate api
        # R1: if pm2_5 is low or tvoc is low or co is low or no2 is low THEN api is good
        rule1 = ctrl.Rule(pm2_5['low'] | tvoc['low'] | co['low'] | no2['low'], api['good'])
        # R2: if pm2_5 is moderate or tvoc is moderate or co is moderate or no2 is moderate THEN api is moderate
        rule2 = ctrl.Rule(pm2_5['moderate'] | tvoc['moderate'] | co['moderate'] | no2['moderate'], api['moderate'])
        # R3: if pm2_5 is high or tvoc is high or co is high or no2 is high THEN api is unhealthy
        rule3 = ctrl.Rule(pm2_5['high'] | tvoc['high'] | co['high'] | no2['high'], api['unhealthy'])
        # R4: if pm2_5 is very high or tvoc is very high or co is very high or no2 is very high THEN api is hazardous
        rule4 = ctrl.Rule(pm2_5['very high'] | tvoc['very high'] | co['very high'] | no2['very high'], api['hazardous'])

        # create the control system for API (inference - for evaluation later)
        apiControlSystem = ctrl.ControlSystem(rules=[rule1, rule2, rule3, rule4])

        api_sim = ctrl.ControlSystemSimulation(apiControlSystem)

        #############################################################################################
        # RULES for temp and humidity
        # generate tci
        # R5: if temperature is low or humidity is low THEN tci is unhealthy
        rule5 = ctrl.Rule(temperature['low'] | humidity['low'], tci['unhealthy'])
        # R6: if temperature is moderate or humidity is moderate THEN tci is good
        rule6 = ctrl.Rule(temperature['moderate'] | humidity['moderate'], tci['good'])
        # R7: if temperature is high and humidity is moderate THEN tci is moderate
        rule7 = ctrl.Rule(temperature['high'] & humidity['moderate'], tci['moderate'])
        # R8: if temperature is high or humidity is high THEN tci is hazardous
        rule8 = ctrl.Rule(temperature['high'] | humidity['high'], tci['hazardous'])
        # R9: if temperature is very high or humidity is very high THEN tci is hazardous
        rule9 = ctrl.Rule(temperature['very high'] | humidity['very high'], tci['hazardous'])

        # create the control system (inference - for evaluation later)
        tci_ctrl = ctrl.ControlSystem(rules=[rule5, rule6, rule7, rule8, rule9])

        tci_sim = ctrl.ControlSystemSimulation(tci_ctrl)

        ####################################################################################################################
        ## Input:api and tci Output:iaq
        ##RULES for api and tci
        # generate iaq
        # R10: if api is good or tci is good THEN iaq is excellent
        rule10 = ctrl.Rule(api['good'] | tci['good'], iaq['excellent'])
        # R11: if api is moderate or tci is moderate THEN iaq is good
        rule11 = ctrl.Rule(api['moderate'] | tci['moderate'], iaq['good'])

        # R12: if api is unhealthy or tci is unhealthy THEN iaq is unhealthy
        rule12 = ctrl.Rule(api['unhealthy'] | tci['unhealthy'], iaq['unhealthy'])
        # R13: if api is hazardous or tci is hazardous THEN iaq is hazardous
        rule13 = ctrl.Rule(api['hazardous'] | tci['hazardous'], iaq['hazardous'])

        # Control System Creation and Simulation
        iaq_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11,
                                    rule12, rule13])

        #iaq_ctrl = ctrl.ControlSystem([rule10, rule11, rule12, rule13])
        iaq_sim = ctrl.ControlSystemSimulation(iaq_ctrl)

        # Get the sensor decect input values
        pm25_input = float(pm25_entry.get())
        tvoc_input = float(tvoc_entry.get())
        co_input = float(co_entry.get())
        no2_input = float(no2_entry.get())
        temp_input = float(temp_entry.get())
        humd_input = float(humd_entry.get())

        # Check if the inputs are within valid ranges
        if pm25_input < 0 or pm25_input > 300 or tvoc_input < 0 or tvoc_input > 10000 or \
                co_input < 0 or co_input > 90 or no2_input < 0 or no2_input > 200 or \
                temp_input < -15 or temp_input > 40 or humd_input < 0 or humd_input > 100:
            messagebox.showerror("Invalid Input",
                                 "Please enter a number between the specified range for each parameter.")
            return

        # Set the input values for the fuzzy system
        api_sim.input['pm2_5'] = pm25_input
        api_sim.input['tvoc'] = tvoc_input
        api_sim.input['co'] = co_input
        api_sim.input['no2'] = no2_input
        tci_sim.input['temperature'] = temp_input
        tci_sim.input['humidity'] = humd_input

        # Compute the fuzzy output values and display the results
        api_sim.compute()
        api_canvas.delete("all")
        api_canvas.create_image(0, 0, anchor="nw", image=api_image)
        api.view(sim=api_sim, canvas=api_canvas)

        tci_sim.compute()
        tci_canvas.delete("all")
        tci_canvas.create_image(0, 0, anchor="nw", image=tci_image)
        tci.view(sim=tci_sim, canvas=tci_canvas)

        #iaq_sim.input['api'] = api_output['api']
        #iaq_sim.input['tci'] = tci_output['tci']
        iaq_sim.compute()
        iaq_canvas.delete("all")
        iaq_canvas.create_image(0, 0, anchor="nw", image=iaq_image)
        iaq.view(sim=iaq_sim, canvas=iaq_canvas)

        api_label.config(text="API value: " + str(api_sim.output['api']))
        tci_label.config(text="TCI value: " + str(tci_sim.output['tci']))
        iaq_label.config(text="iaq value: " + str(iaq_sim.output['iaq']))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for each parameter.")
        return


# Create the GUI window
window = tk.Tk()
window.title("Air Quality Index Calculator")

# Create the GUI widgets
pm25_label = tk.Label(window, text="pm2.5 value (between 0 and 300, like: 0,35,75,80): ")
pm25_entry = tk.Entry(window)
pm25_label.grid(row=0, column=0)
pm25_entry.grid(row=0, column=1)

tvoc_label = tk.Label(window, text="tvoc value (between 0 and 10000, like: 0,620,1900,6200): ")
tvoc_entry = tk.Entry(window)
tvoc_label.grid(row=1, column=0)
tvoc_entry.grid(row=1, column=1)

co_label = tk.Label(window, text="co value (between 0 and 90, like: 0,19,37,40): ")
co_entry = tk.Entry(window)
co_label.grid(row=2, column=0)
co_entry.grid(row=2, column=1)

no2_label = tk.Label(window, text="no2 value (between 0 and 200, like: 0,56,92,148): ")
no2_entry = tk.Entry(window)
no2_label.grid(row=3, column=0)
no2_entry.grid(row=3, column=1)

temp_label = tk.Label(window, text="temperature value (between -15 and 40, like: -15,20,26,33): ")
temp_entry = tk.Entry(window)
temp_label.grid(row=4, column=0)
temp_entry.grid(row=4, column=1)

humd_label = tk.Label(window, text="humidity value (between 0 and 100, like: 0,46,64,82): ")
humd_entry = tk.Entry(window)
humd_label.grid(row=5, column=0)
humd_entry.grid(row=5, column=1)

calc_button = tk.Button(window, text="Calculate", command=calculate)
calc_button.grid(row=6, column=0)

# Create a canvas to display the fuzzy output
api_canvas = tk.Canvas(window, width=300, height=300)
api_canvas.grid(row=7, column=0)
api_image = tk.PhotoImage(file="api.png")
api_canvas.create_image(0, 0, anchor="nw", image=api_image)

tci_canvas = tk.Canvas(window, width=300, height=300)
tci_canvas.grid(row=7, column=1)
tci_image = tk.PhotoImage(file="tci.png")
tci_canvas.create_image(0, 0, anchor="nw", image=tci_image)

iaq_canvas = tk.Canvas(window, width=300, height=300)
iaq_canvas.grid(row=7, column=2)
iaq_image = tk.PhotoImage(file="iaq.png")
iaq_canvas.create_image(0, 0, anchor="nw", image=iaq_image)

# Create labels to display the calculated values
api_label = tk.Label(window, text="API value:")
api_label.grid(row=8, column=0)
tci_label = tk.Label(window, text="TCI value:")
tci_label.grid(row=8, column=1)
iaq_label = tk.Label(window, text="iaq value:")
iaq_label.grid(row=8, column=2)

# Run the GUI
window.mainloop()