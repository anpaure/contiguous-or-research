# Ordinary one-packet stopped profiles: minimax collapse and the dual gate

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, web
input, or probabilistic black box is used.

## 0. Outcome

Use the notation of
MATH_THEOREM_ORDINARY_ANNULAR_STOPPED_PROFILE_FUNCTIONAL_20260727.md:

\[
 n=2m,\qquad r=m-q_0,\qquad J=H-q_0,
 \qquad V_d=\binom{[n]}{r-d},\qquad N_d=|V_d|.
\tag{0.1}
\]

At a reachable entrance matching \({\cal M}\), let
\({\cal L}({\cal M})\) be the raw legal next-packet catalogue,
\({\cal H}_d\) the current depth-\(d\) holes, and \(c_d\) the scalar
capacity increment. For a legal packet \(e\), define its hole score

\[
                         h_d(e)=|e_d\cap{\cal H}_d|,
 \qquad h(e)=\sum_{d=0}^{J}h_d(e),
 \qquad C=\sum_{d=0}^{J}c_d.
\tag{0.2}
\]

The conclusions are exact.

1. The one-packet minimax problem has no stochastic advantage. Among
   all state-dependent laws on the legal catalogue, the smallest
   stopped-profile drift is

   \[
                         \Delta({\cal M})
          =C-\max_{e\in{\cal L}({\cal M})}h(e).
   \tag{0.3}
   \]

   Hence the least nonnegative error with which (SD) can hold at this
   state is

   \[
                         \boxed{\varepsilon^*({\cal M})
                              =(\Delta({\cal M}))_+.}
   \tag{0.4}
   \]

   A deterministic maximum-hole packet is optimal. No minimax mixture,
   entropy bias, or fractional packet law can improve (0.4).

2. Maximum-hole selection is exactly steepest descent for the stopped
   potential \(\mathfrak C\):

   \[
      \mathfrak C({\cal M}\cup\{e\})-\mathfrak C({\cal M})
                         =C-h(e).
   \tag{0.5}
   \]

   Therefore a deterministic greedy process proves the one-packet SD
   route to the Ordinary stopped-profile theorem if

   \[
                         \sum_{j<\tau}
                         \varepsilon^*({\cal M}_j)=o(W).
   \tag{0.6}
   \]

   Conversely, every one-packet proof using nonnegative SD errors must
   pay at least \(\varepsilon^*({\cal M}_j)\) at each state it visits.
   Thus (0.6), along a greedy trajectory which also reaches the scalar
   stopping window, is the exact sufficient local theorem still
   required. It is not asserted to be necessary for the weaker signed
   theorem (SP), or globally optimal among trajectories: a locally
   nonoptimal packet can change the future residual catalogue.

3. The stronger simultaneous depth-profile problem has a genuine LP
   dual. If one asks for

   \[
            {\mathbb E}h_d(e)\ge c_d-\varepsilon
                         \quad(0\le d\le J),
   \tag{0.7}
   \]

   the least common error is

   \[
   \boxed{
   \varepsilon_{\rm vec}^*
    =
    \left[
    \max_{\theta\in\Delta_{J+1}}
      \left\{
       \sum_d\theta_dc_d
       -\max_{e\in{\cal L}({\cal M})}
          \sum_d\theta_dh_d(e)
      \right\}
    \right]_+.}
   \tag{0.8}
   \]

   A nonnegative depth weight \(\theta\) with a positive gap is the
   exact statewise Farkas obstruction.

4. There is an exact early positive regime. If

   \[
                  |{\cal M}|(J+1)n^2<N_J,
   \tag{0.9}
   \]

   then some legal packet is disjoint from the current support at
   every depth:

   \[
                         e_d\cap S_d=\varnothing
                         \quad(0\le d\le J).
   \tag{0.10}
   \]

   In the asymptotic annular regime all depths are then unsaturated,
   \(h_d(e)=c_d=n\), and

   \[
                         \Delta({\cal M})=0.
   \tag{0.11}
   \]

   Thus a deterministic zero-drift process runs for
   \(\Theta(N_J/((J+1)n^2))\) packets. Any genuine statewise
   obstruction must occur after this collision-free range.

