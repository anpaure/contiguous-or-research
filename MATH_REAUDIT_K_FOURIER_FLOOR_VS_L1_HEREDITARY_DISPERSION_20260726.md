# Re-audit of the Fourier/floor obstruction at the exact \(L^1\) coverage threshold

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Corrected verdict

The exact constant-one target for the retained packet factor is

\[
 \mathfrak H
 :=\sum_{1\le q\le H}\sum_{\epsilon\in\{-,+\}}M_q^\epsilon
 =\sum_{1\le q\le H}\sum_{\epsilon}\sum_{T\in\mathcal T_q^\epsilon}
        (1-L_q^\epsilon(T))_+
 =o(W).                                                   \tag{0.1}
\]

Here

\[
 W=\binom{2m}{m},\qquad
 N_q=|\mathcal T_q^\epsilon|=\binom{2m}{m-q}
      =\binom{2m}{m+q},                                  \tag{0.2}
\]

the retained owner mass satisfies \(G=W-o(W/H)\). For the audited
rank-twisted packet atlas one has the stronger leave estimate

\[
                         W-G=2^{m+o(m)}=o(W/m),             \tag{0.2a}
\]

so \(G>N_q\) for every \(q\ge1\) and all sufficiently large \(m\).
Also, \(L_q^\epsilon(T)\) is the integral occurrence load of target \(T\).

The earlier Fourier/floor report mixed this target with the strictly
stronger requirement that every load be close to the two adjacent integers
around \(G/N_q\). The correction is as follows.

1. The exact repeat identity remains valid:

   \[
    M_q^\epsilon=N_q-G+
       \sum_T(L_q^\epsilon(T)-1)_+.                       \tag{0.3}
   \]

2. The floor energy and its pairwise Fourier/Gram expansion give a
   sufficient route to (0.1), but a large floor energy does not imply even
   one hole. Consequently negative cross-packet Gram of order \(W\) is not
   necessary for constant one.

3. The independent-random-choice hole theorem remains a genuine \(L^1\)
   theorem, but it rules out only the product distribution. It does not rule
   out an exceptional correlated deterministic assignment.

4. The localized carrier-\(E\) construction remains a deterministic
   counterexample to every assignment in that atlas. Its proof is a literal
   invariant-fibre capacity cut, not a floor-energy argument. The same is
   true of the audited frozen-suffix, one-touch first-eligible, and full
   common-order support obstructions, within their stated scopes.

5. The sharp hereditary dispersion test supplied by an invariant tag is

   \[
   \boxed{
    \Phi_{q,\epsilon}(\mathcal S,\pi)
    :=\left[
       \sum_y(s_y-n_y)_+-(G-N_q)
      \right]_+
    =\left[
       \sum_y(n_y-s_y)_+-(G-|\mathcal S|)
      \right]_+.}                                         \tag{0.4}
   \]

   Every assignment has \(M_q^\epsilon\ge\Phi_{q,\epsilon}\).
   Here \(\mathcal S\) is any localized owner subfamily, every legal state
   preserves its tag \(\pi=y\), \(s_y\) is its owner mass in tag fibre
   \(y\), and \(n_y\) is the number of signed depth-\(q\) targets in that
   fibre. Formula (0.4) is sharp from these fibre capacities alone.

Thus the surviving constant-one gate is a correlated grouped set-cover
problem. It is not a floor-quota or second-moment problem.

## 1. Exact \(L^1\), repeat, pair, and floor ledgers

Fix one signed context \(c=(q,\epsilon)\), suppress \(c\), and write

\[
 N=N_q,\qquad \sum_{T\in\mathcal T}L(T)=G.                 \tag{1.1}
\]

Define

\[
 M=|\{T:L(T)=0\}|,qquad
 \mathcal R=\sum_T(L(T)-1)_+.                             \tag{1.2}
\]

Since the covered set has size \(G-\mathcal R\),

\[
 \boxed{M=N-G+\mathcal R.}                                \tag{1.3}
\]

Under the actual leave (0.2a), \(G>N\) for every protected \(q\ge1\).
The unavoidable global repeat baseline is then \(G-N\), and

\[
 \boxed{M=\mathcal R-(G-N).}                              \tag{1.4}
\]

This is the exact baseline relevant to coverage. It is not the adjacent
integer floor baseline.

Let

\[
 P=\sum_T\binom{L(T)}2.                                   \tag{1.5}
\]

Then

\[
 \boxed{
 P-\mathcal R
 =\sum_T\binom{(L(T)-1)_+}{2}.}                         \tag{1.6}
\]

