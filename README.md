# Pomodoro Timer

A GUI-based Pomodoro timer built with Tkinter to help manage work and break intervals using the Pomodoro technique.

## Features
- Standard Pomodoro cycles (25 min work, 5 min short break, 20 min long break)
- Visual timer with tomato graphic
- Pause and resume functionality
- Reset option
- Checkmarks for completed work sessions
- Audio alert and window focus when timer nears completion

## Prerequisites
- Python 3.x
- Required Python packages:
  - `tkinter` (usually included with Python)
  - `winsound` (Windows only, included with Python)
- Required asset:
  - `tomato.png` (220x224 pixel image file)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/pomodoro-timer.git
cd pomodoro-timer
```

2. Ensure `tomato.png` is in the project directory

## Usage
1. Run the application:
```bash
python pomodoro_timer.py
```

2. Use the GUI:
- Click "Start" to begin the timer
- Click "Pause" to pause/resume
- Click "Reset" to start over

## Pomodoro Cycle
- Work: 25 minutes
- Short Break: 5 minutes (after every work session except 4th)
- Long Break: 20 minutes (after 4th work session)
- Checkmark (✔) added after each work session

## How It Works
- Uses 25/5/20 minute intervals following Pomodoro technique
- Plays a beep sound 3 seconds before timer ends (Windows only)
- Brings window to front for last 3 seconds
- Tracks completed work sessions with checkmarks
- Supports pausing and resuming from exact point

## File Structure
- `pomodoro_timer.py`: Main application file
- `tomato.png`: Tomato image for GUI (required)

## GUI Components
- Timer label (Work/Break indicator)
- Tomato canvas with countdown display
- Start, Pause, and Reset buttons
- Checkmark display for completed sessions

## Customization
Constants available for modification:
- `WORK_MIN`: Work session length (default: 25)
- `SHORT_BREAK_MIN`: Short break length (default: 5)
- `LONG_BREAK_MIN`: Long break length (default: 20)
- Colors: `PINK`, `RED`, `GREEN`, `YELLOW`
- `FONT_NAME`: Default "Courier"

## Notes
- Designed for Windows (uses `winsound` for audio)
- Window stays on top for 3 seconds before timer ends
- Paused time is preserved for resuming
- Background color and padding customizable
- Requires `tomato.png` in same directory

## Limitations
- Audio alert Windows-only (modify for other OS)
- No persistent storage of progress
- Fixed 25/5/20 minute intervals (customizable in code only)
- Single-task focus

## License
[MIT License](LICENSE)

## Disclaimer
- Ensure `tomato.png` is present or update image path
- For non-Windows systems, modify/remove `winsound` usage
- Basic implementation without settings persistence
```

