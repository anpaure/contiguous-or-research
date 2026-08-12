# Saturating Johnson cycle: omitted-owner Hall correction and logarithmic abstract extension

Date: 2026-07-25

Method: pure mathematics only.  No finite search, solver, or computation is
used.

## 0. Result

Put

\[
 n=2m+1,\qquad
 W=\binom{2m+1}{m},\qquad
 V_q=\binom{[2m+1]}{m-q},\qquad N_q=|V_q|.
\]

Let

\[
 S_0,X_0,S_1,X_1,\ldots,S_{N_1-1},X_{N_1-1},S_0
 \tag{0.1}
\]

be the saturating Boolean cycle of Theorem 18 in
`TRANSLATION_PACKET_MULTIDEPTH_RAINBOW_LEMMA_20260725.md`.  Thus the
\(S_i\)'s are all members of \(V_1\), the \(X_i\)'s are distinct members
of \(V_0\), and

\[
 S_i\subset X_i\supset S_{i+1}.
 \tag{0.2}
\]

Write

\[
 U=\{X_i:i\in\mathbb Z_{N_1}\},\qquad
 E=V_0\setminus U,
 \qquad
 d=|E|=W-N_1=\frac{2W}{m+2}.
 \tag{0.3}
\]

The previously asserted unresolved Hall obstruction at depth one is false.
The cycle itself gives the exact incidence cap

\[
 \boxed{d_E(S):=|\{X\in E:S\subset X\}|\le m
 \quad(S\in V_1),}
 \tag{0.4}
\]

and hence

\[
 \boxed{|\partial\mathcal A|\ge |\mathcal A|
 \quad(\mathcal A\subseteq E).}
 \tag{0.5}
\]

Thus the omitted owners have distinct facet representatives.  Together
with the rainbow cycle bijection, they give the exact balanced depth-one
load: one core owner at every target and one omitted owner at each of \(d\)
distinct high targets.

There is also no abstract Boolean cut obstruction at the next transition.
For every \(m\ge37\), **every** possible set of \(d\) depth-one high targets
extends integrally from \(V_1\) to \(V_2\) with every depth-two load equal to
one or two.  The proof below checks both families of Gale inequalities,
including the exact floor baselines and the exact binomial threshold.

This does not prove a monotone-release certificate through
\(q\le A\sqrt m\).  More importantly, the saturating Johnson cycle is not
known to be a disjoint union of literal length-\(n\) tight wreath cycles.
The extensions below are allowed to choose arbitrary Boolean children of
the cycle owners; they do not produce their canonical same-start cyclic
flags.  Hence they prove an abstract owner-labelled extension only to
logarithmic depth, not \(\mathrm{MR}_A\), \(\mathrm{CA}_A\), or the
constant-one theorem.

## 1. The exact omitted-owner incidence cap

For \(S\in V_1\), let

\[
 d_E(S)=|\{X\in E:S\subset X\}|.
\]

### Lemma 1.1

For every \(S\in V_1\),

\[
 d_E(S)\le m.
 \tag{1.1}
\]

#### Proof

The set \(S\) occurs exactly once among the lower vertices in (0.1).  Its
two neighbours on that simple alternating cycle are two distinct middle
sets in \(U\), and both contain \(S\).  A rank-\((m-1)\) set in
\([2m+1]\) has exactly

\[
 (2m+1)-(m-1)=m+2
\]

middle supersets.  At least two of them belong to \(U\), so at most \(m\)
belong to \(E\).  This is (1.1). \(\square\)

### Theorem 1.2 — the omitted owners have an SDR

There is an injection

\[
 \eta:E\longrightarrow V_1,
 \qquad \eta(X)\subset X.
 \tag{1.2}
\]

Equivalently, for every \(\mathcal A\subseteq E\),

\[
 |\partial\mathcal A|\ge|\mathcal A|.
 \tag{1.3}
\]

#### Proof

