# Residence redistribution: the exact run automaton and the `m=5` endpoint-lock obstruction

Date: 2026-07-31  
Status: exact all-`m` finite-state theorem and exact finite `m=5`
connector no-go; no all-`m` balancing construction and no completed compiler

## 0. Verdict

The new residence-clean `m=5` Catalan matching is genuine: its `210`
diamonds give exact lower and upper q1 palettes, a spanning `42`-path
forest, and no positive coordinate run of length below three strictly
inside a path.  Residence is therefore not an intrinsic obstruction to the
central matching.

It is not, however, joinable by merely orienting and ordering its forty-two
intact paths.

> **Exact endpoint-lock obstruction.** Among the forty-two paths, fourteen
> components cannot occur internally in any depth-two-resident chronology:
> in either orientation, every Johnson-legal predecessor--component--
> successor triple already contains an internal `010` or `0110`.  A linear
> chronology has only two endpoint positions.  Hence no orientation and
> permutation of the intact paths gives a depth-two-resident Hamilton path.

This obstruction is prior to deeper flags or compiler Hall.  The twenty-one
deep targets missing inside the paths all have single-seam providers, but
those providers cannot overcome the fourteen-versus-two residence failure.
The next move must alter path interiors or merge the locked components by a
further palette-preserving rethread; an endpoint-only socket solve is now
closed for this certificate.

The all-dimensional positive statement is an exact capped-run automaton.
Together with the exact seam-run identity, it turns “redistribute the run
mass” into a literal finite boundary state.  A simple immediate-safe socket
graph gives a sufficient Hamilton-path criterion.  Uniform expansion of
that graph, or a general rethread which makes its automaton word exist,
remains unproved.

## 1. The all-`m` run budget

Let `F` be a Catalan linear matching forest in `J(2m,m)`, and put

\[
 M={2m\choose m},\qquad N={2m\choose {m-1}},\qquad
 K=M-N=\operatorname {Cat}_m.                       \tag{1.1}
\]

For every coordinate \(z\), the subforest induced by owners containing
\(z\) has

\[
 {2m-1\choose m-1}\quad\hbox{vertices},\qquad
 {2m-1\choose m-2}\quad\hbox{edges}.               \tag{1.2}
\]

The edge count follows from the once-used lower colours containing \(z\).
Their difference is \(K\), so every coordinate has exactly \(K\) path
runs before joining.

Every Johnson seam between two current path components has \(m-1\) common
coordinates and merges exactly one boundary run in each of them.  After
\(c\) such seams the total run count is therefore

\[
                         2mK-(m-1)c.                 \tag{1.3}
\]

A Hamilton path has \((m+1)K+m-1\) runs; a cyclic closure has
\((m+1)K\).  Since the cyclic one-mass is

\[
                         mM=m(m+1)K,                 \tag{1.4}
\]

the cyclic average run length is exactly \(m\).  In the intended calibrated
regime the compiler threshold is \(D=d+1=\Theta(\sqrt m)\).  Thus the aggregate budget has a
\(\Theta(\sqrt m)\) margin, but this arithmetic alone gives no lower bound
on the shortest run.

## 2. Exact capped-run automaton

Fix the required minimum internal run length \(D\ge2\).  For one coordinate
use the state set

\[
                 Q_D=\{0,1,\ldots,D,\star\}.        \tag{2.1}
\]

The meanings are:

* `0`: no positive run is currently open;
* \(a\in\{1,\ldots,D-1\}\): an open run has exact length \(a\);
* `D`: an open run has length at least \(D\); and
* \(\star\): the open run began at the left endpoint and is exempt from the
  internal lower bound.

Reading a one sends

\[
 0\mapsto1,qquad a\mapsto\min(D,a+1),qquad
 D\mapsto D,qquad\star\mapsto\star.                \tag{2.2}
\]

Reading a zero sends \(0,D,\star\) to `0` and is undefined from each
\(a=1,\ldots,D-1\).  Initialize at \(\star\).  Every final state is
accepting, because a short run reaching the right endpoint is also legal.

