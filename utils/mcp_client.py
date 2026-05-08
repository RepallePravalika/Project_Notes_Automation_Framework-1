import os
from openai import OpenAI
from dotenv import load_dotenv
from utils.logger import logger

# Load environment variables
load_dotenv()

class MCPClient:
    """
    Model Context Protocol (MCP) Implementation Layer.
    Handles communication with LLM for test data generation, failure analysis, and locator optimization.
    """
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("LLM_MODEL", "gpt-4o")
        
        if not self.api_key or "your_openai_api_key" in self.api_key:
            logger.warning("OPENAI_API_KEY is not set or using placeholder. AI features will be limited.")
            self.client = None
        else:
            try:
                self.client = OpenAI(api_key=self.api_key)
            except Exception as e:
                logger.error(f"Failed to initialize OpenAI client: {e}")
                self.client = None

    def _get_completion(self, prompt, system_prompt="You are an expert QA Automation Engineer."):
        """Helper to get completion from LLM."""
        if not self.client:
            return None
            
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"LLM Call failed: {e}")
            return None

    def generate_data(self, context_type, requirements):
        """Generates test data based on context."""
        prompt = f"Generate realistic test data for {context_type}. Requirements: {requirements}. Return only a valid JSON object."
        result = self._get_completion(prompt, system_prompt="You are a data generation assistant for QA testing. Always output JSON.")
        return result

    def analyze_failure(self, error_message, context=""):
        """Analyzes a test failure and provides insights."""
        prompt = f"Analyze the following test failure:\nError: {error_message}\nContext: {context}\nProvide a concise 'Insight' and 'Suggested Action'."
        return self._get_completion(prompt)

    def optimize_locator(self, failed_locator, html_snippet=""):
        """Suggests better locators based on failure and HTML context."""
        prompt = f"The locator '{failed_locator}' failed. Here is the relevant HTML snippet:\n{html_snippet}\nSuggest 3 more robust Selenium locators (CSS or XPath)."
        return self._get_completion(prompt)

# Singleton instance
mcp_client = MCPClient()
