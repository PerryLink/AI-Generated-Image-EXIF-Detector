"""AI 平台签名数据库"""

from dataclasses import dataclass
from typing import List, Literal

MatchMode = Literal["regex", "exact", "contains"]


@dataclass
class SignaturePattern:
    """签名匹配模式"""
    field: str  # 元数据字段名
    pattern: str  # 匹配模式（正则/精确/包含）
    mode: MatchMode = "contains"


@dataclass
class AISignature:
    """AI 平台签名定义"""
    name: str  # 平台名称
    platform: str  # 平台标识
    confidence: Literal["high", "medium", "low"]  # 置信度
    patterns: List[SignaturePattern]  # 匹配模式列表


# AI 平台签名数据库
AI_SIGNATURES = [
    # Midjourney
    AISignature(
        name="Midjourney",
        platform="midjourney",
        confidence="high",
        patterns=[
            SignaturePattern("parameters", "--v", "contains"),
            SignaturePattern("parameters", "--ar", "contains"),
            SignaturePattern("parameters", "--chaos", "contains"),
            SignaturePattern("Software", "Midjourney", "contains"),
            SignaturePattern("prompt", "midjourney", "contains"),
        ]
    ),

    # Stable Diffusion
    AISignature(
        name="Stable Diffusion",
        platform="stable_diffusion",
        confidence="high",
        patterns=[
            SignaturePattern("parameters", "Steps:", "contains"),
            SignaturePattern("parameters", "Sampler:", "contains"),
            SignaturePattern("parameters", "CFG scale:", "contains"),
            SignaturePattern("Software", "AUTOMATIC1111", "contains"),
            SignaturePattern("Software", "ComfyUI", "contains"),
            SignaturePattern("parameters", "Model:", "contains"),
        ]
    ),

    # DALL-E
    AISignature(
        name="DALL-E",
        platform="dalle",
        confidence="high",
        patterns=[
            SignaturePattern("Software", "DALL·E", "contains"),
            SignaturePattern("ImageDescription", "DALL-E", "contains"),
            SignaturePattern("UserComment", "DALL-E", "contains"),
        ]
    ),

    # Leonardo.Ai
    AISignature(
        name="Leonardo.Ai",
        platform="leonardo",
        confidence="high",
        patterns=[
            SignaturePattern("Software", "Leonardo", "contains"),
            SignaturePattern("parameters", "leonardo", "contains"),
        ]
    ),

    # Adobe Firefly
    AISignature(
        name="Adobe Firefly",
        platform="firefly",
        confidence="high",
        patterns=[
            SignaturePattern("Software", "Firefly", "contains"),
            SignaturePattern("Creator", "Adobe Firefly", "contains"),
        ]
    ),
]
