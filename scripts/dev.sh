#!/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "🚀 Starting Bookless development server..."

cd apps/api

if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "📦 Activating virtual environment..."
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install -e . --quiet

echo "🔧 Starting uvicorn..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
