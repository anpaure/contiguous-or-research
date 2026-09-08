# Anchored two-sector transport: optimized joint flux, an exact balanced SCD coupling, and the Monge-fork obstruction

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 H=\max\{h:W/N_h\le m+h\},
\]

\[
 M=m+H,\qquad N=N_H,\qquad T=MN=W+o(W).
\tag{0.1}
\]

Write \(E=T-W\ge0\).

Fix a coordinate \(x\). This note continues the exceptional
targetwise, history-closed alignment gate left by
MATH_THEOREM_W_ANCHORED_TWO_ORBIT_PAIRED_QUOTIENT_STATEWISE_GATE_20260726.md.

The exact conclusions are as follows.

1. The earlier statewise spill cut can be optimized over its whole
   positive range. If \(h_q\) is the common signed hole count and
   \(G_q(x)\) is the number of active exterior \(x\)-bridge histories,
   then every owner-preserving, arbitrarily correlated common-history
   construction satisfies

   \[
   \boxed{
   {D_{\rm deep}\over2}
   +\sum_{q=q_0}^{Q_*}G_q(x)
   \ge
   \left({1-\log2\over4}+o(1)\right)W,}
   \tag{0.2}
   \]

   where

   \[
   q_0=\lceil m^{1/4}\rceil,\qquad
   Q_*=\max\{q:N_q>T/2\},
   \qquad {Q_*\over\sqrt m}\to\sqrt{\log2},
   \tag{0.3}
   \]

   and \(D_{\rm deep}=2\sum_{q=q_0}^Hh_q\). Complete suppression of
   exterior histories therefore forces

   \[
   D_{\rm deep}\ge
   \left({1-\log2\over2}+o(1)\right)W
   =(0.1534\ldots+o(1))W.
   \tag{0.4}
   \]

2. Common history makes the \(G_q\)'s interval-residence loads. If
   \(K_x\) is the number of distinct exterior histories meeting the
   controlled range, then exactly

   \[
   {D_{\rm deep}\over2}
   \ge
   \sum_{q=q_0}^{Q_*}
   \left(
      {q\over m}\left(N_q-{T\over2}\right)-K_x
   \right)_+.
   \tag{0.5}
   \]

   Consequently \(D_{\rm deep}=o(W)\) forces

   \[
   \boxed{
   K_x\ge(\gamma-o(1)){W\over\sqrt m},}
   \tag{0.6}
   \]

   where

   \[
   \gamma=
   \max_{0<t<\sqrt{\log2}}
       t\left(e^{-t^2}-{1\over2}\right)>0.
   \tag{0.7}
   \]

   The unique maximizer \(t_*\) satisfies

   \[
   e^{-t_*^2}(1-2t_*^2)={1\over2}.
   \tag{0.8}
   \]

   Thus the earlier \(\Omega(W/H)\) statement strengthens to the sharp
   scale \(\Omega(W/\sqrt m)\) for distinct exterior histories.

3. No universal targetwise/common-history defect obstruction exists.
   There is an explicit integral full SCD of \(B_{2m}\) whose middle
   owners and both signed projections are bijective at every depth,
   whose common tags are exact, and for which

   \[
   D_{\rm deep}=0,\qquad
   \left|G_q(x)-{q\over2m}N_q\right|\le1
   \quad(1\le q\le m).
   \tag{0.9}
   \]

   A biased version attains equality in the original statewise cut
   simultaneously for every
   \(q\le\lfloor\sqrt m/2\rfloor\):

   \[
   I_q(x)=qR_0,\qquad
   G_q(x)={q\over m}\left(N_q-{T\over2}\right),
   \qquad h_q=0,
   \tag{0.10}
   \]

   where \(R_0=T/(2m)\). Hence target identities, owner uniqueness,
   common tags, and the paired quotient condition alone do not force
   positive defect.

4. Every chain in these product SCDs is individually a literal
   promotion history. The balanced product SCD nevertheless cannot be
   injected history-for-history into an exact promotion factor. Its short
   chains cannot presently be bundled into the remaining phases of the
   one cyclic frame already fixed at each depth-\(H\) root. In fact the
   balanced SCD uses \(\Theta(W)\) distinct internal histories, whereas
   the anchored physical catalogue has only

   \[
   HR_0=O\left({H\over m}W\right)=o(W)
   \tag{0.11}
   \]

   internal phase slots. A local three-window triangle obstruction also
   rules out the naive plan of putting one product-SCD block into one
   ring. The surviving positive problem is therefore a genuinely
   nonlocal common-frame rethreading/factorization.

5. Ordinary monotone transport does not construct that factorization.
   On any fixed signed layer all targets have equal rank, so Boolean
   inclusion monotonicity reduces to equality. On the coarse signature
   quotient a monotone coupling exists, but it forgets every literal
   target. The exact transport of preassembled complete histories is a
   capacitated Hall problem; unassembled layer holes instead give the
   original configuration-hypergraph/Farkas gate.

6. The direct fixed-donor two-history Monge plan is rigorously
   impossible at coefficient one. If every exterior history is assigned one
   \({\cal A}_1\) donor with the same upper trace throughout its spill
   interval, then

   \[
   \boxed{
   D_{\rm deep}
   +\sum_{q=q_0}^{Q_*}(K_q+R_q)
   \ge
   \left({1-\log2\over4}+o(1)\right)W,}
   \tag{0.12}
   \]

   where \(K_q\) is donor-lower multiplicity excess and \(R_q\) counts
   nonlocal lower repairs. Thus a lower-simple, target-closed Monge
   coupling has linear defect, while every successful \(o(W)\)-defect
   coupling within this architecture needs \(\Omega(W)\)
   coalescence/rectangle-repair incidences.

No constant-one theorem is claimed. The advance is a precise
separation: the complete target-history relaxation has an exact
zero-defect integral solution, while the simplest literal monotone
coupling fails linearly. What remains is exactly nonlocal compression
of the SCD-like histories into owner-simple common cyclic frames.

## 1. Anchored signatures and complete histories

Let

\[
 k=m-H,\qquad
 {\cal A}_1=\{A\in\tbinom{[2m]}k:x\in A\},\qquad
 {\cal A}_0=\{A\in\tbinom{[2m]}k:x\notin A\}.
\tag{1.1}
\]

Their sizes are

\[
 R_1={k\over2m}N,\qquad
 R_0={M\over2m}N={T\over2m}.
\tag{1.2}
\]

For a phase occurrence \(e\), write

\[
 L_q(e)\subset X(e)\subset U_q(e)
\tag{1.3}
\]

for its lower, middle, and upper traces, of ranks \(m-q,m,m+q\).
At a fixed coordinate \(x\), the only possible signatures are

