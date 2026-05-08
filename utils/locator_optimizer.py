from utils.mcp_client import mcp_client
from utils.logger import logger

class LocatorOptimizer:
    """
    LLM-powered locator optimization utility.
    Suggests robust locators based on failed attempts and HTML structure.
    """
    
    @staticmethod
    def suggest_improvements(failed_locator, html_snippet=""):
        """
        Requests LLM to suggest better locators.
        """
        logger.info(f"Suggesting improvements for locator: {failed_locator}")
        
        suggestions = mcp_client.optimize_locator(failed_locator, html_snippet)
        
        if suggestions:
            return {
                "status": "Suggestions Generated",
                "original_locator": failed_locator,
                "ai_suggestions": suggestions
            }
        
        return {
            "status": "Failed to generate suggestions",
            "message": "LLM was unable to provide alternatives or API key is missing."
        }

if __name__ == "__main__":
    # Example usage for manual testing
    sample_html = '<button id="btn-123" class="btn btn-primary" data-testid="login-submit">Login</button>'
    result = LocatorOptimizer.suggest_improvements("#btn-123", sample_html)
    print(f"Original: {result['original_locator']}")
    print(f"Suggestions:\n{result.get('ai_suggestions', 'N/A')}")
