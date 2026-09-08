# The integral two-coordinate Catalan braid: prefix ports, diagonal min--max, and the exact forest gate

Date: 2026-07-31  
Lane: R, balanced-subcube integral recursion  
Status: exact all-\(n\) reduction, an all-\(n\) nonempty circuit family, one
independently replayed positive \(n=3\to4\) integral braid, an all-\(n\)
canonical-BTK degree obstruction, and exact product audits through \(n=7\).
The all-\(n\) diagonal-forest existence theorem remains open.

## 0. Result

Let the ambient parameter be \(m=n+1\), split off collar coordinates
\(\{c,z\}\), and freeze the parameter-\(n\) child on trace \(\{c\}\).
The fractional five-block flow of Theorem 5.3 in
`MATH_THEOREM_CATALAN_BALANCED_SUBCUBE_RESERVE_AND_EXACT_COLLAR_DEFECT_20260731.md`
has an exact integral normal form and an exact remaining gate.

1. The five trace totals are forced:
   \[
      (00,0z,zz,zcz,czcz)=(P,C,R,C,P).                 \tag{0.1}
   \]
   Therefore every genuine rethread has zero projection to this five-count
   quotient.  A trace-only LP has no correction direction.

2. For **every** parameter-\(n\) Catalan path forest \(F\), a path-prefix
   construction chooses \(C=\operatorname{Cat}_{n+1}\) peeled edges \(Q\)
   and a common \(C\)-vertex port bank \(B\).  The same bijection
   \(Q\to B\) simultaneously satisfies the lower and upper port containments,
   and \(F-Q\) avoids \(B\).  Thus the central pruning and both port-Hall
   rows are automatic; no matroid-intersection hypothesis remains there.

3. What remains is exactly two collision-capacitated diagonal perfect
   matchings.  Their fractional feasibility has an explicit assignment
   min--max theorem.  Integral selection, graphic acyclicity, and the
   coupling of the two diagonal component systems remain separate.

4. Once the diagonal supports are fixed, the whole complement is a linear
   forest if and only if the three rail supports are forests, every port is
   attached at a legal endpoint, and the contracted port multigraph is a
   forest.  In the common-prefix form this contracted graph is bipartite and
   must be a path forest.  This is an exact physical criterion, not an
   inference from fractional feasibility.

5. The marginal-preserving circuit fibre is nonempty for every \(n\ge2\):
   an explicit suspended P3 changes opposite heads while preserving all
   lower, upper, and tail resources.  P1 and P2 are impossible.

6. The first strict five-block case is positive.  A literal
   \(n=3\to m=4\) construction has all 56 lower and upper resources once,
   56 distinct physical edges on all 70 middle vertices, degree profile
   \(0^4 1^{20}2^{46}\), and 14 path components.  It is independently
   replayed.

7. The unmodified canonical BTK diagonal choice is not the induction.  At
   \(n=3\) it has only 13 legal endpoint sockets for 14 ports.  For every
   \(n\ge4\), one explicit physical vertex has BTK diagonal degree at least
   \(n-1>2\).  The positive \(n=3\to4\) construction uses different
   diagonals and therefore escapes this scoped obstruction.

The exact all-\(n\) missing theorem is now only a **forest-compatible
realization of an automatic common deletion basis**, stated in Section 9.
The paired prefix-diagonal braid is one explicit stronger sufficient
subclass.  No physical acyclicity is claimed from the fractional recursion
or from common-basis incidence alone.

## 1. Forced five-sector arithmetic

Let \(R_0\) be the \(2n\)-coordinate core.  Put

\[
\begin{aligned}
 K&=\operatorname{Cat}_n,\\
 M&=\binom{2n}{n},&N&=\binom{2n}{n-1}=M-K,\\
 P&=\binom{2n}{n-2},&C&=M-P=\operatorname{Cat}_{n+1},\\
 R&=N-C=P-K.                                           \tag{1.1}
\end{aligned}
\]

