# Adjacent principal-star unions: exact fibres, pivot-swap loss, and protected closure

**Date:** 2026-08-04  
**Status:** unconditional asymptotic pure-mathematical theorem for the
constant-spread clipped-resident common-core reservoir.  It closes the
two-level partial-colex obstruction isolated by the capped-shadow theorem.
More generally, it closes every fixed-size union of principal up-stars
whose cores share a common codimension-one root.  No computation, search,
or solver is used.

## 0. Setting and reservoir properties

Put

\[
 n=2m-1,qquad k=m-1,qquad
 \mathcal L={{[n]}\choose k},\qquad
 \mathcal U={{[n]}\choose m}.
\]

Let `mathscr P` be the protected incidence bank supplied by the frozen
constant-spread, clipped-resident common-core reservoir.  We use only the
following proved properties of that bank.

1. Its projection is a disjoint union of simple Johnson paths on
   `mathcal U`.
2. Along every protected path, the owners containing a fixed coordinate
   form an interval.
3. For a core `C` of size `c`, with `r=m-c`, at most

   \[
                            H_r(m)=\sum_{j=0}^r{m\choose j}
   \tag{0.1}
   \]

   low fixed-trace paths meet the owner star `{U:C subseteq U}`.  There
   are only `m` top paths and at most `H_d=2^{o(m)}` high paths in total.
4. Every singleton lower cut has protected loss at most `R_0=10`, and
   every lower cut `A` satisfies

   \[
                            \lambda_{\mathscr P}(A)
                            \le15|A|+2m.
   \tag{0.2}
   \]

These are the exact inputs of
`MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md`.

## 1. Two adjacent cores

Choose

\[
 C_0=H\cup\{a\},\qquad C_1=H\cup\{b\},
 \qquad a\ne b,qquad |C_0|=|C_1|=c,
\tag{1.1}
\]

and put

\[
 r=m-c,qquad
 A=\mathcal A_{C_0}\cup\mathcal A_{C_1},
 \qquad
 \mathcal A_C=\{X\in\mathcal L:C\subseteq X\}.
\tag{1.2}
\]

Thus

\[
 A=\{X:H\subseteq X,\ X\cap\{a,b\}\ne\varnothing\}.
\tag{1.3}
\]

Write

\[
 Q=\{U\in\mathcal U:H\subseteq U,\
                         U\cap\{a,b\}\ne\varnothing\}.
\tag{1.4}
\]

### Theorem 1.1 (exact owner fibres)

For `U in mathcal U`, let `s=|U cap {a,b}|`.  Then

\[
 a_U=|\{X\in A:X\subset U\}|=
 \begin{cases}
 0,&H\not\subset U\text{ or }s=0,\\
 r,&H\subset U\text{ and }s=1,\\
 r+1,&H\subset U\text{ and }s=2.
 \end{cases}
\tag{1.5}
\]

Put `N=m+r-2` and `B=binom(N,r-1)`.  If `r>=2`, then

\[
 \boxed{|A|=2{m+r-1\choose r-1}-{m+r-2\choose r-2}
             ={2m+r-1\over m}B,}
\tag{1.6}
\]

and

\[
 \boxed{
 \sigma(A)=
 {4(m-r)\over m}{N\choose r}
 +{2(m-r-1)\over m}{N\choose r-1}}
\tag{1.7}
\]

or equivalently

\[
 \boxed{
 {\sigma(A)\over|A|}
 ={2\bigl(2(m-r)(m-1)/r+m-r-1\bigr)
    \over2m+r-1}.}
\tag{1.8}
\]

For `r=1`, the family consists of the two adjacent lower vertices
`C_0,C_1` and

\[
                            \boxed{\sigma(A)=2(m-2).}
\tag{1.9}
\]

#### Proof

Assume `H subset U`.  There are `r+1` elements of `U-H`.  If `U`
contains one pivot, deleting that pivot is the unique deletion outside
`H` which destroys (1.3), leaving `r` selected facets.  If it contains
both pivots, every deletion outside `H` leaves at least one pivot, giving
`r+1` selected facets.  This proves (1.5).

The numbers of owners in the last two rows of (1.5) are

\[
                         2{N\choose r},\qquad {N\choose r-1}.
\tag{1.10}
\]

