# A three-ring has a clipped-resident upper-cone reservoir and all-width transparency

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional protected-bank construction.  For the complete
common-history three-ring, every potentially damaged upper target has a
pairwise owner/lower-q1/upper-q1-disjoint clipped-resident witness path; the
three seam-base witnesses are the ring hinges themselves.  Consequently the
zero-cost ring rethread preserves the complete strict-lower deck and the
complete arbitrary-width upper deck once this joint bank is planted in an
ambient carrier which was upper-complete before the rethread.  The remaining
premise is joint extension of the bank to the required global
factor/cap/regenerative state.

## 0. Parameters and the three upper cones

Work in `ML_m` on `[2m-1]`, let

\[
 d=O(\sqrt m),\qquad d\longrightarrow\infty,
\]

and take the complete common-history three-ring with

\[
 |B|=m-2,qquad K=B\cup\{b\},qquad
 E=[2m-1]\setminus K,qquad |E|=m.
\tag{0.1}
\]

Choose distinct `a_0,a_1,a_2 in E`, cyclically indexed, and put

\[
 L_i=K\cup\{a_i\},qquad
 R_i=B\cup\{a_{i-1},a_i\},qquad
 I_i=B\cup\{a_i\},
\tag{0.2}
\]

\[
 U_i=K\cup\{a_{i-1},a_i\}.
\tag{0.3}
\]

The old hinge is `L_i-I_i-R_i`; the new hinge is
`L_i-I_i-R_(i+1)`.  Let

\[
 \mathcal D_3=
 \left\{K\cup T:\varnothing\ne T\subsetneq E,
  \ \{a_{i-1},a_i\}\subseteq T\text{ for some }i\right\}.
\tag{0.4}
\]

The common-history upper-damage theorem says that every old upper target
which could lose its selected crossing witness under the rethread belongs
to `mathcal D_3`; the full-ground target is automatic and has been removed.

## 1. The three seam bases need no duplicate witness

### Lemma 1.1

The three ring hinges are pairwise resource-disjoint Johnson paths and

\[
                       L_i\cup R_i=U_i.
\tag{1.1}
\]

Under the cyclic rethread their upper-q1 values are permuted
`U_i -> U_(i+1)`.  Hence every rank-`m+1` seam base already has a surviving
literal occurrence; no auxiliary path is required for the three traces of
size two.

#### Proof

The owner, lower-colour, and upper-colour simplicity is the common-history
ring theorem.  Equation (1.1) is literal, and the new union at role `i` is
`U_(i+1)`. \(\square\)

## 2. Low traces: deterministic shortened paths

Fix a trace `T subset E` represented in `mathcal D_3`, put

\[
 q=|T|,qquad h=m-q,
\]

and suppose

\[
                         3\le q\le m-d-1.
\tag{2.1}
\]

Choose a linear presentation

\[
                         K=(k_0,\ldots,k_{m-2})
\]

(it may depend on `T`) and, for `0<=j<q`, put

\[
 W_{T,j}=\{k_j,k_{j+1},\ldots,k_{j+h-1}\},
 \qquad V_{T,j}=T\cup W_{T,j}.
\tag{2.2}
\]

There is no wrap because `(q-1)+(h-1)=m-2`.

### Lemma 2.1 (private clipped path)

The word

\[
                         \mathcal Q_T=(V_{T,0},\ldots,V_{T,q-1})
\tag{2.3}
\]

is a simple rank-`m` Johnson path with union `K union T`.  Its owners,
immediate lower colours, and immediate upper colours all have exact external
trace `T`; they are simple inside the path.  The path is `d`-clipped
resident.

#### Proof

Every owner has size `q+h=m`.  Successive windows delete `k_j` and insert
`k_(j+h)`.  Their lower and upper colours are

\[
 T\cup\{k_{j+1},\ldots,k_{j+h-1}\},
 \qquad
 T\cup\{k_j,\ldots,k_{j+h}\},
\]

so starting positions make both palettes simple and their external trace is
exactly `T`.  The union of the `q` consecutive `h`-windows is all of `K`.
Finally every internal positive run of a `K` coordinate has length `h`, and
`h>=d+1`; all `T` coordinates occur throughout. \(\square\)

Different traces give disjoint owner and immediate-palette resources.
They are also disjoint from the ring resources.  Indeed, intersection with
`E` gives exact trace `T` on every owner and both immediate palettes of a
low path, whereas the ring owners and lower colours have external trace of
size one or two and the ring upper colours have one of the three size-two
seam traces.

## 3. High traces: one simultaneous symmetric packing

It remains to treat

\[
 q=m-h,qquad 1\le h\le d.
\tag{3.1}
\]

There are at most

