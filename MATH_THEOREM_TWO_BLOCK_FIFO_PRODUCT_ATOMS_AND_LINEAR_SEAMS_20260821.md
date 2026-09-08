# Two-block FIFO product atoms and linear seams

**Status (2026-08-21).**  The product and seam theorems below are proved.
They give an unconditional legal `Theta(n^2)` atom which exactly factors one
central split slice, and a conditional exact factorization of all but an
exponentially small part of the middle layer from tight-Hamilton
decompositions on the two halves.  The connector cost is `o(W)`, not a new
barrier.  What is not proved is simultaneous coverage of the other
`Theta(sqrt(n log n))` ranks: ordinary Baranyai--Katona decompositions at the
payload rank do not control the other cyclic-window decks of the same orders.

## 1. A torus product word

Let `b>=3`, let `A,B` be disjoint `b`-sets, and fix cyclic orders

\[
 \alpha=(\alpha_0,\ldots,\alpha_{b-1}),\qquad
 \beta=(\beta_0,\ldots,\beta_{b-1}).                 \tag{1.1}
\]

Let `tau` be a binary cyclic word of length `b` having `r` letters `A` and
`b-r` letters `B`.  Read `tau` periodically.  At an `A`-step emit the next
letter of the periodic stream `alpha`, and at a `B`-step emit the next letter
of the periodic stream `beta`.  Denote the resulting singleton word by
`w(alpha,beta;tau)`.

### Lemma 1.1 (coprime torus enumeration)

If `gcd(r,b)=1`, the first `b^2` length-`b` windows of `w` are precisely

\[
 \bigl\{I_\alpha(i,r)\mathbin\cup I_\beta(j,b-r):
             (i,j)\in\mathbb Z_b^2\bigr\},           \tag{1.2}
\]

each once.  Here `I_alpha(i,q)` is the set of `q` consecutive entries of
`alpha` ending at `i` (the choice of ending rather than starting indices is
immaterial).  The word is cyclic with period `b^2`.

#### Proof

Let `(i_t,j_t)` be the two stream counters after step `t`.  Their sum is
`t` modulo `b`.  Therefore equal counter pairs force equal residues modulo
`b`.  For a fixed residue write `t=qb+s`.  Advancing one period of `tau`
adds

\[
                         (r,b-r)\equiv(r,-r)\pmod b. \tag{1.3}
\]

Since `r` is a unit modulo `b`, the `b` possible values of `q` give all
counter pairs having the fixed counter sum.  Thus
`t -> (i_t,j_t)` is a bijection from `Z_(b^2)` to `Z_b^2`.
Every `b` consecutive type letters contain exactly `r` `A`'s and `b-r`
`B`'s, so its emitted set is (1.2).  After `b^2` steps each stream counter
has advanced a multiple of `b`, proving cyclicity.  \(\square\)

A cyclic binary word with `r` occurrences of `A` can be chosen balanced:
the number of `A`'s in two intervals of equal length differs by at most one.
For such a choice, consecutive occurrences of one fixed `A`-label, which
are `b` `A`-events apart, have physical separation at least

\[
 \left\lfloor{b^2\over r}\right\rfloor,              \tag{1.4}
\]

and the analogous lower bound for `B` is
`floor(b^2/(b-r))`.  This is the standard mechanical-word spacing: the
locations of the `q`th `A`-event differ from `qb/r` by less than one.

Consequently, if the required singleton separation is `f`, the sufficient
condition

\[
 r,b-r\le {b^2\over f}                               \tag{1.5}
\]

makes the product word legal.  In particular, for integer `H>=0`,

\[
 f=b+H+2,qquad H+2\le r\le b-H-2                    \tag{1.6}
\]

is sufficient, because
`(b-H-2)(b+H+2)=b^2-(H+2)^2<b^2`.

## 2. The unconditional middle-slice atom

Put

\[
 b=2h+1,qquad r=h,                                  \tag{2.1}
\]

and take

\[
                 \tau=BABA\cdots B                  \tag{2.2}
\]

with `h` letters `A` and `h+1` letters `B`.  The gaps between consecutive
`A`-events are cyclically `2,...,2,3`, while those between consecutive
`B`-events are `2,...,2,1`.  A fixed `A`-label recurs after `b` `A`-events
and a fixed `B`-label after `b` `B`-events.  Hence the exact minimum
same-label separation is at least

