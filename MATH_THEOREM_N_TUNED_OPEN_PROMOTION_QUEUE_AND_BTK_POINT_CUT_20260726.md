# Tuned open promotion queues and the canonical-BTK point cut

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\]

and tune

\[
 q_0=\lceil m^{1/4}\rceil,
 \qquad
 H=\left\lfloor\sqrt{m\log m}\right\rfloor,
 \qquad
 M=m+H.
\tag{0.1}
\]

There are two sharply different conclusions.

### A. Promotion rings pass every present open-path queue cut

There is an exact formal queue path system with one path for every
rank-\(M\) top and exactly \(N_{q_0}\) retained states. Its number of
paths is

\[
 \boxed{
 p=N_H=(1+o(1))\frac Wm=o(W/H).}
\tag{0.2}
\]

Every internal edge is a promotion at cache slot \(H\), hence is late
relative to \(q_0\). Simultaneously for every \(q\le H\), the entrance
blocks obey the exact queue shift

\[
 B_{i-q}^{(q)}=A_i^{(q)}.
\tag{0.3}
\]

After opening each ring along one contiguous gap, the aggregate queue
and tail-context discrepancies obey

\[
 \frac12\sum_C|a_C-b_C|le q_0N_H
   =(1+o(1))\frac{W}{m^{3/4}},
\tag{0.4}
\]

\[
 \frac12\sum_\kappa|O_\kappa-I_\kappa|le N_H
   =(1+o(1))\frac Wm.
\tag{0.5}
\]

The gaps can moreover be rotated so that the selected owner-occurrence
point margins satisfy

\[
 \boxed{
 \sum_{x=1}^{2m}|2M_x-N_{q_0}|=O(W/m).}
\tag{0.6}
\]

The exact clipped radius census can be placed monotonically on these
paths, and every threshold-run cut is then satisfied.

This is a formal within-top queue factor, not yet an exact middle-owner
factor. The unresolved gate is a correlated integral choice of the top
frames and gap phases which simultaneously gives owner simplicity and
\(o(W)\) aggregate target holes at every depth. Thus promotion rings are
not obstructed by the queue or antipode cuts, but coefficient one is not
proved.

### B. Canonical BTK is ruled out by its owner point margins

Retain the chains of the standard BTK SCD having native radius at least
\(q_0\), and use their native lower and upper entrance flags. Every
owner-simple exact-entrance bridge-one path cover of these states obeys

\[
 \boxed{
 p\ge
 \left(\frac2{\sqrt\pi}+o(1)\right)\frac W{\sqrt m}.}
\tag{0.7}
\]

Equivalently,

\[
 \boxed{
 \frac{p}{W/H}
 \ge
 \left(\frac2{\sqrt\pi}+o(1)\right)\sqrt{\log m}
 \longrightarrow\infty.}
\tag{0.8}
\]

This is stronger than the earlier monotone-radius bound
\((\sqrt{2/e}+o(1))W/\sqrt m\). It permits arbitrary entrance
orderings, arbitrary short-chain extensions, late promotions, and
nonmonotone native-radius changes. It uses only the fixed canonical BTK
owner set and its exact native entrance bijections.

In particular, canonical BTK cannot have
\(O(Wm^{-1}(\log m)^C)\) paths for any fixed \(C\). The obstruction can
be escaped only by changing the selected owner/provider system, for
example through a second SCD or noncanonical middle corners.

## 1. Tuned scalar ledger

Write

\[
 R=N_H,\qquad N=N_{q_0},\qquad T=MR,
 \qquad D=T-N.
\tag{1.1}
\]

The elementary product

\[
 \frac W{N_q}=\prod_{j=1}^q\frac{m+j}{m-j+1}
\tag{1.2}
\]

gives, uniformly for \(q\le H\),

\[
 \log\frac W{N_q}
 =\frac{q^2}{m}
 +O\!\left(\frac{q^2}{m^2}+\frac{q^4}{m^3}\right).
\tag{1.3}
\]

Consequently

\[
 \frac NW
 =1-m^{-1/2}+O(m^{-3/4}),
\tag{1.4}
\]

\[
 R=(1+o(1))\frac Wm,
 \qquad T\ge W>N,
 \qquad D=O\!\left(W\sqrt{\frac{\log m}{m}}\right)=o(W).
\tag{1.5}
\]

