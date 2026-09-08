# Gate A: the activity bridge has negligible puncture oscillation on every clean block

**Date:** 2026-08-22  
**Status:** proved product-law boundary theorem; closes the within-clean-block
puncture regression for the positive external activity bridge

## 0. Result

Let \(b=2r+1\).  For a cyclic word
\(C=(c_0,\ldots,c_{b-1})\), write
\(I_s^C(j)=\{c_j,\ldots,c_{j+s-1}\}\), with indices modulo \(b\), and
define
\[
 \widehat E(C)=
 \{(M,I_r^C(j)):j\in\mathbb Z_b\}\mathbin{\dot\cup}
 \{(L,I_{r-1}^C(j)):j\in\mathbb Z_b\},
\]
\[
 E_h(C)=\widehat E(C)-
 \{(M,I_r^C(h)),(L,I_{r-1}^C(h))\}.
\]
Let \(C,D\) be two full cyclic factors with
\(\widehat E(C)\cap\widehat E(D)=\{v\}\).  A **valid puncture** means one
which does not delete \(v\).  For valid punctures \(h,k\), put
\[
 F_h=E_h(C),\qquad H_k=E_k(D).
\]
Under the product law, lower targets have retention
probability \(x\), middle targets have retention probability \(y\ge x\),
and
\[
 p_t=p_{\operatorname{sh}(t)},\qquad
 w(A)=\prod_{t\in A}p_t^{-1},\qquad q_0=x^{2r}y^{2r}.
\]
All asymptotic assertions are as \(r\to\infty\); in the geometric lemmas
below we take \(r\ge3\).
\[
 B^+(F_h,H_k)=\sum_{G\not\ni v}
 \{w(G\cap F_h)-1\}\{w(G\cap H_k)-1\}.                 \tag{0.1}
\]
Every target-retention probability is at least \(x\).

Uniformly for \(x\ge r^{-\alpha}\) with fixed \(\alpha<3/32\),
\[
 \boxed{
 {1\over D_M}\operatorname {osc}_{h,k}B^+(F_h,H_k)
 =O\!\left({1\over\sqrt r\,x^5}
           +{1\over r^{3/4}x^8}\right)=o(1).}           \tag{0.2}
\]
Here \(D_M=2r\,r!(r+1)!\). In particular, throughout the live Gate-A
range \(\alpha\le1/(256K)\), \(K\ge1\),
\[
 \boxed{q_0\operatorname {osc}_{h,k}B^+(F_h,H_k)=o(z_v),} \tag{0.3}
\]
where \(z_v=D_vq_0/p_v\).

Here and below, \(\operatorname{osc}_{h,k}\) is the maximum minus the
minimum over all valid puncture pairs of this fixed ordered full-factor
pair.

Thus, for any two probability laws \(\mu,\nu\) on the puncture pairs of
one fixed clean full-factor block,
\[
 q_0\left|\mathbb E_\mu B^+-\mathbb E_\nu B^+\right|=o(z_v). \tag{0.4}
\]
Together with the already-proved
\(q_0\operatorname {osc}B^0=O(z_v/r)\), this removes *all*
within-clean-block puncture dependence of the external two-star kernel.
The unresolved dominant-cell problem is now a regression between the
baseline values of different clean full-factor blocks, plus
kernel-weighted control of the previously isolated exceptional mass.

## 1. Inputs

For a target \(t\), write \(D_t\) for its complete-catalogue degree.
The two shore degrees satisfy
\[
 D_M\le D_t\le(1+2/r)D_M.                              \tag{1.1}
\]
For a row \(R\ni t\), put
\[
 \tau_t(R,G)=|(R\cap G)-\{t\}|.
\]
The rooted overlap theorem C.3bis gives, for each fixed \(c\ge1\),
\[
 \mathcal R_c:=
 \max_{t,R\ni t}{1\over D_t}
 \sum_{\substack{G\ni t\\G\ne R}}
       \{x^{-c\tau_t(R,G)}-1\}
 =O_c\!\left({1\over rx^{3c}}+{1\over r^2x^{4c}}\right), \tag{1.2}
\]
provided \(c\alpha<1/2\).

The exact pair inventory C.8 has only two high-codegree skeleton types:
middle--lower containment and disjoint middle--middle pairs. For distinct
targets \(u,t\),
\[
 d(u,t):=|\{G:u,t\in G\}|
 \le
 \begin{cases}
 C D_M/r,&(u,t)\text{ is a skeleton pair},\\
 C D_M/r^2,&\text{otherwise}.
 \end{cases}                                             \tag{1.3}
\]

We also use the following elementary consequence of cyclic intervals.

### Lemma 1.1 (constant many skeleton neighbours)

Let \(\widehat E(D)\) be a full cyclic factor and let
\(u\notin\widehat E(D)\). Among the \(2b\) tagged targets of
\(\widehat E(D)\), at most two form a skeleton pair with \(u\).

