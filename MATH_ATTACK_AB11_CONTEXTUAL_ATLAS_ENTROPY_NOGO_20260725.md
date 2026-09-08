# AB11: entropy ceiling for the lineage-respecting shifted two-for-two MSW atlas

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver,
computer algebra, or numerical experiment is used. Every state mentioned
below is a literal integral exact middle wreath factor, and every transition
is required to be a complete cut of freshly recomputed genuine ownership
components.

## 0. Verdict

The AB10 groupwise obstruction asks for an \(O(H)\)-stage mechanism which
branches almost every private Catalan group in almost every useful round.
The complete certified lineage-respecting atlas of shifted MSW two-for-two
components does not provide such a mechanism, even if one grants arbitrary
durability, arbitrary adaptive chart signs, and unlimited chart reuse.

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\operatorname{Cat}_m=\frac Wn,
\qquad H=\lceil A\sqrt m\rceil,
\tag{0.1}
\]

and fix either the original AB7 colour \(s=0\), or an AB8 shifted colour,

\[
s=0\quad\text{or}\quad2\le s\le m-H-4,
\qquad r=m-s-H-2\ge2.
\tag{0.2}
\]

The canonical shifted packet rows are indexed by

\[
P_sGUV,qquad
P_s=1^s0^s,\quad
G\in\{1100,1010\},\quad
U\in\mathcal D_H,\quad V\in\mathcal D_r.
\tag{0.3}
\]

For each fixed \(V\), the audited four-arm formula supplies one literal
depth-\(H\) occurrence token from the two rows in (0.3), for every
\(U\in\mathcal D_H\), on the private target pair \(\{S_V,T_V\}\).
Thus there are

\[
T=\operatorname{Cat}_H
\tag{0.4}
\]

labelled canonical packet tokens in each of

\[
L=\operatorname{Cat}_r
\tag{0.5}
\]

private groups.

For a Dyck word \(Z\in\mathcal D_h\), let \(\chi(Z)\) be the set of
shifted contextual two-for-two chart positions:

\[
\chi(Z)=
\left\{
p\in\{0,\ldots,h-2\}:
Z=P1100R\ \text{or}\ Z=P1010R
\text{ for some }P\in\mathcal D_p
\right\}.
\tag{0.6}
\]

At position \(p\), the chart colour is

\[
\tau_p=(2p+2\ \ 2p+3).
\tag{0.7}
\]

Call a history **contextual-atlas-only** if every nontrivial component it
switches is a current genuine transported copy of one of these certified
size-two contextual components, with row lineages retained, **and** a token
whose initial canonical MSW row has index \(Z\) may be acted on by
\(\tau_p\) only when \(p\in\chi(Z)\). This definition grants the route
the strongest possible durability: whenever a certified chart survives as
a fresh component, it may be signed arbitrarily, repeatedly, and
adaptively. A history in which overlapping chart switches give an old
lineage a new chart colour, or which uses a newly recombined, larger, or
nonnative component, is outside this lineage-respecting atlas and outside
the present no-go.

### Main theorem

Let \(\mathscr X_{m,s}\) be the full intrinsic \(\tau_s\)-component cell
of the canonical MSW factor, including every orientation of every large
component as well as all size-two packet components. For fixed \(A>0\),
all sufficiently large \(m\), every starting vertex
\(F_0\in\mathscr X_{m,s}\), and every contextual-atlas-only history from
\(F_0\), the endpoint obeys

\[
\boxed{
\Phi_H(F_{\rm end})
\ge
\frac{L_0T_0^2}{64}-\frac{L_0T_0}{2}-P_H^{\min},}
\tag{0.8}
\]

where

\[
T_0
=\operatorname{Cat}_H-2\operatorname{Cat}_{H-1}
=T\frac{H-2}{2H-1},
\tag{0.9}
\]

\[
L_0
=\operatorname{Cat}_r-2\operatorname{Cat}_{r-1}
=L\frac{r-2}{2r-1}.
\tag{0.10}
\]

In particular, when \(H,r\ge4\),

\[
\boxed{
\Phi_H(F_{\rm end})
\ge
\frac{LT^2}{4096}-\frac{LT}{2}-P_H^{\min}.}
\tag{0.11}
\]

Let

\[
K_A=
\binom{\left\lceil e^{2(A+1)(A+2)}\right\rceil+1}{2}.
\tag{0.12}
\]

Using the exact factorial normalization

