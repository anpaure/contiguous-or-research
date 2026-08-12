# Contextual \(B_4\), rootable pair factorizations, and the local Latin-pair gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Exact verdict

Put

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal M=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}{m+1},
\]

\[
 W=|\mathcal M|,\qquad
 N=|\mathcal L|=|\mathcal U|={m\over m+1}W,
 \qquad D=W-N={W\over m+1}=\operatorname {Cat}_m,
 \tag{0.1}
\]

and

\[
 n=m+1,\qquad Q=\binom n2=\binom{m+1}2.
 \tag{0.2}
\]

Let \(H_m\) be the inclusion graph between \(\mathcal L\) and
\(\mathcal M\), and let

\[
 \kappa:E(H_m)\longrightarrow\mathscr C,qquad |\mathscr C|=n,
 \tag{0.3}
\]

be a proper edge-coloring.  Such a coloring exists by the bipartite
edge-coloring theorem.  It induces, at every \(U\in\mathcal U\), a map

\[
 \psi_U:\binom U2\longrightarrow\binom{\mathscr C}2.
 \tag{0.4}
\]

The local defect

\[
 \ell(U)=Q-|\operatorname {im}\psi_U|
 \tag{0.5}
\]

has the following exact interpretation.  If \(p\in\binom{\mathscr C}2\)
is a color pair and \(H_p\) is the number of missing upper colors in its
suppressed Johnson graph, then

\[
 \boxed{
 \sum_p H_p=\sum_{U\in\mathcal U}\ell(U).}
 \tag{0.6}
\]

Consequently

\[
 \boxed{
 \min_pH_p\le
 \left\lfloor {\sum_U\ell(U)\over Q}\right\rfloor.}
 \tag{0.7}
\]

For each fixed pair, upper holes equal upper collision excess exactly.
Thus the uniform contextual target

\[
 \max_U\ell(U)=o(Q)=o(m^2)
 \tag{0.8}
\]

is sufficient for a distinguished pair with \(o(W)\) upper error.  The
weaker average condition

\[
 \sum_U\ell(U)=o(QN)
 \tag{0.9}
\]

is already sufficient.

There are, however, three exact warnings.

1.  A closed paired-SCD central factor has middle degrees \(0,2\), while
    every bichromatic subgraph of a full coloring has middle degrees
    \(1,2\).  Hence the closed complement-symmetric \(B_4\) cycle is not
    literally a standalone, owner-closed color pair.  A contextual copy
    must open exterior selected-color ports as in Section 4.
2.  Requiring \(\ell(U)=0\) for every \(U\) is far stronger than (0.8).
    It forces a large set of Steiner systems
    \(S(m-1,m,2m)\).  The complete design divisibility conditions force
    \(m+1\) to be prime.  Even that is not sufficient: universal local
    Latinness is impossible at \(m=2\).
3.  Pair labels cannot be assembled as independent perfect matchings.
    They must be **rootable** at every lower set by one common labeling of
    its \(m+1\) middle extensions, and these roots must remain proper at
    every middle set.  This is the compatibility a contextual recursion
    still has to prove.

The finite \(B_4\) situation is nevertheless positive after opening the
seed.  There is a proper 3-edge-coloring with

\[
 \sum_{U\in\binom{[4]}3}\ell(U)=2,
 \tag{0.10}
\]

which is the minimum possible, and one of its three color pairs is exactly
upper-perfect and acyclic.  Its suppressed graph is two disjoint
three-vertex paths.  Thus the correct recursive atom for the edge-coloring
engine is an open \(B_4\) path packet, not the closed paired-SCD \(C_4\).

What is **not** proved here is a growing contextual recursion satisfying
(0.8) or (0.9), nor control of the number of bichromatic cycles.  The note
gives the exact finite criterion such a recursion must meet and closes the
literal closed-seed interpretation.

## 1. The induced pair coloring of the diamond graph

Let \(\mathfrak D_m\) be the bipartite inclusion graph between
\(\mathcal L\) and \(\mathcal U\): its edges are the diamonds

\[
 (S,U),\qquad S\subset U,\quad |U\setminus S|=2.
 \tag{1.1}
\]

It is \(Q\)-regular on both shores.  If

