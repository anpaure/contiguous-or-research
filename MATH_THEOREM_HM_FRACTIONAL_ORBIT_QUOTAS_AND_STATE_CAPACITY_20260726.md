# Hyperoctahedral target orbits: fractional quota compatibility and the fixed-state capacity obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result and precise scope

Partition a \(2m\)-element coordinate set into pairs

\[
P_i=\{a_i,b_i\},\qquad i\in[m],
\]

and let

\[
G=C_2^m\rtimes S_m=S_2\wr S_m
\]

act by swapping points inside pairs and permuting the pairs. Put

\[
W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q},\qquad
\lambda_q=\frac{W}{N_q}=c_q+\theta_q,
\]

where \(c_q=\lfloor\lambda_q\rfloor\), \(0\leq\theta_q<1\), and

\[
\rho_q=W-c_qN_q=\theta_qN_q.
\]

The conclusions are:

1. Rank-\((m-q)\) targets have \(G\)-orbits indexed by their number \(f\)
   of full pairs, of exact size
   \[
   T_{f,q}
   =\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.
   \]

2. Pure \(G\)-symmetry has no fractional floor-quota obstruction.
   Fractional high-quota densities \(x_f\) are feasible exactly when
   \[
   0\leq x_f\leq1,\qquad
   \sum_fT_{f,q}x_f=\rho_q.
   \]
   The constant solution \(x_f=\theta_q\) works. Every target orbit is a
   coordinate \(1\)-design, so this solution also has the exact fractional
   point margins.

3. A pointwise \(G\)-fixed integral balanced quota exists exactly when
   \(\rho_q\) is a subset sum of the orbit sizes \(T_{f,q}\). Regardless
   of this arithmetic condition, an integral balanced quota can be made a
   union of whole orbits except inside one orbit. Uniformly for
   \(q\leq A\sqrt m\), that exceptional orbit has size
   \[
   O_A(N_q/\sqrt m)=O_A(W/\sqrt m).
   \]
   Thus pure orbit granularity is only \(o(W)\).

4. For prescribed orbit masses \(M_f\), \(\sum_fM_f=W\), define
   \[
   D_q^-(M)=\sum_f(c_qT_{f,q}-M_f)_+,\qquad
   D_q^+(M)=\sum_f(M_f-(c_q+1)T_{f,q})_+.
   \]
   The exact orbit-relaxed projection formula is
   \[
   \min_b\frac12\|\mu-b\|_1
   =\max\{D_q^-(M),D_q^+(M)\}.
   \]
   In particular, prescribed masses are compatible with balanced quotas
   exactly when
   \[
   c_qT_{f,q}\leq M_f\leq(c_q+1)T_{f,q}
   \quad\text{for every }f.
   \]

5. The actual one-frame, pair-face architecture violates these intervals
   by \(\Omega(W)\) at every fixed positive Gaussian depth. Its source
   state capacity is
   \[
   V_f=T_{f,0}
   =\frac{m!}{f!^2(m-2f)!}\,2^{m-2f},
   \]
   and its exact capacity ratio is
   \[
   R_{f,q}:=\frac{V_f}{T_{f,q}}
   =2^q\frac{(f+q)!}{f!}
          \frac{(m-2f-q)!}{(m-2f)!}.
   \]
   It is strictly increasing in \(f\). If \(q/\sqrt m\to\gamma>0\), then
   \[
   \sum_f(c_qT_{f,q}-V_f)_+
   \geq(\kappa_\gamma+o(1))W
   \]
   for an explicit \(\kappa_\gamma>0\). The same obstruction holds in
   the complementary upper ledger.

The distinction is essential: \(G\)-symmetry by itself is harmless
fractionally. The linear obstruction comes from the diagonal state law
\(f\mapsto f\) for windows confined to one fixed pair frame. Mixing pair
frames or using a genuine cross-state exact-factor trade is outside the
no-go.

## 1. Exact orbit classification

For \(S\subseteq[2m]\), let \(F(S),E(S),B(S)\) be its numbers of full,
empty, and split pairs. Then

