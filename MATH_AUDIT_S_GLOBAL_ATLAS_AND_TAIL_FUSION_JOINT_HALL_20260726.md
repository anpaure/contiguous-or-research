# Audit of the global common-core atlas and the first exact joint-Hall gate

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or web
input is used.

## 0. Verdict

This note audits
`MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md` and
then isolates the first integral obstruction to its missing tight-path
fusion.

The random-core degree calculations, the separate clone-Hall matchings,
the core-safe path construction, and the aggregate rankwise hole estimate
in that note are correct under their stated hypotheses.  The symmetric
fractional path statement is also correct, with one scope qualification:
its written proof averages over **all** core choices.  That proof does not
apply to the one fixed random core assignment used in Theorems 1.1--3.2.
Proposition 1.1 below repairs the scope gap: the maximum-degree caps
themselves imply an exact fixed-core fractional distribution on literal
tagged paths.  Hence all additive cuts pass even on the common restricted
catalogue; only integral rounding remains.

The missing fusion cannot be obtained by postprocessing arbitrary outputs
of the separate Hall matchings.  This is already false at depth one.  The
exact first gate is a node-capacitated three-layer flow, equivalently the
intersection of two transversal matroids on the middle owners.  A physical
counterexample below has

* a genuine core-safe tight middle path of length \(L\);
* \(L-1\) distinct, core-compatible lower targets;
* \(L-1\) distinct, core-compatible upper targets; and
* separate integral matchings at all three ranks,

but no common set of \(L-1\) middle phases supporting both signed
matchings.  Thus it cannot be a tagged promotion path.

This does not obstruct a fresh *joint* choice of the rankwise matchings.
It proves that such a joint choice is an additional theorem, not a formal
consequence of the atlas.

## 1. Audit of the four proved blocks

Retain the notation

\[
 W=\binom{2m}{m},\quad N_q=\binom{2m}{m-q},\quad
 M=m+H,\quad s=m-H,\quad L=s-2H+1,
\tag{1.1}
\]

and

\[
 \Lambda=\frac{W}{N_H},\qquad
 H=(1+o(1))\sqrt{m\log m},\qquad m>4H,
\tag{1.2}
\]

with \(L+c_0H\leq\Lambda\leq m+C_0H\).

### 1.1 Random-core middle cap

For fixed \(X\in\binom{[2m]}m\), the number \(Z_X\) of tops \(U\supset X\)
whose random \(2H\)-core lies in \(X\) is binomial with mean

\[
 \binom mH\frac{\binom m{2H}}{\binom{m+H}{2H}}
 =\frac{(m!)^2}{H!(m-2H)!(m+H)!}
 =\frac{\binom{s}{H}}{\Lambda}.
\tag{1.3}
\]

At threshold \(\binom{s}{H}/L\), the multiplicative excess is
\(\Lambda/L-1=\Theta(H/m)\).  Hence the Chernoff exponent is

\[
 \Omega\!\left(\frac{\binom{s}{H}H^2}{m^3}\right)\gg m.
\tag{1.4}
\]

The union bound over fewer than \(4^m\) middle owners is valid.  For an
arbitrary subset of clones, let \(\mathcal A\) be the set of touched top
fibres.  Its neighbourhood is the neighbourhood of \(\mathcal A\), while
the number of selected clones is at most \(L|\mathcal A|\).  Thus the
incidence proof in Theorem 1.2 verifies Hall for partial as well as full
clone fibres.

### 1.2 Core-safe path

The \(L=s-2H+1\) eligible central \(2H\)-windows are consecutive phases.
At any fixed non-top rank, distinct phases delete distinct equal-length
intervals of an injective word.  At rank \(m+H\) all deletions are empty,
which is why at most one phase may have tag \(H\).  These observations
prove all three assertions of Theorem 2.1.

### 1.3 Signed-rank caps and the hole ledger

At signed rank \(m+r\), a fixed target has random degree mean

\[
 \binom{m-r}{H-r}
 \frac{\binom{m+r}{2H}}{\binom{m+H}{2H}}
 =\frac{\binom{s}{H-r}}{N_{|r|}/N_H}.
\tag{1.5}
\]

