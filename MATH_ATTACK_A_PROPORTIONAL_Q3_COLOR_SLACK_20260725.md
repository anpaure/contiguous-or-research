# Proportional cyclic rounding closes the exact rank-three mixed cut

Date: 2026-07-25

Method: pure mathematics only. No computation, search, or solver is used.

## 1. Statement

Put

\[
n=2m+1,\qquad V_i=\binom{[n]}{m-i},\qquad N_i=|V_i|,
\qquad W=N_0,
\]

and

\[
r=W-N_1=\frac{2W}{m+2}.
\]

At transition \(V_2\to V_3\), the balanced-core/injective-residual
criterion is

\[
|\mathcal P|+|C_2\cap\mathcal P|
\le 2|\partial\mathcal P|-|R_3\cap\partial\mathcal P|
\qquad(\mathcal P\subseteq V_2),                 \tag{1.1}
\]

where

\[
|C_2|=N_1-N_2,\qquad |R_3|=r.                    \tag{1.2}
\]

### Theorem 1.1 — proportional cyclic rank-three slack

For all sufficiently large \(m\), there is a set \(C_2\subseteq V_2\)
of the exact size

\[
|C_2|=N_1-N_2=\frac4{m-1}N_2                    \tag{1.3}
\]

such that, for every \(R_3\subseteq V_3\) with \(|R_3|=r\), inequality
(1.1) holds for every \(\mathcal P\subseteq V_2\).

More precisely, write

\[
k=m-2,\qquad
T_m=\binom{2k-10}{k}=\binom{2m-14}{m-2},
\qquad
\beta_m=\frac{k-15}{k+6}=\frac{m-17}{m+4}.       \tag{1.4}
\]

For \(t=|\mathcal P|\), \(s=|\partial\mathcal P|\), and

\[
\operatorname{slack}(\mathcal P)
:=2s-|R_3\cap\partial\mathcal P|-t-|C_2\cap\mathcal P|,
\]

one has

\[
\operatorname{slack}(\mathcal P)
\ge
\left(s-|R_3\cap\partial\mathcal P|\right)
+\left(\frac{m-11}{m-2}s-t\right)\ge0
\quad(t\le T_m),                                 \tag{1.5}
\]

and

\[
\operatorname{slack}(\mathcal P)
\ge \beta_m t-r
\quad(t\ge T_m).                                 \tag{1.6}
\]

Moreover,

\[
\frac{T_m}{W}\longrightarrow 2^{-15},
\qquad \frac rW=\frac2{m+2},                     \tag{1.7}
\]

so (1.6) is positive for all sufficiently large \(m\). Thus the first
mixed core-high cut has no intrinsic obstruction after a bounded-overlap
proportional rounding.

## 2. Exact cyclic proportional rounding

Identify the ground set with \(\mathbb Z_n\). Partition \(V_2\) into
cyclic sum classes

\[
\mathcal K_a=
\left\{S\in V_2:\sum_{x\in S}x\equiv a\pmod n\right\},
\qquad a\in\mathbb Z_n.                           \tag{2.1}
\]

The union of the nine largest classes has size at least

\[
\frac9nN_2=\frac9{2m+1}N_2.
\]

For \(m\ge13\),

\[
\frac9{2m+1}\ge\frac4{m-1},                      \tag{2.2}
\]

so one may choose from that union a subfamily \(C_2\) of the exact size
(1.3). This rounding has the local-overlap bound

\[
\boxed{\deg_{C_2}(T):=
|\{S\in C_2:T\subset S\}|\le9
\qquad(T\in V_3).}                               \tag{2.3}
\]

Indeed, the supersets of a fixed \(T\in V_3\) are \(T\cup\{x\}\),
where \(x\in\mathbb Z_n\setminus T\). Their colors are

\[
\sum_{y\in T}y+x\pmod n,
\]

which are pairwise distinct as \(x\) varies. Each of the nine classes
therefore contributes at most one superset. Passing to a subfamily cannot
increase the degree.

Thus (2.3) is a deterministic local \(O(1/m)\)-overlap statement: among
the \(m+4\) rank-two supersets of a rank-three target, at most nine are
high.

## 3. Bounded-codegree mixed-cut lemma

### Lemma 3.1

Let \(L=\binom{[n]}k\), \(M=\binom{[n]}{k-1}\), where \(n=2k+5\).
Let \(C\subseteq L\) satisfy

\[
\max_{T\in M}|\{S\in C:T\subset S\}|\le D<k-6.   \tag{3.1}
\]

Let \(R\subseteq M\) have size \(r_0\). Put

\[
T_0=\binom{2k-D-1}{k},
\qquad
\beta=\frac{k-D-6}{k+6}.                         \tag{3.2}
\]

For every \(\mathcal P\subseteq L\), with \(t=|\mathcal P|\),
\(s=|\partial\mathcal P|\), and \(c=|C\cap\mathcal P|\), one has

\[
2s-|R\cap\partial\mathcal P|-t-c
\ge
\left(s-|R\cap\partial\mathcal P|\right)
+\left(1-\frac Dk\right)s-t\ge0                  \tag{3.3}
\]

when \(t\le T_0\), and

\[
2s-|R\cap\partial\mathcal P|-t-c
\ge\beta t-r_0                                   \tag{3.4}
\]

when \(t\ge T_0\).

#### Proof

Count incidences between \(C\cap\mathcal P\) and its facets. Every member
of \(C\cap\mathcal P\) has \(k\) facets, while every member of
\(\partial\mathcal P\) receives at most \(D\) such incidences. Hence

\[
kc\le Ds,\qquad c\le\frac Dk s.                  \tag{3.5}
\]

Suppose \(t\le T_0\), and write \(t=\binom xk\) in the Lovasz form.
Then \(x\le2k-D-1\), so Kruskal--Katona gives

