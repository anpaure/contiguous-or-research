# Choosing SCD extensions to make the signature flow Eulerian

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The arbitrary extension step in the SCD flag theorem can be isolated exactly.
For every owner \(X\), choose one ordered length-\(H\) deletion word extending
the forced prefix supplied by its symmetric chain.  Regard that word as an arc
from its length-\((H-1)\) prefix to its length-\((H-1)\) suffix.  The desired
condition \(\Delta_{\rm seq}=0\) is precisely that the selected colored arcs
form an Eulerian directed multigraph.

The complete selection problem is a **colored circulation**:

\[
 \sum_{w\in\mathcal W_X}x_{X,w}=1
 \quad(X\in\Omega),\qquad
 \operatorname{div}_\theta(x)=0
 \quad(\theta\text{ a signature}).                               \tag{0.1}
\]

Its fractional feasibility has an exact potential dual.  For every real
potential \(\phi\) on the signature vertices one must have

\[
 \boxed{
 \sum_X\max_{w\in\mathcal W_X}
       \big(\phi(\operatorname{head}w)
             -\phi(\operatorname{tail}w)\big)\ge0.}               \tag{0.2}
\]

This condition is also sufficient fractionally.  Taking
\(\phi=\mathbf1_U\) gives an explicit cut: the number of owners forced to
leave \(U\) cannot exceed the number of owners having some option to enter
\(U\).  All real potentials, not just set indicators, are needed in general.

The whole matrix is not an ordinary network matrix: the requirement “one arc
of each owner color” is a side constraint.  However, after the first \(H-1\)
letters have been fixed, choosing the final letter *is* an ordinary
capacitated bipartite flow.  This yields a complete integral Hoffman theorem
and a concrete cut which can be tested on any proposed SCD extension scheme.

No proof is obtained that the cuts always pass.  The exact remaining design
problem is to choose the first \(H-1\) letters so that the final-step demand is
nonnegative and satisfies every capacitated Hall cut.  The frame catalogue
does not interfere: every deterministic valid extension table has the same
success probability \(p_H\), so the existing \(W^{o(1)}\) augmentation
literalizes it unchanged.

## 1. Allowed words

For every middle owner \(X\), let

\[
 r_X=\min\{d_X,H\}                                                \tag{1.1}
\]

be its truncated SCD radius, and let

\[
 a_1(X),\ldots,a_{r_X}(X)                                        \tag{1.2}
\]

be its forced ordered lower deletions.  Define

\[
 \mathcal W_X=
 \left\{
 (d_1,\ldots,d_H):
 \begin{array}{l}
 d_i=a_i(X)\quad(1\le i\le r_X),\\
 d_1,\ldots,d_H\text{ are distinct elements of }X
 \end{array}
 \right\}.                                                       \tag{1.3}
\]

This set is nonempty because \(H\le m\).  For \(w=(d_1,\ldots,d_H)\), put

\[
 t(w)=(d_1,\ldots,d_{H-1}),\qquad
 h(w)=(d_2,\ldots,d_H).                                          \tag{1.4}
\]

Let \(\Theta\) be the set of injective ordered \((H-1)\)-tuples on
\([2m]\).  Every word in (1.3) is a directed arc \(t(w)\to h(w)\) in the
injective de Bruijn graph on \(\Theta\).

Choose variables \(x_{X,w}\), one color class for each owner.  The exact
extension system is

\[
 \sum_{w\in\mathcal W_X}x_{X,w}=1
 \qquad(X\in\Omega),                                             \tag{1.5}
\]

\[
 \sum_{X,w:t(w)=\theta}x_{X,w}
 -
 \sum_{X,w:h(w)=\theta}x_{X,w}=0
 \qquad(\theta\in\Theta),                                        \tag{1.6}
\]

\[
                         x_{X,w}\in\mathbb Z_{\ge0}.              \tag{1.7}
\]

The owner equation makes every integral variable binary.

### Proposition 1.1 (exactness)

