# 🎙️ Smart Meeting Summarizer

A modern, user-friendly application that transcribes audio recordings and generates intelligent summaries using OpenAI's Whisper and GPT APIs.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)

## ✨ Features

- 🎯 **Automatic Transcription**: Uses OpenAI's Whisper API for accurate speech-to-text conversion
- 🤖 **Intelligent Summaries**: Leverages GPT-4 to generate clear, actionable summaries
- 🌍 **Multi-language Support**: Supports 12+ languages with automatic detection
- 📊 **Multiple Summary Styles**:
  - **Brief**: Quick 3-5 sentence overview
  - **Detailed**: Comprehensive summary with key points
  - **Action Items**: Focus on decisions, tasks, and deadlines
- 💾 **Export Options**: Download full transcripts and complete reports
- 🎨 **Modern UI**: Clean, intuitive Gradio interface
- 🎤 **Recording Support**: Upload files or record directly in the browser

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone or download this repository**:
   ```bash
   cd /Users/yash/Documents/Projects/Unthinkable/meeting-summarizer-whisper-api
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key**:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   
   Or create a `.env` file in the project directory:
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

5. **Run the application**:
   ```bash
   python main.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:7860
   ```

## 📖 Usage

### Basic Workflow

1. **Upload Audio**: Click to upload an audio file or use the microphone to record
2. **Add Context** (Optional): Provide information about the meeting for better summaries
3. **Select Summary Style**: Choose between brief, detailed, or action-items format
4. **Choose Language**: Select the audio language or use auto-detection
5. **Submit**: Click submit and wait for processing (usually 30-60 seconds)
6. **Review & Download**: View the summary and download transcript/report files

### Supported Audio Formats

The application supports various audio formats including:
- MP3
- WAV
- M4A
- FLAC
- OGG
- WEBM

**Note**: Maximum file size is 25MB (OpenAI API limitation)

### Summary Styles Explained

- **Brief**: Perfect for quick overviews and time-pressed situations
  ```
  Example: "The team discussed Q4 goals, decided to prioritize feature X, 
  and assigned John to lead the implementation by October 30th."
  ```

- **Detailed**: Comprehensive breakdown of the entire meeting
  ```
  Example includes:
  - Main topics discussed
  - Key arguments and points
  - Decisions made with rationale
  - Action items and owners
  - Questions raised
  ```

- **Action Items**: Focused extraction of tasks and deliverables
  ```
  Example format:
  • Key Decisions:
    - Approved budget for Project X
  • Action Items:
    - John: Complete design mockups by Oct 20
    - Sarah: Review vendor proposals by Oct 25
  • Next Steps:
    - Schedule follow-up meeting for Oct 27
  ```

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY` (required): Your OpenAI API key

### Customization

You can modify the following in `main.py`:

- **Model Selection**: Change `gpt-4o-mini` to `gpt-4` or `gpt-3.5-turbo` (line 114)
- **Max Tokens**: Adjust `max_tokens` parameter for longer/shorter summaries (line 117)
- **Temperature**: Modify creativity level (0.0-1.0) in the GPT call (line 116)
- **Port**: Change `server_port` in the launch configuration (line 403)

## 💡 Tips for Best Results

1. **Audio Quality**: Use clear audio with minimal background noise
2. **File Size**: For longer meetings, consider splitting into shorter segments
3. **Context**: Providing meeting context significantly improves summary quality
4. **Language**: Specifying the language (instead of auto) can improve accuracy
5. **Summary Style**: Use action-items style for productive meeting summaries

## 📊 Output Files

The application generates two types of downloadable files:

### 1. Transcript File (`transcript_YYYYMMDD_HHMMSS.txt`)
- Complete transcription of the audio
- Metadata (language, duration)
- Timestamp

### 2. Full Report (`meeting_report_YYYYMMDD_HHMMSS.txt`)
- Meeting summary
- Full transcript
- Context and metadata
- Formatted for easy reading

## 🔒 Privacy & Security

- **API Calls**: All processing happens through OpenAI's secure API
- **Data Storage**: Files are saved locally only
- **No Cloud Storage**: Your audio and transcripts are not stored on external servers
- **API Key**: Keep your API key secure and never share it

## 💰 Cost Estimation

OpenAI API pricing (as of October 2024):

- **Whisper API**: ~$0.006 per minute of audio
- **GPT-4 Mini**: ~$0.15 per million input tokens, ~$0.60 per million output tokens

**Example**: A 30-minute meeting costs approximately:
- Transcription: $0.18
- Summary: $0.02-0.05
- **Total**: ~$0.20-0.23 per meeting

## 🛠️ Troubleshooting

### "OPENAI_API_KEY environment variable is not set"
- Make sure you've exported the API key in your terminal
- Or create a `.env` file with your API key

### "Error during transcription"
- Check if your audio file is under 25MB
- Verify the audio format is supported
- Ensure your API key is valid and has credits

### "Module not found" errors
- Make sure you've activated the virtual environment
- Run `pip install -r requirements.txt` again

### Gradio won't launch
- Check if port 7860 is already in use
- Try a different port by modifying `server_port` in main.py

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation


## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for the Whisper and GPT APIs
- [Gradio](https://gradio.app/) for the amazing UI framework

## 📧 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review [OpenAI API documentation](https://platform.openai.com/docs)
3. Open an issue on GitHub

---

**Built with ❤️ using Python, OpenAI, and Gradio**