### Theorem 2.1 (exact residence automaton)

A finite binary word is accepted by (2.1)--(2.2) if and only if every
positive run bounded by zeroes strictly inside the word has length at least
\(D\).

#### Proof

The only undefined transition closes an ordinary open run of length below
\(D\).  The state \(\star\) persists exactly while the initial run remains
open and becomes `0` at its first zero, so that run is exempt.  A final
ordinary state is accepted without reading a closing zero, exactly
exempting the terminal run.  All other closed runs pass through state `D`
before their closing zero. \(\square\)

For an oriented path \(P\) and coordinate \(z\), reading the literal
\(z\)-word of \(P\) gives a partial transformation

\[
                         \Phi_{P,z}:Q_D\dashrightarrow Q_D.    \tag{2.3}
\]

### Corollary 2.2 (exact component-word criterion)

Let \(P_1,\ldots,P_K\) be the paths of an internally \(D\)-clean Catalan
forest.  A chosen orientation and order is a depth-\(D-1\) resident middle
chronology if and only if:

1. every consecutive endpoint pair is a Johnson edge; and
2. for every coordinate \(z\), the composition
   \[
        \Phi_{P_K,z}\cdots\Phi_{P_1,z}(\star)        \tag{2.4}
   \]
   is defined.

This is an exact all-`m` run-redistribution formulation.  It is finite and
integral, but it is not an existence theorem; the product state can be
large and the all-different component order remains correlated.

## 3. Local sockets: one obstruction and one sufficient class

Call an oriented triple \((P,Q,R)\) **locally resident** if both endpoint
joins are Johnson seams and the literal concatenation \(PQR\) contains no
internal positive run shorter than \(D\).  A component \(Q\) is
**endpoint-locked** if neither orientation of \(Q\) occurs as the centre of
any locally resident triple using three distinct components.

### Theorem 3.1 (locked-component obstruction)

If an internally \(D\)-clean path forest has a resident linear joining,
then it has at most two endpoint-locked components.

#### Proof

Every component which is not first or last has an immediate predecessor
and successor in the joining.  Their three-component subword is a literal
subword of the final chronology.  Any short run bounded strictly inside
that subword is bounded strictly inside the final word, so the triple must
be locally resident.  Therefore every locked component occupies one of the
two global endpoint positions. \(\square\)

The converse is false: short runs can span several components and the
component order must still be Hamiltonian.

There is also a useful positive subclass.  For an oriented path \(P\), let
\(s_z(P)\) be the length of its terminal \(z\)-run and let \(p_z(P)\) be
the length of its initial \(z\)-run, with value zero when the corresponding
endpoint omits \(z\).  For a Johnson seam from terminal owner \(X\) of
\(P\) to initial owner \(Y\) of \(Q\), call the arc **immediately safe**
when

\[
\begin{array}{ll}
s_z(P)\ge D, &z\in X\setminus Y,\\
p_z(Q)\ge D, &z\in Y\setminus X,\\
s_z(P)+p_z(Q)\ge D, &z\in X\cap Y.
\end{array}                                           \tag{3.1}
\]

### Theorem 3.2 (immediate-safe Hamilton criterion)

If one can orient the components and find a Hamilton path using only
immediately safe arcs, then their literal concatenation is resident.

#### Proof

A positive run closed at a seam loses the exchanged-out coordinate and has
terminal length at least \(D\).  A run beginning at a seam in the
exchanged-in coordinate has initial length at least \(D\).  Every common
coordinate merges its two boundary pieces to length at least \(D\).
Interior runs were already clean.  Initial and terminal runs of the whole
word are exempt. \(\square\)

Condition (3.1) is sufficient, not necessary: a path which is all-one in a
coordinate can transport a still-short run to a later seam, and the exact
automaton (2.3) remembers that extra state.

## 4. Exact `m=5` endpoint-lock certificate

