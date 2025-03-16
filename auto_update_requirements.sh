#!/bin/bash

echo "🚀 Starting dependency update..."

# Ensure pip, setuptools, and wheel are updated
echo "🔄 Updating pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel

# Upgrade all packages listed in requirements.txt
echo "📦 Upgrading packages from requirements.txt..."
pip install --upgrade -r requirements.txt

# Save updated versions back to requirements.txt
echo "💾 Saving updated dependencies..."
pip freeze > requirements.txt

echo "✅ Dependencies updated successfully!"
