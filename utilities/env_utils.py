import os


class EnvUtils:
    @staticmethod
    def get_variable(name: str) -> int | str | float | bool:
        return os.environ.get(name)
