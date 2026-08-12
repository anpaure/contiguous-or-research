# Promotion rings: the same-block triple floor and the global latent boundary

Date: 2026-07-26

Method: pure mathematics. No computation, solver, or external theorem is
used, apart from the standard total-unimodularity theorem for bipartite
flows in Section 8 (where a direct max-flow formulation is equivalent).

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad N=N_H=\binom{2m}{m-H},\qquad M=m+H,
\]

and use the covering-side calibrated height

\[
 H=\max\{h:\lambda_h\le m+h\},\qquad
 \lambda_h={W\over N_h}.
\tag{0.1}
\]

Then

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 m-H<\lambda_H\le m+H,
\tag{0.2}
\]

so all estimates below have their required critical normalization.

For a root \(A\in\binom{[2m]}{m-H}\), its promotion top is
\(U_A=[2m]\setminus A\).  A cyclic frame on \(U_A\) selects the middle
complements

\[
                         D=A\cup J,
\tag{0.3}
\]

where \(J\) runs over its \(M\) cyclic \(H\)-windows.  Complementing all
the \(D\)'s gives the usual middle owners, so middle support and hole
counts are unchanged.

Set

\[
 R=\binom mH,\qquad L=\binom MH,\qquad
 p={M\over L},\qquad
 \theta=Rp={MN\over W}=1+o(1).
\tag{0.4}
\]

The previously proved block-product theorem gives the necessary block
scale \(R^{1-o(1)}\).  The main result here is strictly stronger.

> **Same-block triple theorem.**  Partition the roots into blocks of size
> at most \(B\).  Inside a block the frames may have an arbitrary joint
> law, while distinct blocks are independent.  Assume only the balanced
> one-root marginal
> \[
>  \Pr(A\text{ selects }D)=p
>  \quad(A\subset D).
> \tag{0.5}
> \]
> If the expected number of missed middle targets is \(o(W)\), then, for
> every integer \(\tau\) satisfying
> \[
>  {H^2\over m\tau}=o(1),\qquad
>  \log\binom{m+\tau}{\tau}=o(\log R),
> \tag{0.6}
> \]
> one has
> \[
>  \boxed{
>  B\ge(1-o(1)){LR\over\binom{m+\tau}{\tau}}.}
> \tag{0.7}
> \]

Taking \(\tau=\lceil(\log m)^2\rceil\) gives

\[
                         \boxed{B\ge R^{2-o(1)}}
\tag{0.8}
\]

and

\[
 \boxed{
  \log B\ge(1+o(1))\sqrt m\,(\log m)^{3/2}.}
\tag{0.9}
\]

Conversely, if

\[
 B=o\!\left({LR\over\binom{m+\tau}{\tau}}\right),
\tag{0.10}
\]

then the expected middle-hole count is at least

\[
                         (e^{-1}-o(1))W.
\tag{0.11}
\]

Thus every independent-block promotion construction below the
\(R^{2-o(1)}\) scale fails.  Arcs, blanks, and tags cannot evade the
theorem, because they only delete occurrences from their underlying full
rings.

The second conclusion of this note is that **global latent support size is
not an obstruction**.  If one deterministic good selection exists, its
single common coordinate orbit gives balanced one-root marginals and has
support at most

\[
                         (2m)!=\exp(o(R)).
\tag{0.12}
\]

Moreover, without the cyclic-window constraint there is unconditionally
an exact globally coupled root--target resolution whose orbit already has
this support bound.  The only remaining deterministic condition is the
fibrewise cyclic tight-window geometry, jointly with the shallow shadow
ledger.

## 1. Exact root--target incidence

Fix a middle target \(D\in\binom{[2m]}m\).  Its compatible roots are

\[
 \mathcal R(D)=\{A\in\tbinom D{m-H}\},\qquad
 |\mathcal R(D)|=R.
\tag{1.1}
\]

For a fixed root \(A\), there are \(L=\binom MH\) possible middle targets
containing it.  A cyclic frame has exactly \(M\) distinct \(H\)-windows,
which proves (0.5) for a uniform cyclic frame.

The two incidence degrees satisfy

\[
 {L\over R}={W\over N}=\lambda_H.
\tag{1.2}
\]

Consequently

\[
                         Rp={MR\over L}={MN\over W}=\theta.
\tag{1.3}
\]

The calibration in (0.1) is essential here.  Maximality gives

\[
 \lambda_{H+1}=\lambda_H{m+H+1\over m-H}>m+H+1,
\]

