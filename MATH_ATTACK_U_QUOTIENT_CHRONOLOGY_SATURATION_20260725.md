# Lane U: actual PBBS fibre saturation and the residual long-period quotient gate

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
\]

where \(A>0\) is fixed.  The corrected weakest quotient gate is

\[
 \boxed{\overline\nu_H=o_A(B_r/\sqrt r).}          \tag{QST_A}
\]

Here \(\overline\nu_H\) is taken only over quotient \(\tau\)-cycles of
length greater than \(H+1\).

This report does **not** prove or disprove \((QST_A)\).  It settles the
local chronology question and sharply reduces the global one.

1. Genuine PBBS first-return chronology can asymptotically saturate the
   reciprocal-height edge budget inside one actual Gaussian-height inverse
   fibre.  For every \(A>0\), every fixed

   \[
      \frac A2<c<A,
   \]

   and infinitely many ranks, there is an actual height-\(h\) fibre of
   size \(P_{r,h}\), lying on quotient cycles longer than \(H+1\), with an
   edge-disjoint family of literal first-return intervals of size

   \[
   \boxed{
   \left(\frac{1-e^{-4c^2}}{2c}+o(1)\right)
       \frac{P_{r,h}}{\sqrt r}.}                   \tag{0.1}
   \]

   Since its reciprocal-height capacity is
   \(P_{r,h}/(h+2)\), the ratio tends

   \[
      \boxed{\frac{1-e^{-4c^2}}2>0.}              \tag{0.2}
   \]

   This uses the exact peak-deletion predecessor-passage criterion, not a
   static sector relaxation.

2. The saturating fibre is globally negligible.  More generally, if the
   first-pruned core has quotient period at most \(L\), the total exact
   Pascal capacity of all its outer lifts is at most

   \[
      3^r\,r(2L+2)(2r+1)^{2L+2}.                  \tag{0.3}
   \]

   Hence it is \(o(B_r/r^K)\) for every fixed \(K\) whenever
   \(L\log r=o(r)\).

3. Consequently every local, orbitwise, or fibrewise assertion of the form

   \[
   \operatorname{pack}(E)
      \le o(1)\frac{P_r(E)}{\operatorname{ht}(E)+1}
   \]

   is false even for literal PBBS first returns.  But all presently known
   local saturators can be deleted at exponentially negligible global cost.
   The unresolved part of \((QST_A)\) is a genuinely aggregate theorem for
   linear-defect, long-period reduced cores.

No \(d=1\) converse is used anywhere below.

## 1. The mountain core and its exact predecessor passage

Fix integers \(r>h\ge4\), and put

\[
 d=h-1,\qquad p=2d+1=2h-1,
 \qquad E_h=1^{h-1}0^{h-1}.                       \tag{1.1}
\]

The first maximum of \(E_h\) is reached at its \((h-1)\)-st step.  The
normalized one-step PBBS formula therefore gives

\[
 \phi E_h=E_h,\qquad \delta(E_h)=h-1.             \tag{1.2}
\]

Label the persistent omitted-particle coordinates of the rank-\(d\) PBBS
by \(\mathbb Z_p\), with the time-zero coordinate labelled zero.  Since
each ordinary PBBS step advances the distinguished coordinate by \(d=h-1\),

\[
 \kappa_t=t(h-1)\pmod p.                           \tag{1.3}
\]

Because \(2(h-1)=p-1\), this is equivalently

\[
 \boxed{
 \kappa_{2t}=-t,\qquad
 \kappa_{2t+1}=h-1-t\pmod p.}                     \tag{1.4}
\]

Set

\[
 g=p+2=2h+1.                                      \tag{1.5}
\]

Equation (1.4) gives the three exact chronology facts

\[
 \kappa_g=-1,\qquad
 \min\{t>0:\kappa_t=0\}=p=g-2,                  \tag{1.6}
\]

and the only occurrence of the predecessor \(-1\) strictly before time
\(g\) is at time two.  Thus

