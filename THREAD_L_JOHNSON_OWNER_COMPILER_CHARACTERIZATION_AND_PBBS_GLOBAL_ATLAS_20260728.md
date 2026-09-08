# Johnson owner compilers: interval Boolean rank, PQ atlases, and PBBS global batching

Date: 2026-07-28

Method: pure mathematics. No computation, finite search, or solver is
used. Section 14 compares the construction with the primary GKS
chain-cover paper cited there.

## 0. Exact outcome

Let

\[
P=(X_0,X_1,\ldots,X_S)
\tag{0.1}
\]

be a Johnson owner path, and require all consecutive lower
intersections and upper unions through a chosen depth \(H\). This note
proves the following.

1. The exact invariant for an arbitrary literal compiler is an
   **interval Boolean rank**. If \(M\) is the target-by-coordinate
   incidence matrix, then the minimum word length is the least \(L\)
   for which

   \[
   M=B\odot A,
   \tag{0.2}
   \]

   where every row of \(B\) is the indicator of one nonempty integer
   interval in \([L]\), every row of \(A\) is nonzero, and
   \(\odot\) is Boolean matrix multiplication. Thus a block has a
   coefficient-one compiler exactly when this interval Boolean rank is
   at most \(S+o(S)\). For a simple block with \(S+1\) distinct
   owners, the fixed-rank endpoint bound makes this \(S+o(S)\).

2. On a constant-width, single-run Johnson path, the one-mountain
   condition from Theorem 4.1 of
   THREAD_K_PBBS_GLOBAL_SEAM_BATCHING_AND_ONE_MOUNTAIN_COMPILER_20260728.md
   collapses to FIFO. Ordinary repetition-free consecutive ones, even
   with an arbitrary PQ-tree frontier, also forces FIFO. Therefore a
   genuinely broader theorem must permit repeated atoms, changing local
   orders, circular orders, or multi-coordinate letters.

3. One-mountain is not necessary. There is an infinite active-width-two
   non-one-mountain family with an exact compiler of length

   \[
   S+4.
   \tag{0.3}
   \]

   More generally, \(d\) disjoint adjacent entry/exit braids have length
   \(S+w+d+1\).

4. More generally, a path of local PQ orders
   \(\pi_0,\ldots,\pi_S\), with lower intersections anchored as
   intervals in those orders, has an exact compiler of length

   \[
   \boxed{
   S+w+1+\Delta,\qquad
   \Delta=\sum_{t=0}^{S-1}(w-1-\lambda_t),}
   \tag{0.4}
   \]

   where \(w\) is active width and \(\lambda_t\) is the literal
   suffix-prefix overlap between consecutive orders. This is the
   requested bounded-mountain/PQ-tree extension.

5. Global batching is governed by baseline overlap, not seam count.
   Charts charging total owner multiplicity \(M\), using \(U\) distinct
   owner positions, and having total excess \(E\), satisfy

   \[
   \boxed{L\le W+(M-U)+E.}
   \tag{0.5}
   \]

6. A rainbow PBBS packet has an audited two-core circular portal of
   cyclic excess one, but opening one packet ordinarily costs \(s-1\)
   extra letters. Complete phase decks amortize this opening toll by
   normalized port type. They yield a coefficient-one global word if
   they form a low-overlap support cover of all target values. This is
   one exact conditional bypass of the likely-critical \(\nu_H\)
   barrier; a low-defect moving-PQ atlas is another.

7. The Griggs--Killian--Savage chain-cover tree does not supply a hidden
   optimal endpoint recursion.  Its preorder is a planar column labeling,
   not a traversal.  The exact ordered-partition MTF distance is a stable
   deletion-suffix defect.  For the Greene--Kleitman parent map, the
   forward-compatible cover edges are exactly the known last-pair edges;
   they form a matching and leave \(W_{k-1}\) path starts.  Moreover, the
   standard parent-first preorder already has at least \(k-3\) internally
   non-unit boundaries for \(k\ge6\), exceeding the sharp allowance
   \(d(k)\).  Non-cover state-fibre arcs remain possible, but finding them
   is the original state-transversal problem rather than a consequence of
   planar chain cover.

8. Replacing the middle chronology by its rank-\((r-d)\) erosion controller
   does not rescue the **natural** GKS preorder.  Every positive-depth
   controller chronology is Johnson and has no internal positive coordinate
   run shorter than \(d+1\).  An exact embedded \(B_4\) subtree for even
   \(k\), and an exact upper-middle \(B_5\) subtree for odd \(k\), force
   either a non-Johnson jump or an internal singleton run for every
   parent-first sibling order.  Controller pins would be automatic after a
   valid \(P\) existed; they do not repair this chronology failure or prove
   lower-ideal exposure.

Thus the two strongest sufficient PBBS hypotheses isolated here are a
global low-defect moving-PQ atlas and a global low-overlap packet
support cover. Neither is asserted necessary for an arbitrary literal
compiler.

## 1. Required target family and literal words

For \(0\le a\le b\le S\), write

\[
L_{a,b}=\bigcap_{t=a}^{b}X_t,
\qquad
U_{a,b}=\bigcup_{t=a}^{b}X_t.
\tag{1.1}
\]

For a cutoff \(H\le S\), let

\[
\mathcal T_H(P)
=\{L_{a,b},U_{a,b}:0\le a\le b\le S,\ b-a\le H\},
\tag{1.2}
\]

with repeated set values retained only once. Literal contiguous OR
requires value support, not an occurrence-private witness.

A nonzero word is

\[
\mathcal A=(A_1,\ldots,A_\ell),
\qquad
\varnothing\ne A_i\subseteq\Omega.
\tag{1.3}
\]

It represents \(T\) if

\[
T=\bigcup_{i=p}^{q}A_i
\tag{1.4}
\]

for some \(1\le p\le q\le\ell\). If
\(\varnothing\in\mathcal T_H(P)\), no nonzero word represents the full
family; below every required target is assumed nonempty.

Let \(\lambda_H(P)\) be the minimum possible \(\ell\). For a sequence
with \(S\to\infty\), coefficient one means

\[
\lambda_H(P)\le S+o(S).
\tag{1.5}
\]

The difference between \(S\) transitions and \(S+1\) owners is
asymptotically harmless. If the \(S+1\) owner values are distinct, the
fixed-rank endpoint lemma gives \(\lambda_H(P)\ge S+1\), so (1.5) is
equivalent to equality \(S+o(S)\).

## 2. Exact interval Boolean-rank characterization

Let \(\mathcal T\) be any finite family of nonempty subsets of
\(\Omega\), and let

\[
M_{T,x}=\mathbf1_{\{x\in T\}}
\tag{2.1}
\]

be its incidence matrix.

For zero-one matrices \(B,A\), Boolean multiplication is

\[
(B\odot A)_{T,x}
=\bigvee_i(B_{T,i}\wedge A_{i,x}).
\tag{2.2}
\]

Call \(B\) an interval matrix when every row is the indicator of one
nonempty integer interval of its column order. Define
\(\operatorname{ibr}(M)\) to be the least \(L\) for which

\[
M=B\odot A
\tag{2.3}
\]

with \(B\) an interval matrix on \(L\) columns and every row of
\(A\) nonzero.

### Theorem 2.1 (literal compiler iff interval Boolean factorization)

\[
\boxed{
\min\{\text{literal word length representing }\mathcal T\}
=\operatorname{ibr}(M).}
\tag{2.4}
\]

#### Proof

Given a word \(A_1,\ldots,A_L\), let row \(i\) of \(A\) be the
coordinate incidence vector of the letter \(A_i\). Choose one witnessing
interval for each target \(T\), and put its indicator in the row
\(B_T\). Equation (1.4) is exactly the Boolean factorization
\(M=B\odot A\). Nonzero letters give nonzero rows of \(A\).

Conversely, read the rows of \(A\) as set-letters. The interval support
of \(B_T\) has OR equal to row \(M_T\), so it witnesses \(T\).
\(\square\)

There is an equivalent formulation which eliminates the letters. Assign
an interval \(J_T\subseteq[L]\) to each target and, after deleting
unused positions, define

\[
C_i=\bigcap_{T:i\in J_T}T.
\tag{2.5}
\]

### Corollary 2.2 (interval-kernel iff)

The assigned intervals admit a nonzero compiler if and only if

\[
C_i\ne\varnothing
\tag{2.6}
\]

for every position and

\[
\boxed{
T=\bigcup_{i\in J_T}C_i
\qquad(T\in\mathcal T).}
\tag{2.7}
\]

When these conditions hold, \((C_1,\ldots,C_L)\) is the canonical
maximal compiler for that interval assignment.

#### Proof

If \(A_i\) is a realizing letter and \(i\in J_T\), then
\(A_i\subseteq T\), hence
\(\varnothing\ne A_i\subseteq C_i\). Therefore

\[
T=\bigcup_{i\in J_T}A_i
\subseteq\bigcup_{i\in J_T}C_i
\subseteq T.
\]

This proves necessity. Sufficiency follows by taking \(A_i=C_i\).
\(\square\)

### Corollary 2.3 (exact coefficient-one criterion)

A sequence of Johnson blocks has coefficient-one literal compilers if and
only if the target incidence matrices satisfy

\[
\boxed{
\operatorname{ibr}(M_H(P))\le S+o(S).}
\tag{2.8}
\]

