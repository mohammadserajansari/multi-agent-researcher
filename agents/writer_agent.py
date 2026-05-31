from crewai import Agent

from core.llm_manager import llm_manager
llm = llm_manager.get_llm()
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

