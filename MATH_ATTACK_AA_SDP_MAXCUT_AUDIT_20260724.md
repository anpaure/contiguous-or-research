# Adversarial audit of the SDP/Max-Cut lane

## 1. Verdict

The central algebra of MATH_ATTACK_AA_SDP_MAXCUT_REPORT_RAW_20260724.md
survives audit. In particular:

* the factors \(2\) and \(4\) in the orbit, parity, and Max-Cut formulas are
  correct;
* the ideal Johnson gain formula and its integer \(1\)-Lipschitz kernel are
  exact;
* the matching constants \(1/2\) and the Rademacher-chaos constants
  \(1/36,1/18\) are correct, with unordered-pair normalization;
* the forest simultaneous-minimization theorem is valid;
* the high-energy \(1\)-Lipschitz load construction, including its margins,
  regular bonus family, energies, and constants \(1/64,1/128\), is valid;
* equations (16)--(22) for the genuine MSW local components are valid after
  adding their rank range and weighted-norm conventions.

There are, however, several material qualifications.

1. The actual three-floor decomposition contains the intermediate rowwise
   floor \(B_\tau=\sum_p\alpha_pb_p\). The loss
   \(\beta_\tau-\Pi_\tau\) combines local amplitude locking and global
   cycle frustration; it should not be described as one undifferentiated
   holonomy loss.
2. The kernel in (4) is a set of integer \(1\)-Lipschitz loads, not a cone.
3. Every \(W_+,W_-\), matching, and Frobenius sum must be over unordered
   pairs \(K<L\). Matrix-Frobenius normalization introduces an additional
   factor \(\sqrt2\).
4. The Section 4 conclusion is initially rankwise:
   \(A_{\tau,1}=\Pi_{\tau,1}\), not the unqualified aggregate
   \(A_\tau=\Pi_\tau\). Aggregate equality follows only after the other
   ranks are also prescribed to be \(1\)-Lipschitz.
5. The resulting signed exact-middle vector is stationary for the
   histogram-level ideal transposition functional. It is not a local
   minimum of the unrestricted signed selector lattice.
6. The three-vector SDP example obstructs the basic elliptope/vector
   residual relaxation with parity floors. It does not obstruct all SDPs:
   its proposed SDP point violates a triangle inequality, so the
   three-variable metric/cut relaxation already removes it.
7. The large positive Gram coherence in (20)--(22) is favorable, not
   harmful, in the exact Bernoulli cut formula unless the larger components
   have comparably adverse alignment. It disproves a bounded-overlap
   argument, not Bernoulli thinning itself.
8. The final implication requires a joint same-transposition theorem,
   uniform over every exact factor visited by descent. A bound on
   \(\max_\tau G_\tau\) and a low bundling loss for a different transposition
   do not combine.

With these corrections, the report remains a useful exact reduction but
does not prove \(LM_A\), MWB, or labelled synchronization.

## 2. Three exact floors and the Johnson formula

For one moved orbit \(p=\{S,\tau S\}\), put

\[
 z_{pK}=a_K(S)-a_K(\tau S),\qquad
 D_p=\sum_Kz_{pK},\qquad \alpha_p=\frac2{c_q}.
\]

The component vector \(d_K=a_K-\tau a_K\) has the two coordinates
\((z_{pK},-z_{pK})\) on \(p\). Therefore

\[
 \|d\|_H^2=\sum_p\alpha_pD_p^2=A_\tau.
\]

For a sign vector \(\varepsilon\), if \(I\) is one sign class, then

\[
 \left\|\sum_K\varepsilon_Kd_K\right\|_H^2
 =\|d_I-d_{I^c}\|_H^2.
\]

Since

\[
 \|d_I+d_{I^c}\|_H^2-\|d_I-d_{I^c}\|_H^2
 =4\langle d_I,d_{I^c}\rangle_H,
\]

one obtains exactly

\[
 \boxed{C_\tau^*=\frac{A_\tau-\beta_\tau}{4}.}
\]

Let

\[
 \ell_p=\mu(S)+\mu(\tau S),\qquad \pi_p=\ell_p\bmod2.
\]

Because \(\varepsilon_K\equiv1\pmod2\),

\[
 \sum_K\varepsilon_Kz_{pK}\equiv\sum_Kz_{pK}\equiv\ell_p\pmod2.
\]

Hence every signed row residual has square at least \(\pi_p\), and

