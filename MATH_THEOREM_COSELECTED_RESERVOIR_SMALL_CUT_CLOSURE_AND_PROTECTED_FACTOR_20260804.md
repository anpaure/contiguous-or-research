# Co-selected common-core reservoir: small-cut closure and protected factor extension

**Date:** 2026-08-04  
**Method:** pure mathematics; minimal deficient shores, the Chao--Yu
partial-shadow theorem, and Kruskal--Katona; no computation, search, or
solver  
**Status:** unconditional asymptotic theorem.  For the co-selected
common-core witness reservoir having lower-star load at most ten, private
endpoint exposure at most ten, and forced-facet load at most nine, every
small residual Hall shore passes.  Together with the independently proved
optional co-small closure, this proves that the protected witness bank
extends to a spanning two-factor.  It does not prove connectedness of that
factor, endpoint-collar compatibility, one globally resident chronology,
or the terminal compiler.

## 0. Setting and result

Put

\[
 \mathcal L=\binom{[2m-1]}{m-1},\qquad
 \mathcal U=\binom{[2m-1]}m.
\]

Let `P` be the incidence lift of the co-selected hybrid common-core
reservoir.  Write

\[
 Z=\{x\in\mathcal L:d_P(x)=2\},\qquad
 X=\mathcal L\setminus Z,
\]

and give each owner residual capacity

\[
 c_U=2-d_P(U)\in\{0,1,2\}.
\tag{0.1}
\]

The co-selection supplies all of the following simultaneously:

\[
 \ell_P(x):=\lambda_P(\{x\})\le10,
 \qquad e_P^{\rm priv}(x)\le10
 \quad(x\in\mathcal L),
\tag{0.2}
\]

there are at most `2m` deterministic top-bank endpoint owners, and

\[
 z_U:=|N(U)\cap Z|\le9
 \quad(U\in\mathcal U).
\tag{0.3}
\]

For `A subseteq X`, put

\[
 a_U=|N(U)\cap A|,\qquad
 \kappa(A)=\sum_U\min\{c_U,a_U\}.
\tag{0.4}
\]

The residual factor criterion is

\[
                    \kappa(A)\ge2|A|
                    \qquad(A\subseteq X).
\tag{0.5}
\]

### Main theorem

For all sufficiently large `m`, the co-selected reservoir satisfies
(0.5) for every `A subseteq X`.  Consequently `P` extends to a spanning
two-factor of the Middle-Levels incidence graph.

The proof uses (0.3) through the already proved optional co-small closure.
The new content below closes the complementary small side.

## 1. Minimal deficiency leaves at most one loose owner per vertex

Assume for contradiction that (0.5) fails, and choose an
inclusion-minimal nonempty failed shore `A`.  Since all quantities are
integral,

\[
                         \kappa(A)\le2|A|-1.
\tag{1.1}
\]

Call an owner `U` **loose** for `A` when

\[
                         1\le a_U\le c_U.
\tag{1.2}
\]

### Lemma 1.1 (one loose owner)

Every `x in A` lies below at most one loose owner.

#### Proof

Removing `x` changes the summand at an owner `U superset x` by one exactly
when `a_U<=c_U`.  Therefore

\[
 q_A(x):=\kappa(A)-\kappa(A\setminus\{x\})
 =|\{U\supset x:1\le a_U\le c_U\}|.
\]

Minimality makes `A setminus {x}` safe.  Together with (1.1),

\[
 q_A(x)
 \le (2|A|-1)-2(|A|-1)=1.
\]

\(\square\)

## 2. Every nonexceptional vertex has `m-21` saturated unused owners

Let `mathcal T` be the set of deterministic top-bank endpoint owners, and
put

\[
 H=\bigcup_{U\in\mathcal T}N(U).
\tag{2.1}
\]

Since `|mathcal T|<=2m` and every owner has `m` lower facets,

\[
                         |H|\le2m^2.
\tag{2.2}
\]

An owner with `c_U=0` is an internal protected owner.  If it contains
`x in X`, both protected incidences go to members of `Z`, hence away from
`x`.  It therefore contributes one to `ell_P(x)`.  By (0.2), at most ten
internal owners contain `x`.

An endpoint owner outside `mathcal T` has one protected lower neighbour
in `Z`.  If it contains `x in X`, that neighbour is not `x`, so the owner
is counted in `e_P^priv(x)`.  Again by (0.2), at most ten private endpoint
owners contain `x`.

### Lemma 2.1 (large saturated-unused incidence degree)

Let

\[
 \mathcal F=\{U\in\mathcal U:d_P(U)=0,\ a_U\ge3\}.
\tag{2.3}
\]

Then

\[
 |\{U\in\mathcal F:x\subset U\}|\ge D:=m-21
 \qquad(x\in A\setminus H),
\tag{2.4}
\]

and

\[
                         |\mathcal F|\le|A|-1.
\tag{2.5}
\]

#### Proof