Thus pair collisions determine repeats only when no target has load at
least three. Triple and higher occupancy is exactly the missing information.

Now put

\[
 \lambda={G\over N}=c+\theta,qquad
 c=\lfloor\lambda\rfloor,\quad0\le\theta<1,               \tag{1.7}
\]

and suppose \(c\ge1\). Let \(\Delta\) be the pair-collision excess above
the adjacent-integer minimum. The exact identity is

\[
 \boxed{
 2\Delta=\sum_T(L(T)-c)(L(T)-c-1).}                       \tag{1.8}
\]

Every term is nonnegative for integral \(L(T)\). A hole contributes
\(c(c+1)\), so

\[
 \boxed{M\le {2\Delta\over c(c+1)}.}                     \tag{1.9}
\]

The direction in (1.9) is decisive: \(\Delta=o(W)\) is sufficient for
few holes, but \(\Delta=\Omega(W)\) supplies no lower bound on holes.

For example, if \(G=2N\), give half the targets load \(1\) and half load
\(3\). Then \(M=0\), while \(\Delta=N/2\).

There is also an exact pair-data counterexample. Partition a target universe
into four sets \(B_1,B_2,B_3,B_4\), each of size \(b\). Consider the three
packet images

\[
 B_1\cup B_2,\qquad B_1\cup B_3,\qquad B_2\cup B_3.       \tag{1.10}
\]

They leave \(B_4\) uncovered. By contrast,

\[
 B_1\cup B_2,\qquad B_1\cup B_3,\qquad B_1\cup B_4       \tag{1.11}
\]

cover the universe. Both systems have packet-image size (2b), every
off-diagonal packet intersection has size \(b\), total mass \(6b\), and the
same floor energy. Hence even the complete packet Gram matrix does not
determine the union size.

## 2. Exact scope of the Fourier statements

The individual ambient Walsh transform of a packet indicator is invertible
and therefore contains the whole packet image. The loss occurs only after
contracting to second order.

The physical Parseval identity

\[
 |I_P\cap I_Q|
 =2^{-2m}\sum_\xi\widehat{1_{I_P}}(\xi)
                         \widehat{1_{I_Q}}(\xi)             \tag{2.1}
\]

is exact. So are the reduced same-atlas pair kernel and the pair-orbit
covariance formulas. But these formulas compute only

\[
 \sum_{P\ne Q}|I_P\cap I_Q|,                              \tag{2.2}
\]

or refinements of the same pair data. Coverage instead depends on the
nonlinear zero class, equivalently on all intersection orders:

\[
 \left|\bigcup_PI_P\right|
 =\sum_{\varnothing\ne J\subseteq\mathcal P}
     (-1)^{|J|+1}\left|\bigcap_{P\in J}I_P\right|.         \tag{2.3}
\]

Consequently:

* ambient physical tag disjointness is (L^1)-relevant because it gives an
  actual zero intersection or invariant target partition;
* the pair-orbit spectrum, centered cross-Gram, and floor quota are only
  second-order data;
* a degree-one Fourier coefficient is (L^1)-relevant only when converted
  into an explicit target-subset capacity cut;
* cycle and seam counts control physical word cost, not target coverage.

The old conclusion that successful constant-one coverage must generate a
negative cross-packet Gram term of order \(W\) is therefore retracted. That
term is necessary only for the stronger demand \(\Delta=o(W)\).

## 3. Invariant-tag capacity theorem

The following theorem is the exact replacement for the scalar localized
carrier bound.

### Theorem 3.1 (sharp hereditary invariant-tag deficit)

Fix a signed context \(c=(q,\epsilon)\). Let the target family
\(\mathcal T_c\), of size \(N=N_q\), be partitioned into tag fibres

\[
 \mathcal T_c=\mathop{\dot\bigcup}_{y\in\mathcal Y}
                    \mathcal T_{c,y},qquad
 n_y=|\mathcal T_{c,y}|.                                  \tag{3.1}
\]

Let \(\mathcal S\) be a subfamily of \(S=|\mathcal S|\) retained owner
occurrences. Suppose every legal state of every packet containing an
occurrence \(x\in\mathcal S\) sends \(x\) to a target in one prescribed
fibre \(\mathcal T_{c,\pi(x)}\). Put

\[
 s_y=|\{x\in\mathcal S:\pi(x)=y\}|.                       \tag{3.2}
\]

Then every deterministic, arbitrarily dependent legal packet-state
assignment obeys