If the quota \(b_{|r|}\) is positive, then
\(H-r=\Omega(m/H)\) for \(r>0\), whereas \(H-r\geq H\) for \(r<0\).
The corresponding Chernoff exponent is superexponential relative to the
\(O(H4^m)\) union bound.  The rankwise clone-Hall argument is therefore
valid simultaneously for the fixed cores.

For uncapped depths,

\[
 0\leq N_q-b_qN_H<2N_H.
\tag{1.6}
\]

The cap \(b_q=L-1\) can occur only for \(q=O(\sqrt H)\), and at such a
depth \(N_q/N_H-(L-1)=O(H)\).  Hence the two signs together leave

\[
 O(H^{3/2}N_H)=o(W)
\tag{1.7}
\]

targets, as claimed.

### 1.4 Scope of the fractional statement

Theorem 4.1 is valid for the catalogue in which a configuration may
choose its own core \(Q\subset U\), its two orders, and its tags.  Full
coordinate symmetry makes every target load equal, so its loads are
\(LN_H/W\) at the middle and \(b_qN_H/N_q\) at signed depth \(q\).

However, Theorems 1.1--3.2 first fix one generally nonsymmetric core
\(Q_U\) for each top.  The proof of Theorem 4.1 does not show that the
catalogue restricted to those fixed cores has the same fractional point.
Thus the following two correct conclusions must remain distinct:

1. some fixed core assignment admits all the separate integral Hall
   matchings;
2. the unrestricted variable-core path catalogue admits a symmetric
   fractional configuration point.

As written, no result in the audited note proves both statements for one
fixed-core path catalogue.  This is a scope correction, not a refutation
of either theorem.  The following proposition supplies the missing
argument.

### Proposition 1.1 (fixed-core fractional path repair)

Fix the core assignment supplied by Theorem 3.1 of the audited note.  In
each top \(U\), order \(S_U=U\setminus Q_U\) uniformly at random.  Assign
tags independently of the order, uniformly over all phase assignments
having

\[
 \#\{j:d_j\ge q\}=b_q\quad(0\le q<H),\qquad b_0=L,
\tag{1.8}
\]

and put \(b_H=0\).  This defines a fractional distribution on literal
core-safe tagged paths for the fixed cores.  Every middle target has load
at most one, and every signed depth-\(q\) target has load at most one.

#### Proof

Fix a signed target \(Y\subset U\) at rank \(m+r\), and put \(k=H-r\).
Its deleted set \(D=U\setminus Y\) is a fixed \(k\)-subset of \(S_U\).
At each one of the \(L\) eligible phases, the corresponding length-\(k\)
interval is uniform among the

\[
 d_r=\binom{s}{k}
\tag{1.9}
\]

subsets of \(S_U\).  Two distinct eligible intervals cannot both equal
the same set \(D\): an injective word places the elements of \(D\) in one
fixed set of positions.  Thus \(D\) occurs as an eligible interval with
probability \(L/d_r\).  Conditional on its phase, exchangeability and
independence of the tags make that phase active at depth \(|r|\) with
probability \(b_{|r|}/L\).  Therefore

\[
 \Pr_U(Y\text{ is used})=\frac{b_{|r|}}{d_r}.
\tag{1.10}
\]

The fixed-core degree cap gives

\[
 \operatorname{load}(Y)
 =\deg_r(Y)\frac{b_{|r|}}{d_r}\le1.
\tag{1.11}
\]

At the middle, every phase is active and the identical calculation gives

\[
 \operatorname{load}(X)=\deg_0(X)\frac L{d_0}\le1.
\tag{1.12}
\]

Every top's distribution has total mass one, so this is an exact
root-saturating fractional point.  \(\square\)

## 2. Exact tail-order reconstruction

The common-history constraint has a particularly rigid normal form.

### Theorem 2.1 (permutation-window normal form)

Fix a top \(U\), a core \(Q\in\binom U{2H}\), and put \(S=U\setminus Q\),
so \(|S|=s\).  A core-safe promotion path of length \(L\) is equivalent to
a listing

\[
 (c_{1-H},c_{2-H},\ldots,c_{L+H-1})
\tag{2.1}
\]

of all \(s=L+2H-1\) elements of \(S\), without repetition.