Count the inclusion flags \((X,S)\) with
\(X\in\mathcal A\), \(S\in\partial\mathcal A\), and \(S\subset X\).
Every \(X\in\mathcal A\) has exactly \(m\) facets, whereas Lemma 1.1
shows that every \(S\in\partial\mathcal A\) is incident with at most \(m\)
members of \(E\), and therefore with at most \(m\) members of
\(\mathcal A\).  Hence

\[
 m|\mathcal A|
 \le m|\partial\mathcal A|.
 \tag{1.4}
\]

This proves (1.3), and Hall's theorem gives (1.2). \(\square\)

The proof also gives the exact nonnegative slack identity

\[
 m\bigl(|\partial\mathcal A|-|\mathcal A|\bigr)
 =\sum_{S\in\partial\mathcal A}
   \bigl(m-d_{\mathcal A}(S)\bigr),
 \tag{1.5}
\]

where \(d_{\mathcal A}(S)=|\{X\in\mathcal A:S\subset X\}|\).

## 2. Exact depth-one balance

Orient the rainbow assignment by

\[
 \phi(X_i)=S_i.
 \tag{2.1}
\]

This is a bijection \(U\to V_1\), and \(\phi(X_i)\subset X_i\).
Let

\[
 H_1=\eta(E).
 \tag{2.2}
\]

Then \(|H_1|=d\), one owner in \(U\) is assigned to every member of
\(V_1\), and one owner in \(E\) is assigned to every member of \(H_1\).
The resulting depth-one load is

\[
 b_1(S)=1+\mathbf1_{H_1}(S).
 \tag{2.3}
\]

Indeed

\[
 \frac W{N_1}=\frac{m+2}{m}=1+\frac2m.
 \tag{2.4}
\]

For \(m\ge3\), the exact floor is \(c_1=1\), and the number of high
targets is

\[
 W-N_1=d.
 \tag{2.5}
\]

Thus (2.3) is precisely a floor/ceiling-balanced depth-one load.  No
additional released cycle owner is required.

## 3. The two Gale cut families for the next transition

Let \(H\subseteq V_1\) be arbitrary with \(|H|=d\), and give each
\(R\in V_1\) supply

\[
 w(R)=1+\mathbf1_H(R).
 \tag{3.1}
\]

We seek a nonnegative integral flow on the facet incidences

\[
 R\in V_1\longrightarrow T\in V_2,\qquad T\subset R,
 \tag{3.2}
\]

which uses all parent supply and gives every child total load in
\([1,2]\).

For \(\mathcal A\subseteq V_2\), write

\[
 N(\mathcal A)=\{R\in V_1:T\subset R
                  \text{ for some }T\in\mathcal A\},
 \tag{3.3}
\]

and for \(\mathcal B\subseteq V_1\), write

\[
 \partial\mathcal B=\{T\in V_2:T\subset R
                       \text{ for some }R\in\mathcal B\}.
 \tag{3.4}
\]

The lower/upper transportation theorem, equivalently Hoffman's circulation
theorem applied to the bipartite network, says that the desired flow exists
if and only if

\[
 \boxed{|\mathcal A|\le w(N(\mathcal A))
 \quad(\mathcal A\subseteq V_2),}
 \tag{L}
\]

and

\[
 \boxed{w(\mathcal B)\le2|\partial\mathcal B|
 \quad(\mathcal B\subseteq V_1).}
 \tag{U}
\]

For completeness, these are exactly the two nontrivial types of Hoffman
cut.  A child family needs its one required copy from its parent
neighbourhood, giving (L).  A parent family must place all its supply into
at most two copies of its child neighbourhood, giving (U).  Conversely,
after adding a return arc carrying the total supply, every finite-capacity
Hoffman cut reduces to one of these two forms.  All bounds are integral, so
feasibility gives an integral flow.

## 4. The lower cuts

The normalized matching property between consecutive Boolean levels gives

\[
 |N(\mathcal A)|
 \ge \frac{N_1}{N_2}|\mathcal A|
 =\frac{m+3}{m-1}|\mathcal A|.
 \tag{4.1}
\]

Since \(w(R)\ge1\), every nonempty \(\mathcal A\subseteq V_2\) satisfies

