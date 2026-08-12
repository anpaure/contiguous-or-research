# The PBBS short-return start process: exact renewal and degree pullback at (ST_A)

Date: 2026-07-26

Method: pure mathematics only.  No computation, experiment, probabilistic
surrogate, or external input is used.

## 0. Verdict

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
 \qquad h=H+1,
 \qquad G=2H-1.
\]

Let \(\tau_m=\phi^2\) be the step-two PBBS permutation of normalized
rank-\(m\) Dyck roots.  Let \(E_H\) be the roots on parent quotient
cycles longer than \(h\) which start a genuine first return by time
\(G\), and put

\[
 R_H=|E_H|,
 \qquad
 \mathcal C_H=\sum_{t=1}^{h}
     |E_H\cap\tau_m^{-t}E_H|.
 \tag{0.1}
\]

This note gives an exact renewal audit of the remaining \(ST_A\) gate.
The outcome is a sharp non-decision, together with a stronger one-sided
theorem which is useful for a future decision.

1.  The universal Fejér-window bound gives

    \[
     \boxed{
     \mathcal C_H\ge {1\over2}
       \left({(h+1)R_H^2\over B_m}-R_H\right).}
     \tag{0.2}
    \]

    Hence \(H R_H/B_m\to\infty\) forces
    \(\mathcal C_H/R_H\to\infty\).  At the critical density
    \(R_H=\Theta(B_m/H)\), (0.2) gives only a constant.

2.  Under exact simultaneous peak deletion, every active reduced phase
    contributes at least its terminal-zero Pascal hyperplane, of exact
    relative size

    \[
       {2d\over m+d-k}=3/4+o(1)
    \]

    in the critical saddle.  Two active reduced phases contribute a
    common parent fibre of relative size at least \(1/2-o(1)\).  Thus the
    first inverse-Pascal level is two-point neutral: it cannot create the
    missing divergence and cannot wash out bounded clustering.

3.  There is an exact degree-profile pullback which is stronger than the
    scalar two-point comparison.  For an active reduced root \(F\), let

    \[
     \Delta_H(F)=\sum_{t=1}^{h}
       \left(
       \mathbf1_{\mathscr A_H}(\tau_d^tF)
       +\mathbf1_{\mathscr A_H}(\tau_d^{-t}F)
       \right),
     \tag{0.3}
    \]

    where \(\mathscr A_H\) is the literal predecessor-active set

    \[
       \mathscr A_H=\{F:B_2(F)\le G\}.
    \]

    If \(d_H(D)\) is the actual quotient-edge conflict degree of an
    eligible parent start \(D\) and \(\partial D=F\), then

    \[
       \boxed{d_H(D)\le\Delta_H(F).}
       \tag{0.4}
    \]

    Consequently, for every fixed integer \(K\ge0\),

    \[
     \boxed{
     \overline\nu_H\ge {1\over K+1}
      \left[
       \sum_{d,k}K_0(d,k)
       \#\{F\in\mathscr A_H(d,k):\Delta_H(F)\le K\}
       -Z_H
      \right]_+,}
     \tag{0.5}
    \]

    where \(\overline\nu_H\) is the maximum quotient-edge-disjoint
    return packing,

    \[
       K_0(d,k)=\binom{m+d-k-1}{2d-1},
       \qquad
       Z_H\le(2H+2)N^{2H+2}=o(B_m/H).
    \]

    The established minimal-simple-return reduction loses at most a
    factor two.  Therefore a critical Pascal mass of reduced active
    phases with bounded \(\Delta_H\) refutes \(ST_A\), with an explicit
    positive constant.

4.  The implication proposed in the task,

    \[
       \mathcal C_H/R_H\to\infty
       \quad\Longrightarrow\quad
       \overline\nu_H=o(B_m/H),
    \]

    is false even for circular interval systems having exactly the same
    support geometry.  Divergence of the scalar mean is necessary at
    critical start mass, but it is not sufficient for a little-oh
    packing.  The necessary positive statement is instead

    \[
       \Delta_H(F)\to\infty
    \]

    in Pascal-weighted probability, and even that remains only necessary,
    not sufficient.

