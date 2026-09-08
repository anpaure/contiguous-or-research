# The `d`-overlap removes every lower/middle cut casualty, and two protected paths duplicate the exact upper leave

**Date:** 2026-08-01  
**Status:** unconditional local deck-and-raw-q1 theorem.  For the complete-reversal
reset--return packet, a coefficient-one `d`-overlap has an exact leave of
two upper Ferrers triangles.  Two explicit phase-common Johnson paths with
`5d` owners cover that whole leave.  Their owners and immediate palettes
are simple and can be made disjoint from the opened packet by four permanent
marker coordinates.  This removes the local duplicate-witness obstruction.
The two raw paths are internally resident; completing all four clipped ends
requires a resource-simple four-collar realization (or certified ambient
continuations).  The note does **not** prove that the three protected paths
extend to one globally upper-complete carrier or that the final common
compiler is feasible.

## 1. Normal form and notation

Add a permanent set `H` of size `h` to the sharp reset--return source in
`MATH_THEOREM_RESET_RETURN_RAIL_LINEARIZATION_COLLATERAL_20260801.md`.
Write

\[
 \Omega=H\mathbin{\dot\cup}X\mathbin{\dot\cup}C
       \mathbin{\dot\cup}U\mathbin{\dot\cup}Y
       \mathbin{\dot\cup}\{\alpha,\delta\},                 \tag{1.1}
\]

where all four displayed letter banks have size `d`.  Then

\[
 r=h+2d+1,\qquad |\Omega|=h+4d+2,\qquad M=4d+2.             \tag{1.2}
\]

The maximal cyclic antecedent is

\[
 A_t=H\cup\{\delta\}\cup X[1,t]\cup C[t+1,d]
                 \quad(0\le t\le d),                       \tag{1.3}
\]

\[
 A_{d+j}=H\cup X\cup\{u_j\}
                 \quad(1\le j\le d),                       \tag{1.4}
\]

\[
 A_{2d+1+s}=H\cup\{\alpha\}\cup X[s+1,d]\cup C[1,s]
                 \quad(0\le s\le d),                       \tag{1.5}
\]

and

\[
 A_{3d+1+j}=H\cup C\cup\{y_j\}
                 \quad(1\le j\le d).                       \tag{1.6}
\]

Every source letter has rank `h+d+1=r-d`.  Let `T_i` be its cyclic
length-`d+1` unions, so the `T_i` are the `M` distinct rank-`r` owners of
the complete-reversal cycle.

## 2. The coefficient-one `d`-overlap

Instead of the bare linearization `A_0,...,A_(M-1)`, use

\[
 \widetilde A=
 (A_{M-d},\ldots,A_{M-1},A_0,A_1,\ldots,A_{M-1}).           \tag{2.1}
\]

This is not an `O(d)` appendage to an owner path.  A linear depth-`d`
factor with `M` owners necessarily has `M+d` source positions.  Formula
(2.1) uses precisely those `d` global boundary positions.

### Theorem 2.1 (coefficient-one overlap)

The length-`d+1` windows of `\widetilde A`, in order, are

\[
 T_{M-d},T_{M-d+1},\ldots,T_{M-1},T_0,T_1,\ldots,T_{M-d-1}.
                                                                    \tag{2.2}
\]

Thus every packet owner occurs exactly once and no owner is duplicated.
Every cyclic interval crossing `A_(M-1)|A_0` whose left suffix has at most
`d` source cells is also restored literally by the overlap.

#### Proof

Apply `D^d` to (2.1).  Its `M` windows are exactly the cyclic windows in
(2.2).  A crossing interval with `a<=d` left cells uses the corresponding
suffix inside the copied prefix and then continues into `A_0,A_1,...`.
\(\square\)

In particular, all ranks below `r` survive: a source interval of length at
least `d+1` contains a rank-`r` owner.  All rank-`r` values survive by
(2.2).  Hence any remaining leave is necessarily **upper**, not a lower
compiler casualty.

## 3. Exact two-triangle leave

Put

\[
 B_X=H\cup C\cup Y\cup\{\alpha,\delta\},
 \qquad B_U=\Omega\setminus U=B_X\cup X.                   \tag{3.1}
\]

For `0<=i<=j<=d-1`, define

