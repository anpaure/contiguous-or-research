# Binary-rotor two-prefix program: exact Farkas inequality and the repeated-owner cycle obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,\qquad
 H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed and \(m\) is large enough that \(H\le m-1\).
This note audits the surviving nonsymmetric binary-rotor problem from
`MATH_THEOREM_ANTI_DIHEDRAL_NESTED_UCYCLE_GAUSSIAN_RETHREADING_20260726.md`.

There are two exact conclusions.

First, the finite fractional problem consisting of

* one unit from every middle-owner fibre;
* conservation at every permutation state; and
* both prefix-cover systems through depth \(H\)

has the following Farkas criterion.  If \(\phi:S_n\to\mathbb R\) is a
state potential and \(u_{q,T}^{\pm}\ge0\) are arbitrary weights on the
two signed target systems, define the weight \(\Lambda_u(\pi)\) collected
by a state and put

\[
 M_X(\phi,u)=
 \max_{\substack{\pi\in\mathcal F_X\\g\in\{A,B\}}}
 \bigl(\phi_\pi-\phi_{g\pi}+\Lambda_u(\pi)\bigr).
\]

Then fractional feasibility is equivalent to

\[
 \boxed{
 \sum_{q=0}^{H}\sum_T(u_{q,T}^-+u_{q,T}^+)
 \le \sum_{X\in\binom{[n]}m}M_X(\phi,u)
 \quad\hbox{for every }(\phi,u).}
 \tag{0.1}
\]

The exact uniform rotor circulation proves the strictly stronger bound

\[
 \boxed{
 \sum_XM_X(\phi,u)
 \ge
 \sum_{q=0}^{H}\lambda_q
       \sum_T(u_{q,T}^-+u_{q,T}^+),
 \qquad
 \lambda_q={W\over\binom n{m-q}}.}
 \tag{0.2}
\]

Thus **no fractional Farkas/Hall obstruction exists**, at Gaussian scale
or at any smaller scale.  The margin is exact: \(\lambda_0=1\),
\(\lambda_1=1+2/m\), and

\[
 \lambda_H=e^{A^2}\bigl(1+O_A(m^{-1/2})\bigr).
 \tag{0.3}
\]

Second, there is an exact support-preserving integrality obstruction on
the full Gaussian prefix program.  On the face

\[
                         z_{\pi,B}=0\quad(\pi\in S_n),
\]

the uniform \(A\)-circulation satisfies every constraint fractionally.
But every integral circulation on that face is a union of \(A\)-orbits,
each of length \(n-1=2m\), and hence requires \(2m\mid W\).  For every
prime \(m>2\),

\[
                         W=\binom{2m+1}{m}\equiv2\pmod m,
\]

so that face has no integral point.  This gives infinitely many genuine
Gaussian-scale fractional-feasible/integer-infeasible faces.
Moreover every unrestricted integral point then satisfies
\(\sum_\pi z_{\pi,B}\ge1\), which the feasible \(A\)-only point violates;
so the full LP is not the convex hull of its integral feasible points.

More locally, total-unimodularity fails by a growing determinant.  The
owner-plus-state-flow coefficient matrix contains, for every \(m\ge2\),
a square minor of determinant at least \(m\).  It comes
from the genuine rotor cycle

\[
                         (B^{n-2}A)^{n-1},
 \tag{0.4}
\]

on which some middle owner occurs \(k\ge m\) times.  On that cycle the
local integral right-hand side

\[
 \text{state flow }=0,\qquad \text{load of that owner }=1
\]

has the unique nonnegative solution \(x_e=1/k\) and no integral
solution.  This minor remains present after every prefix row through
\(H=\lceil A\sqrt m\rceil\) is added.

Hence the exact boundary is

\[
 \boxed{
 \text{the LP has quantitative Gaussian slack, but even a natural
 support face has an exact orbit-divisibility obstruction.}}
 \tag{0.5}
\]

This is an obstruction to LP/TU or independent-cycle rounding, not a
proof that the full integral rotor system is infeasible.  A positive
result still requires a global rounding in the owner-simple cycle
semigroup (and, for the coefficient-one compiler, the required small
component count).  No constant-one conclusion is claimed.

