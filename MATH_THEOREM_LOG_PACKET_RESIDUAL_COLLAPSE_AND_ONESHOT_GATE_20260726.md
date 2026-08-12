# Logarithmic pair-cube packets: initial mixed-codegree margin, residual collapse, and the one-shot gate

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Statement of the result

Fix a constant \(0<\alpha<1\), and let

\[
 r=\alpha\log _2m+O(1),\qquad R=2^r=m^{\alpha+o(1)},
 \qquad H\longrightarrow\infty,\qquad H\le r/4.       \tag{0.1}
\]

An owner packet is a physical pair cube

\[
 P(F,M)=\{F\cup Z:Z\text{ chooses one endpoint of each of the
 }r\text{ pairs of }M\},qquad |P(F,M)|=R.              \tag{0.2}
\]

Assume that a local cube state has injective signed traces through depth
\(H\).  At every signed depth use the exact mandatory-target plus dump
lift: the slot part consists of the \(N_q=\binom{2m}{m-q}\) physical
targets and \(W-N_q\) labelled dump tokens, where
\(W=\binom{2m}{m}\).  Every column uses all \(R\) owners and exactly
\(R\) resources from every signed slot part.  Thus

\[
 K=(2H+1)R.                                             \tag{0.3}
\]

For the fully coordinate-symmetrized catalogue with uniform quota
marking, all resources have a common degree \(D\).  Its maximum normalized
mixed codegree satisfies

\[
 \boxed{\frac{\Delta _2}{D}\le
        \frac{2r}{m-2r}+\frac RW=O(r/m),}
 \qquad
 \boxed{K\frac{\Delta _2}{D}
        =O\!\left(\frac{RH r}{m}\right)
        =O(m^{\alpha-1}(\log m)^2)=o(1).}              \tag{0.4}
\]

Thus the logarithmic pilot genuinely passes the **initial** growing-rank
pair-codegree test.  This is not, however, a multiround theorem.  If
owners are retained independently with density \(\rho\), then, conditional
on retaining an owner \(X\), the expected number of surviving physical
packets through \(X\) is exactly

\[
 \boxed{D_r\rho^{R-1}},
 \qquad D_r=\binom mr^2r!.                              \tag{0.5}
\]

At the density needed for the coefficient-one packet compiler,

\[
 \rho={1\over H\log H},                                \tag{0.6}
\]

the expression in (0.5) is \(o(1)\).  Consequently all but an
\(o(1)\) fraction of retained owners lie in no surviving packet.  This
remains true although the **global** expected number of surviving packets
is exponentially large:

\[
 \mathbb E|\mathscr P_r[V_\rho]|
 ={WD_r\over R}\rho^R
 =\exp\{(2\log2-o(1))m\}.                              \tag{0.7}
\]

The distinction between (0.5) and (0.7) is essential.  Global edge
abundance is concentrated on a vanishing fraction of residual owners and
does not supply hereditary regeneration.

There is also no density-only repair: deleting only the \(m\) lower
depth-one facets of one retained owner makes that owner have residual
degree zero, while changing the target-part density by only \(m/N_1=o(1)\).

The missing quantitative theorem which would finish this logarithmic
pilot must therefore be one-shot or packet-correlated.  In particular, if for
some absolute \(c>0\) the augmented packet hypergraph always had a
matching with common part leave

\[
 \ell\le C\left(K\frac{\Delta _2}{D}\right)^cW,        \tag{0.8}
\]

then \(H\ell=o(W)\), so the owner leave would be \(o(W/H)\) and the
aggregate signed-target hole count would be \(o(W)\).  No such theorem is
proved here.  Equations (0.5)--(0.7) show that it cannot be obtained by
ordinary product-residual iteration followed by a small terminal
absorber.

## 1. Exact shallow quota sizes

Put

\[
 p_q={N_q\over W}
 =\prod_{i=0}^{q-1}{m-i\over m+i+1}.                   \tag{1.1}
\]

Writing the \(i\)-th factor as

\[
 {m-i\over m+i+1}=1-{2i+1\over m+i+1},                 \tag{1.2}
\]

gives

