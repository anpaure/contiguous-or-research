# ST_A for PBBS: a golden-ratio long-period reduction and sharp local saturation obstructions

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,\qquad
 H=\lceil A\sqrt r\rceil,
 \tag{0.1}
\]

where \(A>0\) is fixed.  Let \(\overline\nu_H\) be the maximum number of
pairwise quotient-edge-disjoint, nonwrapping PBBS coordinate-residence
intervals of residence at most \(H\), restricted to quotient cycles longer
than \(H+1\).  The exact deck theorem makes

\[
 \overline\nu_H=o_A(B_r/\sqrt r)                 \tag{QST_A}
\]

equivalent to

\[
 \nu_H(P_r)=o_A(B_r\sqrt r).                    \tag{ST_A}
\]

This note does **not** prove or disprove \((QST_A)\).  It proves a new
global chronology reduction and closes several proposed local sources of
the missing little-oh.

Let \(E\) be the nonempty first-pruned Dyck core of an outer rank-\(r\)
root, and let \(\operatorname {per}_\tau(E)\) be the period of \(E\) under
the normalized step-two PBBS map.  Write

\[
 \varphi={1+\sqrt5\over2},\qquad
 \gamma_0={1\over2}\log{4\over\varphi^2}
          =\log{2\over\varphi},                 \tag{0.2}
\]

and

\[
 \gamma_{\rm P}
 ={1\over2}\log{3\over4^{1/3}}.                \tag{0.3}
\]

Numerically, \(\gamma_0\approx0.2119\) and
\(\gamma_{\rm P}\approx0.3183\).  The new conclusions are as follows.

1.  For every fixed \(0<\gamma<\gamma_0\), all outer roots whose
    first-pruned core has

    \[
      \operatorname {per}_\tau(E)
      \le \gamma {r\over\log r}                 \tag{0.4}
    \]

    have exponentially negligible total Catalan mass.  In particular they
    contribute \(o(B_r/r^K)\) possible residence starts for every fixed
    \(K\).

2.  The Pascal-saddle entropy sharpens this to a global conclusion.  All
    cells outside a fixed neighborhood of

    \[
      \left({d\over r},{k\over r}\right)
      =\left({1\over2},{1\over6}\right)          \tag{0.5}
    \]

    already have exponential Catalan deficit, while inside that
    neighborhood the inverse-fibre exponent is uniformly close to its
    saddle value.  Consequently the same conclusion holds, for **all**
    outer roots, for every fixed \(0<\gamma<\gamma_{\rm P}\).  Thus a
    critical counterfamily to \((QST_A)\) may, after a diagonal deletion,
    be assumed to satisfy

    \[
      \operatorname {per}_\tau(E)\ge
      (\gamma_{\rm P}-o(1)){r\over\log r}.       \tag{0.6}
    \]

    Relative to the Gaussian horizon this is

    \[
      {\operatorname {per}_\tau(E)\over H}
      \ge\left({\gamma_{\rm P}\over A}-o(1)\right)
        {\sqrt r\over\log r}\longrightarrow\infty.             \tag{0.7}
    \]

    This quantitatively strengthens the former conclusion
    \(\operatorname {per}_\tau(E)/H\to\infty\).

3.  The critical one-edge-translated deck does not create a second Hall
    constraint: translation is a bijection, so its trace-conflict graph is
    exactly a renamed copy of the first.  The full mixed fixed-core Hall
    hierarchy has sharp capacity

    \[
      \Delta_{r;t,u}
      =\binom{r+1}{t}\binom{r+1}{u}
       -\binom r{t-1}\binom r{u-1},              \tag{0.8}
    \]

    and genuine PBBS Gaussian fibres use a positive limiting fraction of
    all these capacities.  Hence no bounded- or Gaussian-order local Hall
    cut yields an \(o(1)\) gain.

4.  Uniform phase-multiplicity and the pointwise/unconditioned-marginal
    binary dense-reframing routes are also closed.  Actual PBBS families
    exist with exactly one admissible phase
    in a whole terminal rotor, and arbitrary binary reframing words are
    realized by genuine first returns.  After a slow entropy diagonal,
    relative \(1-o(1)\) subfamilies of both calibrations have Pascal-saddle
    first cores and period \((\gamma_{\rm P}-o(1))r/\log r\).  These
    calibration families are
    exponentially subcritical globally, so they do not refute
    \((QST_A)\); they leave a fixed-coefficient contraction, global
    cross-core incidence, or cross-return carrier incidence as the possible
    sources of gain.

5.  The maximum packing now has an exact two-point decision gate.  If
    \(R_H\) is the number of eligible starts and \(\mathcal C_H\) their
    short-lag autocorrelation, then

    \[
      \overline\nu_H\ge{R_H^2\over R_H+2\mathcal C_H}.        \tag{0.9}
    \]

    At critical start mass \(R_H=\Theta(B_r/H)\), \((QST_A)\) requires
    \(\mathcal C_H/R_H\to\infty\).  Exact peak-deletion pullback and the
    harmonic fibre calculation show that outer Pascal sheets preserve,
    rather than create, this divergence.  It must occur among the actual
    reduced predecessor-passage phases.

