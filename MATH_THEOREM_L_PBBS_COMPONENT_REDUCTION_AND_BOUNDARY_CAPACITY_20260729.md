# PBBS component reduction, the exact cut--join law, and the boundary-capacity threshold

Date: 2026-07-29

Status: exact fixed-`M0` cut--join theorem; independently replayed
`k=15` all-depth chain `9 -> 4 -> 3 -> 2`; exact connectivity-free
compiler criterion; exact finite support-`<=8`, two-packet, and neutral-router
boundaries at the final two-cycle state.  The universal assertion that every
PBBS resident all-depth factor admits descent to `O(d)` components is **not
proved or disproved**.  The statement that `O(d)` components alone are enough
for boundary absorption is false: the rank-`r-1` boundary capacity is exactly
two, independent of `d`.

## 1. Main conclusions

Let `k=2r-1` be odd and let a lower-`q1`-rainbow Johnson factor have `c`
physical components.  There are two different questions.

1. **Factor surgery.**  Can alternating matching exchanges reduce `c` while
   preserving residence and the complete lower/upper deck?
2. **Linear compilation.**  After opening the remaining cycles and joining
   the resulting paths, can the deleted edge colours and all other lower
   targets be installed in one common source word?

The `k=15` certificate answers both questions, but by different mechanisms:

```text
9 cycles --support 4--> 4 --support 6--> 3 --support 4--> 2,
```

followed by one arbitrary upper-safe Johnson seam and absorption of the two
unrecycled cut colours at the two global source boundaries.  A final
`2 -> 1` factor switch is neither present nor needed.

The correct general compiler threshold is

\[
             h=|R\setminus Q|\le 2,                 \tag{1.1}
\]

where `R` is the set of cut colours and `Q` is the set of colours restored by
new seams.  It is **not** `c=O(d)`.  In particular:

* `c<=2` makes the `q1` colour ledger boundary-absorbable without requiring a
  seam to recycle either cut colour;
* for `c>2`, at least `c-2` distinct cut colours must be restored by seams,
  unless some other literal mechanism outside the usual depth-`d` source
  architecture is supplied;
* even when (1.1) holds, residence, every upper layer, the exact boundary
  omission equations, and the full lower compiler/Hall system remain
  separate gates.

Thus connectedness is a sufficient normalization, not a necessary theorem
hypothesis.  Two components are the robust topology endpoint for the usual
odd-middle compiler.

## 2. Exact fixed-matching cut--join theorem

Let `X,Y` be finite sets of the same size.  Fix perfect matchings

\[
              M_0,P:X\longrightarrow Y
\]

and identify their alternating factor with

\[
              \sigma=M_0^{-1}P\in\operatorname{Sym}(X).     \tag{2.1}
\]

Its components are exactly the cycles of `sigma`.  Let another perfect
matching be

\[
              Q=P\pi,
\]

where `pi` is a permutation supported on `S subseteq X`; the nontrivial
cycles of `pi` are precisely the connected alternating components of
`P triangle Q`.

For `x in S`, let `rho(x)` be the next member of `S` encountered after `x`
on its old `sigma`-cycle.

### Theorem 2.1 (cut--join identity)

One has

\[
 \boxed{
 c(\sigma\pi)=c(\sigma)-c(\rho)+c(\pi\rho).}
                                                               \tag{2.2}
\]

Here `c(rho)` is the number of old factor components touched by the
exchange, while the cycles of `pi rho` are exactly the new components built
from the touched old fragments.  More precisely, put

\[
 a_x=\min\{a\ge1:\sigma^a x=\rho(x)\}.                       \tag{2.3}
\]

The new component indexed by a cycle `K` of `pi rho` has length

\[
                         \sum_{x\in K}a_x.                    \tag{2.4}
\]

Consequently the touched components are fused into one if and only if

\[
                         c(\pi\rho)=1.                        \tag{2.5}
\]

#### Proof

Cut each old arrow immediately before the marked successor of every member
of `S`.  The old components become directed fragments.  The fragment
labelled by `x` has length `a_x`, and under the rematched permutation its
successor fragment is labelled by `pi rho(x)`.  Hence fragment cycles are
the cycles of `pi rho`, proving (2.2)--(2.5).  `square`