\[
 n_{-1}(g)=1,
 \qquad z_*(g)=\frac{n_{-1}(g)-1}{2}=0.           \tag{1.7}
\]

This is the exact peak-deletion passage criterion: the distinguished
particle is reselected first at time \(g-2\), and its immediate predecessor
makes the terminal entry at time \(g\), after one prior selection.

## 2. The full inverse fibre and the exact \(\tau\)-transport

The core \(E_h\) has rank \(d=h-1\) and one peak.  Its rank-\(r\) inverse
peak-deletion fibre is the weak-composition simplex

\[
 \Omega_{r,h}=
 \left\{(n_0,\ldots,n_{p-1})\in\mathbb Z_{\ge0}^p:
       \sum_{j=0}^{p-1}n_j=y\right\},
 \qquad y=r-h.                                    \tag{2.1}
\]

Hence

\[
 \boxed{
 P_{r,h}:=|\Omega_{r,h}|
 =\binom{y+p-1}{p-1}
 =\binom{r+h-2}{2h-2}.}                           \tag{2.2}
\]

Let \(w=0E_h\) be the reduced particle word, and put

\[
 \epsilon_j=\mathbf1_{\{w_{j-1}\ne w_j\}}.
\]

The physical gap from particle \(j-1\) to particle \(j\) is

\[
 q_j=1+\epsilon_j+2n_j.                           \tag{2.3}
\]

Only \(\epsilon_1\) and \(\epsilon_h\) are nonzero.  During one
\(\tau=\phi^2\) step the two selected particles are \(0\) and \(h-1\).
If \(C_j\) is their two-step selection count, then direct inspection of
these two boundary indices gives

\[
 C_{j-1}-C_{j-2}=\epsilon_j-\epsilon_{j-1}.        \tag{2.4}
\]

After the two steps, the normalized distinguished particle has advanced by

\[
 2(h-1)=-1\pmod p.
\]

Therefore the newly normalized gap is

\[
\begin{aligned}
 q'_j
 &=q_{j-1}+C_{j-1}-C_{j-2}\\
 &=1+\epsilon_j+2n_{j-1}.
\end{aligned}                                      \tag{2.5}
\]

Comparing with (2.3) proves the exact fibre transport

\[
 \boxed{n'_j=n_{j-1}\qquad(j\in\mathbb Z_p).}     \tag{2.6}
\]

Thus \(\tau\) acts on this entire inverse fibre by one cyclic rotation of
the weak-composition coordinates.

### Theorem 2.1 (literal first-return criterion in the fibre)

An inverse lift \(D\in\Omega_{r,h}\), at its current normalized phase,
has a genuine first physical omitted-label return of gap \(2h+1\) if and
only if

\[
 \boxed{n_0=0.}                                    \tag{2.7}
\]

Every such lift has Dyck height exactly \(h\).  Its positive residence is
\(h+1\), and its quotient trace contains exactly \(h+2\) transition
edges.

#### Proof

Equations (1.6)--(1.7) give a reduced predecessor passage with required
terminal slot zero.  The exact inverse passage theorem therefore gives the
outer return precisely when the terminal free slot is zero, which is
(2.7).  Before time \(g-2\), the distinguished particle still occupies the
returned physical edge.  After it vacates that edge, particle order permits
only its immediate predecessor to enter; (1.6)--(1.7) show that this occurs
at time \(g\).  Hence the return is first, not merely an endpoint
congruence.

Simultaneous deletion of all Dyck peaks lowers the height of every nonempty
Dyck word by exactly one.  Since \(\operatorname{ht}(E_h)=h-1\), every
inverse lift has height \(h\).  The residence and trace-edge counts follow
from \(g=2h+1\). \(\square\)

## 3. Actual local saturation of the height-stratum budget

Assume now that \(p=2h-1\) is prime.  Since \(y=r-h>0\), every composition
in \(\Omega_{r,h}\) which has a zero coordinate is nonconstant.  A
nonconstant composition has full rotation period \(p\), because \(p\) is
prime.  By (2.6), it therefore lies on an actual quotient \(\tau\)-cycle of
length \(p\).

Let

\[
 U_{r,h}=\#\{\mathbf n\in\Omega_{r,h}:
                   n_j=0\text{ for some }j\}.     \tag{3.1}
\]