\[
F+E+B=m,\qquad |S|=2F+B.
\]

For \(|S|=m-q\), subtraction gives \(E-F=q\). Hence, on putting \(F=f\),

\[
(F,E,B)=(f,f+q,m-2f-q),
\qquad
0\leq f\leq\left\lfloor\frac{m-q}{2}\right\rfloor.
\]

These three counts are invariant under \(G\). Conversely, a pair
permutation aligns the three pair classes and the internal swaps align
the selected point of every split pair. They are therefore a complete
orbit invariant. Counting gives

\[
\boxed{
T_{f,q}
=\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.}
\tag{1.1}
\]

Thus

\[
\sum_fT_{f,q}=N_q.
\tag{1.2}
\]

Complementation gives the paired rank-\((m+q)\) orbit with \(f+q\) full,
\(f\) empty, and \(m-2f-q\) split pairs. It has the same size \(T_{f,q}\).

## 2. Pure symmetry: fractional and integral quotas

A balanced quota has the form

\[
b(S)=c_q+\mathbf1_{\mathcal H}(S),
\qquad |\mathcal H|=\rho_q.
\tag{2.1}
\]

Let \(x_f\) be the fractional density of \(\mathcal H\) in orbit
\(\mathcal O_{f,q}\). The exact fractional orbit polytope is

\[
\mathcal P_q=
\left\{x:\ 0\leq x_f\leq1,\
\sum_fT_{f,q}x_f=\rho_q\right\}.
\tag{2.2}
\]

It is nonempty for every \(m,q\), because

\[
\boxed{x_f=\theta_q=\rho_q/N_q\quad\text{for all }f}
\tag{2.3}
\]

satisfies (2.2).

There is no hidden one-point constraint. The group \(G\) is transitive on
the \(2m\) coordinates, so each orbit is a \(1\)-design. Every coordinate
occurs in exactly

\[
\frac{m-q}{2m}T_{f,q}
\tag{2.4}
\]

members of orbit \(f\). Consequently every solution of (2.2) has high
point margin

\[
\sum_fx_f\frac{m-q}{2m}T_{f,q}
=\frac{m-q}{2m}\rho_q.
\tag{2.5}
\]

For a pointwise \(G\)-fixed integral quota, \(x_f\in\{0,1\}\). Therefore

\[
\boxed{
\text{a \(G\)-fixed integral quota exists}
\iff
\rho_q=\sum_{f\in I}T_{f,q}
\text{ for some }I.}
\tag{2.6}
\]

This subset-sum condition is exact; gcd divisibility is only necessary.

Even when (2.6) fails, order the orbits and take whole orbits until the
next one would cross \(\rho_q\); take the required number of targets from
that one orbit. The resulting integral quota breaks \(G\)-symmetry only
inside one orbit.

Uniformly for \(q\leq A\sqrt m\),

\[
\max_fT_{f,q}\leq C_A\frac{N_q}{\sqrt m}.
\tag{2.7}
\]

Indeed,

\[
\frac{T_{f+1,q}}{T_{f,q}}
=\frac{(m-2f-q)(m-2f-q-1)}
       {4(f+1)(f+q+1)}
\tag{2.8}
\]

is strictly decreasing in \(f\). Thus \(T_{f,q}\) is log-concave, with
mode within \(O_A(1)\) of

\[
f_q^*=\frac{(m-q)^2}{4m}.
\tag{2.9}
\]

Multiplying (2.8) for \(|j|\leq\sqrt m/20\) shows

\[
T_{f_q^*+j,q}\geq e^{-C_A}\max_fT_{f,q}.
\tag{2.10}
\]

There are \(\Theta(\sqrt m)\) such indices, and their sum is at most
\(N_q\), proving (2.7). Also \(N_q/W\) stays between positive
\(A\)-dependent constants. Hence the single exceptional orbit is
\(O_A(W/\sqrt m)\).

This last construction does not assert that a partial orbit is
point-regular. Equation (2.5) is a fractional statement.

## 3. Exact projection for prescribed orbit masses

