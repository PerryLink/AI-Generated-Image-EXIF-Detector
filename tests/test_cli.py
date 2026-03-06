"""CLI 集成测试"""

from click.testing import CliRunner
from ai_generated_image_exif.cli import main


def test_cli_help():
    """测试 CLI 帮助"""
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert 'AI 图片检测工具' in result.output
