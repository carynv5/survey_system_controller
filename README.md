# Databricks Survey Processing System Controller

## Overview
Python survey processing databricks bundle that is built into a wheel and deployed as a databricks job. This job can be deployed and triggered using the databricks CLI or as an API call.

This package provides:
- Automated wheel building and deployment process
- Configurable job parameters (date and region)
- Detailed logging and job monitoring
- Email notifications for job status
- Retry mechanisms for job reliability
- CLI commands for deployment and execution

## Key Components
- **Build Process**: Clean build system using Python wheel packaging
- **Deployment**: Databricks bundle deployment with validation
- **Job Configuration**: Customizable job settings via `databricks.yml`
- **Execution**: CLI commands for job triggering with parameters
- **Monitoring**: Structured logging and status tracking
- **Notifications**: Email alerts for job success/failure

## Quick Start
```bash
# Build the wheel
python -m build

# Validate and deploy the bundle
databricks bundle validate
databricks bundle deploy

# Run the job
databricks bundle run survey_processing_job \
  --python-named-params "date=2024-11-05,region=EU"
```

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

## Project Structure

Your Databricks bundle should follow this structure:

```
your_bundle/
├── databricks.yml     # Job configuration
├── requirements.txt   # Package dependencies
├── pyproject.toml     # Package configuration
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

This repository is an example Databricks bundle that processes survey data. You can use this as a template or replace it entirely with your own bundle. To use your own bundle:

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

### Example build output:
```
 carynv5 on RMT-L-292 at ../db_sp_handler  main (++(1) ) is 📦 v0.1.2 via 🐍 pyenv via 🅒 base
 python -m build
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - setuptools>=61.0
* Getting build dependencies for sdist...
running egg_info
creating survey_processing.egg-info
writing survey_processing.egg-info/PKG-INFO
writing dependency_links to survey_processing.egg-info/dependency_links.txt
writing entry points to survey_processing.egg-info/entry_points.txt
writing requirements to survey_processing.egg-info/requires.txt
writing top-level names to survey_processing.egg-info/top_level.txt
writing manifest file 'survey_processing.egg-info/SOURCES.txt'
reading manifest file 'survey_processing.egg-info/SOURCES.txt'
writing manifest file 'survey_processing.egg-info/SOURCES.txt'
* Building sdist...
running sdist
running egg_info
writing survey_processing.egg-info/PKG-INFO
writing dependency_links to survey_processing.egg-info/dependency_links.txt
writing entry points to survey_processing.egg-info/entry_points.txt
writing requirements to survey_processing.egg-info/requires.txt
writing top-level names to survey_processing.egg-info/top_level.txt
reading manifest file 'survey_processing.egg-info/SOURCES.txt'
writing manifest file 'survey_processing.egg-info/SOURCES.txt'
running check
creating survey_processing-0.1.2
creating survey_processing-0.1.2/survey_processing
creating survey_processing-0.1.2/survey_processing.egg-info
copying files to survey_processing-0.1.2...
copying README.md -> survey_processing-0.1.2
copying pyproject.toml -> survey_processing-0.1.2
copying survey_processing/__init__.py -> survey_processing-0.1.2/survey_processing
copying survey_processing/main.py -> survey_processing-0.1.2/survey_processing
copying survey_processing.egg-info/PKG-INFO -> survey_processing-0.1.2/survey_processing.egg-info
copying survey_processing.egg-info/SOURCES.txt -> survey_processing-0.1.2/survey_processing.egg-info
copying survey_processing.egg-info/dependency_links.txt -> survey_processing-0.1.2/survey_processing.egg-info
copying survey_processing.egg-info/entry_points.txt -> survey_processing-0.1.2/survey_processing.egg-info
copying survey_processing.egg-info/requires.txt -> survey_processing-0.1.2/survey_processing.egg-info
copying survey_processing.egg-info/top_level.txt -> survey_processing-0.1.2/survey_processing.egg-info
copying survey_processing.egg-info/SOURCES.txt -> survey_processing-0.1.2/survey_processing.egg-info
Writing survey_processing-0.1.2/setup.cfg
Creating tar archive
removing 'survey_processing-0.1.2' (and everything under it)
* Building wheel from sdist
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - setuptools>=61.0
* Getting build dependencies for wheel...
running egg_info
writing survey_processing.egg-info/PKG-INFO
writing dependency_links to survey_processing.egg-info/dependency_links.txt
writing entry points to survey_processing.egg-info/entry_points.txt
writing requirements to survey_processing.egg-info/requires.txt
writing top-level names to survey_processing.egg-info/top_level.txt
reading manifest file 'survey_processing.egg-info/SOURCES.txt'
writing manifest file 'survey_processing.egg-info/SOURCES.txt'
* Building wheel...
running bdist_wheel
running build
running build_py
creating build/lib/survey_processing
copying survey_processing/__init__.py -> build/lib/survey_processing
copying survey_processing/main.py -> build/lib/survey_processing
running egg_info
writing survey_processing.egg-info/PKG-INFO
writing dependency_links to survey_processing.egg-info/dependency_links.txt
writing entry points to survey_processing.egg-info/entry_points.txt
writing requirements to survey_processing.egg-info/requires.txt
writing top-level names to survey_processing.egg-info/top_level.txt
reading manifest file 'survey_processing.egg-info/SOURCES.txt'
writing manifest file 'survey_processing.egg-info/SOURCES.txt'
installing to build/bdist.macosx-11.1-arm64/wheel
running install
running install_lib
creating build/bdist.macosx-11.1-arm64/wheel
creating build/bdist.macosx-11.1-arm64/wheel/survey_processing
copying build/lib/survey_processing/__init__.py -> build/bdist.macosx-11.1-arm64/wheel/./survey_processing
copying build/lib/survey_processing/main.py -> build/bdist.macosx-11.1-arm64/wheel/./survey_processing
running install_egg_info
Copying survey_processing.egg-info to build/bdist.macosx-11.1-arm64/wheel/./survey_processing-0.1.2-py3.12.egg-info
running install_scripts
creating build/bdist.macosx-11.1-arm64/wheel/survey_processing-0.1.2.dist-info/WHEEL
creating '/Users/carynv5/Documents/dev/db_sp_handler/dist/.tmp-rtgukios/survey_processing-0.1.2-py3-none-any.whl' and adding 'build/bdist.macosx-11.1-arm64/wheel' to it
adding 'survey_processing/__init__.py'
adding 'survey_processing/main.py'
adding 'survey_processing-0.1.2.dist-info/METADATA'
adding 'survey_processing-0.1.2.dist-info/WHEEL'
adding 'survey_processing-0.1.2.dist-info/entry_points.txt'
adding 'survey_processing-0.1.2.dist-info/top_level.txt'
adding 'survey_processing-0.1.2.dist-info/RECORD'
removing build/bdist.macosx-11.1-arm64/wheel
Successfully built survey_processing-0.1.2.tar.gz and survey_processing-0.1.2-py3-none-any.whl
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

