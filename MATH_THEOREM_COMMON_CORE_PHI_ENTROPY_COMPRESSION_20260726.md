# The common-core coefficient gate: exact entropy compression and failure of factorwise support convexity

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Scope and conclusion

Put

\[
 n=2m,\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N=\binom{2m}{m-H},
\tag{0.1}
\]

and assume

\[
 H=(1+o(1))\sqrt{m\log m},\qquad m>5H.
\tag{0.2}
\]

At every root \(A\in\binom{[2m]}{m-H}\), retain a common-core tight
path of length

\[
 r=m-3H+1.
\tag{0.3}
\]

Equivalently, in the repaired cyclic-ring formulation, delete

\[
 k=M-r=4H-1
\tag{0.4}
\]

consecutive phases.  Let \(\Omega_A\) be the full all-core transitive
catalogue of labelled path options (the core is part of the option),
and let \(e(A,\pi)\) be the \(r\)
middle targets in option \(\pi\).  Define

\[
 P_A(\mathbf z)=\sum_{\pi\in\Omega_A}
        \prod_{D\in e(A,\pi)}z_D,
 \qquad P(\mathbf z)=\prod_AP_A(\mathbf z).
\tag{0.5}
\]

For a deterministic choice \(\omega=(\pi_A)_A\), write \(L_D(\omega)\)
for its load at \(D\in\binom{[2m]}m\), and put

\[
\Phi(\omega)=\sum_D\binom{L_D(\omega)}2.
\tag{0.6}
\]

This is the packing-side nonlinear coefficient defect: it vanishes
exactly when the selected path monomials are pairwise target-disjoint.
It is also the original floor energy up to the forced path deficit.  In
fact, with \(\psi(l)=(l-1)(l-2)/2\),

\[
 \Phi_{\rm floor}(\omega):=\sum_D\psi(L_D(\omega))
 =\Phi(\omega)+W-rN
 =\Phi(\omega)+\delta W.
\tag{0.6a}
\]

Consequently \(\min\Phi=o(W)\) is equivalent to
\(\min\Phi_{\rm floor}=o(W)\) in the calibrated common-core regime.

Write

\[
 C=\binom MH,\qquad R=\binom mH,\qquad
 \Lambda={W\over N}={C\over R},\qquad
 \rho={rN\over W}={r\over\Lambda},\qquad
 \delta=1-\rho.
\tag{0.7}
\]

We assume the packing calibration \(0\le\delta=o(1)\), which holds in
the common-core atlas regime.

This note proves four exact facts.

1. Under the product of the uniform root-factor measures,

   \[
   \mathbb E\Phi
    ={W\rho^2\over2}\left(1-{1\over R}\right)
    =\left({1\over2}+o(1)\right)W,
   \tag{0.8}
   \]

   and the expected number of holes is \((e^{-1}+o(1))W\).
   In fact

   \[
   \operatorname {Var}\Phi\le 2Nr^2R^2=o(W^2),
   \tag{0.8a}
   \]

   so \(\Phi/W\to1/2\) in probability.  Thus an ordinary second-
   moment argument rigorously concentrates at the wrong plateau.

2. Let \(\mathbb Q\) denote that product law.  Every global coupling
   \(\mathbb P\) with

   \[
   \mathbb E_{\mathbb P}\Phi\le\varepsilon W,
   \qquad \delta+\varepsilon=o(1),
   \tag{0.9}
   \]

   obeys the nonlinear entropy lower bound

   \[
   \boxed{
   D_{\rm KL}(\mathbb P\Vert\mathbb Q)
      \ge(1-o(1)){W\over\binom MH}
      =(1-o(1)){N\over\binom mH}.}
   \tag{0.10}
   \]

   Its logarithmic scale is

   \[
   \log {W\over\binom MH}
    =2m\log2-\left({1\over2}+o(1)\right)
       \sqrt m\,(\log m)^{3/2}.
   \tag{0.10a}
   \]

   Consequently

   \[
   \boxed{
   \mathbb Q\{\Phi\le\varepsilon W\}
      \le
      \exp\!\left(-(1-o(1)){W\over\binom MH}\right).}
   \tag{0.11}
   \]

   Equivalently, if \(F=|\Omega_A|\), then the total number of product
   terms contributing load monomials of defect at most \(\varepsilon W\)
   is at most

   \[
   F^N\exp\!\left(-(1-o(1)){W\over\binom MH}\right).
   \tag{0.12}
   \]

   Thus a low-defect coefficient, if it exists, lies in an
   exponentially compressed part of the product support.  It cannot be
   obtained by treating the product law's second moment as typical.

