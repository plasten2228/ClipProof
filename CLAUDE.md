# Instructions for Claude Code

You are contributing to ClipProof, a free, local-first Python CLI that checks rendered videos using FFmpeg/FFprobe.

## Product principles
- Keep the core offline. Never upload media or add telemetry.
- Prefer deterministic, explainable checks over opaque AI claims.
- Findings must distinguish `error`, `warning`, and `info`.
- Be honest about heuristics and false positives.
- Preserve Python 3.10 compatibility and a dependency-light core.

## Architecture
- `src/clipproof/core.py`: probing, FFmpeg invocation, SRT parsing, report data structures.
- `src/clipproof/cli.py`: arguments, terminal presentation, exit codes.
- `tests/`: pytest tests.

## Development rules
- Add tests for every bug fix and feature.
- Use `subprocess.run` with argument lists; never build shell command strings or use `shell=True`.
- Handle missing executables, malformed media, timeouts, and unreadable files with actionable errors.
- Do not silently swallow FFmpeg errors. If a check cannot run, add a clear finding or raise `ClipProofError`.
- Do not claim silence detection is speech detection, or peak-level checks prove audible clipping.
- Keep JSON output stable and machine-readable.
- Do not add network access, analytics, or cloud dependencies.
- Update README and this file when CLI behavior or limitations change.

## Before finishing
1. Run `python -m pytest`.
2. Run `python -m compileall src`.
3. Test `clipproof --help` after editable installation.
4. Summarize changed files, tests run, and known limitations.

## Version 0.2.0
- `--html` writes a self-contained HTML report. Escape all user-controlled text.
- `--batch` scans one directory level for supported video extensions.
- `--profile` applies resolution/orientation recommendations, not platform guarantees.
- `--transcript` compares supplied script text with SRT text only; it does not inspect spoken audio.
