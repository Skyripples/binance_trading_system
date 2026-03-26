# ETH Futures 4 Showcase

## Summary
This showcase represents a lower-frequency ETHUSDT perpetual futures research branch.

## Public scope
Included:
- strategy intent
- architecture overview
- validation workflow
- sample config shape
- sample report format

Excluded:
- production signal formula
- live execution code
- private deployment logic
- sensitive parameter presets

## Strategy profile
- market: ETHUSDT perpetual futures
- style: trend-following / regime-filtered swing intraday
- target behavior: fewer but higher-quality trades
- emphasis: validation discipline over signal frequency

## Validation approach
- historical backtest
- cost-aware evaluation
- regime decomposition
- walk-forward review
- live vs paper operational comparison in private environment

## Files
- `docs/architecture.md`: system overview
- `examples/public_config.example.yaml`: public-safe config shape
- `examples/sample_backtest_summary.json`: sample report schema
- `examples/sample_trades.csv`: sample trade log schema
- `src/run_backtest_showcase.py`: runner stub for portfolio demonstration