\[
 \boxed{
 \begin{aligned}
 M_c
 &\ge
 \left[\sum_y(n_y-s_y)_+-(G-S)\right]_+                  \\[1mm]
 &=\left[\sum_y(s_y-n_y)_+-(G-N)\right]_+                \\[1mm]
 &=\frac12\left[
       \|n-s\|_1-(2G-N-S)
     \right]_+.
 \end{aligned}}                                           \tag{3.3}
\]

Here \([z]_+=\max\{z,0\}\), including in the last line.

#### Proof

The localized occurrences can cover at most

\[
 \sum_y\min\{s_y,n_y\}                                   \tag{3.4}
\]

distinct targets. The other (G-S) retained occurrences can cover at most
(G-S) further targets. Therefore

\[
 M_c\ge
 \left[N-(G-S)-\sum_y\min\{s_y,n_y\}\right]_+.           \tag{3.5}
\]

Since

\[
 N-\sum_y\min\{s_y,n_y\}=\sum_y(n_y-s_y)_+,              \tag{3.6}
\]

the first line of (3.3) follows. Also

\[
 \sum_y(n_y-s_y)=N-S,                                    \tag{3.7}
\]

so

\[
 \sum_y(n_y-s_y)_+
 =N-S+\sum_y(s_y-n_y)_+.                                 \tag{3.8}
\]

This gives the second line. Finally,

\[
 \sum_y(n_y-s_y)_+
 ={\|n-s\|_1+N-S\over2},                                 \tag{3.9}
\]

which gives the third. \(\square\)

The theorem has the exact global repeat interpretation. The quantity

\[
 \mathfrak E_c(\mathcal S,\pi)
 :=\sum_y(s_y-n_y)_+                                     \tag{3.10}
\]

is repeat mass forced inside the invariant fibres. When \(G\ge N\), up to
\(G-N\) repeats are globally unavoidable and can coexist with full
coverage. Only

\[
 \left[\mathfrak E_c-(G-N)\right]_+                       \tag{3.11}
\]

forces holes. When \(G<N\), \(N-G\) holes are forced even with no repeats;
the same displayed positive-part formula already incorporates that case.
This is precisely the correction missing from a floor-energy or
raw-collision argument.

### Sharpness

Formula (3.3) is sharp from the numbers \(s_y,n_y,G\) alone. If packet
grouping and all other geometry are discarded, choose
\(\min\{s_y,n_y\}\) distinct targets in every fibre for the localized
occurrences, and let the other \(G-S\) occurrences occupy as many still
uncovered targets as possible. The resulting hole count is exactly (3.5).

Thus no stronger universal hole inequality follows from this invariant-tag
capacity information. Sharpness here does not assert that the abstract
allocation is realizable by a common exact-factor choice; packet grouping,
cycle closure, and coupling across depths can impose further constraints.

### Optimistic full-owner completion

If the \(W-G\) omitted owners are granted one arbitrary new target each,
replace \(G\) by \(W\) in (3.3):

\[
 \boxed{
 M_{c,\mathrm{after\ leave}}
 \ge
 \left[\mathfrak E_c-(W-N)\right]_+
 =\frac12\left[
   \|n-s\|_1-(2W-N-S)
 \right]_+.}                                             \tag{3.12}
\]

This is a stronger audit convention than the actual retained-factor
ledger. Since \(2H(W-G)=o(W)\), the \(G\)- and \(W\)-based hereditary
conditions are asymptotically equivalent after summing all signed depths.

## 4. The sharp hereditary dispersion conditions

There are two useful levels. The first is the full hereditary Hall
condition in the ungrouped owner-to-target reachability graph. The second
is the explicit invariant-tag specialization used by the localized
atlases.

### 4.1 Full support-neighborhood form

Freeze one literal owner atlas and one context \(c\). Let
\(\mathcal O\) be its \(G\) retained owner occurrences, and form the
optimistic edge-union graph

\[
 E_c=\{(x,T)\in\mathcal O\times\mathcal T_c:
       \text{some legal global state sends }x\text{ to }T\}. \tag{4.0}
\]

For \(\mathcal A\subseteq\mathcal O\), let

\[
 \Gamma_c(\mathcal A)
 :=\{T\in\mathcal T_c:\text{some legal global state sends some }
             x\in\mathcal A\text{ to }T\}.                 \tag{4.1}
\]

Every fixed legal state covers at most

\[
 (G-|\mathcal A|)
   +\min\{|\mathcal A|,|\Gamma_c(\mathcal A)|\}             \tag{4.2}
\]

