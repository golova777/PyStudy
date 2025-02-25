import structlog
import logging
import os

level = os.environ.get("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, level)
print(LOG_LEVEL)


def set_process_id(_, __, event_dict):
    event_dict["process_id"] = os.getpid()
    return event_dict


def drop_messages(_, __, event_dict):
    if event_dict.get("route") == "login":
        raise structlog.DropEvent
    return event_dict


structlog.configure(
    processors=[
        # важен порядок следования процессоров
        # structlog.processors.TimeStamper(fmt="iso"),  # временные метки
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M.%S"),
        structlog.processors.add_log_level,  # добавит вывод уровля логирования [info     ]
        set_process_id,
        drop_messages,
        # structlog.dev.ConsoleRenderer(),  # конвертирует в строку и выводи т в консоль
        structlog.processors.JSONRenderer(),  # конвертирует в строку и выводи т в консоль
    ],
    wrapper_class=structlog.make_filtering_bound_logger(LOG_LEVEL)
)
logger = structlog.get_logger()
logger1 = logger.bind(cpu_count=os.cpu_count())

mydat = {"hello": "world",
         "jack": "sparrow"}

logger.debug("Database connection established")
logger1.info("Обрабатываем API")
logger1.warning("Resource usage is nearing capacity")
logger1.error("Failed to save the file. Please check permissions")
logger1.critical("System has encountered a critical failure. Shutting down")
logger1.info("User created", name="John Doe", route="login")