\[
 \Pi_\tau=\sum_p\alpha_p\pi_p\le\beta_\tau.
\]

The report's equations (1)--(2) are therefore correct. The sharper literal
three-floor version is obtained by defining

\[
 b_p=\min_{\eta_K=\pm1}\left(\sum_K\eta_Kz_{pK}\right)^2,\qquad
 B_\tau=\sum_p\alpha_pb_p.
\]

Then

\[
 \boxed{\Pi_\tau\le B_\tau\le\beta_\tau\le A_\tau}
\]

and

\[
 \boxed{
 C_\tau^*
 =\frac{A_\tau-\Pi_\tau}{4}
 -\frac{B_\tau-\Pi_\tau}{4}
 -\frac{\beta_\tau-B_\tau}{4}.}
\]

The second term is local amplitude locking. The third is the exact global
compatibility/holonomy loss. Thus \((\beta_\tau-\Pi_\tau)/4\) is a valid
combined ownership-bundling loss, but it is not purely global frustration.

For an integer \(D\),

\[
 \frac{D^2-(D\bmod2)}4=\left\lfloor\frac{D^2}{4}\right\rfloor.
\]

Consequently the ideal row gain at depth \(q\) is

\[
 \frac2{c_q}\left\lfloor
       \frac{(\mu_q(S)-\mu_q(\tau S))^2}{4}\right\rfloor.
\]

Every Johnson edge \(ST\) is the moved orbit of the unique transposition
exchanging the two coordinates in \(S\triangle T\). Summing over
transpositions gives exactly

\[
 \boxed{
 \mathbb E_\tau G_{\tau,q}
 =\frac{2}{\binom n2c_q}
   \sum_{\{S,T\}\in E(J(n,r))}
   \left\lfloor\frac{(\mu_q(S)-\mu_q(T))^2}{4}\right\rfloor.}
\]

This vanishes precisely when every Johnson-edge difference has absolute
value at most one. The word "cone" in the report is incorrect: integer
\(1\)-Lipschitz functions are not closed under positive scaling or addition.

## 3. Matching and Rademacher/Frobenius Max-Cut bounds

All sums in this section must be interpreted as \(\sum_{K<L}\). Put

\[
 w_{KL}=\langle d_K,d_L\rangle_H,\quad
 W_+=\sum_{K<L}(w_{KL})_+,\quad
 W_-=\sum_{K<L}(-w_{KL})_+,\quad s=W_+-W_-.
\]

Then \(A_\tau=V_\tau+2s\). For signs \(\varepsilon_K\), put

\[
 Z(\varepsilon)=\sum_{K<L}w_{KL}\varepsilon_K\varepsilon_L.
\]

The corresponding cut has value

\[
 C(\varepsilon)=\frac{s-Z(\varepsilon)}2.
\]

If

\[
 \operatorname{fr}(\varepsilon)
 =\sum_{\substack{w_{KL}>0\\K,L\text{ uncut}}}w_{KL}
 +\sum_{\substack{w_{KL}<0\\K,L\text{ cut}}}|w_{KL}|,
\]

then \(C(\varepsilon)=W_+-\operatorname{fr}(\varepsilon)\), proving (5).

Let \(\mathfrak M_\tau\) be a maximum \(|w|\)-weight matching. Force every
matched positive edge to cross and every matched negative edge not to
cross. Choose one random seed sign per matched pair and independent signs
on unmatched vertices. Every nonmatched edge has mean sign product zero,
while every matched edge improves the random-cut baseline by
\(|w_{KL}|/2\). Thus

\[
 \boxed{
 C_\tau^*\ge\frac{W_+-W_-}{2}+\frac{\mathfrak M_\tau}{2}
 =\frac{A_\tau-V_\tau}{4}+\frac{\mathfrak M_\tau}{2}.}
\]

The factor \(1/2\) is correct.

For the chaos bound,

\[
 \|Z\|_2=\left(\sum_{K<L}w_{KL}^2\right)^{1/2}.
\]

Degree-two Bonami gives \(\|Z\|_4\le3\|Z\|_2\). Interpolation gives

\[
 \|Z\|_2\le\|Z\|_1^{1/3}\|Z\|_4^{2/3},\qquad
 \mathbb E|Z|\ge\frac{\|Z\|_2}{9}.
\]

As \(\mathbb EZ=0\), some signing has

