# Exact floor collar for complementary star cuts in residual cyclic completion

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web input is
used.

## 0. Result and scope

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn,
\qquad K=\lceil A\sqrt m\rceil .
\]

This note does not prove \((\mathrm{CA}_A)\). It proves the missing
floor-exact statement for the *lower-demand* side of every fixed-order star
cut in the residual inclusion flow.

For a fixed \(t\), a cyclic transition can cross a \(t\)-star at most once
per wreath, hence at most \(B\) times. On the other hand, if the balanced
floor/ceiling quotas at the two adjacent ranks are optimized for this one
cut, their exact boundary slack is at least \(B\) at every depth

\[
q\ge Q_{A,t},
\]

where \(Q_{A,t}\) is a constant independent of \(m\). Thus a
quota-independent complementary \(t\)-star obstruction is confined to a
fixed *shallow* collar. It cannot recur at each of the integer-crossing
depths of \(\lambda_q\).

The note also gives an exact packed-star dual lower bound for any proposed
exceptional owner family. What remains unproved is simultaneous choice of
one common nested quota flow: optimizing the quotas for each star separately
does not select one quota system satisfying all stars or all Hall families.

## 1. Exact balanced star ranges

At depth \(j\), set

\[
r_j=m-j,\qquad N_j=\binom n{r_j},\qquad
\lambda_j=\frac W{N_j},\qquad c_j=\lfloor\lambda_j\rfloor,
\]

and

\[
\rho_j=W-c_jN_j,qquad \theta_j=\frac{\rho_j}{N_j}.
\tag{1.1}
\]

This also covers \(j=0\): \(N_0=W\), \(\lambda_0=c_0=1\), and
\(\rho_0=0\).

Fix a \(t\)-set \(T\), and write

\[
\mathcal U_{j,t}(T)=
\{S\in\tbinom{[n]}{r_j}:T\subseteq S\},\qquad
u_{j,t}=|\mathcal U_{j,t}(T)|=\binom{n-t}{r_j-t}.
\tag{1.2}
\]

Every balanced depth-\(j\) quota has the form

\[
b_j(S)=c_j+\mathbf1_{\{S\in\mathcal H_j\}},
\qquad |\mathcal H_j|=\rho_j.
\tag{1.3}
\]

Consequently its mass on the star (1.2) ranges over every integer in the
interval

\[
\boxed{
L_{j,t}
=c_ju_{j,t}+\max\{0,\rho_j-(N_j-u_{j,t})\}
\le b_j(\mathcal U_{j,t}(T))
\le
U_{j,t}
=c_ju_{j,t}+\min\{\rho_j,u_{j,t}\}.}
\tag{1.4}
\]

Indeed, the intersection size
\(|\mathcal H_j\cap\mathcal U_{j,t}(T)|\) ranges over precisely the
integer interval between the two displayed extrema.

Let

\[
\alpha_{j,t}=\frac{u_{j,t}}{N_j}
=\frac{(r_j)_t}{(n)_t},
\qquad d_j=\operatorname {dist}(\lambda_j,\mathbb Z).
\tag{1.5}
\]

The exact upper and lower floor margins are

\[
U_{j,t}-\lambda_ju_{j,t}
=N_j
\begin{cases}
\theta_j(1-\alpha_{j,t}),&\theta_j\le\alpha_{j,t},\\
\alpha_{j,t}(1-\theta_j),&\theta_j\ge\alpha_{j,t},
\end{cases}
\tag{1.6}
\]

and

\[
\lambda_ju_{j,t}-L_{j,t}
=N_j
\begin{cases}
\theta_j\alpha_{j,t},&\theta_j\le1-\alpha_{j,t},\\
(1-\theta_j)(1-\alpha_{j,t}),&\theta_j\ge1-\alpha_{j,t}.
\end{cases}
\tag{1.7}
\]

These identities retain the floor baseline exactly.

## 2. The exact cyclic crossing ledger

Let \(F\) be an oriented exact wreath factor, and let
\(\Gamma_j(X)\) denote the canonical depth-\(j\) interval owned by the
middle set \(X\). For \(1\le q\le K\), define

\[
C_q^F(T)=
\#\{X:T\subseteq\Gamma_{q-1}(X),\quad
        T\nsubseteq\Gamma_q(X)\}.
\tag{2.1}
\]

### Lemma 2.1 -- one crossing per row

