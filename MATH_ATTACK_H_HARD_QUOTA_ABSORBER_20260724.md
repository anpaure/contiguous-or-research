# Mathematical attack H: hard-quota absorber inside an exact wreath factor

Date: 2026-07-24

Method: theorem-proof analysis only. No web search, finite search, random
experiment, or solver was used.

## 0. Verdict

This route does **not** presently prove MWB or the contiguous-OR width
conjecture.

It does give a sharper exact reduction.  On every fixed Gaussian window, the
quota vectors can be eliminated completely: a common core is quota-safe if and
only if it obeys one ceiling inequality and one total floor-deficit inequality
at each depth.  If one starts from an exact factor, exact residual
factorability is also eliminated as a separate issue: it is enough to delete a
small transversal of the quota violations.  Thus the smallest equivalent
statement within this hard-quota exceptional-core route is an integral
common-depth deletion-cover lemma inside one exact factor.

Three possible shortcuts fail rigorously.

1. Coordinate-star Hall cuts can always be made arithmetically feasible by
   regular balanced quotas, so they do not supply the missing factor.
2. All weighted Hall cuts characterize only a fractional deletion.  A small
   finite set-system example shows that integral rounding does not follow.
3. The binary choice between the two lifts of a projected star trace is not
   independent.  Exact-factor-preserving gap flips are precisely closed
   alternating cycles in a sparse \(Q_v\)-lift graph; no one- or two-wreath
   \(P_v\)-trace-preserving gap-flip trade exists for \(m\geq 3\).

The strongest positive special case obtained here is also exact: if an exact
factor has balanced quota vectors whose *total positive violation mass* over a
fixed Gaussian window is \(o(\operatorname{Cat}_m/\sqrt m)\), deleting owners
of those violations produces the desired core and an exactly factorable
exceptional family.  No construction of such a factor is proved.

## 1. Definitions and the bounded-capacity fixed window

Put
\[
 n=2m+1,\qquad
 W=\binom{n}{m},\qquad
 t=t_m=\frac Wn=\operatorname{Cat}_m.
\]
A wreath support is the family of the \(n\) cyclic length-\(m\) intervals in
a cyclic order of \([n]\).  An exact wreath factor \(F\) partitions the whole
middle layer into wreath supports and therefore has exactly \(t\) members.

At depth \(q\), put
\[
 r=m-q,\qquad
 N_q=\binom nr,\qquad
 \lambda_q=\frac W{N_q},\qquad
 c_q=\lfloor\lambda_q\rfloor,\qquad
 \rho_q=W-c_qN_q.
\]
Thus \(0\leq\rho_q<N_q\).  A balanced quota is a vector
\[
 \beta_q(S)\in\{c_q,c_q+1\},\qquad
 \sum_{S\in\binom{[n]}r}\beta_q(S)=W;
\]
equivalently, exactly \(\rho_q\) targets receive quota \(c_q+1\).

For a family \(X\) of wreaths, let \(\mu_q^X(S)\) be the number of members of
\(X\) in which \(S\) is a cyclic length-\(r\) interval.  Every wreath has
exactly \(n\) such intervals, so
\[
 \sum_S\mu_q^X(S)=n|X|.                                      \tag{1.1}
\]

Fix \(A>0\) and write
\[
 K_A=\lceil A\sqrt m\rceil.
\]

### Lemma 1.1 (bounded capacities on a fixed window)

For every fixed \(A\), there are constants \(C_A<\infty\) and
\(\kappa_A>0\) such that, for all sufficiently large \(m\) and all
\(1\leq q\leq K_A\),
\[
 1\leq c_q\leq C_A,\qquad N_q\geq\kappa_AW.                  \tag{1.2}
\]
Moreover
\[
 \sum_{q\leq K_A}\frac1{c_q}\leq K_A=O_A(\sqrt m).           \tag{1.3}
\]

#### Proof

The exact product is
\[
 \lambda_q
 =\prod_{i=0}^{q-1}\left(1+\frac{2(i+1)}{m-i}\right).
\]
Since \(\log(1+x)\leq x\),
\[
 \log\lambda_q
 \leq\sum_{i=0}^{q-1}\frac{2(i+1)}{m-i}
 \leq\frac{q(q+1)}{m-q+1}.                                  \tag{1.4}
\]
For fixed \(A\), the last expression is at most \(2(A+2)^2\) for all
sufficiently large \(m\) and \(q\leq K_A\).  Hence one may take
\[
 C_A=\left\lceil e^{2(A+2)^2}\right\rceil,\qquad
 \kappa_A=e^{-2(A+2)^2}.
\]
Since \(\lambda_q\geq1\), also \(c_q\geq1\), and (1.3) follows immediately.
\(\square\)

We will also use the fixed-scale asymptotic
\[
 \lambda_{\lfloor x\sqrt m\rfloor}\longrightarrow e^{x^2}
 \qquad(x\geq0\text{ fixed}).                               \tag{1.5}
\]
Indeed, on a fixed Gaussian window the summands
\[
 u_i=\frac{2(i+1)}{m-i}
\]
are \(O_A(m^{-1/2})\),
\[
 \sum_{i<q}u_i=\frac{q(q+1)}m+O_A(m^{-1/2}),\qquad
 \sum_{i<q}u_i^2=O_A(m^{-1/2}),
\]
and \(\log(1+u_i)=u_i+O(u_i^2)\).  This proves (1.5).