For phase \(1\leq j\leq L\), its middle owner is

\[
 X_j=U\setminus\{c_j,c_{j+1},\ldots,c_{j+H-1}\}.
\tag{2.2}
\]

At depth \(0\leq q\leq H\), its upper and lower traces are exactly

\[
 T^+_{j,q}
 =X_j\cup\{c_j,\ldots,c_{j+q-1}\},
\tag{2.3}
\]

\[
 T^-_{j,q}
 =X_j\setminus\{c_{j-q},\ldots,c_{j-1}\}.
\tag{2.4}
\]

In the interior of the path these become

\[
 T^+_{j,q}=\bigcup_{a=0}^{q}X_{j+a}
 \quad(j+q\leq L),
\tag{2.5}
\]

\[
 T^-_{j,q}=\bigcap_{a=0}^{q}X_{j-a}
 \quad(j-q\geq1).
\tag{2.6}
\]

In particular,

\[
 X_{j+1}=X_j\mathbin{\dot\cup}\{c_j\}\setminus\{c_{j+H}\},
\tag{2.7}
\]

and the oriented Johnson edges obey the lag-\(H\) successor cocycle

\[
 \boxed{
 X_j\setminus X_{j+1}
 =X_{j+H+1}\setminus X_{j+H}}
 \qquad(1\leq j\leq L-H-1).
\tag{2.8}
\]

#### Proof

Write the ordered \(S\)-block of the promotion order as
\((w_1,\ldots,w_s)\), and set \(c_i=w_{H+i}\).  As \(i\) runs from
\(1-H\) to \(L+H-1=s-H\), this lists every entry of the \(S\)-block.
The middle deletion interval of phase \(j\) is
\((w_{j+H},\ldots,w_{j+2H-1})\), which gives (2.2).

At upper depth \(q\), the first \(q\) letters of that middle deletion
interval are restored.  At lower depth \(q\), the preceding \(q\)
letters are additionally deleted.  This proves (2.3)--(2.4).

The intersection of the \(q+1\) consecutive deletion windows starting at
\(j,\ldots,j+q\) is
\(\{c_{j+q},\ldots,c_{j+H-1}\}\), proving (2.5).  Their union when the
windows end at \(j-q,\ldots,j\) is
\(\{c_{j-q},\ldots,c_{j+H-1}\}\), proving (2.6).

Equation (2.7) follows by shifting one deletion window.  Its removed
owner-coordinate is \(c_{j+H}\), and that same coordinate is added to the
owner at transition \(j+H\), which proves (2.8).

Conversely, a listing (2.1) defines \(w_{H+i}=c_i\).  Ordering \(Q\)
arbitrarily and applying the promotion construction recovers
(2.2)--(2.4), so every such listing is physical.  \(\square\)

Thus a Hamilton path in the ordinary Johnson graph is not enough.  It
must be a sliding \(H\)-window path with the exact delayed edge-direction
identity (2.8), and all signed targets are then forced by consecutive
unions and intersections.

## 3. The first exact joint-Hall theorem

Fix one top and suppose three separately assigned families are given:

\[
 \mathcal R\subseteq\binom U{m-1},\qquad
 \mathcal X\subseteq\binom U m,\qquad
 \mathcal Y\subseteq\binom U{m+1},
\tag{3.1}
\]

with \(|\mathcal R|=|\mathcal Y|=b\leq|\mathcal X|\).  A depth-one
common support is a set \(I\subseteq\mathcal X\), \(|I|=b\), together
with bijections which place each \(R\in\mathcal R\) below one member of
\(I\) and each \(Y\in\mathcal Y\) above one member of \(I\).

For \(A\subseteq\mathcal X\), let \(r_-(A)\) be the maximum number of
members of \(A\) which can be matched to distinct members of
\(\mathcal R\) using containment \(R\subset X\).  Define \(r_+(A)\)
analogously using \(X\subset Y\) and \(\mathcal Y\).

### Theorem 3.1 (exact common-support cut)

A depth-one common support of size \(b\) exists if and only if

\[
 \boxed{
 r_-(A)+r_+(\mathcal X\setminus A)\geq b
 \quad\hbox{for every }A\subseteq\mathcal X.}
\tag{3.2}
\]

