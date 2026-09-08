# Lane M: exact harmonic component restitution and the fixed-transposition no-go

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver,
computer algebra, random experiment, or fractional exact-factor surrogate is
used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 t=\frac Wn=\operatorname{Cat}_m,\qquad
 H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed; all Gaussian-window assertions are for
\(m\ge m_0(A)\), so in particular \(H\le m-2\).  The universal fixed-transposition route requested
in this lane is false, even after the exact integer-floor correction and even
when the comparison is made harmonic by harmonic.

The exact conclusions are as follows.

1.  In the canonical MSW factor, for \(\tau=(2\ 3)\), there are
    \(\operatorname{Cat}_{m-2}\) genuine size-two interaction components.
    Their exact weighted private component variance through depth \(H\) is

    \[
      \boxed{
      V^{\rm priv}_{\tau,H}
      =(8S_H-4)\operatorname{Cat}_{m-2},\qquad
      S_H=\sum_{q=1}^H\frac1{c_q}.}
      \tag{0.1}
    \]

    For \(H=\lceil A\sqrt m\rceil\),

    \[
      \boxed{
      V^{\rm priv}_{\tau,H}
      =\left(
       \frac1{2A}\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}
       +o_A(1)\right)Ht.}
      \tag{0.2}
    \]

    Thus a fixed-\(\tau\) strict comparison

    \[
       V_{\tau,H}\le(1-\eta)A_{\tau,H}+B_m
    \]

    with fixed \(\eta>0\) necessarily has

    \[
       B_m=\Omega_A(\eta Ht).
       \tag{0.3}
    \]

2.  This is not merely slow \(E_2\) noise.  At depth one, each private
    component is an elementary four-cell rectangle \(v\), and its exact
    Johnson decomposition satisfies

    \[
      \|\Pi_2v\|_2^2=\frac4{\binom{2m-3}{m-3}},\qquad
      \sum_{j\ge3}\|\Pi_jv\|_2^2
      =4\left(1-\binom{2m-3}{m-3}^{-1}\right).
      \tag{0.4}
    \]

    Consequently the genuine cell has

    \[
       \boxed{V_{\tau,1,\ge3}>\frac15t\qquad(m\ge4).}
       \tag{0.5}
    \]

    The exact higher-harmonic spectral-surplus trace contributed by these
    components is

    \[
      \boxed{
      \sum_{j\ge3}
       \frac{(j-2)(n-j-1)}{n(n-1)}V^{\rm priv}_{\tau,1,j}
      =\frac{2(m-3)}{2m+1}\operatorname{Cat}_{m-2}
      =\left(\frac1{16}+o(1)\right)t.}
      \tag{0.6}
    \]

    Hence the hoped-for higher-harmonic rebate is itself replenished at
    Catalan scale in one physical exact switching cell.

3.  There is a stronger nonlinear obstruction after subtracting the exact
    adjacent-integer floor.  For a moved target pair \(p\), let \(G_p\) be
    its ideal integral smoothing gain and \(C_p\) the component restitution
    above the same pair floor.  In an MSW subfamily proved for every
    \(m\ge4\),

    \[
       \boxed{C_{\tau,1}\ge2\operatorname{Cat}_{m-4}>\frac{t}{128}.}
       \tag{0.7}
    \]

    This is harmful parity-subtracted component collision noise, not raw
    variance.  Since \(C\) is cell-invariant and the cell mean of \(G\) is
    exactly \(C\), every all-factor estimate

    \[
       C_{\tau,H}\le(1-\eta)G_{\tau,H}+B_m
       \tag{0.8}
    \]

    forces \(B_m>\eta t/128\).  In particular the pointwise heat-descent
    budget \(O_A(Ht/n)=o(t)\) is impossible.

4.  Integer smoothing has the exact parity--Johnson identity

    \[
    \boxed{
      \sum_\tau G_{\tau,q}
      =\frac1{2c_q}\left(
       \langle f_q,L_qf_q\rangle
       -\langle p_q,L_qp_q\rangle\right),}
       \tag{0.9}
    \]

    where \(p_q(S)=\mu_q(S)\bmod2\).  Thus the floor correction is a
    nonlinear Dirichlet term; it cannot simply be assigned to the same
    harmonic of \(f_q\).

5.  The uniform-transposition averaged gate is **not** disproved.  At every
    stationary law of fair exact component heat, noise exactly replenishes
    coherent smoothing at every \((q,j)\).  Therefore an averaged deficit
    sufficient for heat descent already implies that every recurrent class
    has \(O_A(Ht)\) mean energy.  That is the missing structural theorem,
    not a consequence of the Johnson eigenvalues.

This closes the pointwise fixed-transposition, harmonic-by-harmonic
variance-deficit lane.  It does not disprove MWB, the constant-one theorem,
an existential good-transposition theorem, or adaptive multistep heat.

## 1. Exact setup and cell trace

At depth \(q\), put

\[
 r=m-q,\qquad N_q=\binom nr,\qquad
 \lambda_q=\frac W{N_q}=c_q+\theta_q,
 \qquad c_q=\lfloor\lambda_q\rfloor,
\]