Integral solutions of (1.5)--(1.7) are in bijection with one extension word
per owner having \(\Delta_{\rm seq}=0\).

#### Proof

Equation (1.5) selects exactly one allowed word for every owner.  Equation
(1.6) says that the selected word arcs have equal indegree and outdegree at
every signature.  This is exactly the vanishing of every summand in the
prefix/suffix imbalance. \(\square\)

The upper extensions have an identical system on \(X^c\).  The two systems
may be solved independently at this stage; their later placement on one
cycle is an additional coupling.

## 2. Exact fractional dual

Let \(P\) be the owner--word incidence matrix and \(B\) the directed
signature incidence matrix, with column

\[
                         B_w=e_{t(w)}-e_{h(w)}.                    \tag{2.1}
\]

The fractional system is

\[
                         Px=\mathbf1,\qquad Bx=0,\qquad x\ge0.    \tag{2.2}
\]

### Theorem 2.1 (potential form of every fractional cut)

System (2.2) is feasible if and only if, for every potential
\(\phi:\Theta\to\mathbb R\),

\[
 \boxed{
 \sum_X\max_{w\in\mathcal W_X}
       \big(\phi(h(w))-\phi(t(w))\big)\ge0.}                       \tag{2.3}
\]

#### Proof

Apply Farkas' lemma to the equality matrix

\[
                         M=\begin{pmatrix}P\\B\end{pmatrix},
 \qquad b=\binom{\mathbf1}{0}.                                   \tag{2.4}
\]

A dual pair \((\alpha,\phi)\) satisfies \(M^T(\alpha,\phi)\ge0\) precisely
when

\[
 \alpha_X+\phi(t(w))-\phi(h(w))\ge0
 \qquad(X,\ w\in\mathcal W_X).                                   \tag{2.5}
\]

For fixed \(\phi\), the smallest permitted \(\alpha_X\) is

\[
 \alpha_X=
 \max_{w\in\mathcal W_X}
       \big(\phi(h(w))-\phi(t(w))\big).                            \tag{2.6}
\]

Farkas says that \(\sum_X\alpha_X\ge0\) for every feasible dual pair.
Substitution gives (2.3), and the same argument in reverse proves
sufficiency. \(\square\)

Thus an explicit counterexample to fractional extension is a potential
\(\phi\) for which the left side of (2.3) is negative.

### Corollary 2.2 (set cut)

For \(U\subseteq\Theta\), define

\[
 L(U)=\#\{X:\text{every }w\in\mathcal W_X
                  \text{ leaves }U\},                            \tag{2.7}
\]

\[
 I(U)=\#\{X:\text{some }w\in\mathcal W_X
                  \text{ enters }U\}.                            \tag{2.8}
\]

Here “leaves” means \(t(w)\in U,h(w)\notin U\), and “enters” means the
reverse.  Fractional feasibility implies

\[
                              L(U)\le I(U).                        \tag{2.9}
\]

#### Proof

Take \(\phi=\mathbf1_U\) in (2.3).  A forced leaver contributes \(-1\), an
owner with an entering option contributes \(1\), and every remaining owner
contributes \(0\). \(\square\)

Applying the same statement to \(\Theta\setminus U\) gives the reverse
forced-entering cut.  These are genuine statewise Hoffman-type cuts, but set
potentials need not generate every real-potential inequality (2.3).

One tractable family of real potentials comes from coordinate weights.  For
\(\psi:[2m]\to\mathbb R\), put

\[
                         \phi_\psi(\theta_1,\ldots,\theta_{H-1})
                         =\sum_{i=1}^{H-1}\psi(\theta_i).          \tag{2.10}
\]

Then every word has telescoping potential difference

\[
 \phi_\psi(h(w))-\phi_\psi(t(w))
 =\psi(d_H)-\psi(d_1).                                           \tag{2.11}
\]

Hence fractional feasibility implies the explicit coordinate-potential
inequality

\[
 \boxed{
 \sum_X
 \max_{w\in\mathcal W_X}
 \big(\psi(d_H(w))-\psi(d_1(w))\big)\ge0.}                        \tag{2.12}
\]

