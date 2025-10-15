#!/usr/bin/env python3
"""
Smart Meeting Summarizer using OpenAI Whisper API
This application transcribes audio files and generates summaries using OpenAI's APIs.
"""

import os
import gradio as gr
from openai import OpenAI
from pathlib import Path
import json
from datetime import datetime
from typing import Optional, Tuple
import tempfile

# Initialize OpenAI client
client = None


def initialize_client():
    """Initialize OpenAI client with API key from environment variable."""
    global client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set. "
            "Please set it with: export OPENAI_API_KEY='your-api-key'"
        )
    client = OpenAI(api_key=api_key)
    return client


def transcribe_audio(audio_file_path: str, language: Optional[str] = None) -> dict:
    """
    Transcribe audio file using OpenAI Whisper API.
    
    Args:
        audio_file_path: Path to the audio file
        language: Optional language code (e.g., 'en', 'es', 'fr')
    
    Returns:
        Dictionary containing transcript and metadata
    """
    if not client:
        initialize_client()
    
    print(f"Transcribing audio file: {audio_file_path}")
    
    try:
        with open(audio_file_path, "rb") as audio_file:
            # Use Whisper API for transcription
            transcript_params = {
                "model": "whisper-1",
                "file": audio_file,
                "response_format": "verbose_json"
            }
            
            if language:
                transcript_params["language"] = language
            
            transcript_response = client.audio.transcriptions.create(**transcript_params)
        
        # Extract transcript text
        transcript_text = transcript_response.text
        
        # Get additional metadata if available
        metadata = {
            "language": getattr(transcript_response, 'language', 'unknown'),
            "duration": getattr(transcript_response, 'duration', 0),
            "segments": getattr(transcript_response, 'segments', [])
        }
        
        print("Transcription completed successfully")
        return {
            "text": transcript_text,
            "metadata": metadata
        }
    
    except Exception as e:
        raise Exception(f"Error during transcription: {str(e)}")


def generate_summary(
    transcript: str,
    context: str = "",
    summary_style: str = "detailed"
) -> str:
    """
    Generate a summary of the transcript using OpenAI GPT API.
    
    Args:
        transcript: The transcribed text
        context: Optional context about the meeting
        summary_style: Style of summary ('brief', 'detailed', 'action-items')
    
    Returns:
        Generated summary text
    """
    if not client:
        initialize_client()
    
    print(f"Generating {summary_style} summary...")
    
    # Customize prompt based on summary style
    if summary_style == "brief":
        style_instruction = "Provide a brief, high-level summary in 3-5 sentences."
    elif summary_style == "action-items":
        style_instruction = """Focus on extracting:
        - Key decisions made
        - Action items and their owners
        - Deadlines mentioned
        - Next steps
        Format as a bulleted list."""
    else:  # detailed
        style_instruction = """Provide a comprehensive summary including:
        - Main topics discussed
        - Key points and arguments
        - Decisions made
        - Action items
        - Important questions raised"""
    
    system_prompt = """You are an expert meeting assistant that creates clear, 
    well-structured summaries of meeting transcripts. Focus on extracting the most 
    important information and presenting it in an organized manner."""
    
    user_prompt = f"""Please analyze this meeting transcript and create a summary.

Context: {context if context else 'No additional context provided.'}

Summary Style: {style_instruction}

Transcript:
{transcript}

Please provide the summary:"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using GPT-4 mini for cost-effectiveness
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        summary = response.choices[0].message.content
        print("Summary generated successfully")
        return summary
    
    except Exception as e:
        raise Exception(f"Error during summary generation: {str(e)}")


def save_transcript_to_file(transcript: str, metadata: dict = None) -> str:
    """
    Save transcript to a text file with timestamp.
    
    Args:
        transcript: The transcript text
        metadata: Optional metadata to include
    
    Returns:
        Path to the saved file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcript_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("MEETING TRANSCRIPT\n")
        f.write("=" * 80 + "\n\n")
        
        if metadata:
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            if metadata.get('language'):
                f.write(f"Language: {metadata['language']}\n")
            if metadata.get('duration'):
                f.write(f"Duration: {metadata['duration']:.2f} seconds\n")
            f.write("\n")
        
        f.write("TRANSCRIPT:\n")
        f.write("-" * 80 + "\n\n")
        f.write(transcript)
        f.write("\n\n" + "=" * 80 + "\n")
    
    return filename


