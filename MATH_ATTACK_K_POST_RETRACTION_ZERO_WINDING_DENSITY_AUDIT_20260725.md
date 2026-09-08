# Adversarial audit of the post-retraction zero-winding density theorem

Date: 2026-07-25

Audited source:
`MATH_ATTACK_K_POST_RETRACTION_ZERO_WINDING_DENSITY_20260725.md`.

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict

After the corrections recorded in Section 6 below, the principal theorem

\[
 |\mathcal Z_r(A)|=o_A(\operatorname{Cat}_r)
 \tag{0.1}
\]

is valid. The bivariate pruning equation, both factorial-moment
normalizations, the slow diagonal, the harmonic fan envelope, and the
conditional summation over pruning profiles and bottom roots all check.

The proof is genuinely qualitative. Its diagonal can tend to infinity
arbitrarily slowly, so (0.1) supplies no rate comparable to
\(1/H\) when \(H\asymp\sqrt r\). It therefore does not prove the quotient
packing estimate \(o(B_r/H)\), does not treat positive-winding returns,
and does not prove \((RP_A)\) or coefficient one.

The source required four repairs, none of which changes (0.1):

1. pruning ranks had to be normalized as Dyck **semilengths**, namely
   \(r_j=|D^{(j)}|/2\), rather than literal word lengths;
2. the height equality and uniqueness of a zero-winding duration had to
   be stated before the global fibre sum;
3. good-profile tower capacities sum to **at most** \(B_r\); equality
   holds only after all profiles are restored;
4. the quotient-packing implication had to display the deck comparison
   and the short-period exceptional term.

## 1. Audit of the bivariate pruning generating function

Let \(X_j(T)\) be the number of plane-tree edges left after \(j\)
simultaneous leaf deletions, and let

\[
 F_j(z,u)=\sum_T z^{|T|}u^{X_j(T)}.
\]

For one root child \(U\), the joining edge survives \(j\) rounds exactly
when \(\operatorname{ht}(U)\ge j\). If it survives, its contribution is
one in addition to the \(X_j(U)\) surviving internal edges. If
\(\operatorname{ht}(U)<j\), then \(X_j(U)=0\). Since the generating
function for the latter class is \(A_j=C_{j-1}\), the one-child series is

\[
 z\{uF_j-(u-1)A_j\}.
\]

An ordered sequence of such children therefore gives exactly

\[
 F_j={1\over1-z\{uF_j-(u-1)A_j\}},
\]

or equivalently

\[
 zuF_j^2-\{1+z(u-1)A_j\}F_j+1=0.
 \tag{1.1}
\]

There is no independence assumption here. The height cutoff and the
ordered-sequence construction are exact.

Put \(C=F_j(z,1)\), \(M=\partial_uF_j(z,1)\), and
\(V=\partial_u^2F_j(z,1)\). Differentiating (1.1) once gives

\[
 zC(C-A_j)+(2zC-1)M=0.
\]

Using \(zC^2=C-1\) and \(1-2zC=(2-C)/C\) yields

\[
 \boxed{M={(C-1)(C-A_j)\over2-C}.}
 \tag{1.2}
\]

A second differentiation gives

\[
 2z\{M^2+(2C-A_j)M\}+(2zC-1)V=0,
\]

hence

\[
 \boxed{V={2zC\over2-C}\{M^2+(2C-A_j)M\}.}
 \tag{1.3}
\]

Thus both displayed identities in the source have the correct signs and
normalizations.

For \(t=\sqrt{1-4z}\),

\[
 C={2\over1+t},
 \qquad A_j(1/4)=C_{j-1}(1/4)={2j\over j+1}.
\]

The finite-height series \(A_j\) is analytic across \(z=1/4\) for fixed
\(j\). Substitution in (1.2)--(1.3) gives

\[
 M={1\over(j+1)t}+O_j(1),
 \qquad
 V={1\over2(j+1)^2t^3}+O_j(t^{-2}).
 \tag{1.4}
\]

Since

\[
 [z^r]t^{-1}\sim{4^r\over\sqrt{\pi r}},
 \qquad
 [z^r]t^{-3}\sim{2\,4^r\sqrt r\over\sqrt\pi},
 \qquad
 B_r\sim{4^r\over\sqrt\pi r^{3/2}},
\]

coefficient division by \(B_r\) gives

\[
 \mathbb E X_j={r\over j+1}+O_j(\sqrt r)
 \tag{1.5}
\]

and, remembering that \(V\) marks \(X_j(X_j-1)\),

\[
 \mathbb E[X_j(X_j-1)]
 ={r^2\over(j+1)^2}+O_j(r^{3/2}).
 \tag{1.6}
\]

Equations (1.5)--(1.6) imply

\[
 \operatorname{Var}(X_j)=O_j(r^{3/2}).
\]

