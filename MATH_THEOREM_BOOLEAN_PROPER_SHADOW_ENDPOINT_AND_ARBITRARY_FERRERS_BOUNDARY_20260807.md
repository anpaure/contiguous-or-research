# Proper Boolean shadows make every optimal Ferrers boundary capacity-safe

**Date:** 2026-08-07  
**Status:** unconditional exact shadow theorem and exact residual
capacity-matching consequence.  This closes the capacity-only
Hamilton--Ferrers intersection row.  It does not chainize the matched lower
targets inside owners and does not construct a literal antecedent.

## 1. Parameters

Let

\[
 \mathcal O={ [k]\choose r},\qquad W=|\mathcal O|,
 \qquad
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|\mathcal L|.
\]

Let `d` be the optimal deadline parameter and suppose the positive Ferrers
residue is

\[
 h=\Lambda-dW>0.
 \tag{1.1}
\]

By the definition of `d`,

\[
 1\le h\le {d+1\choose2},
 \qquad d\le r-1.
 \tag{1.2}
\]

For `Q subseteq mathcal O`, write

\[
 \partial_{<r}Q
 =\{S\in\mathcal L:S\subseteq T\text{ for some }T\in Q\}.
 \tag{1.3}
\]

## 2. A general endpoint theorem for complete lower shadows

For `n>=r>=1` and `0<=q<=binom(n,r)`, let `D_(n,r)(q)` be the minimum,
over all families of `q` rank-`r` sets, of the number of their proper
subsets **including the empty set**.  Put `D_(n,r)(0)=0`.

### Theorem 2.1 (linear functionals minimize at an endpoint)

For every real `lambda>=0`,

\[
 \min_{1\le q\le {n\choose r}}
 \bigl(D_{n,r}(q)-\lambda q\bigr)
 =
 \min\left\{
 2^r-1-\lambda,
 \sum_{s=0}^{r-1}{n\choose s}
       -\lambda {n\choose r}
 \right\}.
 \tag{2.1}
\]

Thus, among all nonempty sizes, a linear penalty in the number of top sets
is minimized either by one top set or by the complete top layer.

#### Proof

Kruskal--Katona says that the initial colex segment simultaneously minimizes
every lower shadow, hence their sum.  If

\[
 {a\choose r}\le q\le {a+1\choose r},
 \qquad q={a\choose r}+q',
 \qquad0\le q'\le {a\choose {r-1}},
\]

the colex recursion is exact:

\[
 D_{n,r}(q)
 =\sum_{s=0}^{r-1}{a\choose s}+D_{a,r-1}(q').
 \tag{2.2}
\]

Indeed, the first block consists of every rank-`r` subset of `[a]`.
The remaining sets contain `a+1`; after deleting that coordinate they are
the initial colex rank-`r-1` family on `[a]`.  The two displayed proper
downsets are disjoint according as they omit or contain `a+1`.

We prove by induction on `r` that, after allowing `q=0`, the minimum of
`D_(n,r)(q)-lambda q` occurs at `q=0` or the full layer.  For `r=1`, the
value is zero at `q=0` and `1-lambda q` for `q>0`, so the assertion is
immediate.

Assume it for `r-1`.  Equation (2.2) shows that the minimum in each block
occurs at `q'=0` or at `q'=binom(a,r-1)`.  Hence global candidates are the
binomial breakpoints.  Write

\[
 G_r(a)=\sum_{s=0}^{r-1}{a\choose s}
        -\lambda {a\choose r}.
 \tag{2.3}
\]

Pascal's identity gives

\[
 G_r(a+1)-G_r(a)
 =G_{r-1}(a)
 = {a\choose {r-1}}
 \left(
   \frac{\sum_{s=0}^{r-2}{a\choose s}}{{a\choose {r-1}}}
   -\lambda
 \right).
 \tag{2.4}
\]

For each fixed `s<r-1`, the ratio

\[
 {a\choose s}/{a\choose {r-1}}
\]

strictly decreases with `a`.  Therefore the bracket in (2.4) changes sign
at most once, from positive to negative.  The breakpoint sequence `G_r(a)`
first increases and then decreases, so its minimum is at `a=r` or `a=n`.

Including `q=0` does not create a third positive-size candidate.  If
`2^r-1-lambda>=0`, zero beats the one-set endpoint.  If it is negative,
the union bound

\[
 D_{n,r}\!\left({n\choose r}\right)
 \le {n\choose r}(2^r-1)
\]

shows that the full-layer value is no larger than the one-set value.
Deleting the optional zero endpoint yields (2.1).  This completes the
induction. \(\square\)

## 3. The sharp proper-shadow inequality

### Theorem 3.1

For every nonempty `Q subseteq mathcal O`,

\[
 \boxed{\ |\partial_{<r}Q|\ge d|Q|+h.\ }
 \tag{3.1}
\]

#### Proof

Apply Theorem 2.1 with `n=k`, `lambda=d`, and subtract the common empty
set.  The complete-layer endpoint equals

\[
 \Lambda-dW=h.
\]

The one-set endpoint equals `2^r-2-d`.  It is at least `h`: from (1.2),

\[
 h\le {d+1\choose2}\le 2^r-2-d.
 \tag{3.2}
\]

For the second inequality it is enough to take the largest possible
`d=r-1`, reducing it to

\[
 {r\choose2}\le2^r-r-1,
\]

which holds at `r=2` and then inductively.  Both endpoints in (2.1), after
removing the empty set, are therefore at least `h`.  Kruskal--Katona gives
(3.1). \(\square\)

Equality holds at `Q=mathcal O`.  The theorem says that no nonempty proper
owner family has a smaller affine lower-shadow surplus.

## 4. Arbitrary boundary deletion is capacity-safe

Make `d` labelled copies of every owner in `mathcal O`, and join a lower
target `S` to every copy of every owner containing it.

### Theorem 4.1

For **every** boundary family `mathcal B subseteq mathcal L` of size `h`,
the residual family `mathcal L\mathcal B` has a perfect matching to the
`dW` owner copies.

#### Proof

The two shores both have size `dW`.  Let `mathcal F` be a residual target
family and let `U=N(mathcal F) subseteq mathcal O` be its unlabelled owner
neighbourhood.

If `U=mathcal O`, then

\[
 |\mathcal F|\le|\mathcal L\setminus\mathcal B|=dW=d|U|.
\]

Otherwise put `Q=mathcal O\setminus U`, which is nonempty.  No member of
`mathcal F` is contained in an owner from `Q`, so

\[
 \mathcal F\subseteq
 \mathcal L\setminus\partial_{<r}Q.
\]

Theorem 3.1 gives

\[
 |\mathcal F|
 \le\Lambda-(d|Q|+h)
 =d(W-|Q|)=d|U|.
\]

This is Hall's inequality for all `mathcal F`; hence a perfect matching
exists. \(\square\)

### Corollary 4.2 (the capacity transversal matroid is uniform)

On the ground set `mathcal L`, the transversal matroid defined by the
`dW` labelled owner copies is exactly

\[
 U_{dW,\Lambda}.
 \tag{4.1}
\]

Indeed, Theorem 4.1 says that every `dW`-subset is a basis.  Every smaller
family extends to a `dW`-subset and is therefore independent.  Thus there
are no hidden containment circuits below the scalar capacity; every
remaining lower obstruction necessarily uses the correlations between
several targets assigned to the same owner (nestedness, chronology, or
literal cells).

## 5. PBBS consequence and remaining quantifier

The Hamilton-first extraction theorem may choose its `h` distinct
rank-profiled boundary targets inside the clean packet bottoms in any
convenient way.  Theorem 4.1 guarantees that deleting those targets always
leaves an exact capacity-`d` containment matching.  Thus the
**capacity-only** Hamilton--Ferrers intersection is automatic; no joint
selection is required at that projection.

This does not prove that the `d` targets assigned to one owner form one
nested flag.  A capacity matching can assign incomparable targets to the
same owner.  The surviving all-dimensional lower gate is therefore the
sharp correlated chain/compiler problem, followed by the common literal
chronology and deep-upper conditions.
