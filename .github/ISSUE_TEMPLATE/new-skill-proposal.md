---
name: New skill proposal
about: Propose a new skill
title: "[skill] <name>"
labels: proposal
---

**Name**
Lowercase, hyphens, same as the folder.

**User-invoked or model-invoked?**
User-invoked skills are commands the user runs. Model-invoked skills are applied by the agent inside those commands.

**What gap does it fill?**
What plain models or the current skills get wrong today.

**Why not extend an existing skill?**
Fewer skills trigger more cleanly. Say why this needs its own.

**Description (draft)**
User-invoked: must say "Use only when the user runs /<name> or explicitly asks to ...".
Model-invoked: name the concrete situations, tied to the flow, so it does not clash with built-in data skills.

**Inputs, outputs, and the skills it calls**

**Three eval cases**
Two with a planted flaw or ambiguity, one clean. One line each. Invented data from the neutral domain only.