\[
 11,\qquad 01,\qquad 00.
\tag{1.4}
\]

An internal bridge has \(x\in X\setminus L_q\); an exterior bridge has
\(x\in U_q\setminus X\). Let

\[
 I_q(x),\qquad G_q(x)
\tag{1.5}
\]

be their selected counts. If the paired image has common size
\(N_q-h_q\), the exact bridge identity gives

\[
 I_q(x)+G_q(x)
 ={q\over m}N_q-h_q^+(x)+h_q^-(x),
\tag{1.6}
\]

and hence

\[
 \left|I_q(x)+G_q(x)-{q\over m}N_q\right|\le h_q.
\tag{1.7}
\]

There are exactly \(qR_0=qT/(2m)\) raw internal bridge slots at depth
\(q\). Therefore every correlated physical construction satisfies

\[
 \boxed{
 h_q+G_q(x)\ge
 \alpha_q:=
 {q\over m}\left(N_q-{T\over2}\right)_+.}
\tag{1.8}
\]

A complete exterior history \(e\) has a first-entry depth \(s(e)\) and
a common stopping depth \(d(e)\). Thus

\[
 \boxed{
 G_q(x)=
 |\{e:s(e)\le q\le d(e)\}|.}
\tag{1.9}
\]

This interval law is the only extra information supplied by common
tags at the anchored-signature level.

## 2. The optimized joint defect--exterior-flux theorem

### Theorem 2.1

For every sufficiently large \(m\), every owner-preserving,
arbitrarily correlated common-history family satisfies (0.2).

#### Proof

By definition of \(Q_*\), the positive part in (1.8) may be removed for
\(q\le Q_*\). Summing (1.8) gives

\[
 {D_{\rm deep}\over2}
 +\sum_{q=q_0}^{Q_*}G_q(x)
 \ge
 \sum_{q=q_0}^{Q_*}
 {q\over m}\left(N_q-{T\over2}\right).
\tag{2.1}
\]

Uniformly for \(q=O(\sqrt m)\),

\[
 {N_q\over W}
 =\exp(-q^2/m+o(1)),
\qquad {T\over W}=1+o(1).
\tag{2.2}
\]

Consequently

\[
 {Q_*\over\sqrt m}\longrightarrow\sqrt{\log2}.
\tag{2.3}
\]

Also \(Q_*+1\le H\) for all sufficiently large \(m\): adjacent
Gaussian-layer ratios tend to one here, so
\(N_{Q_*+1}=(1/2+o(1))W\), whence
\(W/N_{Q_*+1}=O(1)<m+Q_*+1\). Thus every depth used below lies inside
the calibrated range.

With \(s=\sqrt{\log2}\), the first half of the sum in (2.1) is

\[
 \sum_{q=q_0}^{Q_*}{q\over m}N_q
 =
 \left(\int_0^s te^{-t^2}\,dt+o(1)\right)W
 =
 \left({1\over4}+o(1)\right)W,
\tag{2.4}
\]

while the second half is

\[
 \sum_{q=q_0}^{Q_*}{qT\over2m}
 =
 \left({s^2\over4}+o(1)\right)W
 =
 \left({\log2\over4}+o(1)\right)W.
\tag{2.5}
\]

Subtracting proves (0.2). If every exterior history is suppressed,
\(\sum_qG_q=0\), and multiplying by two gives (0.4).
\(\square\)

The coefficient \((1-\log2)/4\) is the exact anchored-signature
transport mass. It charges required exterior residence, not collision
energy. A positive construction is allowed to pay it through \(G_q\);
therefore (0.2) alone is not a constant-one obstruction.

### Theorem 2.2 (integral sharpness in the signature/history quotient)

At the level of the exact fixed-\(x\) signature census, including the
raw internal/exterior threshold multiplicities and one common stopping
tag per selected slot, inequality (0.2) is sharp. There is an integral
common-tag assignment with zero formal signature deficiency
\(h_q^{\rm sig}\), namely

\[
 h_q^{\rm sig}=0,\qquad
 I_q=\min\left\{{q\over m}N_q,{qT\over2m}\right\},
\tag{2.6}
\]

\[
 G_q=
 {q\over m}\left(N_q-{T\over2}\right)_+,
\tag{2.7}
\]

and exact pure-signature counts

\[
 11_q=00_q={m-q\over2m}N_q.
\tag{2.8}
\]

At the middle rank it selects exactly \(W/2\) slots in either
\(x\)-sector, leaving exactly \(E/2\) vacancies in either sector.
Consequently

\[
 \sum_q(h_q^{\rm sig}+G_q)
 =
 \left({1-\log2\over4}+o(1)\right)W.
\tag{2.9}
\]

This theorem imposes no literal target identities, middle-owner
injectivity, prescribed tag-\(H\) root anchors, or repeated phase
profile.

#### Proof

Put

\[
 b_q={q\over m}N_q,\qquad
 c_q={qT\over2m}=qR_0.
\]

For each entrance threshold \(a\), the raw anchored catalogue has
exactly \(R_0\) internal and \(R_0\) exterior slots. A slot stopped at
depth \(d\ge a\) contributes the residence interval \([a,d]\).

The internal sequence \(I_q=\min(b_q,c_q)\) grows by exactly \(R_0\)
per depth until the crossover \(N_q=T/2\). The crossover lies after
the maximum of \(qN_q\), so thereafter \(I_q=b_q\) is decreasing. The
one boundary increase is at most \(R_0\). For the exterior sequence,
whenever it increases,

\[
 G_q-G_{q-1}
 =(b_q-b_{q-1})-R_0\le R_0.
\tag{2.10}
\]

Indeed

\[
 b_q-b_{q-1}\le {N_q\over m}\le {T\over m}=2R_0;
\]

the first inequality follows from
\[
 {N_q\over N_{q-1}}={m-q+1\over m+q}.
\]

Thus the standard greedy interval decomposition realizes both integer
bridge-load sequences. More explicitly, put \(I_0=G_0=0\) and

\[
 s_q^I=(I_q-I_{q-1})_+,
 \qquad
 s_q^G=(G_q-G_{q-1})_+.
\tag{2.10a}
\]

For the internal sequence, \(s_q^I\le R_0\): before the crossover
\(I_q=c_q\), and after the crossover \(qN_q\) is already decreasing.
For the exterior sequence this follows from (2.10). Start exactly
\(s_q^I\), respectively \(s_q^G\), histories at entrance threshold
\(q\), and whenever the load decreases stop the required number of
active bridge histories. This gives integral bridge intervals with
the prescribed loads.

It remains to fill the pure signatures. Put

\[
 u_q^-={m-q\over2m}N_q.
\]

It is useful also to put

\[
 u_q^+={m+q\over2m}N_q=u_q^-+b_q.
\tag{2.10b}
\]

