# Databricks Deployment Tool

This tool automates the end-to-end process of deploying Python packages and jobs to Databricks workspaces. It handles the complete deployment pipeline: building Python wheel packages locally, uploading them to Databricks File System (DBFS), creating or updating job configurations, and managing job execution. The tool is particularly useful for data engineering teams who need to maintain consistent deployment processes across multiple Databricks jobs and packages. When you run the tool, it executes the following steps:

1. Validates your Databricks connection and environment setup
2. Lists available clusters and verifies cluster accessibility
3. Builds your Python package into a wheel file
4. Creates necessary DBFS directories
5. Uploads the wheel file and any requirements to DBFS
6. Deploys additional bundle files to the Databricks workspace
7. Creates or updates the Databricks job configuration
8. Initiates the job with specified parameters (if requested)

The setup process is straightforward: after cloning the repository, you'll need to configure your Databricks credentials in a `.env` file, install the required dependencies using pip, and install the package in editable mode using uv. This creates a development installation that allows you to modify the source code without reinstalling the package.

## Features

- Automated wheel package building
- DBFS file upload management
- Job creation and updates
- Bundle deployment automation
- Cluster management and validation
- Direct job execution capability

## Prerequisites

- Python 3.x
- Access to a Databricks workspace
- Databricks CLI configured or environment variables set
- `python-build` package installed

## Environment Setup

Create a `.env` file in the project root with the following variables:

```
DATABRICKS_WORKSPACE_URL=<your-workspace-url>
DATABRICKS_ACCESS_TOKEN=<your-access-token>
```

## Installation

1. Clone this repository
2. Create and activate a virtual environment, then install the package:
   ```bash
   uv venv --python 3.12
   source .venv/bin/activate
   uv pip install -e .
   uv sync
   ```

## Usage

### Basic Deployment

```python
from databricks_manager import DatabricksManager

dbx = DatabricksManager()
dbx.deploy_bundle("path/to/your/bundle")
```

### Running a Job

```python
parameters = {
    "date": "2024-03-01",
    "region": "NA"
}

dbx.run_job(
    job_name="Survey Processing Job",
    parameters=parameters
)
```

## Project Structure

Your Databricks bundle should follow this structure:

```
your_bundle/
├── databricks.yml     # Job configuration
├── requirements.txt   # Package dependencies
├── pyproject.toml     # Package configuration
├── setup.py           # Package setup file
└── src/               # Source code
```

It's best practice to maintain a second virtual env for the bundle being deployed:
```bash
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e .
uv sync
```

This then allows you to dump all pyproject.toml requirements to a requirements.txt:
```bash
uv pip compile pyproject.toml -o requirements.txt
```

The included `db_sp_handler` folder in this repository is an example Databricks bundle that processes survey data. You can use this as a template or replace it entirely with your own bundle. To use your own bundle:

1. Ensure your bundle follows the structure above
2. Replace the bundle path in the deployment command:
   ```python
   # Instead of using the example bundle:
   # dbx.deploy_bundle("db_sp_handler")
   
   # Use your own bundle:
   dbx.deploy_bundle("path/to/your/bundle")
   ```

## Configuration

### databricks.yml Example

```yaml
resources:
  jobs:
    survey_job:
      name: "Survey Processing Job"
      existing_cluster_id: "your-cluster-id"
      email_notifications:
        on_success:
          - "success@example.com"
        on_failure:
          - "failure@example.com"
```

## Preparing and Building Wheel

The Python wheel is a built package format that can be easily installed and deployed. Follow these steps to build the wheel:

### 1. Clean Previous Builds
Remove any existing build artifacts to ensure a clean build:
```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info/
```

### 2. Build the Wheel
Use Python's build module to create the wheel package:
```bash
# Build new wheel
python -m build
```

This command will create two files in the `dist/` directory:
- `survey_processing-0.1.2.tar.gz` (source distribution)
- `survey_processing-0.1.2-py3-none-any.whl` (wheel distribution)

