# Laminar ports: exact target regularity, off-edge star sparsity, and the layered Hall gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Outcome

Put

\[
 W=\binom{2m}m,\qquad N_q=\binom{2m}{m-q},
 \qquad 1\le H<h=o(m),
\]

and let \(\mathscr C_{m,h}\) be the complete physical cyclic
\(C_{2h}\)-strip catalogue.  The integral port theorem in
`MATH_THEOREM_FINE_STRIP_INTEGRAL_PORT_SPARSIFICATION_AND_ANNULUS_MATCHING_GATE_20260726.md`
balances the number of ports separately on every strip.  That balance is
useful but is not required either for exact target degrees or for the
annulus matching compiler.

This note proves a different port theorem.  Assume, for definiteness,

\[
 H=\sqrt m\,m^{o(1)},\qquad
 h=m^{2/3+o(1)},\qquad H/h=o(1),                    \tag{0.1}
\]

where the subpolynomial factors are such that \(H=o(h)\).  There are
integral ports for which

1. every signed nonmiddle target has degree exactly \(D_1\);
2. every port edge has width \(O(h\sqrt m)\); and
3. for every target \(S\) and every physical strip \(E\) whose selected
   port edge does not contain \(S\), only

   \[
   O\!\left({1\over m}+{h\over m^{3/2}}\right)D_1=o(D_1)           \tag{0.2}
   \]

   selected strips through \(S\) can meet the selected edge of \(E\).

The point of (0.2) is that the critical \(D_1/m\) codegrees occur only
along nested comparable flags.  A fixed strip contains only
\(O(d+1)\) targets comparable to a fixed target at rank gap \(d\).
Every noncomparable pair pays two independent coordinate choices and has
relative codegree \(O(m^{-2})\).  Summing the actual selected-port
profile gives (0.2),
whereas multiplying the maximum codegree by the full port width gives the
false scale \(h/\sqrt m\).

This is a genuine flag-aware sparsification theorem, but it does **not**
prove the annulus matching statement.  Two exact residual formulations are
proved:

* a quantitative fractional edge-colouring criterion with required error
  \(o(m^{-1/2})\), not merely \(o(1)\); and
* a strictly weaker layered Hall criterion which dispenses with global
  port completion altogether.

The second formulation exposes the remaining obstruction precisely.  Once
a critical three-layer strip matching is fixed, every later rank is a
capacitated bipartite matching problem.  Its exact deficiency is

\[
 \max_{\mathcal A\subseteq\mathcal F}
 \left(\sum_{C\in\mathcal A}b_C-|N_q(\mathcal A)|\right)_+.        \tag{0.3}
\]

The flag chains inside one strip are nested, but the row supports in
(0.3) cross.  Thus total unimodularity of each individual chain does not
settle the joint Hall cuts.  This is the sharp surviving gate.

## 1. Physical strips and pair orbits

A physical strip has a core \(K\), \(|K|=m-h\), and a cyclically ordered
active set

\[
 z_0,z_1,\ldots,z_{2h-1}.
\]

At signed rank \(m+a\), \(-H\le a\le H\), its targets are

\[
 K\cup I_z(t,h+a),\qquad t\in\mathbb Z_{2h}.                         \tag{1.1}
\]

For a fixed target \(S\), \(|S|=m+a\), the number of strips through it is

\[
 D_a={ (m+a)!(m-a)!\over2(m-h)!^2}.                                  \tag{1.2}
\]

For another target \(T\), \(|T|=m+b\), put

\[
 i=|S\setminus T|,\qquad j=|T\setminus S|;qquad j-i=b-a.             \tag{1.3}
\]

The stabilizer of \(S\) is transitive on the targets with parameters
\((i,j)\), and that orbit has size

\[
 \mathcal O_{a,b}(i,j)
 =\binom{m+a}{i}\binom{m-a}{j}.                                      \tag{1.4}
\]

### Lemma 1.1 (cyclic pair multiplicity)

Let \(n_{a,b}(i,j)\) be the number of signed rank-\(b\) targets in one
strip through \(S\) which have parameters \((i,j)\) relative to \(S\).
Then

