# Parity fibers in the fixed-endpoint tail-MTF palette are rigid

**Status (2026-08-21).**  The statements below are proved.  They rule out a
naive two-stage rounding in which one first fixes the resource projection on
one rank parity and then repairs the other parity by independently switching
inside each selected block.  They do **not** rule out rare deliberately
switch-rich cores, a simultaneous two-parity selection, or a global
recomposition that moves middle-rank targets between different block slots.

## 1. Model and terminology

Let a tail move-to-front state be a permutation of `[n]`.  Fix an eligibility
floor `f<n`.  At every step, select a letter in a position at least `f`, record
it, and move it to the front.  Put

\[
 d=n-f+1.
\]

If the recorded letters are `(x_t)`, equal letters have occurrence gap at
least `f`.  For `k<=f`, the post-move top-`k` set is therefore

\[
 C_k(t)=\{x_t,x_{t-1},\ldots,x_{t-k+1}\}.              \tag{1.1}
\]

For a core of length `b`, its ordered rank-`k` trace is
`(C_k(1),...,C_k(b))`, while its unordered rank-`k` **deck** is

\[
 \mathcal P_k=\{C_k(t):1\le t\le b\}.                  \tag{1.2}
\]

A core is band-simple on a rank set `K` if every deck `\mathcal P_k`,
`k in K`, has cardinality `b`.

Write `J(n,k)` for the Johnson graph on `binom([n],k)`: two vertices are
adjacent when their symmetric difference has size two.  For `k<f`,
consecutive members of every ordered rank-`k` trace are adjacent in
`J(n,k)`.

For the asymptotic palette, use

\[
 n=2m+1,\qquad H=\lceil\sqrt{n\log n}\rceil,
\]

\[
 K=\{m-H,\ldots,m+1+H\},\qquad
 f=m+H+2,\qquad d=m-H,                                 \tag{1.3}
\]

and core lengths

\[
 1\le b\le A:=\lfloor e^{n/5}\rfloor.                 \tag{1.4}
\]

Thus every `k in K` satisfies `d<=k<f`, and both middle ranks `m,m+1`
satisfy `k<=f-2`.

## 2. A time-labelled trace has no bulk fiber

### Lemma 2.1 (adjacent-prefix identities)

Whenever the displayed times exist and `k+1<=f`,

\[
 C_k(t)\setminus C_k(t-1)=\{x_t\},\qquad
 C_k(t-1)\setminus C_k(t)=\{x_{t-k}\},                 \tag{2.1}
\]

\[
 C_{k+1}(t)=C_k(t-1)\cup C_k(t),                       \tag{2.2}
\]

and

\[
 C_{k-1}(t)=C_k(t)\cap C_k(t+1).                       \tag{2.3}
\]

More generally, for `r>=0` and `k+r<=f`,

\[
 C_{k+r}(t)=\bigcup_{j=0}^{r}C_k(t-j),                 \tag{2.4}
\]

and, for `0<=r<k`,

\[
 C_{k-r}(t)=\bigcap_{j=0}^{r}C_k(t+j).                 \tag{2.5}
\]

#### Proof

Every interval of at most `f` recorded occurrences has distinct letters.
Substitution of (1.1) gives every identity.  In particular, two consecutive
`k`-windows share exactly their `k-1` overlapping occurrences.  \(\square\)

### Proposition 2.2 (exact ordered-trace rigidity)

Let two legal cores of the same length `b>=k` have the same time-labelled
rank-`k` trace, where `k<f`.  Then their entire core access words are equal.
Their time-labelled traces agree at every rank `ell<=k`.  At a rank
`k<ell<f` they agree at every time

\[
 t\ge \ell-k+1,                                       \tag{2.6}
\]

so only the first `ell-k` observations can depend on the older part of the
seed state.  If the seed states themselves are fixed, all rank traces agree.

#### Proof

Equation (2.1) recovers `x_2,...,x_b` from consecutive trace differences.
The `k-1` removed letters in the transitions from times `1` through `k` are,
in order,

\[
 x_{2-k},x_{3-k},\ldots,x_0.
\]