For owners with \(r_X\ge1\), the first letter in (2.12) is fixed; for owners
with \(r_X\ge H\), the last letter is fixed as well.  Taking
\(\psi=\mathbf1_C\) recovers coordinate cuts such as Example 5.3 without
enumerating the full signature space.

More explicitly, the summand in (2.12) is

\[
\begin{cases}
 \max_{u\in X}\psi(u)-\min_{v\in X}\psi(v),
    &r_X=0,\\[1mm]
 \max\limits_{u\in X\setminus\{a_1,\ldots,a_{r_X}\}}\psi(u)
       -\psi(a_1),
    &1\le r_X<H,\\[1mm]
 \psi(a_H)-\psi(a_1),
    &r_X\ge H,
\end{cases}                                                       \tag{2.13}
\]

with the evident modification when the maximum and minimum must be attained
at distinct coordinates.  Formula (2.13) is a directly computable family of
statewise cuts for any concrete SCD.

## 3. Fractional minimum imbalance

The fractional relaxation of the best possible imbalance is

\[
 \delta_{\rm frac}
 =
 \min\left\{\|Bx\|_1:Px=\mathbf1,\ x\ge0\right\}.                  \tag{3.1}
\]

Its exact dual is

\[
 \boxed{
 \delta_{\rm frac}
 =
 \max_{\|\phi\|_\infty\le1}
 \sum_X
 \min_{w\in\mathcal W_X}
 \big(\phi(t(w))-\phi(h(w))\big).}                                \tag{3.2}
\]

#### Proof

Introduce \(z^+,z^-\ge0\) with
\(Bx-z^++z^-=0\) and minimize \(\mathbf1^T(z^++z^-)\).
The LP dual has owner multipliers \(\alpha_X\), signature multiplier
\(\phi\), constraints

\[
 \alpha_X+\phi(t(w))-\phi(h(w))\le0,\qquad
 \|\phi\|_\infty\le1.                                             \tag{3.3}
\]

Maximizing \(\sum_X\alpha_X\) eliminates \(\alpha_X\) and gives (3.2).
\(\square\)

For an integral choice, the owner leave needed to make the selected arcs
Eulerian is at least half its \(\ell_1\) imbalance.  Therefore any positive
lower bound from (3.2) is also a quantitative obstruction to the cycle
program.

There is also an exact dual for deleting owners before demanding fractional
Euler balance.  Put

\[
 \ell_{\rm ext}^{\mathbb R}
 =
 \min\left\{
 \sum_Xz_X:
 Px+z=\mathbf1,\ Bx=0,\ x,z\ge0
 \right\}.                                                       \tag{3.3a}
\]

Then

\[
 \boxed{
 \ell_{\rm ext}^{\mathbb R}
 =
 \max_{\phi:\Theta\to\mathbb R}
 \sum_X
 \min\left\{
 1,\
 \min_{w\in\mathcal W_X}
       \big(\phi(h(w))-\phi(t(w))\big)
 \right\}.}                                                      \tag{3.3b}
\]

Indeed, the owner dual variable is bounded above both by \(1\), from the
deletion variable, and by every potential difference
\(\phi(h(w))-\phi(t(w))\), from the word variables.  Formula (3.3b) is the
complete fractional statewise-cut value when an owner leave is allowed.
The required first-gate estimate is

\[
                         \ell_{\rm ext}^{\mathbb R}=o(W/H),       \tag{3.3c}
\]

or, more weakly but still sufficiently by Theorem 3.1,
\(\delta_{\rm frac}=o(W/H)\).

Taking \(\phi=-\mathbf1_U\) in (3.3b) yields the explicit quantitative
bound

\[
 \boxed{
 \ell_{\rm ext}^{\mathbb R}
 \ge
 \max_{U\subseteq\Theta}\big(L(U)-I(U)\big)_+.}                   \tag{3.3d}
\]

Thus the set cut of Corollary 2.2 measures actual unavoidable owner loss,
not merely failure of an exact no-leave system.

