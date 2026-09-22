# Executed source snapshot

This directory contains the final source files that were present in the verified
RoboDojo experiments. Files are grouped by their original codebase so that their
repository-relative paths remain explicit.

- `gpt_as_policy/` contains the hybrid rollout, teacher-gate, validation,
  checkpoint, bounded-context, RPC, and evidence-recording implementation used
  by the successful one-layer tower episode.
- `robodojo/` contains the modified `build_tower.py` evaluator used for that
  episode. Its `run_reward()` terminates after the first supported layer is
  complete and both grippers are open.

The source snapshot intentionally excludes temporary `*.before_*` backups,
credentials, model weights, generated workspaces, raw observations, and code
paths not used by the reported hybrid-policy experiments.

The later grasp-recovery pilot used an additional simulator-side perturbation
patch. That final patch source was not included in the retained source archive,
so it is not reconstructed here. The executed action records are retained as
experiment evidence instead.
