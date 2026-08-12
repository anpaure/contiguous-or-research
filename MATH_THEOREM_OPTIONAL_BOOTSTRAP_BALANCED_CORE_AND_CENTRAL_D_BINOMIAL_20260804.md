# Balanced two-level Boolean cores force a central-`D` binomial lower bound

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, solver, or external
theorem  
**Status:** unconditional.  It strengthens the cube-edge exponential core
bound from `2^D/(1+m/D)` to `binom(D,floor(D/2))`.  It also proves the
conjectured sharper `binom(2D-1,D-1)` bound under the additional hypothesis
that both shores have minimum incidence degree at least `D`.  The existing
optional-core ledger gives degree `D` on the owner shore and average degree
at least `D` on the lower shore, not lower minimum degree `D`; the jump to
the sharper threshold was left open by the elementary argument in this
file.

**2026-08-04 addendum:** that sharper one-sided threshold is now closed by
the Chao--Yu theorem resolving the Bollobas--Eccles partial-shadow
conjecture.  See
`MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`.
Under strict side imbalance it gives

\[
 |B^-|\ge\binom{2d-7}{d-4}+1.
\]

The elementary balanced-core theorem below remains useful as a
self-contained weaker proof independent of the deep partial-shadow input.

## 0. Main result

Let

\[
 \mathcal A\subseteq\binom{[N]}k,
 \qquad
 \mathcal C\subseteq\binom{[N]}{k+1},                \tag{0.1}
\]

and join `A in mathcal A` to `C in mathcal C` when `A subset C`.
Suppose

\[
 |\mathcal C|\ge|\mathcal A|,
 \qquad
 d_{\mathcal A}(C)\ge D\quad(C\in\mathcal C).       \tag{0.2}
\]

Then

\[
 \boxed{
 |\mathcal A|\ge
 \binom D{\lfloor D/2\rfloor}.}                     \tag{0.3}
\]

More generally, if a nonempty two-level Boolean incidence graph has
minimum lower-to-upper degree at least `a` and minimum upper-to-lower degree
at least `b`, then

\[
 \boxed{
 |\mathcal A|\ge\binom{a+b-1}{b-1},
 \qquad
 |\mathcal C|\ge\binom{a+b-1}{b}.}                  \tag{0.4}
\]

In particular, the two-sided degree-`D` hypothesis gives

\[
 \boxed{
 |\mathcal A|,|\mathcal C|\ge
 \binom{2D-1}{D-1}.}                                \tag{0.5}
\]

The bound is sharp: fix a core `R`, take a set `S` of size `a+b-1`, and
use

\[
 \mathcal A=\{R\cup X:X\in\binom S{b-1}\},
 \qquad
 \mathcal C=\{R\cup Y:Y\in\binom S b\}.             \tag{0.6}
\]

Its two degrees are `a` and `b`, and equality holds in (0.4).

For the optional bootstrap core, take `D=d-3`.  The positive-owner shore
has size strictly larger than the lower shore and every positive owner contains at
least `D` core vertices.  Therefore

\[
 \boxed{
 |B^-|\ge\binom{d-2}{\lfloor(d-2)/2\rfloor}
       =\frac{2^{d-2}}{O(\sqrt d)}
       =2^{\Omega(\sqrt m)}.}                       \tag{0.7}
\]

This is stronger by a polynomial factor than the general cube-edge bound
`2^(d-3)/O(d)`.

## 1. The two-parameter minimum-degree theorem

### Theorem 1.1

Let `a,b>=1`.  If the nonempty incidence graph in (0.1) satisfies

\[
 d_{\mathcal C}(A)\ge a\quad(A\in\mathcal A),
 \qquad
 d_{\mathcal A}(C)\ge b\quad(C\in\mathcal C),        \tag{1.1}
\]

then (0.4) holds.

#### Proof

Induct on `a+b`.

If `a=1`, choose any `C in mathcal C`.  It contains at least `b` members of
`mathcal A`, so

\[
 |\mathcal A|\ge b=\binom b{b-1},
 \qquad |\mathcal C|\ge1=\binom b b.
\]

The case `b=1` is symmetric.

Now let `a,b>=2` and choose an incidence `A_* subset C_*`.  Put

\[
                              x=C_*-A_*.              \tag{1.2}
\]

Split both families according to `x`, deleting `x` from the section which
contains it:

\[
\begin{aligned}
 \mathcal A_0&=\{A\in\mathcal A:x\notin A\},&
 \mathcal A_1&=\{A-x:A\in\mathcal A, x\in A\},\\
 \mathcal C_0&=\{C\in\mathcal C:x\notin C\},&
 \mathcal C_1&=\{C-x:C\in\mathcal C, x\in C\}.
\end{aligned}                                        \tag{1.3}
\]

Inside the `x=0` section, a lower vertex loses at most the one upper
neighbour obtained by adjoining `x`, while an upper vertex loses none.
Hence the incidence graph

\[
                         \mathcal A_0-\mathcal C_0
\]

has minimum degrees at least `(a-1,b)`.  It is nonempty: `A_*` belongs to
`mathcal A_0`, and because `a>=2` it has an upper neighbour other than
`C_*`, necessarily in `mathcal C_0`.

Inside the `x=1` section, a lower vertex loses no upper neighbour, while an
upper vertex loses at most the one lower facet obtained by deleting `x`.
Thus

\[
                         \mathcal A_1-\mathcal C_1
\]

has minimum degrees at least `(a,b-1)`.  It is nonempty: `C_*-x` belongs
to `mathcal C_1`, and because `b>=2`, `C_*` has a lower neighbour other
than `A_*`; that neighbour contains `x` and supplies a member of
`mathcal A_1`.

Apply induction to the two sections:

\[
\begin{aligned}
 |\mathcal A_0|&\ge\binom{a+b-2}{b-1},&
 |\mathcal A_1|&\ge\binom{a+b-2}{b-2},\\
 |\mathcal C_0|&\ge\binom{a+b-2}{b},&
 |\mathcal C_1|&\ge\binom{a+b-2}{b-1}.
\end{aligned}                                        \tag{1.4}
\]

The two sections are disjoint and exhaust their families.  Pascal's
identity turns (1.4) into (0.4). \(\square\)

### Audit of the section degrees

The cross-section incidences are a matching: `A in mathcal A_0` has at
most one neighbour in `mathcal C_1`, namely `A union {x}`, and
`C in mathcal C_1` has at most one neighbour in `mathcal A_0`, namely
`C` itself before `x` is restored.  There are no incidences from
`mathcal A_1` to `mathcal C_0`.  Therefore exactly the two degree losses
used above, and no hidden multiplicities, occur.

## 2. Density extracts a balanced minimum-degree core

The original hypotheses do not give lower minimum degree `D`.  They do
give enough density to extract a core whose two minimum degrees sum to
`D+1`.

### Lemma 2.1 (asymmetric bipartite peeling)

Let `G=(L,R;E)` be any finite bipartite graph with

\[
 |R|\ge|L|,
 \qquad |E|\ge D|R|.                                 \tag{2.1}
\]

For every pair of positive integers `a,b` satisfying

\[
                              a+b=D+1,                \tag{2.2}
\]

`G` contains a nonempty subgraph with left minimum degree at least `a`
and right minimum degree at least `b`.

#### Proof

Repeatedly delete a left vertex of current degree at most `a-1` or a right
vertex of current degree at most `b-1`.  Suppose all vertices were deleted.
Charge each edge at the first deletion of one of its endpoints.  The total
charge would be at most

\[
 (a-1)|L|+(b-1)|R|
 \le(a+b-2)|R|=(D-1)|R|,                             \tag{2.3}
\]

contradicting (2.1).  Therefore the process stops with a nonempty subgraph
having the claimed two minimum degrees. \(\square\)

### Theorem 2.2 (central-`D` lower bound)

Under (0.2), equation (0.3) holds.

#### Proof

Let `G` be the Boolean incidence graph.  Its edge count obeys

\[
 |E(G)|\ge D|\mathcal C|.                            \tag{2.4}
\]

Choose

\[
 b-1=\lfloor D/2\rfloor,
 \qquad a=D+1-b.                                     \tag{2.5}
\]

Lemma 2.1 supplies a nonempty `(a,b)` minimum-degree subgraph.  It remains
a subgraph of the same two consecutive Boolean levels, so Theorem 1.1
gives

\[
 |\mathcal A|
 \ge\binom{a+b-1}{b-1}
 =\binom D{\lfloor D/2\rfloor}.
\]

This proves (0.3). \(\square\)