5. A Gibbs hole-biased law can approximate the deterministic maximum,
   but supplies no new combinatorics. With

   \[
                 p_\vartheta(e)
                 =\frac{\exp(\vartheta h(e))}
                        {\sum_{f\in{\cal L}}\exp(\vartheta h(f))},
   \tag{0.12}
   \]

   one has

   \[
        \max_eh(e)-{\mathbb E}_{p_\vartheta}h(e)
                     \le\frac{\log|{\cal L}|}{\vartheta}.
   \tag{0.13}
   \]

   Sending \(\vartheta\) sufficiently fast to infinity makes the
   cumulative soft-max loss \(o(W)\); the unresolved term remains
   exactly the deterministic gap (0.3).

Consequently one-step minimax or state-dependent randomization alone
cannot prove (SD). The proposed SD route has been reduced to a concrete
maximum-weight cyclic-order assertion: along one near-perfect entrance
trajectory, the cumulative positive support-function gaps (0.4) must
be \(o(W)\). A statewise obstruction is a reachable state with a
positive dual gap in (0.3) or (0.8); a global no-go additionally needs
such gaps to be unavoidable on a positive-density part of every
near-perfect trajectory.

This note does not construct such a macroscopic reachable obstruction,
nor does it prove that the gaps stay small after the early regime.

## 1. The one-packet score is linear in the law

Fix a reachable state \({\cal M}\) and abbreviate
\({\cal L}={\cal L}({\cal M})\). Let \(p=(p_e)_{e\in{\cal L}}\) be an
arbitrary conditional law for the next packet. The one-packet formula
from the stopped-profile theorem gives

\[
 \begin{aligned}
 {\mathscr P}({\cal M},p)
 &=C-\sum_{d=0}^{J}
       \sum_{T\in{\cal H}_d}
         \Pr_{e\sim p}(T\in e_d)\\
 &=C-\sum_{e\in{\cal L}}p_eh(e).
 \end{aligned}
\tag{1.1}
\]

### Theorem 1.1 (simplex-extreme-point theorem)

\[
 \boxed{
 \min_{p\in\Delta({\cal L})}{\mathscr P}({\cal M},p)
   =C-\max_{e\in{\cal L}}h(e).}
\tag{1.2}
\]

The minimizer may be taken to be a point mass on one maximum-hole
packet.

#### Proof

Equation (1.1) is affine in \(p\). A linear functional on a simplex
attains its minimum at an extreme point. Equivalently,
\(\sum_ep_eh(e)\le\max_eh(e)\), with equality at a maximizer.
\(\square\)

### Corollary 1.2 (exact SD error)

At the fixed state, there exists a one-packet law satisfying

\[
                         {\mathscr P}\le\varepsilon,
 \qquad \varepsilon\ge0,
\tag{1.3}
\]

if and only if

\[
                         \varepsilon\ge
            \left(C-\max_{e\in{\cal L}}h(e)\right)_+.
\tag{1.4}
\]

Thus (0.4) is the exact optimum over laws. A specified nonoptimal law
can of course require a larger error.

The result concerns the aggregate signed SD functional. Randomization
can still be useful for controlling unrelated degrees or for producing
concentration, but it cannot improve its conditional mean.

### Corollary 1.3 (the entrance depth is identically neutral)

For the raw ordinary legal catalogue, if a legal next packet exists,
then every legal \(e\) satisfies

\[
                         h_0(e)=c_0=n.
\tag{1.5}
\]

Hence depth zero contributes exactly zero to every scalar gap
\(C-h(e)\); all positive obstruction comes from depths \(d\ge1\).

#### Proof

Entrance legality is \(e_0\subseteq V_0\setminus S_0={\cal H}_0\), so
\(h_0(e)=|e_0|=n\). Since entrance supports of previously selected
packets are disjoint, \(|S_0|=G\). Existence of \(e\) forces
\(|{\cal H}_0|=N_0-G\ge n\), and consequently \(c_0=n\). \(\square\)

## 2. Potential maximization and the exact cumulative condition

The pathwise stopped identity gives, for a single next packet,

\[
 \mathfrak C({\cal M}\cup\{e\})-\mathfrak C({\cal M})
                 =\sum_d(c_d-h_d(e))=C-h(e).
\tag{2.1}
\]

### Theorem 2.1 (maximum-hole steepest descent)

At every state, a packet maximizing \(h(e)\) minimizes the next value
of \(\mathfrak C\) among all legal one-packet extensions.

For the deterministic maximum-hole process,

\[
 \mathfrak C_\tau
                  =\sum_{j<\tau}\Delta({\cal M}_j),
\tag{2.2}
\]

and

\[
 \mathfrak C_\tau
                  \le\sum_{j<\tau}
                         \varepsilon^*({\cal M}_j).
\tag{2.3}
\]

#### Proof

