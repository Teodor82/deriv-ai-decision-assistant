"""Analyze routes."""
from fastapi import APIRouter, HTTPException
from auxiliary.analyze_logic import perform_analysis
from models.analyze import AnalyzeRequest, AnalyzeResponse

router = APIRouter(prefix="/analyze", tags=["analyze"])


@router.post("/", response_model=AnalyzeResponse, name="Analyze Market")
async def analyze(request: AnalyzeRequest):
    """
    Analyze market conditions and provide decision support.
    
    Takes asset, timeframe, market context, and optional data;
    returns structured analysis with summary, risks, scenarios, confidence, and questions.
    """
    try:
        # Perform analysis using the new structure
        analysis_result = await perform_analysis(
            asset=request.asset,
            timeframe=request.timeframe,
            market_context=request.market_context.model_dump(),
            optional_data=request.data
        )

        return AnalyzeResponse(**analysis_result)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
