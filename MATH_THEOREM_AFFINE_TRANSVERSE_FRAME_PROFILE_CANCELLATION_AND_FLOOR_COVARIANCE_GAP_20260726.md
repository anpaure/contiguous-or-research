# Affine transverse frames cancel the Gaussian profile cut fractionally, but not the integral floor covariance

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, web input, or
crossed recursion is used.

## 0. Result

This note tests the proposed strategy of averaging a small orthogonal family
of block decompositions before resolving owner conflicts.

Put

\[
 n=2m=2^d,\qquad G=\mathbb F_2^d,\qquad
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
 \qquad \lambda_q={W\over N_q}.
 \tag{0.1}
\]

For every nonzero \(a\in G\), let

\[
 M_a=\{\{x,x+a\}:x\in G\}/2.                 \tag{0.2}
\]

The \(2m-1\) matchings \(M_a\) form a one-factorization of \(K_{2m}\),
and any two of them have union equal to a disjoint union of four-cycles.
Thus this is a linear-size, exactly transverse moving-frame family.

For a lower target \(T\in\binom G{m-q}\), write

\[
 f_a(T)=|\{e\in M_a:e\subset T\}|.             \tag{0.3}
\]

After averaging a valid fixed-frame factor over the wreath stabilizer of
\(M_a\), the target load is exactly

\[
 g_{m,q}(f_a(T)),\qquad
 g_{m,q}(f)={V_f\over T_{f,q}}
 =2^q{(f+q)!\over f!}{(m-2f-q)!\over(m-2f)!},    \tag{0.4}
\]

where

\[
 V_f={m!\over f!^2(m-2f)!}2^{m-2f},\qquad
 T_{f,q}={m!\over f!(f+q)!(m-2f-q)!}2^{m-2f-q}.
 \tag{0.5}
\]

Define the affine-frame average

\[
 \overline g_q(T)={1\over2m-1}
             \sum_{a\ne0}g_{m,q}(f_a(T)).          \tag{0.6}
\]

The first theorem is positive. Uniformly for \(0\le q\le A\sqrt m\),

\[
 {1\over N_q}\sum_{|T|=m-q}
       (\overline g_q(T)-\lambda_q)^2=O_A(m^{-1}). \tag{0.7}
\]

Upper targets satisfy the identical estimate by complementation. Hence, for
\(H\le A\sqrt m\),

\[
 \sum_{\epsilon\in\{-,+\}}\sum_{q=1}^H
 \sum_{T\in\binom G{m+\epsilon q}}
 (\overline g_{q,\epsilon}(T)-\lambda_q)^2
 =O_A\left({HW\over m}\right)
 =O_A\left({W\over\sqrt m}\right)=o(W).          \tag{0.8}
\]

Thus a linear-size orthogonal family really does erase the fixed-frame
Gaussian profile cut at the fractional, simultaneous all-depth level. This
is stronger than mere one-point orbit balance.

The second theorem identifies the exact failure of the naive integral
rounding. Put

\[
 c_q=\lfloor\lambda_q\rfloor,\qquad
 \theta_q=\lambda_q-c_q.                           \tag{0.9}
\]

The averaged fractional profile lies at

\[
 \sum_T(\overline g_q(T)-c_q)
       (\overline g_q(T)-c_q-1)
 =-N_q\theta_q(1-\theta_q)+O_A(N_q/m).             \tag{0.10}
\]

So it has exactly the fractional reserve one would want before rounding.
But a law which chooses one whole affine frame at a time has, at
\(q=a\sqrt m+o(\sqrt m)\), \(a>0\), floor energy at least

\[
 \bigl(\gamma(a)+o(1)\bigr)N_q,                   \tag{0.11}
\]

where

\[
 \gamma(a)=e^{6a^2}-e^{2a^2}
 -\vartheta(a)(1-\vartheta(a))>0,
 \qquad \vartheta(a)=\{e^{a^2}\}.                 \tag{0.12}
\]

The discrepancy between (0.10) and (0.11) is target-load variance. More
generally, let a probability law on integral owner resolutions have target
loads \(Z_T\), and suppose its mean is \(\mu_T=\overline g_q(T)\). Then

\[
 \mathbb E Q_q
 =\sum_T\operatorname {Var}(Z_T)
   -N_q\theta_q(1-\theta_q)+O_A(N_q/m),             \tag{0.13}
\]

where

\[
 Q_q=\sum_T(Z_T-c_q)(Z_T-c_q-1).                   \tag{0.14}
\]

Consequently a successful correlated resolution must have, after summing
both signs and all protected depths,

\[
 \sum_{\epsilon\in\{-,+\}}\sum_{q=1}^H
 \left[
 \sum_T\operatorname {Var}(Z_{q,\epsilon,T})
 -N_q\theta_q(1-\theta_q)
 \right]=o(W).                                      \tag{0.15}
\]

A stronger convenient pointwise form makes each bracket \(o(W/H)\). At
packet level, if \(I_P\) is the selection indicator and

\[
 K_q(P,P')=|A_q(P)\cap A_q(P')|,
\tag{0.16}
\]

then the variance within one bracket of (0.15) is exactly

