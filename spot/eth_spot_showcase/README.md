# ETH Spot Showcase

Public portfolio version of the current ETH spot strategy branch.

This showcase is intentionally built around a simple but operationally useful idea: maintain a base ETH inventory, trade around it with fixed grid spacing, and preserve enough state that the strategy can run continuously instead of behaving like a one-shot backtest.

## What This Showcase Represents

The private strategy behind this showcase currently centers on:

- bootstrapping to a target ETH inventory at startup
- fixed USD grid spacing for recurring buy / sell execution
- anchor-based logic so the same price zone is not repeatedly traded without a new level transition
- persistent state for long-running operation
- trade logging and notification payloads designed for live monitoring
- separate live and backtest entry points

This public folder keeps that structure visible while removing sensitive execution details.

## Private-To-Public Mapping

Private project:
- `eth_spot.py`
  Live spot executor
- `eth_spot_backtest.py`
  Backtest and strategy evaluation workflow

Public showcase:
- `src/eth_spot_live_showcase.py`
  Public-safe live execution skeleton
- `src/eth_spot_backtest_showcase.py`
  Public-safe backtest skeleton

## Live Workflow Represented Here

The live branch is modeled as this sequence:

1. load runtime config from environment variables
2. validate exchange connectivity and symbol filters
3. check current inventory and top up to the target ETH amount if needed
4. restore or initialize anchor/state
5. trigger a single buy on a lower grid transition
6. trigger a single sell on an upper grid transition
7. persist updated state
8. append trade records
9. emit Telegram-style operational notifications

## Why This Is Interesting From A Systems Perspective

This strategy is intentionally simpler than the futures research branches, but it highlights a different engineering problem set:

- inventory-aware trading instead of flat/position-flip logic
- startup bootstrap behavior
- durable state for 24/7 execution
- integration between execution, logging, and operator notifications
- clear distinction between research code and production-safe runtime logic

That makes it a useful example for discussing how a small strategy becomes a maintainable system.

## Public Examples Included

- public environment schema
- sample backtest summary
- sample live state file
- sample trade log schema
- public-safe live and backtest runner stubs

## What Is Intentionally Redacted

This public repository does not include:

- exchange API keys or secrets
- real Telegram credentials
- production Binance order-routing details
- exact live signal thresholds or tuned private presets
- private infrastructure/deployment configuration
- real account logs or execution journals

## Portfolio Use

This folder is intended for:

- interview review
- architecture discussion
- portfolio reading

It is not a plug-and-play live trading bot.