Every one of the \(U_{r,h}/p\) rotation orbits contains at least one phase
with current seam coordinate zero.  Choose one such phase on each orbit.
The resulting literal first-return intervals lie on different quotient
cycles and hence are pairwise quotient-edge-disjoint.  Since

\[
 h+2<2h-1=p\qquad(h\ge4),                         \tag{3.2}
\]

they are nonwrapping.  Consequently

\[
 \boxed{\operatorname{pack}(\Omega_{r,h})
          \ge U_{r,h}/p.}                          \tag{3.3}
\]

The complement of (3.1) consists of the positive compositions of \(y\)
into \(p\) parts.  Thus, with the convention that the second binomial is
zero when \(y<p\),

\[
 U_{r,h}
 =\binom{y+p-1}{p-1}-\binom{y-1}{p-1}.            \tag{3.4}
\]

When \(y\ge p\), division by (2.2) gives the exact ratio

\[
 \frac{U_{r,h}}{P_{r,h}}
 =1-\prod_{i=1}^{p-1}\frac{y-i}{y+i}.             \tag{3.5}
\]

Suppose

\[
 \frac h{\sqrt r}\longrightarrow c>0.
\]

Here \(p=2h+O(1)\) and \(y=r+O(\sqrt r)\).  Uniform Taylor expansion in
\(i/y=O(r^{-1/2})\) gives

\[
 \sum_{i=1}^{p-1}
 \log\frac{y-i}{y+i}
 =-\frac{2}{y}\sum_{i=1}^{p-1}i+o(1)
 =-4c^2+o(1).                                     \tag{3.6}
\]

Therefore

\[
 \boxed{
 \frac{U_{r,h}}{P_{r,h}}
 \longrightarrow1-e^{-4c^2}.}                    \tag{3.7}
\]

Combining (3.3), (3.7), and \(p/\sqrt r\to2c\) proves

\[
 \boxed{
 \operatorname{pack}(\Omega_{r,h})
 \ge
 \left(\frac{1-e^{-4c^2}}{2c}+o(1)\right)
 \frac{P_{r,h}}{\sqrt r}.}                        \tag{3.8}
\]

The height-stratum trace bound on this fibre is

\[
 \operatorname{pack}(\Omega_{r,h})
 \le\frac{P_{r,h}}{h+2}.
\]

Thus (3.8) occupies the limiting fraction

\[
 \boxed{\frac{1-e^{-4c^2}}2}                      \tag{3.9}
\]

of the exact reciprocal-height capacity.

### Corollary 3.2 (the cycles occur in the corrected long-cycle deck)

Fix \(A>0\) and choose

\[
 \frac A2<c<A.                                    \tag{3.10}
\]

Take any sequence of odd primes \(p\to\infty\), put

\[
 h=\frac{p+1}{2},\qquad
 r=\left\lceil\frac{h^2}{c^2}\right\rceil.
\]

Then

\[
 \frac Hh\longrightarrow\frac Ac.
\]

The inequality \(c<A\) gives \(h+1\le H\) eventually, so all intervals
are eligible.  The inequality \(c>A/2\) gives

\[
 p=2h-1>H+1
\]

eventually, so these are cycles retained in the definition of
\(\overline\nu_H\), not members of the discarded short-cycle deck.  Hence
(0.1)--(0.2) hold on genuine corrected-deck examples for every fixed
\(A\).

## 4. Why this does not refute \((QST_A)\)

The fibre dimension is only \(p-1=O(\sqrt r)\).  From (2.2),

\[
 \log P_{r,h}=O(\sqrt r\log r)=o(r).               \tag{4.1}
\]

Since

\[
 B_r=\exp(r\log4-O(\log r)),
\]