\[
 Z\le-\frac{\|Z\|_2}{18}.
\]

Therefore

\[
 \boxed{
 C_\tau^*\ge\frac{A_\tau-V_\tau}{4}
 +\frac1{36}\left(\sum_{K<L}w_{KL}^2\right)^{1/2}.}
\]

The constants \(1/36\) and \(1/18\) in (7)--(8) are correct. If one calls
the last quantity a matrix Frobenius norm, however,

\[
 \|G_{\rm off}\|_F
 =\left(\sum_{K\ne L}w_{KL}^2\right)^{1/2}
 =\sqrt2\left(\sum_{K<L}w_{KL}^2\right)^{1/2}.
\]

Thus the matrix-Frobenius constants are \(1/(36\sqrt2)\) and
\(1/(18\sqrt2)\).

At a transposition-cut local minimum, \(C_\tau^*=0\), since the empty cut
has value zero. Equations (6)--(7) then imply exactly

\[
 W_--W_+\ge\mathfrak M_\tau,\qquad
 W_--W_+\ge\frac1{18}\left(\sum_{K<L}w_{KL}^2\right)^{1/2}.
\]

Here "cut-local" must mean no profitable union of components, not merely no
profitable one-component flip. Density is not used in the chaos proof, so
"dense-graph bound" is only descriptive. The unconditional statement is
most cleanly written as the maximum of zero and the right sides of
(6)--(7).

## 4. Forest and feedback-row theorem

The forest theorem is correct. Root each nontrivial incidence-tree at a
component variable. When a row is reached through its parent variable,
take a locally minimizing sign pattern on its neighbors. If its parent
sign disagrees with the already assigned sign, negate the whole pattern;
the squared row residual is unchanged. All other neighbors are new
variables because the incidence graph is acyclic. Induction gives one
common signing attaining every \(b_p\), and hence

\[
 \beta_\tau=\sum_p\alpha_pb_p.
\]

If deleting rows \(\mathcal R\) leaves a forest, use its simultaneous
minimizer. On a deleted row,

\[
 \left|\sum_K\varepsilon_Kz_{pK}\right|\le L_p,\qquad
 L_p=\sum_K|z_{pK}|.
\]

This proves (10), including its factor \(1/4\). A more transparent form is

\[
 C_\tau^*\ge G_\tau-\frac14\left[
 \sum_p\alpha_p(b_p-\pi_p)
 +\sum_{p\in\mathcal R}\alpha_p(L_p^2-b_p)\right].
\]

The first sum is the exact local-amplitude loss. The second is a coarse
certificate for global cycle frustration. The feedback-row expression is
not itself the exact holonomy loss and still contains amplitude if written
as \(L_p^2-\pi_p\).

The examples in the report are valid. A row with coefficients
\((2,2,-2)\) has \(b_p=4>\pi_p=0\), even though its incidence graph is a
tree. Three inconsistent two-variable unit constraints on a bipartite
six-cycle have \(b_p=\pi_p=0\) rowwise but force one positive global
residual.

## 5. Audit of the high-energy \(1\)-Lipschitz obstruction

Put \(r=m-1\), \(N=\binom nr\), and \(B=C_m=W/n\). Then

\[
 W=\frac{m+2}{m}N,\qquad
 R=W-N=\frac{2N}{m}=\frac{2nC_m}{m+2},
\]

and

\[
 d=\frac{rR}{n}=\frac{2(m-1)C_m}{m+2}.
\]

The integer \(d\) is integral. One direct proof is

\[
 R-d=R\frac{n-r}{n}
 =R\frac{m+2}{2m+1}
 =\frac{2W}{2m+1}=2C_m.
\]

For the function \(x\) in (11), the two positive and two negative local
patterns have equal cardinality

\[
 T=\binom{n-8}{r-4}.
\]

Every outside point occurs equally often in all four strata. Each point of
\(U\) occurs in one positive and one negative pattern. Therefore \(x\) has
zero total and zero point margins. A positive pattern and a negative
pattern differ in at least two Johnson exchanges, so no Johnson edge joins
opposite signs. Hence \(x\) is \(1\)-Lipschitz.

The two ambient strata for \(\mathcal E_0,\mathcal E_8\) have sizes

\[
 \binom{n-8}{r},\qquad \binom{n-8}{r-8}.
\]

