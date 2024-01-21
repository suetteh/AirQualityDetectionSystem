# Air Quality Detection System (Group Project)

### Introduction
Indoor air quality (IAQ) is an important factor that affects our daily lives.This project attempted to build an Air Quality Detection system using fuzzy logic. 
This system measures Air Pollutant Index (API) and Thermal Comfort Index (TCI) in real-time and send out signal based on the ultimate output achieved. The system is composed of sensors that detect particulate matter 2.5 (PM2.5) on a scale of 0-300 μg/m3, total volatile organic compounds (TVOCs) on a scale of 0-10000 μg/m3, carbon monoxide (CO) on a scale of 0-90 ppm, nitrogen dioxide (NO2) on a scale of 0-200 μg/m3, temperature on a scale of -15°C to 40°C, and humidity on a scale of 0-100 percent.

### Challenges
As this system detects six different input factors, it posed a challenge to set the rules which covers all possible conditions which in turn generate a precise output.

### Tools Used
This controller utilizes the Mamdani Fuzzy Inference System. When the input variable is passed into the system, the crisp value will be changed into a fuzzy value through the fuzzification process. This process is achieved based on the membership functions. Next, rules are evaluated in parallel and generate the fuzzy output. The outputs of all rules are then aggregated into a single fuzzy set and the fuzzy value is finally converted to crisp output using the centroid defuzzification method.

### Possible Improvement
Overall, the controller is able to generate the expected results based on the input values and fuzzy membership classifications. However, there are still room for improvement. Firstly, even though the current rules set is in line with the UNEP’s concept which Air Quality Index is directly dependent on the density of air pollutants, but additional rules can be introduced to the system to ensure the overall condition possibilities is covered and more precise output can be generated. In terms of the coding, separate try-except blocks should be included in different sections for easier error handling purpose.

### Conclusion
An air quality detection system has been developed using rule based fuzzy logic. This system will help user to understand the indoor air quality and take appropriate action when the air quality level is detected as unhealthy or hazardous. The system takes in readings of PM2.5, TVOC, CO, NO2, temperature and humidity from the sensor and generate API and TCI readings which are then passed into the system and generate the indoor air quality output. With the output value, the user will get to know the indoor air quality status.