This is more than enough for \(X_j/r\to1/(j+1)\) in probability at each
fixed depth. No factor of two is missing once \(X_j\) and \(r_j\) are both
interpreted as edge counts, equivalently Dyck semilengths.

## 2. Audit of the diagonal quantifiers

Fix an integer \(K\). Apply fixed-depth convergence with the fixed
tolerance \(K^{-4}\) at each depth \(1,\ldots,K+1\). A finite union bound
permits a threshold \(R_K^{(1)}\) after which the exceptional proportion is
at most \(K^{-2}\).

For the height exception, a Dyck path of height below \(2K\) is an
excursion in the path graph on heights \(0,\ldots,2K-1\). Write
\(\mathsf A_K\) for its adjacency matrix; its spectral radius is

\[
 \rho_K=2\cos{\pi\over2K+1}<2.
\]

Consequently

\[
 \#\{D:\operatorname{ht}(D)<2K\}
 \le (\mathsf A_K^{2r})_{0,0}\le\rho_K^{2r},
\]

which is \(o_K(B_r)\). This gives a second threshold
\(R_K^{(2)}\) for an exceptional proportion at most \(K^{-2}\).

Choose increasing thresholds

\[
 R_K\ge\max(R_K^{(1)},R_K^{(2)},K^{12})
\]

and define \(K(r)=K\) on \([R_K,R_{K+1})\). Then

\[
 K(r)\to\infty,
 \qquad K(r)\le r^{1/12}.
\]

This is a legitimate diagonal: every concentration statement is invoked
only with fixed \(K\) before its threshold is chosen. No estimate uniform
in a growing depth is assumed.

For a genuine zero-winding return, the audited height equality gives
\(h=\operatorname{ht}(D)\). Thus a tall root has \(h\ge2K\). If its first
path-core level \(\ell\) were below \(K\), then

\[
 r_\ell=h-\ell\le A\sqrt r,
\]

whereas goodness gives

\[
 r_\ell\ge(1-K^{-4}){r\over\ell+1}
 \ge {r\over2K}
 \ge {1\over2}r^{11/12}>A\sqrt r
\]

for all sufficiently large \(r\). This contradiction proves
\(K\le\ell\), while tallness proves \(K\le h/2\). The early-core deletion
is therefore exact rather than heuristic.

## 3. Audit of the harmonic fan-capacity factor

At inverse level \(j\), let

\[
 y_j=r_{j-1}-2r_j+r_{j+1}\ge0
\]

be the free-leaf mass. It is distributed among \(2r_j+1\) ordered slots,
so the unrestricted conditional fibre has size

\[
 \binom{y_j+2r_j}{2r_j}
 =\binom{r_{j-1}+r_{j+1}}{2r_j}.
 \tag{3.1}
\]

The audited Pascal fan prescribes \(j\) distinct slot variables. If their
prescribed values have total \(w\ge0\), the number of remaining weak
compositions is

\[
 \binom{y_j-w+2r_j-j}{2r_j-j}
 \le
 \binom{y_j+2r_j-j}{2r_j-j}.
 \tag{3.2}
\]

Dividing (3.2) by (3.1) gives

\[
 \prod_{i=0}^{j-1}
 {2r_j-i\over r_{j-1}+r_{j+1}-i}.
 \tag{3.3}
\]

The discrete convexity
\(r_{j-1}+r_{j+1}\ge2r_j\) has the correct direction. For
\(0\le i<j\), cross multiplication gives

\[
 {2r_j-i\over r_{j-1}+r_{j+1}-i}
 \le {2r_j\over r_{j-1}+r_{j+1}}.
\]

On a profile

\[
 r_j={r\over j+1}(1+\theta_j),
 \qquad |\theta_j|\le K^{-4},
\]

put \(q_j=2r_j/(r_{j-1}+r_{j+1})\). Relative to

\[
 q_j^*={j(j+2)\over(j+1)^2},
\]

the numerator changes by at most \(1+K^{-4}\), while the positive
weighted denominator changes by at least \(1-K^{-4}\). Hence

\[
 q_j\le q_j^*e^{3K^{-4}}.
\]

It follows that

\[
 \begin{aligned}
 Q_K
 &\le \exp\!\left(3K^{-4}\sum_{j=1}^Kj\right)
       \prod_{j=1}^K(q_j^*)^j\\
 &=e^{O(K^{-2})}{(K+2)^K\over(K+1)^{K+1}}
 \le {2e\over K+1}
 \end{aligned}
 \tag{3.4}
\]

for all large \(K\). The telescoping constant and the power \(j\) are
both correct. The expression in (3.4) is the harmonic **envelope**; the
finite-slot product (3.3) can only be smaller.

## 4. Audit of the global profile/bottom-root summation

This is the point at which a one-profile estimate could have failed to
become a global density theorem. It does not fail, for the following
reasons.

