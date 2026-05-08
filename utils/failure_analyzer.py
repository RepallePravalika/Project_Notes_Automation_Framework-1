import re
from utils.mcp_client import mcp_client
from utils.logger import logger

class FailureAnalyzer:
    """
    LLM-powered test failure analysis layer.
    Analyzes exception messages and provides AI-powered insights and solutions.
    """
    
    # Fallback static patterns
    PATTERNS = {
        r"TimeoutException": {
            "insight": "Slow-loading element or network latency detected.",
            "action": "Consider increasing the WebDriverWait timeout."
        },
        r"NoSuchElementException": {
            "insight": "The target element was not found in the DOM.",
            "action": "Check if the locator is still valid."
        },
        r"401": {
            "insight": "API Authentication failed (Unauthorized).",
            "action": "Check bearer token validity."
        }
    }

    @staticmethod
    def analyze(error_message, context=""):
        """
        Analyzes the error message using LLM with fallback.
        """
        error_str = str(error_message)
        
        # Try LLM first
        llm_analysis = mcp_client.analyze_failure(error_str, context)
        
        if llm_analysis:
            logger.info("Retrieved failure analysis from LLM.")
            # Simple parsing of LLM response (expecting Insight: and Suggested Action:)
            insight = "AI analysis provided below."
            action = "See insight for details."
            
            if "Insight:" in llm_analysis:
                parts = llm_analysis.split("Suggested Action:")
                insight = parts[0].replace("Insight:", "").strip()
                if len(parts) > 1:
                    action = parts[1].strip()
                else:
                    action = llm_analysis # Fallback if split fails
            
            return {
                "status": "AI Analysis Complete (LLM)",
                "detected_issue": "Dynamic Analysis",
                "insight": insight,
                "suggested_action": action,
                "raw_llm_output": llm_analysis
            }

        # Fallback to pattern matching
        for pattern, info in FailureAnalyzer.PATTERNS.items():
            if re.search(pattern, error_str, re.IGNORECASE):
                return {
                    "status": "AI Analysis Complete (Pattern)",
                    "detected_issue": pattern,
                    "insight": info["insight"],
                    "suggested_action": info["action"]
                }
        
        return {
            "status": "Analysis Complete (Limited)",
            "detected_issue": "Unknown Pattern",
            "insight": "No specific pattern matched and LLM was unavailable.",
            "suggested_action": "Manually inspect logs."
        }