The complement lower trace classes \(0,z,cz\) have orders \(M,N,P\),
while the complement upper trace classes have orders \(P,N,M\).  Avoiding
the child middle trace \(c\) leaves exactly the transitions

\[
                  00,\quad0z,\quad zz,\quad zcz,\quad czcz.       \tag{1.2}
\]

### Theorem 1.1 (the trace polytope is a point)

Every fractional or integral outer-perfect complement supported on (1.2)
has sector totals (0.1).  It exists only if \(R\ge0\), which holds exactly
from \(n=3\) onward.

#### Proof

Write the five totals as \(x_{00},x_{0z},x_{zz},x_{zcz},x_{czcz}\).
The upper trace-0 column and lower trace-\(cz\) row force

\[
                  x_{00}=P,\qquad x_{czcz}=P.
\]

The lower trace-0 row and upper trace-\(cz\) column then force

\[
                  x_{0z}=M-P=C,\qquad x_{zcz}=M-P=C.
\]

Finally either trace-\(z\) equation gives \(x_{zz}=N-C=R\).
The binomial quotient gives

\[
 {R\over M}={n^2-2n-2\over(n+1)(n+2)},
\]

which is nonnegative exactly for integral \(n\ge3\). \(\square\)

### Corollary 1.2 (trace blindness)

Every signed trade supported on the five allowed transitions (1.2) and
preserving the outer palettes has zero change in all five totals.  Hence a
flow or separating functional on only those five trace blocks cannot
distinguish a repair from the starting state.  Trades using child-crossing
transitions lie outside this fibre.  Occurrence labels, head loads, port
sockets, and component identities are indispensable.

## 2. What must be unfrozen

An ordered complement atom is \(e=(L,U,T,H)\), where

\[
 |L|=n,\qquad |T|=|H|=n+1,\qquad |U|=n+2,
\]

and

\[
                   H=L\cup(U\setminus T).                         \tag{2.1}
\]

### Lemma 2.1 (literal triple-freeze rigidity)

If every supplied nonchild triple \((L,U,T)\) is frozen occurrencewise,
then the feasible face is a singleton and no opposite-head-changing circuit
exists.

#### Proof

Equation (2.1) determines each head separately. \(\square\)

Thus “freeze the matching” must mean freeze the child and the three
**marginal banks** of lower, upper, and tail resources, while allowing their
associations to change.

Index a finite old atom bank by \(i\).  Every marginal-preserving trade has
the normal form

\[
 (L_i,U_i,T_i)\longmapsto
 (L_i,U_{\sigma(i)},T_{\tau(i)}),                       \tag{2.2}
\]

for permutations \(\sigma,\tau\), subject to

\[
                  L_i\subset T_{\tau(i)}\subset U_{\sigma(i)}.    \tag{2.3}
\]

The new heads are then forced by (2.1).  Minimal supports of the integer
kernel of the three marginal incidence matrices are the relevant
alternating bitrades; they are not ordinary graph cycles in general.

### Lemma 2.2 (no marginal P2)

No nontrivial two-atom marginal-preserving trade exists.

#### Proof

For two atoms there are three nonidentity choices for
\((\sigma,\tau)\).

* If only \(\sigma\) swaps, both distinct rank-\((n+1)\) tails lie in
  \(U_1\cap U_2\), whose size is at most \(n+1\); hence the tails coincide.
* If only \(\tau\) swaps, both distinct rank-\(n\) lowers lie in
  \(T_1\cap T_2\), whose size is at most \(n\); hence the lowers coincide.
* If both swap, each of the two rank-\((n+1)\) tails contains both lower
  sets.  Their union has size at least \(n+1\), so the two tails coincide.

Each conclusion contradicts the corresponding marginal injectivity.
\(\square\)

## 3. Prefix banks solve the central and port rows

Let \(F\) be any parameter-\(n\) Catalan linear matching, viewed as a
spanning \(K\)-path forest on the \(M\) rank-\(n\) vertices with \(N\)
edges.  Orient every component

