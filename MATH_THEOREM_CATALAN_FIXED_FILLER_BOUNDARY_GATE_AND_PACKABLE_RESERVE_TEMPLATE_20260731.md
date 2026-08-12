# Fixed-filler boundary gate and a packable variable-filler reserve template

Date: 2026-07-31  
Status: exact source-relative absorber lemmas, an exact boundary-conflict
reduction, and a self-contained bounded-degree sufficient criterion; no
all-`m` reserve packing or Catalan linear matching theorem is claimed

> **Supersession note (later 2026-07-31).**  The fixed-filler bottleneck
> proved below is real for that family, but it is no longer the local
> frontier.  An explicit variable-filler construction now realizes every
> prescribed start/end boundary pair whenever `|L-U|>=3`; see
> `MATH_THEOREM_CATALAN_INDEPENDENT_BOUNDARY_ABSORBER_20260731.md`.
> The packing criteria below remain sufficient global conditions.

## 0. Verdict

The single-pair absorber in
`MATH_THEOREM_CATALAN_CRITICAL_RESERVE_ABSORBER_AND_BTK_TAIL_GATE_20260731.md`
has an exact boundary bottleneck which its interior schedule entropy cannot
change.

For endpoints `L,U` and held-out filler `c`, its off-state middle resource
set is contained in its on-state resource set and

\[
             R^+(L,U;c)\setminus R^-(L,U;c)
                    =\{L+c,\ U-c\}.                 \tag{0.1}
\]

Consequently, in independent Bernoulli middle pools of density
`p=C/m`, a prescribed endpoint pair has a usable shared filler with
probability at most

\[
                    |U\setminus L|p^2
                    \le (m+1)p^2=O(C^2/m).          \tag{0.2}
\]

This remains true no matter how the exchanged coordinates are ordered in
the interior.  Allowing either orientation only changes the right side by
a factor at most two.

Variable fillers can escape (0.2), but only through a genuinely global
selection.  Once option-specific interiors have been certified private,
the exact remaining boundary gate is an **independent transversal** in the
conflict graph of the two-resource pairs `\{L+c,U-c\}`.  This note proves a
simple packable template: if every gadget has `r` certified options, every
middle resource occurs in at most `lambda` options, and

\[
                    r\ge 4e(\lambda-1),             \tag{0.3}
\]

then a resource-disjoint choice exists.  This is a sufficient template,
not an existence proof for Boolean reserves.  The unstructured Boolean
catalogue has only `r<=m+1` and may have `lambda=2m`, so (0.3) deliberately
does not pretend that the missing critical packing is automatic.

At the critical reserve size `K=Cat_m`, there is also a sharp deterministic
resource ledger.  A fixed-filler gadget of distance
`s=|L\setminus U|` reserves exactly `2(s+1)` middle vertices across its two
states.  Therefore `K` pairwise resource-disjoint gadgets necessarily obey

\[
                  {1\over K}\sum_i s_i\le {m-1\over2}.       \tag{0.4}
\]

This is the precise capacity condition which any pairing/rethread must
meet before a variable-filler argument can start.

## 1. The explicit absorber and its boundary

Fix

\[
 L\in\binom{[2m]}{m-1},\qquad
 U\in\binom{[2m]}{m+1},\qquad s=|L\setminus U|.
\]

As in the single-pair theorem, write

\[
 L\setminus U=\{a_1,\ldots,a_s\},\qquad
 U\setminus L=\{b_1,\ldots,b_s,c,d\},
\]

put

\[
 L_i=L-\{a_1,\ldots,a_i\}+\{b_1,\ldots,b_i\},
\]

and define

\[
 Z_i=L_i+b_{i+1},\qquad C_i=L_i+c,
 \qquad D_s=L_s+d=U-c.                              \tag{1.1}
\]

The off and on states use respectively

\[
 \begin{aligned}
 R^-&=\{Z_i,C_{i+1}:0\le i<s\},\\
 R^+&=\{Z_i,C_i:0\le i<s\}\cup\{C_s,D_s\}.
 \end{aligned}                                      \tag{1.2}
\]

### Lemma 1.1 (exact nested boundary identity)

The sets in (1.2) have no repetitions and

\[
 R^-=R^+\setminus\{C_0,D_s\},\qquad
 \{C_0,D_s\}=\{L+c,U-c\}.                          \tag{1.3}
\]

In particular, the full two-state resource union has exactly

\[
                         2s+2=2(s+1)                \tag{1.4}
\]

middle vertices.

#### Proof

The distinctness is the one proved in the single-pair absorber theorem:
the `Z_i` omit both held coordinates, the `C_i` contain `c` and omit `d`,
and `D_s` contains `d` and omits `c`.  Equation (1.2) shows that both states
contain every `Z_i`, the off state contains `C_1,...,C_s`, and the on state
contains `C_0,...,C_s,D_s`.  Thus only `C_0=L+c` and `D_s=U-c` are added.
Counting gives (1.4). \(\square\)

The orderings of the `a_i,b_i` change the common interior in (1.2), but not
the two resources in (1.3).  This is why factorial interior entropy does
not repair the boundary probability.

