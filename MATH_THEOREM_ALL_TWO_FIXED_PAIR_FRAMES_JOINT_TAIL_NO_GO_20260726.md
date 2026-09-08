# Every two fixed-pair strip frames have a linear Gaussian two-copy deficit

Date: 2026-07-26

Method: pure mathematics.  No computation, search, solver, or probabilistic
construction is used.

## 0. Outcome

Let

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}.
\]

Take **arbitrary** perfect matchings \(\mathcal P_0,\mathcal P_1\) of the
\(2m\) physical coordinates.  On shore \(i\), let \(\mathcal F_i\) be
any middle-owner strip factor whose strip transitions flip endpoints only
inside pairs of \(\mathcal P_i\).  The two matchings may be disjoint, may
be a linear matching-switch distance apart, and the two factors may use
unrelated active faces, direction orders, and cycle resolutions.

For a selected lower depth-\(q\) port system, let \(k_i(T)\) be the
number of selected occurrences of the rank-\((m-q)\) target \(T\) on
shore \(i\), and put

\[
 r_T=k_0(T)+k_1(T),\qquad
 \mathfrak B_{2,q}^-=
   \sum_{T\in\binom{[2m]}{m-q}}|r_T-2|.             \tag{0.1}
\]

The main result is the uniform bound

\[
 \boxed{
 \mathfrak B_{2,\lfloor\sqrt m\rfloor}^-
 \ge \bigl(\kappa+o(1)\bigr)W,}                    \tag{0.2}
\]

where

\[
 \kappa=
 2\left[e^{-1}\bigl(2\Phi(1)-1\bigr)-\Phi(-1)\right]
 =0.1849843498\ldots>0.                              \tag{0.3}
\]

This is statewise and does not depend on the distance between
\(\mathcal P_0\) and \(\mathcal P_1\).  In particular, genuinely distant
or random pairings do not rescue the **two-copy balance certificate** for
a two-shore fixed-pair construction.

More generally, if \(q=c\sqrt m+o(\sqrt m)\), then for every fixed real
\(t\),

\[
 \boxed{
 \liminf_{m\to\infty}{\mathfrak B_{2,q}^-\over W}
 \ge
 2\left[
 e^{-c^2}\bigl(2\Phi(t+2c)-1\bigr)-\Phi(t)
 \right]_+.}                                        \tag{0.4}
\]

After overlaying the two factors into support-matched packets, the
two-occurrence targets still form the usual signed frustration graph
\(G\).  Since its frustration index is nonnegative, (0.2) immediately
gives

\[
 \boxed{
 \mathfrak B_2+\tau(G)\ge(\kappa+o(1))W.}           \tag{0.5}
\]

Thus every pair of fixed-pair frames fails the sufficient gate
\(\mathfrak B_2+\tau(G)=o(W)\) **before** signed frustration becomes
relevant.  This extends the same-frame orbit obstruction and the local
matching-switch transport obstruction to all two-frame pairs at once.  It
does not rule out a qualitatively different, highly anchored two-shore CSP
whose catalogue deliberately has linear two-copy imbalance.

The theorem does not cover a physical strip factor whose transitions are
not confined to one perfect matching, such as a still-hypothetical
globally cross-box product-SCD factor.  Section 5 records the exact
abstract conserved-statistic criterion which such a factor would have to
evade.

## 1. The matching-type census

For a perfect matching \(\mathcal P\) and a set \(S\subseteq[2m]\), let

\[
 f_{\mathcal P}(S)
 =\#\{e\in\mathcal P:e\subseteq S\}.                \tag{1.1}
\]

The number of rank-\((m-q)\) targets of type \(f\) is

\[
 T_{f,q}
 =\frac{m!\,2^{m-2f-q}}
        {f!(f+q)!(m-2f-q)!},                        \tag{1.2}
\]

and the number of middle owners of type \(f\) is

\[
 V_f=T_{f,0}
 =\frac{m!\,2^{m-2f}}
        {f!^2(m-2f)!}.                              \tag{1.3}
\]

