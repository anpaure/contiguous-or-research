# The all-winding PBBS killed-transfer operator and the exact predecessor renewal-block gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
 \qquad G=2H-1,
\]

where \(A>0\) is fixed.  This note gives an exact transfer formulation of
the genuine PBBS two-point statistic, including firstness, all return
durations, and every winding.  It then puts the reduced
predecessor-passage process into an exact renewal-block normal form.

The outcome is a theorem-level reduction, not an evaluation of the final
asymptotic.

1.  On the full labelled PBBS state space, let \({\cal U}\) be the
    permutation matrix of one PBBS update, and let \(Q_j\) project onto
    states whose unmatched coordinate is \(j\).  The killed operator

    \[
      K_j=(I-Q_j){\cal U}
    \]

    gives the exact first-return partial permutation

    \[
      {\cal R}_{j,g}=Q_j{\cal U}K_j^{g-1}Q_j.
    \]

    Hence the diagonal projection onto genuine residence-\(\le H\)
    starts is

    \[
      \Pi_H=\sum_{j\in\mathbb Z_N}\sum_{g=1}^{G}
                 {\cal R}_{j,g}^{*}{\cal R}_{j,g}.
    \]

    Proper-prefix firstness is built into the powers of \(K_j\); it is
    not imposed after the count.

2.  If \(\Lambda_H\) projects onto the lifts of quotient cycles of length
    greater than \(H+1\), then, for

    \[
      {\cal E}_H=\Lambda_H\Pi_H,
    \]

    the genuine quotient statistics satisfy the exact trace identities

    \[
      \boxed{
      NR_H=\operatorname {Tr}{\cal E}_H,\qquad
      N\mathcal C_H=
       \sum_{u=1}^{H+1}
       \operatorname {Tr}
       ({\cal E}_H{\cal U}^{-2u}{\cal E}_H{\cal U}^{2u}).}
      \tag{0.1}
    \]