\[
 {d(S,T)\over D_a}
 ={n_{a,b}(i,j)\over
   \binom{m+a}{i}\binom{m-a}{j}}.                                   \tag{1.5}
\]

Moreover:

1. if \(i=0\) or \(j=0\), and \(d=|a-b|\), then

   \[
   n_{a,b}(i,j)=d+1;                                                   \tag{1.6}
   \]

2. if \(i,j>0\) and the two active intervals overlap, then

   \[
   n_{a,b}(i,j)\le2;                                                   \tag{1.7}
   \]

3. the remaining, active-disjoint, case has \(i\ge h-H\) and
   \(j\ge h-H\), and hence

   \[
   {d(S,T)\over D_a}
   \le 2h\left({h+H\over m-H}\right)^{2(h-H)}.                       \tag{1.8}
   \]

#### Proof

Double-count the pairs consisting of a strip through \(S\) and one of its
rank-\(b\) targets in the orbit (1.4).  The stabilizer transitivity gives
(1.5).

Inside a fixed strip through \(S\), remove the common core.  The two
targets become cyclic intervals of lengths \(h+a\) and \(h+b\) in a
\(2h\)-cycle.  An interval longer by \(d\) contains the shorter interval
in exactly \(d+1\) positions, proving (1.6).  If neither interval contains
the other and they overlap, their intersection size determines the second
start in at most the clockwise and counterclockwise positions, proving
(1.7).  If their active parts are disjoint, both differences have size at
least \(h-H\).  Use

\[
 \binom nk\ge(n/k)^k
\]

in (1.5), together with the trivial numerator \(n_{a,b}\le2h\), to obtain
(1.8). \(\square\)

## 2. A raw one-star interaction bound

For a target \(S\) and a physical strip \(E\), let

\[
 \Gamma_S^{\rm raw}(E)
 =\{C:S\in\mathcal T_H(C),\ 
   (\mathcal T_H(C)\cap\mathcal T_H(E))\setminus\{S\}
          \ne\varnothing\}.                                        \tag{2.1}
\]

### Lemma 2.1 (few comparable targets on one strip)

Fix \(S\) of rank \(m+a\).  At a rank gap \(d\ge1\), a physical strip
contains at most \(2(d+1)\) targets comparable with \(S\).

#### Proof

Consider first supersets of \(S\).  After deleting the strip core, every
candidate is a cyclic interval of a fixed length, containing a fixed
subset with at most \(d\) unused positions.  The allowed starting points
form at most two cyclic intervals of total length at most \(2(d+1)\).
For subsets of \(S\), decompose \(S\) minus the core into runs around the
active circle.  If the desired interval length is \(L\) and the available
set has size at most \(L+d\), the number of contained \(L\)-windows is

\[
 \sum_r (|r|-L+1)_+\le d+1.
\]

The same harmless factor two covers both cyclic orientations. \(\square\)

### Theorem 2.2 (raw flag-aware star bound)

Uniformly for \(|a|\le H\), every target \(S\), and every physical strip
\(E\),

\[
 \boxed{
 { |\Gamma_S^{\rm raw}(E)|\over D_a}
 \le
 C\left({1\over m}+{hH\over m^2}\right)
 +8h^2H\left({h+H\over m-H}\right)^{2(h-H)}.}                       \tag{2.2}
\]

In the range (0.1), the right side is

\[
 \rho_m=O\!\left(m^{-1}+m^{-5/6+o(1)}\right)=o(1).                  \tag{2.3}
\]

#### Proof

Use the union bound over the raw targets \(T\ne S\) of \(E\):

\[
 |\Gamma_S^{\rm raw}(E)|
 \le\sum_{T\in\mathcal T_H(E)}d(S,T).                               \tag{2.4}
\]

For comparable pairs at gap \(d\), Lemmas 1.1 and 2.1 give total
normalized contribution at most

\[
 4{(d+1)^2\over\binom{m-H}{d}}.                                     \tag{2.5}
\]

Summing (2.5) for \(1\le d\le2H=o(m)\) is \(O(m^{-1})\): the
\(d=1\) term has this order and the remaining binomial denominators grow
geometrically.