\[
 \begin{aligned}
 w(N(\mathcal A))-|\mathcal A|
 &\ge |N(\mathcal A)|-|\mathcal A|\\
 &\ge \frac4{m-1}|\mathcal A|>0.
 \end{aligned}
 \tag{4.2}
\]

The empty cut is equality.  Thus every lower Gale inequality (L) holds,
with the quantitative slack in (4.2).

## 5. The upper cuts

Put

\[
 T_m=\binom{2m-3}{m-1},\qquad
 \alpha_m=\frac{N_2}{N_1}=\frac{m-1}{m+3},\qquad
 \beta_m=2\alpha_m-1=\frac{m-5}{m+3}.
 \tag{5.1}
\]

Fix \(\mathcal B\subseteq V_1\).

### Case 1: \(|\mathcal B|\le T_m\)

For nonempty \(\mathcal B\), choose the real \(x\ge m-1\) satisfying

\[
 |\mathcal B|=\binom{x}{m-1}.
\]

The bound \(|\mathcal B|\le T_m\) implies \(x\le2m-3\).  The Lovasz form
of the Kruskal--Katona theorem gives

\[
 |\partial\mathcal B|
 \ge\binom{x}{m-2}
 =|\mathcal B|\frac{m-1}{x-m+2}
 \ge|\mathcal B|.
 \tag{5.2}
\]

Therefore

\[
 w(\mathcal B)
 =|\mathcal B|+|H\cap\mathcal B|
 \le2|\mathcal B|
 \le2|\partial\mathcal B|.
 \tag{5.3}
\]

The same conclusion is trivial for the empty family.

### Case 2: \(|\mathcal B|>T_m\)

Normalized matching in the downward direction gives

\[
 |\partial\mathcal B|\ge\alpha_m|\mathcal B|.
 \tag{5.4}
\]

Hence

\[
 2|\partial\mathcal B|-|\mathcal B|
 \ge\beta_m|\mathcal B|.
 \tag{5.5}
\]

It remains to compare \(d\) with \(\beta_mT_m\).  The exact quotient is

\[
 \frac{W}{T_m}
 =\frac{4(4m^2-1)}{m(m+1)},
 \tag{5.6}
\]

and consequently

\[
 \frac d{T_m}
 =\frac{8(4m^2-1)}{m(m+1)(m+2)}.
 \tag{5.7}
\]

The inequality \(d\le\beta_mT_m\) is exactly

\[
 8(4m^2-1)(m+3)
 \le m(m+1)(m+2)(m-5).
 \tag{5.8}
\]

After subtraction, its right side minus its left side is

\[
 f(m)=m^4-34m^3-109m^2-2m+24.
 \tag{5.9}
\]

One has \(f(37)=2688>0\).  Moreover, for \(m\ge37\),

\[
 f'(m)=4m^3-102m^2-218m-2
 \ge46m^2-218m-2>0.
 \tag{5.10}
\]

Thus (5.8) holds for every \(m\ge37\).  Since
\(|H\cap\mathcal B|\le d\) and \(|\mathcal B|>T_m\), equations
(5.5)--(5.8) give

\[
 |H\cap\mathcal B|
 \le d
 \le\beta_mT_m
 <\beta_m|\mathcal B|
 \le2|\partial\mathcal B|-|\mathcal B|.
 \tag{5.11}
\]

This is (U).  Both Gale cut families are now proved.

## 6. Exact integral depth-two extension

### Theorem 6.1

For every \(m\ge37\) and every \(H\subseteq V_1\) of cardinality

\[
 |H|=d=\frac{2W}{m+2},
\]

there is an integral assignment of the \(W\) parent copies with supply
\(1+\mathbf1_H\) to rank-\((m-2)\) children such that every child receives
one or two copies.

#### Proof

Sections 4 and 5 verify (L) and (U), so the lower/upper transportation
theorem gives an integral flow.

The exact target floor is indeed one.  Namely

\[
 \frac W{N_2}
 =\frac{(m+2)(m+3)}{m(m-1)}.
 \tag{6.1}
\]

This is less than two precisely when

\[
 m^2-7m-6>0,
\]

