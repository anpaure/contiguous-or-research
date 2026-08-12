# Promotion rings: the root-matching floor, the valid fresh bite, and the global representative gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, or external
matching theorem is used.

## 0. Outcome

Put

\[
 s=m-H,\qquad M=m+H,\qquad
 N=N_H=\binom{2m}{m-H},\qquad W=\binom{2m}{m},
\]

and take

\[
                     H=\left\lfloor\sqrt{m\log m}\right\rfloor .
\tag{0.1}
\]

For each root \(A\in\binom{[2m]}s\), a frame is a directed cyclic order
of \(A^c\), modulo rotation.  Its edge consists of the root \(A\) and
the \(M\) middle targets obtained from its cyclic \(H\)-windows.  This is
the rooted promotion-ring hypergraph \(\mathcal G\).

Write

\[
 R=(M-1)!,\qquad
 D=\frac{(m!)^2}{(m-H)!},\qquad
 \lambda_H=\frac WN,\qquad
 \theta=\frac DR=\frac M{\lambda_H}=\frac{MN}{W}.
\tag{0.2}
\]

The requested ordinary-matching conclusion

\[
       \text{root leave }o(N/\sqrt m)
\tag{0.3}
\]

is impossible at (0.1).  Indeed every matching has root leave at least

\[
 \boxed{
 N-\frac WM=N\left(1-\frac1\theta\right)
 =(1+2\delta_m+o(1))\frac{NH}{m}
 =\omega(N/\sqrt m).}
\tag{0.4}
\]

Here \(\delta_m=\sqrt{m\log m}-H\in[0,1)\).

Thus no growing-rank nibble, regardless of its concentration or
regeneration properties, can prove (0.3) in the capacity-one rooted
hypergraph.  The obstruction is not a defect of the nibble analysis.

There is nevertheless a rigorous fresh isolated bite.  Its exact root
and target hazards obey the capacity relation, and it exposes the
deterministic invariant which prevents iteration to (0.3).  What must
replace the matching is a **global lower-quota representative theorem**:
choose one frame at every root while allowing the unavoidable

\[
                    E=MN-W=o(W)
\tag{0.5}
\]

aggregate excess middle occurrences.  If there are no holes this excess
is exactly \(E\); with \(o(W)\) holes it is still \(o(W)\).  The
block-factor hole theorem shows that a
law proving this cannot factor over root blocks of size

\[
 o\!\left(\binom mH\right).
\tag{0.6}
\]

Consequently local absorption and product regeneration are both outside
the surviving route.  The support must be fibre-dense on essentially the
whole root star of a typical middle target.

## 1. Exact degree ledger

Every root is contained in exactly

\[
                              R=(M-1)!
\tag{1.1}
\]

frame edges.  A fixed middle target \(Y\) first chooses a root
\(A\subset Y\) in \(\binom mH\) ways and then makes \(Y\setminus A\) a
cyclic interval in \(H!m!\) frames.  Hence

\[
 D=\binom mH H!m!=\frac{(m!)^2}{(m-H)!}.
\tag{1.2}
\]

Since

\[
 \lambda_H=\frac{(m+H)!(m-H)!}{(m!)^2},
\]

equation (0.2) follows.  Distinct roots have codegree zero.  A compatible
root--target pair has codegree \(H!m!\), which is

\[
 \frac{H!m!}{R}=\frac M{\binom MH}
\tag{1.3}
\]

of the root degree.  For distinct middle targets the maximum normalized
codegree is

\[
                         \frac{2}{m^2}
\tag{1.4}
\]

relative to \(D\), attained at Johnson distance one. Thus the stated
small pair-codegree ledger is asymptotically correct. Literally, when it
is normalized by \(R\), the maximum is

\[
                         \Delta_2=\frac{2D}{m^2}
                         =\frac{2\theta R}{m^2},
\tag{1.5}
\]

