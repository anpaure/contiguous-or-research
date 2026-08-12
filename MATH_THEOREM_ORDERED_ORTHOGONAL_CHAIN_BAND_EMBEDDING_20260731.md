# Ordered orthogonal chains: the exact band-embedding theorem

Date: 2026-07-31  
Status: proved; this is a construction interface, not an all-dimensional
existence claim

## 0. Purpose

The endpoint-decomposition theorem says that chosen interval witnesses form
two orthogonal chain partitions: targets with a common left endpoint form a
chain, and targets with a common right endpoint form a chain.  Abstract
orthogonal chain decompositions are known to exist, but three additional
requirements were previously entangled:

1. the chains must admit compatible endpoint orders;
2. their occupied intersections must fit in the physical short-cell band;
3. their interval labels must pass coordinatewise pin survival.

This note separates those requirements exactly.  The new point is that the
first two have a purely finite order-theoretic test: two precedence DAGs and
one greedy interval schedule.  Once pin survival is added, the OR--Pascal
recurrence is automatic because the physical word is reconstructed
coordinatewise.

## 1. Orthogonal chain data and precedence digraphs

Let \({\cal P}\) be a finite family of nonempty subsets of \([k]\).  Let

\[
 {\cal L}=\{L_1,\ldots,L_a\},\qquad
 {\cal R}=\{R_1,\ldots,R_b\}
\]

be two chain partitions of \({\cal P}\), with

\[
                         |L\cap R|\le 1
                  \qquad(L\in{\cal L},R\in{\cal R}).       \tag{1.1}
\]

For \(S\in{\cal P}\), write \(L(S)\) and \(R(S)\) for its two chains.
Define two directed graphs.

* \(D_R\) has vertex set \({\cal R}\).  Put an arc
  \(R(S)\to R(T)\) whenever \(S\subset T\) are consecutive elements of
  one \({\cal L}\)-chain.
* \(D_L\) has vertex set \({\cal L}\).  Put an arc
  \(L(T)\to L(S)\) whenever \(S\subset T\) are consecutive elements of
  one \({\cal R}\)-chain.

The reversal in the second definition is forced by interval geometry: at a
fixed right endpoint, larger targets have earlier left endpoints.

### Theorem 1.1 (precedence criterion)

There are total orders of the left and right chains with the following two
properties,

* along every left chain, right-chain indices strictly increase with set
  inclusion; and
* along every right chain, left-chain indices strictly decrease with set
  inclusion,

if and only if both \(D_R\) and \(D_L\) are acyclic.  When they are acyclic,
any topological orders of \(D_R\) and \(D_L\) have the required property.

#### Proof

Every required comparison is exactly one of the displayed arcs; comparisons
between nonconsecutive members follow by transitivity along their chain.
Thus a compatible total order is a linear extension of the corresponding
digraph.  A finite digraph has a linear extension exactly when it is
acyclic. \(\square\)

This is a sharp obstruction.  A directed precedence cycle cannot be repaired
by adding blank physical positions; one must split or rechain at least one of
its incidences.

## 2. Exact short-band embedding for fixed chain orders

Fix compatible total orders and rename the chains accordingly:

\[
                    L_1<\cdots<L_a,\qquad R_1<\cdots<R_b.
\]

Choose strictly increasing proposed left-endpoint positions

\[
                    \lambda_1<\cdots<\lambda_a.              \tag{2.1}
\]

For a nonempty right chain \(R_j\), define

\[
 \begin{aligned}
 A_j&=\max\{\lambda_i:L_i\cap R_j\ne\varnothing\},\\
 B_j&=\min\{\lambda_i+d-1:L_i\cap R_j\ne\varnothing\}.
 \end{aligned}                                                \tag{2.2}
\]

Thus a right endpoint \(\rho_j\) makes every intersection in its column a
nonempty interval of length at most \(d\) exactly when

\[
                         A_j\le\rho_j\le B_j.                 \tag{2.3}
\]

Empty chains may be deleted or placed in unused positions and play no role.

### Theorem 2.1 (greedy band-embedding criterion)

Define recursively

\[
 \rho_1^*=A_1,
 \qquad
 \rho_j^*=\max\{A_j,\rho_{j-1}^*+1\}\quad(2\le j\le b).       \tag{2.4}
\]

There are strictly increasing right endpoints \(\rho_1<\cdots<\rho_b\)
for which every occupied cell \((i,j)\) gives an interval

\[
                      [\lambda_i,\rho_j]
             \quad\hbox{of length at most }d                 \tag{2.5}
\]

if and only if

\[
                         \rho_j^*\le B_j
                         \qquad(1\le j\le b).                 \tag{2.6}
\]

For a physical line \([1,n]\), add only

\[
                         \lambda_a\le n,qquad \rho_b^*\le n. \tag{2.7}
\]

Equivalently,

\[
 \boxed{
   \max_{1\le t\le j}(A_t+j-t)\le B_j
       \qquad(1\le j\le b).}                                \tag{2.8}
\]

#### Proof

Any legal increasing endpoint sequence must obey \(\rho_1\ge A_1\) and
\(\rho_j\ge\max(A_j,\rho_{j-1}+1)\).  Induction gives
\(\rho_j\ge\rho_j^*\), so (2.6) is necessary.  Conversely, if (2.6) holds,
the greedy sequence (2.4) is increasing and belongs to every interval
\([A_j,B_j]\), proving sufficiency.  Expanding the recurrence gives

\[
                         \rho_j^*=\max_{t\le j}(A_t+j-t),
\]

which proves (2.8). \(\square\)

