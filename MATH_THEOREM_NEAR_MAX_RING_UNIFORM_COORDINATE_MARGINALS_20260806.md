# Near-maximal ring schedules have exact uniform coordinate marginals

## Status

For the masked-core periods `q+h-3` and `q+h-2`, every scalar and
coordinatewise owner/root moment can be satisfied exactly and uniformly.
No residue balancing, Gale--Ryser rounding, or exceptional coordinate is
needed: divide the total ring counts by the ground-set size and use all
cyclic shifts of one core/moving/unused partition.

This closes the coordinate-marginal and first-moment divisibility gate.  It
does not partition the *named* owner and root sets into cyclic-window rings;
that is the remaining one-copy design theorem.

No computation or search is used.

## 1. Parameters

Put

\[
 n=2q-1,\qquad W=\binom{2q-1}{q},\qquad
 C={W\over n}=\operatorname {Cat}_{q-1},               \tag{1.1}
\]

and let

\[
 s=q-h,\qquad p=q+h-3.                                 \tag{1.2}
\]

A period-`p` masked ring has core, moving and unused sizes

\[
                         s,\quad p,\quad2,              \tag{1.3}
\]

while a period-`p+1` ring has sizes

\[
                         s,\quad p+1,\quad1.            \tag{1.4}
\]

Both triples sum to `n`.

Since `p` and `p+1` are coprime and `C` is exponential in `q`, for every
sufficiently large `q` there are positive integers `A,B` satisfying

\[
                         C=Ap+B(p+1).                  \tag{1.5}
\]

Indeed `B` is prescribed modulo `p`.  Consecutive admissible values differ
by `p`, and hence change `B(p+1)` by only `p(p+1)=O(q^2)`.  Choose the
representative for which `B(p+1)` is nearest `C/2`.  Then both `Ap` and
`B(p+1)` equal `C/2+O(q^2)` and are exponential.  Replacing

\[
                         (A,B)\mapsto(A-(p+1),B+p)      \tag{1.5a}
\]

preserves (1.5) and reverses the parity of `A+B`; for large `q` both
choices remain positive.  Thus the total ring count below may also be
given either parity.

Set

\[
                         a=nA,\qquad b=nB.              \tag{1.6}
\]

Then the exact scalar schedule is

\[
                         ap+b(p+1)=nC=W.                \tag{1.7}
\]

Since `n` is odd, the parity of the ring count `a+b=n(A+B)` is the parity
of `A+B`.  The adjustment (1.5a) therefore allows an odd ring count, so the
abstract masked-core loose tree need not leave a parity component.

## 2. Exact uniform incidence ledger

First record why the displayed marginals are forced.  In the complete
central layers, every coordinate has owner-minus-root excess

\[
 \binom{2q-2}{q-1}-\binom{2q-2}{q-2}=C.               \tag{2.0}
\]

Inside one ring a core or unused coordinate has excess zero, whereas a
moving coordinate has one more owner occurrence than root occurrence.
Hence every exact ring factor must make every coordinate moving exactly
`C` times.  Its owner incidence is `qC`; subtracting the `hC` moving
incidences forces weighted core load `(q-h)C=sC`.  Thus (2.2)--(2.3) are
necessary, not only convenient symmetric choices.

### Theorem 2.1 (uniform core/moving/unused marginals)

There are `a` labelled period-`p` partition states and `b` labelled
period-`p+1` partition states such that every coordinate occurs exactly

\[
\begin{array}{c|ccc}
 &\text{core}&\text{moving}&\text{unused}\\ \hline
 p\text{-group}&As&Ap&2A\\
 (p+1)\text{-group}&Bs&B(p+1)&B
\end{array}                                             \tag{2.1}
\]

times.  Consequently every coordinate is moving in exactly

\[
                         Ap+B(p+1)=C                  \tag{2.2}
\]

rings, and its weighted core load is exactly

\[
                         p(As)+(p+1)(Bs)=sC.            \tag{2.3}
\]

#### Proof

Identify the coordinates with `mathbb Z/n mathbb Z`.  In the period-`p`
group take the `n` cyclic shifts of the ordered partition

\[
 \{0,\ldots,s-1\}\;\dot\cup\;\{s,s+1\}\;\dot\cup\;
 \{s+2,\ldots,n-1\},                                  \tag{2.4}
\]

whose cells are core, unused and moving, and repeat this complete shift
orbit `A` times.  Every coordinate then occurs `As,2A,Ap` times in the
three cells.

For the period-`p+1` group use `B` copies of all shifts of

\[
 \{0,\ldots,s-1\}\;\dot\cup\;\{s\}\;\dot\cup\;
 \{s+1,\ldots,n-1\}.                                  \tag{2.5}
\]

This gives the second row of (2.1).  Equations (2.2)--(2.3) are (1.5)
multiplied respectively by one and by `s`. \(\square\)

### Corollary 2.2 (all coordinate owner/root moments are exact)