Fix integers \(M_f\geq0\) with \(\sum_fM_f=W\). If \(h_f\) targets in
orbit \(f\) receive upper quota, then

\[
0\leq h_f\leq T_{f,q},\qquad
\sum_fh_f=\rho_q.
\tag{3.1}
\]

Put

\[
y_f=M_f-c_qT_{f,q}.
\tag{3.2}
\]

Then \(\sum_fy_f=\rho_q\). At orbit-mass level the optimization is

\[
\frac12\min_h\sum_f|y_f-h_f|.
\tag{3.3}
\]

Clip \(y_f\) to \([0,T_{f,q}]\):

\[
h_f^0=\min\{T_{f,q},\max\{0,y_f\}\}.
\]

The two clipping losses are exactly

\[
D_q^-=\sum_f(-y_f)_+,\qquad
D_q^+=\sum_f(y_f-T_{f,q})_+,
\tag{3.4}
\]

and

\[
\sum_fh_f^0=\rho_q+D_q^- -D_q^+.
\tag{3.5}
\]

If \(D_q^->D_q^+\), lower the clipped coordinates by total
\(D_q^--D_q^+\). If the reverse inequality holds, raise them by the
opposite difference. The interval capacity is sufficient because
\(\sum_fy_f=\rho_q\). Since all data are integral, the correction may be
integral. It adds \(|D_q^--D_q^+|\) to the unhalved distance, proving

\[
\boxed{
\min_h\frac12\sum_f
|M_f-(c_qT_{f,q}+h_f)|
=\max\{D_q^-,D_q^+\}.}
\tag{3.6}
\]

This orbit-mass bound is attained by target histograms in the relaxation:
inside each orbit, align the histogram with its quota, putting any
residual wholly below or wholly above it. A literal factor may have
additional chronology and ownership restrictions, so (3.6) is only a
lower bound for literal factors.

The distance is zero exactly when

\[
c_qT_{f,q}\leq M_f\leq(c_q+1)T_{f,q}
\quad\text{for all }f.
\tag{3.7}
\]

## 4. The one-frame state law

A middle owner in state \(f\) has \(f\) full, \(f\) empty, and \(m-2f\)
split pairs. There are

\[
\boxed{
V_f
=\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}
=T_{f,0}}
\tag{4.1}
\]

such owners.

A pair-face depth-\(q\) window flips \(q\) distinct split directions. Its
intersection makes those pairs empty and its union makes them full.
Therefore its lower and upper target types are

\[
(f,f+q,m-2f-q),
\qquad
(f+q,f,m-2f-q).
\tag{4.2}
\]

Both ledgers retain the source index \(f\). A middle owner gives at most
one start at a fixed depth, so \(V_f\) is an upper capacity for the load
of either target orbit. States with \(m-2f<q\) have no valid
distinct-direction \(q\)-window; counting them as defects only strengthens
the bound.

From (1.1) and (4.1),

\[
\boxed{
R_{f,q}:=\frac{V_f}{T_{f,q}}
=2^q\frac{(f+q)!}{f!}
       \frac{(m-2f-q)!}{(m-2f)!}.}
\tag{4.3}
\]

Furthermore,

\[
\frac{R_{f+1,q}}{R_{f,q}}
=\frac{f+q+1}{f+1}
\frac{(m-2f)(m-2f-1)}
     {(m-2f-q)(m-2f-q-1)}
>1.
\tag{4.4}
\]

Thus the under-floor states form an initial interval in \(f\), while the
over-ceiling states form a terminal interval. This is an exact finite
classification.

For any construction confined to this frame, every balanced quota has at
least

\[
\boxed{\sum_f(c_qT_{f,q}-V_f)_+}
\tag{4.5}
\]

aggregate underload in the low-\(f\) orbits. If total supplied mass is
\(W\), equal histogram and quota totals turn the same quantity into a
lower bound for positive overload. If \(E\) starts are discarded, then

\[
\text{discarded mass}+\text{positive overload}
\geq\sum_f(c_qT_{f,q}-V_f)_+.
\tag{4.6}
\]

