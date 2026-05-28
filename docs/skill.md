# Claude skill

`xrayctl` ships a generic Claude skill at
`src/xrayctl/skill/SKILL.md`. Drop it into any project's
`.claude/skills/xrayctl/` directory and the skill will load the project's
`.xrayctl.yaml` to surface notes, paths, and reminders.

## Install

```bash
# project-level
xrayctl skill install --target .claude/skills/

# user-level
xrayctl skill install --target ~/.claude/skills/
```

`--target` defaults to `.claude/skills/xrayctl/`. The command copies
`SKILL.md` (and any future supporting files) into the target directory.

## Authoring `.xrayctl.yaml`

The skill always reads `.xrayctl.yaml` first. See
[`.xrayctl.example.yaml`](.xrayctl.example.yaml) for the full schema.

Recommended pattern: keep `.xrayctl.yaml` **committed** at the repository
root with env-variable names and project-specific notes. Keep the
corresponding env-variable **values** in your shell or in a gitignored
`.envrc`.

## Sharing the skill across teams

Because the skill is generic, the same `SKILL.md` works for every
`.xrayctl.yaml` deployment. Distribute the skill via
`xrayctl skill install` (one command per machine) and let project-specific
context live in each repo's `.xrayctl.yaml`.