Equivalently, construct the node-capacitated network

\[
 s\longrightarrow\mathcal R\longrightarrow\mathcal X
 \longrightarrow\mathcal Y\longrightarrow t,
\tag{3.3}
\]

put capacity one on every vertex in the three displayed layers, and use
containment arcs of infinite capacity.  The required support exists if
and only if the minimum \(s\)-\(t\) cut has capacity at least \(b\).

#### Proof

An integral flow of value \(b\) in (3.3) is a collection of \(b\)
vertex-disjoint paths \(R-X-Y\).  Since each outside family has exactly
\(b\) vertices, the flow uses every \(R\) and every \(Y\), and its middle
vertices form the desired support.  The converse concatenates the two
given bijections.  Integral capacities and the augmenting-path proof of
max-flow give an integral maximum flow.

Eliminating the two outside layers from the minimum-cut formula gives

\[
 \max |I|
 =\min_{A\subseteq\mathcal X}
   \bigl(r_-(A)+r_+(\mathcal X\setminus A)\bigr),
\tag{3.4}
\]

the usual two-transversal-matroid intersection formula.  Equation (3.2)
is therefore equivalent to flow value at least \(b\).  \(\square\)

Separate Hall at the lower and upper ranks proves only
\(r_-(\mathcal X)=r_+(\mathcal X)=b\).  These are the two endpoint cases
of (3.2); they do not imply its internal cuts.

## 4. A physical failure of separate-Hall fusion

Under the hypotheses of the audited atlas, the depth-one quota is

\[
 b_1=L-1
\tag{4.1}
\]

for all sufficiently large \(m\).  Indeed,

\[
 \frac{N_1}{N_H}=\frac m{m+1}\Lambda
 \geq L+c_0H-O(1),
\tag{4.2}
\]

so the cap in the definition of \(b_1\) is active.

### Theorem 4.1 (core-compatible \(q=1\) counterexample)

For every sufficiently large \(m\), fix any top \(U\) and core \(Q\).
There are families

\[
 |\mathcal X|=L,qquad
 |\mathcal R|=|\mathcal Y|=L-1,
\tag{4.3}
\]

such that:

1. \(\mathcal X\) is exactly the middle-owner sequence of a literal
   core-safe tight path;
2. every member of all three families contains \(Q\) and lies in \(U\);
3. \(\mathcal R\) and \(\mathcal Y\) separately have integral containment
   matchings into \(\mathcal X\); but
4. the maximum common depth-one support has size \(L-2\).

Consequently these separately valid rank assignments cannot be traces of
one tagged promotion path.

#### Proof

Choose any listing (2.1) of \(S=U\setminus Q\), and let

\[
 X_i=U\setminus\{c_i,\ldots,c_{i+H-1}\},
 \qquad 1\leq i\leq L.
\tag{4.4}
\]

These are the middle owners of a literal tight path.  Two of them have
Johnson distance one exactly when their indices differ by one.

For every \(i\), choose

\[
 a_i\in X_i\setminus Q
\tag{4.5}
\]

different from the at most two coordinates \(X_i\setminus X_j\) arising
from neighbours \(j=i\pm1\).  This is possible because
\(|X_i\setminus Q|=m-2H>2\).  Put

\[
 R_i=X_i\setminus\{a_i\}.
\tag{4.6}
\]

If \(R_i\subseteq X_j\), then \(d_J(X_i,X_j)\leq1\).  For \(j\ne i\)
this forces \(j=i\pm1\), and then containment forces
\(a_i=X_i\setminus X_j\), excluded by construction.  Hence

\[
 R_i\subseteq X_j\quad\Longleftrightarrow\quad i=j.
\tag{4.7}
\]

Likewise choose

\[
 e_i\in U\setminus X_i
\tag{4.8}
\]

different from the at most two coordinates \(X_j\setminus X_i\) for
\(j=i\pm1\); this is possible because \(H>2\).  Set

\[
 Y_i=X_i\cup\{e_i\}.
\tag{4.9}
\]

The same distance-one argument gives

\[
 X_j\subseteq Y_i\quad\Longleftrightarrow\quad i=j.
\tag{4.10}
\]

Now take

