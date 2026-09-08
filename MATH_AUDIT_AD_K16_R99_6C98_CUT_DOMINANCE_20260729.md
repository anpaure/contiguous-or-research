# AD audit: dominance of the `6c98` signed and endpoint-cover cuts

Date: 2026-07-29  
Scope: solver-free comparison of two projections of the fixed-delete `6c98`
four-upper-colour obstruction.  No branch infeasibility is claimed.

## 1. Verdict

Both signed forcing-chain clauses in
`MATH_AUDIT_AD_K16_R99_6C98_SIGNED_RAINBOW_CORE_20260729.md` are globally
valid for every binary source-cut vector in the loopless off-source exact
degree-restoration model.  They are not merely valid at `6c98`.

They should nevertheless **not** be installed in addition to the 26-node
four-colour endpoint-cover row.  That single row implies both signed clauses,
and the implication is strict even after imposing `sum x=99`.  The exact
36-new-variable, 41-row `K_9` endpoint-witness block is stronger again; this
second implication is also strict on the radius-99 Boolean cube.

Thus the safe production choices are:

1. for one eager cut, install only the 26-node endpoint-cover row;
2. for the strongest audited local recourse layer, install the exact
   36-variable endpoint-witness block instead;
3. do not duplicate either choice with the two dominated signed rows.

The first choice is one row with 52 net nonzero cut coefficients.  The one
signed clause that rejects `6c98` has 51 nonzeros and is therefore one
coefficient sparser, but it is strictly weaker.  No global minimality claim
is made for the endpoint cover or for the lifted block.

## 2. Exact notation and support identity

Let `x_e=1` mean that source-factor edge `e` is cut.  Write

```text
A=4742, B=22511, C=23229, D=24034,
f=18158, g=21391.
```

The four letters `A,B,C,D` are the unique source providers of upper colours

```text
(1,1883), (1,1907), (1,3255), (1,5939).
```

Let `N0` be the audited 46-edge escape set: all source edges incident with
the 23 outside provider nodes, together with the second source incidences at
nodes 611 and 617.  The two signed rows are

\[
 x_A+x_B+x_C+x_D-\sum_{e\in N_0}x_e-x_f\le3,       \tag{S_f}
\]

\[
 x_A+x_B+x_C+x_D-\sum_{e\in N_0}x_e-x_g\le3.       \tag{S_g}
\]

For the 26-node endpoint cover `P` in the fixed-delete audit, literal
reconstruction gives the exact support identity

\[
 d_x(P)=
 \sum_{e\in N_0}w_e x_e+x_f+x_g+2x_B,              \tag{2.1}
\]

where `w_e=|ends(e) intersect P|` belongs to `{1,2}`.  There are no other
source terms.  The provider-cover row is

\[
 d_x(P)\ge x_A+x_B+x_C+x_D.                         \tag{E}
\]

The endpoint audit verifies all 140 loopless off-source providers of the
four colours and proves that each meets `P`.

## 3. Global validity of the signed rows

### Theorem 3.1

Every binary source cut admitting a loopless off-source exact
degree-restoring completion with the complete upper-q1 palette satisfies
both `(S_f)` and `(S_g)`.

### Proof

It suffices to prove `(S_f)`; interchange `f,g` for the other row.  A
violation is integral.  Since the positive sum is at most four, it forces

```text
x_A=x_B=x_C=x_D=1, all x_e=0 for e in N0, and x_f=0.
```

Equivalently, every one of the four colours is lost, every outside provider
node has cut degree zero, and the extra source incidences at nodes 611 and
617 are retained.  Because `B` itself is cut and has endpoints 611 and 617,
those two nodes each have cut capacity exactly one.  Node 576 has capacity
`x_f+x_g<=1`.

After the zero-capacity outside nodes are removed, every provider of `C`
uses 576 and every provider of `D` uses 611.  Thus `C` exhausts 576 and `D`
exhausts 611.  Every provider of `B` then uses 617.  Finally every provider
of `A` uses 576 or 617, both exhausted.  This contradicts exact degree
restoration.  Hence `(S_f)` is valid.  The same argument proves `(S_g)`.
∎

This proof uses the full `K_9` provider catalogues, the loopless source
2-factor incidences, and the off-source rule.  It does not freeze the other
cut bits and does not use the `6c98` SAT transcript.

