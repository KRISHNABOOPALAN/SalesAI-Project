import logging
from django.utils.module_loading import import_string

class DatabaseLogHandler(logging.Handler):
    """
    Custom logging handler to save log records to the database using the LogEntry model.
    Uses lazy loading to avoid AppRegistryNotReady errors.
    """
    def emit(self, record):
        try:
            # Dynamically load the LogEntry model to avoid early app registry loading
            LogEntry = import_string('MYAPP.models.LogEntry')
            
            # Create a log entry in the database
            log_entry = LogEntry(
                level=record.levelname,
                message=record.getMessage(),
                module=record.module,
                func_name=record.funcName,
                line_no=record.lineno,
            )
            log_entry.save()
        except Exception as e:
            # Avoid crashing the app due to logging errors
            print(f"Failed to save log to database: {e}")
