"""Public-safe stub for the live spot runner interface.

This file intentionally omits production exchange calls and secrets.
It exists to show public repository structure only.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class LiveConfig:
    symbol: str = 'ETHUSDT'
    grid_step: float = 100.0
    trade_qty: float = 0.1
    startup_target_eth: float = 1.0
    poll_seconds: int = 30
    state_file: Path = Path('state/eth_spot_live_state.json')
    trades_file: Path = Path('result/eth_spot_live_trades.csv')


def main() -> None:
    cfg = LiveConfig()
    print('Public live runner stub')
    print(cfg)


if __name__ == '__main__':
    main()