Consequently the critical \(O\)-to-\(o\) saving is now confined to
long-period, linear-defect Pascal-saddle cores with literal PBBS carrier
compatibility.  Height capacity, the shifted deck, individual core
subset stars, terminal phase multiplicity, the binary reframing itinerary
at the tested marginal level,
and all periods below \((\gamma_{\rm P}-o(1))r/\log r\) are insufficient.

## 1. Exact scale and the root-to-packing implication

The exact rotation-deck sandwich is

\[
 N\overline\nu_H\le\nu_H(P_r)
 \le2N\overline\nu_H+NZ_H,\qquad
 Z_H\le(2H+2)N^{2H+2}.                           \tag{1.0}
\]

For fixed \(A\), \(NZ_H=\exp(o(r))=o(B_r\sqrt r)\), proving the
equivalence of \((QST_A)\) and \((ST_A)\) stated above.

The accepted height trace is

\[
 (h+2)|\mathcal P_h|\le b_{r,h},\qquad
 \overline\nu_H\le\sum_{h<H}{b_{r,h}\over h+2}
                  =O_A(B_r/\sqrt r),             \tag{1.1}
\]

where \(b_{r,h}\) is the number of rank-\(r\) Dyck roots of exact height
\(h\).  Thus \((QST_A)\) asks only for a vanishing improvement over the
right side of (1.1).

Every residence interval has a unique normalized start root.  Therefore,
for every set \(\mathcal R\) of roots,

\[
 \#\{I\in\mathcal P:\text{the start of }I\text{ lies in }\mathcal R\}
 \le |\mathcal R|.                               \tag{1.2}
\]

This elementary injection is what transfers the root-counting theorem
below to the maximum edge-disjoint packing.  No assertion that all roots
are starts is used.

## 2. The exact Fibonacci cap for one inverse pruning fibre

Let the nonempty first-pruned core \(E\) have rank \(d\) and \(k\) peaks.
Put

\[
 y=r-d-k\ge0.                                    \tag{2.1}
\]

The exact complete inverse-fibre size is

\[
 P_r(E)=\binom{y+2d}{2d}
       =\binom{r+d-k}{2d}.                       \tag{2.2}
\]

Since a nonempty Dyck word has \(k\ge1\),

\[
 P_r(E)\le\binom{r+d-1}{2d}.                    \tag{2.3}
\]

The required global cap comes from an exact identity.

### Lemma 2.1 (odd-Fibonacci binomial identity)

For every integer \(n\ge0\), with \(F_0=0,F_1=1\),

\[
 \boxed{
 \sum_{d=0}^{n}\binom{n+d}{2d}=F_{2n+1}.}       \tag{2.4}
\]

#### Proof

Let the left side be \(S_n\).  Its ordinary generating function is

\[
\begin{aligned}
 \sum_{n\ge0}S_nx^n
 &=\sum_{d\ge0}\sum_{j\ge0}
     \binom{j+2d}{2d}x^{j+d}\\
 &=\sum_{d\ge0}{x^d\over(1-x)^{2d+1}}\\
 &={1-x\over1-3x+x^2}.
\end{aligned}                                    \tag{2.5}
\]

The odd Fibonacci subsequence has the same generating function, so
coefficient comparison proves (2.4). \(\square\)

Taking \(n=r-1\) in (2.4), and noting that the term \(d=0\) equals one,
gives the exact summed cap

\[
 \boxed{
 \sum_{d=1}^{r-1}\binom{r+d-1}{2d}=F_{2r-1}-1.} \tag{2.6}
\]

This replaces the former pointwise bound \(P_r(E)\le3^r\).  It also
removes the extraneous factor \(r\) which arose from summing that uniform
pointwise estimate over \(d\).

## 3. Golden-ratio deletion of all moderately short reduced periods

We use the established normalized voltage-itinerary bound: for fixed rank
\(d\), the number of Dyck roots on quotient \(\tau\)-cycles of period at
most \(L\) is at most

\[
 Q_{d,L}:=(2L+2)(2d+1)^{2L+2}.                  \tag{3.1}
\]

The factor \(2L\) is retained: a \(\tau\)-period at most \(L\) gives a
one-step normalized period at most \(2L\).

Let \(\mathcal C_{r,L}\) be the set of rank-\(r\) roots with a nonempty
first-pruned core of quotient period at most \(L\).

### Theorem 3.1 (exact Fibonacci short-period bound)

For all integers \(r\ge2\) and \(L\ge1\),

\[
 \boxed{
 |\mathcal C_{r,L}|
 \le (F_{2r-1}-1)(2L+2)(2r-1)^{2L+2}.}          \tag{3.2}
\]

#### Proof

For fixed \(d\), every core counted by (3.1) has at most the fibre size
in (2.3).  Hence

\[
\begin{aligned}
 |\mathcal C_{r,L}|
 &\le\sum_{d=1}^{r-1}Q_{d,L}\binom{r+d-1}{2d}\\
 &\le(2L+2)(2r-1)^{2L+2}
      \sum_{d=1}^{r-1}\binom{r+d-1}{2d}.
\end{aligned}
\]

Equation (2.6) proves (3.2). \(\square\)

### Corollary 3.2 (universal positive \(r/\log r\) period window)

Let \(L=L(r)\) satisfy

\[
 \limsup_{r\to\infty}{L(r)\log r\over r}<\gamma_0.           \tag{3.3}
\]