They are `k-1` distinct members of `C_k(1)`; its one remaining member is
`x_1`.  Thus the trace recovers the core word and the part of the pre-core
word needed by every rank at most `k`.  Formula (1.1) now proves equality at
all ranks at most `k`.  At rank `k<ell<f`, the oldest occurrence needed at time
`t` is `x_(t-ell+1)`, which lies in the recovered range as soon as
`t-ell+1>=2-k`; this is (2.6).  A common full seed removes the remaining
initial ambiguity.  \(\square\)

There is an especially sharp parity consequence.  The two largest ranks in
`K` are `f-2` and `f-1`, one in each parity.  For a core of length at least
`f-1`, fixing all time-labelled traces of either parity fixes the entire
opposite parity, except that when the largest fixed rank is `f-2`, the first
rank-`f-1` observation may still vary.  Thus a time-labelled parity fiber can
replace at most one band observation per block.  The large palette blocks
have length `A>>f`; a possible short remainder block has total size `o(W)`
and is immaterial asymptotically.

This is exact, not probabilistic.  It also explains why any genuine residual
freedom must reorder an **unordered** deck rather than preserve a temporal
trace.

## 3. Unordered decks and Johnson chords

Assume the rank-`k` trace is simple.  Its consecutive pairs form a Hamilton
path `E_0` through the induced Johnson graph `J(n,k)[\mathcal P_k]`.  Define
the number of non-temporal Johnson chords by

\[
 \chi_k=e\bigl(J(n,k)[\mathcal P_k]\bigr)-(b-1).        \tag{3.1}
\]

An alternative chronology of the same deck must be another Hamilton path
in this induced graph.  This condition is not sufficient for tail-MTF
legality.  If `a_t` and `r_t` are respectively the added and removed labels
on a directed Johnson transition, then a sliding `k`-window trajectory also
obeys the FIFO constraint

\[
 r_t=a_{t-k}                                            \tag{3.2}
\]

whenever both sides are core transition labels.  Thus arbitrary Johnson-path
reordering overestimates the true fiber.

### Lemma 3.1 (deterministic deck-fiber bound)

Let `1<k<f`.  Let two legal cores be simple at rank `k` and at the adjacent rank being
compared, and suppose they have the same unordered rank-`k` deck
`\mathcal P_k`.  If the first core has chord count `\chi_k`, then their two
sets of temporal Johnson edges have symmetric difference at most `2\chi_k`.
Consequently their rank-`k+1` decks differ by at most `\chi_k+1` target
replacements, equivalently their set symmetric difference has size at most
`2\chi_k+2`; the same is true of their rank-`k-1` decks.

In particular, if `\chi_k=0`, the deck has only its two possible path
orientations, and either adjacent-rank deck is fixed except for one boundary
target.

#### Proof

Both temporal edge sets have size `b-1`.  Every edge used by the second path
but not by the first is one of the `\chi_k` extra induced edges.  The two
equal-sized edge sets therefore have symmetric difference at most `2\chi_k`.

For times `2<=t<=b`, (2.2) says that the rank-`k+1` target is the union label
of the temporal edge `{C_k(t-1),C_k(t)}`.  These `b-1` internal labels depend
only on the temporal edge set; only `C_{k+1}(1)` is a boundary label.  Changing
at most `\chi_k` edges replaces at most `\chi_k` internal labels, and the two
boundary labels contribute at most one further replacement.  The proof for
rank `k-1` uses the intersection labels in (2.3), with the terminal target as
the one boundary label.  \(\square\)

## 4. The central decks are chordless with overwhelming probability

The buffer `f-k>=2` at the two middle ranks gives a much stronger fact than
a generic codegree estimate.

### Lemma 4.1 (short Johnson chords are impossible below the top rank)

Let a legal word have equal-letter gap at least `f`.  Suppose `2<=g<k<f`
and the rank-`k` windows ending at times `t` and `t+g` are Johnson-adjacent.
Then necessarily

\[
 k=f-1.                                                \tag{4.1}
\]

More precisely, when `k=f-1`, write the `g` exiting occurrences in temporal
order as positions `i=1,...,g` and the `g` entering occurrences as positions
`j=1,...,g`.  The unique unmatched exit is `i=g`, the unique unmatched entry
is `j=1`, and every other match has `j=i+1`; all `g-1` matched letters recur
after exactly `f` steps.

#### Proof