3. Every \(b=o(m/H)\) target cluster has exact floor-event probability
   between \(e^{-(1+o(1))b}\) and
   \(e^{-(1-\log2-o(1))b}\).  Its entropy toll is only linear in \(b\),
   and root-scope overlap prevents all such bounded-cluster inequalities
   from improving the global scale \(W/\binom MH\).  Any cluster-entropy
   route based on only linear local tolls needs cluster size at least
   \(\Omega(\binom MH\,m/H)\), hence genuinely catalogue-scale
   chronology.

4. Every individual full all-core path factor has non-\(M\)-convex
   support.  In particular it is neither a homogeneous real-stable
   multiaffine polynomial nor a Lorentzian polynomial.  Hence the
   fractional barycentre in the Newton polytope cannot be rounded to a
   floor coefficient by the standard stable/Lorentzian support-saturation
   theorem.

The all-core qualification is essential: a catalogue with one
preassigned core is not transitive on the middle targets.  No estimate
\(\min\Phi=o(W)\) or \(\min\Phi=\Omega(W)\) follows from
these statements.  The positive content is an exact nonlinear entropy
scale; the negative content is that both ordinary product typicality and
factorwise discrete-convex support are unavailable.

## 1. One-target product law

Fix a middle target \(D\).  Its eligible roots are

\[
 \mathcal R(D)=\{A:A\subset D,\ |A|=m-H\},
 \qquad |\mathcal R(D)|=R.
\tag{1.1}
\]

For a fixed eligible root \(A\), transitivity of the local catalogue on
the \(C\) possible residual \(H\)-sets gives

\[
 q:=\Pr_{\pi\in\Omega_A}(D\in e(A,\pi))={r\over C}.
\tag{1.2}
\]

The flag count

\[
 NC=WR
\tag{1.3}
\]

gives \(Rq=\rho\).  Under \(\mathbb Q\), the \(R\) eligible root
variables are independent, and therefore

\[
                         L_D\sim\operatorname {Bin}(R,q).
\tag{1.4}
\]

### Proposition 1.1 (exact independent energy and hole count)

One has

\[
 \mathbb E_{\mathbb Q}\Phi
 =W\binom R2q^2
 ={W\rho^2\over2}\left(1-{1\over R}\right),
\tag{1.5}
\]

and

\[
 \mathbb E_{\mathbb Q}|\{D:L_D=0\}|
 =W(1-q)^R=(e^{-1}+o(1))W.
\tag{1.6}
\]

#### Proof

Equation (1.5) follows by applying
\(\mathbb E\binom{\operatorname {Bin}(R,q)}2=\binom R2q^2\) to every
target.  For (1.6), use \(Rq=\rho=1-o(1)\), \(q=o(1)\), and
\((1-q)^R=e^{-1+o(1)}\). \(\square\)

Thus the unconditioned coefficient measure sits at the constant
\(1/2\), not at \(o(W)\).

### Proposition 1.2 (the product plateau is concentrated)

One has

\[
 \operatorname {Var}_{\mathbb Q}\Phi\le2Nr^2R^2=o(W^2).
\tag{1.7}
\]

