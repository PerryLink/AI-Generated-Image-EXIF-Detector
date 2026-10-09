# AI Generated Image EXIF Detector
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/ai-generated-image-exif-detector)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)

A powerful CLI tool to detect AI-generated images by analyzing their metadata signatures.

一个强大的命令行工具,通过分析图片元数据签名来检测 AI 生成的图片。

---

## ✨ Features | 功能特性

- 🔍 Detect images from major AI platforms (Midjourney, Stable Diffusion, DALL-E, Leonardo.Ai, Adobe Firefly)
- 📊 Extract comprehensive metadata (EXIF/PNG tEXt chunks)
- 💬 Display AI generation prompts
- 🎨 Beautiful terminal output with rich formatting
- 📤 JSON output support for automation

- 🔍 检测主流 AI 平台生成的图片(Midjourney、Stable Diffusion、DALL-E、Leonardo.Ai、Adobe Firefly)
- 📊 提取完整的图片元数据(EXIF/PNG tEXt chunks)
- 💬 显示 AI 生成时使用的 Prompt(咒语)
- 🎨 友好的终端输出界面
- 📤 支持 JSON 格式输出,便于自动化处理

---

## 🚀 Quick Start | 快速开始

### Installation | 安装

```bash
# Using Poetry (recommended)
poetry install

# Using pip
pip install "git+https://github.com/PerryLink/AI-Generated-Image-EXIF-Detector.git"
# (installs from source; not yet on PyPI)
```

### Basic Usage | 基础使用

```bash
# Detect an image
ai-image-detect image.png

# Show detailed metadata
ai-image-detect -v image.png

# Display generation prompt
ai-image-detect --show-prompt image.png

# JSON output
ai-image-detect --json image.png
```

---

## 📖 Usage Guide | 使用指南

### Command Options | 命令选项

- `image_path`: Path to the image file to analyze | 要分析的图片文件路径
- `-v, --verbose`: Show detailed metadata | 显示详细元数据
- `--show-prompt`: Display AI generation prompt | 显示生成 Prompt
- `--json`: Output results in JSON format | JSON 格式输出

### Supported Platforms | 支持的 AI 平台

| Platform | Detection Method | Confidence |
|----------|-----------------|------------|
| Midjourney | Metadata signatures | High |
| Stable Diffusion | EXIF parameters | High |
| DALL-E | Software tags | High |
| Leonardo.Ai | Metadata patterns | High |
| Adobe Firefly | Creator information | High |

---

## 📁 Project Structure | 项目结构

```
ai-generated-image-exif/
├── src/
│   └── ai_generated_image_exif/
│       ├── __init__.py          # Package initialization
│       ├── cli.py               # Command-line interface
│       ├── detector.py          # AI detection logic
│       ├── extractor.py         # Metadata extraction
│       ├── signatures.py        # AI platform signatures
│       └── utils.py             # Utility functions
├── tests/                       # Test suite
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

---

## 🛠️ Tech Stack | 技术栈

- **Python**: 3.8+
- **CLI Framework**: Click
- **Terminal UI**: Rich
- **Image Processing**: Pillow
- **EXIF Reading**: ExifRead
- **Testing**: pytest
- **Code Quality**: black, ruff

---

## 🔬 How It Works | 工作原理

This tool analyzes image metadata (EXIF tags and PNG text chunks) to identify AI-generated images. Each AI platform leaves unique signatures in the metadata, which we match against our signature database.

本工具通过读取图片的元数据(EXIF 标签和 PNG 文本块)来识别 AI 生成的图片。每个 AI 平台都会在元数据中留下独特的签名,我们通过匹配签名数据库来识别。

**Note**: If image metadata has been stripped, detection is not possible.

**注意**: 如果图片的元数据被清除,则无法检测。

---

## 🧪 Development | 开发

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov

# Format code
poetry run black src/

# Lint code
poetry run ruff check src/
```

---

## 📄 License | 许可证

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

---

## 🤝 Contributing | 贡献

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

欢迎贡献!详情请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📧 Contact | 联系方式

- GitHub: [@PerryLink](https://github.com/PerryLink)
- Email: novelnexusai@outlook.com
