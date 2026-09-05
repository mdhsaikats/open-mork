# Open Mork

Open Mork is a Python-based personal assistant backend prototype inspired by voice-first AI assistants. The project is still in an early stage and currently focuses on the foundation for voice input, tool integrations, and future LLM-powered assistant behavior.

## Overview

This project is organized around a simple assistant architecture:

- A voice layer to capture and process microphone input
- A core layer for LLM and memory orchestration
- A tools layer for actions such as weather, smart home control, and web search
- A central application entry point for running the assistant

At this stage, the repository is a scaffold for building a voice-enabled assistant rather than a fully complete application.

## Current project structure

```text
open-mork-backend/
├── main.py
├── README.md
├── requirements.txt
├── .env
├── core/
│   ├── llm_engin.py
│   ├── memory.py
│   └── prompts.py
├── senses/
│   ├── ears.py
│   └── mouth.py
└── tools/
    ├── __init__.py
    ├── smarthome.py
    ├── weather.py
    └── web_search.py
```

### What each part is for

- `main.py` — application entry point
- `core/llm_engin.py` — intended for LLM engine integration
- `core/memory.py` — intended for conversation/state memory
- `core/prompts.py` — prompts and assistant behavior definitions
- `senses/ears.py` — microphone-based speech recognition using SpeechRecognition
- `senses/mouth.py` — intended for text-to-speech output
- `tools/weather.py` — weather tool placeholder
- `tools/smarthome.py` — smart home automation placeholder
- `tools/web_search.py` — web search tool placeholder

## Features

### Implemented or partially implemented

- Microphone listening via `SpeechRecognition`
- Ambient-noise calibration before listening
- Speech-to-text conversion using Google Speech Recognition API
- Basic command loop for listening and exiting on `exit`

### Planned / scaffolded

- LLM-powered assistant reasoning
- Persistent memory layer
- Prompt engineering and assistant persona setup
- Voice output / text-to-speech
- Weather lookup
- Smart home actions
- Web search integrations

## Requirements

This project requires:

- Python 3.10+
- A microphone connected to the system
- Internet access for Google speech recognition requests

## Setup

1. Clone the repository:

```bash
git clone https://github.com/mdhsaikats/open-mork.git
cd open-mork-backend
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the project

The current entry point is:

```bash
python main.py
```

At the moment, the script is a placeholder and simply prints a message. The more functional voice-assistant behavior is in the early development stage, especially in the `senses/ears.py` module.

## Important notes

- This project is not yet a production-ready assistant.
- Several modules are intentionally empty placeholders.
- The `senses/ears.py` implementation depends on Google’s speech recognition service and may require a valid network connection.
- The `.env` file exists but is currently empty, so environment variables should be added as the project evolves.

## Dependencies

The project currently uses:

```text
audioop-lts==0.2.2
PyAudio==0.2.14
SpeechRecognition==3.17.0
standard-aifc==3.13.0
standard-chunk==3.13.0
typing_extensions==4.16.0
```

## Future direction

The repository appears to be aiming toward a local voice assistant with capabilities similar to:

- wake word or command listening
- voice-to-text input
- LLM-generated responses
- memory-driven conversations
- useful tool execution for weather, home automation, and web lookup

This README reflects the current repository state and should be updated as the assistant becomes more feature-complete.
