# Thread AD: erosion-safe de-Bruijn flow and the fixed-skeleton occurrence gate

Date: 2026-07-28

Status: pure-mathematical theorem package.  The ordered erosion
representation criterion, its one-turn obstruction, the erosion-safe
integer-flow theorem, and the fixed-\(z\) transportation/TU factorization
are proved.  The fixed-skeleton reduction is used only in its audited
right-degree-one scope.  No \(k=15\) word and no coefficient-one theorem is
claimed.

## 0. Outcome

Fix a rank-\(r\) Johnson chronology

\[
 T_0,T_1,\ldots,T_{N-1}
\]

and a protected depth \(d\).  The exact bridge between the all-depth trace
tower and one erosion-letter word has four parts.

1. The current safe-de-Bruijn graph \(D_d(k,r)\) is one transition too
   short for the depth-\(d\) erosion compiler.  Its rows through depth \(d\)
   exclude returns

   \[
   b_i=a_{i+t}\qquad(1\le t\le d-1),
   \]

   but do not exclude the wall return

   \[
   \boxed{b_i=a_{i+d}.}
   \tag{0.1}
   \]

   A single such return leaves every lower and upper trace through depth
   \(d\) at the correct rank, but prevents any erosion word from realizing
   the prescribed depth-\((d-1)\) lower occurrence.

2. Once (0.1) is excluded, the endpoint-capped maximal erosion gives a
   literal word of length \(N+d\).  The prescribed ordered rows are
   representable if and only if their lower and upper recurrences hold and
   consecutive deepest lower traces are Johnson-adjacent.  This is one
   exact extra turn cut, not another rankwise marginal condition.

3. For a fixed integral safe-de-Bruijn arc multiset \(z\), erosion-compatible
   Euler orderings are exactly the integral points of an allowed-turn
   transportation system with connected support.  After fixing a spanning
   tree of the positive turn support, that system is totally unimodular.
   Thus owner multiplicities and all lower/upper trace multiplicities may
   be fixed first in \(z\), while the remaining residence wall is imposed
   by an integral transportation flow.  Its connected **integer** points
   are a finite union of integer points of fixed-tree TU pieces.

4. For pairwise distinct underlying subset targets, a fixed trace-two
   controller skeleton adds no residual matching problem.  It adds only
   target-occurrence requirements

   \[
   \bigcup_{p\in I_c}Q_p=S
   \]

   together with base eligibility and controller-footprint containment.
   These occurrence requirements can be put into a bounded-memory decorated
   Euler graph.  They are not consequences of the transportation marginals.

There is also a sharp TU boundary.  The fixed-order erosion-letter block is
an interval matrix and is TU.  The chronology-selection block is not: the
natural erosion-safe state-incidence plus middle-owner matrix already
contains a determinant-\(2\) minor, including at

\[
(k,r,d)=(15,8,3).
\]

Therefore the positive theorem is an **integral-flow theorem**, not an
unqualified LP-integrality theorem.

## 1. Trace notation and two notions of safety

Let \(K\) be a \(k\)-element ground set, and assume

\[
 1\le d\le \min\{r-1,k-r\},
 \qquad
 N\ge d+2.
 \tag{1.1}
\]

Let

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\},
 \qquad 0\le i\le N-2,
 \tag{1.2}
\]

be a rank-\(r\) Johnson chronology.  Put

\[
 L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h},
 \qquad
 U_i^{(q)}=\bigcup_{h=0}^{q}T_{i+h}
 \tag{1.3}
\]

for \(0\le q\le d\) and \(0\le i<N-q\).

The chronology is **two-sided \(d\)-safe** when

\[
 |L_i^{(q)}|=r-q,
 \qquad
 |U_i^{(q)}|=r+q
 \tag{1.4}
\]

for every displayed \(i,q\).  This is exactly the local condition encoded
by the safe graph \(D_d(k,r)\).

The chronology is **\(d\)-erosion-safe** when it is two-sided \(d\)-safe
and every internally bounded positive coordinate run has length at least
\(d+1\).

### Lemma 1.1 (the single missing wall)

A two-sided \(d\)-safe chronology is \(d\)-erosion-safe if and only if

\[
\boxed{
 b_i\ne a_{i+d}
 \qquad(0\le i\le N-d-2).}
\tag{1.5}
\]

#### Proof

Suppose \(b_i=a_{i+t}\) for some \(1\le t\le d-1\).  In the
\((t+1)\)-transition window

\[
T_i,T_{i+1},\ldots,T_{i+t+1},
\]

the last deleted label was not in \(T_i\).  Hence at most \(t\) elements of
\(T_i\) disappear, so the intersection has rank at least \(r-t\), larger
than \(r-(t+1)\).  This contradicts (1.4).  Thus two-sided \(d\)-safety
already excludes every return delay \(t<d\).

An internally bounded positive run of length \(t\) is precisely an
insertion \(b_i\) followed by the deletion \(a_{i+t}\).  The only remaining
forbidden length is therefore \(t=d\), which is exactly (1.5).
\(\square\)

### Proposition 1.2 (small local obstruction)

Assume