\[
\mathfrak F_A(F)=\sum_{q=1}^H\frac{\Phi_q(F)}{b_q},
\qquad
b_q=\binom{c_q+1}{2},
\tag{0.13}
\]

one obtains

\[
\boxed{
\frac{\mathfrak F_A(F_{\rm end})}{W}
>
\frac{4^{H-s}}{2^{20}K_A nH^4}
-1-\frac1{2n}.}
\tag{0.14}
\]

For the balanced cage \(s=\lfloor H/2\rfloor\), the right side tends to
infinity. Hence no contextual-atlas-only history of any length reaches

\[
\mathcal Q_H=O_A(H\operatorname{Cat}_m),
\tag{0.15}
\]

and in particular none proves an energy-decreasing escape to the
constant-one scale.

For \(s=0\), \(\mathscr X_{m,0}\) is the original AB7
\((2\ 3)\)-cell. Its high cell minimizer \(G_m\) is therefore covered by
the same theorem, now with the stronger numerator \(4^H\) in (0.14).
Thus leaving that prescribed cell through any number of
lineage-respecting shifted two-for-two charts still cannot lower its energy
to the constant-one scale.

This closes the complete lineage-respecting shifted two-for-two atlas as the
requested binary-routing bypass. Any successful chronology must use a
genuinely recombined/larger ownership component, a new colour created by
overlapping chart recombination, or a nonnative circuit. It does not
exclude such moves, so no constant-one theorem is claimed.

## 1. Exact chart-incidence census

### Lemma 1.1 (complete Catalan chart census)

For every \(h\ge2\),

\[
\boxed{
\sum_{Z\in\mathcal D_h}|\chi(Z)|
=2\operatorname{Cat}_{h-1}.}
\tag{1.1}
\]

Consequently

\[
\boxed{
\#\{Z\in\mathcal D_h:\chi(Z)=\varnothing\}
\ge
\operatorname{Cat}_h-2\operatorname{Cat}_{h-1}
=\operatorname{Cat}_h\frac{h-2}{2h-1}.}
\tag{1.2}
\]

#### Proof

For a fixed position \(p\), every chart is determined uniquely by

\[
P\in\mathcal D_p,qquad
R\in\mathcal D_{h-p-2},
\]

and it contains exactly the two Dyck words \(P1100R\) and
\(P1010R\). Therefore

\[
\sum_{Z\in\mathcal D_h}|\chi(Z)|
=2\sum_{p=0}^{h-2}
\operatorname{Cat}_p\operatorname{Cat}_{h-p-2}.
\]

The Catalan convolution makes the last sum
\(2\operatorname{Cat}_{h-1}\), proving (1.1).

The number of words incident with at least one chart is at most the total
incidence count in (1.1). Hence the number incident with no chart is at
least the first difference in (1.2). Finally,

\[
\frac{2\operatorname{Cat}_{h-1}}{\operatorname{Cat}_h}
=\frac{h+1}{2h-1},
\]

which gives the displayed exact ratio. \(\square\)

Thus asymptotically half of all Dyck words are missed by every shifted
two-for-two chart in the complete native atlas. This is a row-lineage
statement, not a count of colours or stages.

## 2. Concatenation has only one new seam chart

### Lemma 2.1 (chart positions under Dyck concatenation)

Let \(X\in\mathcal D_a\) and \(Y\in\mathcal D_b\), with \(a,b\ge1\).
Then

\[
\boxed{
\chi(XY)
\subseteq
\chi(X)
\cup(a+\chi(Y))
\cup\{a-1\}.}
\tag{2.1}
\]

Here \(a+\chi(Y)=\{a+p:p\in\chi(Y)\}\). The exceptional position
\(a-1\) is possible only when the last primitive component of \(X\) and
the first primitive component of \(Y\) are both \(10\), producing the
cross-seam block \(1010\).

#### Proof

Take \(p\in\chi(XY)\). The prefix of semilength \(p\) is Dyck, and the
next four symbols are \(1100\) or \(1010\).

If \(p\ge a\), the chart begins in \(Y\), so
\(p\in a+\chi(Y)\). Suppose \(p<a\). The suffix of \(X\) after that
Dyck prefix is itself Dyck. If it has semilength at least two, the full
four-symbol chart lies in \(X\), giving \(p\in\chi(X)\). If it has
semilength one, it is exactly \(10\), so \(p=a-1\); the chart can cross
the seam only as \(10\,10=1010\). There is no other case. \(\square\)

Apply Lemma 2.1 three times to

\[
Z=P_sGUV.
\tag{2.2}
\]