The exact recursion

\[
 u_{q-1}^--u_q^-={q\over m}N_q=b_q
\tag{2.11}
\]

matches the number of histories which either enter a bridge state or
stop at threshold \(q\).

We must still check that the already prescribed bridge starters can
coexist with the pure filler. Do this separately in the internal and
exterior middle sectors. Write \(s_q\) for the corresponding sequence
in (2.10a), and reserve every selected threshold-\(a\) bridge starter
as a pure active history at all depths before \(a\). At depth \(q\)
the number of such future starters is

\[
 S_q=\sum_{a>q}s_a.
\tag{2.11a}
\]

All starts occur by \(Q_*+1=O(\sqrt m)\), and \(s_a\le R_0\). Hence
\(S_q=O(\sqrt m R_0)=o(W)\). Uniformly while \(S_q\ne0\),
\(q\le Q_*\) and \(u_q^-\ge(1/4-o(1))W\), so \(S_q\le u_q^-\) for all
sufficiently large \(m\). After the last start this inequality is
trivial. Moreover every nonzero starter obeys
\(s_q\le R_0\le b_q\), and therefore the residual pure demand

\[
 r_q=u_q^- - S_q
\tag{2.11b}
\]

is nonincreasing, since

\[
 r_{q-1}-r_q
 =(u_{q-1}^--u_q^-)-(S_{q-1}-S_q)
 =b_q-s_q\ge0.
\tag{2.11c}
\]

The residual eligibility graph is Ferrers: a raw pure slot whose
bridge threshold is \(a\) may receive any stopping endpoint before
\(a\). After reserving the \(S_q\) future starters, the residual raw
capacity at depth \(q\) is

\[
 v_q-S_q,
 \qquad
 v_q={T\over2}-qR_0={m-q\over2m}T.
\tag{2.12}
\]

The nested Hall inequalities are exactly

\[
 r_q\le v_q-S_q.
\]

After cancelling \(S_q\), these reduce to \(u_q^-\le v_q\), which
follows from \(N_q\le T\). Ferrers incidence has the consecutive-ones
property and is totally unimodular, so the residual filler is integral.

For completeness, the resulting total active counts in the two middle
sectors are

\[
 C_q=u_q^-+I_q,
 \qquad A_q=u_q^-+G_q.
\tag{2.12a}
\]

Before the crossover these equal \(u_q^-+c_q\) and \(u_q^+-c_q\);
after it they equal \(u_q^+\) and \(u_q^-\). Each is nonincreasing
(the boundary step follows directly from (2.11)), so the assigned
endpoints are common stopping tags, not merely layerwise fillers. Also
\(C_q+A_q=2u_q^-+b_q=N_q\), so their common active cardinality is
exact. At
depth zero each raw sector has \(T/2\) slots; choosing \(W/2\) gives
the claimed \(E/2\) vacancies. Equations (2.6)--(2.8) follow.

Finally, summing (2.7) and applying the calculation in
(2.4)--(2.5) proves (2.9). \(\square\)

Theorem 2.2 proves that common stopping tags and the exact anchored
signature capacities add no transport premium. All remaining
difficulty is targetwise and ownerwise. Moreover the exterior sequence
in (2.7) has, up to \(o(W/\sqrt m)\), one increasing and one decreasing
part, with maximum

\[
 \max_qG_q=(\gamma+o(1)){W\over\sqrt m}.
\]

The greedy interval decomposition therefore uses
\((\gamma+o(1))W/\sqrt m\) distinct exterior slots. Thus the constant
in (0.6) is attained in the integral signature/history quotient.

## 3. Joint residence and the number of distinct exterior histories

Let \(K_x\) be the number of distinct exterior histories contributing
at least once in \([q_0,Q_*]\).

### Theorem 3.1

Every common-history construction satisfies the exact finite inequality

\[
 {D_{\rm deep}\over2}
 \ge
 \sum_{q=q_0}^{Q_*}(\alpha_q-K_x)_+.
\tag{3.1}
\]

If

\[
 K_x=\left(\kappa+o(1)\right){W\over\sqrt m},
\tag{3.2}
\]

then

\[
 \liminf_{m\to\infty}{D_{\rm deep}\over2W}
 \ge
 J(\kappa):=
 \int_0^{\sqrt{\log2}}
 \left[
 t\left(e^{-t^2}-{1\over2}\right)-\kappa
 \right]_+dt.
\tag{3.3}
\]

In particular, \(D_{\rm deep}=o(W)\) implies (0.6).

#### Proof

At every depth \(q\), (1.9) gives \(G_q(x)\le K_x\). Equation (1.8)
therefore implies

\[
 h_q\ge(\alpha_q-K_x)_+.
\]

Summing proves (3.1). Under (3.2), put \(q=t\sqrt m\). Uniformly on the
displayed compact interval,

\[
 \alpha_q={W\over\sqrt m}
 t\left(e^{-t^2}-{1\over2}\right)
+o(W/\sqrt m).
\]

The Riemann sum gives (3.3).

The function

\[
 f(t)=t(e^{-t^2}-1/2)
\]

has derivative

\[
 f'(t)=e^{-t^2}(1-2t^2)-1/2.
\]

The first term is strictly decreasing on
\([0,\sqrt{\log2}]\), since its derivative is
\(-2te^{-t^2}(3-2t^2)<0\). It starts above \(1/2\) and ends below it.
Hence (0.8) has one solution, and \(f\) has the unique maximum
\(\gamma\). If \(\kappa<\gamma\), then \(J(\kappa)>0\). Thus
\(D_{\rm deep}=o(W)\) forces
\(\kappa\ge\gamma\), proving (0.6). \(\square\)

Under middle-owner injectivity, the \(K_x\) histories in (0.6) have
distinct owner-avoiding middle owners. The theorem is a demand, not a
contradiction: \(K_x=o(W)\).

## 4. An exact integral zero-defect target-history coupling

The next theorem shows that no statewise lower bound can force positive
deep defect once arbitrary complete symmetric-chain histories are
allowed.

Fix a second coordinate \(y\ne x\), and put

\[
 Z=[2m]\setminus\{x,y\}.
\]

Take any SCD of \(B_Z\). A base chain of half-length \(\tau\) has the
form

\[
 C_0\subset C_1\subset\cdots\subset C_{2\tau},
 \qquad |C_i|=m-1-\tau+i.
\tag{4.1}
\]

### 4.1 The two product shores

For \(\tau\ge1\), define the following four \(U\)-chains:

\[
\begin{aligned}
U_0:\;&C_0\subset\cdots\subset C_{2\tau}
       \subset C_{2\tau}x\subset C_{2\tau}xy,\\
U_1:\;&C_0x\subset\cdots\subset C_{2\tau-1}x
       \subset C_{2\tau-1}xy,\\
U_2:\;&C_0xy\subset\cdots\subset C_{2\tau-2}xy,\\
U_3:\;&C_0y\subset\cdots\subset C_{2\tau}y.
\end{aligned}
\tag{4.2}
\]

Define the four \(L\)-chains:

\[
\begin{aligned}
L_0:\;&C_0\subset C_0x\subset C_0xy
       \subset C_1xy\subset\cdots\subset C_{2\tau}xy,\\
L_1:\;&C_1\subset C_1x\subset C_2x
       \subset\cdots\subset C_{2\tau}x,\\
L_2:\;&C_2\subset\cdots\subset C_{2\tau},\\
L_3:\;&C_0y\subset\cdots\subset C_{2\tau}y.
\end{aligned}
\tag{4.3}
\]

Empty chains are omitted. For \(\tau=0\), use

\[
 U:\quad C_0\subset C_0y\subset C_0xy,
 \qquad C_0x,
\tag{4.4}
\]

or

\[
 L:\quad C_0\subset C_0x\subset C_0xy,
 \qquad C_0y.
\tag{4.5}
\]

### Lemma 4.1

Each of (4.2) and (4.3) partitions

\[
 \{C_0,\ldots,C_{2\tau}\}\times B_{\{x,y\}}
\]

into symmetric chains of \(B_{2m}\).

#### Proof

In (4.2), the \(x,y\)-states on the four chains are respectively

\[
 0\to x\to xy,\qquad x\to xy,\qquad xy,\qquad y.
\]

They use every pair \((C_i,S)\) exactly once. The endpoint-rank pairs
are

\[
 (m-1-\tau,m+1+\tau),\quad
 (m-\tau,m+\tau),\quad
 (m+1-\tau,m-1+\tau),\quad
 (m-\tau,m+\tau),
\]

and each sums to \(2m\). The verification for (4.3) is identical; its
four state patterns are

\[
 0\to x\to xy,\qquad 0\to x,\qquad0,\qquad y.
\]

Equations (4.4)--(4.5) are the \(\tau=0\) versions. \(\square\)

### Lemma 4.2 (local bridge ledger)

A \(U\)-block contributes exactly one exterior \(x\)-bridge at depth
\(\tau\) and one at depth \(\tau+1\). An \(L\)-block contributes
exactly one internal \(x\)-bridge at each of those depths. At
\(\tau=0\), there is the corresponding single bridge at depth \(1\).

#### Proof

In \(U_0\), the middle set avoids \(x\), while \(x\) first appears at
upper depth \(\tau\) and remains present at depth \(\tau+1\). Every
other \(U\)-chain either contains \(x\) throughout or avoids it
throughout.

In \(L_1\), the middle contains \(x\), while its depth-\(\tau\) lower
set does not. In \(L_0\), the analogous loss occurs only at depth
\(\tau+1\). The other two chains never bridge \(x\). \(\square\)

Let \(a_\tau\) be the number of base chains of half-length \(\tau\),
where \(0\le\tau\le m-1\). Every SCD of \(B_Z\) has the exact census

\[
\begin{aligned}
a_\tau
&=\binom{2m-2}{m-1-\tau}
  -\binom{2m-2}{m-2-\tau}\\
&=
N_\tau\,{(m-\tau)(2\tau+1)\over2m(2m-1)}.
\end{aligned}
\tag{4.6}
\]

Choose \(l_\tau\) of these blocks to use the \(L\)-shore and
\(u_\tau=a_\tau-l_\tau\) to use the \(U\)-shore. Put

\[
 \varepsilon_\tau=l_\tau-u_\tau.
\tag{4.7}
\]

### Theorem 4.3 (balanced product-SCD coupling)

The chosen blocks form a full SCD of \(B_{2m}\). Its exact bridge
counts satisfy

\[
 I_q(x)-G_q(x)=\varepsilon_{q-1}+\varepsilon_q,
\tag{4.8}
\]

\[
 I_q(x)+G_q(x)=a_{q-1}+a_q={q\over m}N_q,
\tag{4.9}
\]

for \(1\le q\le m\), where
\[
 a_{-1}=a_m=0,\qquad
 \varepsilon_{-1}=\varepsilon_m=0.
\]
Choosing

\[
 |\varepsilon_\tau|\le1,\qquad
 \varepsilon_\tau\equiv a_\tau\pmod2,
\tag{4.10}
\]

gives

\[
 \boxed{
 \left|G_q(x)-{q\over2m}N_q\right|\le1}
\tag{4.11}
\]

for every \(q\). The SCD has exactly one middle owner and exactly one
lower and upper target at every active depth; hence

\[
 D_{\rm deep}=0
\tag{4.12}
\]

and the paired quotient condition is automatic.

#### Proof

Different base chains partition \(B_Z\), and Lemma 4.1 partitions the
product over each base chain. Their union is therefore a full SCD.
Lemma 4.2 gives (4.8).

Every full SCD has one chain through each target in either signed rank
layer. Thus its number of \(x\)-bridges is the number of selected upper
targets containing \(x\) minus the analogous lower number:

\[
 {m+q\over2m}N_q-{m-q\over2m}N_q
 ={q\over m}N_q.
\]

This proves (4.9). Conditions (4.10) are realized by splitting each
integer \(a_\tau\) as evenly as possible. Solving (4.8)--(4.9) gives
(4.11). Exact SCD bijectivity proves (4.12). \(\square\)

Summing (4.11) through \(H\) gives

\[
 \sum_{q=1}^HG_q(x)
 =\left({1\over4}+o(1)\right)W.
\tag{4.13}
\]

Thus there is an integral, owner-simple, targetwise exact common-history
coupling with zero defect and the expected half of all bridge incidence
on the exterior side.

### 4.2 A biased SCD attaining the statewise lower envelope

Put

\[
 Q=\left\lfloor{\sqrt m\over2}\right\rfloor,\qquad
 c_q=qR_0={qT\over2m},\qquad
 b_q={q\over m}N_q,
\tag{4.14}
\]

\[
 \Delta_q^*=2c_q-b_q={q\over m}(T-N_q).
\tag{4.15}
\]

All these quantities are integers.

### Theorem 4.4 (biased shore recurrence)

For every sufficiently large \(m\), the product blocks can be chosen so
that, simultaneously for all \(1\le q\le Q\),

\[
 \boxed{
 I_q(x)=qR_0,\qquad
 G_q(x)={q\over m}\left(N_q-{T\over2}\right).}
\tag{4.16}
\]

The resulting object remains a full SCD, so \(h_q=0\) at every depth.
Consequently equality holds in (1.8) for every \(q\le Q\).

#### Proof

