# Lane N master redirect: adaptive adjacent-deletion orientation

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
long computation is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn=\operatorname{Cat}_m,
\]

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,qquad
\rho_q=\theta_qN_q,
\]
and (K=\lceil A\sqrt m\rceil), where (A>0) is fixed.

The adaptive orientation theorem \(\mathrm{AO}_A\), equivalently the
one-pass version of \(\mathrm{SDH}_A\), is **not proved or disproved here**.
No exact-factor counterexample to its existential assertion was found. The
turn does, however, produce four new exact results.

1. There is an exact ownerwise global cost potential. The total weighted
   toggle cost is half a weighted Spearman footrule of the final
   interval-rotation permutation; unweighted cost is also its Kendall
   inversion number. This removes all residual online ambiguity.

2. The natural interval-configuration matrix has a universal determinant-
   two minor already on one owner and three stages. Thus direct total
   unimodularity and balanced-matrix proofs fail in every sufficiently long
   fixed window, without any owner collision or packet-completion issue.

3. The full Hall test for a containment star has two sides. Both the
   internal side and the complementary resource side admit exact
   history-robust cyclic-residence estimates. For every fixed order (t),
   every (t)-star and its complement are automatically Hall-safe at

   \[
   K-O_{A,t}(1)
   \]

   depths, simultaneously for all (t)-sets, every exact factor, and every
   earlier balanced swap history. More generally, if
   (t_*=O(\log m)) and (2^{t_*}=o(\sqrt m)), then all containment stars
   of orders (1\le t\le t_*) are safe at

   \[
   K-O_A(2^{t_*})
   \]

   depths. This corrects the earlier one-sided star analysis.

4. There are exact history-invariant core-shadow Hall obstructions, a
   literal homogeneous cyclic-packet counterexample to inference from
   homogeneous middle-ownership and packet moments, and an exact lower
   bound on depth-one recourse in the canonical MSW factor and its edit
   neighbourhood. The latter has the audited certificate constant

   \[
   T_1\ge
   \left(\frac{275}{19321}-o(1)\right)B
   =\left(\frac{275}{38642}+o(1)\right)\frac Wm.
   \]

These results definitively rule out a uniform positive full-graph
Cheeger/conductance theorem, recourse potentials depending only on
point/deletion marginals, direct configuration-matrix TU, and rounding
based only on homogeneous middle
ownership and the recorded pair moments, and an \(o(B)\)-recourse
construction in an \(o(B)\)-row neighbourhood of canonical MSW. They do
not close the existential
\(o(W)\)-recourse theorem: fixed-order quota-wall cuts, growing-order or
nonstar Hall families, and packet-specific short transport remain genuine.

## 1. Exact global cost potential

Fix one owner (X), with canonical deletion word

\[
a_1,a_2,\ldots,a_{K+1}.
\]

An ascending one-pass trajectory is equivalently a composition of these
positions into consecutive blocks. A nontrivial block ([s,t]) is rotated
left:

\[
(a_s,a_{s+1},\ldots,a_t)
\longmapsto
(a_{s+1},\ldots,a_t,a_s),
\]

and it toggles exactly the stages (s,s+1,\ldots,t-1).

Let (w_q>0) be arbitrary stage weights and define

\[
\Omega(1)=0,\qquad
\Omega(j)=\sum_{q<j}w_q
\quad(2\le j\le K+1).
\]

Let \(\operatorname{pos}_\sigma(a_i)\) be the position of (a_i) after
all block rotations.

### Theorem 1.1 -- weighted footrule identity

For every owner trajectory,

\[
\boxed{
\sum_{q=1}^K w_q\varepsilon_q(X)
=\frac12\sum_{i=1}^{K+1}
\left|
\Omega(\operatorname{pos}_\sigma(a_i))-\Omega(i)
\right|.}
\tag{1.1}
\]

With (w_q=1),

\[
\boxed{
\sum_q\varepsilon_q(X)
=\operatorname{inv}(\sigma)
=\frac12\sum_i
|\operatorname{pos}_\sigma(a_i)-i|.}
\tag{1.2}
\]

Thus the toggle count is simultaneously the Kendall distance and half the
Spearman footrule for this interval-rotation language.

#### Proof

On one block ([s,t]), (a_s) moves from (s) to (t), while every
(a_i), (s<i\le t), moves from (i) to (i-1). Hence the contribution
to the right side of (1.1), before division by two, is

\[
|\Omega(t)-\Omega(s)|
+\sum_{i=s+1}^t|\Omega(i)-\Omega(i-1)|
=2\sum_{q=s}^{t-1}w_q.
\]

