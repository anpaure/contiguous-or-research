# Two- and three-component outward-ray trace coherence

Date: 2026-07-30  
Lane: R, pure mathematics  
Status: exact `b=2` and `b=3` specializations of the item-2028 seam-grid
condition.  The `b=2` gate is a two-trace forbidden-insertion criterion.
For `b=3`, the exact fixed-width catalogue has two single-seam diagonals
and, when the middle fragment is short enough, one two-seam diagonal.
The scalar inequality `q(b-1)>=b` does not imply label service.  Explicit
Johnson trace systems give the sharp local obstruction.  No global PBBS
endpoint-coherence theorem and no lower compiler are claimed here.

## 1. One seam as two insertion traces

Let

\[
 P=(P_0,\ldots,P_{m-1}),\qquad
 Q=(Q_0,\ldots,Q_{n-1})                              \tag{1.1}
\]

be two nonempty oriented rank-`r` path fragments, concatenated in the order
`P|Q`.  Define their seam-facing suffix and prefix traces by

\[
 S_i=\bigcup_{u=m-1-i}^{m-1}P_u\quad(0\le i<m),
 \qquad
 R_j=\bigcup_{u=0}^{j}Q_u\quad(0\le j<n).           \tag{1.2}
\]

For a coordinate `x`, define its first insertion times

\[
 \lambda(x)=\min\{i:x\in S_i\},\qquad
 \rho(x)=\min\{j:x\in R_j\},                       \tag{1.3}
\]

with value `infinity` if the coordinate never occurs in that trace.  Thus

\[
 S_i=\{x:\lambda(x)\le i\},\qquad
 R_j=\{x:\rho(x)\le j\}.                           \tag{1.4}
\]

The exact single-seam grid is

\[
 \mathcal G(P,Q)=\{S_i\cup R_j:0\le i<m,\ 0\le j<n\}.             \tag{1.5}
\]

For a target `Y`, put

\[
 a_Y=\min_{x\notin Y}\lambda(x),\qquad
 b_Y=\min_{x\notin Y}\rho(x),                      \tag{1.6}
\]

where the minimum of the empty set is `infinity`.

### Theorem 1.1 (forbidden-insertion trace criterion)

The host pairs for `Y` are exactly

\[
 \mathcal H_{P,Q}(Y)=
 \left\{(i,j):
 \begin{array}{l}
 i<a_Y,\ j<b_Y,\\
 \lambda(y)\le i\text{ or }\rho(y)\le j
       \quad(y\in Y)
 \end{array}\right\}.                              \tag{1.7}
\]

Consequently

\[
 \boxed{
 Y\in\mathcal G(P,Q)
 \iff
 \begin{cases}
 P_{m-1}\cup Q_0\subseteq Y,\\
 \lambda(y)<a_Y\text{ or }\rho(y)<b_Y
       \quad\text{for every }y\in Y.
 \end{cases}}                                      \tag{1.8}
\]

Equivalently, the complement of `Y` is a northeast quadrant in the
two-dimensional insertion-time diagram:

\[
 [k]\setminus Y
   =\{x:\lambda(x)>i,\ \rho(x)>j\}                 \tag{1.9}
\]

for some valid `(i,j)`.

#### Proof

The identity `S_i union R_j=Y` excludes every coordinate outside `Y`, hence
forces `i<a_Y` and `j<b_Y`.  It contains a coordinate `y in Y` exactly when
one of the two inequalities in (1.7) holds.  This proves (1.7).

If the seam endpoints are contained in `Y`, the maximal indices which do
not insert an outside coordinate are

\[
 i_Y=\min\{m-1,a_Y-1\},\qquad
 j_Y=\min\{n-1,b_Y-1\},                             \tag{1.10}
\]

with the evident convention at infinity.  Every other admissible cell lies
coordinatewise below `(i_Y,j_Y)`.  Hence a host exists exactly when its
maximal cell contains every coordinate of `Y`, which is the second line of
(1.8).  Formula (1.9) is the complement of (1.4).  QED.

### Corollary 1.2 (nested-chain monotonicity)

Let

\[
 Y_0\subsetneq Y_1\subsetneq\cdots\subsetneq Y_s   \tag{1.11}
\]

be a proper nested casualty chain.  The barriers `a_(Y_t),b_(Y_t)` and the
maximal host indices (1.10) are nondecreasing in `t`.  Therefore the whole
chain lies in the seam grid if and only if:

1. the smallest target contains the two seam endpoints and satisfies
   (1.8); and
2. at step `t>=1`, only the new coordinates in
   `Y_t setminus Y_(t-1)` need be checked in (1.8).

