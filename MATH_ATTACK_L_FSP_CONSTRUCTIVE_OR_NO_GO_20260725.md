# Lane L: fractional survival packets, constructive near-factors, and the exact no-go frontier

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, random
experiment, solver, or unproved asymptotic matching theorem is used.  All
rounding which produces a claimed object is performed inside one already
exact wreath factor.  Ambient candidate-hypergraph calculations are used
only as diagnostics unless an exact completion is explicitly present.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 W=\binom nm,\qquad
 t=\frac Wn=\operatorname{Cat}_m,
 \qquad K=K_A:=\lceil A\sqrt m\rceil .
 \tag{0.1}
\]

All fixed-window statements below are for sufficiently large \(m\), so in
particular \(K_A\le m-1\).  Every specialization using
\(c_1=1\) assumes \(m\ge3\); at the exceptional value \(m=2\), one has
\(\lambda_1=c_1=2\).

This attack does **not** prove \((\mathrm{FSP}_A)\), and it does not prove a
factor-fibre-wide \(\Omega(t)\) obstruction.  It does, however, give an
exact constructive/no-go reduction considerably sharper than the bare
packet LP.

The principal new statements are as follows.

1.  If \(\nu(F,\beta)\) is the maximum number of pairwise row-disjoint
    survival packets, then, on a packet system of rank at most \(R\),
    \[
      \boxed{
      \nu(F,\beta)\le \vartheta(F,\beta)
      \le \tau(F,\beta)\le R\nu(F,\beta).
      }
      \tag{0.2}
    \]
    The union of any maximal disjoint packet family is an integral
    quota-safe deletion set.  Thus, at fixed \(A\), a target-small maximum
    packet
    matching is already a constructive quota-safe near-factor inside the
    same exact factor.  No dependent-rounding lemma remains after the
    factor has been fixed.

2.  There is an explicit load score \(L_q^*(F)\), optimized exactly over
    the balanced high-quota positions, for which
    \[
      \boxed{
      \frac1n\max_{q\le K}L_q^*(F)
      \le \vartheta_A(F)
      \le \sum_{q\le K}L_q^*(F).
      }
      \tag{0.3}
    \]
    Both inequalities are constructive: the lower one is a feasible
    packet packing in the compressed dual, while the upper one is a
    closed-form fractional packet cover.  Moreover
    \[
      \boxed{
      \frac{O_q(F)}{R_A}\le L_q^*(F)\le O_q(F),
      }
      \tag{0.4}
    \]
    where \(O_q\) is the nearest balanced overload and \(R_A=O_A(1)\) is
    explicit below.

3.  At depth one, writing
    \[
      a_j=\#\{S:\mu_1^F(S)=j\},\qquad
      \rho_1=\frac{2W}{m+2},\qquad
      T_3=\sum_{j\ge3}j a_j,
    \]
    one has
    \[
      \boxed{
      \vartheta_A(F)
      \ge \frac1n\left((a_2-\rho_1)_++\frac{T_3}{3}\right).
      }
      \tag{0.5}
    \]
    Hence \((\mathrm{FSP}_A)\) forces the number of holes, the error in the
    number of double targets, and all triple-plus occurrence mass to be
    \(o(W/\sqrt m)\).  Conversely, every factor having a positive-density
    value in the parentheses in (0.5), and every sufficiently small linear
    edit of that factor, has packet mass \(\Omega(t)\).  This is a genuine
    noncanonical edit-basin obstruction, although not a universal one.

4.  The quadratic coownership surplus
    \[
      V_q(F):=
      \sum_S\binom{\mu_q^F(S)}2
      -\left[N_q\binom{c_q}2+c_q\rho_q\right]
      \tag{0.6}
    \]
    is nonnegative and satisfies
    \[
      \boxed{
      \vartheta_A(F)\le
      \sum_{q\le K}L_q^*(F)
      \le\sum_{q\le K}O_q(F)
      \le\sum_{q\le K}V_q(F).
      }
      \tag{0.7}
    \]
    Therefore
    \[
      \sum_{q\le K}V_q(F)=o_A(t/\sqrt m)
      \tag{0.8}
    \]
    is a clean exact pair-energy sufficient target for a prospective
    dependent construction.  It is stronger than
    FSP, but it is an exact pair-energy statement on middle-disjoint rows
    of one factor.

5.  The attractive \(O(m^{-2})\) codegree belongs only to the projected
    \(P_v\)-star hypergraph.  The full middle hypergraph has normalized
    codegree \(2/(m+1)\), lower resources have nested correlations already
    equal to \(2/m\) at depth one, and the augmented edge rank is
    \(n(K+1)=\Theta_A(m^{3/2})\).  More decisively, there is an exact
    conditioning dichotomy:
    
    * before an exact factor is selected, the ambient star codegrees are
      available but exact residual completion is absent;
    * after an exact factor is selected, completion is automatic, but the
      induced middle degree is one and the ambient codegrees say nothing
      about its lower owner cuts.

6.  The symmetric fractional star point cannot be repaired
    perturbatively.  At a suitable depth \(q\le A\sqrt m\), every
    target-small quota-feasible fractional near-factor, with
    \(b=o_A(t/\sqrt m)\), is \(\Omega_A(t)\) in
    \(\ell^1\) from the uniformly thinned candidate vector.  One-shot
    independent candidate selection followed only by deletion leaves at
    most \((1-e^{-1}+o(1))t\) matching rows with high probability, and the
    depth-one quota alteration alone requires
    \((3/e-1-o(1))t\) deletions.  These are rigorous no-go statements for
    symmetric thinning and one-shot alteration, not for a global
    dependent construction.

7.  Any successful quota-safe near-factor, after coordinate
    symmetrization, must create
    \[
       (1/2-o(1))W
    \]
    aggregate negative covariance among depth-one coowner pairs.  Only
    \(O(W/m)\) of this is supplied by pairs forbidden through middle
    intersection.  Thus the missing rounding must impose macroscopic
    negative correlation among middle-disjoint, pairwise compatible
    wreaths.  The exact constant and the conditioned-owner calculation are
    proved in Section 9.

8.  A genuine positive-density obstruction is already known beyond the
    single canonical point.  The suspended first-occurrence packet matching
    gives
    \[
      \vartheta(F,\beta)
      \ge (L_m-d(F,F_m^{\rm MSW}))_+,
      \qquad
      \frac{L_m}{t}\longrightarrow
      \frac{17608}{1238769}.
      \tag{0.9}
    \]
    Hence an entire positive-radius edit ball around the canonical factor,
    including the first explicit rebundling, has \(\Omega(t)\) packet mass.
    This still leaves exact factors outside that basin.

The exact surviving positive theorem is therefore not a local rounding
lemma.  It must construct a macroscopically nonuniform exact factor whose
bounded packets have a target-small maximum matching number (equivalently,
any maximal matching once that number is bounded), or whose
compressed dual admits no packing above that scale.  The exact surviving
negative theorem must force either the depth score in (0.3), or a
bounded-congestion owner packing, to have linear mass in **every** positive
exact factor.  Neither statement follows from the current star or
point-margin identities.

## 1. Fixed-window packet normalization

At depth \(q\), put

\[
 r_q=m-q,\qquad
 N_q=\binom n{r_q},\qquad
 \lambda_q=\frac W{N_q},\qquad
 c_q=\lfloor\lambda_q\rfloor,
 \tag{1.1}
\]

and

\[
 \rho_q=W-c_qN_q,
 \qquad 0\le\rho_q<N_q.
 \tag{1.2}
\]

A balanced quota has the unique form

\[
 \beta_q(S)=c_q+\mathbf1_{H_q}(S),
 \qquad |H_q|=\rho_q.
 \tag{1.3}
\]

Fix one exact middle wreath factor \(F\), \(|F|=t\).  For
\(S\in\binom{[n]}{m-q}\), let

\[
 \mathcal O_{q,S}
 =\{E\in F:E\text{ owns }S\text{ as a cyclic }(m-q)\text{-interval}\},
 \qquad h_{q,S}=|\mathcal O_{q,S}|.
 \tag{1.4}
\]

One wreath owns a target at most once and owns exactly \(n\) targets at
every depth.  With

\[
 k_{q,S}:=\beta_q(S)+1,
 \tag{1.5}
\]

the survival packets generated by \((q,S)\) are all
\(k_{q,S}\)-subsets of \(\mathcal O_{q,S}\).  They exist exactly when
\(h_{q,S}\ge k_{q,S}\).  Denote the union of these resource-labelled
packet families by \(\mathcal P(F,\beta)\).

For a row set \(B\subseteq F\), the following are exactly equivalent:

\[
 \mu_q^{F\setminus B}(S)\le\beta_q(S)\quad(q\le K,S)
 \tag{1.6}
\]

and

\[
 B\cap P\ne\varnothing\quad(P\in\mathcal P(F,\beta)).
 \tag{1.7}
\]

Thus the fractional and integral deletion values are

\[
 \vartheta(F,\beta)=
 \min\left\{\sum_{E\in F}x_E:
 x_E\ge0,\ \sum_{E\in P}x_E\ge1\ (P\in\mathcal P)\right\},
 \tag{1.8}
\]

and

\[
 \tau(F,\beta)=
 \min\{|B|:B\subseteq F\text{ satisfies }(1.7)\}.
 \tag{1.9}
\]

The compressed dual imported from `PACKET_HALL_RECOURSE_20260725.md` is

