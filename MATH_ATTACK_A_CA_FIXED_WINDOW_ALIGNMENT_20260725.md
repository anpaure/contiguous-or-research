# Fixed-window cyclic alignment: star-cut safety and the integral rounding gate

Date: 2026-07-25

Method: pure mathematics only.  No finite search, solver, web lookup, or
long computation is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn=\operatorname{Cat}_m,
\qquad K=\lceil A\sqrt m\rceil .
\]

This attack does **not** prove \((\mathrm{CA}_A)\).  It proves four new
facts which sharply reduce, and partly close, natural subroutes to it.

1.  The zero-error form of \((\mathrm{CA}_A)\) is exactly a simultaneous
    strict-discrepancy-one integral rounding problem in one layered
    cyclic-order hypergraph.  The uniform fractional point lies in the
    convex hull of genuine exact middle factors, so there is no fractional
    exact-factor or common-flag obstruction.

2.  For every fixed order \(t\), every internal \(t\)-star Hall-capacity
    cut in the evolving adjacent-swap graphs is automatically safe at

    \[
    K-O_{A,t}(1)
    \]

    depths, for every exact factor and every earlier swap history.  Thus an
    internal fixed-order star-capacity obstruction can occur only in an
    order-one collar of the depths at which \(W/N_q\) crosses an integer.
    The pair case has a sharp cyclic-distance formula and gives a
    factor-specific lower bound directly on the labelled error \(e_q\).

3.  Exact point-regular balanced quotas exist at every rank.  When
    \(2m+1\) is prime, there is moreover an integral common balanced nested
    resolution with exact deletion-time coordinate homomesy.  Thus point
    margins, common nesting, and integrality are jointly compatible, while
    every fixed-order containment margin is separately compatible rank by
    rank.  None can be the missing obstruction by itself.

4.  Two tempting rounding principles are false.  A literal cyclic
    \(\tau\)-fold exact middle cover satisfies all homogeneous ownership
    ledgers but violates a pair-star Hall cut throughout the bulk.  Also,
    regularity, a uniform fractional perfect matching, edge rank
    \(\Theta(m^{3/2})\), and relative codegree \(\Theta(1/m)\) do not imply
    even a nontrivial matching.  Therefore neither homogeneous/fractional
    packet averaging nor a growing-rank matching argument based only on
    those numerical summaries can prove \((\mathrm{CA}_A)\).

The smallest surviving sufficient lemma is collective.  One must choose
one indivisible exact factor, balanced quotas, and
\(o(W/K)\) permanently exceptional owners so that both the bounded-rank
survival packets and **every residual inclusion-Hall cut** are satisfied.
This condition directly implies \((\mathrm{CA}_A)\), but is unproved.

## 1. The layered cyclic-order hypergraph

Let \(\mathscr W_m\) be the set of cyclic orders of \([n]\), modulo
rotation and reversal.  For \(\pi\in\mathscr W_m\), put

\[
\mathcal C_q(\pi)
=\{I_\pi(j,m-q):j\in\mathbb Z_n\},
\qquad 0\le q\le K.
\tag{1.1}
\]

For every proper interval length, the \(n\) members of
\(\mathcal C_q(\pi)\) are distinct.  Define the layered hypergraph with
parts

\[
V_q=\binom{[n]}{m-q}
\]

and one edge

\[
E_\pi=\mathop{\dot\bigcup}_{q=0}^{K}\mathcal C_q(\pi)
\tag{1.2}
\]

for every \(\pi\).  Let \(A_q\) be its incidence matrix on the part
\(V_q\).  Finally put

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q},\qquad
c_q=\lfloor\lambda_q\rfloor.
\tag{1.3}
\]

### Theorem 1.1 — exact capacitated-factor formulation

For a nonnegative integral vector \(x=(x_\pi)\), the system

\[
A_0x=\mathbf1,
\qquad
c_q\mathbf1\le A_qx\le(c_q+1)\mathbf1
\quad(1\le q\le K)
\tag{1.4}
\]

is equivalent to a zero-error fixed-window alignment: one exact middle
wreath factor \(F\) and one balanced nested resolution \(P\) for which

\[
e_q(F,P)=0\qquad(q\le K).
\tag{1.5}
\]

Equivalently, (1.4) is

\[
\boxed{
A_0x=\mathbf1,\qquad
\|A_qx-\lambda_q\mathbf1\|_\infty<1
\quad(1\le q\le K).}
\tag{1.6}
\]

#### Proof

The equation \(A_0x=\mathbf1\) forces \(x_\pi\in\{0,1\}\) and says that
the selected middle wreaths partition \(\binom{[n]}m\).  They therefore
form an exact middle factor.  Orient every selected row arbitrarily.  For
the unique pointed occurrence \(X=I_\pi(j,m)\), define

\[
P_q(X)=I_\pi(j,m-q).
\tag{1.7}
\]

These sets are nested in \(q\), and their depth-\(q\) fibre vector is
exactly \(A_qx\).  Thus (1.4) makes \(P\) balanced and gives (1.5).
The converse reads the same fibre vectors from a zero-error pair.