For the exact gap scale, put

\[
 \vartheta=\sqrt{m\log m}-H\in[0,1).
\]

Equation (1.3), with its displayed error, gives

\[
 \frac W{N_H}
 =m-2\vartheta\sqrt{m\log m}+o(\sqrt m),
\tag{1.6}
\]

and hence

\[
 \boxed{
 \frac DR
 =H+2\vartheta\sqrt{m\log m}+\sqrt m+o(\sqrt m).}
\tag{1.7}
\]

In particular, for all sufficiently large \(m\),

\[
 H< D/R=O(H),
 \qquad
 R<N<MR.
\tag{1.8}
\]

Finally,

\[
 \frac{R}{W/H}
 =\frac{H}{W/N_H}
 =(1+o(1))\frac Hm\longrightarrow0,
 \qquad
 2HR=o(W).
\tag{1.9}
\]

All floor effects used below are therefore explicit.

## 2. The full-top promotion ring

Fix a top \(U\in\binom{[2m]}M\) and an oriented cyclic frame

\[
 U=(c_0,c_1,\ldots,c_{M-1}),
\]

with indices modulo \(M\). Use the phase orientation \(i\to i-1\), and
put

\[
 X_i
 =U\setminus\{c_{i+H},c_{i+H+1},\ldots,c_{i+2H-1}\}.
\tag{2.1}
\]

Thus \(|X_i|=m\), and

\[
 X_{i-1}=X_i-c_{i+H-1}+c_{i+2H-1}.
\tag{2.2}
\]

The full ordered state has

\[
 \alpha_d(i)=c_{i+H-d},
 \qquad
 \beta_d(i)=c_{i+H+d-1},
 \qquad 1\le d\le H.
\tag{2.3}
\]

The arrival in (2.2) is \(c_{i+2H-1}=\beta_H(i)\). Hence every edge
is a promotion which evicts cache slot \(H\). Since \(q_0<H\), no edge
is an excluded early promotion.

For every \(1\le q\le H\), define the depth-\(q\) entrance blocks

\[
 A_i^{(q)}
 =\{c_{i+H-q},\ldots,c_{i+H-1}\},
\tag{2.4}
\]

\[
 B_i^{(q)}
 =\{c_{i+H},\ldots,c_{i+H+q-1}\}.
\tag{2.5}
\]

Then, exactly and simultaneously at all depths,

\[
 \boxed{B_{i-q}^{(q)}=A_i^{(q)}.}
\tag{2.6}
\]

The full lower contexts also telescope. If

\[
 P_i=(\alpha_1,\ldots,\alpha_{H-1})(i),
 \qquad
 S_i=(\alpha_2,\ldots,\alpha_H)(i),
\]

then

\[
 \boxed{S_i=P_{i-1}.}
\tag{2.7}
\]

Every projected tail key inherits the same identity.

## 3. Exact integer opening of all rings

Put

\[
 \ell=\left\lfloor\frac NR\right\rfloor,
 \qquad
 \rho=N-\ell R,
 \qquad 0\le\rho<R.
\tag{3.1}
\]

Retain \(\ell+1\) consecutive phases on exactly \(\rho\) tops and
\(\ell\) consecutive phases on the other \(R-\rho\) tops. The retained
phase count is exactly

\[
 \rho(\ell+1)+(R-\rho)\ell=N.
\tag{3.2}
\]

Equivalently, let

\[
 d=M-\ell=\left\lceil\frac DR\right\rceil.
\tag{3.3}
\]

The discarded gaps have length \(d-1\) on the first \(\rho\) tops and
length \(d\) on the others. By (1.7), for all sufficiently large \(m\),

\[
 H\le d-1\le d=O(H),
 \qquad
 \ell=m-O(H)\gg H.
\tag{3.4}
\]

Thus every retained and every discarded interval is nonempty, every
retained interval is one directed open path, and

\[
 \boxed{p=R=N_H.}
\tag{3.5}
\]

No cyclic closure is being imposed.

## 4. Exact queue and context histograms

Let \(J_U\) be the retained phase interval on one top, of length \(s_U\),
and let \(g_U=M-s_U\) be its gap. Before cancellations with other tops,
(2.6) gives

