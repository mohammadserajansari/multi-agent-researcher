from crewai import Crew, Process

from agents.tasks import (
    planning_task,
    source_task,
    extraction_task,
    comparison_task,
    writing_task,
    confidence_task,
)


research_crew = Crew(
    agents=[
        planning_task.agent,
        source_task.agent,
        extraction_task.agent,
        comparison_task.agent,
        writing_task.agent,
        confidence_task.agent,
    ],
    tasks=[
        planning_task,
        source_task,
        extraction_task,
        comparison_task,
        writing_task,
        confidence_task,
    ],
    process=Process.sequential,
    verbose=True,
)