\[
 r\ge d+1,\qquad k-r\ge d+1.
 \tag{1.6}
\]

There is a two-sided \(d\)-safe Johnson chronology on \(d+2\) owners which
is not \(d\)-erosion-safe and whose all-depth rows through \(d\) have their
correct ranks.

#### Proof

Choose distinct

\[
 x_0,\ldots,x_{r-1}\in K
\]

and distinct fresh labels

\[
 y_0,y_1,\ldots,y_d\in K\setminus\{x_0,\ldots,x_{r-1}\}.
\]

Start with \(T_0=\{x_0,\ldots,x_{r-1}\}\).  Use the transitions

\[
\begin{array}{ll}
a_0=x_0,&b_0=y_0,\\
a_j=x_j,&b_j=y_j\quad(1\le j\le d-1),\\
a_d=y_0,&b_d=y_d.
\end{array}
\tag{1.7}
\]

In the first \(d\)-transition window, the deleted labels are
\(x_0,\ldots,x_{d-1}\) and the inserted labels are
\(y_0,\ldots,y_{d-1}\).  In the second, they are
\(x_1,\ldots,x_{d-1},y_0\) and \(y_1,\ldots,y_d\).  Each list is
repetition-free and the two directions are disjoint.  Both length-\(d\)
windows, and hence every shorter subwindow, satisfy (1.4).

But \(b_0=a_d=y_0\).  The coordinate \(y_0\) occurs exactly in

\[
T_1,T_2,\ldots,T_d,
\]

a positive run of length \(d\).  The next section shows directly that this
one run prevents the erosion representation.  \(\square\)

## 2. Endpoint-capped erosion and the exact OR identities

Extend the chronology constantly:

\[
 \widetilde T_i=
 \begin{cases}
 T_0,&i<0,\\
 T_i,&0\le i<N,\\
 T_{N-1},&i\ge N.
 \end{cases}
 \tag{2.1}
\]

For

\[
 -d\le j\le N-1
\]

define the forward maximal erosion letter

\[
 E_j=\bigcap_{h=0}^{d}\widetilde T_{j+h}.
 \tag{2.2}
\]

The displayed index interval contains \(N+d\) letters.

### Theorem 2.1 (linear erosion compiler with both endpoint corrections)

If \(T\) is \(d\)-erosion-safe, then every \(E_j\) is nonempty and, for
every \(0\le q\le d\) and \(0\le i<N-q\),

\[
\boxed{
 L_i^{(q)}
 =\bigcup_{j=i+q-d}^{i}E_j,
 \qquad
 U_i^{(q)}
 =\bigcup_{j=i-d}^{i+q}E_j.}
\tag{2.3}
\]

Thus the ordered word

\[
 E_{-d},E_{-d+1},\ldots,E_{N-1}
 \tag{2.4}
\]

literally realizes every prescribed lower and upper occurrence through
depth \(d\).

Its endpoint and core letters are exactly

\[
\boxed{
\begin{aligned}
E_{-d+s}&=L_0^{(s)}
 &&(0\le s<d),\\
E_i&=L_i^{(d)}
 &&(0\le i<N-d),\\
E_{N-d+s}&=L_{N-d+s}^{(d-1-s)}
 &&(0\le s<d).
\end{aligned}}
\tag{2.5}
\]

#### Proof

Fix a coordinate \(x\).  Constant endpoint extension makes every positive
run touching an endpoint infinite.  Every other positive run has length at
least \(d+1\).  If such a run is \([a,b]\), its positive interval in the
erosion word is \([a,b-d]\) in the present forward indexing.

The interval \([i+q-d,i]\) meets \([a,b-d]\) if and only if

\[
 i\ge a,\qquad i+q\le b,
\]

which says that \(x\) belongs to every owner
\(T_i,\ldots,T_{i+q}\).  Likewise \([i-d,i+q]\) meets
\([a,b-d]\) if and only if

\[
 i\le b,\qquad i+q\ge a,
\]

which says that \(x\) belongs to at least one of those owners.  The
identically-zero and identically-one coordinate words are immediate.  This
proves (2.3) coordinatewise.

Every interior erosion letter has rank \(r-d\), and the endpoint letters
have at least that rank.  Condition (1.1) makes them nonempty.  Formula
(2.5) is obtained by substituting the constant extension into (2.2).
\(\square\)

Proposition 1.2 is now an explicit obstruction.  Its target
\(L_1^{(d-1)}\) contains \(y_0\), while its compiler interval is

\[
[0,1].
\]

But \(y_0\notin E_0\) because \(T_0\) omits it, and
\(y_0\notin E_1\) because \(T_{d+1}\) omits it.  Hence (2.3) fails.

## 3. Exact ordered-row and interval-barrier characterizations

Suppose ordered families

\[
\mathcal L_i^{(q)},\qquad \mathcal U_i^{(q)}
\tag{3.1}
\]

are prescribed for \(0\le q\le d\), \(0\le i<N-q\), with intended ranks
\(r-q\) and \(r+q\).