Different blocks are disjoint, so summation proves (1.1). In the unweighted
case the only inversions created by this block are the (t-s) pairs in
which (a_s) crosses a later block letter. This proves (1.2). \(\square\)

The theorem applies in particular to (w_q=1/c_q). Since (c_q=O_A(1))
on a fixed Gaussian window, it is quantitatively equivalent to unweighted
recourse.

### Theorem 1.2 -- exact carry-age identity

If the carried letter before stage (q) originated at position (s_q), put

\[
A_q=q-s_q.
\]

Then

\[
\boxed{
\sum_{q=1}^K\varepsilon_q(X)
=A_{K+1}+\sum_{q:\,\varepsilon_q(X)=0}A_q.}
\tag{1.3}
\]

#### Proof

Every maximal toggle run of length (ell) either ends immediately before a
no-toggle stage, where the carry age is (ell), or reaches the final
boundary, where (A_{K+1}=ell). These contributions partition all toggled
stages. \(\square\)

Equation (1.3) is an exact accumulated-age potential, but not an upper bound:
the feasibility constraints may force old carries.

### Corollary 1.3 -- almost every row is almost canonical

Suppose a complete trajectory has total unweighted cost

\[
T=\delta_mW,\qquad \delta_m\to0.
\]

Then all but at most (\sqrt{\delta_m}B) wreath rows contain at most
(\sqrt{\delta_m}n) toggled owner-stage pairs. In every remaining row, all
but at most (\sqrt{\delta_m}n) owners are canonical at every depth.

#### Proof

There are (B) rows and (W=nB). Markov's inequality applied to the
rowwise toggle counts gives

\[
\#\{R:T(R)>\sqrt{\delta_m}n\}
\le\frac{\delta_mnB}{\sqrt{\delta_m}n}
=\sqrt{\delta_m}B.
\]

Every noncanonical owner has at least one toggled stage. \(\square\)

This is a strong necessary packet-stability statement: an \(o(W)\)-cost
construction cannot reroute a positive proportion of owners in a positive
proportion of rows.

### Exact marginal blindness

Apply the same nontrivial block rotation ([s,t]) to all (n) shifted
owners in one genuine wreath row. At each depth the resulting (n) chosen
sets are cyclic translates of one fixed rank-(r) pattern, so every
coordinate occurs exactly (r) times. At each final deletion position the
deleted coordinates also run once through all (n) labels. Consequently
every depth-point marginal and every deletion-position coordinate marginal
is unchanged, although the exact cost is

\[
n(t-s).
\tag{1.4}
\]

Applying the operation in every row gives cost (W(t-s)) while preserving
all those marginals globally. Therefore no potential depending only on
point marginals and deletion-position marginals can control ownerwise
recourse, even on genuine exact-factor packets.

## 2. A universal direct-integrality obstruction

The static formulation has one column for every interval composition of
every owner and one target-incidence row for each pair ((q,S)).

### Theorem 2.1 -- universal determinant-two minor

For every exact factor and every (K\ge3), the natural interval-
configuration matrix is neither totally unimodular nor balanced.

#### Proof

Fix one owner and three distinct stages (q_1,q_2,q_3). For (i=1,2,3),
take the valid configuration which toggles only at (q_i). A single toggle
changes precisely its own depth and resets at the next no-toggle stage.

Restrict to the three rows

\[
(q_i,L_{q_i}(X)),\qquad i=1,2,3.
\]

The selected submatrix, up to simultaneous row and column permutation, is

\[
\begin{pmatrix}
0&1&1\\
1&0&1\\
1&1&0
\end{pmatrix},
\qquad \det=2.
\tag{2.1}
\]

It is also the forbidden odd-cycle submatrix for balanced matrices. \(\square\)

This theorem needs no collision between owners and occurs inside every
exact factor. It rules out TU or balancedness of the direct configuration
matrix. It does **not** rule out an extended network formulation: the path
language of one owner alone has such an extension. Nor does it by itself
give an integrality gap for the particular balanced right-hand side.

## 3. The exact two-sided containment-star theorem

At stage (q), put (r=m-q). For owner (X), write its two current
endpoints as

\[
A_X=L_q(X),\qquad
B_X=L_{q+1}(X)\cup\{\kappa_q(X)\}.
\]

Their bottom, top, and difference pair are

\[
C_X=A_X\cap B_X=L_{q+1}(X),
\]

\[
R_X=A_X\cup B_X=P_{q-1}(X),
\qquad
p_X=R_X\setminus C_X
=\{a_{q+1}(X),\kappa_q(X)\}.
\tag{3.1}
\]