\[
\boxed{
\begin{aligned}
 \vartheta(F,\beta)=\max\ &\sum_{a\in\mathcal V}Y_a\\
 \text{subject to }&Y_a\ge0,\\
 &\sum_{a\in\mathcal V}
   Y_a\bigl(k_a-|\mathcal O_a\setminus Z|\bigr)_+
   \le |Z|\qquad(Z\subseteq F),
\end{aligned}}
\tag{1.10}
\]

where \(\mathcal V=\{a:h_a\ge k_a\}\).  Equivalently, a resource mass
\(Y_a\) must distribute \(k_aY_a\) owner load, at most \(Y_a\) per owner,
under unit total capacity at every wreath.  The cut in (1.10) is exactly the
amount which packets of resource \(a\) are forced to place in \(Z\).

### 1.1 Explicit packet-rank constant

The exact ratio is

\[
 \lambda_q
 =\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.
 \tag{1.11}
\]

If \(m\ge4(A+1)^2\) and \(q\le K_A\), then

\[
\begin{aligned}
 \log\lambda_q
 &\le\sum_{i=0}^{q-1}\frac{2(i+1)}{m-i}\\
 &\le\frac{q(q+1)}{m-q+1}
 \le2(A+1)(A+2).
\end{aligned}
\tag{1.12}
\]

Consequently one may take

\[
 C_A:=\left\lceil e^{2(A+1)(A+2)}\right\rceil,
 \qquad
 \boxed{R_A:=C_A+2},
 \tag{1.13}
\]

and every nonempty packet in the window has size at most \(R_A\).  The
constant depends on fixed \(A\), never on \(m\).

## 2. Bounded packet rank gives a direct integral alteration

Let \(\nu(F,\beta)\) be the maximum cardinality of a family of pairwise
vertex-disjoint survival packets.

### Theorem 2.1 -- packet matching/cover sandwich

For every finite packet hypergraph of rank at most \(R\),

\[
 \boxed{
 \nu\le\vartheta\le\tau\le R\nu.
 }
 \tag{2.1}
\]

Moreover, if \(\mathcal M\) is any maximal pairwise disjoint packet family,
then

\[
 B_{\mathcal M}:=\bigcup_{P\in\mathcal M}P
 \tag{2.2}
\]

is an integral packet cover and

\[
 |B_{\mathcal M}|\le R|\mathcal M|\le R\nu.
 \tag{2.3}
\]

#### Proof

Putting dual weight one on pairwise disjoint packets gives a feasible
packet packing, so \(\nu\le\vartheta\).  Fractional relaxation gives
\(\vartheta\le\tau\).

If a packet avoided the union in (2.2), it could be adjoined to
\(\mathcal M\), contradicting maximality.  Thus the union is a cover.  It
contains at most \(R\) rows per selected packet, proving (2.3) and
\(\tau\le R\nu\).  \(\square\)

### Corollary 2.2 -- exact-factor constructive dichotomy

For fixed \(A\), the following are equivalent up to the fixed factor
\(R_A\), with the **same** exact factor and the **same** balanced quota
system:

\[
 \nu(F,\beta)=o_A(t/\sqrt m),
 \quad
 \vartheta(F,\beta)=o_A(t/\sqrt m),
 \quad
 \tau(F,\beta)=o_A(t/\sqrt m).
 \tag{2.4}
\]

If the first condition holds, delete (2.2) and put

\[
 G=F\setminus B_{\mathcal M}.
 \tag{2.5}
\]

Then \(G\) is quota-safe and the deleted rows themselves are an exact
wreath completion of \(G\).  The conclusion is a quota-safe core inside
one exact factor; the deleted rows do not separately form an exact factor
of the whole middle layer, nor is that required.

This is the cleanest constructive use of bounded packet rank.  A random or
dependent rounding of a fractional cover cannot improve the asymptotic
scale: a maximal disjoint-packet alteration already gives the integral
object within \(R_A\).

## 3. The exact quota score and its compressed-dual packing

Fix a depth \(q\) and a high-quota set \(H_q\) of size \(\rho_q\).  Suppress
the subscript \(q\) temporarily and define

\[
 L_q(F,H_q)
 :=\sum_{S:h_S\ge k_S}\frac{h_S}{k_S},
 \qquad
 L_q^*(F):=\min_{|H_q|=\rho_q}L_q(F,H_q).
 \tag{3.1}
\]

### Theorem 3.1 -- exact score sandwich

For every exact factor \(F\),

\[
 \boxed{
 \frac1n\max_{q\le K}L_q^*(F)
 \le\vartheta_A(F)
 \le\sum_{q\le K}L_q^*(F),
 }
 \tag{3.2}
\]

where

\[
 \vartheta_A(F)=\min_{H_1,\ldots,H_K}
                    \vartheta(F,\beta).
 \tag{3.3}
\]

More generally, for fixed quota sets and nonnegative \(\alpha_q\) with
\(\sum_q\alpha_q\le1\),

\[
 \vartheta(F,\beta)
 \ge\frac1n\sum_{q\le K}\alpha_q L_q(F,H_q).
 \tag{3.4}
\]

#### Proof: lower bound

For an active resource \((q,S)\), put total dual packet mass

\[
 Y_{q,S}:=\frac{\alpha_qh_{q,S}}{nk_{q,S}}
 \tag{3.5}
\]

uniformly on its \(\binom{h_{q,S}}{k_{q,S}}\) packets.  A fixed owner belongs
to the fraction \(k_{q,S}/h_{q,S}\) of those packets, so this resource puts
exactly \(\alpha_q/n\) congestion on each owner.  A wreath owns exactly
\(n\) resources at each depth.  Its total congestion is therefore at most
\(\sum_q\alpha_q\le1\).  The packing is feasible and has objective (3.4).

Taking one \(\alpha_q=1\) at a time, then minimizing the quota system, gives
the lower half of (3.2).

#### Proof: upper bound

Choose a minimizing high set at each depth and define, for every row,

\[
 x_E=\max\left(
  \left\{\frac1{k_{q,S}}:
  h_{q,S}\ge k_{q,S},\ E\in\mathcal O_{q,S}\right\}
  \cup\{0\}\right).
 \tag{3.6}
\]

Every member of a packet generated by \((q,S)\) has weight at least
\(1/k_{q,S}\).  Since that packet has \(k_{q,S}\) members, its weight is at
least one.  Hence \(x\) is a fractional cover.  Also

\[
\begin{aligned}
 \sum_{E\in F}x_E
 &\le\sum_E\sum_{\substack{q,S:\ E\in\mathcal O_{q,S}\\h_{q,S}\ge k_{q,S}}}
                \frac1{k_{q,S}}\\
 &=\sum_{q\le K}\sum_{S:h_{q,S}\ge k_{q,S}}
                \frac{h_{q,S}}{k_{q,S}}
 =\sum_{q\le K}L_q^*(F).
\end{aligned}
\tag{3.7}
\]

This proves the upper half.  \(\square\)

Thresholding (3.6), or applying Theorem 2.1, gives an integral quota-safe
deletion family of size at most

\[
 R_A\sum_{q\le K}L_q^*(F).
 \tag{3.8}
\]

Thus

\[
 \boxed{
 \sum_{q\le K}L_q^*(F)=o_A(t/\sqrt m)
 \quad\Longrightarrow\quad (\mathrm{FSP}_A)\text{ and }HQ_A.
 }
 \tag{3.9}
\]

### 3.1 Exact optimization of the high-quota positions

For an integer load \(h\), define

\[
 g_{c,0}(h)=
 \begin{cases}
 0,&h\le c,\\
 h/(c+1),&h\ge c+1,
 \end{cases}
 \qquad
 g_{c,1}(h)=
 \begin{cases}
 0,&h\le c+1,\\
 h/(c+2),&h\ge c+2.
 \end{cases}
 \tag{3.10}
\]

The benefit from assigning a high quota to a cell of load \(h\) is

\[
 \Delta_c(h):=g_{c,0}(h)-g_{c,1}(h)
 =\begin{cases}
 0,&h\le c,\\
 1,&h=c+1,\\
 \dfrac{h}{(c+1)(c+2)},&h\ge c+2.
 \end{cases}
 \tag{3.11}
\]

Let
\(\Delta_{(1)}\ge\cdots\ge\Delta_{(N_q)}\) be these benefits in decreasing
order, with ties arbitrary.  Then

\[
 \boxed{
 L_q^*(F)
 =\sum_Sg_{c_q,0}(h_{q,S})
  -\sum_{i=1}^{\rho_q}\Delta_{(i)}.
 }
 \tag{3.12}
\]

Indeed, every high cell replaces \(g_{c,0}\) by \(g_{c,1}\), and exactly
\(\rho_q\) cells must be high.  Thus the optimum consists precisely of the
largest benefits.  Formula (3.12) is exact, including \(\rho_q=0\).

### 3.2 Comparison with nearest balanced overload

For a fixed high set put

\[
 D_q(H_q)=\sum_S(h_{q,S}-\beta_q(S))_+.
 \tag{3.13}
\]

On an active cell, with \(k=\beta+1\), its contribution is

\[
 d=h-k+1.
 \tag{3.14}
\]

Since \(k\le R_A\),

\[
 \frac d{R_A}\le\frac hk\le d.
 \tag{3.15}
\]

