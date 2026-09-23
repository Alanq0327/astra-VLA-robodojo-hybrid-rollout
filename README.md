# Astra-Gated VLA Hybrid Rollout in RoboDojo

This repository contains the implementation, configurations, and experimental results of an Astra-gated vision-language-action system in the RoboDojo dual-arm simulator.

The system uses a pretrained $\pi_{0.5}$ policy to generate robot actions. Astra acts as a high-level teacher gate. It reviews task progress, proposal intent, and execution evidence at discrete decision points. The approved action prefix is then executed before the system requests a new observation.

The closed-loop process is:

**Observation → $\pi_{0.5}$ proposal → Astra assessment → bounded execution → new observation**

## Repository Structure

| Folder                 | Contents                                                                                                                                                                                                         |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`src/`](src/)         | Core implementation of the hybrid rollout system. It includes the Astra teacher gate, RoboDojo communication layer, proposal validation, checkpoint handling, decision logging, and the modified task evaluator. |
| [`configs/`](configs/) | Configuration files used for the full-episode experiment and the controlled grasp-recovery experiment.                                                                                                           |
| [`Results/`](Results/) | Experimental records, structured result files, logs, and videos. See [`Results/README.md`](Results/README.md) for details.                                                                                       |

## Experimental Results

### Full Episode

The system completed the one-layer tower-building task in 240 control steps. The simulator reported native task success with a score of `1.0`. The run contained 18 student proposals and Astra decisions. It ended normally without truncation or rollback.

The corresponding records are stored in:

* [`Results/Full_episode_results/`](Results/Full_episode_results/)
* [`Results/Video/`](Results/Video/)

### Controlled Grasp Recovery

A separate short experiment tested recovery after a controlled grasp failure. The left-gripper action channel was externally forced open during action indices 15–44. The failed acquisition was identified at step 45. After the perturbation ended, the student policy generated a new grasp attempt. The object was held at step 68, and continued retention was verified at step 73.

The corresponding records are stored in:

* [`Results/small_grasp_recovery_test_results/`](Results/small_grasp_recovery_test_results/)
* [`Results/Video/`](Results/Video/)

The short-recovery video covers only a brief motion sequence, so the failure and recovery may not be visually obvious during normal playback. The structured action records, decision files, and recorded observations provide the main evidence for this experiment.

## Scope

This repository documents one successful full episode and one controlled short-recovery experiment. The included files support inspection of the system implementation, experimental settings, execution process, and reported results. They do not represent a multi-seed benchmark or a statistical evaluation.