\[
 Z^X_{i,j}=B_X\cup X[1,i]\cup X[j+2,d],                    \tag{3.2}
\]

and

\[
 Z^U_{i,j}=\Omega\setminus U[i+1,j+1].                    \tag{3.3}
\]

Empty initial or final pieces in (3.2) are omitted.

### Theorem 3.1 (exact overlap leave)

The exact deck difference is

\[
 \operatorname{Deck}_{\rm cyc}(A)
 \setminus \operatorname{Deck}(\widetilde A)
 =\{Z^X_{i,j}:0\le i\le j<d\}
  \mathbin{\dot\cup}
  \{Z^U_{i,j}:0\le i\le j<d\}.                            \tag{3.4}
\]

Each family has `binom(d+1,2)` members.  If `t=d+1-(j-i+1)`, their rank
histograms are

\[
 \begin{array}{c|c}
 \text{rank}&\text{multiplicity}\\ \hline
 r+t&t\\
 r+d+t&t
 \end{array}
 \qquad(1\le t\le d).                                    \tag{3.5}
\]

Thus the full leave has exactly

\[
                         d(d+1)                            \tag{3.6}
\]

upper targets and no target of rank at most `r`.

#### Proof

In the linear order (2.1), the four source blocks occur as

\[
        (\text{copied }B_4),B_1,B_2,B_3,B_4.               \tag{3.7}
\]

Any cyclic interval not copied by Theorem 2.1 starts before the last `d`
source cells and crosses the old cut.

If it starts in `B_3` and ends in `B_1`, its union contains `B_X`.  When
the two exposed `X` tails leave a nonempty middle gap, its value is exactly
(3.2).  When the tails meet, the value is `B_U`, which is the member of
(3.3) omitting all of `U`.

If it starts in `B_2` (allowing the boundary cases immediately before or
after `B_2`) and ends in `B_2`, it contains everything except one
contiguous, possibly empty, interval of the ordered `U` bank.  A nonempty
gap gives (3.3); an empty gap gives the full set.  Starting still earlier,
or ending still later, also gives the full set.  The full set has a linear
witness, so this exhausts the possible leave.

Conversely, every set in (3.2) contains both `alpha` and `delta` and no
`U` coordinate.  In the order (3.7), a linear interval containing both
`alpha` (from `B_3`) and `delta` (from `B_1`) must pass through `B_2`, and
therefore contains `U`.  So no set (3.2) has a linear witness.  The same
argument shows that a linear interval containing `alpha` and `delta` cannot
omit a nonempty subinterval of `U`; hence no set (3.3) has a linear witness.

For a missing gap of length `ell`, there are `d-ell+1=t` placements.
Equations (3.1)--(3.3) give the two ranks in (3.5).  This proves (3.4)--
(3.6). \(\square\)

The first row of (3.5) includes the previously guaranteed short residual
`t=1,...,d-1` and the width-`2d+1` row `t=d`.  The second row is the exact
long-interval contribution which the earlier cut-collateral note had only
censused.

## 4. A `2d`-owner bank for the `X`-gap triangle

Assume `h>=4`, and choose distinct markers

\[
                   \eta_1,\eta_2,\eta_3,\eta_4\in H.       \tag{4.1}
\]

Set

\[
 V_0=B_X\setminus\{\eta_1\},\qquad
 V_1=B_X\setminus\{\eta_2\}.                             \tag{4.2}
\]

For `0<=i,j<=d-1`, put

\[
 L_i=(V_0\setminus C[1,i])\cup X[1,i],                    \tag{4.3}
\]

\[
 R_j=(V_1\setminus Y[1,j])\cup X[d-j+1,d].                \tag{4.4}
\]

Consider the owner path

\[
 \mathcal P_X=(L_{d-1},L_{d-2},\ldots,L_0,
               R_0,R_1,\ldots,R_{d-1}).                  \tag{4.5}
\]

### Theorem 4.1 (`X`-gap bank)

`P_X` is a simple Johnson path on `2d` rank-`r` owners.  Its `2d-1`
lower-q1 colours are all different, and so are its `2d-1` upper-q1
colours.  For every `0<=i<=j<d`, the interval from `L_i` through the
central edge to `R_(d-j-1)` has owner union