and

\[
 \beta_q=N_q\theta_q(1-\theta_q).
\]

For an exact middle-wreath factor \(F\), let \(\mu_q(F)\) be its
rank-\(r\) cyclic-interval histogram and

\[
 f_q(F)=\mu_q(F)-\lambda_q\mathbf1.
\]

The unhalved exact floor energy is

\[
 Q_q(F)=\|f_q(F)\|_2^2-\beta_q
 =\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1),
\]

and

\[
 \mathcal Q_H(F)=\sum_{q=1}^H\frac{Q_q(F)}{c_q}.
 \tag{1.1}
\]

Fix a coordinate transposition \(\tau\).  Let \(K\) range over the
connected components of the ownership overlay between \(F\) and \(\tau F\).
Orient the two equally sized sides of \(K\) and put

\[
 \Delta_{K,q}=\mu_q(L_K)-\mu_q(R_K).
\]

Every complete choice of one side of every component is a literal integral
exact factor.  Write

\[
 A_{\tau,q,j}
 =\left\|\sum_K\Pi_{q,j}\Delta_{K,q}\right\|_2^2,
 \qquad
 V_{\tau,q,j}
 =\sum_K\|\Pi_{q,j}\Delta_{K,q}\|_2^2.
 \tag{1.2}
\]

Use the aggregate conventions

\[
 A_{\tau,H}=\sum_{q=1}^H\frac1{c_q}\sum_{j\ge2}A_{\tau,q,j},
 \qquad
 V_{\tau,H}=\sum_{q=1}^H\frac1{c_q}\sum_{j\ge2}V_{\tau,q,j}.
 \tag{1.2a}
\]

The degree-zero and degree-one parts of every \(\Delta_{K,q}\) vanish,
because the two component sides have equal row count and equal point
margins.  Moreover \(\tau\Delta_{K,q}=-\Delta_{K,q}\).

### Theorem 1.1 -- exact harmonic cell trace

On every intrinsic fixed-\(\tau\) switching cell, separately for every
\(q\) and \(j\ge2\),

\[
 \boxed{\mathbb E_{\rm corners}A_{\tau,q,j}=V_{\tau,q,j}.}
 \tag{1.3}
\]

The same assertion holds after stacking ranks and inserting any fixed
positive-semidefinite form on the multiplicity space of copies of \(E_j\).

#### Proof

Index the cell corners by signs \(\sigma_K\in\{\pm1\}\).  Passing to a
corner changes only the orientations of component differences, so

\[
 A_{\tau,q,j}(F_\sigma)
 =\left\|\sum_K\sigma_K\Pi_{q,j}\Delta_{K,q}\right\|_2^2,
\]

whereas \(V_{\tau,q,j}\) is corner-invariant.  Independent sign averaging
kills every cross term \(K\ne L\), proving (1.3).  The same expansion proves
the filtered statement. \(\square\)

Equivalently, fair component resampling has conditional drift

\[
 \boxed{
 \mathbb E\bigl[
 \|f'_{q,j}\|_2^2-\|f_{q,j}\|_2^2\mid F,\tau
 \bigr]
 =\frac14(V_{\tau,q,j}-A_{\tau,q,j}).}
 \tag{1.4}
\]

Thus a strict harmonic noise deficit has positive cell trace.  A genuine
cell with large \(V\) forces a comparably large additive restitution term.

## 2. Exact all-depth MSW component profile

Take the canonical MSW factor and \(\tau=(2\ 3)\).  For each Dyck word
\(R\in\mathcal D_{m-2}\), the canonical overlay has the genuine size-two
component with old and new omitted-label orders

\[
\begin{aligned}
 C_R&=(4,2,3,1,T_R),&
 D_R&=(2,1,4,3,T_R),\\
 C'_R&=(4,3,2,1,T_R),&
 D'_R&=(3,1,4,2,T_R),
\end{aligned}
\tag{2.1}
\]

where \(T_R=(4+\rho(R),n)\).  These are distinct connected ownership
components and may all be switched independently.

Write

\[
 T_R=(t_1,\ldots,t_{2m-3}),
\]

\[
 E_R=(t_1,t_3,\ldots,t_{2m-3}),\qquad
 O_R=(t_2,t_4,\ldots,t_{2m-4}).
\]

Then \(|E_R|=m-1\), \(|O_R|=m-2\).  Multiplication of cyclic positions by
two converts the omitted-label model to ordinary contiguous intervals and
turns (2.1) into

\[
\begin{aligned}
 C_R&=(4,3,E_R,2,1,O_R),\\
 D_R&=(2,4,E_R,1,3,O_R),\\
 C'_R&=(4,2,E_R,3,1,O_R),\\
 D'_R&=(3,4,E_R,1,2,O_R).
\end{aligned}
\tag{2.2}
\]

Delete labels \(2,3\).  The common base cycle is
\((4,E_R,1,O_R)\).  Its four relevant insertion slots are before \(4\),
after \(4\), after \(E_R\), and after \(1\); the old-to-new labels at
those slots are