The core (C_X) and anchor (A_X) are canonical and history-independent;
the top and the second difference label may depend on the entire preceding
carry history.

For a nonempty (t)-set (T), let

\[
U_T=\{S\in\tbinom{[n]}r:T\subseteq S\},
\qquad
u_t=|U_T|=\binom{n-t}{r-t}.
\tag{3.2}
\]

Let \(\iota_q(T)\) be the number of owner edges internal to (U_T), and
let \(\eta_q(T)\) be the number incident with (U_T).

For a wreath row \(\pi\), define

\[
a_\pi(T)=
\#\{j:T\subseteq I_\pi(j,m)\}.
\]

Exact middle ownership gives

\[
\sum_{\pi\in F}a_\pi(T)=\binom{n-t}{m-t},
\qquad
0\le a_\pi(T)\le m-t+1.
\tag{3.3}
\]

### Lemma 3.1 -- exact cyclic residence

Let

\[
M_s^F(T)=
\#\{X:T\subseteq L_s(X)\}.
\]

Then, for every (s\le m-t),

\[
\boxed{
M_s^F(T)=\sum_{\pi\in F}(a_\pi(T)-s)_+.}
\tag{3.4}
\]

#### Proof

If \(T\) is contained in no length-\(m\) interval of a row, both sides
contribute zero. Otherwise, because \(n=2m+1\), a set fitting in an
\(m\)-interval has a unique short cyclic covering arc: its complementary
cyclic gap has at least \(m+2\) edges, equivalently at least \(m+1\)
omitted internal vertices. Two such gaps cannot fit in a cycle of
\(2m+1\) edges, so it is unique. If this covering arc has length \(\ell\),
then exactly \(m-\ell+1=a_\pi(T)\) length-\(m\) intervals contain it.
Shortening the window to length \(m-s\) removes exactly \(s\) possible
starts, leaving \((a_\pi(T)-s)_+\). Sum over rows. \(\square\)

### Lemma 3.2 -- internal and incident identities

For every earlier history,

\[
\boxed{\iota_q(T)=M_{q+1}^F(T).}
\tag{3.5}
\]

Moreover,

\[
\boxed{
\eta_q(T)
=\#\{X:T\subseteq R_X\}-\Sigma_q(T),}
\tag{3.6}
\]

where

\[
\Sigma_q(T)=
\#\{X:p_X\subseteq T,
\ T\setminus p_X\subseteq C_X\}.
\tag{3.7}
\]

In particular,

\[
\boxed{
\eta_q(T)\ge M_q^F(T),
\qquad
\Sigma_q(T)\le tB.}
\tag{3.8}
\]

#### Proof

Both endpoints contain (T) exactly when their intersection (C_X)
contains (T), proving (3.5).

At least one endpoint contains (T) exactly when (T\subseteq R_X),
except that if both difference letters lie in (T), the two endpoints split
those letters and neither contains all of (T). The remaining (t-2)
letters must lie in the core; this is precisely (3.7), proving (3.6).

Every edge whose anchor (A_X=L_q(X)) contains (T) is incident with
(U_T), giving the first inequality in (3.8). For the second, in each
wreath row the map (X\mapsto a_{q+1}(X)) is a bijection onto the (n)
coordinates. An edge counted by (3.7) has (a_{q+1}(X)\in T), so there are
at most (t) such edges per row. \(\square\)

The residual containment condition in (3.7) is essential. For (t=2) it
is empty, but for (t>2) one may not subtract every edge with
(p_X\subseteq T).

### Lemma 3.3 -- the two quota margins

Write (N=N_q), (c=c_q), \(\rho=\rho_q\), and

\[
\alpha=\frac{u_t}{N}=\frac{(r)_t}{(n)_t}.
\]

The largest and smallest mass which a floor/ceiling-balanced quota can put
on (U_T) are

\[
\mathcal C_q^+(U_T)
=cu_t+\min\{u_t,\rho\},
\tag{3.9}
\]

\[
\mathcal C_q^-(U_T)
=cu_t+\max\{0,\rho-(N-u_t)\}.
\tag{3.10}
\]

The Hall rows for (U_T) and its complement are exactly

\[
\boxed{
\iota_q(T)\le\mathcal C_q^+(U_T),
\qquad
\eta_q(T)\ge\mathcal C_q^-(U_T).}
\tag{3.11}
\]

If \(\theta=\rho/N\), their margins about proportional mass are