which holds for \(m\ge8\), and it is greater than one.  Hence the integral
loads in \([1,2]\) are exactly the floor/ceiling-balanced loads at depth
two. \(\square\)

Apply this theorem to \(H=H_1\) from (2.2).  At every parent
\(S\notin H_1\), the unique outgoing unit is labelled by the unique core
owner \(\phi^{-1}(S)\).  At every \(S\in H_1\), label the two outgoing
units by \(\phi^{-1}(S)\) and \(\eta^{-1}(S)\), in either order.  The
result is one owner-labelled nested Boolean extension through depth two.
Because an actual integral completion exists, all survival and directed
crossing inequalities of the monotone-release theorem hold through
\(q=2\) for these **chosen abstract** owner paths.

## 7. General same-floor propagation and the logarithmic range

The preceding Gale argument has an exact adjacent-rank form.  It gives a
short but growing abstract extension beyond depth two.

Fix \(q\ge2\), and put

\[
 k=m-q+1,
 \qquad
 \alpha_q=\frac{N_q}{N_{q-1}}
          =\frac{m-q+1}{m+q+1},
 \qquad
 \beta_q=2\alpha_q-1
        =\frac{m-3q+1}{m+q+1},
 \tag{7.1}
\]

and

\[
 T_q=\binom{2k-1}{k}
    =\binom{2m-2q+1}{m-q+1}.
 \tag{7.2}
\]

### Theorem 7.1 — exact universal same-floor transition

Assume

\[
 c_{q-1}=c_q=1,
 \qquad \beta_q>0,
 \qquad
 h_{q-1}:=W-N_{q-1}\le\beta_qT_q.
 \tag{7.3}
\]

Then every balanced parent load

\[
 w(R)=1+\mathbf1_H(R),
 \qquad H\subseteq V_{q-1},\quad |H|=h_{q-1},
 \tag{7.4}
\]

has an integral extension to a balanced load in \(\{1,2\}\) on \(V_q\).

#### Proof

Apply the same lower/upper transportation theorem as in Section 3.
For \(\mathcal A\subseteq V_q\), normalized matching gives

\[
 |N(\mathcal A)|
 \ge\frac{N_{q-1}}{N_q}|\mathcal A|
 =\frac{m+q+1}{m-q+1}|\mathcal A|
 \ge|\mathcal A|,
 \tag{7.5}
\]

so every lower cut holds.

For \(\mathcal B\subseteq V_{q-1}\), first suppose
\(|\mathcal B|\le T_q\).  The members of \(V_{q-1}\) have size \(k\),
and \(T_q=\binom{2k-1}{k}\).  The Lovasz--Kruskal--Katona argument from
(5.2) gives

\[
 |\partial\mathcal B|\ge|\mathcal B|,
\]

and hence \(w(\mathcal B)\le2|\partial\mathcal B|\).

If \(|\mathcal B|>T_q\), normalized matching gives

\[
 |\partial\mathcal B|\ge\alpha_q|\mathcal B|,
\]

and therefore

\[
 2|\partial\mathcal B|-|\mathcal B|
 \ge\beta_q|\mathcal B|
 >\beta_qT_q
 \ge h_{q-1}
 \ge|H\cap\mathcal B|.
 \tag{7.6}
\]

Thus every upper cut holds as well.  Network integrality supplies the
claimed integral extension. \(\square\)

### Corollary 7.2 — unconditional abstract propagation to logarithmic depth

Fix \(\varepsilon\in(0,1/2)\), and set

\[
 Q_m=\left\lfloor
       \left(\frac12-\varepsilon\right)\log_2m
      \right\rfloor.
 \tag{7.7}
\]

For all sufficiently large \(m\), the depth-one assignment in Section 2
extends to one owner-labelled balanced nested Boolean flow through every
depth \(q\le Q_m\).

#### Proof

First, for \(j\le Q_m\),

\[
 \lambda_j:=\frac W{N_j}
 =\prod_{t=1}^j\frac{m+t+1}{m-t+1}.
 \tag{7.8}
\]

Since \(j=O(\log m)=o(m)\), and in particular \(j\le m/2\) for large
\(m\),

