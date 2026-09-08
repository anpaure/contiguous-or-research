# The complete low rolling-collar bank extends to one middle-levels two-factor

**Date:** 2026-08-06  
**Method:** stabilizer-orbit halo avoidance, exact rolling-window exposure,
protected Ore localization, Kruskal--Katona, and optional-core partial
shadows; no computation or search  
**Status:** unconditional asymptotic owner/`q1` theorem.  Every target of
rank at most the deadline receives one literal rolling-star source collar,
and all collars coexist in one spanning owner/lower-`q1` two-factor.  The
theorem does not yet impose the global upper deck, zero-gap residence,
component count, or terminal common cap.

## 1. Complete target bank

Work in the middle-levels incidence graph

\[
 \mathcal L=\binom{[2m-1]}{m-1},
 \qquad
 \mathcal U=\binom{[2m-1]}m,
 \qquad W=|\mathcal L|=|\mathcal U|.
\tag{1.1}
\]

Let `d=O(sqrt(m))` and assume eventually

\[
                              4d+4\le m.             \tag{1.2}
\]

Put

\[
 \mathcal S_d=\{S\subseteq[2m-1]:1\le |S|\le d\},
 \qquad
 L_d=|\mathcal S_d|=2^{o(m)}.                        \tag{1.3}
\]

For every `S in mathcal S_d`, take the rolling-star collar from
`MATH_THEOREM_ARBITRARY_LOW_TARGET_ROLLING_STAR_COLLAR_AND_Q1_EXTENSION_20260806.md`.
It consists of a simple rank-`m` Johnson path

\[
 T_i=B\cup\{z_i,\ldots,z_{i+d}\}                     \tag{1.4}
\]

of at most `2d+2` owners, whose incidence lift `P_S` has at most `4d+2`
edges.  The target coordinates occur as consecutive markers and the
corresponding maximal source envelopes may be thinned to singleton letters,
giving one literal source interval with OR exactly `S`.

## 2. Full exposure halos can be separated

For one collar define its full incidence halo to contain:

1. every protected owner and protected lower colour;
2. every lower facet of a protected owner;
3. every owner containing a protected lower colour; and
4. every immediate-upper colour of the owner path.

This halo has `O(md)` named central-rank resources.

Fix the target `S` pointwise and apply a uniform permutation of its
complement to the background and non-target marker labels.  Every named
halo role has rank `m+O(1)` and intersects `S` in at most `d` labels.  Its
stabilizer orbit therefore has size

\[
 \binom{2m-1-|S|}{m+O(d)-O(d)}=2^{2m-o(m)}.          \tag{2.1}
\]

There are

\[
                         O(m^2d^2L_d^2)=2^{o(m)}      \tag{2.2}
\]

ordered pairs of packet halo roles.  Choosing the complement permutations
independently, one fixed pair collides with probability at most
`2^(-2m+o(m))`.  The union bound is less than one.

### Lemma 2.1 (halo-disjoint collar bank)

The collars may be chosen so that their complete incidence halos are
pairwise disjoint.

This is the target-stabilizer specialization of the general
subexponential packet-packing theorem.  Notice that the target itself is
not moved.

## 3. Uniform exposure of one rolling path

Let `P` be the union of the halo-disjoint incidence paths.  Then `P` is a
path forest and `Delta(P)<=2`.

For `x in mathcal L`, let

\[
                         \ell_P(x)=\lambda_P(\{x\})
\]

be its singleton protected-Ore loss.  Let `e_P^priv(x)` be the number of
protected endpoint owners containing `x` whose unique protected lower
neighbour is internal to a protected path.  Finally put

\[
 Z=\{x\in\mathcal L:d_P(x)=2\},
 \qquad z_U=|N(U)\cap Z|.                             \tag{3.1}
\]

### Lemma 3.1 (two-exposure bounds)

For the complete collar bank,

\[
 \boxed{
 \ell_P(x)\le2,
 \qquad e_P^{\rm priv}(x)\le2,
 \qquad z_U\le2.}                                    \tag{3.2}
\]

#### Proof

Within one rolling path, for `i<j` one has

\[
                         |T_i\cap T_j|=m-(j-i)        \tag{3.3}
\]

as long as the displayed windows overlap, and a still smaller intersection
after they separate.  A rank-`m-1` set can be a facet of both owners only
when `j-i<=1`.  Hence a fixed lower vertex lies below at most two protected
owners.  This bounds both the singleton loss and private endpoint exposure
by two.

The protected lower colours are

\[
 I_i=B\cup\{z_{i+1},\ldots,z_{i+d}\}.
\]

For `i<j`,

\[
                         |I_i\cup I_j|=m-1+(j-i)      \tag{3.4}
\]

while the marker windows overlap.  One rank-`m` owner can contain both only
when `j-i<=1`; it therefore contains at most two protected lower colours.
Halo disjointness says that no vertex receives exposure from a second
collar.  This proves `(3.2)`.  \(\square\)

