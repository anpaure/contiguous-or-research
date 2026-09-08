# Independent audit: movable bottoms, gammoid carry, and layer freezing

**Date:** 2026-08-02  
**Verdict:** **PASS with scope clarification.**  The movable-bottom lemma is
an exact integral payload theorem.  Its equal-cardinality statement must be
replaced by the rectangular form for a chronology block against \(W\)
suffixes.  Exact layer-by-layer freezing is possible when the full
exposed-minimum or propagated matroid state is retained; scalar reserve and
local Hall alone do not choose a future-viable carry.

Audited files:

- `MATH_THEOREM_K17_BOTTOM_TOKEN_PERFECT_MATCHING_AND_COMPOUND_RELAY_CIRCUITS_20260802.md`, especially Section 5;
- `MATH_THEOREM_MOVABLE_FRONTIER_GAMMOID_CARRY_AND_TWO_LAYER_FUSION_20260802.md`;
- `scratch/audit_movable_frontier_gammoid_carry_20260802.py`.

## 1. Section 5 audit

In the cited theorem there are \(n\) real bottoms, \(f\) mandatory free
receivers, \(n\) optional hard slots, and \(f\) dummies.  Both augmented
shores therefore have size \(n+f\).  A left subset \(X\) of real bottoms
with no dummy gives

\[
                         |N_F(X)|+|N_H(X)|\ge|X|.                \tag{1.1}
\]

If the subset also contains \(t>0\) dummies, its neighbourhood contains all
\(n\) hard slots and \(N_F(X)\).  The strongest choice is \(t=f\), giving

\[
                         |N_F(X)|\ge |X|-(n-f).                 \tag{1.2}
\]

These exhaust augmented Hall.  The materialization and converse maps use
each bottom and receiver once, and dummy labels are the only ambiguity.
The bipartite degree polytope and its placement projection are integral.

The statement relies on four payload hypotheses which should accompany any
export:

1. the frozen suffix rows and free maxima already use pairwise disjoint
   named targets and are strict;
2. they are disjoint from the movable bottoms;
3. receiver labels and capacity one are fixed; and
4. every compatibility menu is a fixed edge predicate depending only on
   the first suffix target or free maximum.

State/history or choice-dependent menus are not covered.  Also, the literal
Section 5 cardinalities have \(|H|=|B|=n\); they are not the natural
\(|H|=W\), \(|B|=|P_t|\) chronology parameters.

## 2. Rectangular generalization

With \(b\) real bottoms, \(f\) mandatory receivers, and \(h\) optional
slots, the correct dummy count is

\[
                              d=f+h-b.                            \tag{2.1}
\]

The physical range is \(f\le b\le f+h\).  Dummies see every optional slot
and no mandatory receiver.  The same Hall calculation gives exactly

\[
\boxed{
\begin{aligned}
 |N_F(X)|+|N_H(X)|&\ge|X|,\\
 |N_F(X)|&\ge|X|-(b-f)
\end{aligned}}\qquad(X\subseteq B).                             \tag{2.2}
\]

The second line follows from
\(h+|N_F(X)|\ge|X|+d\).  Conversely the two rows cover every left subset,
so there is no omitted mixed-dummy cut.

For an ordinary chronology block, \(f=0,h=W,b=|P_t|\).  The second row is
automatic and (2.2) is ordinary Hall into the \(W\) exposed suffix minima.
The audit script exhausts 1,820 small arbitrary compatibility graphs and
finds perfect matching exactly when (2.2) holds.

## 3. Carry matroid and Markov recursion

For a fixed exposed receiver set \(S\), let \(M_t\) be the transversal
matroid on \(S\) induced by current-block neighbourhoods.  A saturating
placement uses a base \(I\) of \(M_t\); its unmatched carry is

\[
                              D=S\setminus I.
\]

Hence the possible carries are exactly the bases of \(M_t^*\).  With a
mandatory receiver set \(F\), they are the bases of \((M_t/F)^*\).  The
dual of a transversal matroid is a strict gammoid, so this terminology is
exact and not an analogy.

Processing chronology blocks from late to early gives

\[
 S_q=O,\qquad
 P_t\hookrightarrow S_{t+1},\qquad
 S_t=P_t\mathbin{\dot\cup}
       (S_{t+1}\setminus\operatorname {image}P_t).              \tag{3.1}
\]