### Corollary 2.3 (strict side imbalance buys one more dimension)

Assume `D>=2`, replace `|mathcal C|>=|mathcal A|` by the strict inequality

\[
                         |\mathcal C|>|\mathcal A|,   \tag{2.6}
\]

and retain `|E|>=D|mathcal C|`.  Then

\[
 \boxed{
 |\mathcal A|\ge
 \binom{D+1}{\lfloor(D+1)/2\rfloor}.}                \tag{2.7}
\]

#### Proof

Choose positive integers `a,b` with

\[
 a+b=D+2,\qquad a\ge2,\qquad
 b-1=\lfloor(D+1)/2\rfloor.                          \tag{2.8}
\]

Run the peeling proof of Lemma 2.1.  If every vertex were deleted, the
edge charge would be at most

\[
\begin{aligned}
 (a-1)|\mathcal A|+(b-1)|\mathcal C|
 &=D|\mathcal C|-(a-1)(|\mathcal C|-|\mathcal A|)\\
 &<D|\mathcal C|,
\end{aligned}                                        \tag{2.9}
\]

contrary to the edge lower bound.  Thus an `(a,b)` minimum-degree core
survives.  Theorem 1.1 gives

\[
 |\mathcal A|\ge\binom{a+b-1}{b-1}
 =\binom{D+1}{\lfloor(D+1)/2\rfloor}.
\]

\(\square\)

## 3. Why the elementary argument alone does not give the `2D-1` candidate

If both original shores had minimum degree at least `D`, Theorem 1.1 with
`a=b=D` would prove exactly

\[
 |\mathcal A|\ge\binom{2D-1}{D-1}.                  \tag{3.1}
\]

The equality construction is the consecutive middle pair of a
`(2D-1)`-coordinate Boolean subcube, lifted by a fixed core.

The actual hypotheses give:

\[
 \min_{C\in\mathcal C}d(C)\ge D,
 \qquad
 \frac{|E|}{|\mathcal A|}\ge D,                    \tag{3.2}
\]

but the second row is only an **average** lower-shore degree.  Peeling can
force thresholds whose sum is `D+1`, as in Lemma 2.1; it cannot force
`a=b=D` from (3.2).  Abstract incidence systems demonstrate the danger:
affine planes have right degree `D`, more right vertices than left, strict
robust two-Hall expansion, and only `D^2` left vertices.  They fail Boolean
literal-union rigidity, so they do not refute (3.1) on the Boolean face,
but they prove that no graph-theoretic density argument can bridge the gap.

Accordingly, the elementary method isolates the following rank-sensitive
threshold-shadow problem:

> If `mathcal C` consists of rank-`(k+1)` sets having at least `D` facets
> in `mathcal A`, and `|mathcal C|>=|mathcal A|`, must
> `|mathcal A|>=binom(2D-1,D-1)`?

Theorem 2.2 proves the weaker central-`D` bound.  None of ordinary cube
isoperimetry, pair counting, strict two-Hall, or the present peeling lemma
supplies the displayed strengthening.  The separate addendum theorem
closes it instead by translating it exactly to the resolved partial-shadow
problem.

## 4. Optional-core specialization

For the minimal optional maximizer `B^-`, let `Q` be its positive-capacity
owners.  The bootstrap theorem gives

\[
 |Q|\ge|B^-|+1,
 \qquad
 |B^-\cap N(U)|\ge d-3\quad(U\in Q).                 \tag{4.1}
\]

For all sufficiently large `m`, one has `D=d-3>=2`, so Corollary 2.3
applies and gives (0.7).  The standard central binomial estimates

\[
 \frac{2^{D+1}}{D+2}
 \le\binom{D+1}{\lfloor(D+1)/2\rfloor}
 \le2^{D+1}                                              \tag{4.2}
\]

already imply `2^{Omega(sqrt m)}`.  Stirling's formula sharpens the
polynomial factor to `Theta(sqrt D)`; the asymptotic equality in (0.7) may
also be read with this standard estimate.

## 5. Exact scope

The elementary theorem proves a stronger unconditional size obstruction
for any surviving optional core.  It does not prove that the core is
absent, shifted, compressible, or contained in a safe two-sided subcube.
The `2D-1` threshold-shadow statement is proved only in the separate
partial-shadow addendum cited above.  Neither result alone gives a new
upper bound for `nu(k)`.