## 2. Exact elimination of the quota variables

Let an exact factor be split as
\[
 F=G\sqcup B,\qquad |B|=b.
\]
The same \(F,G,B\) is used at every controlled depth.  At depth \(q\), write
\[
 \eta(S)=\mu_q^G(S).
\]
By (1.1),
\[
 \sum_S\eta(S)=W-nb=c_qN_q+\rho_q-nb.                       \tag{2.1}
\]
Define the total deficit below the floor by
\[
 \Delta_q(\eta)=\sum_S(c_q-\eta(S))_+.
\]

### Theorem 2.1 (exact partial-quota criterion)

There is a balanced quota \(\beta_q\) satisfying
\[
 \eta(S)\leq\beta_q(S)\quad\text{for every }S               \tag{2.2}
\]
if and only if
\[
 \max_S\eta(S)\leq c_q+1                                   \tag{2.3}
\]
and
\[
 \Delta_q(\eta)\leq nb.                                     \tag{2.4}
\]

#### Proof

Assume (2.3), and put
\[
 h=\#\{S:\eta(S)=c_q+1\}.
\]
Every other deviation from the baseline \(c_q\) is nonpositive.  Therefore
\[
 \sum_S\eta(S)=c_qN_q+h-\Delta_q(\eta).
\]
Comparison with (2.1) gives the exact identity
\[
 h=\rho_q-nb+\Delta_q(\eta).                                \tag{2.5}
\]
A balanced quota dominates \(\eta\) exactly when its \(\rho_q\) high
positions contain all \(h\) ceiling positions.  Such a choice is possible if
and only if \(h\leq\rho_q\), which by (2.5) is equivalent to (2.4).
The ceiling (2.3) is plainly necessary. \(\square\)

Thus the unlabelled fixed-window hard-quota problem has the following
quota-free form, which we denote by \(HQ_A\):
\[
 \boxed{
 \begin{aligned}
 &\text{find one exact }F=G\sqcup B,\quad
 |B|=o(t/\sqrt m),\\
 &\max_S\mu_q^G(S)\leq c_q+1,\qquad
 \sum_S(c_q-\mu_q^G(S))_+\leq n|B|\\
 &\hspace{42mm}(1\leq q\leq K_A).
 \end{aligned}}                                             \tag{\(HQ_A\)}
\]
This preserves exact ownership: \(B\) is a family of whole wreaths, not a
depth-dependent or fractional correction.

The balanced quotas in \(HQ_A\) are unlabelled overload witnesses and may be
chosen independently at different depths.  Only \(F,G,B\) must be common.
Thus \(HQ_A\) is not the previously used labelled/nested condition denoted
elsewhere by \(CA_A\).

### Corollary 2.2 (the mean-one first shadow)

For \(m\geq3\),
\[
 \lambda_1=\frac{m+2}{m},\qquad c_1=1,\qquad
 N_1=\frac m{m+2}W,\qquad
 \rho_1=\frac2{m+2}W.                                       \tag{2.6}
\]
Consequently a depth-one core is quota-safe if and only if
\[
 \max_S\mu_1^G(S)\leq2,\qquad
 \#\{S:\mu_1^G(S)=0\}\leq nb.                               \tag{2.7}
\]
If \(Z\) is its zero family and \(D\) its double family, then
\[
 |D|=\rho_1-nb+|Z|.                                         \tag{2.8}
\]

#### Proof

The identities in (2.6) follow from the adjacent binomial ratio.  With
\(c_1=1\), the deficit in (2.4) is exactly the number of zero cells, and
(2.8) is (2.5). \(\square\)

More generally, if \(A<\sqrt{\log2}\), then (1.5), uniformly on compact
subintervals up to \(A\), gives \(c_q=1\) for every
\(q\leq A\sqrt m\) and all sufficiently large \(m\).  Hence an entire short
Gaussian window is a simultaneous bounded-fold near-design problem: every
load is at most two and at most \(nb\) targets at each depth are missed.

## 3. The exact conditional implication to MWB

For a full factor \(F\), let \(O_q(F)\) be the minimum, over balanced quotas
\(\beta_q\), of
\[
 \sum_S(\mu_q^F(S)-\beta_q(S))_+.
\]

### Theorem 3.1 (hard-quota exceptional charging)

Suppose \(F=G\sqcup B\) satisfies \(HQ_A\), with \(|B|=b\).  Then, for every
\(q\leq K_A\),
\[
 O_q(F)\leq nb,                                              \tag{3.1}
\]
and
\[
 \sum_{q\leq K_A}\frac{O_q(F)}{c_q}
 \leq nb\sum_{q\leq K_A}\frac1{c_q}
 \leq nbK_A.                                                 \tag{3.2}
\]
In particular,
\[
 b=o(t/\sqrt m)
 \quad\Longrightarrow\quad
 \sum_{q\leq K_A}\frac{O_q(F)}{c_q}=o(W).                    \tag{3.3}
\]

