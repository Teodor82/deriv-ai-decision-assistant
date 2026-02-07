"""Request and response schemas for analyze endpoint."""
from pydantic import BaseModel, Field
from typing import Optional, Any


class MarketContext(BaseModel):
    """Market context information."""
    trend: str = Field(..., description="Current trend (e.g., 'uptrend', 'downtrend', 'sideways')")
    range: str = Field(..., description="Price range (e.g., 'consolidating', 'expanding')")
    volatility: str = Field(..., description="Volatility level (e.g., 'high', 'moderate', 'low')")
    recent_move: str = Field(..., description="Recent price movement description")


class AnalyzeRequest(BaseModel):
    """Request schema for analyze endpoint."""
    asset: str = Field(..., description="Asset symbol (e.g., 'EURUSD', 'Bitcoin')")
    timeframe: int = Field(..., description="Timeframe in minutes (e.g., 60, 240, 1440)")
    market_context: MarketContext = Field(..., description="Current market context")
    data: Optional[Any] = Field(default=None, description="Optional additional market data")


class Scenario(BaseModel):
    """Market scenario."""
    name: str = Field(..., description="Scenario name (e.g., 'Bull case', 'Base case', 'Bear case')")
    conditions: str = Field(..., description="Conditions for this scenario")
    implications: str = Field(..., description="Trading implications")


class AnalyzeResponse(BaseModel):
    """Response schema for analyze endpoint."""
    summary: str = Field(..., description="Market summary")
    risks: list[str] = Field(..., description="List of identified risks")
    scenarios: list[Scenario] = Field(..., description="Market scenarios")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence level (0-1)")
    disclaimer: str = Field(..., description="Risk disclaimer")
    questions: list[str] = Field(..., description="Clarifying questions for trader")
