"""
Deep Research Search Window
A search interface for LLM-powered deep research
"""

from abstra.forms import Page


def create_search_window():
    """
    Creates and displays a search window page for deep research queries.

    Returns:
        dict: Contains the search query and research parameters
    """
    page = Page()

    # Page header
    page.heading("🔍 Deep Research Search")
    page.text("Enter your research query below and let AI conduct comprehensive research for you.")

    # Main search input
    query = page.text_input(
        label="Research Query",
        placeholder="What would you like to research? (e.g., 'Impact of AI on healthcare')",
        required=True
    )

    # Research type selector
    research_type = page.dropdown(
        label="Research Type",
        options=[
            {"label": "General Research", "value": "general"},
            {"label": "Academic Papers", "value": "academic"},
            {"label": "News & Current Events", "value": "news"},
            {"label": "Technical Documentation", "value": "technical"},
            {"label": "Market Analysis", "value": "market"}
        ],
        initial_value="general"
    )

    # Research depth
    depth = page.dropdown(
        label="Research Depth",
        options=[
            {"label": "Quick Overview", "value": "quick"},
            {"label": "Standard Analysis", "value": "standard"},
            {"label": "Deep Dive", "value": "deep"}
        ],
        initial_value="standard"
    )

    # Optional advanced settings
    page.text("### Advanced Options (Optional)")

    # Date range for research
    include_recent_only = page.checkbox(
        label="Focus on recent information (last 12 months)"
    )

    # Language preference
    language = page.dropdown(
        label="Preferred Language",
        options=[
            {"label": "English", "value": "en"},
            {"label": "中文 (Chinese)", "value": "zh"},
            {"label": "Any Language", "value": "any"}
        ],
        initial_value="any"
    )

    # Number of sources
    max_sources = page.number_input(
        label="Maximum number of sources",
        min=5,
        max=50,
        initial_value=10
    )

    # Submit button
    page.run_button(label="Start Research")

    # Return collected data
    return {
        "query": query,
        "research_type": research_type,
        "depth": depth,
        "include_recent_only": include_recent_only,
        "language": language,
        "max_sources": max_sources
    }


if __name__ == "__main__":
    # Execute the search window
    search_params = create_search_window()

    # Display confirmation
    page = Page()
    page.heading("Research Parameters Collected")
    page.text(f"**Query:** {search_params['query']}")
    page.text(f"**Type:** {search_params['research_type']}")
    page.text(f"**Depth:** {search_params['depth']}")
    page.text(f"**Language:** {search_params['language']}")
    page.text(f"**Max Sources:** {search_params['max_sources']}")
    page.display()

    # TODO: Connect to LLM deep research backend
    # For now, just display the collected parameters