Fix `x in A setminus H`.  It has exactly `m` owner neighbours.  At most
ten are internal, at most ten are private endpoints, none is a top
endpoint, and by Lemma 1.1 at most one is loose.  Every remaining owner
has `c_U=2` and `a_U>c_U`, so it belongs to `mathcal F`.  This proves
(2.4).

Every owner in `mathcal F` contributes exactly two to `kappa(A)`.  Hence

\[
 2|\mathcal F|\le\kappa(A)\le2|A|-1.
\]

Integrality gives (2.5). \(\square\)

The point of (2.5) is that the high incidence degree (2.4) is supported
on an upper family no larger than the failed shore itself.  This is the
side balance needed by the sharp partial-shadow theorem.

## 3. A bounded-imbalance partial-shadow corollary

We record the exact form needed below.

### Lemma 3.1 (threshold shadow with side ratio)

Let

\[
 \mathcal J\subseteq\binom{[N]}r,\qquad
 \mathcal C\subseteq\binom{[N]}{r-1},
\]

with `mathcal J` nonempty, and suppose every member of `mathcal J`
contains at least `D>=2` members
of `mathcal C`.  If

\[
                         |\mathcal C|\le q|\mathcal J|
                         \qquad(q\ge1),
\tag{3.1}
\]

then

\[
 \boxed{
 |\mathcal J|\ge
 \binom{D+D/q-1}{D}.}
\tag{3.2}
\]

The top parameter in (3.2) is allowed to be real.

#### Proof

Write `|mathcal J|=binom(y,D)` for the unique real `y>=D`.  The
Chao--Yu partial-shadow theorem gives

\[
                         |\mathcal C|\ge\binom y{D-1}.
\]

Using (3.1) and the consecutive-binomial ratio,

\[
 {D\over y-D+1}
 ={\binom y{D-1}\over\binom yD}
 \le q.
\]

Thus `y>=D+D/q-1`.  Monotonicity of the generalized binomial coefficient
proves (3.2). \(\square\)

## 4. A large small-side obstruction is too large

Put

\[
 A_0=A\setminus H,\qquad a=|A|,\qquad a_0=|A_0|.
\]

Assume first that

\[
                         a\ge4m^2.
\tag{4.1}
\]

By (2.2),

\[
                         a_0\ge a-2m^2\ge2m^2,
 \qquad a\le a_0+2m^2\le2a_0.
\tag{4.2}
\]

Complement the two families from Lemma 2.1 in `[2m-1]`:

\[
 \mathcal J=\{[2m-1]\setminus x:x\in A_0\}
       \subseteq\binom{[2m-1]}m,
\]

\[
 \mathcal C=\{[2m-1]\setminus U:U\in\mathcal F\}
       \subseteq\binom{[2m-1]}{m-1}.
\]

The incidence `x subset U` becomes the facet incidence
`U^c subset x^c`.  Therefore every member of `mathcal J` contains at
least `D=m-21` members of `mathcal C`.  Equations (2.5) and (4.2) give

\[
                         |\mathcal C|\le a-1<2a_0
                         =2|\mathcal J|.
\]

Lemma 3.1 with `q=2` yields

\[
 a_0\ge\binom{\frac32D-1}{D}
       =2^{(c_*+o(1))m},
 \qquad
 c_*={3\over2}H_2(2/3)>1.
\tag{4.3}
\]

On the other hand, the near-shadow cardinality theorem localizes every
failed cut for this reservoir to

\[
 \min\{|A|,|\mathcal L|-|A|\}
       =O(m^2 2^m)=2^{m+o(m)}.
\tag{4.4}
\]

The uniform forced-facet theorem closes the optional co-small side for
the same co-selected reservoir.  Hence a remaining failed shore must be
on the small side of (4.4), and in particular

\[
                         a\le2^{m+o(m)}.
\tag{4.5}
\]

This use of the optional theorem is literal.  If
`B=X setminus A`, then the exact optional-complement identity is

\[
 \kappa(A)-2|A|=2|B|-\Omega_P(Z\cup B).
\tag{4.6}
\]

Moreover `mathcal L setminus A=Z dotcup B`.  Thus the co-small side of
(4.4) is exactly the localized optional bank closed by the uniform
forced-facet theorem; no change of reservoir or cut convention occurs.

Equations (4.3) and (4.5) are incompatible because `c_*>1`.  Therefore a
failed small-side shore cannot satisfy (4.1).

## 5. Kruskal--Katona closes the remaining polynomial range

It remains to exclude

\[
                         1\le a<4m^2.
\tag{5.1}
\]

We first sharpen the loss estimate by pricing the deterministic top
endpoints by pairs rather than by their total number.

### Lemma 5.1 (pair-priced endpoint loss)

For every `A subseteq X`,

\[
 \boxed{
 \lambda_P(A)\le
 15|A|+\min\left\{2m,\binom{|A|}{2}\right\}.}
\tag{5.2}
\]

#### Proof

The exact path-forest identity is

\[
 \lambda_P(A)=
 \sum_{x\in A}\ell_P(x)
 -\sum_{U:d_P(U)=2}(a_U-2)_+
 +E_1(A),
\tag{5.3}
\]

