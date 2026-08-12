# Unbuffered multi-primitive reservoirs: clustered pruning and balanced socket reservation

Date: 2026-08-02  
Status: unconditional asymptotic owner/lower/immediate-upper named-target
packing and exact aggregate occurrence reservation.  Physical component
fusion and the deeper-upper/residence/compiler interfaces are not claimed.

## 0. Outcome

Put

\[
 q=d+2,\qquad c=r-q+1=r-d-1,\qquad W=\binom{k}{r},
\]

and assume the canonical sufficiently-large range with `d>=2`, `c>=1`.
Let

\[
 m=\left\lfloor{q\over2}\right\rfloor+1,
 \qquad
 L=2m=
 \begin{cases}q+2,&q\text{ even},\\q+1,&q\text{ odd},\end{cases}
 \qquad Q=L+1.                                            \tag{0.1}
\]

Thus `m` equals the sharp minimum `ceil(q/2)` when `q` is odd and exceeds
it by one when `q` is even.  The one extra `PH` pair in the even case is
used solely to keep the immediate-upper cyclic intervals proper.

The common-core construction underlying the sharp primitive theorem proves
that the alternating cycle `(PH)^m` is a literal owner-simple realization
of `m` copies of

\[
                         g_{d-1,d+1}=e_{d-1}+e_{d+1},       \tag{0.2}
\]

with no short-buffer occurrences.

Place all cycles over singleton-base subset-core reservoirs.  One support
is

\[
                         A=\{\beta\}\dot\cup V,
 \qquad |V|=L,                                           \tag{0.3}
\]

and for every

\[
                         X\in\binom{[k]-A}{c-1}            \tag{0.4}
\]

use `X` as the common source core and `beta` as the alternating refreshed
point.  Every named resource has outside-`A` trace exactly `X`.

Here the deliberate strict inequality `L>q` makes not only the owners but
also their consecutive unions distinct.  The random clustered-pruning
argument therefore applies verbatim to the complete marked lower deck,
the owner deck, and the immediate-upper deck, with `Lq=Theta(q^2)`
occurrence cylinders per cycle.  It yields

\[
 \boxed{\Omega(W/q^2)\text{ pairwise owner/target-disjoint literal cycles}}
                                                                  \tag{0.5}
\]

and hence

\[
 \boxed{\Omega(W/q)\text{ primitive signatures realized inside pairwise
 named-deck-disjoint cycles}.}
                                                                  \tag{0.6}
\]

At the aggregate age-signature layer, reserving one cycle subtracts

\[
                         me_{d-1}+me_{d+1}.                \tag{0.7}
\]

This is resource-balanced, so it does not consume the low-minus-high slack
`E=L_low-H_high`.  With conductor margin, `Theta(W/q^2)` such cycles can be
reserved while the residual canonical age vector remains integrally
decomposable.  Thus the scalar `E=0` obstruction to the one-primitive plus
`d`-buffer family is absent here.

The cycles remain separate components.  This theorem does not order them
in one physical chronology or prove deeper upper shadows, global residence,
protected positional pins, or compiler/common-cap feasibility.

## 1. The literal alternating cycle

Fix `X` and an oriented cyclic order

\[
                         V=(z_0,z_1,\ldots,z_{L-1}).         \tag{1.1}
\]

At even positions use a `P` source and at odd positions an `H` source:

\[
 S_t=\begin{cases}
 X\cup\{z_t\},&t\text{ even},\\
 X\cup\{\beta,z_t\},&t\text{ odd}.
 \end{cases}                                               \tag{1.2}
\]

Here `|X|=c-1=s-2` in the notation of the primitive theorem.  There are
`m` occurrences of each type, and `(1.2)` is exactly its common-core
construction.

### Proposition 1.1 (exact literal deck)

The cycle (1.2) has the following injective named deck:

