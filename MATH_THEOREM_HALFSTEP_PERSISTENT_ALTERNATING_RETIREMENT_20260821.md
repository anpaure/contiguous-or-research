# Persistent alternating phases give an `o(W_b)` half-step retirement point

**Status (2026-08-21).**  The scalar fractional theorem below is proved.  It
constructs one explicit feasible point of the half-step affine retirement LP
whose aggregate quota deficit is `o(W_b)` for
`H=O(sqrt(b log b))`.  The construction does not use the proportional
prefix envelope; that envelope has a separate positive adjacent-variation
obstruction.

For clarity, the phase-preserving retirement LP used here has one variable
`x_(r,p)(q)` for every retained central source split `r`, affine phase `p`,
and layer `q`.
Writing `s_(r,p)(q)` for its profile, feasibility means

\[
 0\le x_{r,p}(H)\le\cdots\le x_{r,p}(1)\le {L_r\over b},
 \qquad
 \sum_{(r,p):s_{r,p}(q)=s}x_{r,p}(q)\le P_{q,s}.             \tag{0.1}
\]

Its optimum quota deficit is

\[
 \mathfrak D_{\rm ret}
 =\sum_{q=1}^H M_q-\max_x\sum_{q=1}^H\sum_{r,p}x_{r,p}(q).   \tag{0.2}
\]

## 1. The exact Boolean two-orientation flow

Let `b` be an odd prime and write

\[
 C_t={b\choose t},\qquad L_r=C_r^2,
 \qquad W_b={2b\choose b},\qquad
 M_q={2b\choose{b+q}}.                                      \tag{1.1}
\]

For `u>=0` and `u<=r<=b-u`, put

\[
 E_{r,u}=C_{r+u}C_{r-u}.                                    \tag{1.2}
\]

There are two persistent alternating orientations, denoted `A` and `B`.
At even layer `q=2u` define

\[
 A^E_{r,u}=E_{r,u}{b-r-u\over b-2u},
 \qquad
 B^E_{r,u}=E_{r,u}{r-u\over b-2u};                          \tag{1.3}
\]

at odd layer `q=2u+1` define

\[
 A^O_{r,u}=E_{r,u}{b-r-u\over b+2u+1},
 \qquad
 B^O_{r,u}=E_{r,u}{r-u\over b+2u+1}.                        \tag{1.4}
\]

Orientation `B` has the odd profile `s=r+u`, while orientation `A` has
the odd profile `s=r+u+1`.  At the even layer both have profile `s=r+u`.

The even identity is immediate:

\[
                  A^E_{r,u}+B^E_{r,u}=E_{r,u}.              \tag{1.5}
\]

At an odd profile `s=r+u`, Pascal ratios give

\[
 B^O_{r,u}+A^O_{r-1,u}
 =C_{r+u}C_{r-u-1}.                                         \tag{1.6}
\]

Thus (1.3)--(1.4) fill the exact Boolean quotas

\[
 P_{q,s}=C_sC_{s-q}.                                        \tag{1.7}
\]

Whenever `u+1<=r<=b-u-1` they are also pathwise nonincreasing:

\[
 A^E_{r,u}\ge A^O_{r,u}\ge A^E_{r,u+1},
 \qquad
 B^E_{r,u}\ge B^O_{r,u}\ge B^E_{r,u+1}.                   \tag{1.8}
\]

At a boundary the unavailable next term is zero, so the same conclusion
holds with the usual zero convention.  The first inequalities compare the
two denominators.  For the second ones set

\[
 a=r-u-1,qquad c=b-r-u-1.
\]

After clearing positive denominators, the `A` inequality is exactly

\[
\begin{aligned}
 &2a^2u+2a^2+4au^2+8au+4a\\
 &\quad+2c^2u+c^2+4cu^2+4cu+c\ge0,                         \tag{1.9}
\end{aligned}
\]

and the `B` inequality is its `a,c` reflection,

\[
 2a^2u+a^2+4au^2+4au+a
 +2c^2u+2c^2+4cu^2+8cu+4c\ge0.                             \tag{1.10}
\]