The first assertion is (2.1). Summing (2.1) along the greedy
trajectory gives (2.2). Since
\(\Delta\le(\Delta)_+=\varepsilon^*\), (2.3) follows.
\(\square\)

For an arbitrary conditional one-packet law at the same state,
Theorem 1.1 gives

\[
                         {\mathscr P}_j\ge\Delta({\cal M}_j).
\tag{2.4}
\]

If a proof insists on nonnegative statewise SD errors
\({\mathscr P}_j\le\varepsilon_j\), then whenever
\(\Delta({\cal M}_j)>0\),

\[
                         \varepsilon_j
                         \ge\varepsilon^*({\cal M}_j).
\tag{2.5}
\]

Thus no conditional mixing argument can lower the positive-gap bill.
The weaker signed theorem (SP) may exploit later negative
\(\Delta\)'s; the stronger SD route pays the positive part as in
(2.3).

The greedy process is only one-step optimal. Entrance-packet matchings
do not have a proved exchange property which would make steepest
descent globally optimal. Equation (2.3) is therefore an exact
reduction, not a terminal estimate.

## 3. The vector minimax theorem

The aggregate SD constraint tests only the all-ones combination of
depths. A stronger question is whether one law can hit every depth
near its scalar increment.

Let \(A\) be the \((J+1)\times|{\cal L}|\) matrix

\[
                         A_{d,e}=h_d(e).
\tag{3.1}
\]

Define

\[
 \varepsilon_{\rm vec}^*
 =\min_{p\in\Delta({\cal L})}
       \max_{0\le d\le J}
       \left(c_d-(Ap)_d\right)_+.
\tag{3.2}
\]

### Theorem 3.1 (depth-profile minimax dual)

Equation (0.8) holds.

#### Proof

First omit the outer positive part. For a vector \(z\),

\[
                         \max_d z_d
       =\max_{\theta\in\Delta_{J+1}}\sum_d\theta_dz_d.
\tag{3.3}
\]

The payoff is bilinear in \(p,\theta\), and both simplices are compact.
Finite minimax gives

\[
 \begin{aligned}
 \min_{p\in\Delta({\cal L})}
 \max_{\theta\in\Delta_{J+1}}
 \sum_d\theta_d(c_d-(Ap)_d)
 &=
 \max_{\theta\in\Delta_{J+1}}
 \min_{p\in\Delta({\cal L})}
 \sum_d\theta_d(c_d-(Ap)_d)\\
 &=
 \max_{\theta\in\Delta_{J+1}}
 \left[
 \sum_d\theta_dc_d
 -\max_{e\in{\cal L}}\sum_d\theta_dh_d(e)
 \right].
 \end{aligned}
\tag{3.4}
\]

Now

\[
 \max_d(z_d)_+=\max\{0,\max_dz_d\}.
\tag{3.5}
\]

Since the outer maximum with zero is monotone and the minimum is
attained, minimizing the left side of (3.5) takes the positive part of
the value in (3.4). \(\square\)

### Corollary 3.2 (statewise dual obstruction)

If a reachable state admits \(\theta\in\Delta_{J+1}\) and
\(\gamma>0\) such that

\[
 \max_{e\in{\cal L}}
       \sum_d\theta_dh_d(e)
 \le
       \sum_d\theta_dc_d-\gamma,
\tag{3.6}
\]

then every one-packet law has vector-profile error at least
\(\gamma\).

For the actual aggregate SD inequality, the exact obstruction is

\[
                         \max_{e\in{\cal L}}h(e)
                                  \le C-\gamma.
\tag{3.7}
\]

No target-degree average can refute (3.6) or (3.7); one must exhibit a
legal cyclic order crossing the weighted current holes.

## 4. A deterministic collision-free initial regime

Let \({\cal E}\) be the full directed cyclic-packet catalogue, with
cyclic rotations identified. Symmetry gives, for every
\(T\in V_d\),

\[
 \frac{|\{e\in{\cal E}:T\in e_d\}|}{|{\cal E}|}
                         =\frac n{N_d}.
\tag{4.1}
\]

This is the same target-regularity identity used in the stopped-profile
note, but here it is applied to the actual current support.

### Theorem 4.1 (exact zero-drift prefix)

If a reachable entrance matching \({\cal M}\) of size \(s\) satisfies

\[
                         s(J+1)n^2<N_J,
\tag{4.2}
\]

then there is a packet \(e\) such that

\[
                         e_d\cap S_d=\varnothing
                         \qquad(0\le d\le J).
\tag{4.3}
\]

