# Final audit of the revised pure-shore Q8 binary-dual report

Date: 2026-07-26

Audited source:
MATH_ATTACK_L_Q8_MOVING_ATLAS_BINARY_DUAL_AND_OCCUPANCY_COMPRESSION_20260726.md.

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Final verdict

The revised main theorem is valid with its now-explicit **pure-shore**
scope. In particular:

1. The binary/occurrence distinction, the one-simplex collapse, and the
   all-ones optimal dual are exact.
2. The packet-master dual (1.6)--(1.7) is the correct dual for overlapping
   packet columns with exact owner equations.
3. The full-space compression criterion (4.3) and positive-domain criterion
   (4.3a) are correct.
4. The literal 24-owner lower and upper target census (4.6)--(4.9) is
   correct. No multiplicity-to-support inference is hidden there.
5. The fixed-matching capacity bounds (5.1)--(5.4), likelihood-ratio
   threshold (5.5), local limits (6.7)--(6.8), and conclusion
   (6.13)--(6.15) are correct, including the constant
   \[
      \delta_A^{\mathrm{pair}}
      =e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.
   \]
6. The report no longer claims that connected owner overlap classifies the
   full associator-switch fibre. Its conclusion is correctly restricted to
   whole options subordinate to one global matching.

The revised Section 4 now averages over the full 56-target local
rank-three layer, with the correct constant \(3/7\), compressed dual value
\(96/7\), and loss \(16/7\). The revised Section 5 also takes the minimum
with the trivial support cap before deriving the positive-part exceptional
bound. The discrete crossing convention and the tail argument in Section 6
are explicit. No remaining mathematical correction or overclaim was found.

## 1. Binary LP and catalogue scope

### 1.1 One-simplex collapse

Let \(R\) be the tagged simultaneous-depth row set, let \(\Theta\) be any
finite catalogue of whole options, and let \(a_o\in\{0,1\}^R\) be the
incidence vector of the distinct literal support \(I_o\). The primal is

\[
\begin{aligned}
 \min\quad&\sum_{r\in R}z_r,\\
 z_r+\sum_{o\in\Theta}a_o(r)x_o&\ge1,\\
 \sum_{o\in\Theta}x_o&=1,\qquad x_o,z_r\ge0.
\end{aligned}
\]

Since \(0\le\sum_o a_o(r)x_o\le1\), the optimal repair is

\[
 z_r=1-\sum_o a_o(r)x_o.
\]

Consequently

\[
 \sum_rz_r=|R|-\sum_ox_o|I_o|,
\]

and hence

\[
 \eta^{\mathrm{bin}}(R,\Theta)
 =|R|-\max_{o\in\Theta}|I_o|.                    \tag{1.1}
\]

The all-ones dual attains (1.1). This proof uses neither coordinate
symmetry nor an assumption that different depths can choose different
options. The same \(o\) is used throughout the tagged row set.

This remains true if the pure-shore catalogue is enlarged: what changes is
the unknown maximum in (1.1). Thus the revised report correctly separates
the unconditional one-simplex identity from the conditional fixed-matching
capacity estimate.

### 1.2 Pure-shore versus switch closure

The four-coordinate recoupling graph on perfect matchings is connected, and
the union of the declared atlas of all perfect matchings is \(K_{2m}\).
The exclusion theorem therefore gives one common status-selector support,
the full middle layer.

The exact implication is the one now stated in the revised report:
within the declared pure-shore architecture, the single selector chooses
one global matching resolution. This does not say that every exact factor
obtainable from compatible local associator trades has one underlying
matching. The revised Sections 0, 2, and 8 preserve this distinction.

The assertion that the six cycles of one 24-owner shore are not six
independent owner supplies is also correct for the disjoint-component
simplex. A different packet-master model may expose overlapping packet
variables, but then its owner equations and dual prices must be retained.

### 1.3 Packet-master dual

For the primal

\[
\begin{aligned}
 \min\quad&\sum_tz_t,\\
 z_t+\sum_{a:t\in S(a)}x_a&\ge1,\\
 \sum_{a:X\in P(a)}x_a&=1\qquad(X),\\
 x_a,z_t&\ge0,
\end{aligned}
\]

