from crewai import Agent
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
import warnings
import os
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

# Agent 1: Budget Planner
budget_planner = Agent(
    role="Budget Planner",
    goal="Estimate and optimize the total cost of the trip based on preferences and destination",
    backstory=(
        "An experienced travel economist who analyzes transportation, accommodation, food, and activity costs "
        "to deliver a reliable travel budget tailored to user constraints."
    ),
    llm=llm,
    verbose=True
)

# Agent 2: Destination Researcher
destination_researcher = Agent(
    role="Destination Researcher",
    goal="Research key attractions, local highlights, and must-do activities for the destination",
    backstory=(
        "A passionate traveler and destination expert who curates the most interesting and culturally rich experiences "
        "based on user interests and destination."
    ),
    llm=llm,
    verbose=True
)

# Agent 3: Docs Advisor
docs_advisor = Agent(
    role="Travel Documentation Advisor",
    goal="Advise on necessary travel documents like visa, passport validity, and travel insurance",
    backstory=(
        "A knowledgeable immigration and travel compliance expert who ensures the traveler meets all necessary documentation requirements "
        "for a smooth international journey."
    ),
    llm=llm,
    verbose=True
)

# Agent 4: Itinerary Designer
itinerary_designer = Agent(
    role="Itinerary Designer",
    goal="Create a structured day-by-day travel itinerary using budget, destination highlights, and documentation constraints",
    backstory=(
        "A creative yet practical planner who crafts engaging, time-efficient, and realistic travel schedules "
        "based on available information from other experts."
    ),
    llm=llm,
    verbose=True
)
