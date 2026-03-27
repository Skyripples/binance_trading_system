# ETH Spot Showcase

Public portfolio version of the current ETH spot strategy branch.

This strategy is intentionally simpler than the private futures stack and is designed around a stateful spot inventory process instead of leveraged directional exposure.

## Public Strategy Summary

Core behavior shown in this public version:
- startup inventory bootstrap to a target ETH base position
- fixed USD grid spacing for recurring buy / sell execution
- state persistence for long-running execution
- trade log output for operational review
- optional Telegram notifications for live events
- clear separation between backtest and live runner responsibilities

## Private / Redacted Boundaries

The following are intentionally excluded from the public repository:
- API keys and environment secrets
- exact server deployment credentials
- production account state and real trade logs
- full operational hardening details
- production-specific safeguards and recovery playbooks

## Repository Mapping

The private project keeps two separate files for this strategy line:
- `eth_spot_backtest.py`: backtest and validation workflow
- `eth_spot.py`: live spot executor

The public showcase mirrors that split conceptually, while keeping the implementation sanitized.

## Live Execution Model

High-level live flow:
1. load environment and exchange metadata
2. verify account connectivity
3. top up startup inventory to a target ETH amount if needed
4. establish or restore grid anchor state
5. place spot market buys on downward grid breaks
6. place spot market sells on upward grid breaks
7. persist state and append trade logs
8. send notifications for startup, trades, and errors

## Backtest Model

High-level backtest flow:
1. load merged historical spot bars
2. compute basic volatility and range context
3. simulate startup inventory bootstrap
4. simulate grid buys and sells with fees
5. generate trade log, equity curve, and summary output

## Public Files In This Showcase

- `docs/architecture.md`
- `examples/public_env.example`
- `examples/sample_trade_log.csv`
- `examples/sample_live_state.json`
- `examples/sample_backtest_summary.json`
- `src/live_runner_stub.py`

## Portfolio Use

This folder is intended for interview discussion and code review. It is not a plug-and-play live trading bot.
