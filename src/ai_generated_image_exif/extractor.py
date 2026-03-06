"""元数据提取模块"""

from typing import Dict, Any
from PIL import Image
import exifread


class MetadataExtractor:
    """元数据提取器"""

    def __init__(self, image_path: str):
        self.image_path = image_path

    def extract(self) -> Dict[str, Any]:
        """提取完整元数据"""
        metadata = {}

        # 提取 Pillow 信息（PNG tEXt chunks）
        metadata.update(self._extract_pillow_info())

        # 提取 EXIF 数据
        metadata.update(self._extract_exif())

        return metadata

    def _extract_pillow_info(self) -> Dict[str, Any]:
        """提取 PNG tEXt chunks"""
        try:
            with Image.open(self.image_path) as img:
                info = {}
                if hasattr(img, 'text'):
                    info.update(img.text)
                if hasattr(img, 'info'):
                    info.update(img.info)
                return info
        except Exception:
            return {}

    def _extract_exif(self) -> Dict[str, Any]:
        """提取 EXIF 数据"""
        try:
            with open(self.image_path, 'rb') as f:
                tags = exifread.process_file(f, details=False)
                return {k: str(v) for k, v in tags.items()}
        except Exception:
            return {}