These counts do not depend on the matching.  Put

\[
 T_{\le a,q}=\sum_{f\le a}T_{f,q},\qquad
 V_{\le a}=\sum_{f\le a}V_f.                       \tag{1.4}
\]

### Lemma 1.1 (uniform matching CLT)

Let \(R_r\) be a uniformly random \(r\)-subset of \([2m]\), where
\(r=m+O(\sqrt m)\).  For every fixed perfect matching \(\mathcal P\),

\[
 \frac{f_{\mathcal P}(R_r)-\mu_r}{\sqrt m/4}
 \Longrightarrow N(0,1),\qquad
 \mu_r=\frac{r(r-1)}{2(2m-1)}.                    \tag{1.5}
\]

The convergence is uniform over \(r=m+O(\sqrt m)\) and over the choice
of \(\mathcal P\).

#### Proof

Write \(F=f_{\mathcal P}(R_r)\).  For every fixed \(j\), choosing an
ordered \(j\)-tuple of distinct matching edges gives the exact factorial
moment

\[
 \mathbb E(F)_j=(m)_j\frac{(r)_{2j}}{(2m)_{2j}}.    \tag{1.6}
\]

In particular,

\[
 \mathbb EF=\mu_r,qquad
 \operatorname {Var}F=\frac m{16}+O(\sqrt m).      \tag{1.7}
\]

Expanding the factorial cumulants from (1.6), the \(j\)-th ordinary
cumulant is \(O(m)\) for every fixed \(j\ge2\), uniformly in the stated
range of \(r\).  After division by \((\sqrt m/4)^j\), every cumulant of
order \(j\ge3\) tends to zero, while the second tends to one.  The method
of moments proves (1.5).  All formulas are invariant under relabelling of
the perfect matching, giving the asserted uniformity. \(\square\)

For later reference, if \(q=c\sqrt m+o(\sqrt m)\), then

\[
 \frac{N_q}{W}\longrightarrow e^{-c^2},            \tag{1.8}
\]

and

\[
 \frac{\mu_m-\mu_{m-q}}{\sqrt m/4}
 \longrightarrow2c.                                \tag{1.9}
\]

For fixed \(t\), set

\[
 a_m(t)=\left\lfloor\mu_m+t\frac{\sqrt m}{4}\right\rfloor.
                                                               \tag{1.10}
\]

Lemma 1.1 and (1.8)--(1.9) give

\[
 {V_{\le a_m(t)}\over W}\longrightarrow\Phi(t),   \tag{1.11}
\]

\[
 {T_{\le a_m(t),q}\over W}
 \longrightarrow e^{-c^2}\Phi(t+2c).              \tag{1.12}
\]

## 2. A joint lower-tail cut for arbitrary pairings

Fix arbitrary perfect matchings \(\mathcal P_0,\mathcal P_1\).  In the
common rank-\((m-q)\) target layer define

\[
 A_i(a)=\{T:f_{\mathcal P_i}(T)\le a\},\qquad
 A(a)=A_0(a)\cap A_1(a).                           \tag{2.1}
\]

Each marginal set has cardinality \(T_{\le a,q}\), independently of the
matching.  Bonferroni therefore gives the correlation-free bound

\[
 |A(a)|\ge2T_{\le a,q}-N_q.                        \tag{2.2}
\]

No joint central limit theorem, no assumption on the alternating cycles
of \(\mathcal P_0\cup\mathcal P_1\), and no lower bound on their distance
is used here.

### Lemma 2.1 (two-shore capacity of the joint tail)

For arbitrary selected port subsets,

\[
 \sum_{T\in A(a)}r_T\le2V_{\le a}.                 \tag{2.3}
\]

#### Proof

Associate every selected lower depth-\(q\) occurrence on shore \(i\) to
its unique starting middle owner.  A strip transition empties split
\(\mathcal P_i\)-pairs and never changes which \(\mathcal P_i\)-pairs are
full.  Hence

