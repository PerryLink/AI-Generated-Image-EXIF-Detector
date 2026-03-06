"""工具函数"""

import os
from pathlib import Path


def validate_image_path(path: str) -> bool:
    """验证图片路径"""
    if not os.path.exists(path):
        return False

    valid_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
    return Path(path).suffix.lower() in valid_extensions


def format_metadata(metadata: dict) -> str:
    """格式化元数据"""
    lines = []
    for key, value in metadata.items():
        lines.append(f"{key}: {value}")
    return "\n".join(lines)
