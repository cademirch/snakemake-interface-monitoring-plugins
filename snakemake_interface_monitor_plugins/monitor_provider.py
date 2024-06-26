__author__ = "Cade Mirchandani, Christopher Tomkins-Tinch, Johannes Köster"
__copyright__ = (
    "Copyright 2023, Cade Mirchandani, Christopher Tomkins-Tinch, Johannes Köster"
)
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from abc import ABC, abstractmethod
from typing import Optional
from snakemake_interface_monitor_plugins.settings import (
    MonitorProviderSettingsBase,
)


class MonitorProviderBase(ABC):
    def __init__(self, settings: Optional[MonitorProviderSettingsBase] = None) -> None:
        self.settings = settings
        self.__post_init__()

    def __post_init__(self):  # noqa B027
        pass

    @abstractmethod
    def log_handler(self, msg: dict) -> None:
        pass