\[
                 v_{i,0},v_{i,1},\ldots,v_{i,\ell_i},              \tag{3.1}
\]

so \(\sum_i\ell_i=N\).

### Theorem 3.1 (common prefix-bank theorem)

For every \(n\ge3\), there are integers
\(0\le s_i\le\ell_i\) with \(\sum_i s_i=C\).  Put

\[
\begin{aligned}
 B&=\{v_{i,j}:0\le j<s_i\},\\
 Q&=\{v_{i,j}v_{i,j+1}:0\le j<s_i\}.                   \tag{3.2}
\end{aligned}
\]

Then:

1. \(|B|=|Q|=C\);
2. \(F-Q\) has exactly \(R\) edges and no edge incident with \(B\);
3. \(q_{i,j}=v_{i,j}v_{i,j+1}\mapsto v_{i,j}\) is a bijection
   \(Q\to B\); and
4. writing \(L(q)=x\cap y\), \(U(q)=x\cup y\) for \(q=xy\), the same map
   gives simultaneous port bijections
   \[
      p^-:U(Q)\to B,qquad p^+:L(Q)\to B,               \tag{3.3}
   \]
   with \(p^-(U)\subset U\) and \(L\subset p^+(L)\).

#### Proof

Theorem 1.1 gives \(N-C=R\ge0\), so the total interval
\(\sum_i[0,\ell_i]\) contains \(C\); choose the \(s_i\) greedily.
Each selected prefix vertex is paired with its forward edge, proving the
bijection in (3).  Removing those forward edges isolates every selected
prefix vertex from the suffix forest and deletes exactly \(C\) edges, so
(1)--(2) follow.  Finally, every endpoint \(v_{i,j}\) of a Johnson edge
\(q=xy\) lies between its intersection and union.  Since a Catalan linear
matching has distinct lower and upper colours, (3.3) is bijective on both
shores. \(\square\)

This theorem removes the previous common-basis/matroid-intersection gate.
It does **not** construct the two diagonal matchings on

\[
                       D=\binom{R_0}{n}\setminus B,qquad |D|=P.   \tag{3.4}
\]

For \(n\ge4\), the Kruskal--Katona/Edmonds theorem
MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md
is stronger at the incidence level: without requiring a common prefix
bank, it chooses a deletion set \(Q\) for which both diagonal containment
matchings exist simultaneously.  Theorem 3.1 is retained as an explicit
physical normal form and as the source of the positive base; incidence Hall
is not counted among the remaining all-\(n\) gates.

## 4. Exact diagonal collision LP and min--max cut

Consider the upper diagonal sector \(00\).  It must perfectly match
\(D\) to \(\mathcal W^-:=\binom{R_0}{n+2}\).  A candidate \(d\subset V\)
has two physical intermediate vertices

\[
 I(d,V)=\{d+x,d+y\}\subset\mathcal V^-:=\binom{R_0}{n+1},
 \qquad V\setminus d=\{x,y\}.                          \tag{4.1}
\]

The upper endpoints \(P^-:=U(Q)\) already receive one port edge.  Hence
the remaining diagonal capacity is

\[
 b_X^-=
 \begin{cases}
 1,&X\in P^-,\\
 2,&X\notin P^-.
 \end{cases}                                             \tag{4.2}
\]

The exact fractional collision system is

\[
\begin{aligned}
 \sum_{V\supset d}x_{dV}&=1 &&(d\in D),\\
 \sum_{d\subset V}x_{dV}&=1 &&(V\in\mathcal W^-),\\
 \sum_{(d,V):\,d\subset X\subset V}x_{dV}&\le b_X^-
      &&(X\in\mathcal V^-),\\
 x_{dV}&\ge0.                                             \tag{4.3}
\end{aligned}
\]

### Theorem 4.1 (exact fractional diagonal min--max)

For \(\gamma\in\mathbb R_{\ge0}^{\mathcal V^-}\), define