Here an **endpoint-capped erosion representation** means that the common
middle row \(T\) is extended as in (2.1), its letters are the maximal
erosions (2.2), and the prescribed rows are exactly the OR intervals
(2.3).  In particular the \(q=0\) owner row is part of the representation.

### Theorem 3.1 (ordered all-depth erosion criterion)

The prescribed rows have a nonempty endpoint-capped erosion representation
if and only if all of the following hold.

1. Their middle rows agree:

   \[
   \mathcal L_i^{(0)}=\mathcal U_i^{(0)}=:T_i.
   \tag{3.2}
   \]

2. Their exact tower recurrences hold:

   \[
   \mathcal L_i^{(q+1)}
   =\mathcal L_i^{(q)}\cap\mathcal L_{i+1}^{(q)},
   \tag{3.3}
   \]

   \[
   \mathcal U_i^{(q+1)}
   =\mathcal U_i^{(q)}\cup\mathcal U_{i+1}^{(q)}
   \tag{3.4}
   \]

   for \(0\le q<d\).

3. Every displayed set has its intended rank, and consecutive deepest
   lower traces satisfy

   \[
   \boxed{
   \left|
   \mathcal L_i^{(d)}\cap\mathcal L_{i+1}^{(d)}
   \right|=r-d-1
   \quad(0\le i<N-d-1).}
   \tag{3.5}
   \]

When these conditions hold, the canonical representation is (2.5).

#### Proof

Equations (3.2)--(3.4) identify the prescribed rows with the actual
consecutive intersections and unions of \(T\).  The rank conditions at
depth one make consecutive \(T_i\)'s Johnson-adjacent, and all the rank
conditions are exactly two-sided \(d\)-safety.

Put \(C_i=\mathcal L_i^{(d)}\).  Consecutive \(C_i,C_{i+1}\) are rank
\(r-d\) sets.  Their intersection is

\[
\bigcap_{h=0}^{d+1}T_{i+h}.
\]

Two-sided \(d\)-safety leaves only two possibilities: it has rank \(r-d\)
exactly when \(b_i=a_{i+d}\), in which case \(C_i=C_{i+1}\); otherwise it
has rank \(r-d-1\).  Thus (3.5) is exactly the wall condition (1.5).
Theorem 2.1 then supplies (2.5) and all OR identities.

Conversely, suppose a representation exists.  Its \(q=0\) identities say

\[
T_i=\bigcup_{j=i-d}^{i}E_j.
\]

If a coordinate had an internally bounded positive run of length at most
\(d\), fix an owner position \(i\) in that run.  Every erosion interval
\([j,j+d]\) contributing to the \(q=0\) compiler interval
\([i-d,i]\) contains \(i\), and hence would have to lie inside that same
positive run in order to contain the coordinate.  This is impossible for a
run of length at most \(d\).  The \(q=0\) identity would fail at \(T_i\).
Hence every internal positive run has length at least \(d+1\).

The coordinatewise argument in Theorem 2.1 uses only this run-length fact,
not the rank conditions.  It now identifies every prescribed OR interval
with the actual consecutive intersection or union of the middle row \(T\).
Therefore (3.2)--(3.4) hold.  The stipulated ranks make \(T\) a two-sided
\(d\)-safe Johnson chronology.  Its run-length condition excludes
\(b_i=a_{i+d}\), so the deepest-row dichotomy proved above gives (3.5).
\(\square\)

The preceding criterion is for ordered occurrences.  Hole-free row
multisets do not come with these orderings; selecting one common ordering is
the chronology problem.

There is also an exact criterion if one temporarily forgets chronology and
asks only for one word whose specified intervals have prescribed unions.
Let \(P\) be a linearly ordered position set, and let

\[
\mathscr I=\{(I_\alpha,R_\alpha)\}
\tag{3.6}
\]

be any family of interval/target pairs.  For \(x\in K\), put

\[
B_x=\bigcup_{\alpha:x\notin R_\alpha}I_\alpha,
\qquad
A_x=P\setminus B_x.
\tag{3.7}
\]

### Theorem 3.2 (exact interval-barrier criterion)

There are nonempty letters \(F_p\subseteq K\), \(p\in P\), satisfying

\[
\bigcup_{p\in I_\alpha}F_p=R_\alpha
\qquad(\alpha\in\mathscr I)
\tag{3.8}
\]

if and only if

\[
I_\alpha\cap A_x\ne\varnothing
\quad\text{whenever }x\in R_\alpha,
\tag{3.9}
\]

and

\[
\{x:p\in A_x\}\ne\varnothing
\quad(p\in P).
\tag{3.10}
\]

The coordinatewise maximal solution is

\[
\boxed{
F_p^{\max}=\{x:p\in A_x\}.}
\tag{3.11}
\]

Every solution is coordinatewise contained in \(F^{\max}\).

#### Proof

If \(x\notin R_\alpha\), every position of \(I_\alpha\) must omit \(x\).
Thus every possible support position of \(x\) lies in \(A_x\), proving the
containment assertion and the necessity of (3.9)--(3.10).

Conversely, take (3.11).  Negative targets omit \(x\) throughout their
intervals by definition of \(B_x\).  Every positive target interval
contains an allowed \(x\)-position by (3.9).  Therefore every union in
(3.8) is exact, and (3.10) makes all letters nonempty.  \(\square\)

