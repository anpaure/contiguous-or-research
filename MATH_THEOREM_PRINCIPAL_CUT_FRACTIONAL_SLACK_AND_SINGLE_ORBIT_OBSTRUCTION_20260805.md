# Principal-cut fractional slack and the single-orbit obstruction for Catalan collar banks

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation or finite search  
**Status:** unconditional exact ledger and obstruction theorem.  It proves
that every short principal-upset inequality has a factor-`Theta(sqrt(r))`
margin at the fully symmetric fractional collar point.  It also proves that
one global random relabelling of an already chosen collar bank cannot improve
any worst principal cut.  Thus the remaining integral statement is a genuinely
prospective, growing-rank coloured-matching theorem; it is not a consequence of
the thinning argument in the existing three-palette bank theorem.

## 0. Notation

Work on the odd ground set

\[
 n=2r-1,\qquad
 W={n\choose r}={n\choose r-1},\qquad
 b={W\over n}-1.                                      \tag{0.1}
\]

Let `h=d(n)+1` and `s=h+1`.  A generalized balanced collar has

* `s+2` rank-`r` owners;
* `s+1` distinct rank-`(r-1)` lower colours;
* `s` distinct rank-`(r+1)` upper colours; and
* `s+1` Johnson edges.

The left seam and the first internal Johnson edge deliberately have the
same upper colour.  Every Johnson edge `AB` has lower colour
`z=A cap B` and lifts to the two middle-level incidences `zA,zB`.
Consequently one collar has exactly

\[
                         2(s+1)                     \tag{0.2}
\]

protected incidences.

For `S subseteq [n]`, `|S|=t`, put

\[
 \mathcal U_S=\{U\in{[n]\choose r}:S\subseteq U\}. \tag{0.3}
\]

For an incidence bank `P`, recall the entering charge

\[
 g_S(P)=|\{(z,U)\in E(P):S\subseteq U, S\nsubseteq z\}|.       \tag{0.4}
\]

The principal residual Hall row from
`MATH_THEOREM_PROTECTED_FACTOR_TWO_MATCHING_COORDINATE_CUT_OBSTRUCTION_20260805.md`
is

\[
                  g_S(P)\le A_S,
 \qquad A_S={2t\over r}|\mathcal U_S|.             \tag{0.5}
\]

## 1. The charge is exactly a Johnson cut

### Lemma 1.1 (boundary identity)

Let `J(P)` be the Johnson-edge bank underlying `P`.  Then

\[
 \boxed{
 g_S(P)=|\delta_{J(P)}(\mathcal U_S)|.
 }                                                     \tag{1.1}
\]

Every selected Johnson edge contributes either zero or one to the right
side.

#### Proof

Write a selected Johnson edge as

\[
 A=z+\{a\},\qquad B=z+\{b\},\qquad a\ne b.           \tag{1.2}
\]

If the incidence `(z,A)` is counted by (0.4), then `S subseteq A` but
`S not subseteq z`.  Since `A-z={a}`, necessarily `a in S`.  Hence
`S not subseteq B`, and `AB` crosses the owner upset `mathcal U_S`.
The converse is identical: if `A` contains `S` and `B` does not, the
unique exchanged label `a` lies in `S`, so `(z,A)` is counted.  The two
endpoints cannot both give entering incidences.  This proves (1.1).
`square`

This identity is useful conceptually: the missing condition is not an
additional local owner-star bound.  It is directed boundary discrepancy of
the complete protected Johnson path bank.

## 2. Exact symmetric expectation

### Lemma 2.1 (one incidence)

Fix an oriented incidence `(z,U)` with `|z|=r-1`, `U=z+{a}`.  Apply a
uniform random coordinate permutation `sigma`.  For every fixed rank-`t`
set `S`,

\[
 \Pr\bigl(S\subseteq\sigma U, S\nsubseteq\sigma z\bigr)
 ={|\mathcal U_S|\over W}{t\over r}.                 \tag{2.1}
\]

#### Proof

The image `sigma U` is a uniform rank-`r` owner.  Conditional on this
owner, the distinguished label `sigma a` is uniform among its `r` labels.
The owner contains `S` with probability `|mathcal U_S|/W`; conditional on
that event, the distinguished label belongs to `S` with probability `t/r`.
`square`