The right inequality is equivalent to
\((k-1)(h-k)\ge0\); the left follows from \(d\le h\) and \(k\le R_A\).
Because equal-total histograms satisfy

\[
 O_q(F)=\min_{|H_q|=\rho_q}D_q(H_q),
 \tag{3.16}
\]

minimizing (3.15) gives

\[
 \boxed{
 \frac{O_q(F)}{R_A}\le L_q^*(F)\le O_q(F).
 }
 \tag{3.17}
\]

The minimizing high sets in the two quantities need not coincide.  The
lower inequality holds for every high set; for the upper inequality one
evaluates \(L_q\) at an overload-minimizing high set.

Combining (2.1), (3.2), and (3.17) gives the useful one-depth no-go gate

\[
 O_q(F)\ge\varepsilon W
 \quad\Longrightarrow\quad
 \vartheta_A(F)\ge\frac{\varepsilon}{R_A}t,
 \quad
 \nu_A(F)\ge\frac{\varepsilon}{R_A^2}t.
 \tag{3.18}
\]

Here \(\nu_A(F)\) denotes the packet matching number for any chosen quota
system minimizing \(\vartheta_A(F)\); the same chosen minimizer must be used
throughout the comparison.

## 4. The sharp depth-one score

For \(m\ge3\), at \(q=1\),

\[
 \lambda_1=\frac{m+2}{m},\qquad
 c_1=1,\qquad
 N_1=\frac m{m+2}W,\qquad
 \rho_1=\frac{2W}{m+2}.
 \tag{4.1}
\]

Let

\[
 a_j=\#\{S:h_{1,S}=j\},
 \qquad
 T_3=\sum_{j\ge3}j a_j.
 \tag{4.2}
\]

Formula (3.12) specializes to

\[
\boxed{
 L_1^*(F)
 =\frac12\sum_{j\ge2}j a_j
  -\operatorname{Top}_{\rho_1}
  \left(
    \{1^{[a_2]}\}\cup
    \bigcup_{j\ge3}\{(j/6)^{[a_j]}\}
  \right),
}
\tag{4.3}
\]

where \(\operatorname{Top}_{\rho}\) means the sum of the \(\rho\) largest
entries, with zeros available from cells of load at most one.

The selected top sum is at most

\[
 \min(a_2,\rho_1)+\frac16T_3.
 \tag{4.4}
\]

Consequently

\[
 \boxed{
 L_1^*(F)\ge(a_2-\rho_1)_++\frac13T_3,
 }
 \tag{4.5}
\]

and (0.5) follows from Theorem 3.1.

The two mass identities

\[
 \sum_ja_j=N_1,
 \qquad
 \sum_jj a_j=W=N_1+\rho_1
 \tag{4.6}
\]

give

\[
 a_0=a_2-\rho_1+\sum_{j\ge3}(j-1)a_j.
 \tag{4.7}
\]

From (4.5)--(4.7),

\[
 \boxed{
 T_3\le3L_1^*,\qquad
 |a_2-\rho_1|\le3L_1^*,\qquad
 a_0\le4L_1^*.
 }
 \tag{4.8}
\]

Therefore

\[
 \vartheta_A(F)=o_A(t/\sqrt m)
 \tag{4.9}
\]

forces

\[
 a_0=o_A(W/\sqrt m),\qquad
 |a_2-\rho_1|=o_A(W/\sqrt m),\qquad
 T_3=o_A(W/\sqrt m).
 \tag{4.10}
\]

This is stronger than aggregate \(o(W)\) prebalance: already at one depth,
FSP requires the factor to be within \(o(W/\sqrt m)\) occurrence mass of a
perfect \(\{1,2\}\)-valued first shadow.

If all first-shadow loads lie in \(\{0,1,2\}\), then (4.7) gives

\[
 a_2=\rho_1+a_0,
 \tag{4.11}
\]

and the score is exact:

\[
 \boxed{L_1^*(F)=O_1(F)=a_0.}
 \tag{4.12}
\]

### 4.1 A general noncanonical edit-basin obstruction

Suppose, for some fixed \(\varepsilon>0\),

\[
 (a_2-\rho_1)_++T_3\ge\varepsilon W.
 \tag{4.13}
\]

Then (4.5) gives

\[
 \vartheta_A(F)\ge\frac\varepsilon3t.
 \tag{4.14}
\]