Finally Vandermonde and one adjacent binomial ratio give

\[
 \sum_rE_{r,u}=M_{2u},
 \qquad
 \sum_r(A^O_{r,u}+B^O_{r,u})=M_{2u+1}.                     \tag{1.11}
\]

Equations (1.5)--(1.11) are an exact retired two-orientation Boolean flow,
before physical phase capacities are imposed.

## 2. Persistent physical phases in the half-step word

Use the half-step rank map

\[
 R(x)={b-1\over2}x\pmod b,
 \qquad P_r=\{x:R(x)<r\}.                                  \tag{2.1}
\]

Put

\[
                       d_r=|2r-b|.                          \tag{2.2}
\]

The cyclic bit word `1_(P_r)` has one majority-letter run of length
`d_r+1`.  Starting with either endpoint of that run and traversing the
complementary arc gives a maximal alternating linear word of length

\[
                       b-d_r+1.                             \tag{2.3}
\]

Here is the direct word calculation.  Since `R^(-1)(t)=-2t mod b`, for
`r<=(b-1)/2` the equal-bit edges (an edge is indexed by its left endpoint)
are exactly

\[
                    \{1,2,\ldots,b-2r\},
\]

while for `r>=(b+1)/2` they are exactly the cyclic interval

\[
                    \{2(b-r)+1,\ldots,b-1,0\}.
\]

Thus in either case there is one defect-edge interval of length `d_r`,
which proves (2.3).  When `H>=2` and `H-1<=b-d_r`, a string of `H`
consecutive bits is alternating precisely when its `H-1` edges lie in the
complementary linear arc.  Consequently that arc supplies exactly
`b-d_r-H+2` such phase origins.  For `H=1` select instead the
`b-d_r+1` origins along the same maximal linear word; there can be
additional trivial origins, which are not used.  In both cases the selected
starting bits alternate, so each of the two orientations occurs at least

\[
 n_r=\left\lfloor{b-d_r-H+2\over2}\right\rfloor.            \tag{2.4}
\]

We use (2.4) only on the core in (3.2), where its numerator is positive.

Every phase path has scalar capacity `L_r/b`; primality makes this the
integer occurrence-token count used by the labelled affine lift.  Hence
each persistent orientation has the literal physical capacity

\[
                         K_r={n_rL_r\over b}.                \tag{2.5}
\]

Choose exactly `n_r` of the available phase origins in each orientation.
For every selected persistent phase of orientation `A`, give it at layer
`q` the weight `overline A_r(q)/n_r`, where

\[
 \overline A_r(2u)=\min(A^E_{r,u},K_r),
 \quad
 \overline A_r(2u+1)=\min(A^O_{r,u},K_r),                   \tag{2.6}
\]

and define `overline B` analogously.  All unselected phases receive zero.
On the core used below `n_r>0`.  By (1.8), these path weights never revive.
By (2.5), no path exceeds its phase capacity.  At every even or odd
profile, (1.5)--(1.7) and clamping show that the total load is at most
`P_(q,s)`.  Thus (2.6) is a literal feasible point of (0.1).

## 3. Aggregate clamp bound

Assume from now on

\[
 b\ge64,qquad 1\le H\le b/16,                              \tag{3.1}
\]

and use only the central source core

\[
                    d_r\le b/16.                            \tag{3.2}
\]

The omitted squared-binomial source mass is exponentially small.  Indeed,
under

\[
 \Pr(\mathbf R=r)={L_r\over W_b},                            \tag{3.3}
\]

`R` is hypergeometric with mean `b/2`, and Hoeffding gives

\[
 \Pr(d_{\mathbf R}>b/16)\le2e^{-b/512}.                    \tag{3.4}
\]

The asymptotic conclusion does not require this exponential estimate:
the exact second moment in (3.14) and Markov also give the fully elementary
bound

\[
 \Pr(d_{\mathbf R}>b/16)\le {256\over2b-1}.                 \tag{3.4a}
\]

Fix a core source, write `d=d_r` and `Delta=d+H`, and consider either
orientation.  From (2.4),

