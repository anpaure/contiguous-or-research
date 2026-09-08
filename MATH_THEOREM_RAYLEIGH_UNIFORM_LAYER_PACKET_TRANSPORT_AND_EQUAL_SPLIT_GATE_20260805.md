# Rayleigh residual coagulation: uniform layer packets and the equal-split high-band gate

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact construction reduction and tail theorem.  Every continuous
density has a canonical interval-uniform layer decomposition.  Packetwise
joint mixability of those intervals is therefore an exact sufficient
transport theorem.  Applied to the high Rayleigh residual bands, it gives
an explicit `n+1`-piece equal-split kernel.  The combined demand of all
sufficiently high bands is pointwise dominated by the physical residual
socket density, so the entire unbounded job tail is coagulated exactly.
The finitely bounded remaining job bank is not solved here.

## 1. Uniform layer decomposition

Let `f>=0` be an integrable continuous density on an open interval of the
real line.  For `t>0`, write the open superlevel set as its disjoint interval
components

\[
                         \{x:f(x)>t\}
                         =\bigsqcup_q I_{t,q}.       \tag{1.1}
\]

Let `U_I` denote normalized Lebesgue measure on a nondegenerate bounded
interval `I`.  Define a measure `Lambda_f` on interval-uniform laws by

\[
 \int \Phi(U_I)\,d\Lambda_f(I)
 :=\int_0^\infty\sum_q |I_{t,q}|\Phi(U_{I_{t,q}})\,dt
\tag{1.2}
\]

for nonnegative measurable test functions `Phi`.  Unbounded or degenerate
components occur only on a null set for the Rayleigh densities below; the
same formula may generally be read after discarding zero-length
components.

### Lemma 1.1 (exact barycenter)

The original measure is the barycenter of its interval layers:

\[
                         f(x)dx
                         =\int U_I\,d\Lambda_f(I).  \tag{1.3}
\]

Moreover

\[
 \Lambda_f(\mathcal I)=\int f(x)dx,
 \qquad
 \int {\inf I+\sup I\over2}\,d\Lambda_f(I)
 =\int x f(x)dx.                                   \tag{1.4}
\]

#### Proof

For a Borel set `B`, Tonelli and layer cake give

\[
\begin{aligned}
 \int U_I(B)\,d\Lambda_f(I)
 &=\int_0^\infty\sum_q
    |I_{t,q}|{|B\cap I_{t,q}|\over|I_{t,q}|}\,dt\\
 &=\int_0^\infty |B\cap\{f>t\}|\,dt
 =\int_B f(x)dx.
\end{aligned}
\]

This is (1.3).  Testing it against one and against `x` proves (1.4).
`square`

## 2. Packetwise uniform joint mixability

For a bounded interval `I=[a,b]`, put

\[
                         m(I)={a+b\over2},
 \qquad \ell(I)=b-a.                               \tag{2.1}
\]

A **uniform packet** is one job interval `J` and finitely many socket
intervals `S_1,...,S_N`, all on the positive half-line, satisfying

\[
                         m(J)=\sum_{i=1}^N m(S_i)  \tag{2.2}
\]

and

\[
 \boxed{
 \ell(J)+\sum_{i=1}^N\ell(S_i)
 \ge
 2\max\{\ell(J),\ell(S_1),\ldots,\ell(S_N)\}.}
\tag{2.3}
\]

The uniform-distribution joint-mixability theorem says that (2.2)--(2.3)
are necessary and sufficient for random variables

\[
 X\sim U_J,qquad Y_i\sim U_{S_i}
\]

to be coupled with

\[
                         X=\sum_iY_i\quad\text{a.s.} \tag{2.4}
\]

Indeed, apply the theorem to `(Y_1,...,Y_N,-X)`: (2.2) fixes center zero,
and its support/length inequality is exactly (2.3).

### Theorem 2.1 (uniform-layer packet transport)

Let `mu=f(x)dx` be a finite job measure and `nu=g(y)dy` a finite socket
measure, with equal first moments.  Suppose there is a finite measure `Pi`
on uniform packets such that

1. the job-interval marginal of `Pi` is `Lambda_f`;
2. the aggregate socket-interval marginal of `Pi` is `Lambda_g`;
3. `Pi` is supported on (2.2)--(2.3).

Then `(mu,nu)` has a finite coagulation kernel.

Conversely, these three conditions are necessary for a construction which
first uses the canonical layer decompositions (1.2) and then couples each
layer packet separately by uniform joint mixability.

#### Proof

For each packet, (2.2)--(2.3) give a joint mix satisfying (2.4).  A
measurable choice may be made packetwise: for fixed arity, the set of
probability couplings with the prescribed interval-uniform marginals and
support on the closed sum hyperplane is a nonempty compact-valued
correspondence with Borel graph.  The standard measurable-selection theorem
therefore supplies a kernel; take the disjoint union over arities.