\[
s\ge\binom{x}{k-1}
=\frac{k}{x-k+1}t
\ge\frac{k}{k-D}t.                               \tag{3.6}
\]

Consequently

\[
t+c\le t+\frac Dk s\le s.                        \tag{3.7}
\]

Together with \(|R\cap\partial\mathcal P|\le s\), this gives (3.3).

For arbitrary \(\mathcal P\), normalized matching between the two complete
Boolean ranks gives

\[
s\ge\frac{|M|}{|L|}t
=\frac{k}{n-k+1}t
=\frac{k}{k+6}t.                                 \tag{3.8}
\]

If \(t\ge T_0\), equations (3.5), (3.8), and
\(|R\cap\partial\mathcal P|\le r_0\) give

\[
\begin{aligned}
2s-|R\cap\partial\mathcal P|-t-c
&\ge\left(2-\frac Dk\right)s-t-r_0\\
&\ge
\left(\left(2-\frac Dk\right)\frac{k}{k+6}-1\right)t-r_0\\
&=\frac{k-D-6}{k+6}t-r_0.
\end{aligned}                                    \tag{3.9}
\]

This is (3.4). \(\square\)

### Corollary 3.2 — logarithmic local overlap is enough

Let \(D=D_m=o(m)\), and suppose a physically produced rank-two high set
\(C_2\) obeys

\[
\max_{T\in V_3}\deg_{C_2}(T)\le D.
\]

If, for some fixed \(\varepsilon>0\),

\[
D\le(1-\varepsilon)\log_2m,                      \tag{3.10}
\]

then every rank-three mixed cut holds uniformly for every \(R_3\) of
size \(r\), for all sufficiently large \(m\).

Indeed, uniformly under (3.10),

\[
\frac{\binom{2k-D-1}{k}}{W}
=2^{-D-6}\exp\!\left(O\!\left(\frac{D^2+1}{m}\right)\right),             \tag{3.11}
\]

while \(\beta=1-o(1)\) and \(r/W=2/(m+2)\). Thus
\(\beta T_0/r\to\infty\), and Lemma 3.1 applies. In particular, the
rank-three Hall argument needs only a sublogarithmic (or suitably
one-sided logarithmic) **maximum** local overlap; constant nine is a
convenient explicit realization, not the threshold.

## 4. Proof of Theorem 1.1

Apply Lemma 3.1 with

\[
k=m-2,\qquad D=9,\qquad C=C_2,\qquad R=R_3,\qquad r_0=r.
\]

Then (3.2)--(3.4) become (1.4)--(1.6). Finally,

\[
\frac{\binom{2m-14}{m-2}}{\binom{2m+1}{m}}
=
\frac{m(m-1)\prod_{j=-11}^{1}(m+j)}
     {\prod_{j=-13}^{1}(2m+j)}
\longrightarrow2^{-15},                          \tag{4.1}
\]

whereas \(r/W=2/(m+2)\to0\), and \(\beta_m\to1\). Hence
\(\beta_mT_m>r\) for all sufficiently large \(m\). This proves every cut
(1.1). \(\square\)

## 5. Exact construction consequence and remaining seam

Suppose the rank-two core has high set \(C_2\) as above and
\(R_2\subseteq V_2\setminus C_2\) is the rank-two residual image. The
ordinary residual SDR

\[
R_2\longrightarrow R_3\subseteq V_3,\qquad |R_3|=r,
\]

exists for all sufficiently large \(m\) by Lovasz--Kruskal--Katona
(indeed \(r\ll\binom{2m-5}{m-2}\)). Theorem 1.1 applies to whatever
image \(R_3\) that matching produces. The exact coupled Hall theorem
therefore extends the balanced core and injective residual through rank
three.

Thus the rank-three mixed cut itself is closed by a proportional profile
whose local overlap is \(9/(m+4)=O(1/m)\). The remaining compatibility
question lies one step earlier: construct the rank-two core and residual
so that this bounded-codegree exact high set \(C_2\) is realized and is
disjoint from \(R_2\). That realization is not proved here; no claim of a
full proportional-atom matching or of the constant-one theorem is made.

There is also a precise distinction from the proportional tight-atom
profile. In that profile, \(p b_{-2}\) rank-two targets occur once and the
remainder \(N_2-pb_{-2}<p\) is repaired separately. This is not the same
object as an \(N_1\)-mass core row whose loads are \(1+\mathbf1_{C_2}\).
To invoke Theorem 1.1 for physical atoms one must still prove a
disaggregation/regrouping theorem producing a common rank-two row with
the displayed high set (or at least the maximum-overlap condition of
Corollary 3.2), while preserving the rank-one residual ownership and the
same-start interval geometry. The rank-dependent scalar counts \(b_q\)
and the averaged \(O(1/m)\) atom-overlap sum do not by themselves imply
that statement.

## 6. Adversarial audit

1. No equidistribution of sum classes is assumed. The nine largest classes
   have the required total size by averaging, and arbitrary truncation
   preserves (2.3).
2. The color argument uses only distinct added coordinates modulo \(n\);
   primality and free cyclic orbits are irrelevant.
3. The small-cut proof uses the worst possible bound
   \(|R_3\cap\partial\mathcal P|\le s\), not an expectation.
4. The large-cut proof uses only \(|R_3|=r\).
5. Realizing the displayed \(C_2\) in the preceding rank-two flow remains
   a genuine seam. Treating it as automatic would be invalid.
6. The intrinsic \(O(1/m)\) overlap sum for proportional atoms is an
   averaged conditional statement. Corollary 3.2 assumes a maximum
   downward codegree for one integral physical row; passing from the
   former to the latter is not justified by Markov's inequality or by
   marginal balance.
