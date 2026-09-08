# Prime-equivariant sigma factors: quotient equations and voltage audit

Date: 2026-07-27

This note audits the proposed prime-equivariant formulation of the immediate
two-sided shadow problem.  The conclusions are:

* the numerical (k=11) quotient is exactly the advertised
  (42\times15\) multiple-choice system;
* the relaxed quotient system (degree two and upper coverage) has both an
  exact uniform fractional solution and an integral equivariant solution;
* upper coverage does **not** imply the simple (1/2) load profile;
* the constraint matrix is not totally unimodular;
* there is no universal zero-voltage obstruction: the integral PBBS solution
  has at least one nonzero-voltage quotient component;
* obtaining one connected quotient cycle, cap two, and a prescribed excess
  design remains the unresolved global condition.

## 1. The sigma normal form

Put

\[
 p=2r-1,qquad
 \mathcal L=\binom{\mathbb Z_p}{r-1},quad
 \mathcal V=\binom{\mathbb Z_p}{r},quad
 \mathcal U=\binom{\mathbb Z_p}{r+1}.
\]

For every (C\in\mathcal L), choose

\[
 \sigma(C)\in\mathcal U,qquad C\subset\sigma(C).
\tag{1.1}
\]

Writing \(\sigma(C)\setminus C=\{a,b\}\), associate the Johnson edge

\[
 e_C=\{C\cup\{a\},C\cup\{b\}\}.
\tag{1.2}
\]

### Proposition 1.1

The graph (G_\sigma=(\mathcal V,\{e_C:C\in\mathcal L\})) is a spanning
2-factor if and only if

\[
 \boxed{
 \#\{C:C\subset T\subset\sigma(C)\}=2
 \quad(T\in\mathcal V).}
\tag{1.3}
\]

Its lower colours are automatically all distinct and exhaustive.  Its upper
load is

\[
 \mu(U)=\#\{C:\sigma(C)=U\}.
\tag{1.4}
\]

Thus upper surjectivity is precisely \(\mu(U)\ge1\) for every (U).

The proof is immediate from (1.2): (C) is the intersection and
\(\sigma(C)\) the union of the endpoints of (e_C), while (1.3) is exactly
the degree of (T).

An important correction is that surjectivity and degree two do not imply
\(\mu\le2\).  Loads three and higher are possible.  If the additional cap
\(1\le\mu\le2\) is imposed, then counting forces exactly

\[
 |\mathcal L|-|\mathcal U|=\operatorname{Cat}_r
\tag{1.5}
\]

upper colours to have load two.

## 2. Linear equations and the exact fractional point

For every diamond (C\subset U), let (x_{C,U}\ge0).  The linear
relaxation is

\[
 \begin{aligned}
 \sum_{U\supset C}x_{C,U}&=1 &&(C\in\mathcal L),\\
 \sum_{C\subset T\subset U}x_{C,U}&=2 &&(T\in\mathcal V),\\
 1\le\sum_{C\subset U}x_{C,U}&\le2 &&(U\in\mathcal U).
 \end{aligned}
\tag{2.1}
\]

Every lower colour has \(\binom r2\) possible diamonds, every central set
has (r(r-1)) incident diamonds, and every upper colour has
\(\binom{r+1}{2}\) diamonds.  Consequently

\[
 \boxed{x_{C,U}=\binom r2^{-1}}
\tag{2.2}
\]

solves the two equality systems and gives every upper colour load

\[
 \binom{r+1}{2}/\binom r2=\frac{r+1}{r-1}\in(1,2)
 \qquad(r>3).
\tag{2.3}
\]

Thus there is no fractional or capacity obstruction to degree two plus
upper coverage/cap two.  Prescribing *which* upper colours have loads one
and two is stronger; (2.2) does not solve that equality-constrained problem.
For a prescribed vector (b_U\in\{1,2\}), nonnegative fractional
feasibility is exactly the Farkas condition

\[
 \sum_C\alpha_C+2\sum_T\beta_T+\sum_Ub_U\gamma_U\ge0
\tag{2.4}
\]