\[
 U\setminus S=\{a,b\},\qquad
 X=S+a,\quad Y=S+b,
 \tag{1.2}
\]

define the induced pair label

\[
 \chi_\kappa(S,U)=
 \{\kappa(S,X),\kappa(S,Y)\}
 \in\binom{\mathscr C}2.
 \tag{1.3}
\]

The two colors are distinct because the two incidences meet at \(S\).

### Theorem 1.1 (lower pair completeness is automatic)

For every \(S\in\mathcal L\), the map

\[
 U\longmapsto\chi_\kappa(S,U),\qquad U\supset S,
 \tag{1.4}
\]

is a bijection from the \(Q\) upper extensions of \(S\) to
\(\binom{\mathscr C}2\).

#### Proof

The \(n=m+1\) middle extensions of \(S\) receive all \(n\) colors once,
because \(\deg_{H_m}(S)=n\) and \(\kappa\) is proper.  A diamond over
\(S\) is an unordered pair of these extensions.  Passing from a vertex
bijection to its induced map on unordered pairs gives (1.4). \(\square\)

For \(U\in\mathcal U\), write

\[
 X_a=U\setminus\{a\},\qquad
 S_{ab}=U\setminus\{a,b\}.
 \tag{1.5}
\]

Then the local map in (0.4) is

\[
 \psi_U(\{a,b\})=
 \{\kappa(S_{ab},X_a),\kappa(S_{ab},X_b)\}.
 \tag{1.6}
\]

For a pair \(p\), put

\[
 h_p(U)=|\psi_U^{-1}(p)|.
 \tag{1.7}
\]

By construction, \(h_p(U)\) is exactly the number of selected
pair-\(p\) Johnson edges with union color \(U\).

### Corollary 1.2 (universal Latinness is a rootable 1-factorization)

The following are equivalent.

1.  Every \(\psi_U\) is a bijection.
2.  For every pair \(p\), the edges of \(\mathfrak D_m\) labeled \(p\)
    form a perfect matching between \(\mathcal L\) and \(\mathcal U\).
3.  The induced label \(\chi_\kappa\) is a proper \(Q\)-edge-coloring of
    the \(Q\)-regular bipartite graph \(\mathfrak D_m\).

This is not an arbitrary 1-factorization.  It is one induced from the
\(n\) base colors of \(H_m\).

#### Proof

Theorem 1.1 gives degree one at every lower vertex in every pair class.
The condition \(h_p(U)=1\) gives degree one at every upper vertex.  This is
exactly clauses 2 and 3. \(\square\)

The extra word “rootable” can be made exact.

### Proposition 1.3 (exact rootability criterion)

Let

\[
 \chi:E(\mathfrak D_m)\to\binom{\mathscr C}2
 \tag{1.8}
\]

be any pair labeling.  It equals \(\chi_\kappa\) for a proper base
edge-coloring \(\kappa\) if and only if there are maps

\[
 c_S:\{X\in\mathcal M:S\subset X\}\longrightarrow\mathscr C
 \tag{1.9}
\]

such that

1. every \(c_S\) is a bijection;
2. for the two middle corners \(X,Y\) of every diamond \((S,U)\),
   \[
   \chi(S,U)=\{c_S(X),c_S(Y)\};
   \tag{1.10}
   \]
3. for every \(X\in\mathcal M\), the \(m\) values
   \[
   \{c_S(X):S\subset X,\ |S|=m-1\}
   \tag{1.11}
   \]
   are pairwise distinct.

#### Proof

Given \(\kappa\), set \(c_S(X)=\kappa(S,X)\).  Properness at \(S\), the
definition of \(\chi_\kappa\), and properness at \(X\) give clauses
1--3.  Conversely define \(\kappa(S,X)=c_S(X)\).  Clauses 1 and 3 are
exactly properness at the two shores, and clause 2 gives
\(\chi=\chi_\kappa\). \(\square\)

Thus independently chosen central-diamond perfect matchings do not compose
into the desired coloring.  All \(Q\) matchings must admit the common
lower-star roots (1.9), and those roots must satisfy the middle constraint
(1.11).

## 2. Exact local-defect averaging

At each \(U\), both the domain and codomain of \(\psi_U\) have size \(Q\).
Therefore

