# Configuration file for Meeting Summarizer
# Copy this to config.py and customize as needed

# OpenAI Configuration
OPENAI_MODEL_TRANSCRIPTION = "whisper-1"  # Whisper model for transcription
OPENAI_MODEL_SUMMARY = "gpt-4o-mini"       # GPT model for summarization (gpt-4, gpt-4o-mini, gpt-3.5-turbo)

# Summary Generation
MAX_TOKENS = 2000           # Maximum tokens for summary generation
TEMPERATURE = 0.7           # Creativity level (0.0-1.0, lower = more focused)

# Gradio Interface
GRADIO_SERVER_NAME = "127.0.0.1"
GRADIO_SERVER_PORT = 7860
GRADIO_SHARE = False        # Set to True to create a public link
GRADIO_DEBUG = True

# File Settings
MAX_AUDIO_SIZE_MB = 25      # Maximum audio file size (OpenAI limit)
OUTPUT_DIR = "."            # Directory for output files

# Supported Languages
SUPPORTED_LANGUAGES = {
    "auto": "Auto-detect",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "pl": "Polish",
    "ru": "Russian",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean"
}