\[
\mathcal C_q^+(U_T)-\lambda_qu_t
=N
\begin{cases}
\theta(1-\alpha),&\theta\le\alpha,\\
\alpha(1-\theta),&\theta\ge\alpha,
\end{cases}
\tag{3.12}
\]

and

\[
\lambda_qu_t-\mathcal C_q^-(U_T)
=N
\begin{cases}
\theta\alpha,&\theta\le1-\alpha,\\
(1-\theta)(1-\alpha),&\theta\ge1-\alpha.
\end{cases}
\tag{3.13}
\]

Both are at least

\[
N\min\{\alpha,1-\alpha\}
\operatorname{dist}(\lambda_q,\mathbb Z).
\tag{3.14}
\]

#### Proof

Equations (3.9)--(3.10) follow by placing as many, or as few, of the
(\rho) high cells in (U_T) as possible. An orientation exists with
vertex indegrees in \(\{c,c+1\}\) exactly when every internal-edge count
is at most the maximum quota mass. Applying the same inequality to
(U_T^c), and using

\[
|E|=\iota(U_T)+\iota(U_T^c)+|\partial U_T|,
\]

gives the incident lower row in (3.11). Direct substitution proves
(3.12)--(3.14). \(\square\)

### Theorem 3.4 -- exact two-sided star bounds

For (1\le t\le r-1),

\[
\boxed{
\iota_q(T)
\le
\binom{n-t}{m-t}
\frac{(m-t-q)_+}{m-t+1}.}
\tag{3.15}
\]

Consequently

\[
\iota_q(T)-\lambda_qu_t
\le E^+_{q,t},
\tag{3.16}
\]

where

\[
\boxed{
E^+_{q,t}
=\frac{W}{(n)_t}
\left[(m)_{t-1}(m-q-t)-(m-q)_t\right]_+.}
\tag{3.17}
\]

On the resource side,

\[
\lambda_qu_t-\eta_q(T)
\le E^-_{q,t},
\tag{3.18}
\]

where

\[
\boxed{
E^-_{q,t}
=\left[
qB-\frac{W}{(n)_t}
\bigl((m)_t-(m-q)_t\bigr)
\right]_+.}
\tag{3.19}
\]

For fixed (A,t), uniformly for (q\le K),

\[
\frac{E^+_{q,t}}{N_q}=O_{A,t}(q/m),
\qquad
\frac{E^-_{q,t}}{N_q}=O_A(q/m).
\tag{3.20}
\]

#### Proof

On (0\le a\le L=m-t+1), the chord inequality gives

\[
(a-q-1)_+
\le a\frac{(L-q-1)_+}{L}.
\]

Use (3.3)--(3.5) to obtain (3.15). Since

\[
\binom{n-t}{m-t}=\frac{W(m)_t}{(n)_t},
\qquad
\lambda_qu_t=\frac{W(m-q)_t}{(n)_t},
\]

cancelling (m-t+1) gives (3.17).

For the other side, (3.4) and ((a-q)_+\ge a-q) give

\[
\eta_q(T)\ge M_q^F(T)
\ge\binom{n-t}{m-t}-qB.
\]

Subtract this from proportional mass to get (3.19).

Finally,

\[
\left[(m)_{t-1}(m-q-t)-(m-q)_t\right]_+
\le (m)_t-(m-q)_t
=O_t(qm^{t-1}),
\]

while (E^-_{q,t}\le qB=qW/n). Divide by (N_q=W/\lambda_q), and use
\(\lambda_q=O_A(1)\). \(\square\)

The leading fixed-(t) expansions are informative:

\[
(m)_{t-1}(m-q-t)-(m-q)_t
=((t-1)q-1)m^{t-1}
+O_t((q+1)^2m^{t-2}),
\tag{3.21}
\]

and

\[
\frac{E^-_{q,t}}{N_q}
\le
\lambda_q
\left[
\left(\frac12-\frac{t}{2^t}\right)\frac qm
+O_t\left(\frac{(q+1)^2}{m^2}\right)
\right]_+.
\tag{3.22}
\]

For (t=1), both error terms vanish exactly. For (t=2),

\[
\iota_q(\{x,y\})\le\frac B2(m-q-2),
\tag{3.23}
\]

and

\[
E^-_{q,2}=\frac{Bq(q+1)}{2m}.
\tag{3.24}
\]

### Theorem 3.5 -- fixed-order quota-wall localization

Fix (A>0) and (t\ge1). Uniformly over every exact factor, every
earlier balanced swap history, and every (t)-set (T), failure of either
Hall row in (3.11) at a depth (q\le K) implies