def save_full_report(
    transcript: str,
    summary: str,
    context: str = "",
    metadata: dict = None
) -> str:
    """
    Save a full report including transcript and summary.
    
    Args:
        transcript: The transcript text
        summary: The generated summary
        context: Optional context
        metadata: Optional metadata
    
    Returns:
        Path to the saved file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"meeting_report_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("MEETING REPORT\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        if context:
            f.write(f"Context: {context}\n\n")
        
        if metadata:
            if metadata.get('language'):
                f.write(f"Language: {metadata['language']}\n")
            if metadata.get('duration'):
                f.write(f"Duration: {metadata['duration']:.2f} seconds\n")
            f.write("\n")
        
        f.write("=" * 80 + "\n")
        f.write("SUMMARY\n")
        f.write("=" * 80 + "\n\n")
        f.write(summary)
        f.write("\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("FULL TRANSCRIPT\n")
        f.write("=" * 80 + "\n\n")
        f.write(transcript)
        f.write("\n\n" + "=" * 80 + "\n")
    
    return filename


def process_meeting(
    audio_file_path: str,
    context: str,
    summary_style: str,
    language: Optional[str]
) -> Tuple[str, str, str]:
    """
    Main processing function that handles the complete workflow.
    
    Args:
        audio_file_path: Path to the audio file
        context: Optional context about the meeting
        summary_style: Style of summary to generate
        language: Optional language code
    
    Returns:
        Tuple of (summary, transcript_file_path, report_file_path)
    """
    try:
        # Step 1: Transcribe audio
        transcript_data = transcribe_audio(audio_file_path, language)
        transcript = transcript_data["text"]
        metadata = transcript_data["metadata"]
        
        # Step 2: Generate summary
        summary = generate_summary(transcript, context, summary_style)
        
        # Step 3: Save files
        transcript_file = save_transcript_to_file(transcript, metadata)
        report_file = save_full_report(transcript, summary, context, metadata)
        
        return summary, transcript_file, report_file
    
    except Exception as e:
        error_msg = f"Error processing meeting: {str(e)}"
        print(error_msg)
        return error_msg, None, None


def gradio_interface(
    audio,
    context: str,
    summary_style: str,
    language: str
) -> Tuple[str, str, str]:
    """
    Gradio wrapper function for the interface.
    
    Args:
        audio: Uploaded audio file from Gradio
        context: Meeting context
        summary_style: Type of summary
        language: Language code
    
    Returns:
        Tuple of (summary, transcript_file, report_file)
    """
    if audio is None:
        return "Please upload an audio file.", None, None
    
    # Process language input
    language_code = None if language == "auto" else language
    
    return process_meeting(audio, context, summary_style, language_code)


def create_gradio_app():
    """Create and configure the Gradio interface."""
    
    # Check if API key is set
    try:
        initialize_client()
    except ValueError as e:
        print(f"\n⚠️  ERROR: {str(e)}\n")
        return None
    
    # Define the interface
    iface = gr.Interface(
        fn=gradio_interface,
        inputs=[
            gr.Audio(
                sources=["upload", "microphone"],
                type="filepath",
                label="Upload Audio File or Record"
            ),
            gr.Textbox(
                label="Meeting Context (Optional)",
                placeholder="e.g., 'Weekly team standup' or 'Q4 planning meeting'",
                lines=2
            ),
            gr.Radio(
                choices=["brief", "detailed", "action-items"],
                value="detailed",
                label="Summary Style",
                info="Choose the type of summary you want"
            ),
            gr.Dropdown(
                choices=["auto", "en", "es", "fr", "de", "it", "pt", "nl", "pl", "ru", "zh", "ja", "ko"],
                value="auto",
                label="Audio Language",
                info="Select language for better accuracy, or use 'auto' for automatic detection"
            )
        ],
        outputs=[
            gr.Textbox(
                label="Meeting Summary",
                lines=15,
                show_copy_button=True
            ),
            gr.File(
                label="Download Transcript"
            ),
            gr.File(
                label="Download Full Report"
            )
        ],
        title="🎙️ Smart Meeting Summarizer",
        description="""
        Upload an audio recording of your meeting and get an AI-generated summary along with the full transcript.
        
        **Features:**
        - 🎯 Automatic transcription using OpenAI Whisper API
        - 📝 Intelligent summarization with GPT-4
        - 🌍 Multi-language support
        - 📊 Multiple summary styles (brief, detailed, action items)
        - 💾 Downloadable transcripts and reports
        
        **Supported audio formats:** MP3, WAV, M4A, FLAC, and more (max 25MB)
        """,
        article="""
        ### How to use:
        1. Upload an audio file or record directly
        2. (Optional) Provide context about the meeting
        3. Select your preferred summary style
        4. Choose the audio language or use auto-detection
        5. Click Submit and wait for processing
        
        ### Tips:
        - For best results, use clear audio with minimal background noise
        - The 'action-items' style is great for extracting tasks and deadlines
        - Use 'brief' for quick overviews, 'detailed' for comprehensive summaries
        
        **Note:** Requires OpenAI API key to be set in environment variables.
        """,
        theme=gr.themes.Soft(),
        analytics_enabled=False
    )
    
    return iface


def main():
    """Main entry point for the application."""
    print("=" * 80)
    print("Smart Meeting Summarizer with OpenAI Whisper API")
    print("=" * 80)
    print()
    
    # Create and launch the Gradio app
    app = create_gradio_app()
    
    if app:
        print("\n✅ Application ready!")
        print("🚀 Launching Gradio interface...\n")
        app.launch(
            share=False,
            server_name="127.0.0.1",
            server_port=7860,
            show_error=True
        )
    else:
        print("❌ Failed to initialize application. Please check your API key.")
        print("\nTo set your OpenAI API key:")
        print("  export OPENAI_API_KEY='your-api-key-here'")


if __name__ == "__main__":
    main()
