import os
from dotenv import load_dotenv
from crewai import Crew, Process
from tasks import industry_researcher_task, use_case_generator_task, dataset_search_task, genai_solution_task
from agents import industry_researcher, use_case_generator, resource_collector, genai_recommender
import streamlit as st

# Load environment variables
load_dotenv()

crew = Crew(
    agents=[industry_researcher, use_case_generator, resource_collector, genai_recommender],
    tasks=[industry_researcher_task, use_case_generator_task, dataset_search_task, genai_solution_task],
    process=Process.sequential,
)

result=crew.kickoff(inputs={'company':'Google'})
print(result)


# import os
# import gradio as gr
# from dotenv import load_dotenv
# from crewai import Crew, Process
# from tasks import (
#     industry_researcher_task,
#     use_case_generator_task,
#     dataset_search_task,
#     genai_solution_task,
# )
# from agents import (
#     industry_researcher,
#     use_case_generator,
#     resource_collector,
#     genai_recommender,
# )
# import asyncio

# # Load environment variables
# load_dotenv()

# # Initialize Crew with agents and tasks
# crew = Crew(
#     agents=[industry_researcher, use_case_generator, resource_collector, genai_recommender],
#     tasks=[industry_researcher_task, use_case_generator_task, dataset_search_task, genai_solution_task],
#     process=Process.sequential,
# )

# # Path where the proposal file will be saved
# OUTPUT_FILE_PATH = 'genai_solutions_proposal.md'


# async def execute_crew_task(inputs: dict) -> dict:
#     """
#     Asynchronous function to execute Crew tasks and save the results to a .md file.
#     """
#     result = await crew.kickoff(inputs=inputs)
    
#     # Save the result to the .md file
#     with open(OUTPUT_FILE_PATH, "w") as file:
#         file.write(result.get("genai_solution_proposal", ""))  # Assuming result contains the proposal
    
#     return OUTPUT_FILE_PATH  # Return the file path for download


# def sync_execute_crew_task(company: str):
#     """
#     Synchronous wrapper for the asynchronous task handler.
#     """
#     try:
#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#         result_file_path = loop.run_until_complete(execute_crew_task({"company": company}))
#         return f"Task executed successfully. Download the result from the link below:", result_file_path
#     except Exception as e:
#         return f"An error occurred: {e}", None


# # Define the Gradio interface
# interface = gr.Interface(
#     fn=sync_execute_crew_task,
#     inputs=gr.Textbox(label="Company Name", placeholder="Enter the company name"),
#     outputs=[gr.Textbox(), gr.File(label="Download GenAI Solution Proposal")],  # Corrected output for both textbox and file
#     title="Crew AI GenAI Solution Proposal Generator",
#     description="Enter a company name to generate a GenAI solution proposal and download it.",
# )

# if __name__ == "__main__":
#     # Launch Gradio app
#     interface.launch(share=False)  # You can change share=True to get a public link
