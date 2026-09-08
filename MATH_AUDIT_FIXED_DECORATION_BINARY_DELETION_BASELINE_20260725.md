# Fixed priority decorations: binary deletion is exact, but the proposed degree baseline is not

Date: 2026-07-25

Method: pure mathematics only. No computation, search, or solver is used.

## 0. Verdict

After expanding every base chunk into all of its fixed priority copies, the
committed residual catalogue is indeed a literal sub-multihypergraph of the
initial decorated catalogue. In particular, all decorated codegrees are
pathwise nonincreasing. The factorial priority update is only a quotient
count of surviving fixed copies; it neither changes a surviving copy's claim
set nor assigns it a nonintegral weight.

This validates the following conditional implication. If, for one common
number \(\zeta_t\), every relevant live fibre satisfies

\[
 d_t(v)\ge \zeta_t d_0(v),                                      \tag{0.1}
\]

then normalized pair squares inflate by at most \(\zeta_t^{-2}\), and
normalized common-link triangles inflate by at most \(\zeta_t^{-3}\).
There is also a direct configuration-count proof that the exact scalar
common-killer square inflates by at most \(\zeta_t^{-3}\).

The proposed variance closure does **not** follow from the degree stopping
theorem currently proved. The symbol \(z_t\) in the conditioned recurrence
is resource density:

\[
 z_t=\prod_{s<t}q_s,
\]

whereas the one-root decorated degree reference is

\[
 \rho_{1,s}=q_s^{g-1},\qquad
 \prod_{s<t}\rho_{1,s}=z_t^{g-1}.                              \tag{0.2}
\]

Thus the stopped lower bound presently available, conditional on its
predictable mean statement, is

\[
 d_t(v)\ge (1-o(1))z_t^{g-1}d_0(v),                            \tag{0.3}
\]

not \((1-o(1))z_td_0(v)\). Binary deletion alone consequently gives only

\[
 S_t\le (1-o(1))^{-2}z_t^{-2(g-1)}S_0,
\qquad
 \mathfrak T_t\le (1-o(1))^{-3}z_t^{-3(g-1)}\mathfrak T_0.     \tag{0.4}
\]

At \(z_t=1/\log m\) and \(g=m^{1/2+o(1)}\), the second factor in
(0.4) is

\[
 (\log m)^{3(g-1)}
 =\exp\!\bigl((3+o(1))g\log\log m\bigr),                       \tag{0.5}
\]

so it overwhelms the raw \(m^{-1+o(1)}\) triangle by a
superpolynomial factor. The stopped-Doob variance ledger is therefore not
closed by monotonicity at the present baseline.

There are exactly two valid continuations.

1. Prove the much stronger coherent mean theorem
   \(d_t(v)\ge(1-o(1))z_td_0(v)\). Conditional on that new theorem, the
   variance does close automatically and only predictable mean-spread
   remains.
2. Prove contraction of pair/common-link numerators at their natural
   \(z_t^{g-2}\)-type scale. This is the conditioned link-mean/four-walk
   statement which the monotonicity proposal was meant to bypass.

Allowing a live chunk to shed blocked phase columns could change the
one-root baseline, but that is not binary deletion of fixed full-chunk
decorations. It is a separate shortened-chunk/token recombination
architecture and needs a new raw catalogue and a new physical seam ledger.

No coefficient-one conclusion follows from binary deletion alone.

## 1. The fixed decorated catalogue

Fix all static choices before the nibble starts:

* the labelled geodesic chunks and their tags;
* the coordinate labellings and symmetrizing copies;
* the calibrated integers \(c_q\), or their once-for-all modified values
  \(\bar c_q\);
* the bad-grid relation used by dynamic quarantine; and
* the complete set of priority orders on the \(g\) phase columns.

For a base chunk \(P\) and a priority order \(\pi\), let

\[
 e=(P,\pi)                                                       \tag{1.1}
\]

be a labelled decoration. Its resource set is fixed:

\[
 R(e)=\{\tau(P)\}\cup O(P)\cup C(P,\pi),                       \tag{1.2}
\]

where \(O(P)\) is the set of its \(g\) middle owners and
\(C(P,\pi)\) is the set of protected targets claimed by the fixed height
profile assigned by \(\pi\). Distinct labelled priorities remain distinct
edges even when they happen to have equal resource sets. Thus the natural
object is a multihypergraph.

Let \(\widehat{\mathcal E}_0\) be the set of all such decorations after
the once-for-all initial pruning. Let \(Z_t\) be the used resource set,
\(S_t\) the committed selected chunks, and \(D_t^{\rm aux}\) any set of
decorations voluntarily discarded by the auxiliary wasteful restriction.
Let \(B\) be the fixed bad-grid relation. Then the committed live edge set
is of the form