#### Proof

Choose a dominating balanced quota \(\beta_q\) supplied by Theorem 2.1 and
put
\[
 s_q=\beta_q-\mu_q^G\geq0.
\]
Both vectors have known total mass, so
\[
 \sum_Ss_q(S)=W-(W-nb)=nb.
\]
Also
\[
 \mu_q^F-\beta_q=\mu_q^B-s_q.
\]
Taking positive parts and summing gives
\[
 \sum_S(\mu_q^F(S)-\beta_q(S))_+
 \leq\sum_S\mu_q^B(S)=nb,
\]
which proves (3.1).  Equations (3.2) and (3.3) follow from (1.3) and
\(W=nt\). \(\square\)

If \(HQ_A\) is proved for every fixed \(A\), a standard diagonalization
chooses \(A_j\uparrow\infty\) and then a slowly increasing \(j=j(m)\) for
which the normalized error in (3.3) tends to zero.  This gives a common
window \(H(m)=A_{j(m)}\sqrt m\) with \(H/\sqrt m\to\infty\) and weighted
overload \(o(W)\).  The already audited MWB-to-OR reduction then gives the
final contiguous-OR bound \(W+o(W)\).  The missing point is precisely the
unproved antecedent \(HQ_A\), not any estimate in Theorem 3.1.

## 4. Exact-factor-first deletion transversals

Starting from an exact factor makes residual factorability automatic and
turns the hard-quota task into a finite integral covering problem.

Fix \(F\), a window \(1\leq q\leq K_A\), and balanced quotas \(\beta_q\).
For every resource \(a=(q,S)\), define its violation demand
\[
 d_a=(\mu_q^F(S)-\beta_q(S))_+.
\]
For \(E\in F\), let \(A_{aE}=1\) if \(S\) occurs as a depth-\(q\) interval
of \(E\), and \(A_{aE}=0\) otherwise.  Define
\[
 \tau_A(F,\beta)=
 \min\left\{|B|:B\subseteq F,\ 
       \sum_{E\in B}A_{aE}\geq d_a\ \text{for every }a\right\}.             \tag{4.1}
\]

### Theorem 4.1 (exact deletion-cover equivalence)

For \(B\subseteq F\) and \(G=F\setminus B\), the following are equivalent:

\[
 \mu_q^G(S)\leq\beta_q(S)
 \quad\text{for all }q\leq K_A\text{ and all }S;             \tag{4.2}
\]
\[
 \sum_{E\in B}A_{aE}\geq d_a
 \quad\text{for every resource }a.                           \tag{4.3}
\]

When these conditions hold, \(F=G\sqcup B\) is already the required exact
completion.  No separate residual theorem is needed.

#### Proof

For \(a=(q,S)\),
\[
 \mu_q^G(S)
 =\mu_q^F(S)-\sum_{E\in B}A_{aE}.
\]
Thus (4.2) is equivalent to deletion of at least
\(\mu_q^F(S)-\beta_q(S)\) occurrences whenever this number is positive,
which is exactly (4.3).  Since \(B\) is a subset of the exact factor, its
wreath supports partition the middle-layer leave of \(G\). \(\square\)

Put
\[
 \Xi_A(F,\beta)=\sum_a d_a,\qquad
 \Xi_q(F,\beta_q)=\sum_Sd_{q,S}.
\]
Every deleted wreath covers at most \(n\) demand units at one depth and at
most \(nK_A\) across the window.  Conversely, for each resource one may
choose \(d_a\) distinct owner wreaths and take their union.  Hence
\[
 \boxed{
 \max_{q\leq K_A}\frac{\Xi_q(F,\beta_q)}n
 \leq\tau_A(F,\beta),\qquad
 \frac{\Xi_A(F,\beta)}{nK_A}
 \leq\tau_A(F,\beta)
 \leq\Xi_A(F,\beta).}                                       \tag{4.4}
\]

### Corollary 4.2 (a proved sufficient special case)

If, for every fixed \(A\), there are an exact factor \(F\) and balanced
quotas \(\beta_q\) such that
\[
 \Xi_A(F,\beta)=o(t/\sqrt m),                                \tag{4.5}
\]
then \(HQ_A\) holds, hence MWB and the \(W+o(W)\) contiguous-OR bound hold.

#### Proof

The upper bound in (4.4) supplies \(B\subseteq F\) with
\(|B|\leq\Xi_A=o(t/\sqrt m)\); Theorem 4.1 gives quota domination, and
Theorem 3.1 gives the required weighted estimate. \(\square\)

Condition (4.5) is sufficient but not necessary.  The exact quantity is the
transversal number \(\tau_A\): one deleted wreath can cover as many as
\(nK_A\) violation tokens.  Therefore the absorber problem is a
*concentration* problem, asking whether all demands can be clustered on very
few whole wreaths.

## 5. Rigidity forced before an absorber can act

A small exceptional family cannot repair undercoverage: deletion only lowers
loads.  The next lemma quantifies this obstruction.

### Lemma 5.1 (two-sided prebalance of the ambient factor)

