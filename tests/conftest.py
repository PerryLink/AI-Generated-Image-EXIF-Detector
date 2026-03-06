"""pytest fixtures"""

import pytest


@pytest.fixture
def mock_midjourney_metadata():
    """模拟 Midjourney 元数据"""
    return {
        "parameters": "a beautiful landscape --v 5.2 --ar 16:9",
        "Software": "Midjourney",
    }


@pytest.fixture
def mock_sd_metadata():
    """模拟 Stable Diffusion 元数据"""
    return {
        "parameters": "Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Model: sd_xl_base_1.0",
        "Software": "AUTOMATIC1111",
    }


@pytest.fixture
def mock_real_photo_metadata():
    """模拟真实照片元数据"""
    return {
        "Make": "Canon",
        "Model": "Canon EOS 5D",
        "DateTime": "2024:01:01 12:00:00",
    }