\[
 \begin{aligned}
 \log\lambda_j
 &=\sum_{t=1}^j
   \log\left(1+\frac{2t}{m-t+1}\right)\\
 &\le\sum_{t=1}^j\frac{2t}{m-t+1}
 \le\frac{2j(j+1)}m=o(1).
 \end{aligned}
 \tag{7.9}
\]

Thus \(1\le\lambda_j<2\) and \(c_j=1\) throughout this range.  Moreover,

\[
 \frac{h_j}{W}
 =1-\frac1{\lambda_j}
 \le\log\lambda_j
 \le\frac{2j(j+1)}m.
 \tag{7.10}
\]

The exact threshold ratio has a particularly simple lower bound.  For
\(q=1\),

\[
 \frac{T_1}{W}
 =\frac{m+1}{2(2m+1)}>\frac14.
 \tag{7.11}
\]

Writing \(r=m-q+1\), one has

\[
 \frac{T_{q+1}}{T_q}
 =\frac{\binom{2r-3}{r-1}}{\binom{2r-1}{r}}
 =\frac{r}{2(2r-1)}>\frac14.
 \tag{7.12}
\]

Induction therefore gives the exact bound

\[
 \frac{T_q}{W}>4^{-q}.
 \tag{7.13}
\]

Also \(\beta_q\ge1/2\) whenever \(m-7q+1\ge0\), which holds throughout
the present logarithmic range for large \(m\).  For a transition
\(q\le Q_m\), (7.10), with \(j=q-1\), and (7.13) give

\[
 \frac{h_{q-1}}W
 \le\frac{2q^2}{m},
 \qquad
 \frac{\beta_qT_q}{W}>\frac12\cdot4^{-q}.
 \tag{7.14}
\]

Now

\[
 4^q\le4^{Q_m}\le m^{1-2\varepsilon},
\]

so

\[
 4q^2\,4^q
 \le4Q_m^2m^{1-2\varepsilon}<m
 \tag{7.15}
\]

for all sufficiently large \(m\).  Equations (7.14)--(7.15) imply

\[
 h_{q-1}\le\beta_qT_q
\]

at every transition \(2\le q\le Q_m\).  Starting with the exact balanced
depth-one load from Section 2 and applying Theorem 7.1 successively proves
the corollary.  Existing unit paths can be assigned to the outgoing
integral units at each parent, so all original owner labels persist.
If the resulting paths of the owners in \(U\) are declared to be the
abstract frozen core flags, then the same set \(E\) is a permanent release
set and every abstract survival and crossing cut holds through \(Q_m\).
Its cost on this range is

\[
 |E|Q_m=O\left(\frac{W\log m}{m}\right)=o(W),
 \tag{7.16}
\]

because all the relevant floors equal one. \(\square\)

The coefficient may be made explicit without diagonal notation.  With

\[
 Q_m^*=\left\lfloor
  \frac12\log_2m-2\log_2\log_2m
 \right\rfloor,
 \tag{7.17}
\]

one has

\[
 4^{Q_m^*}\le\frac{m}{(\log_2m)^4},
 \qquad
 4(Q_m^*)^2 4^{Q_m^*}\le\frac{m}{(\log_2m)^2}<m
 \tag{7.18}
\]

for all sufficiently large \(m\).  Thus the same proof reaches \(Q_m^*\),
which is \((1/2-o(1))\log_2m\).

This logarithmic propagation is still far shorter than the required
fixed Gaussian window \(A\sqrt m\).  The threshold proof is deliberately
uniform over every high-set geometry; once \(q\) is larger, the exact
quantity \(h_{q-1}\) exceeds this universal small-family certificate, and
new structure rather than the same two-case estimate is needed.

## 8. The exact depth-two cut for the natural cycle child

The abstract rerouting theorem should not be confused with the child
suggested by the displayed Johnson cycle itself.  Retain the orientation
\(\phi(X_i)=S_i\) and define

\[
 \psi_2(X_i)=S_i\cap S_{i+1}\in V_2.
 \tag{8.1}
\]