If \(F=G\sqcup B\) satisfies \(HQ_A\), then, for every \(q\leq K_A\),
\[
 \sum_S(c_q-\mu_q^F(S))_+\leq nb,                            \tag{5.1}
\]
\[
 \sum_S(\mu_q^F(S)-c_q-1)_+\leq nb.                          \tag{5.2}
\]
Consequently, if \(b=o(t/\sqrt m)\), then
\[
 \sum_{q\leq K_A}\left[
 \sum_S(c_q-\mu_q^F(S))_+
 +\sum_S(\mu_q^F(S)-c_q-1)_+\right]=o(W).                    \tag{5.3}
\]

#### Proof

Since \(\mu_q^G\leq\mu_q^F\),
\[
 (c_q-\mu_q^F(S))_+\leq(c_q-\mu_q^G(S))_+,
\]
and (5.1) follows from (2.4).  Since
\(\mu_q^G(S)\leq c_q+1\),
\[
 (\mu_q^F(S)-c_q-1)_+
 \leq\mu_q^B(S).
\]
Summing proves (5.2).  Finally \(K_Anb=o(W)\) under the stated scale.
\(\square\)

Thus the exceptional family is not a bulk balancing device.  The exact factor
must already have only \(o(W)\) total underfloor and over-ceiling mass across
the fixed window.  In particular, at depth one,
\[
 \#\{S:\mu_1^F(S)=0\}\leq nb,\qquad
 \sum_S(\mu_1^F(S)-2)_+\leq nb.                              \tag{5.4}
\]

There is also an exact point-margin identity.  Let
\[
 H_q=\{S:\mu_q^G(S)=c_q+1\},\qquad
 \delta_q(S)=(c_q-\mu_q^G(S))_+.
\]

### Lemma 5.2 (signed coordinate-star identity)

For every coordinate \(v\),
\[
 \deg_{H_q}(v)-\sum_{S\ni v}\delta_q(S)
 =r(t-b)-c_q\binom{n-1}{r-1}.                               \tag{5.5}
\]

#### Proof

Every wreath has exactly \(r\) cyclic length-\(r\) intervals containing
\(v\), so
\[
 \sum_{S\ni v}\mu_q^G(S)=r(t-b).
\]
Under the ceiling condition,
\[
 \mu_q^G(S)=c_q+\mathbf1_{H_q}(S)-\delta_q(S).
\]
Summing this identity over the \(r\)-sets containing \(v\) gives (5.5).
\(\square\)

In the unit-floor window, \(H_q\) is the double family and \(\delta_q\) is
the indicator of the zero family.  Hence the doubles and holes must form a
common signed-regular design at every depth, not merely have the right total
cardinalities.

Point-star divisibility itself is not an obstruction.  If
\(\mathcal H_q\) is the family of the \(\rho_q\) high positions of a quota,
then
\[
 \frac{r\rho_q}{n}
 =rt-c_q\binom{n-1}{r-1}\in\mathbb Z.                        \tag{5.6}
\]

### Lemma 5.3 (regular high quotas exist)

For every \(q\), there is a balanced quota whose high family
\(\mathcal H_q\subseteq\binom{[n]}r\) is regular of degree
\(r\rho_q/n\).

#### Proof