## 1. The exact finite two-prefix LP

Write \(\Pi=S_n\).  For

\[
 \pi=(x_1,\ldots,x_n)
\]

let

\[
 A\pi=(x_2,\ldots,x_{n-1},x_1,x_n),\qquad
 B\pi=(x_2,\ldots,x_n,x_1).
 \tag{1.1}
\]

The middle owner and its fibre are

\[
 X(\pi)=\{x_1,\ldots,x_m\},\qquad
 \mathcal F_X=\{\pi:X(\pi)=X\}.
 \tag{1.2}
\]

Their common size is

\[
                         D=m!(m+1)!.
 \tag{1.3}
\]

For \(0\le q\le H\), set

\[
 \mathcal V_q^- =\binom{[n]}{m-q},\qquad
 \mathcal V_q^+ =\binom{[n]}{m+1+q}.
 \tag{1.4}
\]

Define the two prefix incidences

\[
 p_{q,S}^-(\pi)=
 \mathbf1_{\{\{x_1,\ldots,x_{m-q}\}=S\}},
 \tag{1.5}
\]

\[
 p_{q,U}^+(\pi)=
 \mathbf1_{\{\{x_1,\ldots,x_{m+1+q}\}=U\}}.
 \tag{1.6}
\]

The fractional feasibility problem \((P_H)\) has variables
\(z_{\pi,g}\ge0\), \(\pi\in\Pi\), \(g\in\{A,B\}\), and constraints

\[
 \sum_{\pi\in\mathcal F_X}\sum_gz_{\pi,g}=1
 \qquad\left(X\in\binom{[n]}m\right),
 \tag{1.7}
\]

\[
 \sum_gz_{\sigma,g}
 -\sum_gz_{g^{-1}\sigma,g}=0
 \qquad(\sigma\in\Pi),
 \tag{1.8}
\]

\[
 \sum_{\pi,g}p_{q,S}^-(\pi)z_{\pi,g}\ge1
 \qquad(0\le q\le H,\ S\in\mathcal V_q^-),
 \tag{1.9}
\]

\[
 \sum_{\pi,g}p_{q,U}^+(\pi)z_{\pi,g}\ge1
 \qquad(0\le q\le H,\ U\in\mathcal V_q^+).
 \tag{1.10}
\]

The integral rotor problem is obtained by requiring

\[
                         z_{\pi,g}\in\{0,1\}.
 \tag{1.11}
\]

Nonnegative integrality would be equivalent, because (1.7) bounds every
variable by one.  Equations (1.7)--(1.8) then select directed state
cycles, exactly one selected state over every middle owner.  Equations
(1.9)--(1.10) are precisely the two all-depth prefix systems.

There are useful forced equalities.  The depth-zero lower equations in
(1.9) duplicate (1.7).  Moreover, for either sign and every \(q\),

\[
 \sum_T\sum_{\pi,g}p_{q,T}^{\pm}(\pi)z_{\pi,g}=W.
 \tag{1.12}
\]

At \(q=0\), both target layers have exactly \(W\) members.  Therefore
(1.10) at \(q=0\) is automatically an equality target by target.  For an
integral feasible point, if

\[
 N_q=\binom n{m-q},\qquad E_q=W-N_q,
 \tag{1.13}
\]

then the exact excess-multiplicity ledger at either sign is

\[
 \sum_{T\in\mathcal V_q^{\pm}}
       \bigl(\operatorname{load}_q^{\pm}(T)-1\bigr)=E_q.
 \tag{1.14}
\]

In particular,

\[
 E_0=0,qquad E_1={2W\over m+2}.
 \tag{1.15}
\]

Thus the shallow rows have very little integral collision allowance;
this fact is not visible as a fractional feasibility failure.

## 2. Exact Farkas dual

For nonnegative target weights

\[
 u^-=(u_{q,S}^-)\ge0,qquad
 u^+=(u_{q,U}^+)\ge0,
\]

put

\[
 \Lambda_u(\pi)=
 \sum_{q=0}^{H}
 \left(
  u^-_{q,\{x_1,\ldots,x_{m-q}\}}
 +u^+_{q,\{x_1,\ldots,x_{m+1+q}\}}
 \right).
 \tag{2.1}
\]

