from pathlib import Path
from clipproof.core import Report
from clipproof.cli import render_html

def test_report_profile_and_transcript_fields():
    report = Report("demo.mp4", "PASS", 5.0, {}, {}, {}, [], "shorts", {"sequence_similarity": 1.0})
    data = report.to_dict()
    assert data["profile"] == "shorts"
    assert data["transcript_comparison"]["sequence_similarity"] == 1.0

def test_html_escapes_filename(tmp_path: Path):
    report = {"file":"<video>.mp4", "status":"WARN", "duration_seconds":8,
              "video":{"width":1080,"height":1920,"codec":"h264"}, "profile":"shorts",
              "findings":[{"code":"LONG_SILENCE","severity":"warning","message":"Quiet part","details":{"start":2,"end":4}}]}
    output = tmp_path / "report.html"
    render_html([report], output)
    content = output.read_text()
    assert "&lt;video&gt;.mp4" in content
    assert "LONG_SILENCE" in content
    assert "timeline" in content