for every triple of potentials satisfying

\[
 \alpha_C+\beta_{C\cup\{a\}}+\beta_{C\cup\{b\}}+\gamma_{C\cup\{a,b\}}
 \ge0
\tag{2.5}
\]

for every (C) and distinct (a,b\notin C).

## 3. The matrix is not TU; the exact integral encoding

Fix (C\in\mathcal L) and three distinct points (a,b,c\notin C).  Restrict
the constraint matrix to the three central rows

\[
 C+a,quad C+b,quad C+c
\]

and the three diamond columns (ab,bc,ca).  The resulting matrix is the
vertex-edge incidence matrix of a triangle,

\[
 \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},
\]

whose determinant is (2).  Hence the matrix in (2.1) is not totally
unimodular for every (r\ge3).  The multiple-choice system is not a hidden
network flow.

For prescribed (b_U\in\{1,2\}), there is nevertheless an exact matching
encoding.  Make one vertex for each lower colour, (b_U) clones of every
upper colour, and two clones of every central set.  For each diamond use
all hyperedges consisting of its lower vertex, one upper clone, and one
clone of each of its two central endpoints.  Then

\[
 \boxed{
 \text{a prescribed-colour 2-factor}
 \iff
 \text{a perfect matching of this (4)-uniform hypergraph}.}
\tag{3.1}
\]

This identifies the exact residual integrality problem.  Ordinary Hall cuts
are necessary, and the central projection must obey the usual (2)-factor
blossom inequalities, but neither family alone is sufficient for the
four-part matching in (3.1).

## 4. Forced first- and second-order identities

For each selected diamond (C\subset U=C\cup\{a,b\}), its two central
endpoints obey, coordinatewise,

\[
 \mathbf1_{C+a}+\mathbf1_{C+b}=\mathbf1_C+\mathbf1_U.
\tag{4.1}
\]

After summation, degree two forces the upper multihypergraph's point degrees.
If (1\le\mu\le2), put

\[
 \widetilde D=\{\mathbb Z_p\setminus U:\mu(U)=2\}
 \subseteq\binom{\mathbb Z_p}{r-2}.
\]

Then

\[
 |\widetilde D|=\operatorname{Cat}_r,qquad
 d_{\widetilde D}(i)=\frac{(r-2)\operatorname{Cat}_r}{2r-1}.
\tag{4.2}
\]

There is also a useful pair identity.  Let (h_{ij}) be the number of
selected transitions whose exchanged pair is exactly \(\{i,j\}\).  Comparing
pair incidence in the two central endpoints with incidence in (C) and
(U) gives

\[
 \boxed{
 h_{ij}=d_{\widetilde D}(\{i,j\})
 +\frac{(5-r)\operatorname{Cat}_r}{2(2r-1)}.}
\tag{4.3}
\]

In particular, for (r\ge6), every realizable simple excess design must
satisfy

\[
 d_{\widetilde D}(\{i,j\})
 \ge\frac{(r-5)\operatorname{Cat}_r}{2(2r-1)}.
\tag{4.4}
\]

The cyclic-orbit designs of the static theorem satisfy this with large
margin, but (4.3) shows that cardinality and vertex regularity are not the
whole inverse problem.

## 5. Prime quotient and the (p=11,r=6) ledger

Assume (p) is prime.  Translation acts freely on all nonempty proper
subsets.  Quotienting (1.1) by translation gives a voltage multigraph:

* lower colour orbits choose one edge orbit;
* middle-set orbits are its vertices;
* upper-set orbits are a second edge colouring;
* loops count twice in the degree equations.

For (p=11,r=6), the exact counts are

\[
 \begin{array}{c|c}
 \text{object}&\text{number}\\ \hline
 (r-1)\text{-set orbits}&\binom{11}{5}/11=42\\
 r\text{-set orbits}&\binom{11}{6}/11=42\\
 (r+1)\text{-set orbits}&\binom{11}{7}/11=30\\
 \text{choices per lower orbit}&\binom62=15\\
 \text{all edge orbits}&42\cdot15=630.
 \end{array}
\tag{5.1}
\]