\[
 \ell(U)=Q-|\operatorname {im}\psi_U|
        =|\{p:h_p(U)=0\}|
        =\sum_p(h_p(U)-1)_+.
 \tag{2.1}
\]

For a fixed \(p\), every \(S\in\mathcal L\) supplies exactly one selected
edge, so

\[
 \sum_{U\in\mathcal U}h_p(U)=N=|\mathcal U|.
 \tag{2.2}
\]

### Theorem 2.1 (holes, collisions, and exact averaging)

For every pair \(p\),

\[
 |\{U:h_p(U)=0\}|=
 \sum_U(h_p(U)-1)_+.
 \tag{2.3}
\]

Moreover,

\[
 \sum_p|\{U:h_p(U)=0\}|=\sum_U\ell(U).
 \tag{2.4}
\]

Hence, if \(\ell(U)\le b_m\) for all \(U\), some pair has at most

\[
 \left\lfloor {b_mN\over Q}\right\rfloor
 \tag{2.5}
\]

upper holes and the same collision excess.

#### Proof

Equation (2.3) follows by distributing the integer total \(N\) in (2.2)
among \(N\) cells: total deficit below one equals total excess above one,
and the deficit is the number of zero cells.  Summing the zero-cell
indicator first over \(p\) and then over \(U\) gives (2.4).  Averaging over
the \(Q\) pairs gives (2.5). \(\square\)

In particular, even the strong-looking uniform estimate

\[
 b_m=O(1)
 \tag{2.6}
\]

would give only \(O(W/m^2)\) missing upper colors for one pair.  More
generally \(b_m=o(m^2)\) is enough for \(o(W)\) error.  No exact local
Latinness is needed.

## 3. Every color pair is an open path system

Every \(X\in\mathcal M\) sees \(m\) distinct colors and hence misses a
unique color \(\mu(X)\).  For \(c\in\mathscr C\), put

\[
 \mathcal E_c=\{X:\mu(X)=c\}.
 \tag{3.1}
\]

Each color class is a matching of size \(N\) saturating \(\mathcal L\), so

\[
 |\mathcal E_c|=W-N=D.
 \tag{3.2}
\]

Fix \(p=\{\alpha,\beta\}\).  The union of these two color classes has
degree two at every lower vertex and, at a middle vertex \(X\), degree

\[
 \deg_p(X)=
 \begin{cases}
 1,&\mu(X)\in\{\alpha,\beta\},\\
 2,&\text{otherwise}.
 \end{cases}
 \tag{3.3}
\]

After suppressing lower vertices, it is a Johnson graph on **all** \(W\)
middle owners.

### Theorem 3.1 (exact endpoint and component ledger)

The suppressed pair graph has exactly \(2D\) endpoints, namely

\[
 \mathcal E_\alpha\mathbin{\dot\cup}\mathcal E_\beta,
 \tag{3.4}
\]

and no isolated middle vertex.  It consists of exactly \(D\) path
components and some number \(z_p\) of cycle components.  Hence its total
component count is

\[
 D+z_p.
 \tag{3.5}
\]

#### Proof

The two color classes are matchings, so every component is an alternating
path or cycle.  Equation (3.3) gives \(2D\) degree-one vertices and no
degree-zero vertex.  Each path has two endpoints. \(\square\)

The forced path term is already coefficient-safe whenever \(H=o(m)\):

\[
 D={W\over m+1}=o(W/H).
 \tag{3.6}
\]

The independent remaining component gate is

\[
 z_p=o(W/H).
 \tag{3.7}
\]

Local Latin-pair balance does not imply (3.7).

The endpoint family also has an exact point margin when the upper colors
are balanced.  For \(p=\{\alpha,\beta\}\) and a coordinate \(v\), put

\[
 e_p(v)=|\{X\in\mathcal E_\alpha\dot\cup\mathcal E_\beta:v\in X\}|.
 \tag{3.8}
\]

### Theorem 3.2 (selected endpoint point-margin identity)

For every pair \(p\) and coordinate \(v\),

\[
 \boxed{
 e_p(v)-D=-\sum_{\substack{U\in\mathcal U\\v\in U}}(h_p(U)-1).}
 \tag{3.9}
\]

In particular, an upper-perfect pair has

\[
 e_p(v)=D\qquad(v\in[2m]),
 \tag{3.10}
\]