\[
                         H_d=\sum_{h=1}^d\binom mh=2^{o(m)}
\tag{3.2}
\]

such traces, even before imposing the three-edge condition in (0.4).

For `Z=K union T`, choose a symmetric monotone Johnson geodesic inside `Z`
as follows.  Put `N=|Z|=2m-h-1`, choose

\[
 Z=C\mathbin{\dot\cup}X\mathbin{\dot\cup}Y,qquad
 |C|=h+1,qquad |X|=|Y|=q-1,
\]

and orders `X=(x_1,...,x_(q-1))`, `Y=(y_1,...,y_(q-1))`.  Let

\[
 A_t=C\cup\{x_{t+1},\ldots,x_{q-1}\}
       \cup\{y_1,\ldots,y_t\},qquad0\le t<q.
\tag{3.3}
\]

This path has union `Z` and no internal positive coordinate run.

### Lemma 3.1 (simultaneous high-tail packing)

For all sufficiently large `m`, one may choose the paths (3.3) for every
high trace so that all their owners, immediate lower colours, and immediate
upper colours are pairwise distinct and avoid every ring and low-trace
resource.

#### Proof

Under the uniform symmetric choice of `C,X,Y`, a fixed contained owner,
lower colour, or upper colour is hit with probability respectively

\[
 {q\over\binom Nm},\qquad
 {q-1\over\binom N{m-1}},\qquad
 {q-1\over\binom N{m+1}}.
\tag{3.4}
\]

Uniformly for `h<=d=O(sqrt m)`, all three denominators are
`2^(2m-o(m))`.  Before choosing one high path, the combined ring, low, and
earlier-high bank forbids at most

\[
                         O\bigl(m(2^m+H_d)\bigr)
\tag{3.5}
\]

resources of each rank.  The union bound for (3.4) is therefore

\[
 {2^{m+o(m)}\over2^{2m-o(m)}}<1.
\]

A legal choice exists at every greedy step. \(\square\)

## 4. The complete protected reservoir

Let `P_3` be the incidence lift of:

1. the three ring hinges for the three size-two traces;
2. every deterministic low path (2.3); and
3. every packed high path (3.3).

### Theorem 4.1

The bank `P_3` has maximum degree at most two, no repeated owner, immediate
lower colour, or immediate upper colour, and supplies one contiguous
Johnson witness for every target in `mathcal D_3`.  Every constituent path
is `d`-clipped resident.  Moreover

\[
                         |E(P_3)|=O(m2^m)=o\!\binom{2m-1}m.
\tag{4.1}
\]

#### Proof

The three trace ranges are disjoint.  Lemma 1.1 handles size two, Lemma 2.1
handles the low range, and Lemma 3.1 handles the high range and all
cross-range collisions.  Each target path uses `O(m)` incidence edges and
there are fewer than `2^m` target traces.  The central binomial estimate
gives the final little-oh relation. \(\square\)

## 5. All-width transparency of the planted move

### Theorem 5.1 (complete lower and upper transport)

Suppose an upper-complete physical carrier contains the protected bank
`P_3` and the three common-history hinge fragments, with the displayed path
occurrences unchanged outside the ring switch.  Then the cyclic ring
rethread preserves:

1. the occurrence-labelled multiset of every strict-lower interval value;
2. one literal occurrence of every rank-`m` owner and every immediate
   palette target in the protected bank; and
3. at least one literal interval occurrence of every upper target of every
   rank, with no restriction on the width of its witnessing interval.

It adds no source position.

#### Proof

The common-history theorem transports the entire strict-lower deck and the
owner/lower-q1/upper-q1 ring palettes with zero deletion.  Every old upper
target whose selected crossing witness could change lies in `mathcal D_3`.
The three seam bases survive by Lemma 1.1.  Every larger target has its
selected witness on a low or high private path disjoint from the ring and
therefore unchanged.  Targets outside `mathcal D_3` retain their old
crossing or exterior witness by the exact upper-damage-cone theorem; such an
old witness exists by the assumed upper completeness of the ambient carrier.
\(\square\)

## 6. Exact remaining theorem

The three-ring now has a simultaneous literal package for:

- zero-cost Hamilton topology on the bare owner/factor row;
- complete strict-lower compiler transport;
- clipped positive residence;
- complete arbitrary-width upper transparency; and
- simple owner and immediate palettes.

These conclusions become one global construction only after proving that
`P_3` and the coherent ring can be selected in one factor/cap state.  The
remaining row is therefore the guarded residual-factor/common-cap
intersection, not an upper-witness counting or ring-topology problem.

## 7. Dependencies

- `MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md`
- `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md`
- `MATH_THEOREM_COHERENT_SINGLE_PULL_THREE_RING_HAMILTON_PLANTING_20260804.md`
