"""CLI 界面模块"""

import json
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from pathlib import Path

from .extractor import MetadataExtractor
from .detector import AIDetector
from .utils import validate_image_path

console = Console()


@click.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('-v', '--verbose', is_flag=True, help='显示详细元数据')
@click.option('--json', 'json_output', is_flag=True, help='JSON 格式输出')
@click.option('--show-prompt', is_flag=True, help='显示生成 Prompt')
def main(image_path, verbose, json_output, show_prompt):
    """AI 图片检测工具 - 识别 AI 生成的图片"""

    # 验证图片路径
    if not validate_image_path(image_path):
        console.print("[red]错误: 无效的图片文件[/red]")
        return

    # 提取元数据
    extractor = MetadataExtractor(image_path)
    metadata = extractor.extract()

    # 检测 AI 签名
    detector = AIDetector(metadata)
    result = detector.detect()

    # JSON 输出
    if json_output:
        output = {
            "file": str(Path(image_path).name),
            "is_ai_generated": result.is_ai_generated,
            "platform": result.platform,
            "platform_name": result.platform_name,
            "confidence": result.confidence,
            "prompt": result.prompt if show_prompt else None,
            "matches": [{"field": m.field, "value": m.value} for m in result.matches]
        }
        console.print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    # 友好输出
    if result.is_ai_generated:
        panel_content = f"[bold red]⚠️  检测到 AI 生成图片[/bold red]\n\n"
        panel_content += f"平台: [yellow]{result.platform_name}[/yellow]\n"
        panel_content += f"置信度: [yellow]{result.confidence}[/yellow]\n"

        if show_prompt and result.prompt:
            panel_content += f"\n生成 Prompt:\n[cyan]{result.prompt}[/cyan]"

        console.print(Panel(panel_content, title="检测结果", border_style="red"))

        if verbose and result.matches:
            table = Table(title="匹配证据")
            table.add_column("字段", style="cyan")
            table.add_column("值", style="yellow")

            for match in result.matches:
                table.add_row(match.field, match.value[:100])

            console.print(table)
    else:
        panel_content = "[bold green]✓ 未检测到 AI 生成签名[/bold green]\n\n"
        panel_content += "这可能是真实照片，或 AI 生成但未保留元数据"
        console.print(Panel(panel_content, title="检测结果", border_style="green"))

    # 显示详细元数据
    if verbose and metadata:
        table = Table(title="完整元数据")
        table.add_column("字段", style="cyan")
        table.add_column("值", style="white")

        for key, value in list(metadata.items())[:20]:
            table.add_row(key, str(value)[:100])

        console.print(table)


if __name__ == '__main__':
    main()