\[
 \sum_{P,P'}K_q(P,P')\operatorname {Cov}(I_P,I_{P'}). \tag{0.17}
\]

For a catalogue diffuse at the protected scale,
\(\sum_P|A_q(P)|x_P^2=o(W/H)\), the diagonal part is
\(W-o(W/H)\) at one depth. Therefore the stronger pointwise form requires

\[
 \sum_{P\ne P'}K_q(P,P')\operatorname {Cov}(I_P,I_{P'})
 =-N_q(c_q+\theta_q^2)+o(W/H),                     \tag{0.18}
\]

while the exact aggregate form sums the left side plus
\(N_q(c_q+\theta_q^2)\) over signs and depths and requires \(o(W)\).
This is precisely the negative floor-covariance gate found in the
full-orbit packet audit.

Thus the verdict is sharp:

* a small orthogonal family cancels the fixed Gaussian cut before owner
  conflicts are resolved;
* choosing one whole transverse resolution retains a linear floor gap;
* independently choosing packets has zero off-diagonal covariance and
  retains the different linear gap \(N_q(c_q+\theta_q^2)\);
* the complete-quartet no-go still does not apply to a correlated packet
  mosaic, but orthogonal first moments alone do not construct that mosaic.

The remaining statement is an integral transverse-resolution coupling
whose packet indicators satisfy (0.18) simultaneously in \(q\).

## 1. The affine one-factorization

### Lemma 1.1 (exact transversality)

The family \(\{M_a:a\in G\setminus\{0\}\}\) has the following properties.

1. Every \(M_a\) is a perfect matching of \(G\).
2. Every edge of \(K_G\) belongs to exactly one \(M_a\).
3. If \(a\ne b\), then \(M_a\cup M_b\) is a disjoint union of \(m/2\)
   four-cycles.

#### Proof

Translation by nonzero \(a\) is a fixed-point-free involution, proving the
first claim. The unordered edge \(\{x,y\}\) has the unique nonzero
difference \(a=x+y\), proving the second.

For distinct nonzero \(a,b\), linear independence over \(\mathbb F_2\) is
automatic. Every coset of \(\langle a,b\rangle\) has the four vertices

\[
 x,\quad x+a,\quad x+b,\quad x+a+b.                \tag{1.1}
\]

The \(a\)- and \(b\)-edges alternate around the resulting four-cycle.
There are \(|G|/4=m/2\) cosets. \(\square\)

The third property is the exact orthogonality used below. Merely requiring
the matchings to be edge-disjoint would give the same leading covariance
cancellation, but the four-cycle decomposition makes every joint
coefficient explicit.

## 2. Exact fixed-frame profile load

Fix a perfect matching \(M\) of \(G\). A middle owner has \(f\) full
matching pairs precisely when it also has \(f\) empty pairs and
\(m-2f\) split pairs. This gives \(V_f\) in (0.5).

A lower target of rank \(m-q\) with \(f\) full pairs has \(f+q\) empty
pairs and \(m-2f-q\) split pairs. This gives \(T_{f,q}\) in (0.5).
The valid fixed-frame trace preserves its full-pair set: it changes \(q\)
split pairs into empty pairs. Hence all \(V_f\) source occurrences of type
\(f\) land among the \(T_{f,q}\) targets of the same type.

The wreath stabilizer

\[
 C_2^m\rtimes S_m                                           \tag{2.1}
\]

is transitive on both type classes. Averaging any valid fixed-frame factor
over this stabilizer therefore gives every type-\(f\) target the exact load
\(V_f/T_{f,q}=g_{m,q}(f)\). In particular,

\[
 {1\over N_q}\sum_{|T|=m-q}g_{m,q}(f_M(T))
 ={1\over N_q}\sum_fT_{f,q}{V_f\over T_{f,q}}
 ={W\over N_q}=\lambda_q.                           \tag{2.2}
\]

This argument uses only the valid within-frame trace. It does not introduce
the false crossed recursion.

## 3. The exact two-frame coefficient polynomial

Let \(a\ne b\), and consider one square (1.1). For a subset \(S\) of its
four vertices, let \(A(S)\) and \(B(S)\) be the numbers of its internal
\(a\)- and \(b\)-edges. Directly separating the subsets by cardinality
gives

\[
\begin{aligned}
 P(x;u,v)
 &=\sum_{S\subseteq\mathbb F_2^2}
       x^{|S|}u^{A(S)}v^{B(S)}\\
 &=1+4x+2x^2(1+u+v)+4x^3uv+x^4u^2v^2.             \tag{3.1}
\end{aligned}
\]

Therefore the exact number of rank-\(r\) targets with
\((f_a,f_b)=(i,j)\) is

\[
 [x^ru^iv^j]P(x;u,v)^{m/2}.                         \tag{3.2}
\]

The marginal identity

\[
 P(x;u,1)=(1+2x+x^2u)^2                            \tag{3.3}
\]

recovers \(T_{i,q}\) when \(r=m-q\). Thus (3.1), rather than an
independence assertion, contains the whole two-frame calculation.

### Lemma 3.1 (uniform transverse likelihood moments)

For every fixed \(A<\infty\), uniformly for \(0\le q\le A\sqrt m\), and
for a uniform \(T\in\binom G{m-q}\),

\[
\begin{aligned}
 \mathbb E g_{m,q}(f_a(T))&=\lambda_q,\\
 \mathbb E g_{m,q}(f_a(T))^2&=O_A(1),\\
 \mathbb E[g_{m,q}(f_a(T))g_{m,q}(f_b(T))]
 &=\lambda_q^2+O_A(m^{-1})\qquad(a\ne b).           \tag{3.4}
\end{aligned}
\]

If \(q=a_0\sqrt m+o(\sqrt m)\), then more precisely

\[
 \lambda_q\longrightarrow e^{a_0^2},\qquad
 \mathbb E g_{m,q}(f_a(T))^2\longrightarrow e^{6a_0^2}.
                                                               \tag{3.5}
\]

#### Proof

The first identity is (2.2). We give the coefficient argument for the two
remaining assertions, including the reason the cross error is
\(O(m^{-1})\), not merely \(O(m^{-1/2})\).

Put

\[
 p={m-q\over2m}={1\over2}+O_A(m^{-1/2}).             \tag{3.6}
\]

Give the four vertices of one square independent Bernoulli-\(p\) labels.
Let \(S\) be their sum and let \(A,B\) be their two internal-edge counts.
Conditioning the \(m/2\) independent squares on total sum \(m-q\) gives
the uniform target law. At one square,

\[
\begin{aligned}
 \operatorname {Cov}(A,B)&=4p^3(1-p),\\
 \operatorname {Cov}(A,S)&=\operatorname {Cov}(B,S)
                    =4p^2(1-p),\\
 \operatorname {Var}(S)&=4p(1-p).                 \tag{3.7}
\end{aligned}
\]

Consequently the conditional Gaussian cross covariance, namely the Schur
complement, vanishes identically:

\[
 \operatorname {Cov}(A,B)
 -{\operatorname {Cov}(A,S)\operatorname {Cov}(B,S)
       \over\operatorname {Var}(S)}=0.             \tag{3.8}
\]

There is no hidden cubic \(m^{-1/2}\) cross term. At \(p=1/2\), put

\[
 U=A-\tfrac12S+\tfrac12,\qquad
 V=B-\tfrac12S+\tfrac12.                            \tag{3.9}
\]

Enumeration of the sixteen subsets in (3.1) gives

\[
 \mathbb EUV=0,\qquad
 \mathbb EU^2V=\mathbb EUV^2=0.                    \tag{3.10}
\]

For completeness, the nonzero values needed for the cubic check are as
follows. The empty and full subsets give \((U,V)=(1/2,1/2)\).
The one- and three-subsets give \((0,0)\). Among two-subsets, the two
\(a\)-edges give \((1/2,-1/2)\), the two \(b\)-edges give
\((-1/2,1/2)\), and the two diagonals give \((-1/2,-1/2)\).
Their weighted cubic sums are zero. Since all one-square cumulants are
analytic in \(p\), the mixed conditional cubic cumulants are
\(O(|p-1/2|)=O_A(m^{-1/2})\). Mixed cumulants of total order at least four
are \(O_A(1)\) per square.

Here is why conditioning introduces no omitted cubic term. In the
three-variable cumulant generating function of \((A,B,S)\), eliminate the
\(S\)-parameter by the implicit equation which keeps its derivative equal
to \(4p\). Its first derivatives in the \(A\)- and \(B\)-directions are
respectively
\(-\operatorname {Cov}(A,S)/\operatorname {Var}(S)=-p\).
Consequently the quadratic derivatives are the Schur complement (3.8).
At \(p=1/2\), the mixed cubic derivative is the mixed third cumulant of the
efficient residuals \(U,V\) in (3.9): terms involving the second derivative
of the eliminated parameter are multiplied by
\(\operatorname {Cov}(U,S)\) or \(\operatorname {Cov}(V,S)\), both zero.
Thus (3.10) is exactly the conditional cubic calculation, not an
unconditioned proxy.

We now apply Cauchy's coefficient formula to (3.1) on the rank saddle

\[
 x_0={p\over1-p}.                                    \tag{3.11}
\]

The likelihood ratio (0.4) has logarithmic derivative
\(O_A(m^{-1/2})\) on the central \(O(\sqrt m)\) window. After centering and
scaling both edge counts by \(\sqrt m\), (3.8) removes the mixed quadratic
term. By (3.10) and (3.6), the mixed cubic term is

\[
 {m\over2}\,O_A(m^{-1/2})O_A(m^{-3/2})=O_A(m^{-1}), \tag{3.12}
\]

and every mixed term of order at least four is also \(O_A(m^{-1})\).
The one-variable terms are exactly the corresponding marginal saddle
expansions and cancel on subtracting the two marginal logarithms. Thus,
uniformly for the bounded likelihood tilts generated by (0.4),

\[
 \log {\mathbb E[g_{m,q}(f_a)g_{m,q}(f_b)]
       \over \mathbb E g_{m,q}(f_a)\,\mathbb E g_{m,q}(f_b)}
 =O_A(m^{-1}).                                      \tag{3.13}
\]

The part of the Cauchy integral outside a fixed central arc is
exponentially smaller: (3.1) has nonnegative coefficients, rank span one,
and its normalized modulus is strictly below one off that arc. The same
one-dimensional saddle estimate applied to (3.3) gives uniformly bounded
fourth likelihood moments, so truncating first to a growing central window
and then removing the truncation preserves (3.13). This proves the last two
claims in (3.4).

Finally, the standard quadratic term of the same displayed saddle
calculation can be read directly from (0.4). If

\[
 Y={4(f-\mathbb Ef)\over\sqrt m},                  \tag{3.14}
\]

then under the target law \(Y\Rightarrow N(0,1)\), uniformly on bounded
\(a_0=q/\sqrt m\), and

\[
 g_{m,q}(f)=\exp(2a_0Y-a_0^2+o(1))                 \tag{3.15}
\]

in every bounded likelihood moment. Hence its first and second moments
tend respectively to

\[
 e^{-a_0^2}e^{(2a_0)^2/2}=e^{a_0^2},\qquad
 e^{-2a_0^2}e^{(4a_0)^2/2}=e^{6a_0^2}.              \tag{3.16}
\]

This proves (3.5) and the lemma. \(\square\)

## 4. Simultaneous fractional profile cancellation

### Theorem 4.1 (linear orthogonal family)

Equations (0.7) and (0.8) hold.

#### Proof

The affine group is transitive on ordered pairs of distinct nonzero
directions: every \(M_a\cup M_b\) has the same square decomposition. Let
\(L=2m-1\). From Lemma 3.1,

\[
\begin{aligned}
 \mathbb E_T(\overline g_q-\lambda_q)^2
 &={1\over L}\operatorname {Var}(g_{m,q}(f_a))\\
 &\quad+{L-1\over L}
       \operatorname {Cov}(g_{m,q}(f_a),g_{m,q}(f_b))\\
 &=O_A(m^{-1}).                                      \tag{4.1}
\end{aligned}
\]

This is (0.7). Complementation maps a rank-\(m+q\) upper target to a
rank-\(m-q\) lower target and exchanges full and empty pairs, so the upper
calculation is identical. Since \(N_q\le W\), summing (0.7) over two signs
and \(H\le A\sqrt m\) gives

\[
 2\sum_{q=1}^HO_A(N_q/m)
 =O_A(HW/m)=O_A(W/\sqrt m),                         \tag{4.2}
\]

which is (0.8). \(\square\)

This theorem is exactly at the useful aggregate scale: its total squared
profile error through the Gaussian window is already \(o(W)\). It does not
select owner-disjoint cells from different resolutions.

## 5. Exact comparison with the floor baseline

For any real load vector \(z=(z_T)\) of total mass \(W=N_q\lambda_q\),
write \(c=c_q\), \(\theta=\theta_q\). The identity

\[
\begin{aligned}
 \sum_T(z_T-c)(z_T-c-1)
 &=\sum_T(z_T-\lambda_q)^2-N_q\theta(1-\theta)
\tag{5.1}
\end{aligned}
\]

is exact: the linear cross term vanishes because
\(\sum_T(z_T-\lambda_q)=0\). Applying (5.1) to (0.6) and using (0.7)
proves (0.10).

For integral \(z_T\), every summand on the left of (5.1) is nonnegative.
Thus (0.10) measures the exact variance which an integral rounding must
add: it must turn the fractional reserve
\(N_q\theta_q(1-\theta_q)\) into Bernoulli floor/ceiling fluctuations, but
must add no further linear variance.

### Theorem 5.1 (global-frame variance obstruction)

Let \(q=a\sqrt m+o(\sqrt m)\) with fixed \(a>0\). Any integral
fixed-frame trace assignment, and hence any law which chooses one entire
affine frame before making its within-frame choices, has expected floor
energy at least (0.11).

#### Proof

In one frame, targets of type \(f\) receive in total \(V_f\) occurrences.
The function

\[
 \phi_c(z)=(z-c)(z-c-1)                              \tag{5.2}
\]

is convex. Therefore every integral allocation within that type satisfies

\[
 \sum_{T:\,f_M(T)=f}\phi_c(Z_T)
 \ge T_{f,q}\phi_c(V_f/T_{f,q}).                    \tag{5.3}
\]

Summing (5.3), dividing by \(N_q\), and invoking Lemma 3.1 gives

\[
\begin{aligned}
 {Q_q\over N_q}
 &\ge \mathbb E\phi_c(g_{m,q}(f_M(T)))\\
 &=\mathbb E g_{m,q}(f_M(T))^2-(2c+1)\lambda_q+c(c+1)\\
 &\longrightarrow e^{6a^2}-(2c_\infty+1)e^{a^2}
                         +c_\infty(c_\infty+1)\\
 &=e^{6a^2}-e^{2a^2}-\vartheta(a)(1-\vartheta(a)). \tag{5.4}
\end{aligned}
\]

At a limiting integer value of \(e^{a^2}\), either adjacent choice of the
finite \(c_q\) gives the same last limit because
\(\theta_q(1-\theta_q)\to0\).

It remains only to check positivity. Put \(y=e^{a^2}>1\). If
\(1<y<2\), then

\[
 y^6-y^2-(y-1)(2-y)>y^6-y^2-(y-1)>0,              \tag{5.5}
\]

because the last expression vanishes at \(y=1\) and has derivative
\(6y^5-2y-1>0\) for \(y>1\). If \(y\ge2\), then
\(y^6-y^2\ge60>1/4\ge\vartheta(1-\vartheta)\). Thus
\(\gamma(a)>0\). The bound is identical for every affine frame, so taking
a law over whole frames cannot reduce it. \(\square\)

This is the precise max-versus-average obstruction. Formula (0.10) averages
the target loads first and then evaluates the quadratic. Theorem 5.1
evaluates every integral resolution first and then averages. Convexity
makes the difference linear.

## 6. Packet covariance identity and the exact remaining law

Let \(\nu\) be any law on integral owner-disjoint packet resolutions which
uses one literal depth-\(q\) trace per covered owner. For simplicity write
the exact-cover form; an owner leave \(L\) contributes the already audited
\(O(HL)\) correction. Let

\[
 I_P={\bf1}_{\{P\text{ is selected}\}},\qquad
 Z_T=\sum_P I_P{\bf1}_{\{T\in A_q(P)\}}.            \tag{6.1}
\]

Then

\[
 \sum_T\operatorname {Var}(Z_T)
 =\sum_{P,P'}K_q(P,P')\operatorname {Cov}(I_P,I_{P'}),
                                                               \tag{6.2}
\]

including the diagonal \(K_q(P,P)=|A_q(P)|\). This follows simply by
expanding both sides.

If \(\mathbb EZ_T=\overline g_q(T)\), then

\[
\begin{aligned}
 \mathbb E Q_q
 &=\sum_T\operatorname {Var}(Z_T)
   +\sum_T(\mathbb EZ_T-c)(\mathbb EZ_T-c-1)\\
 &=\sum_T\operatorname {Var}(Z_T)
   -N_q\theta_q(1-\theta_q)+O_A(N_q/m),             \tag{6.3}
\end{aligned}
\]

proving (0.13). Thus the summed identity (0.15) is the exact aggregate
variance target.

Put \(x_P=\mathbb EI_P\). In a catalogue diffuse at the protected
pointwise scale,

\[
 \sum_P|A_q(P)|x_P^2=o(W/H).                        \tag{6.4}
\]

Since \(\sum_P|A_q(P)|x_P=W\), the diagonal part of (6.2) is
\(W-o(W/H)\). Therefore the stronger pointwise form of (0.15) is equivalent
to

\[
\begin{aligned}
 \sum_{P\ne P'}K_q(P,P')\operatorname {Cov}(I_P,I_{P'})
 &=N_q\theta_q(1-\theta_q)-W+o(W/H)\\
 &=-N_q(c_q+\theta_q^2)+o(W/H),                     \tag{6.5}
\end{aligned}
\]

which proves (0.18). Without imposing a pointwise rate, the exact version
requires the sum over both signs and all \(q\le H\) of the left side of
(6.5) plus \(N_q(c_q+\theta_q^2)\) to be \(o(W)\).

Two tempting laws now fail for opposite reasons.

1. **One global frame.** It preserves owner integrality automatically, but
   Theorem 5.1 gives \(Q_q=\Omega_a(W)\) at every fixed positive Gaussian
   depth.
2. **Independent packet choices.** Their off-diagonal covariance is zero,
   so (6.3) gives
   \[
      \mathbb E Q_q
      =W-N_q\theta_q(1-\theta_q)+o(W)
      =N_q(c_q+\theta_q^2)+o(W).                    \tag{6.6}
   \]

The affine average solves neither integrality nor (6.5); it supplies an
exceptionally flat set of one-point marginals on which the remaining
correlation problem can be posed without a Gaussian profile bias.

## 7. Incorporating the two-sign cross-quartet shores

The affine four-cycles can host the exact shores from
MATH_THEOREM_TWO_SIGN_CROSS_QUARTET_PROFILE_TRANSPORT_20260726.md.
This removes a possible sign obstruction, but it also makes clear why
independent local shore choices do not provide (6.5).

Fix distinct directions \(a,b\). Their affine squares are the cosets of
\(\langle a,b\rangle\). For \(d\ge3\), pair these \(m/2\) squares
arbitrarily into disjoint ordered pairs \((A,B)\). On one such eight-set,
put

\[
 V_k^+=\binom Ak\times\binom B{k-1},\qquad
 V_k^-=\binom A{k-1}\times\binom Bk.                \tag{7.1}
\]

There are three owner shores whenever they are defined:

\[
 \mathsf B=\text{large-layer internal shore},\qquad
 \mathsf C=\text{cross shore},\qquad
 \mathsf S=\text{small-layer internal shore}.       \tag{7.2}
\]

After profile symmetrization, their lower and upper load vectors have the
form

\[
\begin{array}{c|ccc}
 &\mathsf B&\mathsf C&\mathsf S\\ \hline
 \text{lower}&L_0&L_0&L_1\\
 \text{upper}&U_0&U_1&U_1.
\end{array}                                         \tag{7.3}
\]

Indeed, \(\mathsf B\leftrightarrow\mathsf C\) preserves the lower
intersection profile and changes the upper union profile, while
\(\mathsf C\leftrightarrow\mathsf S\) changes the lower profile and
preserves the upper one.

### Proposition 7.1 (a common two-sign affine-square switch)

On the sectors \(k=2,3\), both \(\mathsf B\) and \(\mathsf S\) exist.
Replacing \(\mathsf B\) by \(\mathsf S\), either directly or through the
intermediate shore \(\mathsf C\), is an exact whole-packet owner trade
which changes both signed profiles. In one paired-square round its central
owner density is

\[
 {2\displaystyle\sum_{k=2}^3\binom4k\binom4{k-1}\over2^8}
 ={2(24+24)\over256}={3\over8}.                    \tag{7.4}
\]

The local shore choices on different paired affine squares can be tensored
to form a simultaneous product owner resolution. This statement is about
owner legality; it does not assert that their literal target derivatives
are additive.

#### Proof

For \(k=2,3\), the large-layer and small-layer one-factors both partition
the same owner set \(V_k^+\mathbin{\dot\cup}V_k^-\). Tensoring either with
the same disjoint \(Q_{r-1}\) reservoir gives two tilings by whole
\(Q_r\) packets. Equation (7.3) shows that both signs change. The local
owner masses are \(2\binom4k\binom4{k-1}\); summing and dividing by
\(2^8\) gives (7.4).

For simultaneous owner legality, partition the Boolean cube by the local
occupancy sector on every paired square, choose one local shore factor in
each nontrivial sector, and tensor the local factors. Their product edges
partition every product sector, and restricting to total rank \(m\)
preserves that partition. Thus the choices commute as factors in an owner
resolution. Notice, however, that one global packet can use axes from many
paired squares. Hence the owner regions of the corresponding *individual
trade descriptions* need not be disjoint. \(\square\)

Thus a common all-sign selection is physically available on positive
density. One does not have to choose the lower and upper repairs in
different owner resolutions.

The three-state geometry is also exact. If a random shore has probabilities
\((\alpha,\beta,\gamma)\) on
\((\mathsf B,\mathsf C,\mathsf S)\), put

\[
 X={\bf1}_{\{\mathsf S\}},\qquad
 Y={\bf1}_{\{\mathsf C,\mathsf S\}}.                \tag{7.5}
\]

Then \(X\le Y\) and

\[
\begin{aligned}
 \operatorname {Var}X&=\gamma(1-\gamma),\\
 \operatorname {Var}Y&=(\beta+\gamma)\alpha,\\
 \operatorname {Cov}(X,Y)&=\alpha\gamma\ge0.        \tag{7.6}
\end{aligned}
\]

The positive last covariance is between opposite signs. It is neither
helpful nor harmful to the floor objective, which is the sum of two
separate signed quadratic forms and has no lower--upper cross term.
Restricting to the common binary \(\mathsf B/\mathsf S\) switch makes
\(X=Y\), so it enforces one chronology for both signs exactly.

### 7.1 The joined derivative Gram, and the additivity gap

There are two different ways to use the local shores, and conflating them
would give a false covariance proof.

First suppose that an additional refinement has assigned owner-disjoint
trade regions to paired-square carriers indexed by \(b\). Choose the
\(\mathsf B/\mathsf S\) state \(X_b\in\{0,1\}\), and let
\(\Delta_{b,q,\epsilon}\) be the complete literal target-load derivative
of that switch, including the installed compiler chronology. Since the
owner trades are disjoint, their target ledgers add:

\[
 Z_{q,\epsilon}
 =Z^0_{q,\epsilon}+\sum_bX_b\Delta_{b,q,\epsilon}.   \tag{7.7}
\]

For an arbitrary joint law of the common switches,

\[
\begin{aligned}
 \sum_T\operatorname {Var}(Z_{q,\epsilon,T})
 &=\sum_{b,b'}\operatorname {Cov}(X_b,X_{b'})
       \mathcal G_{bb'}^{q,\epsilon},\\
 \mathcal G_{bb'}^{q,\epsilon}
 &:=\left\langle\Delta_{b,q,\epsilon},
                    \Delta_{b',q,\epsilon}\right\rangle.
                                                               \tag{7.8}
\end{aligned}
\]

This is the exact joined-owner cross-Gram for the affine-square shore
system. Combining (7.8) with (0.15), the common all-depth gate is

\[
\boxed{
 \sum_{\epsilon,q}\sum_{b,b'}
 \operatorname {Cov}(X_b,X_{b'})
       \mathcal G_{bb'}^{q,\epsilon}
 =
 \sum_{\epsilon,q}N_q\theta_q(1-\theta_q)+o(W).
 }                                                            \tag{7.9}
\]

Equivalently, after including the packet diagonal, (7.9) is (6.5). The
two-sign profile theorem determines which \(\Delta\)'s are nonzero at the
block-profile level, but it does not determine the literal inner products
\(\mathcal G_{bb'}^{q,\epsilon}\). Those depend on the common compiler
orders and on whether the two physical trace images coincide. Consequently
the number \(13/32\), or the common density \(3/8\), is a capacity statement
and not yet a covariance estimate.

### Proposition 7.2 (product shore choices retain the floor gap)

Suppose a transverse-square resolution is randomized independently over
its carrier blocks. At a fixed signed depth write its nonnegative block
contributions as

\[
 Z_T=\sum_bY_{b,T},                                   \tag{7.10}
\]

where the vectors \(Y_b\) are independent. If

\[
 \varepsilon_m:=\max_{b,T}\mathbb EY_{b,T}=o(1)       \tag{7.11}
\]

and \(\sum_{b,T}\mathbb EY_{b,T}=W-o(W)\), then

\[
 \sum_T\operatorname {Var}(Z_T)\ge W-o(W),            \tag{7.12}
\]

and hence

\[
 \mathbb E Q_q\ge N_q(c_q+\theta_q^2)-o(W).           \tag{7.13}
\]

Thus independent choices of the two-sign shores do not improve the
independent-packet floor obstruction.

#### Proof

An integer-valued nonnegative random variable satisfies \(Y^2\ge Y\).
Independence across \(b\) therefore gives

\[
\begin{aligned}
 \sum_T\operatorname {Var}(Z_T)
 &=\sum_{b,T}\left(\mathbb EY_{b,T}^2
                   -(\mathbb EY_{b,T})^2\right)\\
 &\ge\sum_{b,T}\mathbb EY_{b,T}
        -\varepsilon_m\sum_{b,T}\mathbb EY_{b,T}
 =W-o(W).                                            \tag{7.14}
\end{aligned}
\]

Insert (7.14) into (6.3) and use
\(W-N_q\theta_q(1-\theta_q)=N_q(c_q+\theta_q^2)\).
\(\square\)

Condition (7.11) is exactly the diffuse regime created by averaging many
transverse frames and stabilizer conjugates. If a positive mass is
deterministic within single carrier blocks, it must be separated before
applying Proposition 7.2; the proposition makes no assertion about that
non-diffuse part.

The only possible use of the two-sign shores at the floor scale is
therefore a genuinely dependent law across different affine-square
carriers. Its covariance matrix must have negative off-diagonal entries
whose Gram-weighted total is (7.9). Neither pairwise \(C_4\) transversality
nor the shore densities imply that assertion.

The natural product owner resolution from Proposition 7.1 is not yet in
this additive situation. Coordinate-disjoint carriers can occur in the
same global packet, and changing one local shore can change the compiler
order in which another carrier is met. For its Boolean shore vector
\(X=(X_b)\), the literal load has only the general Möbius expansion

\[
 Z_{q,\epsilon}(X)
 =Z^0_{q,\epsilon}
  +\sum_{\varnothing\ne J}\Delta^{q,\epsilon}_J
                  \prod_{b\in J}X_b.                         \tag{7.15}
\]

The two-sign profile identities determine the one-carrier block sizes, but
they do not prove \(\Delta_J=0\) for \(|J|\ge2\). Thus (7.8)--(7.9) are
the exact covariance gate **after** an owner-disjoint additive refinement;
they are not consequences of coordinate-disjoint tensoring alone.

The needed refinement can in fact be constructed.

### Theorem 7.3 (first-eligible additive shore resolution)

Let \(r=o(m)\), and suppose a valid \(Q_r\) compiler protects all
\(q\le H<r\). The paired affine squares admit an exact owner-disjoint
resolution by physical \(Q_r\) packets with the following properties.

1. Its owner leave satisfies
   \[
    L_r\le\sum_{e<r}\binom{m/4}{e}96^e160^{m/4-e}
       =2^{(\log_2(160)/4+o(1))m}
       =o(W/H).                                      \tag{7.16}
   \]
2. Every retained product region has one distinguished carrier on which
   either the \(\mathsf B\) or the \(\mathsf S\) shore may be chosen.
   Both choices tile exactly the same owner region and change both signed
   block profiles.
3. The product regions are owner-disjoint. Consequently their complete
   literal all-depth target derivatives are additive exactly as in (7.7).
4. Every region has exactly
   \[
                         24\cdot2^{r-1}=12\cdot2^r   \tag{7.16a}
   \]
   owners and either shore contains exactly twelve \(Q_r\) packets.

In particular, the affine shore additivity partition is not an additional
gate.

#### Proof

Write the paired affine squares as

\[
 C_1\dot\cup\cdots\dot\cup C_B=G,\qquad
 |C_i|=8,\qquad B={m\over4}.                         \tag{7.17}
\]

For an owner \(X\), call \(i\) eligible if its local pattern on \(C_i\)
lies in one of the \(k=2,3\) sectors

\[
 V_2^+\dot\cup V_2^-\dot\cup V_3^+\dot\cup V_3^-.
                                                               \tag{7.18}
\]

There are exactly

\[
 2\binom42\binom41+2\binom43\binom42=48+48=96       \tag{7.19}
\]

eligible subsets of one eight-set, and \(256-96=160\) ineligible ones.
Call \(X\) good if it has at least \(r\) eligible carriers.

Fix the local sector type \((k,+)\) or \((k,-)\) at every eligible
carrier. For a good sector vector, take the first \(r\) eligible indices
\[
 i_1<i_2<\cdots<i_r.                                 \tag{7.20}
\]
At every inactive index freeze the exact local subset. At the active
indices \(i_2,\ldots,i_r\), fix once and for all one internal local
one-factor and tag one edge of that factor. At \(i_1\), allow either the
large-layer factor
\(\mathsf B\) or the small-layer factor \(\mathsf S\). Both factors exist
for \(k=2,3\), separately partition each of \(V_k^+\) and \(V_k^-\), and
preserve the local sector type.

For fixed reservoir edge tags at \(i_2,\ldots,i_r\), let the distinguished
local subset at \(i_1\) range over its entire \(24\)-vertex sector
\(V_k^+\) or \(V_k^-\). Each of \(\mathsf B,\mathsf S\) partitions that
sector into twelve edges. Taking the product of one distinguished edge
with the \(r-1\) tagged reservoir edges gives a literal orientation cube
\(Q_r\). Thus either shore tiles a region of size
\(24\cdot2^{r-1}=12\cdot2^r\) by twelve \(Q_r\) packets.
As the reservoir edge tags range over their fixed factors, these regions
partition the former full product block. Local Johnson moves
within either shore preserve all eligibility indicators, all sector types,
and therefore the first-active list (7.20). Hence no cube leaves its
declared product region.

Different sector vectors or inactive tags define disjoint owner regions.
Thus choosing \(\mathsf B\) or \(\mathsf S\) independently as an
*integral state* of each region preserves owner disjointness. A valid
compiler is installed separately in every resulting \(Q_r\) packet, so
the total literal target ledger is the sum of the region ledgers. There
are no cross-region compiler intervals. This proves exact additivity and
properties 2--4.

It remains to count the leave. Ignoring the central-rank condition only
increases the number of bad owners. Choosing the \(e<r\) eligible blocks,
then their local patterns, gives the first bound in (7.16). Since
\(r=o(m)\),

\[
 \sum_{e<r}\binom{m/4}{e}96^e160^{m/4-e}
 \le160^{m/4}\exp(o(m)).                             \tag{7.21}
\]

Now \(\log_2(160)/4<2\), whereas
\(W=2^{2m-o(m)}\). Hence \(L_r/W=2^{-\Omega(m)}\), which is
\(o(1/H)\) for every \(H\le m\). This proves (7.16). \(\square\)

Theorem 7.3 removes all higher terms in (7.15) by changing the
decomposition, not by asserting that they vanish in the unrefined tensor
product. The actual remaining object is therefore the joined Gram
\(\mathcal G\) of the distinguished-region derivatives and a dependent
selection law satisfying (7.9).

There is also a uniform literal norm bound. Write \(R_0=2^r\). At one
signed depth, either shore of one region has \(12R_0\) target occurrences.
Trace injectivity inside each of its twelve packets implies that any fixed
target has shore load at most twelve. Hence

\[
\begin{aligned}
 \|\Delta_{b,q,\epsilon}\|_1&\le24R_0,\\
 \|\Delta_{b,q,\epsilon}\|_\infty&\le12,\\
 \|\Delta_{b,q,\epsilon}\|_2^2&\le288R_0,\\
 \|\Delta_b\|_2^2&\le576HR_0.                       \tag{7.21a}
\end{aligned}
\]

Since the retained regions partition \(S=W-L_r\) owners, their number is
\(S/(12R_0)\), and therefore

\[
 \sum_b\|\Delta_b\|_2^2\le48HS.                     \tag{7.21b}
\]

This places the centered-scatter problem at the correct \(HW\) scale. It
does not give the \(o(W)\)-accurate comparison with the floor baseline.

### Theorem 7.4 (exact fixed-slice selection law)

Let \(R\) owner-disjoint additive regions from Theorem 7.3 have common
two-sign derivative vectors

\[
 \Delta_b=\bigoplus_{\epsilon\in\{-,+\},\,q\le H}
                 \Delta_{b,q,\epsilon}
 \quad(1\le b\le R),                                 \tag{7.22}
\]

in the direct sum of all protected target spaces. Fix \(0\le s\le R\),
put \(p=s/R\), and choose uniformly an \(s\)-subset of the regions on which
to use shore \(\mathsf S\), using \(\mathsf B\) elsewhere. Then

\[
\begin{aligned}
 \mathbb EX_b&=p,\\
 \operatorname {Cov}(X_b,X_{b'})
 &=
 \begin{cases}
 p(1-p),&b=b',\\
 -p(1-p)/(R-1),&b\ne b',
 \end{cases}                                         \tag{7.23}
\end{aligned}
\]

and, with

\[
 \overline\Delta={1\over R}\sum_b\Delta_b,\qquad
 \mu=Z^0+p\sum_b\Delta_b,                            \tag{7.24}
\]

let \(S\) be the common total target-occurrence mass in each signed depth
(the number of retained owners), and put

\[
 \lambda_{q,S}={S\over N_q},\qquad
 c_{q,S}=\lfloor\lambda_{q,S}\rfloor,\qquad
 \theta_{q,S}=\lambda_{q,S}-c_{q,S}.                 \tag{7.24a}
\]

In this theorem \(Q\) denotes the sum of
\((Z_{q,\epsilon,T}-c_{q,S})(Z_{q,\epsilon,T}-c_{q,S}-1)\) over all
protected typed targets. Then the exact all-depth expected floor energy is

\[
\boxed{
\begin{aligned}
 \mathbb E Q
={}&{s(R-s)\over R(R-1)}
       \sum_{b=1}^R\|\Delta_b-\overline\Delta\|_2^2\\
 &+\sum_{\epsilon,q}
       \|\mu_{q,\epsilon}-\lambda_{q,S}{\bf1}\|_2^2
 -\sum_{\epsilon,q}N_q\theta_{q,S}(1-\theta_{q,S}).
                                                               \tag{7.25}
\end{aligned}}
\]

Consequently, if the right side of

\[
 {s(R-s)\over R(R-1)}
       \sum_b\|\Delta_b-\overline\Delta\|_2^2
 +\sum_{\epsilon,q}
       \|\mu_{q,\epsilon}-\lambda_{q,S}{\bf1}\|_2^2
 \le
 \sum_{\epsilon,q}N_q\theta_{q,S}(1-\theta_{q,S})+o(W)
                                                               \tag{7.26}
\]

holds, then one deterministic common all-\(q\), two-sign shore selection
has \(Q=o(W)\).

#### Proof

The covariance formula (7.23) is the elementary hypergeometric census:
two distinct indices lie in a uniform \(s\)-subset with probability
\(s(s-1)/(R(R-1))\). Hence

\[
\begin{aligned}
 \sum_{\epsilon,q,T}\operatorname {Var}(Z_{q,\epsilon,T})
 &=\sum_{b,b'}\operatorname {Cov}(X_b,X_{b'})
                  \langle\Delta_b,\Delta_{b'}\rangle\\
 &={p(1-p)R\over R-1}
       \left(\sum_b\|\Delta_b\|_2^2
              -{1\over R}\left\|\sum_b\Delta_b\right\|_2^2
       \right)\\
 &={s(R-s)\over R(R-1)}
       \sum_b\|\Delta_b-\overline\Delta\|_2^2.        \tag{7.27}
\end{aligned}
\]

Apply the exact identity (5.1) to the mean vector \(\mu\), then add the
variance (7.27). This proves (7.25). Since every realized \(Q\) is
nonnegative, (7.26) implies that at least one member of the finite support
has \(Q=o(W)\). \(\square\)

The same formula holds after stratifying regions by local sector type and
choosing a fixed number in every stratum: one sums the centered scatter in
(7.27) over strata. This is often necessary to preserve prescribed
one-point frame weights. Crucially, the same selected subset is used for
all \(q\) and both signs; no marginal-by-marginal rounding is hidden.

Theorem 7.4 is the promised deterministic selection law reduced to one
literal inequality. The two-sign shore theorem supplies the integral
states and Theorem 7.3 supplies simultaneous owner legality. What remains
uncomputed is the centered all-depth derivative scatter in (7.26).

## 8. Exact boundary

Proved here:

1. On \(2m=2^d\) coordinates there is a catalogue of only \(2m-1\)
   pairwise transverse frames.
2. Its stabilizer-symmetrized target loads have mean-square discrepancy
   \(O_A(1/m)\) at every signed depth \(q\le A\sqrt m\).
3. The total all-depth fractional discrepancy is
   \(O_A(W/\sqrt m)=o(W)\).
4. The exact four-cycle coefficient polynomial is (3.1); its absence of
   mixed quadratic and cubic saddle terms is the source of the gain.
5. Every whole-frame integral law retains the positive linear floor gap
   (0.11)--(0.12).
6. The required packetwise correction is exactly the negative covariance
   (0.18).
7. Paired affine \(C_4\) blocks carry a common lower/upper whole-packet
   switch on density \(3/8\); there is no residual one-sign support
   obstruction.
8. Independent local choices of those two-sign shores retain the linear
   floor gap under the exact diffuse hypothesis (7.11).
9. The first-eligible construction gives an exact owner-disjoint additive
   \(Q_r\)-packet resolution with exponentially small leave and one common
   two-sign binary shore variable in every retained product region.
10. Uniform fixed-slice sampling gives the exact common all-depth
    covariance formula (7.25) and a deterministic rounding theorem under
    the explicit centered-scatter inequality (7.26).

Not proved here:

* an owner-disjoint packet mosaic attaining (0.18);
* a resolution-flow or absorber which rounds the affine fractional mean;
* a proof of the centered-scatter inequality (7.26) for the physical
  compiler derivatives;
* an extension of the affine construction from the power-of-two subsequence
  to every \(2m\).

The complete-quartet/global-frame no-go does not apply to the first missing
item. The present theorem instead rules out a more specific shortcut:
orthogonal averaging may remove the fixed-profile bias, but evaluating its
mean before enforcing integral packet covariance is not a rounding theorem.
The next exact statement is an affine-square packet coupling whose selected
indicators have (6.5) simultaneously for all \(q\le H\).