For \(m\ge18\), each is at least \(3^{-8}N\), while
\(R/N=2/m\le3^{-8}\) for \(m\ge13122\). Thus families of sizes
\(R-d\) and \(d\) fit.

To obtain exact combined degree \(d\), start with any two simple families
of the required sizes and minimize the sum of squared combined degrees on
\(V\). If vertices \(u,v\) have combined degree gap at least two, one of
the two color families has \(\deg(u)>\deg(v)\). In a simple uniform family
with this degree inequality, some set containing \(u\) and not \(v\) can be
swapped from \(u\) to \(v\) without duplicating an existing set; otherwise
the swaps would inject all \(u\)-only incidences into the fewer
\(v\)-only incidences. The swap decreases the squared-degree sum. Thus all
combined degrees differ by at most one. Their average is the integer \(d\),
so all equal \(d\).

The family \(\mathcal H\) consequently has size \(R\) and degree \(d\) at
every coordinate, including every point of \(U\). Therefore

\[
 \mu=1+x+\mathbf1_{\mathcal H}
\]

has total \(W\), point margins \(rW/n\), and values in \(\{0,1,2\}\).
Every member of \(\mathcal H\) has \(U\)-intersection size zero or eight,
whereas every member of \(\operatorname{supp}x\) has \(U\)-intersection
size four. Their Johnson distance is at least four, so adding
\(\mathbf1_{\mathcal H}\) preserves the \(1\)-Lipschitz property.

At depth one, \(c_1=1\). The two negative \(x\)-strata are exactly the
\(2T\) holes. There is no load above two. Hence

\[
 \boxed{Q_1=4T,\qquad O_1=2T.}
\]

The exact ratio is

\[
 \frac{T}{W}
 =\frac{m(m-1)(m+1)(m-4)}
 {16(2m+1)(2m-1)(2m-3)(2m-5)}\longrightarrow\frac1{256}.
\]

Thus \(Q_1/W\to1/64\) and \(O_1/W\to1/128\), as claimed.

Because \(\mu\) is \(1\)-Lipschitz,

\[
 G_{\tau,1}=0,\qquad
 A_{\tau,1}=\Pi_{\tau,1},\qquad
 \beta_{\tau,1}=A_{\tau,1},\qquad
 C_{\tau,1}^*=0
\]

for every transposition. The unqualified aggregate equalities in the raw
report require all other included ranks to be \(1\)-Lipschitz as well.

That aggregate signed relaxation can be supplied. At another rank \(s\),
write \(W=cN_s+h\). Since

\[
 \frac{sh}{n}=\frac{sW}{n}-c\binom{n-1}{s-1}\in\mathbb Z,
\]

there exists a simple \(s\)-uniform family of \(h\) sets having constant
degree \(sh/n\): choose \(h\) distinct \(s\)-sets minimizing the squared
degree sum and use the same high-to-low exchange argument. Giving these
sets load \(c+1\) and all others load \(c\) produces a point-regular
balanced, hence \(1\)-Lipschitz, load vector. Simultaneous integral
selector surjectivity then produces an integral signed cyclic-order vector
with exact middle incidence and all prescribed lower histograms.

The proper conclusion is nevertheless limited. This signed vector has
zero ideal transposition gain at every chosen rank, but it is not a local
minimum of the unrestricted signed lattice: signed selector moves can
directly change and balance the first-shadow load. It obstructs deductions
from totals, margins, parity, Johnson geometry, and signed affine
surjectivity alone. It is not an exact factor and does not obstruct
nonnegative squarefree support-feasible moves.

## 6. Scope of the SDP and zonotope obstructions

For the formal pattern

\[
 d_1=2u,\qquad d_2=2u,\qquad d_3=-2u,
\]

take \(u\) to be an integral anti-invariant vector. If \(h=\|u\|^2\), then

\[
 A=4h,\quad V=12h,\quad
 (w_{12},w_{13},w_{23})=(4h,-4h,-4h),\quad \Pi=0.
\]

Every integral coefficient
\(\varepsilon_1+\varepsilon_2-\varepsilon_3\) is odd, so

\[
 \beta=A,\qquad C^*=0.
\]

In the basic vector-residual SDP, choose unit vectors \(a,b\) with
\(\langle a,b\rangle=-1/2\), and put \(c=a+b\). Then \(c\) is unit and
\(a+b-c=0\), so the SDP residual is zero and its formal cut gain is \(A/4\).
This algebra is correct, and the parity floor is vacuous because all row
coefficients are even.