targets. Hence

\[
 \boxed{
 M_c\ge
 \left[
  N_q-G+
  \bigl(|\mathcal A|-|\Gamma_c(\mathcal A)|\bigr)_+
 \right]_+.}                                               \tag{4.3}
\]

Put

\[
 d_c:=\max_{\mathcal A\subseteq\mathcal O}
       \bigl(|\mathcal A|-|\Gamma_c(\mathcal A)|\bigr).
                                                               \tag{4.4}
\]

The sharp hereditary support-dispersion condition is

\[
 \boxed{
 \sum_{1\le q\le H}\sum_\epsilon
       [d_{q,\epsilon}-(G-N_q)]_+=o(W).}             \tag{HD\(_{\rm Hall}\)}
\]

It is sharp for the ungrouped edge-union relaxation. Indeed, if every edge
of \(E_c\) could be selected independently, the Hall--Berge deficiency
theorem gives maximum matching size \(G-d_c\). Therefore the minimum
number of holes in that relaxation is exactly

\[
                         N_q-G+d_c.                         \tag{4.5}
\]

This is nonnegative: if \(G\ge N_q\), taking
\(\mathcal A=\mathcal O\) gives
\(d_c\ge G-|\Gamma_c(\mathcal O)|\ge G-N_q\); if \(G<N_q\), the
cardinality deficit is already positive. Actual factor states group many
edges and couple all depths, so
\(\mathrm{HD}_{\rm Hall}\) is necessary, not sufficient, for the literal
problem.

### 4.2 Invariant-tag form

For each context \(c=(q,\epsilon)\), let \(\mathscr I_c\) be the class of
all pairs \((\mathcal S,\pi)\) satisfying the statewise invariant-tag
hypothesis of Theorem 3.1. Define

\[
 \Phi_c^*
 :=\sup_{(\mathcal S,\pi)\in\mathscr I_c}
 \left[\mathfrak E_c(\mathcal S,\pi)-(G-N_q)\right]_+.     \tag{4.6}
\]

Then every common assignment of packet states satisfies

\[
 \boxed{
 \mathfrak H
 \ge\sum_{1\le q\le H}\sum_{\epsilon\in\{-,+\}}
           \Phi_{q,\epsilon}^*.}                           \tag{4.7}
\]

Therefore the sharp hereditary invariant-fibre certificate condition for
exact \(L^1\) coverage is

\[
 \boxed{
 \sum_{1\le q\le H}\sum_\epsilon
 \sup_{(\mathcal S,\pi)\in\mathscr I_{q,\epsilon}}
 \left[
    \sum_y(s_y-n_{q,\epsilon,y})_+-(G-N_q)
 \right]_+
 =o(W).}                                                   \tag{HD\(_1\)}
\]

Equivalently, by (3.3), the summand may be written

\[
 \sup_{(\mathcal S,\pi)}
 \left[
   \sum_y(n_{q,\epsilon,y}-s_y)_+-(G-|\mathcal S|)
 \right]_+,                                               \tag{4.8}
\]

or

\[
 {1\over2}\sup_{(\mathcal S,\pi)}
 \left[
   \|n_{q,\epsilon}-s\|_1
      -(2G-N_q-|\mathcal S|)
 \right]_+.                                               \tag{4.9}
\]

Condition \(\mathrm{HD}_1\) is necessary for (0.1), and is sharp for the
entire class of invariant-tag capacity certificates. It is the computable
fibre specialization of \(\mathrm{HD}_{\rm Hall}\): take all occurrences
in fibres with \(s_y>n_y\), whose reachable target union is contained in
the corresponding union of target fibres. It is not sufficient for a legal
common packet assignment: it deliberately forgets the grouped option
constraint and the requirement that one state work at all depths and both
signs.

The placement of the positive part and the subtraction of \(G-N_q\) are
essential. A large raw fibre discrepancy may be absorbed completely by the
repeat mass already forced by \(G>N_q\).

## 5. Exterior-set specialization and the small-carrier corollary

Let \(E\subset[2m]\), \(e=|E|\), and let \(\mathcal S_E\) be a subfamily
of \(G_E\) owner occurrences such that every legal trace move of these
occurrences changes only coordinates in \(E\). The exterior subset

\[
                         Y=X\cap E^c                       \tag{5.1}
\]

is then a literal statewise tag. Put

\[
 s_E(Y)=|\{X\in\mathcal S_E:X\cap E^c=Y\}|.               \tag{5.2}
\]

The exact target-fibre sizes are