If \(a_R(T)\) is the number of middle intervals of row \(R\) which contain
\(T\), then

\[
\boxed{
C_q^F(T)
=M_{q-1}^F(T)-M_q^F(T)
=\sum_{R\in F}\mathbf1_{\{a_R(T)\ge q\}}
\le B.}
\tag{2.2}
\]

#### Proof

The child is contained in its parent, so the first equality is obtained by
subtracting the two containment counts. The cyclic span-truncation identity
gives

\[
M_j^F(T)=\sum_{R\in F}(a_R(T)-j)_+.
\]

The difference of the summands at \(j=q-1,q\) is
\(\mathbf1_{\{a_R(T)\ge q\}}\). There are \(B\) rows. \(\square\)

The bound is independent of all row orientations, although the identities
of the crossing owners may depend on them.

## 3. Exact residual Hall obstruction

Freeze every canonical owner outside an exceptional family \(E\). Let
\(f_j(S)\) be the frozen load and let

\[
r_j(S)=b_j(S)-f_j(S)
\tag{3.1}
\]

be the residual load. At transition \(q\), the parent neighbourhood of
the child star is exactly the parent star:

\[
N(\mathcal U_{q,t}(T))=\mathcal U_{q-1,t}(T).
\tag{3.2}
\]

Here and below \(m-q\ge t\), which holds throughout a fixed window for
fixed \(t\) and large \(m\).

### Theorem 3.1 -- floor-exact complementary-star certificate

Define the exact one-cut quota envelope

\[
\boxed{H_{q,t}=U_{q-1,t}-L_{q,t}.}
\tag{3.3}
\]

If the residual inclusion-Hall inequality holds for the child star
\(\mathcal U_{q,t}(T)\), then

\[
\boxed{
|E\cap\mathcal C_q^F(T)|
\ge
\bigl(C_q^F(T)-H_{q,t}\bigr)_+,}
\tag{3.4}
\]

where \(\mathcal C_q^F(T)\) is the owner set counted in (2.1). In
particular,

\[
\boxed{|E|\ge\bigl(C_q^F(T)-H_{q,t}\bigr)_+.}
\tag{3.5}
\]

#### Proof

The residual Hall inequality for this star is

\[
r_q(\mathcal U_{q,t}(T))
\le r_{q-1}(\mathcal U_{q-1,t}(T)).
\]

After inserting (3.1), it becomes

\[
f_{q-1}(\mathcal U_{q-1,t}(T))
-f_q(\mathcal U_{q,t}(T))
\le
b_{q-1}(\mathcal U_{q-1,t}(T))
-b_q(\mathcal U_{q,t}(T)).
\tag{3.6}
\]

The left side is precisely the number of *frozen* canonical transitions
which cross the star boundary. It is at least

\[
C_q^F(T)-|E\cap\mathcal C_q^F(T)|.
\]

By (1.4), the right side of (3.6) is at most
\(U_{q-1,t}-L_{q,t}=H_{q,t}\). Rearrangement proves (3.4), and (3.5)
follows. \(\square\)

Thus (3.4) is a literal obstruction for one exact factor, one fixed star,
and the exact floor baselines. It is stronger than comparing marginal
star moments: it records the actual canonical transitions which leave the
star.

### Corollary 3.2 -- packed-star dual

Let \(\mathcal T\) be any family of \(t\)-sets and let \(y_T\ge0\). Put

\[
D(y)=\max_X
\sum_{\substack{T\in\mathcal T:\\
X\in\mathcal C_q^F(T)}}y_T.
\tag{3.7}
\]

Every exceptional family whose residual flow passes all these star cuts
satisfies

\[
\boxed{
|E|\ge
\frac1{D(y)}
\sum_{T\in\mathcal T}
y_T\bigl(C_q^F(T)-H_{q,t}\bigr)_+,}
\tag{3.8}
\]

with the right side interpreted as zero if \(D(y)=0\).

#### Proof

Multiply (3.4) by \(y_T\), sum in \(T\), and interchange the order of
summation over \(E\) and \(\mathcal T\). The total weight charged to one
exceptional owner is at most \(D(y)\). \(\square\)

For equal weights on all \(t\)-sets, every transition which deletes one
point crosses exactly \(\binom{m-q}{t-1}\) such stars. This gives the
exact congestion in (3.7).

## 4. Complementary fixed-order stars have only a shallow collar

### Theorem 4.1 -- uniform shallow-collar theorem

