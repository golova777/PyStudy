import structlog
import asyncio
from pathlib import Path

structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    logger_factory=structlog.WriteLoggerFactory(
        file=Path("app").with_suffix(".log").open("wt")
    ),
)
logger = structlog.get_logger()


async def check_file_type():
    await logger.awarning("Unsupported File", name="file1.t3x")


logger.warning("Resource usage is nearing capacity")

asyncio.run(check_file_type())