\[
 n_{E,q}^-(Y)=\binom e{m-q-|Y|},\qquad
 n_{E,q}^+(Y)=\binom e{m+q-|Y|},                           \tag{5.3}
\]

with out-of-range binomial coefficients zero. Theorem 3.1 gives

\[
 \boxed{
 M_q^\epsilon\ge
 {1\over2}\left[
  \|n_{E,q}^\epsilon-s_E\|_1
       -(2G-N_q-G_E)
 \right]_+.}                                              \tag{5.4}
\]

This is the exact fibrewise replacement for the earlier scalar condition.

### Corollary 5.1 (small localized carrier)

Assume

\[
 q=a\sqrt m+o(\sqrt m),\quad a>0,\qquad
 e=o(m),\quad q=o(e),\quad {q^2\over e}\longrightarrow\infty.
                                                               \tag{5.5}
\]

Then, uniformly over every localized owner subfamily \(\mathcal S_E\),

\[
 \sum_Y\min\{s_E(Y),n_{E,q}^\epsilon(Y)\}=o(W),           \tag{5.6}
\]

for both signs. Consequently

\[
 \boxed{
 M_q^\epsilon
 \ge\left[N_q+G_E-G-o(W)\right]_+.}                      \tag{5.7}
\]

If \(G=W-o(W)\), a necessary condition for \(M_q^\epsilon=o(W)\) is

\[
 \boxed{
 {G_E\over W}\le1-e^{-a^2}+o(1).}                        \tag{5.8}
\]

#### Proof

For a lower target put \(t=|T\cap E|\). Under the uniform rank-\((m-q)\)
target law,

\[
 \mathbb Et={e(m-q)\over2m},\qquad
 \operatorname {Var}t\le {e\over4}.                      \tag{5.9}
\]

By \(e/q^2=o(1)\), all but \(o(N_q)\) targets have

\[
 \left|t-{e(m-q)\over2m}\right|\le q/10.                 \tag{5.10}
\]

In a fixed exterior fibre the total number of available middle owners is
\(\binom e{t+q}\), while the number of lower targets is \(\binom et\).
Writing \(t=e/2-r\), conditions (5.5) and (5.10) give \(|r|\le q/8\)
eventually, and

\[
 {\binom e{t+q}\over\binom et}
 =\prod_{j=1}^q{e/2+r-j+1\over e/2-r+j}
 \le\exp\left[-\left({3\over5}-o(1)\right){q^2\over e}\right]
 =o(1).                                                   \tag{5.11}
\]

Since \(s_E(Y)\) is bounded by the total middle-owner capacity in that
fibre, summing the minimum of source and target capacities proves (5.6).
For upper targets the source/target ratio is

\[
 {\binom e{u-q}\over\binom eu},                           \tag{5.12}
\]

and the same calculation applies. Formula (5.7) follows from (3.5), and

\[
                         {N_q\over W}\longrightarrow e^{-a^2}
                                                               \tag{5.13}
\]

gives (5.8). \(\square\)

If all depths \(q\le A\sqrt m\) are protected, then no positive-density
owner mass may remain confined to a carrier satisfying

\[
                         \sqrt m\ll e=o(m).                 \tag{5.14}
\]

Indeed, if \(\limsup G_E/W=\gamma>0\), choose a fixed
\(0<a<A\) so small that \(1-e^{-a^2}<\gamma\), and apply (5.8).
This is the clean multiscale meaning of hereditary dispersion.

## 6. Localized legal atlases that still force literal holes

All statements in this section are support-capacity theorems. They survive
the weakening from floor balance to (0.1).

### 6.1 Localized active-axis selector

Let \(d\to\infty\), \(d=m^{o(1)}\), and let the dyadic packet dimension
\(r\) satisfy

\[
 {r\over d\log m}\to\infty,qquad
 \sqrt m\ll r=o(m).                                      \tag{6.1}
\]

Choose the first rank-twisted macroblocks whose coordinate union \(E\) has

\[
                         16r\le|E|<16r+2d.                 \tag{6.2}
\]

All but

\[
                   O(\sqrt m\,e^{-2r/d})W=o(W)             \tag{6.3}
\]

middle owners have at least \(r\) split axes in \(E\). Retaining \(r\) of
them gives a legal parallel-\(Q_r\) packet atlas. For every choice of exact
factor, order, affine phase, and every dependence between packet choices,
Corollary 5.1 gives, at \(q=A\sqrt m+O(1)\),