\[
 \kappa_D^-(\gamma)=
 \min_{\mu:D\overset\sim\longrightarrow\mathcal W^-}
 \sum_{(d,V)\in\mu}\ \sum_{X\in I(d,V)}\gamma_X,        \tag{4.4}
\]

where \(\mu\) ranges over containment perfect matchings and the minimum is
\(+\infty\) if none exists.  System (4.3) is feasible if and only if

\[
            \kappa_D^-(\gamma)\le\sum_Xb_X^-\gamma_X
            \qquad\text{for every }\gamma\ge0.            \tag{4.5}
\]

Equivalently, for every \(\gamma\ge0\) and every assignment-dual pair
\(\alpha_d,\beta_V\in\mathbb R\) satisfying

\[
       \alpha_d+\beta_V\le
       \sum_{X\in I(d,V)}\gamma_X\qquad(d\subset V),    \tag{4.6}
\]

one must have

\[
             \sum_d\alpha_d+\sum_V\beta_V
             \le\sum_Xb_X^-\gamma_X.                     \tag{4.7}
\]

#### Proof

The bipartite perfect-matching polytope on \(D\sqcup\mathcal W^-\) is the
convex hull of its integral perfect matchings.  Take the convex hull of the
finite set of their intermediate-load vectors.  This hull meets the
coordinatewise down-set \(\{y:y\le b^-\}\) exactly when every nonnegative
separating functional satisfies (4.5).  The equality of (4.4) with the
maximum in (4.6)--(4.7) is the ordinary assignment duality theorem.
\(\square\)

The lower diagonal \(czcz\) has the dual system on ranks
\(n-2,n-1,n\), with the lower port endpoints \(P^+:=L(Q)\).

Theorem 4.1 is **fractional only**.  The capacities in (4.2)--(4.3) already
enforce the required degree bounds.  An integral diagonal must additionally
have \(x_{dV}\in\{0,1\}\) and satisfy the graphic inequalities

\[
 \sum_{dV:I(d,V)\subseteq S}x_{dV}\le |S|-1
 \quad(\varnothing\ne S\subseteq\mathcal V^-)             \tag{4.8}
\]

must hold; the lower side is analogous.  Neither (4.5) nor bipartite
integrality implies (4.8).

## 5. The exact three-rail forest criterion

Let \(D^-\) and \(D^+\) be chosen upper and lower diagonal physical
supports, regarded as spanning graphs on their complete rank-
\((n+1)\) and rank-\((n-1)\) core banks.  Let \(F_0=F-Q\) be the spanning
central \(z\)-rail graph on all \(M\) rank-\(n\) core vertices.  Its
vertices \(B\) are isolated and then used as the common port vertices.  The
port edges are

\[
\begin{aligned}
 E^-&=\bigl\{\,\{U(q),\{z\}\cup p(q)\}:q\in Q\,\bigr\},\\
 E^+&=\bigl\{\,\{\{z\}\cup p(q),\{c,z\}\cup L(q)\}:q\in Q\,\bigr\}.
                                                                  \tag{5.1}
\end{aligned}
\]

For each \(q\), its edge in \(E^-\) followed by its edge in \(E^+\) is the
two-edge path
\[
            U(q)-\bigl(\{z\}\cup p(q)\bigr)
                 -\bigl(\{c,z\}\cup L(q)\bigr).
\]
Suppressing collar tags, the complete complement support is

\[
                G=D^-\cup E^-\cup F_0\cup E^+\cup D^+.            \tag{5.2}
\]

### Theorem 5.1 (collision graph and forest criterion)

The support \(G\) is a linear forest if and only if all of the following
hold.

1. \(D^-\), \(F_0\), and \(D^+\) are forests.
2. Every diagonal port endpoint has diagonal degree at most one; all other
   diagonal vertices have degree at most two.  Every central port vertex is
   isolated in \(F_0\).