and hence \(\lambda_H>m-H\).  Therefore

\[
 1\le\theta={M\over\lambda_H}
 <{m+H\over m-H}=1+O(H/m)=1+o(1).
\tag{1.4}
\]

Merely writing \(H=(1+o(1))\sqrt{m\log m}\), without the calibrated
one-sided condition, would not by itself imply (1.4).

## 2. Vanishing holes force one dominant block in almost every star

Let the root blocks be \(\mathcal B_1,\ldots,\mathcal B_s\), and for a
fixed target \(D\) put

\[
 r_j(D)=|\mathcal B_j\cap\mathcal R(D)|,
 \qquad \mu_j(D)=p\,r_j(D).
\tag{2.1}
\]

If \(Y_{j,D}\) is the number of roots in block \(j\) whose frames select
\(D\), then

\[
 \mathbb EY_{j,D}=\mu_j(D),\qquad
 \Pr(Y_{j,D}=0)\ge1-\mu_j(D)
\tag{2.2}
\]

whenever \(\mu_j(D)<1\).  Distinct blocks are independent.

Fix \(\varepsilon>0\).  If

\[
                     \max_j r_j(D)\le(1-\varepsilon)R,
\tag{2.3}
\]

then, by (1.4), eventually every \(\mu_j(D)\le1-\varepsilon/2\).  Thus

\[
 \begin{aligned}
 \Pr(D\text{ is missed})
 &\ge\prod_j(1-\mu_j(D))\\
 &\ge\exp\!\left(-{\sum_j\mu_j(D)\over1-\max_j\mu_j(D)}\right)\\
 &\ge\exp(-2\theta/\varepsilon).
 \end{aligned}
\tag{2.4}
\]

If some \(\mu_j(D)\ge1\), then already

\[
 r_j(D)\ge p^{-1}=R/\theta=(1-o(1))R.
\tag{2.5}
\]

It follows from (2.4), first for every fixed \(\varepsilon\) and then by
a diagonal choice \(\varepsilon=\varepsilon_m\downarrow0\), that
\(o(W)\) expected holes force

\[
 \boxed{
  \max_jr_j(D)=(1-o(1))R}
\tag{2.6}
\]

for all but \(o(W)\) targets \(D\).

This is the exact near-monochromatic-star consequence of block
independence.

## 3. The same-block triple double count

For every target satisfying (2.6), select one dominant block.  It contains

\[
                         (1-o(1))\binom R2
\tag{3.1}
\]

unordered pairs of distinct roots from \(\mathcal R(D)\).

Write two roots in the same target as

\[
                         A=D\setminus I,\qquad
                         A'=D\setminus I',
\tag{3.2}
\]

