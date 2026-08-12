# Minimum residence cuts as coloured interval stabbing at `k=17`

Date: 2026-08-01  
Status: exact theorem and finite audit for the frozen SCD owner forest.  The
multiple-choice provider formulation is exact at its stated gates.  No
global braid, optimal `k=17` word, or all-`k` claim is made.

## 1. The cut intervals

Let

\[
                 P=(T_0,T_1,\ldots,T_{n-1})
\]

be one directed component of the frozen rank-nine Johnson forest, and let
`h=3`.  A cut position `p in {1,...,n-1}` means the gap between `T_(p-1)`
and `T_p`.

For a coordinate `x`, let `[a,b)` be a maximal positive run in its owner
trace.  If the run is internal and has length below `h+1=4`, associate the
closed gap interval

\[
                            I_x=[a,b].                  \tag{1.1}
\]

The endpoints in (1.1) are intentional.  Cutting at `a` makes the run a
left boundary run; cutting at `b` makes it a right boundary run; cutting at
an interior gap splits it into two boundary runs.

### Theorem 1 (exact interval-stabbing criterion)

A set `C` of gaps cuts `P` into depth-three factorable pieces if and only if

\[
                         C\cap I_x\ne\varnothing        \tag{1.2}
\]

for every internal positive run of length at most three.

#### Proof

If `C` misses one such interval, that complete short run remains internal to
one piece, so the residence criterion fails there.

Conversely, after every interval is hit, every positive run internal to a
piece was already a full internal run of `P` and has length at least four.
Every newly clipped short run touches a piece boundary.  Coordinatewise
maximal erosion therefore has depth-three OR equal to the owner trace.
Moreover, four consecutive rank-nine Johnson owners have intersection rank
at least `9-3=6`, so every maximal source letter is nonempty.  Hence every
piece is a legal depth-three factor. `square`

The same proof works at rank `r` and depth `h` whenever `r>h`: use one
interval `[a,b]` for each internal positive run of length at most `h`.

## 2. Every minimum cut set

The minimum number `tau(P)` of cuts is the interval transversal number.
It is found by the standard greedy rule: process intervals by increasing
right endpoint, and whenever the current point misses the next interval,
choose that interval's right endpoint.

All minimum cut sets admit an equally short recursion.  Let `[a,b]` be an
interval with minimum right endpoint and let `tau` be the greedy optimum.
For every `p in [a,b]`, delete the intervals containing `p`; retain the
branch precisely when

\[
                 1+\tau(\mathcal I\setminus N(p))=\tau. \tag{2.1}
\]

Then recurse.  Sorting and deduplicating the selected points enumerates
every minimum transversal exactly once.  Equation (2.1) is both necessary
and sufficient because every hitting set must choose a point of `[a,b]`.

For the authenticated `k=17` forest the exact census is:

| quantity | value |
|---|---:|
| owner components | 4,862 |
| owners | 24,310 |
| old edges | 19,448 |
| affected components | 1,213 |
| minimum cuts | 1,419 |
| sum of componentwise minimum alternatives | 8,894 |
| components with more than one alternative | 1,113 |
| maximum alternatives on one component | 144 |
| forced cut edges over all alternatives | 132 |
| cut edges occurring in some alternative | 4,232 |
| maximum component length | 27 |
| maximum cuts in one component | 4 |

The minimum-cut histogram on affected components is

\[
                     1:1037,\quad2:149,\quad3:24,\quad4:3. \tag{2.2}
\]

Every one of the 8,894 alternatives was replayed through the literal
factorization test, not only through the abstract interval predicate.

## 3. Allowed and weighted cuts

Let `A` be any set of allowed cut positions.  The restricted transversal
number `tau_A(P)` is obtained greedily as follows: at the first-ending
unhit interval, choose its rightmost point belonging to `A`; declare
infeasibility if it contains none.

The usual exchange proof still applies: replacing any feasible selected
point in the first-ending interval by its rightmost allowed point cannot
hurt a later interval.  Therefore

\[
 \boxed{\text{a minimum residence cut contained in }A\text{ exists}
        \iff \tau_A(P)=\tau(P).}                         \tag{3.1}
\]

More generally, for weights `w_p`, the minimum-cardinality, minimum-weight
cut is

\[
       \min_{H\in\mathcal H_P}\sum_{p\in H}w_p,          \tag{3.2}
\]