For simple blocks with \(S+1\) distinct owners, this is equivalently an
equality.

This includes multi-coordinate letters, repeated target values, owner
recycling, and different witnesses at different depths.

## 3. Repeated-atom routes and ordinary PQ trees

Suppose all targets contain a common nonempty core \(K\), and put

\[
\mathcal H=\{T\setminus K:T\in\mathcal T\}.
\tag{3.1}
\]

A **support route** is a symbol word

\[
\pi=(x_1,\ldots,x_d)
\tag{3.2}
\]

over \(\Omega\setminus K\), with repetitions allowed, such that every
nonempty \(H\in\mathcal H\) is the set of distinct symbols in some
contiguous factor. The empty active target is represented separately by
\(K\). Let \(\rho(\mathcal H)\) be the minimum possible \(d\), and put

\[
\varepsilon_K=\mathbf1_{\{\varnothing\in\mathcal H\}}.
\tag{3.2a}
\]

### Theorem 3.1 (exact atom-route compiler)

The minimum length among compilers whose letters outside \(K\) are
singletons is

\[
\boxed{\rho(\mathcal H)+\varepsilon_K.}
\tag{3.3}
\]

Indeed, replace each route symbol \(x_i\) by \(K\cup\{x_i\}\) and
append \(K\) exactly when the empty active target is required.

#### Proof

The OR of a factor is \(K\) together with its factor alphabet.
Conversely, deleting \(K\) from a singleton-atom word recovers the
support route, while a \(K\)-only target forces one core-only letter.
\(\square\)

If repetitions are forbidden and all \(N\) active coordinates are used,
the condition is exactly that every row of the target-coordinate matrix
have consecutive ones in one column order.

### Corollary 3.2 (PQ-tree specialization)

\[
\rho(\mathcal H)=N
\tag{3.4}
\]

if and only if the target hypergraph has the consecutive-ones property.
Its permissible coordinate orders are precisely the PQ-tree frontiers.
The repeated-column toll

\[
\operatorname{split}(\mathcal H)=\rho(\mathcal H)-N
\tag{3.5}
\]

measures the strict extension beyond ordinary PQ trees.

## 4. One-mountain and repetition-free PQ both collapse to FIFO

Let \(P=(X_0,\ldots,X_S)\) be a constant-rank Johnson path. Put

\[
K=\bigcap_{t=0}^{S}X_t,\qquad
B_t=X_t\setminus K,\qquad |B_t|=w.
\tag{4.1}
\]

Assume every noncore coordinate has one membership interval
\([l_x,r_x]\). Exactly \(w\) runs start at time \(0\), and one new run
starts at each later owner time. Order the runs by left endpoint,
resolving the initial tie:

\[
x_1,\ldots,x_{S+w}.
\tag{4.2}
\]

### Theorem 4.1 (one-mountain iff FIFO)

The condition

\[
\{i:r_i\ge t\}\text{ is an integer interval for every }t
\tag{4.3}
\]

holds if and only if the initial tie can be resolved so that

\[
\boxed{
B_t=\{x_{t+1},\ldots,x_{t+w}\}
\qquad(0\le t\le S).}
\tag{4.4}
\]

Thus, in the exact hypotheses of the source theorem, one-mountain is
equivalent to FIFO.

#### Proof

At time \(t\), the started runs form the prefix
\(\{x_1,\ldots,x_{w+t}\}\). Condition (4.3) makes the live runs an
interval in the same order. Their intersection is \(B_t\), an interval
of size \(w\) containing the newest run \(x_{w+t}\). It must therefore
be the last \(w\) indices of that prefix, which is (4.4).

Conversely, the sliding windows (4.4) have interval exit-threshold sets,
so (4.3) holds. \(\square\)

### Theorem 4.2 (arbitrary repetition-free C1P order iff FIFO)

Assume \(w\ge2\). There is an order of the noncore coordinates in which
every owner row \(B_t\) is an interval if and only if, up to reversing
that order, the rows are consecutive sliding \(w\)-windows.

#### Proof

Write \(B_t=[p_t,p_t+w-1]\). Distinct consecutive owners share
\(w-1\) active coordinates, so

\[
p_{t+1}-p_t\in\{-1,+1\}.
\]

A change of sign makes a just-departed coordinate immediately re-enter,
contrary to the single-run hypothesis. Hence all signs agree. The
converse is immediate. \(\square\)

Because the full target matrix contains the owner rows, an ordinary
PQ-tree order cannot certify a non-FIFO single-run block. A broader
compiler must change local orders, repeat atoms, use circular portals, or
use multi-coordinate Boolean factors.

## 5. Moving PQ atlases: the exact bounded-mountain compiler

The preceding negative statement concerns one fixed repetition-free
coordinate order. Local PQ orders can move along the owner path and share
most of their letters.

Continue with a Johnson path with nonempty common core \(K\), and put

\[
Y_t=X_t\setminus K,\qquad |Y_t|=w.
\tag{5.1}
\]

No single-run hypothesis is needed in this section.

For every lower owner interval \(I=[a,b]\), define its active lower
target

\[
D_I=\left(\bigcap_{t=a}^{b}X_t\right)\setminus K.
\tag{5.2}
\]

An **anchored PQ atlas** consists of:

1. an anchor \(\eta(I)\in I\) for every nonempty \(D_I\);
2. a linear order \(\pi_t\) of \(Y_t\) for every owner time \(t\);
3. the condition that every \(D_I\) assigned to \(t\) is an interval
   in \(\pi_t\).

Equivalently, at time \(t\), the assigned-target incidence matrix has
the consecutive-ones property, and \(\pi_t\) is one of its PQ-tree
frontiers.

For consecutive orders, let

\[
\lambda_t
=\max\{\ell:
\operatorname{suffix}_{\ell}(\pi_t)
=\operatorname{prefix}_{\ell}(\pi_{t+1})\}.
\tag{5.3}
\]

Since \(Y_t,Y_{t+1}\) are distinct \(w\)-sets meeting in \(w-1\)
coordinates,

\[
0\le\lambda_t\le w-1.
\tag{5.4}
\]

Put

\[
\delta_t=w-1-\lambda_t,
\qquad
\Delta=\sum_{t=0}^{S-1}\delta_t.
\tag{5.5}
\]

### Theorem 5.1 (moving-PQ compiler)

Every anchored PQ atlas gives a literal compiler of exact constructed
length

\[
\boxed{
L=S+w+1+\Delta.}
\tag{5.6}
\]

It represents every consecutive lower intersection and every consecutive
upper union. Moreover, every upper prefix is represented by a literal
prefix of the compiler, and every upper suffix by a literal suffix.

#### Proof

Write \(\pi_0\). Inductively, after the marked occurrence of
\(\pi_t\), append the part of \(\pi_{t+1}\) not already supplied by
the overlap (5.3). Thus every \(\pi_t\) occurs as a marked contiguous
factor. Replace every active symbol \(x\) by \(K\cup\{x\}\), and append
one final \(K\).

The active symbol-word length is

\[
\begin{aligned}
w+\sum_{t=0}^{S-1}(w-\lambda_t)
&=w+\sum_{t=0}^{S-1}(1+\delta_t)\\
&=S+w+\Delta.
\end{aligned}
\tag{5.7}
\]

The final core letter proves (5.6).

If \(D_I\ne\varnothing\), its assigned interval inside the marked
\(\pi_{\eta(I)}\) occurrence has OR
\(K\cup D_I=\cap_{t\in I}X_t\). If \(D_I=\varnothing\), use the
final core letter.

For an upper interval \([a,b]\), take the factor from the beginning of
the marked \(\pi_a\) occurrence through the end of the marked
\(\pi_b\) occurrence. Every symbol in this factor belongs to some
\(Y_t\) with \(a\le t\le b\), and the factor contains the complete
marked occurrence of every such \(Y_t\). Its alphabet is therefore
exactly

\[
\bigcup_{t=a}^{b}Y_t.
\]

Adding \(K\) gives the required upper union. When \(a=0\), the witness
begins at the first word position; when \(b=S\), extend through the
final \(K\). This proves two-sided upper transparency. \(\square\)

### Corollary 5.2 (bounded reset criterion)

If only \(R_0\) transitions have \(\lambda_t<w-1\), then

\[
\boxed{
L\le S+w+1+(w-1)R_0.}
\tag{5.8}
\]

More sharply, coefficient one follows whenever

\[
w+\Delta=o(S).
\tag{5.9}
\]

This is a bounded-mountain theorem in an exact quantitative form.
Partial order overlap is credited rather than rounded to a full reset.

## 6. The exact local crossing-grid PQ gate

Assume now that every noncore coordinate has one membership interval

\[
I_x=[l_x,r_x].
\tag{6.1}
\]

Fix an anchor time \(t\). For \(a\le t\le b\), define subsets of
\(Y_t\) by

\[
E_a(t)=\{x\in Y_t:l_x\le a\},
\qquad
R_b(t)=\{x\in Y_t:r_x\ge b\}.
\tag{6.2}
\]

Then

\[
D_{[a,b]}=E_a(t)\cap R_b(t).
\tag{6.3}
\]

### Theorem 6.1 (crossing grid iff two nested chains are consecutive)

An order \(\pi_t\) makes every **nonempty active** lower target whose
owner interval crosses \(t\) consecutive if and only if it makes every
nonempty set in both nested
chains