## 4. Exact dominance

### Theorem 4.1

On the full binary source-cut cube, `(E)` implies both `(S_f)` and `(S_g)`.
The converse fails even on the hyperplane `sum x=99`.

### Proof

Suppose `(S_f)` fails.  As above, all four positive bits are one, all `N0`
bits are zero, and `x_f=0`.  By (2.1),

\[
 d_x(P)=x_g+2x_B\le3<4=x_A+x_B+x_C+x_D,
\]

so `(E)` fails.  Contraposition proves that `(E)` implies `(S_f)`; the proof
for `(S_g)` is symmetric.

For strictness, cut all four source providers and one coefficient-one edge
of `N0`, namely edge 4228, and extend with 94 source edges outside the union
of the two row supports.  Both signed left sides equal three, whereas `(E)`
has capacity three and demand four.  The replay stores the exact 99-edge
vector, whose sorted-value SHA-256 is

```text
6e5ddf2e715c6d59ea85af43064aede2319bbac31e8c5df2dec3888bcbe532c0.
```

Thus the implication is strict on the radius-99 Boolean cube.  This witness
is not asserted to satisfy the delete-branch motif, portal, or lifted
matching constraints. ∎

## 5. The exact local block is stronger again

For each colour `c`, the audited provider graph is `K_9` and its unique
source edge is one forbidden pair.  Binary variables `u_(c,v)` therefore
give an exact local rainbow-capacity formulation:

\[
 \sum_{v\in V_c}u_{c,v}=2x_{s_c},\qquad
 u_{c,a_c}+u_{c,b_c}\le x_{s_c},                  \tag{5.1}
\]

and

\[
 \sum_{c:v\in V_c}u_{c,v}\le
 \sum_{e\in F:v\in\partial e}x_e.                \tag{5.2}
\]

There are 36 new binary variables, four cardinality equalities, four
forbidden-pair inequalities, and 33 node-capacity inequalities.  This block
is exactly the existence of node-capacity-compatible providers for these
four colours, not a sufficient model for the other q1 rows.

The block implies `(E)`: each chosen provider has at least one endpoint in
`P`, so charging one such endpoint and applying (5.2) yields the endpoint
row.

The implication is strict.  Cut all four source providers and both source
edges at node 485, namely 16183 and 17976, then extend to radius 99 using
only source edges disjoint from all 33 provider nodes.  Row `(E)` is tight:
the cut source edge `B` contributes two units and node 485 contributes two,
for capacity and demand both equal to four.  But lost colour `(1,3255)` has
positive cut degree only at its source endpoints 638 and 754; their joining
provider is the forbidden source edge 23229, so it has no eligible
off-source provider.  The exact block is infeasible.  The sorted cut digest
is

```text
e58deaff5073ac245655688abf8587a481b99da02bf0da9de663f8c7b9deec4c.
```

Again this is a projection strictness witness, not a branch-master
candidate.

## 6. Replay and exact boundary

The solver-free replay is

```text
scratch/audit_ad_k16_r99_6c98_cut_dominance_20260729.py
scratch/ad_k16_r99_6c98_cut_dominance_20260729.audit.json
```

with SHA-256 digests

```text
2c7c29cc6834a8e1a8c50649e808b89b38e2fde359c76b9d54a7fb579712dc36
2ada06ba8de12fe958a5d13a45350f9bb425e6448bbb4d4fa20427668b2bf1d9.
```

It pins both upstream audit files and the catalogue module, reconstructs the
support identity (2.1), checks the 64 nonautomatic aggregate truth cases,
and verifies both radius-99 strictness witnesses literally.

Proved:

1. both signed clauses are global necessary conditions;
2. the single endpoint-cover row strictly dominates their conjunction on
   the radius-99 Boolean cube;
3. the exact four-colour endpoint-witness block strictly dominates that row
   on the same cube.

No joint-cover row is installed or used in this comparison; whether any
stronger part of the existing lifted master independently implies a displayed
row is outside this audit's scope.

Not proved:

1. that either strictness witness belongs to the current branch master;
2. that the endpoint cover, signed clauses, or 36-variable block are support-
   minimal;
3. feasibility or infeasibility of any other radius-99 cut;
4. connectivity, voltage, residence, or deeper-shadow completion.
