"""Data source plugins for querying data."""

# Import the built-in plugins to register them
from .databricks import DatabricksDataSource
from .local import LocalDataSource
from .s3 import S3DataSource