3. Contract every component of \(D^-\sqcup F_0\sqcup D^+\), and suppress
   the degree-two vertex \(z+p(q)\) in each paired port path.  The resulting
   component multigraph is acyclic.

Under the prefix construction, \(F_0\) has no incident port, and the only
nontrivial contracted coupling is a bipartite graph \(J\) between components
of \(D^-\) and \(D^+\), with one edge per \(q\in Q\).  Conditions 2--3 say
exactly that \(J\) is a path forest: Condition 2 permits at most two legal
endpoint ports on each diagonal path component, and Condition 3 excludes
cycles.

#### Proof

The three rails have disjoint collar traces.  If \(G\) is a linear forest,
each induced rail is a forest, every added port meets an endpoint or isolate,
and contraction cannot create a cycle; necessity follows.

Conversely, Condition 1 makes the disjoint rail union a forest.  Condition
2 attaches every port only at a legal endpoint and bounds the final degree
by two.  For a forest, adding edges creates a cycle exactly when their image
after contracting old components contains a loop or cycle.  Condition 3
therefore gives acyclicity, and the degree bound makes the result a linear
forest.  In the prefix case each common port already has its two port edges,
while Theorem 3.1 makes it isolated in \(F_0\), giving the final statement.
\(\square\)

Here component counts include all ambient vertices of each rail.  The
spanning graph \(F_0\) has \(C+K\) components: \(C\) singleton vertices in
\(B\) that become internal port vertices, and \(P-R=K\) suffix components
on \(D\).  If both diagonals are forests, each has \(N-P=C-K\)
components.  After suppressing the \(C\) internal port vertices, a forest
\(J\) has \(C-2K\) components.  Adding the \(K\) untouched suffix
components, the complement has \(C-K\) components, and
adjoining the \(K\)-component child gives exactly \(C=\operatorname{Cat}_{n+1}\)
paths, as required.

### Theorem 5.2 (automatic-basis physical gate)

Let \(n\ge4\), let \(F\) be an oriented child Catalan path forest, and let
\(Q\) be a common deletion basis supplied by the automatic-common-basis
theorem.  Use the inherited ports

\[
                   p^-(U_q)=t_q,\qquad p^+(L_q)=h_q
                                                                  \tag{5.3}
\]

for the oriented child edge \(q=t_qh_q\).  Let \(G^-\) and \(G^+\) be
physical representatives of the two guaranteed diagonal containment
matchings.  The five-sector complement is a linear forest if and only if:

1. \(G^-\), \(F-Q\), and \(G^+\) are forests;
2. both side graphs have maximum degree at most two, with
   \(d_{G^-}(U_q)\le1\) and \(d_{G^+}(L_q)\le1\) for every \(q\in Q\);
   and
3. after contracting all components of the three rail forests, the
   \(2C\) seam edges \(U_qt_q\) and \(h_qL_q\) form an acyclic multigraph
   \(\Gamma_Q\).

Under Condition 2 every component of \(\Gamma_Q\) has degree at most two,
so Condition 3 is equivalently the absence of a closed transition orbit.

#### Proof

The inherited ports replace the two incidences of every deleted child edge
one-for-one, so the central rail retains exactly its old degree profile.
Conditions 1--2 are therefore exactly the remaining degree/forest rows.
Contraction preserves cycle rank: adding the seams creates a physical cycle
if and only if their component multigraph contains a loop, parallel pair,
or ordinary cycle.  Finally each side path component has at most two legal
endpoint anchors, and each central path fragment has at most two cut
boundaries, proving the transition-orbit statement. \(\square\)

The common-prefix interface of Theorem 5.1 and the inherited-port interface
of Theorem 5.2 are different exact normal forms.  The former makes every
port pair a literal two-edge path through one isolated central vertex; the
latter is the broader interface for which incidence existence is automatic.

## 6. The first marginal circuit is a suspended P3