where \(I,I'\in\binom DH\).  Put

\[
 t=|I\cap I'|=m-|A\cup A'|.
\tag{3.3}
\]

For a uniform ordered pair of distinct \(H\)-sets \(I,I'\),

\[
 \mathbb Et
 ={RH^2/m-H\over R-1}
 \le {R\over R-1}{H^2\over m}.
\tag{3.4}
\]

Hence Markov's inequality and (0.6) show that the proportion of root pairs
inside a uniform target having \(t>\tau\) is \(o(1)\).  After deleting all
such pairs from (3.1), there remain

\[
                         (1-o(1))W\binom R2
\tag{3.5}
\]

same-block triples \((D,\{A,A'\})\) with \(t\le\tau\).

Conversely, fix distinct roots \(A,A'\) with parameter \(t\).  Their union
has size \(m-t\).  A middle target containing both is obtained by adjoining
\(t\) points from the \(m+t\) points outside their union.  Therefore the
number of such targets is exactly

\[
                         \binom{m+t}{t}.
\tag{3.6}
\]

For \(t\le\tau\), this is at most \(\binom{m+\tau}{\tau}\).  Consequently

\[
 (1-o(1))W\binom R2
 \le
 \binom{m+\tau}{\tau}
 \sum_j\binom{|\mathcal B_j|}{2}.
\tag{3.7}
\]

Since the blocks partition all \(N\) roots and have size at most \(B\),

\[
 \sum_j\binom{|\mathcal B_j|}{2}
 \le{(B-1)N\over2}.
\tag{3.8}
\]

Combining (3.7)--(3.8), using (1.2), gives the sharper form

\[
 B-1\ge(1-o(1)){L(R-1)\over\binom{m+\tau}{\tau}},
\tag{3.9}
\]

and hence, since \(R\to\infty\),

\[
 B\ge(1-o(1)){WR^2\over
 N\binom{m+\tau}{\tau}}
 =(1-o(1)){LR\over\binom{m+\tau}{\tau}},
\tag{3.10}
\]

which proves (0.7).

## 4. The converse linear-hole floor

Define

\[
 Q={1\over WR^2}\sum_D\sum_jr_j(D)^2.
\tag{4.1}
\]

Equivalently, choose \(D\) uniformly and then choose two independent
uniform roots \(A,A'\in\mathcal R(D)\).  Then \(Q\) is the probability
that \(A,A'\) lie in the same root block.

The calculation in Section 3, now used as an upper bound, gives

\[
 Q\le {H^2\over m\tau}
 +{B\binom{m+\tau}{\tau}\over LR}.
\tag{4.2}
\]

Under (0.10), equation (4.2) gives \(Q=o(1)\).  Hence, for all but
\(o(W)\) targets,

\[
 \sum_j\left({r_j(D)\over R}\right)^2=o(1),
 \qquad
 \max_j{r_j(D)\over R}=o(1).
\tag{4.3}
\]

For such a target, \(\max_j\mu_j(D)=o(1)\) and
\(\sum_j\mu_j(D)=\theta\).  Therefore

\[
 \begin{aligned}
 \Pr(D\text{ is missed})
 &\ge\prod_j(1-\mu_j(D))\\
 &=\exp\left(-\theta
   +O\!\left(\sum_j\mu_j(D)^2\right)\right)\\
 &=e^{-1}-o(1).
 \end{aligned}
\tag{4.4}
\]

Summing over the nonexceptional targets proves (0.11).  The little-\(o\)
hypothesis in (0.10) is important: this argument does not prove the
\(e^{-1}\) constant merely from
\(B\le(1-\varepsilon)LR/\binom{m+\tau}{\tau}\).

## 5. Critical asymptotics

For \(H=o(m)\), Stirling's formula gives

\[
 \log R
 =H\log{m\over H}+H
  +O\!\left({H^2\over m}+\log H\right).
\tag{5.1}
\]

At the calibrated height,

\[
 \log{m\over H}
 ={1\over2}(\log m-\log\log m)+o(\log m),
\tag{5.2}
\]

and hence

\[
 \log R
 =\left({1\over2}+o(1)\right)
   \sqrt m\,(\log m)^{3/2}.
\tag{5.3}
\]

Also \(L/R=\lambda_H=(1+o(1))m\), so

\[
                         \log L=\log R+O(\log m).
\tag{5.4}
\]

For \(\tau=\lceil(\log m)^2\rceil\),

\[
 \log\binom{m+\tau}{\tau}
 \le\tau\log{e(m+\tau)\over\tau}
 =O((\log m)^3)=o(\log R).
\tag{5.5}
\]

Substitution in (0.7) yields

\[
 \log B\ge2\log R-o(\log R)
 =(1+o(1))\sqrt m\,(\log m)^{3/2},
\tag{5.6}
\]

which proves (0.8)--(0.9).

## 6. The deterministic overlap-capacity residue

The triple count has a formulation which does not require a root
partition or a probability law.  Let \(\mathfrak C\) be any family of
candidate correlation cells, each a set of roots, and put

\[
 \Phi_\tau(\mathfrak C)=
 \sum_{C\in\mathfrak C}
 \sum_{\substack{\{A,A'\}\subset C\\
                  A\ne A',\ 0\le t(A,A')\le\tau}}
 \binom{m+t(A,A')}{t(A,A')}.
\tag{6.1}
\]

Suppose that for all but \(o(W)\) targets \(D\), some cell
\(C=C(D)\) contains \((1-o(1))R\) roots of \(\mathcal R(D)\).  Repeating
Section 3 inside the selected cell gives the necessary deterministic
condition

\[
 \boxed{
  \Phi_\tau(\mathfrak C)
  \ge(1-o(1))W\binom R2.}
\tag{6.2}
\]

This is the weakest residue of the same-block triple argument: it asks for
enough weighted low-overlap root pairs to support the near-monochromatic
stars.  When \(\mathfrak C\) is a partition into cells of size at most
\(B\), the upper bound

\[
 \Phi_\tau(\mathfrak C)
 \le\binom{m+\tau}{\tau}{(B-1)N\over2}
\tag{6.3}
\]

recovers (3.9).  Without a cell/locality hypothesis, (6.2) does not turn
into a latent-support lower bound.

## 7. Global latent variables: the exact overlap identity

Let \(\Omega\) be an arbitrary finite or countable global latent space;
no product structure is assumed.  For an atom \(\omega\), let

\[
 X_{A,D}(\omega)=
 \mathbf1\{\text{the choice at root }A\text{ selects }D\},
\]

and define the load

\[
                         \ell_D(\omega)=
 \sum_{A\in\mathcal R(D)}X_{A,D}(\omega).
\tag{7.1}
\]

For a deterministic full-ring atom \(\omega\), let

\[
 Z(\omega)=\#\{D:\ell_D(\omega)=0\}.
\]

Every root contributes exactly \(M\) middle occurrences, so
\(\sum_D\ell_D(\omega)=MN=\theta W\).  Splitting the targets according
to whether their load is zero or positive gives the pointwise identity

\[
 \boxed{
  \sum_D|\ell_D(\omega)-1|
   =(\theta-1)W+2Z(\omega).}
\tag{7.2}
\]

Thus, already deterministically, \(o(W)\) holes are equivalent to an
\(o(W)\) total \(L^1\) deviation from an exact root--target resolution.

Under the balanced full-ring marginal (0.5),

\[
                         \mathbb E\ell_D=Rp=\theta.
\tag{7.3}
\]

Let

\[
                         h_D=\Pr(\ell_D=0).
\tag{7.4}
\]

The following identity is exact:

\[
 \boxed{
  \mathbb E(\ell_D-1)_+=\theta-1+h_D.}
\tag{7.5}
\]

Indeed,

\[
 \mathbb E\ell_D
 =\Pr(\ell_D\ge1)+\mathbb E(\ell_D-1)_+
 =1-h_D+\mathbb E(\ell_D-1)_+.
\]

More strongly, the following \(L^1\) identity is exact:

\[
 \boxed{
  \mathbb E|\ell_D-1|=\theta-1+2h_D.}
\tag{7.6}
\]

Thus if \(W^{-1}\sum_Dh_D=o(1)\), then

\[
 {1\over W}\sum_D\mathbb E_\omega|\ell_D(\omega)-1|=o(1).
\tag{7.7}
\]

This is the weakest deterministic overlap-design condition forced without
block independence: outside weighted atom--target mass \(o(W)\), exactly
one compatible root selects the target.  Equivalently, the
root-star hit events form an approximate partition of the latent space,
not merely a family with balanced first moments.  A pairwise-collision
moment is not equivalent to (7.7) without additional maximum-load control,
because rare atoms may carry high multiplicity.

By averaging (7.7), some atom \(\omega\) itself satisfies

\[
                         \#\{D:\ell_D(\omega)\ne1\}=o(W).
\tag{7.8}
\]

Therefore a global latent law with small expected holes cannot avoid the
underlying deterministic near-resolution problem.

## 8. Why support \(\exp(o(R))\) cannot be a universal obstruction

Suppose one deterministic good cyclic-frame selection exists.  Apply one
uniform common coordinate permutation \(\sigma\in S_{2m}\) to the entire
selection.  Every orbit atom has exactly the same number of holes.  For a
fixed root, conditioning on its image makes the induced bijection on its
\(M\)-point complement uniform; hence its cyclic frame is uniform among
all directed cyclic frames.  Thus the orbit law has the balanced marginal
(0.5).  Transitivity on middle targets also makes every target's hole
probability exactly the deterministic hole fraction \(Z/W\).

Its support is at most \((2m)!\), while

\[
 \log((2m)!)=O(m\log m)=o(R).
\tag{8.1}
\]

Hence

\[
                         (2m)!=\exp(o(R)).
\tag{8.2}
\]

It follows that no theorem based only on the support size of one global
latent variable can rule out the desired design at the
\(\exp(o(R))\) scale.  Such a support bound is automatically available
once a single deterministic solution exists.

There is a matching elementary lower bound, but it lies on the same much
smaller scale.  If the latent variable deterministically specifies every
root frame and the marginal frame at one root is uniform, then

\[
 |\operatorname{supp}\Omega|\ge(M-1)!,\qquad
 H_{\rm Sh}(\Omega)\ge\log((M-1)!),
\tag{8.3}
\]

because a directed cyclic frame has \((M-1)!\) possible values and is a
function of the latent variable.  Yet

\[
 \log((M-1)!)=\Theta(m\log m)=o(R).
\tag{8.4}
\]

Thus both the unavoidable frame entropy and the orbit upper bound are
\(o(R)\); neither can yield the desired no-go.

There is also an unconditional exact statement before cyclic orderability.
Consider the bipartite containment graph between roots \(A\) and middle
targets \(D\).  It has root degree \(L\), target degree \(R\), and
\(L/R=\lambda_H\le M\).

First retain the full-ring row size \(M\).  For every target family
\(\mathcal X\), incidence double counting gives

\[
 R|\mathcal X|\le L|N(\mathcal X)|
 \le MR|N(\mathcal X)|.
\tag{8.5}
\]

Capacitated Hall therefore assigns every target to one containing root,
with no root receiving more than \(M\) targets.  Since every root has
\(L\ge M\) distinct neighbors, fill each root to exactly \(M\) distinct
targets.  The resulting deterministic relaxed incidence field has zero
holes and only

\[
                         MN-W=(\theta-1)W=o(W)
\tag{8.6}
\]

duplicate excess.  Orbit-averaging it gives support at most \((2m)!\)
and exact incidence marginal \(M/L=p\).  Thus simultaneous global star
overlap, with the correct full-ring row size and marginal, is already
solved before cyclic-window representability is imposed.

There is also an exact no-duplicate version at the promotion-arc row
sizes.  Put

\[
 a=\lfloor\lambda_H\rfloor,
 \qquad \rho=W-aN.
\tag{8.7}
\]

The fractional edge assignment \(x_{A,D}=1/R\) has target load one and
root load \(L/R=\lambda_H\).  The bipartite flow polytope

\[
 \sum_{A\subset D}x_{A,D}=1,qquad
 a\le\sum_{D\supset A}x_{A,D}\le a+1,qquad x_{A,D}\ge0
\tag{8.8}
\]

is integral.  Therefore there is an integral assignment in which every
target is assigned exactly once, exactly \(\rho\) roots receive \(a+1\)
targets, and all other roots receive \(a\) targets.

Orbit-averaging this one integral assignment gives a global latent law
with support at most \((2m)!\), exact unique target coverage in every
atom, and incidence marginal exactly \(1/R\).  Thus global overlap and
balanced ownership are already solved at support \(\exp(o(R))\).

## 9. The exact surviving deterministic condition

For the integral assignment in Section 8, put

\[
 \mathcal J_A=\{D\setminus A:D\text{ is assigned to }A\}
 \subseteq\binom{A^c}{H}.
\tag{9.1}
\]

Promotion chronology requires much more than (8.8).  For every root \(A\),
there must be a cyclic order

\[
                         z^A_0,z^A_1,\ldots,z^A_{M-1}
\tag{9.2}
\]

of \(A^c\), and one cyclic interval \(I_A\) of \(a\) or \(a+1\) phase
indices, such that

\[
 \boxed{
  \mathcal J_A=
  \bigl\{\{z^A_i,z^A_{i+1},\ldots,z^A_{i+H-1}\}:i\in I_A\bigr\}.}
\tag{9.3}
\]

In addition, the chosen phase tags and the induced lower and upper flags
must have aggregate physical shadow defect \(o(W)\).

Equation (9.3), together with that two-sided shadow condition, is the
weakest presently known deterministic overlap-design gate.  Sections
7--8 show that neither small global latent support, balanced marginals,
nor exact middle ownership adds a further obstruction.  Sections 2--5
show that attempting to realize (9.3) through independent product blocks
below \(R^{2-o(1)}\) is impossible.

## 10. Audit boundary

Proved here:

1. targetwise dominant-block concentration from vanishing expected holes;
2. the exact same-block triple count and the lower bound (0.7);
3. the converse \((e^{-1}-o(1))W\) hole floor in the little-\(o\) regime;
4. the critical \(R^{2-o(1)}\) asymptotics;
5. the deterministic overlap-capacity inequality (6.2);
6. the pointwise and global latent \(L^1\) identities (7.2) and (7.6);
7. the absence of any support-size obstruction at \(\exp(o(R))\); and
8. an exact globally coupled unbundled middle resolution.

Not proved:

1. a deterministic cyclic tight-window lift satisfying (9.3);
2. the common lower/upper shadow estimate; or
3. coefficient one.

The block theorem applies only when the final root choices genuinely
factor into independent blocks.  A single common permutation, a globally
conditioned recursion, or overlapping updates whose dependency graph is
connected do not satisfy that hypothesis.

The orbit argument uniformizes plain cyclic frames.  Tag and arc patterns
are transported with the orbit; it does not make arbitrary decoration
types uniform.  Likewise, a fixed external product decomposition must be
transported if the orbit is to remain inside that decorated architecture.