so the proposed bound \(2R/m^2\) misses the factor \(\theta>1\). The
correct form is \((2+o(1))R/m^2\).

## 2. The capacity floor at the prescribed height

### Theorem 2.1 (ordinary matching is quantitatively impossible)

Every matching \(\mathcal M\) in \(\mathcal G\) satisfies (0.4).

#### Proof

If \(r=|\mathcal M|\), the matching uses \(r\) distinct roots and \(Mr\)
distinct middle targets.  Therefore

\[
                         r\le \frac WM=\frac N\theta,
\tag{2.1}
\]

and the first inequality in (0.4) is exact.

It remains to estimate \(\theta\). Put

\[
 \delta_m=\sqrt{m\log m}-H\in[0,1).
\tag{2.2}
\]

Uniformly in the present range,

\[
 \log\lambda_H
 =\frac{H^2}{m}-\frac{H^2}{2m^2}
  +O\!\left(\frac{H^4}{m^3}+\frac H{m^2}\right).
\tag{2.3}
\]

All terms after \(H^2/m\) are \(o(H/m)\) at (0.1).  Moreover

\[
 \frac{H^2}{m}
 =\log m-2\delta_m\frac Hm+o(H/m),
\tag{2.4}
\]

whereas

\[
 \log M=\log m+\frac Hm+o(H/m).
\tag{2.5}
\]

Thus

\[
 \log\theta=(1+2\delta_m+o(1))\frac Hm.
\tag{2.6}
\]

In particular \(\log\theta=O(H/m)=o(1)\), and therefore

\[
 1-\theta^{-1}
 =1-e^{-\log\theta}
 =(1+2\delta_m+o(1))\frac Hm.
\tag{2.7}
\]

Substitution into (2.1) gives (0.4).  Finally

\[
 \frac{NH/m}{N/\sqrt m}=\frac H{\sqrt m}
 =(1+o(1))\sqrt{\log m}\longrightarrow\infty.
\]

This proves the theorem. \(\square\)

The conclusion uses the exact floor in (0.1), not merely
\(H\sim\sqrt{m\log m}\). The floor displacement \(\delta_m\) fixes the
coefficient in (2.7); in particular its sign cannot reverse.

## 3. The exact trajectory invariant

The capacity obstruction persists at every time, independently of how a
matching is generated.

### Lemma 3.1 (root--target residual identity)

After any \(r\) matching edges have been selected, let

\[
 x=\frac{N-r}{N},\qquad y=\frac{W-Mr}{W}
\tag{3.1}
\]

be the residual root and target densities.  Then

\[
                         \boxed{y=\theta x-(\theta-1).}
\tag{3.2}
\]

#### Proof

Use \(MN=\theta W\) in (3.1):

\[
 y=1-\frac{Mr}{W}
  =1-\theta(1-x)=\theta x-(\theta-1).
\]

\(\square\)

In particular \(y\ge0\) forces \(x\ge1-1/\theta\).  A multiround
invariant which treats both shores as having a common multiplicative
residual density is already incompatible with (3.2) near the terminal
scale.  Equation (3.2), rather than a concentration estimate, is the
first invariant every proposed sparse-round proof must respect.

## 4. What the fresh isolated bite actually proves

The scalar obstruction does not invalidate the favorable one-round
geometry.  It only limits its terminal point.

For an edge \(e\), let \(\Gamma(e)\) be the set of catalogue edges
meeting \(e\), including \(e\).  The exact ring-local pair calculation is

\[
 \sum_{\{Y,Z\}\subset e\cap\mathcal Y}D(Y,Z)
 =\left(\frac2m+O(m^{-2})\right)D.
\tag{4.1}
\]

The sum of the root--target codegrees inside \(e\) is \(M H!m!\), which
is superpolynomially smaller than \(R\).  Bonferroni's first two terms
therefore give, uniformly in \(e\),

\[
 \boxed{
 |\Gamma(e)|=(R+MD)(1+O(m^{-2})).}
\tag{4.2}
\]