Give every moving coordinate an owner run of length `h` and a root run of
length `h-1`, as in an antipodal ring.  Core coordinates occur throughout
their ring and unused coordinates never occur.  Then every coordinate has
owner-minus-root excess `C`, exactly matching the complete two central
Boolean layers.  Its total owner incidence is `qC` and its total root
incidence is `(q-1)C`.

#### Proof

Only a moving coordinate contributes to owner-minus-root excess, and its
contribution is one.  Equation (2.2) gives excess `C`.

The owner incidence is weighted core load plus `h` times moving load:

\[
                         sC+hC=qC.
\]

The root incidence is `sC+(h-1)C=(q-1)C`.  These are exactly
`binom(2q-2,q-1)` and `binom(2q-2,q-2)`, respectively. \(\square\)

## 3. Exact cyclic-necklace reduction

Let `Z_n` act regularly on the coordinate set and hence on every Boolean
layer.

### Lemma 3.1 (both central actions are free)

The `Z_n`-actions on the rank-`q` and rank-`(q-1)` layers are free.  Each
layer therefore has exactly

\[
                         {W\over n}=C                   \tag{3.1}
\]

necklaces.

#### Proof

A nonidentity rotation has coordinate orbits of one common length `d>1`
dividing `n`.  An invariant subset is a union of these orbits and hence has
size divisible by `d`.  But

\[
             \gcd(q,2q-1)=\gcd(q-1,2q-1)=1,
\]

so neither `q` nor `q-1` is divisible by a nontrivial divisor of `n`.
\(\square\)

Call a ring **quotient-simple** if its owners lie in pairwise distinct
owner necklaces and its roots lie in pairwise distinct root necklaces.
The full translation orbit of such a ring has size `n` and covers each of
those owner and root necklaces completely.

### Theorem 3.2 (necklace ring resolution is sufficient)

Suppose there are

* `A` quotient-simple base rings of period `p`, and
* `B` quotient-simple base rings of period `p+1`,

such that their projected owner blocks partition the `C` owner necklaces
and their projected root blocks partition the `C` root necklaces.  Then
all `n` coordinate translations of those base rings form an exact
one-copy owner/root ring factor with the uniform coordinate marginals of
Theorem 2.1.

Conversely, every translation-invariant exact ring factor whose ring
orbits are quotient-simple projects to such a simultaneous necklace
partition.

#### Proof

For a quotient-simple base ring, translating one displayed owner through
`Z_n` covers its entire necklace once, and distinct displayed owners cover
disjoint necklaces.  The same holds for roots.  Hence a partition of both
quotient shores lifts to an exact partition of both literal shores.

The number of projected owner and root vertices used is

\[
                         Ap+B(p+1)=C,
\]

so no resource remains.  Taking full translation orbits also gives the
uniform coordinate counts of Theorem 2.1.  The converse follows by
quotienting every complete ring orbit. \(\square\)

Thus the central one-copy problem has the following exact sufficient
form:

> partition two `C`-element necklace shores simultaneously by the owner
> and root projections of `A+B` quotient-simple cyclic-window rings.

This is a resolvable two-shore cyclic-window design.  It is still an
integral block-selection problem, but all scalar and coordinate equations
have disappeared.

## 4. Relation to standard integral objects

Equivalently, before quotienting, let `G_q` be the regular bipartite
incidence graph between rank-`q` owners and rank-`(q-1)` roots.  An exact
ring factor is a spanning `2`-factor whose owner cycles have lengths
`p,p+1` and whose Johnson deletion/insertion labels satisfy

\[
 a_0,\ldots,a_{\ell-1}\text{ distinct},qquad
                         b_t=a_{t+h}.                  \tag{4.1}
\]

This is the exact long-ring recognition law.  After a core is fixed, the
residual owner sets are the `h`-windows of one cyclic order—one tight
Hamilton cycle in an `h`-uniform complete hypergraph—and the residual
roots are its `(h-1)`-windows.

Therefore:

* bipartite perfect matching or network flow supplies an arbitrary
  `2`-factor but does not enforce (4.1);
* Baranyai factorization controls one uniform layer but does not
  simultaneously partition the `(h-1)`-window shadow; and
* ordinary tight-cycle decomposition does not correlate different cores
  or the masked connector states.

No currently invoked standard theorem supplies this simultaneous
two-shore, growing-`h` cyclic-window resolution.  The weakest exact central
statement still needed is precisely the necklace ring resolution in
Theorem 3.2, strengthened by occurrence tickets and masked-tree states.

## 5. Exact scope

The theorem proves that the near-maximal masked periods have no scalar,
coordinate, parity, congruence, or first-moment obstruction.  It even gives
literal core/moving/unused partitions with those marginals.

It does **not** choose cyclic orders so that the resulting `h`-windows
partition every named rank-`q` owner and every named rank-`(q-1)` root.
Nor does it prove the necklace resolution of Theorem 3.2, correlate the
partition states into masked triangles, or carry
the nonlocal lower/upper occurrence tickets.  The remaining central object
is therefore an exact resolvable cyclic-window design, not a degree-sequence
or coordinate-flow problem.