\[
 \frac12\sum_C
 \left|
 \sum_{i\in J_U}
 \bigl(
 1_{\{A_i^{(q)}=C\}}-1_{\{B_i^{(q)}=C\}}
 \bigr)
 \right|
 =\min\{q,s_U,g_U\}.
\tag{4.1}
\]

Indeed the \(B\)-histogram is the \(A\)-histogram of the phase interval
shifted by \(q\); cyclic \(q\)-intervals are distinct, and the half
symmetric difference of one cyclic interval and its \(q\)-shift is the
right side of (4.1).

By (3.4), \(s_U,g_U\ge H\). Hence (4.1) equals \(q\) for every
\(q\le H\). Summing and allowing cross-top cancellations gives

\[
 \boxed{
 \frac12\sum_C|a_C^{(q)}-b_C^{(q)}|
 \le qR
 \qquad(1\le q\le H).}
\tag{4.2}
\]

At \(q=q_0\), this is (0.4), with the exact factor required by the
open-path queue theorem.

Similarly, (2.7) pairs every internal edge of a retained interval. Only
one context remains on each shore, so

\[
 \boxed{
 \frac12\sum_w|O_w-I_w|\le R.}
\tag{4.3}
\]

Projection cannot increase total variation, proving (0.5) for every
refinement-independent tail key.

These endpoint discrepancies are precisely the open-path boundary term.
The literal antipode theorem applies to closed length-\(2m\) packets and
has no hypothesis here. Closing the retained paths is neither used nor
needed.

## 5. Exact clipped tag census and run cuts

Define

\[
 \gamma_j=N_j-N_{j+1}
 \quad(q_0\le j<H),
 \qquad
 \gamma_H=N_H=R.
\tag{5.1}
\]

Then

\[
 \sum_{j=q_0}^H\gamma_j=N_{q_0}=N.
\tag{5.2}
\]

Reserve one terminal state in every retained interval and tag it \(H\).
Distribute the remaining multiset of tags among the remaining states and
sort the tags nondecreasingly toward the reserved terminal state on each
path. This is always possible because (5.2) is the exact slot count.

For every \(q_0\le q\le H\), the tag-at-least-\(q\) states form one
terminal interval on each of the \(R\) paths and have total cardinality

\[
 \sum_{j=q}^H\gamma_j=N_q.
\tag{5.3}
\]

Consequently the number of internal tag-at-least-\(q\) edges is exactly

\[
 \boxed{e_q=N_q-R.}
\tag{5.4}
\]

In particular,

\[
 e_q-(2N_q-N-R)=N-N_q\ge0.
\tag{5.5}
\]

Thus the strongest zero-hole threshold-run demand is met at every depth.
This is an exact integral census statement. It does not assert global
injectivity of the target identities carried by those slots.

Promotions preserve the full top \(U\). Since every top has one tag-\(H\)
anchor, any promotion-only realization has at least \(R\) components.
Therefore (3.5) is optimal inside the promotion-only formal catalogue.

## 6. Point-balanced opening of the rings

The segment lengths alone do not balance the owner point margins, but the
gap positions can be chosen to do so without changing any preceding
count.

### Lemma 6.1 (almost-regular selection of the longer segments)

Among the complete family of rank-\(M\) tops, choose \(\rho\) tops so
that their coordinate degrees differ by at most one.

#### Proof

Choose a \(\rho\)-edge subfamily minimizing the sum of squared coordinate
degrees. If \(d_x\ge d_y+2\), some selected top contains \(x\) and not
\(y\) whose exchange \(x\mapsto y\) is not already selected. Otherwise
the exchange map injects all selected tops containing \(x\) and not
\(y\) into selected tops containing \(y\) and not \(x\), contradicting
\(d_x>d_y\). The available exchange lowers the squared-degree sum, a
contradiction. \(\square\)

Give the chosen tops gap length \(d-1\), and all other tops gap length
\(d\). Write the resulting gap length on top \(U\) as \(d_U\). For a
coordinate \(x\), put

\[
 S_x=\sum_{U\ni x}d_U.
\tag{6.1}
\]

Lemma 6.1 and coordinate transitivity give

\[
 S_x=\frac{MD}{2m}+O(1)
 \qquad(1\le x\le2m).
\tag{6.2}
\]

