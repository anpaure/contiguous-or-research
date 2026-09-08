# Balanced DERF preservation by uniform component debt and residual donors

Date: 2026-07-31  
Status: exact bounded-transshipment and residual-donor preservation
theorems, with an independently replayed finite invariant at outputs
`n=5,6,7`.  Simultaneous donor packing and all-parameter preservation
remain open.  Generic endpoint rounding is not used.

## 0. Verdict

The balanced strict-DERF orientation gate has a bounded-transshipment
normal form.  Put uniform weight `1/(n+2)` on every strict occurrence.
Every outer row is already saturated.  The remaining middle correction is

\[
\begin{array}{c|c}
\text{middle type}&b_Z(x)\\ \hline
\text{internal}&-2/[n(n+2)]\\
\text{unchosen endpoint}&-1/n\\
\text{chosen endpoint}&3/(n+2)\\
\text{isolate}&2/(n+2).
\end{array}                                                \tag{0.1}
\]

A path of length `ell` has total debt

\[
                         {2(n-\ell)\over n(n+2)},             \tag{0.2}
\]

independent of orientation.  Reversal changes only one endpoint dipole of
strength `C/N`.  Thus the live invariant is a bounded correction flow for
the component-length debts together with a routable bank of complementary
endpoint dipoles.  No generic rounding assertion is needed.

There is also an exact residual-flow form.  For a fixed SBE orientation,
reverse one path with currently selected terminal `a` and mate `b`.  The
reversal preserves the shore if and only if the residual SBE closure
network carries `C` units from `a` to `b`.  For several reversals the exact
condition is one setwise residual cut inequality, equivalently a
simultaneous donor transshipment.  Individual donor paths are not enough.

The authenticated direct-lift outputs have the following sharp finite
property:

\[
\begin{array}{c|c|c|c}
n&C&\text{nontrivial paths}&\text{paths with donor }\ge C
   \text{ on both shores}\\ \hline
5&132&33&33\\
6&429&114&114\\
7&1430&386&386.
\end{array}                                                \tag{0.3}
\]

Literal min-cut replay confirms that every one-component reversal remains
both-SBE in all three rows.  The first both-SBE `n=4` orientation is a
negative control: three components have deficient donor values and exactly
those three reversals fail.  Since that forest already has
`eta^\pm>=3`, the facet-continuation margin does not imply donor
preservation.

The proper tight families at `n=5,6,7` are terminal Hall lattices, but the
upper lattices contain many crossing pairs.  Therefore ordinary laminarity
is false on the positive chain.  The correct surviving coordinate is the
Dulmage--Mendelsohn/residual-donor order.  The first unproved induction row
is simultaneous donor cut domination for the component set required by the
next common-basis/graphic choice.  This is a capacity/congestion row in the
bounded correction, not another endpoint-rounding row.

## 1. Uniform flow and component debt

For one shore, every outer occurrence degree is `n+2`, while the exact
direct degree law at a middle vertex is

\[
                         d_G(x)=n-d_F(x).                     \tag{U.1}
\]

The uniform occurrence flow

\[
                              f_0(e)={1\over n+2}              \tag{U.2}
\]

therefore gives every outer vertex load one and gives `x` middle load

\[
                         \ell_F(x)={n-d_F(x)\over n+2}.        \tag{U.3}
\]

The desired SBE load is one at a chosen terminal and `R/N` elsewhere.
Using

\[
 {C\over N}={2(2n+1)\over n(n+2)},\qquad
 {R\over N}=1-{C\over N},                                  \tag{U.4}
\]

subtraction of (U.3) gives exactly the four rows of (0.1).

### Theorem 1.1 (orientation-free component debt)

If a path has `ell` edges, with `ell=0` for an isolate, then the sum of its
middle corrections is (0.2).  The total over all components is zero.
Reversing a nontrivial component replaces the correction vector by