dualize the cover inequalities by \(0\le y_t\le1\). Write the free dual
variable for the owner equality as \(-\pi_X\). The column constraint is

\[
 \sum_{t\in S(a)}y_t-\sum_{X\in P(a)}\pi_X\le0,
\]

and the objective is

\[
 \sum_ty_t-\sum_X\pi_X.
\]

This is exactly (1.6)--(1.7). In particular, the free owner-price term
cannot be discarded when conjugate packets overlap.

## 2. Compression criteria

Let

\[
 K_\kappa=\operatorname{conv}\{a_{\kappa,o}:o\in\Theta_\kappa\},
 \qquad K=\sum_\kappa K_\kappa,
\]

so

\[
 \mathfrak D(y)=\mathbf1^Ty-h_K(y).
\]

Assume \(\mathbf1^TP=\mathbf1^T\).

### Proposition 2.1 (all real directions)

\[
 \mathfrak D(Py)\ge\mathfrak D(y)\quad(y\in\mathbb R^R)
 \quad\Longleftrightarrow\quad P^TK\subseteq K.    \tag{2.1}
\]

Indeed,

\[
 h_K(Py)=h_{P^TK}(y),
\]

and support-function domination in every real direction is equivalent to
convex inclusion. Thus (4.3) is exact as written.

### Proposition 2.2 (positive Hall domain)

If also \(P[0,1]^R\subseteq[0,1]^R\), then

\[
 \mathfrak D(Py)\ge\mathfrak D(y)\quad(0\le y\le1)
 \quad\Longleftrightarrow\quad
 P^TK\subseteq K-\mathbb R_{\ge0}^R.              \tag{2.2}
\]

After the mass terms cancel, positive homogeneity extends the test from
the unit cube to every \(y\ge0\). The set
\(K-\mathbb R_{\ge0}^R\) is closed, convex, downward closed, and has the
same support function as \(K\) in nonnegative directions. Conversely, a
point outside this downward closure has a separating normal in the
nonnegative orthant. This proves (2.2), hence validates (4.3a).

Reynolds averaging over an actual option-system symmetry satisfies the
stronger inclusion in (2.1). No such conclusion follows for an arbitrary
conditional expectation.

## 3. Literal audit of the 24-owner census

Let

\[
 A=\{a,b,c,d\},\qquad R=\{u,v,w,x\},
\]

and

\[
 \mathcal Y=\{uw,ux,vw,vx\}.
\]

Each middle owner in

\[
 \mathcal V=\binom A2\times\mathcal Y
\]

has two coordinates from \(A\) and one endpoint from each reservoir pair,
and \(|\mathcal V|=6\cdot4=24\).

The three matchings

\[
 M_0=\{ab,cd\},\quad M_1=\{ac,bd\},\quad M_2=\{ad,bc\}
\]

partition the six two-subsets of \(A\).

### 3.1 Lower targets

For shore \(j\), four local squares hold \(Y\in\mathcal Y\) fixed and
cycle through the four split orientations of \(M_j\). Along their four
edges, the intersection in \(A\) is successively each singleton
\(\{a_0\}\), \(a_0\in A\). Hence their distinct lower targets are

\[
 C^-=\{\{a_0\}\cup Y:a_0\in A,\ Y\in\mathcal Y\},
 \qquad |C^-|=16.                                  \tag{3.1}
\]

The other two squares hold one edge \(Z\in M_j\) full on \(A\) and cycle
through the reservoir square. Its four edge intersections are the four
singletons of \(R\). Thus

\[
 R_j^-=\{Z\cup\{r_0\}:Z\in M_j,\ r_0\in R\},
 \qquad |R_j^-|=8.                                 \tag{3.2}
\]

The two families in (3.1)--(3.2) are disjoint because they contain,
respectively, one and two elements of \(A\). The three \(R_j^-\) are
pairwise disjoint because the \(M_j\) partition \(\binom A2\). Therefore
shore \(j\) has exactly the 24 distinct lower targets

\[
 C^-\ \dot\cup\ R_j^-,
\]

and the three-shore candidate union has size