one has, for every fixed \(K\),

\[
 \boxed{P_{r,h}=o(B_r/r^K).}                       \tag{4.2}
\]

Thus Theorem 2.1 and (3.8) refute a uniform local contraction, not the
global Catalan-weighted packing statement.

## 5. All short reduced-core cycles have negligible lifted capacity

The preceding example has a fixed reduced core.  The next theorem removes
all such low-period mechanisms at once.

Fix a nonempty first-pruned core \(E\in\mathcal D_d\), write

\[
 k=\operatorname{pk}(E),\qquad y=r-d-k\ge0.
\]

Its complete outer inverse-fibre capacity is

\[
 P_r(E)=\binom{y+2d}{2d}.                          \tag{5.1}
\]

Using nonnegative coefficient extraction at \(t=1/3\),

\[
\begin{aligned}
 P_r(E)
 &=[t^y](1-t)^{-(2d+1)}\\
 &\le3^y(3/2)^{2d+1}\\
 &=3^r\left(\frac32\right)
       \left(\frac34\right)^d3^{-k}
 \le3^r.                                          \tag{5.2}
\end{aligned}
\]

The normalized voltage-itinerary bound says that the number of rank-\(d\)
Dyck roots on quotient \(\tau\)-cycles of period at most \(L\) is at most

\[
 (2L+2)(2d+1)^{2L+2}.                              \tag{5.3}
\]

Indeed a \(\tau\)-period at most \(L\) gives a \(\phi\)-period at most
\(2L\), and a normalized orbit is determined by its bounded voltage word.

### Theorem 5.1 (short-core-period deletion)

Let \(\mathcal C_{r,L}\) be the set of outer rank-\(r\) roots whose
nonempty first-pruned core lies on a quotient \(\tau\)-cycle of period at
most \(L\).  Then

\[
 \boxed{
 |\mathcal C_{r,L}|
 \le 3^r r(2L+2)(2r+1)^{2L+2}.}                   \tag{5.4}
\]

If \(L\log r=o(r)\), then for every fixed \(K\),

\[
 \boxed{|\mathcal C_{r,L}|=o(B_r/r^K).}            \tag{5.5}
\]

#### Proof

For each core counted by (5.3), bound its exact fibre by (5.2), then sum
over \(1\le d<r\).  This proves (5.4).  Under \(L\log r=o(r)\), its
right-hand side is

\[
 \exp(r\log3+o(r)),
\]

whereas \(B_r/r^K=\exp(r\log4-o(r))\).  This proves
(5.5). \(\square\)

For the Gaussian horizon one may take

\[
 L=H\,\omega(r),\qquad
 \omega(r)\to\infty,qquad
 \omega(r)\log r=o(\sqrt r).                     \tag{5.6}
\]

Thus every globally threatening first-pruned core may be assumed to have

\[
 \frac{\operatorname{per}_\tau(E)}H\longrightarrow\infty.    \tag{5.7}
\]

The mountain saturator and the defect-one affine passage cycles are both
removed by Theorem 5.1.

## 6. Exact residual global gate

Combine Theorem 5.1 with the already proved Narayana--Pascal saddle tails,
the small-core-defect entropy bound, and the exact terminal-slot tail.  At
cost \(o(B_r/\sqrt r)\), every putative counterfamily to \((QST_A)\) may
be restricted to first-pruned cores satisfying

\[
 \boxed{
 \begin{gathered}
 d=\frac r2+O(\sqrt{r\log r}),\\
 k=\frac r6+O(\sqrt{r\log r}),\\
 d-k\ge c_0r,\qquad z\le3\log r,\\
 \operatorname{per}_\tau(E)/H\longrightarrow\infty,
 \end{gathered}}                                   \tag{6.1}
\]

for some absolute \(c_0>0\).  Every surviving start must obey the literal
predecessor-passage equations

\[
 \boxed{
 \kappa_g=-1,\qquad
 h_E<g\le2H-1,\qquad
 n_{-1}(g)=2z+1.}                                  \tag{6.2}
\]

