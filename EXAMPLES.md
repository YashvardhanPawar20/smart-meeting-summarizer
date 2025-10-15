# 📖 Usage Examples

## Example 1: Quick Summary of Team Meeting

### Input:
- **Audio File**: `team_standup.mp3` (5 minutes)
- **Context**: "Daily standup meeting"
- **Summary Style**: Brief
- **Language**: English

### Output:
```
Summary:
The team discussed progress on the Q4 roadmap. Sarah completed the 
user authentication feature, John is working on the payment integration 
with an expected completion by Friday, and Mike raised concerns about 
API rate limits that need to be addressed in the next sprint.

Files Generated:
- transcript_20241015_143022.txt (Full transcription)
- meeting_report_20241015_143022.txt (Summary + Transcript)
```

---

## Example 2: Client Meeting with Action Items

### Input:
- **Audio File**: `client_meeting.m4a` (30 minutes)
- **Context**: "Q4 planning meeting with Acme Corp"
- **Summary Style**: Action Items
- **Language**: English

### Output:
```
Summary:

KEY DECISIONS:
• Approved the proposed timeline for Phase 2 implementation
• Agreed to bi-weekly progress reports starting next Monday
• Budget increase of $50K approved for additional resources

ACTION ITEMS:
• Sarah: Prepare detailed technical specification by Oct 20
• John: Set up staging environment for client testing by Oct 22
• Team: Complete user acceptance testing by Nov 1
• Client (Tom): Provide list of required integrations by Oct 18

NEXT STEPS:
• Schedule kickoff meeting for Phase 2 on Oct 25
• Weekly check-ins every Thursday at 2 PM
• Next client meeting on Nov 5 to review progress

IMPORTANT DATES:
• Oct 18: Client deliverables due
• Oct 20: Technical spec due
• Oct 22: Staging environment ready
• Oct 25: Phase 2 kickoff
• Nov 1: UAT completion
• Nov 5: Progress review meeting
```

---

## Example 3: Multi-language Conference Call

### Input:
- **Audio File**: `spanish_meeting.wav` (15 minutes)
- **Context**: "Partnership discussion with Madrid office"
- **Summary Style**: Detailed
- **Language**: Spanish (es)

### Process:
1. Whisper API transcribes the Spanish audio
2. GPT-4 generates an English summary
3. Both transcript (in Spanish) and summary (in English) are saved

### Output:
```
Summary:

MAIN TOPICS DISCUSSED:
The Madrid office presented their Q4 results, showing 23% growth in 
customer acquisition. The team discussed expanding the partnership 
program to include three new regions: Valencia, Barcelona, and Seville.

KEY POINTS:
• Madrid office exceeded quarterly targets by 15%
• New partnership model proposed for regional expansion
• Budget allocation discussed for marketing campaigns
• Technical integration requirements identified

DECISIONS MADE:
• Approved expansion to three new Spanish regions
• Allocated €150,000 for regional marketing
• Agreed to standardize technical documentation in both languages
• Established monthly cross-office sync meetings

QUESTIONS RAISED:
• How to handle different tax regulations across regions?
• What's the timeline for technical integration?
• Who will lead the regional expansion efforts?

ACTION ITEMS:
• Ana: Draft expansion proposal by next week
• Carlos: Prepare cost analysis for regional offices
• Tech team: Create integration timeline and requirements
• Legal: Review regional compliance requirements
```

---

## Example 4: Recording Directly in Browser

### Steps:
1. Open the application: http://127.0.0.1:7860
2. Click the microphone icon in the audio input
3. Click "Record" and start speaking
4. Click "Stop" when done
5. Add context: "Quick voice note about project ideas"
6. Select "Brief" summary
7. Click Submit

### Use Cases:
- Quick voice notes after meetings
- Personal reminders with automatic transcription
- Brainstorming sessions
- Interview recordings
- Lecture notes

---

## Example 5: Batch Processing (Using Python Script)

If you need to process multiple files, you can use this script:

```python
import os
from main import process_meeting

# List of audio files to process
audio_files = [
    "meeting1.mp3",
    "meeting2.wav",
    "meeting3.m4a"
]

contexts = [
    "Monday team standup",
    "Client review meeting",
    "Sprint planning"
]

# Process each file
for audio_file, context in zip(audio_files, contexts):
    if os.path.exists(audio_file):
        print(f"Processing: {audio_file}")
        summary, transcript_file, report_file = process_meeting(
            audio_file, 
            context, 
            "detailed",  # summary style
            None  # auto-detect language
        )
        print(f"✓ Completed: {audio_file}")
        print(f"  Summary: {summary[:100]}...")
        print()
```

---

## Tips for Best Results

### Audio Quality
✅ **Good:**
- Clear recording with minimal background noise
- Single speaker or well-separated voices
- Good microphone quality
- Proper audio levels (not too quiet or distorted)

❌ **Avoid:**
- Very noisy environments
- Multiple overlapping speakers
- Poor microphone quality
- Very low volume recordings

### Summary Styles

**Use "Brief" when:**
- You need a quick overview
- Time is limited
- Just want key takeaways
- Sending to busy executives

**Use "Detailed" when:**
- You need comprehensive notes
- Want to capture all discussion points
- Creating meeting documentation
- Need to reference specific topics later

**Use "Action Items" when:**
- Need to track tasks and responsibilities
- Following up on decisions
- Creating project documentation
- Sending to team members for action

### Context Tips

Good context examples:
- "Weekly engineering team standup"
- "Q4 planning meeting with product and marketing"
- "Client onboarding call for Project Phoenix"
- "Technical discussion about API design"

Bad context examples:
- "Meeting" (too vague)
- [Empty] (missing helpful information)
- Very long paragraphs (keep it concise)

---

## Cost Examples

Based on OpenAI pricing (October 2024):

| Meeting Length | Transcription Cost | Summary Cost | Total Cost |
|----------------|-------------------|--------------|------------|
| 5 minutes      | $0.03             | $0.01        | ~$0.04     |
| 15 minutes     | $0.09             | $0.02        | ~$0.11     |
| 30 minutes     | $0.18             | $0.03        | ~$0.21     |
| 1 hour         | $0.36             | $0.05        | ~$0.41     |

*Note: Actual costs may vary based on audio quality and summary length*

---

## Common Workflows

### Workflow 1: Daily Standups
```
1. Record 5-min standup (upload or record)
2. Use "Brief" summary
3. Share summary with team via email/Slack
4. Archive transcript for reference
```

### Workflow 2: Client Meetings
```
1. Upload meeting recording
2. Add context with client name and topics
3. Use "Action Items" summary
4. Send action items to team
5. File full report for documentation
```

### Workflow 3: Lectures/Training
```
1. Upload lecture recording
2. Use "Detailed" summary
3. Review transcript for accuracy
4. Create study notes from summary
5. Share with classmates/team
```

---

## Troubleshooting Examples

### Problem: "Audio file too large"
**Solution**: 
- Split large files into smaller segments
- Compress audio (lower bitrate)
- Use MP3 format instead of WAV

### Problem: "Poor transcription quality"
**Solution**:
- Specify language instead of auto-detect
- Improve audio quality
- Remove background noise with audio editor

### Problem: "Summary not detailed enough"
**Solution**:
- Switch from "Brief" to "Detailed"
- Add more context about the meeting
- Edit `MAX_TOKENS` in config to allow longer summaries

---

**Ready to try these examples? Run `./start.sh` and start processing your meetings!**