while a pair with \(H_p\) holes satisfies

\[
 |e_p(v)-D|\le2H_p.
 \tag{3.11}
\]

#### Proof

For the edge generated by \(S\), with endpoints \(X_S,Y_S\) and union
\(U_S\),

\[
 \mathbf1_{X_S}+\mathbf1_{Y_S}=\mathbf1_S+\mathbf1_{U_S}.
 \tag{3.12}
\]

Sum over all \(S\).  At a middle owner \(X\), the left multiplicity is
\(2-\mathbf1_{\mu(X)\in p}\), so its coordinate-\(v\) total is
\(W-e_p(v)\).  The lower coordinate total plus the once-each upper
coordinate total is \(N=W-D\); replacing the latter by the actual upper
histogram adds the sum in (3.9).  Rearrangement proves (3.9).  Finally,
\(\sum_U|h_p(U)-1|=2H_p\), proving (3.11). \(\square\)

Thus even one exact pair requires its two endpoint classes jointly to form
an exact point design.  This is necessary, not sufficient for upper
rainbowness.

There is also an exact converse which clarifies the role of the full
edge-coloring.

### Theorem 3.3 (open-pair completion)

Suppose a Johnson graph \(F\) has exactly one edge of every lower color
\(S\in\mathcal L\) and satisfies

\[
 1\le\deg_F(X)\le2\qquad(X\in\mathcal M).
 \tag{3.13}
\]

Then the lower-incidence lift of \(F\) can be colored with two colors and
extended to a proper \((m+1)\)-edge-coloring of all of \(H_m\).  Thus
\(F\) is a bichromatic pair in some full coloring.

#### Proof

The incidence lift has maximum degree two and is bipartite, so it has a
proper 2-edge-coloring.  Every lower vertex has degree two and therefore
sees both selected colors.  Remove these incidences from \(H_m\).  The
residual bipartite graph has degree exactly \(m-1\) at every lower vertex
and degree at most \(m-1\) at every middle vertex, by (3.13).  The
bipartite edge-coloring theorem colors it with \(m-1\) new colors.  The
combined coloring is proper and uses \(m+1\) colors. \(\square\)

So, for **one prescribed distinguished pair**, the full edge-coloring
requirement adds no obstruction after a spanning lower-perfect
degree-\(\{1,2\}\) graph has been constructed.  This does not complete
several prescribed pair graphs independently and does not remove the
whole-family rootability gate in Proposition 1.3.  For the one-pair
completion, the obstruction appears precisely when degree-zero owners are
present.

## 4. Closed paired factors are not bichromatic

A paired-SCD central factor has a set \(A\subset\mathcal M\) of
\(|A|=N\) active owners and a singleton leave \(E=\mathcal M\setminus A\)
of size \(D\).  Its lower-incidence lift has

\[
 \deg(X)=2\quad(X\in A),\qquad
 \deg(X)=0\quad(X\in E).
 \tag{4.1}
\]

### Theorem 4.1 (degree-defect obstruction and unavoidable global toll)

No paired-SCD central factor is a color pair in a full proper
\((m+1)\)-edge-coloring.  More quantitatively, its lower-incidence lift
has symmetric difference at least \(2D\) from every bichromatic lift.
Since both lifts have \(2N\) incidences, at least \(D\) old incidences must
be replaced.

#### Proof

The qualitative statement follows from (3.3): a bichromatic lift has no
middle vertex of degree zero.

For the quantitative statement let \(B\) be the \(2D\)-element endpoint
set of the bichromatic lift, and put \(t=|E\cap B|\).  The \(\ell^1\)
distance between the two middle-degree vectors is

\[
 t+2(D-t)+(2D-t)=4D-2t\ge2D.
 \tag{4.2}
\]

Every incidence in the symmetric difference has one middle endpoint, so
the symmetric difference is at least this degree distance.  Equal total
edge counts make the deleted and inserted halves equal. \(\square\)

The lower bound is sharp at \(m=2\), as Section 5 shows.  Globally, the
sharp \(D=\Theta(W/m)\) edit scale is \(o(W)\), so this obstruction rules
out the *literal* closed-seed interpretation but does not rule out a
coherently opened asymptotic construction.

