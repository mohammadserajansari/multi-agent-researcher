# from tavily import TavilyClient
# from core.config import settings


# tavily_client = TavilyClient(
#     api_key=settings.TAVILY_API_KEY
# )


# def tavily_search(query: str):

#     response = tavily_client.search(query=query)

#     final_results = []

#     for result in response.get("results", []):

#         formatted_result = f"""
# Title      : {result.get('title')}
# URL        : {result.get('url')}
# Content    : {result.get('content')}
# Score      : {result.get('score')}
# """

#         final_results.append(formatted_result)

#     return "\n\n".join(final_results)



from crewai.tools import tool

from tavily import TavilyClient

from core.config import settings


tavily_client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)


@tool("Internet Search Tool")
def tavily_search(query: str) -> str:
    """
    Search the internet using Tavily.
    """

    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    final_results = []

    for result in response.get("results", []):

        formatted_result = f"""
Title: {result.get('title')}
URL: {result.get('url')}
Content: {result.get('content')}
Score: {result.get('score')}
"""

        final_results.append(formatted_result)

    return "\n\n".join(final_results)