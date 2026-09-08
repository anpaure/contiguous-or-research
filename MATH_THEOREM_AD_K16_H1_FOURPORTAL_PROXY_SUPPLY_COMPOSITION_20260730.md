# K16 H1 four-portal proxy/supply composition theorem

Date: 2026-07-30  
Lane: AD  
Status: **exact frozen-support composition; UNSOLVED/UNKNOWN**

## 1. Two independently audited parents

This note composes, without invoking a solver, the following two exact
certificates.

### Parent A: normalized supply/code model

```text
scratch/ad_k16_h1_fourportal_joint13_supplycode_20260730/model.map.json
SHA-256 2c89b0f77e830139a7cb2027a1f76a6e2698efef88b1ee9b3b50fdb1606825f2

scratch/ad_k16_h1_fourportal_joint13_supplycode_20260730/model.independent_audit.json
SHA-256 d7e7b917bababca25dc5de5d100c01f3cbfdd593d0cc8c6751d5520507aa316b
```

It has 469 variables, retains 1,579 of the 1,595 local charts after 16 exact
common-core contractions, and uses existential supply flags on 194 live
cell-coordinate pairs.

### Parent B: target-OR proxy closure

```text
scratch/ad_k16_h1_joint13_proxyclosure_reduced_20260730/model.audit.json
SHA-256 e7e24b3cac5fb1820f4da3b6bd7f098f1459063ca4b1ca421f20d2b9ddbe1617

scratch/ad_k16_h1_joint13_proxyclosure_reduced_20260730/model.independent_audit.json
SHA-256 d8c7d189daf2bd705c07873f40cd0c197e3a674f3159842d0c732b17f7e145f8
```

It independently reconstructs the 216-state target-intersection closure and
replaces the 10,301 original durable coordinate rows by 5,465 singleton proxy
rows.  Its exhaustive positive-clause audit covers 445 distinct
\((T,w,N)\) scenarios and 2,336 prime candidates; no nonsingleton positive
clause beats the certified singleton generators.

Both parents pin the same occupancy map

```text
scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.map.json
SHA-256 f624e5684fe58c122d43371c16fbd4e1c8db9b9ae8a84930d3b9cf59a4758f31.
```

## 2. Proxy equivalence on canonical OR states

Let \(R\) be the 55 residual targets and let

\[
 \mathcal C=\left\{\bigcap\mathcal F:\mathcal F\subseteq R\right\},
                                                                    \tag{2.1}
\]

where the empty intersection is \(\mathtt{0xffff}\).  The audited closure has
exactly 216 states.  Fix a local chart

\[
                     \alpha=(T,I,N),\qquad w=|I|.
\]

Because the selected \(T\)-interval crosses every cell of \(I\), each
canonical cell value on that interval has the form

\[
                         T\cap C,qquad C\in\mathcal C.             \tag{2.2}
\]

Let \(\mathcal O_{T,w}\) be the set of ORs of \(w\) independently selected
states of the form (2.2).  This may contain unattainable independent-cell
combinations, so it is a safe superset of the actual canonical OR states.

The frozen proxy generator \(G_\alpha\subseteq[16]\setminus\{6\}\)
satisfies the exact two-sided identity

\[
 G_\alpha\subseteq V
       \quad\Longleftrightarrow\quad
 N\subseteq V
       \qquad(V\in\mathcal O_{T,w}).                              \tag{2.3}
\]

Indeed, every good state \(V\supseteq N\) contains every eligible proxy bit,
and the certified generator hits the missing-coordinate set of every bad
state.  Parent B proves (2.3) independently for all 445 scenarios and proves
the displayed generators minimum among all chartwise positive-clause
deletions in this closure model.

The sixteen charts deleted by Parent A have no tracked need and no proxy
generator.  Hence their deletion leaves the proxy-row census exactly 5,465.
The composed independent audit rechecks (2.3) directly on all 429 scenarios
which remain after those deletions.

## 3. Exact composition theorem

For a selected chart \(\alpha=(T,I,N)\), impose

\[
 \bigvee_{p\in I}X_{p,q}=1\qquad(q\in G_\alpha),                  \tag{3.1}
\]

and retain the Parent-A omitter rows

\[
 X_{p,q}=0\qquad(p\in I,\ q\notin T).                            \tag{3.2}
\]

Bit 6 remains implicit.

### Theorem 3.1 (proxy/supply composition)

Replacing all 10,301 original need-supply rows of Parent A by the 5,465 rows
(3.1), while retaining its code-validity and omitter rows, is equisatisfiable
with arbitrary nonzero substitutions on the frozen joint13 support.

