## https://serper.dev/

from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


from crewai_tools import SerperDevTool

# Tool to search for industry/company insights
industry_research_tool = SerperDevTool(
    name="IndustryResearchTool",
    description=(
        "A tool designed to perform web searches and gather detailed insights about "
        "industries, companies, and market trends. Useful for identifying key offerings, challenges, "
        "and strategies."
    )
)

# Tool for searching AI/ML trends and use cases
use_case_analysis_tool = SerperDevTool(
    name="UseCaseAnalysisTool",
    description=(
        "This tool performs web searches to analyze market standards and industry trends in AI/ML. "
        "It is specialized in identifying relevant use cases for AI/GenAI adoption in specific industries."
    )
)

# Tool for finding datasets
dataset_search_tool = SerperDevTool(
    name="DatasetSearchTool",
    description=(
        "A tool designed to search for datasets and resources related to AI/GenAI use cases. "
        "It searches platforms such as Kaggle, HuggingFace, and GitHub."
    )
)

# Tool for researching GenAI solutions
genai_solution_tool = SerperDevTool(
    name="GenAISolutionTool",
    description=(
        "A tool designed to search for cutting-edge Generative AI solutions such as document search, "
        "automated reporting, and AI-powered customer interaction systems."
    )
)