For noncomparable overlapping pairs, (1.4) has both \(i,j\ge1\), so
(1.7) gives at most \(2/(m-H)^2\) per target.  The raw strip has at most
\(2h(2H+1)\) targets.  This contributes \(O(hH/m^2)\).  Finally apply
(1.8) to the at most \(2h(2H+1)\) active-disjoint targets.  Enlarging the
absolute constant gives (2.2). \(\square\)

The proof is the precise sense in which the large codegrees are laminar:
the \(m^{-1}\) pair scale can occur only in the summable comparable
sequence (2.5).  The \(\Theta(hH)\) remaining vertices see only the
\(m^{-2}\) pair scale.

The raw estimate has an immediate selected-set refinement.  If
\(\mathcal P\subseteq\mathcal T_H(E)\setminus\{S\}\) has
\(|\mathcal P|\le K\), then the same proof, summing the comparable
sequence over all ranks but the noncomparable contribution only over
\(\mathcal P\), gives

\[
 {1\over D_a}
 \left|\{C:S\in\mathcal T_H(C),\ 
              \mathcal T_H(C)\cap\mathcal P\ne\varnothing\}\right|
 \le C\left({1\over m}+{K\over m^2}\right)
 +2hK\left({h+H\over m-H}\right)^{2(h-H)}.             \tag{2.6}
\]

## 3. Two locally sparse integral port systems

We first retain all the rankwise degree conclusions of the original TU
port theorem.

### Lemma 3.1 (bipartite dependent rounding)

Let \(G=(L,R;E)\) be bipartite and let \(x\in[0,1]^E\).  There is a
random integral vector \(X\in\{0,1\}^E\) such that

1. \(\mathbb E X_e=x_e\) for every edge;
2. every vertex degree is either the floor or the ceiling of its
   fractional degree (and hence is exact when that degree is integral);
3. for every vertex \(v\), every \(A\subseteq\delta(v)\), and every
   \(t>0\), the sum \(\sum_{e\in A}X_e\) obeys the usual Chernoff upper
   tail with mean \(\sum_{e\in A}x_e\).

#### Proof sketch

While fractional edges remain, take a maximal alternating path or cycle
of fractional edges.  Move alternately by \(+\alpha,-\alpha\), or by the
opposite signed vector, until one coordinate reaches \(0\) or \(1\), and
choose the two moves with probabilities preserving every coordinate
expectation.  Internal vertex sums are fixed; only path endpoints can
change, always inside their original floor/ceiling interval.  Iteration
proves 1--2.  For a fixed star, the two fractional coordinates affected
in one move have opposite signs.  Expanding the elementary symmetric
polynomials shows that every upper cylinder
\(\mathbb E\prod_{e\in A}X_e\) is at most
\(\prod_{e\in A}x_e\).  The exponential-moment proof of Chernoff's
inequality then gives 3.  This is the standard alternating-path proof of
bipartite dependent rounding. \(\square\)

### Theorem 3.2 (balanced ports with local star sparsity)

There are port systems satisfying the exact target degree and the
rankwise strip floor/ceiling conditions of Theorem 2.1 in the original
annulus-matching note, and also