where `mathcal H_P` is the audited finite family of minimum transversals.
Thus no new search inside a component is needed when provider prices change.

Against the zero-provider colours of the original canonical segmentation,
(3.2) gives the following deliberately frozen-weight diagnostics:

| provider predicate used as weight | canonical zero colours | minimum weighted cuts |
|---|---:|---:|
| extendable | 322 | 43 |
| conservative robust | 784 | 75 |

These are not fixed-point theorems: changing cuts changes the pieces and
hence the provider atlas.

## 4. The exact multiple-choice support master

For each component `c`, let `mathcal H_c` be its minimum cut alternatives,
and introduce

\[
                         y_{cH}\in\{0,1\},\qquad
                         \sum_{H\in\mathcal H_c}y_{cH}=1. \tag{4.1}
\]

An alternative determines a set of physical segments.  For a segment `s`
of component `c`, put

\[
                         a_s=\sum_{H:s\in H}y_{cH}.       \tag{4.2}
\]

Here `s in H` means that `s` is one of the half-open owner intervals induced
by the cut pattern `H`.

For every candidate oriented one-seam provider arc `e=(s,o,t,o')`, introduce
`x_e`.  At the support gate,

\[
                         x_e\le a_s,\qquad x_e\le a_t.   \tag{4.3}
\]

Let `U_p=T_(p-1) union T_p` be the colour destroyed by cut `p`.  All 19,448
old edge colours are distinct in the frozen forest, so the demand of a
rank-ten colour is binary.  The exact coverage clause is

\[
 y_{cH}\le
 \sum_{e:\operatorname{col}(e)=U_p}x_e
 \qquad(p\in H).                                        \tag{4.4}
\]

Adding one orientation bit `theta_s` per selected segment and the implications

