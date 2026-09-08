# Positive-winding ST susceptibility: exact terminal-layer transfer and the surviving renewal obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
 \qquad G=2H-1,
\]

where (A>0) is fixed.  All asymptotic statements below are for fixed
(A) and (r\to\infty).  Let (E_H^+) be the set of genuine
positive-winding PBBS return starts of gap at most (G), and define

\[
 R_H^+=|E_H^+|,
 \qquad
 \mathcal C_H^{++}
 =\sum_{u=1}^{H+1}|E_H^+\cap\tau^{-u}E_H^+|.
 \tag{0.1}
\]

This note does not prove that
(\mathcal C_H^{++}/R_H^+) is bounded or divergent.  It gives an exact
winding-resolved transfer theorem and identifies the smallest surviving
positive-winding process.

1.  For a first-pruned core (F), fixing the terminal free occupancy
    (z) fixes not only the first outer return time
    (B_{2z+2}(F)), but also its winding.  Thus there is a well-defined
    integer

    \[
      \omega_z(F)\ge0                                      \tag{0.2}
    \]

    shared by every lift in that exact terminal layer.  This is a genuine
    fibre theorem, not a marginal assertion.

2.  The full fixed-winding one- and two-point statistics have exact
    formulas in terms of an integral transportation matrix between two
    weak-composition coordinates.  If (F) has rank (d), (k) peaks,
    and

    \[
      M=r+d-k,qquad y=r-d-k,qquad p=2d+1,
    \]

    then the terminal-(z) layer has size

    \[
      K_z(d,k)=\binom{M-z-1}{2d-1}.              \tag{0.3}
    \]

    For two phases, the matrix entry is either zero, a one-coordinate
    layer (K_z), or the exact two-coordinate coefficient

    \[
      \binom{M-z-b-2}{2d-2}.                    \tag{0.4}
    \]

    Here \(b=z'\) after both phases are expressed in their free
    weak-composition coordinates.  Formula (0.4) retains the actual core
    itinerary and, in particular, whether the two tests address the same
    free coordinate.

3.  On the Pascal saddle, the terminal-zero winding classes inherit the
    same sharp constants as the all-winding two-point pullback.  For every
    two sets of windings (U,V\subseteq\mathbb Z_{\ge0}), their reduced
    weighted statistics (S_U^{(0)},K_{U,V}^{(0)}) and their parent
    terminal-zero statistics (R_U^{(0)},C_{U,V}^{(0)}) satisfy

    \[
    \left({3\over4}-o(1)\right)S_U^{(0)}
       \le R_U^{(0)}\le S_U^{(0)},                \tag{0.5}
    \]

    \[
    \left({1\over2}-o(1)\right)K_{U,V}^{(0)}
       \le C_{U,V}^{(0)}\le K_{U,V}^{(0)},        \tag{0.6}
    \]

    up to additive (o_A(B_r/H)) long-cycle and saddle errors.  Hence, at
    critical terminal-zero mass,

    \[
    \boxed{
    \left({1\over2}-o(1)\right){K_{U,U}^{(0)}\over S_U^{(0)}}
       \le {C_{U,U}^{(0)}\over R_U^{(0)}}
       \le
    \left({4\over3}+o(1)\right){K_{U,U}^{(0)}\over S_U^{(0)}}.}
                                                               \tag{0.7}
    \]

    Taking (U=\{1,2,\ldots\}) gives the exact positive-winding
    terminal-zero susceptibility.  Taking (U=\{0\}),
    (V=\{1,2,\ldots\}) gives the exact zero--positive cross term.

4.  The same deterministic lower constant is unavailable for positive
    terminal layers (z\ge1).  Their total fibre density is at most

    \[
      {P_r(F)-K_0(d,k)\over P_r(F)}
      ={y\over M}={1\over4}+o(1)                 \tag{0.8}
    \]

    on the saddle.  Two such transported subsets can therefore have zero
    intersection without contradicting their sizes.  The explicit matrix
    (0.4), rather than a one-point Pascal density, is indispensable.

5.  At the parent level, for duration (s) define

    \[
      X_i^{(s)}=\sum_{j=0}^{s-1}d(\tau^{i+j}D)
                    -\delta(\tau^{i+s}D).         \tag{0.9}
    \]

    Fixed-((s,w)) starts are first-passage-filtered visits of the cyclic
    walk (X_i^{(s)}) to the level (wN), and

    \[
      X_{i+1}^{(s)}-X_i^{(s)}
       =d(\phi\tau^{i+s}D)-d(\tau^iD).            \tag{0.10}
    \]

    This gives an exact renewal representation of every fixed-winding and
    mixed-winding pair count.  The missing asymptotic is the short-lag
    local time of these actual level sets.

6.  This failure is sharp for every scalar or phasewise argument already
    on the table.  The audited coverage-complete formal winding-one
    construction has (\Theta_A(B_r/H)) distinguished starts separated
    by (\Theta(H)), and its distinguished two-point ratio is (O_A(1))
    (indeed it can be zero for the strict (H+1) window).  It has exact
    ledgers, firstness, winding one, long cycles, full coordinate coverage,
    voltage and area closure, and literal phasewise Dyck realizations.  It
    fails only the simultaneous identity (D_{i+1}=\tau D_i).

Consequently the exact positive-winding decision is

\[
 \boxed{
 \text{evaluate the Pascal-weighted, winding-labelled renewal matrix
 of actual reduced predecessor passages.}}       \tag{0.11}
\]

A bounded value in (0.7), together with critical mass, refutes
((ST_A)).  Divergence is necessary for ((ST_A)), but is not proved by
the terminal-layer margins, winding budgets, or scalar renewal identities.

## 1. Fixed-duration and fixed-winding parent renewal

Along one parent quotient cycle write

\[
 D_i=\tau^iD,qquad
 a_i=\delta(D_i),qquad
 c_i=d(D_i),qquad
 \widehat c_i=d(\phi D_i).                       \tag{1.1}
\]

The exact two-step block identity is

\[
 a_{i+1}-a_i=c_i-\widehat c_i.                   \tag{1.2}
\]

For (s\ge1), put

\[
 X_i^{(s)}=\sum_{j=0}^{s-1}c_{i+j}-a_{i+s}.      \tag{1.3}
\]

### Lemma 1.1 (complete first-return indicator)

For (1\le s\le H-1) and (w\ge0), (D_i) starts a genuine return of
step-two duration (s) and winding (w) if and only if

\[
 X_i^{(s)}=wN                                     \tag{1.4}
\]

and

\[
 X_i^{(q)}\notin N\mathbb Z
 \qquad(1\le q<s).                               \tag{1.5}
\]

#### Proof

The endpoint return ledger is exactly (1.4).  At an earlier odd endpoint
the signed displacement is

\[
 a_{i+q}-\sum_{j=0}^{q-1}c_{i+j}=-X_i^{(q)}.
\]

Thus (1.5) is precisely the proper-prefix exclusion.  The audited
sub-circumference parity theorem says every same-label return gap is odd,
so no additional even-gap case is missing. \(\square\)

Let (I_{s,w}(i)) denote this indicator.

### Theorem 1.2 (duration--winding transfer cocycle)

For all (t\ge1),

\[
 \boxed{
 X_{i+t}^{(s)}-X_i^{(s)}
 =\sum_{u=0}^{t-1}\widehat c_{i+s+u}
  -\sum_{u=0}^{t-1}c_{i+u}.}                    \tag{1.6}
\]

More generally, if (s'\ge s), then

\[
\boxed{
\begin{aligned}
 X_{i+t}^{(s')}-X_i^{(s)}
 ={}&\sum_{u=0}^{t-1}
       (\widehat c_{i+s+u}-c_{i+u})\\
    &+\sum_{v=s}^{s'-1}\widehat c_{i+t+v}.
\end{aligned}}                                   \tag{1.7}
\]

If (s'<s), the last line is replaced by

\[
 -\sum_{v=s'}^{s-1}\widehat c_{i+t+v}.           \tag{1.8}
\]

Consequently, a pair of starts of types ((s,w)) and ((s',w')) at
phases (i,i+t) must make the right side of (1.7) or (1.8) equal

\[
 (w'-w)N.                                         \tag{1.9}
\]

#### Proof

From (1.2),

\[
\begin{aligned}
 X_{i+1}^{(s)}-X_i^{(s)}
 &=c_{i+s}-c_i-(a_{i+s+1}-a_{i+s})\\
 &=\widehat c_{i+s}-c_i.
\end{aligned}
\]

Summing proves (1.6).  Increasing the duration by one gives

\[
 X_j^{(q+1)}-X_j^{(q)}
 =c_{j+q}-(a_{j+q+1}-a_{j+q})
 =\widehat c_{j+q}.
\]

Telescope this identity upward or downward in (q), then use (1.6).
Equation (1.9) follows from (1.4). \(\square\)

For fixed (s), (1.6) says that (X_i^{(s)}) is a cyclic integral walk
with increments

\[
 g_i^{(s)}=\widehat c_{i+s}-c_i.                 \tag{1.10}
\]

The sum of the increments around a quotient cycle is zero because both
(c) and (\widehat c) have the same cyclic total.

### Corollary 1.3 (exact renewal formula)

On a quotient cycle (C), list the phases at which (I_{s,w}=1) as

\[
 \rho_1<\rho_2<\cdots<\rho_m
\]

cyclically, and put (q_j=\rho_{j+1}-\rho_j), with the final gap read
cyclically.  Then

\[
 \boxed{
 \sum_{t=1}^{H+1}|E_{s,w}(C)\cap\tau^{-t}E_{s,w}(C)|
 =\sum_{j=1}^{m}
   \#\left\{\ell\ge1:
      \sum_{v=0}^{\ell-1}q_{j+v}\le H+1\right\}.} \tag{1.11}
\]

Thus the fixed-type susceptibility is exactly the Palm mean number of
further filtered visits to the level (wN) in the next (H+1) phases.

#### Proof

Each ordered pair of starts in the indicated window is uniquely the pair
((\rho_j,\rho_{j+\ell})), and its displacement is the displayed sum of
successive renewal gaps. \(\square\)

Equation (1.11) is the desired renewal object.  It is not evaluated by the
one-point distributions of (c_i) and (\widehat c_i).  The proper-prefix
filter (1.5) is part of the renewal set and cannot be deleted.

## 2. Exact winding constancy on one terminal layer

Fix a nonempty first-pruned core

\[
 F\in\mathcal D_d,qquad k=\operatorname {pk}(F),
\]

and let

\[
 y=r-d-k,qquad p=2d+1,qquad M=y+p-1=r+d-k.      \tag{2.1}
\]

After subtracting the compulsory leaf at every old leaf, the inverse
fibre is the weak-composition simplex

\[
 \Omega_r(F)=\left\{(q_0,\ldots,q_{p-1})\in
 \mathbb Z_{\ge0}^{p}:\sum_jq_j=y\right\}.       \tag{2.2}
\]

Choose the indexing so that (q_0) is the terminal free root slot.  Put

\[
 \Omega_r(F;z)=\{q\in\Omega_r(F):q_0=z\}.        \tag{2.3}
\]

Stars and bars gives

\[
 P_r(F)=|\Omega_r(F)|=\binom M{2d},               \tag{2.4}
\]

\[
 K_z(d,k)=|\Omega_r(F;z)|
 =\binom{M-z-1}{2d-1}.                            \tag{2.5}
\]

Let

\[
 0<B_1(F)<B_2(F)<\cdots
\]

be the positive selection times of the immediate predecessor of the
time-zero selected equality particle in the reduced PBBS.

### Theorem 2.1 (terminal-layer winding invariance)

Suppose

\[
 B_{2z+2}(F)\le G<N.                              \tag{2.6}
\]

Every parent (D\in\Omega_r(F;z)) has the same first return gap

\[
 g=B_{2z+2}(F),                                   \tag{2.7}
\]

and the same winding.  Denote that winding by

\[
 \boxed{\omega_z(F).}                            \tag{2.8}
\]

The outer rank \(r\), and hence \(N\), is fixed throughout; it is
suppressed from the notation \(\omega_z(F)\).  No invariance across
different outer ranks is asserted.

#### Proof

The exact adjacent-particle passage kernel gives (2.7) for every lift in
the layer.  It remains to prove constancy of the integer winding.

Use persistent equality-particle labels in their cyclic identity order.
Peak deletion fixes the entire selected-particle itinerary
\(\kappa_0,\ldots,\kappa_g\); it does not depend on the free gap lengths.
The terminal value \(z\) fixes both the initial spacing of the distinguished
particle and its predecessor and the occurrence \(B_{2z+2}\) at which
that predecessor closes the passage.

The normalized root cut therefore follows the same cyclic sequence of
persistent particle identities for every lift in (2.3).  Changing the
nonterminal free occupancies changes only the positive lengths of the
arcs between consecutive particles.  It neither changes their cyclic
order nor lets the moving cut cross a particle at a different time.
Hence all lifts in one connected fixed-\(z\) layer give
orientation-preservingly homotopic closed cut trajectories on the physical
circle.  Their integer degree is the same.  By the exact skew-product
return ledger, this degree is precisely the winding in (1.4).

For an independent arithmetic audit of this topological argument, connect
two lifts by one unit transfer between nonterminal slots.  The transfer
increases one persistent particle gap by two and decreases another by two.
At every fixed PBBS time it shifts one interval of persistent particle
positions by exactly two.  Every oriented cut-to-selected-particle arc
therefore changes by \(0\) or \(\pm2\).  This statement uses persistent
particle arcs, so a tie between first maxima cannot create a root-cut
jump: the selected particle identity is already fixed by \(\kappa_t\).
Positivity of all particle gaps prevents a modular endpoint crossing.

In particular, at each even phase, both one-step first-maximum positions
change by at most two.  Since

\[
 d(D)=N-\delta(D)-\delta(\phi D),                 \tag{2.9}
\]

the two-step deficit changes by at most four, while the terminal
first-maximum position changes by at most two.  Put
(s=(g-1)/2\le H-1).  The two endpoint ledgers therefore differ in
absolute value by at most

\[
 4s+2\le4H-2<N                                   \tag{2.10}
\]

for all sufficiently large (r).  Both ledgers are integer multiples of
(N), because both lifts return at time (g).  Their difference is hence
zero.  The fixed-\(z\) weak-composition layer is connected by these unit
transfers, which proves constancy throughout (2.3).
\(\square\)

The qualification “fixed (z)” is essential.  Changing (z) changes
the initial adjacent-particle spacing, the occurrence index (2z+2), and
usually the return time itself.

### Corollary 2.2 (exact winding-resolved one-point formula)

Define

\[
 a_H(F)=\max\{z\ge0:B_{2z+2}(F)\le G\},          \tag{2.11}
\]

with value (-1) if the set is empty, and truncate at (y).  Before
deleting short parent cycles, the number of winding-(w) starts is

\[
 \boxed{
 \widetilde R_{H,w}
 =\sum_F\sum_{0\le z\le\min(y,a_H(F))}
   K_z(d,k)\mathbf1_{\{\omega_z(F)=w\}}.}        \tag{2.12}
\]

In particular

\[
 \widetilde R_H^+=\sum_{w\ge1}\widetilde R_{H,w}. \tag{2.13}
\]

#### Proof

The terminal layers partition every inverse fibre.  The passage kernel
and Theorem 2.1 give exactly the indicator and winding in (2.12).
\(\square\)

## 3. The exact two-phase terminal transportation matrix

Peak deletion commutes with (\tau).  For (u\ge1), let

\[
 \Sigma_F^{(u)}:\Omega_r(F)\longrightarrow
 \Omega_r(\tau^uF)                               \tag{3.1}
\]

be the actual parent-fibre transport.  Define

\[
 J_u(F;z,z')=\left|
 \Omega_r(F;z)\cap
 (\Sigma_F^{(u)})^{-1}\Omega_r(\tau^uF;z')
 \right|.                                        \tag{3.2}
\]

The particle-gap transport gives a core-determined coordinate
\(\eta_u\in\{0,\ldots,p-1\}\) such that, after subtracting the compulsory
leaf occupancies at both phases, the phase-\(u\) terminal coordinate is

\[
 \boxed{z_u=q_{\eta_u}.}                         \tag{3.3}
\]

Indeed, before compulsory occupancies are subtracted, the physical gap
formula contains the core-determined shift

\[
 {C_{j_u}(2u)-C_{j_u^-}(2u)\over2}.              \tag{3.4}
\]

That shift is exactly the change in the compulsory part of the addressed
gap.  It vanishes from the free coordinate.  There is also a direct
surjectivity audit: if \(z_u=q_{\eta_u}+\Delta\) on the full free simplex,
then testing \(q_{\eta_u}=0\) forces \(\Delta\ge0\), while testing
\(q_{\eta_u}=y\) forces \(\Delta\le0\); hence \(\Delta=0\).

### Theorem 3.1 (exact layer transfer entry)

With the binomial-zero convention,

\[
 \boxed{
 J_u(F;z,z')=
 \begin{cases}
 \displaystyle\binom{M-z-z'-2}{2d-2},
      &\eta_u\ne0,\\[3mm]
 K_z(d,k),&\eta_u=0,\ z'=z,\\
 0,&\eta_u=0,\ z'\ne z.
 \end{cases}}                                    \tag{3.6}
\]

Moreover (J_u(F;z,z')) is an integral transportation matrix:

\[
 \sum_{z'}J_u(F;z,z')=K_z(d,k),
 \qquad
 \sum_zJ_u(F;z,z')=K_{z'}(d,k).                 \tag{3.7}
\]

#### Proof

The phase-zero condition is (q_0=z).  By (3.3), the phase-(u)
condition is \(q_{\eta_u}=z'\).  If the coordinates differ, fixing both
leaves \(y-z-z'\) free units in \(p-2\) boxes, giving

\[
 \binom{y-z-z'+p-3}{p-3}
 =\binom{M-z-z'-2}{2d-2}.
\]

If the coordinates agree, the two equations are either the same or
inconsistent.  This proves (3.6).  Finally, the terminal layers partition
the source and target fibres, and (\Sigma_F^{(u)}) is a bijection.
Summing rows or columns proves (3.7). \(\square\)

At the Pascal saddle

\[
 d={r\over2}+O(\sqrt{r\log r}),
 \qquad
 k={r\over6}+O(\sqrt{r\log r}),                 \tag{3.8}
\]

one has, uniformly for (z=O(\log r)),

\[
 {K_z(d,k)\over P_r(F)}
 ={2d\over M}
  \prod_{j=0}^{z-1}{M-2d-j\over M-1-j}
 =\left({3\over4}+o(1)\right)4^{-z}.            \tag{3.9}
\]

When the two coordinates in (3.6) differ and
\(z+z'=O(\log r)\),

\[
 {J_u(F;z,z')\over P_r(F)}
 =\left({9\over16}+o(1)\right)4^{-(z+z')}.       \tag{3.10}
\]

When they agree consistently, the ratio is (3.9).  These are coefficient
asymptotics of the exact matrix, not an independence assumption.

### Theorem 3.2 (exact winding-resolved two-point formula)

Before short-parent-cycle deletion,

\[
\boxed{
\begin{aligned}
 \widetilde{\mathcal C}_{H}^{w,w'}
 ={}&\sum_{u=1}^{H+1}\sum_F
 \sum_{\substack{0\le z\le\min(y,a_H(F))\\
                   0\le z'\le\min(y,a_H(\tau^uF))}}
 J_u(F;z,z')\\
 &\qquad\qquad\times
 \mathbf1_{\{\omega_z(F)=w\}}
 \mathbf1_{\{\omega_{z'}(\tau^uF)=w'\}}.
\end{aligned}}                                    \tag{3.11}
\]

Thus

\[
 \widetilde{\mathcal C}_H^{++}
 =\sum_{w,w'\ge1}\widetilde{\mathcal C}_H^{w,w'}, \tag{3.12}
\]

and the two ordered zero--positive cross terms are obtained by taking
((w,w')=(0,>0)) and ((>0,0)).

#### Proof

For a parent counted at phases (0,u), its initial and transported
terminal occupancies are unique.  The two passage cutoffs give the two
ranges of (z,z'); Theorem 2.1 gives the winding labels; and (3.2) counts
the common parents.  Summing the disjoint cases proves (3.11).
\(\square\)

Equations (2.12) and (3.11) are the requested genuine transfer matrix.
Every unresolved chronological datum is visible: the predecessor local
times \(a_H\), winding labels \(\omega_z\), and addressed coordinates
\(\eta_u\).

## 4. Terminal zero transmits every winding class with fixed constants

For (U\subseteq\mathbb Z_{\ge0}), define the reduced terminal-zero
predicate

\[
 A_U^{(0)}(F)
 =\mathbf1_{\{B_2(F)\le G,\ \omega_0(F)\in U\}}. \tag{4.1}
\]

Put

\[
 S_U^{(0)}=\sum_FP_r(F)A_U^{(0)}(F),             \tag{4.2}
\]

\[
 K_{U,V}^{(0)}
 =\sum_{u=1}^{H+1}\sum_F
 P_r(F)A_U^{(0)}(F)A_V^{(0)}(\tau^uF).           \tag{4.3}
\]

Let (R_U^{(0)}) and (C_{U,V}^{(0)}) be the corresponding parent
statistics with the terminal occupancy fixed to zero at every displayed
phase.

### Theorem 4.1 (winding-labelled terminal-zero pullback)

After restricting to the saddle tube (3.8),

\[
 \left({3\over4}-o(1)\right)S_U^{(0)}
 \le R_U^{(0)}\le S_U^{(0)},                     \tag{4.4}
\]

and

\[
 \left({1\over2}-o(1)\right)K_{U,V}^{(0)}
 \le C_{U,V}^{(0)}\le K_{U,V}^{(0)}.             \tag{4.5}
\]

These inequalities hold simultaneously for arbitrary (U,V), including
fixed singleton windings.

#### Proof

One active terminal-zero core phase contributes exactly (K_0(d,k))
parents.  Since

\[
 {K_0(d,k)\over P_r(F)}={2d\over M}
 ={3\over4}+o(1)                                  \tag{4.6}
\]

uniformly in the saddle, summation proves (4.4).

For a reduced phase pair, the two terminal-zero parent subsets both have
size (K_0(d,k)) inside one fibre of size (P_r(F)).  Their actual
transport can be arbitrary, but inclusion--exclusion gives

\[
 |A\cap A'|\ge2K_0(d,k)-P_r(F)
 =\left({1\over2}-o(1)\right)P_r(F).             \tag{4.7}
\]

The upper bound is (P_r(F)).  The winding predicates are core-layer
labels by Theorem 2.1, so they are constant on each of the two subsets and
do not alter (4.7).  Sum over the reduced phase pairs. \(\square\)

The audited Pascal moderate-deviation deletion has parent mass
(o(B_r/N)).  Its whole two-point contribution is therefore
(o_A(B_r/H)).  Deleting parent cycles of length at most (H+1) changes
one-point mass by (\exp(o(r))) and two-point mass by at most
((H+1)\exp(o(r))).  Thus (4.4)--(4.5) imply (0.5)--(0.7) for the
retained long-cycle process.

This settles the implication scope exactly.  Positive winding does not
destroy the (3/4,1/2) pullback constants on terminal zero.  It merely
labels the reduced active phases.  The remaining question is their actual
short-lag arrangement under (\tau).

## 5. Why positive terminal layers do not inherit the half-fibre bound

Every active layer with \(z\ge1\) is positive-winding.  Indeed the
terminal root corner contributes the literal suffix \((10)^z\), so

\[
 d(D)=|S(D)|+1\ge2z+1>1.
\]

The audited zero-winding necessity theorem gives \(d(D)=1\) for every
zero-winding return.  Therefore \(\omega_z(F)\ge1\) whenever \(z\ge1\)
and the layer is active.  Terminal zero is the only layer on which the
winding label can be either zero or positive.

Summing (2.5) over all (z\ge1) gives

\[
 \sum_{z=1}^{y}K_z(d,k)
 =P_r(F)-K_0(d,k)
 =\binom{M-1}{2d}.                                \tag{5.1}
\]

Therefore

\[
 \boxed{
 {\sum_{z\ge1}K_z(d,k)\over P_r(F)}
 ={M-2d\over M}={y\over M}.}                    \tag{5.2}
\]

On the saddle this is (1/4+o(1)).  Also a positive terminal layer can
be eligible only when (B_4(F)\le G), equivalently when the predecessor
has at least four positive selections by the horizon.  If this occurs,
the first positive layer alone has size

\[
 {K_1(d,k)\over P_r(F)}
 ={2d(M-2d)\over M(M-1)}
 ={3\over16}+o(1).                                \tag{5.3}
\]

The upper density (5.2) is below one half.  Consequently the deterministic
inclusion--exclusion argument used in (4.7) gives no positive lower bound
for two positive-layer subsets.  The exact entry (3.6) can be positive,
small, or zero according to whether the transported test addresses the
same coordinate and according to the two exact terminal values.

This is not merely a loss of a convenient constant.  It means that the
all-winding two-point pullback cannot be specialized to (z\ge1) by
deleting the terminal-zero sheet after the proof.  One must retain the
transportation matrix (J_u(F;z,z')).

There is nevertheless a one-point companion relation.  On every core
for which a positive layer is eligible,

\[
 \sum_{z\ge1}K_z(d,k)
 \le {M-2d\over2d}K_0(d,k)
 =\left({1\over3}+o(1)\right)K_0(d,k)             \tag{5.4}
\]

in the saddle.  Thus critical positive-layer mass is accompanied by at
least constant-factor terminal-zero **all-winding** mass over the same
reduced active phases.  This is useful for the total (ST_A) gate, but it
does not identify the winding of the companion sheet.

There is also an exact two-point companion domination.  Write

\[
 \alpha={K_0(d,k)\over P_r(F)}={2d\over M},
 \qquad \beta=1-\alpha={M-2d\over M}.             \tag{5.5}
\]

Assume \(\alpha>1/2\), as holds uniformly in the saddle tube.  For a
reduced phase \(F\), let \(S_+(F)\) be the union of all its eligible
layers \(z\ge1\), and let \(S_0(F)\) be its terminal-zero layer.  If two
reduced phases \(F,\tau^uF\) are active, then

\[
 |S_0(F)\cap\Sigma^{-u}S_0(\tau^uF)|
 \ge(2\alpha-1)P_r(F).                            \tag{5.6}
\]

If both phases have a positive layer, then

\[
\boxed{
 |S_+(F)\cap\Sigma^{-u}S_+(\tau^uF)|
 \le{\beta\over2\alpha-1}
 |S_0(F)\cap\Sigma^{-u}S_0(\tau^uF)|.}           \tag{5.7}
\]

More generally, the number of common parents for which at least one of
the two displayed terminal occupancies is positive is at most

\[
\boxed{
 {2\beta\over2\alpha-1}
 |S_0(F)\cap\Sigma^{-u}S_0(\tau^uF)|.}           \tag{5.8}
\]

On the saddle, the constants in (5.7)--(5.8) are respectively
\(1/2+o(1)\) and \(1+o(1)\).

Indeed, \(|S_+(F)|\le\beta P_r(F)\), so the left side of (5.7) is at
most \(\beta P_r(F)\).  Equation (5.6) is inclusion--exclusion.  For
(5.8), split according to which displayed phase has positive terminal
occupancy and use the union bound, costing \(2\beta P_r(F)\).

After summing over reduced phase pairs, every positive-layer pair
contribution is therefore dominated, with an asymptotic absolute constant,
by the terminal-zero **all-winding** correlation over the same cores.
Thus positive terminal occupancy creates no new two-point alternative for
the total \(ST_A\) process.  The only possible bounded-susceptibility
escape already appears on terminal zero, where the winding can be zero or
positive and where (0.7) is exact.

## 6. A deterministic two-parity consequence of four predecessor hits

The following observation records what positive terminal occupancy does
force dynamically.  It is insufficient quantitatively by itself, but it
prevents treating (B_4\le G) as four unrelated marginal hits.

### Lemma 6.1 (four hits create a nearby active pair)

In the one-step reduced equality-particle process, suppose the immediate
predecessor (b=a-1) of the time-zero selected particle (a) is selected
at least four times by time (G).  Then among the one-step phases in
([0,G]) there are two phases of the same parity whose normalized roots
belong to the predecessor-active set (\{B_2\le G\}), with phase distance
at most (G).

#### Proof

Write the first four positive (b)-selection times as

\[
 B_1<B_2<B_3<B_4.
\]

Equality particles do not overtake.  Between (B_j) and (B_{j+1}),
particle (a) must be selected at least once; otherwise (b) cannot move
again into the next edge occupied by (a).  Choose such phases (A_1)
between (B_1,B_2) and (A_2) between (B_2,B_3).

At time zero, the future contains four (b)-selections, so the time-zero
root is active.  At (A_1), the same immediate predecessor (b) has the
three future selections (B_2,B_3,B_4), so that root is active.  At
(A_2), it has the two future selections (B_3,B_4), so that root is
active.  Among the three integer times (0,A_1,A_2), two have the same
parity.  Their distance is at most (G). \(\square\)

The lemma is genuinely two-time, but charging an original phase to the
resulting pair can have multiplicity (O(G)).  It therefore gives only a
constant-order or worse inequality at the critical scale, not the needed
divergence.  The terminal-zero (B_2) boundary remains the sharp isolated
threat.

### 6.2 Actual fixed-winding calibration: bounded, but short-cycle

The complete mountain inverse fibre gives an exact realization of the
bounded branch before long-cycle deletion; see
MATH_THEOREM_N_ST_MOUNTAIN_POSITIVE_WINDING_RENEWAL_AND_SHORT_CYCLE_NOGO_20260726.md.
If its reduced mountain has

\[
 p=2h-1
\]

particles and the parent terminal occupancy is \(z\), then

\[
 g_z=2+(2z+1)p,\qquad
 s_z=h+zp,\qquad
 \omega_z=z.                                     \tag{6.1}
\]

For a fixed finite winding set \(S\), if
\(h/\sqrt r\to c>0\) and \(H/\sqrt r\to A>0\), the exact coordinate
rotation gives

\[
 \boxed{
 {\mathcal C_S(H+1)\over R_S}
 =\left\lfloor{H+1\over p}\right\rfloor
   +2Ac|S|+o(1).}                                \tag{6.2}
\]

Thus genuine PBBS dynamics can have bounded fixed-winding susceptibility.
It does not refute \(ST_A\).  If any positive value \(z\ge1\) is active,
then

\[
 3p+2\le g_z\le2H-1,
\]

so \(p<H+1\).  The whole mountain fibre has quotient period dividing
\(p\), and every one of these positive starts is removed by the exact
short-cycle truncation.  A retained bounded-susceptibility counterexample
must therefore reproduce this renewal behavior on a genuinely long
first-pruned core; one-generation mountain spectators cannot do so.

## 7. A bounded-susceptibility obstruction satisfying every scalar test

The coverage-complete winding-one construction in
`MATH_ATTACK_POSITIVE_WINDING_VANISHING_REDUCTION_AND_COVERAGE_NOGO_20260725.md`
can be read directly as a two-point obstruction.

Choose odd (s,e\to\infty), put

\[
 N=e(2s+1),\qquad h=s-1,qquad L=2s+1,            \tag{7.1}
\]

and choose (e/s\) in a fixed compact interval so that
(s+1\le H\) and (H/L=O_A(1)).  The formal long quotient cycles are
partitioned into blocks of length (L).  One distinguished winding-one
start of duration (s) is selected in every block.  Its full support has
(s+2<L) edges.  Hence the distinguished starts are pairwise
support-disjoint and have density

\[
 {1\over L}=\Theta_A(1/H).                        \tag{7.2}
\]

After the aperiodic amplification, the cycles use
((1-o(1))B_r) formal phases and the distinguished set has

\[
 R_H^{\rm form}=\Theta_A(B_r/H).                  \tag{7.3}
\]

Every distinguished start has at most

\[
 \left\lfloor{H+1\over L}\right\rfloor          \tag{7.4}
\]

further distinguished starts in the forward correlation window.  Thus

\[
 \boxed{
 {\mathcal C_H^{\rm form}\over R_H^{\rm form}}
 \le\left\lfloor{H+1\over L}\right\rfloor=O_A(1).} \tag{7.5}
\]

By choosing (1<H/s<2-o(1)), one may make the strict displacement range
(1\le u\le H+1) contain no next block start, so the left side of (7.5)
is zero.

The same construction has:

* both exact endpoint ledgers and winding one;
* complete proper-prefix firstness;
* Gaussian height (h=s-1);
* long aperiodic quotient cycles;
* exact voltage and area closure;
* complete physical coordinate coverage;
* exact first-deficit moment order; and
* for every individual phase datum, a literal first-dominant Dyck word
  realizing both parity deficits.

It is not a PBBS counterexample because the assigned consecutive phase
words are not proved to satisfy

\[
 D_{i+1}=\tau D_i.                                \tag{7.6}
\]

Equation (7.5) is nevertheless a sharp logical obstruction.  Every
scalar ledger, moment, coverage, phasewise Dyck, and abstract renewal
constraint currently available admits the bounded-susceptibility branch
which would refute (ST_A).  Only simultaneous block-rotation chronology
can exclude it.

## 8. Exact proved and unproved boundary

### Proved

1.  The complete duration--winding transfer cocycle (1.6)--(1.9).
2.  The exact renewal formula (1.11).
3.  Winding constancy on every exact terminal layer, Theorem 2.1.
4.  The all-winding, fixed-winding, and mixed-winding one-point formula
    (2.12) and two-point formula (3.11).
5.  The exact layer transportation entry (3.6), including its same- and
    distinct-coordinate cases.
6.  The saddle coefficients \(3/4\), \(9/16\), and \(4^{-z}\).
7.  The winding-labelled terminal-zero pullback constants (3/4,1/2).
8.  The absence of any deterministic two-phase lower constant on the
    union of positive terminal layers.
9.  The terminal-zero companion domination (5.7)--(5.8).
10. The four-hit two-parity consequence, Lemma 6.1.
11. The exact bounded-susceptibility mountain calibration and its
    short-cycle exclusion (6.1)--(6.2).
12. The bounded-susceptibility formal obstruction (7.5).

### Not proved

1.  (R_H^+=\Theta(B_r/H)) for the genuine PBBS process.
2.  Boundedness or divergence of
    (\mathcal C_H^{++}/R_H^+).
3.  Boundedness or divergence of the terminal-zero reduced ratio
    (K_{U,U}^{(0)}/S_U^{(0)}), even for (U=\{1\}).
4.  A useful aggregate estimate for the transported positive-layer matrix
    (3.6).
5.  Exclusion or realization of the bounded-renewal-gap pattern (7.5)
    under the literal recursion (D_{i+1}=\tau D_i).

The precise positive-winding gate is therefore not another marginal
suffix estimate.  It is the asymptotic susceptibility of the exact
winding-labelled transfer matrix:

\[
 \boxed{
 {\displaystyle
 \sum_{u,F,z,z'}J_u(F;z,z')
   \mathbf1_{\{B_{2z+2}(F)\le G\}}
   \mathbf1_{\{B_{2z'+2}(\tau^uF)\le G\}}
   \mathbf1_{\{\omega_z(F)>0\}}
   \mathbf1_{\{\omega_{z'}(\tau^uF)>0\}}
  \over
  \displaystyle
  \sum_{F,z}K_z(d,k)
   \mathbf1_{\{B_{2z+2}(F)\le G\}}
   \mathbf1_{\{\omega_z(F)>0\}}}.}               \tag{8.1}
\]

At critical mass, a bounded value in (8.1) gives a genuine
(\Omega_A(B_r/H)) packing by the two-point/Caro--Wei inequality and
therefore refutes (ST_A).  If (ST_A) is true, (8.1) must diverge.
Nothing proved here chooses between those alternatives.

## 9. Audit of the decisive fibre steps

1. **Connectivity.**  After compulsory leaves are removed, fixing
   \(q_0=z\) leaves a weak composition of \(y-z\) over \(2d\) boxes.
   It is connected by unit transfers; no passage between different
   terminal values is used.
2. **Itinerary independence.**  The persistent selected-particle word
   \(\kappa_t(F)\) is the reduced PBBS word and is independent of every
   free parent gap.  Thus all lifts in one layer use the same closing
   occurrence \(B_{2z+2}(F)\).
3. **First-maximum ties.**  The winding proof is made on persistent
   particle arcs, not by tracking a chosen deepest leaf.  A tie or change
   of the displayed first maximum cannot alter the selected particle
   identity or the cyclic cut degree.
4. **Arithmetic check.**  Under one unit transfer, every relevant
   one-step cut arc changes by \(0,\pm2\); hence the step-two return ledger
   changes by at most \(4s+2<N\).  Since both values are multiples of
   \(N\), they agree.
5. **Compulsory-offset cancellation.**  The selection-count difference
   in (3.4) belongs to the physical gap.  Passing to free occupancies at
   both phases subtracts exactly the two compulsory core gaps.  Any
   residual affine shift would contradict the fact that the transported
   terminal free coordinate ranges over every integer \(0,\ldots,y\).
6. **Two-coordinate coefficient.**  When the addressed coordinates are
   distinct, two exact values \(z,z'\) leave \(y-z-z'\) units in
   \(p-2\) boxes, giving (3.6).  Same-coordinate tests are diagonal.
7. **Transportation margins.**  Equation (3.7) follows from the two
   terminal-layer partitions and the bijectivity of the actual PBBS
   fibre transport; it independently checks that no affine shift remains.
8. **Scope.**  The exact transfer and winding labels hold for genuine
   parents.  The bounded model in Section 7 is used only as a no-go for
   weaker axioms and is never claimed to satisfy the simultaneous PBBS
   recursion.