For the independently replayed residence-clean matching of item2188:

\[
 |E(F)|=210,qquad c(F)=42,                           \tag{4.1}
\]

both q1 palettes are exact, and the strictly internal positive-run
histogram is

\[
                         3^{42}4^7 5^3 6^4 7^8 9^1. \tag{4.2}
\]

The exact endpoint audit has:

\[
\begin{array}{c|c}
\text{oriented component states}&84\\
\text{directed Johnson connector arcs}&608\\
\text{oriented predecessor--centre--successor candidates}&4270\\
\text{locally resident oriented triples}&220.
\end{array}                                           \tag{4.3}
\]

Exactly the following fourteen component indices are endpoint-locked:

\[
      0,5,10,14,15,20,21,27,29,31,34,36,38,39.       \tag{4.4}
\]

The indices are those obtained by reconstructing components in increasing
minimum-owner order; the audit JSON includes every literal path.  In each
of the twenty-eight oriented rows, the resident predecessor/successor count
is zero despite nonempty raw predecessor and successor banks.

### Corollary 4.1 (no intact-path residence joining)

No Hamilton path obtained by orienting, permuting and Johnson-joining the
forty-two paths in item2188 is depth-two resident.

#### Proof

Theorem 3.1 permits at most two locked components, whereas (4.4) gives
fourteen. \(\square\)

No solver result is needed for the mathematical implication.

## 5. The deep-flag ledger does not cause this no-go

The internally clean paths miss twenty-one fixed-width, depth-aligned flag
targets.  Every one has at least one provider window crossing exactly one
raw Johnson connector.  In the
table below, `a/e` means `a` oriented-state arcs and `e` distinct physical
connector edges.  Reversing a physical edge usually contributes the factor
two in the first count.  The exact single-seam provider counts are:

\[
\begin{array}{c|c|l}
q&\text{shore}&\text{target: oriented arcs/physical edges}\\ \hline
2&-&026:18/9,\ 029:4/2,\ 032:4/2,\ 049:12/6,\ 190:6/3,\ 2c0:8/4\\
2&+&1e7:10/5,\ 1f6:2/1,\ 23f:12/6,\ 2bb:6/3,\ 35e:4/2,\ 375:2/1,\\
 &&3b5:4/2,\ 3cd:16/8,\ 3d3:12/6,\ 3f1:16/8\\
3&-&042:22/11,\ 048:38/19\\
3&+&1ef:12/6,\ 2bf:14/7\\
4&+&3ef:54/26.
\end{array}                                           \tag{5.1}
\]

Thus no target is individually socket-dead, and no rankwise marginal
zero-host obstruction appears.  These counts impose **no** residence,
distinct-port, connector-colour, connectivity or simultaneous-scheduling
filter; in particular they do not prove a rankwise matching statement.
A provider arc is useful only inside a globally resident component word.
Corollary 4.1 says that such a word does not exist on the intact component
bank, even before the twenty-one service requirements are imposed.

## 6. Consequences for the next interior rethread

Relative to the synchronized item2183 source, the item2188 matching changes
`119` of the `210` lower-to-upper partners.  The independently
proof-producing run-span model gives the central-subsystem bracket

\[
                         30\le s_{\rm int}\le119,     \tag{6.1}
\]

where \(s_{\rm int}\) is the number of changed matching partners needed to
obtain a two-palette-exact, internally residence-clean Catalan path forest.
The lower bound uses the exact support-29 degree-\(\le2\) UNSAT
certificate; it does not assert feasibility at support 30.

Corollary 4.1 shows that the upper endpoint in (6.1) is not yet
connector-ready.  A successful next rethread must, at minimum:

1. retain both q1 palettes and the path-forest row;
2. keep all path-internal runs clean;
3. reduce the endpoint-locked count from fourteen to at most two, or bypass
   the fixed component bank by changing its interiors again;
4. select connector windows covering the twenty-one rows in (5.1); and
5. only then pass the depth-two envelope and lower compiler Hall test.

