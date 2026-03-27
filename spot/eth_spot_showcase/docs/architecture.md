# Architecture

## Overview

This spot branch is built around a simple operational idea:

- keep a base ETH inventory
- react to discrete price moves with fixed-size spot orders
- persist enough local state to continue running after restarts

## Components

### Backtest layer
- historical data loader
- feature preparation
- strategy simulation
- trade / equity / summary export

### Live layer
- environment loader
- Binance spot client
- exchange filter normalization
- startup inventory bootstrap
- grid execution engine
- state persistence
- trade log writer
- notifier interface

## State Model

A minimal live state file contains:
- current grid anchor
- last observed price
- last check timestamp
- current ETH balance snapshot
- current quote balance snapshot
- whether an action was taken in the latest loop

## Safety Principles

The private implementation enforces safety at the execution boundary by checking:
- minimum notional
- quantity step size
- available quote balance before buy
- available ETH balance before sell
- startup inventory sufficiency before normal loop begins

## Public Redaction Notes

This public showcase preserves the system shape and responsibilities, while removing production-sensitive details such as secret management, exact operational recovery logic, and server-specific commands.
