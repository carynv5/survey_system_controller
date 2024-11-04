import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse

def get_run_url(workspace_url: str, job_id: int, run_id: str, org_id: str) -> str:
    """
    Construct the Databricks run URL from components.
    
    Args:
        workspace_url (str): Databricks workspace URL
        job_id (int): The job ID
        run_id (str): The run ID from the API response
        org_id (str): Organization ID
    """
    # Parse the workspace URL to get the host
    parsed_url = urlparse(workspace_url)
    host = parsed_url.netloc
    
    return f"https://{host}/?o={org_id}#job/{job_id}/run/{run_id}"

def run_survey_processing_job(date: str, region: str) -> dict:
    """Run the survey processing job with specified parameters."""
    # Load environment variables
    load_dotenv()
    
    # Setup API configuration
    workspace_url = os.getenv('DATABRICKS_WORKSPACE_URL')
    token = os.getenv('DATABRICKS_ACCESS_TOKEN')
    org_id = os.getenv('DATABRICKS_ORG_ID', '4924241215537505')  # Your org ID
    job_id = 860716632182514  # Your job ID
    
    api_path = "/api/2.1/jobs/run-now"
    
    # API headers
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Job configuration
    data = {
        "job_id": job_id,
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
        response.raise_for_status()
        return response.json(), workspace_url, job_id, org_id
    except requests.exceptions.RequestException as e:
        print(f"Error running job: {e}")
        return None, None, None, None

if __name__ == "__main__":
    # Example usage
    result, workspace_url, job_id, org_id = run_survey_processing_job(
        date="2024-11-05",
        region="EU"
    )
    
    if result:
        run_id = result.get('run_id')
        run_url = get_run_url(workspace_url, job_id, run_id, org_id)
        print(f"Job started successfully!")
        print(f"Run ID: {run_id}")
        print(f"Run URL: {run_url}")
    else:
        print("Failed to start job")