\[
                         2b-2.                       \tag{2.3}
\]

It follows that this atom is legal for the palette floor
`f=b+H+2` whenever `b>=H+4`.

The MSW middle-wreath theorem supplies, on every `b=2h+1` element set, a
family of cyclic orders whose `h`-windows partition the rank-`h` layer.
The `(h+1)`-windows of the same orders partition the rank-`(h+1)` layer by
complementation.

### Theorem 2.1 (exact product-slice factor)

Fix disjoint `b`-sets `A,B`.  Pair every wreath of an MSW factor on `A`
with every wreath of an MSW factor on `B`, and apply (2.2).  The resulting
`b^2`-cycles partition exactly the split slice

\[
 \mathcal S(A,B)=
 \{S\subseteq A\cup B:|S\cap A|=h, |S\cap B|=h+1\}. \tag{2.4}
\]

There are

\[
 {1\over b^2}{b\choose h}^2                         \tag{2.5}
\]

atoms, each with `b^2` distinct middle targets.

#### Proof

Lemma 1.1 says that the atom from a pair of wreaths is the Cartesian product
of their two window decks.  Each local deck occurs in exactly one MSW
wreath, so the Cartesian products are pairwise disjoint and exhaust (2.4).
\(\square\)

If an extra pivot is adjoined, so that the ambient size is `2b+1`, the slice
in (2.4) has, with `W=binom(2b+1,b)`,

\[
 |\mathcal S(A,B)|={b\choose h}^2
       =(1+o(1)){W\over\sqrt{\pi b}}.                \tag{2.6}
\]

Thus one fixed split slice is only `Theta(b^(-1/2))` of the odd middle
layer.  Pure volume would require `(1+o(1))sqrt(pi b)` disjoint slices;
Theorem 2.1 does not provide such a slice design.

## 3. Every nearby deck inside one atom is simple

### Proposition 3.1 (full internal band simplicity)

For the atom in Lemma 1.1, fix a rank `ell` such that every length-`ell`
type interval contains between `1` and `b-1` letters of each type.  Then its
`b^2` cyclic length-`ell` windows are pairwise distinct.

In particular, for (2.2) this holds simultaneously for

\[
 b-H\le \ell\le b+1+H                             \tag{3.1}
\]

whenever `H<=b-5` (in particular, whenever `H=o(b)` and `b` is
sufficiently large).

#### Proof

Suppose the targets at times `t,u` are equal.  Intersecting them with `A`
and `B` shows first that the two type counts agree.  A proper nonempty cyclic
interval in a cyclic order of distinct labels is determined by its set, so
the two `A`-window endpoints agree modulo `b`, and so do the two `B`-window
endpoints.  These endpoints are precisely the counter pair
`(i_t,j_t)`.  The bijection in Lemma 1.1 gives `t=u` modulo `b^2`.
\(\square\)

This is stronger than central simplicity of the atom, but it is only an
**internal** statement.  It does not prevent equal rank-`ell` targets in two
different atoms.

## 4. Linear universal seams

Let `P(d,k)` be the directed permutation shift graph.  Its vertices are the
ordered `k`-tuples of distinct symbols from an alphabet of size `N=k+d`;
one step deletes the oldest entry and appends any symbol absent from the
current tuple.  A path in this graph is exactly a singleton word having no
equal letters at distance at most `k`.

### Theorem 4.1 (near-half permutation-shift diameter)

Put `s=k-d`.  If

\[
                         d\ge s+2,                   \tag{4.1}
\]

then any ordered `k`-tuple `u` can be joined to any ordered `k`-tuple `v`
by a directed path of length at most

\[
                         3k+1.                       \tag{4.2}
\]

#### Proof

If `d>=k+1`, choose any `2k+1` symbols containing (u\cup v) and restrict
all intermediate moves to this subalphabet.  It is enough to prove the
result there with `N'=2k+1` and `d'=k+1`; rename `(N',d')` as `(N,d)`.
This case has `s=-1` and `t=0` in the construction below.  We may therefore
assume `d<=k+1`.

Write tuples oldest to newest and put `t=s+1`.  Starting from `u`, append
`t` arbitrary legal symbols while avoiding `{v_1,...,v_t}`.  This is always
possible: the free pool has size `d>t`, so it is not contained in the
forbidden `t`-set.  Let the resulting queue be `u'`.