\[
                 Z^X_{i,j}.                               \tag{4.6}
\]

#### Proof

Every step on the left exchanges `c_i` with `x_i`; the central step
exchanges `eta_2` with `eta_1`; every step on the right exchanges `y_j`
with `x_(d-j+1)`.  Hence all owners have rank `r` and the path is Johnson.

Every left edge misses `eta_1` and contains `eta_2`; every right edge has
the opposite signature.  The central lower colour misses both and its
upper colour contains both.  Within one side, the strict `X` prefix or
suffix distinguishes every edge.  This proves both q1 simplicity claims.

Finally `L_0 union R_0=B_X`.  All coordinates removed in (4.3)--(4.4)
are restored by this central pair.  Therefore the displayed interval union
is

\[
 B_X\cup X[1,i]\cup X[j+2,d]=Z^X_{i,j}.
\]

\(\square\)

## 5. A `3d`-owner bank for the `U`-gap triangle

Partition `B_U` as

\[
 B_U=Q\mathbin{\dot\cup}\mathcal L\mathbin{\dot\cup}\mathcal R,
                                                                    \tag{5.1}
\]

where

\[
 Q=(H\setminus\{\eta_3,\eta_4\})\cup C\cup\{\alpha,\delta\},
 \quad |Q|=r-d-1,                                           \tag{5.2}
\]

\[
 \mathcal L=(\eta_3,x_1,\ldots,x_d),\qquad
 \mathcal R=(y_1,\ldots,y_d,\eta_4).                       \tag{5.3}
\]

For `0<=s<=d+1`, let

\[
 M_s=Q\cup\mathcal R[1,s]\cup\mathcal L[s+1,d+1].         \tag{5.4}
\]

This is the standard length-`d+2` geodesic whose total union is `B_U`.
For `0<=i,j<=d-1`, put

\[
 P_i=(M_0\setminus C[1,i])\cup U[1,i],                     \tag{5.5}
\]

\[
 S_j=(M_{d+1}\setminus C[1,j])\cup U[d-j+1,d].             \tag{5.6}
\]

Use the owner path

\[
 \mathcal P_U=(P_{d-1},\ldots,P_1,M_0,M_1,\ldots,M_{d+1},
                S_1,\ldots,S_{d-1}).                       \tag{5.7}
\]

### Theorem 5.1 (`U`-gap bank)

`P_U` is a simple Johnson path on `3d` rank-`r` owners.  Its `3d-1`
lower-q1 colours are all different, and so are its `3d-1` upper-q1
colours.  For every `0<=i<=j<d`, the interval from `P_i` through the
complete middle geodesic to `S_(d-j-1)` has owner union

\[
                         Z^U_{i,j}.                         \tag{5.8}
\]

#### Proof

The middle path successively exchanges the ordered `L` labels for the
ordered `R` labels.  The two outer paths exchange `C` labels for the two
tails of `U`, so every step is Johnson.

Left outer q1 colours contain `eta_3` and miss `eta_4`; right outer colours
have the reverse signature.  Every outer upper colour, and every outer
lower colour except the first, is additionally distinguished by a nonempty
`U` prefix or suffix.  The first outer lower colour removes a `C` label,
whereas the neighbouring middle lower colour removes the first `L` or `R`
label.  The middle geodesic colours are simple by their ordered exchanged
labels.  Thus no q1 colour repeats.

The full middle geodesic has union `B_U`.  The removed `C` labels are
restored there, so the indicated interval union is

\[
 B_U\cup U[1,i]\cup U[j+2,d]
   =\Omega\setminus U[i+1,j+1].
\]

\(\square\)

## 6. Exact coefficient-one and q1 separation

The marker choice makes the two banks compatible with the packet at the
owner/q1 level.

### Theorem 6.1 (protected resource ledger)

The union of `P_X` and `P_U` has

\[
 \begin{array}{c|c}
 \text{resource}&\text{count}\\ \hline
 \text{owners}&5d\\
 \text{lower q1 colours}&5d-2\\
 \text{upper q1 colours}&5d-2\\
 \text{upper targets duplicated}&d(d+1).
 \end{array}                                                \tag{6.1}
\]

All owners in this ledger are different.  All lower-q1 colours are
different, and all upper-q1 colours are different.

