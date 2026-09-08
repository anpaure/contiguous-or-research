# Nested-priority claims on truncated carrier-rotor paths

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or web search is
used.

## 0. Verdict

Let

\[
 W=\binom{2m}{m},\qquad N=N_H=\binom{2m}{m-H},\qquad
 M=m+H,
\]

where \(H\) is the first crossing height, and put

\[
 Q=\left\lceil\sqrt{m(\log\log m+\gamma(m))}\right\rceil,
 \qquad \gamma\to\infty,\quad \gamma=o(\log\log m).
\]

Decorate the \(M\) columns of a length-\(M\), radius-\(Q\) carrier-rotor
path by one common priority order, and make the same nested claims as for a
cyclic packet. The exact mean effective augmented size is

\[
 K_Q=M+2\sum_{q=1}^{Q}\mathbb E b_q,
 \qquad
 \mathbb E b_q=\min\left(M,{\lambda_H\over\lambda_q}\right),
 \tag{0.1}
\]

and

\[
 \boxed{K_Q=(\sqrt\pi+o(1))m^{3/2}.}
 \tag{0.2}
\]

Thus truncating \(H\) to \(Q\) does **not** reduce the order, or even the
leading constant, of the augmented size. The mass of (0.1) is concentrated
at depths \(q=O(\sqrt m)\), already far below \(Q\).

The rotor does improve two secondary parameters.

* A state has only one prescribed facet below its owner, so the
  instantaneous owner--facet relative incidence is \(1/m\), rather than
  the \(2/m\) coming from the two boundaries of a cyclic interval row.
* If one can restrict to paths satisfying the star-spread and temporal
  Green bounds formulated in Section 4, then the packet--link parameter is

  \[
  O(Q/m)+\Gamma_Q
  =O\!\left(\sqrt{(\log\log m+\gamma)/m}\right)+\Gamma_Q,
  \tag{0.3}
  \]

  in place of \(O(H/m)\).

Neither improvement is automatic. Raw uniform-successor rotor walks can
revisit a short slot cycle, and even internally simple paths are not known
to obey a uniform star-spread or temporal Green estimate. This is the exact
new link obstruction.

Finally, raw dynamic branching enlarges the decorated atom entropy from

\[
 (2+o(1))m\log m
 \quad\hbox{to}\quad
 (5/2+o(1))m\log m,
 \tag{0.4}
\]

but \(K_Q\asymp m^{3/2}\) is unchanged. Consequently the independent
survival horizon remains

\[
 \boxed{\delta=\Theta(\log m/\sqrt m)}
 \tag{0.5}
\]

for a deleted density \(\delta\). Dynamic branching improves a constant,
not the iterative stability rate. It therefore does not by itself supply
the required \(o(W)\)-residual nibble.

## 1. The truncated nested-priority decoration

Write

\[
 \lambda_q={W\over N_q},\qquad N_q=\binom{2m}{m-q},
 \qquad \rho={MN\over W}={M\over\lambda_H}=1-o(1).
 \tag{1.1}
\]

Take a directed sequence of \(M\) rotor states

\[
 P=(\omega_0,\ldots,\omega_{M-1})
 \tag{1.2}
\]

in one carrier \(U\in\binom{[2m]}M\). Give the time positions one common
uniform priority order. For \(1\le q\le Q\), let \(b_q\) be coupled integer
roundings with

\[
 b_1\ge b_2\ge\cdots\ge b_Q,
 \qquad
 \mathbb E b_q=\min\left(M,{\lambda_H\over\lambda_q}\right).
 \tag{1.3}
\]

Claim the owners at all \(M\) times. On both signed sides at depth \(q\),
claim exactly the first \(b_q\) time positions in the common priority
order. Thus every claimed object is a complete initial segment of one flag
column, and no row is independently thinned.

The stationarity calculation in the rotor reduction applies at each time.
Before thinning, a fixed rank-\((m\pm q)\) target has load

\[
 \mu_q={MN\over N_q}=\rho\lambda_q.
 \tag{1.4}
\]

Multiplication by the mean claimed fraction gives

\[
 \mu_q{\mathbb E b_q\over M}
 =1
 \tag{1.5}
\]