\[
 0<1-p_q\le\sum_{i=0}^{q-1}{2i+1\over m+i+1}
 \le {q^2\over m}.                                     \tag{1.3}
\]

Uniformly for \(q\le H\), (0.1) and (1.3) imply

\[
 0<R(1-p_q)\le {RH^2\over m}
 =m^{\alpha-1+o(1)}=o(1).                              \tag{1.4}
\]

Therefore the two integral mandatory quota sizes at every signed depth
are exactly

\[
 \lfloor Rp_q\rfloor=R-1,
 \qquad \lceil Rp_q\rceil=R.                           \tag{1.5}
\]

Mix these two sizes in proportions giving mean \(Rp_q\), choose the
accepted trace subset uniformly conditional on its size, and take the
Cartesian product of these choices over the signed depths.  If the size
is \(R-1\), assign the unique rejected occurrence uniformly to a labelled
dump token.  Clearing denominators gives a finite integral catalogue.
The full coordinate orbit and full dump-label orbit make every owner,
physical target, and dump token have the same degree \(D\).

The full lifted columns are exactly \(K\)-uniform with \(K\) as in
(0.3).  Their mandatory projections have sizes in

\[
 R(2H+1)-2H\le K_{\rm mand}\le R(2H+1),                \tag{1.6}
\]

so the two ranks are asymptotically the same.

## 2. Complete mixed-codegree audit

The purpose of this section is to ensure that (0.4) is not inferred only
from owner--owner or owner--target pairs.  All binomial coefficients below
are interpreted as zero outside their natural range.

### 2.1 Owner--owner and owner--target

Two owners at Johnson distance \(d\) have exact relative physical-packet
codegree

\[
 {\lambda_d\over D}
 ={1\over\binom rd}
  \left({(r)_{\underline d}\over(m)_{\underline d}}\right)^2,
 \qquad 1\le d\le r,                                  \tag{2.1}
\]

and zero codegree for \(d>r\).  Its maximum is
\(r/m^2\).

Let \(T\) be a lower depth-\(q\) target and let \(X\) be an owner.  Put
\(j=|T\setminus X|\).  A lower \(q\)-face has \(q\) zero active pairs;
on each of them an owner has two choices, while \(j\) of the other
\(r-q\) active orientations must be flipped.  Full-orbit double counting
therefore gives the exact formula

\[
 \boxed{
 {d(T,X)\over D}
 ={2^q\binom{r-q}{j}\over
   \binom{m-q}{j}\binom{m+q}{q+j}}.}                   \tag{2.2}
\]

Complementation gives the upper formula.  The maximum of (2.2) is the
incident depth-one value

\[
 {2\over m+1}.                                         \tag{2.3}
\]

### 2.2 Same-sign targets at different or equal depths

Fix a lower depth-\(q\) target \(T\) and a lower depth-\(p\) target
\(S\).  Put

\[
 a=|T\setminus S|,
 \qquad b=|S\setminus T|=a+q-p.                        \tag{2.4}
\]

The size of the full physical shell around \(T\) is

\[
 M^-_{q,p}(a)=\binom{m-q}{a}\binom{m+q}{b}.            \tag{2.5}
\]

Inside one pair frame, encode \(T\) by a set of \(q\) zero pairs and an
orientation on the other pairs.  If \(t\) formerly nonzero pairs become
zero in \(S\), direct classification of the pair states gives at most

\[
 f^-_{q,p}(a)
 =\sum_t
 \binom{r-q}{t}
 \binom q{t+q-p}2^{t+q-p}
 \binom{r-q-t}{a-t}                                    \tag{2.6}
\]

same-frame companions in this shell.  Hence

\[
 {d(T,S)\over D}\le {f^-_{q,p}(a)\over M^-_{q,p}(a)}. \tag{2.7}
\]

Uniform quota marking cannot increase (2.7): within one depth its
conditional second acceptance probability is at most its first
acceptance probability, and choices at distinct depths are independent.

Every set difference in (2.4) is supported on the \(2r\) active
coordinates.  Since \(q,p,a,b\le r\), the elementary bounds on the
numerator and denominator in (2.7) give

\[
 {d(T,S)\over D}
 \le\left({2r\over m-2r}\right)^{a+b}.                 \tag{2.8}
\]

