# The present Boolean-C6 splice is confined to one invariant-core fibre

## Status

The orientation-reversal identity closes the scalar upper-seam deficit and
regenerates the displayed shared collar.  It does not by itself give a
global connector for a long-ring factor.  The reason is exact: every
literal C6 port presently constructed uses three collars with one common
antipodal core, and the regenerated collar has that same core.  Hence a
serial network of these ports is monochromatic in the invariant-core
colouring.

This note proves the resulting lower bound on the number of components
which can remain after using only the current C6 ports.  At critical width
it is exponential.  Thus the shortest additive-constant route needs either
a core-changing zero-charge port, or a stronger joint cover-down whose
connector is not confined to the current common-core C6 class.

No computation or search is used.

## 1. The effective core of a prepared port

Work on a `(2q-1)`-set at owner rank `q` and owner-window width `h`.  A
long antipodal ring has owners

\[
             O_t=J\cup F[t,t+h),\qquad |J|=q-h,
\]

and its invariant core is

\[
                         J=\bigcap_t O_t.
\tag{1.1}
\]

The current three-way C6 collar has one common fixed base of size `q-h`.
In the notation of the abstract splice this is `K union {z}`; in the
ported antipodal-ring notation it is denoted directly by `K`.  Call it
`J` here.

### Lemma 1.1 (a prepared C6 triple has one core)

If three antipodal rings contain the three literal collars of the present
Boolean-C6 port, then all three rings have invariant core `J`.

#### Proof

Each displayed collar contains at least `h+1` consecutive owner phases.
The sealed-collar core theorem says that the intersection of those phases
is the invariant core of its ambient antipodal ring.  In the C6 tensor the
same intersection is the displayed common fixed base `J`.  Hence every one
of the three ambient rings has core `J`. \(\square\)

This is stronger than pairwise owner/root resource disjointness.  Three
resource-disjoint collars with different invariant cores do not form one
of the presently proved C6 ports.

### Lemma 1.2 (the two typed extreme bases already recover the core)

In the explicit antipodal collar, write the two omitted immediate-upper
values as

\[
 \begin{aligned}
 E^R&=B^R\cup\{a_i,a_{i+1},x_i\},\\
 E^L&=B^L\cup\{a_i,a_{i+1},y_i\},
 \end{aligned}                                         \tag{1.4}
\]

where

\[
 B^R=J\cup\{\rho_1,\ldots,\rho_{h-2}\},\qquad
 B^L=J\cup\{\lambda_1,\ldots,\lambda_{h-2}\}.       \tag{1.5}
\]

All displayed label banks are disjoint, and therefore

\[
                         B^R\cap B^L=J.                 \tag{1.6}
\]

Consequently a second collar in the same explicit normal form which
agrees with both *typed* extreme values under the orientation-reversal
identification has the same invariant core `J`.

#### Proof

After the active pair and the typed far token are removed from each value
in (1.4), the two bases are recovered literally.  Their intersection is
`J` by disjointness of the lambda and rho banks.  Equality of both typed
extreme values therefore gives equality of both bases and hence equality
of their intersections.  Lemma 1.1 identifies this intersection with the
ambient ring core. \(\square\)

Thus weakening whole-collar regeneration to equality of the two typed
extreme values does not change the conclusion *inside the current
disjoint-bank collar family*.  A base-changing adapter must leave that
normal form (or telescope a different collection of occurrences); mere
reindexing of its active and far labels cannot change the core.

## 2. Core-fibre invariance under serial reversal

### Theorem 2.1 (core-monochromatic serial closure)

Start from antipodal rings and apply any serial sequence of the currently
proved common-core C6 splices, allowing the orientation-reversal telescope
at every shared hub.  Every connected output component is assembled from
initial rings having one common invariant core `J`.  Moreover every owner
occurrence in that output component contains `J`, and every regenerated
shared collar again has fixed base `J`.

#### Proof

For the first port, Lemma 1.1 gives a common core `J` for its three input
rings.  The splice only permutes their old owner occurrences, so every
owner in the fused component still contains `J`.  The whole-profile
orientation-reversal identity sends

\[
       \Lambda_i\cup\{a_t\},\quad P_j\cup\{a_{t+2}\}
\]

to the next old collar with the same common profiles.  Their fixed
intersection remains `J`; reversal changes only the active cyclic labels.

Inductively, if this regenerated collar is the shared input of the next
port, the other two input collars must have the same displayed fixed base
in order to instantiate the proved C6 tensor.  By Lemma 1.1 their two fresh
rings therefore also have core `J`.  The next splice again only permutes
owner occurrences and regenerates a collar with base `J`.  The assertion
follows by induction. \(\square\)

