from crew_setup import run_travel_planner

destination = "Bali"
interests = "beaches, temples, street food"
num_days = 5
num_people = 2

print("\n📍 Starting Travel Planner...\n")
result = run_travel_planner(destination, interests, num_days, num_people)

print("\n✅ Final Travel Plan:\n")
print(result)