For a geodesic outward ray the eligible depths form an initial interval and
successive eligible targets differ by one coordinate.  Thus, after the
smallest casualty, trace coherence is one two-trace test per depth.

#### Proof

Enlarging `Y` removes forbidden coordinates, so neither first-forbidden
time can decrease.  A coordinate already accessible at the earlier
barriers remains accessible at the later barriers.  The remaining claims
follow.  Once a ray step fails to increase the union rank, later steps
cannot recover the lost unit relative to `r+q`; hence eligible geodesic
depths form an initial interval.  QED.

### Corollary 1.3 (fixed-width diagonal)

A rank-`(r+q)` target has a `q`-edge witness crossing the seam if and only if
there is an integer `i` with valid endpoint indices such that

\[
                  S_i\cup R_{q-1-i}=Y.              \tag{1.12}
\]

Equivalently,

\[
 i<a_Y,\qquad q-1-i<b_Y,                            \tag{1.13}
\]

and every `y in Y` satisfies

\[
          \lambda(y)\le i\quad\text{or}\quad
          \rho(y)\le q-1-i.                        \tag{1.14}
\]

#### Proof

Such an interval uses `i+1` vertices from the left fragment and `q-i`
vertices from the right fragment, for `q+1` vertices and `q` transitions.
Its union is (1.12).  Theorem 1.1 gives (1.13)--(1.14).  QED.

The unrestricted upper compiler needs Theorem 1.1.  Corollary 1.3 is the
stronger condition when the repaired carrier must retain fixed-width
all-depth witnesses.

## 2. Exact `b=2` theorem

Open two cyclic components at fixed edges, orient their retained fragments,
and let `C_P,C_Q` be their two nested families of proper outward-ray targets
which have lost every retained component-interior witness.  They may be
empty.  The only new owner seam in the order `P|Q` is the grid (1.5).

### Theorem 2.1 (`b=2` two-trace coherence)

For the fixed cut states and order `P|Q`, all casualties in both components
are repaired if and only if every

\[
                         Y\in\mathcal C_P\cup\mathcal C_Q             \tag{2.1}
\]

satisfies (1.8).  If fixed-width repair is required, replace (1.8) at depth
`q` by (1.12).

There is no additional target-occurrence SDR condition: different target
labels have disjoint physical interval-host families, while repeated labels
need only one witness.

#### Proof

Every interval crossing the unique seam has a suffix-prefix union (1.5),
and every member of (1.5) is a literal crossing interval.  Apply Theorem
1.1 target by target.  One interval has one union label, so host families of
distinct labels are disjoint.  QED.

A useful necessary anchor condition follows.  If both chains are nonempty,
then

\[
 P_{m-1}\cup Q_0
 \subseteq
 \left(\bigcap_{Y\in\mathcal C_P}Y\right)
 \cap
 \left(\bigcap_{Y\in\mathcal C_Q}Y\right).          \tag{2.2}
\]

For a genuine Johnson seam the left side has rank `r+1`; hence the
intersection on the right must have rank at least `r+1`.  This anchor test
is not sufficient: a desired coordinate may be stranded behind the first
forbidden insertion on both traces.

### Definition 2.2 (`E1-port_2`)

There is a legal pair of cuts, an orientation of each component, and one of
the two component orders such that:

1. the connecting edge is legal and the full seam residence/erosion tests
   pass; and
2. every proper casualty in both outward-ray chains satisfies (1.8), or
   (1.12) when fixed-width repair is demanded.

Given the retained interiors, `(E1-port_2)` is necessary and sufficient for
zero-cost upper repair with two components.  It removes the artificial
terminal-empty requirement of the one-outgoing-seam normalization: both
components' chains may use the same physical seam grid.

Cyclic reindexing with the cut edge fixed changes nothing.  Reversal swaps
a component's prefix and suffix traces; swapping component order changes
which two traces face the seam.  Moving a cut changes both its trace and its
casualty chain.  Thus existence over rotations, orientations and cut banks
is exactly the finite disjunction of Definition 2.2 over the legal states.
Fixed-width support supplies the old ray labels but contains no cross-
component insertion-time equation.

## 3. A minimal two-component trace obstruction

There are two complementary minimal obstructions.  The first isolates trace
coherence while passing an actual Johnson seam and the anchor condition.
In `J(9,5)`, take the path germs

```text
P = (12789,12389,12348,12345),
Q = (12346,12368,12689,16789).
```

The seam `12345-12346` is Johnson.  Starting from the seam endpoints, both
seam-facing traces add coordinates in the order

```text
8, 9, 7
```

