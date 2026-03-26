# Binance Trading System

Public portfolio version of a larger private trading research system focused on Binance markets.

This repository is designed for interviews and technical review. It showcases how I structure strategy research, backtesting, risk controls, and execution boundaries without exposing production-sensitive logic.

## Scope

The private system behind this portfolio includes:
- futures strategy research
- spot strategy research
- backtest and validation workflows
- execution abstractions for paper / testnet / live modes
- reporting, stress testing, and operational tooling

This public version keeps the engineering structure and documentation, while removing sensitive details.

## What This Repository Demonstrates

- strategy-oriented project organization
- reusable module boundaries for data, signals, risk, execution, and reporting
- separation between research code and production deployment
- cost-aware validation mindset
- portfolio-safe examples of configs, reports, and runner interfaces

## What Is Intentionally Excluded

To keep the repository safe for public release, the following are not included:

- exchange API keys, secrets, and environment files
- Telegram / notification credentials
- server deployment details and SSH / infrastructure configs
- live order routing implementation details
- production signal formulas and alpha logic
- tuned production parameter presets
- real account state, private logs, and private datasets

## Repository Layout

```text
binance_trading_system/
  docs/
  futures/
    eth_futures_4_showcase/
    eth_futures_7_showcase/
  spot/
    eth_spot_showcase/
  shared/
```

### Folder Summary

- `docs/`
  Portfolio-level documentation, including redaction policy and public design notes.

- `futures/`
  Futures strategy showcase folders. Each showcase is meant to explain system structure, validation approach, and report shape without exposing production logic.

- `spot/`
  Spot strategy showcase folders. This area is reserved for public-safe spot strategy presentations as they are prepared.

- `shared/`
  Shared concepts and reusable public-facing abstractions such as config patterns, reporting formats, and interface boundaries.

## Current Public Showcase

### `futures/eth_futures_4_showcase`

This showcase represents a lower-frequency ETHUSDT perpetual futures research branch.

Public materials included:
- architecture note
- public-safe config example
- sample report schema
- sample trade log schema
- runner stub for demonstration

## Validation Philosophy

The private system is built around the idea that a strategy is not just a signal formula. A usable trading system needs:

- cost-aware backtesting
- risk controls and position sizing discipline
- regime awareness
- walk-forward or out-of-sample validation
- clean separation between research and execution layers

This repository reflects that engineering approach, even where implementation details are intentionally abstracted.

## Intended Use

This repository is meant to be read as:

- a portfolio project
- an engineering showcase
- a discussion artifact for interviews

It is not intended to be used as a plug-and-play live trading bot.

## Notes

If you are reviewing this repository for interview or collaboration purposes, the best place to start is:

1. `futures/eth_futures_4_showcase/README.md`
2. `futures/eth_futures_4_showcase/docs/architecture.md`
3. `docs/redaction_policy.md`