### 3. Test Locally
Before deploying to Databricks, test the wheel installation locally:
```bash
# Install the wheel
pip install dist/survey_processing-0.1.2-py3-none-any.whl

# Test the import and main function
python -c "import survey_processing; survey_processing.main()"
```

### 4. Common Build Issues and Solutions

1. **Multiple Top-Level Packages**
   - Error: `Multiple top-level packages discovered in a flat-layout`
   - Solution: Ensure your package structure is correct and remove any unintended packages

2. **Missing Dependencies**
   - Error: `ModuleNotFoundError` during testing
   - Solution: Add required dependencies to `pyproject.toml`

3. **Import Errors**
   - Error: `ImportError` or `ModuleNotFoundError`
   - Solution: Verify package structure matches import statements

### 5. Build Verification Steps
1. Check the `dist/` directory contains new wheel file
2. Verify wheel filename format: `survey_processing-0.1.2-py3-none-any.whl`
3. Confirm wheel can be installed locally
4. Test basic functionality before deployment

## Monitoring and Logs

### Example Job Output
A successful job run will show output similar to this:
```
2024-11-04 12:19:32 "Survey Processing Job" TERMINATED SUCCESS
2024-11-04 17:18:53 [INFO] ================================================================================
2024-11-04 17:18:53 [INFO] Survey Processing Job Started
2024-11-04 17:18:53 [INFO] ================================================================================
2024-11-04 17:18:53 [INFO] Job Configuration:
2024-11-04 17:18:53 [INFO]   Date: 2024-11-05
2024-11-04 17:18:53 [INFO]   Region: EU
2024-11-04 17:18:53 [INFO] --------------------------------------------------------------------------------
2024-11-04 17:18:53 [INFO] Starting data processing...
2024-11-04 17:18:53 [INFO] Step: Loading data
2024-11-04 17:18:53 [INFO] Step: Validating schema
2024-11-04 17:18:53 [INFO] Step: Applying transformations
2024-11-04 17:18:53 [INFO] Step: Saving results
2024-11-04 17:18:53 [INFO] --------------------------------------------------------------------------------
2024-11-04 17:18:53 [INFO] Survey processing completed successfully
2024-11-04 17:18:53 [INFO] ================================================================================
```

### Understanding the Log Output
1. **Job Status Line**
   - Shows timestamp, job name, and final status
   - Example: `2024-11-04 12:19:32 "Survey Processing Job" TERMINATED SUCCESS`

2. **Job Start Section**
   - Marked by `================` borders
   - Shows job initialization and configuration parameters

3. **Processing Steps**
   - Each major step is logged with timestamp and description
   - Steps are separated by `----------------` borders
   - Shows progress through the processing pipeline

4. **Completion Status**
   - Final log entries confirm successful completion
   - Marked by closing `================` border

### Viewing Job Runs
1. Access the Databricks workspace
2. Navigate to the Jobs page
3. Find your job run
4. Click on the task name to view:
   - Output tab: Contains the above log output
   - Logs tab: Additional cluster and Spark logs
   - Results tab: Task results and metrics

## Error Handling

The tool includes comprehensive error handling and logging:
- Connection validation
- Environment variable verification
- Deployment status checks
- Job creation/update validation

## Best Practices

1. Always validate your cluster status before deployment:
   ```python
   dbx.validate_cluster(cluster_id)
   ```

2. Test your connection before performing operations:
   ```python
   dbx.test_connection(dbx.client)
   ```

3. Keep your bundle structure organized and consistent

## Troubleshooting

Common issues and solutions:

1. **Connection Failed**
   - Verify your environment variables
   - Check your Databricks token permissions

2. **Wheel Build Failed**
   - Ensure your `setup.py` is properly configured
   - Check for missing dependencies

3. **Job Creation Failed**
   - Validate your `databricks.yml` format
   - Confirm cluster availability

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.