Consequently \(\Phi/W\to1/2\) in \(\mathbb Q\)-probability.

#### Proof

Resample the path at one root.  Only the at most \(2r\) owners in the
old or new path can change load.  At any such owner, toggling the
chosen root changes \(\binom{L_D}{2}\) in absolute value by at most
\(R-1\).  Hence the total change in \(\Phi\) is at most \(2rR\).
The Efron--Stein inequality gives

\[
 \operatorname {Var}\Phi
 \le {1\over2}N(2rR)^2=2Nr^2R^2.
\]

Now \(N=\Theta(W/m)\), \(r=O(m)\), and
\(\log R=O(H\log(m/H))=o(m)\), whereas
\(\log W=(2\log2+o(1))m\).  Therefore

\[
 {Nr^2R^2\over W^2}
 =O\!\left({mR^2\over W}\right)=o(1).
\]

Combine this with Proposition 1.1 and \(\rho\to1\). \(\square\)

## 2. A one-star entropy toll

The local entropy cost can first be computed exactly.  Let
\(Q_{R,p}=\operatorname {Ber}(p)^{\otimes R}\), put
\(K=\sum_{i=1}^RX_i\), and suppose a law \(\mu\) has all coordinate
marginals equal to \(p\).  If \(K\in\{a,a+1\}\) almost surely, where
\(a\le Rp\le a+1\), then its two layer masses are forced to be

\[
 \alpha=a+1-Rp,\qquad \beta=Rp-a.
\tag{2.a}
\]

Writing

\[
 q_j=\binom Rj p^j(1-p)^{R-j},
\tag{2.b}
\]

one has the exact bound

\[
 D_{\rm KL}(\mu\Vert Q_{R,p})
 \ge \alpha\log{\alpha\over q_a}
       +\beta\log{\beta\over q_{a+1}}.
\tag{2.c}
\]

Equality holds precisely for the mixture which is uniform within each
of the two Hamming layers.  Indeed the cross-entropy against
\(Q_{R,p}\) is fixed by the coordinate marginals, so minimizing
relative entropy is the same as maximizing entropy; conditioning on
\(K\) proves the assertion.  In the common-core packing case \(a=0\),
this specializes to

\[
 \kappa_-
 =(1-\rho)\log(1-\rho)-(R-\rho)\log(1-p)
 =1-o(1).
\tag{2.d}
\]

Thus the one-nat toll below is sharp already at the isolated-star
level; it is not an artifact of binary data processing.

Let \(\mathbb P\) be any law on the product configuration space.
Average it under \(S_{2m}\), and call the result \(\overline{\mathbb P}\).
The product law \(\mathbb Q\) and the energy \(\Phi\) are invariant, so

\[
 D_{\rm KL}(\overline{\mathbb P}\Vert\mathbb Q)
 \le D_{\rm KL}(\mathbb P\Vert\mathbb Q),
 \qquad
 \mathbb E_{\overline{\mathbb P}}\Phi
 =\mathbb E_{\mathbb P}\Phi.
\tag{2.0}
\]

The first inequality is convexity of relative entropy.  Transitivity on
root-option pairs makes every one-root marginal of the orbit average
uniform.  It is therefore enough
to prove the entropy lower bound for an invariant law, and we henceforth
rename \(\overline{\mathbb P}\) as \(\mathbb P\).  By invariance, the law of
\(L_D\) is the same for every \(D\).  Put

\[
                         K=L_D.
\tag{2.1}
\]

Under (0.9),

\[
 \mathbb E_{\mathbb P}K=\rho,
 \qquad
 \mathbb E_{\mathbb P}\binom K2\le\varepsilon.
\tag{2.2}
\]

Since \(\mathbf1_{\{K\ge2\}}\le\binom K2\) and
\((K-1)_+\le\binom K2\),

\[
 \Pr_{\mathbb P}(K\ge2)\le\varepsilon
\tag{2.3}
\]

