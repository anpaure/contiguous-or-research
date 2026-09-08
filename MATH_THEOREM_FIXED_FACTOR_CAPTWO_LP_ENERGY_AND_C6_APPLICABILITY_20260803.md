# Fixed-factor cap-two LP, exact switch energy, and the occupied-hexagon obstruction

**Date:** 2026-08-03  
**Status:** unconditional fractional theorem, exact integral/rainbow
reduction, exact alternating-switch identity, and a scoped obstruction to a
potential-hexagon descent argument. No computation is used. This note does
not prove that every Boolean fixed factor has a cap-two second factor.

## 0. Outcome

Use the notation of
MATH_THEOREM_FIXED_FACTOR_FUNCTIONAL_DIGRAPH_STEINER_PARITY_AND_C6_20260803.md.
Thus \(H=G-F_0\) is \((m-1)\)-regular on the tail and head copies of
\(\mathcal M\), and its arcs are partitioned into functional upper-colour
classes

\[
                         E(H)=\mathop{\dot\bigcup}_{R\in\mathcal U}E_R,
 \qquad |E_R|=m+1.
\tag{0.1}
\]

Write \(d=m-1\). The cap-two cycle-cover polytope is

\[
\begin{aligned}
\mathcal P_{\rm cap}=\{x\in\mathbb R_{\ge0}^{E(H)}:\quad
 &x(\delta^+(S))=1 &&(S\in\mathcal M),\\
 &x(\delta^-(T))=1 &&(T\in\mathcal M),\\
 &1\le x(E_R)\le2 &&(R\in\mathcal U)\}.
\end{aligned}
\tag{0.2}
\]

The canonical point

\[
                              x_e={1\over m-1}
\tag{0.3}
\]

belongs to \(\mathcal P_{\rm cap}\) for every fixed factor \(F_0\). Thus
the relaxation consisting of the rows in (0.2) has no feasibility
separator.  This does not exclude stronger valid inequalities.  An
integral point of (0.2) is exactly the required cap-two second perfect
matching.

There are three further exact conclusions.

1. A cap-two second factor is equivalently a rainbow one-per-colour
   matching followed by a vertex-disjoint rainbow residual completion.