Choose

\[
 \varepsilon_0\in\{0,1\},\qquad
 \varepsilon_0\equiv a_0\pmod2,
\tag{4.17}
\]

and recursively put

\[
 \varepsilon_q=\Delta_q^*-\varepsilon_{q-1}
 \qquad(1\le q\le Q).
\tag{4.18}
\]

The sequence \(\Delta_q^*\) is nondecreasing in this range. Since
\(\varepsilon_0\le\Delta_1^*\) for all large \(m\), induction gives

\[
 0\le\varepsilon_q\le\Delta_q^*.
\tag{4.19}
\]

For completeness,

\[
 m(\Delta_{q+1}^*-\Delta_q^*)
 =
 T-\bigl((q+1)N_{q+1}-qN_q\bigr)\ge0,
\]

because the parenthesized difference is at most \(N_q\le T\).

Also

\[
 \Delta_q^*\equiv b_q
 \equiv a_{q-1}+a_q\pmod2.
\]

Thus (4.18) propagates
\(\varepsilon_q\equiv a_q\pmod2\).

Uniformly for \(q\le Q\),

\[
 {T\over N_q}\le e^{1/4}+o(1)<{4\over3},
\tag{4.20}
\]

and (4.6) gives

\[
 {a_q\over N_q}
 ={(m-q)(2q+1)\over2m(2m-1)}
 >{q\over3m}.
\tag{4.21}
\]

Equations (4.15), (4.20), and (4.21) imply
\(\Delta_q^*\le a_q\). Hence

\[
 l_q={a_q+\varepsilon_q\over2},\qquad
 u_q={a_q-\varepsilon_q\over2}
\tag{4.22}
\]

are nonnegative integers. Choose the remaining shores arbitrarily.
Then (4.8), (4.9), and (4.18) give

\[
 I_q-G_q=\Delta_q^*,\qquad I_q+G_q=b_q.
\]

Solving proves (4.16). \(\square\)

Theorem 4.4 is stronger than fractional feasibility: through the
displayed range, the earlier one-coordinate cut is attained by an
integral targetwise bijection with exact owner uniqueness and exact
common tags.

## 5. Every SCD chain is individually literal, but balanced history-for-history injection fails

### Lemma 5.1 (individual promotion embedding)

Let

\[
 D_{-t}\subset D_{-t+1}\subset\cdots\subset D_0
 \subset\cdots\subset D_t
\tag{5.1}
\]

be one symmetric chain of \(B_{2m}\), centered at the middle owner
\(D_0\). Put \(r=\min(t,H)\). There is a root

\[
 A\in\binom{[2m]}{m-H}
\]

and one cyclic phase on \(A^c\) whose promotion traces satisfy

\[
 L_q=D_{-q},\qquad U_q=D_q
 \quad(0\le q\le r).
\tag{5.2}
\]

If \(t\ge H\), the root is forced to be \(A=D_{-H}\). If \(t<H\),
any \(A\subset D_{-t}\) of size \(m-H\) may be used.

#### Proof

For \(1\le q\le r\), let

\[
 \rho_q=D_{-(q-1)}\setminus D_{-q},\qquad
 \upsilon_q=D_q\setminus D_{q-1}.
\tag{5.3}
\]

In one directed top order, place consecutively:

1. \(\rho_1,\ldots,\rho_r\);
2. the \(H-r\) elements of \(D_{-r}\setminus A\);
3. \(\upsilon_1,\ldots,\upsilon_r\);
4. all elements outside \(D_r\), in arbitrary order.

The first \(H\) symbols form \(D_0\setminus A\). Deleting their first
\(q\) symbols leaves \(D_{-q}\setminus A\); extending them by the next
\(q\) symbols gives \(D_q\setminus A\). This is exactly (5.2).
\(\square\)

Every rank-\((m-H)\) set occurs once as the lower depth-\(H\) vertex of
the full SCD. Hence the chains of half-length at least \(H\) give one
literal tag-\(H\) anchor at every physical root. Rotate each chosen
cyclic order so that this chain occupies a designated local phase;
this is only a per-root normalization and does not impose one common
phase profile across different roots. The obstruction begins with the
shorter chains.

### Theorem 5.2 (exact scope of the SCD construction)

The balanced and biased SCDs prove all of the following:

1. exact middle-owner bijectivity;
2. exact lower and upper target bijectivity at every depth;
3. one common stopping tag per history;
4. the paired quotient-chain property; and
5. individual literal promotion realizability of every history.

They do not prove a one-frame-per-root promotion factor.

#### Proof

The positive statements follow from Theorems 4.3--4.4 and Lemma 5.1.
For a short chain \(t<H\), Lemma 5.1 chooses a root and cyclic order
independently. Nothing shows that these choices are distinct phase
positions of the single cyclic frame already fixed by the tag-\(H\)
anchor at that root.

For the balanced product SCD there is also a global anchored-type
mismatch. In a physical frame over
an \({\cal A}_0\) root, exactly \(H\) middle phases contain \(x\).
Thus the entire one-frame-per-root catalogue has only

\[
 HR_0=o(W)
\tag{5.4}
\]

possible internal \(x\)-bridge histories. Moreover

\[
 \sum_{\tau=0}^{H}a_\tau
 =
 \binom{2m-2}{m-1}
 -\binom{2m-2}{m-2-H}
 =
 \left({1\over4}+o(1)\right)W.
\tag{5.4a}
\]

Thus, among the controlled base blocks, the balanced product SCD uses
the \(L\)-shore on asymptotically half of

\[
 \binom{2m-2}{m-1}=\left({1\over4}+o(1)\right)W
\]

base chains, and each nontrivial \(L\)-block has internal chains. Hence
it uses \(\Theta(W)\) distinct controlled internal histories.
The balanced product SCD cannot even be injected history-for-history
into the physical anchored phase types without nonlocal rethreading.
\(\square\)

There is a local obstruction to the most obvious bundling.

### Lemma 5.3 (three-window triangle obstruction)

For a nontrivial base block, four of its middle owners have the form

\[
 B+\{a,b\},\qquad B+\{a,x\},\qquad
 B+\{a,y\},\qquad B+\{x,y\},
\qquad |B|=m-2.
\tag{5.5}
\]

The first three cannot be phases of one promotion ring.

#### Proof

If the three owners belonged to one ring with root \(A\), then
\(A\subseteq B+\{a\}\). Put
\[
 S=(B+\{a\})\setminus A,
\]
so \(|S|=H-1\). Their three \(H\)-window parts would be

\[
 S+\{b\},\qquad S+\{x\},\qquad S+\{y\}.
\tag{5.6}
\]