The criterion is exact for arbitrary staircase starts.  Taking
\(\lambda_i=i\) gives the consecutive-start special case.  Inserting the
\(d\) available start holes changes only the vector \(\lambda\); for every
such choice the optimal deadline vector is still the one greedy scan (2.4).

### Corollary 2.2 (fixed-order minimum bandwidth)

For fixed chain orders and fixed starts \(\lambda\), the least admissible
bandwidth is

\[
 \boxed{
 d_{\min}=1+\max_j\left(
       \rho_j^*-\min\{\lambda_i:L_i\cap R_j\ne\varnothing\}
                         \right).}                             \tag{2.9}
\]

Thus an abstract orthogonal pair can fail the optimal depth for either of
two mathematically distinct reasons: a precedence cycle, or a positive
bandwidth overflow after both precedence graphs have been topologically
sorted.

### Corollary 2.3 (heterogeneous rank caps)

The same greedy theorem holds when an occupied intersection
\(S\in L_i\cap R_j\) has its own permitted maximum interval length
\(w(S)\).  Replace (2.2) by

\[
 A_j=\max\{\lambda_i:L_i\cap R_j\ne\varnothing\},
 \qquad
 B_j=\min\bigl\{\lambda_i+w(S)-1:
                 S\in L_i\cap R_j\text{ for some }i\bigr\}.     \tag{2.10}
\]

Then (2.4) and (2.6) are again necessary and sufficient.

#### Proof

For the unique label \(S\in L_i\cap R_j\), its cell is legal exactly when

\[
                    \lambda_i\le\rho_j
                    \le\lambda_i+w(S)-1.
\]

Intersecting these intervals over the column gives (2.10), after which the
proof of Theorem 2.1 is unchanged. \(\square\)

This version fits the forced optimal staircase directly: take

\[
 w(S)=d\quad(|S|<r),\qquad w(S)=d+1\quad(|S|=r).                \tag{2.11}
\]

Thus lower witnesses and selected middle witnesses can be ordered in one
orthogonal-chain instance; the central layer is not an external row that
must later be synchronized.

## 3. Exact passage to an OR--Pascal word

Assume Theorems 1.1 and 2.1 pass.  Assign to every
\(S\in L_i\cap R_j\) the physical interval

\[
                            I_S=[\lambda_i,\rho_j].             \tag{3.1}
\]

Orthogonality makes these intervals distinct.  The precedence orders make
the labels strictly increase along fixed-left rows and strictly increase
when a fixed-right column is read from right to left, exactly as interval
containment demands.

For a coordinate \(x\), put

\[
 Z_x=[n]\setminus\bigcup_{S\in{\cal P}:x\notin S}I_S.          \tag{3.2}
\]

### Theorem 3.1 (ordered-chain compiler)

There is a nonempty word \(Q_1,\ldots,Q_n\) satisfying

\[
                         \bigcup_{p\in I_S}Q_p=S
                         \qquad(S\in{\cal P})                 \tag{3.3}
\]

if and only if

\[
 I_S\cap Z_x\ne\varnothing\quad(x\in S),
 \qquad
 \bigcup_{x=1}^k Z_x=[n].                                    \tag{3.4}
\]

When (3.4) holds, the coordinatewise maximal word

\[
                           Q_p=\{x:p\in Z_x\}                  \tag{3.5}
\]

works.  Its complete interval table automatically obeys

\[
 C_{i,j}=C_{i,j-1}\cup C_{i+1,j}.                             \tag{3.6}
\]

#### Proof

If (3.3) holds, every occurrence of \(x\) avoids every assigned interval
whose label omits \(x\), so it lies in \(Z_x\); each positive interval must
meet this occurrence set.  Nonempty letters give the second condition.

Conversely, (3.5) puts no forbidden bit into any assigned interval and
(3.4) supplies every required bit and every physical position.  This proves
(3.3).  Equation (3.6) is then the associativity identity for literal
interval unions, not an additional compatibility assumption. \(\square\)

Theorem 3.1 is the endpoint pin-survival theorem included here to make the
construction interface self-contained.  The genuinely new reduction is
Theorems 1.1--2.1: for a proposed pair of Boolean chain decompositions, all
ordering and short-band geometry is decidable before any coordinate pins are
chosen.

## 4. Consequence for the exact conjecture

Let \({\cal P}\) consist of the punctured lower ideal together with the
rank-\(r=\lceil k/2\rceil\) layer, let \(d=d(k)\), and let \(n=B(k)\).
A direct OR--Pascal proof of \(\nu(k)=B(k)\) is obtained if one constructs
two orthogonal chain partitions of \({\cal P}\) such that

1. both precedence digraphs are acyclic;
2. some topological orders and some \(d\)-hole start embedding pass the
   heterogeneous test (2.6), (2.10), with the caps (2.11);
3. the resulting intervals pass (3.4); and
4. after the middle intervals are ordered by left endpoint, their right
   endpoints increase, successive supports overlap or touch, and consecutive
   unions of their labels cover all upper targets.

The first two clauses in item 4 make those label unions literal physical
intervals.  Increasing right endpoints is forced automatically once (3.4)
has produced distinct equal-rank labels, but the overlap-or-touch condition
is an additional chain-alignment test.

This is not the conditional Shadow--Braid lemma in different notation.  It
is a direct, exact test on the lower tableau.  In particular, it distinguishes
three failure certificates:

\[
 \boxed{
 \text{precedence cycle}\quad|\quad
 \text{band overflow}\quad|\quad
 \text{pin-cover obstruction}.}
\]

Only the last one concerns the set labels themselves.  The first two are
ordinary finite order/scheduling obstructions and should be enforced at the
moment an orthogonal chain pair is constructed, not repaired afterward.
