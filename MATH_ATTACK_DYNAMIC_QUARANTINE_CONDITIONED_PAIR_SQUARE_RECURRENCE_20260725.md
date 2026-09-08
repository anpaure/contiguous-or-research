# The survival-conditioned one-bite pair-square recurrence

Date: 2026-07-25

Method: pure mathematics only. No computation, search, or solver is used.

## 0. Outcome

This note gives the exact one-bite recurrence which the dynamic-quarantine
four-walk lane needs.  There are two corrections which cannot be omitted.

1. A target fibre has to be followed **conditional on its root target
   surviving**.  For a pair link, both roots have to survive.  Otherwise a
   chunk which deliberately consumes a root contributes loss one, and the
   resulting diagonal has total size

   \[
      \Theta(KT)=\Theta(W\sqrt m),
   \]

   rather than \(o(W)\).
2. The raw two-link census has to hold under the current pair-link law,
   after owner/priority conditioning and after conditioning on the two roots
   surviving.  A raw or full-cube estimate does not have this quantifier.

After these corrections, the recurrence is short.  Let \(q_t\) be the
one-bite resource-retention factor, let

\[
 \rho_{1,t}=q_t^{g-1},\qquad \rho_{2,t}=q_t^{g-2},                 \tag{0.1}
\]

and let \(S_{t,h}(x)\) be one block of the normalized pair-square row.
If the conditioned pair-link mean contracts by \(\rho_{2,t}\), the
conditioned four-walk is at most \(\beta_m S_{t,h}(x)\), and surviving
one-root degrees contract by \(\rho_{1,t}\), then

\[
 \boxed{
 \mathbb E\!\left[S_{t+1,h}(x)\mid x\text{ survives},\mathcal F_t\right]
 \le q_t^{-2}
 \left(1+C\epsilon_t+C\alpha_t\beta_m\right)S_{t,h}(x).}        \tag{0.2}
\]

Here \(\alpha_t\) is the tag activation probability and \(\epsilon_t\)
contains the stated mean- and degree-balance errors.  Therefore, if

\[
 \sum_t\epsilon_t=o(1),\qquad
 \sum_t\alpha_t=O(\log\log m),\qquad
 \beta_m=m^{-1/2+o(1)},                                           \tag{0.3}
\]

then, for \(z_t=\prod_{s<t}q_s\ge1/\log m\),

\[
 \boxed{
 \mathbb E\!\left[S_{t,h}(x)\mid x\text{ survives to time }t\right]
 \le(1+o(1))z_t^{-2}S_{0,h}(x).}                                 \tag{0.4}
\]

Thus the numerical recurrence closes all the way to \(1/\log m\).

What is **not** proved by the currently stated cube and \(\beta\) inputs is
the conditioned hypothesis used in (0.2).  The \(m^{-4+o(1)}\) cube
deletion estimate concerns quarantine under the raw cube measure.  The
owner/priority history may force a rare face, and conditioning a raw event
of mass \(\beta\) on a face of mass \(\theta\) permits inflation to
\(\min(1,\beta/\theta)\).  A one-generation branching estimate also does
not tensorize: all witness events may be the same event.

The exact sufficient strengthening is a **fresh, pair-rooted branching
statement**: after every history and every partial witness tree, the next
new branch has conditional mass at most \(\beta_m\), and a failed pair-link
contraction supplies many distinct admissible branches.  Section 6 proves
that this strengthening, combined with the logarithmic swap-face reservoir,
makes the exceptional probability superpolynomially small.  The natural raw
interpretation does not imply it.  This is the precise proved/conditional
boundary; no coefficient-one conclusion is claimed.

The later cover/remainder refinement improves the triangle scale from the
naive \(g/m\) bound to \(m^{-1+o(1)}\).  Section 9 proves that this is
enough for one global stopped corridor for the **scalar** degree
martingales.  It also shows why the same stop does not automatically lift
to the pair-square functional: its quadratic variation contains a
cross-physical-label square not present in the scalar triangle.

## 1. Fixed decorations and pair-square blocks

Expand every currently feasible priority order as a fixed decorated
candidate.  A later history only deletes such decorations: it never changes
which targets a surviving decoration claims.  Let

