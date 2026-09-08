# K16 S4 sharp-pair cascade: five rehosts are necessary

Date: 2026-07-30  
Scope: the nine sharp hole-provider pairs in the frozen seed-4 `4/9/5`
collar atlas only.

Let

\[
S=0x31ce\subset L=0x7bce.
\]

The exact host-choice frontier previously identified nine compatible pairs
with only three immediately displaced incumbent targets:

\[
\{36,68,69\}\times\{2,3,133\}.
\]

This audit strengthens that frontier.

## Theorem

For every one of the nine pairs, remove its three already-displaced targets
completely, thereby giving their eventual replacement providers maximal
freedom.  Allow every other protected target to choose any of its
incumbent-realized intervals.  In order for the large-hole provider to retain
all bits of `L` not supplied by its fixed OR, at least two additional
protected targets must be rehosted.  The unique minimum additional set is

\[
\{0x31cc,0x33cc\}.
\]

Consequently every completion through one of the nine sharp pairs uses at
least five nonincumbent protected rows.  If exactly five are used, the two
rows beyond the three pair-displaced rows are uniquely `0x31cc` and
`0x33cc`.  This uniqueness is cardinality-qualified: a larger relaxation
can avoid one or both of those two rows.

The apparent equality case is itself impossible.  Relax exactly these five
targets and restrict every other protected target to an incumbent-realized
interval.  Across all valid incumbent base states, at least one relaxed row
has no provider individually compatible with the base:

* for small shape `36`, all 24 valid bases kill
  `{0x33cc,0x73cc,0xb0cc,0xb0ce}`;
* for small shape `68` or `69`, all 36 valid bases kill all five relaxed
  targets `{0x31cc,0x33cc,0x3cc8,0x3ce8,0x73cc}`.

Therefore the exact five-rehost fibre is empty.  Any completion through a
sharp pair must also move at least one further protected target, or abandon
incumbent provenance more globally.

## Proof calculation

Fix a sharp pair and one incumbent interval choice for every protected row.
For a demanded bit `b` of the large provider and a cell `p` in its interval,
let

\[
B_{b,p}=\{T:p\in Q_T,\ b\notin T\}.
\]

The maximal-core theorem says that bit `b` can survive at `p` only if every
row in `B_{b,p}` is rehosted.  Thus the minimum additional relaxation set is

\[
\min_{p_b\in Q_L}\left|\bigcup_b B_{b,p_b}\right|.
\]

There are only six protected targets with multiple incumbent intervals, for
exactly

\[
2\cdot3\cdot3\cdot3\cdot2\cdot2=216
\]

incumbent assignments.  The audit enumerates all 216 assignments for each
of the nine pairs, performs the displayed union minimization exactly, and
obtains minimum two with the same unique minimizer
`{0x31cc,0x33cc}` in every case.  Since the three originally displaced rows
were omitted from the blocker calculation altogether, adding their actual
replacement providers cannot weaken this lower bound.

## Reproducer

Run:

```text
python3 scratch/audit_k16_s4_sharp_pair_five_rehost_floor_20260730.py
```

It writes:

```text
scratch/k16_s4_sharp_pair_five_rehost_floor_20260730.audit.json
```

The input semantic-incidence table is hash-pinned inside the script.  This
result closes only the three-compensator subcase; it does not decide the full
5,692-pair S4 provider CSP.