### Theorem 2.1 (arc-potential Farkas criterion)

The fractional system \((P_H)\) is feasible if and only if (0.1) holds
for every \(\phi\in\mathbb R^{\Pi}\) and every \(u^{\pm}\ge0\).

#### Proof

Give (1.7) a free multiplier \(\alpha_X\), give (1.8) a free multiplier
\(\phi_\sigma\), and give (1.9)--(1.10) the nonnegative multipliers
\(u^{\pm}\).  The coefficient of \(z_{\pi,g}\) is

\[
 \alpha_{X(\pi)}+\phi_\pi-\phi_{g\pi}+\Lambda_u(\pi).
 \tag{2.2}
\]

Farkas' lemma says that infeasibility is equivalent to the existence of
these multipliers such that

\[
 \alpha_{X(\pi)}+\phi_\pi-\phi_{g\pi}+\Lambda_u(\pi)\le0
 \quad(\pi,g)
 \tag{2.3}
\]

but

\[
                     \sum_X\alpha_X+\sum_{q,T}(u_{q,T}^-+u_{q,T}^+)>0.
 \tag{2.4}
\]

For fixed \((\phi,u)\), the largest allowed value of \(\alpha_X\) is

\[
 \alpha_X=-
 \max_{\substack{\pi\in\mathcal F_X\\g\in\{A,B\}}}
 \bigl(\phi_\pi-\phi_{g\pi}+\Lambda_u(\pi)\bigr)
 =-M_X(\phi,u).
 \tag{2.5}
\]

Substituting (2.5) into (2.4) shows that a certificate exists exactly
when (0.1) fails. \(\square\)

The state potential in (0.1) is essential.  It is the price of exact
chronological flow and cannot in general be replaced by target weights
alone.

### Theorem 2.2 (uniform domination of every Farkas functional)

For every \(\phi\) and \(u^{\pm}\ge0\), inequality (0.2) holds.

#### Proof

Fix any \(t\in[0,1]\) and set

\[
 z^0_{\pi,A}={t\over D},\qquad
 z^0_{\pi,B}={1-t\over D}.
 \tag{2.6}
\]

The total mass in each owner fibre is one.  Every state has outgoing
mass \(1/D\), and its two incoming arc weights sum to \(1/D\), so
(1.8) holds.

For a fixed set of rank \(r\), exactly \(r!(n-r)!\) permutations have
that set in their first \(r\) positions.  Hence every target in either
system at depth \(q\) has load

\[
 { (m-q)!(m+1+q)!\over m!(m+1)!}
 ={W\over\binom n{m-q}}
 =\lambda_q.
 \tag{2.7}
\]

For each owner, a maximum is at least the average with respect to the
unit fibre mass (2.6).  Summing those averages gives

\[
\begin{aligned}
 \sum_XM_X(\phi,u)
 &\ge
 \sum_{\pi,g}z^0_{\pi,g}
 \bigl(\phi_\pi-\phi_{g\pi}+\Lambda_u(\pi)\bigr)\\
 &=\sum_{q=0}^{H}\lambda_q
       \sum_T(u_{q,T}^-+u_{q,T}^+).
\end{aligned}
 \tag{2.8}
\]

The potential term vanishes by state-flow conservation.  This proves
(0.2). \(\square\)

Thus a dual search cannot close the nonsymmetric rotor lane at the
fractional level.  It must either add a valid integer/cycle inequality or
price a condition absent from (1.7)--(1.10), such as the number of
components.

## 3. Exact Gaussian accounting

From factorial cancellation,

\[
 \lambda_q
 =\prod_{j=0}^{q-1}{m+2+j\over m-j}.
 \tag{3.1}
\]

Uniformly for \(0\le q\le H=\lceil A\sqrt m\rceil\), Taylor expansion
with a uniform remainder gives

\[
 \log\lambda_q
 ={q(q+1)\over m}
 +O_A\!\left({(q+1)^3\over m^2}\right)
 ={q(q+1)\over m}+O_A(m^{-1/2}).
 \tag{3.2}
\]