when the cap in (1.3) is inactive; when it is active, the normalized degree
lies in \([\rho,1)\). Hence the truncated claim system retains the exact
near-regular degrees of the full packet system at every controlled rank.

## 2. Exact augmented size

### Theorem 2.1

For the decoration in Section 1,

\[
 K_Q=M+2\sum_{q=1}^{Q}\min\left(M,{\lambda_H\over\lambda_q}\right)
 =(\sqrt\pi+o(1))m^{3/2}.
 \tag{2.1}
\]

Moreover, deleting all claims at depths \(q>Q\) saves only

\[
 o(m^{3/2})
 \tag{2.2}
\]

claims per atom compared with the full calibrated nested decoration.

#### Proof

Uniformly for \(q\le H\),

\[
 \log\lambda_q={q^2\over m}
 +O\left({q\over m}+{q^3\over m^2}\right).
 \tag{2.3}
\]

At the first crossing,

\[
 \lambda_H=(1+o(1))M.
 \tag{2.4}
\]

Indeed \(\lambda_{H-1}<M\) and

\[
 1\le{\lambda_H\over M}
 <{\lambda_H\over\lambda_{H-1}}
 ={m+H\over m-H+1}
 =1+O(H/m).
\]

Consequently the cap in (2.1) can affect only \(q=O(\sqrt H)=o(\sqrt m)\).
Changing those
terms from \(M\exp(-q^2/m)\) to \(M\) changes the sum by \(o(M\sqrt m)\).
Therefore

\[
 \sum_{q=1}^{Q}\min\left(M,{\lambda_H\over\lambda_q}\right)
 =(1+o(1))M\sum_{q=1}^{Q}e^{-q^2/m}.
 \tag{2.5}
\]

Since \(Q/\sqrt m\to\infty\), the Gaussian Riemann sum gives

\[
 \sum_{q=1}^{Q}e^{-q^2/m}
 =\left({\sqrt\pi\over2}+o(1)\right)\sqrt m.
 \tag{2.6}
\]

The omitted tail is harmless more quantitatively: putting

\[
 L=\log\log m+\gamma(m),
\]

one has

\[
 \sum_{q>Q}e^{-q^2/m}
 \le {m\over2Q}e^{-Q^2/m}(1+o(1))
 ={\sqrt m\over2\sqrt L\,\log m\,e^{\gamma}}(1+o(1))
 =o(\sqrt m).
 \tag{2.7}
\]

Equations (2.5)--(2.7), \(M\sim m\), and the two signed sides prove
(2.1) and (2.2). \(\square\)

The mean number of protected entries in one time column is consequently

\[
 \kappa_Q={K_Q\over M}
 =(\sqrt\pi+o(1))\sqrt m.
 \tag{2.8}
\]

This is the parameter seen by any dynamic continuation argument.

## 3. Exact one-column incidences

Fix a uniform carrier state and condition on its owner \(X\). For
\(1\le q\le Q\), its lower flag is uniform among the
\(\binom mq\) rank-\((m-q)\) subsets of \(X\). Its upper flag is uniform
among the \(\binom mq\) rank-\((m+q)\) supersets of \(X\) in \([2m]\).
For the upper assertion, a prescribed \(q\)-set outside \(X\) first lies in
the random \(H\)-extension \(U\setminus X\) with probability
\((H)_q/(m)_q\), and is then the prescribed addition set with probability
\(1/\binom Hq\); the product is \(1/\binom mq\).

Hence, whenever the required containment holds,

\[
 \Pr(L_q=S\mid X)={1\over\binom mq},\qquad
 \Pr(U_q=T\mid X)={1\over\binom mq}.
 \tag{3.1}
\]

In particular, if the depth-one flag is claimed, then

\[
 \boxed{
 \Pr(L_1=S\mid X)={1\over m}}
 \tag{3.2}
\]

for a prescribed facet \(S\subset X\); the same holds for a prescribed
cofacet \(T\supset X\). The priority cap multiplies this by \(1-o(1)\).
Thus the worst instantaneous vertical occurrence ratio is
\((1+o(1))/m\).

This calculation must not be confused with an atom--link bound. For a
decorated path \(P\), let