The exact Dyck renewal identities therefore do not presently choose
between the two requested PBBS alternatives.  They reduce the decision to
one literal dynamical statistic: the Pascal-weighted distribution, along
the actual reduced PBBS cycles, of the two-sided number of translated
phases whose immediate predecessor is selected twice by time \(2H-1\).
Neither a critical lower bound for that active mass nor bounded/divergent
degree in that mass follows from the known renewal census.

## 1. Exact one-start renewal identity

Let \(D\) be a nonexceptional rank-\(m\) root and let

\[
  F=\partial D\in\mathcal D_d,
  \qquad k=\operatorname {pk}(F).
\]

The inverse peak-deletion fibre \(\mathcal F_F\) is the weak-composition
simplex of the free inserted leaves.  Its exact size is

\[
  \boxed{
  P_m(F)=|\mathcal F_F|
  =\binom{m+d-k}{2d}.}
  \tag{1.1}
\]

Let \(z_*(D)\) be the terminal free-slot occupancy.  In the reduced PBBS
started at \(F\), let

\[
  0<B_1(F)<B_2(F)<\cdots
\]

be the positive selection times of the immediate predecessor of the
time-zero selected equality particle.  The no-overtaking predecessor
identity is

\[
  \boxed{G(D)=B_{2z_*(D)+2}(F)}
  \tag{1.2}
\]

whenever the displayed time is below the outer circumference \(N\).
Since \(G<N\) in the present Gaussian window, no wrap correction occurs.

Define

\[
 a_H(F)=\max\{a\ge0:B_{2a+2}(F)\le G\},
 \tag{1.3}
\]

with value \(-1\) when the set is empty.  Then the eligible parent lifts
over \(F\) are exactly

\[
 \mathcal E_H(F)
 =\{D\in\mathcal F_F:z_*(D)\le a_H(F)\}.
 \tag{1.4}
\]

Stars and bars gives the exact cumulative renewal kernel

\[
 \boxed{
 |\mathcal E_H(F)|
 =P_m(F)-
   \binom{m+d-k-a_H(F)-1}{2d},}
 \tag{1.5}
\]

with the binomial-zero convention and with value zero when
\(a_H(F)=-1\).

In particular,

\[
 \mathcal E_H(F)\ne\varnothing
 \quad\Longleftrightarrow\quad
 B_2(F)\le G.
 \tag{1.6}
\]

This proves that the reduced support is precisely

\[
 \mathscr A_H(d,k)
 =\{F\in\mathcal D_d:
       \operatorname {pk}(F)=k, B_2(F)\le G\}.
 \tag{1.7}
\]

If \(F\in\mathscr A_H\), every terminal-zero lift is eligible.  The
number of such lifts is

\[
 \boxed{
 K_0(d,k)=\binom{m+d-k-1}{2d-1},
 \qquad
 {K_0(d,k)\over P_m(F)}={2d\over m+d-k}.}
 \tag{1.8}
\]

Thus a reduced active phase contributes either no parent at all or at
least a fixed positive fraction of its entire parent fibre.  There is no
hidden \(1/H\) factor in the inverse lift.

Summing (1.5) over every reduced root gives the exact untrimmed one-point
census

\[
 \boxed{
 \widetilde R_H=\sum_F|\mathcal E_H(F)|.}
 \tag{1.9}
\]

Deleting parent cycles of length at most \(h\) changes this by at most
\(Z_H\).

## 2. Exact two-start renewal identity

Peak deletion semiconjugates the simultaneous canonical rotations:

\[
 \partial\tau_m^t=\tau_d^t\partial.
 \tag{2.1}
\]

Therefore the actual PBBS evolution gives a fibre bijection

\[
 \Sigma_F^{(t)}:
 \mathcal F_F\longrightarrow\mathcal F_{\tau_d^tF}.
 \tag{2.2}
\]

Put

\[
 J_t(F)=
 \left|
 \mathcal E_H(F)\cap
 (\Sigma_F^{(t)})^{-1}
 \mathcal E_H(\tau_d^tF)
 \right|.
 \tag{2.3}
\]

Partitioning parent starts by their reduced phase gives the exact identity

\[
 \boxed{
 \widetilde{\mathcal C}_H
 =\sum_{t=1}^{h}\sum_FJ_t(F).}
 \tag{2.4}
\]

No independent fibre coupling appears in (2.4): both tests are pulled
back by the same literal PBBS transport.