They are distinct and pairwise have symmetric difference two. Since
\(M>2H\) for all large \(m\), two distinct cyclic \(H\)-intervals have
symmetric difference two only when their starting positions are
adjacent. Three vertices cannot be pairwise adjacent in the cycle
\(C_M\). \(\square\)

Lemma 5.3 rules out blockwise bundling, not global reassignment between
different blocks. The exact remaining task is to rethread a linear
number of short SCD bridge pieces into only \(O(W/\sqrt m)\)-scale long
anchored bridge histories while simultaneously preserving target
bijectivity, owner uniqueness, and the one-frame-per-root cyclic
identities.

## 6. Why monotone and ordinary optimal transport collapse

### Lemma 6.1 (equal-rank monotonicity is diagonal)

Let \(\mu,\nu\) be measures on \(\binom{\Omega}{r}\). A coupling
\(\pi\) supported on

\[
 \{(S,T):S\subseteq T\}
\]

is supported on the diagonal \(S=T\). In particular such a coupling
exists only if \(\mu=\nu\).

#### Proof

If \(S,T\) have the same cardinality and \(S\subseteq T\), then
\(S=T\). \(\square\)

At every typed signed depth, the donor targets and vacancy targets have
the same rank. Therefore Boolean monotone transport between them says
only that the literal targets must already agree. On complete histories
the product order is equally discrete, because every corresponding
middle, lower, and upper coordinate has fixed rank.

On the coarse status quotient one may impose the ad hoc bridge-state
\(V\)-order

\[
 00\prec01,\qquad 11\prec01.
\tag{6.1}
\]

This is not the quotient of Boolean coordinatewise inclusion (whose
three status states form \(00<01<11\)); it only records progress toward
the bridge state. In this auxiliary order both exterior and internal
histories move monotonically toward \(01\). This quotient forgets every
target identity. The uniform survival point

\[
 z_{e,q}={N_q\over T}
\tag{6.2}
\]

is an exact fractional common-tag coupling in this quotient and has

\[
 I_q^{\rm frac}=G_q^{\rm frac}={q\over2m}N_q,
\qquad h_q^{\rm frac}=0.
\tag{6.3}
\]

Thus no monotone theorem on the signature quotient can prove positive
deep defect.

Let \(G_x\le S_{2m}\) be the coordinate-permutation stabilizer of
\(x\).

### Lemma 6.2 (random common motion has no transport advantage)

Fix two class seeds and let \(\Delta(h)\) be their exact signed
collision-plus-hole cost under the common relative motion
\(h\in G_x\). For every probability law \(\rho\) on \(G_x\),

\[
 \mathbb E_\rho\Delta(h)\ge\min_{g\in G_x}\Delta(g).
\tag{6.4}
\]

Hence optimizing a correlated law over common motions is exactly the
original deterministic exceptional-alignment problem.

#### Proof

The expectation is a convex combination of the deterministic costs.
\(\square\)

Allowing an arbitrary Kantorovich coupling between individual targets
is strictly weaker than one common motion. For example, choose
\(B_1,B_2,A_1,A_2\) to be \(r\)-sets in the same \(x\)-sector, with

\[
 |B_1\cap B_2|=r-1,\qquad |A_1\cap A_2|=r-2.
\tag{6.5}
\]

Every individual \(B_i\) can be sent to every \(A_j\) by a permutation
in \(G_x\), so the ordinary transport graph has a perfect matching.
No one permutation sends the source pair to the target pair, because
intersection size is invariant. This witnesses strictness only at the
target-layer coupling level; no common physical promotion collar is
claimed for this four-set example.

More generally, let \(\Gamma\) be a \(G_x\)-invariant graph on one
target layer, of maximum degree \(\Delta_\Gamma>0\), and let
\(e_\Gamma(S)\) count edges induced by a target family \(S\). Then
every common motion satisfies

\[
 \boxed{
 |A\mathbin\triangle hB|
 \ge
 {|e_\Gamma(A)-e_\Gamma(B)|\over\Delta_\Gamma}.}
\tag{6.6}
\]

Indeed changing one family vertex changes the induced-edge count by at
most \(\Delta_\Gamma\). Equation (6.6) is a valid route to a genuine
targetwise obstruction, but no linear invariant gap for the actual
anchored profiles is proved here.

## 7. The exact transport object: complete-history Hall versus configuration Farkas

Ordinary transport becomes exact only after the vacancies have already
been assembled into complete, mutually compatible histories.

Let \({\mathscr S}\) be a finite family of source histories with integer
masses \(a_s\), and let \({\mathscr D}\) be a resource-disjoint family
of complete vacancy histories with integer capacities \(b_d\). A
history records its middle owner, stopping tag, and every active pair
\((L_q,U_q)\). Write \(s\sim d\) when all owner, tag, and trace
requirements are compatible.

### Theorem 7.1 (capacitated complete-history Hall theorem)

The maximum transportable source mass is

\[
 \boxed{
 \nu=
 \min_{{\mathscr U}\subseteq{\mathscr S}}
 \left[
 a({\mathscr S}\setminus{\mathscr U})
 +b(N({\mathscr U}))
 \right].}
\tag{7.1}
\]

Equivalently, the exact deficiency is

\[
 \boxed{
 a({\mathscr S})-\nu
 =
 \max_{{\mathscr U}\subseteq{\mathscr S}}
 \left[
 a({\mathscr U})-b(N({\mathscr U}))
 \right]_+.}
\tag{7.2}
\]

For integer data, an integral optimal transport exists.

#### Proof

Create a source vertex of capacity \(a_s\), a vacancy vertex of
capacity \(b_d\), and an infinite-capacity compatibility edge for every
\(s\sim d\). The source--sink max-flow/min-cut theorem gives (7.1);
moving the first term to the other side gives (7.2). Integral
capacities give an integral flow. \(\square\)

Layerwise hole sets are not a family \({\mathscr D}\). The same hole
target can participate in many candidate chains, and chains at
different depths can merge and then split. Preassembling a disjoint
\({\mathscr D}\) is already a substantial part of the open problem.

For the unassembled problem, let \({\cal C}(A)\) be the tagged physical
configurations at root \(A\). Let

\[
 \rho_{A,c}\in\mathbb Z_{\ge0}^{\cal R}
\]

be the complete resource-incidence vector of configuration \(c\):
middle owners and every signed target at every active depth are all
included in the resource set \({\cal R}\). Let \(C\) be the residual
capacity vector.

### Theorem 7.2 (exact fractional configuration dual)

There are coefficients

\[
 \lambda_{A,c}\ge0,\qquad
 \sum_{c\in{\cal C}(A)}\lambda_{A,c}=1,
\]

with

\[
 \sum_{A,c}\lambda_{A,c}\rho_{A,c}\le C
\tag{7.3}
\]