\[
\{E_a(t):a\le t\},
\qquad
\{R_b(t):b\ge t\}
\tag{6.4}
\]

consecutive.

#### Proof

Necessity follows from

\[
D_{[a,t]}=E_a(t),
\qquad
D_{[t,b]}=R_b(t).
\]

For sufficiency, (6.3) is the intersection of two intervals in
\(\pi_t\), hence an interval or empty. Empty active targets are
represented by the nonempty core letter and impose no C1P condition.
\(\square\)

In the tie-free case, this has an elementary deque description. Let
\(\alpha\) be entrance order and \(\beta\) decreasing-exit order on
\(Y_t\). An order makes every prefix of both \(\alpha\) and
\(\beta\) consecutive if and only if it can be obtained from each order
by starting with its first element and inserting every subsequent element
at one of the two current ends. Thus the gate is a common-deque/PQ
frontier, not equality of entrance and exit orders.

Indeed, if the first \(j-1\) elements of an order occupy an interval and
the first \(j\) also occupy an interval, the new \(j\)-th element must
adjoin one of the two ends. Induction gives the deque construction.
Conversely, successive end insertion makes every prefix an interval.
Applying this argument to both nested chains proves the characterization.

The local pattern \(213\) is feasible:

\[
\alpha=123,\qquad\beta=213,\qquad\pi=312.
\tag{6.5}
\]

Indeed the prefixes of both \(\alpha\) and \(\beta\) are intervals in
\(312\). Therefore the audited PBBS \(213\) motif is not a local
consecutive-ones obstruction and cannot justify an \(H\)-letter charge
by itself.

## 7. Sparse braids and an explicit non-one-mountain family

There is a useful closed form when entry and exit orders differ by sparse
adjacent swaps.

Let the entry order of the \(N=S+w\) single-run coordinates be

\[
\alpha=(x_1,\ldots,x_N).
\tag{7.1}
\]

Suppose ascending exit order is obtained by swapping disjoint adjacent
pairs

\[
(x_i,x_{i+1}),\qquad i\in J,
\tag{7.2}
\]

where \(J\) contains no consecutive integers. Form a symbol word from
\(\alpha\) by replacing each selected pair by

\[
x_i,x_{i+1},x_i.
\tag{7.3}
\]

For a single-run block, the active parts of all lower and upper targets
are precisely

\[
\left(\bigcap_{t=a}^{b}X_t\right)\setminus K
=\{x:l_x\le a,\ r_x\ge b\},
\qquad
\left(\bigcup_{t=a}^{b}X_t\right)\setminus K
=\{x:l_x\le b,\ r_x\ge a\}.
\tag{7.3a}
\]

### Theorem 7.1 (sparse adjacent-braid compiler)

Assume \(K\ne\varnothing\).
Every nonempty set of the form

\[
\{x:l_x\le u,\ r_x\ge v\}
\tag{7.4}
\]

is the alphabet of a contiguous factor of (7.3). Consequently all
consecutive lower intersections and upper unions have a literal atom
compiler of length

\[
\boxed{
L=S+w+|J|+1.}
\tag{7.5}
\]

#### Proof

An entry threshold is a prefix of \(\alpha\), while an exit-survival
threshold is a suffix of ascending exit order. Without a swap, their
intersection is an ordinary index interval.

For a swapped pair \((i,i+1)\), the only exceptional exit suffix is

\[
\{x_i\}\cup\{x_{i+2},\ldots,x_N\}.
\tag{7.6}
\]

Intersecting with an entry prefix gives an ordinary interval, the
singleton \(\{x_i\}\), or

\[
\{x_i\}\cup\{x_{i+2},\ldots,x_u\}.
\tag{7.7}
\]

The last set is read from the second copy of \(x_i\) in (7.3) through
\(x_u\). Disjointness of the swapped pairs ensures that the other
duplicates add no new symbol. This proves every nonempty (7.4); an empty
active set uses the final \(K\). Replacing symbols by
\(K\cup\{x\}\) and appending \(K\) gives (7.5). \(\square\)

Thus

\[
w+|J|=o(S)
\tag{7.8}
\]

is a coefficient-one criterion. A single \(213\) overtaking costs
exactly one repeated atom.

For a completely explicit infinite example, take \(S\ge3\), a nonempty
core \(K\), and active pairs

\[
\begin{aligned}
Y_0&=\{a,b\},\\
Y_1&=\{b,c\},\\
Y_2&=\{b,d\},\\
Y_t&=\{u_{t-3},u_{t-2}\}\quad(3\le t\le S),
\end{aligned}
\tag{7.9}
\]

where \(u_0=d\). Every coordinate has one membership interval. Under the
two possible initial tie orders, the exit sequence begins

\[
(0,2,1,3,\ldots)
\quad\text{or}\quad
(2,0,1,3,\ldots),
\tag{7.10}
\]

so one-mountain fails. Nevertheless

\[
a,b,c,b,d,u_1,\ldots,u_{S-2}
\tag{7.11}
\]

followed by the core letter gives the literal word

\[
K+a,K+b,K+c,K+b,K+d,K+u_1,\ldots,K+u_{S-2},K
\tag{7.12}
\]

of length \(S+4\). Here \(K+x\) abbreviates
\(K\cup\{x\}\). This represents every consecutive lower intersection
and upper union, either by Theorem 5.1 with \(\Delta=1\) or by direct
application of Theorem 7.1.

## 8. Circular consecutive ones

The circular analogue supplies another strict extension.

### Theorem 8.1 (bounded circular-arc compiler)

Suppose every target contains \(K\ne\varnothing\), and its noncore
support is empty or a circular interval in one cyclic order

\[
x_1,x_2,\ldots,x_N.
\tag{8.1}
\]

If proper nonempty active targets exist, put

\[
\rho=\max\{|T\setminus K|:
\varnothing\ne T\setminus K\ne\{x_1,\ldots,x_N\}\}.
\tag{8.1a}
\]

Then \(1\le\rho\le N-1\), and the word

\[
K+x_1,\ldots,K+x_N,
K+x_1,\ldots,K+x_{\rho-1},K
\tag{8.2}
\]

represents every target and has length

\[
\boxed{N+\rho.}
\tag{8.3}
\]

#### Proof

A nonwrapping circular interval lies in the first period. A wrapping
interval of size at most \(\rho\) uses at most \(\rho-1\) symbols
after the cut, so it lies in the first period followed by the copied
prefix. The whole active coordinate set uses the first period, and the
empty active set uses \(K\). \(\square\)

This is the PC-tree/circular-ones counterpart of Theorem 4.1. Failure of
linear C1P is therefore not decisive even without an arbitrary Boolean
factorization.

If there is no proper nonempty active target, one full period followed
by \(K\) has length \(N+1\) and handles the degenerate case.

## 9. Global halo batching with moving PQ defect

Partition the owner start positions on cycles into \(R\) consecutive
arcs \(I_j\) of sizes \(s_j\), with

\[
\sum_{j=1}^{R}s_j=W.
\tag{9.1}
\]

Give each arc its forward \(H\)-halo. The corresponding Johnson path
\(Q_j\) has

\[
S_j=s_j+H-1
\tag{9.2}
\]

transitions. Suppose \(Q_j\) has nonempty core and active width \(w_j\).
Define \(\Delta_j^*\) to be the minimum defect (5.8) over all anchored
PQ atlases for \(Q_j\), and put \(\Delta_j^*=+\infty\) if no such atlas
exists.

### Theorem 9.1 (global moving-PQ compiler)

\[
\boxed{
L_H\le W+HR+\sum_{j=1}^{R}(w_j+\Delta_j^*).}
\tag{9.3}
\]

#### Proof

Choose a minimizing atlas for each finite \(\Delta_j^*\). Theorem 5.1
gives the \(j\)-th halo a word of length

\[
S_j+w_j+1+\Delta_j^*
=s_j+H+w_j+\Delta_j^*.
\]

Concatenate these words. Every required owner window is assigned to the
unique start arc containing its first owner, so it lies in that arc's
forward halo. Sum over \(j\) and use (9.1). \(\square\)

For the residence-cut batching count in the source note,

\[
R\le 2B+\frac{\nu_H+B}{b},
\tag{9.4}
\]

and \(w_j=O_A(H)\), this becomes

\[
\boxed{
L_H\le
W+O_A\!\left(HB+\frac{H\nu_H}{b}\right)
+\sum_j\Delta_j^*.}
\tag{9.5}
\]

Hence a sufficient PBBS gate within this moving-PQ architecture is

\[
\sum_j\Delta_j^*=o_A(W).
\tag{9.6}
\]

An isolated \(213\) motif is one-letter repairable, rather than forcing
an \(H\)-letter chart. Critical residence can therefore be batched if
the actual motifs admit compatible moving PQ orders with small total
defect. This conclusion is integral and chronology-sensitive; it is not
supplied by rankwise hypersimplex feasibility.

## 10. Exact baseline-recycling support atlases

The moving-PQ theorem preserves every required owner-window occurrence.
Literal OR needs less: each target value needs only one witness anywhere.
This permits reordering and fusing charts from distant PBBS packets.

Let \(\mathcal G\) be the family of all required target values in a
global owner system with \(W\) owner positions. A chart \(j\) consists
of:

1. a nonzero word \(\mathcal A_j\);
2. a charged multiset \(O_j\) of owner positions, of size \(M_j\);
3. a represented target subfamily
   \(\mathcal G_j\subseteq\mathcal G\);
4. an excess \(E_j\ge0\) such that

   \[
   |\mathcal A_j|\le M_j+E_j.
   \tag{10.1}
   \]

The chart represents the owner value at every charged position.
Different charts may charge the same physical owner.

Put

\[
M=\sum_jM_j,\qquad
U=\left|\bigcup_jO_j\right|,
\qquad
E=\sum_jE_j.
\tag{10.2}
\]

### Theorem 10.1 (baseline-recycling support atlas)

If

\[
\mathcal G=\bigcup_j\mathcal G_j
\tag{10.3}
\]

after owner targets are included, then one literal word has length

\[
\boxed{
L\le W+(M-U)+E.}
\tag{10.4}
\]

#### Proof

Concatenate the chart words. Every internal witness remains contiguous.
Append as one-letter sets the \(W-U\) owner values at positions charged
by no chart. The length is at most

\[
M+E+(W-U)=W+(M-U)+E.
\]

Condition (10.3) supplies every nonowner target, and charged or appended
letters supply every owner. \(\square\)

The exact toll of this atlas construction is therefore the multiplicity
overlap \(M-U\) plus intrinsic chart excess \(E\). It is not the number
of residence seams. This is an upper-bound ledger, not a necessary
invariant of arbitrary Boolean compilers.

## 11. Canonical PBBS calibration: two-core circular portals

Put

\[
n=2m+1,\qquad
W=\binom{2m+1}{m},\qquad
H=O_A(\sqrt m).
\tag{11.1}
\]

For a rainbow simple PBBS packet of height \(s\), the audited fixed-core
normal form gives two parity owner rows

\[
E_j=K\cup V_j,\qquad
O_j=K'\cup W_j
\qquad(0\le j\le s),
\tag{11.2}
\]