If a shared symbol satisfies `x=u'_j=v_i`, then

\[
                         j-i\le d-2.                 \tag{4.3}
\]

Indeed, an entry surviving from `u` has `j<=k-t=d-1`, while a newly
appended entry avoids the first `t` target positions and hence has `i>t`;
the two cases give (4.3).

We next seek a permutation `P` of all `N` symbols.  Give each symbol the
following allowable interval of positions in `P`:

\[
\begin{array}{c|c}
x=u'_j=v_i &[j+1,d+i-1]\\
x=u'_j\notin v &[j+1,N]\\
x=v_i\notin u' &[1,d+i-1]\\
x\notin u'\cup v &[1,N].
\end{array}                                           \tag{4.4}
\]

The shared intervals are nonempty by (4.3).  This interval family has a
system of distinct representatives.  By the interval form of Hall's
theorem, it is enough to check that at most `b-a+1` intervals are contained
in every position interval `[a,b]`.  If `1<a<=b<N`, only shared-symbol
intervals can be contained in `[a,b]`.  Their indices obey

\[
 j\ge a-1,qquad i\le b-d+1,qquad j-i\le d-2,
\]

and hence

\[
                 a-d+1\le i\le b-d+1.               \tag{4.5}
\]

There are at most `b-a+1` of them because the target indices `i` are
distinct.  For a proper prefix `[1,b]`, every contained interval belongs to
a distinct target position `i<=b-d+1`, so the count is at most `b`.  The
suffix case is the same using the distinct source positions `j`, and the
whole interval contains exactly `N` intervals.  Hall therefore gives `P`.

The lower bounds in (4.4) say that `u'P` has no repeat at distance at most
`k`; the upper bounds say the same for `Pv`.  Thus the appended word

\[
       (\text{the first }t\text{ letters})\;P\;v
\]

is legal, ends in state `v`, and has length

\[
                         t+N+k=3k+1.                 \tag{4.6}
\]

\(\square\)

The construction and the interval matching were exhaustively replayed on
the remote compute host for every target `v`, after fixing `u` by label
transitivity, for all `N<=10` and every parameter pair satisfying (4.1).
This is only a finite audit; the proof above is independent of it.

### Corollary 4.2 (the actual DCC palette has linear word seams)

For

\[
 n=2m+1,\qquad f=m+H+2,\qquad k=f-1,
\]

the permutation-shift degree and imbalance are

\[
 d=n-k=m-H,\qquad s=k-d=2H+1.                       \tag{4.7}
\]

Thus `m>=3H+3` implies (4.1), and any two clean length-`k` boundary
histories can be joined in at most

\[
                         3(m+H+1)+1=O(n)             \tag{4.8}
\]

emissions.  This replaces the `Theta(n^3)` complete-state bridge whenever
only the DCC word and its ranks at most `f-1` must be preserved.  It does not
replace that bridge in an argument which genuinely prescribes the entire
ordered recency state.

### Corollary 4.3 (product atoms have negligible seam cost)

Suppose `Q=O(W/b^2)` cyclic product atoms on an alphabet of size `N=Theta(b)`
are to be serialized, and the required separation is `f=k+1` with (4.1).
Cut each next atom after any prescribed length-`k` history `v`, use Theorem
4.1 to reach `v`, and then traverse the atom.  The resulting cyclic word has
total connector length

\[
                         O(Qb)=O(W/b)=o(W).           \tag{4.9}
\]

All windows meeting connectors may be charged.  Across a band `K` this costs

\[
                         O(|K|W/b)=o(W)               \tag{4.10}
\]

whenever `|K|=o(b)`.  Thus neither exact-state bridges nor compatible atom
endpoints are needed for this construction.

## 5. Conditional Baranyai--Katona aggregation

Now take an **even** ambient alphabet `A union B`, with
`|A|=|B|=b`, middle rank `b`, and
`W=binom(2b,b)`.  Assume `b` is an odd prime.  For every
integer `H>=0` assume also `H=o(b)` (the DCC application has
`H=Theta(sqrt(b log b))`).  For every
`1<=r<=b-1`, the necessary divisibility

\[
                         b\mid {b\choose r}           \tag{5.1}
\]