\[
 2\to3,\qquad3\to2,\qquad2\to3,\qquad3\to2.
 \tag{2.3}
\]

For a list \(X\), write \(\operatorname{pre}_\ell X\) and
\(\operatorname{suf}_\ell X\) for its length-\(\ell\) prefix and suffix,
viewed as sets.  Put

\[
 \partial K=e_{K\cup\{3\}}-e_{K\cup\{2\}}.
\]

### Theorem 2.1 -- exact four-arm formula

For \(1\le q\le m-2\), put \(r=m-q\) and \(\ell=r-1\).  The rank-\(r\)
effect of the component (2.1) is

\[
\boxed{
 d_{R,q}
 =\partial\operatorname{suf}_\ell(O_R)
 +\partial\operatorname{suf}_\ell(E_R)
 -\partial\operatorname{pre}_\ell(E_R)
 -\partial\operatorname{pre}_\ell(O_R).}
\tag{2.4}
\]

Consequently

\[
 \boxed{
 \|d_{R,1}\|_2^2=4,\qquad
 \|d_{R,q}\|_2^2=8\quad(2\le q\le m-2).}
 \tag{2.5}
\]

#### Proof

A rank-\(r\) interval affected by one insertion slot consists of its
inserted label and \(\ell=r-1\) consecutive labels of the base cycle.  In
the stated range no such interval contains both inserted labels.  Match the
windows based at the slots immediately before and after the singleton
\(4\).  Every core cancels except \(\operatorname{suf}_\ell(O_R)\) at the
first slot and \(\operatorname{pre}_\ell(E_R)\) at the second.  The signs
in (2.3) give

\[
 \partial\operatorname{suf}_\ell(O_R)
 -\partial\operatorname{pre}_\ell(E_R).
\]

The identical matching across the singleton \(1\) leaves

\[
 \partial\operatorname{suf}_\ell(E_R)
 -\partial\operatorname{pre}_\ell(O_R).
\]

Adding proves (2.4).

For \(q=1\), \(\ell=m-2=|O_R|\), so the two \(O_R\)-terms cancel.  The
equal-length proper prefix and suffix of the distinct-label list \(E_R\)
are different, leaving two disjoint dipoles and squared norm four.

For \(2\le q\le m-2\),

\[
 1\le\ell\le m-3<|E_R|,|O_R|.
\]

The \(E_R\)-cores and \(O_R\)-cores cannot coincide because the two lists
are disjoint.  Within either list, a proper prefix cannot equal an
equal-length proper suffix: the first list element is absent from the
suffix.  Thus the four cores are distinct.  None contains \(2\) or \(3\),
so their eight dipole cells are also distinct.  This proves (2.5).
\(\square\)

No cross-\(R\) target-support disjointness is asserted or needed.  The
vectors belong to distinct genuine interaction components, and \(V\) is
the sum of their individual squared norms.

Since \(c_1=1\), (2.5) gives the exact private variance (0.1).  Also

\[
 \frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}\longrightarrow\frac1{16}.
 \tag{2.6}
\]

Uniformly for \(q\le A\sqrt m\),

\[
 \lambda_q
 =\prod_{i=0}^{q-1}\frac{m+2+i}{m-i},\qquad
 \log\lambda_q=\frac{q(q+1)}m+O_A(m^{-1/2}).
\]

The bounded function \(x\mapsto1/\lfloor e^{x^2}\rfloor\) has only
finitely many jump points on \([0,A]\), so the Riemann-sum theorem gives

\[
 \frac{S_H}{\sqrt m}\longrightarrow
 \int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
 \tag{2.7}
\]

Equations (2.6)--(2.7) prove (0.2).

### Corollary 2.2 -- raw fixed-cell no-go

Fix \(\eta\in(0,1]\).  If

\[
 V_{\tau,H}(F)\le(1-\eta)A_{\tau,H}(F)+B_m(F,\tau)
 \tag{2.8}
\]

holds at every exact factor and transposition, then on the canonical cell

\[
 \mathbb E_{\rm corners}B_m(F,\tau)
 \ge\eta(8S_H-4)\operatorname{Cat}_{m-2}.
 \tag{2.9}
\]

#### Proof

Average (2.8) over the cell and use Theorem 1.1:

\[
 V_{\tau,H}\le(1-\eta)V_{\tau,H}+\mathbb E B_m.
\]

Now insert (0.1). \(\square\)

In particular, neither \(o_A(Ht)\) nor \(O_A(Ht/n)\) can be the uniform
pointwise remainder.

## 3. Exact harmonic location of the obstruction

At depth one, put \(r=m-1\).  Every component vector in Theorem 2.1 has
the rectangle form

\[
 v=e_{K\cup\{a,c\}}-e_{K\cup\{b,c\}}
   -e_{K\cup\{a,d\}}+e_{K\cup\{b,d\}},
 \tag{3.1}
\]

where \(|K|=r-2=m-3\) and \(a,b,c,d\notin K\) are distinct.

Let

\[
 D_{r,2}g(e)=\sum_{\substack{S\supset e\\|S|=r}}g(S)
\]

be down-incidence to coordinate pairs, and put