This is a two-dimensional Gaussian Pascal saddle with linear core defect,
logarithmic predecessor multiplicity, and reduced period much larger than
the return horizon.

There is no remaining local contraction to invoke.  The theorem still
needed is an aggregate statement saying that the phase-specific passage
hyperplanes in (6.2) cannot occupy and pack a positive fraction of the
height-stratum edge budget on these long, high-defect PBBS cycles.

## 7. Saturation certificate and implication scope

The reciprocal-height trace gives

\[
 \overline\nu_H
 \le\sum_{h<H}\frac{b_{r,h}}{h+2}
 =O_A(B_r/\sqrt r).                                \tag{7.1}
\]

If its little-oh strengthening fails, the exact height spectral tails
remove \(h=o(\sqrt r)\).  Hence some Gaussian height band carries positive
normalized packing mass.  Splitting by winding gives the following
literal alternatives.

1. In the zero-winding branch, some
   \(s\in[a\sqrt r,A\sqrt r]\) carries a positive fraction of its exact
   central three-strip capacity

   \[
   [x^{2r}]H_{s,\lfloor s/2\rfloor}
     =\Theta_{a,A}(B_r/r)
     =\Theta_{a,A}(b_{r,s}/s).
   \]

   After the deletions in Section 6, every retained root satisfies the
   actual equations (6.2).

2. In the positive-winding branch, the exact two-parity deficit budget
   first removes \(w\ge K\), then fixes one integer \(1\le w<K\) carrying
   \(\Omega(B_r/\sqrt r)\) intervals.  Such a family consumes a positive
   fraction of both global deficit moments and has chronological overlap-
   staircase cells of total size \(\Omega(B_r)\).

Neither alternative is contradicted by a proved PBBS theorem.  The local
mountain construction proves that the absence of such a contradiction is
not merely an artefact of static relaxation: literal first-return dynamics
really can attain the critical capacity on individual fibres.

## 8. Independent audit of the decisive step

The local saturation theorem was checked independently as follows.

1. **Itinerary.**  Multiplication by \(h-1\) modulo \(2h-1\) gives
   (1.4); the first later zero is at \(2h-1\), and the sole prior
   predecessor is at time two.
2. **Passage.**  The criterion uses the occurrence count strictly before
   the terminal time, so \(n_{-1}(g)=1\) corresponds exactly to \(z=0\).
3. **Transport.**  Reindexing after the distinguished particle advances by
   \(-1\) gives (2.5), hence the literal cyclic rotation (2.6).
4. **Firstness.**  Particle order excludes any entrant before the leader
   vacates and excludes every entrant other than the immediate predecessor
   afterwards.
5. **Height and edge count.**  The outer height is \(h\), the residence is
   \(h+1\), and the full quotient trace has \(h+2\) edges.
6. **Orbit period.**  Primality of \(p\) and \(y>0\) make every
   zero-containing composition nonconstant of exact period \(p\).
7. **Exact density.**  Equation (3.4) counts all zero-containing
   compositions, and (3.6) has error \(o(1)\) because
   \(p=O(\sqrt r)\) and \(y=\Theta(r)\).
8. **Corrected deck.**  The essential condition is \(A/2<c<A\): its left
   inequality gives \(p>H+1\), while its right inequality gives residence
   at most \(H\).
9. **Scope.**  Equation (4.2) prevents any inference that the construction
   refutes \((QST_A)\).  It refutes only local or marginal predecessor-
   passage contractions.

The proved/unknown boundary is therefore

\[
 \boxed{
 \begin{array}{l}
 \textbf{Proved: }\text{actual PBBS chronology can saturate a Gaussian}
 \text{ fibre budget;}\\
 \text{all reduced cores of period }L\text{ with }L\log r=o(r)
 \text{ have negligible total lift;}\\
 \textbf{Unproved: }(QST_A)\text{ on long-period, linear-defect Pascal-}
 \text{saddle cores.}
 \end{array}}
\]

