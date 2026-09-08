# An explicit affine nested schedule has only `o(W)` full-band profile deficit

**Status (2026-08-21).**  Every theorem-level assertion below is proved.
There is an explicit nested family of phase schedules which simultaneously
has all of the following properties.

1.  The upper phase map is injective across payload ranks at every offset.
2.  The corresponding product words are legal and internally simple through
    the whole DCC band on a fixed central payload interval.
3.  Pooling the formal phase/profile capacities over payload ranks leaves
    total upper-band deficit

    \[
      O\!\left(W_b b^{-1/4}\log^{3/4}b\right)=o(W_b),
      \qquad W_b={2b\choose b},                    \tag{0.1}
    \]

    for `H=Theta(sqrt(b log b))`.

The schedules are the prefixes of the affine rank permutation

\[
 R(x)={b-1\over2}x\pmod b.                         \tag{0.2}
\]

This is a deterministic simultaneous-offset scalar theorem.  It is stronger
than a rankwise random-schedule average, and it uses genuine interior phase
types.  It does **not** supply growing-rank tight-cycle factors, identify the
cyclic-order banks at different payload ranks, or assign distinct labelled
targets to the formal occurrences.  Those order-bank and coinstantiation
requirements remain open.

## 1. Nested schedules and their formal capacity

Let `b=2m+1` tend to infinity through odd primes.  Identify the type phases
with `Z_b` and define

\[
 R(x)=mx\pmod b,
 \qquad P_r=\{x\in\mathbb Z_b:R(x)<r\},
 \qquad 0\le r\le b.                              \tag{1.1}
\]

Thus `P_r` is the set of `A`-phases in the payload-`r` type word and its
complement is the set of `B`-phases.  The sets are nested, and passage from
`P_r` to `P_(r+1)` adds the unique phase of affine rank `r`.

Throughout the capacity statements below, `1<=q<=H` (hence `q<b` for all
large `b`) and `q<=s<=b`, the target-profile range used by the upper DCC
band.

For a phase `p` and offset `q`, put

\[
 J_p(q)=\{p+1,\ldots,p+q\}\pmod b,
 \qquad z_{r,p}(q)=|P_r\cap J_p(q)|,               \tag{1.2}
\]

and define the upper profile map

\[
 \phi_p(r)=r+z_{r,p}(q).                           \tag{1.3}
\]

Because exactly one phase is added at each payload transition,

\[
 \phi_p(r+1)-\phi_p(r)
 =1+1_{\{R^{-1}(r)\in J_p(q)\}}\in\{1,2\}.        \tag{1.4}
\]

Hence `phi_p` is injective.  This is the required upper phase-map
compatibility across all payload ranks, and the same nested family is used
at every `q`.

There is also an exact profilewise hole bound which holds for every affine
rank permutation `R(x)=ax mod b`, not only for (0.2).  Let `h_(q,s)` be the
number of phases `p` for which `s` is missing from the image of `phi_p`.
Then

\[
 \boxed{h_{q,s}\le q.}                             \tag{1.5}
\]

Indeed, a skip at the transition of affine rank `t` is caused by the newly
added phase `x=p+i`, for a unique `1<=i<=q`, and its missing profile obeys

\[
 s-1=t+\sum_{\substack{1\le j\le q\\j\ne i}}
 1_{\{(t+a(j-i)\bmod b)<t\}}.                     \tag{1.6}
\]

For fixed `i`, each summand on the right is a nondecreasing one-jump
function of `t`; the leading `t` makes the whole right side strictly
increasing.  Hence a prescribed `s` has at most one solution for each `i`,
which proves the bound.

Write

\[
 c_r={b\choose r},\qquad
 P_{q,s}=c_sc_{s-q},\qquad
 M_q={2b\choose b+q}.                              \tag{1.7}
\]

Conditionally suppose, for every `1<=r<=b-1` under physical consideration,
that the rank-`r` subsets of each local `b`-set have a tight-cycle factor.
There are `c_r/b` cyclic orders in each such factor, so a pair of local
factors supplies `c_r^2/b^2` order pairs.  At a fixed type phase, its `b`
counter points contribute `c_r^2/b` formal occurrences.
Consequently the exact pooled phase/profile capacity is

\[
 T_{q,s}={1\over b}
 \sum_{p\in\mathbb Z_b}
 \sum_{\substack{0\le r\le b\\\phi_p(r)=s}}c_r^2.
                                                               \tag{1.8}
\]

