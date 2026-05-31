from crewai import Agent

from core.llm_manager import llm

# extractor_agent = Agent(
#     role="Information Extractor",
#     goal="""
#     Extract key insights, entities, metrics,
#     and factual information from collected data.
#     """,
#     backstory="""
#     NLP specialist focused on extracting relevant,
#     high-quality structured information.
#     """,
#     llm=llm,
#     verbose=True,
# )



# =====================================================
# Information Extractor Agent
# =====================================================
extractor_agent = Agent(
    role="Information Extractor",
    goal="""
    Extract key insights, entities, metrics, quantitative statistics, and factual claims 
    exclusively from the raw data gathered by the Source Gatherer. Ensure no data from 
    the original files is lost or generalized.
    """,
    backstory="""
    NLP specialist focused on extracting hyper-specific, high-quality structured 
    information. You avoid summarizing data into generic placeholders, preferring 
    to extract real numbers, strict timelines, and exact names found in the sources.
    """,
    llm=llm,
    verbose=True,
)

