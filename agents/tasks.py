# from crewai import Task
# from agents.planner_agent import planner_agent
# from agents.source_agent import source_gatherer_agent
# from agents.extractor_agent import extractor_agent
# from agents.comparator_agent import comparator_agent
# from agents.writer_agent import writer_agent
# from agents.confidence_scoring_agent import confidence_agent


# # =====================================================
# # Planner Task
# # =====================================================

# planning_task = Task(
#     description="""
#     Analyze the user query and create a detailed
#     research execution plan.

#     Include:
#     - research objectives
#     - required sources
#     - comparison strategy
#     - extraction requirements
#     """,
#     expected_output="""
#     Structured research plan.
#     """,
#     agent=planner_agent,
# )


# # =====================================================
# # Source Gathering Task
# # =====================================================

# source_task = Task(
#     description="""
#     Gather information from:
#     - Internet search (Tavily)
#     - PDF documents
#     - HTML files
#     - CSV files
#     - Excel files
#     - TXT files

#     Collect all relevant raw data.
#     """,
#     expected_output="""
#     Combined raw research data from all sources.
#     """,
#     agent=source_gatherer_agent,
# )


# # =====================================================
# # Extraction Task
# # =====================================================

# extraction_task = Task(
#     description="""
#     Extract key findings, metrics, entities,
#     statistics, trends, and claims from all data.
#     """,
#     expected_output="""
#     Structured extracted insights.
#     """,
#     agent=extractor_agent,
# )


# # =====================================================
# # Comparison Task
# # =====================================================

# comparison_task = Task(
#     description="""
#     Compare all extracted data.

#     Identify:
#     - similarities
#     - differences
#     - contradictions
#     - trends
#     - missing information
#     """,
#     expected_output="""
#     Detailed comparative analysis.
#     """,
#     agent=comparator_agent,
# )


# # =====================================================
# # Report Writing Task
# # =====================================================

# writing_task = Task(
#     description="""
#     Generate a final professional research report.

#     Include:
#     - executive summary
#     - methodology
#     - findings
#     - comparison tables
#     - conclusions
#     - recommendations
#     """,
#     expected_output="""
#     Final detailed research report.
#     """,
#     agent=writer_agent,
# )


# # =====================================================
# # Confidence Scoring Task
# # =====================================================

# confidence_task = Task(
#     description="""
#     Evaluate overall confidence and reliability
#     of the generated report.

#     Score based on:
#     - source quality
#     - consistency
#     - evidence support
#     - completeness
#     """,
#     expected_output="""
#     Confidence score with justification.
#     """,
#     agent=confidence_agent,
# )



from crewai import Task
from agents.planner_agent import planner_agent
from agents.source_agent import source_gatherer_agent
from agents.extractor_agent import extractor_agent
from agents.comparator_agent import comparator_agent
from agents.writer_agent import writer_agent
from agents.confidence_scoring_agent import confidence_agent


# =====================================================
# Planner Task
# =====================================================
planning_task = Task(
    description="""
    Analyze the user query: "{query}" 
    
    If the user has attached local data files, review the extracted text contents here:
    "{loaded_data}"

    Break this query (and any provided document context) into structured research tasks.
    Identify required additional web sources, and define a clear comparison strategy.

    Include:
    - research objectives
    - required sources (both the provided files and needed web updates)
    - comparison strategy
    - extraction requirements
    """,
    expected_output="""
    Structured research plan.
    """,
    agent=planner_agent,
)


# =====================================================
# Source Gathering Task
# =====================================================
source_task = Task(
    description="""
    Your objective is to assemble all raw data required for the user's request: "{query}".
    
    CRITICAL: First, ingest the text content extracted from the user's uploaded local documents:
    "{loaded_data}"
    
    Treat these documents as your primary source of truth. After analyzing this provided data,
    use your internet search tool (Tavily) to gather missing information, update statistics,
    or fact-check variables as required by the research plan.
    """,
    expected_output="""
    Combined raw research data prioritizing the uploaded local documents, supplemented by web search results.
    """,
    agent=source_gatherer_agent,
    context=[planning_task]  # Feeds the research plan context into this task
)


# =====================================================
# Extraction Task
# =====================================================
extraction_task = Task(
    description="""
    Review the combined raw research data gathered in the previous step. 
    Extract key findings, metrics, entities, statistics, trends, and claims from all data. 
    Ensure that specific data structures, numbers, and facts from the user's uploaded files are preserved.
    """,
    expected_output="""
    Structured extracted insights.
    """,
    agent=extractor_agent,
    context=[source_task]  # Ensures the gathered raw file/web data is handed directly to the extractor
)


# =====================================================
# Comparison Task
# =====================================================
comparison_task = Task(
    description="""
    Compare all extracted data from the documents and web resources.

    Identify:
    - similarities
    - differences
    - contradictions
    - trends
    - missing information
    """,
    expected_output="""
    Detailed comparative analysis.
    """,
    agent=comparator_agent,
    context=[extraction_task]  # Hands extracted insights directly to the comparator
)


# =====================================================
# Report Writing Task
# =====================================================
writing_task = Task(
    description="""
    Generate a final professional research report based on the comparative analysis. 
    Ensure the final narrative directly answers the core user request and stays strictly grounded 
    in the facts provided across the uploaded source materials. Do not use generic placeholders.

    Include:
    - executive summary
    - methodology
    - findings
    - comparison tables
    - conclusions
    - recommendations
    """,
    expected_output="""
    Final detailed research report.
    """,
    agent=writer_agent,
    context=[comparison_task]  # Hands the final comparison structure directly to the writer
)


# =====================================================
# Confidence Scoring Task
# =====================================================
confidence_task = Task(
    description="""
    Evaluate overall confidence and reliability of the generated report.
    Verify that the final output accurately represents the information found within the original source files.

    Score based on:
    - source quality
    - consistency
    - evidence support
    - completeness
    """,
    expected_output="""
    Confidence score with justification.
    """,
    agent=confidence_agent,
    context=[writing_task]  # Hands the drafted report to the grader for validation
)