\[
\begin{array}{c|c|c}
\text{rank}&\text{resources}&\text{count}\\ \hline
c&X\cup\{z_t\},\ t\text{ even}&m,\\
c+1&X\cup\{\beta,z_t\},\ t\text{ odd}&m,\\
c+j,\ 2\le j\le q-2
 &X\cup\{\beta\}\cup J,\ J\text{ a cyclic }j\text{-interval}&L,\\
r&X\cup\{\beta\}\cup J,\ J\text{ a cyclic }(q-1)\text{-interval}&L,\\
r+1&X\cup\{\beta\}\cup J,\ J\text{ a cyclic }q\text{-interval}&L.
\end{array}                                                 \tag{1.3}
\]

Every resource in (1.3) has intersection with `[k]-A` exactly `X`, and
the total number of occurrence cylinders is

\[
                 2m+L(q-3)+L+L=Lq.                       \tag{1.4}
\]

### Proof

The age type at an even position is

\[
                         P=(c,2,1,\ldots,1),
\]

and at an odd position it is

\[
                         H=(c+1,1,\ldots,1).
\]

Mark every rank offered by every occurrence, as in the unbuffered
primitive theorem.  A `P` source supplies rank `c`, an `H` source rank
`c+1`, and every prefix of length `j>=2` contains `beta` and exactly the
`j` consecutive private tags ending at that position.  This gives the
first three rows of (1.3).

An owner is a union of `d+1=q-1` consecutive sources.  Such a window
contains both parities, hence contains `beta`, and has exactly `q-1`
consecutive tags.  Its rank is

\[
                         (c-1)+1+(q-1)=r.
\]

Two consecutive owner tag intervals of length `q-1` overlap in `q-2`
tags and have union a cyclic `q`-interval.  Their owners therefore meet in
a marked rank-`r-1` target and unite to the rank-`r+1` target in the last
row of (1.3).  Because `L>q`, every displayed tag interval is proper and
fixed-length cyclic intervals have distinct starts.  This is also the
injectivity proof in the primitive theorem.  Finally `X` is disjoint from
the support `A`, so every row has outside trace exactly `X`.  Summing the
row counts gives (1.4). \(\square\)

For odd `q`, `L=q+1` and the owners omit two consecutive tags.  For even
`q`, `L=q+2` and they omit three.  Both parities are covered by the same
proper-interval proof.  The extra two tags in the even case are essential:
had one chosen the shorter legal primitive cycle `L=q`, every consecutive
owner union would have used all tags and the entire immediate-upper row
would have collapsed to one value.

## 2. One reservoir and its size

For a fixed support and order, let `X` range over (0.4).  Proposition 1.1
shows that modules with different `X` have disjoint decks, because the
outside trace recovers `X`.  Put

\[
                         M_L=\binom{k-Q}{c-1}.              \tag{2.1}
\]

### Lemma 2.1 (reservoir scale)

Uniformly in the two parities of `q`,

\[
                         M_L=\Theta(W/2^q).                \tag{2.2}
\]

### Proof

Here `Q=q+2` or `q+3`, while `c-1=r-q`.  The exact ratio

\[
 {\binom{k-Q}{r-q}\over\binom kr}
\]

is a product of `Q=Theta(sqrt(k))` central factors.  Pairing numerator and
denominator factors gives `2^{-Q}exp(O(Q^2/k))`.  Since `Q^2/k=Theta(1)`,
this is `Theta(2^{-q})`. \(\square\)

## 3. Clustered pruning

Choose two supports `A,A'` of size `Q` and put

\[
                         E=A'-A,\qquad b=|E|.              \tag{3.1}
\]

Every occurrence of the second cycle is a cylinder with one footprint
`R' subseteq A'`.  If a first module `X` collides with it, equality of the
two resources and intersection with `A'` force

\[
                         X\cap E=R'\cap E.                 \tag{3.2}
\]

For one prescribed trace `T subseteq E`, exactly

\[
                         \binom{k-Q-b}{c-1-|T|}            \tag{3.3}
\]

module indices realize it.  As in the buffered clustered-pruning theorem,
there is an absolute `C_0` with

\[
 {\binom{k-Q-b}{c-1-|T|}\over M_L}
                         \le C_0 2^{-b}.                   \tag{3.4}
\]