Fix arbitrary cyclic frames on the tops, and independently rotate each
gap uniformly around its ring. Let \(D_x\) be the number of discarded
owner occurrences containing \(x\). A coordinate in a fixed top belongs
to exactly \(m\) of its \(M\) ring owners, so

\[
 \mathbb E D_x=\frac mM S_x=\frac D2+O(1).
\tag{6.3}
\]

The contribution from top \(U\) lies in an interval of length at most
\(d_U\). Moreover

\[
 \sum_Ud_U^2\le dD=O(W\log m),
\tag{6.4}
\]

by \(d=O(H)\) and \(D=O(WH/m)\). Hoeffding's elementary exponential
moment argument therefore gives, with \(t=W/m^2\),

\[
 \Pr\bigl(|D_x-\mathbb ED_x|>t\bigr)
 \le2\exp\!\left(-\frac{2t^2}{dD}\right).
\tag{6.5}
\]

The right side is \(o(1/m)\), since \(W\) is exponential in \(m\).
A union bound over the \(2m\) coordinates proves the existence of gap
rotations satisfying

\[
 |D_x-D/2|\le W/m^2+O(1)
 \qquad(1\le x\le2m).
\tag{6.6}
\]

Across all full rings, every coordinate has exactly

\[
 m\binom{2m-1}{M-1}=\frac{MR}{2}
\tag{6.7}
\]

owner occurrences. Hence the retained occurrence count is

\[
 M_x=MR/2-D_x.
\]

Since \(N=MR-D\), (6.6) yields

\[
 |2M_x-N|=|D-2D_x|=O(W/m^2),
\]

and therefore

\[
 \boxed{
 \sum_x|2M_x-N|=O(W/m).}
\tag{6.8}
\]

Because \(q_0^2R=(1+o(1))W/\sqrt m\), equation (6.8) is
\(o(q_0^2R)\). Thus the point-margin queue cut places no intrinsic lower
bound above \(R\) on these opened rings.

This balancing is only at the owner-occurrence level. It has not been
made compatible with cross-top owner simplicity or all-depth target
injectivity.

## 7. Canonical BTK as a constrained bridge family

Encode an \(m\)-subset \(X\subset[2m]\) by a balanced word
\(w_1\cdots w_{2m}\), where \(w_t=1\) means \(t\in X\). Put

\[
 \xi_t=1-2w_t\in\{+1,-1\},
 \qquad
 S_j=\sum_{t=1}^j\xi_t.
\tag{7.1}
\]

Thus \(S_{2m}=0\). In canonical BTK bracketing, \(0\) is an opening
symbol and \(1\) a closing symbol. After all \(01\) pairs are removed,
the unmatched word is \(1^r0^r\), where \(r\) is the native radius of
the chain containing \(X\).

### Lemma 7.1 (radius is the negative prefix minimum)

For every balanced word,

\[
 \boxed{r=-\min_{0\le j\le2m}S_j.}
\tag{7.2}
\]

#### Proof

Scanning from left to right, a closing symbol \(1\) is unmatched exactly
when it takes the walk to a new negative record. Hence the number of
unmatched \(1\)'s is \(-\min_jS_j\). Balance forces the same number of
unmatched \(0\)'s. These are exactly the \(2r\) free positions of the
BTK chain. \(\square\)

Let \(\Omega\) be the retained owner set \(r\ge q_0\), and let
\(\mathcal E\) be its omitted complement. With

\[
 h=q_0-1,
\]

Lemma 7.1 gives the exact description

\[
 \boxed{
 \mathcal E={w:S_{2m}=0,\ \min_jS_j\ge-h\}.}
\tag{7.3}
\]

Reflection at the first visit to \(-q_0\) gives

\[
 |\Omega|=N_{q_0},
 \qquad
 E:=|\mathcal E|=W-N_{q_0}.
\tag{7.4}
\]

By (1.4),

\[
 \boxed{E=(1+o(1))\frac W{\sqrt m}.}
\tag{7.5}
\]

For each coordinate \(t\), let \(M_t\) count retained owners containing
\(t\), and let \(E_t\) count omitted owners containing \(t\). Since
exactly \(W/2\) balanced words contain a fixed coordinate,

\[
 M_t=W/2-E_t.
\]