\[
 \alpha=\binom{n-4}{r-2}=\binom{2m-3}{m-3}.
\]

### Theorem 3.1 -- exact rectangle spectrum

For the physical rectangle (3.1),

\[
 \boxed{
 \|\Pi_2v\|_2^2=\frac4\alpha,
 \qquad
 \sum_{j\ge3}\|\Pi_jv\|_2^2
 =4\left(1-\frac1\alpha\right).}
 \tag{3.2}
\]

Moreover,

\[
\boxed{
 \sum_{j\ge3}
 \frac{(j-2)(n-j-1)}{n(n-1)}\|\Pi_jv\|_2^2
 =\frac{2(m-3)}{2m+1}.}
\tag{3.3}
\]

#### Proof

The rectangle has zero total and zero point margins, so it lies in
\(E_2\oplus E_3\oplus\cdots\).  In \(D_{r,2}v\), every pair meeting
\(K\) cancels.  The only nonzero pair coordinates are

\[
 ac,bc,ad,bd
\]

with coefficients \(+1,-1,-1,+1\).  Hence

\[
 \|v\|_2^2=4,\qquad\|D_{r,2}v\|_2^2=4.
\]

The map \(D_{r,2}\) annihilates \(E_j\) for \(j\ge3\), while its squared
singular value on \(E_2\) is \(\alpha\).  This proves (3.2).

For (3.3), let \(L_J\) be the ordinary Johnson Laplacian.  The four support
vertices of \(v\) form a four-cycle, and every internal edge joins opposite
signs.  Since the Johnson degree is

\[
 d=r(n-r)=(m-1)(m+2),
\]

the four vertices have \(4(d-2)\) boundary edges of squared difference one,
while the four internal edges have squared difference four.  Therefore

\[
 \langle v,L_Jv\rangle=4(d-2)+16=4d+8.
\]

The \(E_2\) eigenvalue is \(2(n-1)\).  Subtracting this eigenvalue times
\(\|v\|_2^2=4\) gives

\[
\begin{aligned}
 \sum_{j\ge3}(j-2)(n-j-1)\|\Pi_jv\|_2^2
 &=4d+8-8(n-1)\\
 &=4m(m-3).
\end{aligned}
\]

Division by \(n(n-1)=2m(2m+1)\) proves (3.3). \(\square\)

There are \(\operatorname{Cat}_{m-2}\) genuine rectangles.  Since
\(\alpha\ge5\) for \(m\ge4\), and (2.6) is strictly larger than \(1/16\),

\[
 V_{\tau,1,\ge3}
 \ge4\left(1-\frac1\alpha\right)\operatorname{Cat}_{m-2}
 >\frac15t.
 \tag{3.4}
\]

Summing (3.3) proves (0.6).

### Corollary 3.2 -- harmonic-rebate no-go

For either of the two weight systems

\[
 w_j=1\quad(j\ge3),
\]

or

\[
 w_j=\frac{(j-2)(n-j-1)}{n(n-1)}\quad(j\ge3),
\]

no estimate

\[
 \sum_{j\ge3}w_jV_{\tau,1,j}
 \le(1-\eta)\sum_{j\ge3}w_jA_{\tau,1,j}+B_m
 \tag{3.5}
\]

can hold at every exact factor with fixed \(\eta>0\) and uniformly
\(B_m=o(t)\).

#### Proof

Average (3.5) over the genuine MSW cell and apply Theorem 1.1 degree by
degree.  For the first weights, (3.4) forces

\[
 \mathbb E B_m>\eta t/5.
\]

For the second weights, (0.6) forces

\[
 \mathbb E B_m
 \ge\eta\frac{2(m-3)}{2m+1}\operatorname{Cat}_{m-2}
 =\left(\frac\eta{16}+o(1)\right)t.
\]

Both contradict \(o(t)\). \(\square\)

More generally, a family of levelwise inequalities with a common
fractional improvement \(\eta\) and total error \(o(t)\) is impossible
after summing the levels.  An individual level may depend on \(m\), and no
fixed-\(j\) counterexample is claimed.

## 4. The exact adjacent-integer floor

Fix \(q,\tau\), and one moved target pair

\[
 p=\{S,\tau S\}.
\]

Orient the pair and write the component scalar imbalances as

\[
 d_{K,p}=\Delta_{K,q}(S),
 \qquad
 D_p=\sum_Kd_{K,p}=\mu_q(S)-\mu_q(\tau S).
\]

Put

\[
 \pi_p=D_p\pmod2\in\{0,1\}.
\]

The parity is cell-invariant because changing a component side replaces
\(d_{K,p}\) by \(-d_{K,p}\).

### Theorem 4.1 -- exact pair gain and restitution

For the unhalved floor energy, the excess of the current pair above the
best integer allocation with the same pair sum is

\[
 \boxed{G_p=\frac{D_p^2-\pi_p}{2c_q}.}
 \tag{4.1}
\]

After fair independent component resampling, the expected residual excess
above that same pair floor is

\[
 \boxed{C_p=\frac{\sum_Kd_{K,p}^2-\pi_p}{2c_q}.}
 \tag{4.2}
\]