The potentially dominant exponent-one cases are exact.  If \(p=q+1\)
and \(S\subset T\), then

\[
 {f^-_{q,q+1}(1)\over M^-_{q,q+1}(1)}
 ={r-q\over m-q};                                      \tag{2.9}
\]

if \(p=q-1\) and \(T\subset S\), then

\[
 {f^-_{q,q-1}(0)\over M^-_{q,q-1}(0)}
 ={2q\over m+q}.                                       \tag{2.10}
\]

All upper--upper bounds follow by complementation.

### 2.3 Opposite-sign targets

Let \(T\) be lower depth \(q\), let \(U\) be upper depth \(p\), and put
\(a=|T\setminus U|\).  Necessarily

\[
 |U\setminus T|=p+q+a,                                 \tag{2.11}
\]

and the physical shell has size

\[
 M^{-+}_{q,p}(a)
 =\binom{m-q}{a}\binom{m+q}{p+q+a}.                   \tag{2.12}
\]

If \(u\) of the zero pairs of \(T\) become double pairs of \(U\), the
same-frame census is at most

\[
 f^{-+}_{q,p}(a)
 =\sum_u
 \binom qu\binom{r-q}{p-u}2^{q-u}
 \binom{r-q-p+u}{a}.                                   \tag{2.13}
\]

Consequently

\[
 {d(T,U)\over D}
 \le {f^{-+}_{q,p}(a)\over M^{-+}_{q,p}(a)}
 \le\left({2r\over m-2r}\right)^{p+q+2a}.             \tag{2.14}
\]

The exponent in (2.14) is at least two.

### 2.4 Dump pairs and the maximum

Under the independent uniform dump labelling fixed in Section 1, a dump
token has relative codegree exactly \(R/W\) with an owner or with a
resource in a different slot part, after averaging over that other part's
quota mixture.  With a target in its own signed slot part its relative
codegree is \((R-1)/N_q=(1+o(1))R/W\), and two different dump tokens in
the same part never coexist in a column.  Thus dump pairs are negligible.

Equations (2.1)--(2.14) show

\[
 {\Delta_2\over D}
 \le {2r\over m-2r}+{R\over W}=O(r/m).                 \tag{2.15}
\]

Multiplication by (0.3) proves (0.4).  In particular, the adjacent-depth
same-sign pairs, not the forced depth-one owner--target pair, set the
largest audited scale.  This changes the bound from \(O(1/m)\) to
\(O(r/m)\), but does not change the favorable conclusion
\(K\Delta_2/D=o(1)\).

## 3. What a single fresh bite can use

Let \(\delta=\Delta_2/D\), and expose an independent residual in which
every resource is retained with probability

\[
 \rho=1-{c\over K},\qquad c>0\text{ fixed}.             \tag{3.1}
\]

For a fixed retained resource \(v\), let \(Z_v\) count the surviving
indexed columns through \(v\).  Parallel indices cause no problem in the
second-moment bound below: two such indices have the same survival
indicator, but their full common resource set is counted in (3.3).  Then

\[
 \mu_v=\mathbb EZ_v=D\rho^{K-1}=(e^{-c}+o(1))D.        \tag{3.2}
\]

Two columns through \(v\) are independent unless they share another
resource.  The number of ordered intersecting column pairs through \(v\)
is at most

\[
 \sum_{u\ne v}d(u,v)^2
 \le \Delta_2\sum_{u\ne v}d(u,v)
 =\Delta_2D(K-1).                                      \tag{3.3}
\]

For a pair sharing \(j\le K-1\) additional resources, its joint survival
probability exceeds the product by a factor at most
\(\rho^{-(K-1)}=e^{c+o(1)}\).  Therefore

\[
 {\operatorname {Var}Z_v\over\mu_v^2}
 \le {1\over\mu_v}+O_c(K\delta)=o(1).                 \tag{3.4}
\]

Thus one fresh \(\Theta(1/K)\)-scale bite has a genuine residual supply;
the favorable parameter in (0.4) is not cosmetic.  Equation (3.4) does
not iterate to small density, because the factor
\(\rho^{-(K-1)}\) then becomes exponential.

## 4. Exact owner-packet death in a deep product residual

