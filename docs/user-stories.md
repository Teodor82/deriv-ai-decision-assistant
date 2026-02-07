# User Stories – Deriv AI Decision Assistant

## Scope
Decision-support AI only. No auto-trading. No financial advice.

## User Stories

1. Market Snapshot  
As a trader, I want to submit a market snapshot and a question, so that I get a plain-language summary of the current situation.

2. Risk-First Explanation  
As a trader, I want risks and uncertainty highlighted first, so that I avoid overconfidence.

3. Scenario-Based Thinking  
As a trader, I want 2–3 possible scenarios with conditions, so that I think in probabilities, not predictions.

4. Reasoning Transparency  
As a trader, I want a short explanation of why the AI reached its conclusions, so that I can trust its logic.

5. Safe Language  
As a user, I want the assistant to avoid buy/sell commands and state its limits clearly.

6. Clarifying Questions  
As a trader, I want the assistant to ask clarifying questions when input is incomplete.

7. Stable Output Format  
As a builder, I want a consistent JSON response so the demo remains stable.

## Acceptance Criteria

POST /analyze returns:
- summary (string)
- risks (array)
- scenarios (array)
- confidence (number)
- disclaimer (string)
- questions (array)