Every anchored chain factor restricts to this recursion.  Conversely the
injections in (3.1) concatenate to disjoint owner chains.  Once a matching
is selected, future lower targets see only \(S_t\), not the physical owner
row to which a member of \(P_t\) was attached.  Thus actual suffix rows may
be frozen at the pure static level.

This does not make a greedy matching safe.  The state variable is the named
carry base, not just its size.

## 4. Aggregate suffix alternatives and exact expansion

Let \(G\) be a saturable later-suffix successor graph, with left shore
\(L\), right receiver ground \(E\), and \(|E|-|L|=W\).  Let \(T\) be the
transversal matroid on \(E\) induced by \(L\).  A saturating suffix matching
uses a base of \(T\), so its unmatched exposed-minimum set is a base of

\[
                              C=T^*.                              \tag{4.1}
\]

Let \(K\) be the receiver transversal matroid induced on \(E\) by the next
block \(P\), with full rank \(|P|\).  Some feasible suffix exposure can
receive all of \(P\) exactly when a \(C\)-base spans \(K\).  This is
equivalent to a common independent set of size \(|P|\):

- a spanning \(C\)-base contains a \(K\)-basis;
- a common \(K\)-basis extends to a \(C\)-base.

Matroid intersection therefore gives the exact test

\[
 r_C(X)+r_K(E\setminus X)\ge|P|\qquad(X\subseteq E).           \tag{4.2}
\]

After expansion, the larger successor graph again has a dual-transversal
rank-\(W\) carry matroid.  Induction from the owner set proves that the
recurrence is integral at every depth.  This is the primal counterpart of
global chronological-upset Hall, not a stronger existence theorem.

## 5. Whole-prefix-preserving freeze

The strongest useful fixed-suffix formulation protects all still earlier
blocks at once.  Let \(M_B\) be the current receiver transversal matroid on
mandatory \(F\) and optional \(H\), and put

\[
                              L=M_B/F.                            \tag{5.1}
\]

Occupied optional sets are the bases \(J\) of \(L\), and the carry is
\(D=H\setminus J\).

Let \(Q_A\) be the successor transversal matroid of the whole earlier
prefix on internal right copies \(A^+\), the always exposed current targets
\(\widehat B\), and external optional receivers \(H\).  Assuming the full
ground can saturate the earlier prefix, put

\[
                       K=Q_A/(A^+\cup\widehat B).                 \tag{5.2}
\]

The contraction identity shows that the earlier prefix is completable with
carry \(D\) exactly when \(D\) spans \(K\).  By matroid duality this is
equivalent to \(J=H\setminus D\) being independent in \(K^*\).  Therefore
a current placement can be frozen without destroying any earlier completion
if and only if

\[
 r_L(X)+r_{K^*}(H\setminus X)\ge r(L)
                     \qquad(X\subseteq H).                       \tag{5.3}
\]

This is a genuine exact fusion theorem.  Its rank oracle already contains
the complete earlier chronological matching problem, so it is not a
bounded-state proof of the all-\(k\) asymptotic claim.

## 6. Greedy carry counterexample

On \([5]\), take

\[
 b_1=\{1,2\},\quad b_2=\{1,3\},\quad r=\{1,2,3\},
\]

and optional minima

\[
 m_1=\{1,2,4\},\qquad m_2=\{1,3,5\}.
\]

The legal real edges are

\[
 b_1r,\ b_1m_1,\ b_2r,\ b_2m_2.
\]

With one dummy, there are exactly two first-step perfect matchings.  One
carries \(m_1\), the other carries \(m_2\).  The next target \(\{5\}\) is
contained in none of \(b_1,b_2,m_1\), but is contained in \(m_2\).  Thus
only the second matching is future viable.

The carry matroid has bases \(\{m_1\},\{m_2\}\), while the future
contraction has rank one with \(m_2\) as its only nonloop.  Formula (4.2)
or (5.3) selects the good carry.  Local Hall, carry cardinality, and
same-rank capacity cannot do so.

## 7. Two-layer audit and semantic boundary

The direct two-movable-layer construction is also a square bipartite
matching.  For lower size \(b\), upper size \(m\), and \(s\) fixed suffix
slots with \(\max(b,m)\le s\le b+m\), its exact Hall families are

\[
\begin{aligned}
 |N_M(X)|+|N_S(X,Y)|&\ge |X|+|Y|,\\
 |N_S(X,Y)|&\ge |X|+|Y|+s-b-m
\end{aligned}                                                \tag{7.1}
\]

