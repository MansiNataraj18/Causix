# Causix

Root-cause analysis, impact analysis and fix recommendation for code issues, built from small
single-purpose agents on a shared core. This repository is the entry point: each component lives in
its own repository and is linked here as a git submodule.

| Repository | Purpose |
|---|---|
| [causix-core](https://github.com/MansiNataraj18/causix-core) | Shared engines (parser, graph, RCA, impact, validation) and reasoning contracts |
| [causix-issue-agent](https://github.com/MansiNataraj18/causix-issue-agent) | Turns a raw report into a structured issue |
| [causix-rca-agent](https://github.com/MansiNataraj18/causix-rca-agent) | Grounded root cause analysis |
| [causix-impact-agent](https://github.com/MansiNataraj18/causix-impact-agent) | Explains the blast radius of a change |
| [causix-fix-agent](https://github.com/MansiNataraj18/causix-fix-agent) | Recommends a fix and a regression test |
| [causix-scenario-agent](https://github.com/MansiNataraj18/causix-scenario-agent) | Generates a validation scenario for a fix |
| [causix-documentation-agent](https://github.com/MansiNataraj18/causix-documentation-agent) | Writes the documentation and lessons report |
| [causix-orchestrator](https://github.com/MansiNataraj18/causix-orchestrator) | Chains the agents; FastAPI service and Aetherion entrypoint |

Dependency direction: `orchestrator -> agents -> core`. Agents never depend on each other.

## Getting started

```bash
git clone --recurse-submodules https://github.com/MansiNataraj18/Causix.git
# already cloned?  git submodule update --init --recursive
```

Each repository is developed and tested on its own (`uv sync && uv run pytest`). The agents and the
orchestrator install `causix-core` from its GitHub URL, so you need read access to these repos.

To pull the latest of every component: `git submodule update --remote`.