and the identity

\[
 \Pr(K=0)=1-\mathbb EK+\mathbb E(K-1)_+
\tag{2.4}
\]

gives

\[
 \Pr_{\mathbb P}(K\ne1)\le\delta+2\varepsilon=o(1).
\tag{2.5}
\]

Under \(\mathbb Q\), on the other hand,

\[
 b_m:=\Pr_{\mathbb Q}(K=1)
 =Rq(1-q)^{R-1}=e^{-1}+o(1).
\tag{2.6}
\]

Let \(\mathbb P_D\) and \(\mathbb Q_D\) be the laws of all root
variables in \(\mathcal R(D)\).  Project first to their incidence
indicators at \(D\), and then to the event \(\{K=1\}\).  The
data-processing inequality gives

\[
 D_{\rm KL}(\mathbb P_D\Vert\mathbb Q_D)
 \ge d_{\rm bin}\bigl(\Pr_{\mathbb P}(K=1)\Vert b_m\bigr)
 =1-o(1),
\tag{2.7}
\]

where the last equality uses (2.5)--(2.6).  Thus every almost-floor
target star costs asymptotically one nat relative to the product law.

## 3. Overlap-corrected global entropy

Every root \(A\) belongs to exactly

\[
                         C=\binom MH
\tag{3.1}
\]

target stars \(\mathcal R(D)\).  The following is the precise place at
which their enormous overlap enters.

### Lemma 3.1 (star-relative-entropy Shearer inequality)

If \(\mathbb P\) has the same one-root marginals as the product law
\(\mathbb Q\), then

\[
 \sum_D D_{\rm KL}(\mathbb P_D\Vert\mathbb Q_D)
 \le C D_{\rm KL}(\mathbb P\Vert\mathbb Q).
\tag{3.2}
\]

#### Proof

Let \(F=|\Omega_A|\), independent of \(A\).  Uniform one-root
marginals give

\[
 D_{\rm KL}(\mathbb P_D\Vert\mathbb Q_D)
 =|\mathcal R(D)|\log F-H_{\mathbb P}(Y_{\mathcal R(D)}).
\tag{3.3}
\]

Summing the first term over \(D\) counts each root exactly \(C\) times.
Shearer's entropy inequality for the \(C\)-fold cover
\((\mathcal R(D))_D\) says

\[
 \sum_DH_{\mathbb P}(Y_{\mathcal R(D)})
 \ge C H_{\mathbb P}(Y_{\mathcal A}).
\tag{3.4}
\]

Substitution in (3.3) gives

\[
 \sum_DD_{\rm KL}(\mathbb P_D\Vert\mathbb Q_D)
 \le C\bigl(N\log F-H_{\mathbb P}(Y_{\mathcal A})\bigr),
\]

which is (3.2). \(\square\)

### Theorem 3.2 (global entropy-compression floor)

Under (0.9), equation (0.10) holds.

#### Proof

Sum (2.7) over the \(W\) targets and apply Lemma 3.1:

\[
 (1-o(1))W
 \le\sum_DD_{\rm KL}(\mathbb P_D\Vert\mathbb Q_D)
 \le C D_{\rm KL}(\mathbb P\Vert\mathbb Q).
\]

Finally, (1.3) gives \(W/C=N/R\). \(\square\)

Stirling's formula gives
\(\log W=2m\log2+O(\log m)\) and

\[
 \log\binom MH
 =H\log(M/H)+O(H)
 =\left({1\over2}+o(1)\right)
    \sqrt m\,(\log m)^{3/2},
\]

which proves the scale (0.10a).

### Corollary 3.3 (low-energy coefficients are exponentially rare)

Let

\[
                         \mathcal E_\varepsilon
 =\{\omega:\Phi(\omega)\le\varepsilon W\}.
\tag{3.5}
\]