for \(X\subseteq B,Y\subseteq M\).  The audit script checks 13,081 exact
small incidence systems with no mismatch.  Hence two movable levels are not
the first nonintegral payload gate.

More generally, every **fixed chronology** already has an integral global
bipartite successor-matching polytope.  “Genuinely nonintegral multi-level
chronological-upset gate” can only mean joint chronology/configuration
selection, an insufficient compressed projection, or extra literal
state/history/upper/topology rows.  It is false if applied to the fixed-
chronology static payload itself.

The remaining all-\(k\) task is to choose \(d+C\) blocks for which the
propagated carry matroid retains full rank, or equivalently to prove all
balanced interval profiles.  No bounded representation of that rank
history is proved here.

## 8. Replay

Run

```text
python3 scratch/audit_movable_frontier_gammoid_carry_20260802.py
```

The replay exhausts the rectangular Hall theorem on 1,820 small graphs,
the two-layer Hall theorem on 13,081 exact/sampled small graphs, and the
two-carry warning.  Compilation and replay pass.

## 9. Independent B5 actuator/carry audit

The composition theorem in
`MATH_THEOREM_MODE_TRANSPARENT_B5_ACTUATORS_PRESERVE_GAMMOID_CARRY_20260802.md`
was checked at the occurrence-labelled graph level.

First, prescribing a local alternating circuit removes equal sets
`B_0,R_0` from the two shores.  The residual dummy count is unchanged:

\[
 (|F|-|R_0\cap F|)+(|H|-|R_0\cap H|)-(|B|-|B_0|)
   =|F|+|H|-|B|.                                    \tag{9.1}
\]

Both circuit modes leave the same residual graph, so the two rectangular
Hall families are simultaneously necessary and sufficient for extending
either mode.  This is an exact payload planting theorem, not a relaxation.

Second, if the current occupied set is fixed, the full earlier-prefix
decision can still change.  On `H={h}`, with one always exposed current
copy `b` and one earlier target `a`, take the same current
`L=U_{1,1}` in both modes.  If `Q_A^0` has edges `ab,ah` and `Q_A^1` only
has `ah`, then

\[
                       r(Q_A^0/b)=0,
                       \qquad r(Q_A^1/b)=1.          \tag{9.2}
\]

The empty carry completes the first mode through `b` and fails in the
second.  Hence four-row palettes, occupied slots, and carry cardinality do
not protect the contracted prefix matroid.  Pointwise equality of

\[
 r_{Q_A^\epsilon}(A^+\cup\widehat B\cup X)
 -r_{Q_A^\epsilon}(A^+\cup\widehat B),
 qquad X\subseteq H,                               \tag{9.3}
\]

is exactly equality of the two `K` rank functions.  Equality of each
exported receiver column is a sufficient occurrence-level test.

Third, the local `B_5` constructions were checked against their displayed
atoms, not merely against their palette summaries.

* The saturated `C10` is one 5-cycle between the same five bottoms and
  five fixed suffix slots.
* The one-socket opener `C6` is one 3-cycle with the displayed head and
  upper target fixed occurrencewise.
* The first three-socket fusion `C6` does **not** fix the displayed
  head--upper pairs.  It fixes the tail--upper pairs
  \[
   (\alpha\gamma,\alpha\gamma\delta),\quad
   (\beta\gamma,\beta\gamma\delta),\quad
   (\alpha\beta,\alpha\beta\delta).                \tag{9.4}
  \]
  Thus it is transparent on an untyped payload face which may choose that
  tail shore, but not automatically on a directed fixed-head carry face.
* The fresh-coordinate three-socket opening `C6` again fixes its displayed
  head--upper slots.

Therefore the suite is unconditionally carry-transparent only on the
undecorated containment face.  A slot-inherited protected signature must
be constant on each induced 5- or 3-cycle, or satisfy the equivalent
bottomwise receiver-column identity.

Finally, the opening sidecar does not admit same-base reuse as the next
target while the preceding main path is frozen.
Writing

\[
 F(x,y)=(S+x,S+a+x+y;S+a+x\longrightarrow S+x+y),              \tag{9.5}
\]

one opener changes

\[
 \{F(q,b),F(b,c),F(c,q)\}
 \longrightarrow\{F(b,q),F(c,b),F(q,c)\}.          \tag{9.6}
\]

