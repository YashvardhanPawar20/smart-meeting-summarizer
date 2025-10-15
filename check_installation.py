#!/usr/bin/env python3
"""
Quick demo script to verify the installation
This script checks if all dependencies are installed correctly
"""

import sys

def check_imports():
    """Check if all required packages can be imported."""
    print("=" * 80)
    print("Meeting Summarizer - Installation Verification")
    print("=" * 80)
    print()
    
    packages = [
        ("openai", "OpenAI API client"),
        ("gradio", "Gradio UI framework"),
        ("dotenv", "python-dotenv for environment variables")
    ]
    
    all_good = True
    
    for package, description in packages:
        try:
            __import__(package)
            print(f"✓ {description:50} [OK]")
        except ImportError as e:
            print(f"✗ {description:50} [FAILED]")
            print(f"  Error: {e}")
            all_good = False
    
    print()
    print("=" * 80)
    
    if all_good:
        print("✅ All dependencies are installed correctly!")
        print()
        print("Next steps:")
        print("1. Set your OpenAI API key:")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        print()
        print("2. Run the application:")
        print("   python main.py")
        print()
        return 0
    else:
        print("❌ Some dependencies are missing. Please run:")
        print("   pip install -r requirements.txt")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(check_imports())