Before using the exact final-letter network, there is a useful asymptotic
rounding fact.  The colored-circulation integrality gap disappears at the
\(o(W/H)\) scale once fractional feasibility is known.

### Theorem 3.1 (fractional Euler flow rounds to sublinear imbalance)

Suppose \(x\) satisfies

\[
                         Px=\mathbf1,\qquad x\ge0.                 \tag{3.4}
\]

Choose independently for every owner one word according to its row
distribution \(x_{X,\cdot}\).  Let \(Z\in\mathbb Z^\Theta\) be the resulting
signature divergence.  Then

\[
 \mathbb E\|Z\|_1
 \le
 \|Bx\|_1+\sqrt{2W|\Theta|}.                                      \tag{3.5}
\]

Consequently some integral one-word-per-owner table satisfies

\[
 \Delta_{\rm seq}
 \le {1\over2}\|Bx\|_1+\sqrt{{W|\Theta|\over2}}.                  \tag{3.6}
\]

In the calibrated range

\[
 H\le C\sqrt{m\log m},
 \qquad
 |\Theta|=(2m)_{\underline{H-1}}=W^{o(1)},                        \tag{3.7}
\]

the second term in (3.6) is

\[
                         W^{1/2+o(1)}=o(W/H).                     \tag{3.8}
\]

In particular, a fractionally Eulerian extension table produces an integral
table with \(\Delta_{\rm seq}=o(W/H)\).

#### Proof

Write \(Z=\sum_XZ_X\), where \(Z_X\) is the signed tail-minus-head incidence
vector of the word sampled for owner \(X\).  The \(Z_X\)'s are independent,
\(\mathbb EZ=Bx\), and \(\|Z_X\|_2^2\le2\).  Therefore

\[
 \sum_{\theta\in\Theta}\operatorname{Var}Z_\theta
 \le\sum_X\mathbb E\|Z_X-\mathbb EZ_X\|_2^2
 \le2W.                                                         \tag{3.9}
\]

By the triangle inequality, Cauchy--Schwarz, and Jensen,

\[
\begin{aligned}
 \mathbb E\|Z\|_1
 &\le\|Bx\|_1+
      \sum_\theta\sqrt{\operatorname{Var}Z_\theta}\\
 &\le\|Bx\|_1+
      \sqrt{|\Theta|\sum_\theta\operatorname{Var}Z_\theta}\\
 &\le\|Bx\|_1+\sqrt{2W|\Theta|}.
\end{aligned}                                                    \tag{3.10}
\]

Since \(\Delta_{\rm seq}=\|Z\|_1/2\), some outcome proves (3.6).
Finally,

\[
 \log|\Theta|\le H\log(2m)=o(m),\qquad
 \log W=(2\log2+o(1))m,                                          \tag{3.11}
\]

which gives (3.7)--(3.8). \(\square\)

The lower and upper extension tables can be sampled together (independently,
or from any ownerwise joint law with the prescribed marginals).  Applying
(3.5) to both signs shows that one realization has total two-sided signature
imbalance \(o(W/H)\).

Thus the exact fractional dual (2.3), rather than TU, is the decisive
asymptotic question for this first gate.

## 4. Exact integral final-letter flow

The full colored-circulation matrix is not visibly a network matrix.  A
large and useful slice of it is.

Fix, for every owner, a valid ordered prefix

\[
                         v_X=(d_1(X),\ldots,d_{H-1}(X))            \tag{4.1}
\]

extending all forced SCD letters among the first \(H-1\) positions.

Let

\[
 \mathcal F=\{X:r_X\ge H\},\qquad
 \mathcal U=\Omega\setminus\mathcal F.                            \tag{4.2}
\]

For \(X\in\mathcal F\), the final letter \(d_H(X)=a_H(X)\) is fixed.  For
\(X\in\mathcal U\), its allowed final letters are

\[
                         R_X=X\setminus\{d_1(X),\ldots,d_{H-1}(X)\}.
                                                                         \tag{4.3}
\]