The two lower colours are distinct facets of \(X_i\), so (8.1) really has
rank \(m-2\) and is a child of \(\phi(X_i)\).  Put

\[
 h(T)=|\{i:\psi_2(X_i)=T\}|.
 \tag{8.2}
\]

Let \(H_1\) be the image of an omitted-owner SDR, and let
\(H_2\subseteq V_2\) have the forced balanced cardinality

\[
 |H_2|=\rho_2=W-N_2.
 \tag{8.3}
\]

For \(m\ge8\), the original floors at depths one and two are both one.
If the core owners are frozen to \(\phi,\psi_2\), then the released-child
demand is exactly

\[
 r_2(T)=1+\mathbf1_{H_2}(T)-h(T),
 \tag{8.4}
\]

whereas the released-parent supply is one copy at each member of \(H_1\).
Consequently the natural child extends through depth two if and only if

\[
 \boxed{h(T)\le1+\mathbf1_{H_2}(T)
 \quad(T\in V_2),}
 \tag{8.5}
\]

and

\[
 \boxed{
 |H_1\cap N(\mathcal A)|
 \ge |\mathcal A|+|H_2\cap\mathcal A|-h(\mathcal A)
 \quad(\mathcal A\subseteq V_2).
 }
 \tag{8.6}
\]

Indeed, (8.5) is precisely nonnegativity of every residual child demand.
After cloning each child \(T\) exactly \(r_2(T)\) times, Hall's theorem is
exactly (8.6).  Total supply and demand agree because

\[
 \sum_T r_2(T)=N_2+\rho_2-N_1=W-N_1=d=|H_1|.
 \tag{8.7}
\]

Thus a colour with \(h(T)\ge3\) is an immediate singleton survival
failure, while any violation of (8.6) is the first exact crossing cut.
The saturating-cycle theorem controls neither (8.5) nor (8.6).  No such
failure is asserted to occur for every possible saturating cycle; the
point is that Theorem 7.1 proves its positive result by replacing
\(\psi_2\), not by verifying these natural cyclic-packet cuts.

## 9. Adversarial scope audit

1. **The old depth-one obstruction is invalid.**  The generic biregular
   estimate
   \(m|\mathcal A|\le(m+2)|\partial\mathcal A|\) ignores the two cycle
   neighbours already known to lie outside \(E\).  Subtracting those two
   possible receivers gives the sharp cap \(d_E(S)\le m\), which proves
   Hall exactly.

2. **Every propagated depth uses abstract rerouting.**  The Gale flow is
   free to choose the child of every core owner below its current abstract
   target.  It is not forced to use a same-start child from a pre-existing
   cyclic wreath row.

3. **The saturating cycle is not an exact wreath factor.**  A general
   Johnson cycle has length \(N_1\), not a certified decomposition into
   length-\(n\) tight zero-voltage trajectories.  Theorem 18 supplies no
   maps \(\Gamma_q\) having literal cyclic-packet meaning for \(q\ge2\).
   Therefore the phrase "use its omitted owners as the release set in
   \(\mathrm{MR}_A\)" is not yet formally meaningful until a tight lift is
   constructed.

4. **No fixed-window conclusion is claimed.**  In the abstract Boolean
   model, the proof reaches only
   \((1/2-\varepsilon)\log_2m\), not
   \(\lceil A\sqrt m\rceil\).  It does not construct a single permanent
   release profile relative to one exact factor.

5. **The first natural cyclic statistic remains uncontrolled.**  Its exact
   survival and crossing systems are (8.5)--(8.6).  The
   saturating-cycle theorem asserts neither.  Theorem 7.1 avoids them by
   rerouting abstractly, so it cannot be cited as a cyclic-packet
   completion.

The exact proved boundary is therefore:

\[
 \boxed{
 \text{The omitted set closes Hall at }q=1\text{ and admits an abstract
 balanced continuation through }(1/2-o(1))\log_2m;
 }
\]

\[
 \boxed{
 \text{literal tight flags and the cuts beyond logarithmic depth up to }
 A\sqrt m
 \text{ remain unproved.}
 }
\]