Partition the \(2n\)-coordinate core into four displayed labels
\(3,4,5,6\), a common \((n-2)\)-set \(K_0\), and an unused
\((n-2)\)-set \(W_0\), all pairwise disjoint and disjoint from the collar
\(\{c,z\}\).  Suppress \(K_0\) in the notation below and leave \(W_0\)
absent.  The following three old and three new atoms avoid the child trace
and preserve the lower, upper, and tail banks:

\[
\begin{array}{c|c|c|c|c}
 &L&T&U&H&\text{sector}\\ \hline
\text{old}&34&345&3456&346&00\\
          &z3&z34&z345&z35&zz\\
          &36&346&z346&z36&0z\\ \hline
\text{new}&34&345&z345&z34&0z\\
          &z3&z34&z346&z36&zz\\
          &36&346&3456&356&00.
\end{array}                                                     \tag{6.1}
\]

### Theorem 6.1 (all-\(n\) local fibre supply)

For every \(n\ge2\), (6.1), after adjoining \(K_0\), is a valid
marginal-preserving P3.  Full ground-set complementation, reversal of the
lower/upper roles
\((L,U,T,H)\mapsto(\overline U,\overline L,\overline T,\overline H)\),
and then swapping \(c,z\) gives the analogous circuit on sectors
\(\{zz,zcz,czcz\}\).  Together with Lemma 2.2, P3 is the first possible
marginal circuit layer.

For a current linear forest, such a P3 is physically admissible if and only
if:

1. its new heads are pairwise distinct and avoid every unchanged head; and
2. after deleting the three old physical edges, the three new edges are
   independent in the graphic matroid contracted by the remaining forest.

#### Proof

Direct intersection and union in (6.1) verify every atom.  The lower and
tail columns are unchanged rowwise, while the three uppers are cyclically
permuted, proving marginal balance.  The unused coordinates give the right
ground-set size without changing any relation.

For the guarded statement, lower, upper, and tail injectivity are already
fixed.  The first condition is exactly head injectivity.  Once both roles
are injective, physical degree is at most two.  The second condition is
exactly the absence of a new undirected cycle. \(\square\)

This proves circuit **supply**, not that a specified frozen factor contains
the old side of (6.1), nor that a compatible packet cover exists.

## 7. A literal positive \(n=3\to4\) integral braid

On the six core coordinates take the five paths

```text
07-13-1a-2a
0b-0d-2c-38
0e-26-25-15
16-1c-19-31
29-23-32-34
```

Orient the first two paths as displayed and the last three in reverse.  In
these orientations the common port bank below is literally a union of path
prefixes:

```text
B={07,0b,0d,13,15,19,1c,23,25,26,2c,31,32,34}.
```

The 14 peeled edges are paired with their prefix endpoint as recorded in
the audit artifact.  The only retained central edge is `1a-2a`.  The two
diagonal matchings are

```text
upper: 29->2f, 2a->3e, 0e->1f, 1a->3b, 38->3d, 16->37;
lower: 01->29, 20->38, 10->1a, 08->0e, 04->16, 02->2a.
```

With \(c=0x40,z=0x80\), literal materialization and an independent consumer
audit give:

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
\text{rank-3 lowers / rank-5 uppers}&56/56\text{, both bijective}\\
\text{tails / heads}&56/56\text{, both injective}\\
\text{distinct physical edges}&56\\
\text{middle degree profile}&0^4 1^{20}2^{46}\\
\text{cycle rank}&0\\
\text{component sizes}&1^4,2,3^2,4^5,12,26.
\end{array}                                                     \tag{7.1}
\]

Hence this is an exact Catalan linear matching at parameter 4, obtained by
the strict five-sector recursion.  It proves the integral braid class is
nonempty; it is not an all-\(n\) construction.

## 8. Canonical BTK is a scoped obstruction, not the braid

The canonical BTK SCD supplies diagonal matchings by taking the rank-\(n\)
member of every chain reaching ranks \(n\pm2\).  The following direct
degree obstruction holds in every dimension and does not require knowing
whether the entire diagonal support is acyclic.