The quotient degree equations number (42) (their sum is redundant), and
the uniform quotient assignment (x=1/15) gives degree two and upper load

\[
 21/15=7/5.
\tag{5.2}
\]

Mere coverage of the (30) upper orbits permits loads (3,4,\ldots).  If
cap two is added, the profile is forced to

\[
 1^{18}2^{12}.
\tag{5.3}
\]

The complements of the twelve doubled upper orbits form twelve full
translation orbits of (4)-sets, hence (132) blocks and exact point degree

\[
 12\cdot4=48.
\tag{5.4}
\]

Thus equivariance makes the static Catalan cardinality and first-degree
condition automatic once cap two is achieved.

## 6. An integral equivariant solution to the relaxed system

The cyclic-parenthesis PBBS permutation commutes with coordinate rotation:
cyclic noncrossing matching and the unmatched-zero rule are unchanged by a
rotation of the word.  Its centered Johnson factor is therefore
translation-invariant.  Complementing that centered factor gives a
translation-invariant spanning 2-factor on rank (r) with

* every lower ((r-1))-colour exactly once;
* every upper ((r+1))-colour at least once;
* every upper load at most three.

Equivalently, it supplies an integral prime-quotient sigma satisfying degree
two and upper surjectivity.  What it does not supply is cap two, a prescribed
simple excess design, or connectedness.

## 7. Voltage: no forced-zero obstruction

For a quotient cycle, choose the unique representative (T) of each
middle-set orbit with \(\sum_{t\in T}t=0\pmod p\).  This is possible because
(r\) is invertible modulo (p).  If an oriented transition deletes (a)
and inserts (b), its voltage in this gauge is

\[
 \omega(e)=r^{-1}(b-a)\pmod p.
\tag{7.1}
\]

A quotient cycle lifts to one cycle exactly when its voltage sum is nonzero;
at voltage zero it lifts to (p) disjoint copies.

The degree equations do not force all cycle voltages to vanish.  Indeed,
every PBBS orbit length is a multiple of (p).  Its centered Johnson
components have lengths

\[
 L/\gcd(2,L),
\]

which are still multiples of the odd prime (p).  In the quotient, a
zero-voltage cycle of length (s) lifts to (p) cycles of length (s), so
such an (s) must itself be divisible by (p).  If every quotient component
of the complemented PBBS factor had zero voltage, the total number of
quotient middle vertices would be divisible by (p).  But for (p=11) it
is (42\not\equiv0\pmod{11}).  Therefore

\[
 \boxed{\text{the integral (k=11) quotient has a nonzero-voltage component}.}
\tag{7.2}
\]

There is also a local sanity check: a cyclic interval (T) has (T+1)
Johnson-adjacent to (T), producing a quotient loop of voltage (1).
Thus nonzero voltage is native to the quotient geometry, not prohibited by
parity.

For a disconnected quotient 2-factor there is no canonical “total voltage”:
each component can be oriented independently, changing its sign.  The
invariant datum is the multiset of component voltages up to independent
signs.  For a connected quotient, the single voltage is defined up to sign.
The results above disprove a universal forced-zero law, but they do **not**
construct a connected (42)-cycle with cap two.

## 8. Exact remaining gate

At (k=11), the symmetry-reduced target is now completely explicit:

> choose one of (15) edge orbits for each of (42) lower orbits so that
> the (42) middle vertices form one cycle, the (30) upper loads are
> (1^{18}2^{12}), and the cycle voltage is nonzero in \(\mathbb Z_{11}\).

Fractional feasibility, relaxed integral feasibility, first-degree excess
regularity, and nonzero-voltage compatibility are all proved.  The smallest
unresolved condition is the simultaneous **cap-two connected transversal**.
It is a genuine four-part perfect-matching/cycle-merging problem, not a TU
flow problem and not a modular obstruction.
