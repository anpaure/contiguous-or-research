# Context-path rail squares have an exact ticket-degree invariant

**Date:** 2026-08-13  
**Status:** unconditional obstruction for every nonnegative union of the
literal adjacent-transposition rail squares; local owner-set-preserving
rewiring no-go.  This does not rule out a larger compound gadget with new
auxiliary owners.

## 1. One rail square and its endpoint tickets

Fix distinct labels `x,p`.  A context is an `(R-1)`-set avoiding them.
Let `A,B` be contexts with

\[
             |A\cap B|=c,
             \qquad R=c+q.                          \tag{1.1}
\]

Put

\[
 D=A\cap B,\qquad A_0=A\setminus D,qquad B_0=B\setminus D,
 \qquad |A_0|=|B_0|=q-1.                            \tag{1.2}
\]

The literal adjacent-transposition rail square uses the cyclic orders

\[
        (A_0,x,p,B_0,\omega),
        \qquad (A_0,p,x,B_0,\omega),                 \tag{1.3}
\]

on the toggle ground `[k]-D`.  Its two owner currents differ by

\[
                         \delta_{xp}(A)-\delta_{xp}(B).          \tag{1.4}
\]

The next observation is independent of the filler order `omega`.

### Lemma 1.1 (forced endpoint tickets)

In **each** state of (1.3), the immediate-lower palette contains the two
named targets

\[
                              A,\qquad B,              \tag{1.5}
\]

exactly once.  Its immediate-upper palette contains

\[
                 A\cup\{x,p\},qquad B\cup\{x,p\}     \tag{1.6}
\]

exactly once.

#### Proof

The block `A_0` is a cyclic `(q-1)`-window immediately beside the
adjacent pair `x,p`, and the block `B_0` is the corresponding window on
the other side.  Adjoining the core `D` gives (1.5).

The two cyclic `(q+1)`-windows at the same boundaries are

\[
                          A_0\cup\{x,p\},qquad
                          B_0\cup\{x,p\},              \tag{1.7}
\]

and adjoining `D` gives (1.6).  Interchanging `x,p` changes neither set.
Within one pure rail every proper cyclic window has a unique start, so
each displayed ticket occurs once.  `square`

## 2. The context-degree invariant

Let `H` be any finite context multigraph whose edges satisfy (1.1).  On
each edge choose either orientation and either state of its literal rail
square.  Let `P_low(H)` and `P_up(H)` be the resulting aggregate named
immediate palettes, with multiplicity.

> **Theorem 2.1 (ticket degree equals context degree).**  For every
> context vertex `G`,
> \[
>   \operatorname{mult}_{P_{\rm low}(H)}(G)=\deg_H(G),           \tag{2.1}
> \]
> and
> \[
>   \operatorname{mult}_{P_{\rm up}(H)}(G\cup\{x,p\})
>       =\deg_H(G).                                  \tag{2.2}
> \]
> In particular, if either aggregate named palette must be simple, then
> \[
>                              \Delta(H)\le1.          \tag{2.3}
> \]

#### Proof

By Lemma 1.1, every edge incident with `G` contributes one copy of `G`
and one copy of `G+x+p`, in either orientation and in either switch state.
No edge not incident with `G` contributes these endpoint tickets under
the endpoint labelling being counted.  Contributions are nonnegative, so
they add to the degree.  Simplicity gives (2.3).  `square`

### Corollary 2.2 (cycles and braids do not cure the seam)

A path with an internal context repeats both of its forced seam tickets.
An Eulerian cycle repeats every such ticket at least twice.  More
generally, no nonnegative union of complete literal path squares whose
context graph has a vertex of degree at least two has a simple named
immediate-lower or immediate-upper palette.

Changing edge orientations, alternating the two switch states, or
pairing paths into cycles cannot cancel the repetitions.  The endpoint
tickets are identical in both states and palette incidence is
nonnegative.

Thus the context-current telescope