Every \(u\in R_X\) gives the possible head signature

\[
                         \eta_X(u)=(d_2(X),\ldots,d_{H-1}(X),u).   \tag{4.4}
\]

For \(\eta\in\Theta\), define the required flexible indegree

\[
 q_\eta=
 \#\{X:v_X=\eta\}
 -
 \#\{X\in\mathcal F:
       (d_2(X),\ldots,d_H(X))=\eta\}.                              \tag{4.5}
\]

The identity

\[
                         \sum_\eta q_\eta=|\mathcal U|            \tag{4.6}
\]

is automatic.

Build a bipartite graph with left side \(\mathcal U\), right side
\(\Theta\), and \(X\sim\eta_X(u)\) for \(u\in R_X\).  Give right vertex
\(\eta\) capacity \(q_\eta\).

### Theorem 4.1 (integral last-letter Hoffman theorem)

The fixed prefixes (4.1) extend to an exactly Eulerian one-word-per-owner
table if and only if

\[
                         q_\eta\ge0\quad(\eta\in\Theta)             \tag{4.7}
\]

and, for every \(\mathcal Z\subseteq\mathcal U\),

\[
 \boxed{
 |\mathcal Z|
 \le\sum_{\eta\in N(\mathcal Z)}q_\eta.}                          \tag{4.8}
\]

Equivalently, it is enough to test

\[
 \#\{X\in\mathcal U:N(X)\subseteq C\}
 \le\sum_{\eta\in C}q_\eta
 \qquad(C\subseteq\Theta).                                       \tag{4.9}
\]

Whenever these conditions hold, an integral choice of every final letter
exists.

#### Proof

The desired final letters are precisely a bipartite \(b\)-matching which
saturates every left owner once and uses right vertex \(\eta\) exactly
\(q_\eta\) times.  Conditions (4.7), (4.6), and (4.8) are the capacitated
Hall conditions.  They are necessary.  They are sufficient because the
source--left--right--sink network has integral capacities and a totally
unimodular node--arc incidence matrix.  Equation (4.9) is the standard
dual form of the same cuts. \(\square\)

The graph in Theorem 4.1 splits further.  For a flexible owner put

\[
 \zeta_X=(d_2(X),\ldots,d_{H-1}(X)),                              \tag{4.10}
\]

an ordered \((H-2)\)-tuple.  Every possible head of \(X\) is
\((\zeta_X,u)\).  Thus no final-letter edge crosses between different
stems \(\zeta\).

### Corollary 4.2 (stemwise Hoffman criterion)

For a stem \(\zeta\), set

\[
 \mathcal U_\zeta=\{X\in\mathcal U:\zeta_X=\zeta\},\qquad
 q_{\zeta,u}=q_{(\zeta,u)}.                                      \tag{4.11}
\]

The last-letter extension exists if and only if, for every \(\zeta\),

\[
 q_{\zeta,u}\ge0,\qquad
 \sum_{u\notin\zeta}q_{\zeta,u}=|\mathcal U_\zeta|,               \tag{4.12}
\]

and, for every coordinate set \(C\subseteq[2m]\setminus\zeta\),

\[
 \boxed{
 \#\{X\in\mathcal U_\zeta:R_X\subseteq C\}
 \le\sum_{u\in C}q_{\zeta,u}.}                                   \tag{4.13}
\]

#### Proof

The right neighbourhood of every \(X\in\mathcal U_\zeta\) is
\(\{(\zeta,u):u\in R_X\}\).  Hence the final-letter network is the disjoint
union, over \(\zeta\), of the incidence networks in (4.13).  Apply Theorem
4.1 in every component. \(\square\)

This is substantially sharper than a global expansion request.  The last
step is a family of ordinary coordinate-capacity matchings, one for each
ordered stem.  In particular, a stem with
\(\sum_uq_{\zeta,u}\ne|\mathcal U_\zeta|\) is already an explicit equality
cut, before any subset Hall inequality is tested.

The stem equality has a useful interpretation:

\[
 \sum_uq_{\zeta,u}=|\mathcal U_\zeta|
 \quad\Longleftrightarrow\quad
 \#\{X:(d_1,\ldots,d_{H-2})=\zeta\}
 =
 \#\{X:(d_2,\ldots,d_{H-1})=\zeta\}.                              \tag{4.14}
\]

Thus the chosen length-\((H-1)\) prefixes must already be Eulerian one order
lower.  This yields an exact recursive network formulation.

### Theorem 4.3 (recursive Hoffman resolution)

For \(1\le k\le H\), let

\[
 v_X^{(k)}=(d_1(X),\ldots,d_k(X)).                                \tag{4.15}
\]

There is an exactly Eulerian length-\(H\) extension table if and only if one
can choose the letters successively so that:

1. at stage \(k-1\), the words \(v_X^{(k-1)}\) are Eulerian on ordered
   \((k-2)\)-tuples; and
2. at stage \(k\), the demand and stemwise Hall conditions
   (4.12)--(4.13), with \(H\) replaced by \(k\), hold.

Whenever the stage-\(k\) cuts hold, the \(k\)-th letters can be chosen
integrally by a bipartite network flow.

#### Proof

The length-one table is automatically Eulerian on the unique empty
signature.  Suppose a length-\((k-1)\) table has been chosen.  Owners with
\(r_X\ge k\) have fixed \(k\)-th letter; the others have the coordinate
choices left in their owner sets.  Theorem 4.1 and Corollary 4.2, with \(k\)
in place of \(H\), are exactly the conditions and the integral construction
for the next letter.  Equation (4.14) is the component-total condition and
is equivalent to Eulerianity of the preceding table.

Conversely, project any Eulerian length-\(H\) word multiset onto its
consecutive length-\(k\) windows.  Every directed cycle remains a directed
cycle after this de Bruijn projection, so the projected length-\(k\) table
is Eulerian for every \(k\le H\).  At each stage its last letters constitute
a feasible matching in the network of Theorem 4.1, and hence satisfy all the
displayed cuts. \(\square\)

Theorem 4.3 removes a possible misconception.  There is no fractional
rounding loss *inside one successful stage*: every stage is an integral
network flow.  The open difficulty is adaptive prefix choice—one must choose
an integral point of the stage-\(k\) flow polytope which leaves the
stage-\((k+1)\) cuts feasible.

This theorem gives an explicit obstruction.  A negative \(q_\eta\), or one
violated set in (4.8), proves that the proposed first \(H-1\) prefixes cannot
be completed by any choice of final letters or frames.

## 5. The depth-two pilot

Before specializing, the SCD has an exact coordinate-flux identity.  Put

\[
 t_{q,u}=\#\{X:r_X\ge q,\ a_q(X)=u\},\qquad
 z_{q-1,u}=\#\{X:r_X=q-1,\ u\in X\}.                              \tag{5.0}
\]

### Lemma 5.1 (SCD deletion-label flux)

For every \(q\ge1\) and every coordinate \(u\),

\[
 \boxed{
 t_{q,u}+z_{q-1,u}
 =
 \binom{2m-1}{m-q}
 -
 \binom{2m-1}{m-q-1}.}                                           \tag{5.0a}
\]

#### Proof

Among all \(W/2\) middle owners containing \(u\), separate:

1. owners of radius \(<q\);
2. owners of radius at least \(q\) which delete \(u\) in one of their first
   \(q\) steps; and
3. owners of radius at least \(q\) whose depth-\(q\) target still contains
   \(u\).

The third class is in bijection, through the SCD, with the
rank-\((m-q)\) sets containing \(u\), and hence has size
\(\binom{2m-1}{m-q-1}\).  Writing this partition for \(q\) and \(q-1\) and
subtracting leaves exactly the owners of radius \(q-1\) and the owners
deleting \(u\) at step \(q\).  This proves (5.0a). \(\square\)

For \(H=2\), Theorem 4.1 has a particularly transparent form.  Put