There is a local port version.  Fix an exterior \((m-2)\)-set \(S\) and
four coordinates \(1,2,3,4\) outside it.  If the local paired cycle

\[
 S+14\;--\;S+12\;--\;S+23\;--\;S+34\;--\;S+14
 \tag{4.3}
\]

alternates the selected colors, then each locally omitted owner

\[
 S+13,qquad S+24
 \tag{4.4}
\]

must receive a selected-color incidence through a facet obtained by
deleting a coordinate of \(S\).  Indeed, both of its two local facets are
already incident through (4.3) to active owners, while a middle owner can
miss only one of the two selected colors.  Thus every family of closed
\(B_4\) contexts whose full six-owner sets are pairwise disjoint forces two
distinct exterior selected incidences per context.  Overlapping
contexts may share these ports; without an overlap bound this yields only
the global Catalan-scale toll of Theorem 4.1, not a linear-in-contexts
no-go.

## 5. The optimal open \(B_4\) atom

Let the colors be \(\alpha,\beta,\gamma\).  The following table assigns a
color to every incidence between a singleton and a two-set of \([4]\):

\[
\begin{array}{c|ccc}
 S&\multicolumn{3}{c}{X\supset S}\\ \hline
 1&12:\beta&13:\gamma&14:\alpha\\
 2&12:\alpha&23:\beta&24:\gamma\\
 3&13:\alpha&23:\gamma&34:\beta\\
 4&14:\gamma&24:\beta&34:\alpha
\end{array}
\tag{5.1}
\]

Every row contains all three colors, and the two colors at every middle
two-set are distinct.  Hence (5.1) is a proper 3-edge-coloring of \(H_2\).

The \(\alpha,\beta\) pair suppresses to

\[
 14--12--23,
 \qquad
 13--34--24.
 \tag{5.2}
\]

Its lower/upper diamond list is

\[
\begin{array}{c|c|c}
 \text{lower}&\text{Johnson edge}&\text{upper}\\ \hline
 1&14--12&124\\
 2&12--23&123\\
 3&13--34&134\\
 4&34--24&234.
\end{array}
\tag{5.3}
\]

Thus this pair is exactly lower-perfect, exactly upper-perfect, spanning,
and acyclic.  It is obtained from the closed paired-SCD cycle by replacing
the two edges of lower colors \(3,4\).

The four local pair maps have defects

\[
 \ell(123)=\ell(124)=0,
 \qquad
 \ell(134)=\ell(234)=1.
 \tag{5.4}
\]

For example, the three pair labels at \(134\) are

\[
 \alpha\gamma,\quad\alpha\beta,\quad\alpha\gamma,
 \tag{5.5}
\]

and those at \(234\) are

\[
 \beta\gamma,\quad\beta\gamma,\quad\alpha\beta.
 \tag{5.6}
\]

Hence

\[
 \mathfrak L(\kappa):=\sum_U\ell(U)=2.
 \tag{5.7}
\]

### Theorem 5.1 (\(B_4\) optimality)

Every proper 3-edge-coloring of \(H_2\) satisfies

\[
 \mathfrak L(\kappa)\ge2.
 \tag{5.8}
\]

Thus (5.1) is optimal.

#### Proof

Identify a middle two-set \(ij\) with the edge \(ij\) of \(K_4\), and
write \(\kappa_i(j)=\kappa(i,ij)\).  At each vertex \(i\), the three
values \(\kappa_i(j)\), \(j\ne i\), are all colors.  At each edge
\(ij\),

\[
 \kappa_i(j)\ne\kappa_j(i).
 \tag{5.9}
\]

For \(U=[4]\setminus\{l\}\), the pair label belonging to lower singleton
\(i\in U\) is the complement in \(\{\alpha,\beta,\gamma\}\) of
\(\kappa_i(l)\).  Therefore

\[
 \ell(U)=3-|\{\kappa_i(l):i\ne l\}|.
 \tag{5.10}
\]

Suppose first that all four defects vanish.  The direct half-edge count
(equivalently (6.2) below) then shows that the missing colors on
the six middle two-sets form a proper 3-edge-coloring of \(K_4\), hence
its three color classes are the three perfect matchings.  At a fixed
vertex \(i\), the incidence colors give a derangement of the three missing
colors on its incident edges.  Such a derangement is one of the two
3-cycles relative to one fixed cyclic order of the three colors; attach
its sign to \(i\).  On an edge \(ij\), condition (5.9)
forces the signs at \(i,j\) to be opposite.  This would 2-color \(K_4\),
which is impossible.  Hence \(\mathfrak L>0\).