This theorem explains why “the exchange touches several components” is not
enough.  The cyclic interleaving `rho`, not merely the incidence set, decides
whether the exchange merges or splits.

### Corollary 2.2 (equivariant voltage ledger)

For a `C_k`-equivariant quotient matching, write marked physical ports as
`J x Z_k` and

\[
 \pi(j,a)=(t(j),a+\delta_j),\qquad
 \rho(j,a)=(s(j),a+\eta_j).                                  \tag{2.6}
\]

Then the number of touched old physical components and the number of new
physical components are respectively

\[
 d=\sum_{C\in\operatorname{Cyc}(s)}
      \gcd\left(k,\sum_{j\in C}\eta_j\right),                \tag{2.7}
\]

\[
 f=\sum_{C\in\operatorname{Cyc}(ts)}
      \gcd\left(k,
        \sum_{j\in C}(\eta_j+\delta_{s(j)})\right).           \tag{2.8}
\]

Thus the new total is `c(F)-d+f`.  Voltage alone determines lift
multiplicity, not fusion; the product `pi rho` is decisive.

## 3. Exact preservation gates

Every allowed fixed-`M0` edge has immutable short-deck labels.  For a deck
`a`, let `lambda^a_P(z)` be the load of colour `z` in `P`.  If a packet of
alternating cycles removes edge multiset `E^-` and adds `E^+`, its exact
load derivative is

\[
 \Delta^a(z)=
 |\{e\in E^+:a(e)=z\}|-|\{e\in E^-:a(e)=z\}|.                \tag{3.1}
\]

The packet preserves deck completeness if and only if

\[
             \lambda^a_P(z)+\Delta^a(z)\ge1                 \tag{3.2}
\]

for every protected colour and every protected short deck.  This is exact
for disconnected packets as well as one alternating cycle.

Residence and longer flags are chronological.  Their effects are not
determined by (3.1).  Cutting at the marked ports preserves every old path
fragment literally; only boundary-crossing intervals change.  Therefore an
exact fragment summary consists of:

* the prefix and suffix of length at most the largest fixed window;
* the internal target counters at every protected depth;
* for residence, each coordinate's first/last bit, capped boundary run
  lengths, constant-word flag, and internal short-run flag.

These summaries compose associatively.  For arbitrary-width upper intervals,
the exact first-arrival oracle records, for every start, the union whenever
a previously absent coordinate first appears.  Applying the same oracle to
complements gives arbitrary-width lower intersections.  Thus (3.2), the
fragment summaries, and the final full physical replay form a fail-closed
integral test.  No signed or fractional relaxation is used below.

## 4. The audited `k=15` chain

The source is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    u2u3l3_s801.engine.json
SHA-256 886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83
```

The four replayed stages are:

| stage | candidate SHA-256 | physical component lengths |
|---|---|---|
| `F_0` | `886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83` | `1890,774^5,555,75,45` |
| `F_1` | `8e1af84ce459f825f6c4f41fcb8dce00bc40d8b40c1515dfef4741ac9668240d` | `5715,600,75,45` |
| `F_2` | `ad4cada7a193acaf275349ec90ab264178cb9106277b29e5a3d38c4b658e5b3d` | `5790,600,45` |
| `F_3` | `0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555` | `6390,45` |

In the fixed orientation convention used by the new verifier, their
quotient `(length,voltage,lift-count)` rows are

```text
F0: (258,10,5), (126,4,1), (37,1,1), (5,11,1), (3,4,1)
F1: (381,11,1), (40,4,1), (5,11,1), (3,4,1)
F2: (386, 7,1), (40,4,1), (3,4,1)
F3: (426,11,1), (3,4,1).
```

Reversing a quotient circuit negates its voltage and does not change the
physical lift ledger.  This accounts for the opposite `5/10` convention in
some earlier audits.

The three connected alternating exchanges are:

| switch | support | quotient rows in cycle order | removed variables | added variables |
|---|---:|---|---|---|
| `F0 -> F1` | 4 | `2,39,145,85` | `18,274,1018,599` | `17,277,1016,597` |
| `F1 -> F2` | 6 | `89,311,148,144,178,113` | `626,2181,1041,1010,1248,795` | `628,2184,1038,1012,1249,793` |
| `F2 -> F3` | 4 | `7,50,175,105` | `53,351,1227,739` | `52,354,1226,736` |

For each switch,

\[
             \Delta^{\mathrm{upper} q1}=0,
             \qquad
             \Delta^{\mathrm{lower} q2}=0.                 \tag{4.1}
\]

Independent physical replay at every stage proves:

```text
minimum coordinate run                         4
residence bad/shortfall                      0/0
fixed lower q2 missing                         0
fixed lower q3 positive-degree missing         0
geodesic upper q2 missing                      0
arbitrary-width upper missing, every rank      0
bilateral interval holes, q=1,...,7             0
collision-floor excess                         9.
```

The permanent independent replay is

```text
scratch/audit_k15_pbbs_component_reduction_chain_20260729.py
SHA-256 802b4d81d6e5c44d9fd090e1f1be25cac2ae33fa8a953455762aed7d79e554f3

