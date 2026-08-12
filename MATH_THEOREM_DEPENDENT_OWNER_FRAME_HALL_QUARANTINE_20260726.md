# Dependent owner-frame rounding: simultaneous literal Hall with an \(o(W)\) quarantine

Date: 2026-07-26

Method: pure mathematics only. No computation, script, solver, or web input
is used.

## 0. Verdict

Put

\[
 \mathcal M=\binom{[2m]}m,\qquad W=|\mathcal M|,
 \qquad
 \mathcal L_q^\pm=\binom{[2m]}{m\pm q},
 \qquad
 N_q=|\mathcal L_q^\pm|,
 \qquad
 \rho_q={N_q\over W}.
 \tag{0.1}
\]

Let \(H\le C\sqrt{m\log m}\). There is a polynomial catalogue of pair
frames and one integral assignment of every middle owner to one frame,
respecting any feasible rounded type-bin quota vector from the mixed-frame
fractional assignment, such that

\[
 \boxed{
 \sum_{q=1}^H\left(
  \operatorname {def}G_q^-
 +\operatorname {def}G_q^+\right)=o(W).}
 \tag{0.2}
\]

Here \(G_q^\pm\) is the actual frozen-frame literal face graph and

\[
 \operatorname {def}G
 =\max_{\mathcal Z\subseteq V_{\rm tar}(G)}
       (|\mathcal Z|-|\Gamma_G(\mathcal Z)|)
 \tag{0.3}
\]

is its exact target-side Hall deficiency.

More precisely, before the final exact-quota repair there is a common
owner-frame assignment for which

\[
 \boxed{
 \sum_{q=1}^H\left(
  \operatorname {def}G_q^-
 +\operatorname {def}G_q^+\right)
 \le { (2\sqrt2+o(1))W\over\sqrt m}
      +O(WH\varepsilon),}
 \tag{0.4}
\]

where the polynomial catalogue may be chosen with
\(\varepsilon=m^{-L}\) for any required fixed \(L\).

Every family Hall inequality is controlled simultaneously. There is no
union bound over target families. The deterministic certificate is

\[
 |\mathcal Z|-|\Gamma(\mathcal Z)|
 \le \sum_T(1-Z_{T,q}^\pm)_+,
 \tag{0.5}
\]

where \(Z_{T,q}^\pm\) is a normalized literal-face load. Its total expected
shortfall is \(O(W/\sqrt m)\), with the complete depth sum dominated by
\(q=1\).

Independent owner choices first produce (0.4) and bin counts within total
\(\ell_1\)-distance

\[
 O(\sqrt{RW})
 \tag{0.6}
\]

of the fractional quotas, where \(R=m^{O(1)}\) is the number of frame/type
bins. A deterministic path-swap repair then restores any feasible exact
rounded quota vector while recolouring at most

\[
 O(R^{3/2}\sqrt W)=o(W/H)
 \tag{0.7}
\]

owners. Recolouring \(r\) owners increases the sum of all two-sided Hall
deficiencies by at most \(2Hr\), so (0.2) survives.

Thus the quota-invisible singleton cut from the previous note is not
unavoidable. It obstructs arbitrary quota rounding, but a load-controlled
rounding avoids all singleton and family cuts except for a summable
\(o(W)\) quarantine.

This settles dependent owner-to-frame rounding at the literal-face level.
It does not impose common nested prefixes or group the owners into complete
isometric cycles.

## 1. Catalogue and fractional owner states

Let

\[
 \mathscr P=(P_1,\ldots,P_J)
 \tag{1.1}
\]

be a polynomial catalogue satisfying the uniform mixed-frame estimates.
Let \(\mathcal B\) be the balanced source-type interval and set

\[
 I(X)=\{j:f_{P_j}(X)\in\mathcal B\},
 \qquad
 a_X=|I(X)|,
 \qquad
 \alpha=J(1-\tau).
 \tag{1.2}
\]

For every owner,

\[
 (1-\varepsilon)\alpha\le a_X\le(1+\varepsilon)\alpha.
 \tag{1.3}
\]