It is not an obstruction to arbitrary SDPs. The corresponding SDP cut
distances are

\[
 x_{12}=\frac34,\qquad x_{13}=x_{23}=\frac14,
\]

which violate the triangle inequality
\(x_{12}\le x_{13}+x_{23}\). The three-vertex metric/cut relaxation is
already exact and excludes this point. The safe conclusion is:

> The basic elliptope/vector residual relaxation, even with scalar parity
> floors, has an arbitrarily scalable additive gap on this formal pattern.

The pattern is not proved realizable by genuine wreath ownership
components. It does not refute all SDP hierarchies or Grothendieck-based
arguments. It does show that a generic conversion from this basic
relaxation cannot retain a positive fraction of relaxed gain without an
additive loss at least

\[
 \frac A4=\frac1{12}\sum_{K<L}|w_{KL}|
\]

on this family. Thus standard signed hyperplane/basic-Grothendieck rounding
cannot produce a Catalan error without additional ownership geometry
controlling absolute weight or frustration.

The zonotope rounding identity is correct after stating its hypotheses.
Fix the signs outside \(J\) into a residual \(r\), take
\(x_K\in[-1,1]\), and round independently with
\(\mathbb E\varepsilon_K=x_K\). Then

\[
 \mathbb E\left\|r+\sum_{K\in J}\varepsilon_Kd_K\right\|^2
 =\left\|r+\sum_{K\in J}x_Kd_K\right\|^2
 +\sum_{K\in J}(1-x_K^2)\|d_K\|^2.
\]

Some signing attains at most this expectation. For a fixed fiber

\[
 \left\{x\in[-1,1]^J:\sum_{K\in J}x_Kd_K=y\right\},
\]

an extreme point has at most
\(\rho=\operatorname{rank}\{d_K:K\in J\}\) fractional coordinates, by a
linear-dependence perturbation, and \(\rho\) can occur. This is the precise
rank statement; the report's phrase "fractional boundary components" is
ambiguous. Rank alone gives no Catalan error.

## 7. Genuine MSW local components

Equations (16)--(19) are correct when every unmarked inner product and norm
is interpreted in the weighted \(H\)-space. If each \(K\in J\) is selected
independently with probability \(p\), and

\[
 X=\sum_{K\in J}\xi_Kd_K,\qquad D=d_J,\qquad
 V_J=\sum_{K\in J}\|d_K\|_H^2,
\]

then

\[
 \mathbb E\langle X,d-X\rangle_H
 =p(\langle D,d\rangle_H-V_J)
  -p^2(\|D\|_H^2-V_J).
\]

At \(p=1/2\) this is exactly (17).

For \(H\le m-2\), each local component has unweighted squared rank norm
four at \(q=1\), and eight for \(2\le q\le H\). Therefore

\[
 V_J=C_{m-2}\left(\frac4{c_1}
       +8\sum_{q=2}^H\frac1{c_q}\right)
 \le(8H-4)C_{m-2}.
\]

The range \(H\le m-2\) is needed. Also,
\(V_{J,q}=8C_{m-2}\) only for \(q\ge2\); at \(q=1\) it equals
\(4C_{m-2}\).

The lower bound (20) is valid. Put \(M=m-2\) and write a selected Dyck
suffix as \(R=UV\), with \(U\in\mathcal D_q\) and
\(V\in\mathcal D_{M-q}\). In the exact four-arm formula, deleting the
first \(q\) entries from the \(E\)-list leaves a positive suffix dipole whose
core depends only on \(V\) and contains \(n\). All \(C_q\) choices of
\(U\) pile with the same sign. No opposite-sign arm contains \(n\), and
different \(V\)'s give distinct cores. Each piled dipole has squared norm
\(2C_q^2\). Hence, for \(1\le q\le M\),

\[
 \boxed{\|d_{J,q}\|_2^2\ge2C_{M-q}C_q^2.}
\]

For \(q\ge2\), the clean weighted consequence is

\[
 \|d_J\|_H^2-V_J
 \ge\frac{2C_{M-q}C_q^2}{c_q}-V_J.
\]

Taking \(q=H=\lceil A\sqrt m\rceil\), with fixed \(A\), gives

\[
 \frac{\|d_J\|_H^2-V_J}{V_J}
 \ge c_A\frac{4^H}{H^4}-1,
\]

