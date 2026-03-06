# Contributing to AI Generated Image EXIF Detector

# 贡献指南

Thank you for your interest in contributing to this project!

感谢你对本项目的关注!

---

## Project Status | 项目状态

This is currently a **personal project** maintained by the owner. While contributions are welcome, please note that this is primarily a solo development effort.

这是一个**个人维护项目**。虽然欢迎贡献,但请注意这主要是个人开发项目。

---

## How to Report Issues | 如何报告问题

If you encounter a bug or have a feature request:

如果你遇到 bug 或有功能建议:

1. **Search existing issues** to avoid duplicates | **搜索现有 issues** 避免重复
2. **Open a new issue** with a clear description | **创建新 issue** 并提供清晰描述
3. Include:
   - Steps to reproduce (for bugs) | 复现步骤(针对 bug)
   - Expected vs actual behavior | 期望行为 vs 实际行为
   - Environment details (OS, Python version) | 环境信息(操作系统、Python 版本)
   - Sample images (if applicable) | 示例图片(如适用)

---

## Development Setup | 开发环境搭建

### Prerequisites | 前置要求

- Python 3.8 or higher | Python 3.8 或更高版本
- Poetry (recommended) or pip | Poetry(推荐)或 pip

### Setup Steps | 搭建步骤

```bash
# Clone the repository | 克隆仓库
git clone https://github.com/PerryLink/ai-generated-image-exif.git
cd ai-generated-image-exif

# Install dependencies | 安装依赖
poetry install

# Activate virtual environment | 激活虚拟环境
poetry shell

# Run tests | 运行测试
pytest

# Run the tool | 运行工具
ai-image-detect --help
```

---

## Code Standards | 代码规范

This project follows **PEP 8** style guidelines.

本项目遵循 **PEP 8** 代码规范。

### Before Submitting | 提交前检查

```bash
# Format code | 格式化代码
black src/

# Lint code | 代码检查
ruff check src/

# Run tests | 运行测试
pytest

# Check test coverage | 检查测试覆盖率
pytest --cov
```

---

## Pull Request Process | Pull Request 流程

1. **Fork the repository** | **Fork 仓库**
2. **Create a feature branch** | **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** | **进行修改**
   - Write clear, concise commit messages | 编写清晰简洁的提交信息
   - Add tests for new features | 为新功能添加测试
   - Update documentation if needed | 如需要更新文档
4. **Ensure all tests pass** | **确保所有测试通过**
   ```bash
   pytest
   black src/
   ruff check src/
   ```
5. **Push to your fork** | **推送到你的 fork**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** | **创建 Pull Request**
   - Provide a clear description of changes | 提供清晰的变更描述
   - Reference related issues | 引用相关 issues
   - Wait for review | 等待审查

---

## Development Guidelines | 开发指南

### Adding New AI Platform Signatures | 添加新的 AI 平台签名

To add support for a new AI platform, edit `src/ai_generated_image_exif/signatures.py`:

要添加新 AI 平台支持,编辑 `src/ai_generated_image_exif/signatures.py`:

```python
AISignature(
    name="Platform Name",
    platform="platform_id",
    confidence="high",
    patterns=[
        SignaturePattern("field_name", "pattern", "contains"),
    ]
)
```

### Testing | 测试

- Add test cases in `tests/` directory | 在 `tests/` 目录添加测试用例
- Use pytest fixtures for common setup | 使用 pytest fixtures 进行通用设置
- Aim for high test coverage | 追求高测试覆盖率

---

## Questions? | 有问题?

Feel free to open an issue for any questions or clarifications.

欢迎创建 issue 提问或寻求澄清。

---

## License | 许可证

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

贡献即表示你同意你的贡献将使用 Apache License 2.0 许可证。

---

**Maintainer | 维护者**: Chance Dean ([@PerryLink](https://github.com/PerryLink))
**Contact | 联系方式**: novelnexusai@outlook.com