It also cannot equal one.  If exactly one column \(l\) in (5.10) were
defective, the other three columns would each contain every color once.
Every color occurs exactly four times in the full directed incidence
table, once in each row.  The remaining column would therefore also have
to contain every color once, a contradiction.  Thus
\(\mathfrak L\ge2\), and (5.7) gives equality. \(\square\)

This proves both that the closed \(B_4\) atom is the wrong bichromatic
object and that an optimal open replacement exists.  It does not by itself
give a recursive coloring in larger dimension.

## 6. The universal exact target and its design obstruction

For \(U\in\mathcal U\) and \(c\in\mathscr C\), let

\[
 r_c(U)=|\{a\in U:\mu(U\setminus\{a\})=c\}|.
 \tag{6.1}
\]

Counting occurrences of color \(c\) among all half-edge labels in the
local complete graph gives the exact margin identity

\[
 \boxed{
 \sum_{p\ni c}h_p(U)=n-r_c(U).}
 \tag{6.2}
\]

Thus \(h_p(U)=1\) for all pairs forces

\[
 r_c(U)=1\qquad(c\in\mathscr C).
 \tag{6.3}
\]

Adjacent middle sets have a unique common upper union, so (6.3) makes the
missing-color map \(\mu\) a proper \(n\)-coloring of \(J(2m,m)\).  For
each lower set \(S\), its \(n\) middle extensions form a clique and hence
receive every missing color once.  Consequently every missing-color class
\(\mathcal E_c\) is a Steiner system

\[
 S(m-1,m,2m),
 \tag{6.4}
\]

and the \(n\) classes form a large set partition of \(\mathcal M\).

### Theorem 6.1 (complete divisibility obstruction)

The standard divisibility conditions for (6.4) all hold if and only if

\[
 m+1\ \text{is prime}.
 \tag{6.5}
\]

Therefore universal local Latinness is impossible whenever \(m+1\) is
composite.  Primality is only necessary, not sufficient.

#### Proof

Put \(n=m+1\).  The number of blocks through an \((m-s)\)-set would have
to be

\[
 \lambda_{m-s}=
 {\binom{m+s}{s-1}\over s}
 ={\binom{m+s}s\over m+1}
 ={\binom{n-1+s}s\over n}
 \tag{6.6}
\]

for every \(1\le s\le m=n-1\).

If \(n\) is prime, the product defining
\(\binom{n-1+s}s\) contains one factor divisible by \(n\), while \(s!\)
is prime to \(n\), so (6.6) is integral.

If \(n\) is composite, choose a prime \(p\mid n\) and take \(s=p\).
Then

\[
 \binom{n+p-1}p
 ={n\over p}\prod_{j=1}^{p-1}{n+j\over j}.
 \tag{6.7}
\]

Every ratio in the product has \(p\)-adic valuation zero, so

\[
 v_p\!\left(\binom{n+p-1}p\right)=v_p(n)-1.
 \tag{6.8}
\]

It is not divisible by \(n\), and (6.6) fails. \(\square\)

For \(m\ge2\), every system (6.4), if it exists, is also closed under
complementation.  Indeed, (6.6) with \(s=2\) first forces \(m\) even.  If
\(B\) is a block and \(d_0(B)\) is the number of design blocks disjoint
from it, inclusion-exclusion gives

\[
 d_0(B)=\sum_{i=0}^m(-1)^i\binom mi\lambda_i,
 \qquad \lambda_m=1.
 \tag{6.8a}
\]

Substitution of (6.6), followed by the elementary identity

\[
 \sum_{s=0}^m(-1)^s\binom ms\binom{m+s}s=(-1)^m,
 \tag{6.8b}
\]

which is Vandermonde after using
\((-1)^s\binom{m+s}s=\binom{-m-1}s\) and replacing
\(\binom ms\) by \(\binom m{m-s}\),

gives

\[
 d_0(B)=(-1)^m+{1-(-1)^m\over m+1}=1.
 \tag{6.8c}
\]

