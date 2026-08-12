# Domino-twin superpackets: an annealed near-factor and synchronized odd-depth repeat excess

**Date:** 2026-07-27  
**Status:** constructive probabilistic near-factor with leave
\(O(N/\log m)\), proved without a fixed-uniformity matching theorem; this
gives a simultaneous linear repeat-excess theorem on a growing odd-depth
window.  The stronger leave \(o(N/\sqrt m)\) is not claimed.

## 0. Statement and distinction from the critical square-root gate

Let

\[
 n=2m,\qquad R=m-q_0,\qquad q_0=a\sqrt m+O(1),             \tag{0.1}
\]

and take the parity subsequence on which \(R\) is odd.  Let

\[
 V=\binom{[n]}R,\qquad N=|V|,                              \tag{0.2}
\]

and let \(\mathcal H^\square=(V,\mathcal Q)\) be the **simple**
domino-twin superpacket hypergraph.  Thus repetitions coming from
anchored orders have been quotiented out.

The main result is the following.

### Theorem 0.1 (annealed domino-twin near-factor)

There is a matching \(\mathcal M\subseteq\mathcal Q\) whose leave
\(\mathcal L\) satisfies

\[
 \boxed{|\mathcal L|\le {2N\over\log m}.}                  \tag{0.3}
\]

The matching is produced by the explicit slow isolated-bite algorithm in
Section 3.  Its proof is a time-zero history expansion using the exact
radius-ball and factorial-overlap estimates; no fixed-\(K\)
Pippenger--Spencer theorem is invoked.

Splitting every selected superpacket into its two ordinary cyclic packets
gives the following stronger structural conclusion.

### Theorem 0.2 (synchronized odd-depth repeat)

Let \(T=|\mathcal M|=(N-|\mathcal L|)/(4m)\).  At every odd displacement
\(d\) for which \(2\le R-d\le n-2\), the ordinary component packets have
raw repeat excess

\[
 \boxed{E_{q_0+d}\ge mT={N-|\mathcal L|\over4}
       =\left({1\over4}-o(1)\right)N.}                    \tag{0.4}
\]

If the scalar rank floor is subtracted, then

\[
 \boxed{
 \widetilde E_{q_0+d}
 \ge {N-|\mathcal L|\over4}
   -\left(N-|\mathcal L|-\binom n{R-d}\right)_+.}         \tag{0.5}
\]

Consequently, uniformly for every growing

\[
 H=o\left({\sqrt m\over\log m}\right),                    \tag{0.6}
\]

one has simultaneously at all odd \(1\le d\le H\)

\[
 \widetilde E_{q_0+d}\ge(1/4-o(1))N.                     \tag{0.7}
\]

This is the requested alternative to an \(o(N/\sqrt m)\) critical
leave: it is an integral entrance near-factor and a coherent growing-depth
repeat obstruction, not merely a fractional or one-depth calculation.

There is an unavoidable endpoint distinction.  Product-like thinning in
the simple catalogue has essentially no edge at density
\(z=o(m^{-1/2})\); Section 7 proves this exactly.  Thus factorial-overlap
control can give (0.3), but it cannot by itself continue a quasirandom
trajectory to the stronger square-root leave.  Such a continuation would
require a structured absorber.

## 1. Exact simple-catalogue parameters

A simple superpacket is an unoriented cyclic necklace of \(m\) unordered
dominoes.  Its size, catalogue size, and vertex degree are

\[
 K=2n=4m,                                                  \tag{1.1}
\]

\[
 |\mathcal Q|={(n-1)!\over2^m},                            \tag{1.2}
\]

\[
 D=2^{1-m}R!(n-R)!.                                       \tag{1.3}
\]

The exact maximum normalized pair codegree and edge-local collision
energy are

\[
 \delta:={\Delta_2\over D}={5\over R(n-R)}
 ={5+o(1)\over m^2},                                      \tag{1.4}
\]

\[
 \eta={25n\over R(n-R)}+O_a(m^{-3})
 ={50+o(1)\over m}.                                       \tag{1.5}
\]

If \(F\in\mathcal Q\), \(X\in F\), and \(1\le p\le C_0\log m\),
the factorial-overlap theorem descends from the labelled presentation to
the simple quotient and says

