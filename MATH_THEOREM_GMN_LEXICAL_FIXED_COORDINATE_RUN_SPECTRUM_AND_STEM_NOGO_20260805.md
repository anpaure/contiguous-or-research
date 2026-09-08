# GMN lexical fixed-coordinate run spectrum and the protected-stem no-go

**Date:** 2026-08-05  
**Method:** pure mathematics; exact use of the Gregor--Mütze--Nummenpalo
lexical factor and its published six-cycle switches; no computation or
search  
**Status:** proof-safe obstruction to the canonical lexical protected-spacing
route

## 0. Result

Let `G_n` be the middle-levels graph on bitstrings of length `2n+1`, and
let

\[
                       \mathcal C_n=M\cup N
\]

be the Gregor--Mütze--Nummenpalo (GMN) two-factor obtained from the
`(n-1)`- and `n`-lexical matchings.  Distinguish the last coordinate

\[
                           z=2n+1.
\]

Delete the factor edges that flip `z`, take the `z=0` half, and suppress
the rank-`(n+1)` vertices.  The resulting rank-`n` Johnson path factor has
exactly `Cat_n` components, but their owner lengths are not constant.
Their exact spectrum is

\[
 \boxed{
   \#\{\text{paths with }2h\text{ owners}\}
      =\operatorname {Cat}_{h-1}\operatorname {Cat}_{n-h},
      \qquad 1\le h\le n . }
                                                        \tag{0.1}
\]

In particular the average owner length is `n+1`, but this is only an
average.  If `s=s(n)` tends to infinity and `s=o(n)`, then

\[
 {1\over\operatorname {Cat}_n}
 \#\{\text{paths with fewer than }s\text{ Johnson edges}\}
                         \longrightarrow {1\over2}.    \tag{0.2}
\]

The initial chronology is much more rigid.  If `a(x)` is the initial
ascent length of the Dyck word indexing a path, then the longest initial
Johnson geodesic has exactly `a(x)` edges, and

\[
 \boxed{
   \#\{x\in\mathcal D_n:a(x)\ge s\}
      ={s+1\over n+1}{2n-s\choose n}. }
                                                        \tag{0.3}
\]

Consequently its proportion is at most `(s+1)2^{-s}`.  For
`s=Theta(sqrt(n))`, only an exponentially small (in `sqrt(n)`) fraction of
the lexical paths even has the required initial geodesic.

The obstruction survives the GMN Hamiltonization.  Every published
six-cycle pull is an equal-depth suffix exchange between two `z=0` paths.
It transposes their path lengths.  The noninterleaving theorem for several
pulls makes these transpositions composable.  Thus **every Hamilton cycle
obtained from the lexical factor by the GMN pairwise edge-disjoint pull
family has the same multiset (0.1) of `z`-free run lengths.**

It follows that this canonical family cannot realize a protected
half-projection with `Cat_n-1` distinct initial stems of length
`s=Theta(sqrt(n))`: asymptotically half of its `Cat_n` projected components
are shorter than one such stem.  This remains a no-go when the stems are
chosen after the pull tree (the reverse-quantifier formulation).

There is a second, literal obstruction for the canonical prefix-pull
spanning tree.  Every one of its gluing six-cycles deletes the first old
edge on each of its two incident `z=0` paths.  Hence no nonempty prefix-pull
tree preserves preselected nontrivial initial stems on all incident paths.

This note refutes only the canonical lexical/pull route.  It does not rule
out a nonlexical middle-levels Hamilton cycle with balanced `z`-runs, nor a
different switch family which changes the run spectrum.

## 1. The exact fixed-coordinate path factor

Write `D_n` for the Dyck words of semilength `n`.  Proposition 2 of GMN
states that, after deleting the edges of `mathcal C_n` which flip the last
bit, the factor is

\[
       (\mathcal P_n\circ0)\ \dot\cup\
       (\operatorname {rev}(\mathcal P_n)\circ1),      \tag{1.1}
\]

where `mathcal P_n` contains one path `P_sigma(x)` for every
`x in D_n`.

Use the canonical first-return decomposition

\[
                 x=1u0v,
 \qquad u\in\mathcal D_{h-1},\quad
        v\in\mathcal D_{n-h}.                         \tag{1.2}
\]

The GMN bit-flip recursion gives

\[
                       |\sigma(x)|=2|u|+2=4h-2.       \tag{1.3}
\]

The path starts and ends on the rank-`n` shore.  Suppressing its
rank-`(n+1)` vertices therefore gives a Johnson path with

\[
                 {4h-2\over2}=2h-1
                 \quad\hbox{edges, and}\quad 2h
                 \quad\hbox{owners}.                 \tag{1.4}
\]

For fixed `h`, the two Dyck factors in (1.2) can be chosen in

\[
                \operatorname {Cat}_{h-1}
                \operatorname {Cat}_{n-h}             \tag{1.5}
\]

ways.  This proves (0.1).  Summing (1.5) over `h` is the Catalan
convolution and gives `Cat_n` paths.  Since the paths partition the complete
rank-`n` shore of the `2n`-cube,