The quota-minimized packet value is one-Lipschitz under replacement of one
factor row: retaining a cover on common rows and assigning weight one to a
new row changes the optimum by at most one, and the reverse comparison is
identical.  Hence every exact factor \(F'\) at row distance

\[
 d(F,F')\le\frac\varepsilon6t
 \tag{4.15}
\]

satisfies

\[
 \boxed{\vartheta_A(F')\ge\frac\varepsilon6t.}
 \tag{4.16}
\]

This theorem applies around any exact factor satisfying (4.13), not only
the canonical factor.  It still does not show that every exact factor
satisfies (4.13).

## 5. Quadratic coownership as an exact pair-energy sufficient target

For a full exact factor define

\[
 V_q(F):=
 \sum_S\binom{h_{q,S}}2
 -\left[N_q\binom{c_q}2+c_q\rho_q\right].
 \tag{5.1}
\]

The bracket is the number of equal-target owner pairs in a perfectly
balanced integer histogram: raising one load from \(c_q\) to \(c_q+1\)
increases \(\binom h2\) by \(c_q\), and there are \(\rho_q\) raised cells.

### Theorem 5.1 -- exact quadratic certificate

For every depth,

\[
 \boxed{V_q(F)\ge O_q(F)\ge L_q^*(F)\ge0.}
 \tag{5.2}
\]

Equality \(V_q(F)=0\) holds exactly when the depth-\(q\) histogram is
balanced, in which case its packet system is empty under the matching
balanced quota.

Consequently,

\[
 \boxed{
 \sum_{q\le K}V_q(F)=o_A(t/\sqrt m)
 \quad\Longrightarrow\quad
 \vartheta_A(F)=o_A(t/\sqrt m).
 }
 \tag{5.3}
\]

An integral quota-safe core is then obtained by deleting at most

\[
 R_A\sum_{q\le K}V_q(F)
 \tag{5.4}
\]

rows of \(F\).

#### Proof

Write

\[
 a_S=h_{q,S}-c_q.
 \tag{5.5}
\]

Since \(\sum_Sh_{q,S}=W=c_qN_q+\rho_q\),

\[
 \sum_Sa_S=\rho_q.
 \tag{5.6}
\]

Expanding (5.1) and using (5.6) gives the parity-floor identity

\[
 \boxed{
 V_q(F)=\frac12\sum_Sa_S(a_S-1).
 }
 \tag{5.7}
\]

For every integer \(a\), \(a(a-1)\ge0\); equality holds only for
\(a\in\{0,1\}\).  Thus \(V_q\ge0\), and equality forces all loads to be
\(c_q\) or \(c_q+1\).  Equation (5.6) then forces exactly \(\rho_q\) high
loads.

Define the floor deficit and ceiling excess

\[
 D_q^-:=\sum_S(-a_S)_+,
 \qquad
 D_q^+:=\sum_S(a_S-1)_+.
 \tag{5.8}
\]

The exact nearest-quota identity is

\[
 O_q(F)=\max\{D_q^-,D_q^+\}.
 \tag{5.9}
\]

Indeed, clipping the histogram into \(\{c_q,c_q+1\}\) costs
\(D_q^-+D_q^+\) in full \(\ell^1\) and leaves the wrong number of high
cells by \(D_q^--D_q^+\); correcting that cardinality gives full distance
\(2\max(D_q^-,D_q^+)\).

If \(a=-z\le-1\), then

\[
 \frac{a(a-1)}2=\frac{z(z+1)}2\ge z,
 \tag{5.10}
\]

and if \(a\ge2\), then

\[
 \frac{a(a-1)}2\ge a-1.
 \tag{5.11}
\]

Termwise summation yields

\[
 V_q(F)\ge D_q^-+D_q^+\ge O_q(F).
 \tag{5.12}
\]

Now use (3.17) and Theorem 3.1.  \(\square\)

For \(m\ge3\), at depth one the identity is particularly transparent.  If
\(M=a_0\), then

\[
 \boxed{
 V_1(F)=M+\sum_{j\ge3}\binom{j-1}{2}a_j.
 }
 \tag{5.13}
\]

In particular, if all loads are at most two,

\[
 V_1(F)=O_1(F)=L_1^*(F)=M.
 \tag{5.14}
\]

### 5.1 Pair-energy form

For distinct rows \(E,E'\in F\), let

\[
 \gamma_q(E,E')
 =\#\{S:E,E'\in\mathcal O_{q,S}\}
 \tag{5.15}
\]

be their number of common depth-\(q\) targets.  Double-counting owner pairs
gives

\[
 \sum_S\binom{h_{q,S}}2
 =\sum_{\{E,E'\}\subset F}\gamma_q(E,E').
 \tag{5.16}
\]

Therefore \(V_q\) is exactly the excess pair coownership over the balanced
integer minimum.  Since rows of \(F\) are already middle-disjoint, (5.3)
is a genuine cost-minimization target on compatible candidate pairs:
construct a perfect exact matching whose total shallow coownership energy
is within \(o_A(t/\sqrt m)\) of the floor-corrected minimum.

This criterion is sufficient, not necessary.  A target-small exceptional
row family could hit all packets while the owners concentrated around it
produce much larger quadratic energy.

## 6. An exact quota-safe near-factor criterion

The packet formulation can also be stated directly for a partial matching.
Let \(G\) consist of exactly \(t-b\) pairwise middle-disjoint wreaths and
put

\[
 \eta_{q,S}:=\mu_q^G(S).
 \tag{6.1}
\]

At every depth,

\[
 \sum_S\eta_{q,S}=n(t-b)=W-nb.
 \tag{6.2}
\]

Define

\[
 \mathfrak D_q^-(G)
 :=\sum_S(c_q-\eta_{q,S})_+.
 \tag{6.3}
\]

### Theorem 6.1 -- exact balanced-quota criterion

There is a balanced quota \(\beta_q\) satisfying

\[
 \eta_{q,S}\le\beta_q(S)\quad\text{for every }S
 \tag{6.4}
\]

if and only if

\[
 \boxed{
 \max_S\eta_{q,S}\le c_q+1
 \quad\text{and}\quad
 \mathfrak D_q^-(G)\le nb.
 }
 \tag{6.5}
\]

The criterion must hold at every controlled depth for the same \(G\), but
the balanced high sets may be chosen independently by rank.

#### Proof

Assume first that all loads are at most \(c_q+1\) and put

\[
 T_q=\{S:\eta_{q,S}=c_q+1\}.
 \tag{6.6}
\]

Relative to the constant vector \(c_q\mathbf1\), (6.2) gives

\[
 |T_q|-\mathfrak D_q^-(G)
 =\rho_q-nb.
 \tag{6.7}
\]

A balanced high set of size \(\rho_q\) dominates \(\eta_q\) exactly when
it contains \(T_q\).  Such a set exists precisely when

\[
 |T_q|\le\rho_q,
 \tag{6.8}
\]

which is equivalent by (6.7) to
\(\mathfrak D_q^-(G)\le nb\).  The maximum-load condition is plainly
necessary.  \(\square\)

For \(m\ge3\), at depth one \(c_1=1\).  Under the necessary condition
\(\eta_{1,S}\le2\), the floor deficit is simply the number \(Z\) of
zero-loaded first-shadow targets.  Therefore

\[
 \boxed{
 G\text{ is depth-one quota-safe}
 \iff
 \max_S\eta_{1,S}\le2\text{ and }Z\le nb.
 }
 \tag{6.9}
\]

At the target \(b=o(t/\sqrt m)\), this permits no triple load and only
\(o(W/\sqrt m)\) holes.  A generic almost-perfect middle matching provides
neither property.

If \(G\subseteq F\) for an exact factor, its complement
\(B=F\setminus G\) is automatically the required exact completion, and
Theorem 6.1 is simply the integral packet criterion in a different form.
If \(G\) is constructed in the ambient candidate hypergraph, the numerical
conditions (6.5) do **not** imply that its uncovered middle vertices are a
union of \(b\) wreaths.  Exact residual completion remains a separate
hypothesis.

Theorem 6.1 concerns arbitrary balanced quota sets.  It does not impose a
point-regular, nested, or common labelled resolution on those sets; adding
such synchronization would be strictly stronger than the present
unlabelled MWB gate.

## 7. Exact star codegrees and the conditioning dichotomy

Let \(\mathcal H_m\) be the unoriented candidate-wreath hypergraph on the
middle \(m\)-sets.  Its candidate and degree counts are

\[
 |\mathcal E(\mathcal H_m)|=\frac{(n-1)!}{2}=tD_m,
 \qquad
 D_m=\frac{m!(m+1)!}{2}.
 \tag{7.1}
\]

Every middle vertex has degree \(D_m\).  For distinct middle sets \(A,B\),
write

\[
 d=|A\setminus B|=|B\setminus A|\in\{1,\ldots,m\}.
 \tag{7.2}
\]

Collapsing the common and alternating blocks in a cyclic order gives

\[
 D_m(A,B)=d!^2(m-d)!(m+1-d)!,
 \tag{7.3}
\]

and therefore

\[
 \boxed{
 \frac{D_m(A,B)}{D_m}
 =\frac{2}{\binom md\binom{m+1}d}.
 }
 \tag{7.4}
\]

Fix a coordinate \(v\), and let \(P_v\) and \(Q_v\) be the middle sets
containing and omitting \(v\).  Then

\[
 |P_v|=mt,\qquad |Q_v|=(m+1)t,
 \tag{7.5}
\]

and every wreath contains \(m\) vertices of \(P_v\) and \(m+1\) vertices
of \(Q_v\).  On \(P_v\), distinct sets have \(d\le m-1\), so

\[
 \boxed{
 \max_{A\ne B\in P_v}\frac{D_m(A,B)}{D_m}
 =\frac{2}{m(m+1)}.
 }
 \tag{7.6}
\]

On the full middle layer, disjoint sets have \(d=m\), giving

\[
 \boxed{
 \max_{A\ne B}\frac{D_m(A,B)}{D_m}
 =\frac{2}{m+1}.
 }
 \tag{7.7}
\]

Such maximal pairs occur within \(Q_v\) and across \(P_v,Q_v\).  Thus the
full matching constraint loses one power of \(m\) relative to the projected
star calculation.

At lower depth \(q\), a fixed target has candidate degree

\[
 D_q^\downarrow
 =\frac{(m-q)!(m+q+1)!}{2}
 =\lambda_qD_m.
 \tag{7.8}
\]

For \(S\subset A\), \(|S|=m-q\), \(|A|=m\), block counting gives

\[
 \boxed{
 \frac{\operatorname{codeg}(A,S)}{D_m}
 =\frac{(m-q)!(q+1)!}{m!}
 =\frac{q+1}{\binom mq}.
 }
 \tag{7.9}
\]

At \(q=1\) this is \(2/m\).  If \(r=m-q\ge2\) and
\(T=S\setminus\{x\}\), then conditional on owning \(S\), the target \(T\)
is an interval exactly when \(x\) is one of the two endpoints, so

\[
 \boxed{
 \frac{\operatorname{codeg}(S,T)}{\deg(S)}
 =\frac2{m-q}.
 }
 \tag{7.10}
\]

Thus the augmented system has genuine \(\Theta(m^{-1})\) nested
correlations.  A candidate wreath uses

\[
 n(K+1)=\Theta_A(m^{3/2})
 \tag{7.11}
\]

middle-plus-lower resources.  Bounded packet rank after conditioning on a
factor is not bounded dependency in this ambient hypergraph.

### 7.1 Why the two useful facts do not compose automatically

There are two different incidence structures.

* **Before choosing \(F\).**  Equations (7.1)--(7.10) control the ambient
  candidate hypergraph.  A near-matching found there need not be
  \(Q_v\)-disjoint if only its \(P_v\)-projection was controlled, need not
  obey shallow capacities, and need not have an exactly factorable
  residual.

* **After choosing \(F\).**  Exact completion of \(F\setminus B\) by
  \(B\) is automatic.  But every middle vertex now has selected degree one.
  The packet LP depends on overlaps of selected rows on lower targets and on
  the owner cuts \(Z\subseteq F\); the ambient degree \(D_m\) and codegree
  ratios no longer control those overlaps.

In particular, the statement

\[
 \text{small }P_v\text{ codegree}
 +\text{ bounded packet rank}
 \Longrightarrow\text{ small packet cover}
 \tag{7.12}
\]

mixes statistics from opposite sides of the conditioning step and is
unsupported.

A full-hypergraph matching which saturates \(P_v\) has \(t\) rows and
automatically partitions all middle vertices, hence is an exact factor.
A matching only in the simple \(P_v\)-trace projection has two possible
lifts per trace; those binary choices can collide on \(Q_v\) and are not
independent inside the exact-factor fibre.

The symmetric candidate vector

\[
 u_E=\frac1{D_m}
 \tag{7.13}
\]

is a fractional perfect middle matching.  It even lies in the convex hull
of exact factors: for any exact factor \(F_0\),

\[
 \boxed{
 u=\frac1{|S_n|}\sum_{\sigma\in S_n}\mathbf1_{\sigma F_0}.
 }
 \tag{7.14}
\]

Indeed, transitivity makes the probability that a fixed candidate occurs
in \(\sigma F_0\) equal to
\(t/(tD_m)=1/D_m\).  But coordinate relabelling leaves
\(\vartheta_A(F_0)\) unchanged.  Thus the perfectly regular average can
hide exactly the same packet obstruction in every integral summand.

## 8. What symmetric and local alteration cannot do

Let \(\mathsf A_q\) be the candidate-to-depth-\(q\) incidence matrix.  Every
candidate column has exactly \(n\) ones, and for the uniform vector (7.13),

\[
 \mathsf A_q u=\lambda_q\mathbf1.
 \tag{8.1}
\]

Write

\[
 \lambda_q=c_q+\xi_q,
 \qquad
 \xi_q=\frac{\rho_q}{N_q}\in[0,1).
 \tag{8.2}
\]

### Theorem 8.1 -- macroscopic fractional symmetry breaking

Let \(z\ge0\) be any fractional candidate family of total mass \(t-b\), and
suppose that, for some balanced quota \(\beta_q\),

\[
 \mathsf A_qz\le\beta_q.
 \tag{8.3}
\]

Then

\[
 \boxed{
 \|z-u\|_1
 \ge
 \max\left\{
 b,
 \frac{2t}{\lambda_q}\xi_q(1-\xi_q)-b
 \right\}.
 }
 \tag{8.4}
\]

Let

\[
 \alpha=1-\frac bt,
 \qquad u_\alpha=\alpha u,
 \tag{8.5}
\]

so that \(z\) and \(u_\alpha\) have equal mass.  The sharper same-mass
bound is

\[
 \boxed{
 \|z-u_\alpha\|_1
 \ge
 \frac{2t}{\lambda_q}(1-\xi_q)
       (\alpha\lambda_q-c_q)_+
 =\left[
 \frac{2t}{\lambda_q}\xi_q(1-\xi_q)
 -2b(1-\xi_q)
 \right]_+.
 }
 \tag{8.6}
\]

#### Proof

The balanced vector differs from the constant vector
\(\lambda_q\mathbf1\) by \(\xi_q\) on the
\(N_q-\rho_q\) floor cells and by \(1-\xi_q\) on the \(\rho_q\) high
cells.  Hence

\[
 \|\lambda_q\mathbf1-\beta_q\|_1
 =2N_q\xi_q(1-\xi_q).
 \tag{8.7}
\]

The domination in (8.3), together with the total masses, gives

\[
 \|\beta_q-\mathsf A_qz\|_1
 =W-n(t-b)=nb.
 \tag{8.8}
\]

Every column of \(\mathsf A_q\) has \(\ell^1\)-norm \(n\).  The triangle
inequality therefore gives

\[
\begin{aligned}
 n\|z-u\|_1
 &\ge\|\mathsf A_q(z-u)\|_1\\
 &\ge2N_q\xi_q(1-\xi_q)-nb.
\end{aligned}
 \tag{8.9}
\]

Since \(N_q/n=t/\lambda_q\), this proves the second entry in the maximum
in (8.4).  The first is the elementary mass bound
\(\|z-u\|_1\ge|\sum_E(z_E-u_E)|=b\).

For (8.6), consider the \(N_q(1-\xi_q)\) floor cells.  On each of them

\[
 (\mathsf A_q u_\alpha)(S)=\alpha\lambda_q,
 \qquad
 (\mathsf A_qz)(S)\le c_q.
 \tag{8.10}
\]

The vector \(\mathsf A_q(z-u_\alpha)\) has coordinate sum zero, so its
full \(\ell^1\)-norm is twice its positive, equivalently twice its negative,
mass.  The floor cells alone supply negative mass at least

\[
 N_q(1-\xi_q)(\alpha\lambda_q-c_q)_+.
 \tag{8.11}
\]

Divide twice (8.11) by the column norm \(n\), then substitute
\(\alpha=1-b/t\).  \(\square\)

For every fixed \(A>0\), choose

\[
 x_A=\min\left\{\frac A2,\sqrt{\log(3/2)}\right\},
 \qquad
 q_m=\lfloor x_A\sqrt m\rfloor,
 \qquad
 \delta_A=e^{x_A^2}-1>0.
 \tag{8.12}
\]

Then \(q_m\le K_A\).  Taylor expansion of the exact product (1.11),
uniformly for \(q=O_A(\sqrt m)\), gives

\[
 \log\lambda_q
 =\frac{q(q+1)}m+O_A(m^{-1/2}).
 \tag{8.12a}
\]

Indeed, the linear terms sum to \(q(q+1)/m\), while replacing
\((m-i)^{-1}\) by \(m^{-1}\) and summing the quadratic Taylor remainders
costs \(O_A(q^3/m^2)=O_A(m^{-1/2})\).  Hence

\[
 \lambda_{q_m}\longrightarrow e^{x_A^2}=1+\delta_A\le\frac32.
 \tag{8.13}
\]

For all sufficiently large \(m\), \(c_{q_m}=1\), and continuity in (8.4)
gives the explicit safe bound

\[
 \|z-u\|_1\ge\frac{\delta_A}{7}t-b.
 \tag{8.14}
\]

If \(b=o_A(t/\sqrt m)\), (8.6) also gives

\[
 \boxed{\|z-u_\alpha\|_1=\Omega_A(t).}
 \tag{8.15}
\]

Thus a quota-safe fractional near-factor cannot be an \(o(t)\)
redistribution of the symmetric star point.  This is a perturbative no-go,
not an integrality obstruction: every integral exact factor is already at
\(\ell^1\)-distance \(2t(1-o(1))\) from \(u\).

For the scalar thinning \(z=\alpha u\), one obtains the still simpler
pointwise obstruction.  A floor cell requires

\[
 \alpha\lambda_q\le c_q,
 \tag{8.16}
\]

so at the depth (8.12),

\[
 \frac bt=1-\alpha
 \ge1-\frac{c_q}{\lambda_q}
 =\frac{\xi_q}{\lambda_q}
 =\Omega_A(1).
 \tag{8.17}
\]

Uniform fractional thinning therefore loses linear mass on every
nontrivial fixed Gaussian window.

### 8.1 Random deletion inside one fixed exact factor

Suppose \(B\subseteq F\) is random and is quota-safe almost surely for one
fixed quota system.  Put

\[
 x_E=\Pr(E\in B).
 \tag{8.18}
\]

Every realization meets every survival packet, hence, for each packet,

\[
 \sum_{E\in P}x_E
 =\mathbb E|B\cap P|\ge1.
 \tag{8.19}
\]

Thus the marginal vector is a fractional packet cover and

\[
 \mathbb E|B|=\|x\|_1\ge\vartheta(F,\beta).
 \tag{8.20}
\]

Conversely, deterministic thresholding of a fractional cover produces a
safe deletion set of size at most \(R_A\|x\|_1\).  Therefore every random
or dependent scheme whose output is a deletion set \(B\subseteq F\) inside
one fixed factor and under one fixed quota system is equivalent, within
\(R_A\), to the packet LP itself.  It cannot evade a feasible packet
packing.  This does not cover a trajectory which changes the ambient factor
by twin switches.  If the quota system is random too, this argument
must be conditioned on the selected quota; averaging marginals across
different packet systems is invalid.

There is an elementary manifestation of the same fact.  If
\(x_E<1/R_A\) on every row, no packet can have total weight one.  Every
target-small fractional solution must therefore be concentrated on a
target-small deterministic heavy-row cover.  Bounded packet rank helps
integrality precisely because it forbids a diffuse small-marginal cover.

### 8.2 One-shot independent candidate alteration has linear loss

This subsection concerns a failed ambient construction and makes no
exact-factor claim.  Sample every candidate wreath independently with

\[
 pD_m\longrightarrow1.
 \tag{8.21}
\]

The expected number selected is \((1+o(1))t\).

Let \(U\) be the number of middle vertices contained in at least one
selected candidate.  A middle vertex has candidate degree \(D_m\), so

\[
 \mathbb EU
 =W\left(1-(1-p)^{D_m}\right)
 =(1-e^{-1}+o(1))W.
 \tag{8.22}
\]

Any matching extracted only by deletion has at most \(U/n\) rows.
Moreover \(U\) is concentrated at its mean.  Resampling one candidate
indicator changes \(U\) by at most \(n\), and it differs from its old value
with probability at most \(2p\).  Efron--Stein therefore gives

\[
 \operatorname{Var}U
 \le |\mathcal E(\mathcal H_m)|pn^2
 =(1+o(1))tn^2=(1+o(1))nW=o(W^2).
 \tag{8.23}
\]

Hence, with probability tending to one,

\[
 \boxed{
 \text{every deletion-only extracted matching has at most }
 (1-e^{-1}+o(1))t\text{ rows}.
 }
 \tag{8.24}
\]

There is an independent ceiling-two loss.  For \(m\ge3\), at depth one and
for a fixed target,

\[
 X_S\sim\operatorname{Bin}(\lambda_1D_m,p)
 \Longrightarrow\operatorname{Poisson}(1).
 \tag{8.25}
\]

Put

\[
 \mathcal V=\sum_S(X_S-2)_+.
 \tag{8.26}
\]

Then

\[
\begin{aligned}
 \mathbb E\mathcal V
 &=N_1\left(\mathbb E(\operatorname{Poisson}(1)-2)_++o(1)\right)\\
 &=\left(\frac3e-1+o(1)\right)W.
\end{aligned}
 \tag{8.27}
\]

The identity in the second line follows from

\[
 \mathbb E(X-2)_+
 =\mathbb EX-\Pr(X\ge1)-\Pr(X\ge2)
 =1-(1-e^{-1})-(1-2e^{-1}).
 \tag{8.28}
\]

Resampling a candidate changes \(\mathcal V\) by at most \(n\), so the
same variance argument gives
\(\operatorname{Var}\mathcal V=O(tn^2)=O(nW)=o(W^2)\).  Deleting one
selected wreath can lower \(\mathcal V\) by at most \(n\).  Since every
balanced first-shadow quota has ceiling two, any deletion-only repair which
even enforces this necessary ceiling therefore removes at least

\[
 \boxed{\left(\frac3e-1-o(1)\right)t}
 \tag{8.29}
\]

rows with probability tending to one.  Scarcity of the high quota slots
can only strengthen this ceiling-only obstruction.

The losses (8.24) and (8.29) are not additive.  They rule out one-shot
Bernoulli selection followed only by deletion.  They do not rule out a
staged, globally dependent exact-factor construction.

## 9. A macroscopic compatible-pair covariance requirement

The next theorem isolates what such a globally dependent construction must
do already at depth one.

Assume \(m\ge3\).  Let \(G\) be a quota-safe matching of exactly \(t-b\)
candidate wreaths.  In the intended application \(G\subseteq F\) for an
exact factor, so it has an
exact completion.  Apply a uniformly random coordinate permutation jointly
to \(G\) and its balanced quota.  Denote the resulting random matching by
\(\mathbf G\), and put

\[
 \alpha=1-\frac bt,
 \qquad D=D_m,
 \qquad p=\frac\alpha D.
 \tag{9.1}
\]

Transitivity gives \(\Pr(E\in\mathbf G)=p\) for every candidate wreath.
For a first-shadow target \(S\), let \(\mathscr O_S\) be its ambient
candidate-owner family.  Then

\[
 |\mathscr O_S|=\lambda_1D,
 \qquad
 \lambda_1=\frac{m+2}{m}.
 \tag{9.2}
\]

Define the independent-marginal collision benchmark

\[
 I:=
 \sum_S\sum_{\{E,E'\}\subset\mathscr O_S}p^2
 =p^2N_1\binom{\lambda_1D}{2}
 =\frac{\alpha^2W}{2}
   \left(\lambda_1-\frac1D\right).
 \tag{9.3}
\]

Define the multiplicity-weighted aggregate covariance deficit

\[
 \Gamma:=
 \sum_S\sum_{\{E,E'\}\subset\mathscr O_S}
 \left[p^2-\Pr(E,E'\in\mathbf G)\right].
 \tag{9.4}
\]

### Theorem 9.1 -- compatible-pair anti-correlation is macroscopic

For every quota-safe \(G\) above,

\[
 \boxed{
 \Gamma
 \ge W\left[
 \frac{\alpha^2}{2}\left(\lambda_1-\frac1D\right)
 -\frac2{m+2}
 \right].
 }
 \tag{9.5}
\]

Let \(\Gamma_{\rm comp}\) denote the part of (9.4) summed only over pairs
of candidate wreaths with disjoint middle supports.  Define

\[
 \chi_m
 :=\sum_{d=0}^{m-1}\frac{\nu_d^2}{M_d},
 \tag{9.6}
\]

where

\[
 M_d=\binom{m-1}{d}\binom{m+2}{d+1},
 \qquad
 \nu_d=
 \begin{cases}
 2,&0\le d\le m-2,\\
 3,&d=m-1.
 \end{cases}
 \tag{9.7}
\]

Then

\[
 \chi_m
 \le\frac4{m+2}
 +\frac{4m+1}{\binom{m+2}{2}}
 \le\frac{13}{m},
 \tag{9.8}
\]

and

\[
 \boxed{
 \Gamma_{\rm comp}
 \ge W\left[
 \frac{\alpha^2}{2}
 \left(\lambda_1-\frac1D-\lambda_1\chi_m\right)
 -\frac2{m+2}
 \right].
 }
 \tag{9.9}
\]

In particular, if \(b=o(t)\), and hence in the FSP target regime, then

\[
 \boxed{
 \Gamma_{\rm comp}=(1/2-o(1))W.
 }
 \tag{9.10}
\]

#### Proof: total covariance deficit

Quota safety at depth one implies every load is at most two and at most
\(\rho_1=2W/(m+2)\) targets have load two.  Therefore, pointwise in the
random outcome,

\[
 \sum_S\binom{\mu_1^{\mathbf G}(S)}2\le\rho_1.
 \tag{9.11}
\]

The left side is also the number of selected coowner pairs, with a pair
counted once for every common target.  Taking expectations in (9.11) and
subtracting from (9.3) proves (9.5).

#### Proof: middle-conflict contribution

Fix \(S\in\binom{[n]}{m-1}\), and choose a candidate wreath uniformly
conditioned on owning \(S\).  Put the positions of \(S\) in one cyclic
block.  For a middle window \(A\), let

\[
 d=|S\setminus A|.
 \tag{9.12}
\]

There are exactly

\[
 M_d=\binom{m-1}{d}\binom{m+2}{d+1}
 \tag{9.13}
\]

middle sets of class \(d\).  Sliding an \(m\)-window around the circle
shows that one conditioned wreath contains two such windows for every
\(0\le d\le m-2\).  For \(d=m-1\), the middle window is disjoint from
\(S\); there are three placements inside the complementary block of length
\(m+2\).  This proves the values \(\nu_d\) in (9.7), whose sum is
\(2(m-1)+3=n\).

The stabilizer of \(S\) is transitive on the middle sets in each class.
Thus a fixed \(A\) in class \(d\) belongs to the conditioned candidate with
probability

\[
 \frac{\nu_d}{M_d}.
 \tag{9.14}
\]

For two independent uniform conditioned owners, the expected number of
common middle vertices is therefore exactly

\[
 \sum_dM_d\left(\frac{\nu_d}{M_d}\right)^2
 =\chi_m.
 \tag{9.15}
\]

The probability of any middle conflict is at most this expectation.  For
\(d=0\), the contribution in (9.15) is \(4/(m+2)\).  For
\(1\le d\le m-2\), use
\(M_d\ge\binom{m+2}{2}\); the endpoint contributes
\(9/\binom{m+2}{2}\).  This gives the first inequality in (9.8); the second
is elementary cross multiplication.

Counting conditioned ordered pairs with replacement, then dividing by two,
only enlarges the number of distinct unordered conflicting pairs.  Hence
their total independent \(p^2\)-mass, summed over \(S\), is at most

\[
 \frac12N_1p^2(\lambda_1D)^2\chi_m
 =\frac{\alpha^2W\lambda_1\chi_m}{2}
 =O(W/m).
 \tag{9.16}
\]

Since a matching selects no middle-conflicting pair, (9.16) is their entire
contribution to \(\Gamma\).  Subtracting (9.16) from (9.5) proves (9.9).
Finally \(D\to\infty\), \(\lambda_1\to1\), \(\chi_m\to0\),
\(\rho_1/W\to0\), and \(\alpha\to1\).  The matching lower bound in
(9.9), together with the trivial upper bound
\(\Gamma_{\rm comp}\le I=(1/2+o(1))W\), proves (9.10).  \(\square\)

Equation (9.10) is an aggregate statement with shared-target multiplicity.
Individual compatible pairs may have covariance of either sign.  It says
that any uniform-marginal distribution supported on successful near-factors
must impose \(\Omega(W)\) net negative covariance on pairs which are not
forbidden by middle matching.  Ordinary conflict suppression contributes
only \(O(W/m)\).

This requirement is not a contradiction: symmetrizing a genuinely good
deterministic exact core would exhibit exactly those correlations.  It does
rule out a rounding law whose compatible-pair covariance deficit is
\(o(W)\), and it explains quantitatively why local star codegrees alone do
not create the required quota balance.

## 10. The compressed-cut no-go criterion and what point margins miss

The score packing in Theorem 3.1 spreads mass uniformly within every
resource.  The compressed dual also supports a more combinatorial
bounded-congestion obstruction.

Let \(\mathcal A\) be any family of active resources, with owner sets
\(\mathcal O_a\) and packet sizes \(k_a\).  For
\(\mathcal X\subseteq\mathcal A\), put

\[
 d_{\mathcal X}(E)
 =\#\{a\in\mathcal X:E\in\mathcal O_a\}.
 \tag{10.1}
\]

### Theorem 10.1 -- exact bounded-congestion packet selection

There are packets

\[
 P_a\subseteq\mathcal O_a,
 \qquad |P_a|=k_a\qquad(a\in\mathcal A),
 \tag{10.2}
\]

such that every wreath belongs to at most a positive integer \(D\) selected packets if and only
if, for every \(\mathcal X\subseteq\mathcal A\),

\[
 \boxed{
 \sum_{a\in\mathcal X}k_a
 \le
 \sum_{E\in F}\min\{D,d_{\mathcal X}(E)\}.
 }
 \tag{10.3}
\]

Whenever (10.3) holds,

\[
 \boxed{
 \vartheta(F,\beta)\ge\frac{|\mathcal A|}{D}.
 }
 \tag{10.4}
\]

#### Proof

Build a bipartite flow network.  Every resource \(a\) has integral demand
\(k_a\); every incidence \(aE\), \(E\in\mathcal O_a\), has capacity one;
and every wreath has capacity \(D\).  The max-flow/min-cut theorem and
integrality give (10.2) exactly when all resource-set cuts have enough
wreath capacity.  More explicitly, for resource side
\(\mathcal X\subseteq\mathcal A\) and owner side \(Z\subseteq F\), the cut
condition is

\[
 \sum_{a\in\mathcal X}k_a
 \le D|Z|+e(\mathcal X,F\setminus Z).
 \tag{10.3a}
\]

For fixed \(\mathcal X\), minimizing the right side owner by owner places
\(E\) in \(Z\) exactly when capacity \(D\) is no larger than its
\(d_{\mathcal X}(E)\) incident arcs.  The minimum is therefore
\(\sum_E\min(D,d_{\mathcal X}(E))\), yielding (10.3).

If the packets are selected, give each dual weight \(1/D\).  Wreath
congestion is at most one, and the objective is \(|\mathcal A|/D\), proving
(10.4).  \(\square\)

The case \(D=1\) is a disjoint-packet matching and recovers the lower side
of Theorem 2.1.  More generally, (10.3) identifies the missing owner
expansion theorem.  To prove a factor-independent \(\Omega(t)\) obstruction
through this route, one would need \(\Omega(Dt)\) active resources admitting
such a selection with \(D=O_A(1)\), or a comparably strong fractional
compressed-cut packing.  Bounded packet **rank** alone says nothing about
the owner congestion \(D\).

### 10.1 A universal one-depth packing and its exact quota optimization

For completeness, the score lower bound can be written directly as a
compressed-dual certificate.  At one depth put, for every active resource,

\[
 Y_{q,S}=\frac{h_{q,S}}{nk_{q,S}}.
 \tag{10.5}
\]

Its induced owner load is exactly \(1/n\), and a wreath owns only \(n\)
resources at that depth.  Hence

\[
 \boxed{
 \vartheta(F,\beta)
 \ge\frac1n\sum_{S:h_{q,S}\ge k_{q,S}}
              \frac{h_{q,S}}{k_{q,S}}.
 }
 \tag{10.6}
\]

Optimizing the high set gives \(L_q^*/n\), with the exact top-benefit
formula (3.12).  A quota-uniform but weaker consequence is

\[
 \vartheta_A(F)
 \ge\frac1n
 \left(
 \#\{S:h_{q,S}\ge c_q+2\}
 +\bigl(\#\{S:h_{q,S}=c_q+1\}-\rho_q\bigr)_+
 \right).
 \tag{10.7}
\]

Indeed, loads at least \(c_q+2\) violate either quota, while only
\(\rho_q\) marginal \((c_q+1)\)-loads can be protected.  Every contributing
active resource has \(h/k\ge1\).

Equations (10.6)--(10.7) prove an \(\Omega(t)\) no-go whenever one depth has
\(\Omega(W)\) quota-unavoidable violating resources or score.  No current
identity forces this for every exact factor.

### 10.2 Point margins are exactly blind to owner cuts

Let \(a_{E,q}\) be the rank-\((m-q)\) target-incidence vector of one wreath,
and let \(U_{m-q}\) be the point-incidence operator.  Among the \(n\) cyclic
intervals of length \(r=m-q\), each coordinate occurs exactly \(r\) times.
Thus

\[
 \boxed{U_ra_{E,q}=r\mathbf1.}
 \tag{10.8}
\]

For every owner subset \(Z\subseteq F\),

\[
 \boxed{
 U_r\sum_{E\in Z}a_{E,q}=r|Z|\mathbf1.
 }
 \tag{10.9}
\]

All owner subsets of the same cardinality therefore have identical point
projection.  The decisive coefficient in (1.10), however, depends on the
full targetwise vector through

\[
 |\mathcal O_{q,S}\setminus Z|
 =h_{q,S}-\sum_{E\in Z}a_{E,q}(S).
 \tag{10.10}
\]

Point margins cannot distinguish a dispersed packet family from one whose
every packet passes through a tiny exceptional row set.  They cannot prove
(10.3), bound maximum packet matchings, or control the compressed cuts.

There is an exact formal witness to this blindness.  The integer

\[
 d_q^*:=\frac{(m-q)\rho_q}{n}
 \tag{10.11}
\]

is integral because

\[
 \frac{(m-q)\rho_q}{n}
 =(m-q)t-c_q\binom{n-1}{m-q-1}.
 \tag{10.12}
\]

There exists a family

\[
 \mathcal R_q\subseteq\binom{[n]}{m-q},
 \qquad |\mathcal R_q|=\rho_q,
 \tag{10.13}
\]

of constant point degree \(d_q^*\).  One direct proof starts with any
\(\rho_q\)-set family.  If point \(x\) is overfull and point \(y\) is
underfull, some member containing \(x\) and omitting \(y\) can be exchanged
from \(x\) to \(y\) without duplicating a member; otherwise the exchange
map would inject all such \(x\)-members into the corresponding
\(y\)-members, contradicting the degree inequality.  Each exchange reduces
the positive degree discrepancy, so the process terminates at regularity.

The formal load profile

\[
 \mu_q^\circ(S)=c_q+\mathbf1_{\mathcal R_q}(S)
 \tag{10.14}
\]

satisfies

\[
 \sum_S\mu_q^\circ(S)=W,
 \qquad
 U_r\mu_q^\circ=(m-q)t\mathbf1,
 \tag{10.15}
\]

and is itself balanced, so its histogram-level overcapacity obstruction is
zero; no owner hypergraph is asserted here.  Such
profiles may be chosen separately at every controlled rank.  What is not
constructed is a positive exact factor realizing them simultaneously with
common owners.  Therefore (10.14) refutes only a no-go based on rankwise
total and point moments; it is not a signed-relaxation substitute for an
exact factor.

An already audited explicit \(m=4\) exact factor realizes a perfectly
balanced first shadow, so even positivity permits zero depth-one packet
mass in a nontrivial finite dimension.  This finite witness is not an
asymptotic construction, but it excludes a universal parity or local
first-moment obstruction.

## 11. Positive-density obstructions beyond one canonical point

The score theorem already gives the general edit basin (4.16).  There is
also a much more structured packet matching around the canonical MSW
factor.

Let \(F_m^{\rm MSW}\) be the canonical exact factor and define \(L_m\) by

\[
 \boxed{
 \sum_{m\ge0}L_mz^m
 =\frac{z^4C(z)}
 {1-(1+z^2)(zC(z)-z^2-2z^4)},
 \qquad
 C(z)=\frac{1-\sqrt{1-4z}}{2z}.
 }
 \tag{11.1}
\]

The suspended first-occurrence construction in
`FRACTIONAL_PACKET_GLOBAL_SEED_MATCHING_20260725.md` gives \(L_m\)
pairwise row-disjoint depth-one survival packets for every balanced quota.
Briefly, the three semilength-four seed blocks

\[
 A=11110000,\qquad B=11101000,\qquad D=1100,
 \qquad DD=D\,D=11001100,
 \tag{11.2}
\]

have a common internal first-shadow colour.  In the primitive Dyck-component
factorization, choose a prefix containing no earlier \(A\), \(B\), or
consecutive \(DD\), and not ending in \(D\).  The first active occurrence
then uniquely decodes the prefix, the chosen seed, and the suffix.  Hence
the resulting owner triples are disjoint.

If \(E(z)=zC(z)-z^2-2z^4\) is the series for the other primitive
components, the clean-prefix series is

\[
 U_0(z)=\frac1{1-(1+z^2)E(z)}.
 \tag{11.3}
\]

Multiplication by the active semilength-four block and an arbitrary Dyck
suffix gives (11.1).  The denominator is nonzero at \(z=1/4\); expanding in
\(s=\sqrt{1-4z}\) yields

\[
 \boxed{
 \frac{L_m}{t}\longrightarrow
 \delta_{\rm seed}
 :=\frac{17608}{1238769}
 \approx0.014214.
 }
 \tag{11.4}
\]

Let the row distance between equal-size factors be

\[
 d(F,F')=|F\setminus F'|=|F'\setminus F|.
 \tag{11.5}
\]

Deleting one canonical row destroys at most one member of the disjoint
packet matching.  New rows cannot destroy an intact packet.  Therefore,
for every exact factor \(F\) and every balanced quota system containing
depth one,

\[
 \boxed{
 \nu(F,\beta)\ge
 \bigl(L_m-d(F,F_m^{\rm MSW})\bigr)_+,
 }
 \tag{11.6}
\]

and hence

\[
 \boxed{
 \vartheta(F,\beta)\ge
 \bigl(L_m-d(F,F_m^{\rm MSW})\bigr)_+.
 }
 \tag{11.7}
\]

Thus every factor satisfying FSP must replace at least

\[
 (\delta_{\rm seed}-o(1))t
 \tag{11.8}
\]

canonical rows.  This is a genuine positive-radius obstruction in the exact
factor fibre, not merely a statement about the canonical representative.

For the first explicitly rebundled factor \(F_m^\dagger\),

\[
 d(F_m^\dagger,F_m^{\rm MSW})=2\operatorname{Cat}_{m-4},
 \tag{11.9}
\]

so

\[
 \vartheta(F_m^\dagger,\beta)
 \ge\bigl(L_m-2\operatorname{Cat}_{m-4}\bigr)_+,
 \tag{11.10}
\]

with limiting normalized lower bound

\[
 \delta_{\rm seed}-\frac1{128}
 =\frac{1015055}{158562432}
 \approx0.006402.
 \tag{11.11}
\]

Independently, the audited primitive-prefix packet matching gives the
simpler exact lower bound \(\operatorname{Cat}_{m-4}\) for the canonical
factor and survives arbitrary canonical-row deletion one for one.  It also
proves \(\Omega(t)\) packet mass for every rebundling supported on bounded
Dyck-prefix cylinders.  These results show that those bounded-prefix-
cylinder rebundlings and subcritical total perturbations cannot construct
FSP.  They do not rule out bounded-size trades applied at positive density.

They do **not** prove a universal obstruction.  A successful factor may lie
farther than \(\delta_{\rm seed}t\) from the canonical factor and may destroy
the entire suspended-seed matching.

## 12. Final constructive/no-go theorem and remaining gap

The preceding results can be summarized without any relaxation outside one
factor.

### Theorem 12.1 -- fixed-window support-feasible dichotomy

Fix \(A>0\), let \(m\to\infty\), and let \((F_m,\beta_m)\) be any sequence
of exact factors with balanced quotas through \(K_A\).  Let \(\nu_m\) be
the maximum disjoint survival-packet matching number.

1. If
   \[
     \nu_m=o_A(t/\sqrt m),
     \tag{12.1}
   \]
   then the union of a maximal packet matching is a quota-safe deletion set
   of size \(o_A(t/\sqrt m)\).  Its complement is an exactly completable
   quota-safe near-factor, and the fixed-\(A\) hard-quota implication
   follows.  If this construction is available for every fixed \(A\), the
   audited diagonal implication to MWB follows.

2. If
   \[
     \nu_m=\Omega_A(t),
     \tag{12.2}
   \]
   then
   \[
     \vartheta(F_m,\beta_m)=\Omega_A(t),
     \tag{12.3}
   \]
   and no target-scale fractional cover or integral alteration exists for
   this prescribed quota system in this factor.  Another balanced quota
   system is not excluded by this clause alone.

3. Sufficient conditions for the **existence of a balanced quota system**
   \(\widehat\beta_m\) on the same factor \(F_m\), whose packet matching
   number satisfies (12.1), include
   \[
     \sum_{q\le K}L_q^*(F_m)=o_A(t/\sqrt m)
     \tag{12.4}
   \]
   or the stronger quadratic condition
   \[
     \sum_{q\le K}V_q(F_m)=o_A(t/\sqrt m).
     \tag{12.5}
   \]

4. Sufficient conditions for (12.2) include a linear disjoint packet
   packing in the packet system of the prescribed \(\beta_m\); or, in that
   same packet system, a resource family
   \(\mathcal A_m\) with \(|\mathcal A_m|=\Omega_A(t)\) satisfying (10.3)
   for some \(D=O_A(1)\); or one depth with
   \[
     L_q^*(F_m)=\Omega_A(W).
     \tag{12.6}
   \]

#### Proof

Parts 1 and 2 are Theorem 2.1 and exact packetization.  In Part 3, choose
the score-minimizing high set independently at every rank; Theorems 3.1 and
5.1 followed by (2.1) give (12.1) for that resulting
\(\widehat\beta_m\), not necessarily for the originally displayed
\(\beta_m\).  Part 4 follows from the packet-packing dual,
Theorem 10.1, and
\(\nu\ge\vartheta/R_A\ge L_q^*/(nR_A)\).  \(\square\)

The intermediate regime

\[
 t/\sqrt m\ll\nu_m\ll t
 \tag{12.7}
\]

is not decided by this dichotomy.  Nor has any exact factor sequence
satisfying (12.1), (12.4), or (12.5) been constructed.

### 12.1 The clean positive theorem target

The remaining positive statement may be expressed in any one of the
following equivalent or sufficient forms.

> **Unproved exact packet-matching theorem \(\mathrm{EPM}_A\).**  For every
> fixed \(A>0\) and all sufficiently large \(m\), there is an exact middle
> wreath factor \(F_{m,A}\) and a balanced quota system for all
> \(1\le q\le K_A=\lceil A\sqrt m\rceil\) such that the maximum number of pairwise row-disjoint
> survival packets is
> \[
>   o_A(\operatorname{Cat}_m/\sqrt m).
> \]

By Theorem 2.1, \(\mathrm{EPM}_A\) is equivalent to FSP at the target scale,
up to the explicit fixed constant \(R_A\).  It is wholly integral inside
one exact factor.

A stronger but pairwise-looking target is

> **Unproved quadratic exact-factor theorem \(\mathrm{QEF}_A\).**  There is
> an exact factor with
> \[
>  \sum_{q\le K_A}V_q(F)=o_A(\operatorname{Cat}_m/\sqrt m).
> \]

Theorem 5.1 proves \(\mathrm{QEF}_A\Rightarrow\mathrm{EPM}_A\).  The
covariance theorem shows that a symmetric dependent construction of such a
factor must generate \(\Omega(W)\) negative coowner covariance on compatible
rows; suppressing only middle conflicts is smaller by a factor \(m\).

### 12.2 The clean negative theorem target

The surviving universal obstruction would have to prove at least one of:

* every positive exact factor has \(L_q^*(F)=\Omega_A(W)\) at some
  controlled depth;
* every exact factor admits \(\Omega_A(t)\) disjoint survival packets for
  every balanced quota system;
* the owner incidence satisfies (10.3) with bounded \(D\) on linearly many
  resources;
* the separately balanced formal profiles (10.14) are incompatible across
  ranks in every positive common-owner exact factor, with a quantitative
  linear packet consequence.

None follows from point margins, the \(P_v\) codegree, the full middle
codegree, or bounded packet rank.  The current positive-density lower bounds
cover large exact edit basins but not the whole factor fibre.

## 13. Adversarial audit ledger

### 13.1 Proved in this report

1. The exact rank bound (1.12)--(1.13), with all fixed-\(A\) quantifiers.
2. The packet matching/cover sandwich
   \(\nu\le\vartheta\le\tau\le R_A\nu\), and its maximal-matching
   constructive deletion.
3. The score packing, explicit cover, and optimized sandwich (3.2).
4. The exact top-benefit quota formula (3.12).
5. The constant comparison \(O_q/R_A\le L_q^*\le O_q\), without assuming
   the two minima use the same high set.
6. The depth-one formula, lower bound, prebalance consequences, and general
   edit-basin theorem.
7. The parity-floor identity (5.7), the quadratic certificate
   \(V_q\ge O_q\), and the pair-energy representation.
8. The exact near-factor quota criterion (6.5), using the actual deletion
   count \(b\).
9. The ambient degree/codegree ledger and the exact conditioning dichotomy.
10. The full- and same-mass \(\ell^1\) symmetry-breaking bounds
    (8.4)--(8.6).
11. The equivalence, within \(R_A\), between any fixed-factor randomized
    safe deletion and the deterministic packet LP.
12. The one-shot Bernoulli middle-occupancy and ceiling-two alteration
    losses, including variance bounds sufficient for high probability.
13. The exact conditioned-owner class counts \(M_d,\nu_d\), the bound
    \(\chi_m\le13/m\), and the compatible covariance lower bound (9.9).
14. The integral bounded-congestion Hall criterion (10.3).
15. Exact blindness of point projections to owner cuts and the formal
    point-regular balanced profiles.
16. The imported suspended-seed matching and its exact edit robustness.

The score, quadratic, near-factor, and covariance calculations were
independently rederived by separate proof audits.  The decisive ordered/
unordered normalization in (9.3)--(9.16), including the diagonal
overcount in the conflict upper bound, was checked independently.

### 13.2 Scope caveats

1. A target-small **arbitrary** packet matching proves nothing; it is the
   maximum matching number, or any maximal matching together with an a
   priori upper bound on it, which yields the small cover.
2. Deleting the union of a maximal packet matching produces a quota-safe
   core inside the original factor.  It does not produce a second exact
   factor; exact completion is supplied by the deleted rows of the original
   partition.
3. The identities for \(O_q\) and \(V_q\) use the full-factor mass
   \(\sum_Sh_{q,S}=W\).  They are not to be copied unchanged to a deficient
   near-factor.
4. Theorem 6.1 permits independent balanced high sets at different ranks.
   It does not prove a labelled nested resolution.
5. The ambient fractional statements in Sections 7--9 are diagnostics.
   Only a matching contained in one exact factor, or a matching with an
   explicitly proved exact residual completion, enters the MWB implication.
6. The covariance deficit is multiplicity-weighted and aggregate.
   Individual compatible pairs may be positively correlated.
7. The one-shot random alteration theorem does not exclude a staged nibble;
   the codegree ledger shows only that no standard fixed-rank inference has
   been supplied for such a nibble.
8. The formal balanced profiles (10.14) are not positive exact factors.
   They prove insufficiency of first moments, not existence of FSP.
9. The suspended-seed theorem gives a positive-radius canonical basin, not
   a factor-independent obstruction.
10. No statement here upgrades unlabelled MWB to common-owner labelled
    synchronization.

### 13.3 Still unproved

1. \(\mathrm{EPM}_A\), FSP, or any constructive quota-safe near-factor at
   the required asymptotic leave.
2. \(\mathrm{QEF}_A\), or a dependent exact-factor rounding realizing its
   compatible-pair anticorrelations.
3. A residual-extension theorem for a near-matching built outside a fixed
   exact factor.
4. A bounded-congestion owner-expansion theorem strong enough to force a
   universal \(\Omega(t)\) dual packing.
5. A factor-fibre-wide \(\Omega(t)\) lower bound beyond the proved edit
   basins.

## 14. Final verdict

Bounded packet rank completely removes the final fractional/integral
alteration gap: a maximal disjoint packet family whose size is target-small
gives the quota-safe core directly.  The score theorem and compressed dual
then expose the real geometric demand.  A successful exact factor must be nearly balanced at
every individual shallow depth and must concentrate every remaining packet
through only \(o(t/\sqrt m)\) exceptional rows.

The ambient \(P_v\) codegree does not provide that concentration.  Uniform
or one-shot random rounding fails macroscopically, while any successful
symmetrized rounding must impose \((1/2-o(1))W\) negative covariance on
middle-disjoint coowner pairs.  This is the exact global correlation which
the star statistics omit.

Accordingly, the constructive route is reduced to the integral theorem
\(\mathrm{EPM}_A\), and the no-go route is reduced to a common-owner packet
expansion theorem.  The canonical and general high-score edit basins give
genuine \(\Omega(t)\) obstructions beyond a single representative, but no
universal obstruction has been proved.  The lane is exhausted at this
positive-support/common-owner gap.