\[
 K_r\ge {b-d-H+1\over2b}L_r.                                \tag{3.5}
\]

At `u=0` either ideal orientation is at most
`(b+d)L_r/(2b)`.  Since (1.8) is nonincreasing, every clamp excess is at
most

\[
                         {\Delta\over b}L_r.                 \tag{3.6}
\]

It remains to bound how long an excess can persist.  The exact ratio

\[
 {E_{r,u}\over L_r}
 =\prod_{t=0}^{u-1}
 { (b-r-t)(r-t)\over(r+t+1)(b-r+t+1)}                       \tag{3.7}
\]

obeys

\[
                         {E_{r,u}\over L_r}\le e^{-u^2/b}.  \tag{3.8}
\]

Indeed, the contribution at time `t` to the negative logarithm is

\[
 \log\!\left(1+{2t+1\over b-r-t}\right)
 +\log\!\left(1+{2t+1\over r-t}\right).                    \tag{3.8a}
\]

The hypotheses (3.1)--(3.2), and `u<=H/2` on the displayed layers, keep
both added fractions below one.  Each logarithm is therefore at least one
half of `(2t+1)/b`, using `log(1+x)>=x/2`.  Summing (3.8a) over
`0<=t<u` gives `u^2/b` and proves (3.8).

For either orientation fraction `f_r(u)` in (1.3), direct subtraction gives

\[
 |f_r(u)-f_r(0)|={u d\over b(b-2u)}\le {2ud\over b^2}.       \tag{3.9}
\]

Also `f_r(0)>=1/4`.  If `2<=u<=sqrt b`, (3.8)--(3.9) imply

\[
 f_r(0)L_r-f_r(u)E_{r,u}
 \ge {u^2\over16b}L_r.                                     \tag{3.10}
\]

Indeed, `1-e^(-x)>=x/2` for `0<=x<=1`, while
`f_r(0)>=1/4`; hence the left side is at least

\[
 {u^2\over8b}L_r-{2ud\over b^2}L_r
 \ge {u(u-1)\over8b}L_r
 \ge {u^2\over16b}L_r.                                    \tag{3.10a}
\]

The odd mass with the same `u` is no larger than its even mass, by (1.8).

If `u>=sqrt b`, then (3.8) gives
`f_r(u)E_(r,u)<=e^{-1}L_r<K_r`, because `Delta<=b/8` and
(3.5) gives `K_r>=7L_r/16`.  Combining (3.6) and (3.10), a positive clamp
excess is therefore possible for at most

\[
                         6\sqrt{\Delta+1}                   \tag{3.11}
\]

values of `u` per orientation.  There are at most two displayed layers
per `u`.  Hence the total clamp deficit of source `r` is at most

\[
 {24\over b}(d_r+H+1)^{3/2}L_r.                             \tag{3.12}
\]

At every layer, the total unclamped mass of an omitted source is at most
`L_r`, by log-concavity `E_(r,u)<=L_r`.  Therefore the explicit retirement
point satisfies the finite bound

\[
\boxed{
 {\mathfrak D_{\rm ret}\over W_b}
 \le {24\sqrt2\over b}
 \left[
   \left({b^2\over2b-1}\right)^{3/4}+(H+1)^{3/2}
 \right]
 +2H e^{-b/512}.}                                           \tag{3.13}
\]

Indeed

\[
 \mathbb E(2\mathbf R-b)^2={b^2\over2b-1},
 \quad
 \mathbb E|2\mathbf R-b|^{3/2}
 \le\left({b^2\over2b-1}\right)^{3/4},                    \tag{3.14}
\]

and `(x+y)^(3/2)<=sqrt(2)(x^(3/2)+y^(3/2))`.

### Theorem 3.1

For the half-step affine schedule and every

\[
                         H=O(\sqrt{b\log b}),                \tag{3.15}
\]

the phase-preserving scalar retirement LP has

\[
                         \boxed{\mathfrak D_{\rm ret}=o(W_b).} \tag{3.16}
\]