The inner sum has at most one term by (1.4).  The endpoint terms `r=0,b`
in (1.8) are only an algebraic completion of the phase map; they are not
interpreted as factor edges (indeed `c_r/b` is not integral there).  In the
physical application we retain only a fixed central payload interval, for
example `b/4<=r<=3b/4`, and set the other contributions to zero.  Section 5
shows that this restriction affects only a negligible target-profile tail.

## 2. Uniform random prefixes: the exact expectation and the exact `q=1` row

The scalar advantage is not peculiar to a guessed numerical normalization.
For comparison, let the nested sets `P_r` be the prefixes of a uniformly
random permutation of `Z_b`.  For fixed `r,p,q`, the variable
`z_(r,p)(q)` is hypergeometric.  Substituting `r=s-z` in (1.8) gives the
exact identity

\[
 \boxed{
 \mathbb E T_{q,s}
 =\sum_{z=0}^q
 {b\choose s-z}{q\choose z}{b-q\choose s-2z}.}     \tag{2.1}
\]

Terms with an inadmissible lower index are zero.

Indeed, if `n_(r,q,z)` is the number of phases whose `q`-window has
intersection size `z`, then

\[
 \mathbb E n_{r,q,z}
 =b\,{{q\choose z}{b-q\choose r-z}\over {b\choose r}}.
                                                               \tag{2.2}
\]

Multiplying (2.2) by `c_r^2/b` and summing proves (2.1).

At `q=1` there is a stronger schedule-independent identity.  As the phase
varies, its permutation rank runs once through `0,...,b-1`.  Thus

\[
 \boxed{
 T_{1,s}={1\over b}\left[(b-s)c_s^2+(s-1)c_{s-1}^2\right].}     \tag{2.3}
\]

Moreover

\[
 {T_{1,s}\over c_sc_{s-1}}\ge1-{1\over b}.        \tag{2.4}
\]

To see this, set `A=b-s`, `B=s-1`, and
`rho=c_s/c_(s-1)=(A+1)/(B+1)`.  Then

\[
 A\rho+B\rho^{-1}-(A+B)
 ={(A-B)^2(A+B+1)\over(A+1)(B+1)}\ge0.             \tag{2.5}
\]

For odd `b`, equality in (2.4) occurs at the central profile
`s=(b+1)/2`; its ratio is exactly `1-1/b`.  In particular the entire
`q=1` deficit is at most `M_1/b<=W_b/b`.

## 3. The half-step affine geometry

The special multiplier in (1.1) has inverse `-2`, because

\[
 2m\equiv-1\pmod b.                                \tag{3.1}
\]

Thus the prefix order of the physical phases is
`0,-2,-4,...` modulo `b`.  More importantly, consecutive physical phases
have an exact antipodal-pair description in affine rank.

Fix `p` and write `t=R(p)`.  If `q=2u` is even, the affine ranks in
`J_p(q)` are

\[
 \{t-k,\ t-k+(m+1):1\le k\le u\}\pmod b.          \tag{3.2}
\]

If `q=2u+1` is odd, the same `u` pairs occur together with the extra rank

\[
 e=t+m-u.                                          \tag{3.3}
\]

For `A_r=\{0,...,r-1\}` define

\[
 g_r(y)=1_{A_r}(y)+1_{A_r}(y+m+1).                 \tag{3.4}
\]

The exceptional set

\[
 E_r=\{y:g_r(y)\ne1\}                              \tag{3.5}
\]

has size

\[
 |E_r|=|2r-b|                                      \tag{3.6}
\]

and is the union of at most two cyclic intervals.  Indeed, when `r<=m`,
the two translates of `A_r` are disjoint and `E_r` is the complement of
their union, of size `b-2r`.  When `r>=m+1`, their union is all of `Z_b`
and `E_r` is their intersection, of size `2r-b`.  The interval assertion
is immediate from the two cyclic arcs.

## 4. A dominant central phase color

Put

\[
 x=s-{b+q\over2}.                                  \tag{4.1}
\]

The following deterministic lemma is the core of the construction.

### Lemma 4.1 (dominant affine phase mass)

Assume `q>=2`.  If `q=2u`, put `r=s-u`.  Then the number of phases with
`z_(r,p)(q)=u` is at least

\[
 \left[b-|2x|-q\right]_+.                         \tag{4.2}
\]

If `q=2u+1`, put