For \(s\ge2\), the word \(P_s=1^s0^s\) has no proper Dyck return. Hence
\(|\chi(P_s)|\le1\), with equality only at \(s=2\). Each of
\(G=1100,1010\) has the single chart position zero. Therefore, if

\[
\chi(U)=\chi(V)=\varnothing,
\tag{2.3}
\]

then

\[
\boxed{
\chi(P_sGUV)
\subseteq
\{0,s-1,s,s+1,s+H+1\}.}
\tag{2.4}
\]

For \(s=0\), apply Lemma 2.1 only to \(GUV\); under the same hypothesis,

\[
\boxed{
\chi(GUV)\subseteq\{0,1,H+1\}.}
\tag{2.5}
\]

Some displayed positions may be absent or coincide. The important point is
that the possible chart palette has size at most five and is independent of
the particular chart-free words \(U,V\).

## 3. Canonical private tokens and the at-most-five-colour orbit

The shifted four-arm formula gives, for every \((U,V)\), one consistently
oriented unit dipole on \(\{S_V,T_V\}\) in the difference between the two
sides of the outer \(\tau_s\)-packet component. If the unit coefficient is
positive on one side of the trade, nonnegativity of the opposite side shows
that the other side contains a literal occurrence on the opposite private
target. Consequently **each of the two shores** contains a literal
occurrence on one member of \(\{S_V,T_V\}\).

Every vertex of \(\mathscr X_{m,s}\) chooses exactly one complete shore of
each packet root. The packet roots are disjoint and persist throughout the
whole intrinsic cell. Thus, at an arbitrary starting vertex
\(F_0\in\mathscr X_{m,s}\), one may select a literal occurrence token

\[
\omega_{U,V}
\tag{3.1}
\]

owned either by one of the two canonical rows
\(P_s1100UV,P_s1010UV\) or by its \(\tau_s\)-translated shore, and lying
on \(S_V\) or \(T_V\). Label it by the underlying canonical row lineage.
Tokens with different \((U,V)\) are distinct because their packet roots
are disjoint. The possible initial \(\tau_s\)-translation adds no chart
colour: \(s\) already belongs to the common palette in (2.4), or to (2.5)
when \(s=0\).

Fix a chart-free \(V\), and retain only the tokens with chart-free \(U\).
By Lemma 1.1 their number is at least \(T_0\) from (0.9).

In a contextual-atlas-only history, the lineage of such a token can be
acted on only by a colour in its initial chart set. Lemma 2.1 places every
such set inside the common palette (2.4), or the smaller palette (2.5).
The native colours
\(\tau_p\) form a coordinate matching and hence commute. Repetitions only
change the parity of the action of one involution. Therefore every retained
token of group \(V\) ends in the orbit of its initial target under a group
of order at most

\[
2^5=32.
\tag{3.2}
\]

Moreover \(S_V\) and \(T_V\) are interchanged by \(\tau_s\), and
\(s\) belongs to the common palette. Hence the union of the two possible
initial target orbits still has size at most \(32\), not \(64\).

Let \(u_{V,X}\) be the endpoint multiplicities of the retained tokens.
Cauchy--Schwarz gives

\[
\sum_X\binom{u_{V,X}}2
\ge
\frac{T_0^2}{64}-\frac{T_0}{2}.
\tag{3.3}
\]

By Lemma 1.1, at least \(L_0\) private words \(V\) are chart-free.
The corresponding labelled token-pair sets are disjoint. Collisions with
discarded or unselected occurrences only add nonnegative terms. Summing
(3.3) proves

\[
P_H(F_{\rm end})
\ge
L_0\left(\frac{T_0^2}{64}-\frac{T_0}{2}\right).
\tag{3.4}
\]

Subtract the exact adjacent-integer floor \(P_H^{\min}\). This proves
(0.8).

For \(H,r\ge4\), equations (0.9)--(0.10) give

\[
T_0\ge\frac T4,
\qquad L_0\ge\frac L4.
\tag{3.5}
\]

Using \(L_0T_0\le LT\) in the negative term of (0.8) gives (0.11).

## 3A. Entropy sharpening: repetitions do not create new native bits

The preceding proof discarded every \(U\) which has even one contextual
chart. One can retain all \(T\) tokens and obtain a second, conceptually
sharper ceiling.

For a finite probability vector \(x\), write

\[
\mathsf H(x)=-\sum_i x_i\log_2x_i,
\qquad
h_2(t)=-t\log_2t-(1-t)\log_2(1-t).
\tag{3A.1}
\]