\[
 \boxed{
 M_q^\pm\ge(1-o(1))N_q=(e^{-A^2}-o(1))W.}                 \tag{6.4}
\]

This refutes an unspecified or localized retained-axis selector. It does
not refute the transversal-axis selector, which deliberately destroys the
common carrier \(E\).

### 6.2 Frozen terminal suffix

Let \(r\to\infty\), \(r=o(m)\), and

\[
 q=\lfloor A\sqrt m\rfloor\le\min\{H,r\}.                 \tag{6.5}
\]

Suppose every good component is supported before a fixed terminal suffix
\(R_0\subset[2m]\), where \(|R_0|/(2m)\to1/4\). With
\(s=|R_0|\), exact projection counting gives

\[
 \Delta_q^-=
 \sum_{k=0}^s\binom sk
 \left[
  \binom{2m-s}{m-q-k}-\binom{2m-s}{m-k}
 \right]_+,                                               \tag{6.6}
\]

\[
 \Delta_q^+=
 \sum_{k=0}^s\binom sk
 \left[
  \binom{2m-s}{m+q-k}-\binom{2m-s}{m-k}
 \right]_+.                                               \tag{6.7}
\]

If \(U_{\rm eff}\) owner occurrences can import across the suffix, then

\[
                         M_q^\pm\ge\Delta_q^\pm-U_{\rm eff}.
                                                               \tag{6.8}
\]

The audited completion envelopes

\[
 U_{\rm leave}+(3/2)^rU_{\rm bad},\qquad
 U_{\rm leave}+4^rU_{\rm bad}                              \tag{6.9}
\]

are \(e^{-\Omega(m)}W\). Writing

\[
 d=A\sqrt{2/3},\qquad
 \delta_A^{\rm suf}
 =e^{-A^2}\Phi(-d)-\Phi(-2d)>0,                            \tag{6.10}
\]

one obtains

\[
 \boxed{
 M_q^\pm\ge(\delta_A^{\rm suf}-o(1))W.}                  \tag{6.11}
\]

This survives arbitrary dependence, cube automorphisms, and
recursive/diverse orders as long as suffix projection and unit owner
incidence are preserved. For a fractional component mixture, the identical
bound holds for the lower-hinge deficit
\[
 D_q^\epsilon=\sum_T(1-\ell_q^\epsilon(T))_+,
\]
not for the cardinality of the zero set of a fractional load. A
moving-support atlas can evade the projection hypothesis.

The two envelopes in (6.9) have different audited scopes: \((3/2)^r\)
applies to the three rank-two support union, while \(4^r\) permits arbitrary
local states on the same \(4r\) active coordinates. Their
\(e^{-\Omega(m)}W\) evaluation assumes the canonical first-eligible
localization, or a causal/predictable mixed-seed scan together with the
audited imported-owner estimate. The bare projection inequalities
(6.6)--(6.8) are general once \(U_{\rm eff}\) is supplied.

### 6.3 One-touch first-eligible chronology

In the audited one-touch regime, with \(r\) dyadic and \(h=2r\),

\[
 r=m^{3/4+o(1)},\quad
 H=\left\lceil\sqrt{\beta m\log m}\right\rceil,
 \quad {1\over2}<\beta<1,                                 \tag{6.12}
\]

take

\[
 q=\left\lceil20\sqrt{r\log m}\right\rceil.              \tag{6.13}
\]

Every arbitrarily correlated integral support-preserving packet choice
obeys

\[
                         M_q^\pm=(1-o(1))W.                 \tag{6.14}
\]

For the corresponding fractional packet LP, the same statement holds with
\(M_q^\pm\) replaced by the lower-hinge deficit
\(\sum_T(1-\ell_q^\pm(T))_+\). Under (6.12)--(6.13), \(q\le H\) eventually.

The statewise source and target estimates are

\[
 {G_q\over W}\le C\sqrt m\,e^{-q^2/(4r+2)},               \tag{6.15}
\]

\[
 { |\mathcal Y_q^\pm|\over N_q}
 \ge1-C\sqrt m\left(e^{-q^2/(20r)}+e^{-cm}\right).        \tag{6.16}
\]

If \(B_q^\pm\) occurrence mass breaks one-touch chronology, the remaining
literal deficit is at least

\[
                         (1-o(1))W-B_q^\pm.                 \tag{6.17}
\]

This result is chronology-specific. Full cube permutations that revisit a
block are not covered; the suffix theorem is the robust statement when its
projection invariant remains.

### 6.4 Common-order factors and the corrected mixture threshold

