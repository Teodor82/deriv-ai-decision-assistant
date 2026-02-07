# Deriv AI Decision Assistant

An explainable AI decision-support assistant for trading.
Built for the Deriv Hackathon.

## What it does
- Accepts a market snapshot and user question
- Provides a plain-language summary
- Highlights risks and uncertainty
- Presents scenario-based thinking (not predictions)

## What it does NOT do
- No auto-trading
- No buy/sell commands
- No financial advice

## Demo Flow
1. User submits market context (EURUSD / Gold)
2. AI returns structured analysis
3. User reviews risks, scenarios, and explanations

## Tech Scope
- Single endpoint: POST /analyze
- Mock-first backend
- Explainability and safety by design

## Documentation
See `/docs` for user stories and mock responses.