if and only if, for every \(y\in\mathbb R_{\ge0}^{\cal R}\),

\[
 \boxed{
 \sum_A\min_{c\in{\cal C}(A)}
       \langle y,\rho_{A,c}\rangle
 \le
 \langle y,C\rangle.}
\tag{7.4}
\]

#### Proof

The possible aggregate fractional resource vectors form the Minkowski
sum

\[
 P=\sum_A\operatorname{conv}
       \{\rho_{A,c}:c\in{\cal C}(A)\}.
\]

Condition (7.3) is \(P\cap\{u:u\le C\}\ne\varnothing\). If the two
convex sets are disjoint, separation from the downward-closed second
set uses a nonnegative vector \(y\), and gives

\[
 \min_{u\in P}\langle y,u\rangle>\langle y,C\rangle.
\]

The minimum over the Minkowski sum is the sum of the rootwise minima,
which is exactly the negation of (7.4). The converse is immediate.
\(\square\)

Theorem 7.2 is fractional. A configuration atom consumes many targets,
so ordinary bipartite Hall integrality does not apply. The paired
quotient-chain theorem becomes useful only after an integral,
target-simple, history-closed configuration family has been selected.

## 8. The two-history Monge fork

We now test the most literal monotone construction. At every active
exterior history \(b\), assign one donor history \(a_b\) from
\({\cal A}_1\), consistently throughout the spill interval, with

\[
 U_q(a_b)=U_q(b)
\tag{8.1}
\]

whenever \(b\) is an active exterior bridge.

At depth \(q\), let \({\cal B}_q\) be the active exterior histories,
so \(|{\cal B}_q|=G_q(x)\). Put

\[
 K_q=
 G_q(x)-
 |\{L_q(a_b):b\in{\cal B}_q\}|,
\tag{8.2}
\]

the multiplicity excess among donor lower traces. Let \(R_q\) be the
number of distinct donor lower targets covered by an active occurrence
outside their assigned two-history atoms.

### Theorem 8.1 (Monge-fork inequality)

If the final lower and upper projections are injective, then, exactly,

\[
 \boxed{
 G_q(x)\le h_q+K_q+R_q.}
\tag{8.3}
\]

Consequently,

\[
 \boxed{
 D_{\rm deep}
 +\sum_{q=q_0}^{Q_*}(K_q+R_q)
 \ge
 \left({1-\log2\over4}+o(1)\right)W.}
\tag{8.4}
\]

In particular, every lower-simple, target-closed two-history Monge
coupling, for which \(K_q=R_q=0\), has

\[
 D_{\rm deep}\ge
 \left({1-\log2\over4}+o(1)\right)W.
\tag{8.5}
\]

Every \(o(W)\)-deep-defect construction of this form needs

\[
 \sum_{q=q_0}^{Q_*}(K_q+R_q)
 \ge
 \left({1-\log2\over4}-o(1)\right)W
\tag{8.6}
\]

nonlocal coalescence or repair incidences.

#### Proof

Since \(a_b\in{\cal A}_1\), its lower trace contains \(x\). Since \(b\)
is exterior, \(L_q(b)\) avoids \(x\). Hence

\[
 L_q(a_b)\ne L_q(b).
\tag{8.7}
\]

The donor \(a_b\) cannot itself be active at depth \(q\), because
(8.1) would create an upper collision with \(b\). There are
\(G_q-K_q\) distinct donor lower targets. At most \(R_q\) are covered
by occurrences outside the assigned atoms. Every remaining target is
a lower hole, so

\[
 G_q-K_q-R_q\le h_q.
\]

This proves (8.3). Combining it with (1.8) gives

\[
 2h_q+K_q+R_q\ge \alpha_q.
\]

Sum through \(Q_*\), use the definition of \(D_{\rm deep}\), and apply
(2.4)--(2.5). This proves (8.4)--(8.6). \(\square\)

Before history-closed pruning, let \(H_q^-\) denote the actual lower
hole count (which need not yet equal the common paired hole count
\(h_q\)). The same proof gives

\[
 G_q(x)\le H_q^-+K_q+R_q+C_q^+,
\tag{8.8}
\]

where \(C_q^+\) is upper collision excess.

### 8.1 A literal common-tag quantile slab

The obstruction in Theorem 8.1 is not a shortage of common tags. Form
the bipartite graph between \({\cal A}_1\) and \({\cal A}_0\) in which
an edge swaps \(x\) for one coordinate. Its left degree is \(M\) and
its right degree is \(k=m-H\). Hence, for every
\({\cal S}\subseteq{\cal A}_1\), edge counting gives

\[
 M|{\cal S}|\le k|N({\cal S})|,
\]

so Hall's theorem supplies a matching saturating all \(R_1\) roots of
\({\cal A}_1\). Fix such a matching. For one matched edge write

\[
 A_1=C\cup\{x\},\qquad A_0=C\cup\{y\},
\tag{8.9}
\]

where \(y\) may depend on the matched edge, and use paired marker
frames: replace one common marker by \(y\) in the
\({\cal A}_1\) top and by \(x\) in the \({\cal A}_0\) top. Let

\[
 k_q=\left\lfloor{N_q\over N}\right\rfloor.
\]

### Lemma 8.2 (tag supply)

There is one cyclic tag word
\(d:\mathbb Z_M\to\{0,\ldots,H\}\) with

\[
 |\{i:d(i)\ge q\}|=k_q
\tag{8.10}
\]

for every \(1\le q\le H\), and two rotations of this word such that,
for every
\(1\le\tau\le Q_*\), the exterior phase first acquiring \(x\) at depth
\(\tau\) has donor tag \(\tau-1\) in the \({\cal A}_1\) frame and tag
at least \(Q_*\) in the \({\cal A}_0\) frame.

#### Proof

There is an exact-depth-zero symbol because

\[
 {N_1\over N}<{W\over N}\le M.
\]

For \(1\le r<Q_*\),

\[
 {N_r-N_{r+1}\over N}
 ={N_r\over N}{2r+1\over m+r+1}>1
\tag{8.11}
\]

for all large \(m\), because \(N_r/N\ge(1/2+o(1))m\).
Thus \(k_r-k_{r+1}\ge1\). Also

\[
 k_{Q_*}=(1/2+o(1))m>Q_*.
\]

Reserve one symbol of every exact depth
\(0,1,\ldots,Q_*-1\), and reserve \(Q_*\) symbols of depth at least
\(Q_*\). Since \(2Q_*<M\), put the two reserved lists in disjoint
cyclic blocks. Order the low block in the same order as the consecutive
entrance phases (using the reversed depth order if that is their cyclic
orientation); the arbitrary placement of the symbols permits this.
The exterior phases are consecutive as \(\tau\) varies, so two
rotations, without any illicit reflection, align them with the two
blocks. \(\square\)