### Lemma 3A.1 (pathwise routing entropy)

Let \(\Omega\) be a group of \(T\) labelled tokens initially supported on
at most two targets. In a realized component-cut history, let
\(A_j(\omega)\in\{0,1\}\) be the action bit at stage \(j\), and put

\[
\theta_j=\frac1T\#\{\omega:A_j(\omega)=1\}.
\]

If \(X\) is the endpoint target of a uniformly chosen token, then

\[
\boxed{
\mathsf H(X)
\le1+\sum_jh_2(\theta_j).}
\tag{3A.2}
\]

Consequently its internal endpoint collision count is at least

\[
\boxed{
\frac{T^2}{2^{2+\sum_jh_2(\theta_j)}}-\frac T2.}
\tag{3A.3}
\]

#### Proof

The endpoint target is a deterministic function of the initial target and
the action word \((A_1,\ldots,A_D)\). Entropy decreases under a
deterministic map and is subadditive, so

\[
\mathsf H(X)
\le \mathsf H(X_0,A_1,\ldots,A_D)
\le1+\sum_j\mathsf H(A_j)
=1+\sum_jh_2(\theta_j).
\]

If \(u_Y/T\) is the endpoint target law, Shannon entropy dominates
Rényi entropy of order two:

\[
-\log_2\sum_Y(u_Y/T)^2\le\mathsf H(X).
\]

Thus \(\sum_Yu_Y^2\ge T^2 2^{-\mathsf H(X)}\). Substitution into
\(\sum_Y\binom{u_Y}{2}=(\sum_Yu_Y^2-T)/2\) proves (3A.3). \(\square\)

This statement is pathwise. Adaptivity and correlations among component
signs do not alter it.

For the native matching, repetitions should be collapsed before applying
the lemma. At an endpoint, let \(B_p(\omega)\) be the parity of all actions
of colour \(\tau_p\) on token \(\omega\). Since the \(\tau_p\) are
commuting involutions, the endpoint is a deterministic function of the
initial target and the parity vector \((B_p)_p\). Hence (3A.2) remains true
with one binary-entropy term per **distinct native colour**, regardless of
how often that colour was revisited.

For a uniform \(U\in\mathcal D_H\), put

\[
\alpha_{H,p}
=\frac{2\operatorname{Cat}_p
          \operatorname{Cat}_{H-p-2}}
       {\operatorname{Cat}_H},
\qquad 0\le p\le H-2.
\tag{3A.4}
\]

This is the exact fraction of \(U\)-lineages incident with the contextual
chart at position \(p\). In a contextual-atlas-only history, a parity bit
at that internal colour can be one only on those incident lineages.
Therefore

\[
\Pr(B_p=1)\le\alpha_{H,p}.
\tag{3A.5}
\]

### Lemma 3A.2 (finite total internal chart entropy)

There is an absolute constant \(C_*<\infty\) such that, for all sufficiently
large \(H\), every choice of parity bits satisfying (3A.5) obeys

\[
\boxed{
\sum_{p=0}^{H-2}\mathsf H(B_p)\le C_*.}
\tag{3A.6}
\]

#### Proof

The elementary Wallis bounds give, for \(k\ge1\),

\[
\frac{4^k}{2\sqrt{k}(k+1)}
\le\operatorname{Cat}_k
\le\frac{4^k}{(k+1)^{3/2}}.
\tag{3A.7}
\]

They follow by applying the usual two-sided Wallis estimate to
\(\binom{2k}{k}\) and then dividing by \(k+1\).

For \(0\le p\le(H-2)/2\), (3A.7) gives

\[
\alpha_{H,p}
\le\frac{2}{(p+1)^{3/2}}.
\tag{3A.8}
\]

The same bound with \(p\) replaced by \(H-p-2\) holds in the other half.
For the four positions nearest each endpoint use only
\(\mathsf H(B_p)\le1\). At every remaining position the right side of
(3A.8) is below \(1/2\), and \(h_2\) is increasing on \([0,1/2]\).
Thus one may take

\[
C_*
=8+2\sum_{j=4}^{\infty}
h_2\!\left(\frac{2}{(j+1)^{3/2}}\right).
\tag{3A.9}
\]

This series converges because
\(h_2(x)\le x\log_2(e/x)\) for \(0<x\le1/2\), and
\(\sum_j(\log j)j^{-3/2}<\infty\). Equations (3A.5)--(3A.9) prove
(3A.6). \(\square\)