Indeed \(R+MD\) is the sum of the degrees of the \(M+1\) vertices in
\(e\), and (4.1) together with (1.3) is only an \(O(m^{-2})\) relative
correction.

Fix \(\gamma>0\).  Mark every catalogue edge independently with

\[
                         \rho=\frac\gamma{R+MD},
\tag{4.3}
\]

and retain a marked edge exactly when no other marked edge meets it.

### Proposition 4.1 (valid fresh-round hazards)

Put \(a_\gamma=\gamma e^{-\gamma}\).  Uniformly over roots \(A\) and
middle targets \(Y\),

\[
 \Pr(A\text{ is covered})
 =\frac{a_\gamma+o(1)}{1+M\theta},
\tag{4.4}
\]

\[
 \Pr(Y\text{ is covered})
 =\frac{a_\gamma\theta+o(1)}{1+M\theta}.
\tag{4.5}
\]

Consequently the expected number of retained edges is

\[
             \frac{(a_\gamma+o(1))NR}{R+MD}
             =\frac{(a_\gamma+o(1))N}{1+M\theta}.
\tag{4.6}
\]

#### Proof

By (4.2), a fixed edge is retained with probability

\[
 \rho(1-\rho)^{|\Gamma(e)|-1}
 =\frac{a_\gamma+o(1)}{R+MD}.
\tag{4.7}
\]

Retained edges through one vertex are mutually exclusive.  Sum (4.7)
over the \(R\) edges through a root and over the \(D=\theta R\) edges
through a middle target.  This proves (4.4)--(4.5).  Summing over roots
proves (4.6). \(\square\)

### Proposition 4.2 (fresh-round count and lower-link concentration)

Let \(Z\) be the number of retained edges in Proposition 4.1. Then

\[
                         \operatorname {Var}Z=O_\gamma(\mathbb EZ),
\tag{4.8}
\]

and hence \(Z=(1+o(1))\mathbb EZ\) with probability tending to one.

There is also a simultaneous lower-link statement. Delete aggressively
every vertex lying in any marked edge, whether or not that marked edge is
isolated. Let \(Z_v^{\rm ag}\) be the number of original catalogue edges
through \(v\) which survive this aggressive deletion, and put
\(d_v=R\) on roots and \(d_v=D\) on targets. For either vertex type,

\[
 \mathbb E Z_v^{\rm ag}=(e^{-\gamma}+o(1))d_v,\qquad
 \operatorname {Var}Z_v^{\rm ag}=O_\gamma(d_v^2/m).
\tag{4.9}
\]

Consequently some outcome of the fresh bite has the asymptotic retained
edge count (4.6), and all but \(o(N)\) roots and \(o(W)\) targets have
actual residual degree at least

\[
                         (e^{-\gamma}-o(1))d_v.
\tag{4.10}
\]

#### Proof

Let \(\mathscr E\) be the catalogue edge set and
\(L=|\Gamma(e)|\), which is independent of \(e\) by transitivity.
For distinct nonmeeting edges \(e,f\), put
\(C(e,f)=|\Gamma(e)\cap\Gamma(f)|\). Their retention covariance is at
most

\[
                         C_\gamma\rho^3 C(e,f),
\tag{4.11}
\]

because \(\rho C(e,f)\le\rho L=O_\gamma(1)\) and
\((1-\rho)^{-C(e,f)}-1\le C_\gamma\rho C(e,f)\). Meeting edges have
nonpositive retention covariance. Moreover

\[
 \sum_{e,f\in\mathscr E} C(e,f)
 =\sum_{g\in\mathscr E}|\Gamma(g)|^2
 =|\mathscr E|L^2.
\tag{4.12}
\]

Since \(\rho=\Theta_\gamma(L^{-1})\) and
\(\mathbb EZ=\Theta_\gamma(|\mathscr E|/L)\), summing (4.11), together
with the individual variances, proves (4.8).

For the link assertion define

