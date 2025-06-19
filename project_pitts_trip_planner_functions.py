# This program uses functions to simulate a simple trip planning assistant.
# It includes a personalized greeting, a time rounding feature, and a destination summary with optional transportation mode.

#Building out the initial trip planner function
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0, " + name + "!")
trip_planner_welcome("Pitts")
print("\n")

#Building out a rounded time function
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.5)

#Building destination function
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin + ".")
  print("And you are traveling to " + destination+ ".")
  print("You will be traveling by " + mode_of_transport+ ".")
  print("It will take approximately " + str(estimated_time) + " hours.")
  
destination_setup("BHM", "BKK", 25, "Airport")