Integrate those joint laws against `Pi`.  Lemma 1.1 and the two marginal
conditions give job marginal `mu` and aggregate socket marginal `nu`.
Equation (2.4) gives exact sum in every configuration.  The arity is finite
on every packet.  This is a coagulation kernel.

The converse within the stated layer-packet ansatz follows simply by
recording the packet parameters of each selected uniform joint mix.
`square`

This theorem is not an equivalence with arbitrary coagulation.  Its value is
that the only remaining selection is a transport of explicit interval
layers; the joint coupling inside each selected packet is automatic.

## 3. The Rayleigh high bands

Return to the separated residual pair

\[
 \nu_{\rm res}(dy)=(s(y)-j(y)){\bf1}_{(0,c)}dy,
\]

\[
 \mu_{\rm res}(dx)
 =(j(x)-s(x)){\bf1}_{(c,A)}dx+j(x){\bf1}_{[A,\infty)}dx.
\]

As in the endpoint-saturation theorem, `2c>A`.  For `n>=3`, put

\[
 I_n=((n-1)c,nc),
 \qquad \mu_n(dx)=j(x){\bf1}_{I_n}(x)dx.           \tag{3.1}
\]

### Proposition 3.1 (literal `n+1` equal-split kernel)

Every job `x in I_n` can be assigned `n+1` equal sockets

\[
                         y_1=\cdots=y_{n+1}
                         ={x\over n+1}<c.           \tag{3.2}
\]

The resulting socket occurrence measure is

\[
 \rho_n=(n+1)(D_{1/(n+1)})_\#\mu_n,               \tag{3.3}
\]

where `D_a(x)=ax`.  It has density

\[
 r_n(y)=(n+1)^2j((n+1)y)
 {\bf1}_{((n-1)c/(n+1),\,nc/(n+1))}(y).            \tag{3.4}
\]

Its work is exactly the work of `mu_n`.

#### Proof

Equation (3.2) gives the sum identity and the strict capacity inequality
because `x<nc<(n+1)c`.  The pushforward of `j(x)dx` under
`x=(n+1)y` has density `(n+1)j((n+1)y)`; there are `n+1` occurrences,
giving (3.4).  Finally,

\[
 \int y\,d\rho_n
 =(n+1)\int{x\over n+1}\,d\mu_n(x)
 =\int x\,d\mu_n(x).
\]

`square`

At the uniform-layer level, this construction sends every job interval
`J=[a,b]` to `n+1` copies of