over the base union `123456`.  For

\[
                  Y'=12345678,\qquad Y''=12345679,   \tag{3.0}
\]

the anchor condition holds.  For `Y'`, however, forbidden coordinate `9`
enters at time two on both traces before desired coordinate `7`; for `Y''`,
forbidden coordinate `8` enters at time one before desired coordinates `9`
and `7`.  Theorem 1.1 therefore rejects both targets despite the three
nominal q3 diagonal slots.  This is a trace germ, not a cycle-factor
counterexample; its role is to prove that endpoint containment and Johnson
legality do not imply the remaining insertion inequalities.

The second obstruction supplies actual cycles, two nonempty q3 casualty
chains, depth-two-safe cuts and component-fullness.  It is deliberately not
asserted to be a spanning PBBS factor.

In `J(9,5)`, let

```text
C1 = (12389,12489,13489,13589,15689,15789,14789,
      13479,23479,23489,23459,12359,12379).
```

At the wedge centered at `12489`, cut

\[
                         e=12489\mathbin{-}13489.    \tag{3.1}
\]

The opposite flank `12389-12489` has the same union `123489`, so the q1
wedge colour survives.  The depth-two outward target

\[
                         Z_1=1234589                 \tag{3.2}
\]

has both the cut-crossing witness

```text
12489,13489,13589
```

and the cut-avoiding witness

```text
23489,23459,12359.
```

Thus this cut is depth-two safe.  On the other hand,

\[
                         Y_1=12345689                \tag{3.3}
\]

has exactly the witnesses

```text
12389,12489,13489,13589,15689
12489,13489,13589,15689.
```

Their edge spans both contain `e`; the second is a geodesic three-edge
witness.  Cutting `e` therefore loses `Y_1`.

Let the coordinate permutation be

\[
 \pi:(1,2,3,4,5,6,7,8,9)\longmapsto(2,4,6,8,9,1,3,5,7)           \tag{3.4}
\]

and put

```text
C2 = pi(C1)
   = (24567,24578,25678,25679,12579,23579,23578,
      23678,34678,45678,46789,24679,23467).
```

The two cycles are vertex-disjoint, every consecutive pair including the
closure is Johnson-adjacent, and each component has coordinate union `[9]`.
Cut the transported wedge edge in `C2`.  It is depth-two safe and loses the
geodesic depth-three target

\[
                         Y_2=\pi(Y_1)=12456789.       \tag{3.5}
\]

Every vertex of `C2` contains coordinate `7`, while `7 notin Y_1`.
Consequently every interval crossing the sole seam between the two
components contains `7` and cannot equal `Y_1`.  This remains true for both
component orders, both orientations, and every cyclic representation of
the fixed cuts.  The unique seam cannot host both nonempty casualty chains;
indeed it cannot host `Y_1` at all.

The four endpoint pairs of these two particular fixed cuts do not contain a
Johnson connector.  Accordingly this second example isolates q2-safe,
component-full casualty traces only in the absence of a legal-connector
hypothesis, while the preceding path germ isolates the insertion obstruction
after Johnson seam legality and the anchor test have passed but is not a
cut-cycle casualty system.  Neither example alone, nor their combination,
settles the conjunction of legal connector, actual q2-safe cycle casualties,
and component-fullness.

The example is dimension-minimal in the odd-middle regime after q2
protection: at `k=7,r=4`, the depth-three target is `[7]` and is witnessed by
the whole final owner path.

### Exact scope of the counterexample

The displayed cycles use only 26 of the 126 middle owners.  They are a
genuine vertex-disjoint, component-full Johnson trace system, and are
fixed-width-complete for the displayed q2 and q3 labels.  They do not prove
that a spanning PBBS all-target factor has no different compatible cut.
Thus the strongest rigorous conclusions are separate:

* Johnson seam legality, the cross-anchor and nominal slot count do not
  imply the insertion inequalities, as the path germ shows;
* targetwise `(FW)`, q2 `(E1)`, two actual casualty chains, rotations,
  orientations and component-fullness do not produce a connector or trace
  host in the cycle system;
* their full conjunction with a legal connector remains open, and a PBBS-
  specific positive result still requires a new theorem forcing (1.8) for
  some legal cut pair.

## 4. Exact `b=3` trace catalogue

Let three oriented fragments occur in the order

\[
                         A\mid B\mid C               \tag{4.1}
\]

and let `n_A,n_B,n_C` be their vertex counts.  Write

\[
 S_X(h)=\text{union of the last }h+1\text{ vertices of }X,
 \qquad
 P_X(t)=\text{union of the first }t+1\text{ vertices of }X,        \tag{4.2}
\]

