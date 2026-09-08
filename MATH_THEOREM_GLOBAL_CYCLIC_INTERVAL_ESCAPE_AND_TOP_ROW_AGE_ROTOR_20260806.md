# Global cyclic interval escape and the exact top-row age rotor

**Date:** 2026-08-06  
**Method:** the truncated cyclic interval poset, exchangeable integer
compositions, and literal age-state rotation; no computation or search  
**Status:** unconditional scalar/order escape from the separated-block
no-go and an exact fractional named-target clock for ranks `t,t-1`.  The
existing monotone-rotor theorem separately supplies the complete fractional
lower rank marginals.  Their simultaneous realization in the apparent
constant-length extremizer is impossible: an exact endpoint-chain cut
separates the two feasible projections.  Thus merging the blocks removes
the old quadratic interval shadow, but placing both top payload rows at
maximal width consumes too many endpoints to carry the higher top-`d`
rows.  The audited monotone rotor already supplies a successful fractional
mixture of witness lengths.  Hence the surviving gate is integral
owner-once/named-target Johnson--Euler fusion, with PBBS compatibility,
not another unrestricted fractional rank-marginal theorem.

## 1. The global truncated interval poset

Let `N` source positions be cyclically ordered and let

\[
 \mathcal I_{N,d}=\{[i,i+\ell-1]:i\in\mathbb Z_N,
                              1\le\ell\le d\}                 \tag{1.1}
\]

be the proper cyclic intervals of width at most `d`, ordered by
containment.  Assume `2d<N`, as in the eventual central regime.

### Lemma 1.1 (maximal interval layer)

The `N` intervals of length `d` form an antichain and each has no strict
upper neighbour in `I_(N,d)`.  Hence any family of at most `N` named
same-rank targets has an abstract occurrence placement whose total upset
has exactly the cardinality of the family.

#### Proof

Two distinct proper cyclic intervals of the same length do not contain one
another.  No allowed interval has length greater than `d`.  Assign the
targets injectively to length-`d` intervals. \(\square\)

This is the precise escape from the quadratic shadow in separated blocks:
there a length-`d` interval is the unique whole block, while globally there
are `N` translated maximal intervals.

## 2. Both top lower layers fit in the maximal interval layer

Use the odd central parameters

\[
 n=2m+1,
 \qquad r=m,
 \qquad t=m-d,
 \qquad W={n\choose m}.                                     \tag{2.1}
\]

Put

\[
                         M={n\choose t},
 \qquad                  A={n\choose {t-1}}.                  \tag{2.2}
\]

### Theorem 2.1 (global two-layer order capacity)

For every sufficiently large central parameter,

\[
                         M+A<W.                               \tag{2.3}
\]

Consequently all rank-`t` and rank-`(t-1)` targets can be assigned to
distinct maximal intervals in `I_(W,d)`.  Their complete upset uses only
`M+A` addresses.  The remaining address count is

\[
                         dW-M-A,                              \tag{2.4}
\]

and exceeds the number of targets of ranks at most `t-2` by a linear
multiple of `dW`.

#### Proof

The central local limit gives

\[
 {M\over W}\longrightarrow e^{-\pi/4},
 \qquad {A\over W}\longrightarrow e^{-\pi/4}.                \tag{2.5}
\]

Since `2e^(-pi/4)<1`, (2.3) follows.  Lemma 1.1 gives the placement and
its upset size.

The number of remaining lower targets is at most

\[
 \sum_{s=1}^{t-2}{n\choose s}
 =(2\Phi(-\sqrt{\pi/2})+o(1))dW,                             \tag{2.6}
\]

whereas (2.4), divided by `dW`, tends to one because `M+A=O(W)` and
`d` tends to infinity.  This proves the strict surplus. \(\square\)

The theorem is an order-capacity statement.  It does not label one word
with those values.  Its point is exact: after the free regions are merged,
the former interval-antichain dual separator disappears rather than merely
becoming smaller.

## 3. A literal stationary rotor for the two maximal rows

Put

\[
                         D=d+1,
 \qquad p={M\over W},
 \qquad q={A\over W},
 \qquad h=1-p-q.                                             \tag{3.1}
\]

For all sufficiently large parameters, `h>0`.  An age composition is a
positive integer tuple

\[
                         c=(c_0,\ldots,c_d),
 \qquad                  \sum_{j=0}^{d}c_j=r.                 \tag{3.2}
\]

### Lemma 3.1 (exchangeable top-row composition law)

There is a rotation-invariant rational probability law on the positive
compositions (3.2) such that, for every coordinate `j`,

\[
                         \Pr(c_j=d)=p,
 \qquad                  \Pr(c_j=d+1)=q.                      \tag{3.3}
\]

#### Proof

The desired expected numbers of parts of sizes `d,d+1` are

\[
                         a=Dp,
 \qquad                  b=Dq.                                \tag{3.4}
\]

Choose a rational distribution on the four nearest integer pairs

\[
 (\lfloor a\rfloor,\lfloor b\rfloor),
 (\lfloor a\rfloor,\lceil b\rceil),
 (\lceil a\rceil,\lfloor b\rfloor),
 (\lceil a\rceil,\lceil b\rceil)                            \tag{3.5}
\]