\[
\begin{aligned}
 \widehat{\mathcal E}_t
 =\{e=(P,\pi)\in\widehat{\mathcal E}_0:
 &R(e)\cap Z_t=\varnothing,\\
 &P\notin N_B(S_t),\\
 &e\notin D_t^{\rm aux}\}.
\end{aligned}                                                   \tag{1.3}
\]

Every set on the right which records a prohibition is increasing in
\(t\). Consequently

\[
 \boxed{\widehat{\mathcal E}_{t+1}
        \subseteq\widehat{\mathcal E}_t
        \subseteq\widehat{\mathcal E}_0.}                      \tag{1.4}
\]

This statement is pathwise and does not depend on the law used to choose
the selected chunks.

### Proposition 1.1 (the factorial update is a deletion count)

For every base chunk \(P\), let

\[
 a_t(P)=\#\{\pi:(P,\pi)\in\widehat{\mathcal E}_t\}.            \tag{1.5}
\]

Then \(a_{t+1}(P)\le a_t(P)\). Moreover the exact deadline factorial
formula for \(\Pi_t(P)\) equals (1.5), after the owner and quarantine
indicators are included.

#### Proof

For fixed \(\pi\), the set \(C(P,\pi)\) is determined before time zero.
The priority is feasible at time \(t\) precisely when every target in this
fixed set is still available. The deadline Hall inequalities are an exact
way to count the priorities with this property: sorting phases by their
first blocked depths counts the bijections of phases to the fixed priority
slots. Hence the factorial expression is the sum of the zero-one
indicators

\[
 \Pi_t(P)=\sum_\pi
 \mathbf 1_{\{C(P,\pi)\cap Z_t=\varnothing\}}.                 \tag{1.6}
\]

Used-target sets only grow, so each summand can change only from one to
zero. Owner loss or quarantine sets all the summands above \(P\) to zero.
This proves the proposition. \(\square\)

The changing first-block class of a phase is therefore only a quotient
statistic used to evaluate (1.6). It does not change the claims of any
surviving decorated edge.

## 2. Operation-by-operation audit

The following operations preserve (1.4).

### 2.1 Static floor and deadline corrections

The floors defining \(c_q\), and the later harmless enlargement of the
deadline allowances \(d_q\), are chosen once before
\(\widehat{\mathcal E}_0\) is defined. They change the initial fixed
claim sets but are not runtime operations. A further history-dependent
change of \(c_q\) or \(d_q\) would generally change an edge's claim set
and would not be covered by (1.4). No such runtime change occurs in the
audited nibble.

### 2.2 Owner, tag, and target consumption

Using a tag, owner, or protected target deletes every decorated edge
containing that fixed resource. This is ordinary incident-edge deletion.
A target fibre must be stopped immediately before its own consuming jump;
that lifetime convention changes neither (1.3) nor (1.4).

### 2.3 Adaptive choice of a priority

Choosing a priority after observing the current forbidden targets selects
one of the surviving edges \((P,\pi)\). It does not turn one priority copy
into another. If one works only with the quotient base object \(P\), the
operation looks like reprioritization, but (1.6) proves that the quotient
weight is an integer multiplicity of fixed copies.

There is, however, a probabilistic caveat. If priorities for several
tentative base grids are chosen jointly after seeing the whole bite, then
resampling one tag can change the final priority chosen for other tags.
Nestedness (1.4) still holds, but a local Efron--Stein influence bound does
not follow from nestedness alone. The exact common-killer quadratic-
variation identity applies when the tentative variable is a fixed
decorated choice, or when the stated auxiliary wasteful restriction
permanently deletes the fixed conflict neighbourhood of every tentative
decorated choice. This is a locality requirement, not a failure of binary
deletion.

### 2.4 Parallel activation and alteration

Activation, rejection of a tentative choice, and normalization by the
current tag degree change only the sampling law. A rejected candidate may
remain live; an accepted candidate causes the incident deletions of
Section 2.2. The optional auxiliary rule which discards conflicts of even
rejected tentative choices is again only deletion, provided that discard
is permanent as stated.

### 2.5 Dynamic quarantine

The bad relation \(B\) is determined by the two full base grids and is
fixed. After selecting \(S_t\), quarantine removes

\[
 \bigcup_{E\in S_t}N_B(E).                                     \tag{2.1}
\]