Fix a rank string

\[
 \mathbf r=(r_0,r_1,\ldots,r_{K+1})
\]

and a rooted level-\(K\) Dyck word \(E=D^{(K)}\) satisfying
\(|E|/2=r_K\) and \(|\partial E|/2=r_{K+1}\). At every inverse step, the
number in (3.1) depends only on the adjacent rank triple, not on the shape
of the current core. Therefore the unrestricted number of towers above
\((\mathbf r,E)\) is the product of the conditional fibre sizes.

The multislot bound is also conditional. Once the current rooted core is
fixed, its time-zero fan phase determines the consecutive slot labels and
their prescribed values. Equation (3.2) bounds all allowed preimages of
that core by the same rank-dependent ratio. Iterating this conditional
bound from the bottom upward proves the product estimate without assuming
independence between levels.

There are two potential union factors, but both are absent.

1. A genuine zero-winding hit has duration
   \(h=\operatorname{ht}(D)\). Simultaneous pruning lowers nonzero height
   by exactly one at each level, so for fixed \(E\),
   \(h=\operatorname{ht}(E)+K\). Moreover the strict first-passage variable
   is strictly decreasing, so a root has at most one zero-winding hit.
   There is no sum over \(h\).

2. A bottom object is a rooted Dyck word, not an unrooted cyclic tree.
   The fan begins at its time-zero phase. There is no extra factor
   \(2r_K+1\) for choosing a fan origin.

Finally, every outer Dyck root has exactly one pruning rank string and one
rooted bottom word. Hence the unrestricted tower fibres are disjoint and
partition \(\mathcal D_r\). Summed over every profile and bottom word,
their capacities equal \(B_r\); summed only over good profiles, they are
at most \(B_r\). Therefore

\[
 |\mathcal Z_r(A)|
 \le {2B_r\over K(r)^2}
      +{2eB_r\over K(r)+1}
 =o(B_r).
 \tag{4.1}
\]

No multiplicity in profiles, bottom roots, durations, or phases has been
lost in (4.1).

## 5. Audit of the implication scope

The linear dominance seam has the form

\[
 L_H\le W+2HB_r+2(5H-1)\nu_H(P_r),
 \qquad W=NB_r.
 \tag{5.1}
\]

The deck comparison is

\[
 N\overline\nu_H\le\nu_H(P_r)
 \le2N\overline\nu_H+NZ_H,
 \tag{5.2}
\]

with \(HZ_H=o(B_r)\) in a fixed Gaussian window. Since
\(H=o(N)\), the first error in (5.1) is already \(o(W)\). Requiring

\[
 \overline\nu_H=o(B_r/H)
 \tag{5.3}
\]

makes the main deck term in (5.2) contribute \(o(W)\), and the stated
bound on \(Z_H\) makes its exceptional contribution \(o(W)\). Thus (5.3)
is a valid sufficient gate for this ledger. The stronger condition
\(\overline\nu_H=O(B_r/N)\) also implies (5.3) because \(H/N\to0\).

The density theorem (0.1) does not imply (5.3). Its proof only gives
\(O(B_r/K(r))\), where the diagonal \(K(r)\to\infty\) has no prescribed
rate and can be much smaller than \(H\). Also, a set of
\(o(B_r)\) starts can still contain order \(B_r/H\) mutually
edge-disjoint length-\(H\) intervals. A separate trace-correlation or
clustering theorem is needed before a fan fraction may be multiplied by
an interval-length fraction.

The exact proved boundary is therefore

\[
 \boxed{
 \text{genuine zero-winding starts of Gaussian gap have }o(B_r)
 \text{ quotient density}.}
\]

It does not include positive winding, the packed scale
\(o(B_r/H)\), \((RP_A)\), a global literal braid, coefficient one, MWB,
or labelled synchronization.

## 6. Patches applied to the source

The following corrections were made directly in the audited source.

1. Both occurrences of the pruning rank were normalized as
   \(\tfrac12|\partial^jD|\), matching the plane-tree edge count \(X_j\).

2. The zero-winding height equality and uniqueness of the hit were stated
   at the definition of \(\mathcal Z_r(A)\), and used explicitly in the
   tall-root argument.

3. The missing \(\lfloor\cdot\rfloor\) command in the fan-depth bound was
   repaired.

4. The harmonic formula was identified as the right-hand envelope rather
   than the exact finite-slot product.

5. The global sum was corrected from equality over good profiles to an
   upper bound over good profiles, with equality only over all profiles.
   The absence of duration and phase union factors was made explicit.

6. The deck inequality and the short-period exception \(Z_H\) were added
   to the implication section, and “weakest” was narrowed to the weakest
   sufficient gate obtained by forcing every displayed nonnegative error
   term to be little-oh.

No change to the theorem statement or its constant \(2e/(K+1)\) was
needed.