\[
 d_t(x)=\#\{P:x\in P\},\qquad
 d_t(x,y)=\#\{P:x,y\in P\}.                                      \tag{1.1}
\]

The same formulas apply to integral multiplicities.  Put

\[
 K_t(x,y)={d_t(x,y)\over\sqrt{d_t(x)d_t(y)}}                      \tag{1.2}
\]

and, for a protected rank stratum \(V_{r+h}\),

\[
 S_{t,h}(x)=
 \sum_{\substack{y\in V_{r+h}\\y\ne x}}K_t(x,y)^2.             \tag{1.3}
\]

The raw calculation gives, with a fixed constant \(C_0\),

\[
 S_{0,0}(x)\le C_0m^{-2},                                        \tag{1.4}
\]

and, for \(h\ne0\),

\[
 S_{0,h}(x)
 \le C_0(|h|+1)^2|h|!\left({C_0\over m}\right)^{|h|}.           \tag{1.5}
\]

Fixed-decoration monotonicity gives

\[
 d_{t+1}(x,y)\le d_t(x,y).                                      \tag{1.6}
\]

It does **not** by itself give (0.4).  If one-root degrees have their
ordinary fixed-decoration scale \(z^{g-1}\), then using only (1.6) loses
\(z^{-2(g-1)}\).  The desired \(z^{-2}\) uses the additional contraction
\(d_t(x,y)\sim z^{g-2}d_0(x,y)\).  This distinction is the reason for
tracking pair links below.

## 2. The exact pair-root survival law

First record why conditioning is compulsory.  For a current target fibre
\(F_x\), let \(I_x(E)\) be its fractional loss when tentative chunk \(E\)
is emitted.  If \(x\in C(E)\), every member of \(F_x\) is deleted, and
hence

\[
 I_x(E)=1.                                                       \tag{2.0}
\]

It follows for every emitted chunk that

\[
 \sum_{x\ {\rm available}} I_x(E)^2\ge |C(E)|.                  \tag{2.0a}
\]

In the protected catalogue,

\[
 K:=|C(E)|=g+2\sum_{q\le Q}\bar c_q^{(g)}
          =\Theta(g\sqrt m).                                    \tag{2.0b}
\]

Indeed \(\bar c_q^{(g)}=\Theta(g)\) for \(q\le c\sqrt m\), by the
central-binomial ratio, while Gaussian summation gives the matching upper
bound; the floor/deadline correction is \(o(g)\) in total and does not
change the order.  A run emits \((1-o(1))T\) chunks, where
\(T=(1+o(1))W/g\).  Summing (2.0a) therefore gives

\[
 \sum_E\sum_x I_x(E)^2\ge(1-o(1))KT=\Theta(W\sqrt m).            \tag{2.0c}
\]

Thus an unconditioned \(o(W)\) transfer ledger is false for a purely
diagonal reason.  The fibres in (2.0) have been deliberately consumed and
should no longer be propagated.

At one parallel bite, tag \(U\) is inactive with probability
\(1-\alpha\), and otherwise chooses \(E\) according to its current law
\(\nu_U\).  For two currently available roots \(x,y\), write

\[
 q_U(x,y)=
 \Pr_{E\sim\nu_U}\bigl(C(E)\cap\{x,y\}\ne\varnothing\bigr).     \tag{2.1}
\]

Let \(\mathcal A_{xy}\) be the event that the bite consumes neither
\(x\) nor \(y\).  Independence between tags gives

\[
 \Pr(\mathcal A_{xy})=
 \prod_U\bigl(1-\alpha q_U(x,y)\bigr).                           \tag{2.2}
\]

Conditional on \(\mathcal A_{xy}\), tag variables remain independent,
and their exact laws are

\[
 \Pr(X_U=\varnothing\mid\mathcal A_{xy})
 ={1-\alpha\over1-\alpha q_U(x,y)},                              \tag{2.3}
\]

\[
 \Pr(X_U=E\mid\mathcal A_{xy})
 ={\alpha\nu_U(E)
   \mathbf1_{\{C(E)\cap\{x,y\}=\varnothing\}}
  \over1-\alpha q_U(x,y)}.                                      \tag{2.4}
\]

The denominator in (2.4) is at least \(1-\alpha\).  This is harmless in
a parallel bite.  In a sequential process which certainly samples an
activated tag, the corresponding denominator is \(1-q_U(x,y)\); an
aggregate load estimate does not keep it away from zero.  Thus the parallel
and sequential formulations are not interchangeable without a same-tag
denominator bound.

