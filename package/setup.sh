#!/bin/bash
# Reader3 一键安装脚本 (macOS / Linux)
# 用法: bash setup.sh

set -e
cd "$(dirname "$0")"

echo "==============================="
echo "  Reader3 📚 安装向导"
echo "==============================="
echo ""

# 1. 检查 Python3
if ! command -v python3 &>/dev/null; then
    echo "❌ 未找到 python3，请先安装："
    echo "   打开终端输入: xcode-select --install"
    echo "   或从 https://www.python.org/downloads/ 下载安装"
    exit 1
fi

PY_VER=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "✅ Python $PY_VER"

# 2. 创建虚拟环境
if [ ! -d ".venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv .venv
fi

# 确保 pip 可用
.venv/bin/python3 -m ensurepip --upgrade 2>/dev/null || true

# 3. 安装依赖
echo "📦 安装依赖包（首次可能需要几分钟）..."
.venv/bin/python3 -m pip install -q --upgrade pip
.venv/bin/python3 -m pip install -q -r requirements.txt

# 4. 配置 .env
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ 已从模板创建 .env（可稍后编辑添加 API Key）"
else
    echo "✅ .env 已存在"
fi

# 5. 确保必要目录存在
mkdir -p books dict

# 6. 预处理示例图书（如有）
if [ -f "books/dracula.epub" ] && [ ! -d "books/dracula_data" ]; then
    echo "📖 导入示例图书 Dracula..."
    .venv/bin/python3 reader3.py books/dracula.epub 2>/dev/null || true
fi

echo ""
echo "==============================="
echo "  ✅ 安装完成！"
echo "==============================="
echo ""
echo "启动方式: bash start.sh"
echo "然后在浏览器打开: http://localhost:8000"
echo ""
echo "💡 提示: 词典可在应用「设置」中一键下载安装"
echo ""