If \(\mathcal E_\varepsilon\ne\varnothing\), the conditional law
\(\mathbb P=\mathbb Q(\cdot\mid\mathcal E_\varepsilon)\) is invariant.
Transitivity on root-option pairs makes every one-root marginal uniform.
Moreover

\[
 D_{\rm KL}(\mathbb P\Vert\mathbb Q)
 =-\log\mathbb Q(\mathcal E_\varepsilon).
\tag{3.6}
\]

Theorem 3.2 therefore gives (0.11). \(\square\)

Since \(\mathbb Q\) is uniform on the \(F^N\) labelled product terms,
multiplying (0.11) by \(F^N\) gives the coefficient-count bound (0.12).
This counts representations, and therefore remains valid when several
representations contribute to the same load monomial.

This is a one-sided large-deviation theorem.  It proves rarity, not
emptiness: the right side of (0.11) is positive.

### Proposition 3.4 (sharp ceiling of isolated-star entropy)

Any proof obtained by assigning nonnegative weights \(a_D\) to the
individual target-star entropy inequalities and applying a fractional
packing with

\[
 \sum_{D\subset U}a_D\le1\qquad\text{for every root }U
\tag{3.7}
\]

has total star weight at most

\[
 \sum_Da_D\le {N\over R}={W\over C}.
\tag{3.8}
\]

The uniform choice \(a_D=1/C\) attains equality.  Since the exact
minimum local toll is \(1-o(1)\) by (2.d), the scale \(W/C\) in
Theorem 3.2 is optimal for every argument that only sums isolated-star
KL inequalities through a fractional cover.

#### Proof

Double-count the pairs \((U,D)\) with \(D\subset U\):

\[
 R\sum_Da_D
 =\sum_U\sum_{D\subset U}a_D\le N.
\]

The incidence identity \(NC=WR\) gives (3.8), and the uniform weights
give equality. \(\square\)

### Theorem 3.5 (bounded target clusters have only linear entropy cost)

Put \(\eta=H/m\).  For a family \({\cal C}\) of \(b\) distinct middle
targets, let

\[
 E_{\cal C}=\{L_D=1\text{ for every }D\in{\cal C}\}.
\tag{3.9}
\]

Uniformly over all such families with \(b\eta=o(1)\),

\[
 \exp(-(1+o(1))b)
 \le\mathbb Q(E_{\cal C})
 \le\exp(-(1-\log2-o(1))b).
\tag{3.10}
\]

Consequently, if an invariant global law \(\mathbb P\) has
\(\alpha=\mathbb P(L_D\ne1)\) and \(b\alpha=o(1)\), then, on the union
of the root scopes of \({\cal C}\),

\[
 D_{\rm KL}(\mathbb P_{\cal C}\Vert\mathbb Q_{\cal C})
 \ge(1-\log2-o(1))b.
\tag{3.11}
\]

Thus every cluster below the overlap scale \(m/H\) still has only a
linear, not superlinear, floor-event entropy.

#### Proof

If two distinct targets have Johnson distance \(t\), the number of
roots containing both is zero for \(t>H\), and otherwise equals

\[
 R_t=\binom{m-t}{H-t}
 =R{(H)_t\over(m)_t}\le {H\over m}R=\eta R.
\tag{3.12}
\]

For each \(D\in{\cal C}\), let \({\cal U}_D\) be the roots which
contain \(D\) and no other member of \({\cal C}\).  Then

\[
 u_D:=|{\cal U}_D|\ge R-(b-1)\eta R=(1-o(1))R.
\tag{3.13}
\]

Under \(\mathbb Q\), the numbers \(Z_D\) of hits from \({\cal U}_D\)
are mutually independent \(\operatorname {Bin}(u_D,q)\) variables, and
\(u_Dq=1-o(1)\).  The event \(E_{\cal C}\) implies \(Z_D\le1\) for
every \(D\).  Hence