and `V_X` for the union of all vertices of `X`.

At fixed depth `q`, define

\[
\begin{aligned}
 \mathcal H_q^{AB}
   &=\{S_A(h)\cup P_B(q-1-h):
       \max(0,q-n_B)\le h\le\min(q-1,n_A-1)\},\\
 \mathcal H_q^{BC}
   &=\{S_B(h)\cup P_C(q-1-h):
       \max(0,q-n_C)\le h\le\min(q-1,n_B-1)\},\\
 \mathcal H_q^{ABC}
   &=\{S_A(h)\cup V_B\cup P_C(t):
       h+t=q-n_B-1,\ 0\le h<n_A,\ 0\le t<n_C\}.
                                                               \tag{4.3}
\end{aligned}
\]

The third family is empty unless `q>=n_B+1`.

### Theorem 4.1 (`b=3` fixed-width trace criterion)

Let `C_q` be the distinct old-lost rank-`(r+q)` ray labels.  The final path
has a fixed-width `q`-edge witness for every member of `C_q` if and only if

\[
 \boxed{\mathcal C_q\subseteq
        \mathcal H_q^{AB}\cup
        \mathcal H_q^{BC}\cup
        \mathcal H_q^{ABC}.}                        \tag{4.4}
\]

If `V_B=[k]`, every member of `H_q^(ABC)` is `[k]`; hence no proper casualty
can be repaired across both seams.  The same conclusion holds at depths
`q<n_B+1`, when the two-seam family is empty.

#### Proof

A q-edge interval crossing only `A|B` uses `h` internal edges of `A`, the
seam edge, and `q-1-h` internal edges of `B`, giving the first family and
its endpoint bounds.  The second seam is identical.  An interval crossing
both seams uses `h` internal edges of `A`, both seam edges, all `n_B-1`
internal edges of `B`, and `t` internal edges of `C`.  Its total is

\[
                         h+n_B+t+1=q,                \tag{4.5}
\]

which gives the third family.  These exhaust all q-edge intervals crossing
at least one seam, and every displayed expression is a literal interval.
QED.

For arbitrary-width upper repair, replace the diagonal families (4.3) by
the three full grids

\[
\begin{aligned}
 \mathcal G^{AB}&=\{S_A(h)\cup P_B(t)\},\\
 \mathcal G^{BC}&=\{S_B(h)\cup P_C(t)\},\\
 \mathcal G^{ABC}&=\{S_A(h)\cup V_B\cup P_C(t)\}.
                                                               \tag{4.6}
\end{aligned}
\]

Theorem 1.1 gives a forbidden-insertion fixed-point test for each of the
first two.  The same test applies to the third after requiring `V_B subseteq
Y` and treating `V_B` as a forced base.  Thus (4.4), or its full-grid
version, is a deterministic pointwise trace test.

### Corollary 4.2 (no automatic trace SDR)

After the final path is fixed, target-to-interval host families of distinct
labels are disjoint.  An occurrence SDR therefore exists exactly when every
target has a host; there is no further Hall obstruction.

Before cuts and order are fixed, the exact problem is not an ordinary SDR.
A chosen connector installs an entire label bundle, and the two connectors
must form one directed path through the three components.  For fixed cut
states it is the six-case test

\[
 \exists\pi\in S_3:\quad
 \mathcal C_q\subseteq
 \mathcal H_q^{\pi(1)\pi(2)}\cup
 \mathcal H_q^{\pi(2)\pi(3)}\cup
 \mathcal H_q^{\pi(1)\pi(2)\pi(3)}
 \quad\text{for every }q,                            \tag{4.7}
\]

together with both seam and residence tests.  This is a two-edge
bundle-cover/path condition.  The inequality `2q>=3` counts interval slots
but supplies none of their labels and does not imply (4.7).

### Definition 4.3 (`E1-port_3`)

There exist three legal cut states, orientations, and an order for which
(4.7) holds for every proper casualty and all seams pass the residence and
erosion tests.  Use (4.3) when fixed-width support must be retained and
(4.6) for ordinary upper completeness.

Relative to the retained interiors, `(E1-port_3)` is necessary and
sufficient for zero-cost upper repair with three components.

## 5. Six slots need not service three rays

The failure of scalar slot counting already has a hand-checkable Johnson
realization in `J(9,5)`.  In the following display the common coordinates
`8,9` are suppressed; every triple denotes the corresponding five-set.

\[
\begin{aligned}
 C_1&=(124,145,456,457,247,234,123),\\
 C_2&=(125,135,137,147,146,156,126),\\
 C_3&=(136,236,267,257,357,345,346,134).
                                                               \tag{5.1}
\end{aligned}
\]