More generally, if \(R\) is one puncture of \(\widehat E(D)\) and
\(u\notin R\), then at most three targets of \(R\) form a skeleton pair
with \(u\).

#### Proof

If \(u\) is middle, two distinct length-\((r-1)\) cyclic windows contained
in \(u\) would have union of size at most \(r\). They must be consecutive,
their union is a length-\(r\) cyclic window, and hence \(u\) would belong
to the factor. Thus there is at most one containment neighbour.

Likewise, two distinct length-\(r\) cyclic windows disjoint from \(u\)
would have union inside the \((r+1)\)-set \(\Omega-u\). They must be
consecutive; their union is a cyclic \((r+1)\)-window, whose complement
is the cyclic \(r\)-window \(u\), again a contradiction. Thus there is
at most one disjoint-middle neighbour.

If \(u\) is lower, two distinct cyclic \(r\)-windows containing it have
intersection of size at least \(r-1\). They must be consecutive and their
intersection is the cyclic \((r-1)\)-window \(u\), a contradiction.
There is therefore at most one containment neighbour and no
middle--middle case.

This proves the first assertion.  For the second, only the case
\(u\in\widehat E(D)-R\) is new.  If \(u\) is the deleted lower target,
one of its two containing middle windows is deleted with it, leaving at
most one skeleton neighbour.  If \(u\) is the deleted middle target, one
of its two contained lower windows is deleted with it, while its two
disjoint middle windows remain, leaving at most three. \(\square\)

The restriction \(r\ge3\) in the first assertion is necessary: for
\(r=2\), in the identity factor on \(\mathbb Z_5\), the noncyclic middle
target \((M,\{0,2\})\) has the two containment neighbours
\((L,\{0\}),(L,\{2\})\) and the disjoint-middle neighbour
\((M,\{3,4\})\).  This finite exception has no effect on the asymptotic
theorem.

## 2. An external-root activity estimate

For a catalogue row \(R\) and a target \(u\notin R\), define, for fixed
\(\lambda\ge1\),
\[
 T_\lambda(u,R)
 ={1\over D_M}\sum_{G\ni u}\{w(G\cap R)^\lambda-1\}.     \tag{2.1}
\]

### Lemma 2.1

If \((2\lambda)\alpha<1/2\), then
\[
 \boxed{
 T_\lambda(u,R)
 =O_\lambda\!\left(
 {1\over r x^\lambda}
 +{1\over\sqrt r\,x^{4\lambda}}
 +{1\over r x^{5\lambda}}\right).}                      \tag{2.2}
\]
If additionally \(x^\lambda\sqrt r\to\infty\), the last term is absorbed
by the middle one.

#### Proof

Put \(a_{\lambda,t}=p_t^{-\lambda}-1\le x^{-\lambda}\).
For \(A=G\cap R\), expansion of the product gives
\[
 w(A)^\lambda-1
 \le\sum_{t\in A}a_{\lambda,t}
 \left[1+\{w(A-\{t\})^\lambda-1\}\right].                \tag{2.3}
\]
Indeed, a nonempty activity monomial is counted once if it is a singleton
and \(|S|\ge2\) times if its support is \(S\).

Sum (2.3) over \(G\ni u\). The singleton part is
\[
 \sum_{t\in R}a_{\lambda,t}d(u,t)=O(D_M/(r x^\lambda))  \tag{2.4}
\]
by Lemma 1.1 and (1.3). For the remaining part, Cauchy--Schwarz gives
\[
\begin{aligned}
 &\sum_{G\ni u,t}\{w((G\cap R)-\{t\})^\lambda-1\}\\
 &\qquad\le
 \sqrt{d(u,t)
 \sum_{\substack{G\ni t\\G\ne R}}
       \{w((G\cap R)-\{t\})^\lambda-1\}^2}\\
 &\qquad\le\sqrt{d(u,t)D_t\mathcal R_{2\lambda}}.        \tag{2.5}
\end{aligned}
\]
The last inequality uses
\[
 (a-1)^2\le a^2-1,\qquad
 w((G\cap R)-\{t\})^{2\lambda}
 \le x^{-2\lambda\tau_t(R,G)}.                           \tag{2.6}
\]
There are at most three skeleton \(t\)'s and \(O(r)\) other targets in
\(R\), by the second assertion of Lemma 1.1. Equations (1.1), (1.3), and
(2.5), after division by \(D_M\),
therefore contribute at most
\[
 O_\lambda\!\left(
 x^{-\lambda}\sqrt{\mathcal R_{2\lambda}}\right).        \tag{2.7}
\]
By (1.2),
\[
 \sqrt{\mathcal R_{2\lambda}}
 =O_\lambda\!\left(
 {1\over\sqrt r\,x^{3\lambda}}
 +{1\over r x^{4\lambda}}\right).                        \tag{2.8}
\]
Combining (2.4), (2.7), and (2.8) proves (2.2). \(\square\)