\[
 \mathbb Q(E_{\cal C})
 \le\prod_D\mathbb Q(Z_D\le1)
 =\left({2\over e}+o(1)\right)^b,
\]

which is the upper bound in (3.10).

For the lower bound, require \(Z_D=1\) for every \(D\), and require
each remaining root to avoid all targets of \({\cal C}\) which it
contains.  If such a root contains \(t_A\ge2\) cluster targets, the
union bound gives avoidance probability at least \(1-t_Aq\).  Here
\(bq=o(1)\).  Moreover

\[
 \sum_{A:t_A\ge2}t_A
 \le2\sum_A\binom{t_A}{2}
 \le2\binom b2\eta R,
\tag{3.14}
\]

so the logarithmic cost of all shared-root avoidance constraints is at
most

\[
 O\!\left(qb^2\eta R\right)=O(b^2\eta)=o(b).
\tag{3.15}
\]

The unique-root exact-one probabilities are each

\[
 u_Dq(1-q)^{u_D-1}=e^{-1+o(1)}.
\]

All imposed conditions concern disjoint root variables, proving the
lower bound in (3.10).

Finally \(\mathbb P(E_{\cal C})\ge1-b\alpha=1-o(1)\).  Projecting both
laws to the indicator of \(E_{\cal C}\) and using the upper bound in
(3.10) proves (3.11). \(\square\)

### Proposition 3.6 (bounded-cluster overlap ceiling)

For every family \({\cal C}\) of \(b\) distinct targets, its union of
eligible-root scopes satisfies

\[
 \left|\bigcup_{D\in{\cal C}}{\cal R}(D)\right|
 \ge {bR\over1+(b-1)\eta}.
\tag{3.16}
\]

More generally, take weighted clusters \(({\cal C}_i,a_i)\) with
\(|{\cal C}_i|=b_i\le B\), and put

\[
 \kappa=\max_U\sum_{i:U\in\cup_{D\in{\cal C}_i}{\cal R}(D)}a_i.
\tag{3.17}
\]

Then

\[
 {\sum_i a_i b_i\over\kappa}
 \le(1+(B-1)\eta){N\over R}
 =(1+(B-1)\eta){W\over C}.
\tag{3.18}
\]

Thus weighted Shearer applied to cluster inequalities whose local toll
is only \(O(b_i)\) remains capped at \(O(W/C)\) whenever
\(B=o(m/H)\).  Even granting such a linear local toll at all scales, a
linear-in-\(W\) certificate by this mechanism would require

\[
 B=\Omega\!\left(C{m\over H}\right).
\tag{3.19}
\]

#### Proof

Let \(t_A\) count the cluster targets contained in root \(A\), and let
\(s\) be the number of roots with \(t_A>0\).  Equations (3.12) and
Cauchy--Schwarz give

\[
 (bR)^2=\left(\sum_At_A\right)^2
 \le s\sum_At_A^2
 \le s\bigl(bR+b(b-1)\eta R\bigr),
\]

which proves (3.16).  Double-counting weighted cluster--root incidences
now gives

\[
 N\kappa
 \ge\sum_i a_i
   \left|\bigcup_{D\in{\cal C}_i}{\cal R}(D)\right|
 \ge {R\over1+(B-1)\eta}\sum_i a_i b_i,
\]

and hence (3.18).  Weighted Shearer bounds the weighted sum of the
cluster KL divergences by \(\kappa D_{\rm KL}(\mathbb P\Vert\mathbb Q)\).
The final two assertions follow from (3.18). \(\square\)

## 4. Failure of factorwise algebraic support saturation

Fix one root \(A\), and identify its eligible middle targets with the
\(H\)-subsets of \(U=A^c\).  The support of every option is a family

\[
 E=\{J_1,\ldots,J_r\},
 \qquad
 J_i=\{z_i,z_{i+1},\ldots,z_{i+H-1}\},
\tag{4.1}
\]