For each fixed coordinate, the inequalities

\[
\sum_{p\in I_\alpha\cap A_x}f_{p,x}\ge1
\qquad(x\in R_\alpha)
\tag{3.12}
\]

form an interval matrix after forbidden columns are deleted.  They have the
consecutive-ones property and are totally unimodular.  In fact the maximal
solution (3.11) makes integrality immediate.

Apply Theorem 3.2 to the lower intervals

\[
[i+q-d,i]
\]

and upper intervals

\[
[i-d,i+q]
\tag{3.13}
\]

from (2.3).  The \(q=0\) middle intervals alone force the maximal word to be
the endpoint-capped erosion (2.2).  Thus the interval-barrier theorem and
Theorem 3.1 are two views of the same wall: chronology supplies the ordered
targets, while (3.9) supplies their private coordinate hits.

## 4. Exact safe-flow factorization through an allowed-turn transport

We now pass from ordered rows to prescribed row multiplicities.  Let
\(D_d(k,r)\) be the audited safe-de-Bruijn graph:

* a state is a two-sided safe word of \(d\) owners;
* an arc is a two-sided safe word

  \[
  e=(A_0,A_1,\ldots,A_d)
  \tag{4.1}
  \]

  directed from its length-\(d\) prefix to its length-\(d\) suffix.

Put

\[
\lambda_q(e)=\bigcap_{h=0}^{q}A_h,
\qquad
\upsilon_q(e)=\bigcup_{h=0}^{q}A_h.
\tag{4.2}
\]

For a terminal state \(v=(V_0,\ldots,V_{d-1})\), define

\[
\sigma_{q,S}^-(v)
=
\#\left\{
0\le j<d-q:
\bigcap_{h=0}^{q}V_{j+h}=S
\right\},
\tag{4.3}
\]

\[
\sigma_{q,S}^+(v)
=
\#\left\{
0\le j<d-q:
\bigcup_{h=0}^{q}V_{j+h}=S
\right\}.
\tag{4.4}
\]

At \(q=0\), either formula counts occurrences of the middle owner \(S\)
inside \(v\).

Let \(\mu_q^-\) and \(\mu_q^+\) be prescribed lower and upper row
multiplicities.  In this section set
\[
N=W=\binom{k}{r}
\]
and require every rank-\(r\) owner once.  The existing safe-flow theorem
asks for states \(u,v\) and a nonnegative integral arc vector \(z\)
satisfying

\[
\partial z=\mathbf1_u-\mathbf1_v,
\tag{4.5}
\]

\[
\sum_{e:A_0=S}z_e+\sigma_{0,S}(v)=1
\qquad
\left(S\in\binom K r\right),
\tag{4.6}
\]

\[
\sum_{e:\lambda_q(e)=S}z_e+\sigma_{q,S}^-(v)
=\mu_q^-(S),
\tag{4.7}
\]

\[
\sum_{e:\upsilon_q(e)=S}z_e+\sigma_{q,S}^+(v)
=\mu_q^+(S)
\tag{4.8}
\]

for \(1\le q\le d\), together with connected positive state support.
These equations give a two-sided \(d\)-safe Hamilton chronology, but an
arbitrary Euler ordering of \(z\) may still contain the wall return (0.1).

For two safe arc types \(e,f\), declare the turn \(e\to f\)
**erosion-admissible** when

\[
\operatorname{head}(e)=\operatorname{tail}(f)
\tag{4.9}
\]

and

\[
\boxed{
\left|\lambda_d(e)\cap\lambda_d(f)\right|=r-d-1.}
\tag{4.10}
\]

Because the two deepest colours both have rank \(r-d\), and because their
arcs overlap in \(d\) owners, the only alternatives are equality or
Johnson adjacency.  Equality is exactly \(b_i=a_{i+d}\); hence (4.10) is
the wall cut.

### Theorem 4.1 (exact fixed-\(z\) successor-pairing theorem)

Fix an integral vector \(z\) satisfying (4.5)--(4.8), and fix arc types
\(e_{\rm in},e_{\rm out}\) with

\[
z_{e_{\rm in}},z_{e_{\rm out}}>0,
\qquad
\operatorname{tail}(e_{\rm in})=u,
\qquad
\operatorname{head}(e_{\rm out})=v.
\tag{4.11}
\]

There is an erosion-compatible Euler ordering of all arc occurrences of
\(z\), beginning with \(e_{\rm in}\) and ending with \(e_{\rm out}\), if and
only if there are nonnegative integers \(w_{ef}\), supported on
erosion-admissible turns, such that

\[
\boxed{
\sum_f w_{ef}
=z_e-\mathbf1_{e=e_{\rm out}},}
\tag{4.12}
\]

\[
\boxed{
\sum_e w_{ef}
=z_f-\mathbf1_{f=e_{\rm in}},}
\tag{4.13}
\]

and the directed turn multigraph on the positive \(z\)-types is weakly
connected.

Every such ordering preserves all owner and lower/upper multiplicities in
(4.6)--(4.8), and its canonical erosion word is

