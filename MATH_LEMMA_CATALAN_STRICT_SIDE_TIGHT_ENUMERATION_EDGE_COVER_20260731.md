# Strict punctured sides are tight enumerations with an anchor edge cover

Date: 2026-07-31  
Status: exact all-`n` equivalence inside the fixed-Hamilton-cycle subclass;
no existence theorem for the required cycle/common-basis correlation.

## 0. Result

The strict-extremal side normal form has a simpler description than an
arbitrary prescribed anchor pairing.

Let `H` be a Hamilton cycle on the rank-`(n+1)` owners.  Select `P` edges
whose union/intersection occurrence pairs form an upper-saturating matching,
and call the other `N-P` edges **direct**.  For a prescribed `C`-set `B` of
seam anchors, the selected edges form a strict side forest—anchor degree at
most one and every nonanchor degree exactly two—if and only if the direct
edges have vertex support exactly `B`.

Thus the strict side problem is not “realize an arbitrary matching of
anchors.”  It is:

> construct an intersection-rainbow tight enumeration whose direct
> same-level steps form an edge cover supported exactly on the inherited
> anchor bank.

The `Cat_n` double-anchor pairings then emerge automatically as the
complementary selected runs.

## 1. Exact equivalence

Use

\[
 N={2n\choose n+1},\qquad P={2n\choose n+2},\qquad
 C={2n\choose n}-{2n\choose n+2},\qquad K=\operatorname{Cat}_n.
\]

Let `J subset E(H)` have order `P`, and assume its occurrence labels

\[
                    (X\cup Y,X\cap Y),\qquad XY\in J,
\]

have every rank-`(n+2)` union once and distinct rank-`n` intersections.
Put

\[
                             D=E(H)\setminus J.        \tag{1.1}
\]

Inserting the upper union on every edge of `J` gives the corresponding
tight enumeration; the edges of `D` are its direct same-level steps.

### Theorem 1.1 (anchor edge-cover equivalence)

For a prescribed anchor bank `B subset V(H)`, `|B|=C`, the following are
equivalent.

1. The selected graph `(V(H),J)` is a strict punctured side forest:
   every `b in B` has selected degree at most one and every
   `v notin B` has selected degree exactly two.
2. The direct graph `(V(H),D)` has vertex support exactly `B`:

   \[
                              V(D)=B.                 \tag{1.2}
   \]

Under these conditions, the direct-degree histogram on `B` is

\[
                 1^{,2K},2^{,C-2K},               \tag{1.3}
\]

the selected side forest consists of `K` paths whose endpoints are the
`2K` direct-degree-one anchors and `C-2K` isolated anchors, and it has no
anchor-free component.

#### Proof

Every owner has degree two in `H`, so

\[
                         d_J(v)+d_D(v)=2.             \tag{1.4}
\]

If the selected side is strict, every nonanchor has `d_J=2` and therefore
`d_D=0`; every anchor has `d_J<=1` and therefore `d_D>=1`.  This is exactly
`V(D)=B`.  Conversely (1.2) and (1.4) give those same strict degree rows.

Since `J` is a proper subset of one cycle, it is a spanning linear forest.
No nonanchor can be an endpoint or isolate because its selected degree is
two.  Hence every nontrivial component has two anchor endpoints and every
isolated component is an anchor.

Write `a_1,a_2` for the numbers of anchors of direct degree one and two.
The direct graph has `|D|=N-P=C-K` edges and support `B`, so

\[
                 a_1+a_2=C,qquad a_1+2a_2=2(C-K).
\]

Solving gives `a_1=2K,a_2=C-2K`, proving (1.3).  The complementary selected
degrees are respectively one and zero, yielding the claimed component
profile. \(\square\)

### Corollary 1.2 (pairings are cyclic-run outputs)

In the strict fixed-cycle subclass, the induced `K`-matching of double
anchors is the endpoint pairing of the `K` selected-edge runs.  In
particular, it is noncrossing in the cyclic order of `H`, and every paired
distance is at most the length of its selected run.

This recovers the metric inequality by summing run lengths.  It also
explains why arbitrary prescribed pairings are the wrong primitive: the
direct anchor edge cover, not the pairing itself, is the local object that
a tight-enumeration construction controls.

## 2. Correct recursive target

For a common deletion basis `Q`, the two inherited anchor banks are

\[
 B^- =\{U_q:q\in Q\},\qquad B^+=\{L_q:q\in Q\}.       \tag{2.1}
\]

A strong sufficient side theorem may therefore be stated without an
arbitrary pairing quantifier:

> Find a Hamilton cycle `H^-` and an occurrence matching on it whose direct
> edge support is exactly `B^-`; dually find `H^+` with direct support
> exactly `B^+`; then choose the two cycles so the complementary selected-run
> pairings and the central partial matching have acyclic union.

The occurrence matching supplies both diagonal palettes, Theorem 1.1
supplies every side degree and component row, and only the final contracted
two-shore forest test remains.

This is stronger than the unrestricted punctured-side theorem but weaker
than realizing every requested anchor pairing.  The GMM implementation does
not satisfy it: its occurrence Hall row already fails from `n=4`, and its
literal direct-step support is smaller than the required anchor bank in the
audited dimensions.  The two-`C6` `n=4` repair proves only that another
marking has enough anchor capacity; choosing direct support equal to the
particular inherited bank remains open.

## 3. Scope

The theorem is a degree/count equivalence and needs no finite inference.
It assumes the upper-saturating intersection-rainbow marking from the
fixed-cycle theorem.  It does not construct that marking, choose the common
basis, correlate the opposite shore, prove the final contracted forest, or
address residence, deeper shadows, and the compiler.