Thus the selected-owner point margin is exactly

\[
 \boxed{
 D_t:=2M_t-N_{q_0}
 =E-2E_t
 =\sum_{w\in\mathcal E}\xi_t(w).}
\tag{7.6}
\]

The large point skew in (7.6) is invisible to the scalar owner count.

## 8. The midpoint excursion asymptotic

For nonnegative integers \(a,b\), let \(K_\ell(a,b)\) be the number of
nearest-neighbor length-\(\ell\) paths from height \(a\) to height \(b\)
which remain nonnegative. Reflection gives the exact formula

\[
 K_\ell(a,b)
 =\binom{\ell}{(\ell+b-a)/2}
 -\binom{\ell}{(\ell+b+a+2)/2},
\tag{8.1}
\]

where inadmissible binomial coefficients are zero.

Shift a bridge in \(\mathcal E\) upward by \(h\). At its midpoint the
shifted height is \(y=h+S_m\). Splitting at time \(m\) and reversing the
second half gives

\[
 \boxed{
 \Pr(h+S_m=y\mid\mathcal E)
 =\frac{K_m(h,y)^2}{K_{2m}(h,h)}.}
\tag{8.2}
\]

### Lemma 8.1 (midpoint height)

For \(h=q_0-1\),

\[
 \boxed{
 \mathbb E(S_m\mid\mathcal E)
 =\left(\frac2{\sqrt\pi}+o(1)\right)\sqrt m.}
\tag{8.3}
\]

#### Proof

Put \(y=x\sqrt m\), on the parity lattice allowed by (8.1). Uniformly
for \(x\) in a fixed compact subset of \((0,\infty)\), Stirling's
formula in (8.1), using \(h+1=q_0=o(\sqrt m)\), gives

\[
 K_m(h,y)
 =2^m\sqrt{\frac2{\pi m}}e^{-x^2/2}
 \left(
  \frac{2q_0x}{\sqrt m}
  +o\!\left(\frac{q_0}{\sqrt m}\right)
 \right).
\tag{8.4}
\]

The parity lattice has spacing \(2/\sqrt m\). Squaring (8.4) shows that
the normalized midpoint law converges to the density proportional to

\[
 x^2e^{-x^2}\,1_{\{x>0\}}.
\tag{8.5}
\]

For completeness, the domination needed to pass from compact intervals
to the whole half-line follows directly from the usual Stirling upper
bound for a binomial coefficient and the adjacent-ratio estimate in the
difference (8.1): for absolute constants \(c,C>0\),

\[
 K_m(h,y)
 \le
 C2^m m^{-1/2}e^{-c y^2/m}
 \min\!\left\{1,\frac{q_0(y+q_0)}m\right\}.
\tag{8.6}
\]

The right side squared is summable after multiplication by
\(1+y/\sqrt m\), uniformly in \(m\). Hence dominated Riemann summation is
valid. Since \(h/\sqrt m\to0\),

\[
 \frac{\mathbb E(S_m\mid\mathcal E)}{\sqrt m}
 \longrightarrow
 \frac{\int_0^\infty x^3e^{-x^2}\,dx}
      {\int_0^\infty x^2e^{-x^2}\,dx}
 =\frac{1/2}{\sqrt\pi/4}
 =\frac2{\sqrt\pi}.
\]

This proves (8.3). \(\square\)

The same calculation independently recovers

\[
 K_{2m}(h,h)
 =(1+o(1))W\frac{q_0^2}{m},
\]

which agrees with (7.4)--(7.5).

## 9. The decisive canonical-BTK queue cut

Choose signs

\[
 \varepsilon_t=
 \begin{cases}
  +1,&1\le t\le m,\\
  -1,&m<t\le2m.
 \end{cases}
\tag{9.1}
\]

Every balanced bridge has total increment zero. Therefore (7.6) gives

\[
\begin{aligned}
 \sum_{t=1}^{2m}\varepsilon_tD_t
 &=\sum_{w\in\mathcal E}
   \left(\sum_{t\le m}\xi_t-\sum_{t>m}\xi_t\right)\\
 &=2\sum_{w\in\mathcal E}S_m(w).
\end{aligned}
\tag{9.2}
\]

By Lemma 8.1 the last quantity is positive for all sufficiently large
\(m\). Equations (7.5), (8.3), and (9.2) imply

