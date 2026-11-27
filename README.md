# ClipProof

**Version 0.2.0** · MIT License

A free, local-first command-line quality checker for finished videos. ClipProof inspects rendered videos and reports common delivery problems before publication. Your media stays on your computer; no AI API key is required.

> Early release: ClipProof is a first-pass checker, not a replacement for watching the final video. Detection thresholds can produce false positives.

## Checks

- Video metadata: duration, dimensions, codec, and frame-rate metadata.
- Long black-screen segments via FFmpeg `blackdetect`.
- Long low-audio/silence segments via FFmpeg `silencedetect`.
- Average and peak audio level via FFmpeg `volumedetect`.
- Optional SubRip (`.srt`) timing checks: malformed timestamps, overlaps, cues beyond video duration, and subtitles ending unusually early.
- Terminal output, JSON reports, and standalone HTML reports with timeline markers.
- Batch scanning of a directory.
- Delivery profiles: YouTube landscape, Shorts vertical, and podcast video.
- Optional text-only comparison of an SRT file against a supplied script.
- Exit codes for automation and CI.

## Requirements

- Python 3.10+
- FFprobe (required)
- FFmpeg (recommended for black-screen and audio checks)

Install FFmpeg:
- macOS: `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt install ffmpeg`
- Windows: install a trusted FFmpeg build and add `ffmpeg` and `ffprobe` to `PATH`.

## Install

```bash
git clone https://github.com/plasten2228/ClipProof.git
cd ClipProof
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

## Usage

```bash
clipproof final_video.mp4
clipproof final_video.mp4 --subtitles captions.srt
clipproof final_video.mp4 --subtitles captions.srt --json report.json --html report.html
clipproof final_video.mp4 --profile shorts
clipproof final_video.mp4 --subtitles captions.srt --transcript script.txt
clipproof ./exports --batch --profile shorts --html batch-report.html --json batch-report.json
```

Tune thresholds:

```bash
clipproof final_video.mp4 --black-min-duration 1.5 --silence-min-duration 1.2 --silence-db -42
```

Make warnings fail a CI job:

```bash
clipproof final_video.mp4 --fail-on-warning
```

## Exit codes

| Code | Meaning |
|---:|---|
| `0` | Checks completed; no errors (warnings may exist unless `--fail-on-warning` is used) |
| `1` | A quality error was found, or `--fail-on-warning` was set and a warning was found |
| `2` | Input, dependency, or execution error |

## Known limitations

- Silence detection measures signal level, not whether speech is present. Quiet narration can be flagged; background music can hide missing speech.
- Peak level near 0 dBFS is a clipping-risk indicator, not proof of audible distortion.
- Black detection can flag intentional fades or dark scenes.
- Subtitle checks support SRT files only and validate timing, not translation quality or synchronization against spoken words.
- Script comparison is text-only; it does not listen to audio or verify spoken-word timing.
- Batch mode scans one directory level and does not accept per-video subtitle files.
- Delivery profiles are recommendations, not platform certification.
- No automatic speech recognition, scene understanding, or loudness normalization is included.

## Development

```bash
python -m pip install -e ".[dev]"
pytest
```

Please open an issue with your OS, Python version, FFmpeg version, command used, and a short anonymized report. Do not upload private video files unless you intend to share them publicly.

## Privacy

ClipProof processes files locally. It does not make network requests, send analytics, or upload videos.

## License

MIT. See [LICENSE](LICENSE).