This packet is entrance-legal. If in addition \(n(s+1)\le N_J\), then
all depths remain unsaturated after adding it, and

\[
                         h_d(e)=c_d=n
                         \qquad(0\le d\le J).
\tag{4.4}
\]

#### Proof

At depth \(d\), the current support has size at most \(sn\). By (4.1)
and the union bound, the proportion of all packets meeting \(S_d\) is
at most

\[
                         |S_d|\frac n{N_d}
                         \le\frac{s n^2}{N_d}.
\tag{4.5}
\]

Summing over the \(J+1\) depths and using \(N_d\ge N_J\), the
proportion meeting at least one current support is smaller than one by
(4.2). Hence a packet satisfying (4.3) exists.

The case \(d=0\) of (4.3) is exactly entrance legality. Under the
additional inequality,

\[
             G+n=n(s+1)\le N_J\le N_d,
\tag{4.6}
\]

so \(c_d=n\), while (4.3) says all \(n\) targets of
\(e_d\) are current holes. This proves (4.4). \(\square\)

In the stated Gaussian annulus, (4.2) implies the additional inequality
for all sufficiently large \(m\): indeed

\[
 n(s+1)<\frac{N_J}{(J+1)n}+n<N_J,
\tag{4.6a}
\]

because \(N_J/n\to\infty\). Thus the finite-parameter qualification
does not change the asymptotic prefix.

### Corollary 4.2 (deterministic early scheduler)

Starting from the empty state, repeatedly choose a packet supplied by
Theorem 4.1. This gives a deterministic entrance matching of size

\[
             \left\lfloor
               \frac{N_J-1}{(J+1)n^2}
             \right\rfloor
\tag{4.7}
\]

with

\[
                         \mathfrak C=0
\tag{4.8}
\]

throughout the construction.

The range (4.7) is exponentially large but is only an
\(O((Jn)^{-1})\) fraction of the required \(\Theta(N_0/n)\) packet
count. It does not settle the macroscopic stopped profile.

## 5. Gibbs hole bias and its exact limitation

For \(\vartheta>0\), define the state-dependent law (0.12).

### Lemma 5.1 (soft maximum)

\[
 \max_{e\in{\cal L}}h(e)
 -{\mathbb E}_{p_\vartheta}h(e)
 \le\frac{\log|{\cal L}|}{\vartheta}.
\tag{5.1}
\]

#### Proof

Put \(Z=\sum_e\exp(\vartheta h(e))\). Then

\[
 \log Z
 =\vartheta{\mathbb E}_{p_\vartheta}h
    +{\rm Ent}(p_\vartheta)
 \le\vartheta{\mathbb E}_{p_\vartheta}h+\log|{\cal L}|,
\tag{5.2}
\]

while \(\log Z\ge\vartheta\max_eh(e)\). Subtract and divide by
\(\vartheta\). \(\square\)

Thus

\[
 {\mathscr P}({\cal M},p_\vartheta)
 \le
 \Delta({\cal M})
 +\frac{\log|{\cal L}|}{\vartheta}.
\tag{5.3}
\]

Choose predictable \(\vartheta_j\) so that

\[
                         \sum_{j<\tau}
             \frac{\log|{\cal L}_j|}{\vartheta_j}=o(W).
\tag{5.4}
\]

Then, along the Gibbs scheduler's own trajectory, its conditional drift
exceeds the statewise deterministic optimum by only \(o(W)\) in total.
This does not compare that trajectory with the future states of the
greedy trajectory. Since no restriction in the Ordinary problem
prevents arbitrarily large finite \(\vartheta_j\), the statewise
softening is always available.

It does not bound \(\sum_j(\Delta({\cal M}_j))_+\). The Gibbs law
therefore supplies a bona fide state-dependent hole-biased law, but
reduces its success exactly to the same deterministic gap as
Theorem 1.1.

## 6. The global maximum-coverage LP

For completeness, the terminal ordinary problem also has a direct
fractional formulation. Fix a desired packet count \(s\). Introduce
\(x_e\in[0,1]\) for ordinary packets and
\(y_{d,T}\in[0,1]\) for covered targets. The relaxation is

\[
 \max\sum_{d=0}^{J}\sum_{T\in V_d}y_{d,T}
\tag{6.1}
\]

subject to

\[
 \sum_{e:R\in e_0}x_e\le1
                         \qquad(R\in V_0),
\tag{6.2}
\]

\[
                         \sum_ex_e=s,
\tag{6.3}
\]

