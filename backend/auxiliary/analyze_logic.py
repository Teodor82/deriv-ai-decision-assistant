"""Business logic for analyze route."""
import json
from typing import Dict, Any, Tuple, List, Optional
from clients.gemini_client import GeminiClient


def build_analysis_prompt(asset: str, timeframe: int, market_context: Dict[str, str], optional_data: Optional[Any] = None) -> str:
    """
    Build a structured prompt for the Gemini AI client.
    
    Args:
        asset: Asset symbol
        timeframe: Trading timeframe in minutes
        market_context: Dict with trend, range, volatility, recent_move
        optional_data: Optional additional market data
        
    Returns:
        Formatted prompt string
    """
    context_info = f"""
Asset: {asset}
Timeframe: {timeframe} minutes
Market Context:
  - Trend: {market_context.get('trend', 'Unknown')}
  - Range: {market_context.get('range', 'Unknown')}
  - Volatility: {market_context.get('volatility', 'Unknown')}
  - Recent Move: {market_context.get('recent_move', 'Unknown')}
"""

    if optional_data:
        context_info += f"\nAdditional Data:\n{json.dumps(optional_data, indent=2)}\n"

    prompt = f"""{context_info}

Based on the above market context, provide a concise trading analysis in the following JSON format:
{{
  "summary": "A 1-2 sentence summary of the current market situation and momentum",
  "risks": [
    "First risk",
    "Second risk",
    "Third risk"
  ],
  "scenarios": [
    {{
      "name": "Bull case",
      "conditions": "Specific conditions for this scenario",
      "implications": "Trading implications if this scenario plays out"
    }},
    {{
      "name": "Base case",
      "conditions": "Specific conditions for this scenario",
      "implications": "Trading implications if this scenario plays out"
    }},
    {{
      "name": "Bear case",
      "conditions": "Specific conditions for this scenario",
      "implications": "Trading implications if this scenario plays out"
    }}
  ],
  "confidence": 0.0 to 1.0 (a single decimal number representing model confidence in the analysis),
  "disclaimer": "A brief risk disclaimer emphasizing this is decision support only, not financial advice",
  "questions": [
    "A clarifying question for the trader",
    "Another clarifying question"
  ]
}}

Ensure the response is valid JSON and focuses on actionable, practical insights for the trader."""
    
    return prompt


async def perform_analysis(
    asset: str,
    timeframe: int,
    market_context: Dict[str, str],
    optional_data: Optional[Any] = None
) -> Dict[str, Any]:
    """
    Full analysis flow: build prompt and call Gemini to get structured analysis.

    Args:
        asset: Asset symbol (e.g., 'EURUSD')
        timeframe: Timeframe in minutes
        market_context: Dict with trend, range, volatility, recent_move
        optional_data: Optional additional market data

    Returns:
        Structured analysis response as dictionary
    """
    # Build the prompt for Gemini
    prompt = build_analysis_prompt(asset, timeframe, market_context, optional_data)

    # Call Gemini client
    client = GeminiClient()
    ai_response = await client.generate(prompt)

    # Parse the JSON response from Gemini
    try:
        # Try to extract JSON from the response
        analysis_result = json.loads(ai_response)
        # Ensure all required fields are present
        required_fields = ["summary", "risks", "scenarios", "confidence", "disclaimer", "questions"]
        for field in required_fields:
            if field not in analysis_result:
                raise ValueError(f"Missing required field: {field}")
        return analysis_result
    except json.JSONDecodeError:
        # Fallback if Gemini doesn't return valid JSON
        return {
            "summary": ai_response,
            "risks": ["Unable to parse structured response"],
            "scenarios": [],
            "confidence": 0.0,
            "disclaimer": "Analysis parsing failed; verify independently.",
            "questions": ["Please provide clearer market context data"]
        }