The private edge is `F(c,b)`.  With the same base, making it the next target
forces the next new phase to contain `F(b,c)`, which duplicates the lower
`S+b` and tail `S+a+b` already used by the retained main edge `F(b,q)`.
That same-base target relay is therefore impossible.  The calculation does
not exclude a changed-core representation or using the edge as a later
exterior atom.  A bounded-sidecar proof still needs a complete four-row,
topology, and protected-history audit of one of those cross-core options.

**Audit verdict at this stage:** PASS for movable-frontier integrality,
exact residual planting, pure containment carry transparency, the stated
local graphic deltas, and the scoped same-base target no-go.  The
changed-core exterior route is not excluded by that no-go.

The symbolic receiver-slot, contracted-prefix, and sidecar checks replay at

```text
python3 scratch/audit_mode_transparent_b5_carry_20260802.py
```

## 10. Exact Hall erosion, signature obstruction, and exterior relay

The prescribed-bank Hall calculation admits a sharper exact form.  With
`r=|B_0|=|R_0|`, `r_H=|R_0\cap H|`, put

\[
 s_1(X)=|N_{F\cup H}(X)|-|X|,qquad
 s_2(X)=|N_F(X)|-|X|+(b-f).                         \tag{10.1}
\]

Deleting the prescribed shores preserves Hall if and only if

\[
\begin{aligned}
 s_1(X)&\ge|N_{F\cup H}(X)\cap R_0|,\\
 s_2(X)&\ge|N_F(X)\cap R_0|+r_H
\end{aligned}                                      \tag{10.2}
\]

for every `X\subseteq B\setminus B_0`.  This follows by direct substitution
in the two residual Hall rows.  The symbolic audit checks 334,575 small
prescribed deletions with no mismatch.  It also replays the sharp-by-one
obstruction: an ambient perfect matching and two local cyclic modes may
exist while one outside token loses all `r` neighbours.

If a planted bank's old modes lie inside one incumbent augmented perfect
matching, its residual matching works for every phase vector with zero
Hall slack.  Equivalently, for fixed `B_0`, deletable receiver shores are
the bases of the rank-`r` strict gammoid dual to the receiver transversal
of the remaining real bottoms and dummies.  This was rederived directly
from base complementation; correlated whole B5 bundles still need a native
packing theorem.

The same-base sidecar no-go has an exact cross-core escape.  With the data
of Theorem 3.2 in the composition note,

\[
 F_{S_1,a}(c,b)=F_{S_2,a}(s,b)                     \tag{10.3}
\]

is the first output `P_2` and simultaneously one exterior old atom of the
second opener.  Full literal replay for every `6<=m<=30` gives

\[
 10C_4+3K_2\longrightarrow P_{22}+P_2+C_{20}+K_2
                  \longrightarrow2P_{22}+P_2,       \tag{10.4}
\]

with 15 changed atoms, four-row identity, both bank matchings, and one
carried sidecar.  The clean recurrence extends this to every
`1<=t<=m-4`:

\[
                  5tC_4+(t+1)K_2\longrightarrow tP_{22}+P_2.  \tag{10.5}
\]

All 210 pairs `(m,t)` with `5<=m<=24` replay at every intermediate phase.
The changed shore has size `7t+1`.  A tempting period-three pointwise reset
does fail by an exact repeated lower/tail resource, so the displayed
distinct-address invariant is load-bearing.

Finally, finite signatures do not imply clone planting.  The median versus
extremal two-colouring of a saturated `C10` slot makes every five-cycle
bichromatic; all 120 orders replay.  Hub `C6`s are triangles, so exhaustive
two-colour replay confirms the sharp contrast `R_2(3)=6`, but colouring a
prescribed target matching red and all other edges blue defeats every
rooted opening target.  Thus a global theorem needs positive clone-good
`C10` density and rooted `C6` codegree/Hall, not merely finitely many
protected signatures.

The relay replay is

```text
python3 scratch/audit_b5_cross_core_exterior_relay_20260802.py
```

**Final audit verdict:** PASS for the exact Hall-erosion theorem,
incumbent-aligned zero-slack composition, two-socket and length-`m-4`
bounded-sidecar relays, and the signature obstructions.  Still
**UNPROVED** are an extensive phase-common protected relay-chain host,
directed fixed-head fusion, complete address/history/reset/upper/compiler
transparency, and all-`k` literal serialization.