\[
 b_{Z'}-b_Z={C\over N}({\bf1}_{b}-{\bf1}_{a}),         \tag{U.5}
\]

where `a` is the old selected terminal and `b` its mate.

#### Proof

A nontrivial path has two endpoints and `ell-1` internal vertices, so its
debt is

\[
 {3\over n+2}-{1\over n}
 -(\ell-1){2\over n(n+2)}
 ={2(n-\ell)\over n(n+2)}.                            \tag{U.6}
\]

The isolate row is the same formula at `ell=0`.  Since
`N=n Cat_n` and the forest has `N` edges and `Cat_n` components, the
component lengths have mean `n`, proving total debt zero.  Finally,

\[
 {3\over n+2}+{1\over n}
 ={4n+2\over n(n+2)}={C\over N},                       \tag{U.7}
\]

which proves (U.5). `square`

### Theorem 1.2 (bounded-correction equivalence)

SBE for terminal bank `Z` is equivalent to numbers `theta(e)` on the
occurrences satisfying

\[
\begin{aligned}
 \sum_{e\ni o}\theta(e)&=0 &&(o\in O),\\
 \sum_{e\ni x}\theta(e)&=b_Z(x) &&(x\in X),\\
 \theta(e)&\ge-{1\over n+2} &&(e\in E).
\end{aligned}                                               \tag{U.8}
\]

#### Proof

If `f` is the fractional occurrence matching supplied by SBE, take
`theta=f-f_0`.  Conversely (U.8) makes `f=f_0+theta` nonnegative, preserves
every outer load, and gives the desired middle loads. `square`

The orientation-independent task is to route (0.2) for all components.
The orientation task is only to superpose the dipoles (U.5) without making
an occurrence fall below `-1/(n+2)`.  This is the preservation coordinate
used below.

The authoritative derivation is

```text
MATH_THEOREM_CATALAN_STRICT_UNIFORM_FLOW_COMPONENT_DEBT_20260731.md
  SHA 0e7ec1e9b669975a8c5ccb2570d98fd9086ce53d4e416efe82dc7c310cc66fa0
scratch/h2_audit_catalan_strict_uniform_flow_component_debt_20260731.py
  SHA 2e392abf99224975b25b516ee40747169376437c1bfa05ab34b236ccf9612229
```

The degree `n+2` in (U.1)--(U.3) is an occurrence-**multigraph** degree.
When parallel occurrences have the same simple closure cell, their
nonnegative flow is aggregated for the residual network; conversely an
aggregate can be split among its copies.  Thus the normalized correction
and scaled closure formulations are exactly equivalent despite parallel
occurrences.

## 2. Cut-dual endpoint form (comparison only)

Fix a Catalan path forest at parameter `n`.  Use

\[
 M={2n\choose n},\quad N={2n\choose n-1},\quad
 P={2n\choose n-2},\quad C=M-P,\quad R=N-C,\quad K=M-N.
                                                               \tag{1.1}
\]

For one strict shore let `G=(O,X)` be its occurrence graph.  For
`A subseteq X`, put

\[
 O(A)=\{o\in O:N_G(o)\subseteq A\},\qquad
 g(A)=N|O(A)|-R|A|.                                      \tag{1.2}
\]

The endpoint-orientation theorem gives SBE exactly as

\[
                         C|Z\cap A|\ge g(A)             \tag{1.3}
\]

for every `A`, where `Z` is the terminal bank on that shore.

Let `E` be the endpoints of the nontrivial paths and let `H` be the
matching on `E` which pairs the two endpoints of each path.  Isolated paths
are fixed terminals and are removed by the exact projection

\[
 \Psi^s(A)=
 \max_{S:\,S\cap E=A}
 \bigl(g^s(S)-C|I_0\cap S|\bigr),\qquad A\subseteq E.  \tag{1.4}
\]

Orient every edge of `H` from the lower terminal to the upper terminal.
Write `e_H(A)` for the number of matching edges wholly inside `A`, and
`rho_D(A)` for the number of matching edges entering `A`.  Thus `Z^-` is
the head/upper-terminal bank and `Z^+` is the tail/lower-terminal bank.
Then

\[
 |Z^-\cap A|=e_H(A)+\rho_D(A).                         \tag{1.5}
\]

The lower terminal is the tail.  Hence, for `B=E-A`,

\[
 |Z^+\cap B|=e_H(B)+\rho_D(A).                         \tag{1.6}
\]

Define the exact rounded quotas

\[
 q^s(A)=
 \max\left\{0,
   \left\lceil{\Psi^s(A)\over C}\right\rceil-e_H(A)
 \right\},                                             \tag{1.7}
\]

and

\[
             h(A)=\max\{q^-(A),q^+(E-A)\}.             \tag{1.8}
\]

### Proposition 2.1 (exact coupled cut dual)

A coherent component orientation is SBE on both shores if and only if its
orientation `D` of the endpoint matching satisfies
`rho_D(A)>=h(A)` for every `A subseteq E`.

#### Proof

Partial maximization in (1.4) is the exact elimination of every nonendpoint
middle coordinate.  Substituting (1.5) into the upper rounded form of
(1.3) gives `rho_D(A)>=q^-(A)`.  Substituting (1.6) into the lower row for
`E-A` gives `rho_D(A)>=q^+(E-A)`.  Their conjunction is the displayed
system, and every step is reversible. `square`

This statement is retained only as the exact cut dual of (U.8).  The
ceiling explains why a raw midpoint argument can fail, but no generic
endpoint-rounding or Frank-style preservation claim is made here.  The
bounded correction retains the occurrence congestion which the projected
endpoint system forgets.

## 3. Exact residual-donor theorem

For a fixed shore and terminal bank `Z`, form the standard closure network:

* `source -> o` has capacity `N` for every `o in O`;
* `o -> x` has infinite capacity for every occurrence adjacency; and
* `x -> sink` has capacity `R+C 1_(x in Z)`.

The total source capacity is `NP`.  Also

\[
 RM+CK=(N-C)M+C(M-N)=N(M-C)=NP.                       \tag{3.1}
\]

Thus SBE is equivalent to a maximum flow of value `NP`.

Fix such a maximum flow and let `D` be its residual network.  For every
source-containing, sink-avoiding vertex set `S`, its scaled SBE slack is

\[
             c(\delta^+(S))-NP
             =c_D(\delta^+(S)).                       \tag{3.2}
\]

The equality follows from flow conservation: residual outgoing capacity is
the original cut capacity minus the flow value.

Let `J` be a set of path components to reverse.  On this shore write `a_i`
for the currently selected terminal and `b_i` for its mate.  The new slack
of `S` is exactly

\[
 c_D(\delta^+(S))-C\left(
   |\{i\in J:a_i\in S,b_i\notin S\}|-
   |\{i\in J:b_i\in S,a_i\notin S\}|
 \right).                                             \tag{3.3}
\]

### Theorem 3.1 (setwise donor preservation)

The simultaneous reversal of `J` preserves this shore if and only if
(3.3) is nonnegative for every source-containing, sink-avoiding `S`.
Equivalently, `D` supports an aggregate, pairing-free transshipment with
supply `C` at every old selected terminal `a_i` and demand `C` at every
mate `b_i`.

For one component `i`, preservation is equivalent to a residual
`a_i -> b_i` maximum-flow value at least `C`.

#### Proof

Reversal decreases the middle-to-sink capacity of `a_i` by `C` and
increases that of `b_i` by `C`.  This changes each cut by exactly the signed
term in (3.3), proving the first equivalence.  Standard max-flow/min-cut
applied to the residual network turns the same family of inequalities into
the transshipment criterion.  For one source-sink pair this is the ordinary
residual maximum-flow condition.  All original source arcs and all
middle-to-sink arcs are saturated because their two total capacities both
equal `NP`.  Therefore adjoining the original source to, or removing the
original sink from, a candidate transshipment cut cannot worsen it; the
source-containing, sink-avoiding cuts in (3.3) are sufficient. `square`

For both shores the theorem is applied twice, with complementary selected
terminals.  Pairwise resource-disjoint `C`-unit donor paths are a clean
sufficient certificate for reversing a set of components.  Merely knowing
the individual donor value of every component is at least `C` is not a
simultaneous packing theorem.

### Corollary 3.2 (normalized endpoint actuator)

Divide the scaled closure flow by `N` and subtract the uniform flow `f_0`.
A residual `C`-unit transshipment from `a` to `b` becomes an occurrence
adjustment `psi` with zero outer sums, middle sums

\[
             {C\over N}({\bf1}_{b}-{\bf1}_{a}),       \tag{3.4}
\]

and `theta+psi>=-1/(n+2)`.  Hence it is exactly the bounded actuator for
the endpoint dipole (U.5).  For several reversals, (3.3) is exactly the
shared-congestion condition for the sum of their dipoles.

This identifies what is preserved: the component-length debt is fixed,
while the residual network measures which endpoint dipoles can be moved
through the remaining occurrence capacity.

## 4. Tight cuts are Hall lattices, not laminar families

It is useful to complement a closed middle set.  For `H subseteq X`, put

\[
 \Delta_Z(H)=N|N_G(H)|-R|H|-C|Z\cap H|.               \tag{4.1}
\]

SBE is exactly `Delta_Z(H)>=0` for every `H`.  If `H subseteq Z`, then

\[
               \Delta_Z(H)=N\bigl(|N_G(H)|-|H|\bigr). \tag{4.2}
\]

Hence, whenever every proper tight complement is contained in `Z`, the
proper tight family is exactly the Hall-tight family of the bipartite graph
from terminals to outer vertices.  It is a distributive
Dulmage--Mendelsohn lattice.  It need not be laminar: two Hall-tight sets
may cross, while their intersection and union remain tight.

The independent finite reconstruction finds precisely this terminal-only
property for the stored orientations at `n=5,6,7`.  The numbers of nonempty
proper tight complements on the upper/lower shores are

\[
                 (287,2),\qquad(1151,2),\qquad(1151,2). \tag{4.3}
\]

The upper families have respectively `30,118`, `559,210`, and `559,210`
crossing unordered pairs.  Thus a laminar-all-tight-cuts invariant is
literally false.

The upper `n=5 -> n=6` lattice is the old lattice times two independent
newborn singleton atoms:

\[
                         (287+1)\,2^2-1=1151.          \tag{4.4}
\]

The `n=6 -> n=7` upper lattice is an exact translated copy, and the lower
lattice copies exactly at both steps.  At the raw half-endpoint point, by
contrast, the only nonempty zero-slack closure on either shore at each of
`n=5,6,7` is the full universe.  Therefore the observed recursion has a
stable Hall/DM boundary shell, not a laminar boundary shell.

These facts concern zero-slack rows.  They do not prove bounded correction
for every partial cross-sector debt vector or simultaneous donor
routability.

## 5. Exact finite donor census

The independent audit rebuilds the occurrence graphs from the authenticated
direct-lift witness, computes a maximum closure flow, extracts every
single-component residual donor value, and then reruns literal min-cut SBE
after every reversal.

For the stored direct-lift orientations:

\[
\begin{array}{c|c|c|c|c}
n&C&\text{nontrivial paths}&
 \min\lambda^-&\min\lambda^+\\ \hline
5&132&33&132&132\\
6&429&114&429&429\\
7&1430&386&1430&1430.
\end{array}                                             \tag{5.1}
\]

Every one-component reversal has scaled violation `(0,0)`.

The first both-SBE `n=4` orientation is the sharp negative control.  Here
`C=42`; its donor histograms are

\[
 \text{upper}:42^9,28^1,\qquad
 \text{lower}:42^8,28^1,14^1.                         \tag{5.2}
\]

Exactly three reversals fail: path `0` below by `14`, path `4` above by
`14`, and path `10` below by `28`.  These are exactly `C-lambda`.

The source witness, residual-flow implementation and literal replay are
frozen as

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
  SHA 220994673d2b6f091c8c3493c4ef82023770211ca38df2548eace392a8efa26d
scratch/audit_catalan_derf_residual_donor_paths_n4_n7_20260731.py
  SHA f09622dc2bcd2dbcf85b732a209a8bd111dfae164be783bfbe5f3a967f56ca3a
scratch/catalan_derf_residual_donor_paths_n4_n7_20260731.audit.json
  SHA 010967c00c19c970bc5def3cc3ea32b6ec7a641e390bab0659cc2b333aeff058
  canonical payload
  7d0824c12f47bc977816869b466b68f98fe59390f2c237ed689443561cc3b969
```

The independent tight-lattice reconstruction is frozen as

```text
scratch/audit_h2_catalan_derf_sbe_tight_family_anatomy_20260731.py
  SHA e8151e2d827613a340f98982f45bd741818fabae39b8e410c9ae5ba9484fa72f
scratch/h2_catalan_derf_sbe_tight_family_anatomy_20260731.audit.json
  SHA 3d8733343f5568b8ddf59fcf49535f10dac7e099e3bf7b7156c84d3ada02a833
  canonical payload
  29ebe2879a25f80e36599b5f62874cca1914db0b7b20c2a82ce8f72ec3a5540f
```

## 6. The exact first missing row

The positive finite statement is stronger than stored SBE: the full
single-flip donor margin appears at `n=5` and survives the two audited
outputs `n=6,7`.  It is not implied by `eta^\pm>=3`, because the repaired
`n=4` control has that facet margin and fails (5.2).

Two equivalent theorem targets remain.

1. **Residual form.**  For the set `J` of component reversals needed by the
   next common-`Q` and rooted-graphic selection, prove (3.3) on both shores,
   or construct the two simultaneous donor transshipments.  Individual
   `C`-connectivity does not imply this setwise row.
2. **Bounded-correction form.**  Construct the orientation-independent
   component-debt correction first, then superpose the required endpoint
   dipoles while retaining the lower bound `-1/(n+2)` on every occurrence.
   Full-sector cumulative reserve and the private co-singleton shell do not
   certify this shared congestion row.

A minimal obstruction is therefore an augmented residual cut violating
(3.3), equivalently a subset of endpoint dipoles whose total demand cannot
be routed without pushing some occurrence below `-1/(n+2)`.  This is the
first row to audit at the next direct lift.

## 7. Scope

The uniform-debt identity, bounded-correction equivalence, cut dual, and
residual donor theorem are all-parameter statements.  The tight-lattice and
donor censuses are only for the authenticated direct-lift fixtures.  No
claim is made that every direct-lift output routes its component debts, that
arbitrary component sets can be reversed, or that SBE supplies physical
representatives.  Indeed the authenticated `n=3` counterexample in
`MATH_THEOREM_CATALAN_SBE_ETA3_SIDE_REPRESENTATIVE_N3_COUNTEREXAMPLE_20260731.md`
has both-SBE and `eta^\pm=3` but no degree-capped representative for any
common co-singleton basis.  Rooted topology, residence, deep shadows,
common cap, the word compiler, and the global contiguous-OR equality remain
separate.