For a decoration \(P\supseteq\{x,y\}\) and a chunk \(E\) avoiding the
two roots, let \(h^\circ_t(P,E)\in[0,1]\) be the exact fraction of the
pair-link decoration killed by conflicts away from \(x,y\).  In the fully
expanded catalogue it is binary.  Put

\[
 p_{t,xy}(P)={1\over d_t(x,y)}
 \mathbf1_{\{P\supseteq\{x,y\}\}},                              \tag{2.5}
\]

and

\[
 a_{U,xy}(E)=
 \sum_Pp_{t,xy}(P)h_t^\circ(P,E).                                \tag{2.6}
\]

The survival-conditioned pair-link four-walk is

\[
 \boxed{
 J_t^\circ(x,y)=
 \sum_U{1\over1-\alpha q_U(x,y)}
 \mathbb E_{E\sim\nu_U}
 \left[
  \mathbf1_{\{C(E)\cap\{x,y\}=\varnothing\}}
  a_{U,xy}(E)^2
 \right].}                                                       \tag{2.7}
\]

This is the pair-rooted version of the exact kernel in the pair-square
report.  Direct consumption of either root is absent.

### Lemma 2.1 (conditioned pair-link variance)

Let

\[
 R_t(x,y)={d_{t+1}(x,y)\over d_t(x,y)}                            \tag{2.8}
\]

on \(\mathcal A_{xy}\), before deleting newly exceptional roots.  Then

\[
 \boxed{
 \operatorname {Var}
  \bigl(R_t(x,y)\mid\mathcal A_{xy},\mathcal F_t\bigr)
 \le2\alpha J_t^\circ(x,y).}                                    \tag{2.9}
\]

#### Proof

Resample one conditioned tag variable \(X_U\).  Changing it can alter only
decorations killed by the old or the new choice.  Therefore the absolute
change in the normalized pair-link degree is at most