## Deploying to Databricks

### 1. Validate Bundle Configuration
Before deploying, validate your bundle configuration:
```bash
databricks bundle validate
```

Successful validation will show output similar to:
```
Name: survey-processing
Target: default
Workspace:
  User: cary.greenwood@nv5.com
  Path: /Workspace/Users/cary.greenwood@nv5.com/.bundle/survey-processing/default
Validation OK!
```

### 2. Deploy Bundle
Deploy your package to Databricks:
```bash
databricks bundle deploy
```

Successful deployment will show:
```
Uploading survey_processing-0.1.2-py3-none-any.whl...
Uploading bundle files to /Workspace/Users/cary.greenwood@nv5.com/.bundle/survey-processing/default/files...
Deploying resources...
Updating deployment state...
Deployment complete!
```

### 3. Run the Job
Execute the deployed job with parameters:
```bash
databricks bundle run survey_processing_job \
  --python-named-params "date=2024-11-05,region=EU"
```

### Common Deployment Issues and Solutions

1. **Validation Errors**
   - Check your `databricks.yml` configuration
   - Verify workspace permissions
   - Ensure bundle name matches configuration

2. **Upload Failures**
   - Verify wheel file exists in `dist/` directory
   - Check workspace path permissions
   - Confirm wheel filename matches `databricks.yml`

3. **Job Run Errors**
   - Verify parameter names and formats
   - Check job cluster configuration
   - Review workspace resource limits

### Deployment Tips
1. Always run `databricks bundle validate` before deployment
2. Use `--verbose` flag for detailed deployment logs:
   ```bash
   databricks bundle deploy --verbose
   ```
3. Monitor deployment progress in the Databricks workspace
4. Keep track of wheel versions and updates

[Continue with rest of README...]


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


## Databricks Cluster Configuration

```yaml
job_clusters:
  - job_cluster_key: "main"
    new_cluster:                       # Creating a new cluster for each job run
      spark_version: "13.3.x-scala2.12"  # Using Databricks Runtime 13.3
      node_type_id: "i3.xlarge"          # Using i3.xlarge instance type
      num_workers: 1                      # Single worker node configuration
```

### New Cluster - Current configuration
A new cluster is created for each job run
The cluster will terminate after the job completes
You're using:

Standard Databricks Runtime (not ML, GPU, or Photon)
Single worker node (not autoscaling)
i3.xlarge instance type for both driver and workers

### Use existing cluster
If you want to save costs or reuse an existing cluster, you could switch to using an existing_cluster_id:

```yaml
job_clusters:
  - job_cluster_key: "main"
    existing_cluster_id: "your-cluster-id-here"  # Use an existing cluster
Or add autoscaling to the current configuration:
yamlCopyjob_clusters:
  - job_cluster_key: "main"
    new_cluster:
      spark_version: "13.3.x-scala2.12"
      node_type_id: "i3.xlarge"
      autoscale:
        min_workers: 1
        max_workers: 3
```