### Theorem 8.1 (all-\(n\) canonical-BTK degree obstruction)

Use the standard BTK word convention: scan positions \(1,\ldots,2n\),
regard 0 as an opening bracket and 1 as a closing bracket, and greedily
match each 1 to the latest unmatched 0.  For every \(n\ge3\), the upper
BTK diagonal contains a rank-\((n+1)\) physical vertex of degree at least
\(n-1\).  Consequently the canonical BTK diagonal cannot be a side forest
for any \(n\ge4\).  One obstructed shore already rules out the canonical
pair; no symmetry claim about the other shore is needed.

#### Proof

Write words from left to right in the scan order and put

\[
                     X_n=1110(10)^{n-2}.                \tag{8.1}
\]

This word has length \(2n\) and weight \(n+1\).  For each of the
\(n-2\) displayed occurrences of 01 beginning at positions
\(4,6,\ldots,2n-2\), let \(Y_j\) be obtained by changing that 01 to 10.
Put \(d_j=X_n\cap Y_j\) and \(V_j=X_n\cup Y_j\).  A direct bracket scan
shows that \(d_j,V_j\) have the same matched pairs: all the other displayed
01 pairs are matched, while the free positions are

\[
                 1,2,3,2j,2j+1,2n
\]

after writing \(2j\in\{4,6,\ldots,2n-2\}\).  On those free positions the
two words are respectively 111000 and 111110.  Hence they are the rank-
\(n\) and rank-\((n+2)\) members of one BTK chain.  Its diagonal physical
edge is exactly \(X_nY_j\).

There is one further incident edge.  Let \(Y_*\) be obtained from \(X_n\)
by changing position 3 from 1 to 0 and position \(2n\) from 0 to 1.  For
\(d_*=X_n\cap Y_*\) and \(V_*=X_n\cup Y_*\), all \(n-2\) displayed 01
pairs are matched, the free positions are \(1,2,3,2n\), and the free-bit
patterns are 1100 and 1111.  Thus \(d_*,V_*\) lie two ranks apart on one
BTK chain and contribute the edge \(X_nY_*\).

The \(n-1\) neighbours \(Y_j,Y_*\) are distinct, so
\(d_{\rm BTK}(X_n)\ge n-1\).  \(\square\)

The lightweight audit below additionally verifies that, for
\(n=3,\ldots,7\), both canonical diagonal supports are forests and records
their exact socket and degree profiles:

The exact lightweight audit gives:

\[
\begin{array}{c|rrrrr|rr|l}
n&M&N&P&C&R&\Delta(D^-)&|\text{one-port sockets}|&\text{verdict}\\ \hline
3&20&15&6&14&1&2&13&13<14\\
4&70&56&28&42&14&3&44&\Delta>2\\
5&252&210&120&132&78&4&154&\Delta>2\\
6&924&792&495&429&363&5&552&\Delta>2\\
7&3432&3003&2002&1430&1573&6&2013&\Delta>2.
\end{array}                                                     \tag{8.1}
\]

At \(n=3\), the 14 distinct upper port endpoints would all need vertices
of diagonal degree at most one, but only 13 such vertices exist.  From
\(n=4\) onward Theorem 8.1 shows that the diagonal support itself already
has degree at least three, which adding ports cannot repair.  Coordinate
relabelling preserves these graph invariants.

The unchanged product-SCD state is also immobile under literal triple
freezing.  For \(n=3,\ldots,7\), its nonchild edge-support is acyclic but
has respectively

\[
\begin{array}{c|rrrrr}
n&3&4&5&6&7\\ \hline
\#\text{ nonchild flags}-\#\text{ distinct heads}&11&49&204&825&3289\\
\text{branched edge-components}&6&24&85&291&994\\
\text{maximum degree}&4&5&6&7&8.
\end{array}                                                     \tag{8.2}
\]

Here “edge-components” omits isolated ambient middle vertices.  An explicit
literal collision exhibited by the audit at \(n=3\) is