The ceiling changes \(H(H+1)/m\) by only \(O_A(m^{-1/2})\), so (0.3)
follows.  In particular,

\[
 N_H=\bigl(e^{-A^2}+O_A(m^{-1/2})\bigr)W.
 \tag{3.3}
\]

For the unweighted functional \(u_{q,T}^{\pm}=1\), take \(\phi=0\).
Every state then collects exactly \(2(H+1)\), so (2.8) is an equality
and the Farkas surplus over the required target weight is exactly

\[
 2\sum_{q=0}^{H}(W-N_q).
 \tag{3.4}
\]

The uniform local limit implicit in (3.2), followed by a Riemann sum,
gives

\[
 \sum_{q=0}^{H}{N_q\over W}
 =\sqrt m\int_0^Ae^{-x^2}\,dx+O_A(1).
 \tag{3.5}
\]

Consequently (3.4) equals

\[
 2W\sqrt m
 \left(A-\int_0^Ae^{-x^2}\,dx\right)+O_A(W).
 \tag{3.6}
\]

This is positive for every fixed \(A>0\).  The only tight rank in the
fractional dual is depth zero; the first positive margin is the exact
\(2/m\) in (1.15).

## 4. An exact support-preserving obstruction on the \(A\)-only face

The uniform point (2.6) is feasible even at the endpoint \(t=1\), where
it uses only \(A\)-arcs.  Unlike the general non-TU observation, this
already gives an integer obstruction for the complete all-owner,
all-prefix right-hand side.

### Theorem 4.1 (prime orbit-divisibility obstruction)

Impose the valid face equations

\[
                         z_{\pi,B}=0
 \qquad(\pi\in S_n).
 \tag{4.1}
\]

The face of \((P_H)\) defined by (4.1) is fractionally nonempty for every
\(0\le H\le m-1\).  If it contains an integral point, then

\[
                         2m\mid W.
 \tag{4.2}
\]

Consequently, for every prime \(m>2\), this face is fractionally feasible
but contains no integral point, for

\[
                         W\equiv2\pmod m.
 \tag{4.3}
\]

In particular this is an exact obstruction at
\(H=\lceil A\sqrt m\rceil\) for every sufficiently large prime \(m\).

Equivalently, on the unrestricted program every integral feasible point
for prime \(m>2\) satisfies the valid integer-hull inequality

\[
                         \sum_{\pi\in S_n}z_{\pi,B}\ge1,
 \tag{4.3a}
\]

whereas the feasible fractional point (4.4) has left side zero.  Thus
the full relaxation \((P_H)\) is genuinely nonintegral; the obstruction
is not merely a failure of one rounding algorithm.

#### Proof

Take \(t=1\) in (2.6).  Thus

\[
                         z_{\pi,A}={1\over D},\qquad
                         z_{\pi,B}=0.
 \tag{4.4}
\]

The proof of Theorem 2.2 shows that (4.4) satisfies the owner and flow
equalities and gives every signed depth-\(q\) target load
\(\lambda_q\ge1\).  Hence it is feasible on the displayed face for all
\(H\le m-1\).

Now suppose \(z\) is integral on that face.  If one \(A\)-arc out of a
state \(\pi\) is selected, state-flow conservation forces the unique
\(A\)-arc out of \(A\pi\) to be selected, and then the same is true
around the entire \(A\)-orbit.  The position permutation \(A\) is one
cycle on its first \(n-1=2m\) positions and fixes the last position, so
every state has an \(A\)-orbit of exact length \(2m\).  The selected
states are therefore a disjoint union of \(2m\)-element orbits.

On the other hand, summing the owner equations (1.7) shows that the
number of selected states is exactly \(W\).  This proves (4.2).

It remains to audit (4.3).  If \(m=p>2\) is prime, the freshman's-dream
congruence gives

\[
 (1+x)^{2p+1}
 =(1+x)\bigl((1+x)^p\bigr)^2
 \equiv(1+x)(1+x^p)^2\pmod p.
 \tag{4.5}
\]

The coefficient of \(x^p\) on the right is two.  Therefore

\[
                         \binom{2p+1}{p}\equiv2\pmod p,
\]