Moreover:

1. every packet owner contains all of `H`, whereas every bank owner misses
   at least one marker, so no bank owner equals a packet owner;
2. every `P_X` owner contains `eta_3,eta_4` and misses `eta_1` or `eta_2`;
3. every `P_U` owner contains `eta_1,eta_2` and misses `eta_3` or `eta_4`;
4. the same signatures separate all lower-q1 colours of the two banks from
   each other and from the packet;
5. every bank upper-q1 colour is disjoint from the surviving opened-packet
   upper-q1 palette.  The only bank upper colour containing all four
   markers is `B_X`, and `B_X` is exactly the one upper-q1 colour at the
   opening edge omitted by the owner order (2.2).

#### Proof

Items 1--4 follow directly from (4.2)--(5.7).  For item 5, all upper
colours other than the central `V_0 union V_1=B_X` miss a marker and hence
cannot be a packet upper colour.  Applying the identity

\[
 \bigcup_{q=p}^{p+d+1}A_q=T_p\cup T_{p+1}                  \tag{6.2}
\]

at the cut in (2.2) shows that `B_X` is precisely the upper colour of the
omitted edge `T_(M-d-1) T_(M-d)`. \(\square\)

Thus the banks do not spend duplicate owner or immediate-palette resources.
They are a legitimate protected q1 subgraph, not merely a support-level
target list.

### Corollary 6.2 (sharp standalone protected lower-q1 footprint)

A path used inside a cyclic factor has two physical boundaries.  Therefore
an unconditional standalone embedding must give **both** ends of **both**
banks a `d`-root one-sided collar.  With the opened packet path, the three
protected pieces then contain

\[
 (M-1)+(9d-2)=13d-1                                      \tag{6.3}
\]

Johnson edges, hence exactly

\[
                         26d-2                             \tag{6.4}
\]

incidence edges in the middle-levels containment graph.  Their maximum
degree is two, and their owner and lower-q1 vertices are all distinct.
Therefore the fixed-protected-subgraph two-factor extension theorem applies
whenever

\[
                         m\ge26d.                          \tag{6.5}
\]

Conditional on choosing the four collars with collision-free filler runs,
simple q1 colours and legal continuation edges, it gives one spanning
owner/lower-q1 two-factor containing the opened packet and the complete
four-collared twin bank.  Because the banks are static, this protected
factor is phase-common.  Without that collar realization, the unconditional
raw protected forest has `9d+2` owners, `9d-1` Johnson edges and `18d-2`
incidence edges, so `m>=18d` closes only its owner/lower-q1 projection.

If a later global construction proves that `P_X` is the left endpoint path
and `P_U` the right endpoint path, or supplies two certified nested ambient
continuations, the two exterior collars are unnecessary.  That conditional
layout uses `7d` bank owners, `22d-2` total incidence edges and the weaker
threshold `m>=22d`.  It must not be called an unconditional cyclic host.

This corollary is deliberately limited to the owner/lower-q1 incidence
factor.  It does not assert upper-q1 surjectivity, few components, or any
deeper upper/compiler property.

## 7. Residence and literal source intervals

The raw owner paths already have the correct internal residence property.

### Lemma 7.1 (clipped residence)

Every positive coordinate run in `P_X` or `P_U` which meets neither path
boundary has length at least `d+1`.

#### Proof

In `P_X`, an `X` coordinate has one run meeting the left boundary and one
meeting the right boundary.  A deleted `C` coordinate enters on the left
and then persists to the right boundary; a deleted `Y` coordinate starts at
the left boundary and exits on the right.  The two markers have the same
one-sided form.  Hence there is no short internal run.

In `P_U`, every `U` coordinate again has two boundary runs.  A reused
deletion coordinate `c_j` enters on the left and exits on the right; its
internal positive run has length

\[
                         d+2j\ge d+2.                       \tag{7.1}
\]

The `L` and `R` mobile labels have boundary runs, and all other labels are
constant. \(\square\)

When these paths are placed internally, their clipped boundary runs need
collars on **all four path ends**.  Two representative deficiency profiles
are:

* at the right boundary of `P_X`, `eta_1` needs one more owner and `x_s`
  needs `d+2-s` more owners for `2<=s<=d`;