The two windows have `k-g` overlapping occurrences.  No entering occurrence
can equal an overlap occurrence, since their separation is at most `k-1<f`.
Johnson adjacency therefore requires a bijection between `g-1` of the
exiting and `g-1` of the entering occurrences.  If exit `i` matches entry
`j`, their occurrence gap is

\[
 k+j-i\ge f,
\]

so `j-i>=s:=f-k`.  Let `i_0,j_0` be the unmatched exit and entry.  Summing
over the matching gives

\[
 (g-1)s
 \le \sum_{\rm matched}(j-i)
 =i_0-j_0
 \le g-1.                                             \tag{4.2}
\]

Hence `s=1`, proving (4.1).  Equality throughout (4.2) forces
`i_0=g`, `j_0=1`, and `j-i=1` for every matched pair.  The corresponding
recurrence gaps are all `k+1=f`.  \(\square\)

We also need the following elementary long-gap estimate.  Run a free core by
choosing each of its `d` eligible positions uniformly.  For any history
through time `u`, any history-measurable `k`-set `S`, and any `g>=k>=d`,

\[
 \Pr\bigl(C_k(u+g)=S\mid\mathcal F_u\bigr)
 \le B_d:=\frac{d!}{d^d}.                              \tag{4.3}
\]

Indeed, condition further through time `u+g-k`.  The last `k` selected
letters are distinct because `k<f`.  If their set is prescribed, then when
`r` prescribed letters remain, at most `min(r,d)` of the `d` eligible choices
are favorable.  Multiplying these factors for `r=k,k-1,...,1` gives (4.3),
because `k>=d`.

### Theorem 4.2 (simultaneous central chordlessness)

Choose the seed state uniformly and every free-core generator uniformly.
For either `k=m` or `k=m+1`, and uniformly for `1<=b<=A`,

\[
 \Pr(\text{the simple rank-}k\text{ deck has }\chi_k>0)
 \le {b\choose2}k(n-k)B_d
 \le\exp\{-n/10+o(n)\}=o(1).                          \tag{4.4}
\]

The same conclusion holds after conditioning on band-simplicity, and with
probability `1-o(1)` both central decks are chordless simultaneously.

#### Proof

Both middle ranks are at most `f-2`, so Lemma 4.1 excludes every
nonconsecutive chord whose time lag is below `k`.  At lag at least `k`, a
fixed current target has `k(n-k)` Johnson neighbors.  Apply (4.3) to each
neighbor and take a union bound over time pairs.  This gives the first
inequality in (4.4).

Stirling's bound gives `B_d<=3\sqrt d\,e^{-d}`.  Since

\[
 b\le e^{n/5},\qquad d=(n-1)/2-H,qquad H=o(n),
\]

the logarithm of the right side of (4.4) is at most

\[
 2n/5-d+O(\log n)=-n/10+o(n).
\]

Band-simplicity has probability `1-o(1)` under the same law, so dividing by
that probability preserves the estimate.  For completeness, this last fact
also follows from (4.3).  A rank-`k` target cannot return at a gap `g<f`:
if `g>=k`, matching the two disjoint occurrence intervals makes the sum of
the `k` recurrence distances equal to `kg`, forcing `g>=f`; if `g<k`, cancel
the overlap and the analogous sum over the `g` exiting/entering occurrences
is `gk`, forcing `k>=f`.  At gaps at least `f`, (4.3) bounds a fixed return by
`B_d`.  A union bound over `K` therefore bounds band-simplicity failure by
`|K|{b\choose2}B_d=o(1)`.  Finally, a union bound over the two middle ranks
completes the proof.  \(\square\)

### Corollary 4.3 (the fractional matching may have rigid support)

In the exact and budget-normalized fractional palette constructions, replace
the core law conditioned on band-simplicity by the law conditioned also on
`χ_m=\chi_(m+1)=0`.  This event is nonempty for all sufficiently large
`n` and is invariant under every relabeling of `[n]`.  Therefore every fixed
rank-`k` target still occurs with exact probability

\[
 \frac b{\binom nk}.                                   \tag{4.5}
\]

All real and dummy degree calculations are unchanged.  Hence both the exact
fractional perfect matching and the budget-normalized fractional near-factor
can be supported entirely on cores having chordless decks at both middle
ranks.

