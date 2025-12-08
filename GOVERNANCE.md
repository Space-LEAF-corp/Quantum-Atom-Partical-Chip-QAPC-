# Governance

Role: Steward (Leif) holds final authority.
Process:
- Read-only by default; issues allowed for questions
- No PRs that change canonical files unless invited
- All tags signed; all releases include manifest hashes


---

.github/workflows/verify.yml (immutability + sigstore)

name: verify
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
jobs:
  integrity:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Verify canonical files unchanged
        run: |
          set -e
          for f in README.md LICENSE.md NON-WEAPONIZATION-RIDER.md SECURITY.md GOVERNANCE.md src/qatom_core.py tests/test_invariants.py; do
            if git diff --name-only HEAD~1 HEAD | grep -q "^$f$"; then
              echo "Change detected in canonical file: $f"
              echo "Blocked by governance."
              exit 1
            fi
          done
      - name: Compute manifest hashes
        run: |
          python - <<'PY'
          import hashlib, json, os
          files = [
            "README.md","LICENSE.md","NON-WEAPONIZATION-RIDER.md",
            "SECURITY.md","GOVERNANCE.md","src/qatom_core.py","tests/test_invariants.py"
          ]
          res={}
          for f in files:
            with open(f,"rb") as fh:
              res[f]=hashlib.sha256(fh.read()).hexdigest()
          print(json.dumps(res, indent=2))
          PY
      - name: Sigstore sign tag (dry-run)
        run: echo "Use signed tags/releases per GOVERNANCE.md"


---