\[
 |\{C:S\in e_C^\#,\ e_C^\#\cap e_E^\#\ne\varnothing\}|
 \le2\rho_mD_1                                                   \tag{3.1}
\]

whenever the selected edge of \(E\) does not contain \(S\).  Here
\(\rho_m\) is the raw bound (2.2).

#### Proof

At each signed depth \(q\), apply Lemma 3.1 to the constant fractional
incidence vector

\[
 x_{C,T}=\theta_q={D_1\over D_q}={N_q\over N_1}.
\]

Every target degree is the integer \(D_q\theta_q=D_1\), while every
strip degree is rounded to
\(\lfloor2h\theta_q\rfloor\) or
\(\lceil2h\theta_q\rceil\).  This is exactly the original port system.

Fix \(S,E\).  The selected incidences through \(S\) which can meet the
selected edge of \(E\) are contained in the raw exceptional set
\(\Gamma_S^{\rm raw}(E)\), of size at most \(\rho_mD_a\).  Lemma 3.1(3)
gives mean at most

\[
 \theta_a\rho_mD_a=\rho_mD_1
\]

and failure probability \(\exp[-\Omega(\rho_mD_1)]\) for the bound
(3.1).  The degree \(D_1\) is exponential in \(h\log m\), whereas the
logarithm of the number of target--strip pairs is \(O(m\log m)\).
Hence a union bound fixes all pairs simultaneously.  At depth one the
rounding is the all-one vector, and middle incidences are unthinned, so
the same conclusion follows directly from (2.2). \(\square\)

This theorem is directly compatible with the original
\((\mathrm{AM}_{m,H,h})\).  The following alternative drops the
rank-by-rank strip balance and improves \(\rho_m\) by summing only over
ports actually present on \(E\).

### Exact target-regular independent ports

For every signed target \(T\) at depth \(q\ge1\), independently choose a
uniform \(D_1\)-subset of the \(D_q\) physical strips containing \(T\).
Declare precisely those incidences to be ports.  At depth one this selects
every incidence.

This differs from the rankwise TU construction: target degrees are exact,
but individual strip degrees are not prescribed rank by rank.

### Theorem 3.3 (simultaneous width and sharper star sparsity)

In the range (0.1), some outcome of the preceding experiment satisfies
simultaneously:

\[
 \deg(T)=D_1\qquad\text{for every nonmiddle target }T,                \tag{3.2}
\]

\[
 |e_C^\#|\le C_0h\sqrt m\qquad(C\in\mathscr C_{m,h}),                \tag{3.3}
\]

and, for every target \(S\) and every physical strip \(E\) whose selected
port edge does not contain it,

\[
 \boxed{
 |\{C:S\in e_C^\#,\ e_C^\#\cap e_E^\#\ne\varnothing\}|
 \le 2\widehat\rho_mD_1,}                                            \tag{3.4}
\]

where

\[
 \widehat\rho_m
 =C\left({1\over m}+{h\over m^{3/2}}\right)
 +O(h^2\sqrt m)\left({h+H\over m-H}\right)^{2(h-H)}
 =m^{-5/6+o(1)}.                                      \tag{3.5}
\]

Middle targets in (3.4)
are interpreted as always selected and have degree
\(D_0=(N_1/W)D_1\).

#### Proof

Equation (3.2) holds by construction.  For a fixed strip, its number of
ports is a sum of independent Bernoulli variables, because distinct
physical targets make their choices independently.  Its mean is

\[
 4h\sum_{q=1}^H{D_1\over D_q}
 =4h\sum_{q=1}^H{N_q\over N_1}=\Theta(h\sqrt m).                     \tag{3.6}
\]

Here the lower bound follows already from \(q\le\sqrt m\), while the
upper bound is the Gaussian binomial sum.  Chernoff's inequality gives a
tail \(\exp[-\Omega(h\sqrt m)]\).  Since

\[
 \log|\mathscr C_{m,h}|=O(m\log m)=o(h\sqrt m)                       \tag{3.7}
\]

in (0.1), a union bound proves (3.3).

Fix now \(S,E\), with \(|S|=m+a\ne m\), and expose all port choices at
targets other than \(S\).  On the width event just proved, the selected
target set of \(E\), away from \(S\), has size at most
\(C_0h\sqrt m\).  Equation (2.6) says that at most
\(\widehat\rho_mD_a\) raw strips through \(S\) meet that selected set.
Because the selected edge of \(E\) does not contain \(S\), conditioning
also on that event leaves a uniform \(D_1\)-subset of the other
\(D_a-1\) strips (or the unconditioned uniform subset when \(E\) does not
raw-contain \(S\)).  The number falling in the exceptional set is
hypergeometric with mean at most
\((1+o(1))\widehat\rho_mD_1\), and hence exceeds
\(2\widehat\rho_mD_1\) with probability at most

\[
 \exp[-\Omega(\widehat\rho_mD_1)].                                  \tag{3.8}
\]

The degree

\[
 D_1={(m+1)!(m-1)!\over2(m-h)!^2}
\]

is exponential in \(h\log m\), so (3.8) survives a union bound over all
target--strip pairs.  A selected intersection with \(e_E^\#\) is in
particular an intersection with the selected target set just used,
proving (3.4).  For a middle \(S\), no thinning is needed and (2.6)
applies directly; \(D_0\le D_1\).  The bad width events and bad star
events have summable union bounds, so one outcome avoids all of them.
\(\square\)

Thus the full port hypergraph is not merely low-codegree.  It satisfies
the stronger off-edge-star condition (3.4), with the high codegrees
already summed along their actual nested flags.

## 4. A quantitative fractional edge-colouring criterion

Let

\[
 V_*=2\sum_{q=1}^HN_q=O(\sqrt m\,W)                                  \tag{4.1}
\]

be the number of nonmiddle target vertices in the audited band.

### Theorem 4.1 (fractional colouring implies the annulus compiler)

Let \(\mathcal H^\#\) be any target-regular port hypergraph with every
nonmiddle degree \(D_1\).  Suppose there is a probability distribution on
ordinary matchings \(\mathcal M\) such that every port hyperedge satisfies

\[
 \Pr(e_C^\#\in\mathcal M)
 \ge {1\over(1+\varepsilon_m)D_1},
 \qquad \varepsilon_m=o(m^{-1/2}).                                  \tag{4.2}
\]

Then some matching has nonmiddle leave \(o(W)\).  The proof of the
annulus matching compiler applies verbatim and gives coefficient one.
This is a relaxed port version of \((\mathrm{AM}_{m,H,h})\): it retains
the exact target degrees and uniform total edge width, but does not require
the auxiliary rank-by-rank floor/ceiling degree condition on every strip.

Equivalently, it is sufficient that

\[
 \chi_f'(\mathcal H^\#)
 \le(1+o(m^{-1/2}))D_1.                                               \tag{4.3}
\]

The stronger integral condition

\[
 \chi'(\mathcal H^\#)
 \le D_1+o(D_1/\sqrt m)                                               \tag{4.4}
\]

also suffices.

#### Proof

Edges through a fixed target are mutually incompatible, so their inclusion
events in one matching are disjoint.  From (4.2), every nonmiddle target is
covered with probability at least \((1+\varepsilon_m)^{-1}\).  Therefore
the expected nonmiddle leave is at most

\[
 {\varepsilon_m\over1+\varepsilon_m}V_*=o(W).                         \tag{4.5}
\]

Some matching attains at most its expectation.  The equivalence with
fractional edge colouring is the standard normalization of a nonnegative
combination of matching indicators.  For (4.4), choose a uniformly random
colour class. \(\square\)

The rate in (4.3) is important.  A qualitative
\((1+o(1))D_1\) edge-colouring leaves only \(o(V_*)\), which may still be
\(\omega(W)\).  The Gaussian annulus needs an error smaller by a further
factor \(\sqrt m\).

## 5. A strictly weaker layered Hall criterion

Global port completion is not necessary for the literal strip compiler.
The following criterion works only with the selected strips.

Let \(\mathcal F\) be a matching on the middle and the two signed
depth-one layers.  At signed depth \(q\ge2\), form the bipartite graph

\[
 B_q^\epsilon(\mathcal F)
 \subseteq
 \mathcal F\times\binom{[2m]}{m+\epsilon q},                         \tag{5.1}
\]

where \(C\sim T\) when \(T\) is a physical target of \(C\).  Give each
strip an integer demand \(0\le b_{C,q}^\epsilon\le2h\), and put

\[
 B_q^\epsilon=\sum_{C\in\mathcal F}b_{C,q}^\epsilon.                 \tag{5.2}
\]

The maximum number of distinct targets assignable to strip occurrences,
subject to those strip demands, is

\[
 B_q^\epsilon-\operatorname {def}_q^\epsilon,
\]

where max-flow/min-cut gives the exact deficiency

\[
 \boxed{
 \operatorname {def}_q^\epsilon
 =\max_{\mathcal A\subseteq\mathcal F}
 \left(\sum_{C\in\mathcal A}b_{C,q}^\epsilon
       -|N_q^\epsilon(\mathcal A)|\right)_+.}                        \tag{5.3}
\]

### Theorem 5.1 (layered Hall annulus compiler)

Suppose \(H/h=o(1)\), and there are \(\mathcal F\) and demands as above
such that

\[
 W-2h|\mathcal F|=o(W),                                               \tag{5.4}
\]

the middle and signed depth-one leave is \(o(W)\), and

\[
 \sum_{q=2}^H\sum_{\epsilon=\pm}
 \left[
  (N_q-B_q^\epsilon)_+
  +\operatorname {def}_q^\epsilon
 \right]=o(W).                                                       \tag{5.5}
\]

Then the physical strips in \(\mathcal F\), followed by literal singleton
repair, give a word of length \(W+o(W)\) covering the central band.

#### Proof

At each signed depth, the integral bipartite max-flow associated with
(5.3) assigns \(B_q^\epsilon-\operatorname {def}_q^\epsilon\) distinct
targets to physical occurrences of the selected strips.  Hence the actual
hole count is at most the bracket in (5.5).  The critical and middle holes
are covered by hypothesis.

Literalize every selected strip in \(2h+2H\) letters and append every
hole as a singleton.  The length is

\[
 (2h+2H)|\mathcal F|+\bigl(W-2h|\mathcal F|\bigr)+o(W)
 =W+{H\over h}\,2h|\mathcal F|+o(W)=W+o(W),                           \tag{5.6}
\]

using (5.4), \(2h|\mathcal F|\le W\), and \(H/h=o(1)\). \(\square\)

This is strictly weaker than completing the chosen incidences to global
degree-\(D_1\) port systems and then finding one matching in that completed
hypergraph.  It isolates exactly what an iterative-rank proof must show.

## 6. Why prefix laminarity does not settle (5.3)

For one strip and one phase, the lower targets

\[
 L_t^1\supset L_t^2\supset\cdots\supset L_t^H
\]

form a chain, and the upper targets form the reverse chain.  This is
laminarity in the **Boolean-coordinate ground set**.  Hall deficiency
(5.3), however, is controlled by the row supports

\[
 \{C\in\mathcal F:T\in\mathcal T_H(C)\}
\]

as subsets of the strip catalogue.  Those supports cross already on three
middle targets: the physical strip incidence matrix contains

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},                                                          \tag{6.1}
\]

whose determinant is two.  Adding longer nested flags to the three
columns preserves this crossing minor.  Thus neither the consecutive-ones
property inside one column nor total unimodularity of one flag chain
implies the Hoffman cuts (5.3).

Theorem 3.1 rules out a maximum-codegree explanation of the difficulty:
after exact target-regular sparsification, every off-edge star meets a
fixed edge in only \(o(D_1)\) possible strips.  What remains is genuinely
global: prove either the quantitative fractional-colouring bound (4.3),
or construct one critical matching whose aggregate layered Hall deficiency
(5.5) is \(o(W)\).

## 7. Exact frontier

Proved in this note:

1. the cyclic pair multiplicity and rank-stratified pair bounds;
2. the raw off-edge-star estimate (2.2);
3. balanced AM-compatible ports with (3.1), and exact target-regular
   relaxed ports with uniformly \(O(h\sqrt m)\) width and the sharper
   local star property (3.4);
4. the sharp quantitative fractional edge-colouring implication (4.3);
5. the exact layered Hall deficiency (5.3); and
6. the layered Hall annulus compiler, Theorem 5.1.

Not proved:

1. \(\chi_f'(\mathcal H^\#)\le(1+o(m^{-1/2}))D_1\);
2. the aggregate Hall bound (5.5) for one critical strip matching; or
3. either the original \((\mathrm{AM}_{m,H,h})\) or its target-regular
   relaxed-port version used in Theorem 4.1.

Accordingly, high codegrees have been removed as a local obstruction, but
the matching theorem itself remains open.  A successful flag-aware nibble
must control the crossing row supports, not merely the nested geometry
inside each physical strip.