If \(\lambda_q\notin\mathbb Z\), the integers at distance strictly less
than one from \(\lambda_q\) are precisely \(c_q,c_q+1\).  If
\(\lambda_q\in\mathbb Z\), the total depth-\(q\) mass is
\(W=\lambda_qN_q\), so (1.4) forces every entry to equal \(\lambda_q\).
This proves (1.6).  \(\square\)

Theorem 1.1 is deliberately stronger than \((\mathrm{CA}_A)\): it asks
for zero error, not \(o(W)\) weighted error.

### Theorem 1.2 — one common fractional exact-factor point

A fixed rank-\((m-q)\) target lies in exactly

\[
D_q=\frac{(m-q)!(m+q+1)!}{2}
\tag{1.8}
\]

unoriented cyclic orders.  Hence

\[
\frac{D_q}{D_0}=\lambda_q.
\tag{1.9}
\]

The uniform vector

\[
x^0_\pi=\frac1{D_0}
\tag{1.10}
\]

satisfies simultaneously

\[
A_0x^0=\mathbf1,
\qquad
A_qx^0=\lambda_q\mathbf1
\quad(1\le q\le K).
\tag{1.11}
\]

Moreover \(x^0\) lies in the convex hull of incidence vectors of genuine
exact middle factors.

#### Proof

After contracting a prescribed interval to one cyclic block, its internal
order and the linear order of its complement give (1.8).  Division by

\[
D_0=\frac{m!(m+1)!}{2}
\]

gives (1.9), and the degree equations give (1.11).

Take one known exact factor and average all of its coordinate relabellings.
The symmetric group is transitive on \(\mathscr W_m\), so every wreath has
the same average coefficient.  That coefficient is \(1/D_0\), since every
middle target has average degree one.  Thus the average is exactly (1.10).
\(\square\)

The missing step is therefore a sharp integral rounding inside the exact
factor fibre.  Approximate regularity is not the requested conclusion:
the target discrepancy is strictly below one.

## 2. Exact flag clustering and a generic matching no-go

### Lemma 2.1 — descendant codegrees

Let \(S\in V_q\), put \(|S|=r=m-q\), and let
\(T\subset S\) have size \(r-t\), where \(1\le t\le K-q\).  Then

\[
\boxed{
\operatorname{codeg}(S,T)
=D_q\frac{t+1}{\binom rt}.}
\tag{2.1}
\]

Every edge containing \(S\) contains exactly \(t+1\) descendants of
\(S\) of size \(r-t\).

#### Proof

Condition on \(S\) being one cyclic interval.  Its induced linear order is
uniform.  The specified \((r-t)\)-set \(T\) is an interval precisely when
it occupies one of the \(t+1\) possible positions, among the
\(\binom rt\) equally likely subsets.  This proves (2.1).  Summing over
all \(T\subset S\) gives the last assertion.  \(\square\)

In particular an adjacent nested pair has relative codegree \(2/r\).
The middle wreath hypergraph also has relative codegree

\[
\frac2{m+1}
\tag{2.2}
\]

on a disjoint pair of middle sets.  Thus the fixed-window edge rank and
native pair scale are

\[
|E_\pi|=n(K+1)=\Theta_A(m^{3/2}),
\qquad
\Delta_2/D_0=\Theta_A(m^{-1}).
\tag{2.3}
\]

For completeness, the upper bound in (2.3) follows from the exact
two-interval cases.  Condition on an interval \(S\) of size
\(r\in[m-K,m]\).  For a second interval \(T\) in the same band, its
conditional probability is

\[
\frac{a+1}{\binom ra}
\quad\text{if }T\subsetneq S,\ |S\setminus T|=a,
\]

\[
\frac{b+1}{\binom{n-r}b}
\quad\text{if }S\subsetneq T,\ |T\setminus S|=b,
\]

\[
\frac{h+1}{\binom{n-r}h}
\quad\text{if }S\cap T=\varnothing,\ 
h=n-r-|T|\ge1,
\]

and

\[
\frac2{\binom r{|S\cap T|}
          \binom{n-r}{|T\setminus S|}}
\]

in the proper crossing case.  Every displayed value is at most
\(2/(m-K)\) for sufficiently large \(m\).  Since every band degree is at
most \(C_AD_0\),

\[
\frac{2D_0}{m}\le\Delta_2
\le\frac{2C_AD_0}{m-K}.
\tag{2.3a}
\]

The product of these two normalized parameters diverges like
\(\sqrt m\).  The reason is not accidental noise: (2.1) is an exact
nested-flag cluster.

### Proposition 2.2 — the numerical matching data are insufficient

There are regular hypergraphs with

\[
R=\Theta_A(Q^{3/2}),\qquad
\Delta_2/D=\Theta(Q^{-1}),
\tag{2.4}
\]

and a uniform fractional perfect matching, but with matching number one.

#### Proof

Let \(Q\) be a prime power, put \(N=Q^2+Q+1\), and take

\[
s=\lceil A\sqrt Q\rceil
\]