For a lower target, let \(g^-_{P_j}(T)\) be its number of full pairs. For
an upper target, let \(g^+_{P_j}(T)\) be its number of empty pairs. The
catalogue satisfies, for both signs,

\[
 {1-\varepsilon\over\rho_q}\alpha
 \le
 \sum_{\substack{j\\g^\pm_{P_j}(T)\in\mathcal B}}
       \lambda_{g^\pm_{P_j}(T),q}
 \le
 {1+\varepsilon\over\rho_q}\alpha,
 \tag{1.4}
\]

where

\[
 \lambda_{f,q}
 ={2^q\binom{f+q}{q}\over\binom{m-2f}{q}}.
 \tag{1.5}
\]

These estimates follow from the exact size-bias identity

\[
 \pi_q(f)\lambda_{f,q}=\rho_q^{-1}\pi_0(f)
 \tag{1.6}
\]

and polynomial concentration.

The fractional owner assignment is

\[
 y_{X,j}=
 \begin{cases}
  1/a_X,&j\in I(X),\\
  0,&j\notin I(X).
 \end{cases}
 \tag{1.7}
\]

For a bin \(r=(j,f)\), put

\[
 B_r
 =\sum_{X:f_{P_j}(X)=f}y_{X,j}.
 \tag{1.8}
\]

The vector \(B=(B_r)\) is the fractional type-bin supply.

### Definition 1.1 (feasible rounded quota vector)

An integer vector \(b=(b_r)\) is a feasible rounded quota vector if

\[
 |b_r-B_r|<1,\qquad
 \sum_rb_r=W,
 \tag{1.9}
\]

and there is an owner-to-allowed-bin assignment having bin counts \(b_r\).

Such a vector exists by total unimodularity of the bipartite owner-bin
network: the fractional point (1.7) can be rounded so every right degree is
a floor or ceiling of (1.8).

## 2. One common random rounding

Independently for every owner \(X\), choose

\[
 A(X)\ \text{ uniformly from }I(X).
 \tag{2.1}
\]

This is one common state assignment, used at every depth and on both sides.
Write

\[
 f_X=f_{P_{A(X)}}(X),\qquad
 s_X=m-2f_X,\qquad
 d_X(q)=\binom{s_X}{q}.
 \tag{2.2}
\]

Let

\[
 s_*=\min_{f\in\mathcal B}(m-2f)
     ={m\over2}-O(\sqrt{m\log m}).
 \tag{2.3}
\]

Thus \(s_*\ge m/3\) and \(H<s_*/2\) for large \(m\).

For a lower target \(T\), write \(T\sim^-_{A(X)}X\) if it is obtained from
\(X\) by deleting the selected endpoints of \(q\) distinct split pairs of
the assigned frame. Define

\[
 Z_{T,q}^-=
 \sum_{X:T\sim^-_{A(X)}X}
       {\rho_q\over d_X(q)}.
 \tag{2.4}
\]

Define \(Z_{T,q}^+\) analogously using upper literal faces.

### Lemma 2.1 (uniform mean)

For every target, depth, and sign,

\[
 {1-\varepsilon\over1+\varepsilon}
 \le \mathbb E Z_{T,q}^\pm
 \le {1+\varepsilon\over1-\varepsilon}.
 \tag{2.5}
\]

#### Proof

Fix a target and a frame in which its relevant type is \(f\). The exact
frame incidence degrees are

\[
 d^{\rm src}_{f,q}=\binom{m-2f}{q},
 \qquad
 d^{\rm tar}_{f,q}=2^q\binom{f+q}{q}.
 \tag{2.6}
\]

Hence the total normalized contribution through that frame is

\[
 \sum_{X:T\sim^\pm_jX}{\rho_q\over d^{\rm src}_{f,q}}
 =\rho_q\lambda_{f,q}.
 \tag{2.7}
\]

Every compatible owner has the same type \(f\), so
\(1/a_X\) lies between
\(1/((1+\varepsilon)\alpha)\) and
\(1/((1-\varepsilon)\alpha)\). Sum (2.7) over the allowed frames and apply
(1.4). This gives (2.5). \(\square\)

