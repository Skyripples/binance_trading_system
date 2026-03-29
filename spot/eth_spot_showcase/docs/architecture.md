# Architecture

## Overview

This spot branch is implemented as a stateful inventory process rather than a leveraged directional system.

It keeps a base ETH inventory, manages a price anchor, and reacts to discrete grid movements with spot orders.

## Split Between Research And Execution

### Backtest branch
- reads merged historical spot bars
- computes simplified context features
- simulates startup inventory bootstrap
- simulates grid-based buy and sell actions
- outputs trade logs, equity series, and summary artifacts

### Live branch
- reads runtime config from environment
- loads Binance spot exchange metadata
- checks balances and startup inventory sufficiency
- maintains persistent anchor state across restarts
- executes one buy or sell per newly crossed grid interval
- records trade fills and sends notifications

## State Model

A minimal live state file includes:
- `anchor_price`
- `last_price`
- `last_check_time`
- `eth_balance`
- `quote_balance`
- `action_taken`
- `startup_eth_balance`
- `startup_quote_balance`
- `startup_price`
- `startup_equity_usdt`

## Notification Model

Live notifications are designed around operational visibility:
- boot notification with startup balances and runtime parameters
- startup fill notification if inventory top-up occurs
- grid buy notification with trigger and anchor movement
- grid sell notification with balances, fee, and current USDT profit snapshot
- error notification for startup or loop failures

## Safety Principles

The private implementation enforces safety checks before execution:
- exchange quantity step size
- exchange minimum quantity
- exchange minimum notional
- available quote balance before buys
- available ETH balance before sells
- startup inventory sufficiency before normal loop begins

## Redaction Notes

This public showcase preserves the execution boundaries and system design while intentionally removing production-sensitive order logic, exact strategy formulas, and secret handling details.