\[
 {1\over D}
 \sum_{\substack{F'\ni X\\F'\ne F}}
 (|F\cap F'|-1)_p
 \le(Cp)^{Cp}m^{-2}.                                      \tag{1.6}
\]

Indeed every simple column and every simple link member has the same
anchored multiplicity \(n2^m\), so numerator and denominator in the
labelled estimate are divided by the same number.  The parallel
representations of one simple column disappear rather than create a new
term.

The apparently dangerous whole-component coincidences are included in
(1.6).  A fixed simple \(F\) has \(2^m\) component traces, and every such
trace belongs to one further simple superpacket.  Even if all
whole-component neighbors through \(X\) are charged at overlap \(n\),
their normalized contribution for \(p\le C_0\log m\) is at most

\[
 {2^m n^p\over D}
 =\exp[-(2+o(1))m\log m],                                  \tag{1.7}
\]

which is negligible compared with the right side of (1.6).

Finally, inside one superpacket, every Johnson ball of radius \(h\) has
at most

\[
 4h+2                                                        \tag{1.8}
\]

members.  Equations (1.6)--(1.8), rather than maximum codegree alone,
are the inputs to the history estimate below.

## 2. The annealed history lemma

The point of the next lemma is that it follows the actual random history
from time zero.  It does **not** assert regularity for every residual and
therefore is not contradicted by the dense central-slice residuals.

Put

\[
 z_*=({\log m})^{-1},\qquad
 \gamma=m^{-10},\qquad
 q=1-e^{-\gamma/K},\qquad
 \ell=\lceil40\log m\rceil.                               \tag{2.1}
\]

For a deterministic density \(z\ge z_*\), define

\[
 \rho(z)=Dz^{K-1}.                                         \tag{2.2}
\]

### Lemma 2.1 (time-zero history moment)

Run the isolated-bite process of Section 3, with all marking probabilities
determined by the deterministic reference sequence \(z_s\).  Uniformly
at every round before \(z_s=z_*\), the following hold.

1. For a uniformly chosen entrance vertex \(X\), conditional on \(X\)
   being live, its live degree satisfies
   \[
   \mathbb E\left[
    \left|{d_s(X)\over\rho(z_s)}-1\right|^{2\ell}
    \,\middle|\,X\ {\rm live}
   \right]
   \le
   \left({(C\ell\log m)^C\over mz_s}\right)^\ell.        \tag{2.3}
   \]

2. For a uniformly chosen incidence \(X\in F\), conditional on \(F\)
   being live, the number \(c_s(F)\) of other live superpackets meeting
   \(F\) satisfies
   \[
   \mathbb E\left[
    \left|{c_s(F)\over K\rho(z_s)}-1\right|^{2\ell}
    \,\middle|\,F\ {\rm live}
   \right]
   \le
   \left({(C\ell\log m)^C\over mz_s}\right)^\ell.        \tag{2.4}
   \]

3. With \(\varepsilon=m^{-1/10}\), the expected fraction of live
   vertices or live incidences violating the corresponding
   \((1\pm\varepsilon)\) estimate is at most
   \[
   \exp[-c\log m\log\log m].                                     \tag{2.5}
   \]

The constants depend only on \(a\) and the fixed choice \(C_0>100\) in
(1.6).

### Proof

We give the diagram calculation because this is precisely where a
fixed-rank black box would conceal the growing-\(K\) issue.

#### Step 1: one bite and incidence diagrams

Fix a root target \(X\).  A change in its live degree is caused by a
marked event column \(G\) meeting a link row \(F\ni X\).  Expand a
\(2j\)-th centered moment, \(j\le\ell\), before taking expectation over
the independent marks of the current bite.  A term is encoded by a
bipartite incidence diagram:

- row nodes are link packets through \(X\);
- column nodes are marked packets;
- an incidence records a nonempty row--column intersection.

A column appearing once cancels after centering.  Hence every surviving
column has degree at least two, unless it belongs to a tree attached to a
previous-time row.

#### Step 2: peel all trees

For a row \(F\ni X\), the number of event columns meeting it is at most
\(KD\).  For an event column \(G\not\ni X\), the number of rows through
\(X\) which it can meet is at most

\[
 K\Delta_2\le {C D\over m}.                               \tag{2.6}
\]

Peeling a leaf alternately on the two shores therefore gives, for every
tree diagram, its product of root choices times one factor
\(O((mz)^{-1})\) for each centered branch pair after normalization by
the current reference degree \(\rho(z)\).  This is the elementary
tree-homomorphism induction: sum the label of a leaf first, use \(KD\) on
the row shore and (2.6) on the event shore, and continue toward the root.

#### Step 3: compress the two-core

After the trees are removed, choose a spanning forest of the remaining
bipartite two-core.  Every nonforest bundle joins two already exposed row
packets \(F,F'\ni X\).  Put \(r=|F\cap F'|-1\).  A common event column
meeting both rows either uses one witness in
\(F\cap F'\setminus\{X\}\), or two distinct witnesses, one in each row.
Hence its number is bounded by

\[
 c_X(F,F')\le Dr+K^2\Delta_2\le CD(1+r).                  \tag{2.7}
\]

For a bundle of \(b\) common event columns, reverse the count and use

\[
 c_X(F,F')^b\le (CD)^b(1+r^b),
 \qquad
 r^b=\sum_{p=1}^b S(b,p)(r)_p.                             \tag{2.8}
\]

The same-witness factorial sum is exactly

\[
 p!\sum_{\substack{C\subseteq F\setminus\{X\}\\|C|=p}}
 d(\{X\}\cup C)
 =\sum_{F'\ni X}(|F\cap F'|-1)_p.                         \tag{2.9}
\]

Equation (1.6) pays (2.9) by \((Cp)^{Cp}m^{-2}D\).  The
distinct-witness part has already been summed in
\(K^2\Delta_2=O(D)\); it is the constant term in (2.8), not an unpaid
\(K^{2b}\) choice.  There is likewise no hidden \(K^p\) loss in the
same-witness part: the sum over protected targets is already the left
side of (2.9).  The radius bound (1.8) is exactly what proves (1.6) for
geometrically close clusters; factorial pair codegrees pay the remaining
diameters.

In a later-time branch the two rows need not contain the original root
\(X\).  If their common-conflict witness is the same target \(Y\), recenter
(2.9) at \(Y\); estimate (1.6) is uniform in the protected target.  If the
two witnesses are distinct, the \(K^2\Delta_2\) term in (2.7) applies.
Thus the compression does not assume that an entire multigeneration core
lies in one original vertex link.

Contract the paid bundle and repeat.  This removes the entire two-core.
For a diagram with at most (2\ell) row occurrences, the number of
unlabelled forest/core patterns and all choices of bundle multiplicities
is at most

\[
 (C\ell)^{C\ell}.                                         \tag{2.10}
\]

Combining the tree factors and the core bundles gives the one-bite
normalized moment bound

\[
 (C\ell)^{C\ell}(mz)^{-j}                                 \tag{2.11}
\]

for the (2j)-th centered moment.  The same proof with one distinguished
row packet gives the conflict-neighborhood moment in (2.4).  The
edge-local energy (1.5) supplies its first centered branch; (1.6) supplies
every repeated branch.

#### Step 4: sum time labels rather than condition on a residual

Iterate the one-bite expansion from the original catalogue.  We never
condition on the realized residual.  A time-labelled tree of total scaled
length

\[
 u=s\gamma/K\le \log\log m+O(1).                           \tag{2.12}
\]

has total ordered-time weight at most \(u^b/b!\) when it has \(b\)
successive tree branches.  Summing \(b\ge0\) costs at most
\(e^{Cu}=(\log m)^C\) per rooted component.  A core bundle keeps the
time of its first nonforest incidence and is still paid by (2.9); it does
not regenerate an independent \(K^p\) choice.  Thus time iteration changes
the numerator in (2.11) only from \((C\ell)^{C\ell}\) to
\((C\ell\log m)^{C\ell}\).  This proves (2.3)--(2.4).

There is one truncation implicit in this resummation.  If one fixed row
pair is revisited more than \(L=C_0\log m\) times, its ordered time weight
is at most

\[
 \sum_{b>L}{(Cu)^b\over b!}
 \le \left({Ce\,u\over L}\right)^L
 \le \exp[-c\log m\log\log m].                            \tag{2.13}
\]

The same estimate applies when the total number of time-created core
births exceeds \(L\).  On the complementary histories the core has
\(O(\ell+L)=O(\log m)\) rows and hence \(O((\log m)^2)\) row pairs; this
polynomial factor is absorbed by the displayed exponential tail.  Every
bundle multiplicity then lies in the proved range of (1.6).  We take
\(C_0>100\), larger than all moment and truncation constants used here.

Equivalently, if \(M_j(s)\) denotes either normalized \(2j\)-th moment
after all tree components already exposed before round \(s\) are
resummed, the preceding leaf/core count gives the literal recurrence

\[
 M_j(s+1)
 \le (1+Cjq)M_j(s)
   +q(Cj)^{Cj}(mz_s)^{-j},\qquad
 M_j(0)\le(C/m)^{2j}.                                     \tag{2.14}
\]

Every new event column carries its marking factor \(p_s\); summing its
first row incidence changes \(p_s\rho_s\) into \(\gamma/K=q(1+o(1))\).
This is the factor \(q\) in (2.14).  Iteration uses
\(\sum_{r<s}q=\log(1/z_s)+O(q)\le\log\log m+O(1)\), giving

\[
 M_j(s)\le
 \left({(Cj\log m)^C\over mz_s}\right)^j,                 \tag{2.15}
\]

which is (2.3)--(2.4) for \(j=\ell\).  This recurrence records explicitly
that no estimate is assumed of a frozen residual.

This is the trajectory-specific step missing from a static residual
argument: all residual indicators have been expanded back into their
time-zero mark variables before (1.6) is applied.

#### Step 5: tails

For \(z\ge1/\log m\), Markov's inequality applied to (2.3) gives

\[
 \Pr\left(\left.
 \left|{d_s(X)\over\rho(z_s)}-1\right|>\varepsilon
 \,\right|\,X\text{ live}\right)
 \le
 \left[
 { (C\ell\log m)^C\over mz_s\varepsilon^2}
 \right]^\ell
 \le e^{-c\log m\log\log m}.                              \tag{2.16}
\]

Here \(\varepsilon=m^{-1/10}\), \(\ell=40\log m\), and the
polylogarithmic numerator is absorbed by
\(mz_s\varepsilon^2\ge m^{4/5}/\log m\).  The incidence statement follows
from (2.4) in the same way.  This proves (2.5) and the lemma. \(\square\)

## 3. Explicit slow-bite construction

Set

\[
 q=1-e^{-\gamma/K},
 \qquad z_s=(1-q)^s,
 \qquad \rho_s=Dz_s^{K-1}.                                \tag{3.1}
\]

Start with every vertex and every simple superpacket live.  At round
\(s\):

1. independently mark every currently live superpacket with probability
   \[
   p_s={\gamma\over K\rho_s};                              \tag{3.2}
   \]
2. retain a marked superpacket if it is disjoint from every other marked
   live superpacket;
3. add all retained superpackets to \(\mathcal M\), and remove every
   vertex belonging to any marked live superpacket.  A removed vertex not
   covered by a retained packet is charged to the collision-waste set
   \(\mathcal W\).

Retained packets in one round are disjoint from every other mark, and
later rounds use only vertices untouched by all previous marks.  Hence
\(\mathcal M\) is always a matching and is disjoint from
\(\mathcal W\).
The marking probabilities are deterministic functions of \(s\), so the
whole random mark table may be sampled at time zero.

Stop at the first \(S\) for which

\[
 z_S\le {1\over\log m}.                                    \tag{3.3}
\]

The number of rounds is explicit:

\[
 S=(1+o(1)){K\over\gamma}\log\log m
 =O(m^{11}\log\log m).                                    \tag{3.4}
\]

The degree at the stopping density is still enormous.  From Stirling,

\[
 \log\rho_S
 =2m\log m-4m\log\log m-O_a(m),                         \tag{3.5}
\]

so (3.2) is always a valid probability.

## 4. Coverage recurrence

Let \(U_s\) be the number of live vertices after round \(s\).  For a good
live vertex \(X\), Lemma 2.1 gives

\[
 d_s(X)=(1+O(\varepsilon))\rho_s.                          \tag{4.1}
\]

The marks on the \(d_s(X)\) incident live packets are independent.
Consequently the conditional survival probability of \(X\) is

\[
 (1-p_s)^{d_s(X)}
 =\exp\left[-{\gamma\over K}
       +O\left({\gamma\varepsilon\over K}
              +{\gamma^2\over K^2\rho_s}\right)\right]
 =(1-q)(1+O(q\varepsilon)).                               \tag{4.2}
\]

Bad live vertices have total expected fraction at most
\(e^{-c\log m\log\log m}\) by (2.5).  Averaging (4.2) therefore gives

\[
 \mathbb E U_{s+1}
 =(1-q+O(q\varepsilon))\mathbb E U_s
 +O\left(Ne^{-c\log m\log\log m}\right).                        \tag{4.3}
\]

Iterating through (3.4), and using

\[
 qS=\log\log m+o(1),
 \qquad
 \varepsilon qS=m^{-1/10}\log\log m=o(1),                \tag{4.4}
\]

while a polynomial number of rounds is swallowed by
\(e^{-c\log m\log\log m}\), yields

\[
 \mathbb E U_S=(1+o(1)){N\over\log m}.                    \tag{4.5}
\]

It remains to count unmatched vertices removed by colliding marks.  Let
\(W_s\) be the new collision waste in round \(s\).  For a marked live
packet \(F\), the probability that another live packet meeting it is
marked is at most \(p_sc_s(F)\).  Lemma 2.1(2), followed by incidence
double counting, gives

\[
 \mathbb E W_s
 \le (1+o(1)){N z_s\gamma^2\over K}
      +Ne^{-c\log m\log\log m}.                                  \tag{4.6}
\]

Since \(\sum_{s<S}z_s\le(1+o(1))/q=(1+o(1))K/\gamma\),

\[
 \mathbb E|\mathcal W|
 \le(1+o(1))\gamma N
 =o(N/\log m).                                             \tag{4.7}
\]

Equations (4.5) and (4.7) imply that some realization of the explicit
mark table has

\[
 U_S+|\mathcal W|\le {2N\over\log m}.                      \tag{4.8}
\]

Every vertex outside the selected matching is either still live or lies
in \(\mathcal W\).  Hence its matching leave is their disjoint union, and
(4.8) proves Theorem 0.1.

## 5. Exact synchronized repeat ledger

Write every selected superpacket as

\[
 Q(P)=E_R(P)\,\dot\cup\,E_R(P^\tau).                      \tag{5.1}
\]

Because the superpackets form an entrance matching, all (2T) ordinary
component packets are entrance-disjoint.

For every (2\le s\le n-2), the domino identity is

\[
 |E_s(P)\cap E_s(P^\tau)|=
 \begin{cases}
 n/2=m,&s\text{ even},\\
 0,&s\text{ odd}.
 \end{cases}                                              \tag{5.2}
\]

Since \(R\) is odd, \(R-d\) is even exactly when \(d\) is odd.  Fix such
an odd \(d\).  Every selected twin supplies \(m\) deeper targets with two
occurrences.  If one deeper target is supplied internally by \(s\)
selected twins, its multiplicity is at least (2s), and its repeat
contribution is at least (2s-1\ge s).  Summing over targets proves

\[
 E_{q_0+d}\ge mT.                                         \tag{5.3}
\]

Since \(KT=4mT=N-|\mathcal L|\), this is exactly (0.4), simultaneously
for every eligible odd \(d\); no independence between depths is used.

The total number of occurrences at depth \(d\) is

\[
 G_d=2nT=N-|\mathcal L|.                                  \tag{5.4}
\]

The unavoidable scalar repeat floor is
\((G_d-\binom n{R-d})_+\).  Subtracting it from (5.3) proves (0.5).

Finally, uniformly for \(d=o(\sqrt m)\),

\[
 {\binom n{R-d}\over N}
 =\exp\left[-{2q_0d+d^2\over m}
 +O_a(m^{-1/2}+d/m)\right].                               \tag{5.5}
\]

If \(d=o(\sqrt m/\log m)\), the loss in (5.5) is
\(o(1/\log m)\).  Whether or not \(G_d<\binom n{R-d}\), its scalar
floor is therefore bounded by

\[
 \left(G_d-\binom n{R-d}\right)_+
 \le \left(N-\binom n{R-d}\right)_+
 =o(N/\log m)=o(N).                                      \tag{5.6}
\]

Combining (5.6) with (0.5) proves (0.7).

## 6. Why the factorial hierarchy is used at the correct place

The construction does not make the false assertion that (1.6) is
hereditary for every residual.  Its chronology is:

\[
 \text{time-zero marks}
 \longrightarrow
 \text{history incidence diagram}
 \longrightarrow
 \text{tree peeling and factorial core compression}
 \longrightarrow
 \text{annealed degree/conflict moments}.                 \tag{6.1}
\]

The residual is never frozen and then treated as a new arbitrary
hypergraph.  In particular, a central-slice complement can still be an
edge-free residual; Lemma 2.1 says only that the prescribed random history
reaches such a residual with negligible annealed weight before
\(z=1/\log m\).

The three numerical inputs have distinct roles:

1. \(K\Delta_2/D=O(m^{-1})\) peels event-column trees;
2. \(\eta=O(m^{-1})\) pays the first conflict-coherence branch;
3. the radius bound \(4h+2\) and factorial estimate (1.6) pay every
   repeated two-core bundle without losing \(K^p\).

Maximum pair codegree alone would leave
\(K^2\Delta_2/D=\Theta(1)\) and
would not prove Lemma 2.1.

## 7. The exact square-root entropy barrier

It remains important not to misread Theorem 0.1 as an
\(o(N/\sqrt m)\) construction.  In the simple quotient,

\[
 \log D=2m\log m-(2+\log2)m+O_a(\log m).                  \tag{7.1}
\]

Under product thinning to density \(z\), the reference link degree is

\[
 D_z=Dz^{4m-1}.                                           \tag{7.2}
\]

At \(z=c/\sqrt m\),

\[
 \log D_z=(4\log c-2-\log2)m+O_a(\log m).                 \tag{7.3}
\]

Thus \(D_z\) is exponentially small already at \(c=1\).  More strongly,
the expected number of surviving simple superpackets in an independent
product residual is

\[
 |\mathcal Q|z^K={ND\over K}z^K,
\]

and

\[
 \log(|\mathcal Q|z^K)
 =(\log2-2+4\log c)m+o(m)                                 \tag{7.4}
\]

when \(z=c/\sqrt m\).  It tends to \(-\infty\) linearly whenever

\[
 c<\exp((2-\log2)/4),                                     \tag{7.5}
\]

and tends to \(-\infty\) superlinearly if \(c=o(1)\).
Markov's inequality then says that a product residual of density
\(o(m^{-1/2})\) contains no simple superpacket with probability
\(1-o(1)\).

Therefore an \(o(N/\sqrt m)\) matching leave cannot be reached by merely
extending the annealed quasirandom trajectory.  It requires a deliberately
nonproduct final absorber.  The present theorem settles the alternative
requested route: an explicit entrance near-factor with \(o(N)\) leave and
a synchronized linear repeat excess on a growing depth window.

## 8. Final quantitative ledger

The construction supplies

\[
 |\mathcal L|=O(N/\log m)=o(N),                            \tag{8.1}
\]

\[
 |\mathcal M|={N\over4m}(1-o(1)),                         \tag{8.2}
\]

and, simultaneously at all odd
\(d=o(\sqrt m/\log m)\),

\[
 \widetilde E_{q_0+d}\ge(1/4-o(1))N.                     \tag{8.3}
\]

In particular the first deeper layer already has linear corrected repeat
excess.  The same selected family realizes the obstruction coherently at
an unbounded number of further odd depths.  This conclusion is integral,
uses simple superpackets rather than parallel anchored copies, and is
obtained without any fixed-uniformity matching theorem.