### Corollary 2.2 (one collar and one Catalan bank)

For a uniformly labelled generalized collar `C`,

\[
 \mathbb E g_S(C)
 =2(s+1){t\over r}{|\mathcal U_S|\over W}.           \tag{2.2}
\]

For `b` collars with the same symmetric one-collar marginal,

\[
 \mu_S:=\mathbb E g_S
 =2b(s+1){t\over r}{|\mathcal U_S|\over W}.          \tag{2.3}
\]

Comparing (2.3) with the exact Hall allowance (0.5) gives

\[
 \boxed{
 {\mu_S\over A_S}={b(s+1)\over W}
 <{s+1\over 2r-1}.
 }                                                     \tag{2.4}
\]

At deadline scale `s=Theta(sqrt(r))`, every principal order has a
factor-`Theta(sqrt(r))` expectation margin.  The margin is independent of
`t`; there is no exceptional short order in the fractional ledger.

## 3. The full symmetric fractional collar point

Let `mathscr C` be the catalogue of all labelled generalized balanced
collars of the fixed deadline length.  Form a resource hypergraph
`mathscr H` whose vertices are disjoint copies of

\[
 { [n]\choose r},\qquad { [n]\choose r-1},\qquad
 { [n]\choose r+1},                                  \tag{3.1}
\]

and whose hyperedge for a collar is its set of owner, distinct lower, and
distinct upper resources.  Thus

\[
                         L=3s+3                     \tag{3.2}
\]

is the hyperedge size.

Give every catalogue collar the weight

\[
                         x_C={b\over|\mathscr C|}.   \tag{3.3}
\]

Coordinate transitivity gives the exact resource loads

\[
 \begin{aligned}
  \ell_{\rm own}&={b(s+2)\over W},\\
  \ell_{\rm low}&={b(s+1)\over W},\\
  \ell_{\rm up}&={bs\over {n\choose r+1}}.
 \end{aligned}                                      \tag{3.4}
\]

All three are `Theta(s/r)=o(1)`.  In particular (3.3) is not merely a
fractional matching: every resource inequality has slack tending to one.
By (2.3), all principal inequalities simultaneously have multiplicative
slack `Theta(r/s)`.

### Theorem 3.1 (no fractional separator)

The linear system consisting of

1. total collar mass `b`;
2. capacity one on every owner, lower, and upper immediate resource; and
3. every principal-upset inequality (0.5)

has the fully symmetric fractional solution (3.3), with resource load
`O(s/r)` and principal load at most `(s+1)/(2r-1)` of capacity.

Thus a failed integral principal cut cannot be explained by a scalar,
rankwise, or symmetric fractional obstruction.

## 4. Why a single symmetrized orbit cannot round the point

The most tempting proposed repair is to take the already constructed
three-palette-disjoint bank, apply one uniform random coordinate
permutation, and use the expectation (2.3).  This is invalid for an exact
reason.

### Theorem 4.1 (single-orbit obstruction)

For every fixed bank `P`, every coordinate permutation `sigma`, and every
`t`,

\[
 \{g_S(\sigma P):|S|=t\}
 =\{g_S(P):|S|=t\}                                  \tag{4.1}
\]

as multisets.  Consequently

\[
 \boxed{
 \max_{|S|=t}g_S(\sigma P)=\max_{|S|=t}g_S(P).
 }                                                     \tag{4.2}
\]

#### Proof

Directly from (0.4),

\[
                         g_S(\sigma P)=g_{\sigma^{-1}S}(P).     \tag{4.3}
\]

As `S` runs through the rank-`t` sets, so does `sigma^{-1}S`.
`square`

Therefore orbit averaging proves Theorem 3.1 but cannot improve the worst
cut of any integral orbit member.  A successful symmetrization must mix
collars independently or in many genuinely different banks while enforcing
the three resource matchings.  One global relabelling is categorically
insufficient.

The local geometry really permits such correlations.  In the standard
collar notation, fix two labels `a,b` and impose

\[
                         \rho_1=a,\qquad \lambda_h=b.            \tag{4.4}
\]

For `S={a,b}`, the owner-membership word along

\[
                         P,M_0,M_1,\ldots,M_h,N
\]

is

\[
                         1,0,1,\ldots,1,0,0.                    \tag{4.5}
\]