Then, for every fixed \(K>0\),

\[
 \boxed{|\mathcal C_{r,L}|=o(B_r/r^K).}          \tag{3.4}
\]

More precisely, if the limsup in (3.3) is at most
\(\gamma<\gamma_0\), then for some \(c=c(\gamma)>0\),

\[
 |\mathcal C_{r,L}|\le e^{-cr}B_r               \tag{3.5}
\]

for all sufficiently large \(r\).

#### Proof

Binet's formula and (3.2) give

\[
 \log|\mathcal C_{r,L}|
 \le2r\log\varphi+(2L+2)\log(2r-1)+o(r).        \tag{3.6}
\]

Under (3.3), the right side is at most

\[
 \bigl(2\log\varphi+2\gamma+o(1)\bigr)r.        \tag{3.7}
\]

By (0.2), \(2\log\varphi+2\gamma<\log4\).  Since

\[
 \log B_r=r\log4-O(\log r),                     \tag{3.8}
\]

(3.5), and hence (3.4), follows. \(\square\)

By (1.2), Corollary 3.2 applies unchanged to any maximum family of
pairwise quotient-edge-disjoint residences.  It is an unconditional
global deletion, not a pointwise contraction within one fibre.

## 4. The global Pascal-saddle sharpening

For a first-pruned core of rank \(d\) and peak count \(k\), the complete
outer cell mass is

\[
 \mathsf M_r(d,k)
 ={1\over d}\binom dk\binom d{k-1}
   \binom{r+d-k}{2d}.                            \tag{4.1}
\]

Writing \(a=d/r\), \(b=k/r\), its exponential rate on the interior of
the feasible triangle is

\[
 \Psi(a,b)
 =2aH(b/a)+(1+a-b)H\left({2a\over1+a-b}\right). \tag{4.2}
\]

The established Narayana--Pascal saddle calculation, equivalently direct
differentiation of (4.2), gives the unique maximum

\[
 (a,b)=\left({1\over2},{1\over6}\right),\qquad
 \Psi(1/2,1/6)=\log4.                            \tag{4.3}
\]

For completeness, put \(n=1+a-b\), \(c=1-a-b\).  On the interior,

\[
 \partial_a\Psi
 =\log{nc\over4(a-b)^2},\qquad
 \partial_b\Psi
 =\log\left[{(a-b)^2c\over b^2n}\right].        \tag{4.3a}
\]

The two entropy perspectives in (4.2) are concave on the feasible
triangle, and their sum is strictly concave on its interior.  The equations
in (4.3a) have the interior solution \((a,b)=(1/2,1/6)\); the boundary
rates are strictly smaller.  This proves the asserted uniqueness and, by
substitution, the value \(\log4\).

Consequently, outside every fixed neighborhood of this point, the sum of
all complete cells is at most \(e^{-c r}B_r\) for some neighborhood-
dependent \(c>0\).

Along any sequence with

\[
 {d\over r}\longrightarrow{1\over2},\qquad
 {k\over r}\longrightarrow{1\over6},            \tag{4.4}
\]

Stirling's formula applied to (2.2) gives

\[
\begin{aligned}
 \log P_r(E)
 &\le r\left({4\over3}\log4-\log3+o(1)\right)\\
 &=r\left(\log{4^{4/3}\over3}+o(1)\right).       \tag{4.5}
\end{aligned}
\]

Indeed \(r+d-k=(4/3+o(1))r\) and \(2d=(1+o(1))r\), so the binomial
entropy is

\[
 {4\over3}H(3/4)
 ={4\over3}\log4-\log3.                         \tag{4.6}
\]

More uniformly, inside a fixed \(\epsilon\)-neighborhood of the saddle,
the exponent in (4.5) is at most

\[
 p_0+\omega(\epsilon),\qquad
 p_0=\log{4^{4/3}\over3},\qquad
 \omega(\epsilon)\longrightarrow0.              \tag{4.7}
\]

Let \(\mathcal C^{\rm near}_{r,L}(\epsilon)\) denote the short-period
outer roots in this neighborhood.  Summing over at most \(r\) ranks and
using (3.1) gives

\[
 \log|\mathcal C^{\rm near}_{r,L}(\epsilon)|
 \le r\bigl(p_0+\omega(\epsilon)\bigr)
      +(2L+2)\log(2r-1)+o(r).                    \tag{4.8}
\]

### Theorem 4.1 (global Pascal long-period reduction)

If

\[
 \limsup_{r\to\infty}{L(r)\log r\over r}<\gamma_{\rm P},     \tag{4.9}
\]

then, for every fixed \(K>0\),

\[
 \boxed{|\mathcal C_{r,L}|=o(B_r/r^K).}          \tag{4.10}
\]

#### Proof

If the limsup in (4.9) is at most \(\gamma<\gamma_{\rm P}\), choose
\(\epsilon>0\) so small that

\[
 p_0+\omega(\epsilon)+2\gamma<\log4.             \tag{4.11}
\]

Equation (4.8) makes the near-saddle contribution exponentially smaller
than \(B_r\).  The complement is exponentially smaller by the unique-
saddle conclusion following (4.3), even without a period restriction.
Their sum proves (4.10). \(\square\)

### Corollary 4.2 (diagonal critical period floor)