The cycles are vertex-disjoint, consecutive triples meet in two
coordinates, and every component has coordinate union `[9]`.  Cut each
closure edge.  At the terminal vertex, its incoming edge and the closure
edge have the same four-coordinate union:

\[
 234\cup123=123\cup124,
 \quad156\cup126=126\cup125,
 \quad346\cup134=134\cup136.                        \tag{5.2}
\]

Thus all three closure edges are wedge flanks.  Their geodesic q3 outward
rays have labels

\[
 Y_1=12345689,qquad
 Y_2=12356789,qquad
 Y_3=12346789.                                      \tag{5.3}
\]

Use the order `C1|C2|C3`.  The seams `12389-12589` and `12689-13689` are
Johnson edges.  The six q=3 single-seam interval unions are

\[
\begin{array}{c|ccc}
C_1|C_2&1235789&1234589&12345789\\
C_2|C_3&1236789&1235689&12345689.
\end{array}                                         \tag{5.4}
\]

In particular `Y_3` is absent.  Every component is full, so a proper target
cannot be rescued by a two-seam interval.  Moreover the vertices of `C3`
contained in `Y3` form the cyclic run

```text
346,134,136,236,267,
```

whose union is `Y3`; every subinterval realizing both coordinate `4` and
coordinate `2` crosses the deleted closure edge `134-136`.  The `Y3`-
contained runs in `C1` and `C2` have unions missing respectively coordinate
`6` and coordinate `2` or `4`, so neither supplies `Y3`.  Thus `Y3` is an
actual old-lost target in this displayed three-cycle system and remains
unhosted despite six nominal q=3 slots for the three designated ray labels.

This proves that

\[
                         q(b-1)\ge b                 \tag{5.5}
\]

cannot be upgraded to label coverage from Johnson legality and component-
fullness.  The example is a local trace system, not a spanning all-target
PBBS factor.  Four of the six unions in (5.4) have rank seven and only two
have the required rank eight; this makes explicit why counting interval
positions is weaker than counting eligible labels.  Its three displayed
cuts also fail the separate depth-two `(E1)` condition, losing respectively
`1234589`, `1235689`, and `1234689`.  It isolates only the claimed q3
slot-to-label implication.  Section 3 gives the complementary q2-safe
cycle evidence, but without a legal connector.  A PBBS-specific positive
theorem would have to prove `(E1-port_3)` from additional endpoint
organization.

## 6. Exact implication and remaining scope

Combine this report with item 2028.  Let `tau_2` or `tau_3` be the number
of casualty labels failing the applicable trace criterion after the chosen
legal rethread, and let `lambda_d(T)` be the exact common lower-compiler
deletion number of the final owner path.  Then

\[
             \nu(k)\le B(k)+\tau_b+\lambda_d(T),
             \qquad b\in\{2,3\}.                    \tag{6.1}
\]

`(E1-port_b)` makes `tau_b=0`.  A feasible full `COMP_d(T)` then proves
equality.  Neither trace theorem supplies that lower compiler; all erosion,
common-`Q`, endpoint-pin and lower Hall data must be recomputed after the
chosen order and seams.

The proved/global boundary is exact.

1. Theorems 1.1, 2.1 and 4.1 are necessary and sufficient relative to the
   chosen fragments.
2. The displayed local systems refute the separately scoped deductions from
   slot count and local fixed-width/Johnson data.
3. They do not refute a stronger theorem about the specific global PBBS
   chronology or prove that every alternative cut bank fails.
4. The exact missing positive statements are precisely `(E1-port_2)` and
   `(E1-port_3)`, followed independently by `COMP_d(T)`.

## 7. Independent audit

Three independent proof passes derived respectively the b2 trace criterion,
the b2 cycle obstruction, and the b3 diagonal catalogue.  A fourth
adversarial audit checked every displayed Johnson edge, trace label and
off-by-one bound.  It forced the following scope corrections, all incorporated
above.

1. The legal-seam germ and the q2-safe cycle system establish complementary
   facts; they do not jointly realize the full legal-connector conjunction.
2. The b3 cuts are not q2-safe, so their role is only to refute the q3
   slot-to-label implication.
3. Four entries of (5.4) have rank seven.  The exact theorem counts q-edge
   interval positions first and then filters them by their literal labels.
4. The b2 cycle endpoint intersections have sizes `3,2,2,1`, confirming the
   disclosed absence of a Johnson connector for those fixed cuts.

No finite search, SAT solver, remote computation, or web input was used.