If either \(F\) or \(\tau_d^tF\) is inactive, then \(J_t(F)=0\).  If
both are active, pull the two terminal-zero hyperplanes back to
\(\mathcal F_F\).  They both have size \(K_0(d,k)\), while the ambient
fibre has size \(P_m(F)\).  Inclusion-exclusion gives

\[
 \boxed{
 (2K_0(d,k)-P_m(F))_+
 \le J_t(F)\le P_m(F).}
 \tag{2.5}
\]

At the Pascal saddle

\[
 d={m\over2}+O(\sqrt{m\log m}),
 \qquad
 k={m\over6}+O(\sqrt{m\log m}),
 \tag{2.6}
\]

one has uniformly

\[
 {K_0\over P_m}=\frac34+o(1),
 \qquad
 {2K_0-P_m\over P_m}=\frac12+o(1).
 \tag{2.7}
\]

Define the Pascal-weighted reduced statistics

\[
 \mathscr R_H
 =\sum_{d,k}P_m(d,k)|\mathscr A_H(d,k)|,
 \tag{2.8}
\]

\[
 \mathscr C_H
 =\sum_{d,k}P_m(d,k)
   \sum_{t=1}^{h}
    |\mathscr A_H(d,k)\cap
       \tau_d^{-t}\mathscr A_H(d,k)|.
 \tag{2.9}
\]

The total inverse-fibre mass outside (2.6) is \(o(B_m/m)\), hence
\(o(B_m/H)\).  Thus (1.8) and (2.5), together with this standard
saddle-tail deletion, give

\[
 \left({3\over4}-o(1)\right)\mathscr R_H
 \le \widetilde R_H\le\mathscr R_H,
 \tag{2.10}
\]

\[
 \left({1\over2}-o(1)\right)\mathscr C_H
 \le \widetilde{\mathcal C}_H\le\mathscr C_H.
 \tag{2.11}
\]

Since the short-parent-cycle errors are \(o(B_m/H)\), at critical mass

\[
 \boxed{
 \left({1\over2}-o(1)\right)
   {\mathscr C_H\over\mathscr R_H}
 \le {\mathcal C_H\over R_H}
 \le
 \left({4\over3}+o(1)\right)
   {\mathscr C_H\over\mathscr R_H}.}
 \tag{2.12}
\]

This proves the claimed two-point neutrality of the exact Dyck renewal
lift.

## 3. The active-phase gap renewal identity

The unresolved statistic can be written without any probability
language.  Fix one reduced \(\tau_d\)-cycle \(O\) of length \(L\), and
write

\[
 x_i=\mathbf1_{\mathscr A_H}(\tau_d^iF),
 \qquad i\in\mathbb Z/L\mathbb Z.
 \tag{3.1}
\]

Suppose the active positions in cyclic order are

\[
 s_1,s_2,\ldots,s_q,
\]

and let

\[
 \rho_j=s_{j+1}-s_j\pmod L,
 \qquad \rho_j\in\{1,\ldots,L\},
 \qquad \sum_{j=1}^q\rho_j=L,
 \tag{3.2}
\]

with the \(\rho_j\) repeated periodically.  Then the exact contribution
of this orbit to the reduced forward correlation is

\[
 \boxed{
 \mathscr C_H(O)
 =P_m(O)
  \sum_{j=1}^q\sum_{\ell\ge1}
  \mathbf1\{\rho_j+\rho_{j+1}+\cdots+
                 \rho_{j+\ell-1}\le h\}.}
 \tag{3.3}
\]

Here \(P_m(O)\) is constant on the orbit because reduced rank and peak
count are \(\tau_d\)-invariant.  Formula (3.3) remains exact when
\(L\le h\): the periodic extension counts repeated laps with the same
multiplicity as the lag sum in (2.9).

Equivalently, for active \(F\), put

\[
 \Delta_H^+(F)=\sum_{t=1}^{h}
       \mathbf1_{\mathscr A_H}(\tau_d^tF),
 \qquad
 \Delta_H^-(F)=\sum_{t=1}^{h}
       \mathbf1_{\mathscr A_H}(\tau_d^{-t}F).
 \tag{3.4}
\]

Then

\[
 \Delta_H(F)=\Delta_H^+(F)+\Delta_H^-(F)
 \tag{3.5}
\]

and the exact weighted identities are