of consecutive \(H\)-windows of one injective word of length
\(r+H-1=m-2H\).

### Lemma 4.1 (induced-path rigidity)

In the Johnson graph on \(\binom UH\), the graph induced by \(E\) is
exactly the path

\[
                         J_1J_2\cdots J_r.
\tag{4.2}
\]

#### Proof

Consecutive windows have Johnson distance one.  Windows whose starts
differ by \(d\), with \(2\le d<H\), have Johnson distance \(d\); starts
at distance at least \(H\) give disjoint windows and hence distance
\(H\).  The retained phase interval is linear, so there is no endpoint
adjacency. \(\square\)

### Lemma 4.2 (two cross-separated path supports)

For all sufficiently large \(m\), there are two option supports
\(E,F\in\operatorname {supp}P_A\) such that

\[
                         d_J(X,Y)\ge2
 \qquad(X\in E,\ Y\in F).
\tag{4.3}
\]

#### Proof

Fix \(E\) and choose a uniform labelled option \(F\).  Each fixed phase
window of \(F\) is a uniform member of \(\binom UH\).  For fixed
\(X\in E\),

\[
 \Pr(d_J(X,Y)\le1)
 ={1+H(M-H)\over\binom MH}.
\tag{4.4}
\]

A union bound over the at most \(r^2\) cross-pairs is \(o(1)\), because
\(\binom MH\) dominates every fixed power of \(m\) at (0.2).  Hence an
option satisfying (4.3) exists. \(\square\)

### Theorem 4.3 (non-\(M\)-convex root support)

The constant-cardinality set system \(\operatorname {supp}P_A\) fails
the basis-exchange axiom.  Consequently the exponent support of \(P_A\)
is not \(M\)-convex, and \(P_A\) is neither homogeneous real stable nor
Lorentzian.

#### Proof

Take \(E,F\) from Lemma 4.2 and choose an interior vertex
\(X=J_i\in E\), \(2\le i\le r-1\).  Removing \(X\) splits the induced
path (4.2) into two nonempty components.  By (4.3), every \(Y\in F\)
is nonadjacent in the Johnson graph to every member of \(E\).  Therefore
the induced graph on

\[
                         E-X+Y
\tag{4.5}
\]

is disconnected into at least three components.  Lemma 4.1 shows that
it cannot be an option support.  Thus, for this \(X\in E\setminus F\),
there is no \(Y\in F\setminus E\) for which \(E-X+Y\) lies in the
support.  This is the failure of basis exchange.

For a zero-one constant-sum exponent set, \(M\)-convexity is equivalent
to the matroid basis-exchange property.  Homogeneous multiaffine real-
stable polynomials have matroidal support, and Lorentzian polynomials
have \(M\)-convex support.  The two polynomial conclusions follow.
\(\square\)

The theorem does not say that the full product support lacks every
discrete-convex substructure.  It says that the standard factorwise route
-- prove each root factor stable or Lorentzian, multiply, and infer support
saturation from the Newton polytope -- is unavailable.

## 5. Exact boundary

Proved:

1. the exact product-law value \(\mathbb E\Phi=(1/2+o(1))W\);
2. concentration of that product-law plateau;
3. a one-nat entropy toll at every almost-floor target star;
4. the overlap-corrected global entropy lower bound (0.10);
5. the invariant low-energy large-deviation estimate (0.11);
6. the bounded-cluster linear-cost and overlap-ceiling theorems; and
7. failure of matroidal, real-stable, Lorentzian, and \(M\)-convex
   support at every individual root factor.

Not proved:

1. \(\min\Phi=o(W)\);
2. \(\min\Phi=\Omega(W)\);
3. a lower bound matching (0.11); or
4. hereditary regeneration of the repaired-path matching process.

The remaining positive theorem must therefore locate an exponentially
compressed correlated coefficient.  The remaining negative theorem must
prove that this compressed region is empty; entropy rarity alone does not
do so.