The proof is the identical hypergeometric calculation: the selected
fraction `(c-1)/(k-Q)` is `1/2+O(1/q)` and `b<=Q=O(q)`.

The number of second-frame traces is `Lq=O(q^2)`, so the number
`B(R,R')` of first modules bad against a second reservoir obeys

\[
                         B(R,R')\le C_2M_Lq^2 2^{-b}.      \tag{3.5}
\]

For independent uniform supports, with `Z=|A cap A'|`,

\[
 \mathbb E2^Z
 =\sum_{t=0}^{Q}\binom Qt{(Q)_t\over(k)_t}
 \le\exp\left({Q^2\over k-Q+1}\right)=O(1).              \tag{3.6}
\]

Since `b=Q-Z`, averaging (3.5) gives

\[
                         \mathbb E B(R,R')
                  \le C_3M_L{q^2\over2^q}.               \tag{3.7}
\]

### Theorem 3.1 (unbuffered clustered-pruning extraction)

For every sufficiently large canonical `k`, there are

\[
                         \Omega(W/q^2)                    \tag{3.8}
\]

pairwise owner- and named-target-disjoint literal alternating cycles of the
form (1.2).  They jointly realize `Omega(W/q)` primitive signatures
`g_(d-1,d+1)` inside pairwise named-deck-disjoint cycles.  The
immediate-upper edges belong to the whole alternating cycle; no separate
upper subdeck is assigned to an individual primitive.

### Proof

Sample

\[
                         R_0=\left\lfloor
                 {2^q\over4C_3q^2}\right\rfloor          \tag{3.9}
\]

independent reservoirs.  Delete every module cycle sharing any named
resource with any module in another sampled reservoir.  Ordered-pair
overcounting and (3.7) bound the expected number deleted by `R_0M_L/4`.
Some outcome retains at least `3R_0M_L/4` cycles, and they are pairwise
resource-disjoint by construction.  Equations (2.2) and (3.9) give (3.8).
Each cycle realizes exactly `m=Theta(q)` primitive packages, proving the
last assertion. \(\square\)

In carrier language, the retained cycles form a partial doubly-rainbow
Johnson two-factor: they use `Omega(W/q)` distinct rank-`r` owners, their
adjacent intersections are distinct rank-`r-1` targets, and their adjacent
unions are distinct rank-`r+1` targets.  This is still only a `Theta(1/q)`
fraction of the owner layer; the statement is a protected socket bank, not
a spanning factor.

As before, the constant can be reduced arbitrarily by sampling fewer
reservoirs.  Duplicate supports and multiple collisions are harmless,
because every occurrence involved in any cross collision is deleted.

## 4. Weighted protected-bank extension

Choose all internal labels symmetrically.  For a forbidden named-resource
bank `D_u`, define

\[
 \Psi_{\rm un}=
 m{|D_c|\over\binom{k}{c}}
 +m{|D_{c+1}|\over\binom{k}{c+1}}
 +L\sum_{j=2}^{q-2}{|D_{c+j}|\over\binom{k}{c+j}}
 +L{|D_r|\over W}
 +L{|D_{r+1}|\over\binom{k}{r+1}}.                      \tag{4.1}
\]

One random reservoir has exactly `M_L` times the displayed per-cycle row
counts, so transitivity gives exactly `M_L Psi_un` expected forbidden
incidences.  If `Psi_un<=psi<1`, reduce the constant in (3.9) until the
cross-deletion fraction plus `psi` is below one.  The same proof leaves
`Omega(W/q^2)` cycles avoiding the bank.

## 5. Balanced aggregate socket reservation

Let `A=(A_0,...,A_(r-1))` be the canonical age-signature vector and let
`Q_(r,d)` be the conductor quantum in the exact aggregate semigroup
theorem.

### Theorem 5.1 (unbuffered aggregate reservation)

Assume `d>=4`, `d+1<r`,

\[
 A_{d-3},A_{d-2}\ge Q_{r,d}+1,
\]

and let

\[
 t\le\left\lfloor {1\over m}
       \min\{A_{d-1}-Q_{r,d}-1,
              A_{d+1}-Q_{r,d}-1\}\right\rfloor.          \tag{5.1}
\]

Then `t` literal alternating cycles may be reserved, and the residual age-
signature vector still has an exact integral short/long/mixed rotor
decomposition.

### Proof

Subtract

\[
                 A'=A-tme_{d-1}-tme_{d+1}.                \tag{5.2}
\]

The two coordinates lose equal resource because their distances from `d`
are both one.  Hence the standing slack `L_low-H_high` is unchanged and
remains nonnegative.  Equation (5.1) leaves the two buffer coordinates at
least `Q_(r,d)+1`; the other two conductor coordinates are unchanged.  The
exact buffered semigroup criterion applies to `A'`.  Restoring the `t`
explicit literal cycles proves the assertion. \(\square\)

Canonically,

\[
 A_{d-1},A_{d+1}=\Theta(W/q),\qquad m=\Theta(q),         \tag{5.3}
\]

while the conductor is negligible compared with these coordinates.  Thus
the right side of (5.1) is `Theta(W/q^2)`.  By reducing the sampling
constant in Theorem 3.1, the packed cycles fit this occurrence inventory.
Unlike the one-primitive buffered family, no hypothesis
`L_low-H_high=Omega(W/q)` is needed.

## 6. Exact component-joining boundary

The cycles in Theorem 3.1 are literal chronologies, but they are separate.
For a cyclic source word `S`, define the nested union chain ending at `t`
by

\[
 \mathbf U_t(S)=
 \left(S_t,S_{t-1}\cup S_t,\ldots,
       \bigcup_{i=0}^{d}S_{t-i}\right).                 \tag{6.1}
\]

Cut one edge in each of two source cycles and reconnect the four ends
crosswise.  Only positions within distance `d` of an old or new cut change
their chain.  Equality of the old and new affected marked-chain multisets
is therefore sufficient to transport every protected lower cell, owner,
and named prefix target.  It is also necessary when complete affected
marked chains are protected as unique resources with no outside duplicate
providers.  Under a weaker protection policy it remains sufficient but
need not be necessary.

There is a rank obstruction before this chain test.  If two packets with
cores `X,Y`, both of size `c-1=r-q`, occur in one reconnected owner window,
then that window contains `X union Y`.  Since the cores have equal size,
writing `t=|X\setminus Y|=|Y\setminus X|` gives

\[
       |X\cup Y|=r-q+t.
\]

Thus a rank-`r` mixed owner requires

\[
                         |X\setminus Y|\le q.           \tag{6.2}
\]

This is only necessary: private-tag compatibility, the immediate-upper
row, and the complete chain equation (6.1) can impose more.  Clustered
pruning controls named-resource collisions but does not force its retained
cores to contain a spanning tree of such transparent sockets.  This is the
exact first chronology obstruction left by the packing theorem.

## 7. Exact remaining scope

The theorem proves jointly:

1. a literal local cycle for every selected package;
2. pairwise distinct owners, marked lower targets, and immediate-upper
   targets across all selected cycles;
3. avoidance of any weighted-small preused named bank;
4. exact aggregate reservation with an integrally decomposable residual.

It does not prove that the `Theta(W/q^2)` cycles can be fused into one
physical factor without changing their named decks.  It also does not
establish arbitrary-width upper targets beyond the immediate-upper deck,
global coordinate residence after fusion, protected positional interfaces,
or the final lower compiler/common cap.

The random support action is on coordinate names.  Physical positions and
component ports are not `Sym([k])`-homogeneous, so the weighted bank argument
does not reserve a chronology by itself.  A separate component-fusion and
upper-transparent host theorem remains necessary.

## 8. Dependencies

The alternating literal cycle is the common-core construction in Section 3
(and the minimum-length calibration is Theorem 3.1) of
`MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md`.
The clustered trace method is Section 9 of
`MATH_THEOREM_FACET_FIXED_BASE_COLLISION_TENSOR_AND_WHOLE_FRAME_NOGO_20260802.md`.
The conductor criterion is Theorem 4.1 of
`MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md`.