\[
\boxed{
\operatorname{dist}(\lambda_q,\mathbb Z)
=O_{A,t}(q/m).}
\tag{3.25}
\]

Consequently both Hall rows are automatically safe, simultaneously for all
(t)-sets, at

\[
\boxed{K-O_{A,t}(1)}
\tag{3.26}
\]

depths. Point stars ((t=1)) are safe at every depth, including quota
walls.

#### Proof

For fixed (t), \(\alpha=(m-q)_t/(n)_t\) stays in a compact subinterval
of ((0,1)) throughout the fixed Gaussian window. If the internal row
fails, (3.14), (3.16), and (3.20) imply (3.25). If the incident row fails,
(3.14), (3.18), and (3.20) give the same conclusion.

The exact increment is

\[
\lambda_{q+1}-\lambda_q
=\lambda_q\frac{2(q+1)}{m-q}.
\tag{3.27}
\]

Only (O_A(1)) integers lie below
\(\lambda_K\le e^{A^2+o(1)}\). Near every crossed integer at least two,
the increment and the collar in (3.25) have the same (q/m) scale, so the
collar contains only (O_{A,t}(1)) depths. Near one,

\[
\lambda_q-1\ge\frac{q(q+1)}m,
\]

so (3.25) forces (q=O_{A,t}(1)). Summing over crossed integers proves
(3.26).

For (t=1), (3.17) and (3.19) are zero, so proportional mass itself lies
between the two exact quota margins and both rows are safe even at a wall.
\(\square\)

The conclusion concerns both a star and its complement. Checking only
(3.15) is not a full Hall test.

### Theorem 3.6 -- slowly growing star order

Let (t_*=t_*(m)=O(\log m)) satisfy

\[
2^{t_*}=o(\sqrt m).
\tag{3.28}
\]

Uniformly for all (1\le t\le t_*), all (t)-sets (T), all exact
factors, and all earlier balanced histories, both star Hall rows are safe
at

\[
\boxed{K-O_A(2^{t_*})}
\tag{3.29}
\]

depths.

#### Proof

Uniformly for (t\le t_*) and (q\le A\sqrt m),

\[
\alpha=\frac{(m-q)_t}{(2m+1)_t}
=2^{-t}(1+o_A(1)).
\tag{3.30}
\]

Indeed, the logarithm of the ratio differs from (-t\log2) by
(O_A(tq/m+t^2/m)=o(1)).

Also

\[
1-\frac{(m-q)_t}{(m)_t}
\le\sum_{i=0}^{t-1}\frac q{m-i}
=O(tq/m).
\]

In particular, without using the fixed-\(t\) constants hidden in (3.20),

\[
\frac{E^+_{q,t}}{N_q\alpha}
\le
\lambda_q\left(\frac{(m)_t}{(m-q)_t}-1\right)
=O_A(tq/m),
\]

and

\[
\frac{E^-_{q,t}}{N_q\alpha}
\le\frac{qB}{N_q\alpha}
=O_A(2^tq/m).
\]

Equations (3.14), (3.16), and (3.18) therefore show that failure of an internal row
forces

\[
\operatorname{dist}(\lambda_q,\mathbb Z)=O_A(tq/m),
\]

whereas failure of a resource row forces

\[
\operatorname{dist}(\lambda_q,\mathbb Z)
=O_A(2^tq/m).
\tag{3.31}
\]

The latter contains the former. By (3.27), the largest collar, for
(t=t_*), contains (O_A(2^{t_*})) depths around every integer at least
two. Near one, comparison with
\(\lambda_q-1\ge q(q+1)/m\) gives (q=O_A(2^{t_*})). There are only
(O_A(1)) crossed integers. This proves (3.29). \(\square\)

For example, (t_*=\lfloor(\log_2m)/4\rfloor) eliminates every
containment star of order at most (t_*) at all but (O_A(m^{1/4})) of
the (\Theta_A(\sqrt m)) depths.

This does not eliminate a single fixed-order star at its finitely many
quota walls, a growing-order star outside (3.28), or a nonstar Hall family.

## 4. History-invariant core-shadow obstructions

Fix a rank-((r-1)) core (C), and let

\[
U_C=\{C\cup\{x\}:x\notin C\},
\qquad
|U_C|=n-r+1=m+q+2.
\tag{4.1}
\]

### Theorem 4.1 -- exact core-star obstruction

For every earlier history,

\[
\boxed{
e_{G_q}(U_C)=\mu_{q+1}^F(C).}
\tag{4.2}
\]

Therefore Hall feasibility necessarily requires