disjoint projective planes of order \(Q\).  A hyperedge is the union of
one line chosen from each plane.  It has rank

\[
R=s(Q+1).
\]

A point lies in

\[
D=(Q+1)N^{s-1}
\]

edges.  Two points in different planes have codegree
\((Q+1)^2N^{s-2}\), while two points in the same plane have codegree
\(N^{s-1}\).  Consequently

\[
\frac{\Delta_2}{D}=\frac{Q+1}{N}=\Theta(Q^{-1}).
\]

Regularity supplies the uniform fractional perfect matching.  On the
other hand, any two selected hyperedges meet already inside each projective
plane, because two projective lines intersect.  Hence their matching
number is one.  \(\square\)

This is not a cyclic-wreath counterexample.  It proves that regularity,
fractional feasibility, rank, and maximum codegree alone cannot round
(1.11).  A successful theorem needs additional structure—for example the
indivisible odd-graph factorability and the precise interval clusters—not
merely those numerical parameters.

## 3. Cyclic span truncation

Fix a nonempty coordinate set \(T\).  For one oriented wreath row \(R\),
define

\[
a_R(T)=\#\{j\in\mathbb Z_n:T\subseteq I_R(j,m)\}.
\tag{3.1}
\]

### Lemma 3.1 — exact span-truncation law

For every \(0\le q<m\),

\[
\boxed{
\#\{j:T\subseteq I_R(j,m-q)\}
=(a_R(T)-q)_+.}
\tag{3.2}
\]

#### Proof

List the gaps between consecutive elements of \(T\) in the cyclic order,
and let \(g_i\) be the number of coordinates strictly between the two
consecutive elements.  A cyclic \(s\)-interval
contains \(T\) exactly when its complementary \((n-s)\)-interval lies
inside one of these gaps.  The number of placements is therefore

\[
\sum_i(g_i-(n-s)+1)_+.
\tag{3.3}
\]

For \(s\le m\), one has \(n-s\ge m+1\).  Two gaps cannot both contribute,
because their total length would then be at least \(2(m+1)>n\).  Thus at
\(s=m\), (3.3) equals \((g_{\max}-m)_+=a_R(T)\).  Replacing \(m\) by
\(m-q\) increases the complementary interval length by \(q\), and hence
subtracts exactly \(q\) from the unique possible run.  This proves (3.2),
including the case \(a_R(T)=0\).  \(\square\)

For an exact factor \(F\), put

\[
M_q^F(T)
=\#\{X:T\subseteq L_q^F(X)\}.
\tag{3.4}
\]

Since the middle owners enumerate every middle set once, Lemma 3.1 gives

\[
\boxed{
M_q^F(T)=\sum_{R\in F}(a_R(T)-q)_+,}
\tag{3.5}
\]

\[
\sum_Ra_R(T)=M_0(T)=\binom{n-|T|}{m-|T|},
\tag{3.6}
\]

and

\[
\boxed{0\le M_0(T)-M_q^F(T)\le qB.}
\tag{3.7}
\]

If \(t=|T|\), the proportional rank-\((m-q)\) moment is

\[
\overline M_q(T)
=\lambda_q\binom{n-t}{m-q-t}
=W\frac{(m-q)_t}{(n)_t},
\tag{3.8}
\]

where \((z)_t=z(z-1)\cdots(z-t+1)\).  Therefore

\[
\boxed{
|M_q^F(T)-\overline M_q(T)|
\le qB+
W\frac{(m)_t-(m-q)_t}{(n)_t}.}
\tag{3.9}
\]

Uniformly for \(q\le A\sqrt m\) and \(t=o(\sqrt m)\), the right side is
\(o(W)\).  Indeed,

\[
(m)_t-(m-q)_t\le tq\,m^{t-1},
\]

so the second term is \(O(tqW/m)\), while \(qB=O_A(W/\sqrt m)\).
Thus every fixed-order containment moment is automatically compatible with
uniform balance at the \(o(W)\) scale.

### Pair refinement

For a coordinate pair \(x,y\), let \(d_R(x,y)\in\{1,\ldots,m\}\) be its
short cyclic distance in row \(R\).  Then

\[
a_R(\{x,y\})=m-d_R(x,y).
\]

Every exact factor obeys the pair-distance identity

\[
\sum_{R\in F}d_R(x,y)=\frac{B(m+1)}2.
\tag{3.10}
\]

Indeed, in a row of distance \(d\), exactly \(m-d\) middle intervals
contain both points.  Summing this quantity over the factor counts every
middle set containing \(\{x,y\}\) once, so

\[
\sum_R(m-d_R(x,y))=\binom{n-2}{m-2}=\frac{B(m-1)}2,
\]

which is equivalent to (3.10).

If

\[
Z_q(x,y)=\sum_R(q-a_R(\{x,y\}))_+,
\]

then

\[
M_q^F(x,y)
=B\left(\frac{m-1}{2}-q\right)+Z_q(x,y),
\tag{3.11}
\]

while

\[
\overline M_q(x,y)
=B\left(\frac{m-1}{2}-q+\frac{q(q+1)}{2m}\right).
\tag{3.12}
\]