\[
 \boxed{
 \mathscr C_H
 =\sum_{d,k}P_m(d,k)
   \sum_{F\in\mathscr A_H(d,k)}\Delta_H^+(F),}
 \tag{3.6}
\]

\[
 \boxed{
 2\mathscr C_H
 =\sum_{d,k}P_m(d,k)
   \sum_{F\in\mathscr A_H(d,k)}\Delta_H(F).}
 \tag{3.7}
\]

Equation (3.7) follows by reversing every lag.  Thus
\(2\mathscr C_H/\mathscr R_H\) is exactly the Pascal-weighted mean
two-sided active-phase degree.  It is not the distribution of that
degree, and it is not the actual conflict degree.

## 4. Exact pullback of bounded active-phase degree

Let \(I_D\) be the actual quotient residence trace starting at an
eligible long-cycle parent root \(D\).  It consists of at most \(h\)
consecutive quotient edges.  Make the conflict graph \(G_H\) on \(E_H\)
by joining \(D,D'\) precisely when

\[
 I_D\cap I_{D'}\ne\varnothing.
 \tag{4.1}
\]

Let \(d_H(D)\) be its degree.

### Lemma 4.1 (chronological localization of a conflict)

If \(D,D'\in E_H\) conflict, then for some \(1\le t\le h\),

\[
 D'=\tau_m^tD
 \quad\hbox{or}\quad
 D'=\tau_m^{-t}D.
 \tag{4.2}
\]

#### Proof

Different parent quotient cycles have disjoint quotient edges, so the two
starts lie on one cycle.  Cut that cycle immediately before the first of
the two shared-edge traces.  Each trace is now an ordinary interval of at
most \(h\) consecutive edges.  If the second start is later in the cut
order, it lies within the first trace and has forward displacement at
most \(h\); otherwise the reverse displacement is at most \(h\).  The
parent cycle has length greater than \(h\), so no displacement in (4.2)
fixes \(D\).  This proves the claim. \(\square\)

### Theorem 4.2 (renewal-degree pullback)

If \(D\in E_H\) and \(F=\partial D\), then

\[
 \boxed{d_H(D)\le\Delta_H(F).}
 \tag{4.3}
\]

#### Proof

By Lemma 4.1 every conflict neighbour has the form
\(\tau_m^{\pm t}D\) with \(1\le t\le h\).  Semiconjugacy (2.1) sends it
to \(\tau_d^{\pm t}F\).  Eligibility of that parent neighbour implies,
by (1.6), that its reduced phase belongs to \(\mathscr A_H\).  Thus every
distinct conflict neighbour consumes at least one of the lag incidences
counted by (0.3).  Repeated reduced phases or repeated lag descriptions
can only make the right side larger. \(\square\)

For \(K\ge0\), define the exact terminal-zero low-degree mass

\[
 \mathscr L_{H,K}^{(0)}
 =\sum_{d,k}K_0(d,k)
   \#\{F\in\mathscr A_H(d,k):\Delta_H(F)\le K\}.
 \tag{4.4}
\]

### Theorem 4.3 (critical low-degree mass produces a packing)

For every integer \(K\ge0\),

\[
 \boxed{
 \overline\nu_H
 \ge {\bigl[\mathscr L_{H,K}^{(0)}-Z_H\bigr]_+
        \over K+1}.}
 \tag{4.5}
\]

#### Proof

For each core counted in (4.4), take all its terminal-zero parent lifts.
By (1.6)--(1.8) they are eligible.  By Theorem 4.2 each has conflict
degree at most \(K\) in the full parent conflict graph.  At most \(Z_H\)
of these roots lie on the deleted short parent cycles.

For any finite graph,

\[
 \alpha(G)\ge\sum_{v\in V(G)}{1\over d(v)+1}.
 \tag{4.6}
\]

Indeed, order the vertices uniformly at random and retain a vertex when
it precedes every neighbour; the retained set is independent and vertex
\(v\) is retained with probability \(1/(d(v)+1)\).  Apply (4.6) to the
parent conflict graph and retain only the vertices just constructed.
Each contributes at least \(1/(K+1)\), proving (4.5). \(\square\)

Inside the saddle tube (2.6), define

\[
 \mathscr L_{H,K}
 =\sum_{d,k}P_m(d,k)
   \#\{F\in\mathscr A_H(d,k):\Delta_H(F)\le K\}.
 \tag{4.7}
\]

Then (2.7) and (4.5) give

\[
 \overline\nu_H
 \ge {\left({3\over4}-o(1)\right)
          \mathscr L_{H,K}-o(B_m/H)
       \over K+1}.
 \tag{4.8}
\]

The established minimal-simple-return reduction retains at least one of
the two start parities, and therefore at least half of this packing, as a
quotient-edge-disjoint simple fixed-core family.  Hence the following is
an exact refutation criterion:

\[
 \boxed{
 \liminf {H\mathscr L_{H,K}\over B_m}>0
 \quad\hbox{for some fixed }K
 \quad\Longrightarrow\quad ST_A\hbox{ is false}.}
 \tag{4.9}
\]

Conversely, if \(ST_A\) is true, then for every fixed \(K\),

\[
 \boxed{
 \mathscr L_{H,K}=o(B_m/H).}
 \tag{4.10}
\]

If in addition \(\mathscr R_H\ge\kappa B_m/H\), (4.10) says that

\[
 \Delta_H(F)\longrightarrow\infty
 \tag{4.11}
\]

in Pascal-weighted probability conditional on \(F\in\mathscr A_H\).
This is the correct necessary clustering law at the reduced renewal
level.

## 5. Bounded mean clustering gives bounded-degree mass

The degree pullback recovers the negative branch from a bounded
two-point mean, with no independence assumption.

### Corollary 5.1

Suppose, along a subsequence,

\[
 \mathscr R_H\ge\kappa {B_m\over H},
 \qquad
 \mathscr C_H\le M\mathscr R_H
 \tag{5.1}
\]

for fixed \(\kappa>0\) and \(M<\infty\).  Put

\[
 K=\max\{1,\lceil4M\rceil\}.
\]

Then

\[
 \mathscr L_{H,K}\ge {1\over2}\mathscr R_H,
 \tag{5.2}
\]

and consequently

\[
 \overline\nu_H
 \ge
 \left({3\kappa\over8(K+1)}-o(1)\right){B_m\over H}.
 \tag{5.3}
\]

After the factor-two simple reduction this is still a positive multiple
of \(B_m/H=\Theta_A(B_m/\sqrt m)\), so \(ST_A\) is false.

#### Proof

By (3.7), the Pascal-weighted mean of \(\Delta_H\) on
\(\mathscr A_H\) is at most \(2M\).  If \(M=0\), every active phase has
\(\Delta_H=0\), and (5.2) is immediate.  If \(M>0\), Markov's
inequality, used only as the elementary counting inequality

\[
 \sum_F P_m(F)\Delta_H(F)
 \ge 4M\sum_{\Delta_H(F)>4M}P_m(F),
\]

shows that at least half the weighted mass has
\(\Delta_H(F)\le4M\le K\).  This proves (5.2).  Substitute (5.2) in
(4.8). \(\square\)

Via (2.12), the same conclusion holds from

\[
 R_H\ge\kappa' B_m/H,
 \qquad
 \mathcal C_H=O(R_H).
\]

What is not known is whether the literal predecessor process satisfies
either inequality in (5.1).  Formula (1.2) computes the sheets above one
active phase; it does not position the active phases along the reduced
orbit.

## 6. The universal Fejér bound and its critical limitation

For completeness, let \(\tau\) be any permutation of a set of size
\(B\), let \(E\) have size \(R\), and put

\[
 C_h(E)=\sum_{t=1}^h|E\cap\tau^{-t}E|.
\]

Set

\[
 y(v)=\sum_{a=0}^h\mathbf1_E(\tau^av).
\]

Then

\[
 \sum_vy(v)=(h+1)R
\]

and Cauchy--Schwarz gives

\[
 \sum_vy(v)^2\ge{(h+1)^2R^2\over B}.
 \tag{6.1}
\]

On the other hand,

\[
 \sum_vy(v)^2
 =(h+1)R+2\sum_{t=1}^h(h+1-t)
      |E\cap\tau^{-t}E|
 \le(h+1)(R+2C_h(E)).
 \tag{6.2}
\]

Combining (6.1)--(6.2) proves

\[
 \boxed{
 C_h(E)\ge {1\over2}
     \left({(h+1)R^2\over B}-R\right).}
 \tag{6.3}
\]

Apply (6.3) with \(B=B_m\), \(E=E_H\), and \(h=H+1\) to obtain
(0.2).  If \(H R_H/B_m\to\infty\), then
\(\mathcal C_H/R_H\to\infty\).  If
\(R_H=cB_m/H\), the right side divided by \(R_H\) is only
\((c-1)/2+o(1)\).  The critical scale is exactly where this universal
renewal energy stops deciding the problem.

The same proof applies to the Pascal-replicated reduced cycles because
\(P_m(d,k)\) is constant on each cycle.  It gives

\[
 \mathscr C_H\ge {1\over2}
   \left({(h+1)\mathscr R_H^2\over B_m}
         -\mathscr R_H\right),
 \tag{6.4}
\]

which again has only constant strength at
\(\mathscr R_H=\Theta(B_m/H)\).

## 7. Why scalar divergence is not a packing theorem

The following construction records the precise logical obstruction.

### Proposition 7.1

There are circular interval systems with horizon \(H\to\infty\) and
ambient size \(B\), having

\[
 R=\Theta(B/H),
 \qquad
 C_H/R\to\infty,
 \qquad
 \alpha(G_H)=(1/2+o(1))R.
 \tag{7.1}
\]

#### Proof

Choose \(k=k(H)\to\infty\) with \(k=o(H)\).  In each macroblock place
\(k\) interval starts in \(k\) consecutive positions and give those
intervals length \(H\).  They share an edge and form a \(k\)-clique.
In the rest of the macroblock place another \(k\) starts mutually more
than \(H\) apart and more than \(H\) from the clique.  Take mutually
separated copies of this macroblock around a sufficiently long cycle.

One macroblock has length \(\Theta(kH)\), has \(2k\) starts, and has
exactly \(\binom k2\) short-lag start pairs.  With \(n\) macroblocks,

\[
 B=\Theta(nkH),
 \qquad R=2nk=\Theta(B/H),
 \qquad {C_H\over R}={k-1\over4}\to\infty.
\]

All \(nk\) isolated intervals can be added to any independent family,
while a clique contributes at most one interval; this bound is attained.
Hence

\[
 \alpha(G_H)=n(k+1)=(1/2+o(1))R.
\]

This proves (7.1). \(\square\)

The example is not claimed to be PBBS-realizable.  Its consequence is
logical and exact: no theorem depending only on the scalar pair
\((R_H,\mathcal C_H)\) can turn divergent mean clustering into a
little-oh packing bound.  A positive PBBS proof must control the full
renewal gap sequence (3.2), or an equivalent higher-order cluster/degree
profile, using structure not present in the one- and two-start censuses.

## 8. Exact remaining PBBS statement

The predecessor recursion has now been exhausted at one and two starts.
It supplies:

1. the exact sheet count (1.5) over one reduced phase;
2. the exact simultaneous two-phase transport (2.4);
3. the deterministic saddle overlap constants \(3/4\) and \(1/2\);
4. the cyclic active-gap renewal identity (3.3); and
5. the bounded-degree packing pullback (4.5).

It does not supply:

1. a critical one-point lower bound

   \[
     \mathscr R_H=\Omega(B_m/H);
   \]

2. bounded Pascal-weighted degree, which together with that lower bound
   would refute \(ST_A\); or
3. divergence in probability of \(\Delta_H\), which is necessary for a
   positive proof but still would not alone upper-bound the maximum
   independent set.

Accordingly the honest theorem-level conclusion is

\[
 \boxed{
 \begin{array}{c}
 \text{the exact Dyck renewal identities do not yet prove or refute }ST_A;\\[1mm]
 \text{the remaining statistic is the Pascal-weighted law of }\Delta_H
 \text{ on }\mathscr A_H.
 \end{array}}
 \tag{8.1}
\]

A negative decision can now be obtained from the literal pair

\[
 \mathscr R_H\ge\kappa B_m/H,
 \qquad
 \mathscr C_H\le M\mathscr R_H,
\]

or more weakly from any critical mass in one fixed
\(\{\Delta_H\le K\}\) stratum.  A positive decision requires a genuine
PBBS theorem which rules out every such bounded-degree stratum and then
controls the higher-order circular-interval cluster geometry.  Neither
conclusion is encoded in the scalar renewal energy alone.