Thus orientation reversal is a two-state regeneration inside a core fibre;
it is not a transition between core fibres.

## 3. Exponential residual component lower bound

For a fixed `(q-h)`-set `J`, the number of rank-`q` owners containing it is

\[
       S_{q,h}=\binom{(2q-1)-(q-h)}{q-(q-h)}
              =\binom{q+h-1}{h}.                       \tag{3.1}
\]

### Theorem 3.1 (current C6 ports cannot globally connect the owner shore)

Let an exact factor use every rank-`q` owner once.  After any sequence of
the current common-core C6 splices, the number of connected source
components is at least

\[
       \boxed{
       \left\lceil
       {\binom{2q-1}{q}\over\binom{q+h-1}{h}}
       \right\rceil .}                                 \tag{3.2}
\]

If `h=Theta(sqrt(q))`, the lower bound is `exp(Theta(q))`.

#### Proof

By Theorem 2.1, one connected output component has one core `J`, and all
of its owners belong to the star of `J`.  Equation (3.1) bounds that star
by `S_(q,h)` owners.  Since all `W_q=binom(2q-1,q)` owners must occur once,
at least `ceil(W_q/S_(q,h))` connected components are necessary.

For `h=Theta(sqrt(q))`,

\[
 \log S_{q,h}
 \le h\log\!\left({e(q+h-1)\over h}\right)
 =O(\sqrt q\log q)=o(q),
\]

whereas `log binom(2q-1,q)=Theta(q)`.  This proves the final assertion.
\(\square\)

### Corollary 3.2 (core changes must be zero-charge at scale)

Suppose every additional connector has arity at most a fixed `b` and can
reduce the number of current components by at most `b-1`.  Starting from
the components left by the present common-core C6 system, reducing to
`O(1)` components requires at least

\[
 {1\over b-1}
 \left(
 {\binom{2q-1}{q}\over\binom{q+h-1}{h}}-O(1)
 \right)                                                \tag{3.3}
\]

connectors which cross core fibres.  In particular, if each such connector
inserts even one new source position, its total charge is exponential at
critical width and cannot prove an additive-constant upper bound.

#### Proof

Theorem 3.1 gives the initial component lower bound after all available
same-core C6 compression.  One bounded-arity connector lowers component
count by at most `b-1`; summing this decrease proves (3.3).  The final
claim follows from the critical-width estimate in Theorem 3.1. \(\square\)

Thus a bounded-cost terminal join is not enough.  The construction needs
a zero-charge core transition used at growing scale, or a chronology whose
global connectedness is built before it is decomposed into fixed-core
rings.

## 4. Corrected global implication gate

The exact upper telescope remains useful: inside any connector chain on
which a literal serial realization exists, it reduces the uncancelled
upper current from six terms per port to four and fits the exact scalar
surplus.  But a global additive-constant implication needs one additional
ingredient which is absent from the present port family:

> **Core-transition connector.**  Produce a zero-charge protected splice
> whose shared output collar can have invariant core `J' != J`, or a joint
> one-copy cover-down and connector system which has the same effect while
> preserving owners, roots, upper providers, lower tickets, residence, and
> the terminal common cap.

There are two distinct proof targets.

1. **Base-changing adapter.**  Replace an output collar of core `J` by an
   input collar of core `J' != J` at zero source-length charge, while
   transporting the two upper-current terms (or cancelling them in a
   larger signed trade).  Lemma 1.2 proves that such an adapter cannot be
   another copy of the present disjoint-lambda/rho collar with only its
   labels reindexed.
2. **Core-cluster bridge.**  Use orientation-reversal telescoping only
   inside core-coherent clusters, then join the clusters by a separate
   zero-charge protected connector family.  By (3.2), a bounded-arity
   bridge family must operate at least `W_q/S_(q,h)-O(1)` times unless the
   initial joint cover-down already correlates many core fibres into one
   chronology.

Equivalently, a protected long-ring theorem intended to feed the current
C6 compressor must require more than coherence of two collars *within*
one ring.  Its auxiliary connector hypergraph must contain edges across
the invariant-core classes.  For the literal common-core C6 hypergraph no
such edges exist, by Theorem 2.1.

Therefore the proof-safe shortest chain to `B(k)+O(1)` currently has two
global integral premises:

1. a one-copy decorated long-ring cover-down with bounded terminal
   compiler deficiency and capacity-faithful duplicate providers; and
2. a protected core-transition linkage reducing its components to `O(1)`.

The orientation-reversal telescope closes a sharp local constant in the
second premise, but does not prove the core-transition part itself.