with coordinate expectations `(a,b)`, omitting a zero-weight pair when a
coordinate is integral.  Call one such pair `(a_0,b_0)` and put

\[
 c_0^*=D-a_0-b_0,
 \qquad
 R^*=r-da_0-(d+1)b_0.                                       \tag{3.6}
\]

The asymptotics

\[
 p,q\longrightarrow e^{-\pi/4},
 \qquad {r\over Dd}\longrightarrow{4\over\pi}               \tag{3.7}
\]

give

\[
 c_0^*=\Theta(d),
 \qquad {R^*\over c_0^*}=(4+o(1))d.                          \tag{3.8}
\]

uniformly over the four pairs.  In particular, for every sufficiently
large parameter, `R^*` is a sum of `c_0^*` positive integers, each lying
strictly between `3d` and `5d`; use the quotient and remainder of
`R^*` by `c_0^*`.  None of these residual parts equals `d` or `d+1`.

Adjoin `a_0` parts of size `d`, `b_0` parts of size `d+1`, and the displayed
residual parts.  Uniformly permute the resulting `D` parts.  Finally mix
over (3.5).  Every tuple sums to `r`, the expected counts are (3.4), and
permutation invariance gives (3.3).  The law is rational and in particular
rotation invariant. \(\square\)

Fix a rank-`r` owner `T` and an ordered labelled partition

\[
                         T=C_0\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}C_d,
 \qquad |C_i|=c_i.                                          \tag{3.9}
\]

Rotate its blocks:

\[
 (C_0,C_1,\ldots,C_d)
 \longmapsto
 (C_d,C_0,\ldots,C_{d-1}).                                  \tag{3.10}
\]

This is a literal legal age transition.  The emitted source letters around
the rotor are the blocks `C_i`, every length-`D` window has union `T`, and
the length-`d` window in the phase with terminal class `C_d` has value

\[
                         T\setminus C_d.                      \tag{3.11}
\]

### Theorem 3.2 (fractional named top-two-row rotor)

Average the rotors (3.10) using Lemma 3.1, uniformly over owners, labelled
partitions, and coordinate permutations.  Mark (3.11) whenever
`|C_d|=d` or `d+1`.  Then

1. every rank-`r` owner has normalized load one;
2. every named rank-`t` target has marked load one;
3. every named rank-`(t-1)` target has marked load one; and
4. every marked occurrence has physical width exactly `d`.

#### Proof

Normalize every rotor by its `D` phases.  Uniform owner averaging gives
owner load one.  By (3.3), the total marked rank-`t` mass per owner is
`p=M/W`, so across all `W` owners it is `M`, the number of rank-`t`
targets.  Coordinate transitivity makes the load equal on those targets,
and hence equal to one.  The same argument with `q=A/W` proves the
rank-`(t-1)` row.  Equation (3.11) proves the width statement. \(\square\)

This closes both maximal rows fractionally in exactly the occurrence layer
which minimizes their interval-poset upset.

## 4. The exact joint stationary circulation LP

The corrected monotone-rotor theorem proves a stationary marked trace with
the complete optimal lower rank vector.  Theorem 3.2 proves the additional
maximal-width placement of the top two rows.  Separate feasibility does not
yet prove simultaneous feasibility.

Here is the exact intersection problem.  Let `C_(r,d)` be the age-type
digraph.  Its vertices are positive types (3.2), and `c -> c'` is legal
when

\[
                         c'_{i+1}\le c_i
                         \qquad(0\le i<d).                    \tag{4.1}
\]

For a type `c`, its length-`j` proper suffix rank is

\[
                         s_j(c)=c_0+\cdots+c_{j-1}
                         \qquad(1\le j\le d).                 \tag{4.2}
\]

Let

\[
 q_s={{n\choose s}-b_s\over W}\qquad(1\le s<r)              \tag{4.3}
\]

be the corrected Ferrers residual vector, with `b_s=0` above the boundary
band.

### Definition 4.1 (global join-clock LP, `GJCLK`)

Variables are a rational circulation `f_(c,c')>=0`, its stationary vertex
mass `pi_c`, and mark masses `0<=mu_(c,j)<=pi_c`.  They satisfy

\[
 \sum_{c'}f_{c,c'}=\sum_{c'}f_{c',c}=\pi_c,
 \qquad \sum_c\pi_c=1,                                     \tag{4.4}
\]

\[
 \sum_{c,j:s_j(c)=s}\mu_{c,j}=q_s
                         \qquad(1\le s<r),                    \tag{4.5}
\]

and the maximal-row localization constraints

\[
 \sum_{c:c_d=d}\mu_{c,d}=q_t={M\over W},
 \qquad
 \sum_{c:c_d=d+1}\mu_{c,d}=q_{t-1}={A\over W}.              \tag{4.6}
\]

Since (4.5) already exhausts the rank-`t,t-1` masses, (4.6) forces all of
their marks to occur at width `d`.

### Theorem 4.2 (exact fractional frontier)

Feasibility of `GJCLK` is equivalent to a symmetric stationary literal
source circulation which simultaneously

