# The top lower-shadow Hall gate is frozen by every current coatom packet

Date: 2026-08-01  
Status: exact all-`d` candidate theorem and exact Hall-deficiency formula.
This refutes an unconditional `O(1)` transparent-linkage conclusion from the
enlarged endpoint-planted/adjacent-order packet catalogue alone.  It does
not show that the recursively prepared carriers have large top deficiency.

## 0. Outcome

The reflected pair-degree invariant is not a terminal compiler obstruction,
and the adjacent-order packets can break it anyway.  The first genuinely
frozen compiler gate occurs one level higher and is simpler:

> every current zero-owner packet preserves the complete immediate lower
> palette and both global endpoints.

For a rank-`r` Johnson carrier `T`, a missing rank-`r-1` natural target has
no internal compiler cap.  It can be installed only in the `d` repeated
left endpoint caps, the `d` repeated right endpoint caps, or both.  This
gives an exact two-bank Hall problem.

The resulting deficiency is invariant under the canonical coatom moves,
all endpoint-planted variants, and all adjacent-order reflection breakers.
Therefore those packets do **not** imply an `O(1)` terminal Hall bound in an
arbitrary safe fibre.  A recursive theorem must first guarantee an
endpoint-absorbable q1 deficit of `O(1)` (or introduce a packet which changes
q1/endpoints).

The exact optima `k=11,13,15` pass this gate with deficiency zero.  Their
one/two natural q1 holes are precisely endpoint facets.

## 1. Setup

Let

\[
 T=(T_0,\ldots,T_{W-1})
\]

be a simple rank-`r` Johnson path with a nonzero depth-`d` factor.  Let

\[
 P_j=\bigcap_{\max(0,j-d)\le i\le\min(j,W-1)}T_i
\]

be its maximal erosion, and let

\[
 \widehat P_{h,s}=P_s\cup\cdots\cup P_{s+h},qquad 0\le h<d,
                                                                    \tag{1.1}
\]

be the maximal cap of the physical short cell `(h,s)`.

Write

\[
 \mathcal J_1(T)=\{T_i\cap T_{i+1}:0\le i<W-1\}             \tag{1.2}
\]

for the support of the immediate natural lower palette, and put

\[
 \mathcal H_1(T)={ [k]\choose r-1}\setminus\mathcal J_1(T). \tag{1.3}
\]

These are the natural q1 holes.

## 2. Exact candidate theorem

### Theorem 2.1 (only repeated endpoint caps can pay a q1 hole)

For `Q in H_1(T)`, the complete set of physical short-cell caps containing
`Q` is

\[
\begin{aligned}
 \mathcal N_T(Q)={}&
 \{(h,0):0\le h<d,\ Q\subseteq T_0\}\\
 &\mathbin\cup
 \{(h,W+d-h-1):0\le h<d,\ Q\subseteq T_{W-1}\}.             \tag{2.1}
\end{aligned}
\]

Every left candidate cap in (2.1) is literally `T_0`, and every right
candidate cap is literally `T_(W-1)`.

#### Proof

Put `q=d-h`.  An interior start `q<=s<=W-1` has cap

\[
 \widehat P_{h,s}=T_{s-q}\cap\cdots\cap T_s.                 \tag{2.2}
\]

If `q=1`, this is a member of `J_1(T)` and cannot equal the missing
rank-`r-1` target `Q`.  For any `q>=2`, the cap in (2.2) is contained in
the adjacent intersection

\[
                  T_{s-q}\cap T_{s-q+1}.                    \tag{2.2a}
\]

If it contained `Q`, then `Q` would be contained in (2.2a).  Both have
rank `r-1`, because consecutive distinct rank-`r` Johnson owners meet in
rank `r-1`.  Hence equality would hold and `Q` would belong to `J_1(T)`,
again contradicting (1.3).  Notice that a deeper intersection need not
itself have rank at most `r-2`; the adjacent-palette contradiction is the
required argument.

At the left boundary, `s=0` gives

\[
 \widehat P_{h,0}=T_0,                                      \tag{2.3}
\]

because `P_0=T_0` and every other summand is contained in `T_0`.  If
`1<=s<q`, the whole cell lies in both first carrier windows, so

\[
 \widehat P_{h,s}\subseteq T_0\cap T_1.                     \tag{2.4}
\]

The right side has rank `r-1`; if it contained `Q`, equality would force
\(Q=T_0\cap T_1\), contradicting (1.3).  The right boundary is the
reversal of the same argument.  This proves (2.1).  \(\square\)

The theorem is stronger than the scalar statement “there are boundary
cells.”  All missing top targets on one shore see the **same** `d` physical
addresses.

## 3. Exact two-bank Hall deficiency

Partition `H_1(T)` into four classes:

\[
\begin{array}{c|c}
Z&Q\not\subseteq T_0,\ Q\not\subseteq T_{W-1},\\
L&Q\subseteq T_0,\ Q\not\subseteq T_{W-1},\\
R&Q\not\subseteq T_0,\ Q\subseteq T_{W-1},\\
B&Q\subseteq T_0,\ Q\subseteq T_{W-1}.
\end{array}                                                   \tag{3.1}
\]

Write their cardinalities as `z,ell,rho,b`.  Let

\[
 u_L=\min(\ell,d),\qquad u_R=\min(\rho,d).                   \tag{3.2}
\]

### Theorem 3.1 (top-shadow boundary-bank formula)

The maximum number of q1 holes which can even be assigned distinct physical
caps is

\[
             u_L+u_R+\min\{b,2d-u_L-u_R\}.                   \tag{3.3}
\]

Consequently every compiler satisfies