\[
 a_{U,xy}(X_U)+a_{U,xy}(X'_U).
\]

The square is at most twice the sum of the two squares.  Under (2.3)--(2.4),
the expectation of either square is

\[
 {\alpha\over1-\alpha q_U(x,y)}
 \mathbb E_{E\sim\nu_U}
 \left[
  \mathbf1_{\{C(E)\cap\{x,y\}=\varnothing\}}a_{U,xy}(E)^2
 \right].
\]

Efron--Stein has the prefactor \(1/2\).  Summing over \(U\) proves
(2.9). \(\square\)

## 3. The sharp one-bite recurrence

Fix two rank strata \(V_i,V_j\).  Suppose that, whenever a root in either
stratum survives the bite and is not put in the scalar exceptional ledger,

\[
 d_{t+1}(v)\ge(1-\varepsilon_t)\rho_{1,t}(v)d_t(v),               \tag{3.1}
\]

where \(0\le\varepsilon_t\le1/4\).  Let

\[
 \overline R_t(x,y)=
 \mathbb E\bigl[R_t(x,y)\mid\mathcal A_{xy},\mathcal F_t\bigr]. \tag{3.2}
\]

The two hypotheses needed for a block are the following weighted
statements:

\[
 \boxed{
 \sum_{y\in V_j}K_t(x,y)^2\overline R_t(x,y)^2
 \le(1+\gamma_t)\rho_{2,t}^2S_{t,j-i}(x),}                       \tag{CM}
\]

and

\[
 \boxed{
 \sum_{y\in V_j}K_t(x,y)^2J_t^\circ(x,y)
 \le\beta_tS_{t,j-i}(x).}                                      \tag{CFW}
\]

Here (CM) is the conditioned **mean pair-link contraction**, and (CFW) is
the conditioned four-walk bound.  Pointwise versions imply these weighted
versions, but are stronger than necessary.

### Theorem 3.1 (conditioned one-bite recurrence)

Assume (3.1), (CM), and (CFW).  Put

\[
 \rho^-_{1,t}(i)=\inf_{v\in V_i}\rho_{1,t}(v),\qquad
 \rho^-_{1,t}(j)=\inf_{v\in V_j}\rho_{1,t}(v).                   \tag{3.3}
\]

Then, for every nonexceptional \(x\in V_i\),

\[
\boxed{
\begin{aligned}
 &\mathbb E\!\left[
 S_{t+1,j-i}(x)\mid\mathcal A_x,\mathcal F_t
 \right]                                                        \\
 &\quad\le
 { (1+\gamma_t)\rho_{2,t}^2+2\alpha_t\beta_t
  \over
  (1-\varepsilon_t)^2
  \rho^-_{1,t}(i)\rho^-_{1,t}(j)}
 S_{t,j-i}(x).
\end{aligned}}                                                   \tag{3.4}
\]

#### Proof

On the event that \(x,y\) both survive and remain nonexceptional, (3.1)
gives

\[
 K_{t+1}(x,y)^2
 \le
 {K_t(x,y)^2R_t(x,y)^2
  \over
  (1-\varepsilon_t)^2
  \rho^-_{1,t}(i)\rho^-_{1,t}(j)}.                              \tag{3.5}
\]

Condition first on \(x\) surviving.  For the summand indexed by \(y\),
condition further on \(y\) surviving.  The probability of this latter
event is at most one, so it may be discarded in an upper bound.  Under the
two-root conditional law,

\[
 \mathbb E R_t(x,y)^2
 =\overline R_t(x,y)^2+\operatorname {Var}R_t(x,y)
 \le\overline R_t(x,y)^2+2\alpha_tJ_t^\circ(x,y)                 \tag{3.6}
\]

by Lemma 2.1.  Multiply (3.6) by \(K_t(x,y)^2\), sum over \(y\), and use
(CM) and (CFW).  This proves (3.4). \(\square\)

### Corollary 3.2 (the ideal exponents)

Suppose, uniformly in the protected band,

\[
 \rho^-_{1,t}(i),\rho^-_{1,t}(j)
 \ge(1-e_t)q_t^{g-1},qquad
 \rho_{2,t}\le(1+e_t)q_t^{g-2},                                \tag{3.7}
\]

and \(\alpha_tg=o(1)\).  Then, for an absolute \(C\),

\[
 \boxed{
 \mathbb E[S_{t+1,j-i}(x)\mid\mathcal A_x,\mathcal F_t]
 \le q_t^{-2}
 \bigl(1+C(e_t+\varepsilon_t+\gamma_t+alpha_t\beta_t)\bigr)
 S_{t,j-i}(x).}                                                  \tag{3.8}
\]

#### Proof

The quotient of the two ideal powers is exactly

\[
 {q_t^{2g-4}\over q_t^{2g-2}}=q_t^{-2}.                         \tag{3.9}
\]

Also \(q_t^{g-1}=1-o(1)\), so the denominator multiplying
\(2\alpha_t\beta_t\) is bounded below by an absolute positive constant.
For \(u\le1/4\), \((1-u)^{-2}\le1+4u\).  Applying these facts to (3.4)
gives (3.8). \(\square\)

## 4. Iteration to density \(1/\log m\)

Let

\[
 z_t=\prod_{s<t}q_s.                                             \tag{4.1}
\]

Assume

\[
 z_t\ge{1\over\log m},\qquad
 \sum_{s<t}\alpha_s=O(\log\log m),                              \tag{4.2}
\]

and

\[
 \sum_s(e_s+\varepsilon_s+\gamma_s)=o(1),\qquad
 \sup_s\beta_s\le\beta_m=m^{-1/2+o(1)}.                        \tag{4.3}
\]

Iterating (3.8), using \(1+u\le e^u\), gives

\[
\begin{aligned}
 \mathbb E\!\left[S_{t,h}(x)\mid x\text{ survives to time }t\right]
 &\le z_t^{-2}S_{0,h}(x)
 \exp\left(
 C\sum_{s<t}(e_s+\varepsilon_s+\gamma_s+\alpha_s\beta_s)
 \right)                                                        \\
 &=(1+o(1))z_t^{-2}S_{0,h}(x),                                  \tag{4.4}
\end{aligned}
\]

because

\[
 \sum_s\alpha_s\beta_s
 =O(\beta_m\log\log m)=o(1).                                   \tag{4.5}
\]

Combining (4.4) with (1.4)--(1.5) gives exactly the desired numerical
profile:

\[
 \mathbb E\!\left[S_{t,0}(x)\mid x\text{ survives to time }t\right]
 \le(1+o(1))C_0z_t^{-2}m^{-2},                                  \tag{4.6}
\]

and, for \(h\ne0\),

\[
 \mathbb E\!\left[S_{t,h}(x)\mid x\text{ survives to time }t\right]
 \le(1+o(1))C_0z_t^{-2}(|h|+1)^2|h|!
       \left({C_0\over m}\right)^{|h|}.                         \tag{4.7}
\]

The factorial rank-gap sum is unchanged.  A direct undifferentiated Schur
argument would give only

\[
 \mathfrak T_t(x)\le {Cg\over mz_t^2}.                           \tag{4.8}
\]

The cover/remainder split recorded in Section 9 sharpens (4.8) to
\(m^{-1+o(1)}\) at \(z_t=1/\log m\).  That refinement is essential for
the global physical ledger.

Equations (4.4)--(4.8) are expectation statements under the conditioned
process.  Turning them into a physical \(o(W)\) exceptional ledger needs
the global stopping argument of Section 9 and, for pair-square itself, its
additional physical-label quadratic-variation estimate.

## 5. What the \(s=4\) cube boundary actually gives

Let a full adjacent-switch cube have dimension \(d=\Theta(m)\), and let
quarantine delete a set \(Z\) of density

\[
 \eta=m^{-4+o(1)}.                                                \tag{5.1}
\]

The directed cube-boundary count is

\[
 e(Q_d\setminus Z,Z)\le d|Z|.                                   \tag{5.2}
\]

Hence, for every \(\theta>0\), at most an \(\eta/\theta\) fraction of
cube vertices have more than \(\theta d\) neighbours in \(Z\).  Taking
\(\theta=\sqrt\eta\) proves that all but a

\[
 \sqrt\eta=m^{-2+o(1)}                                           \tag{5.3}
\]

fraction of raw schedules have at least

\[
 (1-\sqrt\eta)d                                                  \tag{5.4}
\]

quarantine-legal swap neighbours.  This verifies the stated boundary
claim with its exact constants.

It does not control the current law.  Write

\[
 A_t=\{P:\text{all owners of }P\text{ are unused and its priority is
 feasible}\}.                                                    \tag{5.5}
\]

The nibble samples from the raw cube conditioned on \(A_t\setminus Z\).
That set may be one rare face.  If \(B\) has raw mass at most \(\beta\)
and \(A_t\) has raw mass \(\theta\), the only general inequality is

\[
 \Pr(B\mid A_t)\le\min\{1,\beta/\theta\}.                       \tag{5.6}
\]

Thus neither (5.3) nor a raw two-link bound \(\beta=m^{-1/2+o(1)}\)
implies (CFW).  There is a second geometric issue: a tag fibre is a union
of full switch cubes, but toggling a switch can change whether a fixed
target, and a fortiori a fixed target pair, is claimed.  A proof for
pair links needs a pair-incidence-preserving subcube or an
incidence-weighted face theorem.  Full tag-cube retention does not supply
one.

## 6. The exact branching statement which would suffice

The phrase "branching factor \(\beta\)" has two inequivalent meanings.
A one-generation raw statement says only that each single witness event
has raw mass at most \(\beta\).  A hereditary branching statement says
that the same bound holds after every partial witness history.  Only the
second tensorizes.

The following elementary lemma gives the exact amplification needed.

### Lemma 6.1 (fresh-branch amplification)

Let \((\Omega,\mu)\) be a current, already conditioned pair-link space.
Suppose every bad object \(P\in\mathcal B\) has a set \(R(P)\subseteq[d]\)
of at least \(L\) distinct admissible witness coordinates.  Assume that
for every \(t\)-set \(J\subseteq[d]\),

\[
 \mu\{P:J\subseteq R(P)\}\le\beta^t.                            \tag{6.1}
\]

Then

\[
 \boxed{
 \mu(\mathcal B)
 \le{\binom dt\over\binom Lt}\beta^t
 \le\left({ed\beta\over L}\right)^t.}                          \tag{6.2}
\]

#### Proof

Count pairs \((P,J)\) with \(P\in\mathcal B\), \(|J|=t\), and
\(J\subseteq R(P)\).  Every bad \(P\) contributes at least
\(\binom Lt\).  Summing (6.1) over all \(\binom dt\) choices of \(J\)
gives the first inequality.  The standard estimates
\(\binom dt\le(ed/t)^t\) and \(\binom Lt\ge(L/t)^t\) give the second.
\(\square\)

If \(L\ge z_td/2\), then

\[
 \mu(\mathcal B)\le\left({2e\beta_m\over z_t}\right)^t.        \tag{6.3}
\]

For \(z_t\ge1/\log m\), \(\beta_m=m^{-1/2+o(1)}\), and

\[
 t=\left\lfloor(2-o(1)){\log m\over\log\log m}\right\rfloor,  \tag{6.4}
\]

the right side of (6.3) is

\[
 \exp\left[-(1-o(1)){(\log m)^2\over\log\log m}\right].        \tag{6.5}
\]

This is more than enough to sum over the
\(\Theta(W\sqrt m)\) physical target ledger.

A conditional child bound

\[
 \Pr(\text{next fresh branch}\mid
       \mathcal F_t,\mathcal A_{xy},
       \text{all earlier branches})\le\beta_m                    \tag{6.6}
\]

implies (6.1) by the chain rule.  Therefore the following two clauses are
a sufficient PBBS theorem:

1. every failure of (CM) or (CFW) supplies at least \(z_td/2\) distinct
   admissible swap-coordinate witnesses in a target-pair-preserving chart;
2. the fresh conditional branch estimate (6.6) holds in the current
   pair-link law.

The logarithmic face reservoir supplies enough coordinates for (6.4).
It does not prove either clause.  In particular, a one-generation estimate
does not imply (6.6): if all witness events are the same event \(B\) of
mass \(\beta\), then every marginal has mass \(\beta\), while the
intersection of any number of them still has mass \(\beta\), not
\(\beta^t\).

## 7. An optional max-influence route to the scalar ledger

The same quantifier appears in the scalar degree martingale.  Let
\(I_{t,x}^\circ(E)\) be the fractional loss of the \(x\)-fibre from
conflicts away from \(x\), under the law conditioned on \(x\) surviving.
Suppose, outside an already charged \(o(W)\) family,

\[
 \sup_{t,x,U,E} I_{t,x}^\circ(E)\le b_m=m^{-1/2+o(1)},           \tag{7.1}
\]

and the predictable quadratic variation through \(z=1/\log m\) is

\[
 V_m\le {Cg(\log m)^2\log\log m\over m}=m^{-1/2+o(1)}.          \tag{7.2}
\]

For the centred sequential martingale, Freedman's inequality gives, for
\(\zeta=m^{-1/8}\),

\[
 \Pr(|M_x|>\zeta)
 \le2\exp\left[-{\zeta^2\over2(V_m+b_m\zeta/3)}\right]
 \le\exp(-m^{1/4-o(1)}).                                        \tag{7.3}
\]

Since the total physical target weight is \(\Theta(W\sqrt m)\), (7.3)
gives an \(o(W)\) exceptional ledger.  Thus a survival-conditioned maximum
influence bound of the \(\beta\)-scale would indeed repair the aggregate
defect of a Chebyshev argument.

But (7.1) is not a consequence of (5.3): the current law may be supported
on the raw exceptional schedules.  Nor is it a consequence of an averaged
four-walk estimate.  Section 9 gives a different scalar route using a
single weighted stopped corridor, so (7.1) is sufficient rather than
necessary.  For pair-square, both routes still encounter the same
physical-label dispersal term.

## 8. Exact boundary

The following are proved in this note.

1. The exact pair-root conditioned laws are (2.3)--(2.4).
2. The pair-link Efron--Stein term is precisely (2.7), and satisfies
   (2.9).
3. The sharp one-bite recurrence is (3.4).
4. Under (CM) and (CFW), its numerical iteration closes with total error
   \(O(\beta_m\log\log m)=o(1)\), giving (4.6)--(4.7).
5. The \(s=4\) boundary statement gives (5.3)--(5.4), but only in the raw
   cube measure.
6. Fresh conditional branching plus a pair-link witness map gives the
   superpolynomial amplification (6.5).
7. A conditioned max-influence bound at the \(\beta\)-scale gives one
   sufficient physical scalar exceptional ledger by (7.3); Section 9
   gives the sharper global-stopping alternative.

The currently supplied raw/per-full-cube statements do **not** prove:

* (CM), the \(z^{g-2}\) pair-link mean contraction;
* (CFW) under the current two-root conditioned law;
* a target-pair-preserving swap chart;
* fresh tensorization (6.6); or
* the aggregate physical-label square needed to stop the pair-square
  functional.

Accordingly hereditary pair-square propagation is conditionally reduced,
but not yet proved.  The next exact statement is the two-clause
pair-rooted fresh-witness theorem in Section 6.  A raw branching number
\(\beta=m^{-1/2+o(1)}\), without those quantifiers, is insufficient.

## 9. The global stopped bootstrap and why it does not yet lift

The sharpened cover/remainder split improves the raw conditioned triangle
to

\[
 \mathfrak T_0(x)
 =O\!\left({1\over m}+{g\over m^{3/2}}\right)
 =m^{-1+o(1)}.                                                   \tag{9.1}
\]

Under the ideal block inflation, its residual version is

\[
 \mathfrak T_z(x)
 \le C\left(
 {z^{-2}\over m}
 +{gz^{-2}\over m^{3/2}}
 +{z^{-3}\over m^{3/2}}
 \right)
 =m^{-1+o(1)}
 \quad(z\ge1/\log m).                                           \tag{9.2}
\]

This changes the aggregate scalar accounting.  The correct way to use it
is one stopped corridor over the whole run, rather than a new exceptional
decision after every bite.

### Lemma 9.1 (weighted global stopping)

Let \(F\) range over fibres with deterministic weights \(a_F\ge0\).  Write

\[
 X_{t,F}=M_{t,F}+A_{t,F},\qquad M_{0,F}=A_{0,F}=0,               \tag{9.3}
\]

where \(M_F\) is a square-integrable martingale and \(A_F\) is predictable.
For \(\eta>0\), put

\[
 \tau_F=\min\{t:|X_{t,F}|\ge\eta\}\wedge(R+1).                  \tag{9.4}
\]

If

\[
 \sum_Fa_F\mathbb E\langle M_F\rangle_{\tau_F\wedge R}\le B_2,
 \qquad
 \sum_Fa_F\mathbb E
  \sup_{t\le\tau_F\wedge R}|A_{t,F}|\le B_1,                    \tag{9.5}
\]

then

\[
 \boxed{
 \sum_Fa_F\Pr(\tau_F\le R)
 \le {4B_1\over\eta}+{16B_2\over\eta^2}.}                       \tag{9.6}
\]

#### Proof

On \(\{\tau_F\le R\}\), either
\(\sup_{t\le\tau_F}|A_{t,F}|\ge\eta/2\) or
\(\sup_{t\le\tau_F}|M_{t,F}|\ge\eta/2\).  Markov bounds the first
probability by \(2\mathbb E\sup|A|/\eta\).  For the stopped martingale,
Doob's \(L^2\) inequality and the martingale isometry give

\[
\begin{aligned}
 \Pr\!\left(\sup_{t\le\tau_F\wedge R}|M_{t,F}|\ge\eta/2\right)
 &\le {4\over\eta^2}
      \mathbb E\sup_{t\le R}|M_{t\wedge\tau_F,F}|^2\\
 &\le {16\over\eta^2}
      \mathbb E\langle M_F\rangle_{\tau_F\wedge R}.
\end{aligned}                                                    \tag{9.7}
\]

Multiply by \(a_F\), sum, and harmlessly enlarge the coefficient of the
first term from two to four. \(\square\)

For scalar degrees, take

\[
 X_{t,F}=
 \log {D_t(F)\over D_0(F)\prod_{s<t}\rho_{s,\operatorname{str}(F)}}.
                                                                    \tag{9.8}
\]

Before \(\tau_F\), logarithm and relative degree error differ by
\(1+O(\eta)\).  The large one-bite event is already in the scalar
Bernstein/deadline ledger.  Hence Lemma 9.1 applies to the compensated
log-degree martingale.

The all-rank quadratic-variation target furnished by (9.2) is

\[
 B_mW,\qquad
 B_m=Qm^{-1+o(1)}\log\log m=m^{-1/2+o(1)}.                       \tag{9.9}
\]

Taking

\[
 \eta=B_m^{1/4}=m^{-1/8+o(1)}                                  \tag{9.10}
\]

in (9.6), with \(B_1+B_2\le B_mW\), gives

\[
 \sum_Fa_F\Pr(\tau_F\le R)
 \le O(B_m^{1/2}W)=o(W).                                       \tag{9.11}
\]

Thus the scalar stopped bootstrap is rigorous: outside \(o(W)\) physical
weight, all normalized degree denominators remain \(1+o(1)\) throughout
the run.

### Proposition 9.2 (the pair-square lift has a new quadratic variation)

The scalar bound (9.11) and the triangle estimate (9.2) do not by
themselves give a stopped corridor for \(S_{t,h}(x)\).

#### Proof

Freeze \(t,x,h\).  For a tag variable \(U\), let
\(\Delta_{U,xy}(E)\) denote the conditioned fractional change of the
\((x,y)\)-link caused by \(E\), with direct root hits removed.  Up to the
already stopped scalar denominators, the first variation of the normalized
row energy has the form

\[
 G_{t,U}(x,h;E)
 =\sum_{y\in V_{r+h}}w_{t,xy}\Delta_{U,xy}(E),                  \tag{9.12}
\]

where \(w_{t,xy}\ge0\) and
\(\sum_yw_{t,xy}=1\) after normalizing by the current block energy.
Consequently the Efron--Stein/quadratic-variation term for a stopped
pair-square martingale contains

\[
\begin{aligned}
 \sum_U\mathbb E G_{t,U}(x,h;E)^2
 &=
 \sum_{y}w_{t,xy}^2
   \sum_U\mathbb E\Delta_{U,xy}(E)^2\\
 &\quad+
 \sum_{\substack{y,y'\in V_{r+h}\\y\ne y'}}
 w_{t,xy}w_{t,xy'}
 \sum_U\mathbb E[
   \Delta_{U,xy}(E)\Delta_{U,xy'}(E)] .                         \tag{9.13}
\end{aligned}
\]

The first line is a diagonal pair-link four-walk.  The second line is a
joined physical-label square.  The scalar triangle controls

\[
 \sum_U\mathbb E
 \left(\sum_{P\in F_x}p_{t,x}(P)h_t^\circ(P,E)\right)^2,        \tag{9.14}
\]

which has only the one root label \(x\).  It does not dominate the
off-diagonal sum in (9.13) without losing the number of possible
\(y\)-labels.  Such a loss destroys the \(B_m=o(1)\) scale.

Equivalently, if \(N_\omega(x,y)\) is the number of switch-square witnesses
in residual slice \(\omega\) carrying physical label pair \((x,y)\), raw
or slice-by-slice entropy controls diagonal quantities, while (9.13)
contains

\[
 \boxed{
 \sum_{x,y}\sum_{\omega\ne\omega'}
 {N_\omega(x,y)N_{\omega'}(x,y)\over D_t(x)D_t(y)}.}            \tag{9.15}
\]

There is no estimate for (9.15) in the raw triangle theorem.  This proves
the claim. \(\square\)

One can instead stop every individual pair-link log degree and apply
Lemma 9.1 with weights \(K_0(x,y)^2\).  That controls the total
pair-square weight of stopped links, but it does not control the physical
cost of declaring their endpoints exceptional, nor the later contribution
of a stopped link.  Removing all candidates in those links is a
first-moment operation, whereas the available charge is quadratic.
Therefore this reformulation does not avoid (9.15).

The exact stopped theorem still needed is the survival-conditioned
aggregate bound

\[
\begin{aligned}
 &\sum_x a_x\,
  \mathbb E\sup_{t\le\tau_x\wedge R}|A^{\rm ps}_{t,x}|
 +\sum_xa_x\,
  \mathbb E\langle M^{\rm ps}_x\rangle_{\tau_x\wedge R}\\
 &\hspace{35mm}\le m^{-1/2+o(1)}W,                              \tag{9.16}
\end{aligned}
\]

or a direct estimate of (9.15) strong enough to imply it.  Thus the new
cover/remainder triangle **does** close the scalar global stopping
bootstrap.  Lifting that bootstrap to the pair-square/four-walk functional
requires physical square-label dispersal; it cannot reuse the scalar
triangle alone.
