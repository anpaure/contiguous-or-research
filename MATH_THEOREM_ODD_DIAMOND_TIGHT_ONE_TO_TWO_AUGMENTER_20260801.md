# A tight one-to-two augmenter for the odd Boolean-diamond selector

Date: 2026-08-01  
Lane: protected odd owner synchronization / exact absorption  
Status: unconditional local augmenter and exact candidate count.  A global
augmenting-tree or absorber-packing theorem is not claimed.

## 0. Outcome

Work on a ground set `Omega` of size `2m-1`, with `m>=3`, and with lower, owner and upper
ranks `m-1,m,m+1`.  Clone every owner into two labelled capacity slots.

For every target upper colour `R`, there are exactly

\[
 16(m+1)m(m-2)(m-1)                                      \tag{0.1}
\]

labelled configurations with the following property.  One auxiliary
diamond `f` can be replaced by the target diamond `e` and a rerouted copy
`g` of the same auxiliary upper colour.  Every resource used by `f` is
still used after the replacement, and the replacement consumes exactly

* one new lower resource; and
* two new owner-slot resources.

Thus, after charging the newly covered upper target, it uses exactly the
three additional capacity resources forced by adding one hyperedge.  The
full new-vertex set also contains that target upper vertex.  If the three
capacity resources are free in a current owner-slot
matching, the replacement is an augmenting move of size `1 -> 2`.

This gives a literal absorption primitive for upgrading the protected
`o(W)`-defect matching.  The remaining theorem is global: arrange that every
unmatched upper colour reaches one of its augmenters whose auxiliary edge
is selected and whose three extra resources are free, possibly through an
alternating augmenting tree.  The local supply is polynomially large and a
fixed `o(m)` protected bank removes only a vanishing fraction of it.

## 1. The owner-slot host

For an upper set `R`, a lower set `L subset R` with `|R-L|=2`, and the two
middle owners `T,H` between them, an owner-slot hyperedge is

\[
                 \{R,L,T^i,H^j\},\qquad i,j\in\{0,1\}. \tag{1.1}
\]

A matching in this four-uniform host has distinct upper colours, distinct
lower colours, and physical owner degree at most two.

## 2. The tight augmenter

Fix a target upper set `R`.  Choose ordered distinct `a,b in R`, put

\[
                         L=R-\{a,b\},                 \tag{2.1}
\]

choose `c notin R`, and choose `x in L`.  Define

\[
\begin{array}{lll}
 A=L+\{a\},&B=L+\{b\},&C=L+\{c\},\\
 L'=(L-\{x\})+\{c\},&&D=(L-\{x\})+\{a,c\},          \tag{2.2}
\end{array}
\]

and let the auxiliary upper colour be

\[
                         S=L+\{a,c\}.                 \tag{2.3}
\]

Choose arbitrary owner slots `i,j,p,q in {0,1}`.  Consider the three
hyperedges