where \(K,K'\) are disjoint and \(V_j,W_j\) are consecutive
\(s\)-windows of one cyclic active order

\[
\Gamma=(\gamma_0,\ldots,\gamma_{2s}).
\tag{11.3}
\]

The two-core portal theorem in
MATH_ATTACK_W_PBBS_QUOTIENT_CYCLE_PHASE_FUSION_20260725.md proves:

1. a cyclic word of length \(2s+3\) represents all \(2s+2\) packet
   owners and every packet-internal lower intersection and upper union;
2. an ordinary word has length \(3s+2\);
3. the linearization port has length \(s-1\);
4. translated equal ordered ports splice literally and integrally.

The whole packet has no common nonempty core: the parity cores are
different and disjoint. Thus it is outside Theorem 4.1 and outside the
common-core atom model, and its **cyclic** excess is exactly one. This
does not by itself give an ordinary coefficient-one chart: the ordinary
opening toll is \(s-1\). It is an alternative two-core architecture
whose opening toll becomes negligible only after the normalized-type
fusion below. The genuine internal counterexample to necessity of
one-mountain is the common-core family in Section 7.

Now take a multiset of quotient packets of heights \(1\le s\le H\),
and include the complete deck of all \(n\) physical phase lifts of every
packet. Let

\[
q_s=\#\{\text{quotient packets of height }s\},
\qquad
T_s=\#\{\text{occupied normalized port types at height }s\}.
\tag{11.4}
\]

The numbers of physical packets and charged owner occurrences are

\[
R=n\sum_{s=1}^{H}q_s,
\qquad
M=n\sum_{s=1}^{H}q_s(2s+2).
\tag{11.5}
\]

### Theorem 11.1 (exact normalized-port fusion ledger)

The packet-internal targets and all packet owners have one ordinary
literal word of exact constructed length

\[
\boxed{
L_{\rm int}
=M+R+n\sum_{s=2}^{H}T_s(s-1).}
\tag{11.6}
\]

Moreover,

\[
\boxed{
n\sum_{s=2}^{H}T_s(s-1)<2Hn^{H-1}.}
\tag{11.7}
\]

#### Proof

Packets of one normalized type have ordered ports differing by one
ground translation. Order the quotient packets of that type in a path.
For each of the \(n\) initial phases, the translated port identity
determines a literal lifted path through all packets of the type, and
the \(n\) paths use every physical phase exactly once.

Every packet contributes its one cyclic excess position. Every lifted
type-chain contributes one final port of length \(s-1\). This is
(11.6).

After translating the first port symbol to zero, at most
\((n-1)_{s-2}\le n^{s-2}\) normalized types occur at height \(s\).
Thus

\[
\begin{aligned}
n\sum_{s=2}^{H}T_s(s-1)
&\le Hn\sum_{s=2}^{H}n^{s-2}\\
&<2Hn^{H-1}.
\end{aligned}
\]

\(\square\)

At Gaussian depth,

\[
2Hn^{H-1}
=\exp(O_A(\sqrt m\log m))
=o_A(W).
\tag{11.8}
\]

Hence port-type diversity is automatically below the coefficient-one
scale.

## 12. PBBS global packet-support theorem

Let \(\mathscr P\) be a complete-phase-deck multiset of rainbow simple
PBBS packets with

\[
\alpha H\le s(P)\le H
\tag{12.1}
\]

for one fixed \(\alpha>0\). Let \(M\) be charged owner multiplicity and
\(U\) the number of distinct physical owner positions in their union.

Call \(\mathscr P\) an **\(H\)-support cover** if every required PBBS
lower and upper target value through depth \(H\), except middle owners,
occurs among the internal targets of at least one selected packet.

### Theorem 12.1 (global packet atlas bypasses \(\nu_H\))

Let \(m\to\infty\) and
\(H=\lceil A\sqrt m\rceil\) (more generally,
\(H\to\infty\) and \(H=O_A(\sqrt m)\)).
Assume

\[
M=O_A(W),
\qquad
M-U=o_A(W),
\tag{12.2}
\]

and that \(\mathscr P\) is an \(H\)-support cover. Then there is a
nonzero central-band word with

\[
\boxed{
L_H
\le W+(M-U)+R+2Hn^{H-1}
=W+o_A(W).}
\tag{12.3}
\]

After the audited outer-tail diagonalization, this implies the
coefficient-one contiguous-OR bound.

#### Proof

Theorem 11.1 supplies an internal word of length at most

\[
M+R+2Hn^{H-1}.
\]

Append the \(W-U\) middle owner values not used by any selected packet.
The support-cover hypothesis says every other required target value
already has an internal packet witness. Therefore Theorem 10.1 gives
(12.3).

By (12.1),

\[
R(2\alpha H+2)\le M=O_A(W),
\]

so

\[
R=O_A(W/H)=o_A(W).
\]

The overlap term is \(o_A(W)\) by (12.2), and the type-opening term is
\(o_A(W)\) by (11.8). \(\square\)

### Corollary 12.2 (edge-disjoint packet cover)

If the selected physical packet arcs are internally edge-simple,
pairwise edge-disjoint, and are subpaths of the same exact PBBS owner
2-factor, then

\[
\boxed{M-U\le R.}
\tag{12.4}
\]

Hence an edge-disjoint Gaussian \(H\)-support cover with \(M=O(W)\)
satisfies Theorem 12.1.

#### Proof

A packet with \(2s+2\) owner positions contains \(2s+1\) distinct
owner edges. The packet family therefore uses \(M-R\) distinct edges.
These edges lie in the PBBS owner cycle factor, whose induced subgraph
has maximum degree two; every path or cycle component has at least as
many vertices as edges. Their vertex union therefore has at least
\(M-R\) positions, so
\(U\ge M-R\). \(\square\)

Theorem 12.1 is genuinely global. Packet charts may be reordered by
normalized type. Original cross-packet occurrences need not survive,
because literal OR requires each target value only once and the support
cover supplies an internal replacement witness.

## 13. Exact remaining PBBS alternatives

There are now two independent sufficient bypasses of the critical
residence ledger.

### Moving-PQ alternative

For the halo partition used in (9.3), prove

\[
\sum_j\Delta_j^*=o_A(W),
\tag{13.1}
\]

with \(w_j=O_A(H)\) and the existing batch count. The local \(213\)
pattern is PQ-feasible and one-letter repairable in the isolated
adjacent-braid model. Its contribution to the global \(\Delta\) is
unbounded without the sparse-braid or compatible moving-order
hypothesis.
Under the proved critical estimate
\(\nu_H=O_A(BH)\), choosing \(b\asymp H\) makes
\(R=O_A(B)\); hence all nondefect terms in (9.3) are
\(O_A(HB)=o(W)\).

### Packet-support alternative

For \(H=\lceil A\sqrt m\rceil\), prove the following
\(\mathrm{GPA}_A\) assertion:

> There is a complete-phase-deck multiset of rainbow simple PBBS packets
> of heights in \([\alpha_AH,H]\) which is an \(H\)-support cover and
> satisfies \(M=O_A(W)\) and \(M-U=o_A(W)\).

Then Theorem 12.1 gives

\[
\boxed{\mathrm{GPA}_A\Longrightarrow L_H=W+o_A(W)}
\tag{13.2}
\]

without any bound on \(\nu_H(P_m)\).

The audited PBBS results already prove:

1. every target has a canonical all-depth PBBS witness;
2. every simple return has the two-core circular normal form;
3. complete phase decks fuse by normalized port type with
   subexponential opening toll.

They do not prove that all target values can choose internal witnesses in
one low-overlap Gaussian packet atlas. A target of canonical load one may
force a packet absent from a naive return packing, and forced packets may
have linear owner overlap. The critical estimate for \(\nu_H\) neither
proves nor disproves this support-cover assertion.

An unconditional negative result for coefficient one itself must
therefore lower-bound interval Boolean rank:

\[
\operatorname{ibr}(M_H(P))
\ge S+\Omega(S)
\tag{13.3}
\]

for the relevant PBBS block family. A proof that
\(M-U+E=\Omega(W)\) for every support-cover atlas would close only
the packet-atlas route, not arbitrary literal compilers. Failure of one
PQ-tree, a \(213\) endpoint pattern, seam count, or rankwise
hypersimplex data cannot establish the general lower bound.

## 14. GKS chain-cover trees versus literal move-to-front chronology

This section compares the preceding compiler criteria with Jerrold Griggs,
Charles Killian, and Carla Savage, *Venn Diagrams and Symmetric Chain
Decompositions in the Boolean Lattice*, Electronic Journal of
Combinatorics 11 (2004), R2
([official article](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v11i1r2),
[official PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/v11i1r2/pdf/)).
It is a subordinate comparison: it does not replace the interval-Boolean or
moving-PQ criteria above.

### 14.1 What the planar chain-cover theorem actually says

For an SCD \(\mathcal C\), GKS call \(\pi\) a chain-cover map when, for
every nonroot chain \(C\), the starter of \(C\) covers an element of
\(\pi(C)\), and the terminator of \(C\) is covered by an element of
\(\pi(C)\).  The parent relation is a rooted chain-cover tree.  In their
Lemma 1, the nodes are put in preorder and the preorder label is used only
as the horizontal coordinate of a planar embedding.  The resulting Venn
diagram in their Theorem 2 is obtained by planar duality; the preorder is
not asserted to be a walk through the chain-cover graph.

For the Greene--Kleitman SCD, a chain starter \(x\) has no unmatched
\(1\)'s.  If \(S(x)\ne\varnothing\), GKS Lemma 9 defines its parent by

\[
 S(y)=S(x)\setminus\{\max S(x)\}.
\tag{14.1}
\]

The child is two ranks shorter than its parent, so siblings have equal
length.  GKS Note 2 consequently permits arbitrary sibling orders (and even
placing their parent among them) without spoiling the planar drawing.  This
is geometric freedom.  It contains no assertion about the recency order of
the difference blocks at two consecutive chain endpoints.

### 14.2 Exact MTF distance and the endpoint-schedule ledger

Let \(V\ne\varnothing\) be finite and let

\[
 \Sigma=(C_1,\ldots,C_a)
\tag{14.2}
\]

be an ordered partition of \(V\).  For a nonempty update mask \(X\), put

\[
 M_X(\Sigma)
 =\bigl(X,C_1\setminus X,\ldots,C_a\setminus X\bigr),
\tag{14.3}
\]

deleting empty blocks.  For a target state

\[
 \Pi=(B_1,\ldots,B_b),
 \qquad U_t=B_1\cup\cdots\cup B_t,
\tag{14.4}
\]

define

\[
 \delta(\Sigma,\Pi)
 =\min\bigl\{0\le t\le b:
 D_{U_t}(\Sigma)=(B_{t+1},\ldots,B_b)\bigr\},
\tag{14.5}
\]

where \(D_U\) deletes \(U\) from every source block and then deletes empty
blocks.  The set in (14.5) is nonempty because \(t=b\) always works.

#### Theorem 14.1 (exact stable deletion-suffix distance)

The minimum number of MTF updates carrying \(\Sigma\) to \(\Pi\) is

\[
 \boxed{d_{\rm MTF}(\Sigma,\Pi)=\delta(\Sigma,\Pi).}
\tag{14.6}
\]

If a positive number of update positions is required even when the two
states agree, the exact distance is

\[
 \boxed{d^+_{\rm MTF}(\Sigma,\Pi)=\max\{1,\delta(\Sigma,\Pi)\}.}
\tag{14.7}
\]

In particular, a one-position transition is possible exactly when

\[
 \boxed{
 \Pi=\bigl(B_1,D_{B_1}(\Sigma)\bigr),
 }
\tag{14.8}
\]

including the harmless idempotent case \(\Sigma=\Pi\).

#### Proof

After updates \(X_1,\ldots,X_q\), group coordinates by their last update
time.  The final state consists of the nonempty blocks

\[
 X_q,\quad
 X_{q-1}\setminus X_q,\quad\ldots,\quad
 X_1\setminus\bigcup_{j=2}^{q}X_j
\tag{14.9}
\]

in that order, followed by

\[
 D_{X_1\cup\cdots\cup X_q}(\Sigma).
\tag{14.10}
\]

If the result is \(\Pi\), the nonempty last-time classes in (14.9) form
some target prefix \(B_1,\ldots,B_t\), with \(t\le q\), and (14.10) is
the remaining target suffix.  Hence \(\delta\le t\le q\).

Conversely, for \(t=\delta>0\), apply

\[
 U_t,U_{t-1},\ldots,U_1.
\tag{14.11}
\]

Their last-time classes are \(B_1,\ldots,B_t\), and (14.5) supplies the
suffix.  If \(t=0\), one idempotent update \(B_1\) gives the positive-slot
version.  This proves (14.6)--(14.8). \(\square\)

If source and target order the same fixed atom blocks, let \(\lambda\) be
the longest suffix of the target whose atoms occur in the source in the
same relative order.  Then

\[
 \delta=b-\lambda.
\tag{14.12}
\]

Thus an allowed PQ-tree reversal of \(b\) atom blocks can cost \(b-1\)
literal MTF updates.  Moving their union once coalesces the union into one
tied block; it does not stably move the difference blocks as separate
blocks.  This is the exact incompatibility hidden by a purely setwise C1P
test.

Now fix a chain order \(C_1,\ldots,C_N\), and choose one exposing state
\(\Sigma_i\) for each chain.  Require distinct designated update
occurrences, and use the positive-slot distance (14.7).  Between the first
and last designated endpoints, the exact number of positions is

\[
 N+\mathcal H(\Sigma_1,\ldots,\Sigma_N),
\tag{14.13}
\]

where the internal transition defect is

\[
 \boxed{
 \mathcal H
 =\sum_{i=1}^{N-1}
   \bigl(\delta(\Sigma_i,\Sigma_{i+1})-1\bigr)_+ .
 }
\tag{14.14}
\]

Indeed, consecutive designated endpoints are separated by at least their
exact MTF distance, and concatenating the shortest bridges from Theorem
14.1 attains equality.

Let \(\iota(C_1,\Sigma_1)\) be the exact least number of initial letters
needed to reach an occurrence exposing \(C_1\) in state \(\Sigma_1\), with
no pre-word history credited.  Writing all \(a=|\Sigma_1|\) blocks in
reverse order proves

\[
 \iota(C_1,\Sigma_1)\le a\le k.
\tag{14.14a}
\]

If every block of \(\Sigma_1\) is required to have appeared before the first
endpoint (in particular for the full root chain), equality
\(\iota=a\) holds.  In general a terminal residual block outside the first
chain top can remain unseen, so the exact initialization cost should not be
replaced blindly by \(a\).  The full fixed-order length is

\[
 L=\iota(C_1,\Sigma_1)
   +\sum_{i=1}^{N-1}d_{\rm MTF}^+(\Sigma_i,\Sigma_{i+1})
  =N+\bigl(\iota(C_1,\Sigma_1)-1\bigr)+\mathcal H.
\tag{14.14b}
\]

A linear word needs no terminal closure; a cyclic schedule would pay that
additional toll separately.  Consequently, the exact fixed-state sharp
budget is

\[
 \bigl(\iota(C_1,\Sigma_1)-1\bigr)+\mathcal H\le d(k).
\tag{14.14c}
\]

Even after initialization is deliberately ignored, the necessary condition
is

\[
 \mathcal H\le d(k),
\tag{14.15}
\]

whereas a coefficient-one compiler requires total internal and boundary
defect \(o(W)\).

For state fibres \(\mathcal E(C_i)\), one must minimize jointly.  The exact
finite-length dynamic program is

\[
 F_1(\Sigma)=\iota(C_1,\Sigma)-1,
\qquad
 F_{i+1}(\Pi)
 =\min_{\Sigma\in\mathcal E(C_i)}
 \left[F_i(\Sigma)+(\delta(\Sigma,\Pi)-1)_+\right].
\tag{14.16}
\]

Independently minimizing every adjacent fibre pair is invalid: the state
chosen as the head of one transition is the tail of the next.

If only the internal defect \(\mathcal H\) is being minimized, replace the
first line of (14.16) by \(F_1(\Sigma)=0\).  For coefficient one the two
versions differ by at most \(k=o(W_k)\), but that equivalence is scoped to
the one-endpoint-per-SCD-chain architecture.

### 14.3 Chain fibres and the exact one-step quotient test

Write a saturated chain as

\[
 C:\quad
 A\subset A+e_1\subset\cdots\subset A+e_1+\cdots+e_h.
\tag{14.17}
\]

An ordered partition exposes all its nonempty members as prefix unions if
and only if it has the form

\[
 (P_1,\ldots,P_s,
   \{e_1\},\ldots,\{e_h\},
   Q_1,\ldots,Q_t),
\tag{14.18}
\]

where the \(P_i\) partition \(A\), and the \(Q_i\) partition the
complement of the chain top.  Thus the chain difference order is a forced
singleton spine even though the two exterior parts may be refined.

Let \(D\) be a target chain with nonempty minimum \(B\).  There exist
states in the fibres of \(C,D\) and one MTF update from the former to the
latter if and only if

\[
 \boxed{C-B\text{ and }D-B\text{ are cross-nested}.}
\tag{14.19}
\]

Necessity follows because both quotient chains must be prefix chains of the
same residual state after deleting the update.  For sufficiency, merge the
two cross-nested quotient chains into one maximal Boolean chain, choose its
singleton order, and insert the deleted elements in the positions forced by
\(C\); updating \(B\) then exposes \(D\).  This proves (14.19) over the
full state fibres, not merely over canonical singleton representatives.

If the target minimum is empty, the update is instead forced to be the
singleton first increment of the target chain; after deleting that anchor,
the remaining quotient chains must pass the same cross-nesting test.

### 14.4 Exact audit of Greene--Kleitman cover edges

Let \(C_x\) be a nonroot Greene--Kleitman chain.  Put

\[
 j=\max S(x),
\tag{14.20}
\]

and let \(m<j\) be the zero matched to the \(1\) at position \(j\).
Write the unmatched zeros of \(x\) as

\[
 U_0(x)=L\mathbin{\dot\cup}R,
 \qquad L<m<j<R,
\tag{14.21}
\]

with both \(L,R\) in increasing order.  There is no unmatched zero between
\(m\) and \(j\), because \(j\) would have matched the rightmost such zero.
For the GKS parent \(C_y=\pi(C_x)\), Lemma 9 gives

\[
 S(y)=S(x)-j,
 \qquad
 U_0(y)=L,m,j,R.
\tag{14.22}
\]

Thus, writing \(A=S(y)\), the parent and child increment profiles are

\[
 \begin{array}{c|c|c}
 &\text{minimum}&\text{successive singleton increments}\\ \hline
 C_y&A&L,m,j,R\\
 C_x&A+j&L,R.
 \end{array}
\tag{14.23}
\]

#### Theorem 14.2 (GKS cover-edge MTF classification)

One has

\[
 \boxed{
 C_y\longrightarrow C_x\text{ in one MTF update}
 \iff R=\varnothing
 \iff j=k.
 }
\tag{14.24}
\]

The reverse direction \(C_x\to C_y\) is impossible when
\(A\ne\varnothing\).  When \(A=\varnothing\), the only reverse-compatible
cover edge is

\[
 01*^{\,k-2}\longrightarrow *^k.
\tag{14.25}
\]

#### Proof

Quotient (14.23) by the target minimum \(A+j\).  If
\(R\ne\varnothing\), let \(r_1\) be its first element.  The parent quotient
contains the prefix \(L+m\), while the child quotient contains
\(L+r_1\).  These sets cross.  If \(R=\varnothing\), the two quotient
chains are nested.  Equation (14.19) proves the first equivalence.

All coordinates after \(j=\max S(x)\) are zeros and can never subsequently
be matched, so they lie in \(R\).  Hence \(R=\varnothing\) exactly when
\(j=k\).

For the reverse direction with \(A\ne\varnothing\), quotient by \(A\).
The child begins with \(\{j\}\), while the parent first acquires a
different singleton from \(L,m\); the two quotient chains cross.  If
\(A=\varnothing\), the empty-minimum anchor is the first root increment.
The same prefix audit leaves only \(j=2,m=1\), giving (14.25), and updating
coordinate \(1\) realizes it. \(\square\)

Let

\[
 W_k=\binom{k}{\lfloor k/2\rfloor}.
\tag{14.26}
\]

A Greene--Kleitman template either ends in a star or in a fixed \(1\).
Deleting a terminal star bijects the former family with the templates in
dimension \(k-1\).  Hence Theorem 14.2 gives exactly

\[
 W_k-W_{k-1}
\tag{14.27}
\]

forward-compatible cover edges.  They form a matching: a compatible parent
ends in a star, its unique compatible child closes its last available pair
at coordinate \(k\) and ends in \(1\).  In a directed vertex-disjoint path
forest, using the exceptional reverse edge (14.25) forces one to discard
its tail's forward matching edge.  Hence for \(k\ge4\) the maximum number
of usable cover arcs remains \(W_k-W_{k-1}\).

Therefore, for \(k\ge4\), every vertex-disjoint path cover using only GKS
cover-tree MTF arcs has at least

\[
 \boxed{W_{k-1}}
\tag{14.28}
\]

components.  Explicitly,

\[
 \frac{W_{k-1}}{W_k}
 =\begin{cases}
 1/2,&k\text{ even},\\[1mm]
 (k+1)/(2k),&k\text{ odd}.
 \end{cases}
\tag{14.29}
\]

Thus the edge-faithful chain-cover route is exactly the already audited
last-pair matching, with a half-sized start set.  It cannot give either
additive \(d(k)\) or coefficient one by separately reinitializing its
components: every component-first state exposing a proper nonempty Boolean
chain has at least two blocks, hence costs at least one position beyond its
first designated endpoint.  Joining components by a new one-step non-cover
arc would instead leave the edge-faithful architecture.

There is also a topology-only warning.  A walk restricted to the edges of
a tree on \(N\) vertices and visiting every vertex has at least

\[
 2(N-1)-\operatorname{diam}(T)
\tag{14.30}
\]

steps; every edge off the start--finish path must be crossed twice.  The GKS
tree has depth at most \(\lfloor k/2\rfloor\), so an edge-only traversal
repeats \(N-1-O(k)\) chain occurrences.  Replacing preorder by a contour
walk therefore does not repair the literal ledger.

### 14.5 The canonical preorder exceeds the sharp \(d(k)\) budget

The preceding matching no-go restricts transitions to cover edges.  The
standard GKS preorder also makes non-cover jumps between subtrees.  Those
jumps do not rescue the sharp finite budget.

The root has the \(k-1\) child chains

\[
 D_b:\quad S(x)=\{b\},
 \qquad 2\le b\le k,
\tag{14.31}
\]

because the unique \(1\) at \(b\) matches \(b-1\).  Its increment list is

\[
 [k]\setminus\{b-1,b\}
\tag{14.32}
\]

in increasing order.  In the parent-first preorder, every child subtree is
contiguous, and the last node of a subtree is a leaf.

#### Lemma 14.3 (early root-child entry obstruction)

Assume \(k\ge7\).  No leaf chain can precede \(D_b\) in one MTF update when

\[
 2\le b\le k-2.
\tag{14.33}
\]

The same conclusion holds for \(k=6\).

#### Proof

If a Greene--Kleitman starter \(z\) is a leaf of the chain-cover tree, then

\[
 \max S(z)\in\{k-1,k\}.
\tag{14.34}
\]

Indeed, if \(\max S(z)\le k-2\), the final two coordinates are unmatched
zeros; changing the last zero to \(1\) closes that pair and creates a child
whose parent is \(z\).

Suppose a leaf chain \(C_z\) could precede \(D_b\).  Quotient by the target
minimum \(\{b\}\), and put

\[
 Q=S(z)\setminus\{b\}.
\tag{14.35}
\]

By (14.19), \(Q\) is comparable with every prefix of the ordered list
(14.32).  A set comparable with every prefix of a linear order is either a
prefix or contains the whole ordered ground set.  The latter is impossible
because a chain starter has size at most \(\lfloor k/2\rfloor\), whereas
(14.32) has size \(k-2\).  Thus \(Q\) must be a prefix.

For \(b\le k-2\), (14.34) says that this prefix reaches coordinate
\(k-1\) or \(k\); it therefore has size at least \(k-3\).  This exceeds
\(\lfloor k/2\rfloor\) for \(k\ge7\), a contradiction.

For \(k=6\), equality could only give the three candidate starters

\[
 \{3,4,5\},\qquad \{1,4,5\},\qquad \{1,2,5\}
\tag{14.36}
\]

for \(b=2,3,4\), respectively.  The last two begin with an unmatched
\(1\); in the first, the third \(1\) is unmatched after the two initial
zeros have been consumed.  None is a Greene--Kleitman starter. \(\square\)

#### Theorem 14.4 (canonical GKS preorder is not sharp-optimal)

For every \(k\ge6\), every parent-first planar preorder of the GKS
chain-cover tree, with arbitrary sibling orders and arbitrary exposing
states, has

\[
 \boxed{\mathcal H\ge k-3.}
\tag{14.37}
\]

Consequently it cannot be linearized with only \(d(k)\) transition states.

#### Proof

There are \(k-3\) early root subtrees \(D_b\), \(2\le b\le k-2\).
If such a subtree is first, the root-to-child transition is impossible by
Theorem 14.2, since \(b<k\).  If it is not first, its predecessor is the
last leaf of the preceding root-child subtree, so Lemma 14.3 applies.  Thus
each early subtree contributes a distinct non-unit boundary, proving
(14.37).

Put \(r=\lceil k/2\rceil\).  Since the strict-lower target count is a sum
of \(r-1\) rank sizes, each at most \(W_k\), the defining inequality for
the sharp allowance gives

\[
 d(k)\le r-1<k-3
\tag{14.38}
\]

for \(k\ge6\).  Hence (14.15) fails even before initialization or terminal
closure is charged. \(\square\)

The strict inequality in (14.38) is immediate for \(k\ge6\): for
\(k=6\), \(r-1=2<3\), and it only widens thereafter.

There is a small composability warning already in \(B_4\).  With the GKS
labels of their Figure 2, the tree has root \(C_1\), root-child blocks

\[
 (C_2,C_6),\qquad(C_3,C_5),\qquad(C_4).
\tag{14.39}
\]

The only sibling order with merely one pairwise-incompatible boundary is

\[
 C_1,C_4,C_3,C_5,C_2,C_6.
\tag{14.40}
\]

For completeness, put \(A=(C_2,C_6)\), \(B=(C_3,C_5)\), and
\(C=(C_4)\).  The quotient-chain test gives

\[
\begin{array}{c|ccc}
 &A&B&C\\ \hline
C_1\to\text{first block}&\text{no}&\text{no}&\text{yes}\\
\text{last of }A\to\text{first of }(\cdot)&-&\text{no}&\text{no}\\
\text{last of }B\to\text{first of }(\cdot)&\text{yes}&-&\text{no}\\
\text{last of }C\to\text{first of }(\cdot)&\text{no}&\text{no}&-
\end{array}
\tag{14.40a}
\]

so every other permutation of the three subtree blocks already has at
least two non-unit boundaries.

The forced singleton states of the three nontrivial children are

\[
 C_2:2|3|4|1,\quad
 C_3:3|1|4|2,\quad
 C_4:4|1|2|3.
\tag{14.41}
\]

After the one-step transition \(C_3\to C_5\), the only reachable states
exposing the singleton chain \(C_5=\{3,4\}\) are

\[
 4|3|1|2,qquad 34|1|2.
\tag{14.42}
\]

Neither can move in one step to \(2|3|4|1\): the first has residual order
\(4,3,1\) after deleting \(2\), and the second has the tied residual block
\(34\).  Thus the two individually feasible incident transitions do not
compose.  Once \(C_1\)'s state is supplied, two internal transition states
are both necessary and sufficient, while \(d(4)=1\).  Sufficiency for that
internal ledger is witnessed by the explicit update/state chain

\[
\begin{aligned}
1|2|3|4
&\xrightarrow{4}4|1|2|3
\xrightarrow{13}13|4|2
\xrightarrow{3}3|1|4|2\\
&\xrightarrow{4}4|3|1|2
\xrightarrow{23}23|4|1
\xrightarrow{2}2|3|4|1
\xrightarrow{4}4|2|3|1.
\end{aligned}
\tag{14.43}
\]

The selected states expose, in order,
\(C_1,C_4,C_3,C_5,C_2,C_6\); the states after updates \(13\) and \(23\)
are the two internal transition states.  Initializing
\(C_1=1|2|3|4\) itself takes four letters, so this is not a general
\(B_4\) compiler lower bound; it is the smallest literal example of the
stable-block collateral hidden by independent pairwise tests.

### 14.6 The corrected erosion-controller lift

The direct endpoint audit is not the whole exact construction target.
Put

\[
 r=\left\lceil\frac{k}{2}\right\rceil,\qquad
 1\le d<r,\qquad s=r-d.
\tag{14.44}
\]

The corrected flat architecture first seeks a controller

\[
 P_0,P_1,\ldots,P_{W+d-1}
\tag{14.45}
\]

whose flat interior consists of rank-\(s\) Johnson steps (with the usual
one-sided boundary ramps, or cyclically), and defines

\[
 T_i=\bigcup_{j=i}^{i+d}P_j,
\qquad 0\le i<W.
\tag{14.46}
\]

The \(T_i\)'s must be the \(W\) distinct rank-\(r\) middle owners.

#### Theorem 14.5 (exact prescribed-chronology controller screen)

Suppose every controller step satisfies

\[
 |P_j\setminus P_{j+1}|\le1,\qquad
 |P_{j+1}\setminus P_j|\le1,
\tag{14.45a}
\]

so the flat interior is Johnson-adjacent and the one-sided ramps are also
unit steps.  If all sets in (14.46) are distinct of rank \(r\), then:

1. \(T_0,\ldots,T_{W-1}\) is a rank-\(r\) Johnson path;
2. every internal positive coordinate run in \(T\) has length at least
   \(d+1\).

Conversely, if a rank-\(r\) Johnson chronology \(T\) has every internal
positive coordinate run of length at least \(d+1\), then its maximal
erosion

\[
 P_j=\bigcap_{i=\max(0,j-d)}^{\min(j,W-1)}T_i
\tag{14.47}
\]

has flat-interior rank \(r-d\), is Johnson-adjacent there, and its
\((d+1)\)-window unions recover \(T\).  Thus, with the one-sided boundary
conventions retained, Johnson adjacency plus the run condition is the exact
gate for a **prescribed** middle chronology.

#### Proof

The old and new windows in (14.46) overlap in
\(P_{i+1},\ldots,P_{i+d}\).  Hence

\[
 T_i\setminus T_{i+1}\subseteq P_i\setminus P_{i+1},
\qquad
 T_{i+1}\setminus T_i
 \subseteq P_{i+d+1}\setminus P_{i+d}.
\tag{14.48}
\]

Both right sides have size at most one.  Equal rank and distinctness force
each difference on the left to have size one, proving Johnson adjacency.

For one coordinate \(x\), a \(P\)-run \([a,b]\) dilates under (14.46) to
the \(T\)-interval

\[
 [a-d,b],
\tag{14.49}
\]

clipped only at the two global boundaries.  Its unclipped length is
\((b-a+1)+d\ge d+1\).  Overlapping dilated runs merge and only become
longer.  This proves the run condition.  The converse is precisely the
coordinatewise erosion--dilation identity together with the Johnson
controller identities in
MATH_EROSION_JOHNSON_CONTROLLER_DUALITY_20260728.md. \(\square\)

Now let \(A_i\) be the physical update at controller position \(i\), and
put

\[
 F_i=(P_i\setminus P_{i-1})\cup(P_i\setminus P_{i+1})
\tag{14.50}
\]

at an interior position.  Controller duality forces

\[
 F_i\subseteq A_i\subseteq P_i.
\tag{14.51}
\]

If the state after \(A_i\) is also required to expose an SCD chain \(C_i\)
with nonempty minimum \(B_i\), then its first MTF block must be contained in
\(B_i\).  Therefore every controller-compatible chain endpoint satisfies
the additional necessary port-anchor condition

\[
 \boxed{F_i\subseteq A_i\subseteq P_i\cap B_i.}
\tag{14.52}
\]

For the root chain, whose minimum is empty, \(A_i\) is instead forced to be
the singleton first increment.  Formula (14.52) is only a necessary local
screen: the residual ordered blocks must still pass Theorem 14.1, and every
coordinate run of \(P\) must satisfy the exact pin rule.  Namely, for an
internal maximal \(x\)-run \([u,v]\), put

\[
 Q_x=\{j\in[u,v]:x\in A_j\}.
\tag{14.52a}
\]

Then

\[
 \boxed{
 u,v\in Q_x,\qquad q_{\ell+1}-q_\ell\le d+1
 \text{ for consecutive pins in }Q_x.
 }
\tag{14.52b}
\]

Boundary runs have the corresponding one-sided endpoint rule.

In particular, a GKS root child has singleton minimum \(\{b\}\).  If it is
used as an interior controller endpoint, (14.52) forces both incident
controller ports to be \(b\), so \(b\) has a one-vertex run in \(P\).
This is legal and gives a length-\((d+1)\) run in \(T\); it is a structural
constraint, not by itself a contradiction.

### 14.7 The natural GKS middle preorder is not a controller

Associate to each Greene--Kleitman chain its unique rank-\(r\) member, and
list these members in a parent-first GKS preorder with arbitrary sibling
orders.  This is the most direct way to use the chain-cover preorder as the
middle chronology \(T\).  It fails at positive depth in every dimension
\(k\ge4\).

#### Theorem 14.6 (embedded \(B_4/B_5\) controller obstruction)

Let \(k\ge4\), \(r=\lceil k/2\rceil\), and \(1\le d<r\).  No parent-first
GKS preorder of the natural rank-\(r\) chain members, with any sibling
orders, is representable by (14.46) for a rank-\((r-d)\) Johnson
controller.

#### Proof for even \(k\)

Write \(k=2h+4\), and prefix every Greene--Kleitman template in \(B_4\)
by the fixed matched word

\[
 (01)^h.
\tag{14.53}
\]

The subtree rooted at \((01)^h****\) is exactly the \(B_4\) GKS
chain-cover tree: every prefix coordinate is already matched, and all
descendant parent operations act only on the final four coordinates.
Every parent-first preorder visits this subtree contiguously.

The fixed prefix contributes one common \(h\)-set.  After deleting that
core, the six natural rank-\(r\) members are

\[
\begin{array}{c|c|c}
\text{node}&\text{local template}&\text{local rank-two member}\\ \hline
C_1&****&12\\
C_2&01**&23\\
C_6&0101&24\\
C_3&*01*&13\\
C_5&0011&34\\
C_4&**01&14.
\end{array}
\tag{14.54}
\]

The three root-child blocks are

\[
 A=(23,24),\qquad B=(13,34),\qquad C=(14).
\tag{14.55}
\]

All six sibling orders have the following exact audit:

\[
\begin{array}{c|c|c}
\text{order}&\text{local chronology after }12&\text{obstruction}\\ \hline
ABC&23,24,13,34,14&24\to13\text{ is not Johnson}\\
ACB&23,24,14,13,34&3\text{ occurs only in }23\\
BAC&13,34,23,24,14&4\text{ occurs only in }34\\
BCA&13,34,14,23,24&14\to23\text{ is not Johnson}\\
CAB&14,23,24,13,34&14\to23\text{ is not Johnson}\\
CBA&14,13,34,23,24&4\text{ occurs only in }14.
\end{array}
\tag{14.56}
\]

The three singleton occurrences in (14.56) are internal: they are flanked
inside the displayed subtree by sets omitting that coordinate.  Adding the
common prefix core changes neither the Johnson differences nor those runs.
Theorem 14.5 excludes every row.

#### Proof for odd \(k\)

Write \(k=2h+5\), prefix all \(B_5\) templates by \((01)^h\), and use
the natural **upper** middle rank \(r=h+3\).  The subtree rooted at
\((01)^h*****\) is exactly the \(B_5\) GKS tree and is contiguous.
After deleting the common fixed-prefix core, its root and four
parent-first child blocks are

\[
\begin{aligned}
R&=(123),\\
A^+&=(234,245,235),&
A^-&=(234,235,245),\\
B^+&=(134,345,135),&
B^-&=(134,135,345),\\
C&=(124,145),&
D&=(125).
\end{aligned}
\tag{14.57}
\]

Here the signs are the two possible orders of the two leaf children in the
\(A\)- and \(B\)-subtrees.  We audit only boundaries which are both Johnson
and free of a positive singleton run at the middle set:

\[
\begin{array}{c|c}
\text{oriented block}&\text{only possible safe continuation}\\ \hline
A^+&\text{none (hence it must be last)}\\
A^-&C\\
B^+&D\\
B^-&A\\
C&D\\
D&C\text{, subject to its incoming edge}.
\end{array}
\tag{14.58}
\]

For example, \(A^+\) can be followed Johnson-adjacently only by \(D\),
but the triple

\[
 245,235,125
\tag{14.59}
\]

gives coordinate \(3\) a singleton positive run.  For \(A^-\), the
candidate \(D\) similarly makes coordinate \(4\) singleton at \(245\),
whereas \(C\) is safe.  The remaining rows follow from

\[
\begin{array}{c|c}
B^+\to D&(345,135,125)\text{ is safe}\\
B^-\to A&(135,345,234)\text{ is safe}\\
C\to B&(124,145,134)\text{ has singleton }5\\
C\to D&(124,145,125)\text{ is safe}.
\end{array}
\tag{14.60}
\]

The entry from the local root \(R\) supplies the final obstruction.
Entering either \(A^-\) or \(B^-\) inserts coordinate \(4\) and deletes it
on the very next step, so those orientations cannot be first.  If \(A^+\)
is first, it cannot continue safely.  If \(B^+\) is first, (14.58) forces

\[
 B^+\to D\to C,
\tag{14.61}
\]

after which the unused \(A\)-block cannot be entered.  If \(C\) is first,
it forces \(C\to D\) and stops before \(A,B\).  If \(D\) is first, the
triple

\[
 123,125,124
\tag{14.62}
\]

gives coordinate \(5\) a singleton positive run.  Thus no permutation of
the four child blocks is both Johnson and free of an internal length-one
positive run.  Theorem 14.5 again excludes every \(d\ge1\). \(\square\)

There is an even simpler failure of the most literal controller assignment.
Only

\[
 \binom{k}{r-d}
\tag{14.63}
\]

of the \(W_k\) SCD chains meet rank \(r-d\): every set at that rank lies
in one chain, and one chain contains at most one set of that rank.  Hence

\[
 W_k-\binom{k}{r-d}\ge0
\tag{14.64}
\]

preorder nodes have no native rank-\((r-d)\) member at all.  The inequality
is strict for even \(k\), and for odd \(k\) whenever \(d\ge2\).  Equality
occurs for odd \(k\) at \(d=1\), because every symmetric chain meets both
middle ranks.  Thus the native-rank count alone is not an odd-\(d=1\)
obstruction; Theorem 14.6 supplies the chronology obstruction there.
Whenever (14.64) is strict, ancestor projection, repetition, or a moving
frame would be a new controller construction, not something supplied by
chain cover.  In every case Theorem 14.6 rules out any such construction
whose window unions are still required to follow the natural
middle-member preorder.

Finally, once a valid controller \(P\) exists, the run-pin condition alone
is not an additional existence obstruction.  Taking

\[
 A_j=P_j
\tag{14.65}
\]

pins every controller-run position, so endpoints are pinned and all gaps
are \(1\le d+1\), while \(D^dA=T\).  This proves only controller and pin
feasibility.  It does **not** make the physical word expose the strict lower
members of the GKS chains, nor does it cover the whole lower ideal.

### 14.8 Exact conclusion for the compiler lane

The GKS analogy yields one useful diagnostic but no new compiler recursion.

1. An edge-faithful chain-cover schedule is rigorously closed: its usable
   forward arcs are the last-pair matching, together with the unique reverse
   root arc (14.25), and every path cover still has
   \(\Theta(W_k)\) components.
2. The standard planar preorder is rigorously closed at the sharp
   \(W_k+d(k)\) target by Theorem 14.4.
3. The natural rank-\(r\) middle-member preorder is not even a
   positive-depth erosion chronology, by the embedded \(B_4/B_5\)
   obstruction in Theorem 14.6.
4. The lower bound \(k-3=o(W_k)\) does **not** by itself refute an
   asymptotic \(W_k+o(W_k)\) schedule using non-cover jumps.  Such a
   schedule exists exactly when the state-fibre dynamic program (14.16),
   optimized over the permitted chain order, has total defect \(o(W_k)\).
   The GKS planarity proof gives no estimate for that quantity.

Theorems 14.4 and 14.6 are scoped to the parent-first preorder used in GKS
Lemma 1.  They do not audit the larger Note 2 class in which a parent column
is interspersed among its child-subtree blocks.  Such orders are neither
proved good nor proved bad here; their endpoint version is governed by
(14.16), and their controller version by Theorem 14.5 plus the pin rule
(14.52b).

Thus the precise incompatibility is stable move-to-front of the chain
difference blocks.  A successful transfer to the Johnson/PBBS compiler
would have to construct new non-cover state-fibre arcs with deletion-suffix
defect \(o(W)\), or translated equal ports as in Section 11.  That is the
same chronology-sensitive state-transversal gate already isolated by the
moving-PQ theorem, not a consequence of SCD chain cover.

## 15. Proved and unproved boundary

Proved here:

1. the exact interval Boolean-rank characterization of arbitrary literal
   compilers;
2. the equivalent interval-kernel criterion;
3. the exact repeated-atom and ordinary PQ-tree specializations;
4. the collapse of one-mountain and repetition-free C1P to FIFO under
   the source theorem's single-run Johnson hypotheses;
5. the moving-PQ compiler with exact defect \(\Delta\);
6. the crossing-grid common-deque criterion and feasibility of \(213\);
7. sparse-braid and explicit non-one-mountain \(S+O(1)\) compilers;
8. the bounded circular-arc compiler;
9. the global halo ledger (9.3);
10. the exact baseline-recycling atlas ledger; and
11. the PBBS global packet-support theorem (12.3);
12. the exact stable deletion-suffix MTF metric and joint endpoint-schedule
    dynamic program;
13. the exact GKS cover-edge classification and its
    \(W_{k-1}\)-component edge-faithful obstruction; and
14. the \(k-3\) transition lower bound for every parent-first GKS preorder;
15. the exact erosion-controller chronology screen and port-anchor
    necessity; and
16. the embedded \(B_4/B_5\) no-go for the natural parent-first GKS
    middle-member chronology at every positive depth.

Imported audited inputs:

1. the PBBS simple-return fixed-core normal form;
2. the two-core circular portal compiler;
3. normalized-port complete-deck splicing and type count; and
4. the outer product-SCD tail/diagonalization;
5. erosion--Johnson controller duality and the exact run-pin rule; and
6. the GKS chain-cover/preorder and Greene--Kleitman parent-map theorems
   cited in Section 14.

Not proved:

1. the moving-PQ defect bound (13.1) for canonical PBBS halos;
2. \(\mathrm{GPA}_A\);
3. a low-overlap target-cover selection of Gaussian simple packets;
4. a direct \(W+o(W)\) interval Boolean factorization for the complete
   PBBS target matrix; or
5. a matching linear interval-Boolean-rank obstruction;
6. an \(o(W_k)\)-defect GKS-chain endpoint schedule using non-cover
   state-fibre arcs; or
7. a no-go for all such non-cover schedules (the cover-tree and canonical
   preorder no-gos do not imply this);
8. a controller realization of a non-parent-first Note 2 planar order; or
9. a proof that an unrelated moving-frame controller can exploit GKS labels
   while abandoning their natural middle-member chronology.

One-mountain is conclusively not necessary. The exact general invariant is
interval Boolean rank, and the strongest current constructive bypass is
either a low-defect moving PQ atlas or a low-overlap canonical PBBS packet
support cover.