\[
 f_{\mathcal P_i}(T)=f_{\mathcal P_i}(X)           \tag{2.4}
\]

for an occurrence from owner \(X\) to target \(T\).  Every owner supplies
at most one forward depth-\(q\) occurrence.  If \(T\in A(a)\), then in
particular \(f_{\mathcal P_i}(T)\le a\), so shore \(i\) can contribute at
most the \(V_{\le a}\) owners of its own type at most \(a\).  Summing the
two shores proves (2.3).  A common owner leave or deletion of ports only
reduces the left side. \(\square\)

### Theorem 2.2 (exact marginal-orbit lower bound)

For every integer \(a\),

\[
 \boxed{
 \mathfrak B_{2,q}^-
 \ge
 2\bigl(2T_{\le a,q}-N_q-V_{\le a}\bigr)_+.}       \tag{2.5}

#### Proof

For every integer \(r\), \(|r-2|\ge2-r\).  Hence Lemma 2.1 and (2.2)
give

\[
\begin{aligned}
 \mathfrak B_{2,q}^-
 &\ge\sum_{T\in A(a)}(2-r_T)\\
 &\ge2|A(a)|-2V_{\le a}\\
 &\ge2\bigl(2T_{\le a,q}-N_q-V_{\le a}\bigr).
\end{aligned}                                                   \tag{2.6}
\]

If the final expression is negative, replace it by zero. \(\square\)

Taking \(a=a_m(t)\) in Theorem 2.2 and using (1.11)--(1.12) proves
(0.4).  At \(c=1,t=-1\),

\[
 e^{-1}(2\Phi(1)-1)-\Phi(-1)
 =0.0924921749\ldots,                              \tag{2.7}
\]

which proves (0.2)--(0.3).

The upper signed layer obeys the same theorem after complementing sources
and targets.  The lower layer alone already gives the claimed linear
obstruction.

## 3. The mixed-pair association statistic

Although Theorem 2.2 deliberately avoids joint-orbit information, the
first joint statistic has a particularly simple exact form.  Let
\(s=|\mathcal P_0\cap\mathcal P_1|\), let \(R_r\) be a uniform
\(r\)-set, and put

\[
 p_j=\frac{(r)_j}{(2m)_j}.                         \tag{3.1}
\]

Then

\[
\boxed{
\begin{aligned}
 \operatorname {Cov}\bigl(f_{\mathcal P_0}(R_r),
                           f_{\mathcal P_1}(R_r)\bigr)
 &=s(p_2-p_2^2)\\
 &\quad+2(m-s)(p_3-p_2^2)\\
 &\quad+(m^2-2m+s)(p_4-p_2^2).
\end{aligned}}                                                   \tag{3.2}
\]

Indeed, an ordered pair consisting of one edge of each matching is either
the same edge (\(s\) choices), meets in one vertex
(\(2(m-s)\) choices), or is disjoint
(\(m^2-2m+s\) choices).  These three cases have joint containment
probabilities \(p_2,p_3,p_4\), respectively.

If \(r=m+O(\sqrt m)\) and \(s/m\to\alpha\), (3.2) and (1.7) give

\[
 \operatorname {Corr}\bigl(f_{\mathcal P_0}(R_r),
                            f_{\mathcal P_1}(R_r)\bigr)
 \longrightarrow\alpha.                             \tag{3.3}
\]

Thus edge-disjoint pairings are asymptotically uncorrelated at the
Gaussian scale and identical pairings have correlation one.  The
linear no-go nevertheless holds throughout the entire interval
\(0\le\alpha\le1\), because the marginal intersection cut (2.2) is
stronger than any correlation hypothesis needed here.

## 4. The signed frustration graph

Overlay \(\mathcal F_0,\mathcal F_1\) by their common middle owners.  As
usual, every connected overlay component \(P\) has the same owner support
on both shores, and choosing one shore in every component preserves exact
middle ownership.

For a target with exactly two catalogue occurrences, write those
occurrences as \((P,\epsilon)\) and \((Q,\epsilon')\), with
\(\epsilon,\epsilon'\in\{0,1\}\) the shore labels.  It creates the signed
edge

\[
 PQ\quad\hbox{with label}\quad
 s_{PQ}=1\oplus\epsilon\oplus\epsilon'.             \tag{4.1}
\]

A packet potential \(x_P\in\{0,1\}\) covers this target exactly once if
and only if

\[
 x_P\oplus x_Q=s_{PQ}.                              \tag{4.2}
\]

Consequently the exact residual signed cost is the frustration index

\[
 \tau(G)=\min_x
 \#\{PQ:x_P\oplus x_Q\ne s_{PQ}\}.                 \tag{4.3}
\]

Theorem 2.2 applies before any packet choices are made and gives

\[
 \mathfrak B_2+\tau(G)
 \ge\mathfrak B_{2,q}^-
 \ge(\kappa+o(1))W.                                 \tag{4.4}
\]

Thus neither an exact coboundary nor a favorable packing of frustrated
cycles can make any two fixed-pair frames satisfy the pair-balanced
criterion.  The catalogue occurrence profile already has linear error.

## 5. Conserved-statistic boundary and product-SCD frames

The proof used only a conserved integer type, not the geometry of Hamming
cycles.  The following abstraction states its exact scope.

### Proposition 5.1 (two-frame conserved-tail obstruction)

Suppose shore \(i\) has an integer type \(g_i\) on middle owners and
rank-\((m-q)\) targets such that:

1. every selected shore-\(i\) occurrence preserves \(g_i\);
2. every owner supplies at most one selected occurrence;
3. the two owner tail counts \(\#\{X:g_i(X)\le a\}\) equal a common
   value \(V_{\le a}\); and
4. the two target tail counts \(\#\{T:g_i(T)\le a\}\) equal a common
   value \(T_{\le a,q}\).

Then the two-copy imbalance satisfies exactly (2.5).

#### Proof

Repeat (2.1)--(2.6) with \(g_i\) in place of
\(f_{\mathcal P_i}\). \(\square\)

Every factor confined to one coordinate pairing has the conserved type
\(f_{\mathcal P_i}\), so Theorem 2.2 is exhaustive for all such pairs.
A product-SCD-induced physical strip factor is also closed whenever its
chronology preserves a type with the same Gaussian tail displacement.
To escape this theorem while retaining the pair-balanced certificate, a
genuinely cross-box product-SCD factor must do at least one of the following
on a positive density of owners:

* destroy every common-tail conserved type;
* let one owner feed more than one certified occurrence at the audited
  depth (which changes the port ledger); or
* replace pair balance by an anchored higher-order CSP.

No existing product-SCD physical strip construction is known to satisfy
those escape requirements.  The theorem therefore completely closes the
mixed-coordinate-pair **two-copy imbalance-plus-frustration gate**, while
leaving genuinely anchored catalogues and non-pair-frame product-SCD
factors outside its quantified scope.

## 6. Exact status

Proved:

1. the exact joint-tail lower bound (2.5) for every two perfect matching
   frames;
2. the universal Gaussian constant (0.3), independent of matching
   distance and factor details;
3. the exact mixed-frame covariance formula (3.2);
4. the signed-frustration normal form and the statewise bound (0.5); and
5. the abstract conserved-tail criterion covering any analogous
   product-SCD frame.

Not proved:

* an obstruction for a genuinely non-pair-frame product-SCD physical
  strip factor with no conserved Gaussian type;
* a no-go for three or more shores (the two-set Bonferroni cut changes at
  higher arity); or
* the annulus theorem.

The decisive conclusion is nevertheless broad: changing one fixed
coordinate pairing to any other fixed coordinate pairing, however far
away, cannot make a conjugate pair satisfy
\(\mathfrak B_2+\tau(G)=o(W)\).  A surviving construction must instead be
anchored rather than pair-balanced, use a higher-alphabet packet system, or
leave the fixed-pair grammar itself.