\[
\boxed{
\begin{aligned}
&\pi_0(u),\ldots,\pi_{d-1}(u),\\
&\lambda_d(e_0),\lambda_d(e_1),\ldots,
  \lambda_d(e_{N-d-1}),\\
&\tau_0(v),\ldots,\tau_{d-1}(v),
\end{aligned}}
\tag{4.14}
\]

Here \(e_0,\ldots,e_{N-d-1}\) is the resulting arc order; write

\[
u=(U_0,\ldots,U_{d-1}),
\qquad
v=(V_0,\ldots,V_{d-1}),
\]

and

\[
\pi_s(u)=\bigcap_{h=0}^{s}U_h,
\qquad
\tau_s(v)=\bigcap_{h=s}^{d-1}V_h.
\tag{4.15}
\]

The three lines of (4.14) have lengths \(d,N-d,d\), respectively.

#### Proof

An Euler ordering pairs every nonterminal occurrence of an arc type \(e\)
to its successor type \(f\).  Counting these pairs gives (4.12); counting
predecessors gives (4.13).  Every consecutive pair overlaps as a
de-Bruijn turn, and erosion compatibility gives (4.10).  One trail gives
weakly connected turn support.

Conversely, (4.12)--(4.13) give the directed degree imbalance

\[
\deg^+_w(e)-\deg^-_w(e)
=\mathbf1_{e=e_{\rm in}}-\mathbf1_{e=e_{\rm out}}.
\]

Connected support and Euler's theorem give one trail in the turn
multigraph from \(e_{\rm in}\) to \(e_{\rm out}\).  Type \(e\) occurs in
its vertex sequence exactly

\[
\deg_w^+(e)+\mathbf1_{e=e_{\rm out}}=z_e
\]

times.  Condition (4.9) makes the arc sequence one trail in
\(D_d(k,r)\), while (4.10) and Lemma 1.1 make the spelled owner chronology
\(d\)-erosion-safe.  Theorem 2.1 gives (4.14)--(4.15).

Reordering the fixed multiset \(z\) changes none of its linear projections,
so (4.6)--(4.8) remain true.  \(\square\)

### Theorem 4.2 (the fixed-tree pieces are TU)

Fix \(z,e_{\rm in},e_{\rm out}\) as above.  Ignore connectedness for a
moment.  Equations (4.12)--(4.13), with forbidden turns deleted, are a
bipartite transportation system between a source and a target copy of the
safe arc types.  Its coefficient matrix is totally unimodular.

More exactly, choose directed admissible turns whose underlying undirected
edges form a spanning tree \(\Theta\) on the positive \(z\)-types, and
impose

\[
w_{ef}\ge1\qquad(e\to f\in\Theta).
\tag{4.16}
\]

After subtracting these lower bounds, the residual system is still a
transportation system with integral margins.  Hence every vertex of a
nonempty fixed-\(\Theta\) polyhedron is integral; in particular, fractional
feasibility implies integral feasibility in that piece.
Conversely, every weakly connected integral solution of Theorem 4.1
contains such a directed-edge spanning tree.

Therefore, at the level relevant here,

\[
\{\text{connected feasible integral }w\}
=
\bigcup_{\Theta}
\left(
\{\text{feasible }w\text{ satisfying (4.16)}\}\cap\mathbb Z^{E}
\right).
\tag{4.17}
\]

Each fixed-\(\Theta\) polyhedron is TU.  No equality of the corresponding
real feasible sets is claimed: a connected fractional support can have all
of its spanning-tree weights strictly between zero and one.

#### Proof

Each turn variable occurs once in its source-degree row and once in its
target-degree row.  This is the node-edge matrix of a bipartite graph, hence
is totally unimodular.  Deleting columns and translating integral lower
bounds preserve integrality.  A weakly connected positive directed support
contains a spanning tree after orientations are forgotten; retain the
actual direction of each selected positive turn.  \(\square\)

This is the positive TU statement.  It starts **after** an integral
owner/trace vector \(z\) has been selected.  It does not make the full
owner-and-colour augmented safe-flow matrix TU.

## 5. Exact cyclic wrap correction

The linear equations (4.5)--(4.8) count only nonwrapping trace windows.
They do not justify the cyclic \(N+2d\) compiler.

Let

\[
u=(U_0,\ldots,U_{d-1}),
\qquad
v=(V_0,\ldots,V_{d-1}).
\]

For \(1\le t\le q\), the cyclic depth-\(q\) window containing the last
\(t\) owners and the first \(q+1-t\) owners has lower and upper values

\[
W_{q,t}^-(u,v)
=
\left(\bigcap_{a=d-t}^{d-1}V_a\right)
\cap
\left(\bigcap_{a=0}^{q-t}U_a\right),
\tag{5.1}
\]

\[
W_{q,t}^+(u,v)
=
\left(\bigcup_{a=d-t}^{d-1}V_a\right)
\cup
\left(\bigcup_{a=0}^{q-t}U_a\right).
\tag{5.2}
\]

Let \(\omega_{q,S}^{\pm}(u,v)\) count the \(q\) displayed records equal to
\(S\).  Then the exact cyclic multiplicity equation is

