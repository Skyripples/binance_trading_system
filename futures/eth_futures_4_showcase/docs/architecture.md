# Architecture

## Design goals
- keep research, backtest, and live execution concerns separated
- make cost assumptions explicit
- keep state and secrets out of source control

## Public module boundaries
1. data ingestion
2. feature engineering
3. regime filter
4. signal generation
5. position sizing / risk control
6. execution abstraction
7. reporting

## Private pieces not published
- final alpha logic
- exchange-specific execution safeguards
- production presets
- infrastructure automation