If \(G_{\rm co}\) owners lie in \(Q_s\)-cells whose chosen factor has one
common cyclic direction order across its components, their signed depth-
\(q\) image has size at most

\[
                         {G_{\rm co}s\over2^q}.              \tag{6.18}
\]

Giving every other owner an arbitrary new target yields the direct support
cut

\[
 \boxed{
 M_q^\pm\ge
 \left[N_q-(W-G_{\rm co})-{G_{\rm co}s\over2^q}\right]_+.}
                                                               \tag{6.19}
\]

Thus a near-spanning common-order atlas with \(s\le2m\) has

\[
                         M_q^\pm\ge(e^{-A^2}-o(1))W         \tag{6.20}
\]

at \(q=A\sqrt m+o(\sqrt m)\). But if
\(G_{\rm co}=\alpha W\), (6.19) gives only

\[
 M_q^\pm\ge
 \left(\alpha+e^{-A^2}-1-o(1)\right)_+W.                  \tag{6.21}
\]

Therefore (6.19), and likewise the old pair/floor calculation, does not
exclude every positive-density common-order mixture for the \(L^1\) target.
Literal holes are forced by this particular cut only above the threshold

\[
                         \alpha>1-e^{-A^2}.                 \tag{6.22}
\]

The pair-collision estimate below this threshold is only a floor-energy
obstruction.

If a factor differs from a common-order reference on \(e_{\rm tail}\)
outgoing edge tails, then the statewise perturbation bound

\[
 |\operatorname {im}\tau_q^\pm|
 \le {Gs\over2^q}+q e_{\rm tail}                           \tag{6.23}
\]

is also a literal support theorem. It applies to sparse chronology
perturbations. The diverse compiler has not been supplied with a comparison
to a common-order reference having \(q e_{\rm tail}=o(W)\), so (6.23)
currently gives no useful bound for it.

### 6.5 Product-box owner lock

Inside the audited product-\(Q_3\) tensor sector, every hybrid
vertex-disjoint tiling of \(\mathcal V^r\) into literal \(Q_{3r}\) product
cells, with arbitrary cellwise Hamming orders and phases, reaches at most
the fraction

\[
 \rho_{r,q}
 =\left({3\over4}\right)^q{r-q+1\over\binom rq}            \tag{6.24}
\]

of the labelled lower family of size

\[
                         \binom rq16^q24^{r-q}.              \tag{6.25}
\]

\(K\) parent catalogues reach at most \(K\rho_{r,q}\). This is a literal,
statewise local support cut. It becomes a global \(W\)-scale hole theorem
only after proving that the locked sector has sufficient global mass and
that outside owners cannot fill the deficit. It does not constrain genuinely
non-box long-cycle mixing.

## 7. What does not force holes for every assignment

The following conclusions must not be advertised as deterministic
constant-one obstructions.

1. **Large floor energy.** It can coexist with perfect coverage by (1.9)
   and the examples after it.

2. **The negative-Gram quota.** It is an exact reformulation of
   \(\Delta=o(W)\), not of \(M=o(W)\).

3. **Pair-orbit covariance or a nonnegative cross-Gram.** Pair data cannot
   distinguish (1.10) from (1.11).

4. **Independent affine/order choices.** The binomial zero probability,
   Jensen lower bound, and concentration theorem genuinely give linear
   holes with high probability under the product distribution. They do not
   exclude a rare correlated assignment.

5. **A diffuse fractional orbit point.** Its product rounding may have
   linear expected holes even when its mean is flat. This refutes that
   rounding method, not the integral option family.

6. **A fixed-frame floor or lognormal score without a capacity upper
   bound.** The lower hinge of the specific fractional realization is an
   \(L^1\) obstruction to that realization, but not to every nonuniform
   routing in the same maximal graph.

7. **Degree-one imbalance by itself.** If \(N_x\) targets contain a
   coordinate \(x\), and total load on them is \(S_x\), the valid cuts are

   \[
    M\ge(N_x-S_x)_+,qquad
    M\ge((N-N_x)-(G-S_x))_+.                       \tag{7.1}
   \]

   A large centered degree-one coefficient which violates neither cut need
   not create a hole.

8. **Cylinder singularity, total variation, \(M\)-convex/TU/Graver
   failure, or post-hoc raw packetization failure.** These are method or
   labelled-allocation obstructions unless converted into a statewise
   invariant-target capacity cut of the form (3.3).

9. **Small common-order subfamilies.** Only the positive part in (6.21) is
   a literal hole conclusion. Their collision energy below that threshold
   may fit entirely inside the unavoidable repeat budget \(G-N_q\).