\[
\boxed{
\mu_{q+1}^F(C)
\le c_q(m+q+2)
+\min\{m+q+2,\rho_q\}.}
\tag{4.3}
\]

More generally, for
\(\mathcal C\subseteq\binom{[n]}{r-1}\),

\[
\boxed{
\sum_{C\in\mathcal C}\mu_{q+1}^F(C)
\le
c_q|\partial^+\mathcal C|
+\min\{|\partial^+\mathcal C|,\rho_q\}}
\tag{4.4}
\]

is necessary.

#### Proof

The two endpoints of every owner edge have intersection (L_{q+1}(X)).
Both lie in (U_C) exactly when this rank-((r-1)) intersection is (C),
proving (4.2). Apply the maximum quota-mass Hall row (3.9).

If an owner core belongs to \(\mathcal C\), both endpoints lie in
\(\partial^+\mathcal C\). Thus the left side of (4.4) is at most the
number of edges internal to that upper shadow, and Hall gives (4.4).
\(\square\)

Earlier toggles cannot repair a violation: they alter the second endpoint
but not the intersection.

There is also a support consequence with no numerical slack. Every endpoint
of every stage-(q) edge contains its canonical core. Since (c_q\ge1), a
balanced orientation cannot have an isolated rank-(r) target. Therefore

\[
\boxed{
\partial^+\operatorname{supp}(\mu_{q+1}^F)
=\binom{[n]}r}
\tag{4.5}
\]

is necessary at every controlled depth. This condition, like (4.3), is
unchanged by the whole preceding adaptive history.

At (q=1), for all sufficiently large (m), (4.3) is

\[
\boxed{\mu_2^F(C)\le2(m+3).}
\tag{4.6}
\]

### Lemma 4.2 -- exact local resource cap

For every rank-((m-q-1)) core (C),

\[
\boxed{
(q+2)\mu_{q+1}^F(C)
\le\binom{m+q+2}{q+1}.}
\tag{4.7}
\]

#### Proof

One row in which (C) is a cyclic interval contains exactly (q+2)
middle (m)-windows containing (C). Different selected rows own disjoint
middle sets. There are exactly

\[
\binom{n-|C|}{m-|C|}
=\binom{m+q+2}{q+1}
\]

middle supersets of (C). \(\square\)

At (q=1), (4.7) gives only

\[
3\mu_2(C)\le\binom{m+3}{2},
\tag{4.8}
\]

quadratic in (m), while Hall demands the linear bound (4.6).

This gap is real at the local packet-resource level. Put (v=m+3). A
maximal edge-disjoint packing of three-edge paths (P_4) in (K_v) leaves
a graph containing no three-edge path. Every connected component of such a
leave is a star or a triangle, so the leave has at most (v) edges. Hence
one can pack at least

\[
\frac{\binom v2-v}{3}
\tag{4.9}
\]

edge-disjoint paths. For \(v\ge16\), this is already more than the
\(2v\) occurrences allowed by the Hall cap (4.6). A path \(b-a-x-y\) is
realized locally by the cyclic segment

\[
b,a,C,x,y;
\]

the three middle windows containing \(C\) use the supersets corresponding
to the path edges \(ba,ax,xy\). Thus these are locally compatible legal
rows whose certified \(C\)-containing owner windows are disjoint. The other
\(n-3\) windows of different rows may collide.

No simultaneous completion of this local packing into one exact factor is
proved. Therefore it is not an exact-factor counterexample to the
existential theorem. It is a rigorous no-go to deriving (4.6) from the
scalar owner-consumption cap, the per-row matching, and the canonical
pair-adjacency upper budget alone.

## 5. A literal homogeneous packet counterexample

The preceding local gap has a global homogeneous analogue. Fix coordinates
(x,y). Take the multiset of all oriented cyclic orders with (x) fixed at
position zero and (y) in one of the four positions

\[
1,-1,m,-m,
\]

with all other coordinates arbitrary. Retain multiplicity.

### Theorem 5.1 -- homogeneous ownership does not imply Hall

Every middle set occurs in this multiset exactly

\[
\boxed{\tau=2(m-1)!(m+1)!}
\tag{5.1}
\]

times. Nevertheless, for every (m\ge7) and every

\[
2\le q\le m-3,
\]

the depth-\(q\) pair-star Hall cut for \(\{x,y\}\) fails in the associated
\(\tau\)-fold sibling graph.

#### Proof

The stabilizer of \(\{x,y\}\) is transitive on middle sets containing
both, exactly one, or neither of the pair. A row at shorter pair-distance
(d) has respectively

