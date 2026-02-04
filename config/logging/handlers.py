import logging


class JSONFileHandler(logging.Handler):
    """Логгер для запису логів у файл у форматі JSON."""

    def __init__(self, filename: str, level: int | str = 0) -> None:
        super().__init__(level)
        self.filename = filename

    def emit(self, record: logging.LogRecord) -> None:
        try:
            msg = self.format(record)
            with open(self.filename, "a", encoding="utf-8") as f:
                f.write(msg + "\n")
        except Exception:
            self.handleError(record)