Consequently

\[
\boxed{
M_q^F(x,y)-\overline M_q(x,y)
=Z_q(x,y)-\frac{Bq(q+1)}{2m},
\qquad 0\le Z_q(x,y)\le qB.}
\tag{3.13}
\]

Even at Gaussian depth, no pair-containment discrepancy of order \(W\)
is forced.

## 4. Fixed-order star Hall cuts

Use the ascending adjacent-deletion-swap formulation.  At stage \(q\),
the two possible rank-\(r\) states of one owner, where \(r=m-q\), have
history-independent intersection

\[
L_{q+1}^F(X).
\tag{4.1}
\]

Earlier toggles can change one endpoint, but not (4.1).

For a fixed \(t\)-set \(T\), put

\[
U_T^{(r)}=\{S\in\tbinom{[n]}r:T\subseteq S\}.
\tag{4.2}
\]

Let \(i_{G_q}(U)\) denote the number of owner edges internal to \(U\).

### Theorem 4.1 — exact history-independent star ledger

For every earlier swap history,

\[
\boxed{
i_{G_q}(U_T^{(r)})=M_{q+1}^F(T)
=\sum_{R\in F}(a_R(T)-q-1)_+.}
\tag{4.3}
\]

If \(L=m-t+1\) and \(q\le m-t\), then

\[
\boxed{
i_{G_q}(U_T^{(r)})
\le
M_0(T)\frac{m-q-t}{m-t+1}.}
\tag{4.4}
\]

#### Proof

Both endpoints of an owner edge lie in \(U_T^{(r)}\) exactly when their
intersection (4.1) contains \(T\).  This proves (4.3) using Lemma 3.1.

One always has \(0\le a_R(T)\le L\).  On \([0,L]\), convexity gives the
chord bound

\[
(a-q-1)_+
\le \frac{L-q-1}{L}a.
\]

Sum this inequality and use (3.6).  \(\square\)

Let

\[
\theta_q=\lambda_q-c_q,
\qquad
\rho_q=N_q\theta_q,
\qquad
\alpha_{q,t}=\frac{|U_T^{(r)}|}{N_q}
=\frac{(r)_t}{(n)_t}.
\tag{4.5}
\]

Among all floor/ceiling-balanced load vectors, the exact maximum possible
mass in \(U\) is

\[
\mathcal C_q(U)
=c_q|U|+\min\{|U|,\rho_q\}.
\tag{4.6}
\]

Thus the internal-capacity Hall constraint associated with this particular
\(U\) is automatically safe whenever
\(i_{G_q}(U)\le\mathcal C_q(U)\).  This does not assert that one orientation
realizes the maximizing load vector simultaneously for all \(U\).

The floor/ceiling margin above proportional mass is

\[
\mathcal C_q(U_T)-\lambda_q|U_T|
=N_q
\begin{cases}
\theta_q(1-\alpha_{q,t}),&\theta_q\le\alpha_{q,t},\\
(1-\theta_q)\alpha_{q,t},&\theta_q\ge\alpha_{q,t}.
\end{cases}
\tag{4.7}
\]

### Theorem 4.2 — fixed-order star internal cuts are exceptional at only
### constantly many depths

Fix \(A>0\) and a positive integer \(t\).  For every exact factor and every
earlier adjacent-swap history, the internal-capacity Hall cuts for the
\(t\)-stars (4.2) are automatically safe at

\[
\boxed{K-O_{A,t}(1)}
\tag{4.8}
\]

of the depths \(q\le K\), simultaneously for every \(t\)-set \(T\).

More precisely, a possibly nonautomatic depth satisfies

\[
\boxed{
\operatorname{dist}(\lambda_q,\mathbb Z)
=O_{A,t}(q/m).}
\tag{4.9}
\]

#### Proof

Subtract the proportional quantity

\[
\lambda_q|U_T|
=W\frac{(m-q)_t}{(n)_t}
\]

from (4.4).  Its positive excess is at most

\[
E_{q,t}
=\frac{W}{(n)_t}
\left[
(m)_t\frac{m-q-t}{m-t+1}-(m-q)_t
\right]_+.
\tag{4.10}
\]

Since the fraction multiplying \((m)_t\) is at most one,

\[
\frac{E_{q,t}}{N_q}
\le
\frac{\lambda_q}{(n)_t}\bigl((m)_t-(m-q)_t\bigr)
=O_{A,t}(q/m).
\tag{4.11}
\]

For fixed \(t\), \(\alpha_{q,t}\) stays uniformly away from zero and one
through the fixed Gaussian window.  Equation (4.7) is therefore at least

\[
\gamma_{A,t}N_q\operatorname{dist}(\lambda_q,\mathbb Z)
\]

for some \(\gamma_{A,t}>0\).  If (4.9) fails with a sufficiently large
constant, the floor margin exceeds (4.11), proving the cut safe.

It remains to count the depths satisfying (4.9).  The exact increment is

\[
\lambda_{q+1}-\lambda_q
=\lambda_q\frac{2(q+1)}{m-q}.
\tag{4.12}
\]