2. If \(F\) is a second perfect matching, \(\mu_R=|F\cap E_R|\), and an
   alternating-cycle switch changes the colour vector by \(\delta\), then

   \[
   \boxed{\Delta(F')-\Delta(F)
   =\sum_R\mu_R\delta_R+\frac12\sum_R\delta_R^2.}
   \tag{0.4}
   \]

3. The cubic supply of full Boolean hexagons is only a potential supply.
   At a fixed rank-\((m-2)\) core, an incumbent second matching occupies at
   most \(\lfloor(m+1)/3\rfloor\) hexagon phases.  The local pointer axioms
   admit zero occupied phases, although no globally extendable Boolean
   factor pair with that local state is asserted.  Hence the
   \(\Omega(m^3)\) support count alone cannot prove energy descent.

The exact missing local statement is now a defect-routing assertion:
whenever \(\Delta(F)>0\), find an occupied alternating cycle for which the
right-hand side of (0.4) is strictly negative.

## 1. Canonical fractional feasibility

### Theorem 1.1

The point (0.3) belongs to (0.2). Moreover

\[
 x(E_R)={m+1\over m-1}=1+{2\over m-1}
\tag{1.1}
\]

for every upper colour, and

\[
 \sum_{R\in\mathcal U}\bigl(x(E_R)-1\bigr)
 =|\mathcal M|-|\mathcal U|
 =\operatorname{Cat}_m.
\tag{1.2}
\]

### Proof

Every tail and every head has degree \(m-1\) in \(H\), so (0.3) gives both
unit equations in (0.2). Every functional colour class has \(m+1\) arcs,
which proves (1.1); this lies in \([1,2]\) for \(m\ge3\).

Finally,

\[
 {|\mathcal M|\over|\mathcal U|}
 ={m+1\over m-1},
\]

so

\[
 |\mathcal M|-|\mathcal U|
 ={2\over m-1}|\mathcal U|.
\]

Summing the excess in (1.1) gives (1.2). \(\square\)

Thus any proof based only on the linear tail, head, and colour-cap rows has
already succeeded fractionally. The remaining question is the integrality
of their three-way intersection.

## 2. Exact two-stage rainbow decomposition

Call a matching rainbow when it uses every upper colour at most once.

### Theorem 2.1 (base plus duplicate completion)

The following are equivalent.

1. \(H\) has a perfect matching \(F\) with
   \(1\le|F\cap E_R|\le2\) for every \(R\).
2. There are vertex-disjoint matchings \(Q,P\subseteq H\) such that
   * \(Q\) contains exactly one arc of every upper colour;
   * \(P\) is rainbow;
   * \(Q\cup P\) is a perfect matching.

In every such decomposition,

\[
 |Q|=|\mathcal U|,
 \qquad
 |P|=|\mathcal M|-|\mathcal U|=\operatorname{Cat}_m,
\tag{2.1}
\]

and the colour set of \(P\) is exactly the duplicate-colour design.

### Proof

Given \(F\), choose one of its arcs from every upper colour and call their
set \(Q\). It is a matching because \(Q\subseteq F\). Put \(P=F-Q\).
Since no colour occurs more than twice in \(F\), \(P\) is rainbow. The
cardinalities follow from the number of colours and the size of a perfect
matching.

Conversely, \(Q\cup P\) is a perfect matching by hypothesis. Every colour
appears once in \(Q\) and at most once more in \(P\), proving the cap-two
condition. \(\square\)

This theorem is stronger than the two separate marginal SDRs. The first
stage must be one actual tail-head matching, and the second stage must be a
rainbow perfect matching of the residual tail/head vertices.

## 3. Exact energy change on an alternating cycle

For a perfect matching \(F\), put

\[
 \mu_R=|F\cap E_R|,
 \qquad
 f(z)={(z-1)(z-2)\over2},
 \qquad
 \Delta(F)=\sum_R f(\mu_R).
\tag{3.1}
\]

Let \(Z\) be an \(F\)-alternating cycle in \(H\), and put
\[
 F'=F\mathbin{\triangle}Z.
\]
For every upper colour define

\[
 \delta_R
 =|(Z-F)\cap E_R|-|(Z\cap F)\cap E_R|.
\tag{3.2}
\]

### Theorem 3.1 (discrete quadratic switch identity)

Equation (0.4) holds. In particular, if the removed and inserted colour
sets are disjoint and each has size \(\ell\), then

\[
 \Delta(F')-\Delta(F)
 =\sum_{\text{inserted }R}\mu_R
  -\sum_{\text{removed }R}\mu_R+\ell.
\tag{3.3}
\]

### Proof

Since an alternating cycle removes and inserts the same number of edges,
\(\sum_R\delta_R=0\). Also

\[
\begin{aligned}
 f(\mu_R+\delta_R)-f(\mu_R)
 &=\mu_R\delta_R+\frac{\delta_R^2-3\delta_R}{2}.
\end{aligned}
\]

Sum over \(R\); the linear \(-3\delta_R/2\) terms cancel. This gives
(0.4). Under the hypothesis of (3.3), every nonzero \(\delta_R\) is
\(+1\) or \(-1\), and there are \(2\ell\) of them. Substitution gives
(3.3). \(\square\)

The identity is valid with repeated or overlapping upper colours; their
signed contributions must first be consolidated into \(\delta\).

## 4. Specialization to a full Boolean hexagon

Fix a core \(C\in\binom{[n]}{m-2}\), put
\(A=[n]\setminus C\), and write

\[
 f_C(a)=x_a.
\]

For a full supported triple \(\{a,b,c\}\), the old and new colour sets of
the two hexagon phases are

\[
\begin{aligned}
\mathcal O&=\{C+ab+x_a,\ C+bc+x_b,\ C+ac+x_c\},\\
\mathcal N&=\{C+ac+x_a,\ C+ab+x_b,\ C+bc+x_c\}.
\end{aligned}
\tag{4.1}
\]

Full support implies \(x_a,x_b,x_c\notin\{a,b,c\}\). Consequently the
three members of \(\mathcal O\) are distinct, as are the three members of
\(\mathcal N\). The only possible old-new coincidences are

\[
\begin{array}{lll}
C+ab+x_a=C+ab+x_b&\Longleftrightarrow&x_a=x_b,\\
C+bc+x_b=C+bc+x_c&\Longleftrightarrow&x_b=x_c,\\
C+ac+x_c=C+ac+x_a&\Longleftrightarrow&x_c=x_a.
\end{array}
\tag{4.2}
\]

Put

\[
 \kappa=|\mathcal O\cap\mathcal N|.
\]

### Corollary 4.1 (exact hexagon descent test)

For an occupied switch from the old phase to the new phase,

\[
\boxed{
\Delta(F')-\Delta(F)
=\sum_{R\in\mathcal N\setminus\mathcal O}\mu_R
 -\sum_{R\in\mathcal O\setminus\mathcal N}\mu_R
 +(3-\kappa).}
\tag{4.3}
\]

It is a strict descent exactly when

\[
 \sum_{R\in\mathcal O\setminus\mathcal N}\mu_R
 -\sum_{R\in\mathcal N\setminus\mathcal O}\mu_R
 \ge4-\kappa.
\tag{4.4}
\]

In particular, if the switch is nontrivial, every inserted colour is
missing, and every removed colour has multiplicity at least two, then

\[
                         \Delta(F')-\Delta(F)\le-(3-\kappa).
\tag{4.5}
\]

### Proof

Cancel the common colours in (4.1). The remaining old and new sets each
have size \(3-\kappa\), and their signed changes are respectively \(-1\)
and \(+1\). Formula (4.3) is (3.3), and integrality gives (4.4). Under the
last hypothesis, the inserted sum is zero and the removed sum is at least
\(2(3-\kappa)\), giving (4.5). \(\square\)

Thus a full hexagon is not automatically beneficial: its direction is
controlled by the *current global multiplicities* in (4.3).

## 5. Potential supports versus occupied phases

Let \(F\subseteq H\) be the incumbent second perfect matching. For the same
core \(C\) and every \(a\in A\), define \(g_C(a)\in A-\{a\}\) by

\[
                         F(C+a)=C+a+g_C(a).
\tag{5.1}
\]

Because \(F\subseteq H\),

\[
                         g_C(a)\ne f_C(a).
\tag{5.2}
\]

### Theorem 5.1 (occupied-hexagon characterization)

A full supported triple \(\{a,b,c\}\) carries one of the two alternating
phases of \(F\) exactly when its restriction under \(g_C\) is one of the
directed cycles

\[
 a\longmapsto b\longmapsto c\longmapsto a,
 \qquad\text{or}\qquad
 a\longmapsto c\longmapsto b\longmapsto a.
\tag{5.3}
\]

Consequently, at one core,

\[
 \#\{\text{occupied full }C_6\text{ supports}\}
 \le\left\lfloor{m+1\over3}\right\rfloor.
\tag{5.4}
\]

The local pointer conditions (5.1)--(5.2) admit zero directed
\(3\)-cycles even when the potential-support lower bound is
\(\Omega(m^3)\).  This does not by itself assert the existence of a global
Boolean factor pair realizing that local state.

### Proof

The first phase uses the three matching edges
\[
 (C+a,C+ab),\quad(C+b,C+bc),\quad(C+c,C+ca),
\]
which is equivalent to
\(g_C(a)=b,g_C(b)=c,g_C(c)=a\). The other phase gives the reverse directed
cycle. Conversely either directed cycle places exactly one of the two
phases in \(F\); full support ensures that all three complementary phase
edges also belong to \(H\).

Directed cycles of one functional digraph are vertex-disjoint. Each
occupied hexagon consumes a directed \(3\)-cycle, proving (5.4).

For the final assertion, take \(m\ge7\) and, on
\(A=\mathbb Z/(m+1)\mathbb Z\), put locally
\[
 g_C(a)=a+1,\qquad f_C(a)=a+2.
\tag{5.5}
\]
Both maps are fixed-point-free, have no directed \(2\)-cycle, and satisfy
(5.2).  Thus their unordered local head choices are distinct within each
map, as required by the matching constraint at this one core.  The map
\(g_C\) is one directed cycle of length \(m+1\) and has no directed
\(3\)-cycle.  The general full-support bound still gives
\(\Omega(m^3)\) potential triples for \(f_C\), while this local \(g_C\)
occupies none.  This proves only that the displayed local pointer axioms do
not force occupancy.  It is not asserted that the two local pointer maps
extend simultaneously to two global Boolean perfect matchings. \(\square\)

This is the exact unconditional limitation of the raw hexagon count:
applicability is linear at best and requires a local \(3\)-cycle of the
incumbent factor.  The zero-occupancy example is a local-consistency
obstruction, not a global Boolean counterexample.

## 6. A scoped abstract integrality obstruction

The degree and functionality rows alone do not force an integral cap-two
cycle cover.

### Proposition 6.1 (functional \(C_8\) obstruction)

There is a \(2\)-in-regular, \(2\)-out-regular bipartite digraph with two
functional colour classes, four arcs in each class, such that:

* the canonical half-edge vector satisfies all tail, head, and exact
  colour-load-two equations;
* the separate colour-tail and colour-head SDRs exist; but
* neither cycle cover has colour multiplicities at most two.

### Construction and proof

Take tails \(L_0,\ldots,L_3\), heads \(M_0,\ldots,M_3\), and indices modulo
four. Let

\[
 e_i=L_iM_i,\qquad h_i=L_iM_{i+1}.
\]

These eight edges form one \(C_8\), whose only perfect matchings are
\[
 E=\{e_0,e_1,e_2,e_3\},
 \qquad
 J=\{h_0,h_1,h_2,h_3\}.
\]

Colour \(e_0,e_1,e_2,h_3\) red and
\(e_3,h_0,h_1,h_2\) blue. Each tail has one arc of each colour, so both
colour classes are functional and have four arcs. The vector assigning
weight \(1/2\) to every edge gives unit tail/head loads and colour load two.
The two colours plainly admit distinct tail representatives and distinct
head representatives.

But the colour counts of \(E\) are \((3,1)\), and those of \(J\) are
\((1,3)\). Hence neither perfect matching is cap-two.
\(\square\)

This is not a Boolean counterexample: its orders are the \(m=3\) degree
parameters but not the Boolean layer cardinalities, the colour-facet
incidence pattern, or the root-consistency/overlap geometry tying all
functional classes to one fixed Boolean factor.  It proves only that the
listed regularity, functionality, fractional, and two marginal Hall rows
do not imply cap-two integrality on their own.  A Boolean positive theorem
may, and must, use additional structure.

## 7. Exact surviving sufficient conditions

Two proof targets now suffice.

### Corollary 7.1 (rainbow completion criterion)

If \(H\) contains a matching \(Q\) with one arc of every upper colour and
the residual graph \(H-V(Q)\) has a perfect matching \(P\) whose colours
are distinct, then \(Q\cup P\) is a cap-two second factor.

This is Theorem 2.1 read in the forward constructive direction.

### Corollary 7.2 (hexagon descent criterion)

Suppose every positive-energy perfect matching \(F\subseteq H\) has an
occupied full Boolean hexagon satisfying (4.4). Then repeated switches
terminate at a cap-two perfect matching.

### Proof

Each switch preserves perfectness and decreases the nonnegative integer
\(\Delta(F)\). Finite descent ends at energy zero, which is exactly the
cap-two condition. \(\square\)

Theorem 5.1 shows why potential-support abundance does not prove the
hypothesis of Corollary 7.2. A successful descent theorem must either force
the needed directed \(3\)-cycles, transport defects along longer
alternating cycles, or change more than one local pointer state at once.

## 8. Proof-safe frontier

The fixed-factor problem is now separated as

\[
\boxed{
\begin{array}{c}
\text{tail/head/colour-cap LP feasibility}\quad\text{(automatic)}\\
\Downarrow\\
\text{integral rainbow base plus rainbow residual completion}
\quad\text{(open in the Boolean host)}\\
\Downarrow\\
\text{connectedness}\quad\text{(deferred)}.
\end{array}}
\]

The exact local energy gradient is (0.4), and the exact occupied-\(C_6\)
gate is (5.3). Neither the fractional LP nor the cubic number of potential
hexagons closes the integral selector.