so \(p\nmid W\), and a fortiori \(2p\nmid W\).  There are infinitely
many primes, completing the proof. \(\square\)

### Corollary 4.2 (what support-preserving rounding cannot do)

No theorem which rounds a feasible rotor circulation while preserving
the zero pattern of its rotor types can hold for \((P_H)\), even with
both prefix systems and their exact Gaussian slack.  In particular, the
uniform \(A\)-point cannot be rounded by cycle decomposition within its
support for infinitely many \(m\).

In fact it does not belong to the convex hull of any unrestricted
integral feasible points: every such point obeys (4.3a), and any
nonnegative convex combination with zero total \(B\)-mass could use only
integral points on the empty \(A\)-only face.

Equivalently, for every prime \(m>2\), the following is a valid inequality
for the integer hull of the complete rotor program:

\[
                         \boxed{\sum_{\pi\in S_n}z_{\pi,B}\ge1.}
 \tag{4.6}
\]

The fractional point (4.4) violates (4.6).  Thus it is not merely a bad
choice for a particular rounding algorithm: it lies outside the convex
hull of all integral feasible rotor circulations.  Indeed, a convex
combination with zero \(B\)-mass could use only integral points having
zero \(B\)-mass, and Theorem 4.1 says that no such point exists.

This does **not** obstruct the unrestricted two-rotor problem: allowing
\(B\)-arcs leaves the face (4.1).  Indeed the \(B\)-only face has orbit
length \(n\), and \(W/n=\operatorname{Cat}_m\) is integral.  The point
of Theorem 4.1 is that the fractional segment between the two rotor types
does not possess support-preserving integrality.

There is a quantitative version once the required component bound is
restored.

### Proposition 4.3 (the reciprocal Catalan rotor toll)

Let an integral owner-transversal rotor circulation have \(C\) support
components, let \(b\) be its number of selected \(B\)-arcs, and let
\(c_A\) be its number of pure-\(A\) components.  Then

\[
 \boxed{W\le(n-2)b+(n-1)c_A\le(n-2)b+(n-1)C.}
 \tag{4.7}
\]

Consequently,

\[
 C=o(W/m)
 \quad\Longrightarrow\quad
 b\ge(1-o(1)){W\over n-2}
   =(1-o(1)){W\over2m}.
 \tag{4.8}
\]

Combined with the previously proved \(A\)-switch toll, every viable
few-component circulation must use **both** rotor types on Catalan order:

\[
                         a,b\ge(1-o(1)){W\over2m}.
 \tag{4.9}
\]

#### Proof

A pure \(A\)-component is one full \(A\)-orbit and has \(n-1\) states.
Consider a maximal \(A\)-run in a component containing a \(B\)-arc.  If
that run contained all \(n-1\) states of its \(A\)-orbit, its first state
\(A\pi\) would be selected when its last state \(\pi\) takes the outgoing
\(B\)-arc.  The state \(B\pi\) is also selected.  But \(A\pi\) and
\(B\pi\) agree in their first \(n-2\) positions, and hence have the same
middle owner, while they are distinct.  This contradicts (1.7).

Thus every non-pure maximal \(A\)-run has at most \(n-2\) states.  A
non-pure component with \(b_C\) \(B\)-arcs has exactly \(b_C\) such
runs.  Summing their lengths and then adding the pure components proves
(4.7).  Rearrangement gives (4.8).  The corresponding lower bound on
\(a\) is the established \(B\)-run toll

\[
                         W\le(n-1)a+nC.
\]

Together they give (4.9). \(\square\)

## 5. The genuine non-TU rotor cycle

The following argument converts the known one-hole rotor geometry into
an exact determinant obstruction.

### Lemma 5.1 (a simple repeated-owner rotor cycle)

For every \(m\ge2\), the directed rotor state graph contains a simple
cycle \(C\) of length

\[
                         L=(n-1)^2
 \tag{5.1}
\]

with control word (0.4).  The states on \(C\) use at most
\(2(n-1)\) distinct middle owners.  Hence some owner \(X_*\) occurs

\[
                         k\ge {L\over2(n-1)}={n-1\over2}=m
 \tag{5.2}
\]