\[
 x_e\le [\theta_s=o],\qquad x_e\le[\theta_t=o']          \tag{4.5}
\]

is the exact next gate.  Degree, one-path connectivity, source compatibility,
deeper upper colours, and the lower compiler are intentionally later gates.

The all-alternative atlas contains:

| object | count |
|---|---:|
| alternatives | 8,894 |
| distinct physical segments | 12,672 |
| oriented states | 25,344 |
| raw compatible Johnson arcs | 2,005,920 |
| extendable arcs | 554,218 |
| conservative robust arcs | 87,316 |

At the merely colourwise, independently projected level, extendable support
leaves 14 unsupported cuts on 14 components.  Solving (4.1)--(4.4) jointly
raises the exact optimum to 19; residual at most 18 is DRAT-UNSAT and 19 is
SAT.  Adding (4.5) costs nothing further.  This is the correct replacement
for the misleading canonical count 322.

## 5. Alternating cut/provider descent

The finite atlas suggests a useful search procedure.

1. Start from selected alternatives `H^(t)`.
2. Build their literal segment/provider graph and compute either zero-provider
   indicators or, better, dual prices from its deficient matching shores.
3. Apply (3.2) independently in every component.
4. Rebuild the provider graph and repeat.

This is a finite best-response walk, but its scalar score need not decrease:
a cut change can destroy the providers that made the previous weights cheap.
Cycle detection or perturbation is therefore an algorithmic safeguard, not
a proof.

A terminal result is sound only after freezing one common assignment and
checking, in order:

1. exactly one minimum cut alternative per component;
2. all provider endpoint segments exist;
3. one orientation per segment;
4. residence legality of every selected seam (or one exact run automaton);
5. in/out degrees and one physical path;
6. every selected lost rank-ten colour is restored;
7. the complete upper interval deck and literal lower compiler.

## 6. Two-seam and facet-socket macro columns

Pairwise robust failure need not be a true residence obstruction.  If the
middle piece is all-one in a coordinate, a run with lengths

\[
                 \operatorname{suf}(A)+|B|+
                 \operatorname{pre}(C)\ge h+1           \tag{6.1}
\]

may be legal across `A|B|C` even though both seams fail the conservative
one-seam test.  A two-seam column is therefore a hyperarc consuming three
oriented pieces and two successor positions; its legality must be checked on
the combined run summary, not as two independent robust seams.

A stronger macro is the compact resident facet socket.  For a missing
rank-ten colour `U` at `h=3`, choose four distinct labels `v_0,...,v_3 in U`
and insert the owner block

\[
                U-v_0,\ U-v_1,\ U-v_2,\ U-v_3.          \tag{6.2}
\]

It supplies `U` at all three internal seams.  Its exact exported guards are

\[
\begin{array}{c|ccc}
\text{left label}&v_1&v_2&v_3\\
\text{required age}&3&2&1
\end{array}
\qquad
\begin{array}{c|ccc}
\text{right label}&v_0&v_1&v_2\\
\text{required age}&1&2&3.
\end{array}                                             \tag{6.3}
\]

Thus a macro column records not only its repaired colour but:

* its four owner facets and ordered labels;
* the exact left/right staircase guard states;
* the component alternatives and extra extraction gaps it requires;
* every new unique colour lost at those extraction gaps;
* the new segment count and degree sockets;
* its lower intersections and compiler incidences.

If `z_m` selects macro `m`, the rank-ten balance is

\[
 D_U(y,z)
 :=\sum_{c,H:U\in H}y_{cH}
   +\sum_{m:U\in\operatorname{loss}(m)}z_m
 \ \le\ 
 \sum_{e:\operatorname{col}(e)=U}x_e
   +\sum_{m:\operatorname{target}(m)=U}z_m.             \tag{6.4}
\]

Equation (6.4) is why a socket is not a free repair: extracting its facets
creates new demands.  Owner-capacity constraints prevent two selected
sockets from consuming the same rank-nine facet.  Segment, orientation,
degree, and guard implications make a selected socket a whole physical
column rather than a symbolic colour token.

## 7. Preliminary compact-socket extraction census

On the former independently projected residual 14 (before the exact coupled
19 correction):

* the fourteen ten-facet sets are pairwise disjoint;
* every target's ten facets occur in nine original components;
* no compact four-facet socket is already exposed for free;
* minimum extra extraction cuts have histogram `1:1, 2:12, 3:1`;
* the independent total is 28;
* the recorded choices are jointly compatible with minimum residence
  patterns and still require exactly 28 extra cuts;
* those 28 cuts destroy 28 further unique rank-ten colours, nine of which
  have zero extendable one-seam support in the all-alternative atlas.

The eight-facet self-buffering socket costs 124 extra cuts on the same 14.
These figures establish that the compact macro is physically small, but the
nine-child cascade proves that macro closure, not raw extraction capacity,
is the next exact gate.  The authoritative census must be rerun on the
coupled residual 19.

## 8. Reproducible artifacts

* Frozen owner components:
  `scratch/threadA_k17_m9_scd_lower_compiler_20260801/components.tsv`,
  SHA-256 `dc4557fb557dccb87bec15476e11b81655d17c6c6c5295b020fec95adbcb47ef`.
* All minimum cuts:
  `scratch/k17_all_minimum_residence_cut_sets_20260801.audit.json`,
  file SHA-256 `a54e24c6238fccef2a88f8582c6d4dc0d499ece4983952cfd13d7bb730e02080`.
* All-minimum generator:
  `scratch/audit_k17_all_minimum_residence_cut_sets_20260801.py`,
  SHA-256 `e660fff33f899b7871010b80f68aea9cd2cc9ccf6893a4c5b38c7d1f0d364346`.
* Provider-atlas generator:
  `scratch/audit_k17_min_cut_alternative_provider_atlas_20260801.cpp`.
* Emitted tables under
  `scratch/k17_min_cut_alternative_provider_atlas_20260801/`:
  `patterns.tsv` SHA `790a3e4292eae6fdb68c1618c05c09c444c82f706bda3bb4bef785763feb143e`,
  `segments.tsv` SHA `e4ceaa36f504086f1ecdadba4b2d3feebabda34865d3fe611272e2201fab8678`,
  `states.tsv` SHA `fe7f8390aad61357ebd7313d250f404fa1c50470a67963f483cc7626560fe7c0`,
  `extendable_arcs.tsv` SHA `9ef66394ffc8c40a04292e836c02fa4838c395c3b338b41908ae994e3555f2c2`,
  and `robust_arcs.tsv` SHA
  `1e34eaf63f12de7b42d2e6f723333757763717ea3c554250e31ada9fe482d9e1`.
* Preliminary socket extraction:
  `scratch/audit_k17_extendable_residual_eight_facet_sockets_20260801.cpp`
  and `scratch/k17_extendable_residual_facet_sockets_20260801.stdout.txt`.

The heavy enumerations and C++ compilations were run on the H100 host's CPU
with `g++ -O3 -march=native`; no local heavy solver was used.

