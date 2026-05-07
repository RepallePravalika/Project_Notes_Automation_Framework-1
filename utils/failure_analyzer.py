import re

class FailureAnalyzer:
    """
    LLM-assisted test failure analysis layer.
    Analyzes exception messages and provides AI-powered insights and solutions.
    """
    
    PATTERNS = {
        r"TimeoutException": {
            "insight": "Slow-loading element or network latency detected.",
            "action": "Consider increasing the WebDriverWait timeout or checking server response time."
        },
        r"NoSuchElementException": {
            "insight": "The target element was not found in the DOM.",
            "action": "Check if the locator is still valid or if the element is inside an iframe/shadow DOM."
        },
        r"ElementClickInterceptedException": {
            "insight": "Another element (like a loader or popup) is blocking the click.",
            "action": "Wait for the overlay to disappear or use a JavaScript fallback click."
        },
        r"StaleElementReferenceException": {
            "insight": "The element has been removed or refreshed in the DOM.",
            "action": "Re-find the element before interacting with it."
        },
        r"401": {
            "insight": "API Authentication failed (Unauthorized).",
            "action": "Check if the bearer token is valid, expired, or missing in headers."
        },
        r"404": {
            "insight": "API Endpoint not found.",
            "action": "Verify the base URL and resource path in the request."
        }
    }

    @staticmethod
    def analyze(error_message):
        """
        Analyzes the error message and returns an AI-powered summary.
        """
        error_str = str(error_message)
        
        for pattern, info in FailureAnalyzer.PATTERNS.items():
            if re.search(pattern, error_str, re.IGNORECASE):
                return {
                    "status": "AI Analysis Complete",
                    "detected_issue": pattern.replace(r"", ""),
                    "insight": info["insight"],
                    "suggested_action": info["action"]
                }
        
        return {
            "status": "AI Analysis Complete",
            "detected_issue": "Unknown Pattern",
            "insight": "No specific pattern matched the error signature.",
            "suggested_action": "Manually inspect the logs and screenshots for visual clues."
        }