Since \(S_t\) grows, this is monotone deletion of all priority copies over
the affected base grids. The relation is not resource intersection, so its
direct loss is handled by the separate deterministic quarantine ledger;
it does not invalidate codegree monotonicity of the remaining catalogue.

### 2.6 Conditioning and stopping

Conditioning on one or two roots surviving, and renormalizing the current
tag law, do not alter the pathwise edge set. In the parallel bite the
conditioned per-tag denominator is \(1-\alpha q_U\ge1-\alpha\). Thus
removing direct root hits can only reduce common-killer numerators and
costs at most the harmless factor \((1-\alpha)^{-1}\). A certainly-active
sequential law instead has denominator \(1-q_U\); binary deletion gives no
lower bound for that denominator.

Declaring a fibre stopped is analytic. If the construction also discards
the corresponding candidates physically, that is again deletion.

No relabelling, release of a used target, unquarantine, or creation of a
new full priority copy occurs in the audited process.

## 3. Exact consequences of binary deletion

For a resource vertex \(x\), and two resource vertices \(x,y\), write

\[
 d_t(x)=\#\{e\in\widehat{\mathcal E}_t:x\in R(e)\},
 \qquad
 d_t(x,y)=\#\{e\in\widehat{\mathcal E}_t:x,y\in R(e)\}.        \tag{3.1}
\]

Equation (1.4) gives

\[
 d_t(x,y)\le d_0(x,y).                                        \tag{3.2}
\]

Allow rank- or type-dependent lower factors \(\lambda_t(x)>0\):

\[
 d_t(x)\ge\lambda_t(x)d_0(x).                                 \tag{3.3}
\]

Then

\[
 \boxed{
 K_t(x,y)\le
 [\lambda_t(x)\lambda_t(y)]^{-1/2}K_0(x,y).}                  \tag{3.4}
\]

This follows immediately by using (3.2) in the numerator and (3.3) in
the two denominators.

Consequently, if \(\lambda_t(v)\ge\lambda_t\) for all vertices in the
relevant blocks, then

\[
 \boxed{
 \sum_{y\in V_j}K_t(x,y)^2
 \le\lambda_t^{-2}\sum_{y\in V_j}K_0(x,y)^2,}                 \tag{3.5}
\]

and, since all summands are nonnegative,

\[
 \boxed{
 \sum_{y,z}K_t(x,y)K_t(y,z)K_t(z,x)
 \le\lambda_t^{-3}
 \sum_{y,z}K_0(x,y)K_0(y,z)K_0(z,x).}                          \tag{3.6}
\]

### Proposition 3.1 (direct common-killer domination)

Let \(F\) be a victim fibre and let \(U\) range over current choice-tag
fibres. Let \(\Gamma\) be any fixed incompatibility relation on decorated
edges. Put

\[
 L_t(F,e)=
 \#\{f\in\widehat{\mathcal E}_t\cap F:(f,e)\in\Gamma\},       \tag{3.7}
\]

and

\[
 J_t(F)=
 \sum_U\frac1{d_t(U)}
 \sum_{e\in\widehat{\mathcal E}_t\cap U}
 \left(\frac{L_t(F,e)}{d_t(F)}\right)^2.                       \tag{3.8}
\]

If

\[
 d_t(F)\ge\lambda_Fd_0(F),
 \qquad d_t(U)\ge\lambda_Ud_0(U),                             \tag{3.9}
\]

then

\[
 \boxed{
 J_t(F)\le
 \lambda_F^{-2}(\inf_U\lambda_U)^{-1}J_0(F).}                 \tag{3.10}
\]

#### Proof

For every surviving \(e\), deletion gives

\[
 L_t(F,e)\le L_0(F,e).                                        \tag{3.11}
\]

Also the outer sum in (3.8) ranges over a subset of its time-zero
decorated choices. Hence its unnormalized numerator is at most the
time-zero numerator. Applying the three denominator bounds in (3.9)
proves (3.10). \(\square\)

For a common lower factor \(\lambda_t\), Proposition 3.1 gives exactly
\(J_t(F)\le\lambda_t^{-3}J_0(F)\). It avoids any need to pass through an
abstract pair-square functional. It still requires the correct lower
factor \(\lambda_t\).

### Proposition 3.2 (the powers in (3.5)--(3.6) are sharp)

For every rational \(0<\lambda<1\), there is a finite fixed decorated
hypergraph and a literal subhypergraph for which every one of three
tracked degrees is multiplied by \(\lambda\), every tracked pair
codegree is unchanged, and the corresponding pair square and triangle
inflate by exactly \(\lambda^{-2}\) and \(\lambda^{-3}\).

#### Proof