\[
\begin{aligned}
 f&=\{S,L,A^i,C^j\},\\
 e&=\{R,L,A^i,B^p\},\\
 g&=\{S,L',C^j,D^q\}.                                \tag{2.4}
\end{aligned}
\]

### Theorem 2.1 (tight one-to-two augmentation)

The singleton family `M^-={f}` and the two-edge family `M^+={e,g}` are
matchings.  Moreover

\[
                 V(M^- )\subset V(M^+),              \tag{2.5}
\]

and the new resource vertices, apart from the newly covered upper colour
`R`, are exactly

\[
                         L',\quad B^p,\quad D^q.       \tag{2.6}
\]

Consequently, if a matching contains `f`, omits `R`, and the three vertices
in (2.6) are free, replacing `f` by `e,g` increases its size and its number
of covered upper colours by one while retaining lower capacity one and
owner capacity two.

#### Proof

The target diamond has interval

\[
 L\subset A,B\subset R,
\]

because `R=L+{a,b}`.  The off diamond has interval

\[
 L\subset A,C\subset S,
\]

because `S=L+{a,c}`.  Finally

\[
 S-L'=\{a,x\},
\]

so the two middle owners of the rerouted auxiliary diamond are

\[
                         S-\{a\}=C,
 \qquad                  S-\{x\}=D.                 \tag{2.7}
\]

Thus all three displayed sets in (2.4) are legal hyperedges.

The two on-edges have different upper colours `R,S` and different lower
colours `L,L'`.  Their four physical owners are `A,B,C,D`.  These are
pairwise distinct: `A,B,C` adjoin three distinct exterior labels to `L`,
while `D` deletes `x` from `L` and adjoins `a,c`.  Hence `M^+` is a
matching for every choice of slots.  The resource vertices of `f` are
`L,A^i,C^j`, all retained respectively by `e,e,g`; its upper vertex `S` is
retained by `g`.  The only additional vertices are precisely `R` and
(2.6), proving (2.5)--(2.6).  \(\square\)

### Corollary 2.2 (information-theoretic sharpness)

Any augmentation from `t` owner-slot hyperedges to `t+1` hyperedges uses
one more lower vertex and two more owner-slot vertices.  Theorem 2.1 meets
this lower bound with equality.

## 3. Exact supply through one target

For fixed `R`, the parameters have the following independent choices:

\[
 (a,b):(m+1)m,\qquad c:m-2,\qquad x:m-1,
 \qquad(i,j,p,q):16.                                  \tag{3.1}
\]

The tuple is recoverable from its labelled configuration: `A=R-b`
recovers `b`, `B=R-a` recovers `a`, then `C=L+c` recovers `c`, and
`L'=L-x+c` recovers `x`.  Hence there is no overcount, proving (0.1).

For any fixed resource vertex other than `R`, at most `O(m^3)` of these
configurations use it.  Therefore a forbidden protected bank of `o(m)`
vertices removes only `o(m^4)` of the `Theta(m^4)` configurations.  In
particular a fixed repaired pivot bank of size `O(sqrt(m))` leaves
`(1-o(1))` of the local augmenters available.

## 4. Exact physical-forest condition

Project owner slots to physical owners.  The off edge is the physical edge
`AC`; the on edges are `AB` and `CD`.  Let `F` be a physical linear forest
containing `AC`.  After deleting `AC`, the augmented support

\[
                         F-AC+AB+CD                  \tag{4.1}
\]

is a linear forest exactly when

1. the free degree capacities at `B,D` admit the two new incidences; and
2. adding `AB` and `CD` successively joins different components of
   `F-AC`.

This is a two-query union--find test.  Thus topology is not automatic, but
it is a literal constant-size guard on the same augmenter; no additional
palette resource is needed.

This guard is exact for one move.  It is not closed under parallel use:
several individually safe augmenters may jointly close a longer cycle.
For a simultaneous round one must test the final graphic inequalities, or
equivalently delete every switched old edge, contract the remaining forest
components, and require all new edges to be graphic-independent in the
quotient.

### Corollary 4.1 (the Catalan component count is automatic)

If `F` is a spanning physical forest with `t` edges and the guard above
passes, the augmented forest has `t+1` edges and therefore one fewer
component.  In particular, starting with an upper/lower/slot-compatible
forest that misses `s` upper colours and has `U-s` edges, any sequence of
`s` guarded augmentations ends with exactly

\[
                         W-U=\operatorname {Cat}_m
\]

components.  No separate component-count correction is required; only the
existence of the guarded augmenting sequence remains.

## 5. Revised absorption target

Let `M` be a protected near-perfect owner-slot matching.  Form a directed
alternating graph whose unmatched upper vertices are sources, whose
selected auxiliary edges are switch vertices, and whose free lower/slot
triples are sinks.  Theorem 2.1 supplies `Theta(m^4)` labelled source-to-
switch incidences per missing upper before current-occupancy restrictions.

An exact synchronization theorem now follows from either of the following
concrete statements.

* **Direct augmentation:** every nonempty unmatched shore has one source
  with a selected compatible `f` and all three vertices (2.6) free.
* **Alternating expansion:** every source family has enough vertex-disjoint
  paths in the augmenter graph to the free-resource sink bank.

The second is the natural robust form.  It must be proved with the actual
Boolean incidence and slot correlations; raw `Theta(m^4)` menu size alone
does not imply it.  This note closes the local absorber algebra, not that
global expansion theorem.
