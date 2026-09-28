class PipelineError(Exception):
    """Base exception for pipeline errors."""
    pass
class DataError(PipelineError):
    """Raised when there is a data-related error."""
    pass


class ConfigurationError(PipelineError):
    """Raised when there is a configuration-related error."""
    pass


class ProcessingError(PipelineError):
    """Raised when an error occurs during pipeline processing."""
    pass