## 2. The fixed-pair probability bottleneck

Let `P,Q` be independently sampled Bernoulli subsets of the middle layer,
each with density `p`.  Give the boundary a fixed orientation and call
`c` usable when

\[
                       L+c\in P,\qquad U-c\in Q.     \tag{2.1}
\]

There are

\[
                   r=|U\setminus L|=s+2\le m+1      \tag{2.2}
\]

possible held-out fillers.

### Lemma 2.1 (fixed-pair gate)

For every prescribed `L,U`,

\[
 \Pr(\hbox{some usable shared filler})\le rp^2.      \tag{2.3}
\]

If the `2r` boundary resources are cross-separated, the exact probability
is

\[
                         1-(1-p^2)^r.                \tag{2.4}
\]

Cross-separation holds for the displayed resources whenever `s>0`.
For `s=0`, the two filler choices give the same unordered two-resource
pair, so only (2.3) is used here.  If either boundary orientation is
accepted, the safe general bound is `2rp^2`.

#### Proof

For fixed `c`, (2.1) has probability `p^2`; the union bound gives (2.3).
Under cross-separation the events use disjoint Bernoulli coordinates and
are independent, giving (2.4).  For `s>0`, every `L+c` contains the
nonempty set `L-U`, while every `U-d` is contained in `U`; hence a lower
boundary resource cannot equal an upper one.  The two maps within each
side are injective.  Finally, accepting either orientation is bounded by
the union of two oriented events. \(\square\)

### Corollary 2.2 (fixed pairings cannot use the critical random reserve)

For any fixed list of `q` endpoint pairs, the expected usable fraction is
at most `(m+1)p^2`.  No independence between different endpoint pairs is
needed.  At `p=C/m` this is

\[
                   {C^2(m+1)\over m^2}=O(C^2/m).    \tag{2.5}
\]

Thus a fixed pairing plus more interior schedules does not yield a robust
critical reserve.  One must re-pair endpoints, correlate the pools, or use
a different absorber whose two new resources are not tied to one filler.

## 3. The critical deterministic middle-resource ledger

Put

\[
 K=\operatorname{Cat}_m,\qquad
 M=\binom{2m}{m}=(m+1)K.                            \tag{3.1}
\]

### Theorem 3.1 (critical distance budget)

Suppose `q` displayed absorbers are packed so that their complete two-state
middle-resource unions are pairwise disjoint.  If their distances are
`s_1,...,s_q`, then

\[
                        2\sum_{i=1}^q(s_i+1)\le M.  \tag{3.2}
\]

For `q=K`, this is exactly (0.4).

#### Proof

Lemma 1.1 gives a disjoint union of size `2(s_i+1)` for gadget `i`.
All unions lie in the `M`-vertex middle layer.  Summing proves (3.2), and
substituting `M=(m+1)K` proves (0.4). \(\square\)

This bound is only a resource no-go: satisfying it does not construct the
interiors.

For calibration, if `L,U` are uniform and independent on their two outer
layers, then

\[
 \Pr(s=t)=
 {\binom{m-1}{t}\binom{m+1}{t+2}\over\binom{2m}{m+1}},
 \qquad
 \mathbb E s={ (m-1)^2\over2m}.                     \tag{3.3}
\]

Hence the exact expected fixed-schedule union size is

\[
             2(\mathbb E s+1)=m+{1\over m},         \tag{3.4}
\]

only `1-1/m` below the critical per-gadget capacity `M/K=m+1`.  The
critical packing is therefore genuinely tight to one middle vertex per
gadget; this expectation is calibration, not an existence argument.

## 4. Why all filler choices are not free Cartesian entropy

For one pair define its full boundary support

\[
 S(L,U)=\{L+c,U-c:c\in U\setminus L\}.              \tag{4.1}
\]

### Lemma 4.1 (exact full-menu support)

With `s=|L-U|`,

\[
 |S(L,U)|=
 \begin{cases}
 2,&s=0,\\
 2(s+2),&s>0.
 \end{cases}                                        \tag{4.2}
\]

For `s=0`, the two fillers give the same unordered boundary pair.  For
`s>0`, the `s+2` boundary pairs are mutually vertex-disjoint.

#### Proof

Injectivity on each side is immediate.  If `s>0`, `L+c` contains an
element of `L-U` whereas `U-d` does not, so no cross equality is possible.
If `s=0`, write `U-L={c,d}`; then the two pairs are both
`{L+c,L+d}`. \(\square\)

Suppose now that one insists that the filler choices of different gadgets
be **fully Cartesian independent**: every vector of one filler per gadget
must be boundary-resource disjoint.  This holds if and only if their sets
`S(L_i,U_i)` are pairwise disjoint.  Consequently

\[
 \sum_i\left(2(s_i+2)-2\mathbf1_{s_i=0}\right)\le M. \tag{4.3}
\]

Equation (4.3) is a sharp scalar no-go for full independent menus.  It does
not rule out a globally correlated choice of one filler per gadget; that
correlated choice is the correct surviving formulation.

## 5. Exact variable-filler conflict reduction