3.  Marking one-step first-maximum displacement by a Laurent variable
    separates winding exactly.  If a first return has gap \(2s+1\) and
    two-step winding \(w\), its marked exponent is

    \[
                         (s-w)N.                 \tag{0.2}
    \]

    Thus coefficient extraction in the killed operator gives mutually
    disjoint projections \({\cal E}_{H,w}\), \(w\ge0\), and

    \[
      \boxed{
      N\mathcal C_H^{w,w'}=
      \sum_{u=1}^{H+1}
       \operatorname {Tr}
       ({\cal E}_{H,w}{\cal U}^{-2u}
        {\cal E}_{H,w'}{\cal U}^{2u}).}
      \tag{0.3}
    \]

    In particular (0.1) does not merge positive winding into an
    uncontrolled error term.

4.  On a first-pruned core, the exact predecessor-active projection is a
    two-hit killed-transfer operator.  If the current selected equality
    particle is \(j\), its immediate predecessor is \(j-1\).  With

    \[
      K_{j-1}=(I-Q_{j-1}){\cal U},
    \]

    put

    \[
    {\cal B}_{j;a,b}=
      Q_{j-1}{\cal U}K_{j-1}^{b-1}Q_{j-1}
      {\cal U}K_{j-1}^{a-1}Q_j .                \tag{0.4}
    \]

    Then

    \[
      \boxed{
      {\cal A}_G=
       \sum_j\sum_{a,b\ge1\atop a+b\le G}
       {\cal B}_{j;a,b}^{*}{\cal B}_{j;a,b}}
      \tag{0.5}
    \]

    is exactly the indicator of the reduced predicate

    \[
       B_2(F)\le G.                               \tag{0.6}
    \]

    Thus (0.5), not an independent-occupancy surrogate, is the transfer
    operator appearing in the audited Pascal pullback.

5.  The killed operator has a surprising exact spectral form.  On every
    PBBS orbit, \(K_j\) is a direct sum of nilpotent Jordan chains whose
    lengths are the consecutive return gaps of coordinate \(j\):

    \[
      \boxed{K_j|_{\mathcal O}\simeq
             \bigoplus_i J_{g_{j,i}}.}           \tag{0.7}
    \]

    In particular every eigenvalue of \(K_j\) is zero.  The genuine
    asymptotic is therefore not a Perron-eigenvalue problem.  It is a
    distribution-and-alignment problem for a growing family of renewal
    chains.

6.  More precisely, if \(t_{b,i}\) are consecutive selections of one
    equality particle \(b\), \(g_{b,i}=t_{b,i+1}-t_{b,i}\), and \(b+1\)
    is its successor, then the complete predecessor-active count on that
    orbit is

    \[
      \boxed{
      \sum_i
      \#\{t_{b,i-1}<s<t_{b,i}:
          \kappa_s=b+1,\quad
          (t_{b,i}-s)+g_{b,i}\le G\}.}           \tag{0.8}
    \]

    This is a nearest-neighbour functional of two consecutive genuine
    renewal blocks: the suffix of the block before \(t_{b,i}\), and the
    next \(b\)-gap.  The one-gap histogram, the spectrum in (0.7), and
    all one-time marginals omit this alignment.

7.  The two-point ratio is exactly the Palm susceptibility of these
    block functionals:

    \[
      \boxed{
      {K_{r,H}\over S_{r,H}}
      =\mathbb E_{\rm active}^{\rm Pascal}
       \#\{1\le u\le H+1:
                   \text{the phase }2u\text{ is active}\}.}
      \tag{0.9}
    \]

    Therefore boundedness and divergence have a literal meaning.  At
    critical mass, a bounded value in (0.9) refutes \((ST_A)\), while
    divergence is necessary for \((ST_A)\).  No asymptotic for (0.9) is
    proved here.

8.  The exact mountain inverse fibre computes the bounded branch, not
    merely an abstract relaxation.  In the Gaussian regime

    \[
       h/\sqrt r\to c,\qquad A/2<c<A,
    \]

    with \(p=2h-1\) prime, its active phases have

    \[
      H{R^{\rm mt}_{r,h}\over|\Omega_{r,h}|}\to2Ac,
      \qquad
      {\mathcal C^{\rm mt}_{r,h;H}\over R^{\rm mt}_{r,h}}
          \to2Ac,                                 \tag{0.10}
    \]

    and their Palm count converges to
    \({\rm Poisson}(2Ac)\).  This is a genuine retained, zero-winding PBBS
    sector.  Its mass is only \(\exp(O(\sqrt r\log r))\), and its reduced
    core has period one, so it is not an \((ST_A)\) counterexample.  It
    proves that local predecessor renewal does not force divergence.

The exact surviving global problem is now unambiguous: determine the
Pascal-weighted alignment law in (0.8) on the long-period saddle cores.
A fixed-dimensional transfer matrix, a one-gap renewal law, or a dominant
eigenvalue of \(K_j\) cannot supply that law.

## 1. Labelled PBBS states and quotient traces

Let

\[
  \Omega_N=\binom{[N]}r
\]

be the set of labelled PBBS states, represented as cyclic binary words
with \(r\) ones and \(r+1\) zeroes.  Every state \(x\) has a unique
unmatched zero; denote its coordinate by

\[
  q(x)\in\mathbb Z_N.                             \tag{1.1}
\]

Let \(f:\Omega_N\to\Omega_N\) be one PBBS update and let
\({\cal U}\) be its permutation matrix:

\[
  {\cal U}e_x=e_{f(x)}.                           \tag{1.2}
\]

Cutting immediately after \(q(x)\) writes \(x\) uniquely as a spatial
rotation of \(0D\), where \(D\in\mathcal D_r\).  Hence

\[
  |\Omega_N|=NB_r.                                \tag{1.3}
\]

For \(j\in\mathbb Z_N\), let \(Q_j\) be the diagonal projection

\[
  Q_je_x=\mathbf1_{\{q(x)=j\}}e_x.               \tag{1.4}
\]

The projections are mutually orthogonal and sum to the identity.
Cyclic coordinate rotation conjugates the \(Q_j\)'s and commutes with
\({\cal U}\).

The normalized one-step quotient is \(\phi\), and

\[
  \tau=\phi^2.                                    \tag{1.5}
\]

Consequently, forgetting the spatial coordinate sends
\({\cal U}^{2u}\) to \(\tau^u\).

Let \(\Lambda_H\) be the diagonal projection onto labelled lifts of
normalized roots whose \(\tau\)-cycle has length greater than \(H+1\).
Since \(\phi\) commutes with \(\tau\), this is an invariant projection:

\[
  \Lambda_H{\cal U}={\cal U}\Lambda_H.           \tag{1.6}
\]

## 2. The exact killed first-return operator

Fix \(j\) and put

\[
  K_j=(I-Q_j){\cal U}.                            \tag{2.1}
\]

For \(g\ge1\), define

\[
  {\cal R}_{j,g}=Q_j{\cal U}K_j^{g-1}Q_j.        \tag{2.2}
\]

### Theorem 2.1 (first-return partial permutations)

For a state \(x\) with \(q(x)=j\), the vector
\({\cal R}_{j,g}e_x\) is nonzero if and only if

\[
  q(f^t x)\ne j\quad(1\le t<g),
  \qquad q(f^g x)=j.                              \tag{2.3}
\]

In that case

\[
  {\cal R}_{j,g}e_x=e_{f^gx}.                    \tag{2.4}
\]

The operators

\[
  {\cal R}_{j,g}^{*}{\cal R}_{j,g}
\]

are mutually orthogonal diagonal projections as \((j,g)\) vary.

#### Proof

Reading (2.2) from right to left, the initial \(Q_j\) imposes
\(q(x)=j\).  Every factor \(K_j\) performs one update and kills the vector
if the new state lies in \(Q_j\).  Thus its \(g-1\) powers impose all the
proper-prefix exclusions in (2.3).  The final \({\cal U}\) makes update
\(g\), and the left \(Q_j\) imposes the endpoint equality.  This proves
(2.3)--(2.4).

The map \(f^g\) is injective, so every nonzero \({\cal R}_{j,g}\) is a
partial permutation.  Every state has one current value \(j=q(x)\) and
one next return time.  Therefore the domains for distinct \((j,g)\) are
disjoint, proving orthogonality. \(\square\)

Define

\[
  \Pi_H=\sum_j\sum_{g=1}^{G}
       {\cal R}_{j,g}^{*}{\cal R}_{j,g}.          \tag{2.5}
\]

Same-coordinate return gaps below the circumference are odd.  If
\(g=2s+1\), the corresponding positive residence is \(s+1\).  Hence

\[
  s+1\le H\quad\Longleftrightarrow\quad
  g\le2H-1=G.                                    \tag{2.6}
\]

Thus \(\Pi_H\) is exactly the active-start indicator before short-cycle
deletion.  Put

\[
  {\cal E}_H=\Lambda_H\Pi_H.                     \tag{2.7}
\]

### Theorem 2.2 (all-winding two-point trace)

The exact identities (0.1) hold.

#### Proof

Every normalized root has exactly \(N\) spatial lifts.  Eligibility and
long quotient period depend only on the normalized root.  Therefore

\[
  \operatorname {Tr}{\cal E}_H=NR_H.             \tag{2.8}
\]

For a diagonal projection \(E\) and a permutation \(U\),

\[
 \operatorname {Tr}(EU^{-t}EU^t)
 =\sum_x E(x)E(U^tx).                             \tag{2.9}
\]

Take \(E={\cal E}_H\), \(U={\cal U}\), and \(t=2u\).  Forgetting the
spatial lift turns the second phase into \(\tau^uD\), and every quotient
pair again has exactly \(N\) lifts.  Sum over \(1\le u\le H+1\). \(\square\)

## 3. Exact Laurent marking of positive winding

For \(x\in\Omega_N\), let \(D(x)\) be its normalized Dyck root and put

\[
  \Delta(x)=\delta(D(x)).                        \tag{3.1}
\]

The one-step skew product says

\[
  q(fx)\equiv q(x)+\Delta(x)\pmod N.             \tag{3.2}
\]

Introduce the monomial permutation matrix

\[
  {\cal U}(z)e_x=z^{\Delta(x)}e_{f(x)}.          \tag{3.3}
\]

Put

\[
 K_j(z)=(I-Q_j){\cal U}(z),
 \qquad
 {\cal R}_{j,g}(z)=Q_j{\cal U}(z)K_j(z)^{g-1}Q_j.
                                                               \tag{3.4}
\]

Every nonzero entry of \({\cal R}_{j,g}(z)\) is one monomial whose
exponent is the lifted total one-step displacement along that first-return
path.

### Theorem 3.1 (duration--winding coefficient)

Suppose \(g=2s+1<N\).  If the path has two-step winding \(w\ge0\), then
its exponent in (3.4) is exactly

\[
                         (s-w)N.                 \tag{3.5}
\]

#### Proof

Write \(D_j=\tau^jD_0\).  The exact two-step block identity gives

\[
 \delta(D_j)+\delta(\phi D_j)=N-d(D_j).          \tag{3.6}
\]

The last, odd update contributes \(\delta(D_s)\).  Thus the total marked
exponent is

\[
 \begin{aligned}
 \sum_{t=0}^{2s}\Delta(f^tx)
 &=\sum_{j=0}^{s-1}(N-d(D_j))+\delta(D_s)\\
 &=sN-\left(\sum_{j=0}^{s-1}d(D_j)-\delta(D_s)\right).
 \end{aligned}                                   \tag{3.7}
\]

The exact return ledger is

\[
  \sum_{j=0}^{s-1}d(D_j)=\delta(D_s)+wN.         \tag{3.8}
\]

Substitution proves (3.5). \(\square\)

Define the coefficient partial permutation

\[
 {\cal R}_{j,2s+1}^{(w)}
 =[z^{(s-w)N}]{\cal R}_{j,2s+1}(z),              \tag{3.9}
\]

and put

\[
 \Pi_{H,w}=
 \sum_j\sum_{0\le s\le H-1}
  ({\cal R}_{j,2s+1}^{(w)})^*
   {\cal R}_{j,2s+1}^{(w)},
 \qquad
 {\cal E}_{H,w}=\Lambda_H\Pi_{H,w}.             \tag{3.10}
\]

Invalid indices, including \(w>s-1\), contribute zero.  First-return
uniqueness gives the orthogonal decomposition

\[
 {\cal E}_H=\sum_{w\ge0}{\cal E}_{H,w}.          \tag{3.11}
\]

Applying (2.9) to each ordered pair of summands proves (0.3).  Thus
zero--positive, positive--zero, and positive--positive correlations are
all exact coefficient traces of one operator.

## 4. The selected-predecessor transfer after peak deletion

Now fix a reduced rank \(d\ge1\), put

\[
  p=2d+1.
\]

The labels in this section are persistent equality-particle identities,
not the original parent physical coordinates.  Formally, augment a
normalized reduced root \(F\) by a cyclic labelling

\[
 \ell:\{\text{its }p\text{ reduced sites}\}\longrightarrow\mathbb Z_p
                                                               \tag{4.0}
\]

preserving cyclic order.  The equality-particle theorem preserves these
labels and says that the recorded word evolves by the canonical PBBS map.
Therefore the augmented states \((F,\ell)\) are canonically conjugate to
the ordinary labelled state space

\[
 \Omega_p=\binom{[p]}d.                           \tag{4.0a}
\]

the site labels of this ordinary state are precisely the persistent
particle identities.  Under this conjugacy, its unique unmatched
coordinate is the identity of the currently selected equality particle.
Write \({\cal U}_d\) for the induced one-step permutation, and let \(Q_j\)
project onto augmented states whose selected persistent particle is \(j\).

If the current particle is \(j\), its immediate cyclic predecessor is
\(j-1\).  Put

\[
  K_{j-1}=(I-Q_{j-1}){\cal U}_d.                 \tag{4.1}
\]

For \(a,b\ge1\), define \({\cal B}_{j;a,b}\) by (0.4).

### Theorem 4.1 (second-predecessor-hit projection)

The operator

\[
  {\cal B}_{j;a,b}^{*}{\cal B}_{j;a,b}           \tag{4.2}
\]

projects onto states for which the first positive selection of particle
\(j-1\) is at time \(a\), and its next selection is at time \(a+b\).
Consequently \({\cal A}_G\) in (0.5) is a diagonal projection and

\[
  {\cal A}_G(x)=1
  \quad\Longleftrightarrow\quad
  B_2(D(x))\le G.                                \tag{4.3}
\]

#### Proof

The right segment

\[
 Q_{j-1}{\cal U}_dK_{j-1}^{a-1}Q_j
\]

is the first-hit operator from \(Q_j\) to \(Q_{j-1}\).  Starting at that
hit, the left segment is the first-return operator to \(Q_{j-1}\) after
\(b\) further updates.  Thus (4.2) has the asserted domain.  The two hit
times are unique, so these domains are disjoint as \((j,a,b)\) vary.
Summing over \(a+b\le G\) proves (4.3).  The no-overtaking theorem ensures
that the original particle has vacated before the second predecessor hit;
no extra leader condition is missing. \(\square\)

For an outer rank \(r\), assign to a normalized reduced root \(F\) of
rank \(d\), with \(k\) peaks, the inverse-fibre weight

\[
  P_r(F)=\binom{r+d-k}{2d},                       \tag{4.4}
\]

declared zero when \(d+k>r\).  Lift this to a diagonal operator
\({\cal W}_{r,d}\) on \(\Omega_p\).  The weight commutes with
\({\cal U}_d\): the cyclic number of \(10\)-transitions, hence the peak
count of the normalized root, is invariant under the complemented
rotation.

### Corollary 4.2 (exact reduced traces)

The weighted reduced quantities in the predecessor-transmission theorem
are

\[
 \boxed{
 S_{r,H}=\sum_{d=1}^{r-1}{1\over2d+1}
       \operatorname {Tr}({\cal W}_{r,d}{\cal A}_{G}),}
                                                               \tag{4.5}
\]

\[
 \boxed{
 K_{r,H}=\sum_{d=1}^{r-1}{1\over2d+1}
  \sum_{u=1}^{H+1}
  \operatorname {Tr}
  ({\cal W}_{r,d}{\cal A}_{G}{\cal U}_d^{-2u}
   {\cal A}_{G}{\cal U}_d^{2u}).}               \tag{4.6}
\]

#### Proof

Every normalized reduced root has exactly \(2d+1\) cyclic persistent-label
augmentations in (4.0), one for each identity assigned to its current
selected particle.  Global cyclic relabelling conjugates these
augmentations, and both the predicate (4.3) and weight (4.4) are invariant
under it.  Divide the augmented trace by \(2d+1\).  A quotient lag \(u\)
is \(2u\) one-step updates.  Summing over ranks proves
(4.5)--(4.6). \(\square\)

Together with the audited outer Pascal constants, (4.5)--(4.6) imply, at
critical saddle mass,

\[
 {\mathcal C_H\over R_H}\asymp {K_{r,H}\over S_{r,H}}.       \tag{4.7}
\]

Thus the transfer operator (0.5) is exactly the remaining reduced object.

## 5. Nilpotent Jordan chains are the genuine renewal gaps

Fix one orbit

\[
  \mathcal O=(x_0,x_1,\ldots,x_{L-1})
\]

of \({\cal U}_d\), with indices read modulo \(L\).  Coordinate homomesy
implies that every particle label occurs equally often as the selected
coordinate.  In particular, for every \(b\in\mathbb Z_p\), list the
visits to \(Q_b\) as

\[
  0\le t_{b,1}<t_{b,2}<\cdots<t_{b,m_b}<L        \tag{5.1}
\]

cyclically, and put

\[
  g_{b,i}=t_{b,i+1}-t_{b,i}>0.                  \tag{5.2}
\]

The final difference is read modulo \(L\), so

\[
  \sum_i g_{b,i}=L.                              \tag{5.3}
\]

### Theorem 5.1 (Jordan--renewal normal form)

On \(\mathbb C^{\mathcal O}\),

\[
 \boxed{
 K_b=(I-Q_b){\cal U}_d
 \simeq\bigoplus_{i=1}^{m_b}J_{g_{b,i}},}        \tag{5.4}
\]

where \(J_g\) is the nilpotent forward shift on a chain of \(g\) basis
vectors.  Hence \(K_b\) is nilpotent and all its eigenvalues are zero.

#### Proof

Partition the cyclic orbit into the half-open blocks

\[
  [t_{b,i},t_{b,i+1})                             \tag{5.5}
\]

of lengths \(g_{b,i}\).  Within one block, \(K_b\) advances the state by
one orbit step.  At the last state of the block, the next update lands in
\(Q_b\), and the left factor \(I-Q_b\) kills it.  Thus the restriction to
the block is exactly one nilpotent chain \(J_{g_{b,i}}\).  The blocks are
disjoint and exhaust the orbit. \(\square\)

This theorem identifies what a standard spectral-radius argument misses.
The eigenvalue multiset of every killed operator is identically zero.
Even its Jordan block sizes retain only the one-coordinate gap histogram

\[
  \{g_{b,i}:i\}.                                  \tag{5.6}
\]

The predecessor event also needs the placement of successor-particle
visits inside those blocks.

## 6. Exact predecessor renewal-block formula

Continue on one orbit.  Put \(a=b+1\).  A time \(s\) with
\(\kappa_s=a\) lies in a unique open block

\[
  t_{b,i-1}<s<t_{b,i}.                            \tag{6.1}
\]

Its first future \(b\)-selection is \(t_{b,i}\), and the next one is
\(t_{b,i+1}\).  Therefore its second predecessor hit occurs after

\[
  t_{b,i+1}-s=(t_{b,i}-s)+g_{b,i}                \tag{6.2}
\]

steps.

### Theorem 6.1 (two-block renewal identity)

For fixed \(b\), the number of predecessor-active phases whose current
particle is \(b+1\) is exactly (0.8).

#### Proof

Equation (6.2) says that the second future \(b\)-selection lies within
the horizon precisely when the displayed sum is at most \(G\).  Every
current-\(b+1\) phase lies in exactly one block (6.1), so summation neither
misses nor repeats a phase. \(\square\)

Equivalently, define the marked renewal block

\[
 \beta_{b,i}=
 \left(g_{b,i},
  (\kappa_{t_{b,i-1}+1},\ldots,
   \kappa_{t_{b,i}-1})\right).                   \tag{6.3}
\]

The contribution at index \(i\) is the number of \(b+1\)'s in the final

\[
  (G-g_{b,i})_+                                  \tag{6.4}
\]

positions of the word component of \(\beta_{b,i}\).  Thus it is a
nearest-neighbour functional of the preceding word block and the next
gap.  This is an exact renewal transfer, not an independence assertion.

For the weighted union of all reduced orbits, let \(A(s)\) be this active
indicator.  Equations (4.5)--(4.6) give

\[
 {K_{r,H}\over S_{r,H}}
 =
 {\displaystyle
   \sum_{d,\mathcal O}{w(\mathcal O)\over2d+1}
    \sum_{s\in\mathcal O}A(s)
       \sum_{u=1}^{H+1}A(s+2u)
  \over
  \displaystyle
   \sum_{d,\mathcal O}{w(\mathcal O)\over2d+1}
    \sum_{s\in\mathcal O}A(s)},                \tag{6.5}
\]

where \(w(\mathcal O)=P_r(F)\) is constant on each orbit.  This is (0.9).

The formula shows two distinct memories.

1. To decide whether one phase is active, one must retain a residual
   time inside one \(b\)-block and the length of the next \(b\)-gap.
2. To evaluate \(A(s)A(s+2u)\), the current label generally changes, so
   one must retain the relative alignment of the renewal decompositions
   for different \(b\)'s.

The Jordan multiset (5.6) contains neither datum 2 nor the successor
placement needed for datum 1.

## 7. The unitary spectral criterion

The same obstruction can be stated as an exact spectral condition.  Work
on the invariant long-cycle subspace of the full labelled rank-\(r\)
process, with normalized counting inner product.  Put

\[
  \rho_H={R_H\over |L_H|},
  \qquad
  e={\cal E}_H,
  \qquad
  f=e-\rho_H I,                                  \tag{7.1}
\]

where \(|L_H|\) is the number of retained normalized roots, and diagonal
projections are identified with their indicator vectors.  Let
\(\sigma_H\) be the spectral measure of \(f\) for the unitary
\({\cal U}\).  Then

\[
 \boxed{
 {\mathcal C_H\over R_H}
 =(H+1)\rho_H+
 {1\over\rho_H}
  \int_{-\pi}^{\pi}
   \left(\sum_{u=1}^{H+1}\cos(2u\theta)\right)
   d\sigma_H(\theta).}                           \tag{7.2}
\]

#### Proof

For every \(u\),

\[
 {1\over N|L_H|}
 \operatorname {Tr}
 ({\cal E}_H{\cal U}^{-2u}{\cal E}_H{\cal U}^{2u})
 =\rho_H^2+\langle f,{\cal U}^{2u}f\rangle.      \tag{7.3}
\]

Sum, divide by
\(R_H/|L_H|=\rho_H\), and apply the spectral theorem.  The correlation is
real, so only the cosine part remains. \(\square\)

At the critical density \(\rho_H\asymp1/H\), the first term in (7.2) is
bounded.  Bounded susceptibility means that the integrated centered
Dirichlet mass is \(O(\rho_H)\); divergence requires a growing coherent
contribution.  The Fejér-window argument supplies only a constant-order
lower bound at this density.  Thus (7.2) is equivalent to, not a solution
of, the missing long-period correlation theorem.

There is no contradiction between (7.2) and Theorem 5.1.  The unitary
operator \({\cal U}\) carries the orbit phases and has roots of unity as
eigenvalues.  The killed operator \(K_j\), which enforces firstness, is
nilpotent.  Renewal asymptotics depend on how the active projection sits
inside the unitary orbit eigenspaces, or equivalently on the block
alignment in (6.5).

## 8. Exact mountain renewal and why it does not globalize automatically

The report
`MATH_THEOREM_N_ST_ZERO_WINDING_MOUNTAIN_RENEWAL_SUSCEPTIBILITY_20260726.md`
computes one complete genuine fibre.  Let

\[
 p=2h-1\text{ be prime},\qquad
 y=r-h,
\]

and

\[
 \Omega_{r,h}=\{(n_0,\ldots,n_{p-1})\ge0:
                         \sum_jn_j=y\}.          \tag{8.1}
\]

The literal PBBS transport is cyclic coordinate rotation, and a phase is
active exactly when its current coordinate is zero.  Hence

\[
 |\Omega_{r,h}|=\binom{y+p-1}{p-1},
 \qquad
 R^{\rm mt}_{r,h}=\binom{y+p-2}{p-2},            \tag{8.2}
\]

\[
 \mathcal C^{\rm mt}_{r,h;H}
 =(H+1)\binom{y+p-3}{p-3}.                       \tag{8.3}
\]

Thus

\[
 {R^{\rm mt}_{r,h}\over|\Omega_{r,h}|}
 ={p-1\over y+p-1},
 \qquad
 {\mathcal C^{\rm mt}_{r,h;H}\over R^{\rm mt}_{r,h}}
 =(H+1){p-2\over y+p-2}.                         \tag{8.4}
\]

If \(h/\sqrt r\to c\) and \(A/2<c<A\), these converge as in (0.10).
Conditioning on one active phase, the factorial moments of the number of
future active phases are

\[
 (H+1)_q{(p-2)_q\over(y+p-2)_q}\longrightarrow(2Ac)^q,       \tag{8.5}
\]

which proves the Poisson limit.

The same exact formula explains the dense one-defect mountain rotor.  If
\(y=O(p)\) while \(H\asymp p\), the second ratio in (8.4) is of order
\(H\), not constant.  Thus one literal PBBS renewal family already
contains both susceptibility regimes:

\[
 \begin{array}{c|c}
 y\asymp r,\ p\asymp\sqrt r&\mathcal C/R=\Theta(1),\\
 y=O(p),\ H\asymp p&\mathcal C/R=\Theta(H).
 \end{array}                                      \tag{8.6}
\]

The global Pascal saddle has \(d\asymp r\), long reduced period, and
non-rotational block transport.  Nothing in (8.2)--(8.5) transfers its
Poisson law to that regime.  Conversely, the mountain example proves that
firstness, zero winding, a critical \(1/H\) active density, and retained
cycles do not force divergent susceptibility.

## 9. Minimal growing state and final boundary

There is a simple automata-theoretic reason that a fixed transfer state
cannot encode (0.5).  After the first predecessor hit, deciding whether a
second hit occurs before a deadline \(G\) requires distinguishing the
residual waiting times

\[
  0,1,\ldots,G-1.                                \tag{9.1}
\]

For the unrestricted hit language these states are pairwise
Myhill--Nerode inequivalent: appending a target hit after exactly \(t\)
further symbols accepts one residual state and rejects a state with a
smaller remaining deadline.  Thus every exact stream automaton has at
least \(G\) states even before recording the current particle label or
the simultaneous renewal alignments.  A smaller PBBS-specific state
space would itself require a new chronology theorem identifying these
continuations; it cannot be assumed from one-point marginals.

The following are proved here.

1. The direct all-winding first-return projection (2.5).
2. The exact quotient traces (0.1).
3. The duration--winding coefficient rule (3.5) and the resolved traces
   (0.3).
4. The selected-predecessor two-hit projection (0.5).
5. The exact weighted reduced traces (4.5)--(4.6).
6. The nilpotent Jordan decomposition (5.4).
7. The two-block renewal identity (0.8).
8. The Palm formula (6.5) and unitary spectral identity (7.2).
9. The independently audited mountain Poisson calibration.

The following are not proved.

1. \(R_H=\Theta_A(B_r/H)\) for the full genuine process.
2. Boundedness or divergence of \(\mathcal C_H/R_H\) at that scale.
3. A limiting transition kernel for the long-period Pascal-saddle renewal
   blocks (6.3).
4. A spectral estimate for the active projection inside the unitary PBBS
   orbit decomposition.

Therefore this note neither proves nor refutes \((ST_A)\).  It closes a
class of proposed shortcuts: no local predecessor law, killed-operator
eigenvalue, single-coordinate renewal histogram, or fixed-state transfer
can decide the ratio.  The exact next theorem must control the joint
long-period renewal-block alignment in (6.5), with its Pascal weights and
the winding coefficients in (3.9) retained.
