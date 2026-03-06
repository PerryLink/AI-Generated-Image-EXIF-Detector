"""AI 检测逻辑模块"""

import re
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
from .signatures import AI_SIGNATURES, AISignature, SignaturePattern


@dataclass
class Match:
    """单个匹配结果"""
    field: str
    value: str
    pattern: str


@dataclass
class DetectionResult:
    """检测结果"""
    is_ai_generated: bool
    platform: Optional[str] = None
    platform_name: Optional[str] = None
    confidence: Optional[str] = None
    matches: List[Match] = None
    prompt: Optional[str] = None

    def __post_init__(self):
        if self.matches is None:
            self.matches = []


class AIDetector:
    """AI 检测器"""

    def __init__(self, metadata: Dict[str, Any]):
        self.metadata = metadata

    def detect(self) -> DetectionResult:
        """执行检测"""
        for signature in AI_SIGNATURES:
            matches = self._match_signature(signature)
            if matches:
                prompt = self._extract_prompt()
                return DetectionResult(
                    is_ai_generated=True,
                    platform=signature.platform,
                    platform_name=signature.name,
                    confidence=signature.confidence,
                    matches=matches,
                    prompt=prompt
                )

        return DetectionResult(is_ai_generated=False)

    def _match_signature(self, signature: AISignature) -> List[Match]:
        """匹配签名"""
        matches = []

        for pattern in signature.patterns:
            for field, value in self.metadata.items():
                if self._match_pattern(field, str(value), pattern):
                    matches.append(Match(field=field, value=str(value), pattern=pattern.pattern))
                    break

            if matches:
                return matches

        return []

    def _match_pattern(self, field: str, value: str, pattern: SignaturePattern) -> bool:
        """匹配单个模式"""
        if pattern.field.lower() not in field.lower():
            return False

        if pattern.mode == "contains":
            return pattern.pattern.lower() in value.lower()
        elif pattern.mode == "exact":
            return pattern.pattern.lower() == value.lower()
        elif pattern.mode == "regex":
            return bool(re.search(pattern.pattern, value, re.IGNORECASE))

        return False

    def _extract_prompt(self) -> Optional[str]:
        """提取 AI 生成 Prompt"""
        prompt_fields = ["prompt", "parameters", "Description", "UserComment", "ImageDescription"]

        for field in prompt_fields:
            for key, value in self.metadata.items():
                if field.lower() in key.lower():
                    return str(value)

        return None