Now fix a chart-free \(V\). Apart from the internal \(U\)-chart colours,
Lemma 2.1 permits only the common palette (2.4), or (2.5) when \(s=0\).
The initial private-pair choice contributes at most one entropy bit, the at
most five common
parities contribute at most five, and Lemma 3A.2 contributes at most
\(C_*\). Lemma 3A.1 therefore gives, using all \(T\) canonical private
tokens,

\[
\boxed{
\sum_X\binom{u_{V,X}}2
\ge
2^{-C_*-7}T^2-\frac T2.}
\tag{3A.10}
\]

There are at least \(L_0\) such chart-free groups \(V\). Hence the stronger
constant-form obstruction

\[
\boxed{
\Phi_H(F_{\rm end})
\ge
2^{-C_*-7}L_0T^2-\frac{L_0T}{2}-P_H^{\min}.}
\tag{3A.11}
\]

The explicit rational constant in (0.11) is retained as the main displayed
bound because it avoids evaluating \(C_*\). Equation (3A.11) explains the
underlying information obstruction: the entire internal shifted atlas
carries only \(O(1)\) endpoint entropy per private group, not the
\((2+o(1))(H-s)\) bits required by the private-pile collision ledger
(in particular \((2+o(1))H\) bits when \(s=0\)).

## 4. Exact asymptotic accounting

For \(H\ge2\),

\[
T=\operatorname{Cat}_H\ge\frac{4^H}{4H^2}.
\tag{4.1}
\]

Since every successive Catalan ratio is less than four,

\[
L=\operatorname{Cat}_{m-s-H-2}
>\frac{\operatorname{Cat}_m}{4^{s+H+2}}
=\frac W{n4^{s+H+2}}.
\tag{4.2}
\]

Consequently

\[
LT^2>
\frac{W4^{H-s}}{256nH^4}.
\tag{4.3}
\]

At depth \(H\),

\[
b_H\le K_A,
\qquad
P_H^{\min}\le Wb_H,
\tag{4.4}
\]

and Catalan concatenation gives

\[
LT\le\operatorname{Cat}_{m-s-2}<B=\frac Wn.
\tag{4.5}
\]

Divide (0.11) by \(b_H\), discard the other nonnegative depths in
\(\mathfrak F_A\), and use (4.3)--(4.5). The positive term is strictly
larger than

\[
\frac{W4^{H-s}}{4096\cdot256\,K_A nH^4}
=\frac{W4^{H-s}}{2^{20}K_A nH^4}.
\tag{4.6}
\]

The two negative terms contribute at worst \(-W/(2n)\) and \(-W\),
respectively. This proves (0.14).

For \(s=\lfloor H/2\rfloor\), the exponential
\(4^{H-s}\) dominates \(nH^4=O_A(m^3)\), so the right side of (0.14)
tends to infinity. Finally,

\[
\mathfrak F_A(F)\le\mathcal Q_H(F)
\tag{4.7}
\]

termwise because \(Q_q=2\Phi_q\) and
\(b_q=c_q(c_q+1)/2\). Hence (0.14) excludes (0.15).

## 5. Precise proved/conditional boundary

The theorem has the following exact quantifiers:

\[
\boxed{
\begin{gathered}
\forall A>0\ \exists m_0(A)\ \forall m\ge m_0(A)\\
\forall s\in\{0\}\cup([2,m-H-4]\cap\mathbb Z)\\
\forall F_0\in\mathscr X_{m,s}\ 
\forall\text{ realized contextual-atlas-only histories from }F_0:\\
\text{the endpoint satisfies (0.8), and if }H,r\ge4\text{, (0.14).}
\end{gathered}}
\tag{5.1}
\]

The route is allowed:

* every shifted native colour \(\tau_p\);
* every certified contextual size-two component at that colour;
* arbitrary subsets of all such components;
* arbitrary order, repetition, and history-dependent signing; and
* every transported copy which genuinely persists after prior moves.

What is not covered is exactly what the certified atlas does not supply:
a fresh component which recombines chart lineages, a component larger than
two which is used essentially, or a nonnative transposition/circuit. Such a
move can give a previously chart-free lineage a new action colour and may
break the at-most-five-colour orbit ceiling.

Thus the lineage-respecting contextual shifted two-for-two family is
rigorously exhausted as an \(O(H)\) Dyck-branching bypass. The next exact
statement must use overlapping-chart recombination, recombined/larger
genuine chronology, or a nonnative colour; merely scheduling more durable
copies of the known charts along their original lineages cannot prove an
energy decrease to the constant-one scale.

No constant-one conclusion is made.