There are exactly

\[
 D_r=\binom mr^2r!                                     \tag{4.1}
\]

physical packets through an owner.  Conditional on retaining \(X\), each
one survives precisely when its other \(R-1\) owners survive.  Linearity
of expectation proves (0.5), with no independence assumption between
different packets.

Stirling's formula, uniformly for (0.1), gives

\[
 \log D_r
 =2r\log m-\log(r!)+o(1)
 ={2\alpha\over\log2}(\log m)^2
  -{\alpha\over\log2}(\log m)\log\log m+O(\log m).     \tag{4.2}
\]

Hence a product residual loses the typical owner link whenever

\[
 (R-1)\log(1/\rho)-\log D_r\longrightarrow+\infty.     \tag{4.3}
\]

For \(\rho=1-\theta\) with \(\theta=o(1)\), the transition scale is

\[
 \theta\asymp {\log D_r\over R}
 =\Theta\!\left({(\log m)^2\over m^\alpha}\right).     \tag{4.4}
\]

This is a vanishing amount of total deletion.  At (0.6),

\[
 \log(D_r\rho^{R-1})
 =O((\log m)^2)
  -(1+o(1))R\log(H\log H)\longrightarrow-\infty,       \tag{4.5}
\]

which proves the local link assertion in Section 0 by Markov's inequality.
Local cycle factors, phase choices, and quota markings cannot revive a
physical frame after one of its owner vertices is missing.

On the other hand, the number of physical packets is \(WD_r/R\), so

\[
 \log\left({WD_r\over R}\rho^R\right)
 =\log W+O((\log m)^2)-R\log(H\log H).                 \tag{4.6}
\]

Since \(\log W=(2\log2+o(1))m\) and
\(R\log(H\log H)=m^{\alpha+o(1)}\log\log m=o(m)\),
(4.6) proves (0.7).

## 5. A sharp obstruction to density-only residual hypotheses

Fix an owner \(X\).  Its lower depth-one facet collar is

\[
 \partial X=\{X\setminus\{x\}:x\in X\},
 \qquad |\partial X|=m.                                \tag{5.1}
\]

In any local cube 2-factor, the owner \(X\) is incident with two distinct
cycle edges.  Their two lower intersection colors are distinct members
of \(\partial X\).  By (1.5), a column rejects at most one lower
depth-one trace.  It therefore claims at least one mandatory target in
\(\partial X\).

Retain every resource except the \(m\) targets in \(\partial X\), and
retain \(X\).  No column through \(X\) survives, yet the lower
depth-one target density is

\[
 1-{m\over N_1}=1-o(1).                                \tag{5.2}
\]

Thus no hereditary packet-residual condition stated only in terms of
global part densities can be true.  A valid regeneration theorem must
preserve physical packets and their nested collars, or allow a
quantitatively charged exceptional owner set.  Pair codegrees and
marginal density alone do not imply that property.

## 6. The exact positive boundary

### 6.1 Strict-rainbow unequal-part formulation

The dump lift is equivalent to the following statement involving only
physical targets.  Let a strict-rainbow packet matching contain \(t\)
columns, and put

\[
 \ell=W-Rt.                                             \tag{6.1a}
\]

At a fixed signed depth \(q\), let \(s_q\) of the selected columns use
the quota \(R-1\), and let the other \(t-s_q\) use the quota \(R\).
Target injectivity then gives exactly

\[
 A_q=Rt-s_q=W-\ell-s_q                                \tag{6.1b}
\]

covered physical targets and hence

\[
 \boxed{h_q=N_q-A_q=\ell-(W-N_q)+s_q.}                \tag{6.1c}
\]

Conversely, a strict-rainbow family satisfying (6.1a)--(6.1c) lifts to
the equal-part hypergraph precisely when

\[
 0\le s_q\le W-N_q;                                    \tag{6.1d}
\]

the \(s_q\) rejected occurrences are then assigned injectively to dump
tokens.  Nonnegative target leave also requires
\(s_q\ge W-N_q-\ell\).  Thus the exact unequal-part target is:

\[
 \ell=o(W/H),\qquad
 0\le s_q\le\min\{t,W-N_q\},\qquad
 h_q=\ell-(W-N_q)+s_q\ge0                              \tag{6.1e}
\]