From any quotient packing of size \(\Omega(B_r/\sqrt r)\), one may delete
\(o(B_r/\sqrt r)\) intervals and retain only starts satisfying

\[
 \boxed{
 \operatorname {per}_\tau(E)\ge
 (\gamma_{\rm P}-o(1)){r\over\log r}.}           \tag{4.12}
\]

#### Proof

Choose constants \(\gamma_j\uparrow\gamma_{\rm P}\).  Theorem 4.1 and
(1.2) give, for each \(j\), a rank threshold above which the packing mass
with period at most \(\gamma_jr/\log r\) is at most
\(2^{-j}B_r/\sqrt r\).  Use these thresholds successively.  The resulting
step function \(\gamma(r)\uparrow\gamma_{\rm P}\) gives (4.12), with
discarded mass \(o(B_r/\sqrt r)\). \(\square\)

The constant \(\gamma_{\rm P}\) is the sharp ceiling of these one-level
ingredients.  At the saddle the core-shape entropy is

\[
 2\cdot{1\over2}H(1/3)
 =\log3-{1\over3}\log4=2\gamma_{\rm P},          \tag{4.13}
\]

while the inverse-fibre exponent is \(p_0\); their sum is \(\log4\).
At \(L\sim\gamma_{\rm P}r/\log r\), the voltage count can therefore use
the entire remaining core-shape entropy.  Passing this endpoint requires
a genuine period--peak or chronology correlation.

### Proposition 4.3 (long period and homomesy still permit abstract saturation)

The period floor (4.12) is not itself a packing contraction.  There is an
exact abstract predecessor-itinerary system, satisfying all presently used
one-level PBBS passage and Pascal-capacity axioms, with normalized
step-two period \(\Theta(r)\) and packing of order one full reciprocal-
height cell capacity.

More explicitly, put

\[
 G=2H-1,\qquad q_0=2(G+1)=4H,qquad
 R=\left\lceil{r\over q_0}\right\rceil,qquad Q=Rq_0.          \tag{4.14}
\]

For \(p=2d+1\), choose offsets \(c_0,\ldots,c_{Q-1}\in\mathbb Z_p\)
so that at each origin \(b_j=jq_0\),

\[
 c_{b_j}=c_{b_j+5}=0,qquad
 c_{b_j+2}=c_{b_j+G}=-1,                         \tag{4.15}
\]

no other offset before \(G\) is \(0\) or \(-1\), and no nontrivial cyclic
shift of \(c\) equals \(c\) plus a global label.  Such words exist for all
large \(r\).  Indeed the number satisfying the local restrictions is at
least

\[
 (p-2)^{(G-3)R}p^{Q-(G+1)R}\ge c_Ap^{Q-4R}.       \tag{4.15a}
\]

For a fixed nontrivial shift and global label, the affine-period equations
leave at most \(Q/2\) free offsets, so all forbidden words number at most
\(Qp^{Q/2+1}\).  The exponent difference is

\[
 Q-4R-(Q/2+1)=R(G-3)-1\longrightarrow\infty,     \tag{4.15b}
\]

which proves existence.

Define

\[
 \kappa_{Qj+t}=j+c_t\pmod p.                    \tag{4.16}
\]

Then every label occurs exactly \(Q\) times.  At each special origin the
distinguished label first reappears at time five, its predecessor occurs
at times two and \(G\), and it does not occur in between.  Thus the exact
predecessor-passage data are

\[
 h=5<G,qquad n_{-1}(G)=1,qquad z=0.            \tag{4.17}
\]

The normalized one-step period is \(Q\), so the step-two period is
\(Q/2=\Theta(r)\).  Consecutive special origins are \(G+1=2H\)
step-two phases apart, while each lifted return trace has

\[
 {G+3\over2}=H+1                                \tag{4.18}
\]

edges.  Hence the special traces are pairwise edge-disjoint.

In a Pascal cell let \(\mathsf N(d,k)\) be its number of cores and
\(F_r(d,k)\) its inverse-fibre size.  Lifting every special origin through
the terminal-zero subfibre

\[
 K_0(d,k)=\binom{r+d-k-1}{2d-1}
          =\left({3\over4}+o(1)\right)F_r(d,k)   \tag{4.19}
\]

gives the abstract packing

\[
 \left\lfloor{\mathsf N(d,k)\over Q}\right\rfloor R K_0(d,k)
 =\left({3\over16}+o(1)\right)
   {\mathsf M_r(d,k)\over H}.                    \tag{4.20}
\]

This construction is **not** asserted to be realized by Dyck/PBBS cores,
so it is not a counterexample to \((QST_A)\).  It is a rigorous logical
obstruction: long period, componentwise label homomesy, bistochastic lag
margins, the exact predecessor order, terminal slot zero, and every
one-level Pascal edge capacity together still permit critical saturation.
The remaining estimate must use a PBBS- and peak-sensitive restriction on
which long itineraries or transported carrier maps are realizable.

## 5. Why the shifted-deck Hall route cannot supply the little-oh

The critical-saturation normal form supplies a simple fixed-core trace
\(I\) and its one-edge translate \(\sigma I\).  But \(\sigma\) is a
bijection between the two quotient edge decks.  Hence, for all traces
\(I,J\),

\[
 \boxed{\sigma I\cap\sigma J=\sigma(I\cap J).}   \tag{5.1}
\]