#### Proof: physical word to composed formula

Take a supported universal word, choose one residual witness per target, and
perform the exact 16-chart normalization from Parent A.  Canonicalize each
editable cell to the intersection of the selected targets crossing it.  The
canonical OR of every chosen chart contains its full need \(N\); by the
forward direction of (2.3), it contains every proxy bit in \(G_\alpha\).
Set \(X_{p,q}=1\) whenever the canonical cell at \(p\) contains \(q\).
Then (3.1) holds.  Every target crossing \(p\) contains every asserted
coordinate, so (3.2) holds as well.

#### Proof: composed formula to physical word

Given a satisfying assignment, decode one retained chart per target and set
each editable cell to the intersection of the targets whose chosen intervals
cross it.  If \(X_{p,q}=1\), all selected targets crossing \(p\) contain
\(q\), by (3.2).  Therefore the canonical cell at \(p\) contains \(q\).
Equation (3.1) consequently puts every proxy bit of \(G_\alpha\) into the
canonical OR of the selected chart.  This OR belongs to
\(\mathcal O_{T,w}\), so the reverse direction of (2.3) supplies the full
original need \(N\).  Adjoining the chart's fixed base gives literal OR
exactly \(T\).  Every nonresidual target retains a fixed-only witness.
Thus the decoded word is universal. \(\square\)

No reverse supply row is needed.  The proof uses only the implication

\[
 X_{p,q}=1\Longrightarrow q\text{ belongs to the canonical cell at }p,
                                                                    \tag{3.3}
\]

which follows from the omitter rows.  Supply flags may be false even when a
canonical coordinate is present.  Conversely, a physical solution can choose
the full canonical membership assignment.

## 4. Exact composed CNF census

The 275 chart-code bits and 194 supply bits are unchanged:

| variable family | count |
|---|---:|
| five chart-code bits for each of 55 targets | 275 |
| live existential supply bits | 194 |
| **total** | **469** |

The exact clause and literal ledger is

| family | clauses | literals |
|---|---:|---:|
| invalid chart codes | 181 | 905 |
| selected proxy generators | 5,465 | 38,235 |
| selected omitters block supply | 22,587 | 135,522 |
| **total** | **28,233** | **174,662** |

Relative to Parent A, the composition removes 4,836 clauses and 32,061
literals.  The sole supply pair `(flat=2, bit=8)` remains fixed false; no
proxy generator uses it.

## 5. Frozen composed artifacts

```text
scratch/build_ad_k16_h1_fourportal_joint13_proxy_supplycode_cnf_20260730.py
SHA-256 c1476781fd1fac7ef3b5960720a6bab3a47693ec5d5f6237fdee3c6201bc090a

scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.cnf
SHA-256 f03c8c3e38caf4d4f47bb7ae4569e07526afdd7689acc2c1b32b8dfd71ab488e

scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.map.json
SHA-256 f5f50ec0563adb1175500ef1426144f753dd72ed37f360f787ebb840feeb5ed8
payload SHA-256 7ff2f7a17a45b40360b7e29a004365b7f7031b169188cb58e85ddf2d1e6c8698

scratch/decode_verify_ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730.py
SHA-256 cbb9e235d8e71b144caf3e69f659f40f3f3651b107366f652a342d35ef88ffe4

scratch/audit_ad_k16_h1_fourportal_joint13_proxy_supplycode_independent_20260730.py
SHA-256 3fb075e588405b8bf3d6a28f602c6b382400503548a7c17aef799ba8b1069ea1

scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.independent_audit.json
SHA-256 331f1d7d56c18c6c639c8abf27b9e177c692a012b9a20e6878b4397efb025c76
payload SHA-256 72be9126c4233d3d18c3008a2751774c52db46410c9ba2aa599d2a6658b774f1
```

The independent auditor does not import or execute the composed builder.  It
reconstructs all 28,233 clauses in exact order, independently recomputes the
216-state closure, rechecks the two-sided proxy identity on the 429 retained
scenarios, and confirms that every deleted chart has empty original and proxy
need.  A separate deterministic rebuild was byte-identical.  The decoder was
tested fail-closed on an empty assignment and produced no output artifacts.

## 6. Scope boundary

This composition is WLOG only inside the frozen thirteen-cell support and
with no edit-cardinality budget.  It does not force any portal to one of the
153 one-cell minimum-debt values, does not move an unrestricted solution into
the support, and does not prove that the composed CNF is satisfiable or
unsatisfiable.  No solver or H100 job was launched.  The exact status remains
**UNSOLVED/UNKNOWN**, and the global bracket remains

\[
                         12873\le\nu(16)\le12874.
\]