Fix \(A>0\) and a positive integer \(t\). There is a constant
\(Q_{A,t}\) such that, for all sufficiently large \(m\), every
\(q\) satisfying

\[
Q_{A,t}\le q\le\lceil A\sqrt m\rceil
\tag{4.1}
\]

obeys

\[
\boxed{H_{q,t}\ge B\ge C_q^F(T)}
\tag{4.2}
\]

for every exact oriented wreath factor \(F\) and every \(t\)-set \(T\).
Consequently (3.4) gives no positive forced exceptional cost outside the
first \(Q_{A,t}-1\) depths.

One admissible constant is obtained as follows. Choose any fixed
\(\Lambda_A\) such that

\[
1\le\lambda_j\le\Lambda_A
\qquad(0\le j\le\lceil A\sqrt m\rceil)
\tag{4.3}
\]

for all sufficiently large \(m\), put \(\eta_t=2^{-t-2}\), and take

\[
Q_{A,t}=1+\left\lceil\frac{\Lambda_A}{4\eta_t}\right\rceil.
\tag{4.4}
\]

#### Proof

Uniformly in the fixed window,

\[
\alpha_{j,t}=\frac{(m-j)_t}{(n)_t}=2^{-t}+o_{A,t}(1).
\]

Hence, for large \(m\),

\[
\eta_t\le\alpha_{j,t}\le1-\eta_t.
\tag{4.5}
\]

Equations (1.6)--(1.7) therefore imply

\[
U_{j,t}-\lambda_ju_{j,t}\ge\eta_tN_jd_j,
\qquad
\lambda_ju_{j,t}-L_{j,t}\ge\eta_tN_jd_j.
\tag{4.6}
\]

The proportional boundary difference is nonnegative and is exactly

\[
\lambda_{q-1}u_{q-1,t}-\lambda_qu_{q,t}
=W\frac{(m-q+1)_t-(m-q)_t}{(n)_t}
=W\frac{t(m-q)_{t-1}}{(n)_t}.
\tag{4.7}
\]

Using (4.6), (4.7), and \(N_j=W/\lambda_j\ge W/\Lambda_A\), we get

\[
H_{q,t}
\ge
\frac{\eta_tW}{\Lambda_A}(d_{q-1}+d_q).
\tag{4.8}
\]

The exact adjacent ratio is

\[
\delta_q:=\lambda_q-\lambda_{q-1}
=\lambda_{q-1}\frac{2q}{m-q+1}.
\tag{4.9}
\]

For fixed \(A\), one has \(0<\delta_q<1/2\) throughout the window when
\(m\) is large. Distance on the circle \(\mathbb R/\mathbb Z\) obeys the
triangle inequality, so

\[
d_{q-1}+d_q
\ge\operatorname {dist}(\delta_q,\mathbb Z)
=\delta_q
\ge\frac{2q}{m-q+1}.
\tag{4.10}
\]

Since \(n=2m+1>2(m-q+1)\), (4.8)--(4.10) yield

\[
\frac{H_{q,t}}B
=\frac{nH_{q,t}}W
>\frac{4\eta_t}{\Lambda_A}q.
\tag{4.11}
\]

The choice (4.4) makes the last quantity at least one. Lemma 2.1 then
gives (4.2). \(\square\)

The important mechanism is exact: even when \(\lambda_{q-1}\) lies just
below an integer and \(\lambda_q\) just above it, the two floor margins
add to at least their exact increment \(\delta_q\). Thus an integer
crossing cannot create a new complementary-star danger collar at Gaussian
depth.

The fixed collar can in fact be evaluated completely.

### Theorem 4.2 -- only the first deletion can be nonautomatic

Fix \(A>0\) and \(t\ge1\). For all sufficiently large \(m\), uniformly
for

\[
2\le q\le\lceil A\sqrt m\rceil,
\]

one has

\[
\boxed{H_{q,t}>B\ge C_q^F(T)}
\tag{4.12}
\]

for every exact factor and every \(t\)-set \(T\). At \(q=1\),

\[
\boxed{
H_{1,t}=\binom{n-t}{m-t}-\binom{n-t}{m-1-t},
\qquad
\frac{H_{1,t}}B\longrightarrow\frac{t+2}{2^{t-1}}.}
\tag{4.13}
\]

Consequently the first deletion is also automatic for \(t\le3\). A
fixed-order complementary-star obstruction can survive the separate-quota
envelope only at

