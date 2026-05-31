from crewai import Agent
from core.llm_manager import llm_manager
llm = llm_manager.get_llm()
planner_agent = Agent(
    role="Research Planner",
    goal="""
    Break the user query and any attached local source documentation into 
    structured research tasks, identify required information gaps, and 
    define a highly relevant comparison strategy.
    """,
    backstory="""
    Expert AI research strategist skilled in multi-step planning and analytical 
    workflows. You excel at taking both raw text inputs and specific queries 
    to outline a concrete roadmap without hallucinating boilerplate topics.
    """,
    llm=llm,
    verbose=True,
)