\[
 r_+=s-u,\qquad r_-=s-u-1.                         \tag{4.3}
\]

The total number of phases satisfying either

\[
 (r,z)=(r_+,u)\quad\hbox{or}\quad(r,z)=(r_-,u+1)  \tag{4.4}
\]

is at least

\[
 \left[b-4|x|-2q\right]_+.                        \tag{4.5}
\]

#### Proof

For even `q`, every pair in (3.2) contributes one point to `A_r` unless
`t-k` belongs to `E_r`.  The union of the `u` translates of `E_r` has size
at most `|E_r|+2(u-1)`, because `E_r` has at most two cyclic-interval
components.  Here

\[
 |2r-b|=|2s-q-b|=|2x|.
\]

Therefore at least `b-|2x|-2(u-1)` phases have `z=u`; (4.2) is the weaker
convenient form.

Now let `q` be odd.  Exclude every `t` for which one of the `u` pairs is
exceptional at either threshold `r_+` or `r_-`.  Also exclude the unique
`t` for which the extra rank (3.3) equals `r_-`.  At every remaining phase,
if `e<r_-` then `(r_-,u+1)` occurs, while if `e>=r_+` then `(r_+,u)`
occurs.  Since the two thresholds are adjacent, these are all remaining
possibilities.  Finally

\[
 |2r_+-b|+|2r_--b|
 =|2x+1|+|2x-1|\le4|x|+2.                         \tag{4.6}
\]

Adding the two interval-enlargement charges `2(u-1)` and the one excluded
extra rank gives at most `4|x|+2q-3` bad phases.  This proves (4.5).
\(\square\)

It follows directly from (1.8) that, throughout a central range where the
displayed payloads are admissible,

\[
 T_{q,s}\ge
 \begin{cases}
 \displaystyle
 \left(1-{|2x|+q\over b}\right)c_{s-q/2}^2,
       &q\text{ even},\\[6pt]
 \displaystyle
 \left(1-{4|x|+2q\over b}\right)
 \min(c_{r_+}^2,c_{r_-}^2),
       &q\text{ odd}.
 \end{cases}                                      \tag{4.7}
\]

Thus a single central color, or two adjacent central colors, already
supplies almost an entire profile row.  The proof does not average over
permutations or reselect the schedule at different offsets.

## 5. Binomial comparison and the aggregate deficit

Assume

\[
 H\le C_0\sqrt{b\log b},                           \tag{5.1}
\]

where `C_0` is fixed.  Choose a sufficiently large fixed `K` and restrict
temporarily to

\[
 |x|\le L:=K\sqrt{b\log b}.                        \tag{5.2}
\]

Let

\[
 F(y)=\log {b\choose b/2+y},                       \tag{5.3}
\]

using the gamma-function interpolation.  Uniformly for
`|y|<=G=H+L+1=o(b)`, the elementary central-binomial expansion is

\[
 F(y)=F(0)-{2y^2\over b}
 +O\!\left({G^2\over b^2}+{G^4\over b^3}\right). \tag{5.4}
\]

For completeness, differentiate (5.3) twice.  Symmetry gives `F'(0)=0`,
and the standard estimate `psi_1(v)=1/v+O(1/v^2)` for the trigamma function
gives

\[
 F''(y)=-{4\over b}
 +O\!\left({1\over b^2}+{y^2\over b^3}\right).
\]

Two integrations prove (5.4).

The two target factors in (1.7) have centered displacements
`x+q/2` and `x-q/2`.  For even `q`, the source index in (4.7) has
displacement `x`.  For odd `q`, the two possible source displacements are
`x+1/2` and `x-1/2`.  Equations (4.7)--(5.4), together with
`log(1-v)>=-2v` for `0<=v<=1/2`, therefore give

\[
 \boxed{
 {T_{q,s}\over P_{q,s}}
 \ge \exp\!\left({q^2\over b}-\varepsilon_b\right)}            \tag{5.5}
\]

uniformly for `2<=q<=H` and (5.2), where

\[
 \varepsilon_b
 =C\left({H+L+1\over b}+{G^2\over b^2}+{G^4\over b^3}\right)
 =O\!\left(\sqrt{\log b\over b}\right).           \tag{5.6}
\]

The harmless odd-`q` loss
`4[(|x|+1/2)^2-x^2]/b=O((|x|+1)/b)` is included in
`epsilon_b`.

For `q=1`, (2.4) gives the same lower bound after increasing the absolute
constant in `epsilon_b`, since `log(1-1/b)>=-2/b`.