\[
\boxed{q=1,\qquad t\ge4.}
\tag{4.14}

#### Proof

Theorem 4.1 already proves (4.12) for \(q\ge Q_{A,t}\). It remains to
handle the finitely many fixed integers \(q<Q_{A,t}\).

For fixed \(j\),

\[
\lambda_j=1+\frac{j(j+1)}m+O_j(m^{-2}).
\tag{4.15}
\]

Hence, for fixed \(q,t\) and large \(m\), both relevant floors equal one,
the upper parent bonus fits entirely inside its star, and the lower child
bonus fits entirely outside its star. Thus

\[
H_{q,t}=u_{q-1,t}+\rho_{q-1}-u_{q,t}.
\tag{4.16}
\]

The two exact ingredients are

\[
\frac{\rho_{q-1}}B
=n\left(1-\frac1{\lambda_{q-1}}\right)
=2q(q-1)+o_{q}(1)
\tag{4.17}
\]

and

\[
u_{q-1,t}-u_{q,t}
=u_{q-1,t}\frac{2q+t}{m+q+1},
\tag{4.18}
\]

so

\[
\frac{u_{q-1,t}-u_{q,t}}B
\longrightarrow\frac{2q+t}{2^{t-1}}.
\tag{4.19}
\]

Combining (4.16)--(4.19) gives

\[
\frac{H_{q,t}}B
\longrightarrow
2q(q-1)+\frac{2q+t}{2^{t-1}}.
\tag{4.20}
\]

For every \(q\ge2\), the right side is greater than four, so each of the
finitely many depths below \(Q_{A,t}\) satisfies \(H_{q,t}>B\) for large
\(m\). Together with Theorem 4.1 this proves (4.12).

At \(q=1\), the parent quota is identically one and the child high bonuses
fit outside the fixed star. Therefore

\[
H_{1,t}=u_{0,t}-u_{1,t},
\]

which is the first formula in (4.13). Equation (4.18) with \(q=1\) gives
the limit there. This limit is greater than one for \(t=1,2,3\), so
\(H_{1,t}>B\) for those orders when \(m\) is large. For \(t\ge4\) the
envelope is below \(B\) asymptotically; no claim that an exact factor
actually attains a crossing count above it is made. This proves the stated
scope (4.14). \(\square\)

## 5. Exact mean cancellation and the surviving obstruction

There is no obstruction in the unweighted sum of all \(t\)-stars. Every
canonical transition deletes one point from an \((m-q+1)\)-set, and hence
crosses exactly

\[
\binom{m-q}{t-1}
\]

stars. Therefore

\[
\boxed{
\sum_{T\in\binom{[n]}t}C_q^F(T)
=W\binom{m-q}{t-1}.}
\tag{5.1}
\]

On the other hand, multiplying (4.7) by \(\binom nt\) gives exactly the
same value:

\[
\binom nt
W\frac{t(m-q)_{t-1}}{(n)_t}
=W\binom{m-q}{t-1}.
\tag{5.2}
\]

Since \(H_{q,t}\) is the proportional term (4.7) plus two nonnegative
floor margins,

\[
\sum_T(C_q^F(T)-H_{q,t})\le0.
\tag{5.3}

Thus a genuine star obstruction must exploit a nonuniform positive part,
as in the packed dual (3.8); first moments over all stars cannot supply it.

Combining Theorem 4.1 with the previously proved internal-star collar gives
the following precise boundary.

* Internal fixed-order star capacity can be nonautomatic at only
  \(O_{A,t}(1)\) integer-threshold depths.
* Complementary fixed-order residual star demand can be forced only at the
  first deletion, and only for star order at least four.
* Neither statement chooses one common high-quota family, one common nested
  flag flow, or handles arbitrary Hall families.

Accordingly, fixed-order stars cannot by themselves produce a repeated
Gaussian-window obstruction. The remaining \((\mathrm{CA}_A)\) gate is a
simultaneous non-star Hall problem, or a bounded number of shallow/threshold
star collars coupled through one actual quota flow. This note neither proves
that coupling nor claims the constant-one theorem.

## 6. Exact obstruction to the fully equivariant coupling shortcut

The prime-equivariant flag-flow theorem might suggest choosing the wreath
factor equivariant under the same prime cycle and then doing all residual
work in the quotient. In half of the prime congruence classes this is
impossible before any lower-rank quota is considered.

### Theorem 6.1 -- Catalan orbit obstruction

Suppose \(n=2m+1\) is prime, \(m\ge3\) is odd, and \(\sigma\) is an
\(n\)-cycle on the coordinates. There is no exact middle wreath factor
which is invariant under \(\langle\sigma\rangle\).

#### Proof

Let \(\mathscr W_m\) be the set of unoriented cyclic coordinate orders,
so rotation and reversal describe the same row. The action of the prime
group \(\langle\sigma\rangle\) on \(\mathscr W_m\) has orbits of size
one or \(n\).

A row is fixed precisely when \(\sigma\) belongs to the dihedral
automorphism group of that cyclic order. Since \(\sigma\) has odd prime
order \(n\), it must be a generator of the rotation subgroup. After
identifying the coordinates with \(\mathbb Z_n\) so that
\(\sigma:x\mapsto x+1\), the fixed rows are therefore the step orders

\[
(0,a,2a,\ldots,(n-1)a),\qquad a\in\mathbb Z_n^*,
\]

with \(a\) and \(-a\) identified by reversal. There are exactly

\[
\frac{n-1}{2}=m
\tag{6.1}
\]

fixed rows.

If an invariant exact factor \(F\) existed and contained \(f\) fixed
rows, all its other rows would occur in full \(n\)-orbits. Hence

\[
|F|=B=\operatorname {Cat}_m\equiv f\pmod n,
\qquad 0\le f\le m.
\tag{6.2}
\]

Modulo the prime \(n=2m+1\),

\[
\binom{2m}{m}=\binom{n-1}{m}
\equiv(-1)^m,
\]

and \(m+1\equiv 1/2\pmod n\). Therefore

\[
B=\frac1{m+1}\binom{2m}{m}
\equiv2(-1)^m\pmod n.
\tag{6.3}
\]

For odd \(m\), the least nonnegative residue in (6.3) is
\(n-2=2m-1>m\), contradicting (6.2). \(\square\)

For even \(m\), the same argument says only that a fully invariant factor
would have to contain exactly two fixed step rows; it does not rule one
out. Theorem 6.1 also does not obstruct a noninvariant factor aligned with
an equivariant resolution on all but a small exceptional owner set. Its
precise consequence is narrower: the prime-equivariant flag flow cannot be
coupled to the cyclic packets merely by imposing the same group symmetry on
the exact factor in prime dimensions \(n\equiv3\pmod4\).

## 7. Adversarial audit

1. **Separate optimization.** The envelope \(H_{q,t}\) uses the maximum
   parent star mass and minimum child star mass. Those two balanced quota
   vectors exist rankwise, but they are not asserted to belong to one common
   nested resolution. Hence \(H_{q,t}\ge C_q^F(T)\) rules out a
   quota-independent one-cut obstruction; it does not prove Hall
   feasibility.

2. **Exceptional-owner identity.** Equation (3.4) charges only exceptional
   owners whose *canonical transition actually crosses the star*. Releasing
   an unrelated owner cannot repair (3.6), so replacing this intersection by
   an arbitrary cardinality before the final inequality would lose
   information.

3. **Floor endpoints.** Equations (1.4), (1.6), and (1.7) include the cases
   \(\theta_j=0\), \(\theta_j=\alpha_{j,t}\), and
   \(\theta_j=1-\alpha_{j,t}\). No generic nonintegrality of
   \(\lambda_j\) is assumed.

4. **Circle-distance step.** The equality in (4.10) uses
   \(\delta_q<1/2\), which is valid only after fixing \(A\) and taking
   \(m\) sufficiently large. It is not a growing-window assertion.

5. **Fixed order.** The constant \(Q_{A,t}\) grows with \(t\). Nothing here
   controls stars of order tending to infinity with \(m\).

6. **No conclusion about \((\mathrm{CA}_A)\).** Arbitrary Hall families can
   have geometry not detected by any fixed-order star. The common
   prime-equivariant flag-flow theorem supplies a feasible balanced flow,
   but this report does not prove that its quotas attain the separate
   envelopes (3.3), nor that it contains a large canonical cyclic subflow.

7. **Equivariance obstruction is exact, not stable.** Theorem 6.1 excludes
   a fully \(\sigma\)-invariant exact factor. It gives no quantitative
   lower bound on the distance of an arbitrary factor from the invariant
   subspace and hence no labelled-error lower bound for \((\mathrm{CA}_A)\).