\[
\boxed{
\mu_{q,\mathrm{cyc}}^\pm(S)
=
\mu_{q,\mathrm{lin}}^\pm(S)
+\omega_{q,S}^{\pm}(u,v).}
\tag{5.3}
\]

Every record in (5.1)--(5.2) must also have rank \(r-q\) or \(r+q\),
respectively.  The wall comparisons crossing the cut are not implied by
these rank equations.  They have the following exact deepest-row form.  Put

\[
C_i=\lambda_d(e_i),
\qquad
R_t=W_{d,t}^-(u,v).
\]

The cyclic order of the deepest records is

\[
C_0,C_1,\ldots,C_{N-d-1},R_d,R_{d-1},\ldots,R_1.
\tag{5.4}
\]

In addition to the internal turns, require

\[
\left|C_{N-d-1}\cap R_d\right|=r-d-1,
\tag{5.5}
\]

\[
\left|R_t\cap R_{t-1}\right|=r-d-1
\qquad(2\le t\le d),
\tag{5.6}
\]

\[
\left|R_1\cap C_0\right|=r-d-1.
\tag{5.7}
\]

These are exactly the \(d+1\) wall turns involving the wrap block.

At \(q=d\), the terminal correction in (4.3)--(4.4) is zero.  Thus the
linear theorem contains only the \(N-d\) deepest core letters

\[
\lambda_d(e_0),\ldots,\lambda_d(e_{N-d-1}).
\]

The missing \(d\) cyclic deepest records are precisely the wrap erosion
letters.  Terminal suffix corrections cannot replace them.

Equivalently, use a genuinely cyclic formulation: take a nonnegative
integral circulation \(z\) on \(D_d(k,r)\) with connected support,

\[
\partial z=0,
\qquad
\sum_{e:A_0=S}z_e=1
\quad\left(S\in\binom K r\right),
\tag{5.8}
\]

and impose the lower and upper row equations with no suffix terms.  Apply
the cyclic version of Theorem 4.1, in which

\[
\sum_f w_{ef}=\sum_f w_{fe}=z_e
\tag{5.9}
\]

and the allowed-turn support is connected.  Euler's theorem then spells one
cyclic erosion-safe Hamilton chronology.  Its \(N\) erosion letters are the
cyclic deepest colours \(\lambda_d(e_i)\); repeating the first \(2d\)
letters gives the exact cyclic compiler, with the owner chronology rotated
forward by \(d\).  To retain the displayed cut
\(T_0,T_1,\ldots,T_{N-1}\), linearize instead as

\[
E_{-d},\ldots,E_{-1},
E_0,\ldots,E_{N-1},
E_0,\ldots,E_{d-1},
\]

where negative indices are cyclic.  This has the same length \(N+2d\).

## 6. Fixed-skeleton Hall collapse becomes occurrence colour

Let the erosion word positions be \(P\).  A fixed trace-two skeleton chooses
at every position a nonempty trace

\[
Q_p=E_p\cap\bigcap_{L\in\Gamma_p}L,
\qquad |\Gamma_p|\le2,
\tag{6.1}
\]

with all controller activity, containment, protected equality, and
private-hit conditions imposed.  A physical cell \(c\) has a source
interval \(I_c\).  Put

\[
\rho_Q(c)=\bigcup_{p\in I_c}Q_p.
\tag{6.2}
\]

For a pairwise distinct residual subset target \(S\), the audited
fixed-skeleton theorem says that \(c\) is usable for \(S\) exactly when

\[
(S,c)\in B,
\qquad
P_\Gamma(S)\subseteq I_c,
\qquad
\rho_Q(c)=S.
\tag{6.3}
\]

In particular, after the skeleton is fixed, one cell has at most one target
value.  Distinct residual targets never compete for a cell.  The residual
extension exists if and only if every \(S\) has at least one occurrence
(6.3).

### Theorem 6.1 (decorated erosion-Euler formulation)

Assume every cell interval and controller footprint contains at most \(h\)
source positions.
There is a finite decorated allowed-turn graph which records

1. the safe owner memory and the wall cut (4.10);
2. the last \(h\) erosion/controller traces;
3. active controller identities and their remaining footprint lifetimes;
4. every eligible **named physical-cell occurrence** which becomes
   complete, including its unique cell identifier and the controller
   footprint tied to that same occurrence.

Decorated source and terminal states carry the finitely many prefix and
suffix erosion/controller letters from (2.5), so cells completed wholly in
an endpoint correction are counted as boundary constants in (6.5).
Each named cell is anchored to a unique Hamilton-owner phase; if that anchor
is not already unique in the chosen model, impose a capacity-one row for
that cell identifier.  Repeated traversal of one local cell *type* is never
credited as several occurrences of the same physical cell.
This sentence uses the owner-anchor-transported convention.  For an
ordinal-fixed cell \(c\) with a prescribed absolute interval \(I_c\), add
the absolute phase to the decorated state and emit \(c\) only when the
actual endpoint of \(I_c\) is reached.  Capacity one prevents duplication;
the phase condition prevents relocation.