### Lemma 8.3 (paired trace fork)

Across all \(R_1\) matched root pairs, the quantile slab has

\[
 G_q^{\rm slab}=qR_1
 \quad(1\le q\le Q_*),
\tag{8.12}
\]

and

\[
 \sum_{q=q_0}^{Q_*}G_q^{\rm slab}
 =\left({\log2\over4}+o(1)\right)W.
\tag{8.13}
\]

Inside each paired root atom, through depth \(Q_*\), it covers every
distinct upper target contributed by the two shores exactly once, but
leaves one donor lower trace missing for every exterior incidence. No
target distinctness or middle-owner distinctness between different
root pairs is claimed.

#### Proof

Put the marker at cyclic position zero. The exterior phase of entrance
depth \(\tau\) has a middle window avoiding the marker. Before depth
\(\tau\), the paired upper traces differ; from depth \(\tau\) onward
they agree. The paired lower traces differ at every depth, containing
\(x\) and \(y\), respectively.

The donor survives exactly through depth \(\tau-1\), while the
\({\cal A}_0\) shore survives through \(Q_*\). Hence, within the atom,
the upper traces are covered once at every depth and the donor lower
trace becomes a hole precisely during the exterior residence interval.
Before entry, the donor upper target contains \(x\) but not \(y\),
whereas the \({\cal A}_0\) upper target contains \(y\) but not \(x\);
after entry the targets agree, the donor has stopped, and the surviving
target contains both. Thus there is no cross-shore upper collision
inside the matched pair.
There are \(q\) such phases per matched pair at depth \(q\), proving
(8.12). These are genuinely distinct within one pair: for
\(q\le Q_*<H\), distinct entrance starts give distinct proper cyclic
intervals, since \(H+q<M\).
Since \(R_1=(1+o(1))W/(2m)\) and
\(Q_*^2=(\log2+o(1))m\), summation gives (8.13).
\(\square\)

For one exterior phase of entrance depth \(\tau\), suppose its donor
has stopping depth \(a\) and the \({\cal A}_0\) shore survives through
\(Q_*\). Its local upper hole-plus-collision cost is

\[
 c^+_{\tau}(a)
 =
 \left|\min(a,Q_*)-(\tau-1)\right|,
\tag{8.14}
\]

while its pair-local unrepaired donor-lower cost is

\[
 c^-_{\tau}(a)=Q_*-\min(a,Q_*).
\tag{8.15}
\]

Therefore

\[
 \boxed{
 c^+_{\tau}(a)+c^-_{\tau}(a)
 \ge Q_*-\tau+1.}
\tag{8.16}
\]

The upper-optimal choice is uniquely \(a=\tau-1\), and then the
pair-local lower toll equals the entire exterior residence. It becomes
a global hole only if no cross-atom repair covers that target. This is
the exact two-sign fork which prevents a direct fixed-donor
quantile/Monge solution.

## 9. Audited implication boundary

### 9.1 What is now proved

1. The optimized all-depth anchored-signature inequality (0.2), with
   exact constant \((1-\log2)/4\).
2. The joint deep-defect/distinct-history tradeoff (3.1)--(3.3), giving
   \(K_x\ge(\gamma-o(1))W/\sqrt m\).
3. Exact integral saturation of the optimized cut in the fixed-\(x\)
   signature/common-tag quotient.
4. An exact integral full SCD with zero owner, target, and common-history
   defect and balanced \(G_q\).
5. A biased product SCD attaining the old pointwise state cut through
   \(q\le\sqrt m/2\).
6. Individual literal promotion realization of every SCD chain.
7. For the balanced construction, failure of history-for-history
   anchored injection, including the raw internal-type shortage and
   the local three-window triangle; for both product constructions,
   simultaneous anchored factorization remains unproved.
8. The complete-history Hall dual and the fractional configuration
   Farkas dual.
9. The exact Monge-fork inequality and a literal common-tag quantile
   slab saturating its local upper-sign choice.

### 9.2 What is not proved

1. A one-frame-per-root promotion factor with target defect \(o(W)\).
2. An injective assignment of the balanced SCD histories to the raw
   anchored phase slots.
3. A nonlocal rectangle/rethreading family realizing the
   \(\Omega(W)\) repairs required by (8.6) within the fixed-donor
   architecture, or an explicit higher-order construction evading
   fixed-donor representability.
4. An invariant graph \(\Gamma\) for which (6.6) gives a linear gap on
   every admissible anchored pair.
5. The configuration integrality statement corresponding to (7.4).

### 9.3 A sufficient surviving factorization lemma

The remaining positive statement can be isolated as follows.

> **Anchored nonlocal rethreading/factorization lemma (open).** Starting
> from an exact targetwise common-history resolution such as Theorem
> 4.3, rethread its short internal and exterior chain pieces into
> physical histories so that:
>
> 1. exactly one cyclic frame is used at every rank-\((m-H)\) root;
> 2. \(W-o(W)\) middle owners are used exactly once, and all retained
>    histories carry one common stopping tag;
> 3. after history-closed pruning, the active family at every depth
>    \(q\le H\) has common size \(N_q-h_q\), both signed target
>    projections are injective, and
>    \(\sum_{q=1}^Hh_q=o(W)\);
> 4. the resulting physical histories have a literal path cover with
>    \(C_{\rm path}=o(W/H)\) components and the accepted crossing-collar
>    interface.

Clauses 1--4 are sufficient data. Indeed clause 3 already gives the
common integral paired representatives; no further quotient
integrality is needed. If \(d_{\rm mid}=o(W)\) is the middle-owner
defect from clause 2, the accepted literal compilation ledger is

\[
 L\le
 T+O(HC_{\rm path})+O(d_{\rm mid})
   +2\sum_{q=1}^Hh_q
 =W+o(W).
\tag{9.1}
\]

Appending the accepted economical exterior therefore gives
coefficient one.

Two necessary diagnostics are automatic rather than extra hypotheses:
(0.6) forces at least
\((\gamma-o(1))W/\sqrt m\) distinct exterior histories with their full
joint residence; and any realization which factors through the
fixed-donor Monge representation must supply the \(\Omega(W)\) repair
incidences forced by (8.6). A higher-order realization need not admit
that representation.

If the sufficient lemma fails, the
obstruction must use common-root cyclic-frame factorization, anchored
threshold multiplicities, or a targetwise invariant such as (6.6). In
the abstract complete-history relaxation, it cannot depend only on
deep defect, the complete \(G_q\) residence process, common stopping
tags, owner uniqueness, or separate signed target bijectivity: the
exact relaxations above already satisfy all of those. This last
statement is not asserted inside the one-frame-per-root physical
factor class.
