import os
import requests
from dotenv import load_dotenv

def run_survey_processing_job(date: str, region: str) -> dict:
    """
    Run the survey processing job with specified parameters.
    
    Args:
        date (str): Processing date in YYYY-MM-DD format
        region (str): Region code (e.g., 'EU', 'US')
    
    Returns:
        dict: Response from Databricks API
    """
    # Load environment variables
    load_dotenv()
    
    # Setup API configuration
    workspace_url = os.getenv('DATABRICKS_WORKSPACE_URL')
    token = os.getenv('DATABRICKS_ACCESS_TOKEN')
    api_path = "/api/2.1/jobs/run-now"
    
    # API headers
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Job configuration
    data = {
        "job_id": 860716632182514,  # Your job ID from the Run URL
        "python_named_params": {
            "date": date,
            "region": region
        }
    }
    
    # Make API request
    try:
        response = requests.post(
            f"{workspace_url}{api_path}",
            headers=headers,
            json=data
        )
        response.raise_for_status()  # Raise exception for non-200 status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error running job: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    result = run_survey_processing_job(
        date="2024-11-05",
        region="EU"
    )
    
    if result:
        run_id = result.get('run_id')
        print(f"Job started successfully!")
        print(f"Run ID: {run_id}")
        print(f"Run URL: https://dbc-45210aa6-83e8.cloud.databricks.com/?o=4924241215537505#job/860716632182514/run/{run_id}")
    else:
        print("Failed to start job")