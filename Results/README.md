# Results

This directory contains the recorded outputs and videos from two RoboDojo experiments:

1. a complete one-layer tower-building episode; and
2. a controlled short grasp-recovery test.

## Directory Structure

| Directory                                                                    | Contents                                                                            |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [`Full_episode_results/`](./Full_episode_results/)                           | Structured results from the complete one-layer tower-building episode               |
| [`small_grasp_recovery_test_results/`](./small_grasp_recovery_test_results/) | Actions, decisions, checkpoints, and result files from the controlled recovery test |
| [`Video/`](./Video/)                                                         | Videos of both the complete episode and the short recovery test                     |

## Full Episode

The full episode completed the one-layer `build_tower` task.

Key results:

* Native success: `true`
* Native score: `1.0`
* Control steps: `240`
* Student-policy predictions: `18`
* Astra decisions: `18`
* Edited steps: `0`
* Recovery steps: `0`
* Truncated: `false`
* Rollback: none

The π0.5 student policy generated the robot actions. Astra monitored task progress, checked the proposed action intent, and selected bounded execution prefixes. Astra judged all 18 proposals as aligned, so it did not apply an unnecessary action edit.

The complete episode video is available in [`Video/`](./Video/).

## Controlled Short Recovery

The short recovery test introduced an external fault into the left-gripper action channel.

Perturbation settings:

* Target: left gripper
* Action channel: `6`
* Affected action indices: `15–44`
* Number of affected actions: `30`
* Forced value: `1.0`
* Attribution: `external_gripper_fault_not_teacher_edit`

The main recovery sequence was:

| Step    | Observed event                                                                |
| ------- | ----------------------------------------------------------------------------- |
| `15–44` | The external gripper perturbation was active                                  |
| `45`    | The post-perturbation observation showed a failed acquisition                 |
| `68`    | The π0.5 policy re-acquired and held the object                               |
| `73`    | A later observation confirmed continued retention, and Astra stopped the test |

The external perturbation caused the failure. The π0.5 student policy generated the recovery motion after the perturbation ended. Astra detected the failed acquisition, monitored the retry, checked the later retention evidence, and stopped the test after it confirmed recovery.

## Video Note

The [`Video/`](./Video/) directory contains both the complete episode video and the short recovery video.

The short recovery test ends soon after recovery is confirmed. Its visual change may therefore be difficult to identify during normal-speed playback. The video should be treated as supplementary qualitative evidence.

The structured action records, teacher decisions, perturbation trace, and step-indexed results in [`small_grasp_recovery_test_results/`](./small_grasp_recovery_test_results/) provide the main evidence for the recovery sequence. In particular, steps 45, 68, and 73 mark the failed acquisition, renewed grasp, and confirmed retention.

## Scope

These results document one verified full episode and one controlled recovery test. They demonstrate end-to-end execution, correct Astra abstention during an aligned trajectory, and recovery verification under one controlled gripper fault. They do not represent a multi-trial success-rate benchmark.