### Lemma 2.2 (variance)

Put

\[
 \beta_q={\rho_q\over\binom{s_*}{q}},
 \qquad
 M_\varepsilon={1+\varepsilon\over1-\varepsilon}.
 \tag{2.8}
\]

Then

\[
 \operatorname {Var}Z_{T,q}^\pm
 \le\beta_q\,\mathbb E Z_{T,q}^\pm
 \le M_\varepsilon\beta_q.
 \tag{2.9}
\]

#### Proof

For a fixed target, contributions indexed by distinct owners are
independent. Each owner contribution \(Y_X\) is nonnegative and at most
\(\beta_q\), so \(Y_X^2\le\beta_qY_X\). Therefore

\[
 \operatorname {Var}Z
 =\sum_X\operatorname {Var}Y_X
 \le\sum_X\mathbb E Y_X^2
 \le\beta_q\mathbb E Z.
 \]

Apply Lemma 2.1. \(\square\)

No independence between different targets, depths, or signs is used.

## 3. One load certificate controls every Hall family

Fix one realization \(A\), one depth, and one sign. Let \(G_q^\pm(A)\) be
the literal compatibility graph after the owner frames have been frozen.

### Lemma 3.1 (simultaneous cut domination)

For every target family \(\mathcal Z\subseteq\mathcal L_q^\pm\),

\[
 |\mathcal Z|-|\Gamma_A(\mathcal Z)|
 \le
 \sum_{T\in\mathcal L_q^\pm}(1-Z_{T,q}^\pm)_+.
 \tag{3.1}
\]

Consequently,

\[
 \boxed{
 \operatorname {def}G_q^\pm(A)
 \le D_q^\pm(A):=
 \sum_T(1-Z_{T,q}^\pm)_+.}
 \tag{3.2}
\]

#### Proof

For one owner \(X\), exactly \(d_X(q)\) targets are literal \(q\)-faces of
its assigned orientation cube. Therefore

\[
\begin{aligned}
 \sum_{T\in\mathcal Z}Z_{T,q}^\pm
 &=
 \sum_{X\in\Gamma_A(\mathcal Z)}
 {\rho_q\over d_X(q)}
 \bigl|\{T\in\mathcal Z:T\sim^\pm_{A(X)}X\}\bigr|\\
 &\le \rho_q|\Gamma_A(\mathcal Z)|
 \le|\Gamma_A(\mathcal Z)|.
\end{aligned}
\tag{3.3}
\]

Thus

\[
 |\mathcal Z|-|\Gamma_A(\mathcal Z)|
 \le\sum_{T\in\mathcal Z}(1-Z_{T,q}^\pm)
 \le\sum_T(1-Z_{T,q}^\pm)_+.
\]

Taking the maximum over \(\mathcal Z\) proves (3.2). \(\square\)

This is the hereditary Hall step. The exponentially many family
inequalities have been reduced deterministically to one targetwise
\(L^1\)-shortfall.

## 4. The total quarantine is \(o(W)\)

Let

\[
 \gamma_\varepsilon={2\varepsilon\over1-\varepsilon}.
 \tag{4.1}
\]

For every target, Lemmas 2.1--2.2 and Cauchy--Schwarz give

\[
\begin{aligned}
 \mathbb E(1-Z_{T,q}^\pm)_+
 &\le(1-\mathbb EZ_{T,q}^\pm)_+
       +\mathbb E|Z_{T,q}^\pm-\mathbb EZ_{T,q}^\pm|\\
 &\le\gamma_\varepsilon+
       \sqrt{M_\varepsilon\beta_q}.
\end{aligned}
\tag{4.2}
\]

Since \(N_q=W\rho_q\le W\),

\[
 \mathbb E D_q^\pm
 \le W\left(
   \gamma_\varepsilon+
   {\sqrt{M_\varepsilon}\over
      \sqrt{\binom{s_*}{q}}}\right).
 \tag{4.3}
\]