times on \(C\).

#### Proof

Choose a state \(h_0\) and put

\[
                         h_j=A^{-j}h_0
 \qquad(j\in\mathbb Z_{n-1}).
 \tag{5.3}
\]

The identity

\[
                         B^{-1}AB^{-1}=A^{-1}
 \tag{5.4}
\]

implies

\[
                         AB^{-1}h_j=Bh_{j+1}.
 \tag{5.5}
\]

For each \(j\), traverse the \(n-1\) states

\[
 Bh_j,B^2h_j,\ldots,B^{-1}h_j
 \tag{5.6}
\]

using \(n-2\) internal \(B\)-arcs, and then use (5.5) as one \(A\)-arc
to the next run.  Since \(A\) has order \(n-1\), the runs close after
\(n-1\) steps.  Distinct runs lie in distinct \(B\)-orbits: after writing

\[
                         h_0=(c_1,\ldots,c_{n-1},z),
 \tag{5.7}
\]

every \(h_j\) has \(z\) in its last position, and two of them can be
cyclic rotations only if they are equal.  Thus the cycle is simple and
has length \((n-1)^2\).

Its \(B\)-orbits are the cyclic coordinate orders obtained by inserting
\(z\) into the gaps of the fixed cycle on
\((c_1,\ldots,c_{n-1})\).  A middle interval either avoids \(z\), in
which case it is one of at most \(n-1\) length-\(m\) intervals of the
fixed cycle, or contains \(z\), in which case deleting \(z\) leaves one
of at most \(n-1\) length-\((m-1)\) intervals.  Thus there are at most
\(2(n-1)\) owner names.  Pigeonhole gives (5.2). \(\square\)

### Theorem 5.2 (large determinant minor)

Let \(M_H\) be the coefficient matrix of (1.7)--(1.10), with the flow
equalities written as rows.  For every \(m\ge2\), \(M_H\) has a square
minor of determinant \(k\) in absolute value for some \(k\ge m\).
In particular, \(M_H\) is not totally unimodular.  This holds for every
\(H\), including \(H=\lceil A\sqrt m\rceil\).

#### Proof

Index the states and selected rotor arcs of the cycle in Lemma 5.1 by

\[
 \pi_0,\ldots,\pi_{L-1},\qquad
 e_i:\pi_i\longrightarrow\pi_{i+1},
 \]

with cyclic subscripts.  Restrict to the \(L\) columns \(e_i\).  Take
the state-flow rows at \(\pi_0,\ldots,\pi_{L-2}\), and append the owner
row for \(X_*\).

The first \(L-1\) rows form the directed incidence matrix of a cycle
with one vertex row deleted.  Every maximal minor of that incidence
matrix has absolute value one, and its signed cofactor vector is the
all-ones vector, since that vector spans the nullspace.  The appended
owner row is the indicator vector \(w\) of the \(k\) occurrences of
\(X_*\) on the cycle.  Expansion along the last row therefore gives

\[
                         |\det M|=\sum_{i=0}^{L-1}w_i=k\ge m.
 \tag{5.8}
\]

Only owner and flow rows were used.  Adding either prefix family cannot
remove this minor. \(\square\)

### Corollary 5.3 (explicit local fractional-only cell)

Set every rotor variable outside \(C\) to zero and impose flow balance
on \(C\) together with unit load on \(X_*\).  The unique nonnegative
solution is

\[
                         x_{e_i}={1\over k}
 \qquad(0\le i<L),
 \tag{5.9}
\]

and there is no integral solution.

#### Proof

Flow balance on a directed cycle forces all arc variables to have one
common value \(t\).  The \(X_*\)-row is then \(kt=1\), giving (5.9).
If the variables were integral, \(kt=1\) would be impossible because
\(k\ge2\). \(\square\)

This is a statewise obstruction with the same owner and flow columns as
the full Gaussian program.  Its scope must not be overstated: it is not
itself a right-hand-side restriction of the complete all-owner system,
because the other owner equations are omitted in the local cell.  It
proves that neither network integrality nor a generic TU theorem can
round (0.2).

There is also an exact integral congruence absent from the LP.  Since
\(A\) is an \((n-1)\)-cycle of positions and \(B\) an \(n\)-cycle,