Fix outer pairs `(L_i,U_i)`, `1<=i<=q`.  Assume that for every allowed
filler `c in F_i subseteq U_i-L_i` a complete absorber embedding has already
been certified, and that all option-specific nonboundary resources lie in
a gadget-private bank `I_i`.  Assume the `I_i` are pairwise disjoint and
disjoint from the common free boundary bank.

Make one option vertex `(i,c)` and give it the boundary pair

\[
                         B_{i,c}=\{L_i+c,U_i-c\}.    \tag{5.1}
\]

Join two option vertices of different gadgets when their pairs intersect.
Call the resulting graph `C`.

### Theorem 5.1 (exact boundary gate)

The certified absorbers admit one choice per gadget with complete
middle-resource disjointness if and only if `C` has an independent
transversal of the parts `\{i\}\times F_i`.

Equivalently, the coloured two-resource pairs (5.1) have a rainbow
matching using every gadget colour once.

#### Proof

The private-bank assumption has removed every nonboundary cross-gadget
conflict.  Two remaining options are compatible exactly when their pairs
in (5.1) are disjoint.  Thus a simultaneous choice is precisely an
independent set containing one vertex from every option part. \(\square\)

The four possible literal conflicts are

\[
 \begin{array}{ll}
 L_i+c=L_j+d,&U_i-c=U_j-d,\\
 L_i+c=U_j-d,&U_i-c=L_j+d.
 \end{array}                                        \tag{5.2}
\]

The first says that the two lower endpoints are facets of one middle set;
the second is the dual statement for upper endpoints.  A cross equality
is exactly a Boolean diamond incidence `L_i subset U_j` (or its transpose)
with the displayed added/deleted coordinates.  Thus (5.2) is a literal,
auditable incidence catalogue rather than a heuristic dependency graph.

## 6. A packable bounded-degree reserve template

For the option system above, define its middle load

\[
 \lambda=\max_{X\in\binom{[2m]}m}
     |\{(i,c):X\in B_{i,c}\}|.                      \tag{6.1}
\]

Every option conflicts with at most `2(lambda-1)` other options.

### Theorem 6.1 (bounded-load variable-filler template)

Suppose every gadget has at least `r` certified options and `lambda>=2`.
If

\[
                         r\ge4e(\lambda-1),          \tag{6.2}
\]

then the exact boundary gate in Theorem 5.1 passes.  For `lambda=1` it
passes trivially whenever every menu is nonempty.

#### Proof

Truncate every menu to exactly `r` options and choose one uniformly and
independently from each menu.  For every conflict edge between different
menus, let the bad event be that both endpoints are chosen.  Its
probability is `1/r^2`.

An option has at most `d=2(lambda-1)` conflict neighbours.  Hence at most
`rd` bad events involve a fixed menu.  A bad event involving two menus is
dependent on fewer than `2rd` other bad events.  The symmetric Lovasz local
lemma applies because

\[
             e{1\over r^2}(2rd)={2ed\over r}\le1
\]

under (6.2).  With positive probability no conflict occurs, which is the
required independent transversal. \(\square\)

For any fixed pairing of distinct outer endpoints, a middle set contains
at most `m` selected lower endpoints and is contained in at most `m`
selected upper endpoints.  Each incidence determines its filler uniquely,
so the unstructured bound is

\[
                              \lambda\le2m.          \tag{6.3}
\]

Since every shared-filler menu has size at most `m+1`, (6.2) does not close
the raw Boolean system.  A construction using this theorem must export a
much lower-congestion bank, roughly

\[
                    \lambda\le1+{m+1\over4e},        \tag{6.4}
\]

or exploit additional structure beyond the black-box local lemma.

The exact independent-transversal condition in Theorem 5.1 is the weakest
boundary statement here.  The bounded-load hypothesis is one explicit,
packable sufficient template.  Neither statement supplies the private
interior banks; at the critical scale those banks must also obey (3.2).

## 7. Finite audit and scope

The deterministic audit

```text
scratch/audit_catalan_fixed_filler_boundary_gate_20260731.py
scratch/catalan_fixed_filler_boundary_gate_m2_m6_20260731.audit.json
```

exhausts every outer pair for `m=2,...,6` and verifies:

* `|U-L|=s+2`;
* the boundary resources `L+c,U-c` and the support formula (4.2);
* the exact distance histogram (3.3);
* the critical identities `M=(m+1)K`, `N=mK` and (3.4).

As additional evidence only, it exhausts all simple alternating outer
paths through the maximum needed length at `m=2,3`.  Every nested two-state
support found has a shared-coordinate boundary pair (`36/36` at `m=2`,
`3690/3690` at `m=3`).  No general arbitrary-path invariant is claimed from
that census.

This note does **not** prove:

1. an all-`m` private-bank construction satisfying (3.2), (5.1), and
   (6.2);
2. that every alternating absorber, outside the displayed nested class,
   has a shared filler;
3. robust correlation with the leave of an almost-perfect bulk matching;
4. physical cycle elimination, residence, deep-shadow coverage, or the
   common-cap compiler;
5. the Catalan Linear Matching theorem or `nu(k)=B(k)` in a new dimension.