at every signed depth, with all claimed targets distinct.  It then has

\[
 \sum_{q,\pm}h_q\le2H\ell=o(W).                        \tag{6.1f}
\]

For the logarithmic regime there is no numerical obstruction in
(6.1e):

\[
 {W-N_q\over t}=O\!\left({Rq^2\over m}\right)=o(1),   \tag{6.1g}
\]

so one may take
\(s_q=\max\{0,W-N_q-\ell\}\), which is at most \(t\).
The obstruction is solely the simultaneous integral selection of the
physical packets and their literal targets.

### 6.2 Minimal correlated-reservoir alternative

A multiround proof need not establish hereditary regularity for every
residual.  The weakest useful version is an **admissible residual chain**:
there must exist successive packet matchings whose induced residuals,
down to density \(1/(H\log H)\), have a common degree scale off exceptional
sets of total size \(o(W/H)\) per part, internal star-overlap \(o(1)\),
and one further isolated bite preserving the same assertions.  The
growing-rank isolated-bite calculation then iterates for
\(O(K\log(H\log H))\) rounds and gives (6.1e).

This correlated-reservoir lemma is strictly weaker than a hereditary
statement for every residual, but it still has to control whole owner
packets and the nested target collars.  Sections 4--5 prove that neither
independent product thinning nor part-density information can establish
it.  No construction of such an admissible chain or of an equivalent
structured absorber is presently proved.

Let

\[
 \Gamma_m=K\Delta_2/D.
\]

By (0.4),

\[
 \Gamma_m=O(m^{\alpha-1}(\log m)^2).                  \tag{6.1}
\]

Suppose a one-shot coloring, correlated nibble, or absorber theorem gives
a matching in the full mandatory-plus-dump lift with common part leave

\[
 \ell\le C\Gamma_m^cW                                 \tag{6.2}
\]

for some fixed constants \(C,c>0\), uniformly in this packet family.
Then

\[
 {H\ell\over W}
 \le CH\,O\!\left(m^{-c(1-\alpha)}
                  (\log m)^{2c}\right)=o(1).           \tag{6.3}
\]

A packet matching leaves exactly \(\ell\) total resources in every slot
part.  Hence it leaves at most \(\ell\) physical targets at each signed
depth and at most \(2H\ell=o(W)\) over all signed depths.  Its owner leave
is \(\ell=o(W/H)\).  This proves the conditional implication (0.8).

The exact weakest leave requirement is, of course,
\(H\ell/W\to0\).  Hypothesis (6.2) is a convenient robust form exposed by
this pilot: any fixed power saving in the initial parameter \(\Gamma_m\)
is enough.  It is not a consequence of the results above.  The product
residual route cannot prove it, because (4.5) leaves almost every residual
owner outside every packet.  A terminal absorber of \(o(W)\) resources
cannot repair a residual containing \((1-o(1))W\) owners.  A successful
proof must therefore be one-shot, preserve a packet-correlated residual
from the outset, or build the absorber throughout the main selection.

## 7. Audited conclusion

The following statements are unconditional.

1. The exact shallow quotas are \(R-1\) and \(R\), and the full dump lift
   has rank \((2H+1)R\).
2. The owner, owner--target, same-sign target, opposite-sign target, and
   dump codegrees are all covered by Section 2.  Their maximum is
   \(O(r/m)\), so the initial parameter \(K\Delta_2/D\) tends to zero.
3. A single fresh bite has concentrated residual links at its natural
   \(1/K\) scale.
4. Deep independent residuals contain exponentially many packets globally
   but no packet through a typical retained owner.
5. Global residual densities, even densities \(1-o(1)\), do not imply
   minimum packet degree because of the exact facet-collar cut.
6. Any one-shot matching theorem with the polynomial leave (6.2) would
   prove the \(c\log m\) simultaneous-band packet pilot.

What remains unproved is precisely (6.2), or a packet-correlated
regeneration/absorption theorem strong enough to imply it.  Thus the
logarithmic regime is a valid positive pilot for a new one-shot theorem,
but it is not licensed by an ordinary fixed-uniformity nibble.