Choose integers \(c<D\) with \(c/D=\lambda\). Take vertices \(x,y,z\).
Make \(c\) distinct edges containing all three, distinguishing them with
private vertices. For each \(v\in\{x,y,z\}\), add \(D-c\) distinct
private edges containing \(v\) and no other one of \(x,y,z\). Thus

\[
 d_0(x)=d_0(y)=d_0(z)=D,
 \qquad d_0(x,y)=d_0(y,z)=d_0(z,x)=c.                           \tag{3.12}
\]

Retain only the \(c\) common edges. Then every tracked degree is \(c\),
and every tracked pair codegree remains \(c\). Hence every normalized
pair entry changes from \(c/D=\lambda\) to one. Its square inflates by
\(\lambda^{-2}\), and the product around the triangle inflates by
\(\lambda^{-3}\). \(\square\)

Thus no better power can follow from binary deletion and one-root lower
bounds alone.

## 4. The baseline mismatch

The conditioned one-bite recurrence fixes the notation

\[
 \rho_{1,t}=q_t^{g-1},
 \qquad \rho_{2,t}=q_t^{g-2},                                  \tag{4.1}
\]

and defines resource density by

\[
 z_t=\prod_{s<t}q_s.                                           \tag{4.2}
\]

The stopped scalar degree martingale is normalized by its predictable
reference contraction, not by resource density itself:

\[
 X_{t,F}=
 \log\frac{D_t(F)}{D_0(F)\prod_{s<t}\rho_{s,\operatorname{str}(F)}}.
                                                                    \tag{4.3}
\]

Under the one-root reference (4.1), and allowing a cumulative \(1-o(1)\)
mean error, (4.3) can give only

\[
 D_t(F)\ge(1-o(1))z_t^{g-1}D_0(F).                             \tag{4.4}
\]

Neither the abstract stopped-Doob lemma nor its logarithmic version
changes the reference product in (4.3). They control fluctuations around
the compensator. They do not prove that the compensator contracts by
\(q_t\) instead of \(q_t^{g-1}\).

There is a simple exact model showing why linear density is not a
consequence of full-edge deletion. Let \(\mathcal H_0\) be the complete
\(g\)-partite \(g\)-uniform hypergraph with \(N\) vertices in every part.
Retain exactly \(zN\) vertices in every part and take the induced
subhypergraph \(\mathcal H_z\), where \(zN\) is integral. Every retained
vertex then has

\[
 \frac{d_z(v)}{d_0(v)}
 =\frac{(zN)^{g-1}}{N^{g-1}}=z^{g-1},                           \tag{4.5}
\]

and every retained pair from distinct parts has codegree ratio
\(z^{g-2}\). This is literal deletion of fixed edges. It disproves any
general implication

\[
 \text{resource density }z
 \quad\Longrightarrow\quad d_z(v)\ge zd_0(v)                  \tag{4.6}
\]

for \(g>2\). It also shows why the missing numerator contraction matters:
using the actual \(z^{g-2}\) pair contraction gives the ideal normalized
factor \(z^{-1}\), whereas discarding it and using monotonicity gives the
much worse \(z^{-(g-1)}\).

### 4.1 Exact failure of the proposed aggregate ledger

Use the strengthened raw triangle

\[
 \mathfrak T_0=m^{-1+o(1)},                                   \tag{4.7}
\]

the number \(Q=m^{1/2+o(1)}\) of protected strata, and effective time
\(O(\log\log m)\). Applying Proposition 3.1 with the actual scalar
baseline (4.4) gives at best

\[
\begin{aligned}
 B_m^{\rm mono}
 &\le
 Q\log\log m\;m^{-1+o(1)}z_t^{-3(g-1)}.                       \tag{4.8}
\end{aligned}
\]

At \(z_t=1/\log m\),

\[
 B_m^{\rm mono}
 =m^{-1/2+o(1)}(\log m)^{3(g-1)}\log\log m.                   \tag{4.9}
\]

Taking logarithms,

\[
 \log B_m^{\rm mono}
 =3(g-1)\log\log m-(1/2+o(1))\log m.                          \tag{4.10}
\]

Since \(g=m^{1/2+o(1)}\), the first term in (4.10) dominates the
second and tends to infinity. Hence (4.8) is not merely too weak for
\(o(1)\); it is superpolynomially large.

If instead one stops while the **decorated degree density** is at least
\(1/\log m\), (4.5) permits resource density only down to

\[
 z_t\ge
 \exp\left(-\frac{\log\log m}{g-1}\right)
 =1-(1+o(1))\frac{\log\log m}{g}.                              \tag{4.11}
\]