\[
 \mathcal F=\{X:r_X\ge2\},\qquad
 \mathcal U=\{X:r_X=1\}.                                         \tag{5.1}
\]

Owners of radius zero may be discarded; their number is

\[
                         {W\over m+1}=o(W/H).                     \tag{5.2}
\]

For \(X\in\mathcal U\), the first deletion \(d_1(X)\) is fixed and the
second may be any member of the rank-\((m-1)\) SCD target

\[
                         T_X=X\setminus\{d_1(X)\}.                 \tag{5.3}
\]

For a coordinate \(u\), define

\[
 q_u=
 \#\{X\in\mathcal F\cup\mathcal U:d_1(X)=u\}
 -
 \#\{X\in\mathcal F:d_2(X)=u\}.                                  \tag{5.4}
\]

There is an exact formula for the first term.  Let

\[
 \mathcal Z=\{X:r_X=0\},\qquad R=|\mathcal Z|={W\over m+1},
 \qquad z_u=\#\{Z\in\mathcal Z:u\in Z\},                           \tag{5.4a}
\]

and let \(t_u=\#\{X:r_X\ge1,\ d_1(X)=u\}\).  Then

\[
 \boxed{t_u+z_u=R\qquad(u\in[2m]).}                               \tag{5.4b}
\]

Indeed, among the \(W/2\) middle owners containing \(u\), there are \(z_u\)
radius-zero owners, \(t_u\) active owners whose first SCD step deletes \(u\),
and exactly
\(\binom{2m-1}{m-2}\) active owners whose rank-\((m-1)\) target still
contains \(u\).  Since

\[
 {W\over2}-\binom{2m-1}{m-2}={W\over m+1}=R,                      \tag{5.4c}
\]

(5.4b) follows.  Thus the first-deletion histogram is completely determined
by the coordinate degrees of the radius-zero SCD antichain.

Using Lemma 5.1 once more at \(q=2\), the demand (5.4) has the fully
SCD-intrinsic form

\[
 q_u=
 \left[
 \binom{2m-1}{m-1}-2\binom{2m-1}{m-2}
 +\binom{2m-1}{m-3}
 \right]
 -z_{0,u}+z_{1,u},                                                \tag{5.4d}
\]

where \(z_{1,u}\) counts radius-one central owners containing \(u\).  Thus a
negative value in (5.4d) is an explicit coordinate cut against Eulerian
two-letter extension.

### Corollary 5.2 (complete \(H=2\) cut)

The active owners admit exactly balanced two-letter extensions if and only if

\[
 q_u\ge0\quad(u\in[2m])                                          \tag{5.5}
\]

and

\[
 \boxed{
 \#\{X\in\mathcal U:T_X\subseteq C\}
 \le\sum_{u\in C}q_u
 \quad(C\subseteq[2m]).}                                         \tag{5.6}
\]

When (5.5)--(5.6) hold, the extensions are integral.

Thus even the first nontrivial depth has a concrete, finite answer.  The SCD
theorem by itself does not imply (5.5) or (5.6).

### Example 5.3 (a literal negative-demand SCD)

The nonnegativity cut (5.5) can fail.  In \(B_4\), take the following SCD:

\[
\begin{array}{rcl}
 \varnothing&\subset&1\subset12\subset123\subset1234,\\
 2&\subset&23\subset234,\\
 3&\subset&34\subset134,\\
 4&\subset&24\subset124,\\
 &&13,\\
 &&14.
\end{array}                                                       \tag{5.7}
\]

Its positive-radius middle owners and lower deletion words are

\[
 12:(2,1),\qquad
 23:(3),\qquad
 34:(4),\qquad
 24:(2).                                                         \tag{5.8}
\]

At \(H=2\), after quarantining the two radius-zero owners \(13,14\), the
first-letter counts are

\[
                         (t_{1,1},t_{1,2},t_{1,3},t_{1,4})
                         =(0,2,1,1),                              \tag{5.9}
\]

whereas the fixed second-letter count from the radius-two owner is

\[
                         (t_{2,1},t_{2,2},t_{2,3},t_{2,4})
                         =(1,0,0,0).                              \tag{5.10}
\]

Thus \(q_1=-1\).  No choice of the three radius-one second letters can make
the active table Eulerian.  In fact the two radius-zero owners cannot repair
the defect: their sets are \(13\) and \(14\), so neither can use coordinate
\(2\) in its two-letter word.  Taking the signature cut
\(U=\{2\}\), the fixed words of owners \(12\) and \(24\) leave \(U\), only
the word of owner \(23\) enters \(U\), and every remaining owner has no
entering option.  Hence

\[
                              L(U)=2>I(U)=1.                       \tag{5.11}
\]

Corollary 2.2 proves fractional infeasibility of the **full** six-owner
extension system.  This is an explicit Hoffman obstruction, not an
integrality gap.

There is also an SCD-independent explanation at this parameter.  When
\(m=H=2\), every owner is one of the six edges of \(K_4\), and choosing its
two-letter word orients that edge.  Euler balance would orient all three
edges incident with every vertex with equal indegree and outdegree, impossible
because the degree is odd.  Thus no SCD of \(B_4\) has an exactly Eulerian
full two-letter extension table.

The finite example does not by itself refute an asymptotic theorem allowing
a small leave.  It proves that “arbitrary SCD plus arbitrary extension always
has \(\Delta_{\rm seq}=0\)” is false even in the first nontrivial case.

## 6. Frame realizability is neutral

Fix any deterministic lower and upper extension tables satisfying the
distinctness conditions.  For every owner the exact probability that a
uniform perfect matching literalizes both tables is

\[
 p_H=
 {((m-H)_{\underline H})^2
  \over\prod_{i=0}^{2H-1}(2m-2i-1)},                              \tag{6.1}
\]

independent of the actual extension labels.  Conditional balanced-type
success changes this by only the uniform factor
\(\gamma_{m,H}\in[1/2,1]\).

Consequently the same choice

\[
                         J=O(mp_H^{-1})                           \tag{6.2}
\]

of independent global frames literalizes at least one state at every owner,
by the original union-bound proof.  Solving (1.5)--(1.7), or the final-letter
flow of Theorem 4.1, before sampling frames does not increase the catalogue
size.

The lower and upper extension circulations can be solved independently before
this step because the success event deliberately pairs their marked
coordinates into disjoint direction families.  Whole-cycle placement later
couples the two orders again.

## 7. Why the general integral problem is still open

Theorem 4.1 is a network theorem only after the first \(H-1\) letters have
been fixed.  Choosing those prefixes simultaneously with the last letters
retains the owner-color constraints in (1.5).  A word column contains one
owner entry and a signed tail/head pair; there is no single node through
which every allowed choice of one owner can be routed without forgetting the
correlation between its tail and head.

Thus ordinary Hoffman theory proves exactly the final-letter slice, not the
whole colored circulation.  Fractional feasibility of the whole problem is
settled by (2.3); integral feasibility additionally requires rounding the
owner colors.  No TU claim is made.

The precise next target is:

> Choose the first \(H-1\) extensions so that the demands (4.5) are
> nonnegative and every cut (4.8) holds, simultaneously for the lower and
> upper tables, with at most \(o(W/H)\) exceptional owners.

If this is achieved, Theorem 4.1 supplies exact integral Euler balance and
Section 6 supplies the same \(W^{o(1)}\) literal frame catalogue.  The later
\(2h\)-cycle closure remains separate.

## 8. Final boundary

The extension gate is now an exact colored-circulation problem, not an
informal balancing request.  Its fractional dual is (2.3), its elementary
statewise cuts include (2.9), and its final-coordinate slice has the complete
integral Hoffman criterion (4.7)--(4.9).  Failure of any one of those cuts is
an explicit obstruction.

What is not proved is that an arbitrary SCD, or any known SCD, admits prefixes
passing those cuts at Gaussian depth.  The freedom in the extension suffixes
is substantial, and frame realizability is uniform, but the owner-colored
circulation remains the first open gate.
