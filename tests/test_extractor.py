"""元数据提取测试"""

from ai_generated_image_exif.extractor import MetadataExtractor


def test_extractor_initialization():
    """测试提取器初始化"""
    extractor = MetadataExtractor("test.png")
    assert extractor.image_path == "test.png"
