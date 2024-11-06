import argparse
import logging
import sys
from datetime import datetime
from typing import Optional

def setup_logging():
    """Configure logging for Databricks environment."""
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    if root_logger.handlers:
        root_logger.handlers = []
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
    
    return logging.getLogger(__name__)

def validate_date(date_str: str) -> Optional[str]:
    """Validate date string format."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

def validate_region(region: str) -> str:
    """Validate region code."""
    valid_regions = {'EU', 'US', 'APAC'}  # Add your valid regions here
    if region.upper() not in valid_regions:
        raise argparse.ArgumentTypeError(f"Invalid region: {region}. Must be one of {valid_regions}")
    return region.upper()

def parse_args():
    """Parse command line arguments with validation."""
    parser = argparse.ArgumentParser(description='Survey Processing Job')
    parser.add_argument('--date', 
                      required=True,
                      type=validate_date,
                      help='Processing date in YYYY-MM-DD format')
    parser.add_argument('--region',
                      required=True,
                      type=validate_region,
                      help='Region code to process (EU/US/APAC)')
    
    # Parse args and immediately log them for debugging
    args = parser.parse_args()
    logging.getLogger(__name__).debug(f"Raw parsed arguments: {args}")
    return args

def main():
    """Main entry point for the survey processing job."""
    logger = setup_logging()
    
    try:
        # Log startup information with parameter debugging
        logger.info("=" * 80)
        logger.info("Survey Processing Job Started")
        logger.info("=" * 80)
        
        # Log all system arguments for debugging
        logger.debug(f"System arguments: {sys.argv}")
        
        # Parse arguments
        args = parse_args()
        
        # Log configuration with explicit type information
        logger.info("Job Configuration:")
        logger.info(f"Date: {args.date} (type: {type(args.date)})")
        logger.info(f"Region: {args.region} (type: {type(args.region)})")
        logger.info("-" * 80)
        
        # Your processing logic here
        logger.info("Starting data processing...")
        
        # Example processing steps
        steps = ["Loading data", "Validating schema", "Applying transformations", "Saving results"]
        for step in steps:
            logger.info(f"Step: {step}")
            # Add your actual processing logic here
            
        logger.info("-" * 80)
        logger.info("Survey processing completed successfully")
        logger.info("=" * 80)
        return 0
        
    except Exception as e:
        logger.error("=" * 80)
        logger.error(f"Error in survey processing: {str(e)}")
        logger.error(f"Stack trace:", exc_info=True)  # Add full stack trace
        logger.error("=" * 80)
        return 1

if __name__ == "__main__":
    sys.exit(main())