\[
 16+3\cdot8=40.                                    \tag{3.3}
\]

This is a direct literal-set proof; no trace-injectivity assumption is
needed.

### 3.2 Upper targets

The same edge calculation with unions gives

\[
 C^+=\{(A\setminus\{a_0\})\cup Y:
              a_0\in A,\ Y\in\mathcal Y\},
 \qquad |C^+|=16,                                  \tag{3.4}
\]

and

\[
 R_j^+=\{Z\cup(R\setminus\{r_0\}):
              Z\in M_j,\ r_0\in R\},
 \qquad |R_j^+|=8.                                 \tag{3.5}
\]

Again these are disjoint by their number of \(A\)-coordinates, and the
selective families for distinct shores are disjoint. Hence the upper
ledger is identical.

### 3.3 Candidate-union Hall witness

On the 40 lower candidate rows, every shore hits 16 common and 8 selective
rows. Therefore

\[
 40-\max_j(16+8)=16.                               \tag{3.6}
\]

Tagging the two signs makes the corresponding value \(32\). The revised
report correctly says this is a deliberately restricted witness. In the
full eight-active-coordinate rank-three layer there are

\[
 \binom83=56
\]

rows. The missing 16 consist of:

\[
\begin{array}{c|c}
\#(T\cap A)&\text{number missing}\\ \hline
0&\binom43=4,\\
1&4\cdot2=8
   \quad\text{(the reservoir pairs \(uv,wx\))},\\
3&\binom43=4.
\end{array}
\]

No shore hits them.

### 3.4 Exact compression correction

Let \(y\) be one on the 24 selective lower rows and zero elsewhere.
On the 40-row candidate system,

\[
 \mathbf1^Ty=24,\qquad h_K(y)=8,\qquad\mathfrak D(y)=16.
\]

The revised compression averages over all 56 local rank-three rows:

\[
 P_{56}y=\frac{24}{56}\mathbf1_{56}
        =\frac37\mathbf1_{56}.
\]

Every shore still hits 24 rows, so

\[
 h_K(P_{56}y)=\frac{72}{7},\qquad
 \mathfrak D(P_{56}y)=24-\frac{72}{7}=\frac{96}{7}.
\]

This is also a strict loss:

\[
 16-\frac{96}{7}=\frac{16}{7}.                    \tag{3.7}
\]

Thus the source's \(3/7\), \(72/7\), \(96/7\), and \(16/7\) ledger is
exact. It is genuine rank-only averaging on the complete local
eight-coordinate rank-three layer. In a global embedding the fixed outside
decoration is retained, exactly as is appropriate for this local component
witness. The asymptotic fixed-matching obstruction separately uses the
global occupancy threshold.

## 4. Fixed-matching capacity and exceptions

Fix a perfect matching \(M\). A middle owner of type \(f\) has \(f\) full,
\(f\) empty, and \(m-2f\) split \(M\)-pairs. Its count is

\[
 V_f=\frac{m!\,2^{m-2f}}{f!^2(m-2f)!}.            \tag{4.1}
\]

A lower rank-\((m-q)\) target with \(f\) full pairs has \(f+q\) empty and
\(m-2f-q\) split pairs, and therefore count

\[
 T_{f,q}
 =\frac{m!\,2^{m-2f-q}}
        {f!(f+q)!(m-2f-q)!}.                      \tag{4.2}
\]

An isometric \(q\)-window inside a fixed \(M\)-status cell empties exactly
\(q\) distinct split pairs and preserves \(f\). Each middle owner supplies
one occurrence, so the number of distinct hit targets of type \(f\) is at
most both \(V_f\) and \(T_{f,q}\). Summing gives

\[
 |I_{o,q}^-|
 \le\sum_f\min(V_f,T_{f,q})
 =N_q-D_{m,q}.                                    \tag{4.3}
\]

For upper targets, count empty pairs instead of full pairs. The same
argument gives

\[
 |I_{o,q}^+|\le N_q-D_{m,q}.                       \tag{4.4}
\]

This proves (5.1)--(5.2) exactly for the declared pure-shore catalogue.

