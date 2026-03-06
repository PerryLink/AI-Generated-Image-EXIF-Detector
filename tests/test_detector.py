"""检测逻辑测试"""

from ai_generated_image_exif.detector import AIDetector


def test_detect_midjourney(mock_midjourney_metadata):
    """测试 Midjourney 检测"""
    detector = AIDetector(mock_midjourney_metadata)
    result = detector.detect()

    assert result.is_ai_generated is True
    assert result.platform == "midjourney"
    assert result.confidence == "high"


def test_detect_stable_diffusion(mock_sd_metadata):
    """测试 Stable Diffusion 检测"""
    detector = AIDetector(mock_sd_metadata)
    result = detector.detect()

    assert result.is_ai_generated is True
    assert result.platform == "stable_diffusion"


def test_detect_real_photo(mock_real_photo_metadata):
    """测试真实照片"""
    detector = AIDetector(mock_real_photo_metadata)
    result = detector.detect()

    assert result.is_ai_generated is False
    assert result.platform is None
