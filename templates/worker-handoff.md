# Worker Handoff: <delegated run>

<!-- Filled by the orchestrator for one delegated run; see Executing build tasks in company/workflows/idea-to-release.md. This message references the durable task record rather than replacing it. -->

Task record: <path>
Isolation boundary: <branch, worktree, runner, or other reversible boundary>
Permissions: <read, write, external access, and explicit exclusions>

## Objective
<!-- The single outcome this run must produce. -->

## Orientation
<!-- Name the canonical documents needed to act correctly. Link to procedure rather than copying it here, because copied guidance goes stale. -->

## Allowed scope
<!-- Paths, systems, and actions this run may change or use. -->

## Forbidden scope
<!-- Paths, systems, and actions this run must leave untouched. -->

## Provisional judgments
<!-- State the orchestrator's current reading as hypotheses the worker should challenge with evidence, not conclusions to confirm. -->

## Expected artifacts and completion signal
<!-- The produced artifact is the completion signal; a notification, exit status, or final message is only a hint to inspect it. -->
- Expected artifacts:
- Durable completion signal:

## Checkpoints
<!-- For a long run, name the decision-grade progress to record in files so interruption can resume from durable state. -->

## Verification commands and environment
- Commands:
- Environment and load assumptions:

## Bounds
- Timeout:
- Retry-and-stop rule:
- Escalate rather than continue when:

## Interruption handoff
<!-- Record the exact run, isolated workspace, changed paths, partial artifacts, verification evidence, and next resumable action before cleanup. -->