## 8. Exact remaining grouped \(L^1\) problem

First freeze an owner-exact packet atlas. Let \(\Omega_P\) be the legal
whole-factor states of packet \(P\), assume every option is trace-injective,
and let

\[
 a_{P,\omega,c,T}
 =\mathbf1_{\{T\in I_{P,c}^{\omega}\}}.                   \tag{8.1}
\]

One state must be chosen for every packet and used simultaneously at every
signed depth. The exact finite optimization is

\[
 \begin{aligned}
 \min\quad&\sum_{c,T}z_{c,T},\\
 \text{subject to}\quad
 &z_{c,T}+\sum_{P}\sum_{\omega\in\Omega_P}
       a_{P,\omega,c,T}x_{P,\omega}\ge1,\\
 &\sum_{\omega\in\Omega_P}x_{P,\omega}=1
       \qquad(P\in\mathcal P),\\
 &x_{P,\omega}\in\{0,1\},\qquad z_{c,T}\ge0.
 \end{aligned}                                             \tag{8.2}
\]

For integral \(x\), an optimum has

\[
                         z_{c,T}=(1-L_c(T))_+,              \tag{8.3}
\]

so (8.2) has value exactly \(\mathfrak H\) for that frozen atlas. Constant
one requires a sequence of literal owner-exact atlases and common state
choices for which this value is \(o(W)\).

The physical handoff then has \(o(W)\) cost only if the components remain
intact cyclic strips or one invokes the audited \(O(H)\)-length
repeated-prefix/boundary-dummy fusion. Raw deletion of all starts within
distance \(q\) of every cut has an \(O(H^2)\), not \(O(H)\), toll per
component and is not justified by the component count alone.

If legal moves can change the matching, selector, or packet decomposition,
there is an outer minimization over those literal owner-exact atlases.
Equivalently, every coupled \(Q_{R+1}\) slab trade or retiling must appear
as one larger choice group in (8.2); it cannot be represented by
independent variables for the packets it couples. Thus (8.2) is the exact
inner grouped problem after the atlas is frozen, not a claim that the full
legal state space has already been parametrized by fixed packets.

The hereditary conditions \(\mathrm{HD}_{\rm Hall}\) and
\(\mathrm{HD}_1\) are respectively sharp for the ungrouped reachability
relaxation and for invariant-fibre capacities. Passing either is not a
rounding theorem for (8.2). The still-missing positive theorem must exploit
cross-parent dispersion and correlated packet choices while respecting
the one-state-for-all-depths constraint.

## 9. Precise corrected boundary

The following parts of the earlier Fourier/floor report survive unchanged
for the exact constant-one objective:

* the diverse-order compiler synthesis and literal within-packet trace
  injectivity;
* the exact repeat identity;
* the ambient physical Walsh identity as an intersection formula;
* the independent-product linear-hole theorem, with its probabilistic
  scope;
* the localized carrier-\(E\) every-assignment obstruction;
* any explicit physical tag or target-subset capacity cut.

The following do not survive as necessary conditions for constant one:

* linear expected floor excess;
* deterministic adjacent-floor balance;
* the order-\(W\) negative cross-Gram requirement;
* exclusion of every positive-density common-order mixture based only on
  pair collisions.

No general dispersed diverse-order atlas is disproved here. Conversely, no
common correlated state assignment with \(\mathfrak H=o(W)\) is constructed.
The proved boundary is exactly the hereditary \(L^1\) support conditions
\(\mathrm{HD}_{\rm Hall}\) and \(\mathrm{HD}_1\), together with the listed
statewise localized obstructions.

## 10. Independent audit

Three independent proof audits checked:

* all three positive-part forms in Theorem 3.1, including the exact
  \(2G-N-S\) normalization and the \(G\)-versus-\(W\) completion baseline;
* the Hall--Berge equality \(G-d_c\) in Section 4.1 and the validity of
  summing contextwise suprema despite a common global state;
* the uniform small-carrier estimate, where the product calculation in
  fact gives the stronger exponent
  \(-(3/2-o(1))q^2/e\), so the displayed \(3/5\) constant is safe;
* the frozen-suffix constant \(\delta_A^{\rm suf}\), one-touch scales,
  common-order mixture threshold, and product-\(Q_3\) scope.

The audits found no remaining mathematical correction after the explicit
shallow-depth leave hypothesis, fractional lower-hinge notation, and
fixed-atlas/outer-retiling distinction were inserted above.