This consumes only a vanishing resource fraction and is far from the
required resource density \(1/\log m\).

## 5. What remains true about the stopped bootstrap

Suppose one proves the genuinely stronger predictable mean theorem

\[
 d_t(v)\ge(1-o(1))z_td_0(v)                                   \tag{5.1}
\]

for every nonexceptional surviving tag and protected-target fibre, with
\(z_t\ge1/\log m\). Then Sections 3 and 4 immediately give

\[
 \mathfrak T_t(v)\le
 (1+o(1))z_t^{-3}m^{-1+o(1)}=m^{-1+o(1)},                      \tag{5.2}
\]

and therefore

\[
 Q\log\log m\sup_{t,v}\mathfrak T_t(v)
 =m^{-1/2+o(1)}.                                               \tag{5.3}
\]

Up to the root-survival lifetime convention and the fixed-local-killer
condition of Section 2.3, the weighted stopped-Doob theorem would then
charge only

\[
 O(B_m^{1/2}W)=o(W),
 \qquad B_m=m^{-1/2+o(1)}.                                    \tag{5.4}
\]

Thus the proposed simplification is a correct **conditional reduction**:
linear one-root degree survival implies automatic variance control. It is
not a consequence of the stopped theorem already available. Establishing
(5.1) requires replacing the current mean reference
\(q_t^{g-1}\) by \(q_t\), i.e. proving coherent survival of almost whole
chunks under substantial resource depletion. That is a new mean-level
theorem, not a covariance estimate.

## 6. The phase-column deletion fork

A possible way to avoid the exponent \(g-1\) is to stop treating a full
\(g\)-column decorated chunk as indivisible. If a blocked phase column is
removed while the remaining columns stay available, a candidate changes
from

\[
 e=(P,\pi)
 \quad\hbox{to}\quad
 e_I=\text{the restriction of }(P,\pi)\text{ to surviving columns }I.
                                                                    \tag{6.1}
\]

Unless \(e_I\) was already a separately labelled edge of the initial
catalogue, (6.1) is edge mutation, not deletion. In the current full-
decoration hypergraph, losing any one of the \(g\) required middle owners
deletes \(e\); priority only changes which shallow targets are claimed and
does not remove that middle-owner requirement.

One may pre-expand every \(e_I\) as a fixed object, but then one has made a
different catalogue. Its tag degrees, target degrees, multiplicities, and
raw pair/common-link statistics must be recalculated. In addition, the
chosen column tokens must be recombined into literal contiguous chunks.
Deleting internal columns can split one chunk into several runs, so the
number of new endpoints and the associated OR-word seams require an
explicit \(o(W)\) ledger.

The minimum phase-column deletion theorem in the existing residual-chain
report is a statement about restoring deadline feasibility and producing
structured donor chains. It is not presently an operation of the fixed
full-chunk nibble. It therefore cannot be used to replace
\(z_t^{g-1}\) by \(z_t\) inside the binary-deletion proof.

An exact positive theorem on this fork would need all three clauses:

1. a fixed initial column-token or all-subchunks catalogue with calibrated
   degree and raw triangle bounds;
2. a monotone selection rule whose residual one-token degrees remain
   linear in resource density; and
3. a reconstruction theorem grouping the selected tokens into legal
   chunks with total new run/seam cost \(o(W)\).

None of these clauses is supplied by the current fixed-decoration
expansion.

## 7. Precise proved/conditional boundary

The audit proves:

1. All current priority, owner, target, tag, and past-current quarantine
   updates are binary deletion after full fixed-priority expansion.
2. The exact priority factorials are integral surviving-copy counts.
3. Binary deletion plus a common degree lower factor \(\lambda\) gives
   exactly \(\lambda^{-2}\) pair-square and \(\lambda^{-3}\)
   common-link inflation; these exponents are sharp.
4. If the factor were \((1-o(1))z_t\), the global variance ledger would
   close at \(m^{-1/2+o(1)}W\).
5. The current conditioned recurrence and stopped normalization instead
   supply the reference \((1-o(1))z_t^{g-1}\). Monotonicity at this
   reference is non-summable by (4.9)--(4.10).

Therefore the hereditary variance gate has not been closed unconditionally.
It has been reduced to one of two exact statements:

\[
 \boxed{\text{linear coherent one-root mean survival (5.1)}}
\]

or

\[
 \boxed{\text{natural pair/common-link numerator contraction}.}
\]

Phase-column deletion is a third architectural fork, but it lies outside
the fixed full-decoration subhypergraph and needs a new recombination
theorem.