This follows from (3.13), since its two algebraic terms are
`O(b^(-1/4))` and `O(b^(-1/4)log^(3/4)b)`.  Alternatively,
replacing the last term of (3.13) by the elementary tail bound
`256H/(2b-1)` from (3.4a) still gives `o(1)`.

### Corollary 3.2 (exact retired-chain fractional lift)

Let `g=floor(b/4)`.  The point (2.6) lifts to a fractional matching in the
labelled variable-rank retired-chain hypergraph whose total real-target
incidence mass is

\[
 \sum_{q=1}^H M_q-o(W_b),                                   \tag{3.17}
\]

and whose maximum pair load on the core is

\[
 \boxed{\alpha\le {1\over g-H}=O(1/b).}                     \tag{3.18}
\]

Here “mass” in (3.17) means the quota objective: an edge retiring at
`ell` is counted once for each of its `ell` real targets.  It is not the
unweighted sum of retired-edge weights.

To see the lift directly, abbreviate a phase path by `i=(r,p)`, put
`a_i=L_r/b`, set `x_i(H+1)=0`, and define

\[
 y_i(\ell)=x_i(\ell)-x_i(\ell+1)\ge0.                       \tag{3.19}
\]

If `z_i(ell)=s_i(ell)-r`, the number of ordered compatible extensions of
one middle source along that path is

\[
 D_i(\ell)=(b-r)_{z_i(\ell)}
             (r)_{\ell-z_i(\ell)}.                          \tag{3.20}
\]

Give every compatible labelled retired edge of type `(i,ell)` weight

\[
 {y_i(\ell)\over a_iL_rD_i(\ell)}.                          \tag{3.21}
\]

There are exactly `a_i L_r D_i(ell)` such edges, so their total weight is
`y_i(ell)`.  A fixed occurrence token has load
`sum_ell y_i(ell)/a_i=x_i(1)/a_i<=1`; a fixed middle source receives
`x_i(1)/L_r` from phase `p`, and summing over the `b` phases gives load at
most one.  At rank `q`, exactly the cohorts `ell>=q` remain.  The affine
orbit count distributes their mass uniformly over the `P_(q,s)` labelled
targets of that profile, giving target load

\[
 {1\over P_{q,s}}
 \sum_{i:s_i(q)=s}x_i(q)\le1.                               \tag{3.22}
\]

The cohort identity gives
`sum_(i,ell) ell y_i(ell)=sum_(q,i)x_i(q)`; combining this with (3.13)
proves (3.17), while (3.22) proves target feasibility.  The same orbit
counts give token--source and token--target pair loads at most `1/L_r` and
`1/P_(q,s)`, a
source--target load at most the reciprocal of its central extension degree,
and, for targets at ranks `q<q'`, load at most

\[
 \left[
 {b-s\choose s'-s}
 {s-q\choose(q'-q)-(s'-s)}
 \right]^{-1}.                                               \tag{3.23}
\]

On (3.2), the nonexponential extension degrees are at least `g-H`; all
other displayed degrees are exponential in `b`.  This proves (3.18).

## 4. Physical and factor scope

The selected phase origins are literal cyclic windows of the half-step
word, and the profile path at every retained layer is a genuine nested
product-word path.  Restricting further to the core (3.2) stays inside the
central payload band used for internal-band simplicity and extension-count
lower bounds.  Thus the theorem is a genuine joint **fractional scalar**
retirement result on physical affine paths.

It is not an integral growing-rank hypergraph matching theorem.  It also
does not by itself coinstantiate common labelled tight-cycle factors,
orders, origins, or physical atoms.  Those factor/order and integral
rounding gates remain separate.

## 5. H100 audit

The checker
`scratch/audit_halfstep_persistent_alternating_retirement_20260821.py`
verifies the Boolean quota identities and monotonicity by exact rational
arithmetic, enumerates the persistent physical origins literally, builds
the clamped retirement point for finite instances, checks every nesting
and profile-capacity constraint exactly, and checks the finite estimates
(3.5)--(3.12).  Its finite rows audit the proof kernel; the asymptotic
conclusion is the analytic bound (3.13).