\[
 f_P^-(X)=\#\{S\in P:|S|=m-1,\ S\subset X\},
\]

and define \(f_P^+(X)\) analogously using rank-\((m+1)\) cofacets. If the
candidate family is internally owner-injective, (3.1) shows that the
same-column occurrence part of the normalized link of \(X\) into \(P\) is

\[
 {f_P^-(X)+f_P^+(X)\over m}
 \tag{3.3}
\]

up to the \(1+o(1)\) priority normalization. Thus an arbitrary rotor path
has no automatic \(o(1)\) link estimate: it is necessary at least that

\[
 \max_X(f_P^-(X)+f_P^+(X))=o(m).
 \tag{3.4}
\]

To recover an \(O(Q/m)\) link, the corresponding quantity must be
\(O(Q)\), together with analogous nested/crossing star bounds at all
controlled ranks.

## 4. The exact link parameter left by truncation

For a decorated atom \(P\) and a protected target \(v\notin P\), use the
standard normalized link

\[
 \Lambda(P,v)={1\over\deg(v)}
 \sum_{u\in P}\deg(u,v).
 \tag{4.1}
\]

After restricting to atoms internally injective in every claimed rank,
split a common occurrence of \(u,v\) in a random path according as the two
flags come from the same rotor time or from distinct rotor times. This is
an exact decomposition

\[
 \Lambda(P,v)=\Lambda_0(P,v)+\Lambda_{\ne0}(P,v).
 \tag{4.2}
\]

The cyclic interval proof formerly bounded both pieces geometrically. A
general rotor path has no interval-row geometry. Define its temporal Green
term by

\[
 \Gamma_Q:=\sup_{P,v\notin P}\Lambda_{\ne0}(P,v),
 \tag{4.3}
\]

where the supremum is taken over whatever pruned path family is proposed
for the nibble.

Call a path family \(C\)-star-spread if, for every protected \(v\), every
rank of the fixed path contributes at most \(C/m\) to
\(\Lambda_0(P,v)\). At rank distance one this includes the explicit
condition

\[
 f_P^-(X)+f_P^+(X)\le C,
 \tag{4.4}
\]

and at larger distances it imposes the analogous normalized nested and
crossing-star counts.

### Proposition 4.1 (conditional truncated link bound)

If the pruned rotor family is \(C\)-star-spread, then

\[
 \boxed{
 \max_{P,v\notin P}\Lambda(P,v)
 =O(CQ/m)+\Gamma_Q.}
 \tag{4.5}
\]

In particular \(C=O(1)\) and \(\Gamma_Q=O(Q/m)\) give

\[
 \max\Lambda=O(Q/m)
 =O\!\left(\sqrt{(\log\log m+\gamma)/m}\right).
 \tag{4.6}
\]

#### Proof

There are \(2Q+1\) protected ranks. The definition of star-spread bounds
the same-time contribution of each rank by \(O(C/m)\), so
\(\Lambda_0=O(CQ/m)\). Equation (4.2) and the definition (4.3) give
(4.5). \(\square\)

The hypotheses of Proposition 4.1 are substantive, not bookkeeping. In
the uniform-successor model of the rotor reduction, a directed sequence is
a walk. Fix one left slot and one right slot. A rotor move acts on these
two slots and the \(2Q\) queue slots as one cycle of length \(2Q+2\).
Repeating the same positional move \(2Q+2\) times returns to the original
state. Repeating this short directed cycle inside a length-\(M\) walk gives
state and flag local time

\[
 \left\lfloor{M\over2Q+2}\right\rfloor
 =\Theta(M/Q).
 \tag{4.7}
\]

Such a walk does not even contain \(M\) distinct owners. Therefore the raw
regular walk family cannot be used as a uniform hypergraph of augmented
size \(K_Q\). It must first be pruned at least to paths which are internally
injective in every claimed rank. Internal injectivity still does not imply
(4.4) or control \(\Gamma_Q\): many distinct flags can lie in one fixed
containment star. A star-spread/Green lemma is the exact missing precursor
to a rotor-path nibble.

## 5. What the dynamic branches actually control

Write a state as

\[
 \omega=(L;z_1,\ldots,z_{2Q};R_U)
\]