Inclusion--exclusion between the two stars gives the first expression in
(1.6); elementary adjacent-binomial ratios give the second.  For `r>=2`,
the weighted boundary contributions of fibres `r` and `r+1` are

\[
 {2(m-r)\over m},\qquad {2(m-r-1)\over m},
\]

which, with (1.10), proves (1.7).  Using
`binom(N,r)=(m-1)B/r` gives (1.8).

When `r=1`, every nonshared owner has fibre one and the shared owner has
fibre two.  Capping at two therefore loses no mass relative to the two
singleton cuts, proving (1.9). \(\square\)

The partial-colex family of the capped-shadow theorem is precisely (1.2)
with `m=4q` and `r=q+1` up to the harmless indexing convention for the
two exchanged core coordinates.  Formula (1.8) recovers its asymptotic
ratio six.

## 2. Exact protected loss: crossings plus pivot swaps

Project every protected two-incidence lower colour to the corresponding
Johnson edge between its two owner endpoints.  Let

* `partial_mathscrP Q` be the number of projected protected edges with
  exactly one owner endpoint in `Q`; and
* `tau_mathscrP(H;a,b)` be the number of projected protected edges whose
  endpoints both contain `H`, one contains `a` but not `b`, the other
  contains `b` but not `a`, and whose common lower facet contains neither
  pivot.

The second kind is exactly a direct `a<->b` exchange.

### Theorem 2.1 (two-star crossing identity)

If `r>=2`, then

\[
 \boxed{
 \lambda_{\mathscr P}(A)
 =|\partial_{\mathscr P}Q|
  +2\tau_{\mathscr P}(H;a,b).}
\tag{2.1}
\]

Every one of the reservoir's protected paths contributes at most four to
the right side.  Consequently

\[
 \boxed{
 \lambda_{\mathscr P}(A)
 \le4\bigl(2H_r(m)+m+H_d\bigr).}
\tag{2.2}
\]

#### Proof

For `r>=2`, every nonzero fibre in (1.5) has size at least two.  Hence the
local protected loss at an owner `U in Q` is exactly the number of its
protected lower incidences whose lower endpoint does not lie in `A`.

Consider one projected edge `UV`, with lower intersection `X=U cap V`.
If exactly one of `U,V` lies in `Q`, then `X notin A`; otherwise both
supersets of `X` would lie in `Q`.  This contributes one incidence to the
loss.  If both owners lie in `Q` but `X notin A`, then `X` contains `H`
but no pivot.  Since adjacent owners differ by one exchange, they must
have the respective singleton pivot sets `{a}` and `{b}`.  This is a
direct pivot swap, and both protected incidences are counted.  There are
no other possibilities.  This proves (2.1).

There is a shorter sharp estimate.  At every owner, a lower incidence
lost by the union is lost by each individual star which is active there.
Thus, path by path,

\[
 \lambda_{\mathscr P}(A;	ext{path})
 \le
 \lambda_{\mathscr P}(\mathcal A_{C_0};	ext{path})
 +\lambda_{\mathscr P}(\mathcal A_{C_1};	ext{path}).
\]

For either individual star, its owner set on the path is an interval, so
its loss is its crossing count and is at most two.  The union path loss is
therefore at most four.  In the language of (2.1), this also shows why a
pivot swap cannot be added independently to four boundary crossings.

A contributing path meets at least one of the two principal owner stars.
Property 3 in Section 0 bounds the low paths meeting each one by `H_r(m)`;
the top and high banks contain only `m` and `H_d` paths in total.  This
proves (2.2). \(\square\)

The factor two on the pivot-swap term is essential.  A direct swap stays
inside the union of the two owner stars, but its common lower facet lies
outside the union of the two lower stars.  Treating loss as ordinary
boundary crossing alone would miss both incidences.

## 3. Uniform protected closure

### Theorem 3.1 (adjacent-star union is safe)

For all sufficiently large `m`, every family (1.2), for every
`1<=r<=m-1`, satisfies

\[
                         \boxed{\lambda_{\mathscr P}(A)\le\sigma(A).}
\tag{3.1}
\]

Thus the connected two-level partial-colex family from the capped-shadow
obstruction is not a protected Ore obstruction for the constant-spread
resident reservoir.