\[
 \sum_{h=1}^n
       2h\operatorname {Cat}_{h-1}\operatorname {Cat}_{n-h}
       ={2n\choose n}.                                \tag{1.6}
\]

Dividing by

\[
             \operatorname {Cat}_n={1\over n+1}{2n\choose n}
\]

shows that the average owner length is exactly `n+1`.

### Corollary 1.1 (half the lexical runs are submacroscopic)

Let `H=H(n)` satisfy `H to infinity` and `H=o(n)`.  Then

\[
 {1\over\operatorname {Cat}_n}
 \sum_{h=1}^{H}
       \operatorname {Cat}_{h-1}\operatorname {Cat}_{n-h}
                         \longrightarrow {1\over2}.    \tag{1.7}
\]

Indeed, uniformly for `h<=H`, the Catalan asymptotic gives

\[
 {\operatorname {Cat}_{n-h}\over\operatorname {Cat}_n}
                         =4^{-h}(1+o(1)).              \tag{1.8}
\]

Consequently the left side of (1.7) tends to

\[
 \sum_{h\ge1}{\operatorname {Cat}_{h-1}\over4^h}
       ={1\over4}\,C(1/4)={1\over2},                 \tag{1.9}
\]

where `C(t)` is the Catalan generating function.  Taking
`H=floor((s-1)/2)` proves (0.2), with an immaterial endpoint convention.

The average `n+1` in (1.6) is therefore produced by a U-shaped spectrum:
roughly half of the components live near the short boundary `h=o(n)` and
roughly half near the long boundary `n-h=o(n)`.  It is not evidence for a
uniform-run theorem.

## 2. Exact initial-geodesic aperture

For a Dyck word `x`, let

\[
                  a(x)=\max\{a:x_1=\cdots=x_a=1\}     \tag{2.1}
\]

be its initial ascent length.  Match each of these initial upsteps to its
Dyck closing downstep.  Denote the closing positions, from outside to
inside, by

\[
                         b_1,b_2,\ldots,b_{a(x)}.
\]

Repeated application of the defining recursion for `sigma` gives the exact
prefix

\[
 \sigma(x)=
 (b_1,1,b_2,2,\ldots,b_{a(x)},a(x),
  a(x)-1,b_{a(x)},\ldots).                            \tag{2.2}
\]

The displayed first `2a(x)` labels are pairwise distinct.  In the
suppressed Johnson path they perform the exchanges

\[
                         i\longmapsto b_i,
                   \qquad 1\le i\le a(x),             \tag{2.3}
\]

so the first `a(x)` edges form a geodesic.  Unless the path ends there, the
next exchange reinserts `a(x)-1` and deletes `b_{a(x)}`.  It reduces the
Johnson distance from the initial owner, so the geodesic cannot be
extended.  In the one-edge terminal case the same conclusion is immediate.
Thus the longest initial Johnson geodesic has exactly `a(x)` edges.

The number of Dyck words beginning with `s` upsteps is the standard ballot
number

\[
             A_{n,s}={s+1\over n+1}{2n-s\choose n}.   \tag{2.4}
\]

For completeness, after the initial `s` upsteps the path starts at height
`s`, uses `n-s` further upsteps and `n` downsteps, and stays nonnegative.
The reflection principle gives (2.4).  Dividing by `Cat_n` gives

\[
 {A_{n,s}\over\operatorname {Cat}_n}
   =(s+1){\binom{2n-s}{n}\over\binom{2n}{n}}
   =(s+1)\prod_{j=0}^{s-1}{n-j\over2n-j}
   \le (s+1)2^{-s}.                                  \tag{2.5}
\]

This proves (0.3) and the claimed `s=Theta(sqrt(n))` estimate.

## 3. Pulls preserve the run-length spectrum

Consider a GMN flippable pair `(x,y)` whose flippable substring starts at
position `a`.  In the notation of equations (8a)--(8c) of GMN, the old
bit-flip words are

\[
 \begin{aligned}
 \sigma(x)&=(\alpha,b,a,a+2,a+1,a,a+2,\gamma),\\
 \sigma(y)&=(\alpha,a+1,a,\delta),
 \end{aligned}                                        \tag{3.1}
\]

and toggling the gluing six-cycle replaces them by

\[
 \begin{aligned}
 \tau(x)&=(\alpha,a+2,a,\delta),\\
 \tau(y)&=(\alpha,b,a,a+1,a+2,a,a+1,\gamma).
 \end{aligned}                                        \tag{3.2}
\]

Therefore

\[
                     |\tau(x)|=|\sigma(y)|,
 \qquad              |\tau(y)|=|\sigma(x)|.          \tag{3.3}
\]

In words, the switch exchanges the two terminal suffixes at the same path
depth.  It transposes the two cube-path lengths, and therefore also the two
suppressed Johnson owner lengths.