\[
 y_{d,T}\le\sum_{e:T\in e_d}x_e,
 \qquad 0\le y_{d,T}\le1.
\tag{6.4}
\]

### Theorem 6.1 (exact terminal LP dual)

The value of (6.1)--(6.4) equals

\[
 \min_{\alpha,\lambda,\beta}
 \left\{
   \sum_{R\in V_0}\alpha_R+s\lambda
   +\sum_{d,T}(1-\beta_{d,T})
 \right\},
\tag{6.5}
\]

where \(\lambda\in\mathbb R\), \(\alpha_R\ge0\),
\(0\le\beta_{d,T}\le1\), and every packet \(e\) obeys

\[
 \sum_{R\in e_0}\alpha_R+\lambda
 \ge
 \sum_{d=0}^{J}\sum_{T\in e_d}\beta_{d,T}.
\tag{6.6}
\]

#### Proof

Give (6.2) dual variables \(\alpha_R\ge0\), (6.3) the free variable
\(\lambda\), (6.4)'s covering inequalities variables
\(\beta_{d,T}\ge0\), and the upper bounds \(y_{d,T}\le1\) variables
\(\gamma_{d,T}\ge0\). The packet columns give

\[
 \sum_{R\in e_0}\alpha_R+\lambda
       \ge\sum_{d,T\in e_d}\beta_{d,T},
\]

and the target columns give \(\beta_{d,T}+\gamma_{d,T}\ge1\). The dual
objective is
\(\sum_R\alpha_R+s\lambda+\sum_{d,T}\gamma_{d,T}\).
At optimum one may take
\(\gamma_{d,T}=(1-\beta_{d,T})_+\), and then truncate every
\(\beta_{d,T}>1\) to one; this only relaxes the packet inequalities and
does not raise the objective. This yields (6.5)--(6.6), and finite LP
duality proves equality. \(\square\)

An integral optimum consists of an entrance matching with \(y\)
recording its depth supports. To achieve correlated leave \(o(W)\),
its objective must be

\[
                         \sum_{d=0}^{J}\min\{ns,N_d\}-o(W).
\tag{6.7}
\]

The stopped maximum-hole scheduler is the natural online primal
augmentation for (6.1)--(6.4). The entrance-packet set system has no
proved exchange or total-unimodularity property, so one-step optimality
does not imply an integral near-optimum of (6.1).

The LP is nevertheless useful for a no-go: a dual target-price
certificate below (6.7) would be a global fractional obstruction,
stronger than a bad trajectory. No such certificate is presently
known for the full ordinary catalogue.

## 7. Exact remaining sufficient gate

Define, along the deterministic maximum-hole process,

\[
 \delta_j=
 \sum_{d=0}^{J}c_{d,j}
 -
 \max_{e\in{\cal L}({\cal M}_j)}
       \sum_{d=0}^{J}|e_d\cap{\cal H}_{d,j}|.
\tag{7.1}
\]

The maximum-hole one-packet SD route is now the concrete assertion

\[
 \boxed{
 L_\tau=O(N_0/\sqrt m),
 \qquad
 \sum_{j<\tau}(\delta_j)_+=o(W).}
\tag{7.2}
\]

Under (7.2), Theorem 2.1 and the scalar leave estimate in the stopped
functional note give an ordinary entrance matching with \(o(W)\)
aggregate annular holes.

Conversely, at any fixed visited state no state-dependent one-packet
law can prove SD with a smaller conditional error than
\((\delta_j)_+\). Thus the proposed one-step stochastic theorem has
become a deterministic maximum-weight cyclic-order problem. This does
not rule out a non-greedy trajectory with a better future state, nor
does it replace the weaker signed cancellation permitted by (SP).

A sharp statewise no-go would consist of a reachable matching
\({\cal M}\) and a number \(\gamma=\Omega(n)\) such that

\[
 \max_{e\in{\cal L}({\cal M})}
       \sum_d|e_d\cap{\cal H}_d|
 \le
       \sum_dc_d-\gamma.
\tag{7.3}
\]

If such states occur on \(\Omega(W/n)\) steps of every near-perfect
trajectory, then cumulative SD is \(\Omega(W)\). No such reachable
ordinary obstruction is constructed here.

Therefore:

* state-dependent Gibbs or minimax laws are completely understood;
* the early collision-free regime is positive and deterministic;
* randomization cannot repair a positive deterministic support gap;
  and
* the unresolved content is the macroscopic geometry of maximum-weight
  legal cyclic orders in the actual stopped holes.