#### Proof

First let `r=1`.  Apart from the one shared owner, local loss is the same
as in the two singleton cuts.  At the shared owner, union loss can exceed
the sum of singleton losses by at most one, and only when that owner is a
protected path endpoint directed to an unselected lower facet.  Therefore

\[
 \lambda_{\mathscr P}(A)le
 l_{\mathscr P}(C_0)+l_{\mathscr P}(C_1)+1\le21.
\]

Equation (1.9) closes this case for `m>=13`.

Now assume `r>=2`.  Since every nonzero owner fibre is at most `r+1`, the
identity

\[
 \sigma(A)=(m-2)|A|-\sum_U(a_U-2)_+
\]

gives

\[
 \boxed{
 \sigma(A)\ge\left({2m\over r+1}-2\right)|A|.}
\tag{3.2}
\]

Indeed `(a-2)/a<=(r-1)/(r+1)` for `a<=r+1`, and
`sum_U a_U=m|A|`.

If `r<=m/10` and `m>=190`, the coefficient in (3.2) is at least `17`.
Also `|A|>=m+1`.  The global spread estimate (0.2) therefore gives

\[
 \lambda_{\mathscr P}(A)le15|A|+2m<17|A|\le\sigma(A).
\]

It remains to take `r>=m/10`.  The first term in (1.7) gives

\[
 \sigma(A)\ge {4\over m}{m+r-2\choose r-1}.
\tag{3.3}
\]

Indeed,

\[
 (m-r){m+r-2\choose r}
 ={(m-r)(m-1)\over r}{m+r-2\choose r-1}
 \ge {m+r-2\choose r-1},
\]

because `(m-r)(m-1)-r=m(m-1-r)>=0`.

If `r<=m/2`, then

\[
 {\binom{m+r-2}{r-1}\over\binom mr}
 ={r\over m+r-1}
   {\binom{m+r-1}{r}\over\binom mr}
 \ge {r\over m+r-1}
      \left(1+{r-1\over m}\right)^r.
\tag{3.4}
\]

Uniformly for `r>=m/10`, the last factor is exponential in `m`, whereas

\[
                         H_r(m)\le(r+1){m\choose r}.
\]

If `r>=m/2`, then

\[
 {m+r-2\choose r-1}
 \ge2^{(\frac32H_2(2/3)+o(1))m},
\tag{3.5}
\]

uniformly, while `H_r(m)<=2^m`.  Since
`(3/2)H_2(2/3)>1` and `H_d=2^{o(m)}`, equations
(3.3)--(3.5) show that `sigma(A)` exceeds the right side of (2.2) for all
sufficiently large `m`, uniformly throughout `r>=m/10`.  This proves
(3.1).  The entropy comparison is uniform: if `alpha=r/m`, the leading
natural-log exponent in the second range is

\[
 f(\alpha)=(1+\alpha)\log(1+\alpha)-\alpha\log\alpha.
\]

Since `f'(alpha)=log((1+alpha)/alpha)>0`, its minimum on `[1/2,1]`
is attained at `alpha=1/2`, giving exactly the exponent in (3.5).
\(\square\)

## 4. Fixed many adjacent centres

The same proof has a clean fixed-`h` extension.  Let

\[
 C_i=H\cup\{p_i\},\qquad 1\le i\le h,
\]

where the pivots are distinct, every core has size `c`, and `h` is fixed.
Put

\[
 A_h=\bigcup_{i=1}^h\mathcal A_{C_i},
 \qquad r=m-c,
 \qquad R=m+r-h.
\tag{4.1}
\]

### Theorem 4.1 (fixed-centre fibres and closure)

An owner containing `H` and exactly `s` pivots has fibre

\[
 a_U=\begin{cases}r,&s=1,\\r+1,&s>=2,
       \end{cases}
\tag{4.2}
\]

and the number of such owners is

\[
                         N_s={h\choose s}{R\choose r+1-s}.
\tag{4.3}
\]

For `r>=2`,

\[
 \boxed{
 |A_h|=\sum_{s=1}^{\min(h,r)}{h\choose s}{R\choose r-s},}
\tag{4.4}
\]