The emission ledger is occurrence-faithful at the two path ends.  If
\(w_{ef}\) are the decorated turn counts with last type \(e_{\rm out}\),
define the safe-window occurrence projection by

\[
z_e=\sum_f w_{ef}+\mathbf1_{e=e_{\rm out}}.
\tag{6.4}
\]

Apply the owner and trace equations to this \(z\), not merely to the source
labels of turn edges.  Equivalently, split every decorated safe-arc type
into an entrance and exit and put all owner/trace/cell emissions on one
mandatory traversal edge; allowed-turn edges are then uncoloured
connectors.  This counts both endpoint safe-arc occurrences exactly once.

A Hamilton chronology, one erosion word, the prescribed lower and upper
rows, and an admissible trace-two residual extension exist if and only if
this decorated graph has a nonnegative integral boundary flow with

1. one Euler component;
2. the middle-owner equations (4.6);
3. the lower and upper equations (4.7)--(4.8), with their endpoint
   corrections; and
4. for every distinct residual target \(S\),

   \[
   \#\{\text{eligible completed named cells labelled }S\}\ge1.
   \tag{6.5}
   \]

For a cyclic compiler use a connected circulation and the wrap conditions
of Section 5.

#### Proof

Given a compiled word, take its consecutive decorated memory windows.  They
give an integral boundary flow, and the four displayed conditions are
literal counts.

Conversely, Euler's theorem orders the connected integral flow into one
decorated trail.  The retained local transitions give the safe chronology,
the wall cut, the erosion/controller word, controller activity, and every
protected equality.  The projection equations give the owner and trace
multiplicities.  Condition (6.5), together with (6.3), supplies one usable
cell for each residual target.  Cells selected for distinct targets are
automatically distinct because one cell has one value \(\rho_Q(c)\).
There is no further Hall choice.  \(\square\)

For repeated labelled copies of the same underlying subset, the
right-degree-one theorem separates that value from all other values but
leaves a Hall problem inside its labelled value fibre.  A single
multiplicity inequality is sufficient only when those copies have identical
base eligibility and controller-footprint requirements.

## 7. The natural full matrix is not TU

Theorem 4.2 must not be extended to the complete chronology-selection
matrix.

### Theorem 7.1 (an erosion-compatible determinant-\(2\) cycle)

In \(D_1(5,2)\), consider the cyclic owner word

\[
12,13,34,14,15,25,12.
\tag{7.1}
\]

Its six depth-one lower colours are

\[
1,3,4,1,5,2.
\tag{7.2}
\]

Every consecutive turn, including the closing turn, satisfies the
depth-one wall cut.  Delete one row from the directed incidence matrix of
the six-cycle and append the lower-colour row for \(\{1\}\).  The resulting
square matrix has determinant

\[
\boxed{\pm2.}
\tag{7.3}
\]

Consequently the natural state-incidence matrix augmented by even one trace
colour row is not totally unimodular.

#### Proof

The six owner transitions in (7.1) are Johnson edges.  Directly from their
successive deletion/insertion labels, no inserted label is deleted on the
next transition, so every turn is erosion-admissible.

The directed cycle incidence matrix with one node row removed has rank five
and one-dimensional right kernel generated by the all-ones vector.  The
row for colour \(\{1\}\) has exactly two ones, on

\[
12\to13,\qquad 14\to15.
\]

Appending that row therefore gives determinant, up to sign, equal to its
sum around the cycle, namely \(2\).  \(\square\)

Equivalently, the equations

\[
\partial z=0,
\qquad
\sum_{e:\lambda_1(e)=\{1\}}z_e=1
\tag{7.4}
\]

on this cycle have the unique nonnegative solution \(z_e=1/2\).  Every
integral circulation is constant and has even \(\{1\}\)-load.

Appending owner, upper, controller, or occurrence rows cannot remove the
displayed submatrix.  A particular skeleton may delete one of its columns,
so Theorem 7.1 refutes the unqualified natural-matrix TU claim, not every
restricted submatrix and not every possible extended formulation.

The same obstruction occurs inside the actual \(k=15,d=3\) parameter
range.

### Theorem 7.2 (general twice-owned erosion-safe cycle)

Assume

\[
2\le d\le r-1,
\qquad
k\ge r+2d+1.
\tag{7.5}
\]

The state-incidence matrix of \(D_d(k,r)\), augmented by the middle-owner
rows, contains a square minor of determinant \(\pm2\).  The witnessing
cycle also has every turn erosion-admissible.
In particular this holds for

\[
(k,r,d)=(15,8,3).
\tag{7.6}
\]

#### Proof

Choose distinct labels

\[
a_0,\ldots,a_{r-1},\quad
c_1,\ldots,c_d,\quad
f_1,\ldots,f_{d+1}
\]

in \(K\), and form the cyclic label word

\[
Z=
a_0,\ldots,a_{r-1},
c_1,\ldots,c_d,
a_0,\ldots,a_{r-1},
f_1,\ldots,f_{d+1}.
\tag{7.7}
\]

Its length is

\[
\ell=2(r+d)+1.
\]