\[
 \mathcal R=\{R_1,\ldots,R_{L-1}\},\qquad
 \mathcal Y=\{Y_2,\ldots,Y_L\}.
\tag{4.11}
\]

Each family has its displayed separate matching into \(\mathcal X\).
By (4.7), every common support must contain all of
\(X_1,\ldots,X_{L-1}\) in order to support the lower family.  By (4.10),
it must contain all of \(X_2,\ldots,X_L\) in order to support the upper
family.  A support of size \(L-1\) cannot equal both sets.  The common
support \(\{X_2,\ldots,X_{L-1}\}\) has size \(L-2\), and this is maximum.

In the cut form, take \(A=\{X_2,\ldots,X_L\}\).  Then

\[
 r_-(A)+r_+(\mathcal X\setminus A)=(L-2)+0<L-1,
\tag{4.12}
\]

which is the exact violated joint-Hall inequality.  \(\square\)

The counterexample is local to one top, so it does not disprove the
existence of a different globally compatible choice.  It does prove that
the already-constructed separate matchings cannot be fed into a generic
fusion routine without an additional joint cut hypothesis.

## 5. The global integral formulation and its odd-set boundary

For each top \(U\), let \(\mathscr C_U\) be its legal tagged core-safe tail
configurations.  A configuration records one permutation (2.1), one tag
on each of its \(L\) phases, and therefore all target incidences given by
(2.3)--(2.4).  The exact selection variables satisfy

\[
 x_{U,P}\in\{0,1\},\qquad
 \sum_{P\in\mathscr C_U}x_{U,P}=1,
\tag{5.1}
\]

and, for every physical signed target \(T\),

\[
 \sum_{U}\sum_{P\ni T}x_{U,P}\leq1.
\tag{5.2}
\]

Theorem 4.1 of the audited atlas gives a fractional point for (5.1)--(5.2)
when the cores are allowed to vary inside \(\mathscr C_U\).  Proposition
1.1 gives one for the single fixed-core catalogue as well.  The integer
system is an independent-transversal problem in the conflict graph on
the configurations: two configurations conflict when they have the same
root or share a target.

Target-capacity inequalities are clique inequalities in this graph.  They
do not contain its odd-cycle inequalities

\[
 \sum_{P\in C}x_P\leq\frac{|C|-1}{2}
\tag{5.3}
\]

for an induced odd cycle \(C\).  The familiar three-root parity gadget
makes the distinction exact: give root \(i\in\mathbb Z/3\mathbb Z\) two
options \(P_i^0,P_i^1\); for every edge \(i(i+1)\), let one target be used
by \(P_i^0,P_{i+1}^0\) and another by \(P_i^1,P_{i+1}^1\).  Assigning
weight \(1/2\) to every option gives target load one, but every integral
bit assignment has two adjacent equal bits and hence a collision.

This gadget is an abstract warning about the configuration polytope; it
is not asserted here to be an unavoidable subinstance of the unrestricted
physical atlas.  The physical obstruction proved in Theorem 4.1 is the
violated common-support cut (4.12).

## 6. Exact proved boundary

The audit proves that the global common-core atlas supplies valid
rankwise marginals but not a common history.  Two additional facts are
now exact:

1. **Tail-order law.**  A physical history is precisely a permutation
   window array (2.1)--(2.4); its middle path has the lag-\(H\) cocycle
   (2.8), and its signed traces are consecutive unions/intersections.
2. **First joint cut.**  Even before imposing the lag-(H) order, the
   lower and upper depth-one assignments must satisfy every cut (3.2).
   Separate Hall checks only two of those cuts and can fail by one unit on
   a fully physical tight middle path.

Therefore the minimum surviving positive theorem cannot say merely that
each signed rank has a matching.  It must jointly choose the targets and
the ordered middle path so that

* the depth-one common-flow value is \(L-1-o(L)\) for almost every top,
  with aggregate loss \(o(W)\);
* the selected owner transitions obey the lag-\(H\) cocycle; and
* the higher signed targets are the forced consecutive
  unions/intersections (2.5)--(2.6), with aggregate collision/leave
  \(o(W)\).

No such global integral theorem is proved here.  In particular this note
does not prove `fcpath`, MWB, or the coefficient-one theorem.