* at the left boundary of `P_U`, `eta_3` needs one preceding owner and
  `u_j` needs `j+1` preceding owners for `1<=j<d`.

The opposite-end profiles are the reflected versions.  At every collar
depth at most `d` coordinates are mandatory.  A one-exchange Ferrers collar
of `d` roots has the correct residence profile on each side: at step `t`,
retain the mandatory superlevel set, drop one expired flag, and insert one
filler which persists toward the exterior host.  Since `r-d>=d+1`, there is
always at least one nonmandatory exchange position.  This proves the
residence schedule, but collision-free filler runs, simple q1 colours and
legal continuation edges must be checked jointly for all four collars in
the ambient host.  When that resource-simple realization is available,
four standalone collars add at most

\[
                    4d\text{ owners and }4d\text{ joins}.   \tag{7.2}
\]

and the standalone collared duplicate bank uses at most `9d` protected
owners.  If two path ends are certified global endpoints or have nested
ambient continuations, two collars can be suppressed and the count drops
conditionally to `7d`.  In either case the candidate protected incidence
ledger is `O(d)`, not `O(d^2)`; only the raw `5d`-owner bank is unconditional
in this note.

Once the banks occur in one resident owner chronology `T`, maximal erosion
gives a nonempty depth-`d` antecedent.  For every consecutive owner interval,

\[
 \bigcup_{q=i}^{j}T_q=\bigcup_{q=i}^{j+d}A_q,               \tag{7.3}
\]

so (4.6) and (5.8) are literal source-interval witnesses, not merely
owner-level shadows.

## 8. Phase commonality

The second reset phase reverses the cyclic source and uses the mirrored
opening.  Equations (3.2)--(3.3) range over **all** nonempty contiguous gaps
of `X` and `U`, so each family is invariant under this reversal.  The two
duplicate banks can therefore remain fixed while the packet trades phase.

This is stronger than giving each phase a separately chosen upper repair:
the owner list, q1 resources, residence collars, and all `d(d+1)` duplicate
witnesses are phase-common.

## 9. H100 audit

The independent C++ audit

```text
scratch/audit_reset_return_upper_ferrers_twin_bank_20260801.cpp
```

constructs the literal packet source and both banks, checks the exact deck
difference (3.4), enumerates every target witness, checks all owner and q1
collisions including the opened packet, and checks all internal positive
runs.  Compiled on H100 with `g++ -std=c++20 -O3`, it passes for
`2<=d<=40`:

```text
PASS_RESET_RETURN_UPPER_FERRERS_TWIN_BANK d=2..40
```

Retained hashes:

```text
cpp  dddaa7446d5fc40f313a1dd0ed98ed4bfdcff29fca589d725383082a8bd8f686
out  ed9ebebf72e4caaa5c5a1bdef73e7719ae624576cfd36eb57fadb01212932e05
```

## 10. Exact remaining global lemma

The local linearization obstruction is now closed:

\[
 \boxed{
 \begin{array}{c}
 d\text{-overlap: every owner exactly once, no lower/middle leave};\\
 \text{exact leave: two upper Ferrers triangles};\\
 \text{two internally resident paths: every leave target duplicated with}\
 \text{simple, coefficient-one owner/q1 resources.}
 \end{array}}
                                                               \tag{10.1}
\]

The remaining statement is global rather than local.

> **Protected twin-bank host lemma.**  Embed the opened reset packet and
> the two collared banks in one coefficient-one carrier, join their path
> components, preserve all exterior arbitrary-width witnesses, and leave a
> terminal common compiler of `O(1)` deficiency.

At the owner/lower-q1 level the protected object has only `O(d)` incidence
edges, so the existing fixed-protected-subgraph two-factor extension theorem
applies for all sufficiently large dimensions.  That theorem does not by
itself give upper-q1 surjectivity, arbitrary-width upper completion,
component joining, or the common compiler.  Those four correlated rows must
not be inferred from the present local construction.

In particular, this note proves neither `nu(k)<=B(k)+O(1)` nor the existence
of the global phase-common host.  It proves that the former quadratic
cut-collateral family is no longer an obstruction requiring `O(k)` appended
letters: it can be absorbed by `O(d)` protected owner positions already
inside the ambient coefficient-one carrier.