Set \(a_q=\binom{s_*}{q}^{-1/2}\). Uniformly for \(q<H\),

\[
 {a_{q+1}\over a_q}
 =\sqrt{{q+1\over s_*-q}}
 \le\sqrt{{H+1\over s_*-H}}=o(1).
 \tag{4.4}
\]

It follows that

\[
 \sum_{q=1}^Ha_q
 ={1+o(1)\over\sqrt{s_*}}
 ={\sqrt2+o(1)\over\sqrt m}.
 \tag{4.5}
\]

Summing (4.3) over all depths and both signs yields

\[
\boxed{
 \mathbb E\sum_{q=1}^H(D_q^-+D_q^+)
 \le{(2\sqrt2+o(1))W\over\sqrt m}
      +O(WH\varepsilon).}
\tag{4.6}
\]

Choose the catalogue accuracy so that \(H\varepsilon=o(1)\). The
right-hand side is \(o(W)\).

By Hall's deficiency theorem, after deleting exactly
\(\operatorname {def}G_q^\pm(A)\) targets, the remaining targets have a
matching into distinct middle owners. Equations (3.2) and (4.6) therefore
give an aggregate \(o(W)\) quarantine.

## 5. Near-quota concentration

Let \(\mathcal R\) be the set of allowed frame/type bins and write

\[
 R=|\mathcal R|\le J|\mathcal B|=m^{O(1)}.
 \tag{5.1}
\]

For \(r=(j,f)\), let

\[
 n_r=|\{X:A(X)=j,\ f_{P_j}(X)=f\}|.
 \tag{5.2}
\]

Then \(\mathbb En_r=B_r\). Because \(n_r\) is a sum of independent
indicators,

\[
 \operatorname {Var}n_r\le B_r,
 \qquad
 \mathbb E|n_r-B_r|\le\sqrt{B_r}.
 \tag{5.3}
\]

Therefore, with

\[
 Q(A)=\sum_{r\in\mathcal R}|n_r-B_r|,
 \tag{5.4}
\]

Cauchy--Schwarz gives

\[
 \mathbb EQ(A)
 \le\sum_r\sqrt{B_r}
 \le\sqrt{R\sum_rB_r}
 =\sqrt{RW}.
 \tag{5.5}
\]

Apply Markov's inequality separately to the two nonnegative random
variables in (4.6) and (5.4), with threshold four times their respective
expectations. The two exceptional probabilities are each at most \(1/4\),
so their complements intersect. Consequently there is one deterministic
realization \(A_0\) satisfying

\[
 \sum_{q=1}^H(D_q^-(A_0)+D_q^+(A_0))
 =O(W/\sqrt m+WH\varepsilon)=o(W),
 \tag{5.6}
\]

and

\[
 Q(A_0)=O(\sqrt{RW}).
 \tag{5.7}
\]

## 6. Exact quotas by dependent path swaps

Fix any feasible rounded quota vector \(b\) from Definition 1.1. Let
\(\Psi\) be an allowed owner-bin assignment realizing \(b\). We repair
\(A_0\) toward the counts of \(\Psi\), while retaining as many owner states
of \(A_0\) as possible.

### Lemma 6.1 (quota repair by simple bin paths)

Let two allowed owner-bin assignments have count vectors \(n\) and \(b\)
on \(R\) bins. There is an allowed assignment with count vector \(b\)
which differs from the first assignment on at most

\[
 {R\over2}\sum_r|n_r-b_r|
 \tag{6.1}
\]

owners.

#### Proof

For every owner assigned to different bins by the two assignments, draw a
directed arc from its first bin to its second bin and label the arc by that
owner. At bin \(r\), outdegree minus indegree is \(n_r-b_r\).

Decompose this directed multigraph into directed cycles and directed paths
from surplus bins to deficit bins. Delete every directed cycle. Replace
each remaining path by a simple path after deleting any internal directed
cycle. There are

\[
 {1\over2}\sum_r|n_r-b_r|
\]

path units, and every simple path uses at most \(R\) arcs.