and its successor under \(x\in L\), \(y\in R_U\) as \(\omega'\). Direct
substitution in the flag formulas gives, for \(0\le q<Q\),

\[
 L_q(\omega')=L+y+z_1+\cdots+z_{Q-q-1},
 \tag{5.1}
\]

and, for \(0\le q\le Q\),

\[
 U_q(\omega')=L+y+z_1+\cdots+z_{Q+q-1}.
 \tag{5.2}
\]

At the bottom endpoint alone,

\[
 L_Q(\omega')=L-x+y.
 \tag{5.3}
\]

Thus every protected flag in the next column except \(L_Q\) is independent
of \(x\). The apparent outdegree

\[
 (m-Q)(H-Q)
 \tag{5.4}
\]

contains only \(H-Q\sim H\) distinct choices of the whole shallow flag
column. The \(m-Q\) choices of \(x\) alter the bottom flag and plant
different data in the queue for future columns, but cannot repair a
currently forbidden shallow flag.

This yields an exact sufficient continuation criterion. At one step let
\(C^- ,C^+\subseteq\{1,\ldots,Q\}\) be the signed depths claimed by its
priority label, let \(\mathcal F_0\) be the forbidden owners, and let
\(\mathcal F_q^\pm\) be the other forbidden targets. Define

\[
 d_0(\omega)
 =\#\{y\in R_U:X(\omega')\in\mathcal F_0\},
 \tag{5.5}
\]

and, for \(q\ge1\),

\[
 d_q^\pm(\omega)
 =\#\{y\in R_U:F_q^\pm(\omega,y)\in\mathcal F_q^\pm\},
 \tag{5.6}
\]

where \(F_q^\pm(\omega,y)\) is (5.1) or (5.2). Each map
\(y\mapsto F_q^\pm(\omega,y)\) is injective. Hence the number of \(y\)'s
spoiled by at least one claimed shallow flag is at most

\[
 d_0(\omega)
 +\sum_{q\in C^-,\ q<Q}d_q^-(\omega)
 +\sum_{q\in C^+}d_q^+(\omega).
 \tag{5.7}
\]

For the exceptional bottom flag define

\[
 d_Q^-(\omega,y)
 =\#\{x\in L:L-x+y\in\mathcal F_Q^-\}.
\]

There is a fully legal branch whenever

\[
 (m-Q)\left(
 d_0+\sum_{q\in C^-,\,q<Q}d_q^-
 +\sum_{q\in C^+}d_q^+\right)
 +\mathbf 1_{\{Q\in C^-\}}\sum_{y\in R_U}d_Q^-(\omega,y)
 <(m-Q)(H-Q).
 \tag{5.8}
\]

Indeed the first term bounds all \((x,y)\) branches killed by a shallow
flag, while the second bounds the remaining branches killed by \(L_Q\).
Thus (5.8) is a rigorous additive local-star stability criterion.

For a quasirandom forbidden density \(\delta\) in every controlled row, the
mean left side of (5.8), normalized by the full outdegree, is of order

\[
 \delta\kappa_Q=(\sqrt\pi+o(1))\delta\sqrt m.
 \tag{5.9}
\]

The deterministic union-bound criterion therefore works only while

\[
 \delta=O(m^{-1/2}).
 \tag{5.10}
\]

There is also a sharp independent-residual benchmark. A positive fraction
of the priority labels claim \(\Theta(\sqrt m)\) shallow ranks: for a
priority quantile \(u\in[1/4,1/2]\), equations (2.3)--(2.5) give a deepest
claimed level

\[
 q(u)=(1+o(1))\sqrt{m\log(1/u)}=\Theta(\sqrt m).
 \tag{5.11}
\]

If every target is independently available with probability
\(x=1-\delta\), a step carrying such a label has the clean-branch benchmark

\[
 Hx^{\Theta(\sqrt m)}.
 \tag{5.12}
\]

It drops below one once

\[
 \delta\gg{\log H\over\sqrt m}
 =\Theta(\log m/\sqrt m).
 \tag{5.13}
\]

Thus online branching turns a multiplicative path condition into the useful
local additive condition (5.8), but it still cannot cross a fixed positive
deleted density. Its natural stability window has the same
\((\log m)/\sqrt m\) order as the old entropy barrier.

## 6. Raw entropy and the iterative rate

Put

\[
 d=(m-Q)(H-Q),\qquad
 |\Omega_Q(U)|={M!\over(m-Q)!(H-Q)!}.
\]

The number of length-\(M\) stationary-start rotor walks in one carrier is
exactly

\[
 A_Q^{\rm walk}=|\Omega_Q(U)|d^{M-1}.
 \tag{6.1}
\]

Now

\[
 \log|\Omega_Q(U)|=o(m\log m)
 \tag{6.2}
\]

because it is bounded by \(2Q\log M+O(H\log(m/H))\), whereas

\[
 \log d
 =\log m+\log H+o(\log m)
 =(3/2+o(1))\log m.
 \tag{6.3}
\]

Consequently

\[
 \log A_Q^{\rm walk}=(3/2+o(1))m\log m.
 \tag{6.4}
\]

The common priority order contributes another factor \(M!\). Therefore the
raw decorated count satisfies

\[
 \boxed{\log A_Q^{\rm dec}=(5/2+o(1))m\log m.}
 \tag{6.5}
\]

This is only an entropy upper benchmark for a useful atom family: pruning
for internal injectivity, star spread, and small \(\Gamma_Q\) may remove a
large fraction.

Under an independent residual in which each of the \(K_Q\) protected
vertices survives with probability \(x=1-\delta\), the scalar count is

\[
 A_Q^{\rm dec}x^{K_Q}.
 \tag{6.6}
\]

Equations (2.1) and (6.5) put its transition at

\[
 \delta
 =\left({5\over2\sqrt\pi}+o(1)\right){\log m\over\sqrt m}.
 \tag{6.7}
\]

Without the priority-order entropy, the constant \(5/2\) is replaced by
\(3/2\). A cyclic order plus its priority order has logarithmic count
\((2+o(1))m\log m\). Thus the rotor improves the raw decorated entropy
constant from \(2\) to \(5/2\), but not the asymptotic survival scale.

The sparse-round claim lemma likewise sees only \(K_Q\). Activating a
fraction

\[
 \alpha=\Theta(1/K_Q)=\Theta(m^{-3/2})
 \tag{6.8}
\]

of the carriers and altering collisions yields only
\(\Theta(N/K_Q)\) compatible paths in one round, provided a suitable
near-regular pruned family exists. The total number of protected non-tag
targets is

\[
 V_Q=W+2\sum_{q=1}^{Q}N_q
 =(\sqrt\pi+o(1))W\sqrt m.
 \tag{6.9}
\]

Thus coefficient one requires a residual fraction \(o(m^{-1/2})\), while
an \(O(W/m)\) absorber-scale residual requires \(O(m^{-3/2})\). An ideal
nibble still needs

\[
 \Theta(K_Q\log m)=\Theta(m^{3/2}\log m)
 \tag{6.10}
\]

degree-preserving rounds to reach the coefficient-one residual scale.
Neither (6.8) nor (6.10) improves asymptotically after truncation.

## 7. Precise remaining gate

The rotor reduction and nested-priority system combine successfully up to
the following statement.

> **Truncated rotor column-nibble gate.** For every carrier \(U\), find a
> coordinate-symmetric family of decorated, length-\(M\), radius-\(Q\)
> rotor paths such that:
>
> 1. every claimed rank is internally injective along every path;
> 2. the tag and target degrees retain the normalized values (1.5);
> 3. the family is \(O(1)\)-star-spread;
> 4. its temporal Green term satisfies \(\Gamma_Q=O(Q/m)\); and
> 5. the family has enough residual degree for a column-preserving nibble
>    through \(\Theta(K_Q\log m)\) adaptive rounds.

Conditions 1--4 would give the improved link parameter \(O(Q/m)\).
Condition 5 is still not a consequence of that link estimate: the augmented
size remains \((\sqrt\pi+o(1))m^{3/2}\), and independent-row survival still
dies after deletion density \(\Theta((\log m)/\sqrt m)\).

So dynamic rotor branching is a genuine local flexibility gain, but not a
rate breakthrough. The next theorem needed is a **spread-preserving path
pruning and nibble theorem**, not another marginal-load calculation.
