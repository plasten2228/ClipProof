from pathlib import Path
from clipproof.core import parse_srt


def test_parse_srt_comma_and_dot_milliseconds(tmp_path: Path):
    sample = """1
00:00:01,000 --> 00:00:02,500
Hello

2
00:00:03.000 --> 00:00:04.000
World
"""
    path = tmp_path / "sample.srt"
    path.write_text(sample, encoding="utf-8")
    cues = parse_srt(path)
    assert len(cues) == 2
    assert cues[0]["start"] == 1
    assert cues[0]["end"] == 2.5
    assert cues[1]["text"] == "World"
