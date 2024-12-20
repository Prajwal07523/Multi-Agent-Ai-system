from crewai import Task
from tools import industry_research_tool,use_case_analysis_tool,dataset_search_tool,genai_solution_tool
from agents import industry_researcher,use_case_generator,resource_collector,genai_recommender



# Industry Researcher Task
industry_researcher_task = Task(
    description=(
        "Perform detailed research on the given industry or company. Identify key trends, challenges, "
        "and strategic goals. Analyze competitors and their use of AI/ML technologies."
    ),
    expected_output=(
        "A comprehensive report including: \n"
        "- Industry trends and segmentation. \n"
        "- Key offerings and challenges of the company. \n"
        "- Competitor analysis and their AI strategies."
    ),
    tools=[industry_research_tool],
    agent=industry_researcher,
    output_file='genai_solutions_proposal.md'
)

# Use Case Generator Task
use_case_generator_task = Task(
    description=(
        "Analyze market standards and industry trends to generate actionable AI/GenAI use cases "
        "for the target industry or company. Use the insights gathered from the industry research task."
    ),
    expected_output=(
        "A list of actionable AI/GenAI use cases, including: \n"
        "- Use case descriptions. \n"
        "- The impact on operations, customer experience, or efficiency. \n"
        "- Prioritized list based on feasibility and business value."
    ),
    tools=[use_case_analysis_tool],
    agent=use_case_generator,
    output_file='genai_solutions_proposal.md'
)

# Dataset Search Task
dataset_search_task = Task(
    description=(
        "Locate relevant datasets and tools to support the proposed AI/GenAI use cases. "
        "Search platforms such as Kaggle, HuggingFace, and GitHub for appropriate resources."
    ),
    expected_output=(
        "A collection of datasets and tools with the following details: \n"
        "- Dataset name and description. \n"
        "- Source link (clickable). \n"
        "- Potential usage in implementing the use cases."
    ),
    tools=[dataset_search_tool],
    agent=resource_collector,
    output_file='genai_solutions_proposal.md'
)

# GenAI Solution Task
genai_solution_task = Task(
    description=(
        "Propose cutting-edge GenAI solutions tailored for the given industry/company. "
        "Focus on areas such as document search, automated reporting, and AI-powered customer interaction systems."
    ),
    expected_output=(
        "A detailed proposal of GenAI solutions, including: \n"
        "- Solution descriptions and potential use cases. \n"
        "- Feasibility and expected impact. \n"
        "- Recommendations for tools and frameworks (e.g., LangChain, HuggingFace models)."
    ),
    tools=[genai_solution_tool],
    agent=genai_recommender,
    async_execution=False,
    output_file='genai_solutions_proposal.md'
)