The statement applies separately to the lower and complementary upper
ledgers.

## 5. Linear deficit at Gaussian depth

Let

\[
q=q_m,\qquad q/\sqrt m\longrightarrow\gamma>0,\qquad
x_f=\frac{f-m/4}{\sqrt m}.
\]

The exact factorial formulas, together with the standard two-sided
Stirling inequalities, give uniformly on each fixed compact \(x\)-set

\[
\sqrt m\,\frac{T_{f,q}}{N_q}
\longrightarrow
\sqrt{\frac8\pi}\,e^{-8(x_f+\gamma/2)^2},
\tag{5.1}
\]

\[
\sqrt m\,\frac{V_f}{W}
\longrightarrow
\sqrt{\frac8\pi}\,e^{-8x_f^2},
\tag{5.2}
\]

and

\[
\frac{W}{N_q}\longrightarrow e^{\gamma^2}.
\tag{5.3}
\]

For clarity, these are not entropy estimates: applying
\[
\sqrt{2\pi n}(n/e)^ne^{1/(12n+1)}
<n!<
\sqrt{2\pi n}(n/e)^ne^{1/(12n)}
\]
to (1.1) and (4.1), then Taylor-expanding their logarithms, gives
(5.1)--(5.3) with uniform \(O_\gamma(m^{-1/2})\) remainder on compact
\(x\)-sets.

Dividing (5.2) by (5.1) and using (5.3) yields

\[
\boxed{
R_{f,q}\longrightarrow e^{8\gamma x_f+3\gamma^2}}
\tag{5.4}
\]

uniformly on compact intervals.

Consider

\[
I_{\gamma,m}
=\left\{f:
\left|x_f+\frac{\gamma}{2}\right|
\leq\frac{\gamma}{16}\right\}.
\tag{5.5}
\]

On this interval the limiting exponent in (5.4) is at most

\[
8\gamma\left(-\frac{\gamma}{2}+\frac{\gamma}{16}\right)
+3\gamma^2=-\frac{\gamma^2}{2}.
\]

Therefore

\[
R_{f,q}\leq e^{-\gamma^2/2+o(1)}<1\leq c_q
\tag{5.6}
\]

uniformly on \(I_{\gamma,m}\). Using (5.1) and (5.3),

\[
\begin{aligned}
\liminf_{m\to\infty}\frac1W
\sum_f(c_qT_{f,q}-V_f)_+
&\geq
e^{-\gamma^2}(1-e^{-\gamma^2/2})
\int_{-\gamma/16}^{\gamma/16}
\sqrt{\frac8\pi}e^{-8y^2}\,dy\\
&=:\kappa_\gamma>0.
\end{aligned}
\tag{5.7}
\]

Only \(c_q\geq1\) was used, so no floor ambiguity arises when
\(e^{\gamma^2}\) is an integer.

For any fixed \(A>0\), take

\[
q_m=\left\lfloor\frac A2\sqrt m\right\rfloor.
\]

Then \(q_m\leq A\sqrt m\), and (5.7) gives an
\(\Omega_A(W)\) statewise quota obstruction inside the required window.

## 6. Literal-factor implication boundary

The theorem closes constructions confined to one coordinate-pair frame
whose lower and upper flags are generated by distinct-direction paths in
the associated orientation cubes. Such paths cannot transport mass
between \(f\)-states.

It does not close:

* mixtures of different pair frames, because one middle owner can have
  different \(f\)-types in different frames;
* non-face-compatible exact-factor trades which genuinely move mass
  between pair states;
* constructions merely averaged under \(G\), without preserving each
  source state;
* chronology, simultaneous-depth selection, ownership completion, or
  literal contiguous-OR realizability. Fractional quota feasibility alone
  implies none of these.

Thus the first exact obstruction is not orbit size or orbit arithmetic.
It is the state-incidence law

\[
\text{source state }f\longrightarrow\text{target state }f.
\]

Any viable fixed-pair-symmetric constant-one construction must break this
law on a positive fraction of the Gaussian-depth occurrence mass.