For an edge in this support, fixing its projection on either rank parity
fixes all of its observations at that parity's middle rank: middle ranks have
no dummies and every observation is claimed.  Lemma 3.1 then says that an
alternative path in the same **slotwise** parity-projection fiber can replace
at most one target at the other middle rank.  Across

\[
 s=O(W/A)
\]

blocks, such switches can alter at most `s=o(W)` opposite-middle resources.
This means at most `s` target replacements, or symmetric difference at most
`2s`.
Thus a first parity rounding that leaves a bulk defect on the other middle
rank cannot be repaired by independent within-slot fiber switches.  The
fractional theorem, by itself, supplies no residual entropy of the needed
kind.

## 5. The explicit common-endpoint diamonds do not evade the theorem

Write a state as

\[
 \pi=(p_1,\ldots,p_{f-1},q_1,\ldots,q_d).
\]

Both the length-`f+1` two-way diamond and the length-`n+1` `d`-way gadget
begin with a branch letter `q_j` and then record

\[
 p_{f-1},p_{f-2},\ldots,p_1.                           \tag{5.1}
\]

After these first `f` gadget moves, the last `f-1` recorded letters are
exactly the set `{p_1,...,p_(f-1)}`.  Consequently

\[
 C_{f-1}(\text{gadget time }f)=C_{f-1}(\pi).           \tag{5.2}
\]

If the gadget starts after any already recorded core step, (5.2) repeats a
rank-`f-1` target and violates band-simplicity.  Such a gadget can therefore
occur only at the very beginning of a band-simple core, where its input state
is outside the incidence ledger.  In particular, two copies cannot be
concatenated inside one band-simple core.

The two-way gadget is even more rigid.  In its `q_1` branch, the first `f`
moves return the full state to `pi`, and the next `q_1` move returns it to
the state already seen after the first move.  Thus that branch itself
violates band-simplicity at every rank.  Its other branch supplies no
two-way switch after conditioning.  The `d`-way gadget can retain at most
`d-1` useful initial branches, hence only `log_2(d-1)=O(log n)` bits and at
most `k=O(n)`
variable rank-`k` observations per entire long block.  Summed over
`s=O(W/A)` blocks, this is `O(ns)=o(W)` central-rank mobility.

One may instead use the known exact bridge of length

\[
 R=n^3+f^2
\]

to isolate repeatedly prescribed gadget starts.  With this currently proved
construction, `G` independently placed diamonds cost `G(R+O(n))` physical
steps, carry only `O(G log n)` branch bits, and expose at most `O(Gn)`
branch-dependent central observations.  Inside physical budget `a`, these
scales are respectively

\[
 O\!\left(\frac{a\log n}{n^3}\right)
 \quad\text{and}\quad
 O\!\left(\frac a{n^2}\right).                         \tag{5.3}
\]

Equation (5.3) is a cost statement for the available bridge-separated
construction, not a lower bound on every possible switch architecture.

## 6. Exact scope of the obstruction

The proved conclusion is:

> Under a relabeling-symmetric fractional law with exactly the same marginals
> as the fixed-endpoint palette theorem, both middle-rank decks may be taken
> chordless.  Once one such middle deck is fixed **within each slot**, its
> chronology has at most two orientations and the other middle deck has only
> one boundary replacement of freedom.

This rules out bulk repair by time-labelled switches or by ordinary
slotwise deck fibers.  It does not prove that every legal palette core is
rigid.  The exceptional chorded fraction in (4.4), although exponentially
small as a probability in `n`, still contains many paths because the raw
palette is enormous.  An integral construction could deliberately seek such
rare switch-rich paths.  Nor does the argument cover a global recomposition
that preserves the union of all first-parity resources while reassigning
those resources between block slots.  Either possibility would require a new
simultaneous common-path theorem; neither is supplied by the present
fractional matching.

## 7. Finite audit

All finite checking was run on `ssh h100`, not on the local machine.  An
exhaustive replay of 130,134 small legal tail-MTF paths found 16,592
nonconsecutive short-lag Johnson adjacencies.  Every one occurred only at
`k=f-1` and had exactly the forced shift-one, recurrence-gap-`f` form in
Lemma 4.1.  Separate enumeration of the two-way and `d`-way gadgets confirmed
(5.2), the loss of the `q_1` branch, and the rank-`f-1` collision on every
attempt to concatenate two gadgets.  These checks audit the formulas; the
proofs above do not depend on them.