\[
 \boxed{
 \sigma(A_h)={2(m-r)\over m}N_1
 +{2(m-r-1)\over m}\sum_{s=2}^{\min(h,r+1)}N_s.}
\tag{4.5}
\]

Its protected loss is

\[
 \lambda_{\mathscr P}(A_h)
 =|\partial_{\mathscr P}Q_h|+2\tau_{\mathscr P}(H;\{p_i\}),
\tag{4.6}
\]

where `Q_h` is the union of the `h` owner stars and `tau` counts direct
exchanges between two distinct singleton-pivot states.  Each path
contributes at most

\[
                         2h,
\]

so

\[
 \boxed{
 \lambda_{\mathscr P}(A_h)
 \le2h\bigl(hH_r(m)+m+H_d\bigr).}
\tag{4.7}
\]

For every fixed `h`, all such families are safe for all sufficiently large
`m`, uniformly in `1<=r<=m-1`.

#### Proof

The fibre computation is the same deletion argument as Theorem 1.1.
Choosing the pivots and the residual owner coordinates proves (4.3), and
choosing the `r` coordinates of a lower set outside `H` proves (4.4).
The weighted boundary formula gives (4.5).

The local proof of (4.6) is unchanged: an internal protected edge can
have a lower intersection outside `A_h` only when its endpoints carry two
different singleton pivots.  For the sharp path bound, use the same local
domination as in Theorem 2.1.  Every incidence lost by the union is lost
by each active individual star, so the union loss on a path is at most the
sum of the `h` individual-star losses.  Each individual star is an
interval on the path and contributes at most two.  Hence the total is at
most `2h`.

At most `hH_r+m+H_d` paths meet `Q_h`, proving (4.7).

For `r=1`, the family consists of `h` singleton lower vertices,
`sigma=h(m-2)`, and comparison with the singleton losses gives

\[
 \lambda_{\mathscr P}(A_h)le hR_0+{h\choose2},
\]

which is safe for fixed `h` and large `m`.

The displayed value of `sigma` is exact: there are `h(m+1-h)` owners
with fibre one and `binom(h,2)` owners with fibre two.  Therefore

\[
 \sigma={m-2\over m}
 \left(h(m+1-h)+2{h\choose2}\right)=h(m-2).
\]

For `r>=2`, the maximum nonzero fibre remains `r+1`, so (3.2) holds with
`A_h` in place of `A`.  It closes `r<=m/10` exactly as before.  For
`r>=m/10`, the `s=1` term of (4.5) gives

\[
 \sigma(A_h)\ge {2h\over m}{m+r-h\choose r}.
\]

For fixed `h`, the same product estimate as (3.4) is exponential over
`binom(m,r)` when `r<=m/2`, and the same entropy estimate as (3.5)
dominates `2^m` when `r>=m/2`.  It therefore dominates (4.7) uniformly.
More explicitly, in the first range

\[
 {{m+r-h\choose r}\over {m\choose r}}
 \ge\left(1+{r-h\over m}\right)^r
 =\exp(\Omega_h(m))
\]

uniformly for `r>=m/10`; in the second range, the fixed shift `h`
changes the exponent by only `o(m)`, and the increasing function `f`
above again has its minimum at `r/m=1/2`.
\(\square\)

## 5. Consequence and frontier

The scalar capped-shadow obstruction is now geometrically closed:

* the two-level initial-colex family is the union of two adjacent
  principal stars;
* its only new protected-loss mechanism is a direct pivot swap, priced
  exactly twice;
* interval traces bound ordinary crossings plus swaps by four per path;
* the path catalogue meeting the union is at most
  `2H_r+m+H_d`; and
* the exact slack dominates that count in every rank regime.

The argument extends to every fixed number of centres.  What it does not
yet close is a shifted family requiring a number of star centres growing
with `m`, or a positive-defect family which has no bounded-centre
principal-star representation.  Those are the remaining capped-shadow
geometries relevant to protected Ore extension.

## 6. Dependencies and scope

The proof uses the frozen constant-spread reservoir theorem

* `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md`,

and its clipped-resident path construction

* `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md`.

The exact protected-loss definition is from

* `MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md`.

No conclusion is made here about extension components, endpoint collars,
or the common cap after the protected two-factor is chosen.
