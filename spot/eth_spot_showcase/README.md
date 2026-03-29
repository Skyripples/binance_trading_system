# ETH Spot Showcase

Public portfolio version of the current ETH spot strategy branch.

This showcase mirrors the private project structure more closely and now exposes two public-safe files:
- `src/eth_spot_live_showcase.py`
- `src/eth_spot_backtest_showcase.py`

## Public Strategy Summary

Core behavior represented in this public version:
- startup inventory bootstrap to a target ETH base position
- fixed USD grid spacing for recurring buy / sell execution
- persistent anchor-based state for long-running spot execution
- trade log output for operational review
- Telegram-style notification payload design
- separation between backtest research and live execution code paths

## What Is Intentionally Redacted

The following are intentionally excluded from the public repository:
- exchange API keys and secrets
- real Telegram credentials
- production Binance order routing details
- exact private trading rules and tuned strategy thresholds
- private server deployment specifics
- real account logs and real execution journals

## Repository Mapping

Private project split:
- `eth_spot_backtest.py`: research and backtest workflow
- `eth_spot.py`: live spot executor

Public showcase split:
- `src/eth_spot_backtest_showcase.py`: public-safe backtest skeleton
- `src/eth_spot_live_showcase.py`: public-safe live execution skeleton

## Current Live Behavior Represented

The live branch currently follows this high-level flow:
1. load env-driven runtime config
2. verify exchange connectivity and symbol filters
3. top up startup inventory to a target ETH amount if needed
4. restore or initialize grid anchor state
5. buy once per lower grid break
6. sell once per upper grid break
7. persist state and append trade records
8. emit notifications for boot, startup buy, grid buys, grid sells, and errors

## Notification Fields Represented

The public showcase reflects the notification shape used in the private project:
- startup USDT / ETH balances
- current USDT / ETH balances
- fee summary
- current profit in USDT on sell-side notifications
- anchor transition and trigger price context

## Portfolio Use

This folder is intended for interview discussion and engineering review. It is not a plug-and-play live trading bot.