scratch/k15_fixed_matching_pbbs_resident_20260729/
    pbbs_component_reduction_chain.audit.json
SHA-256 cdd8bd2539e0bd5428e0762cecff9fe705e277db7c64588009de6fb03bbb8bec.
```

## 5. The exact two-boundary theorem

Let a lower-`q1`-rainbow factor on the rank-`r` layer have cycles
`C_1,...,C_c`.  Cut one edge in every cycle and join the opened paths by
`c-1` Johnson seams.  Let

\[
 R=\{\text{the }c\text{ deleted rank-}(r-1)\text{ colours}\},
\]

and let `Q` be the set of seam colours.  Because the old factor is rainbow,
the internal adjacent-intersection support of the resulting middle path is

\[
       \left(\binom{[k]}{r-1}\setminus R\right)\cup Q.       \tag{5.1}
\]

Hence the exact natural `q1` hole set is

\[
                         H=R\setminus Q.                     \tag{5.2}
\]

### Theorem 5.1 (boundary capacity and connectivity-free compilation)

Let `T` be the resulting linearly depth-`d`-resident Johnson path and let
`A` be a nonzero source word of length `W+d` satisfying `D^d A=T`.

1. Every rank-`r-1` target not already present as a middle-path edge colour
   must occur on one of the two global source boundary chains.
2. Each boundary chain contains at most one distinct rank-`r-1` target.
   Therefore

   \[
                           |H|\le2                            \tag{5.3}
   \]

   is necessary for a universal source word.
3. If the members of `H` admit an injection into the two boundary chains
   satisfying the exact endpoint containment/adjacent-union equations, then
   the missing `q1` colours are installed exactly.
4. If, in addition, the path is upper-complete and the complete lower
   compiler (including every high-boundary omission row) is feasible, then
   `T` compiles to a universal word.  No connected factor is required.

#### Proof

Any source interval of rank `r-1` has length at most `d`: an interval of
length at least `d+1` contains a full middle window of rank `r`.  Away from
the two global ends, the maximal envelope of a shorter interval is contained
in two consecutive middle states and hence in their rank-`r-1`
intersection.  Equality of ranks forces it to be that already-present edge
colour.  Only the two nested boundary chains escape this argument.  A nested
chain contains at most one distinct set of a fixed rank, proving the first
two assertions.  The third assertion is exactly the boundary pin equations;
the fourth is the middle/upper transfer identity

\[
                         D^{d+q}A=D^qT                         \tag{5.4}
\]

together with the exact lower compiler.  `square`

### Corollary 5.2 (two cycles are enough at the `q1` level)

For `c=2`, every residence-safe Johnson seam has boundary-absorbable natural
`q1` holes.

If the seam colour equals one deleted cut colour, place the other at its own
outer component endpoint.  If it equals neither, place the first component's
cut colour at the left outer source position and the second component's cut
colour at the right outer position.  The required endpoint equations hold
because the deleted cut facet and the retained incident factor facet are
distinct in a globally rainbow factor.

This is exactly the mechanism used by the optimal `k=15` word.  Its seam
colour `17017` equals neither deleted cut colour `18553,18033`; those two
colours occupy source positions `0` and `6437`.

## 6. Why `O(d)` components is not the right sufficient statement

The maximal depth-`d` erosion has `2d` high boundary positions across all
high ranks, but this does **not** give rank-`r-1` capacity `O(d)`.  At that
fixed rank, Theorem 5.1 gives capacity exactly two.

Consequently, if a `c`-component splice uses no seam colour from its deleted
palette, then `|H|=c`, and compilation is impossible as soon as `c>2`--even
when `c=O(d)`.  More generally the exact requirement is

\[
               |R\cap Q|\ge c-2,                            \tag{6.1}
\]

together with the endpoint SDR for the remaining colours.

Thus the implication

```text
component count O(d)  =>  boundary absorption
```

is false.  Either reduce to at most two components, or prove the stronger
palette statement (6.1).  The latter can make a many-component factor just
as usable as a connected factor.

## 7. The exact universal PBBS reduction gate

There is one useful nontrivial sufficient form which separates topology from
availability.

### Theorem 7.1 (ordered ternary fusion forest)

Let `F_0` have `c_0` components.  Suppose there is an ordered family of
integral alternating `C6` switches `e_1,...,e_t` such that, when `e_i` is
applied,

1. its three negative factor edges lie in three distinct current components;
2. its cut--join product has one cycle, so those components are replaced by
   one;
3. it preserves every protected deck, residence, and all-depth collar; and
4. every later switch remains literal and admissible after the earlier
   contractions.

Then

\[
                         c(F_t)=c_0-2t.                       \tag{7.1}
\]

In particular, an ordered loose ternary spanning tree reduces odd `c_0` to
one component, and an ordered loose ternary spanning forest with two trees
reduces even `c_0` to two components.  In the latter case the two-boundary
theorem applies without a parity-changing bridge.  Equivalently, a single
admissible two-way even-support merger followed by a ternary tree handles the
opposite parity endpoint.

#### Proof

At step `i`, Theorem 2.1 gives `c(rho)=3` and `c(pi rho)=1`, so the component count falls by
two.  The hypotheses retain the carrier class and allow induction.  A loose
ternary tree admits a leaf-edge order: each leaf hyperedge has two vertices
not used by the remaining tree and one attachment vertex, hence is a legal
three-to-one contraction in that order.  The two-tree statement is applied
componentwise.  `square`

This theorem is stronger than a scalar component-potential estimate, but its
availability hypothesis is precisely what is missing in general PBBS.  A
static list of algebraic `C6` table circuits is insufficient unless their
physical placements and all chronology collars survive the contraction
order.

Let `A(F)` be the family of all integral fixed-`M0` rematchings which retain
the protected short-deck loads, residence, and every required lower/upper
flag of a current PBBS-derived factor `F`.  For an exchange `pi in A(F)`,
let `rho_F(pi)` be its old-fragment return permutation.

Define the positive-cut property

\[
 \mathrm{PC}(F):\quad
 \exists\pi\in A(F)\quad
c(\pi\rho_F(\pi))<c(\rho_F(\pi)).                           \tag{7.2}
\]

**Quantifier correction (2026-07-29).**  Because `A(F)` here contains all
protected rematchings, not only one connected alternating circuit, (7.2) is
equivalent to saying that `F` is not a global component-count minimizer in
the fixed protected fibre.  Its all-state form above two components is
equivalent to existence of a protected at-most-two-component factor; it is
not a local-minimum theorem.  The genuinely local version restricts `pi` to
one nontrivial cycle.  Its exact ribbon criterion, a smallest nonloop generic
protected local minimum, and the additional extraction hypotheses are proved
in
`MATH_THEOREM_L_PBBS_PROTECTED_RIBBON_POSITIVE_CUT_AND_PACKET_LOCK_20260729.md`.

### Theorem 7.2 (conditional monotone PBBS descent)

If every reachable resident all-depth PBBS factor with more than two
components satisfies `PC(F)`, then repeated integral switches reach at most
two components while preserving every deck and residence.  At most
`c(F_0)-2` switches are needed if each step decreases the component count by
at least one.

#### Proof

Theorem 2.1 says that (7.2) decreases the integer component potential.
All defining carrier properties are retained by membership in `A(F)`.
Iteration must stop, and the hypothesis prevents stopping above two.
`square`

As written, this is an exact global-fibre criterion, not a local-minimum
theorem.  The genuinely local reduction replaces `A(F)` by the protected
one-cycle neighbours.  Neither version is a consequence of all-depth support
alone: support completeness says that every target has at least one witness,
whereas a local positive cut requires a component-crossing alternating
circuit whose deletions can all be compensated simultaneously and whose new
chronology passes every collar.

The existing PBBS theory proves neither (7.2) nor its failure.  In
particular:

* the literal signature-primitive `27`-cycle in canonical `KG(9,4)` refutes
  direct hexagon self-peeling, but it does not refute merge--reorder--split
  descent;
* the two-sided PBBS diamond calculus gives a minimum physical `C6` merger,
  but no theorem supplies the ordered fusion forest of Theorem 7.1 with all
  deeper collars;
* parity obstructs an all-`C6` route to one component in some dimensions,
  but it does not obstruct stopping at one or two components;
* no asymptotic PBBS family is known whose full admissible exchange fibre has
  a local minimum with more than `C d` components for every fixed `C`.

Therefore the universal assertion

\[
 \text{“every PBBS resident all-depth factor reduces to }O(d)\text{”}
                                                               \tag{7.3}
\]

remains open.  Claiming it from the `k=15` chain would reverse the
quantifiers.  What is now proved is the exact criterion (7.2), the complete
`k=15` realization, and the fact that even (7.3), if proved, needs (6.1) to
imply boundary absorption.

## 8. Sharp finite boundary at the final `k=15` state

The final two-cycle factor has quotient rows `(426,11)` and `(3,4)`.  Its
relative exchange digraph was enumerated exactly.

### 8.1 Connected alternating cycles through support eight

The raw/simple-cycle counts by support `1,...,8` are

```text
2, 4, 202, 363, 1793, 7932, 38769, 198004.
```

The deck-safe counts are

```text
0, 0, 69, 67, 243, 765, 2356, 8018.
```

All `11,518` deck-safe cycles fail the exact quotient-voltage `2 -> 1`
test.  None reaches the chronology replay.  Hence:

> No connected alternating exchange of quotient support at most eight joins
> the final two components while preserving the two immutable short decks.

This is a finite support theorem only.

### 8.2 Two-cycle packets and neutral routers

For packets of two row-disjoint alternating primitives, each of support at
most six, the exact pair census is

```text
pairs                                      52,998,660
row-overlap rejected                        3,243,896
component-interaction disconnected         46,751,201
summed-deck rejected                         3,003,555
summed-deck safe                                     8
topology rejected                                    8.
```

Thus this compound class also contains no merger.

There are `49` resident/all-depth-safe one-cycle routers through support
five; exactly `10` retain two components.  Every one of those ten routed
states was exhaustively tested through connected support six, with no
connected successor.  These negatives do not cover larger packets,
overlapping active-block rematchings, or nonmonotone routes.  They were
stopped once the independent two-cycle boundary compiler solved `k=15`.

The finite artifacts are bound into the permanent chain audit in Section 4.

## 9. Exact proved/conditional boundary

The following are proved.

1. The cut--join law (2.2) is exact for arbitrary integral rematchings.
2. The `k=15` fixed-PBBS fibre has the all-depth chain `9 -> 4 -> 3 -> 2`.
3. Connectedness is unnecessary whenever all unrecycled cut colours fit the
   exact two-boundary SDR and the full upper/lower compiler passes.
4. Every two-cycle lower-rainbow factor has automatic natural `q1` boundary
   absorption for any Johnson seam.
5. `O(d)` components alone do not imply boundary absorption; (6.1) is the
   exact missing palette condition.
6. The bounded final switch classes of Section 8 are empty.

The following remain unproved.

1. `PC(F)` for every resident all-depth PBBS factor above two components.
2. Any universal reduction to `O(d)`, two, or one components.
3. A PBBS counterexample to such an unrestricted reduction.

For coefficient-one compilation the right target is therefore not universal
Hamiltonization.  It is either

\[
                         c\le2,                              \tag{9.1}
\]

or the strictly more general seam condition

\[
                         |R\setminus Q|\le2                  \tag{9.2}
\]

plus the exact boundary CSP and full compiler.  The optimal `k=15`
certificate realizes (9.1) and uses both boundary channels.