We prove the elementary general statement that if \(n\mid rh\), there is a
simple \(r\)-uniform family of \(h\) sets with all degrees equal.
Among all \(h\)-set families choose one minimizing the sum of squared vertex
degrees.  If vertices \(a,b\) have
\(\deg(a)\geq\deg(b)+2\), some selected edge \(E\) containing \(a\) but not
\(b\) has
\[
 E'=(E\setminus\{a\})\cup\{b\}
\]
unselected.  Otherwise the replacement map would inject all selected edges
containing \(a\) but not \(b\) into selected edges containing \(b\) but not
\(a\), contradicting \(\deg(a)>\deg(b)\).  Replacing \(E\) by \(E'\)
strictly decreases the square sum.  Hence all degrees differ by at most one.
Their average \(rh/n\) is integral, so all are equal.  Apply this with
\(h=\rho_q\), using (5.6). \(\square\)

For completeness, quota domination yields the necessary one-coordinate cuts
\[
 r\left(\frac{\rho_q}{n}-b\right)
 \leq\deg_{\mathcal H_q}(v)
 \leq\frac{r\rho_q}{n}+(n-r)b.                              \tag{5.7}
\]
The lower inequality sums quota capacity over \(r\)-sets containing \(v\);
the upper inequality applies the same argument to sets avoiding \(v\).
The regular family from Lemma 5.3 lies in this interval.  Therefore all
singleton coordinate-star cuts can be passed by the quotas.  This proves
only the absence of an arithmetic point-cut obstruction; it says nothing
about containment of one common core.

## 6. Hall cuts are exactly fractional, not integral

Retain the deletion matrix \(A\) and demand vector \(d\) from Section 4.
For nonnegative resource weights \(y=(y_a)\), put
\[
 w_E(y)=\sum_aA_{aE}y_a.
\]
Let \(\operatorname{Top}_b(w_E:E\in F)\) denote the sum of the \(b\)
largest entries.

### Theorem 6.1 (fractional Hall dual)

There are numbers
\[
 0\leq x_E\leq1,\qquad \sum_{E\in F}x_E\leq b,\qquad Ax\geq d             \tag{6.1}
\]
if and only if, for every \(y\geq0\),
\[
 \sum_ad_ay_a
 \leq\operatorname{Top}_b(w_E(y):E\in F).                   \tag{6.2}
\]

#### Proof

Let
\[
 P_b=\{x\in[0,1]^F:\sum_Ex_E\leq b\}.
\]
The vectors fractionally coverable with budget \(b\) form the coordinatewise
downward closure of \(AP_b\).  A separating functional for this
downward-closed convex set can be taken nonnegative.  For \(y\geq0\), its
support function is
\[
 \max_{x\in P_b}y^\mathsf TAx
 =\max_{x\in P_b}\sum_Ew_E(y)x_E
 =\operatorname{Top}_b(w_E(y):E\in F),
\]
because all \(w_E(y)\geq0\).  Separation proves the equivalence.
\(\square\)

The theorem is not an integral Hall theorem.  Take the seven points of the
Fano plane as resources and the complements of its seven lines as deletion
candidates, with unit demand at every point.  Every point lies in four
candidates, so weight \(1/4\) on every candidate is a fractional cover of
total mass \(7/4<2\).  But any two candidates miss the unique intersection
point of their complementary lines.  Thus the integral cover number is at
least three.  This example is not asserted to be wreath-realizable; it
proves that the weighted Hall inequalities alone need an additional
wreath-specific integrality or absorber theorem.

Two immediate integral cuts are worth recording.  If a deletion set of size
\(b\) exists, then
\[
 b\geq\frac{O_q(F)}n,\qquad
 b\geq\frac{c_qM_q(F)}n,                                    \tag{6.3}
\]
where \(M_q(F)=\#\{S:\mu_q^F(S)=0\}\).  The first follows because a wreath
deletes only \(n\) occurrences at depth \(q\); the second follows from
(5.1), since each hole contributes \(c_q\).  Therefore
\[
 b=o(t/\sqrt m)
\quad\Longrightarrow\quad
 O_q(F)=o(W/\sqrt m),\quad c_qM_q(F)=o(W/\sqrt m)             \tag{6.4}
\]
at every controlled depth.  This uniform per-depth demand is stronger than
the conclusion \(\sum_{q\leq K_A}O_q(F)=o(W)\) alone.

## 7. Fractional benchmarks and the failure of symmetric thinning

Let \(D_m=m!(m+1)!/2\) be the degree of a middle set in the full unoriented
wreath hypergraph.  Giving every wreath support weight \(1/D_m\) gives load
one on each middle set, total wreath mass \(t\), and uniform depth-\(q\)
load \(\lambda_q\).

### Proposition 7.1 (sharp floor-only fractional theorem at depth one)

Scale the uniform weights by
\[
 \alpha=\frac m{m+2}.
\]
Then the middle load is \(\alpha\), every depth-one target has load exactly
one, and the fractional exceptional mass is
\[
 b_*=(1-\alpha)t=\frac{2t}{m+2}=O(t/m).                      \tag{7.1}
\]
This is optimal among fractional cores constrained by the stronger
floor-only condition \(\mu_1\leq1\).

#### Proof

The depth-one load is
\[
 \alpha\lambda_1=\frac m{m+2}\frac{m+2}m=1.
\]
The complementary uniform weights complete the middle load to one and have
total mass (7.1).  Conversely, every weighted wreath contributes \(n\)
depth-one incidences.  Since the total floor-only capacity is \(N_1\),
\[
 n|G|\leq N_1,
\]
so
\[
 |G|\leq\frac{N_1}n=\frac m{m+2}t.
\]
\(\square\)

Thus the desired exceptional scale is fractionally attainable at depth one.
The obstruction is integral and simultaneous, not a first-shadow mass
shortage.

### Proposition 7.2 (sharp integral saturation cost in the floor-only model)

Let \(F\) be exact, and put
\[
 z=\#\{S:\mu_1^F(S)=0\}.
\]
If \(B\subseteq F\) leaves the stronger floor-only core
\[
 \mu_1^{F\setminus B}(S)\leq1\quad\text{for every }S,
\]
then
\[
 |B|\geq
 \left\lceil\frac{\rho_1+z}{n}\right\rceil
 \geq\left\lceil\frac{2t}{m+2}\right\rceil.                 \tag{7.2}
\]
The exact number of deleted depth-one incidences not needed to remove an
initial excess above one is
\[
 n|B|-(\rho_1+z).                                           \tag{7.3}
\]

#### Proof

Because the full depth-one mass is \(W\),
\[
 \sum_S(\mu_1^F(S)-1)_+
 =W-\#\{S:\mu_1^F(S)>0\}
 =W-(N_1-z)=\rho_1+z.
\]
Every one of these excess occurrences must be deleted, while a wreath
deletes only \(n\) depth-one incidences.  This proves (7.2), using
\(\rho_1/n=2t/(m+2)\).  Once the required excess occurrences are charged,
all other deleted incidences are wasted for the floor-only constraint,
which gives (7.3). \(\square\)

In particular, if
\[
 |B|\leq(1+\varepsilon)\frac{\rho_1+z}{n},
\]
then at most an \(\varepsilon/\delta\) fraction of the wreaths in \(B\) can
waste at least \(\delta n\) incidences.  Thus an integral construction near
the \(O(t/m)\) fractional optimum must select wreaths almost saturated by
duplicated first-shadow targets.  The projected pair-codegree estimate does
not provide this saturation.

There is no analogous symmetry-preserving solution on a nontrivial fixed
Gaussian window.

### Proposition 7.3 (stabilizer-symmetric thinning loses constant mass)

Fix \(A>0\) and a coordinate \(v\).  Any nonnegative fractional weighting of
all wreath supports invariant under the stabilizer of \(v\) is constant on
the supports.  If its common middle load is \(\alpha\) and it is dominated
by balanced quotas for every \(q\leq K_A\), then for some
\(\gamma_A>0\),
\[
 \alpha\leq1-\gamma_A+o(1).                                 \tag{7.4}
\]
Hence its missing wreath mass is \(\Omega_A(t)\), not
\(o(t/\sqrt m)\).

#### Proof

The stabilizer of \(v\) is transitive on wreath supports: rotate a
representative of each cyclic order so that \(v\) occupies the same
position, then map the remaining labels positionwise.  Thus invariant
weights are constant.  If the middle load is \(\alpha\), the depth-\(q\)
load is uniformly \(\alpha\lambda_q\).

Choose
\[
 0<x<\min\{A,\sqrt{\log2}\},\qquad q=\lfloor x\sqrt m\rfloor.
\]
By (1.5), \(\lambda_q\to e^{x^2}\in(1,2)\), so \(c_q=1\) and a balanced
quota has at least one low position of capacity one.  Uniformity forces
\[
 \alpha\lambda_q\leq1,
\]
and hence
\[
 \alpha\leq e^{-x^2}+o(1).
\]
Take \(\gamma_A=1-e^{-x^2}>0\). \(\square\)

This proposition rules out only stabilizer-invariant weighting or thinning.
It does not rule out a construction that breaks symmetry at leading order.
It proves that such symmetry breaking is indispensable before integral
rounding.

## 8. Exact star-fibre switching

Fix a coordinate \(v\), and split the middle layer into
\[
 P_v=\{M:v\in M\},\qquad Q_v=\{M:v\notin M\}.
\]
Every wreath has \(m\) vertices in \(P_v\) and \(m+1\) in \(Q_v\).

### Lemma 8.1 (two lifts and the gap flip)

For \(m\geq2\), every projected trace \(T=E\cap P_v\) of a wreath has
exactly two full wreath lifts.  Up to reversal, a representative cyclic
order has the form
\[
 (r_1,\ldots,r_{m-1},v,s_1,\ldots,s_{m-1},x,y),              \tag{8.1}
\]
and the two lifts interchange the adjacent gap labels \(x,y\).

At every interval length used here, \(2\leq\ell\leq m\), an adjacent interchange
changes exactly two old interval sets into exactly two new interval sets.
If \(S_\ell,R_\ell\) are the \(\ell-1\) labels immediately on the two sides
of the gap, the signed change is
\[
 \Delta_{T,\ell}
 =\mathbf1_{S_\ell\cup\{y\}}
  +\mathbf1_{R_\ell\cup\{x\}}
  -\mathbf1_{S_\ell\cup\{x\}}
  -\mathbf1_{R_\ell\cup\{y\}}.                              \tag{8.2}
\]
The four targets are distinct.  At length one the interval family is
unchanged; define \(\Delta_{T,1}=0\).

#### Proof

The \(m\) members of \(T\), in cyclic start order, induce a path in the
Johnson graph.  Consecutive path vertices reveal the leaving and entering
labels; this reconstructs the ordered core in (8.1), up to reversal.
Exactly \(x,y\) are missing from the trace union, and they can fill the
two-position gap only as \(xy\) or \(yx\).

For an adjacent pair \(x,y\), a cyclic \(\ell\)-window changes only if it
contains exactly one of them.  There is exactly one old window containing
\(x\) but not \(y\) and exactly one containing \(y\) but not \(x\), giving
(8.2).  For \(\ell\geq2\), the two side cores are disjoint from one another
and from \(x,y\) when \(\ell\leq m\), so the four sets are distinct.
\(\square\)

At the middle length \(\ell=m\), the unchanged \(Q_v\)-part has size
\(m-1\).  The changed old pair and changed new pair have the form
\[
 R_E=\{S\cup\{x\},\,R\cup\{y\}\},\qquad
 A_E=\{S\cup\{y\},\,R\cup\{x\}\},                            \tag{8.3}
\]
where \(R=\{r_1,\ldots,r_{m-1}\}\) and
\(S=\{s_1,\ldots,s_{m-1}\}\).  Each displayed pair consists of complementary
\(m\)-subsets of \([n]\setminus\{v\}\).

### Theorem 8.2 (exact lift-cycle conservation)

Let \(F\) be an exact factor, and take each member as the base lift of its
\(P_v\)-trace.  For \(E\in F\), define a partial map \(\phi\) by
\[
 \phi(E)=E'
 \quad\Longleftrightarrow\quad
 A_E=R_{E'}.                                                 \tag{8.4}
\]
If \(A_E\) meets the fixed \(Q_v\)-part of any trace, leave \(\phi(E)\)
undefined.

For \(I\subseteq F\), replace every \(E\in I\) by its twin lift.  The
result is an exact factor if and only if \(\phi\) is defined on \(I\) and
\(\phi|_I\) is a permutation of \(I\).  Equivalently, \(I\) is a disjoint
union of directed cycles of \(\phi\).

#### Proof

All \(P_v\)-incidences and all fixed \(Q_v\)-sets remain unchanged.  Since
\(F\) is exact, its variable pairs \(R_E\) partition the remaining
\(Q_v\)-vertices.  Any complementary pair \(A_E\) wholly in this remaining
set equals a unique \(R_{E'}\); if it meets a fixed set, adding it creates an
unremovable collision.  Exactness after the flips is therefore equivalent
to
\[
 \{A_E:E\in I\}=\{R_E:E\in I\}
\]
with multiplicity one, which is exactly the permutation condition.
\(\square\)

Thus the binary lift choices satisfy a global \(Q_v\)-circulation law.  An
individual gap flip is never an exact-factor trade.

### Lemma 8.3 (no one- or two-cycle, \(m\geq3\))

The partial map \(\phi\) has no directed cycle of length one or two.

#### Proof

A fixed point is impossible because \(R_E\cap A_E=\varnothing\) in (8.3).
Suppose \(E,E'\) formed a two-cycle.  The four changed \(Q_v\)-sets would be
\[
 Sx,\ Sy,\ Rx,\ Ry.
\]
For \(m\geq3\), the only pairs among these four having intersection
\(m-1\) are \(\{Sx,Sy\}\) and \(\{Rx,Ry\}\); every cross intersection has
size zero or one.  Hence the same two side cores \(S,R\) are forced for
\(E'\).  Both \(P_v\)-traces then contain the endpoint sets
\(S\cup\{v\}\) and \(R\cup\{v\}\), contradicting the disjointness of the
exact factor. \(\square\)

### Corollary 8.4 (residual-preserving quota switch)

Let \(F=G\sqcup B\) be exact and let \(C\) be a directed \(\phi\)-cycle.
Flip all traces indexed by \(C\), retaining their core/exceptional
designation.  Then \(F'=G'\sqcup B'\) is exact and \(|B'|=|B|\).  If
\[
 s_q=\beta_q-\mu_q^G,
\]
the switch is quota-admissible if and only if
\[
 \sum_{E\in C\cap G}\Delta_{E,m-q}(S)\leq s_q(S)             \tag{8.5}
\]
for every controlled \(q\) and every target \(S\).

This is immediate from Theorem 8.2 and the signed change (8.2).  It is an
exact necessary-and-sufficient test, including all cancellations between
simultaneous flips.

In particular, one exceptional wreath cannot absorb a single open core
gap-flip for \(m\geq3\).  Such an absorption would replace two wreaths by
their two twins: exact \(P_v\)-coverage forces the new exceptional wreath
to be the twin of the old one, producing a forbidden two-cycle.

The lift graph is sparse in the relevant sense.  The complementary pairs in
\(Q_v\) number
\[
 \frac{|Q_v|}{2}=\frac{(m+1)t}{2},
\]
whereas the exact factor activates only \(t\) variable pairs \(R_E\), a
density \(2/(m+1)\).  Neither projected star regularity nor its
\(O(m^{-2})\) codegree estimate gives a lower bound on defined successors,
directed cycles, or cycles satisfying all inequalities (8.5).

## 9. Residual margins do not imply residual factorability

Any matching of \(t-b\) wreaths leaves \(nb\) middle sets, and each
coordinate belongs to exactly \(mb\) of them.  These necessary margins are
not sufficient even when \(b=1\).

### Lemma 9.1 (recognition of a one-wreath leave)

Let \(L\) be a family of \(n\) middle sets in which every coordinate occurs
exactly \(m\) times.  Then \(L\) is a wreath support if and only if its
induced Johnson graph contains a Hamilton cycle.

#### Proof

The forward implication is given by consecutive cyclic windows.  Conversely,
list a Hamilton cycle as \(L_0,L_1,\ldots,L_{n-1}\).  Each edge changes one
coordinate out and one in, so the coordinate indicator words around the
cycle have \(2n\) transitions in total.  Every coordinate word has weight
\(m\), strictly between zero and \(n\), and hence has at least two cyclic
transitions.  There are \(n\) coordinates, so every word has exactly two
transitions.  Its ones consequently occupy one cyclic interval of \(m\)
positions.  Every cycle edge is the entry point of exactly one coordinate;
ordering the coordinates by these entry points makes the \(L_i\) precisely
the cyclic length-\(m\) windows. \(\square\)

### Lemma 9.2 (explicit regular non-wreath family)

For every \(m\geq3\), there is a family \(L\) of \(n\) distinct middle sets
such that every coordinate has degree \(m\), but \(L\) is not a wreath.

#### Proof

Label the coordinates by \(\mathbb Z_n\), and put
\[
 D=\{0,1,\ldots,m-2\}\cup\{m\},\qquad
 L=\{D+j:j\in\mathbb Z_n\}.
\]
Translation symmetry gives degree \(m\) at every coordinate.  For
\(1\leq d\leq m\), direct intersection gives
\[
 |D\cap(D+d)|=
 \begin{cases}
 m-2,&d=1,\\
 m-d,&2\leq d\leq m-2,\\
 1,&d=m-1,m.
 \end{cases}                                                 \tag{9.1}
\]
Autocorrelation symmetry handles the other nonzero differences.  Thus
distinct translates intersect in at most \(m-2\) points; in particular they
are distinct and no pair is Johnson-adjacent.  Every wreath has consecutive
windows intersecting in \(m-1\) points, so \(L\) is not a wreath.
\(\square\)

This example is **not** claimed to arise as the leave of an actual wreath
matching.  It proves exactly what is needed for the audit: cardinality,
coordinate regularity, and all star divisibilities cannot certify exact
residual completion.  The safe architecture is therefore exact-factor-first,
followed by deletion of \(B\subseteq F\).

## 10. The smallest equivalent lemma within this route

The preceding reductions isolate the exact target.

### Integral common-depth deletion-transversal lemma — **UNPROVED**

For every fixed \(A>0\), there exist an exact wreath factor \(F_m\) and
balanced quotas
\[
 \beta_q(S)\in\{c_q,c_q+1\}
 \qquad(1\leq q\leq K_A)
\]
such that
\[
 \boxed{\tau_A(F_m,\beta)=o(t_m/\sqrt m).}                   \tag{10.1}
\]

By Theorems 2.1 and 4.1, this is equivalent to the quota-free statement
\(HQ_A\).
By Theorem 3.1 and diagonalization, it implies MWB and the final
\(W+o(W)\) OR bound.  It preserves one common exact factor, one common
exceptional family, and whole-wreath ownership at every depth.

A switching-based sufficient replacement would assert that one can first
choose an exact factor and then find enough directed lift cycles from
Theorem 8.2 to concentrate all quota demands on
\(o(t/\sqrt m)\) indices while satisfying the simultaneous slack
inequalities (8.5).  This is stronger than (10.1), and is also **UNPROVED**.

The genuine obstruction is now sharp:

- the ambient factor must already satisfy the two-sided \(o(W)\) prebalance
  (5.3);
- fractional Hall feasibility does not imply integral deletion;
- local two-lift switches must close in \(Q_v\)-balanced cycles of length at
  least three;
- no known degree, codegree, star-saturation, or deterministic-nibble
  argument forces either the required integral transversal or enough
  quota-admissible cycles.

## 11. Adversarial audit of the strongest claims

The main claims above were checked independently against the following
failure modes.

1. **Partial mass versus full mass.**  The half-\(\ell^1\) overload identity
   is not applied to \(\mu_q^G\).  Theorem 2.1 instead uses the exact partial
   mass \(W-nb\), leading to (2.5).  This removes a common factor-two error.
2. **Separate depthwise choices.**  Quotas may vary with \(q\), but
   \(F,G,B\) do not.  Every theorem is stated for a common deletion set
   throughout the window.
3. **Point cuts versus global containment.**  Lemma 5.3 proves only that
   regular high quota families exist.  It is not used as a sufficiency
   theorem for a wreath core.
4. **Fractional versus integral Hall.**  Theorem 6.1 is explicitly
   fractional.  The Fano example prevents promotion to an integral theorem
   without new wreath-specific structure.
5. **Projected versus full matching.**  The switching analysis retains all
   \(Q_v\) vertices.  Theorem 8.2 shows exactly why independent binary lift
   choices are invalid.
6. **Open versus closed switches.**  Only directed lift cycles preserve an
   exact factor.  A single gap flip and a two-wreath absorber are ruled out,
   rather than tacitly counted as legal trades.
7. **Margins versus factorability.**  Lemma 9.2 is used only to refute a
   margin-based implication.  It is not asserted to be an actual leave of a
   partial factor.
8. **Symmetry obstruction scope.**  Proposition 7.3 applies only to
   stabilizer-invariant weights.  It establishes the need for leading-order
   symmetry breaking, not impossibility of all nonuniform constructions.
9. **Sufficient violation mass versus the exact target.**  Corollary 4.2 is
   deliberately one-sided.  The exact parameter is \(\tau_A\), because
   violation tokens may share owner wreaths.
10. **Final logical status.**  No unproved matching, absorber, integrality,
    or cycle-richness assertion is used to claim MWB.  The only implication
    to MWB is conditional on the explicitly marked Lemma (10.1).

Accordingly, the report supplies a rigorous reduction, several unconditional
obstructions and fractional benchmarks, and the exact smallest equivalent
missing lemma within the hard-quota exceptional-core route, but not the
conjecture.
