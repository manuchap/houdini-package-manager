from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from houdini_package_manager.meta.meta_tools import StatusBar


class Actions:
    """
    Various actions that can be performed by widgets.
    """

    @staticmethod
    def open_path(path: Path | str) -> None:
        """
        Get the path that is associated with a button and open it.
        """

        path_obj: Path
        path_obj = Path(path) if not isinstance(path, Path) else path

        if not path_obj.exists():
            StatusBar.message(f"Failed to open: {str(path_obj)}")
            return

        QDesktopServices.openUrl(QUrl.fromLocalFile(str(path_obj)))
        StatusBar.message(f"Opened: {path_obj}")
