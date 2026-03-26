"""Public runner stub for portfolio demonstration.

This file intentionally does not include production alpha logic.
It only documents the expected control flow of a backtest entrypoint.
"""

from pathlib import Path
import json


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    example_summary = root / "examples" / "sample_backtest_summary.json"
    data = json.loads(example_summary.read_text(encoding="utf-8-sig"))
    print("ETH Futures 4 public showcase")
    print("This public runner is a stub. Production strategy logic is private.")
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
