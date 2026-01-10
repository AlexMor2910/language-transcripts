# Language Transcripts
CLI application for extracting transcripts from YouTube videos and subtitle files.

# Transcript & Subtitle Processor Documentation

This utility is designed to extract and clean text from YouTube videos and local subtitle files (`.srt`, `.ssa`, `.ass`).

---

## 📖 Table of Contents
1. [Overview](#overview)
2. [Installation & Requirements](#installation)
3. [Module Breakdown](#module-breakdown)
4. [User Instructions](#user-instructions)
5. [Technical Features](#technical-features)

---

## 1. Overview
The program serves two primary functions:
* **YouTube Transcript Extraction:** Connects to the YouTube API to fetch available transcripts in multiple languages.
* **Local Subtitle Processing:** Scans directories for subtitle files and converts them into clean text documents.

---

## 2. Installation & Requirements
The following third-party libraries are required to run the application:
* `youtube-transcript-api`: For fetching YouTube data.
* `pysubs2`: For handling `.ssa` and `.ass` files.
* `srt`: For parsing `.srt` files.
* `chardet`: For automatic file encoding detection.

---

## 3. Module Breakdown

| File | Purpose |
| :--- | :--- |
| `transcript_processor.py` | The main entry point and user menu. |
| `main_transcript_api.py` | Orchestrates the YouTube extraction workflow. |
| `main_srt_ssa.py` | Orchestrates local subtitle file scanning. |
| `auxf_transcript_api.py` | Logic for YouTube API communication and file creation. |
| `auxf_srt.py` | Logic for `.srt` cleaning and general file writing. |
| `auxf_ssa.py` | Logic for `.ssa`/`.ass` cleaning and style filtering. |

---

## 4. User Instructions

### Launching the Program
Run `python transcript_processor.py`.

### Option 's': Local Subtitles
1. **Input Language:** Type the language name to be included in the filename.
2. **Automatic Scan:** The script searches the current directory and subdirectories for `.srt`, `.ssa`, and `.ass` files.
3. **Output:** Generates a `.txt` file for every subtitle file found.

### Option 't': YouTube Transcripts
1. **Enter ID:** Provide the YouTube Video ID.
2. **Select Language:** Choose from the available list by number, or type 'all'.
3. **Output:** Saves transcripts as `Transcript_[VideoID]_[Lang].txt`.

---

## 5. Technical Features
* **Encoding Detection:** Uses `chardet` to ensure local files are read correctly regardless of origin.
* **Style Filtering:** Automatically ignores non-dialogue styles in SSA/ASS files such as 'staff', 'op', 'ed', and 'screen'.
* **Conflict Prevention:** Automatically renames output files (e.g., adding `(1)`) if a file with the same name already exists.
