from crewai import Task
from agents import budget_planner, destination_researcher, docs_advisor, itinerary_designer

# Task 1: Estimate the budget
budget_task = Task(
    description="Estimate the total cost for a {num_days}-day trip to {destination} for {num_people} people, including flights, hotels, food, and attractions.",
    expected_output="Detailed breakdown of estimated travel costs per category (flights, stay, food, activities, extras).",
    agent=budget_planner
)

# Task 2: Research the destination
destination_task = Task(
    description="Research and list the top attractions, experiences, and cultural highlights in {destination} for someone interested in {interests}.",
    expected_output="Curated list of 5–10 attractions or experiences with a short description each.",
    agent=destination_researcher
)

# Task 3: Check documentation requirements
docs_task = Task(
    description="Provide travel documentation requirements for an Indian citizen visiting {destination}. Include visa type, process, and passport validity.",
    expected_output="Clear visa requirements, application steps, and any travel insurance or vaccination mandates.",
    agent=docs_advisor
)

# Task 4: Design the itinerary
itinerary_task = Task(
    description="Based on available budget, documentation requirements, and destination research, create a detailed {num_days}-day itinerary for {destination}. Using the context provided, summarise all the information related to budget, destination and required documents. ",
    expected_output="Day-by-day itinerary with activity suggestions, time allocations, and brief travel guidance. Summarised information of budget estimation, top attractions and documentation requirements with separate headings. "
    "Include Unicode emojis where appropriate to enhance readability and engagement.",
    agent=itinerary_designer,
    context=[budget_task, destination_task, docs_task]
)
