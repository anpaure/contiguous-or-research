# Full-aperture long cells are rigid: upper completion is a chronology theorem

**Date:** 2026-08-13  
**Status:** unconditional coordinatewise theorem  
**Scope:** every flat depth-`d` antecedent of the full-aperture owner
chronology, not only the maximal cyclic-interval antecedent

## 1. The one-coordinate inversion normal form

Put

\[
 k=2m+1,\qquad R=m+1,\qquad q=d+1,
 \qquad a=m-q+2.                                      \tag{1.1}
\]

Fix one full-aperture owner component in cyclic order.  For a ground
coordinate `x`, its owner trace is a cyclic block

\[
                  1^{m+1}0^m.                       \tag{1.2}
\]

Let `b_i` be any Boolean source trace satisfying

\[
  \bigvee_{j=0}^{q-1}b_{i+j}=1
  \quad\Longleftrightarrow\quad
  \text{the owner at start }i\text{ contains }x.     \tag{1.3}
\]

There is a unique cyclic interval `E_x` of source positions at which
`b_i` is allowed to be one.  Its length is

\[
              |E_x|=(m+1)-q+1=a.                    \tag{1.4}
\]

### Lemma 1.1 (exact flat inverse)

After cutting at the zero run and writing

\[
 E_x=\{0,1,\ldots,a-1\},
\]

the supports of the source traces satisfying (1.3) are exactly the sets

\[
 F=\{f_0=0<f_1<\cdots<f_s=a-1\}
 \quad\text{with}\quad f_{j+1}-f_j\le q.             \tag{1.5}
\]

#### Proof

Every source one is contained in each of the owner windows that cover its
position.  It must therefore lie in the intersection of the positive
owner run eroded by `q-1` at its two ends, which is `E_x` and has length
(1.4).

The first positive owner window meets `E_x` only at its left endpoint,
so that endpoint is forced.  The last positive owner window similarly
forces the right endpoint.  An internal owner window is zero-free exactly
when it lies strictly between two consecutive source ones at distance
greater than `q`.  Thus every gap is at most `q`.  Conversely, the two
forced endpoints and the gap condition hit every positive `q`-window,
while support inside `E_x` creates no one in a zero owner window.  This is
equivalent to (1.3). `square`

## 2. Every long cell is immutable

Let `C` be a proper cyclic interval of source positions.  Write

\[
 U_C=\{x:C\cap E_x\ne\varnothing\}.                 \tag{2.1}
\]

Thus `U_C` is the union obtained from the maximal antecedent.  Let `M_C`
be the set of coordinates which occur in the union over `C` for **every**
antecedent inducing the fixed owner chronology.

### Theorem 2.1 (long-cell rigidity)

If

\[
                         |C|\ge q,                  \tag{2.2}
\]

and `C` is a proper cyclic interval, then

\[
                         \boxed{M_C=U_C}.            \tag{2.3}
\]

Consequently every source antecedent inducing the same owner chronology
has exactly the same union on `C`.

#### Proof

Fix `x in U_C`, so `C cap E_x` is nonempty.  If this intersection contains
the left or right endpoint of `E_x`, then
Lemma 1.1 forces a source occurrence of `x` in `C`.

Otherwise the connected proper cyclic interval `C` lies strictly inside
`E_x` (after cutting the cycle outside `C union E_x`).  Its full length is at least
`q`.  If an admissible support avoided `C`, the last support point before
`C` and the first support point after `C` would be separated by at least
`|C|+1>q`, contradicting (1.5).  Hence every admissible support meets
`C`, and `x in M_C`.

This proves `U_C subseteq M_C`; the reverse containment is tautological.
`square`

### Corollary 2.2 (the entire proper upper deck is fixed)

For the cyclic-interval maximal antecedent

\[
 P_i=I_i^a,
\]

one has, for every `ell>=q` before the full-ground row,

\[
 \bigcup_{j=0}^{\ell-1}P_{i+j}
       =I_i^{a+\ell-1}.                             \tag{2.4}
\]

Theorem 2.1 says that (2.4) remains the literal union for **every** flat
antecedent giving the same owners.  In particular the immediate-upper row
`ell=q+1` is immutable:

\[
                      I_i^{m+2}.                    \tag{2.5}
\]

Thus no lower-flag choice, source-letter capping, CNF compiler solution,
or common-cap routing can introduce an immediate-upper target absent from
the cyclic `(m+2)`-interval deck.

The same proof applies to both shores of the even full-aperture factor,
with their corresponding safe intervals.

## 3. Sharp contrast with strict-lower cells

For `1<=ell<q`, avoiding an internal intersection of length `ell` is
possible: place source ones immediately on its two sides, whose distance
is at most `q`.  Hence only safe-interval endpoints are forced.  In the odd
full-aperture normal form this recovers

\[
 U_C=I_i^{m-q+\ell+1},\qquad
 M_C=I_i^\ell\mathbin{\dot\cup}I_{i+a-1}^\ell.      \tag{3.1}
\]

This explains the exact dichotomy:

\[
 \boxed{
 \begin{array}{c|c}
 |C|<q&\text{lower cells have capping freedom}\cr
 |C|\ge q&\text{owner and upper cells are chronology-rigid.}
 \end{array}}                                      \tag{3.2}
\]

In particular, the singleton obstruction for the unchanged full-aperture
chronology and the immediate-upper obstruction have different causes but
cannot repair one another.

## 4. Consequence for the global proof

For odd `k`, an owner chronology which is simultaneously

1. exact on rank `m+1` owners,
2. exact on rank `m` consecutive intersections, and
3. surjective on rank `m+2` consecutive unions,

is exactly the first global chronology demanded by the full-aperture
route.  On a connected chronology this is the lower-exact/upper-surjective
**double-turn Middle Levels cycle** condition.

The canonical MSW factor satisfies Items 1--2 componentwise but has an
explicit `Omega(W/m)` immediate-upper defect.  By Corollary 2.2 that defect
is invariant under every subsequent choice of a flat antecedent.  Therefore
the proof must select a globally different wreath factor or perform a
Catalan-scale owner rethread; it cannot postpone upper completion to the
lower compiler or cap router.

This theorem does not prove the double-turn cycle.  It proves that, inside
the full-aperture architecture, an equivalent chronology-level theorem is
necessary rather than merely sufficient.
