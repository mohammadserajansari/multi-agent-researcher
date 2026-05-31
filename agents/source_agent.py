# from crewai import Agent
# from core.llm_manager import llm
# from tools.tavily_search import tavily_search

# source_gatherer_agent = Agent(
#     role="Source Gatherer",
#     goal="""
#     Collect data from internet search, PDFs, HTML,
#     TXT, CSV, and Excel files.
#     """,
#     backstory="""
#     Expert data collector specialized in structured
#     and unstructured information gathering.
#     """,
#     llm=llm,
#     tools=[tavily_search],
#     verbose=True,
# )


from crewai import Agent

from core.llm_manager import llm
from tools.tavily_search import tavily_search


# source_gatherer_agent = Agent(
#     role="Source Gatherer",

#     goal="""
#     Gather information from internet and files.
#     """,

#     backstory="""
#     Expert internet researcher and data collector.
#     """,

#     llm=llm,

#     tools=[tavily_search],

#     verbose=True
# )



# =====================================================
# Source Gatherer Agent
# =====================================================
source_gatherer_agent = Agent(
    role="Primary Source and Document Collector",
    goal="""
    Ingest, analyze, and extract core findings from the user's provided file strings 
    first. Treat these files as the absolute source of truth. Use the Tavily internet 
    search tool only to supplement missing updates, verify facts, or fill context gaps.
    """,
    backstory="""
    Expert data collector who prioritizes local source materials over generic 
    web results. You carefully isolate the facts buried within text strings, PDFs, 
    spreadsheets, and HTML documents provided directly in your task context.
    """,
    llm=llm,
    tools=[tavily_search],
    verbose=True,
)