The locked-component count is therefore a cheap, exact regeneration
potential.  It is stronger than counting internal short runs and should be
tested at every intermediate matching, not only after a stochastic search
has reached zero internal defects.

## 7. Compiler-envelope boundary

For a final linear chronology \(T=(T_0,\ldots,T_{M-1})\), the maximal
depth-two source envelopes are

\[
 E_j(T)=\bigcap_{\max(0,j-2)\le i\le\min(j,M-1)}T_i,
 \qquad 0\le j\le M+1.                              \tag{7.1}
\]

Theorem 2.1 with \(D=3\) is exactly the coordinatewise condition
\(D^2E(T)=T\).  Compare the old and new chronologies first as cyclic
closures.  If there are \(s\) old-only seams and \(\mathcal P\) is the
family of maximal common cyclic fragments, then the depth-two boundary
family on either cyclic chronology has exact size

\[
             b_2=\sum_{P\in\mathcal P}\min(2,|P|)\le2s           \tag{7.2}
\]

For a fixed linear opening, the changed internal start set is a subset of
this family and has size at most \(2s\); a changed opening is handled by
the endpoint terms below.  The transported OR value of an occurrence-
aligned compiler cell using \(h\) consecutive envelope letters can change
only in a cyclic boundary family of size

\[
             b_{h+1}=\sum_{P\in\mathcal P}\min(h+1,|P|)
             \le(h+1)s.                              \tag{7.3}
\]

Changed linear openings add four endpoint envelope cells per chronology
and the corresponding wider halos.  Absolute-position pins, controller
footprints or nonaligned representative choices require their own phase
support and are not bounded by (7.3).  These are support bounds, not Hall.
The item2188 forest has no resident joining, so it supplies no admissible
`COMP_2(T)` instance; a merely formal incidence graph is irrelevant.  Hall
becomes meaningful only after the endpoint-lock debt has been removed and
one literal chronology passes Theorem 2.1.

## 8. Exact proved and open boundary

Proved:

1. the all-`m` run budget and exact seam-merger identity;
2. the exact capped-run automaton and component-word criterion;
3. the locked-component obstruction and immediate-safe sufficient theorem;
4. the literal fourteen-versus-two no-go for intact joining of item2188;
5. positive individual single-seam providers for all twenty-one deep debts;
6. the central internal-rethread support bracket (6.1); and
7. the exact occurrence-aligned compiler-envelope delta once a final
   chronology exists.

Open:

1. a further palette-preserving rethread of the `m=5` matching which is
   both internally clean and endpoint-joinable;
2. simultaneous residence and service of all twenty-one deep targets;
3. the resulting lower compiler Hall matching; and
4. an all-`m` theorem producing a component word accepted by the automaton.

The new positive central matching therefore changes the frontier but does
not complete the base: residence has moved from a path-interior obstruction
to an exact endpoint-state obstruction.  The compiler remains downstream
of both.

## 9. Reproducibility

The endpoint-lock replay is:

```text
scratch/audit_ad_m5_residence_clean_triple_endpoint_obstruction_20260731.py
scratch/ad_m5_residence_clean_triple_endpoint_obstruction_20260731.audit.json
```

It reconstructs the matching and paths from the item2188 candidate,
enumerates all `608` connector arcs and all `4270` oriented triples, checks
all ten coordinate words literally, and records all twenty-one provider
rows.  It uses no SAT solver or heavy search.

Authoritative upstream inputs are:

```text
MATH_THEOREM_CATALAN_SEAM_RUN_COUNT_AND_RESIDENCE_MARGIN_20260731.md
MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_INTERIOR_RETHREAD_20260731.md
scratch/catalan_m5_residence_rethread_c4c6_candidate_20260731.txt
```

All finite claims are scoped to that exact matching.  No statement here
claims that arbitrary Catalan linear matchings are middle-levels-resolvable
or that average run length implies minimum residence.