\[
 c_v(e)=\#\{f\in\mathscr E:v\in f,\ f\cap e\ne\varnothing\},\qquad
 T_v=\sum_e c_v(e)^2.
\tag{4.13}
\]

The full catalogue satisfies

\[
                         T_v=O(d_v^3).
\tag{4.14}
\]

If \(v\) is a middle target, the \(D\) edges containing \(v\) contribute
\(D^3\). For an edge \(e\not\ni v\), the exact option-influence bound
from (1.4) is \(c_v(e)=O(D/m)\), while reverse counting gives

\[
                         \sum_e c_v(e)
 =\sum_{f\ni v}|\Gamma(f)|=O(MD^2).
\tag{4.15}
\]

Thus the remaining contribution is \(O(D^3)\). If \(v\) is a root, the
edges through \(v\) contribute \(R^3\). Off that root,
\(c_v(e)\le M H!m!\), and reverse counting gives total link mass
\(O(MR^2)\). Since

\[
                         \frac{M^2H!m!}{R}
 =\frac{M^3}{\binom MH}=o(1),
\tag{4.16}
\]

the off-root contribution is \(o(R^3)\). This proves (4.14).

An edge \(f\ni v\) survives the aggressive deletion precisely when no
edge in \(\Gamma(f)\) was marked, giving the mean in (4.9). For
\(f,g\ni v\), the same calculation as (4.11), now without the two
initial marking factors, bounds their survival covariance by

\[
                         C_\gamma\rho C(f,g).
\]

The identity

\[
 \sum_{f,g\ni v}C(f,g)=\sum_e c_v(e)^2=T_v
\tag{4.17}
\]

and (4.14) yield

\[
 \operatorname {Var}Z_v^{\rm ag}
 \le d_v+C_\gamma\rho T_v
 =O_\gamma(d_v^2/m),
\]

because \(\rho=\Theta_\gamma((mR)^{-1})\) and \(d_v=\Theta(R)\).
Chebyshev with, for example, deviation \(m^{-1/4}d_v\), followed by
averaging over each vertex type, leaves only \(O(m^{-1/2})\) expected
exceptional proportion. Markov and (4.8) give a common outcome. Finally
the aggressive residual is contained in the actual residual, so its
surviving degree is a lower bound for the actual one. This proves
(4.10). \(\square\)

The two hazards differ by the exact factor \(\theta\), as required by
(3.2).  Iterating the ideal hazards for \(\Theta(m\log m)\) rounds would
drive the target shore to zero when the root density reaches
\(1-1/\theta\), not when it reaches \(o(m^{-1/2})\).

The missing probabilistic step even before that floor is a hereditary
global overlap condition.  Pair codegrees prove (4.2) only for the full
catalogue.  After several bites, a useful one-step sufficient condition
at a vertex \(v\) is

\[
 T_v(\mathcal H)
 :=\sum_{e\in\mathcal H}
 \#\{f\in\mathcal H:v\in f,\ f\cap e\ne\varnothing\}^{2}
 =O(d_v(\mathcal H)^3).
\tag{4.18}
\]

Proposition 4.2 proves (4.18) at time zero. Pair codegrees alone do not
imply that (4.18) regenerates in an endogenous residual. More importantly,
proving (4.18) through all rounds
would still not defeat Theorem 2.1.

## 5. Why product regeneration is the wrong replacement

For a middle target \(Y\), the roots capable of selecting it form the
star

\[
                    \mathcal R(Y)=\binom{Y}{m-H},
 \qquad |\mathcal R(Y)|=\binom mH=:R_0.
\tag{5.1}
\]

A uniform frame at one such root selects \(Y\) with probability

\[
                    p=\frac M{\binom MH},
 \qquad R_0p=\theta.
\tag{5.2}
\]

The block-factor hole theorem applies verbatim: if the roots are divided
into independent correlation blocks of size at most \(b\), with arbitrary
dependence inside blocks and uniform one-root marginals, then \(bp=o(1)\)
implies an expected