The two occurrences of each \(a_j\) are at cyclic distances \(r+d\) and
\(r+d+1\).  Hence every cyclic block of \(r+d\) labels is injective.  Put

\[
T_i=\{Z_i,Z_{i+1},\ldots,Z_{i+r-1}\}
\qquad(i\in\mathbb Z_\ell).
\tag{7.8}
\]

These are Johnson-adjacent sliding windows.  Every \(q\)-transition window,
\(q\le d\), uses an injective block of \(r+q\) labels, so its intersection
and union have ranks \(r-q\) and \(r+q\).  Moreover its insertion and the
deletion \(d\) transitions later are \(Z_{i+r}\) and \(Z_{i+d}\), which are
distinct in the same injective block.  Thus every cyclic turn is
erosion-admissible.

Let

\[
s_i=(T_i,T_{i+1},\ldots,T_{i+d-1})
\]

be the resulting \(D_d\)-states.  They are distinct.  Indeed, because
\(d\ge2\), equality of two such states reveals equality of their first
deletion labels \(Z_i\).  A filler label has one occurrence.  If the common
label is some \(a_j\), the two possible starts lie in the two displayed
\(a\)-blocks.  Their first \(r\)-windows already differ unless \(j=0\);
for \(j=0\) both first windows equal

\[
S=\{a_0,\ldots,a_{r-1}\},
\]

but their second windows contain \(c_1\) and \(f_1\), respectively.

The safe arcs

\[
e_i=(T_i,T_{i+1},\ldots,T_{i+d})
\colon s_i\longrightarrow s_{i+1}
\]

therefore form a directed \(\ell\)-cycle on distinct \(D_d\)-states.  Every
consecutive arc turn is erosion-admissible by the wall calculation above.
Exactly two arc columns have first middle owner \(S\): the starts of the two
\(a\)-blocks.  Delete one state-incidence row of this directed cycle and
append the owner row \(S\).  As in Theorem 7.1, the determinant is, up to
sign, the sum of that row around the cycle, namely \(2\).  \(\square\)

The smallest positive/negative split is therefore:

\[
\boxed{
\begin{array}{c}
\text{fixed ordered erosion supports: interval-TU},\\
\text{fixed integral \(z\), fixed support tree: transportation-TU},\\
\text{full owner/trace chronology selection: not TU in general}.
\end{array}}
\tag{7.9}
\]

## 8. Precise proved boundary

For prescribed hole-free all-depth row **multisets**, positivity of every
target is only a support condition.  Exact erosion realization requires:

1. one integral safe-de-Bruijn vector \(z\) satisfying the owner and all
   lower/upper projection equations with terminal corrections;
2. one connected admissible-turn transport \(w\), equivalently one ordering
   satisfying the deepest-row cut (3.5);
3. for a cyclic compiler, the cross-end records (5.1)--(5.3) and wall cuts
   (5.4)--(5.7), or a genuine cyclic circulation;
4. one admissible controller skeleton whose fixed interval-union catalogue
   contains every residual target occurrence.

Items 1--2 admit the exact two-stage integral-flow formulation of Section 4,
and the connected integer ordering fibre over fixed \(z\) is the union
described in (4.17), with each fixed-tree piece TU.  Item 4 contains no
post-skeleton Hall competition, but its target
occurrence conditions depend on the final ordered word and are not implied
by row multiplicities.

The new smallest missing cut between the audited safe-de-Bruijn theorem and
the erosion compiler is (3.5), equivalently \(b_i\ne a_{i+d}\).  The new
positive theorem is Theorem 4.2.  Theorem 7.1 is the sharp warning that
these do not combine into one naive TU matrix.

No construction of the required \(k=15\) integral decorated flow is given.

## 9. Independent proof audit

Two independent audits were applied after the theorem package was drafted.
The first checked the erosion criterion, endpoint indices, the local wall
counterexample, and the exact scope of fixed-skeleton Hall collapse.  The
second checked the safe-flow endpoint ledger, occurrence-versus-type
bookkeeping, the fixed-tree transportation factorization, every cyclic-wrap
formula, and both determinant-two witnesses.

The audited corrections now present in the text are:

1. The necessity direction of Theorem 3.1 first derives short-run exclusion
   from the \(q=0\) OR identities and only then identifies the prescribed
   rows with the actual trace recurrences; this removes a circular appeal to
   safety.
2. Equation (4.17) is asserted only for integral connected points.  A
   connected fractional support need not contain a spanning tree all of
   whose edge weights are at least one.
3. Decorated occurrences in Section 6 are named physical-cell occurrences,
   include the terminal safe-window correction, and distinguish transported
   owner anchors from ordinal-fixed cells carrying absolute phase.
4. “No residual Hall problem” is restricted to pairwise distinct underlying
   subset values.  Repeated labelled copies retain Hall inside their common
   value fibre.
5. Theorem 7.2 uses distinct \(D_d\)-states and hence produces the claimed
   minor of the actual safe-state incidence matrix, not merely a quotient
   cycle.

After those corrections, neither audit found a remaining theorem-level
defect.  This audit statement does not promote any unresolved existence
claim in Section 8 to a theorem.