GMN Proposition 3(iii) says that all of their gluing six-cycles are
edge-disjoint.  Proposition 3(iv) says that, when several switches use the
same original path, their two-edge intervals are nested/noninterleaved.
There is also a direct order-free way to see what their simultaneous
symmetric difference does.  Give every edge of every original path its
longitudinal index from the Dyck start.  In (3.1)--(3.2), the continuation
`delta` begins after `|alpha|+2` edges both before and after it is transferred
from the `y`-strip to the `x`-strip.  Similarly, the continuation `gamma`
begins after `|alpha|+6` edges both before and after it is transferred from
the `x`-strip to the `y`-strip.  Thus the switch crosses the two path strips
without translating the longitudinal coordinate of either transferred
continuation.

Trace any old terminal endpoint backwards through the simultaneous switch
network.  Edge-disjointness makes the trace unambiguous, and
noninterleaving prevents a local strip from branching.  Every crossing
preserves its longitudinal coordinate.  Hence an endpoint formerly at
distance `L` is still at distance `L` from whichever Dyck start receives
it.  The switches merely permute the terminal endpoints together with their
length labels.  Equivalently, one may process the noninterleaving strips
from their terminal end backwards; each processed switch applies the
transposition (3.3).  This proves:

### Theorem 3.1 (lexical pull-spectrum invariance)

For every admissible GMN pull family `T_n subseteq S_n`, the `z=0`
path factor of

\[
                    \mathcal C_n\mathbin\triangle T_n
\]

has the same owner-length multiset (0.1) as the original lexical factor.
In particular this holds when the pull family corresponds to a spanning
tree of the plane-tree auxiliary graph and the symmetric difference is a
Hamilton cycle.

The switches may permute which Dyck start receives which run length.  They
cannot change the spectrum.

### Corollary 3.2 (Catalan-scale protected spacing is impossible here)

Let `s=Theta(sqrt(n))`.  Every Hamilton cycle obtained by the canonical GMN
pull construction has

\[
                  (1/2-o(1))\operatorname {Cat}_n     \tag{3.4}
\]

`z`-free projected components with fewer than `s` Johnson edges.  Hence it
cannot have `Cat_n-1` distinct `z`-free runs, each containing a prescribed
length-`s` initial stem.  This conclusion is independent of when the stems
are selected.

## 4. The canonical prefix-pull family hits every incident prefix

The streamlined canonical spanning-tree proof uses pullable trees

\[
                       x=110u0v,
 \qquad                p(x)=101u0v.                  \tag{4.1}
\]

This is the `a=1` case of the general GMN flippable pair.  Proposition
3(ii) states that its six-cycle intersects `P_sigma(x)` in old edges `1`
and `6`, and intersects `P_sigma(p(x))` in old edge `1`.  In particular the
switch deletes the first old edge of both incident `z=0` paths.

Thus a nontrivial initial projected stem on either incident path is not
preserved.  Any spanning pull tree which joins more than one lexical factor
cycle uses at least one such switch, so the canonical prefix-pull tree
cannot simultaneously satisfy

\[
 \text{``every pull old phase lies beyond every incident initial stem.''}
                                                               \tag{4.2}
\]

The larger GMN catalogue includes flippable substrings with `a>1`; those
can lie beyond a fixed short prefix.  However, the published connectivity
argument proves connectivity of the unrestricted plane-tree pull graph,
not of the graph obtained by imposing `a>s` at every protected rooted
occurrence.  More importantly, Theorem 3.1 and Corollary 3.2 already rule
out the required `Cat_n-1` long-run bank even if such a restricted spanning
tree existed.

## 5. Consequence for the current protected half-projection route

The middle-levels half-projection theorem requires, for a Catalan collar
bank, `Cat_n-1` distinct `z`-absent runs of owner length at least `s+1`, one
for each prescribed initial stem.  The GMN lexical construction supplies a
perfectly explicit half-projection, but (0.1) and (3.4) show that it misses
this run requirement by order `Cat_n`, not by a bounded or lower-order
defect.

Therefore the next positive theorem cannot be obtained by merely choosing
a more careful spanning tree inside the same canonical lexical pull family.
At least one of the following must change:

1. the base middle-levels factor;
2. the switch family, so that it can change the fixed-coordinate run
   spectrum rather than only permute it; or
3. the depuncturing architecture, so that it no longer asks for one long
   initial stem in all but one of the Catalan components.

This is the sharp obstruction delivered by the lexical route.

## 6. Scope and sources

Used exactly:

* GMN Proposition 2(i)--(iv), especially
  `|sigma(x)|=2|u|+2` for `x=1u0v`;
* GMN Proposition 3(i)--(iv), especially the explicit words `sigma,tau`
  and the edge-disjoint/noninterleaving statements; and
* the canonical prefix-pull formulation `x=110u0v -> 101u0v` from the
  streamlined book proof.

The note proves an exact obstruction for the distinguished last-coordinate
cut of the lexical construction.  That one coordinate already refutes the
claim that the canonical factor automatically has uniformly balanced
fixed-coordinate runs.  No assertion is made here that every coordinate
cut of an arbitrary nonlexical Hamilton cycle has this spectrum.
