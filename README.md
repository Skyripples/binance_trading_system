# Binance Trading System

Public portfolio version of a larger private Binance trading research system.

This repository is meant for technical review, interviews, and engineering discussion. It focuses on how the system is structured, validated, and operated without exposing live credentials, production alpha, or deployment-sensitive details.

## What This Repository Shows

- strategy-oriented project structure
- separation between backtest, paper/testnet, and live execution concerns
- reusable boundaries for config, state, reporting, and notifications
- cost-aware trading system design
- public-safe examples of research artifacts and execution interfaces

## What Is Deliberately Not Public

To keep the portfolio safe, this repository excludes:

- API keys, secrets, and `.env` files
- Telegram credentials and operational bot settings
- server infrastructure, SSH, and deployment details
- private execution adapters and live order routing internals
- production signal formulas and tuned parameter sets
- private logs, account state, and proprietary datasets

## Repository Layout

```text
binance_trading_system/
  docs/
  futures/
    eth_futures_4_showcase/
  spot/
    eth_spot_showcase/
  shared/
```

## Showcase Overview

### Futures

`futures/eth_futures_4_showcase`

A lower-frequency ETHUSDT perpetual futures branch focused on:
- strategy architecture
- validation/reporting shape
- public-safe config and runner structure

### Spot

`spot/eth_spot_showcase`

An ETH spot inventory strategy branch focused on:
- startup inventory bootstrap
- anchor-based fixed-grid execution
- state persistence for long-running operation
- notification and trade-log design
- clear separation between backtest and live code paths

## Engineering Principles Behind The Private System

The private system is built around the idea that a strategy is more than an entry condition. A usable trading system also needs:

- realistic cost assumptions
- position sizing and capital discipline
- durable state management
- reporting that supports review and debugging
- execution boundaries that reduce accidental live risk

This public repository keeps those engineering principles visible even where exact implementation details are abstracted.

## Best Starting Points

If you are reviewing this repository, start here:

1. `futures/eth_futures_4_showcase/README.md`
2. `spot/eth_spot_showcase/README.md`
3. `docs/redaction_policy.md`

## Intended Audience

This repository is intended to be read as:

- a portfolio project
- a systems-design discussion artifact
- a trading-infrastructure engineering showcase

It is not intended to be used as a plug-and-play live trading bot.