\[
m-d,\qquad2d,\qquad m+1-d
\]

middle windows of these three types. Distances (1) and (m) occur
equally in the construction, so the three averaged degrees coincide. Total
incidence then gives the common degree (5.1).

Half of the rows have distance one and half distance (m). Equality holds
in the sharp pair bound (3.23), so

\[
\iota_q(U_{xy})
=\frac{\tau B}{2}(m-q-2).
\]

Its excess above proportional mass is

\[
\frac{\tau B}{2}
\left(q-1-\frac{q(q+1)}m\right).
\tag{5.2}
\]

The parenthesis is concave in (q) and is at least (1-6/m) on the
displayed interval. The exact floor/ceiling cap for \(\tau W\) owners differs
from proportional mass on (U_{xy}) by at most (|U_{xy}|), while

\[
\frac{|U_{xy}|}{\tau B/2}\le\frac m\tau.
\]

For (m\ge7), (5.2) is larger than the entire floor margin. Thus Hall
fails. \(\square\)

This is a literal integral family of cyclic packets with homogeneous exact
middle ownership. It is not one indivisible exact factor. It proves that
cyclic packets, all homogeneous middle-ownership ledgers, and the exact pair
distance moment do not imply floor/ceiling Hall feasibility. An argument
which averages factors and later rounds using only those coarse statistics
cannot prove \(\mathrm{AO}_A\); richer packet correlations are not excluded.

## 6. Exact depth-one recourse around canonical MSW

The following uses the proved first-occurrence packet matching in
`FRACTIONAL_PACKET_GLOBAL_SEED_MATCHING_20260725.md`.

Let (F_m^{\rm MSW}) be the canonical MSW factor. There are (L_m)
pairwise row-disjoint triples of canonical wreaths, every triple owning a
common canonical depth-one target. The targets of different triples need
not be distinct. The exact generating function is

\[
\sum_{m\ge0}L_mz^m
=
\frac{z^4C(z)}
{1-(1+z^2)(zC(z)-z^2-2z^4)-2z^6},
\tag{6.1}
\]

where (C(z)=\sum_m\operatorname{Cat}_mz^m), and

\[
\boxed{
\frac{L_m}{B}\longrightarrow
\delta_{\rm seed}=\frac{275}{19321}.}
\tag{6.2}
\]

For completeness, the disjointness mechanism is the first occurrence in
the primitive Dyck-component word of one of the three interchangeable seed
blocks (A,B,DD). Clean prefixes contain no earlier seed and do not end in
(D); the first seed therefore recovers the prefix, the variant, and the
suffix. Dirty cylinders are prefix-free and permit recursion. At
(z=1/4), the denominator in (6.1) has constant term (139/256) and
square-root coefficient (17/32). Comparing the square-root coefficient
with that of (C(z)) gives

\[
\frac1{4^4}
\left(\frac{256}{139}
+\frac{17}{32}\frac{256^2}{139^2}\right)
=\frac{275}{19321},
\]

auditing (6.2).

### Theorem 6.1 -- MSW orientation-recourse lower bound

Every balanced stage-one orientation of \(F_m^{\rm MSW}\) satisfies

\[
\boxed{T_1\ge L_m.}
\tag{6.3}
\]

More generally, for an exact factor \(F\), put

\[
d=|F_m^{\rm MSW}\setminus F|.
\]

Then

\[
\boxed{T_1(F)\ge(L_m-d)_+.}
\tag{6.4}
\]

If no balanced stage-one orientation exists, set \(T_1(F)=+\infty\).

#### Proof

At depth one, (c_1=1), so every balanced target load is at most two. For
a target (S), let (k_S) be the number of intact disjoint seed triples
with common target (S). Then the canonical anchor load satisfies

\[
\mu_1(S)\ge3k_S.
\]

Let (O_S) be the number of toggled owner edges leaving their canonical
anchor (S), and (I_S) the number toggled into (S). The final load is

\[
b(S)=\mu_1(S)-O_S+I_S\le2.
\]

Thus, whenever (k_S\ge1),

\[
O_S\ge3k_S-2\ge k_S.
\]

Each toggled edge has exactly one canonical anchor, so

\[
T_1=\sum_SO_S\ge\sum_Sk_S.
\]

For the canonical factor, the last sum is (L_m). Since the seed triples
are row-disjoint, deleting (d) canonical rows destroys at most (d)
triples. Inserted rows cannot remove the surviving anchor occurrences,
proving (6.4). Reversing a wreath does not affect its family of cyclic
rank-((m-1)) anchors, so the argument is orientation-robust. \(\square\)