The unique \(m\)-set disjoint from \(B\) is \(B^c\), so \(B^c\) is a
block.  Thus the missing-color classes would resolve into complementary
pairs.  This recovers a parity shadow of the paired-SCD obstruction, but
is still only a necessary condition for the pair labels.

The divisibility obstruction has a quantitative residue version.  It is
important that its normalized strength vanishes.

### Theorem 6.2 (composite residue floor)

Assume \(n=m+1\) is composite, let \(p<n\) be a prime divisor of \(n\),
and put

\[
 T_{m,p}=\binom{m+p}{p-1}.
 \tag{6.9}
\]

Every proper base coloring satisfies

\[
 \boxed{
 \sum_U\ell(U)\ge {N\over2T_{m,p}}.}
 \tag{6.10}
\]

For odd \(m\ge3\), one may take \(p=2\), giving

\[
 \sum_U\ell(U)\ge {N\over2(m+2)}.
 \tag{6.11}
\]

#### Proof

For a lower set \(S\), let

\[
 t_c(S)=|\{X\supset S:\mu(X)=c\}|.
 \tag{6.12}
\]

Fix an \((m-p)\)-set \(I\).  There are \(T_{m,p}\) lower sets
\(S\supset I\).  If \(e_c(I)\) is the number of members of
\(\mathcal E_c\) containing \(I\), then

\[
 \sum_{S\supset I}(t_c(S)-1)=p e_c(I)-T_{m,p}.
 \tag{6.13}
\]

Because \(p\mid m+1\), one has \(T_{m,p}\equiv1\pmod p\).  Hence the
absolute value in (6.13) is at least one.  Summing over \(I\), and noting
that every \(S\) contains \(\binom{m-1}{p-1}\) such sets, gives

\[
 \sum_S|t_c(S)-1|\ge {N\over T_{m,p}}.
 \tag{6.14}
\]

Sum (6.14) over the \(n\) colors and call the result
\(\mathfrak D^-\).  Since \(\sum_St_c(S)=N\), holes and surplus in each
color row balance.  Therefore

\[
 {\mathfrak D^-\over2}
 \le\sum_{c,S}\binom{t_c(S)}2.
 \tag{6.15}
\]

Both sides of a monochromatic Johnson edge have a unique intersection and
a unique union, so

\[
 \sum_{c,S}\binom{t_c(S)}2
 =\sum_{U,c}\binom{r_c(U)}2.
 \tag{6.16}
\]

At a fixed \(U\), if
\(\sigma(U)=\sum_c(r_c(U)-1)_+\), then

\[
 \sum_c\binom{r_c(U)}2\le{n\over2}\sigma(U).
 \tag{6.17}
\]

The margin identity (6.2), together with
\(\sum_p|h_p(U)-1|=2\ell(U)\), gives

\[
 \sigma(U)\le2\ell(U).
 \tag{6.18}
\]

Equations (6.14)--(6.18) yield

\[
 {nN\over2T_{m,p}}
 \le {\mathfrak D^-\over2}
 \le n\sum_U\ell(U),
\]

which is (6.10). \(\square\)

Since \(Q=\Theta(m^2)\), the normalized bound

\[
 {\sum_U\ell(U)\over QN}\ge {1\over2QT_{m,p}}
 \tag{6.19}
\]

tends to zero.  Hence this proved residue/divisibility bound does **not**
obstruct the asymptotic near-Latin target (0.9).  A stronger stability
consequence of the divisibility failure has not been excluded, and no
positive stability gap is proved here.

## 7. Exact implication for a contextual \(B_4\) recursion

The preceding results give a sharp sufficient theorem which is independent
of how the coloring is generated.

### Theorem 7.1 (uniform contextual near-Latin output)

Let \(m\to\infty\), let \(H=H(m)=o(m)\), and suppose a contextual
\(B_4\), paired-SCD, or other recursion produces proper base colorings
\(\kappa_m\) with

\[
 \max_{U\in\mathcal U}\ell_{\kappa_m}(U)=b_m=o(m^2).
 \tag{7.1}
\]

Then there is a color pair \(p_m\) whose suppressed graph has