and therefore (22) is asymptotically correct.

This refutes a bounded-positive-overlap proof. For example, because all
local vectors have the same squared norm, a bound of \(D\) on the maximum
positive Gram-neighbor degree would imply

\[
 \|d_J\|_H^2-V_J
 =2\sum_{K<L}w_{KL}
 \le2\sum_{K<L}(w_{KL})_+\le D\,V_J.
\]

The displayed ratio forces \(D\) to be much larger than \(O(n)\).
This scope concerns the \(p=0\), \(\tau=(2\,3)\),
\(C_{m-2}\)-component family \(J\), not every contextual family or every
transposition.

The report's Bernoulli interpretation needs correction. Writing

\[
 R'=d-D,\qquad B_J=\|D\|_H^2-V_J,
\]

equation (16) becomes

\[
 \boxed{
 \mathbb E\langle X,d-X\rangle_H
 =p(1-p)B_J+p\langle D,R'\rangle_H.}
\]

Thus the huge positive internal coherence \(B_J\) is favorable. It is not
an obstruction to choosing \(p=1/n\). It shows only that an argument which
tries to upper-bound the quadratic overlap by \(O(n)V_J\) is impossible.
Bernoulli thinning fails only if the larger components have adverse
alignment

\[
 \langle D,R'\rangle_H\lesssim-(1-p)B_J.
\]

Accordingly, "an equally large favorable alignment" should be replaced by
"absence of an equally large adverse alignment." The large coherence may
be a resource rather than a loss.

Finally, the explicit error in (19) is

\[
 (2H-1)C_{m-2}=\Theta(HC_m),
\]

whereas the final \(LM_A\) derivative target requires an error
\(\Theta(HC_m/n)\). Section 6 by itself remains a full factor \(n\) short
in the additive error, unless its coherence/alignment term pays that gap.

## 8. Final implication and exact scope

To imply \(LM_A\), the two proposed lemmas need the following joint form.
For every exact factor \(F\), there must exist one and the same
transposition \(\tau\) and one feedback-row certificate \(\mathcal R\) such
that, with constants uniform in \(F\),

\[
 G_\tau(F)
 \ge \frac{a_A}{n}\bigl(\mathcal Q_A(F)-C_{1,A}H_AC_m\bigr),
\]

and

\[
 \sum_{p\notin\mathcal R}\alpha_p(b_p-\pi_p)
 +\sum_{p\in\mathcal R}\alpha_p(L_p^2-\pi_p)
 \le \frac{C_{2,A}}{n}H_AC_m.
\]

Then (10) gives

\[
 C_\tau^*(F)
 \ge\frac{a_A}{n}\mathcal Q_A(F)
 -\frac{a_AC_{1,A}+C_{2,A}/4}{n}H_AC_m.
\]

Every transposition-cut local minimum would consequently have
\(\mathcal Q_A(F)=O_A(H_AC_m)\), which is \(o(W)\) because
\(H_AC_m/W=H_A/n=o(1)\). Finite exact-factor descent would then prove
fixed-window overload, diagonal MWB, and the asymptotic contiguous-OR
theorem.

The quantifiers are essential:

* the ideal-gain and low-loss estimates must hold for the same \(\tau\);
* they must hold at every exact factor encountered, not only at the
  canonical MSW factor;
* the same component signs act at every depth in the weighted window.

This route proves only unlabelled overload. It does not produce one common
balanced nested owner resolution and therefore does not prove labelled
synchronization.

The report's final claim that any proof must use literal cyclic-prefix
chronology is stronger than what was established. The audit supports the
narrower conclusion: totals, point margins, parity, Johnson
\(1\)-Lipschitz geometry, signed selector surjectivity, the basic elliptope,
row sparsity alone, and the known local MSW atlas do not by themselves
prove the needed component cut. A proof may use chronology, or some other
genuine support-feasible ownership invariant not present in these
relaxations.

## 9. Independent audit record

The normalization, matching/chaos, forest, synthetic-load, and MSW sections
were independently rederived. The independent checks agreed on the
constants \(1/4,1/2,1/36,1/18,1/64,1/128\), the Catalan lower bound in
(20), and the asymptotic ratio in (22). They also independently identified
the unordered-pair convention, the non-cone wording, the basic-SDP-only
scope, the rank range \(H\le m-2\), the favorable sign of internal MSW
coherence, and the need for a joint same-transposition quantifier.
