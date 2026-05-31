from crewai import Agent
# from core.llm_manager import llm
from core.llm_manager import llm_manager
llm = llm_manager.get_llm()

# confidence_agent = Agent(
#     role="Confidence Evaluator",
#     goal="""
#     Evaluate confidence score based on source quality,
#     consistency, completeness, and evidence strength.
#     """,
#     backstory="""
#     AI evaluator specialized in factual consistency
#     and reliability assessment.
#     """,
#     llm=llm,
#     verbose=True,
# )



# =====================================================
# Confidence Evaluator Agent
# =====================================================
confidence_agent = Agent(
    role="Confidence Evaluator",
    goal="""
    Critically audit the generated report's factual alignment with the primary source documents. 
    Evaluate and calculate a confidence score based on consistency, source quality, and 
    evidence strength.
    """,
    backstory="""
    Rigorous AI quality control auditor specialized in factual consistency checking, 
    hallucination detection, and reliability assessment. You verify that every claim made 
    in the final report can be traced back directly to concrete data.
    """,
    llm=llm,
    verbose=True,
)