1. every lower color exactly once;
2. all \(W\) middle owners, with degree one or two;
3. exactly \(D\) path components and \(z_{p_m}\) cycle components;
4. at most
   \[
   \left\lfloor {b_mN\over Q}\right\rfloor=o(W)
   \tag{7.2}
   \]
   missing upper colors and exactly the same collision excess.

If in addition

\[
 z_{p_m}=o(W/H),
 \tag{7.3}
\]

then the total number of components is \(o(W/H)\).

#### Proof

Clauses 1--4 are Theorems 2.1 and 3.1.  Since
\(D=W/(m+1)=o(W/H)\), (7.3) gives the final assertion. \(\square\)

The average hypothesis (0.9) may replace (7.1), with the same conclusion
except for the explicit uniform bound (7.2).

The theorem identifies the exact recursive burden:

* closed \(B_4\) cycles must first be opened and their omitted-owner ports
  routed globally;
* the full family of pair matchings must satisfy the rootability clauses
  of Proposition 1.3, rather than being chosen independently;
* local collisions must total \(o(QN)\), but exact universal Latinness is
  neither needed nor generally possible;
* one low-defect pair must also have \(o(W/H)\) bichromatic cycles.

The open table (5.1) proves that these clauses are locally consistent and
that one distinguished pair can already be exact at \(m=2\).  No product
or outer recursion proving (7.1)--(7.3) is currently available.  In
particular, independent replication of the closed paired-SCD \(B_4\) atom
does not meet Proposition 1.3 and pays the exterior-port condition of
Section 4.

## 8. Relation to the central-diamond and constant-one programs

An exactly upper-perfect pair in Theorem 7.1 is a two-sided-rainbow
spanning path/cycle system, not a paired-SCD 2-factor.  The distinction is
structural:

\[
\begin{array}{c|c|c}
 &\text{paired-SCD central factor}&\text{bichromatic pair}\\ \hline
 \text{middle degrees}&0,2&1,2\\
 \text{defect support}&D\text{ isolated owners}&2D\text{ endpoints}\\
 \text{forced open components}&0&D.
\end{array}
\tag{8.1}
\]

Opening the defect costs at least \(D=o(W)\) incidence replacements, and
the \(B_4\) table shows this lower bound can be sharp.  Conversely,
closing a bichromatic path system into a 0/2 factor is a genuine endpoint
matching problem; its component count depends on the permutation obtained
by composing the old endpoint pairing with the closure matching.  Ordinary
Hall feasibility alone does not force few cycles.

For a coefficient-one proof, the q=1 conclusion still has to be composed
with literal physical ordering and the two-sided flags through all
\(q\le H\).  Local Latin-pair balance gives only the lower and upper
depth-one color ledger.  It does not supply:

1. radius-compatible lower/upper SCD tails;
2. signed \(H\)-run safety;
3. nested flags at depths \(q\ge2\); or
4. the cycle estimate (7.3).

Accordingly, Theorem 7.1 is a rigorous q=1 engine and a precise recursive
target, not a proof of the constant-one theorem.

## 9. Independent audit ledger

The decisive identities and obstructions were checked independently in

* `MATH_THEOREM_N_MPLUS1_EDGE_COLOR_PAIR_LATIN_ENGINE_20260726.md`;
* `MATH_OBSTRUCTION_N_MPLUS1_LATIN_STEINER_PRIME_AND_NEAR_DEFECT_20260726.md`;
* `MATH_THEOREM_BICHROMATIC_PAIRED_SCD_DEGREE_DEFECT_AND_OPEN_CLOSURE_20260726.md`;
* `MATH_THEOREM_N_PAIRED_SCD_RAINBOW_EQUIVALENCE_AND_COMPONENT_GATE_20260726.md`.

The following scope points are essential.

1.  The complete divisibility calculation proves a necessary prime
    condition for universal Latinness, not existence in prime dimensions.
2.  The residue lower bound (6.10) is subcritical after normalization and
    is not an asymptotic no-go.
3.  The optimal \(B_4\) table proves only a finite open seed; no growing
    recursion is inferred from it.
4.  The averaging theorem chooses a pair with small upper defect, but does
    not simultaneously minimize its bichromatic cycle count without an
    additional argument.
5.  Every statement remains integral inside the exact incidence/diamond
    systems.  No fractional matching is promoted to an exact factor.
