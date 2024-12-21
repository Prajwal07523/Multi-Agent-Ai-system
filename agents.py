from crewai import Agent
from tools import industry_research_tool,use_case_analysis_tool,dataset_search_tool,genai_solution_tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import nest_asyncio


# Patch the current event loop
nest_asyncio.apply()

## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))



# Industry/Company Research Agent
industry_researcher = Agent(
    role="Industry Analyst",
    goal="Identify key trends, challenges, and strategic goals in {company}.",
    verbose=True,
    memory=True,
    backstory=(
        "As an industry expert, you excel in uncovering valuable insights "
        "about industries and companies, helping them leverage AI/GenAI solutions."
    ),
    tools=[industry_research_tool],  # Reference the actual tool object
    llm=llm,
    allow_delegation=True
)

# Market Standards & Use Case Generator Agent
use_case_generator = Agent(
    role="AI Strategist",
    goal="Propose actionable AI/GenAI use cases to improve operations and customer satisfaction for {company}.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a visionary strategist focused on leveraging the latest AI/ML technologies "
        "to drive innovation and operational excellence."
    ),
    tools=[use_case_analysis_tool],  # Remove trailing space
    llm=llm,
    allow_delegation=True
)

# Resource Asset Collection Agent
resource_collector = Agent(
    role="Data and Resource Specialist",
    goal="Locate relevant datasets, tools, and APIs to support proposed AI/GenAI use cases for {company}.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a meticulous researcher skilled at discovering datasets, tools, and APIs that enable "
        "practical and impactful AI solutions."
    ),
    tools=[dataset_search_tool],  # Reference the actual tool object
    llm=llm,
    allow_delegation=False  # Adjust delegation based on workflow
)

# GenAI Solution Recommendation Agent
genai_recommender = Agent(
    role="Generative AI Innovator",
    goal="Suggest cutting-edge GenAI solutions for document search, automated reporting, and customer engagement for {company}.",
    verbose=True,
    memory=True,
    backstory=(
        "As a forward-thinking innovator, you specialize in proposing advanced "
        "Generative AI solutions that redefine customer and operational experiences."
    ),
    tools=[genai_solution_tool],  # Reference the actual tool object
    llm=llm,
    allow_delegation=False
)