If at most \(L_q^\epsilon\) distinct targets of sign \(\epsilon\) are
excepted, then

\[
 |I_{o,q}^\epsilon|
 \le \min\{N_q,N_q-D_{m,q}+L_q^\epsilon\}.
\]

Thus the uncovered contribution of that sign is at least

\[
 (D_{m,q}-L_q^\epsilon)_+.
\]

Summing signs and depths proves (5.4). No unspoken assumption that the two
exception sets are disjoint is needed.

Finally,

\[
 \frac{T_{f,q}}{V_f}
 =\prod_{i=0}^{q-1}
   \frac{m-2f-i}{2(f+1+i)}.                       \tag{4.5}
\]

Each factor strictly decreases with \(f\) on its support. Hence
\(\{f:T_{f,q}>V_f\}\) is an initial interval, validating the exact
positive-part threshold used in Section 6.

## 5. Audit of (6.7)--(6.15)

Put

\[
 q=\lfloor A\sqrt m\rfloor,\qquad
 f=\frac m4+x\sqrt m,
\]

where \(A>0\) is fixed.

### 5.1 Crossing

Taking logarithms in (4.5) and expanding uniformly for bounded \(x\)
gives

\[
\begin{aligned}
 \log\frac{T_{f,q}}{V_f}
 &=\sum_{i=0}^{q-1}
 \left[
 \log\left(1-\frac{4x}{\sqrt m}-\frac{2i}{m}\right)
 -\log\left(1+\frac{4x}{\sqrt m}
                  +\frac{4(i+1)}m\right)
 \right]\\
 &=-8Ax-3A^2+o(1).                                \tag{5.1}
\end{aligned}
\]

The quadratic remainders sum to \(o(1)\), because
\(q=O(\sqrt m)\) and \(\sum_{i<q}i^2/m^2=O(m^{-1/2})\).
Monotonicity of (4.5), applied at
\(x=-3A/8\pm\varepsilon\), then gives for the largest positive type

\[
 f_*=\frac m4-\frac{3A}{8}\sqrt m+o(\sqrt m).      \tag{5.2}
\]

An exact equality \(T_{f,q}=V_f\) at one lattice point is harmless, since
its contribution to \(D_{m,q}\) is zero.

### 5.2 Local mass formulae

The consecutive ratios are exactly

\[
 \frac{V_{f+1}}{V_f}
 =\frac{(m-2f)(m-2f-1)}{4(f+1)^2},
\]

and

\[
 \frac{T_{f+1,q}}{T_{f,q}}
 =\frac{(m-2f-q)(m-2f-q-1)}
        {4(f+1)(f+q+1)}.
\]

Uniform Stirling expansion for \(|x|\le K\), with fixed \(K\), yields

\[
 \frac{V_f}{W}
 =\frac{4}{\sqrt m}\varphi(4x)(1+o_K(1)),          \tag{5.3}
\]

and

\[
 \frac{T_{f,q}}{N_q}
 =\frac{4}{\sqrt m}\varphi(4x+2A)(1+o_K(1)).       \tag{5.4}
\]

The factor \(4/\sqrt m\) is correct: the limiting \(x\)-variance is
\(1/16\), so its density is \(4\varphi(4x)\). The shifted law has mean
\(-A/2\), hence density \(4\varphi(4x+2A)\). Thus (6.7)--(6.8) have the
correct normalization and shift.

### 5.3 Tail control and weak convergence

For a uniform \(k\)-subset of \(2m\), \(k=m-q\), let \(f\) count fully
occupied matching pairs. With

\[
 p_2=\frac{(k)_2}{(2m)_2},\qquad
 p_4=\frac{(k)_4}{(2m)_4},
\]

one has

\[
 \mathbb Ef=mp_2,
\]

and

\[
 \operatorname{Var}(f)
 =mp_2(1-p_2)+m(m-1)(p_4-p_2^2).                 \tag{5.5}
\]

For \(q=O(\sqrt m)\), these give

\[
 \mathbb Ef=\frac m4-\frac q2+O(1),
 \qquad \operatorname{Var}(f)=O(m).               \tag{5.6}
\]