holds.  Suppose, conditionally, that the rank-`r` subsets of a `b`-set admit
a decomposition into tight Hamilton cycles, equivalently cyclic orders whose
`r`-windows partition that layer.  This is the Baranyai--Katona tight-cycle
decomposition conjecture, not a known theorem in the required growing-rank
range.

For every

\[
 I=\{H+2,\ldots,b-H-2\},                             \tag{5.2}
\]

pair a rank-`r` factor on `A` with a rank-`(b-r)` factor on `B`, choose a
balanced type word with `r` `A`-steps, and apply Lemma 1.1.  The atoms for
that `r` partition the profile

\[
                         \{S:|S\cap A|=r\}.           \tag{5.3}
\]

Profiles for different `r` are disjoint.  Consequently these atoms cover
exactly

\[
 P=\sum_{r\in I}{b\choose r}^2                       \tag{5.4}
\]

middle targets in exactly `P` payload positions, using exactly `P/b^2`
atoms.  Vandermonde's identity and the elementary binomial-tail bound give

\[
 {2b\choose b}-P
 \le 2(H+2){b\choose H+1}^2
 =e^{-\Omega(b)}{2b\choose b}.                       \tag{5.5}
\]

By (1.6) all payload atoms obey the separation floor, and Corollary 4.3
serializes them with `o(W)` additional positions.  Hence the conjectured
tight-cycle decompositions would yield a coefficient-one **middle-layer**
near-universal singleton word, with no semi-random palette selector.

The restriction to even dimensions `2b` and prime `b` is asymptotically
harmless for a completed OR construction: prime gaps are `o(b)`, and the
proved top-bit splice has only a `1+o(1)` width loss across an `o(b)`
dimension gap.  This observation does not remove the next gate.

## 6. Exact surviving gate

Ordinary tight-Hamilton decompositions at rank `r` control only the
length-`r` windows of their cyclic orders.  A rank-`b+q` window of the
product word uses other local interval lengths, depending on its type phase.
Those other window decks need not be injective or covering across different
wreaths.  Proposition 3.1 proves that each individual atom is band-simple,
but says nothing about collisions between atoms.

Therefore the following implication is **not** valid:

\[
 \text{Baranyai--Katona at every payload rank}
 \quad\Longrightarrow\quad
 \text{a defective central covering}.               \tag{6.1}
\]

What would suffice is a coherent multirank strengthening: choose the local
tight-cycle factors, their orientations, and the serialization so that the
sum of missing global targets over
`b-H<=ell<=b+H` is `o(W)`.  The first-shadow and multidepth wreath audits in
the project show that this is genuine extra content; it is not a consequence
of exact middle factorhood.  Thus the product route removes the torus,
central-volume, internal-simplicity, and seam obstructions, but it currently
lands exactly at a multirank Baranyai--Katona/coherent-wreath gate.

### Proposition 6.1 (equal-block recursion barrier)

The two-block torus atom does not iterate naively to three or more equal
blocks.  More precisely, take `q` periodic streams, each with counter in
`Z_b`, and a type word of period `L` having count vector
`r=(r_1,...,r_q)`.  At a fixed type phase, passage through one period
translates the counter vector by `r` in `(Z_b)^q`.  This translation has
order at most `b`.  Therefore the whole scheduled orbit has at most

\[
                              Lb                     \tag{6.2}
\]

distinct phase/counter states.

If a fixed local window rank is used in every stream, a Cartesian atom
enumerating every counter tuple would require `b^q` distinct tuples.  Hence a
necessary condition is

\[
                              b^q\le Lb.             \tag{6.3}
\]

For a central `q`-block construction `L=Theta(qb)`, so (6.3) fails for every
fixed `q>=3` and all sufficiently large `b`.  The two-block construction has
`q=2,L=b` and meets the bound exactly.  Any recursive product must therefore
use unequal/coprime counter moduli, a nonperiodic rank profile, or a genuinely
different wreath-product mechanism.

#### Proof

At each of the `L` phases, all visits lie in one orbit of translation by
`r`.  Every element of `(Z_b)^q` has additive order at most `b`, giving at
most `b` counter vectors per phase and (6.2).  Enumeration of all `b^q`
counter tuples implies (6.3); the final comparison is immediate.  \(\square\)