where `E_1(A)` counts endpoint owners having at least two facets in `A`
and whose protected edge goes outside `A`.  Discard the favourable middle
term.

For a private endpoint counted by `E_1(A)`, every selected facet below it
counts that endpoint in `e_P^priv(x)`: its unique protected facet belongs
to `Z`, while `A subseteq X`.  Since it has at least two selected facets,
the number of such private endpoints is at most

\[
 {1\over2}\sum_{x\in A}e_P^{\rm priv}(x)\le5|A|.
\]

There are at most `2m` top endpoints.  Also, every counted top endpoint
contains a pair of distinct members of `A`, and a pair of rank-`m-1` sets
has at most one common rank-`m` owner.  Choosing one pair below each
counted endpoint is therefore injective.  The top contribution is at most

\[
                         \min\left\{2m,\binom{|A|}{2}\right\}.
\]

Finally (0.2) gives `sum_(x in A) ell_P(x)<=10|A|`.  Substitution in
(5.3) proves (5.2). \(\square\)

### Lemma 5.2 (polynomial small shores have linear-in-`m` slack)

For all sufficiently large `m`, if `1<=a<4m^2`, then

\[
 \boxed{
 \sigma(A)>
 \beta_m a,
 \qquad
 \beta_m={ (m-2)(m-4)\over4(m-1)}.}
\tag{5.4}
\]

#### Proof

Complement every member of `A`.  This gives an `a`-member family
`mathcal J subseteq binom([2m-1],m)`, and the complements of `N(A)` are
exactly its lower shadow.  Write

\[
                         a=\binom xm
\]

for the unique real `x>=m`.  Kruskal--Katona gives

\[
 |N(A)|\ge\binom x{m-1}
 =a\,{m\over x-m+1}.
\tag{5.5}
\]

For sufficiently large `m`,

\[
 \binom{m+3}m=\binom{m+3}3>4m^2.
\]

Thus (5.1) forces `x<m+3`, and (5.5) gives

\[
                         {|N(A)|\over|A|}>{m\over4}.
\tag{5.6}
\]

The exact shadow-slack inequality now yields

\[
 \sigma(A)
 \ge {m-2\over m-1}(|N(A)|-|A|)
 >{m-2\over m-1}\left({m\over4}-1\right)a
 =\beta_m a.
\]

\(\square\)

### Theorem 5.3 (all polynomial small shores pass)

Every `A subseteq X` satisfying (5.1) passes the protected Ore inequality
for all sufficiently large `m`.

#### Proof

The empty shore is trivial, and a singleton is safe by
`ell_P(x)<=10<m-2`.

For `2<=a<=8`, the quantity `beta_m-15` tends to infinity linearly in
`m`, so for all sufficiently large `m`,

\[
 (\beta_m-15)a>\binom a2.
\]

For `a>=9`, again for all sufficiently large `m`,

\[
 (\beta_m-15)a
 \ge9(\beta_m-15)>2m.
\]

In both ranges, Lemmas 5.1--5.2 give

\[
 \sigma(A)>15a+\min\left\{2m,\binom a2\right\}
 \ge\lambda_P(A).
\]

Thus no shore in (5.1) fails. \(\square\)

## 6. Protected factor extension

### Theorem 6.1

For the co-selected common-core reservoir and all sufficiently large `m`,
the residual Hall system (0.5) holds for every shore.  Therefore the
protected incidence bank extends to a spanning two-factor.

#### Proof

If a failed residual shore existed, choose it inclusion-minimal.  The
near-shadow theorem puts it on the small or co-small side of (4.4).  The
uniform forced-facet theorem, using (0.3), closes the co-small side for
this same reservoir.  On the small side, Section 4 rules out
`|A|>=4m^2`, while Theorem 5.3 rules out `|A|<4m^2`.  No failed shore
remains.

The residual capacitated Hall theorem supplies an integral residual
`b`-matching with lower demand two and owner capacity `c_U`.  Adding it to
`P` gives degree two at every vertex on both shores, hence a spanning
two-factor. \(\square\)

## 7. Exact scope

The theorem closes the all-cut **protected factor-extension** gate for the
co-selected witness reservoir.  The proof uses only four quantitative
facts from that construction:

1. lower-star internal loss at most ten;
2. private endpoint exposure at most ten;
3. at most `2m` deterministic top endpoints; and
4. forced-facet load at most nine, through the co-small theorem.

It does not connect the resulting cycles, make endpoint residence cyclic,
place the reservoir inside one upper-complete physical chronology, or
solve the terminal common cap/lower compiler.  No such conclusion is
implicit in the word "factor."

## 8. Dependencies

- `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md`
- `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`
- `MATH_THEOREM_UNIFORM_FORCED_FACET_SPREAD_ELIMINATES_OPTIONAL_CO_SMALL_CORES_20260804.md`
- `MATH_THEOREM_OPTIONAL_CO_SMALL_CHARGING_LP_EXACT_FACTOR_EQUIVALENCE_20260804.md`
- `MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`