1. has the optimal Ferrers-corrected named lower target marginals; and
2. places every rank-`t,t-1` marked occurrence at maximal width `d`.

The unconstrained projection (4.4)--(4.5) is feasible by the audited
monotone-rotor theorem.  The projection (4.4),(4.6), with the other marks
discarded, is feasible by Theorem 3.2.  The old scalar interval-capacity
inequality does not separate `GJCLK`, and neither isolated marginal
projection does; a correlated terminal-age/prefix-sum separator may still
do so.

#### Proof

The labelled compatibility graph between two legal age types is biregular.
Therefore every rational type circulation lifts uniformly to literal
labelled age states.  A mark at `(c,j)` is exactly a literal length-`j`
suffix interval of rank `s_j(c)`.  Coordinate and owner averaging converts
(4.5) into the named loads complementary to the Ferrers boundary, while
(4.6) gives the required physical widths.  This proves both directions.

The two projection claims are precisely the monotone-rotor theorem and
Theorem 3.2.  Theorem 2.1 removes the only interval-poset scalar separator
created by the old block cuts. \(\square\)

The two projection theorems do not imply their intersection.  A separating
functional may correlate the terminal class size `c_d` with the other
prefix sums.  In fact such a separator exists and is elementary.

### Theorem 4.3 (maximal-two-row endpoint cut)

Every feasible solution of `GJCLK` would satisfy

\[
 \boxed{
 \sum_{s=t+1}^{r-1}q_s
 \le d\bigl(1-q_t-q_{t-1}\bigr).}                            \tag{4.7}
\]

For the optimal central residual vector, (4.7) fails for every sufficiently
large parameter.  Hence `GJCLK` is infeasible.

#### Proof

At one positive age type, the suffix ranks

\[
                         s_1(c)<s_2(c)<\cdots<s_d(c)          \tag{4.8}
\]

are strictly increasing.  If `c_d=d`, then `s_d=t`; if `c_d=d+1`, then
`s_d=t-1`.  In either case no suffix at that endpoint has rank greater than
`t`.

The localization equations (4.6), together with the exact total rank rows
in (4.5), put all `q_t+q_(t-1)` mass of those two ranks on these two
disjoint terminal events.  Since a mark mass is at most the stationary
mass of its type, the total stationary mass of endpoints incapable of
carrying a rank greater than `t` is at least

\[
                         q_t+q_{t-1}.                         \tag{4.9}
\]

Every other endpoint has only `d` proper suffix addresses.  Summing their
maximum possible higher-rank mark mass gives (4.7).

Now `q` is nondecreasing, and there are `d-1` ranks strictly between `t`
and `r`.  Therefore

\[
 \sum_{s=t+1}^{r-1}q_s\ge(d-1)q_t.                           \tag{4.10}
\]

Both `q_t` and `q_(t-1)` tend to

\[
                         e_0=e^{-\pi/4}.                      \tag{4.11}
\]

Dividing (4.7), with (4.10), by `d` and passing to the limit would give

\[
                         e_0\le1-2e_0,                       \tag{4.12}
\]

or `3e_0<=1`.  But `e_0>9/20>1/3`.  This contradiction proves eventual
infeasibility. \(\square\)

Theorem 4.3 is the global analogue of the separated-block shadow, but it
has a different source.  The interval poset alone permits the maximal
placement; the nested endpoint rank chain does not.

## 5. What remains after `GJCLK`

The maximal-width localization `GJCLK` is retired.  The next fractional
object must allow rank-`t,t-1` marks at several lengths, so that a higher
rank may occupy a containing suffix at the same endpoint.  For length
variables `mu_(c,j)`, this means retaining (4.4)--(4.5) but replacing (4.6)
by a joint length profile whose endpoint-chain inequalities all pass.

That mixed-length fractional object is exactly the unconstrained monotone-
rotor circulation (4.4)--(4.5), already proved and independently audited.
Thus clearing denominators gives a labelled Eulerian multicover.  It still
repeats owners and targets.  The remaining theorem must round/fuse it so
that

1. every rank-`r` owner occurs exactly once;
2. every named lower target keeps one occurrence;
3. the owner succession is a simple Johnson chronology retaining or
   repairing the PBBS whole-fan bank;
4. residence and the upper-safe opening survive; and
5. the circulation becomes one rooted component with only `O(1)` sidecar.

Thus the merged route has no global order-capacity obstruction and has an
exact fractional top-row rotor in isolation.  It also has a proved
fractional incompatibility for the simplest constant-length placement.
The required mixed-length stationary join clock is already supplied by the
monotone rotor.  The next gate is therefore the genuinely integral
owner-once/named-target Euler-fusion theorem, including retention or repair
of the PBBS whole-fan bank.  This note does not prove that gate or
`nu(k)<=B(k)+O(1)`.

## 6. Dependencies

Used as inputs:

* the exact lower bound and optimal Ferrers residual vector;
* the audited monotone-rotor fractional trace theorem;
* the labelled biregular age-state lift; and
* the central local-limit/lower-tail estimates.

No finite computation, search, analytic Gram/Bessel estimate, or SSH is
used.