\[
\begin{aligned}
 \sum_{t=1}^{2m}|D_t|
 &\ge\sum_t\varepsilon_tD_t\\
 &=\left(\frac4{\sqrt\pi}+o(1)\right)W.
\end{aligned}
\tag{9.3}
\]

Now use the exact native BTK entrance flags. The retained chains map
bijectively to the lower rank \(m-q_0\) and to the upper rank \(m+q_0\),
and their middle owners are distinct. Hence the exact point-margin queue
inequality applies:

\[
 p\ge\frac1{2q_0^2}\sum_t|D_t|.
\tag{9.4}
\]

Since \(q_0^2=(1+o(1))\sqrt m\), (9.3)--(9.4) prove

\[
 \boxed{
 p\ge
 \left(\frac2{\sqrt\pi}+o(1)\right)\frac W{\sqrt m}.}
\tag{9.5}
\]

At the entrance-block level, if \(a_C,b_C\) are the canonical BTK
\(q_0\)-block histograms, exact entrance coverage gives

\[
 D_t=\sum_{C\ni t}(a_C-b_C).
\tag{9.6}
\]

Therefore

\[
 \boxed{
 \frac12\sum_C|a_C-b_C|
 \ge
 \frac1{2q_0}\sum_t|D_t|
 =\left(\frac2{\sqrt\pi}+o(1)\right)\frac W{m^{1/4}}.}
\tag{9.7}
\]

The open-path queue upper bound

\[
 \frac12\sum_C|a_C-b_C|\le q_0p
\]

is exactly what turns (9.7) into (9.5).

For comparison, the native-radius layer cut gives only

\[
 p\ge(\sqrt{2/e}+o(1))\frac W{\sqrt m}
\]

when every selected edge decreases radius. The point cut is stronger and
does not assume any direction of radius change.

## 10. Exact scope and final boundary

### Proved for promotion rings

1. exact integer opening into \(N_H\) nonempty paths and exactly
   \(N_{q_0}\) retained states;
2. exact simultaneous queue shifts through every \(q\le H\);
3. queue discrepancy \(q_0N_H\) and tail-context discrepancy \(N_H\);
4. an exact integral clipped tag census satisfying every threshold-run
   count;
5. existence of gap phases with aggregate owner point discrepancy
   \(O(W/m)\); and
6. literal internal Johnson chronology, with reset cost
   \(2HN_H=o(W)\).

### Not proved for promotion rings

1. a common integral choice of top frames and gaps with owner collision
   excess \(o(W)\);
2. lower and upper entrance target bijections;
3. aggregate all-depth target holes \(o(W)\); or
4. compatibility of those three conditions with the point-balanced gap
   rotations.

Independent frame choices are not enough: at the tight entrance layer
their mean load is \(1+o(1)\), and a fixed target is missed with
probability \(e^{-1}+o(1)\). The remaining problem is the correlated
vertical-frame rounding theorem, not a queue, antipode, scalar-capacity,
or component-count obstruction.

### Proved for canonical BTK

The lower bound (9.5) holds for every owner-simple bridge-one path cover
which retains exactly the canonical radius-at-least-\(q_0\) BTK middle
owners and their native lower and upper entrance flags. It is unaffected
by

* the \(q_0!^2\) entrance ordering freedom;
* arbitrary extensions of native chains shorter than \(H\);
* arbitrary late promotions or genuine rotors; and
* horizontal or radius-increasing transitions.

It does not apply after replacing the canonical upper provider, changing
the middle owner selected between the two entrance endpoints, mixing two
SCDs, or admitting a material owner collision/leave correction. Those
operations change the point-margin vector in (7.6).

Thus the tuned open-path verdict is exact:

\[
 \boxed{
 \begin{array}{ll}
 \text{promotion rings:}
 &p=N_H\sim W/m\text{ is compatible with all present queue cuts,}\\[1mm]
 \text{canonical BTK:}
 &p\ge(2/\sqrt\pi+o(1))W/\sqrt m
   =\omega(W/H).
 \end{array}}
\]

The promotion catalogue survives, conditionally on its integral
cross-top frame theorem. The canonical BTK catalogue is closed at the
requested scale by the midpoint-excursion point-margin cut.