\[
 \sum_i\bigl(\delta_{xp}(G_i)-\delta_{xp}(G_{i+1})\bigr)
        =\delta_{xp}(G_0)-\delta_{xp}(G_t)            \tag{2.5}
\]

is exact in the owner current but is not a telescope in either immediate
palette.

## 3. Existing seam owners cannot be rewired to remove both repetitions

One might try to cut the two rail cycles at an internal context and
re-pair their existing owner occurrences rather than take their disjoint
union.  Even that cannot make both forced tickets simple without adding
new owners.

Let `G` be the internal context and put

\[
                              U=G\cup\{x,p\}.          \tag{3.1}
\]

On one fixed shore, the two context endpoints are

\[
                              P=G\cup\{p\},qquad
                              X=G\cup\{x\}.            \tag{3.2}
\]

On the outer sides of the seam the two rails have common-deck neighbours

\[
                              K=G\cup\{a\},qquad
                              K'=G\cup\{b\},           \tag{3.3}
\]

for filler labels `a,b` outside `U`.  On their inner sides they have
common-deck neighbours

\[
                              I=U\setminus\{r\},qquad
                              I'=U\setminus\{s\},      \tag{3.4}
\]

for `r,s in G`.  If any of the six displayed owners coincide, owner
simplicity has already failed, so assume they are distinct.

Cut the four original seam arcs while keeping the exterior half-edges at
`K,K',I,I'` fixed.  In a replacement degree-two Johnson subgraph, the
four boundary owners need one new seam edge each, while `P,X` need two
each.  Hence the seam must contain four new edges.

### Lemma 3.1 (two-clique seam obstruction)

Every Johnson edge among the six existing seam owners lies in one of the
two cliques

\[
                         \{P,X,K,K'\},                \tag{3.5}
\]

whose every edge has lower intersection `G`, or

\[
                         \{P,X,I,I'\},                \tag{3.6}
\]

whose every edge has upper union `U`.  Consequently every degree-two
rewiring with the exterior fixed uses at least two edges with lower ticket
`G` or at least two edges with upper ticket `U`.

#### Proof

The four owners in (3.5) are exactly `G` plus one exterior label, so they
form the lower clique and every pair has intersection `G`.  The four in
(3.6) are exactly `U` minus one label, so they form the upper clique and
every pair has union `U`.

For an outer and an inner owner,

\[
 (G+a)\setminus(U-r)=\{r,a\},
 \qquad (U-r)\setminus(G+a)=\{x,p\}.                 \tag{3.7}
\]

Their Johnson distance is two, so there is no cross-clique edge.  The
only overlap of the two cliques is the edge `PX`, which simultaneously
has lower ticket `G` and upper ticket `U`.

The seam needs four edges by the degree count above.  If `G` and `U` were
each used at most once, at most one edge could be selected from each
clique, hence at most two seam edges in total (and selecting `PX` only
reduces that union).  This contradicts the required four.  `square`

### Corollary 3.2 (owner-set-preserving splicing no-go)

No local reconnection of the six existing seam owners, with the exterior
rail remnants fixed, simultaneously makes the lower ticket `G` and upper
ticket `G+x+p` simple.  A successful seam braid must introduce auxiliary
owners, change the exterior remnants, use occurrence copies accepted by
the compiler, or abandon one of the named-palette simplicity demands.

## 4. Exact consequence for Gate A

The balanced multicommodity context identity remains a useful owner-level
normal form.  What this theorem rules out is the most direct proposed
closure:

\[
 \boxed{\text{arrange the existing path squares into Eulerian cycles or
 braids and let their endpoint tickets cancel}.}
\]

They do not cancel.  Their multiplicities are the context degrees.

The next viable construction must replace each degree-two context seam by
a genuinely larger compound gadget whose new owner set carries a simple
lower/upper ticket ledger in both switch states.  Lemma 3.1 shows that a
mere permutation of the existing seam edges is insufficient.  No
invariant here rules out such an auxiliary-owner gadget; constructing it,
maintaining residence and the all-width current, and packing all
commodities owner-disjointly remain the exact open rows.