\[
                         {J\over n+1}
 =\left[{a\over n+1},{b\over n+1}\right].         \tag{3.5}

The centers add exactly.  The job width is `ell(J)`, each socket width is
`ell(J)/(n+1)`, and (2.3) holds with equality.  Thus (3.2) is the simplest
extremal uniform packet behind the disappearance of the `n`-role endpoint
obstruction.

## 4. One explicit analytic gate

Put

\[
 \rho_{\rm hi}=\sum_{n\ge3}\rho_n.                \tag{4.1}
\]

The series is locally finite away from `c`, and its density is

\[
 R_{\rm hi}(y)=
 \sum_{n\ge3}(n+1)^2j((n+1)y)
 {\bf1}_{((n-1)c/(n+1),\,nc/(n+1))}(y).
\tag{4.2}

Equivalently, writing `delta=c-y`, the active integers `m=n+1` at a fixed
`0<y<c` satisfy

\[
                         {c\over\delta}<m
                         <{2c\over\delta},
 \qquad m\ge4.                                    \tag{4.3}

### Corollary 4.1 (pointwise high-band sufficient condition)

If

\[
 \boxed{
 R_{\rm hi}(y)\le s(y)-j(y)
 \quad\text{for almost every }0<y<c,}              \tag{4.4}

\]

then every high residual job `x>2c` has an explicit finite
`ceil(x/c)+1`-piece realization inside the physical residual socket bank.
After removing those jobs and sockets, the remaining job and socket
measures are positive and retain equal first moments.

#### Proof

Proposition 3.1 constructs the high-job kernel with aggregate socket
measure `rho_hi`.  Inequality (4.4) says that this is a submeasure of
`nu_res`.  Removing it and `sum_(n>=3)mu_n` leaves positive measures.
Their first moments remain equal because the removed first moments are
equal band by band. `square`

The full inequality (4.4), beginning at `n=3`, is stronger than needed to
remove the unbounded tail.  Its eventual version is unconditional.

### Theorem 4.2 (all sufficiently high bands fit pointwise)

For `N>=3`, put

\[
 R_{\ge N}(y)=
 \sum_{n\ge N}(n+1)^2j((n+1)y)
 {\bf1}_{((n-1)c/(n+1),\,nc/(n+1))}(y).
\tag{4.5}
\]

There is a finite integer `N_0` such that, for every `N>=N_0`,

\[
 \boxed{
 R_{\ge N}(y)\le s(y)-j(y)
 \quad(0<y<c).}                                    \tag{4.6}
\]

Consequently all residual jobs in

\[
                         ((N_0-1)c,\infty)          \tag{4.7}
\]

have an explicit finite coagulation using `ceil(x/c)+1` equal pieces, and
the unused socket measure and the remaining compactly supported job measure
are positive and have equal work.

#### Proof

Write

\[
                         \sigma(y)=s(y)-j(y),
 \qquad \delta=c-y,
 \qquad L={c\over\delta}.                           \tag{4.8}
\]

The function `sigma` is positive on `(0,c)`, vanishes at `c`, and has a
simple zero there.  Indeed, if `c=A theta`, then `theta>17/20`, and the
crossing identity gives

\[
 K''(c)
 =2A j(c)\left({1\over A^2-c^2}-2\right)>0,
\tag{4.9}
\]

where `K'=j-s=-sigma`.  Thus `-sigma'(c)=K''(c)>0`.  It follows that

\[
 q_0:=\min_{c/2\le y\le c}{\sigma(y)\over c-y}>0, \tag{4.10}
\]

where the quotient at `c` is interpreted by its positive limit.  Hence

\[
                         \sigma(y)\ge q_0\delta
 \qquad(c/2\le y<c).                               \tag{4.11}
\]

Suppose a term in (4.5) is active, and write `m=n+1`.  The exact
active-index algebra (4.3) says

\[
                         L<m<2L.                   \tag{4.12}
\]

If `n>=N`, this also implies

\[
 \delta<{2c\over N+1}.
\tag{4.13}
\]

For large `N`, every point supporting `R_(>=N)` therefore lies in
`[c/2,c)`.  Moreover, (4.12) gives

\[
 my=m(c-\delta)>(m-2)c.                            \tag{4.14}
\]

The Rayleigh job density is decreasing above `A`, and `2c>A`.  For
`m>=4`,

\[
\begin{aligned}
 m^2j(my)
 &\le m^2j((m-2)c)\\
 &\le 2(A+c)m^3
       \exp\left(-{c^2m^2\over4}\right).
\end{aligned}                                      \tag{4.15}
\]

The last inequality uses `m-2>=m/2`.

For every fixed `alpha>0`, there is a finite constant `C_alpha` such that

\[
 \sum_{m>L}m^3e^{-\alpha m^2}
 \le C_\alpha(1+L^3)e^{-\alpha L^2/2}
 \qquad(L\ge1).                                    \tag{4.16}
\]

For example, absorb `m^3e^{-alpha m^2/2}` into a constant and compare the
remaining Gaussian tail with an integral.  Applying (4.16) with
`alpha=c^2/4` to the active subset in (4.12) gives

\[
 R_{\ge N}(y)
 \le C(1+L^3)e^{-c^2L^2/8}.                        \tag{4.17}
\]

The right side is `o(1/L)`, whereas `q_0 delta=q_0c/L`.  Choose `L_0`
so that (4.17) is at most `q_0c/L` whenever `L>=L_0`, and then choose
`N_0` so large that (4.13) forces `L>(N_0+1)/2>=L_0` and `y>=c/2`.
Equations (4.11) and (4.17) prove (4.6).

Now use the equal-split kernels of Proposition 3.1 for all `n>=N_0`.
Their aggregate socket occurrence density is `R_(>=N_0)`, which is a
subdensity of `sigma` by (4.6).  Their aggregate work equals the work of
the job tail band by band.  Removing both leaves positive measures with
equal first moments, proving the final assertion. `square`

This theorem is qualitative: it produces a finite threshold without
optimizing it.  No finite search is hidden in its proof.

## 5. Exact frontier

The uniform-layer theorem supplies an exact constructive interface for
Wang--Wang mixability.  It also makes the hierarchy clear:

1. `n` whole-band roles fail by endpoint saturation;
2. `n+1` roles pass every individual support/mean row;
3. equal splitting gives one explicit packet family and the exact demand
   density (4.2);
4. the Gaussian tail proves pointwise compatibility for all sufficiently
   high bands;
5. compatibility of the remaining bounded bands is (4.4) for those bands,
   or more generally the existence of a layer-packet transport `Pi` in
   Theorem 2.1.

No abstract joint-mixability theorem supplies that finite outer packet
transport.  Accordingly this note does not prove the separated Rayleigh
coagulation or the all-`k` additive conjecture.
