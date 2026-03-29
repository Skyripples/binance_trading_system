"""Public-safe backtest showcase derived from the private eth_spot_backtest.py layout.

This file preserves the research/backtest split while omitting the private
strategy formula and tuning details.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any


@dataclass(frozen=True)
class StrategyConfig:
    run_preset: str = 'dynamic_balanced'
    initial_usdt: float = 3000.0
    startup_target_eth: float = 1.0
    start_date: str = '2023-12-22 00:00:00'
    end_date: str = '2025-12-31 23:59:59'
    grid_step: float = 100.0
    trade_qty: float = 0.1


DATA_FILE = Path('data/ETHUSDT_spot_monthly_klines_5m.csv')


def load_backtest_data() -> str:
    """Public placeholder for merged historical spot data loading."""
    return str(DATA_FILE)


def prepare_features() -> None:
    """Public placeholder for feature engineering.

    Private implementation computes additional context and uses internal rules
    that are intentionally not published here.
    """


def run_backtest(config: StrategyConfig) -> Dict[str, Any]:
    """Public-safe summary schema.

    Private implementation simulates startup inventory bootstrap, grid buys,
    grid sells, fees, and summary generation.
    """
    return {
        'run_preset': config.run_preset,
        'symbol': 'ETHUSDT_SPOT',
        'initial_usdt': config.initial_usdt,
        'startup_target_eth': config.startup_target_eth,
        'grid_step': config.grid_step,
        'trade_qty': config.trade_qty,
    }


def main() -> None:
    config = StrategyConfig()
    print('Public backtest showcase skeleton')
    print(load_backtest_data())
    prepare_features()
    print(run_backtest(config))


if __name__ == '__main__':
    main()