In particular, a central profile can be deficient only when

\[
 q^2<b\varepsilon_b,                               \tag{5.7}
\]

and every such profile has relative deficit at most
`1-exp(-epsilon_b)<=epsilon_b`.  Since
`sum_sP_(q,s)=M_q<=W_b`, summing (5.7) gives

\[
 \sum_{q\le H}\sum_{|x|\le L}[P_{q,s}-T_{q,s}]_+
 \le O\!\left(\sqrt{b}\,\varepsilon_b^{3/2}W_b\right)
 =O\!\left(W_b b^{-1/4}\log^{3/4}b\right).         \tag{5.8}
\]

It remains only to restore the omitted profiles.  Standard binomial bounds
give, uniformly in this band,

\[
 {P_{q,s}\over W_b}
 \le {C\over\sqrt b}
 \exp\!\left[-c{q^2+x^2\over b}\right].           \tag{5.9}
\]

Choose `K` in (5.2) large enough.  Summing (5.9) first over `s` with
`|x|>L` and then over `q<=H` gives `o(W_b)`.  On (5.2), every payload in
(4.7) lies in `[b/4,3b/4]` for all sufficiently large `b`, so only the
declared central payload bank was used.  Combining (2.4), (5.8), and the
tail estimate proves (0.1).  Complementation gives the identical lower-band
scalar statement.

## 6. Physical legality, torus enumeration, and internal simplicity

The scattered affine type words are fully legal on the same central payload
range.  Put

\[
 f=b+H+2,
 \qquad b/4\le r\le3b/4.                          \tag{6.1}
\]

Any physical interval of length `f-1=b+H+1` contains one complete type
period and at most `H+1` additional phases.  It therefore contains at most

\[
 r+H+1<b
 \quad\hbox{`A`-events},\qquad
 b-r+H+1<b
 \quad\hbox{`B`-events}                            \tag{6.2}
\]

for all large `b`.  A local stream symbol recurs only after `b` events of
its own type, so (6.2) proves same-symbol separation at least `f`.

Likewise, every type interval of length between `b-H` and `b+H+1`
contains between `1` and `b-1` events of each type: at the lower endpoint
it contains at least `r-H` `A`-events and `b-r-H` `B`-events, while (6.2)
controls the upper endpoint.  Thus every local interval set used throughout
the DCC band is nonempty and proper.

Finally, after one type period the two stream counters advance by

\[
 (r,b-r)\equiv(r,-r)\pmod b.                       \tag{6.3}
\]

Because `b` is prime and `0<r<b`, this translation has order `b` on each
counter-sum diagonal.  The `b` type phases occupy the `b` different
diagonals, since the counter sum advances by one at each physical step.
Hence the `b^2` length-`b` windows enumerate every pair of local cyclic
intervals exactly once.  If two windows, among the `b^2` starting times in
one fundamental period and of any fixed length in the DCC band, were equal,
their intersections with the two local ground sets would be equal proper
cyclic intervals and would recover both stream endpoints; (6.3) would then
recover the physical time modulo `b^2`.  Thus all those windows are pairwise
distinct within the fundamental period.

This verifies the legality, torus-enumeration, and internal-simplicity
hypotheses without any randomness or offset-dependent choice.

## 7. Exact consequence and surviving gate

The clustered schedule `A^rB^(b-r)` concentrated almost all central profile
mass in two endpoint colors.  Independent rank relabeling then had a
two-coupon obstruction, while canonical product hooks overloaded the very
small interior-color inventory.  The affine prefix schedule changes that
geometry: its antipodal phase pairs put `b-O(q+|x|)` occurrences into a
central interior color (two adjacent colors when `q` is odd), and the
binomial curvature supplies the `exp(q^2/b)` surplus in (5.5).

What has been proved is nevertheless a **formal profile-capacity** theorem.
Formula (1.8) pools occurrence counts supplied by local order pairs.  To
obtain actual labelled chains one must still:

1. construct or replace the required growing-rank tight-cycle factors;
2. couple their cyclic orders coherently across the neighboring payload
   ranks used by the nested phase injection;
3. assign labelled target sets injectively to the occurrence tokens at all
   offsets while retaining one common physical chain bank.

No step above asserts those three conclusions.  The result removes the
deterministic scalar/profile obstruction for a genuinely nested,
band-coherent schedule and isolates the remaining problem at the labelled
order-bank level.
