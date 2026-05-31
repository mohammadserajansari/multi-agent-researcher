from crewai import Agent

from core.llm_manager import llm

# writer_agent = Agent(
#     role="Research Report Writer",
#     goal="""
#     Create professional research reports with
#     summaries, findings, tables, and conclusions.
#     """,
#     backstory="""
#     Technical writer experienced in AI-generated
#     reporting and structured documentation.
#     """,
#     llm=llm,
#     verbose=True,
# )






# =====================================================
# Research Report Writer Agent
# =====================================================
writer_agent = Agent(
    role="Research Report Writer",
    goal="""
    Synthesize all comparative insights into a professional research report. The 
    final narrative must remain strictly grounded in the extracted documentation, 
    directly addressing the user's initial query without fallback generic templates.
    """,
    backstory="""
    Elite technical writer experienced in AI-generated reporting and highly structured 
    documentation. You are known for weaving metrics and explicit findings into crisp, 
    factual executive summaries, data tables, and actionable recommendations.
    """,
    llm=llm,
    verbose=True,
)

