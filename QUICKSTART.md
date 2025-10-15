# 🚀 Quick Start Guide

Get up and running with the Meeting Summarizer in 5 minutes!

## Step 1: Get Your OpenAI API Key

1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy your API key (it starts with `sk-`)
5. **Important**: Keep this key secure!

## Step 2: Run the Setup Script

Open your terminal and run:

```bash
cd /Users/yash/Documents/Projects/Unthinkable/meeting-summarizer-whisper-api
./setup.sh
```

The script will:
- ✓ Check Python installation
- ✓ Create a virtual environment
- ✓ Install all dependencies
- ✓ Prompt you for your API key
- ✓ Start the application

## Step 3: Use the Application

1. The browser will open automatically at `http://127.0.0.1:7860`
2. Upload an audio file or record directly
3. Click "Submit"
4. Wait for processing (usually 30-60 seconds)
5. View your summary and download files!

## Manual Setup (Alternative)

If you prefer to set up manually:

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API key
export OPENAI_API_KEY='your-api-key-here'

# 4. Run application
python main.py
```

## Testing

To test the core functionality without the GUI:

```bash
source venv/bin/activate
python test.py
```

## Troubleshooting

### "Command not found: python3"
- Install Python from [python.org](https://www.python.org/downloads/)

### "OPENAI_API_KEY not set"
```bash
export OPENAI_API_KEY='sk-your-key-here'
```

### Port 7860 already in use
- Change the port in `main.py` (line 403):
```python
server_port=8080  # or any other available port
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [config_example.py](config_example.py) for customization options
- Try different summary styles (brief, detailed, action-items)

## Support

Need help? Check:
- [OpenAI Documentation](https://platform.openai.com/docs)
- [Gradio Documentation](https://gradio.app/docs)
- Project README.md

---

**Ready to go? Run `./setup.sh` and start summarizing!** 🎉