Hence that single collar has

\[
                         g_{\{a,b\}}=3.                         \tag{4.6}
\]

The factor-`sqrt(r)` average margin is therefore a global decorrelation
requirement, not a pointwise property of a collar.

## 5. The exact prospective integral gate

For completeness, the full labelled collar catalogue has favourable local
codegrees.  Let `D_min` and `D_max` be its minimum and maximum resource
degrees.

### Lemma 5.1 (catalogue regularity and pair codegrees)

For `r>=16s`,

\[
 {D_{\max}\over D_{\min}}=1+O(1/s),\qquad
 \Delta_2(\mathscr H)=O(D_{\max}/r).                \tag{5.1}
\]

#### Proof

The degree identities are exact consequences of transitivity:

\[
 D_{\rm own}={|\mathscr C|(s+2)\over W},\quad
 D_{\rm low}={|\mathscr C|(s+1)\over W},\quad
 D_{\rm up}={|\mathscr C|s\over {n\choose r+1}}.    \tag{5.2}
\]

Since `{n choose r+1}/W=(r-1)/(r+1)`, their ratios give the first
claim.

For the codegree claim, condition on a fixed resource and on its slot in
the collar.  A second distinct resource can occur only at some other slot.
If the two slots are adjacent, specifying the second resource specifies
at least one of the exchanged labels, chosen uniformly from a pool of size
at least `r-h>=r/2`; there are only two adjacent slots.  At slot distance
`j>=2`, it specifies the `j` exchanged labels between the slots, and the
conditional proportion is at most

\[
 {O(1)\over {r-h\choose j}{r-h\choose j}}.           \tag{5.3}
\]

The same estimate applies when one or both resources are lower or upper
colours: an adjacent owner--facet pair costs one choice from at least
`r-h`, while every nonadjacent pair fixes the intervening exchanges.
Summing (5.3) over the `O(s^2)` ordered slot pairs gives `O(1/r)`; the
geometric tail begins with `O(1/r^2)`.  Multiplying by the conditioned
resource degree and using the first part proves (5.1). `square`

In particular,

\[
 {L\Delta_2\over D_{\min}}=O(s/r)=o(1),              \tag{5.4}
\]

although

\[
 {L^2\Delta_2\over D_{\min}}=O(s^2/r)=O(1).          \tag{5.5}
\]

This locates the diagonal issue exactly.  A fixed-uniformity
Pippenger--Spencer theorem cannot simply be invoked with `L=3s+3` tending
to infinity.  Conversely, the catalogue does not exhibit the stronger
`L Delta_2/D` obstruction that kills several earlier growing packets.

### Principal-balanced collar matching statement (PBCM)

The missing prospective theorem is now the following precise rounding
statement.

> For all sufficiently large `r`, the resource hypergraph `mathscr H`
> contains a matching `B` of exactly `b` collars for which, simultaneously
> for every `S` with `2<=|S|<=128s`,
> \[
>        \sum_{C\in B}g_S(C)\le {2|S|\over r}|\mathcal U_S|.    \tag{5.6}
> \]

The number of tested sets is only

\[
 \sum_{t\le128s}{n\choose t}=\exp(O(s\log r)),       \tag{5.7}
\]

whereas even the smallest allowance in (5.6) is
`exp(Theta(r)-O(s))`.  Thus any prospective random-greedy theorem giving a
constant-factor upper-tail estimate around (2.3) would clear every test by
a union bound, with room to spare.  What must be proved is that such tails
survive the integral three-palette matching process.  Equations
(3.4), (5.1), and (5.4) are the complete local input to that theorem.

## 6. Scope

This note proves:

* the exact Johnson-boundary meaning of every `g_S`;
* exact factor-`Theta(sqrt(r))` fractional slack at every principal order;
* strict resource slack in all three immediate palettes;
* the failure of one-global-permutation orbit symmetrization; and
* favourable `L Delta_2/D=o(1)` local catalogue geometry.

It does **not** claim PBCM.  In particular, it does not cite a
fixed-uniformity nibble theorem outside its quantified range, and it does
not infer concentration of a matching from independent-collar marginals.
The remaining issue is a growing-rank, weighted random-greedy rounding
theorem (or a direct staged four-resource construction), not another Hall
or scalar inequality.