Using (W=nB), (6.2)--(6.4) give

\[
\boxed{
T_1(F_m^{\rm MSW})
\ge
\left(\frac{275}{38642}+o(1)\right)\frac Wm.}
\tag{6.5}

This closes every (o(B))-recourse attempt in an (o(B))-row edit
neighbourhood of canonical MSW. The scale is nevertheless (o(W)), so it
does not refute \(\mathrm{AO}_A\). The unsupported claim that canonical
MSW has a proved ((1/16-o(1))W) depth-one hole count is not used.

## 7. Ordinary expansion cannot prove the theorem

For a coordinate (x), let

\[
U_x=\{S\in\tbinom{[n]}r:x\in S\}.
\]

The exact point-star calculation gives, in every reachable state,

\[
|\partial G_q(U_x)|=2B+\Delta_{q-1,x},
\qquad
|\Delta_{q-1,x}|\le T_{q-1}.
\tag{7.1}
\]

Also

\[
|U_x|=\frac r nN_q=\Theta_A(W).
\]

Hence along every (o(W))-recourse history,

\[
\boxed{
\frac{|\partial G_q(U_x)|}{|U_x|}=o(1).}
\tag{7.2}
\]

Thus no successful evolving wreath graph can have a positive uniform
Cheeger or conductance constant on the full graph. A uniform whole-graph
expander argument cannot be the short-transport theorem. This does not
exclude quotient expansion, expansion for restricted divergence vectors,
or a multiscale flow which handles point-star bottlenecks separately. Point
stars themselves remain Hall-safe; (7.2) is a proof-method no-go, not a
Hall obstruction.

## 8. Exact implication and caveat audit

The new results have the following precise scope.

1. Theorems 3.5--3.6 are fully adaptive: they use only the fixed canonical
   core, the always-present canonical anchor, and the exact cyclic residence
   ledger. Earlier orientations may alter all second endpoints.

2. The star theorem is genuinely two-sided. The internal inequality alone
   does not certify the complementary Hall row.

3. Fixed-order quota-wall depths remain. At such a depth the integer floor
   margin and the residence error have the same scale and may both vanish.

4. A nonstar family can violate Hall even if every bounded-order star is
   safe. The growing-order theorem does not supply a junta reduction for
   arbitrary Hall witnesses.

5. The core inequalities (4.3)--(4.4) are necessary, not sufficient. The
   local path packing proves that known packet resources cannot imply them,
   but lacks exact-factor completion.

6. The homogeneous counterexample is a literal integral cyclic cover, not
   one exact factor. Since \(\mathrm{AO}_A\) is existential, a bad factor
   would not by itself refute it in any event.

7. The determinant-two minor rules out only the direct configuration
   matrix. It does not rule out all extended formulations or prove a gap at
   the balanced right-hand side.

8. The MSW lower bound is exact and packetized, but only of order
   (W/m=o(W)). It excludes an overly strong recourse scale and a local
   edit basin, not the theorem's allowed scale.

Consequently the honest final status is

\[
\boxed{
\mathrm{SDH}_A/\mathrm{AO}_A
\text{ remains neither proved nor disproved.}}
\]

What is now proved is that direct configuration TU, uniform positive
whole-graph expansion, point/deletion marginals, and the listed coarse
homogeneous packet statistics are insufficient. Bounded-order star checks
settle all but their quota-wall depths. In the canonical MSW
\(o(B)\)-row neighbourhood, an \(o(B)\) depth-one recourse target is
impossible, although the allowed \(o(W)\) target remains possible. Any
proof of \(\mathrm{AO}_A\) must still control the indivisible exact-factor
fibre, the finitely many integer-wall cuts, arbitrary nonstar families, and
ownerwise short transport simultaneously.

## 9. Independent audit record

Three independent theorem-level audits were applied after the draft was
written.

- The weighted footrule, carry-age, universal determinant-two minor, quota
  capacity formulas, and fixed/growing-order collar counts were rederived
  independently.
- The incident identity was checked with the residual condition
  \(T\setminus p_X\subseteq C_X\); this corrected the false shortcut which
  subtracts every \(p_X\subseteq T\) when \(t>2\).
- The homogeneous multiplicity, pair-star excess, core resource cap,
  \(P_4\) local scope, MSW seed grouping, edit robustness, and constants
  \(275/19321\) and \(275/38642\) were separately audited.

All corrections from those audits are incorporated above. In particular,
the report makes no claim of an exact-factor counterexample, optimality of
the MSW certificate constant, or a no-go for structured quotient/multiscale
expansion.