\[
                         (e^{-1}-o(1))W
\tag{5.3}
\]

missed middle targets.  Any law supported on selections with \(o(W)\)
holes must instead have

\[
 \boxed{
 b\ge(1-o(1))p^{-1}
   =(1-o(1))\theta^{-1}\binom mH.}
\tag{5.4}
\]

Thus a claimed multiround proof cannot regenerate by independently
resampling bounded, polynomial, or otherwise
\(o(\binom mH)\)-sized root blocks.  This statement does not refute a
global random-greedy matching: its conflict rule couples all roots in
\(\mathcal R(Y)\) through the common target \(Y\).  It does refute the
usual product-residual surrogate and every local completion of that
form.

## 6. The minimal surviving global theorem

For a choice \(\sigma=(\pi_A)_{A\in\mathcal A}\) of one frame at every
root, let

\[
 \ell_\sigma(Y)
 =\#\{A:Y\text{ is a cyclic }H\text{-window target of }(A,\pi_A)\}.
\tag{6.1}
\]

The total load is fixed:

\[
                         \sum_Y\ell_\sigma(Y)=MN=W+E.
\tag{6.2}
\]

Let

\[
 h(\sigma)=\#\{Y:\ell_\sigma(Y)=0\},\qquad
 c(\sigma)=\sum_Y(\ell_\sigma(Y)-1)_+.
\tag{6.3}
\]

Then the elementary load identity is

\[
                         \boxed{c(\sigma)=E+h(\sigma).}
\tag{6.4}
\]

Hence \(h(\sigma)=o(W)\) is exactly enough for \(o(W)\) middle collision
mass while retaining every root.  The cleanest sufficient statement is
the following.

> **Global promotion-ring representative theorem (GPR).**  There is a
> choice of one cyclic frame at every root such that
> \[
>                         h(\sigma)=o(W).
> \tag{6.5}
> \]
> The choice is made from a support which, after symmetrization, is not a
> product over blocks of size \(o(\binom mH)\).

For later all-depth coupling, a useful arbitrary-dual strengthening is:
there is \(\varepsilon_m\to0\) such that for every nonnegative weight
vector \(w=(w_Y)\), one can choose \(\sigma\) with

\[
 \sum_Yw_Y\mathbf1_{\{\ell_\sigma(Y)=0\}}
 \le\varepsilon_m\sum_Yw_Y.
\tag{6.6}
\]

By finite minimax, (6.6) is equivalent to a globally supported
distribution on complete root selections for which every target is
missed with probability at most \(\varepsilon_m\).  Taking \(w\equiv1\)
then gives (6.5).  The block-factor theorem says that such a distribution
must have root-star-scale dependence; it gives no contradiction to its
existence.

Neither (6.5) nor (6.6) is proved here.  They are the correct
capacity-compatible replacement for the refuted matching target.  An
all-depth fcpath construction needs a nested weighted version, not merely
the middle statement.

## 7. Audited boundary

Proved:

1. the exact degrees and pair-codegree normalization;
2. the exact matching floor (0.4), which refutes root leave
   \(o(N_H/\sqrt m)\) at the prescribed \(H\);
3. the deterministic multiround residual identity (3.2);
4. the fresh isolated-bite hazards (4.4)--(4.6);
5. fresh-round count and lower-link concentration, Proposition 4.2;
6. the exact load identity (6.4); and
7. the necessity of root-star-scale dependence for any product-block
   completion.

Not proved:

1. GPR or its arbitrary-dual form (6.6);
2. hereditary propagation of the overlap statistic (4.18); or
3. the nested all-depth representative theorem required by fcpath.

The sharp conclusion is therefore negative for the assigned ordinary
matching theorem and positive only at one round.  Overflow-aware,
fibre-dense global representation is not an optional absorber refinement;
it is forced first by the scalar capacity floor and then by the block-hole
theorem.