Reassign exactly the owners labelling the retained path arcs to their
second bins. Each internal path bin loses and gains one owner, while the
two endpoints correct one unit of surplus and deficit. All assigned
owner-bin incidences are allowed because they came from the second
assignment. The resulting count vector is \(b\), and the number of changed
owners is bounded by (6.1). \(\square\)

Since \(|b_r-B_r|<1\),

\[
 \sum_r|n_r-b_r|\le Q(A_0)+R.
 \tag{6.2}
\]

Apply Lemma 6.1. The number \(r_0\) of recoloured owners satisfies

\[
 r_0\le {R\over2}(Q(A_0)+R).
 \tag{6.3}
\]

Equations (5.7) and polynomiality of \(H,R\) imply

\[
 Hr_0=o(W).
 \tag{6.4}
\]

Indeed,

\[
 r_0=O(R^{3/2}\sqrt W+R^2)=o(W/H),
 \tag{6.5}
\]

because every fixed polynomial in \(m\) is \(o(\sqrt W/H)\).

### Lemma 6.2 (Hall deficiency is owner-Lipschitz)

If two frozen-frame assignments differ on \(r\) middle owners, then at
every depth and sign,

\[
 |\operatorname {def}G-\operatorname {def}G'|\le r.
 \tag{6.6}
\]

#### Proof

Delete the \(r\) changed owner vertices from both graphs. The remaining
graphs are identical. Deleting or restoring \(r\) right-side owner
vertices changes the maximum matching number by at most \(r\). Since
target-side cardinality is fixed, the same bound holds for deficiency.
\(\square\)

Let \(A_1\) be the exact-quota assignment produced by Lemma 6.1. Summing
Lemma 6.2 over \(H\) depths and two signs gives

\[
\begin{aligned}
 \sum_{q=1}^H\bigl(
  \operatorname {def}G_q^-(A_1)
 +\operatorname {def}G_q^+(A_1)\bigr)
 &\le
 \sum_{q=1}^H(D_q^-(A_0)+D_q^+(A_0))
 +2Hr_0\\
 &=o(W).
\end{aligned}
 \tag{6.7}
\]

This proves (0.2) with the prescribed feasible rounded type-bin quotas.

## 7. Uniform family statement and quarantine

For the final assignment \(A_1\), define

\[
 \eta_q^\pm=\operatorname {def}G_q^\pm(A_1).
 \tag{7.1}
\]

Then

\[
 \sum_{q=1}^H(\eta_q^-+\eta_q^+)=o(W),
 \tag{7.2}
\]

and, uniformly for every target family,

\[
 \boxed{
 |\mathcal Z|-|\Gamma_{A_1}(\mathcal Z)|
 \le\eta_q^\pm
 \qquad
 (\mathcal Z\subseteq\mathcal L_q^\pm).}
 \tag{7.3}
\]

For each depth and sign, Hall's deficiency theorem supplies a matching
covering all but \(\eta_q^\pm\) targets. Quarantine the unmatched targets.
The aggregate quarantine through the entire band is \(o(W)\).

The rounding is therefore hereditary at the exact scale required by the
constant-one literal-face compiler: it controls every singleton cut and
every larger target-family cut simultaneously, rather than merely matching
the pair-type totals.

## 8. Remaining gate

The result chooses one frame per middle owner and uses that same choice at
all depths and on both sides. It also restores the prescribed integral
type-bin quotas.

What it does not provide is a common order of the split directions.
The depth-\(q\) matchings obtained after Hall may use nonnested faces for
the same owner. Nor does the vertexwise frame assignment make the owner
classes unions of complete \(2h\)-cycles.

Thus the exact remaining statement is no longer a face-Hall theorem. It is
a cycle-correlated nested-prefix theorem:

> Recolour only \(o(W/H)\) owners, or select the frames at cycle level from
> the outset, so that the surviving literal face matchings become nested
> prefixes of complete isometric cycles while losing only \(o(W)\)
> additional targets.

All literal singleton, family, and type-quota cuts have now been absorbed
into the \(o(W)\) quarantine.