Only \(O_A(1)\) integers lie between \(1\) and
\(\lambda_K+1\le e^{A^2+o(1)}+1\).  Fix one such integer \(k\ge2\).  At every
depth satisfying (4.9) with nearest integer \(k\), the standard fixed-window
estimate

\[
\log\lambda_q=\frac{q(q+1)}m+O_A(m^{-1/2})
\]

gives \(q\ge c_{A,k}\sqrt m\).  If \(q<q'\) are two such depths, monotonicity
and (4.12) give

\[
\lambda_{q'}-\lambda_q
\ge (q'-q)\frac{2(q+1)}m.
\]

On the other hand, (4.9) bounds the same difference by
\(C_{A,t}(q+q')/m\).  Since both \(q,q'\) lie between
\(c_{A,k}\sqrt m\) and \(A\sqrt m+1\), this forces
\(q'-q=O_{A,t}(1)\).  Hence only constantly many depths occur near each
\(k\ge2\).  Near the initial integer one, telescoping the lower bound

\[
\lambda_{j+1}-\lambda_j\ge\frac{2(j+1)}m
\]

gives

\[
\lambda_q-1\ge\frac{q(q+1)}m.
\]

Together with (4.9), this forces \(q=O_{A,t}(1)\).  Summing over the
finitely many crossed integers proves (4.8).  \(\square\)

This theorem removes the internal-capacity half of every fixed-order star
family from all but constantly many threshold depths.  It does not control
the lower-demand constraint for \(U_T\), equivalently the internal
constraint of \(U_T^c\); that complement need not itself be a fixed-order
star.  Nor does it control arbitrary Hall families or make the orientations
at different depths compatible.

### The sharp pair form

For \(T=\{x,y\}\), Theorem 4.1 and (3.10) give

\[
i_{G_q}(U_{xy}^{(r)})
=\sum_{R\in F}(m-q-1-d_R(x,y))_+.
\tag{4.13}
\]

The chord inequality

\[
(m-q-1-d)_+
\le\frac{m-q-2}{m-1}(m-d)
\]

is sharp at \(d=1,m\).  Hence

\[
\boxed{
i_{G_q}(U_{xy}^{(r)})\le\frac B2(m-q-2).}
\tag{4.14}
\]

Writing

\[
\Delta_q=q-1-\frac{q(q+1)}m,
\]

one has the exact comparison

\[
\frac B2(m-q-2)-\lambda_q|U_{xy}^{(r)}|
=\frac B2\Delta_q.
\tag{4.15}
\]

Thus possible pair-star exceptions lie only extremely close to a quota
threshold.  In fact

\[
\operatorname{dist}(\lambda_q,\mathbb Z)
\le
\frac{\lambda_qm(\Delta_q)_+}{(m-q)(m-q-1)}
\tag{4.16}
\]

is necessary for nonautomaticity.  In particular only \(O_A(1)\) pair-star
exceptional depths can occur in the whole fixed window.

### Corollary 4.3 — direct labelled star diagnostic

The next statement no longer assumes the adjacent-swap construction.  For
any \(t\)-set \(T\), put

\[
u_{q,t}=\binom{n-t}{m-q-t}
\]

and

\[
J_{q,t}=
\left[
c_qu_{q,t}+\max\{0,\rho_q-(N_q-u_{q,t})\},
\quad
c_qu_{q,t}+\min\{\rho_q,u_{q,t}\}
\right].
\tag{4.17}
\]

For every exact factor and every balanced nested resolution,

\[
\boxed{
e_q(F,P)\ge
\operatorname{dist}\bigl(M_q^F(T),J_{q,t}\bigr).}
\tag{4.18}
\]

#### Proof

A balanced depth-\(q\) load vector equals \(c_q\) everywhere plus the
indicator of a \(\rho_q\)-element high family.  Its total mass on the
\(u_{q,t}\) targets containing \(T\) lies in (4.17).  Every owner on which
\(P_q\) differs from the canonical target changes the containment indicator
of \(T\) by at most one.  This proves (4.18).  \(\square\)

Equation (4.18) is a literal factor-specific obstruction which can be
inserted directly into the \((\mathrm{CA}_A)\) objective.

## 5. Marginal balance has no hidden integrality obstruction

### Theorem 5.1 — exactly point-regular balanced quotas

At every rank \(r=m-q\), there is a balanced quota vector

\[
b(S)=c+\mathbf1_{\{S\in\mathcal H\}},
\qquad c=\left\lfloor\frac W{\binom nr}\right\rfloor,
\tag{5.1}
\]

whose point loads are exactly

\[
\boxed{
\sum_{S\ni x}b(S)=rB
\qquad(x\in[n]).}
\tag{5.2}
\]

The high family may simultaneously be chosen so that every containment
moment differs from its proportional value by \(o(W)\).

#### Proof

Put \(N=\binom nr\) and \(h=W-cN\).  The required high family has size
\(h\).  Its desired point degree is

\[
d=\frac{rh}{n}
=rB-c\binom{n-1}{r-1}\in\mathbb Z.
\tag{5.3}
\]

Among all \(h\)-element \(r\)-uniform families, minimize the squared
point-degree deviation.  If \(d_x>d_y+1\), some member \(C\) contains
\(x\) but not \(y\) while

\[
C-x+y\notin\mathcal H.
\]

Otherwise the swap map would inject every \(x\bar y\)-member into a
distinct \(\bar x y\)-member, contradicting \(d_x>d_y\).  Performing this
swap lowers the squared deviation.  At a minimum all point degrees differ
by at most one; their average is the integer \(d\), so they all equal
\(d\).  Equation (5.2) follows from (5.3).

For the last assertion, choose the \(h\) members uniformly at random.
For every \(T\subseteq[n]\), the number of selected members containing
\(T\) is hypergeometric.  The bounded-difference inequality with threshold
\(W^{2/3}\), followed by a union bound over at most \(K2^n\) pairs
\((q,T)\), shows that one may choose the high families so that all these
counts differ from their expectations by at most \(W^{2/3}\).

Their point degrees are then within \(W^{2/3}\) of \(d\).  Repeatedly use
the degree-equalizing swap above between a largest and a smallest degree.
Each such swap decreases the \(\ell^1\) point-degree deviation from \(d\)
by two.  Hence at most \(nW^{2/3}/2=o(W)\) swaps are needed, and every containment count
changes by at most the number of swaps.  Thus all moments retain \(o(W)\)
error while the point degrees become exact.  \(\square\)

Theorem 5.1 chooses the ranks separately.  It does not assert that those
specific quota vectors admit one common nested resolution.

### Theorem 5.2 — common nesting and exact deletion homomesy on prime
### dimensions

Suppose \(n=2m+1\) is prime and \(K\le m-1\).  There is an integral
balanced nested resolution through depth \(K\) such that, if

\[
d_t(X)=P_{t-1}(X)\setminus P_t(X),
\]

then

\[
\boxed{
\#\{X:d_t(X)=x\}=B
\qquad(t\le K,\ x\in[n]).}
\tag{5.4}
\]

#### Proof

Let \(\sigma\) be an \(n\)-cycle on the coordinates.  Since \(n\) is
prime, every nonempty proper subset has a free
\(\langle\sigma\rangle\)-orbit.

Take the usual node-split lower-bounded inclusion-flow network on the ranks

\[
m,m-1,\ldots,m-K.
\]

A rank-\(r\) node has throughput bounds

\[
\left\lfloor\frac W{\binom nr}\right\rfloor
\le f(S)\le
\left\lceil\frac W{\binom nr}\right\rceil,
\tag{5.5}
\]

and every middle node has throughput one.  There is an invariant real flow:
put

\[
\lambda_r=\frac W{\binom nr}
\]

through every rank-\(r\) node and \(\lambda_r/r\) through every deletion
arc.  Conservation is the identity

\[
(n-r+1)\frac{\lambda_r}{r}=\lambda_{r-1}.
\tag{5.6}
\]

Quotient the network by \(\langle\sigma\rangle\).  Every subset-node orbit
and every internal inclusion-arc orbit is free.  The global source and sink
are fixed; divide their physical balance equations by \(n\), so the quotient
source has supply \(B=W/n\) and the quotient sink has demand \(B\).
Every source-to-top orbit becomes one ordinary quotient edge, and each
top-orbit node has throughput one.  An internal arc orbit contains at most
one arc leaving a fixed representative, for otherwise a nonidentity power
of \(\sigma\) would fix its tail.  The quotient is therefore an ordinary
directed multigraph, with parallel arcs allowed.  The invariant real flow
descends to a feasible quotient flow with integral lower and upper bounds.
Network integrality gives an integral quotient flow.

Decompose it into \(B\) unit paths, one from every middle-set orbit.  A
quotient path lifts uniquely after its initial representative is fixed,
because each quotient arc orbit has a unique arc leaving that
representative.  Translating by \(\sigma^j\) produces the \(n\) paths in
the whole middle orbit.  Taking all translates also makes every physical
node in an orbit receive exactly the integral multiplicity of its quotient
node.  Lifting every quotient path therefore yields one balanced nested
flag for every middle owner and satisfies

\[
P_q(\sigma^jX)=\sigma^jP_q(X).
\]

Therefore

\[
d_t(\sigma^jX)=\sigma^jd_t(X).
\]

On each middle orbit the deletion label runs once through all \(n\)
coordinates.  There are \(B\) middle orbits, proving (5.4).  \(\square\)

This theorem is not an alignment theorem: the resolution has not been
coupled to an exact wreath factor.  It proves that common integral nesting
and the exact deletion-column margins required by low-cost alignment are
compatible.

## 6. A literal homogeneous cyclic no-go

The following construction explains why the indivisible \(\tau=1\) factor and
its order-one floor freedom cannot be replaced by homogeneous averaging.

Fix two coordinates \(x,y\).  Take all oriented cyclic orders with \(x\)
in position zero, \(y\) in one of the four positions

\[
1,-1,m,-m,
\]

and the remaining coordinates arbitrary.  Retain multiplicity when two
orientations give the same unoriented wreath.  This is an integral multiset
\(\mathcal C\) of

\[
4(n-2)!
\tag{6.1}
\]

literal cyclic packets.

### Theorem 6.1 — exact homogeneous cover with a Hall failure

Every middle \(m\)-set occurs in \(\mathcal C\) exactly

\[
\boxed{
\tau=2(m-1)!(m+1)!}
\tag{6.2}
\]

times.  Nevertheless, for every \(m\ge7\) and every

\[
2\le q\le m-3,
\]

the depth-\(q\) pair-star Hall cut for \(\{x,y\}\) fails in the associated
\(\tau\)-fold sibling graph.

#### Proof

If the short cyclic distance of \(x,y\) is \(d\), one cyclic row has

\[
m-d,\qquad 2d,\qquad m+1-d
\tag{6.3}
\]

middle windows containing respectively both, exactly one, and neither of
\(x,y\).  The stabilizer of \(\{x,y\}\) is transitive on the middle sets
in each of these three classes.  The construction uses distances \(1\) and
\(m\) equally.  Dividing the three averaged incidence totals by the three
class sizes gives the same degree

\[
2(m-1)!(m+1)!,
\]

proving (6.2).  Equivalently, (6.2) follows from
\(4(n-2)!/B\) after class-regularity is established.

Half of the rows have distance one and half distance \(m\).  Thus equality
holds in (4.14), and the internal pair-star mass is

\[
i_q(U)=\frac{\tau B}{2}(m-q-2).
\]

Its excess above proportional mass is

\[
i_q(U)-\tau\lambda_q|U|=\frac{\tau B}{2}\Delta_q.
\tag{6.4}
\]

For \(\tau W\) owners, put
\(\vartheta=\{\tau\lambda_q\}\).  The exact floor/ceiling Hall cap minus
\(\tau\lambda_q|U|\) equals

\[
\vartheta(N_q-|U|)
\quad\text{if }\vartheta N_q\le |U|,
\]

and

\[
(1-\vartheta)|U|
\quad\text{otherwise}.
\]

It is therefore at most \(|U|\).  Moreover

\[
\frac{|U|}{\tau B/2}\le\frac m\tau.
\tag{6.5}
\]

On \(2\le q\le m-3\), concavity gives

\[
\Delta_q\ge1-\frac6m.
\]

Equations (6.2), (6.4), and (6.5) show that the excess is larger than the
entire floor/ceiling margin for \(m\ge7\).  Hence the Hall cut fails.
\(\square\)

This is not a single exact factor and does not refute \((\mathrm{CA}_A)\).
It is a literal integral counterexample to the inference

\[
\text{cyclic packets + homogeneous exact middle ownership
      + its middle-containment and first-moment ledgers}
\Longrightarrow\text{balanced Hall feasibility}.
\]

The construction is not asserted to be a convex combination of
\(\tau=1\) exact factors, and its lower-rank loads are deliberately
unbalanced.  It shows that any averaging argument which discards provenance
and retains only these homogeneous middle and cyclic first-moment statistics
loses the decisive order-one floor structure.

## 7. Exact residual completion and the remaining lemma

Let \(F\) be one oriented exact factor and let
\(\Gamma_q(X)=L_q^F(X)\) be its canonical flags.  Freeze the canonical
flags of all owners outside a family

\[
E\subseteq\binom{[n]}m.
\]

For balanced quotas \(b_q\), define the residual loads

\[
r_q(S)=b_q(S)-
\#\{X\notin E:\Gamma_q(X)=S\}.
\tag{7.1}
\]

At depth zero use \(b_0(X)=1\), so

\[
r_0(X)=\mathbf1_{\{X\in E\}}.
\tag{7.1a}
\]

### Theorem 7.1 — exact residual inclusion-Hall criterion

The frozen canonical flags extend to one common balanced nested resolution
for the owners in \(E\) if and only if

\[
r_q(S)\ge0,\qquad \sum_Sr_q(S)=|E|
\tag{7.2}
\]

at every depth and, for every \(q\ge1\) and every child family
\(\mathcal A\subseteq\binom{[n]}{m-q}\),

\[
\boxed{
\sum_{S\in\mathcal A}r_q(S)
\le
\sum_{\substack{R\in\binom{[n]}{m-q+1}\\
                 \exists S\in\mathcal A:\ S\subset R}}
r_{q-1}(R).}
\tag{7.3}
\]

#### Proof

Between two adjacent ranks, clone every parent \(R\) exactly
\(r_{q-1}(R)\) times and every child \(S\) exactly \(r_q(S)\) times.
Hall's theorem for the inclusion bipartite graph is exactly (7.3), with
equal total mass supplied by (7.2).  Thus there is an integral matching at
every adjacent pair of ranks.  At each intermediate node, biject its
incoming and outgoing copies; the common multiplicity \(r_q(S)\) makes
this possible.  These bijections concatenate the adjacent matchings into
paths.  Equation (7.1a) then gives exactly one path from each root in
\(E\).  Necessity is immediate from any such path family.  \(\square\)

The nonnegativity in (7.2) is exactly the survival-packet condition: no
target may be owned by more frozen canonical paths than its chosen quota.
Because \(c_q=O_A(1)\), these target packets have bounded rank on a fixed
window.  The new and genuinely collective condition is (7.3); its witness
families may be arbitrarily large.

### Corollary 7.2 — quantitative implication to \((\mathrm{CA}_A)\)

If, for every fixed \(A\), there are \(F,b,E\) satisfying (7.2)--(7.3) and

\[
\boxed{
|E|\sum_{q=1}^{K}\frac1{c_q}=o(W),}
\tag{7.4}
\]

then \((\mathrm{CA}_A)\) holds.  In particular, the simpler bound

\[
|E|=o_A(W/\sqrt m)
\tag{7.5}
\]

is sufficient.

#### Proof

Use Theorem 7.1 and leave every owner outside \(E\) canonical.  At each
depth at most \(|E|\) owners mismatch, so

\[
\sum_{q\le K}\frac{e_q(F,P)}{c_q}
\le |E|\sum_{q\le K}\frac1{c_q}=o(W).
\]

Since \(K=O_A(\sqrt m)\) and \(c_q\ge1\), (7.5) implies (7.4).
\(\square\)

Corollary 7.2 is a proved lemma which composes quantitatively with the
audited fixed-window diagonalization and therefore with the
constant-one contiguous-OR theorem.  Its antecedent is the remaining
unproved cyclic alignment lemma, not a relabelling of rankwise overload.

### Minimal unproved lemma — residual cyclic-packet completion

For every fixed \(A>0\) and all sufficiently large \(m\), there exist an
exact oriented wreath factor \(F\), balanced quota vectors \(b_q\) for
\(1\le q\le K\), and a family

\[
E\subseteq\binom{[n]}m,
\qquad |E|=o_A(W/\sqrt m),
\tag{7.6}
\]

such that, with \(r_q\) defined by (7.1) and (7.1a), every frozen
canonical load is at most its quota, (7.2) holds, and every residual
inclusion cut (7.3) holds simultaneously.

This lemma is **unproved**.  Corollary 7.2 shows that it is sufficient for
\((\mathrm{CA}_A)\).  Theorem 7.1 shows that, once \(F,b,E\) are fixed,
its cut conditions are also necessary for completing precisely those
frozen owners; hence there is no further hidden integrality or
concatenation condition inside this residual formulation.

## 8. Adversarial audit

1. **No proof of \((\mathrm{CA}_A)\).**  The report proves the exact
   residual gate and several universal star estimates.  It does not produce
   the exceptional family \(E\) satisfying all cuts (7.3).

2. **Zero-error versus small error.**  Theorem 1.1 is an exact stronger
   subproblem.  Failure of its rounding would not by itself disprove
   \((\mathrm{CA}_A)\).

3. **Fixed-order scope.**  Theorem 4.2 treats the internal-capacity
   constraint for every star generated by a fixed-size coordinate set,
   uniformly over that set.  It does not treat the complementary
   lower-demand constraint, arbitrary target families, or stars whose order
   grows with \(m\).

4. **One cut versus a common orientation.**  Saying a star cut is
   automatically safe means it cannot individually violate the
   internal-capacity inequality after optimizing placement of the high
   quotas.  It does not certify the lower-demand/boundary inequality, nor
   choose one high-quota family or one orientation satisfying all cuts
   simultaneously.

5. **Threshold depths.**  The \(O_{A,t}(1)\) exceptional depths cannot be
   discarded: capacities are bounded, so even one such depth can carry
   linear labelled cost.

6. **Prime equivariance.**  Theorem 5.2 constructs a balanced resolution,
   not an aligned factor-resolution pair.  It is evidence against a
   marginal integrality obstruction only.  The pseudorandom fixed-order
   moments in Theorem 5.1 were obtained for separately chosen rankwise
   quotas and are not asserted for the same prime-equivariant resolution.

7. **Homogeneous counterexample.**  Theorem 6.1 is an integral
   \(\tau\)-fold cover, not a \(\tau=1\) exact factor.  It closes homogeneous
   packet-ledger arguments, but neither refutes the labelled
   theorem nor the OR conjecture.

8. **Generic matching counterexample.**  Proposition 2.2 has the same
   rank/codegree scales but not the cyclic descendant structure or known
   exact middle factorability.  Its purpose is only to rule out a theorem
   based on those numerical parameters alone.

9. **Moment compatibility is not histogram closeness.**  The
   \(o(W)\) error in each containment moment may occur for exponentially
   many moments.  No \(\ell^1\) balancing conclusion is inferred.

10. **Minimal surviving lemma.**  A completing proof must exploit one
    indivisible exact factor to hit the bounded survival packets while also
    preserving every large residual inclusion cut (7.3), with
    \(|E|=o(W/\sqrt m)\), or must use a resynchronizing owner flow of still
    smaller weighted area.  Point margins, fixed-order stars, homogeneous
    averaging, and generic high-uniformity matching have now been removed
    as possible substitutes for that collective theorem.
