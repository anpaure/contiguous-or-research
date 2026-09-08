# Gate C: an exact fourfold middle resolution by three-rank-disjoint banks

**Status (2026-08-22).**  Every assertion below is proved.  The polynomial
forbidden-difference theorem and the Hamming-coset resolution can be made
simultaneous.  For every fixed perfect pairing and cyclic pair order, there
is a binary linear code of codimension `O(log b)` such that:

1. every coset is a bank of coherent tours jointly target-disjoint at ranks
   `b-1`, `b`, and `b+1`; and
2. over all coset banks, every defect-one middle target occurs in exactly
   four banks.

Thus one fixed pairing has an exact integral fourfold middle resolution
into locally three-rank-compatible banks of size `2^b/poly(b)`.  The
remaining central three-rank selection step is cross-pairing: choose banks
from exponentially many pairings without collisions.  All-offset control
and SCD extension remain additional requirements.

Let `b>=3` be odd.  Fix a pairing `P={P_0,...,P_(b-1)}` in one directed
cyclic order, and parameterize its coherent tours by initial states
`x in F_2^b`.  Put

\[
 q=b(b-1),\qquad
 M_b=2b^3+8b^2-16b.                                    \tag{0.1}
\]

## 1. The collision Cayley set

Let `B subseteq F_2^b\setminus{0}` consist of the differences `h=x+x'` for
which the tours `T(x),T(x')` share at least one attached target at one of
the ranks `b-1,b,b+1`.  Target membership is affine in the initial state,
so this condition depends only on `h`, not on the chosen base state `x`.

The pair-occupancy signature audit gives

\[
\begin{array}{c|c|c}
\text{rank class}&\text{compatible ordered index pairs}&
 \text{possible differences per pair}\\ \hline
b-1&b(b-1)^2&2\\
b&b(b-1)&4\\
b+1\text{ internal}&b(b-2)&8\\
b+1\text{ boundary}&b&2.
\end{array}                                             \tag{1.1}
\]

Indeed equality first forces the same empty/doubled-pair signature.  It
then fixes `h` on every split pair, leaving respectively one, two, three,
or one exceptional state bits free.  Hence

\[
                         |\mathcal B|\le M_b.           \tag{1.2}
\]

The middle-rank part of `B` contains every vector of Hamming weight one or
two: two fixed-order tours share a middle target exactly when their state
difference is supported on its empty and doubled pair.  This observation
will make the fourfold multiplicity below literal.

## 2. A low-codimension kernel avoiding every collision

Define

\[
 r_b=\min\left\{b,\left\lceil\log_2(2M_b)\right\rceil\right\}.    \tag{2.1}
\]

### Lemma 2.1 (linear separation)

There is a linear map

\[
                         A:\mathbb F_2^b\longrightarrow\mathbb F_2^{r_b} \tag{2.2}
\]

such that

\[
                         \ker A\cap\mathcal B=\varnothing.        \tag{2.3}
\]

#### Proof

If `r_b=b`, take the identity.  Otherwise choose the `r_b` rows of `A`
independently and uniformly from `F_2^b`.  For every fixed nonzero `h`,

\[
                         \Pr(Ah=0)=2^{-r_b}.            \tag{2.4}
\]

The union bound and (1.2) give

\[
 \Pr(\ker A\cap\mathcal B\ne\varnothing)
 \le |\mathcal B|2^{-r_b}\le {1\over2}<1.              \tag{2.5}
\]

Thus a desired map exists. \(\square\)

Let `C=ker A`.  Since `rank(A)<=r_b`,

\[
                         |\mathcal C|\ge2^{b-r_b}
                         \ge {2^b\over4M_b}.            \tag{2.6}
\]

The last inequality is immediate when `r_b<b` from
`2^(r_b)<4M_b`; when `r_b=b` its right side is at most one.

### Theorem 2.2 (every coset is three-rank-disjoint)

For every coset `z+C`, the tours

\[
                         \{\mathcal T(x):x\in z+\mathcal C\}      \tag{2.7}
\]

are jointly target-disjoint at ranks `b-1,b,b+1`, and the bank contains at
least `2^(b-r_b)` tours.

#### Proof

The difference of two distinct states in one coset is a nonzero member of
`C`.  By (2.3) it is not a collision difference, so the two tours share no
target at any of the three ranks.  Targets are already distinct within one
coherent tour.  Equation (2.6) gives the size. \(\square\)

## 3. Exact coset multiplicities

Fix a defect-one middle target.  Its ordered empty and doubled pairs are
unique, say `(P_t,P_i)`.  Its split choices determine all initial-state
bits outside `{t,i}`, so its four preimage states form

\[
                         x_0+\{0,e_t,e_i,e_t+e_i\}.      \tag{3.1}
\]

No difference between two of these states lies in `C`: every such
difference has weight one or two and therefore belongs to `B`.  The four
states consequently lie in four distinct cosets of `C`.

### Theorem 3.1 (exact fourfold middle resolution)

The coset banks of `C` form an exact fourfold resolution of the fixed-
pairing defect-one middle stratum:

\[
 \boxed{\sum_{Z\in\mathbb F_2^b/\mathcal C}
       \mathbf1_{\{T\text{ occurs in bank }Z\}}=4}      \tag{3.2}
\]

for every defect-one target `T`.  Every bank in this resolution is already
three-rank-disjoint by Theorem 2.2.

#### Proof

The four states in (3.1) are all the preimages of `T`, and the preceding
paragraph puts them in four distinct cosets.  A bank contains at most one
of them and hence contains `T` once or not at all.  This proves (3.2).
\(\square\)

There are also exact adjacent-rank multiplicities.  A lower target in the
fixed-pairing stratum has one empty pair and splits all others.  For each of
the `b-1` packet columns its split choices fix all state bits except the
empty-pair bit, giving `2(b-1)` state-index preimages.  Since a coset bank is
lower-rank-disjoint, these lie in `2(b-1)` distinct cosets.  Thus the lower
stratum is resolved exactly `2(b-1)` times.

For upper targets, every accessible internal signature (one empty and two
consecutive doubled pairs) has eight preimage states, while every packet-
boundary signature (no empty and one doubled pair) has two.  The same
within-bank disjointness puts these preimages in respectively eight and two
distinct cosets.  Hence the coset family has exact, signaturewise adjacent
loads as well as the fourfold middle load.

## 4. Scope

The theorem removes three local concerns at once: exponentially many
pairing states are grouped into polynomial-loss banks; each bank is a
genuine three-rank partial factor; and the entire fixed-pairing middle
stratum has an exact constant-fold bank resolution.

It does not make banks belonging to different perfect pairings disjoint.
A near-global construction must choose from
`Omega(2^b/b^(5/2))` pairings, and their defect-one strata overlap.  Nor do
the three controlled ranks imply literal coverage at every offset or
automatic extension to a full SCD.  These are the remaining global gates.

The companion checker
`scratch/verify_gate_c_three_rank_linear_coset_resolution_20260822.py`
constructs the exact collision set for small `b`, searches a separating
linear map, and verifies three-rank disjointness and fourfold middle
multiplicity for every coset.