Consequently

\[
 \boxed{
 \mathbb E\mathcal Q_H(F')-\mathcal Q_H(F)
 =\sum_{q,p}(C_p-G_p)
 =\frac14(V_{\tau,H}-A_{\tau,H}).}
 \tag{4.3}
\]

Inside a fixed cell, \(C_p\) is corner-invariant and

\[
 \boxed{\mathbb E_{\rm corners}G_p=C_p}
 \tag{4.4}
\]

pair by pair.

For later use, write

\[
 G_{\tau,q}=\sum_{p\text{ moved by }\tau}G_p,
 \qquad
 C_{\tau,q}=\sum_{p\text{ moved by }\tau}C_p,
\]

and sum these quantities over \(q\le H\) to obtain
\(G_{\tau,H}\) and \(C_{\tau,H}\).

#### Proof

Let the two loads be \(x,y\), with fixed sum \(M=x+y\) and difference
\(D=x-y\).  The part of the pair floor polynomial depending on \(D\) is
\(D^2/2\).  Among integers with the same sum, the minimum has difference
zero if \(M\) is even and difference one if \(M\) is odd.  Since
\(M\equiv D\pmod2\), the excess is \((D^2-\pi)/2\), proving (4.1).

At a random cell corner,

\[
 D'=\sum_K\varepsilon_Kd_{K,p},
\]

so \(\mathbb E(D')^2=\sum_Kd_{K,p}^2\).  The parity remains \(\pi_p\),
which proves (4.2) and (4.4).  Finally, on one pair

\[
 C_p-G_p
 =\frac{\sum_Kd_{K,p}^2-D_p^2}{2c_q}
 =\frac{V_p-A_p}{4c_q}.
\]

Summing proves (4.3). \(\square\)

There is also the useful exact decomposition

\[
 2c_qC_p
 =\sum_K\left(d_{K,p}^2-\mathbf1_{d_{K,p}\ \mathrm{odd}}\right)
 +2\left\lfloor
   \frac{\#\{K:d_{K,p}\text{ odd}\}}2
 \right\rfloor.
 \tag{4.5}
\]

The last term is precisely harmful paired-odd component collision.

## 5. Parity--Johnson identity

Let

\[
 p_q(S)=\mu_q(S)\pmod2\in\{0,1\}
\]

and let \(L_q\) be the Johnson Laplacian on
\(\binom{[n]}{m-q}\).

### Theorem 5.1 -- exact integral smoothing sum

\[
\boxed{
 \sum_\tau G_{\tau,q}
 =\frac1{2c_q}\left(
   \langle f_q,L_qf_q\rangle
   -\langle p_q,L_qp_q\rangle
 \right).}
\tag{5.1}
\]

Equivalently, if \(f_{q,j}\) and \(p_{q,j}\) denote Johnson projections,

\[
\boxed{
 \sum_\tau G_{\tau,q}
 =\frac1{2c_q}\left[
  \sum_{j\ge2}j(n-j+1)\|f_{q,j}\|_2^2
  -\sum_{j\ge1}j(n-j+1)\|p_{q,j}\|_2^2
 \right].}
\tag{5.2}
\]

#### Proof

Every unordered Johnson edge \(\{S,T\}\) is generated by exactly one
coordinate transposition, namely the exchange of the two coordinates in
\(S\triangle T\).  If \(d=\mu_q(S)-\mu_q(T)\), then

\[
 d^2-(d\bmod2)
 =(\mu_q(S)-\mu_q(T))^2-(p_q(S)-p_q(T))^2.
\]

Sum this edge identity and use the Dirichlet form of the Johnson
Laplacian.  Constants are killed by \(L_q\), and exact point margins give
\(f_{q,1}=0\).  The Johnson eigenvalue on \(E_j\) is
\(j(n-j+1)\), proving both formulas. \(\square\)

Thus the exact floor subtraction is the Dirichlet energy of a nonlinear
Boolean parity vector.  Formula (5.2) is an aggregate identity, not a list
of nonnegative same-\(j\) gains.  In particular, the parity vector may have
degrees absent from \(f_q\).  No relaxed-load example is needed for the
physical no-go below.

## 6. Genuine parity-subtracted MSW obstruction

The following exact owner theorem was proved symbolically for all \(m\ge4\)
in `MATH_ATTACK_P5_AFR_BRIDGE_SELECTION_20260725.md`, Theorem 2.1, and was
independently audited there in Section 9.1.

For every \(V\in\mathcal D_{m-4}\), put

\[
 K(V)=\{7\}\cup(8+\operatorname{Down}(V)),
\]

\[
 S_V=K(V)\cup\{2,n\},\qquad
 T_V=K(V)\cup\{3,8\}.
\]

The canonical \((2\ 3)\)-overlay has a genuine private component

\[
 \mathcal K_V
 =\{E(11001100V),E(10101100V)\}
\]

whose exact depth-one effect is

\[
 d_V=-e_{S_V}+e_{\tau S_V}-e_{T_V}+e_{\tau T_V}.
 \tag{6.1}
\]

The exact canonical loads are

\[
 \boxed{
 (\mu_1(S_V),\mu_1(\tau S_V))=(3,1),\qquad
 (\mu_1(T_V),\mu_1(\tau T_V))=(1,1).}
 \tag{6.2}
\]

The four target cells in (6.1) are disjoint as \(V\) varies.  The proof of
(6.1)--(6.2) uses the MSW recursion
\(\rho(1100V)=(4,2,3,1,4+\rho(V))\), followed by the complete symbolic
inverse-owner classification of the two displayed targets.  No finite
enumeration enters this statement.

### Theorem 6.1 -- Catalan harmful floor collision

Throughout the full intrinsic \((2\ 3)\)-cell,

\[
 \boxed{C_{\tau,1}\ge2\operatorname{Cat}_{m-4}>\frac t{128}.}
 \tag{6.3}
\]

#### Proof

Consider first \(p_V=\{S_V,\tau S_V\}\).  Its total load difference at the
canonical corner is \(2\), hence its invariant parity is zero.  The private
component \(\mathcal K_V\) contributes \(d_{K,p}=\pm1\).  Since the sum of
all component imbalances is even, the number of odd component imbalances is
even.  The private odd term therefore forces at least one additional odd
physical component term.  Hence

\[
 \sum_Kd_{K,p_V}^2\ge2,
 \qquad C_{p_V}\ge1.
\]

For \(p'_V=\{T_V,\tau T_V\}\), the total difference is zero and the same
argument gives \(C_{p'_V}\ge1\).  All these pairs are distinct as \(V\)
varies, so summing proves

\[
 C_{\tau,1}\ge2|\mathcal D_{m-4}|.
\]

Finally,

\[
 \frac{\operatorname{Cat}_{m-4}}{\operatorname{Cat}_m}
 =\frac{(m-2)(m-1)m(m+1)}
 {16(2m-7)(2m-5)(2m-3)(2m-1)}
 >\frac1{256}.
\]

For the strict inequality, compare the four denominator factors with
\(2(m-2),2(m-1),2m,2(m+1)\), respectively.  This proves (6.3).
\(\square\)

### Corollary 6.2 -- floor-corrected fixed-\(\tau\) no-go

Fix \(\eta\in(0,1]\).  If (0.8) holds at every exact-factor corner of the
cell, then

\[
 \boxed{
 \mathbb E_{\rm corners}B_m
 \ge2\eta\operatorname{Cat}_{m-4}
 >\frac{\eta t}{128}.}
 \tag{6.4}
\]

#### Proof

Average (0.8) over the cell.  Theorem 4.1 gives

\[
 C_{\tau,H}\le(1-\eta)C_{\tau,H}+\mathbb E B_m.
\]

Now use \(C_{\tau,H}\ge C_{\tau,1}\) and Theorem 6.1. \(\square\)

Since

\[
 \frac{Ht}{n}=\left(\frac A2+o_A(1)\right)\frac t{\sqrt m}=o(t),
\]

no pointwise fixed-transposition theorem with the heat-descent restitution
budget \(O_A(Ht/n)\) can survive (6.4).  The conclusion uses the exact
integer floor, not a real-valued relaxation.

### Proposition 6.3 -- shifted Catalan collision piles

The preceding collision is not confined to one isolated packet.  Fix
\(q\ge2\), and for

\[
 0\le s\le m-q-2
\]

put

\[
 \tau_s=(2s+2\ \ 2s+3).
\]

Then the canonical MSW factor satisfies the exact weighted lower bound

\[
\boxed{
 C_{\tau_s,q}
 \ge\frac1{c_q}
 \operatorname{Cat}_s\operatorname{Cat}_{m-s-q-2}
 \left\lfloor\frac{\operatorname{Cat}_q}{2}\right\rfloor.}
\tag{6.5}
\]

Consequently

\[
\boxed{
 \sum_{s=0}^{m-q-2}C_{\tau_s,q}
 \ge\frac1{c_q}
 \left\lfloor\frac{\operatorname{Cat}_q}{2}\right\rfloor
 \operatorname{Cat}_{m-q-1}.}
\tag{6.6}
\]

In particular, for \(m\ge8\), \(c_2=1\) and

\[
 \sum_{s=0}^{m-4}C_{\tau_s,2}
 \ge\operatorname{Cat}_{m-3}
 =\left(\frac1{64}+o(1)\right)t.
 \tag{6.7}
\]

#### Proof

The contextual MSW selector theorem gives, for every
\(P\in\mathcal D_s\) and \(R\in\mathcal D_{m-s-2}\), a genuine size-two
\(\tau_s\)-component indexed by

\[
 P1100R,\qquad P1010R.
\]

Restrict to suffixes

\[
 R=UV,qquad U\in\mathcal D_q,qquad
 V\in\mathcal D_{m-s-q-2}.
\]

After rotating the displayed four-letter selector block to the beginning,
its common tail is, up to the displayed coordinate shifts,

\[
 T_{P,R}=(2s+4+\rho(R),n,\rho(P)).
\]

The MSW concatenation law gives

\[
 \rho(R)=(\rho(U),2q+\rho(V)).
\]

The block \(\rho(U)\) has even length \(2q\).  In the notation of
Theorem 2.1, the first \(q\) entries of the odd-position parity list
\(E_{P,R}\) are precisely the odd-position sublist of \(\rho(U)\), and these
are all its \(U\)-dependent entries.  At depth \(q\),

\[
 \ell=m-q-1=|E_{P,R}|-q.
\]

Hence the positive arm

\[
 \partial\operatorname{suf}_\ell(E_{P,R})
\]

in (2.4) deletes all \(U\)-dependent entries and depends only on \((P,V)\).
As \(U\) ranges over \(\mathcal D_q\), the
\(\operatorname{Cat}_q\) distinct genuine components therefore put
same-sign odd unit imbalances on one common moved target pair.

If a target pair contains \(a\) specified odd unit component imbalances
and \(b\) further odd component imbalances, then

\[
 \pi_p\equiv a+b\pmod2,
 \qquad
 \sum_Kd_{K,p}^2\ge a+b.
\]

Consequently, regardless of all other component magnitudes,

\[
 2c_qC_p=\sum_Kd_{K,p}^2-\pi_p
 \ge2\left\lfloor\frac{a+b}{2}\right\rfloor
 \ge2\left\lfloor\frac a2\right\rfloor.
\]

Thus every fixed \((P,V)\) group contributes the lower bound
\(c_q^{-1}\lfloor\operatorname{Cat}_q/2\rfloor\).  If target pairs from
different groups coincide, the bound remains additive because

\[
 \left\lfloor\frac{a+b}{2}\right\rfloor
 \ge\left\lfloor\frac a2\right\rfloor
   +\left\lfloor\frac b2\right\rfloor.
\]

There are
\(\operatorname{Cat}_s\operatorname{Cat}_{m-s-q-2}\) groups, proving
(6.5).  The Catalan convolution

\[
 \sum_{s=0}^{m-q-2}
 \operatorname{Cat}_s\operatorname{Cat}_{m-q-2-s}
 =\operatorname{Cat}_{m-q-1}
\]

proves (6.6).  For \(q=2\),
\(\lfloor\operatorname{Cat}_2/2\rfloor=1\), and

\[
 \lambda_2=\frac{(m+2)(m+3)}{m(m-1)}<2
\]

for \(m\ge8\), so \(c_2=1\).  The Catalan ratio tends to \(1/64\),
proving (6.7). \(\square\)

For fixed small \(q\), the certified contribution on the right side of
(6.6) has Catalan scale \(\Theta(t)\), and hence becomes only
\(\Theta(t/n^2)\) after uniform averaging over all \(\binom n2\)
transpositions.  This lower bound does not upper-bound the unlisted
transpositions and therefore does not refute the averaged gate.

## 7. Stationary replenishment and the surviving averaged gate

Consider fair exact component heat: at state \(F\), choose a transposition
and then choose every complete component side independently and uniformly.
The state space is finite.

### Theorem 7.1 -- stationary harmonic replenishment

For any predictable state-dependent transposition distribution and any
stationary law \(\pi\) of the resulting chain,

\[
 \boxed{
 \mathbb E_{\pi,\tau}V_{\tau,q,j}
 =\mathbb E_{\pi,\tau}A_{\tau,q,j}}
 \tag{7.1}
\]

for every \(q,j\ge2\).

If \(\tau\) is a uniform unordered coordinate transposition, then

\[
 \boxed{
 \frac14\mathbb E_{\pi,\tau}V_{\tau,q,j}
 =\kappa_j\mathbb E_\pi\|f_{q,j}\|_2^2,
 \qquad
 \kappa_j=\frac{j(n-j+1)}{n(n-1)}.}
 \tag{7.2}
\]

#### Proof

Average the conditional drift identity (1.4) under stationarity to obtain
(7.1).  For uniform \(\tau\), the Johnson Laplacian identity gives

\[
 \mathbb E_\tau A_{\tau,q,j}
 =4\kappa_j\|f_{q,j}\|_2^2,
\]

which proves (7.2). \(\square\)

There is an exact suffix-filtered form.  For iid uniform transpositions put

\[
 \lambda_j=1-\kappa_j.
\]

At stationarity, for every horizon \(T\),

\[
\boxed{
 \frac14\sum_{s=0}^{T-1}
 \lambda_j^{T-1-s}\,
 \mathbb E_\pi V_{s,q,j}
 =(1-\lambda_j^T)\mathbb E_\pi\|f_{q,j}\|_2^2.}
\tag{7.2a}
\]

Indeed, iterating the conditional harmonic recurrence gives

\[
 \mathbb E\|f_{T,q,j}\|_2^2
 =\lambda_j^T\mathbb E\|f_{0,q,j}\|_2^2
 +\frac14\sum_{s<T}\lambda_j^{T-1-s}
   \mathbb EV_{s,q,j};
\]

stationarity makes the two endpoint expectations equal.  Thus iid future
suffixes do filter old innovations, but at stationarity the accumulated
filtered variance exactly restores all coherent loss, degree by degree.

Put

\[
 s_q(F)=\sum_{j\ge3}
 \frac{(j-2)(n-j-1)}{n(n-1)}\|f_{q,j}(F)\|_2^2,
\]

\[
 \mathscr R_q(F)=\mathbb E_\tau\frac{V_{\tau,q}(F)}4,
\]

and

\[
 Z_A(F)=\sum_{q\le H}\frac1{c_q}
 \left(\mathscr R_q(F)-\frac2n\beta_q-s_q(F)\right).
\]

The exact floor-corrected recurrence is

\[
 \mathbb E[\mathcal Q_H(F')\mid F]
 =\left(1-\frac2n\right)\mathcal Q_H(F)+Z_A(F).
 \tag{7.3}
\]

Therefore every stationary law satisfies

\[
 \boxed{\mathbb E_\pi Z_A=\frac2n\mathbb E_\pi\mathcal Q_H.}
 \tag{7.4}
\]

In particular, the still-unproved averaged drift gate

\[
 Z_A(F)
 \le\frac{2-\eta_A}{n}\mathcal Q_H(F)
   +\frac{C_A}{n}Ht
 \tag{7.5}
\]

would imply

\[
 \boxed{
 \mathbb E_\pi\mathcal Q_H
 \le\frac{C_A}{\eta_A}Ht}
 \tag{7.6}
\]

in every recurrent class.  Thus (7.5) already contains a classwise
low-energy theorem; it is not furnished by the harmonic eigenvalues alone.

The explicit MSW obstruction concerns one transposition.  Uniform averaging
divides its contribution by \(\binom n2=\Theta(n^2)\).  Its
\(\Theta(t)\) harmful floor excess becomes only \(\Theta(t/n^2)\), whereas
the permitted term in (7.5) is

\[
 \frac{Ht}{n}=\Theta_A(t/\sqrt m).
\]

Therefore Theorem 6.1 does not contradict (7.5), an existential
good-transposition policy, or an adaptive multistep policy.

## 8. Independent audit and scope

1. **Integrality.**  Every cell corner used above is an actual exact
   middle-wreath factor.  The decisive countercell consists of complete
   ownership components, not fractional rows or an abstract signed kernel.

2. **The all-depth norm.**  Formula (2.4) proves the formerly experimental
   value eight for every \(2\le q\le m-2\).  No target-support disjointness
   between different \(R\)'s is used; component variance sums norms before
   any such overlap matters.

3. **The harmonic projection.**  The factor
   \(\alpha=\binom{n-4}{r-2}\) is the squared singular value of
   down-incidence on \(E_2\), not its singular value.  This is why (3.2)
   contains \(4/\alpha\), not \(4/\alpha^2\).

4. **The Laplacian normalization.**  The convention
   \(\langle g,L_Jg\rangle=\sum_{\{S,T\}}(g(S)-g(T))^2\) counts every
   unordered Johnson edge once.  Under this convention the rectangle has
   energy \(4d+8\), and (3.3) has the stated factor
   \(2(m-3)/(2m+1)\).

5. **The floor factor of two.**  The report uses the unhalved polynomial
   \((u-c)(u-c-1)\).  At fixed pair sum, excess above the adjacent-integer
   minimum is \((D^2-\pi)/2\).  This agrees exactly with
   \((V-A)/4\) in (4.3).

6. **The owner input.**  The load pairs \((3,1)\) and \((1,1)\), their
   signs, and cross-\(V\) disjointness were independently checked in the
   source theorem.  The new deduction needs only their parity and the
   private odd unit; arbitrary splitting of all remaining components cannot
   weaken the lower bound.

7. **What is refuted.**  Universal fixed-\(\tau\) strict component variance
   below coherent smoothing, including a sum of harmonic-level inequalities
   with a fixed positive fractional gain and total
   \(O_A(Ht/n)\) restitution, is false.  Exact parity-floor subtraction does
   not repair it.

8. **What remains unproved.**  The uniform-\(\tau\) averaged gate (7.5),
   nonstationary restitution for a fixed smoothing word, adaptive suffix
   filtering, correlated nonfair choices, and the direct local-minimum
   theorem remain open.  No literal contiguous-OR word is constructed, and
   the constant-one theorem is not proved here.

## 9. Final lane status

The requested local harmonic inequality cannot exist at the quantitative
scale required for one-step floor-corrected descent:

\[
 \boxed{
 \text{fixed-}\tau\text{ raw restitution}=\Theta_A(Ht),\qquad
 \text{fixed-}\tau\text{ harmful floor restitution}>t/128.}
\]

Both statements occur inside one genuine exact MSW switching cell, and the
depth-one obstruction lies overwhelmingly in \(E_{j\ge3}\), with an exact
Catalan-scale spectral-surplus trace.  Fair harmonic smoothing has zero cell
trace and exact stationary replenishment.  Therefore harmonic comparison by
itself cannot yield the missing descent.

Any surviving heat proof must use a genuinely nonlocal selection of
transpositions, ownership-sensitive averaging, or adaptive recomputation.
Those are different structural theorems; they are not consequences of an
interaction-component variance bound below transposition smoothing.