For \(\alpha<3/32\), and hence throughout the live range, Lemma 2.1 gives
the convenient specializations
\[
 T_1(u,R)=O(r^{-1/2}x^{-4}),\qquad
 T_2(u,R)=O(r^{-1/2}x^{-8}).                             \tag{2.9}
\]

## 3. One target toggle

Let \(R,H\) be off-root-disjoint carrier rows through \(v\). Suppose
\(u\in R-\{v\}\) and \(u\) does not belong to the full cyclic factor
underlying \(H\).  Let \(A\) be any intermediate target set satisfying
\(\{v,u\}\subseteq A\subseteq R\), put \(A_0=A-\{u\}\), and write
\[
 h_G(R)=w(G\cap R)-1.
\]
Extend \(B^+\) to such intermediate target sets by the same formula as
in (0.1).  Since every summand below is nonnegative,
\[
\begin{aligned}
 &|B^+(A,H)-B^+(A_0,H)|\\
 &\quad\le (p_u^{-1}-1)
 \sum_{\substack{G\not\ni v\\G\ni u}}
       w(G\cap A_0)h_G(H)\\
 &\quad=(p_u^{-1}-1)
 \left[
 \sum_{\substack{G\not\ni v\\G\ni u}}h_G(H)
 +\sum_{\substack{G\not\ni v\\G\ni u}}h_G(A_0)h_G(H)
 \right].                                               \tag{3.1}
\end{aligned}
\]

The first sum divided by \(D_M\) is at most \(T_1(u,H)\).
For the second, Cauchy--Schwarz gives
\[
 \sum_{\substack{G\not\ni v\\G\ni u}}h_G(A_0)h_G(H)
 \le
 \left(\sum_{\substack{G\not\ni v\\G\ni u}}h_G(A_0)^2
 \right)^{1/2}
 \left(\sum_{G\ni u}h_G(H)^2\right)^{1/2}.               \tag{3.2}
\]
Because \(G\not\ni v\), the first sum omits \(G=R\). Moreover, by
\(A_0\subseteq R-\{u\}\),
\[
 h_G(A_0)^2
 \le x^{-2|(G\cap R)-\{u\}|}-1.
\]
Thus (1.2), rooted at \(u\), bounds that sum by
\(D_u\mathcal R_2\). The second sum is at most
\[
 \sum_{G\ni u}\{w(G\cap H)^2-1\}
 =D_M T_2(u,H).                                         \tag{3.3}
\]
Using (1.1), (2.9), and
\[
 \mathcal R_2=O(r^{-1}x^{-6})                            \tag{3.4}
\]
throughout \(\alpha<3/32\), (3.1)--(3.3) yield
\[
 { |B^+(A,H)-B^+(A_0,H)|\over D_M}
 =O\!\left({1\over\sqrt r\,x^5}
           +{1\over r^{3/4}x^8}\right).                  \tag{3.5}
\]

## 4. Puncture oscillation

Two valid punctures of one full factor differ in at most four targets and
their intersection still contains \(v\).  To pass from \(F_h\) to
\(F_{h'}\), first remove the targets of \(F_h-F_{h'}\), keeping every
intermediate set inside the genuine carrier row \(F_h\); then add the
targets of \(F_{h'}-F_h\), reading each addition backwards as a removal
from an intermediate set inside the genuine carrier row \(F_{h'}\).
Thus every step is covered literally by the generalized toggle estimate
(3.5), even though its intermediate target set need not itself be a
catalogue row.  Cleanliness of the two full factors ensures that every
toggled target \(u\ne v\) is absent from the opposite full factor.

Changing both punctures therefore uses at most eight applications of
(3.5), which proves (0.2). Since
\[
 {q_0D_M\over z_v}
 ={p_vD_M\over D_v}=O(1),                               \tag{4.1}
\]
(0.3) follows.  Indeed the two terms in (0.2) are respectively
\(O(r^{-1/2+5\alpha})\) and \(O(r^{-3/4+8\alpha})\).  Hence
\(\alpha<3/32\) makes both vanish; it also implies \(4\alpha<1/2\),
which validates every use of (1.2), including \(c=4\).
Finally, the difference of expectations under two laws is bounded by the
oscillation, proving (0.4). \(\square\)

## 5. Exact scope

This theorem closes only the puncture coordinate inside a fixed clean
full-factor block. It does not compare different full factors. After
combining it with root-star suppression, nonclean-block mass deletion,
and duplicate-bridge puncture oscillation, the remaining dominant-cell
two-star problem is:

1. prove kernel-weighted uniform integrability on the deleted
   exceptional mass;
2. control the signed shift of the clean-block baselines of \(B^+-B^0\)
   between the factorial and cutoff pair laws;
3. control cutoff mass outside the dominant overlap cell, and then the
   higher \(s=3,\ldots,12\) kernels and stopped transfers.

No favorable sign is asserted.