\[
(L,T,U)=(0x13,0x17,0x37),\quad(0x32,0x72,0x73),
\]

both forcing \(H=0x33\).  Lemma 2.1 then closes that literal frozen face.

Tables (8.1)--(8.2) rule out only the canonical supplied incidences.  The
positive construction in Section 7 uses a different prefix bank and
different diagonals, so there is no contradiction.

## 9. Exact remaining all-\(n\) theorem

The weakest exact remaining statement is now the following.

> **Forest-compatible common-basis realization \(\mathrm{FCBR}(n)\).**
> For every recursively supplied parameter-\(n\) Catalan path forest \(F\)
> (or, more weakly, for at least one such \(F\) at each induction step),
> some automatic common deletion basis \(Q\) and some physical
> representatives of its two guaranteed diagonal matchings satisfy all
> three conditions of Theorem 5.2.

Incidence Hall and synchronized common-basis existence are theorems and
are not hypotheses in \(\mathrm{FCBR}(n)\).  The only choices left are the
side physical representatives and their anchor transition system.

The independently audited topology-decoupling theorem further shows that,
on the no-anchor-free face, one realized left anchor pairing can always be
completed by an *abstract* right pairing because
\(C>2\operatorname{Cat}_n\).  This does not permit an arbitrary prescribed
physical pairing: the exact endpoint-distance budget

\[
       \sum_{\{X,Y\}\text{ paired}} d_J(X,Y)\le P
\]

already refutes universality at \(n=3\).  The viable shore-local target is
therefore an adaptive cross-component ear property, or equivalently an
intersection between the two physically realizable pairing families and
the acyclic pairing relation.  This sharpening is recorded in
MATH_AUDIT_R_CATALAN_SIDE_ANCHOR_PAIRING_TOPOLOGY_DECOUPLING_20260731.md
and
MATH_THEOREM_R_TWO_COORDINATE_SIDE_TURN_FOREST_AND_CAPACITY_CUT_20260731.md.

The following prefix form is a stronger, especially explicit sufficient
statement.

> **Paired diagonal-forest braid \(\mathrm{PDFB}(n)\).**  For every
> parameter-\(n\) Catalan path forest \(F\), some oriented prefix bank from
> Theorem 3.1 admits integral upper and lower diagonal perfect matchings
> satisfying their collision capacities and graphic inequalities, such that
> the contracted bipartite socket graph \(J\) is a forest.

Theorem 3.1 supplies the central suffix and both port bijections in that
strict prefix form.  Theorems 4.1, 5.1, and 5.2 give exact, checkable
physical cut certificates.  The positive \(n=3\to4\) artifact proves
\(\mathrm{PDFB}(3)\) for one child forest, not for every child forest.
Theorem 8.1 proves only that the canonical BTK representative cannot prove
\(\mathrm{FCBR}(n)\); it is not an obstruction to other side matchings.
No proof of \(\mathrm{FCBR}(n)\) or \(\mathrm{PDFB}(n)\) for all \(n\), and
therefore no all-dimensional Catalan linear matching theorem, is claimed.

## 10. Frozen artifacts

The theorem and companion audit cite the following literal files:

```text
scratch/audit_catalan_a1_integral_braid_btk_gate_20260731.py
scratch/catalan_a1_integral_braid_btk_gate_20260731.audit.json
scratch/audit_catalan_a1_n3_to_n4_integral_braid_20260731.py
scratch/catalan_a1_n3_to_n4_integral_braid_20260731.audit.json
scratch/verify_catalan_a1_n3_to_n4_integral_braid_20260731.py
scratch/catalan_a1_n3_to_n4_integral_braid_20260731.independent.audit.json
```

The stale raw GLOP output made before correction of the reserve-touch
predicate is quarantined as
`scratch/balanced_subcube_trace_lp_m3_m8_20260731.STALE_BUGGY.json` and is
not evidence for any claim above.
