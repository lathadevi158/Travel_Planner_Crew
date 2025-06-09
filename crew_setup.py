from crewai import Crew, Process
import warnings, os
from tasks import budget_task, destination_task, docs_task, itinerary_task
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm = AzureChatOpenAI(
    deployment_name=os.getenv("AZURE_DEPLOYMENT_NAME"),
    model_name=os.getenv("AZURE_MODEL_NAME"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_API_VERSION"),
    openai_api_key=os.getenv("AZURE_API_KEY"),
    temperature=0
)

def run_travel_planner(destination, interests, num_days, num_people):
    # Fill placeholders in task descriptions
    budget_task.description = budget_task.description.format(destination=destination, num_days=num_days, num_people=num_people)
    destination_task.description = destination_task.description.format(destination=destination, interests=interests)
    docs_task.description = docs_task.description.format(destination=destination)
    itinerary_task.description = itinerary_task.description.format(destination=destination, num_days=num_days)

    # Setup crew
    crew = Crew(
        agents=[
            budget_task.agent,
            destination_task.agent,
            docs_task.agent,
            itinerary_task.agent
        ],
        tasks=[
            budget_task,
            destination_task,
            docs_task,
            itinerary_task
        ],
        process=Process.sequential,
        llm=llm,
        verbose=True
    )

    return crew.kickoff()
