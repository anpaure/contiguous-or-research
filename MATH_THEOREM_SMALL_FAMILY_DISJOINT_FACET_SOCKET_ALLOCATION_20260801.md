# Small defect banks admit disjoint facet sockets

Date: 2026-08-01  
Status: unconditional set-system theorem.  It solves only the facet-owner
allocation row of the resident-socket construction.  It does not plant
residence guards, choose compatible extraction cuts, preserve the upper
deck, connect the chronology, or prove a compiler.

## 1. Statement

Let

\[
  \mathcal U\subseteq \binom{[k]}{r+1}
\]

be a family of upper colours.  A `b`-facet allocation assigns to each
`U in mathcal U` a set `F(U)` of `b` different rank-`r` facets of `U`, with
all the sets `F(U)` pairwise disjoint.

### Theorem 1 (disjoint facet allocation)

Let `1<=b<=r+1` and put

\[
 s=\left\lfloor\frac{r+1}{b}\right\rfloor.
\]

If

\[
 |\mathcal U|\le \binom{r+s}{r+1},                 \tag{1.1}
\]

then `mathcal U` has a `b`-facet allocation.

Equivalently, there are labelled facets

\[
 F_{U,1},\ldots,F_{U,b}\in\binom{[k]}r,
 \qquad F_{U,j}\subset U,
\]

which are distinct over all pairs `(U,j)`.

### Corollary 2 (resident socket facets)

For the compact depth-`h` resident facet socket, take `b=h+1`.  If

\[
 |\mathcal U|
 \le
 \binom{r+\lfloor(r+1)/(h+1)\rfloor}{r+1},          \tag{1.2}
\]

then every target in `mathcal U` can be assigned the `h+1` distinct facets
needed by its socket, with no middle owner used by two sockets.

In particular, if `h=O(sqrt(r))`, every polynomial-size family
`|mathcal U|<=r^C` satisfies (1.2) for all sufficiently large `r`.

## 2. Proof

For `mathcal A subseteq mathcal U`, write

\[
 \partial\mathcal A
 =\{F\in\tbinom{[k]}r:F\subset U\text{ for some }U\in\mathcal A\}
\]

for its rank-`r` lower shadow.

Let `a=|mathcal A|`, and choose the real number `x>=r+1` satisfying

\[
 a=\binom{x}{r+1}.
\]

The Lovasz form of the Kruskal--Katona theorem gives

\[
 |\partial\mathcal A|\ge\binom{x}{r}.                \tag{2.1}
\]

Because `a<=|mathcal U|<=binom(r+s,r+1)` and the generalized binomial
coefficient is increasing in `x` on this range, `x<=r+s`.  Hence

\[
 \frac{|\partial\mathcal A|}{|\mathcal A|}
 \ge
 \frac{\binom{x}{r}}{\binom{x}{r+1}}
 =\frac{r+1}{x-r}
 \ge\frac{r+1}{s}
 \ge b.                                               \tag{2.2}
\]

Thus

\[
                  |\partial\mathcal A|\ge b|\mathcal A|  \tag{2.3}
\]

for every subfamily `mathcal A`.

Now replace every `U in mathcal U` by `b` labelled copies, each adjacent
to all `r`-facets of `U`.  For an arbitrary family `X` of these copies,
let `mathcal A` be the underlying set of upper colours.  Then

\[
 |X|\le b|\mathcal A|
 \le |\partial\mathcal A|
 =|N(X)|.
\]

Hall's theorem gives a matching saturating all copies.  Reading the matched
facets at the `b` copies of `U` gives `F(U)`.  This proves Theorem 1 and the
first assertion of Corollary 2.

For the asymptotic assertion, `h=O(sqrt(r))` implies

\[
 s=\Omega(\sqrt r).
\]

In particular `s>=2` for all sufficiently large `r`.  On that range,

\[
 \binom{r+s}{r+1}=\binom{r+s}{s-1}
 \ge \left(\frac{r}{s-1}\right)^{s-1}.
\]

The logarithm of the right-hand side is
`Omega(sqrt(r) log r)`, which eventually dominates `C log r` for every
fixed `C`.  Therefore it exceeds `r^C` for all sufficiently large `r`.

## 3. Extraction-cost corollary

Suppose every rank-`r` owner occurs once in a physical owner chronology.
After applying Theorem 1, isolate every selected facet occurrence.  Two cuts
per selected owner always suffice, so the crude total extraction cost is

\[
                         2b|\mathcal U|.               \tag{3.1}
\]

Adjacent selected owners can only reduce this count.  Thus a polynomial-size
socket bank has polynomial extraction cost even though the central owner
layer is exponentially large.

This is only a scalar and ownership statement.  The cuts in (3.1) can destroy
unique upper colours, and the isolated facets still need compatible left and
right residence guards.  Those effects are occurrence-labelled and are not
controlled by Kruskal--Katona.

## 4. What this removes, and what remains

The theorem rules out a possible all-dimensional obstruction:

> A polynomial bank of missing immediate-upper colours cannot fail merely
> because its compact sockets compete for too few distinct middle facets.

For `h=Theta(sqrt(r))`, the available Hall range is in fact much larger than
polynomial.

The unresolved regenerative statement is now narrower.  One must select,
for the already-disjoint facet blocks,

1. compatible minimum residence-cut refinements;
2. two physical guard pieces per socket with the prescribed age vectors;
3. child-colour providers for every extraction casualty;
4. one bounded-component/global path ordering;
5. the transported lower compiler.

The finite `k=17` socket campaign is an exact calibration of these remaining
rows: facet existence is abundant, while guard/cut and child-provider
correlation determine whether a proposed simultaneous bank is real.