\[
                         \operatorname{sgn}(A)=-1,
 \qquad \operatorname{sgn}(B)=+1.
 \tag{5.10}
\]

The control product around every integral rotor component is the
identity permutation of positions.  Hence every integral component
contains an even number of \(A\)-arcs.  This parity is another genuine
cycle-semigroup constraint not expressible by (0.1).

## 6. Exact cycle-semigroup boundary

Let \(\mathscr C\) be the directed simple cycles of the rotor state graph.
For \(C\in\mathscr C\), let

\[
 a_X(C)=\#\{\pi\in C:X(\pi)=X\},
\]

and let \(b_{q,T}^{\pm}(C)\) be its signed prefix multiplicities.  The
exact integral feasibility problem is

\[
\begin{aligned}
 &\sum_Ca_X(C)\xi_C=1 &&\left(X\in\binom{[n]}m\right),\\
 &\sum_Cb_{q,T}^{\pm}(C)\xi_C\ge1
     &&(0\le q\le H,\ T\in\mathcal V_q^{\pm}),\\
 &\xi_C\in\mathbb Z_{\ge0}.&&
\end{aligned}
 \tag{6.1}
\]

The owner equations automatically forbid every repeated-owner cycle,
including Lemma 5.1, and make distinct selected cycles state-disjoint.
Thus (6.1) is exactly the Boolean rotor problem.  Dropping integrality
recovers the fractional circulation after ordinary cycle decomposition.

If component count is minimized, the exact integer master is

\[
                         \min\sum_C\xi_C
 \tag{6.2}
\]

subject to (6.1).  Its fractional dual is

\[
\begin{aligned}
 \max\quad&\sum_X\alpha_X+\sum_{q,T,\pm}\beta_{q,T}^{\pm},\\
 \text{subject to}\quad&
 \sum_Xa_X(C)\alpha_X+
 \sum_{q,T,\pm}b_{q,T}^{\pm}(C)\beta_{q,T}^{\pm}\le1
 \quad(C\in\mathscr C),\\
 &\alpha_X\in\mathbb R,\qquad \beta_{q,T}^{\pm}\ge0.
\end{aligned}
 \tag{6.3}
\]

The arc potentials in Theorem 2.1 are the finite-state reduced-cost form
of the same fractional separation.  Corollary 5.3 shows exactly where
the integer master departs from it: a fractional circulation may use a
repeated-owner cycle with a fractional coefficient, while the integral
semigroup may not use that cycle at all.

## 7. Proved and unproved boundary

Proved here:

1. (1.7)--(1.10) is the exact finite LP coupling owner transversality,
   binary-rotor flow, and both prefix-cover systems, with all rank floors
   explicit.
2. (0.1) is its exact arc-potential Farkas dual.
3. The uniform rotor circulation proves the stronger quantitative
   inequality (0.2); hence no fractional dual obstruction exists.
4. At \(H=\lceil A\sqrt m\rceil\), the exact endpoint margin is
   \(e^{A^2}(1+O_A(m^{-1/2}))\), while depth one has only the exact
   margin \(2/m\).
5. On the \(A\)-only support face, the complete two-prefix LP is
   fractionally feasible but has no integer point for every prime
   \(m>2\).
6. With \(o(W/m)\) components, both rotor types must occur at least
   \((1-o(1))W/(2m)\) times.
7. The full constraint matrix contains a determinant-\(k\) minor with
   \(k\ge m\), and the corresponding rotor-cycle cell has a unique
   fractional solution and no integral solution.
8. Every integral component has even \(A\)-switch parity.

Not proved here:

1. infeasibility of the complete unrestricted integer system (6.1);
2. an integral solution satisfying both prefix systems;
3. the required bound \(o(W/m)\) on its number of support cycles; or
4. the constant-one theorem.

The LP/Farkas lane is therefore exhausted cleanly.  Any next theorem
must concern the owner-simple cycle semigroup itself: an odd-set or
congruence inequality violated by the uniform point, or a global
dependent rounding which never creates a repeated-owner cycle.  Pure
fractional Hall weights cannot decide the gate.
