import json, os
from pathlib import Path

def save_checkpoint(r):
    history_path = Path(r.output) / "history.json"
    dst = Path(r.output) / "resume_checkpoint.json"
    tmp = Path(str(dst) + ".tmp")
    data = {
        "episode_id": r.episode,
        "step_id": r.tick,
        "task": r.task,
        "counters": dict(r.counters),
        "history_path": str(history_path),
        "history_length": len(r.history),
    }
    tmp.write_text(json.dumps(data, indent=2))
    os.replace(tmp, dst)
    print(f"CHECKPOINT_SAVED step={r.tick}", flush=True)