\[
 \boxed{
 \lambda_d(T)\ge
 \delta_{\rm top}(T):=
 z+\ell+\rho+b-u_L-u_R-\min\{b,2d-u_L-u_R\}.}                \tag{3.4}
\]

#### Proof

By Theorem 2.1, every `L` target is adjacent to all `d` left addresses and
no right address; every `R` target has the reverse list; every `B` target is
adjacent to both banks; and every `Z` target is isolated.  First match as
many one-shore targets as possible, using `u_L,u_R` slots.  The both-shore
targets then see every remaining slot.  This gives (3.3), and no matching
can do better by the two single-bank capacity cuts.  Every realized target
needs a distinct witness interval, so the unmatched count lower-bounds
`lambda_d(T)`.  \(\square\)

Common-`Q` compatibility can only increase the true compiler deletion
number.  Formula (3.4) is the exact deficiency of the **cap candidate
graph**, not an assertion of sufficiency.

## 4. The enlarged packet catalogue cannot change this gate

### Theorem 4.1 (frozen top-shadow deficiency)

Suppose a safe packet replacement preserves

1. the two global carrier endpoints; and
2. the immediate lower-palette multiset

\[
       \{\!\{T_i\cap T_{i+1}\}\!\}.
\]

Then it preserves `H_1(T)`, the four classes (3.1), and
`delta_top(T)` exactly.

#### Proof

The palette multiset determines its support and hence (1.3).  The fixed
endpoints determine the two containment predicates in (3.1).  Formula (3.4)
then has no changing term.  \(\square\)

Every authenticated mixed-coatom packet has precisely these two
properties.  Reordering coatoms inside one active block—including every
adjacent-order reflection breaker—changes neither its endpoint owners nor
the old/new q1 palette equality.  Endpoint planting changes how a packet is
available, not what the safe replacement preserves.  Hence the entire
current enlarged catalogue leaves `delta_top` fixed.

### Corollary 4.2 (no arbitrary-fibre `O(1)` deduction)

The endpoint-planted/adjacent-order catalogue alone cannot prove

\[
                    \lambda_d(T_{\rm terminal})=O(1)
\]

from an arbitrary starting safe carrier.  At minimum, the recursive input
must satisfy

\[
                         \delta_{\rm top}(T)=O(1),             \tag{4.1}
\]

because every reachable carrier has the same lower bound.

This is a quantifier obstruction: it does not assert that the intended
Pascal carrier has large `delta_top`.  It says the local packet catalogue
cannot manufacture the required bound if the input does not already have
it.

### Proposition 4.3 (the maximal-erosion linkage graph is never enough)

Take the maximal erosion itself as the base antecedent, `C=P`, with no
protected pins.  Then every target of rank below `r-d` is isolated in the
transparent singleton cap-linkage graph.  Consequently its Hall deficiency
is at least

\[
                   \sum_{s=1}^{r-d-1}\binom{k}{s}.             \tag{4.2}
\]

#### Proof

Every maximal erosion letter is an intersection of at most `d+1`
rank-`r` vertices along a Johnson path, hence has rank at least `r-d`.
An expansion edge from target `S` to position `p` requires
`P_p subseteq S`.  No target of smaller rank satisfies this at any position.
All such target vertices are therefore isolated.  \(\square\)

For the exact zero-deletion carriers this lower bound is already

```text
k=11: 66
k=13: 377
k=15: 1940.
```

Yet their true `lambda_3` is zero.  Thus the transparent cap-linkage theorem
needs a **pre-carved base antecedent**; it cannot be applied uniformly from
the canonical maximal word.  The endpoint-planted packet catalogue supplies
carrier motion but, as currently certified, supplies no such common carving
or U5 cell list.  Adjacent-order freedom does not fix this quantifier.

## 5. Exact calibration

| `k` | q1 holes | endpoint classes `(z,ell,rho,b)` | `delta_top` |
|---:|:---|:---:|---:|
| 11 | `{155}` | `(0,0,0,1)` | 0 |
| 13 | `{2135}` | `(0,0,1,0)` | 0 |
| 15 | `{18553,18033}` | `(0,1,1,0)` | 0 |

The full candidate lists are exactly:

```text
k=11: 155 -> three left + three right endpoint caps;
k=13: 2135 -> three right endpoint caps;
k=15: 18553 -> three left, 18033 -> three right endpoint caps.
```

Thus the finite exact compilers satisfy not merely `H<=2`; they satisfy the
precise two-bank Hall condition which the all-`d` theorem identifies.

## 6. Consequence for the `B+O(1)` programme

There are now two separate conclusions.

1. **Below q1:** reflected pair-degree invariants do not constrain the
   compiler directly, cap capacity uses the symmetric rather than difference
   mode, and adjacent-order packets span the missing quadratic currents.
2. **At q1:** the support and endpoint bank are frozen by every current
   packet.  This is a real immutable Hall gate.

Therefore the next recursive theorem must export an endpoint-absorbable q1
palette with bounded two-bank deficiency.  Once that is included in the
sidecar, the serial coatom route may focus on the genuinely movable q2 and
deeper common-`Q` conflicts.  Without it, no amount of adjacent-order
reflection breaking can prove bounded terminal deletion.

## 7. Replay

Run

```text
python3 scratch/audit_top_shadow_frozen_boundary_hall_20260801.py
```

which writes

```text
scratch/top_shadow_frozen_boundary_hall_20260801.audit.json
```

with expected status

```text
PASS_TOP_SHADOW_FROZEN_BOUNDARY_HALL
```

No all-`k` q1-sidecar theorem or bounded terminal compiler theorem is
claimed.