The total protected incidence size is

\[
                         e=|E(P)|=O(dL_d)=2^{o(m)}.   \tag{3.5}
\]

## 4. Every failed shore is subexponentially small or co-small

The exact protected Ore criterion is

\[
                         \lambda_P(A)\le\sigma(A)
 \qquad(A\subseteq\mathcal L).                       \tag{4.1}
\]

The protected-Ore small/co-small localization theorem says that a failed
shore satisfies

\[
 \min\{|A|,W-|A|\}
 <{m(m-1)\over2m-1}e=2^{o(m)}.                       \tag{4.2}
\]

We exclude the two alternatives separately.

## 5. The small side

For a path forest whose endpoint owners are all private, the exact loss
identity gives

\[
 \lambda_P(A)
 \le\sum_{x\in A}\ell_P(x)+E_1(A),                  \tag{5.1}
\]

where `E_1(A)` counts endpoint owners containing at least two members of
`A` and whose protected edge goes outside `A`.  Every such endpoint is
counted by at least two incidences in
`sum_(x in A)e_P^priv(x)`.  Lemma 3.1 therefore gives

\[
                         E_1(A)\le |A|,
 \qquad
                         \lambda_P(A)\le3|A|.         \tag{5.2}
\]

Suppose now that `a=|A|=2^{o(m)}`.  Write

\[
                         a=\binom xm,
 \qquad x=m+t_m
\]

with real `x>=m`.  Necessarily `t_m=o(m)`: if `t_m>=epsilon m` along a
subsequence, the binomial coefficient is `2^(Omega(m))`.

Complementation and Kruskal--Katona give

\[
 {|N(A)|\over |A|}
 \ge {\binom x{m-1}\over\binom xm}
 ={m\over t_m+1}\longrightarrow\infty.              \tag{5.3}
\]

The exact shadow-slack inequality then gives

\[
 \sigma(A)
 \ge {m-2\over m-1}\bigl(|N(A)|-|A|\bigr)
 >3|A|\ge\lambda_P(A)                                \tag{5.4}
\]

for all sufficiently large `m`.  Thus no small shore from `(4.2)` fails.

## 6. The co-small side

Let

\[
                         X=\mathcal L\setminus Z.
\]

The residual Hall system may be tested on shores contained in `X`.
Complement such a shore inside `X`, obtaining an optional bank `B`.
If the optional deficiency were positive, choose an inclusion-minimal
positive core `B^-` and let `Q` be its positive owner family.  The exact
optional-core ledger gives

\[
                         |Q|>|B^-|.                  \tag{6.1}
\]

An owner has optional gap

\[
                         g_U=m-z_U\ge m-2
\]

and residual capacity at most two.  Positivity therefore forces every
`U in Q` to contain at least

\[
                         D=m-3                       \tag{6.2}
\]

members of `B^-`.  The sharp one-sided partial-shadow theorem and `(6.1)`
give

\[
 |B^-|
 \ge\binom{2D-1}{D-1}+1
 =\binom{2m-7}{m-4}+1
 =2^{2m-o(m)}.                                      \tag{6.3}
\]

On the other hand the co-small alternative in `(4.2)` gives

\[
                         |B^-|\le|B|=2^{o(m)},       \tag{6.4}
\]

a contradiction.  Hence no co-small shore fails.

## 7. Complete q1 extension

### Theorem 7.1

For all sufficiently large `m`, the union `P` of one rolling-star collar
for every nonempty target of rank at most `d` extends to a spanning
two-factor of `ML_m`.

#### Proof

Lemma 2.1 selects the halo-disjoint bank, and Lemma 3.1 gives its uniform
exposures.  If extension failed, the exact protected Ore criterion would
give a failed shore.  Equation `(4.2)` makes it small or co-small.  Sections
5 and 6 exclude both alternatives.  Bipartite `b`-matching integrality then
supplies the residual factor.  \(\square\)

In the retained source collars, each target block may be thinned to its
singleton marker letters.  Therefore the theorem simultaneously provides:

* one literal source interval for every target of rank at most `d`;
* distinct rank-`m` owners;
* a simple immediate-lower palette; and
* one global spanning owner/`q1` two-factor containing every collar.

## 8. Remaining global rows

The arbitrary residual two-factor supplied by Theorem 7.1 need not have a
bounded number of components or a complete immediate-upper palette.  Nor
does it automatically extend the clipped collar runs into globally legal
positive and zero gaps.  The remaining statement is therefore a decorated
completion theorem:

> Complete the halo-disjoint rolling-collar bank to a resident,
> upper-complete, bounded-component owner chronology while retaining one
> terminal common-cap/compiler state.

The low-target source language, its simultaneous physical resource
packing, and the entire owner/lower-`q1` factor extension are no longer
parts of that gate.