Thus pairwise disjointness of all translated traces is equivalent to
pairwise disjointness of the original traces.  The second deck duplicates
the conflict graph; it does not add an independent set-packing constraint.

There remains a mixed containment-star hierarchy because a simple sector
has disjoint fixed cores \(K,K'\), each of size \(q=r-s\), in the two
decks.  At paired transition columns, the two available coordinate shores
have size \(r+1\) and intersect in exactly one coordinate.  Since
\(K\cap K'=\varnothing\), charging a \(t\)-subset of \(K\) and a
\(u\)-subset of \(K'\) gives the exact capacity (0.8): every disjoint
family obeys

\[
 \sum_I\binom{q_I}{t}\binom{q_I}{u}|I|
 \le\Delta_{r;t,u}E,                             \tag{5.2}
\]

where \(E\) is the relevant edge volume.  Its ratio to the naive product
capacity is

\[
 {\Delta_{r;t,u}\over
   \binom{r+1}{t}\binom{r+1}{u}}
 =1-{tu\over(r+1)^2}.                            \tag{5.3}
\]

In particular (5.3) tends to one for \(t,u=O(\sqrt r)\).

This lack of gain is attained locally by actual PBBS dynamics.  In the
prime-period mountain inverse fibre with \(s/\sqrt r\to c\), a literal
simple fixed-core packing covers the limiting edge fraction

\[
 \theta(c)={1-e^{-4c^2}\over2}>0.                \tag{5.4}
\]

For \(t/\sqrt r\to\alpha\) and \(u/\sqrt r\to\beta\), its utilization
of (5.2) tends

\[
 \theta(c)e^{-c(\alpha+\beta)}>0.                \tag{5.5}
\]

That fibre has only \(\exp(O(\sqrt r\log r))\) roots, so it is not a
counterexample to \((QST_A)\).  Equations (5.1)--(5.5) prove the exact
no-go: no bounded- or Gaussian-order mixed subset-star Hall inequality,
even on the double deck, can force the required vanishing factor.

## 6. Phase and reframing obstructions are actual but globally sparse

Two further possible uniform gains fail on literal PBBS families.

### 6.1 No uniform multiplicity of admissible terminal phases

There are actual roots of the form

\[
 D(F)=1^p0^p1^{2p-1}0^{p+1}F0^{p-2},             \tag{6.1}
\]

where \(F\) has semilength \(M\) and exact height \(p-2\), for which the
duration \(2p-1\) return has exactly one admissible phase in its whole
terminal rotor.  The same family has positive endpoint excess \(2p\), and
distinct constructed starts on one quotient cycle have cyclic separation
at least \(s=2p-1\) in both directions.  A full duration-\(s\) residence
trace has \(s+2\) edges, so starts separated by exactly \(s\) can share two
boundary edges.  Pairwise disjointness of the whole family does not follow.

All constructed roots project to the same phase of a terminal rotor of
exact period \(s\), so same-orbit start separations are multiples of
\(s\).  Only the immediately preceding and following constructed starts
can conflict.  The conflict graph has maximum degree at most two, and a
greedy three-colouring retains at least one third.  Thus, writing \(U\) for
transported-union mass and \(S\) for start mass,

\[
 U=S,\qquad {S\over3}\le\operatorname {Pack}\le S.           \tag{6.2}
\]

Its ambient rank is \(r=M+3p-1\), and its size is only
\(\exp[-\Theta(\sqrt r)]\) times the critical Catalan scale.  Hence (6.1)
does not disprove \((QST_A)\); it rules out a pointwise phase-multiplicity
gain.

The same family can be filtered into the long-period Pascal saddle.  Its
first deepest root child is its final primitive component and is the last
root child, so the first-pruning terminal slot is exactly \(z=0\).  Its
total start mass is

\[
 B_r\exp[-\Theta_A(\sqrt r)]/\sqrt r.            \tag{6.2a}
\]

Choose the saddle-neighborhood and period diagonals slowly enough that the
discarded root set has mass \(B_r\exp[-\omega(\sqrt r)]\).  A relative
\(1-o(1)\) subfamily of (6.1) then satisfies

\[
 {d\over r}\to{1\over2},\qquad {k\over r}\to{1\over6},
 \qquad
 \operatorname {per}_\tau(E)\ge
 (\gamma_{\rm P}-o(1)){r\over\log r}.            \tag{6.2b}
\]

Thus positive endpoint boundary, a singleton admissible phase, a
constant-fraction actual edge-disjoint subfamily, and long Pascal-saddle
core period still do not give a pointwise contraction.  Only the
stretched-exponential global rarity of these contexts keeps the family
subcritical.

### 6.2 Dense reframing and long-period fibre amplification

For every binary word of length \(s-1\), the spectator-conveyor
construction gives a genuine first zero-winding duration-\(s\) return
whose canonical frame changes exactly at the ones of that word.  An
arbitrary bounded-height Dyck spectator of semilength
\(r-O(\sqrt r)\), subject to the exact cap
\(\operatorname{ht}(Q)\le\lfloor s/2\rfloor\), may be inserted without
changing the binary itinerary or the exact endpoint floor.

For fixed \(0<\alpha<A\), \(s=\lfloor\alpha\sqrt r\rfloor\), and every
\(\varepsilon,\eta>0\), this yields a long-cycle, pairwise
quotient-edge-disjoint actual family satisfying

\[
 R(I)\ge s/10,\qquad
 G(I)<\left\lceil(1/2+\varepsilon)\log_2r\right\rceil,         \tag{6.3}
\]

and

\[
 |\mathcal P_r|\ge {B_r\over s}
 \exp\left[-\bigl(\log(3+\eta)+o(1)\bigr)s\right].            \tag{6.4}
\]

Here a duration-\(s\) return has a full positive-residence trace of
\(s+2\) quotient edges.  The cyclic greedy denominator used in (6.4) is
therefore \(2(s+2)-1=2s+3\), not \(2s-1\); this finite correction is
absorbed by the displayed factor \(B_r/s\).

This calibration can be placed inside the full long-period Pascal class.
For a reduced predecessor passage \((E,g)\), with core rank \(d\), peak
count \(k\), and prescribed terminal slot \(z\), its exact permitted
parent hyperplane has size

\[
 K_r(E,g)=\binom{r+d-k-z-1}{2d-1}.               \tag{6.5}
\]

If a collection of reduced passage supports is simple and pairwise
edge-disjoint, then **all** permitted parent lifts in (6.5) are pairwise
edge-disjoint.  Indeed, a collision projects under
\(\partial\tau=\tau\partial\) to a reduced-edge collision; simplicity
then fixes the same time offset, and bijectivity of fibre transport fixes
the same parent lift.

The exact utilization ratio is

\[
 \boxed{
 {K_r(E,g)\over P_r(E)}
 ={2d\over r+d-k}
  \prod_{j=0}^{z-1}
  {r-d-k-j\over r+d-k-1-j}.}                    \tag{6.6}
\]

Uniformly on the Gaussian Pascal tube and for \(z\le3\log r\),

\[
 {K_r(E,g)\over P_r(E)}
 =\left({3\over4}+o(1)\right)4^{-z}.             \tag{6.7}
\]

For the conveyor family \(z=0\).  Because its start mass is
\(B_r\exp[-O(\sqrt r)]\), whereas roots outside a shrinking Pascal
neighborhood or below a sufficiently slow diagonal period threshold have
mass \(B_r\exp[-\omega(\sqrt r)]\), a relative \(1-o(1)\) subfamily
satisfies simultaneously

\[
 {d\over r}\to{1\over2},\qquad {k\over r}\to{1\over6},
 \qquad
 \operatorname {per}_\tau(E)\ge
 (\gamma_{\rm P}-o(1)){r\over\log r}.            \tag{6.8}
\]

Thus (6.4) is an actual long-period Pascal-saddle packing in which every
individual reduced passage packet uses \((3/4+o(1))\) of its full parent
fibre.  Long period creates no local loss; it guarantees simplicity and
thereby enables fibre amplification.

The exact capped dual-product is even sharper at the marginal level: the
unconditioned critical Boltzmann mass of the occupancy event corresponding
to the dense/no-long-stable-block inequalities in (6.3) tends to one.
Product tuples need not be actual PBBS returns.  Formula (6.4) is
exponentially below \(B_r/s\), so again it is a calibration rather than a
counterexample.  The product statement does **not** imply the same ratio
after conditioning on the target total semilength.  It proves only that
the binary itinerary and individual cap entropies cannot supply the
missing little-oh through this unconditioned marginal-product estimate.

The literal information omitted by the saturated product is the common
carrier identity between different phases and, globally, between
different selected returns.  In addition, a coefficientwise contraction
at the prescribed total dual size is not excluded by the unconditioned
calculation.  These are the surviving possible sources of strictness.

The calibration has endpoint excess \(\Lambda=0\).  It therefore does not
obstruct a proof which first removes that sector and then uses a genuinely
positive-boundary condition.  Its exact scope is that long period, saddle
ranks, dense reframing, bounded terminal slot, and all per-core capacities
together still do not yield a local \(o(1)\) contraction.

## 7. The exact two-point gate for the maximum packing

Let \(E_H\) be the set of genuine eligible long-cycle return starts, put

\[
 R_H=|E_H|,
 \qquad
 \mathcal C_H=\sum_{t=1}^{H+1}|E_H\cap\tau^{-t}E_H|.          \tag{7.1}
\]

The conflict graph has vertex set \(E_H\), with two starts adjacent when
their residence traces share a quotient edge.  Every conflict appears in
one of the displacements in (7.1), so Caro--Wei and Cauchy--Schwarz give

\[
 \boxed{
 {R_H^2\over R_H+2\mathcal C_H}
 \le\overline\nu_H\le R_H.}                    \tag{7.2}
\]

There is also a sharp universal Fejer-window lower bound on the
autocorrelation itself:

\[
 \boxed{
 \mathcal C_H\ge{1\over2}\left(
 { (H+2)R_H^2\over B_r}-R_H\right).}             \tag{7.3}
\]

Indeed, for \(x=\mathbf1_{E_H}\), set

\[
 y(v)=\sum_{a=0}^{H+1}x(\tau^av).
\]

Then \(\sum_vy(v)=(H+2)R_H\), so Cauchy--Schwarz gives
\(\sum_vy(v)^2\ge(H+2)^2R_H^2/B_r\).  Expanding by displacement and
bounding each triangular weight by \(H+2\) gives (7.3).

Equations (7.2)--(7.3) locate the exact critical ambiguity.  If

\[
 R_H\ge\kappa {B_r\over H},\qquad
 \mathcal C_H\le\chi R_H                       \tag{7.4}
\]

for fixed \(\kappa>0,\chi<\infty\), then

\[
 \overline\nu_H\ge {\kappa\over1+2\chi}{B_r\over H},         \tag{7.5}
\]

and \((QST_A)\) is false.  Conversely, if \((QST_A)\) is true while
\(R_H=\Omega(B_r/H)\), it is necessary that

\[
 {\mathcal C_H\over R_H}\longrightarrow\infty.               \tag{7.6}
\]

The lower bound (7.3) forces divergence only when
\(HR_H/B_r\to\infty\); it is exactly constant-order at
\(R_H=\Theta(B_r/H)\).

Peak deletion does not resolve this ambiguity.  In the Pascal saddle, let
\(\mathcal A_{d,k,H}\) be the reduced cores carrying the decorated
terminal-zero predecessor passage, and define

\[
\begin{aligned}
 \mathscr R_H
 &=\sum_{d,k}F_r(d,k)|\mathcal A_{d,k,H}|,\\
 \mathscr C_H
 &=\sum_{d,k}F_r(d,k)
   \sum_{t=1}^{H+1}
   |\mathcal A_{d,k,H}\cap
      \tau_d^{-t}\mathcal A_{d,k,H}|,
\end{aligned}                                                    \tag{7.7}
\]

where \(F_r(d,k)=\binom{r+d-k}{2d}\).  The exact first peak-deletion
pullback gives, on every critical saddle-concentrated subsequence,

\[
 \boxed{
 \left({1\over2}-o(1)\right){\mathscr C_H\over\mathscr R_H}
 \le {\mathcal C_H\over R_H}
 \le\left({4\over3}+o(1)\right)
       {\mathscr C_H\over\mathscr R_H}.}          \tag{7.8}
\]

Thus the outer Pascal fibre neither creates nor removes divergent
clustering.

On a coordinate-stable harmonic inverse profile, this becomes still more
literal.  If \(J_C\) is the set of genuine reduced passage phases on a
reduced cycle \(C\), and the profile has \(L\) inverse levels, its
terminal-zero cylinder density is

\[
 Q_L=\prod_{j=0}^{L-1}\left(1-{1\over(j+2)^2}\right)
 ={L+2\over2(L+1)}.                              \tag{7.9}
\]

Writing \(M_L\) for the complete profile fibre and

\[
 P_H(J_C)=\sum_{t=1}^{H+1}|J_C\cap(J_C-t)|,      \tag{7.10}
\]

the exact transported-cylinder intersections give

\[
 R_H(C)=Q_LM_L|J_C|,                             \tag{7.11}
\]

\[
 (1-o(1))Q_L^2M_LP_H(J_C)
 \le\mathcal C_H(C)
 \le Q_LM_LP_H(J_C).                             \tag{7.12}
\]

Hence

\[
 {\mathcal C_H(C)\over R_H(C)}
 \asymp {P_H(J_C)\over|J_C|}.                   \tag{7.13}
\]

The decisive maximum-packing question is therefore a weighted
short-lag-degree theorem for the **actual reduced predecessor-passage
phases**.  A bounded weighted degree together with critical start mass
refutes \((QST_A)\); a proof of \((QST_A)\) at critical start mass must
force the weighted degree to diverge.  Neither the Pascal sheets, long
period, nor one-point port capacities decide this alternative.

## 8. The exact critical normal form after all proved deletions

Assume that \((QST_A)\) fails.  Then for some \(\varepsilon>0\) and an
infinite sequence of \(r\), there are quotient-edge-disjoint families
\(\mathcal P_r\) with

\[
 |\mathcal P_r|\ge\varepsilon B_r/\sqrt r.       \tag{8.1}
\]

Combine the audited height, minimal-return, Pascal-saddle, terminal-slot,
and reciprocal-height stability reductions with Theorem 4.1.  After an
absolute-factor loss, an arbitrarily small fixed-fraction loss, and
discarding \(o(B_r/\sqrt r)\) intervals, one obtains a positive critical
subfamily in which every member has:

\[
\begin{gathered}
 a\sqrt r\le h\le A\sqrt r,\qquad
 a\sqrt r\le |I|\le H+1\le A\sqrt r+2,\tag{8.2}\\
 d={r\over2}+O(\sqrt{r\log r}),\qquad
 k={r\over6}+O(\sqrt{r\log r}),                 \tag{8.3}\\
 d-k\ge c_0r,\qquad z\le3\log r,               \tag{8.4}\\
 \kappa_g=-1,\qquad h_E<g\le2H-1,\qquad
 n_{-1}(g)=2z+1,                                 \tag{8.5}\\
 R(I)\ge\delta |I|,\qquad
 G(I)<\left({1\over2}+\epsilon\right)\log_2r+1,\tag{8.6}\\
 \operatorname {per}_\tau(E)\ge
       (\gamma_{\rm P}-o(1)){r\over\log r}      \tag{8.7}
\end{gathered}
\]

for constants \(a,c_0,\delta>0\) and every fixed
\(\epsilon>0\).  The retained subfamily and the harmless \(o(1)\) in
(8.7) may depend on \(\epsilon\).  The simple fixed-core traces and their
one-edge translates are pairwise disjoint, and their trace union contains
a positive fraction of the quotient edge deck.

In (8.2), \(|I|\) counts the full positive-residence trace, hence
\(|I|=s(I)+2\).  The chronology theorem originally gives
\(R(I)\ge\delta_0s(I)\); because \(s(I)\ge a\sqrt r-2\), replacing
\(\delta_0\) by a smaller fixed constant gives the displayed
\(R(I)\ge\delta|I|\) for all sufficiently large \(r\).

The quantifiers in (8.7) are important.  It is a diagonal consequence of
the theorem for every fixed \(\gamma<\gamma_{\rm P}\).  It does not give
the same exponential estimate at the endpoint
\(\gamma=\gamma_{\rm P}\).

This is the strongest currently proved ST normal form.  A counterfamily
must be simultaneously Gaussian, long-period, linear-defect,
bounded-terminal-slot, linearly reframing, half-logarithmically
gap-free, and a positive-density double-deck fixed-core partial tiling.

## 9. Independent audit of the decisive new count

The golden-ratio and fibre-amplification steps were checked independently
at the level of every factor in the estimates.

1.  **Exact fibre.**  Peak deletion gives (2.2), and nonempty cores have
    \(k\ge1\), giving (2.3).
2.  **No rank overcount.**  At fixed \(d\), (3.1) counts core roots, not
    core cycles.  Multiplying by the largest exact fibre at that rank and
    summing over \(d\) is therefore legitimate.
3.  **Fibonacci identity.**  The generating function (2.5) proves
    (2.4) exactly; setting \(n=r-1\) gives (2.6).
4.  **Period exponent.**  At \(L\sim\gamma r/\log r\), the voltage factor
    contributes \(2\gamma r+o(r)\), not \(\gamma r\).  This is why the
    thresholds in (0.2)--(0.3) contain the factor \(1/2\).
5.  **Catalan comparison.**  \(B_r=\exp(r\log4-O(\log r))\), while the
    Fibonacci term has exponent \(2r\log\varphi\).
6.  **Pascal entropy.**  At \((d/r,k/r)=(1/2,1/6)\), the inverse-fibre
    exponent is exactly \((4/3)H(3/4)), equal to
    \(\log(4^{4/3}/3)\).
7.  **Global split.**  Outside a fixed saddle neighborhood, the complete
    cell entropy has a fixed deficit.  Inside, (4.7) and the voltage count
    give (4.11).  Thus no shrinking-tube tail estimate is silently
    multiplied into the period estimate.
8.  **Packing transfer.**  Deleting a root set of size
    \(o(B_r/r^K)\) deletes at most that many interval starts by (1.2).
9.  **Full residence support.**  A duration-\(s\) return uses \(s+2\)
    quotient edges.  This gives the exact greedy denominator \(2s+3\).
    In the terminal-singleton family, separation \(s\) does not imply
    whole-family disjointness; the common period-\(s\) terminal phase gives
    conflict degree at most two and hence the audited factor \(1/3\).
10. **Fibre amplification.**  Simplicity of the reduced trace fixes the
    collision offset, and bijective fibre transport then fixes the parent
    lift.  This independently verifies (6.5)--(6.7).
11. **Positive-boundary filter.**  The terminal-singleton root has
    first-pruning slot \(z=0\); its exact-height shell is
    \(B_re^{-\Theta(\sqrt r)}/\sqrt r\), so a slow saddle/period diagonal
    retains relative \(1-o(1)\) before the degree-two selection.

The independent audit also checked that the stricter itinerary convention
\(2L(2d+1)^{2L}\) changes only finite factors, not either threshold.  This
report retains the previously audited looser convention (3.1).

## 10. Proved and unproved boundary

Proved:

\[
\boxed{
\begin{array}{l}
\text{all first-pruned core periods below }
(\gamma_{\rm P}-o(1))r/\log r\\
\text{are negligible globally at the critical packing scale;}\\
\text{the shifted deck duplicates the conflict graph, and its full local}
\text{ Hall hierarchy is sharply saturable;}\\
\text{terminal singleton phases and arbitrary dense binary reframing occur}
\text{in genuine PBBS long-cycle families;}\\
\text{the maximum packing obeys the exact two-point gate (7.2), and the}
\text{outer Pascal sheets preserve its bounded/divergent clustering ratio.}
\end{array}}
\tag{10.1}
\]

Unproved:

\[
\boxed{
 \overline\nu_{\lceil A\sqrt r\rceil}=o_A(B_r/\sqrt r)
 \quad\text{on the long-period class (8.2)--(8.7).}}         \tag{10.2}
\]

The exact remaining theorem must exploit a fixed-coefficient contraction,
the literal common-carrier equations, or a PBBS-specific cross-return
trace-overlap invariant on long-period Pascal-saddle cores.  In the exact
two-point formulation, it must show that critical weighted reduced
passage-phase mass has diverging short-lag degree; a bounded degree would
instead refute \((QST_A)\) by (7.2).  No conclusion stronger than (10.2)
is claimed, and in particular this report does not claim the constant-one
theorem.