At \(q=0\) this gives the \(V\)-law. Therefore Chebyshev makes the scaled
laws tight. On every bounded \(x\)-interval, (5.3)--(5.4) turn sums over
the lattice of mesh \(m^{-1/2}\) into Riemann sums. Tightness then extends
the local convergence to

\[
 x\Longrightarrow N(0,1/16)\quad(V\text{-law}),
\]

and

\[
 x\Longrightarrow N(-A/2,1/16)\quad(T\text{-law}).
\]

This validates the implication (6.7)--(6.11); the tail step is not being
assumed from local Stirling alone.

### 5.4 Central-binomial ratio

Exactly,

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}.
\]

Its logarithm is

\[
 -\frac1m\sum_{i=0}^{q-1}(2i+1)+o(1)
 =-\frac{q^2}{m}+o(1),
\]

so

\[
 \frac{N_q}{W}\longrightarrow e^{-A^2}.           \tag{5.7}
\]

This proves (6.12), including the floor in \(q\).

### 5.5 Positive part and limiting constant

Since the positive types form the exact initial interval,

\[
\begin{aligned}
 \frac{D_{m,q}}W
 &=\frac1W\sum_{f\le f_*}(T_{f,q}-V_f)\\
 &=\frac{N_q}{W}\,\mathbb P_T\{f\le f_*\}
   -\mathbb P_V\{f\le f_*\}.                     \tag{5.8}
\end{aligned}
\]

By (5.2) and the two continuous Gaussian limits,

\[
 \mathbb P_T\{f\le f_*\}\longrightarrow\Phi(A/2),
\]

whereas

\[
 \mathbb P_V\{f\le f_*\}\longrightarrow\Phi(-3A/2).
\]

Combining with (5.7) proves

\[
 \frac{D_{m,q}}W
 \longrightarrow e^{-A^2}\Phi(A/2)-\Phi(-3A/2).   \tag{5.9}
\]

Finally, substitute \(u=t-2A\) in the second normal cdf:

\[
\begin{aligned}
 e^{-A^2}\Phi(A/2)-\Phi(-3A/2)
 &=e^{-A^2}\int_{-\infty}^{A/2}
       \left(1-e^{2At-A^2}\right)\varphi(t)\,dt.
                                                               \tag{5.10}
\end{aligned}
\]

For \(A>0\) and \(t<A/2\), the exponent \(2At-A^2\) is strictly negative.
The integrand is therefore positive except at the endpoint, proving strict
positivity. Equations (5.8)--(5.10) validate (6.13)--(6.15) exactly.

## 6. Correct final theorem

Let \(\Theta_{\mathrm{shore}}\) be the declared catalogue of whole
isometric status-cell factors, each subordinate throughout all protected
windows to one global perfect matching. Then for every protected depth set
\(\mathcal Q\),

\[
 \eta_{\mathcal Q}^{\mathrm{bin}}
 =|\mathcal R_{\mathcal Q}|
   -\max_{o\in\Theta_{\mathrm{shore}}}|I_o|,
\]

and \(y\equiv1\) is dual-optimal. Moreover,

\[
 \eta_{\mathcal Q}^{\mathrm{bin}}
 \ge2\sum_{q\in\mathcal Q}D_{m,q}.
\]

If \(\lfloor A\sqrt m\rfloor\in\mathcal Q\), then

\[
 \eta_{\mathcal Q}^{\mathrm{bin}}
 \ge\left(
 2e^{-A^2}\Phi(A/2)-2\Phi(-3A/2)-o(1)
 \right)W.
\]

For a catalogue with at most \(L_q^\epsilon\) exceptional distinct targets
at signed depth \((q,\epsilon)\), the valid robust replacement is

\[
 \eta_{\mathcal Q}^{\mathrm{bin}}
 \ge\sum_{q\in\mathcal Q}
 \left[
 (D_{m,q}-L_q^-)_+
 +(D_{m,q}-L_q^+)_+
 \right].
\]

No part of this theorem extends the capacity bound to a phase-changing or
mosaic associator-switch fibre. Such an extension requires a new invariant
or a direct support bound for the enlarged whole-option catalogue. The
revised main report states this boundary correctly.
