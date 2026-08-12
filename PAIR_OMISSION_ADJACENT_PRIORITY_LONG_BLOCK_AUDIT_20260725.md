# Adjacent pair priority and long-block interpolation: exact exchange order, boundary toll, and the surviving gate

Date: 2026-07-25

## 1. Verdict

Let (M,N) be two lower-saturating matchings in the pair-omission token
multigraph.  Componentwise interpolation is more rigid than an arbitrary
choice of long subblocks.

* On an alternating cycle of (M\triangle N), an exact central child has
  only the two endpoint orientations.
* On an alternating path, every exact central child has one and only one
  transition: it takes an initial block of the (M)-edges and a terminal
  block of the (N)-edges, in **alternating-component order**.

The second point does not by itself preserve the physical predecessor
correlation.  Alternating-component order and physical source-row order are
unrelated by the present first-avoided-pair theorem.  A single legal
component threshold can be interlaced through its physical rows and create
linearly many run starts, even though both endpoint matchings have one run.

For an adjacent swap of omitted-pair priorities, the changed lower targets
are explicit and can have linear mass.  The number of open alternating
paths is nevertheless only (O(W/m)).  This is potentially the right
scale, but it is not yet a positive theorem: (O(W/m)) paths of length
(\Theta(m)) can still have linear physical boundary toll.

The exact surviving condition is an order-ideal cut problem.  One must find
a legal down-set in the exchange paths whose directed physical boundary is
(o(W/H)) and whose flag-load vector has the required energy.  No audited
property of the first-avoided construction currently supplies that
alignment.

## 2. Exact central interpolation theorem

Let \(\mathcal L\) be the lower side and \(\mathcal Y\) the middle side of a
bipartite multigraph.  Suppose (M,N) are matchings which saturate the same
set \(\mathcal L_0\subseteq\mathcal L\).  Delete their common token edges.
Every remaining lower vertex has degree two in (M\cup N), and every
middle vertex has degree at most two.  Hence every component of
(M\triangle N) is an even alternating cycle or an even alternating path
whose endpoints lie in \(\mathcal Y\).

### Theorem 2.1 (cycle rigidity and one-cut path theorem)

Let \(X\subseteq M\cup N\) saturate \(\mathcal L_0\) and be middle-simple.

1. On every alternating cycle (K), (X\cap K) is either (M\cap K) or
   (N\cap K).
2. Label an alternating path as
   \[
     y_0,x_1,y_1,x_2,\ldots,x_k,y_k
   \]
   so that
   \[
     M\cap K=\{y_{i-1}x_i:1\le i\le k\},\qquad
     N\cap K=\{x_i y_i:1\le i\le k\}.
   \]
   Then there is a unique (r\in\{0,1,\ldots,k\}) such that
   \[
     X\cap K=
     \{y_{i-1}x_i:i\le r\}
     \cup
     \{x_i y_i:i>r\}.
   \tag{2.1}
   \]

Conversely, independent choices of the two cycle orientations and of one
cut (r) on every path always give a lower-saturating, middle-simple
matching.

#### Proof

At (x_i), the child must choose exactly one of its two incident edges.
Write (u_i=1) for its (M)-edge and (u_i=0) for its (N)-edge.  At an
internal middle vertex (y_i), the choices (u_i=0,u_{i+1}=1) would select
both incident edges.  Thus

\[
 u_i\ge u_{i+1}.
\tag{2.2}
\]

On a path, (2.2) says that the binary word is (1^r0^{k-r}), proving
(2.1).  On a cycle the inequalities are cyclic and force all bits to be
equal.  The converse follows by direct inspection.  \(\square\)

This corrects the informal idea of switching several long pieces inside
one component.  An open component permits one monotone seam.  A closed
component permits none.

### Corollary 2.2 (few open components)

Put \(U_M=V(M)\cap\mathcal Y\) and \(U_N=V(N)\cap\mathcal Y\).  The number
of alternating paths is

\[
 p(M,N)=|U_M\setminus U_N|
       =|U_N\setminus U_M|
       ={1\over2}|U_M\triangle U_N|.
\tag{2.3}
\]

For the pair-omission central graph,

\[
 |U_M|=|U_N|=\binom{n}{m-1},\qquad |\mathcal Y|=W=\binom n m,
\]

and hence

\[
 \boxed{p(M,N)\le W-\binom n{m-1}={2W\over m+2}.}
\tag{2.4}
\]

Thus there are only (O(W/m)) components on which an internal legal cut
is possible.  Alternating cycles can still be arbitrarily numerous.

Indeed, every alternating path has one endpoint in
\(U_M\setminus U_N\) and one in \(U_N\setminus U_M\), proving (2.3).
Moreover \(|U_M\setminus U_N|\) is at most the number of middle vertices
missed by (N), which is (W-\binom n{m-1}), proving (2.4).

## 3. The exact predecessor-correlation functional

For every changed lower vertex (x), let (e_M(x)) and (e_N(x)) be its
two token edges and retain the bit convention

\[
 u_x=1\Longleftrightarrow e_M(x)\text{ is selected},\qquad
 u_x=0\Longleftrightarrow e_N(x)\text{ is selected}.
\tag{3.1}
\]

Whenever (e_N(x)) and (e_M(y)) meet the same internal middle vertex,
put an exchange arc (x\to y).  Theorem 2.1 says exactly that the legal
states are the binary solutions of

\[
 u_x\ge u_y\qquad(x\to y\text{ an exchange arc}).
\tag{3.2}
\]

Equivalently, (A=\{x:u_x=1\}) is a down-set on every directed exchange
path and is constant on every directed exchange cycle.

Now retain only adjacencies lying in the interiors of changed-token
intervals of physical source rows.  If an (M)-token of (x) immediately
precedes an (M)-token of (y), put an (M)-physical arc (x\to y).  If
the analogous adjacency holds for the (N)-tokens, put an (N)-physical
arc (x\to y).  Define

\[
 T(A)=
 |\{x\to y\in E_M^{\rm phys}:x\notin A, y\in A\}|
 +|\{x\to y\in E_N^{\rm phys}:x\in A, y\notin A\}|.
\tag{3.3}
\]

The first term is a (0\to1) run start in an (M)-row.  The second is a
(0\to1) run start for the selected bits (1-u) in an (N)-row.

### Proposition 3.1 (exact interior boundary toll)

For every legal child (X_A), each edge counted by (T(A)) is a distinct
physical selected-run start.  Thus

\[
 \boxed{J(X_A)\ge T(A).}
\tag{3.4}
\]

If the (M)- and (N)-changed tokens occupy disjoint physical row
families, then

\[
 J(X_A)\le T(A)+B_0,
\tag{3.5}
\]

where (B_0) is the number of starts outside the interiors of the changed
intervals.  In particular one may take

\[
 B_0=O\bigl(J(M)+J(N)+I_D\bigr),
\tag{3.6}
\]

with (I_D) the total number of changed intervals in the two endpoint row
systems.

The proof is the literal binary run-start identity on each row.  There are
no other interior starts; all remaining starts occur in an endpoint
matching or at an endpoint of a changed interval.

For cyclic rows,

\[
 {1\over |\mathcal L_0|}
 \sum_{e\in X_A}{\bf1}_{\{\operatorname{pred}(e)\in X_A\}}
 =1-{J(X_A)\over |\mathcal L_0|}.
\tag{3.7}
\]

Consequently predecessor correlation (1-o(1/H)) is **equivalent** to
(J(X_A)=o(W/H)), and (3.3) is the exact interior gate for a two-matching
long-block interpolation.

The zero-toll rigidity can also be read as an implication graph.  Exchange
arcs and (M)-physical arcs impose (u_x\ge u_y), while (N)-physical
arcs impose (u_x\le u_y).  If these implications form one strongly
connected class, the only zero-toll states are (A=\varnothing) and the
full (A).  More generally, every nontrivial child must pay the appropriate
directed cut.  This is the precise cyclic obstruction behind a failed
long-block coupling.

### Proposition 3.2 (exact correlated shadow-twin ledger)

Let \(U=(u_x)\) be any random legal state satisfying (3.2) almost surely,
and let

\[
 v_x=\mu(e_M(x))-\mu(e_N(x)),\qquad
 \overline\mu=\mu(N)+\sum_x\mathbb E[u_x]v_x.
\tag{3.8}
\]

Then the child is an exact central matching almost surely and

\[
 \mathbb E\|\mu(X_U)-\lambda\|_w^2
 =\|\overline\mu-\lambda\|_w^2
 +\sum_{x,y}\operatorname{Cov}(u_x,u_y)
   \langle v_x,v_y\rangle_w.
\tag{3.9}
\]

Its expected interior predecessor toll is exactly

\[
 \mathbb ET(U)=
 \sum_{x\to y\in E_M^{\rm phys}}\Pr(u_x=0,u_y=1)
 +\sum_{x\to y\in E_N^{\rm phys}}\Pr(u_x=1,u_y=0).
\tag{3.10}
\]

Thus a correlated LONG-BLOCK rounding is valid precisely when its law is
supported on the exchange down-sets, the directed disagreement sum in
(3.10) is (o(W/H)), and the covariance expression in (3.9), after the
integer floor is subtracted, is (o(W)).  These are identities, not
independence estimates.  In particular, correlating nearby physical tokens
is harmless only if the resulting equal-bit bundles remain compatible with
all exchange-path inequalities; a cyclic closure of those requirements can
collapse the law to the two endpoint states.

#### Proof

Equation (3.9) is the Hilbert-space mean-plus-variance identity applied to
\(\mu(X_U)=\mu(N)+\sum_xu_xv_x\).  Equation (3.10) is (3.3) averaged term by
term.  Exact central ownership follows from Theorem 2.1.  \(\square\)

## 4. An adjacent priority swap

Let the ordered disjoint omitted pairs contain consecutive pairs

\[
 A=P_j,\qquad B=P_{j+1}.
\]

Compare the first-avoided matching before and after swapping their
priorities, keeping the local carrier chosen for each omitted pair fixed.
A lower target changes carrier if and only if

\[
 S\cap P_h\ne\varnothing\quad(h<j),\qquad
 S\cap A=S\cap B=\varnothing.
\tag{4.1}
\]

Indeed, a set missing an earlier pair is decided earlier in both orders; a
set missing just one of (A,B) is assigned to that same pair in both
orders; and a set missing both is assigned to whichever of (A,B) comes
first.

Let (D_j) denote the set in (4.1).  Inclusion-exclusion gives

\[
 \boxed{
 |D_j|=\sum_{t=0}^{j-1}(-1)^t\binom{j-1}{t}
 \binom{2m-3-2t}{m-1}.}
\tag{4.2}
\]

In particular,

\[
 |D_1|=\binom{2m-3}{m-1}
 ={m(m+1)\over4(2m-1)(2m+1)}W
 =\left({1\over16}+O(m^{-1})\right)W.
\tag{4.3}
\]

Thus the first adjacent swap is large enough to alter a bulk flag profile.

Write (f,g:D_j\to\mathcal Y) for the middle-owner injections supplied by
the old and new carriers.  The number of open exchange paths is exactly

\[
 p_j=|f(D_j)\setminus g(D_j)|
    =|D_j|-|f(D_j)\cap g(D_j)|
    \le {2W\over m+2}.
\tag{4.4}
\]

The rest of the changed mass lies on alternating cycles.  Formula (4.4) is
the complete component-count information forced by central matching.  It
does not control the cycle count or any component length: the overlay can
have many parallel two-edge cycles, paths of length \(\Theta(m)\), or much
longer cycles.  None of these alternatives is excluded by the low-run
proof.

There is, however, a useful row-level interval bound before exchange labels
are imposed.  In a row of the old (A)-carrier, (4.1) says that the
length-((m-1)) window avoids (B) and meets the (j-1) earlier pairs.
For a fixed pair, its avoid-set has at most two circular components.  Hence
the changed starts have at most (2j) circular components in one row.  The
same bound holds in a row of the new (B)-carrier.  If

\[
 R_m={1\over2m-1}\binom{2m-1}{m-1}
 ={m+1\over2(2m+1)(2m-1)}W,
\tag{4.5}
\]

then

\[
 \boxed{I_D\le4jR_m=O(jW/m).}
\tag{4.6}
\]

For (j=1), the membership change therefore consists of only (O(W/m))
physical intervals even though it contains ((1/16+o(1))W) tokens.
Together with the first-avoided endpoint bound
(J(M)+J(N)=O(W\log ^2m/m)), this part of the ledger is
(o(W/H)) for (H=\sqrt m\,\omega) whenever
(\omega\log ^2m=o(\sqrt m)).

This does **not** bound (T(A)).  Exchange-component indices can oscillate
arbitrarily fast inside those long physical intervals.  Long membership
blocks and long legal exchange blocks are two different statements.

## 5. What telescopes, and what does not

Let \(\Delta_K\) be the flag-load difference between the (N)- and
(M)-sides of an exchange component (K).

1. At the outgoing lower rank (L_1=S),
   \[
     \Delta_K^{L_1}=0
   \tag{5.1}
   \]
   componentwise, because each side covers every lower vertex of (K)
   exactly once.
2. At the central middle rank, a cycle has
   \(\Delta_K^{Y}=0\).  A path telescopes exactly to its two endpoints:
   \[
     \Delta_K^{Y}=\mathbf e_{y_k}-\mathbf e_{y_0}
   \tag{5.2}
   \]
   with the orientation of Theorem 2.1.
3. No analogous identity follows for (L_q) with (q\ge2) or (U_q)
   with (q\ge1).  Equality of an internal middle owner pairs two central
   edges, but their row continuations, and hence their deeper flags, need
   not agree.  Explicitly, at an internal owner (Y) the contribution has
   the form
   \[
     \mathbf e_{F_N(Y)}-\mathbf e_{F_M(Y)},
   \tag{5.3}
   \]
   and there is no next-term cancellation unless an additional carrier
   coupling proves (F_N(Y)=F_M(Y)) or a genuine multiset telescope.

There is an exact phase-separation functional for the adjacent priority
swap.  At upper rank (r=m+q), define

\[
 \chi_{A,B}(T)=
 {\bf1}_{\{T\cap A\ne\varnothing\}}
 -{\bf1}_{\{T\cap B\ne\varnothing\}}.
\tag{5.4}
\]

Every old upper flag avoids (A), and every new upper flag avoids (B).
Therefore, for every component or correlated bundle \(\mathcal C\),

\[
 \boxed{
 \langle\chi_{A,B},\Delta_{\mathcal C}^{U_q}\rangle
 =E_{\mathcal C,q}^{N,A}+E_{\mathcal C,q}^{M,B}\ge0,}
\tag{5.5}
\]

where the two terms count new flags meeting (A) and old flags meeting
(B).  These exclusive-sector contributions cannot cancel between
components.

For this particular swap, (5.5) is only a collar-scale obstruction.  Since
the changed lower window (S) avoids both (A,B), the upper flag differs
from it in (q+1) row positions.  For either coordinate of the opposite
pair, exactly (q+1) cyclic starts can place it in this collar.  Hence

\[
 \sum_{\mathcal C}
 \bigl(E_{\mathcal C,q}^{N,A}+E_{\mathcal C,q}^{M,B}\bigr)
 \le4(q+1)R_m
 =O(Wq/m).
\tag{5.6}
\]

All deeper lower flags are subsets of (S), so the phase functional
vanishes there.  Thus pair residence gives a genuine noncancellation
invariant, but it does not by itself rule out the adjacent-swap route for
(q=o(m)).  The possible bulk discrepancy in the common core remains
completely uncontrolled rather than telescoping.

## 6. Sharp fragmentation example

The mismatch between exchange order and physical order is not a cosmetic
gap.  It can destroy predecessor correlation at full scale.

### Proposition 6.1 (one legal cut can have linear physical toll)

For every even (k=2h), there is an abstract two-matching token instance
whose symmetric difference is one alternating path of (k) lower
vertices, in which both endpoint matchings occupy one consecutive physical
row block, but the legal cut (r) of Theorem 2.1 satisfies

\[
 J(X_r)\ge2\min\{r,k-r\}-2.
\tag{6.1}
\]

#### Construction and proof

In each of the two endpoint row blocks, order the lower indices as

\[
 1,k,2,k-1,3,k-2,\ldots,h,h+1.
\tag{6.2}
\]

The (M)-row membership of the cut child is
({\bf1}_{\{i\le r\}}), and the (N)-row membership is its complement.
For (r\le h), the first (r) selected (M)-positions are isolated by
the first (r) unselected high positions, while the complementary
(N)-mask has the same number of alternating runs up to an endpoint.
This gives (2r-O(1)) starts.  The case (r\ge h) follows by complement
symmetry.  Both endpoint states (r=0,k) have only one selected block.
\(\square\)

Taking (O(W/m)) disjoint examples with (k=\Theta(m)) is compatible with
the path-count bound (2.4), yet any interpolation which cuts a positive
fraction of their mass away from both endpoints has \(\Theta(W)\) run
starts.

The example can also be given endpoint-symmetric energy.  Attach one flag
target (a) to every (M)-edge and a second target (b) to every
(N)-edge.  The two endpoints have equal quadratic energy under the target
swap (a\leftrightarrow b), while the balanced load occurs only near
(r=k/2), precisely where (6.1) is linear.  This is an abstract obstruction,
not a claim that these flag assignments are realized by a pair-omission
factor.  It proves that central matching, equal endpoint energy, and low
endpoint run count alone cannot imply the desired correlated rounding.

## 7. Necessary and sufficient remaining component gate

For two concrete first-avoided matchings, form the exchange digraph, the
two directed physical adjacency sets, and the literal flag vectors

\[
 v_x=\mu(e_M(x))-\mu(e_N(x)).
\]

Every exact child is parameterized by a legal down-set (A), and its load
is

\[
 \mu(X_A)=\mu(N)+\sum_{x\in A}v_x.
\tag{7.1}
\]

Therefore the desired two-matching interpolation exists if and only if
there is a down-set (A) such that

\[
 \boxed{
 T(A)=o(W/H),\qquad
 \Phi\!\left(\mu(N)+\sum_{x\in A}v_x\right)=o(W),}
\tag{7.2}
\]

with the harmless (B_0=o(W/H)) endpoint ledger included as in (3.5).

This formulation preserves the central matching exactly and measures
predecessor correlation exactly.  A sufficient structural theorem would
show that an adjacent priority swap has a low-directed-boundary down-set
which changes the needed bulk flag energy.  The current inputs prove the
large support (4.3), the few-path bound (4.4), and the raw long physical
interval bound (4.6), but they do not control the relative order needed to
deduce (7.2).

Accordingly, adjacent-priority long-block interpolation remains a viable
conditional route, not a completed contraction.  The exact missing lemma
is an exchange-order/physical-order alignment theorem; without it the
fragmentation example gives a sharp no-go to any purely component-count or
endpoint-run argument.

## 8. Reverse transport is an aligned nontrivial subclass

The generic interlacing obstruction disappears for one concrete coupling
of the two adjacent-pair carriers.  Keep

\[
 A=P_j,\qquad B=P_{j+1},\qquad
 \tau=(a_1\ b_1)(a_2\ b_2),
\]

choose \(F_B=\tau F_A\), and traverse every paired \(F_B\)-row in the
opposite cyclic orientation.  In a row
\(\pi=(x_0,\ldots,x_{2m-2})\) of \(F_A\), put

\[
 S_i=I_\pi(i,m-1),\qquad X_i=I_\pi(i,m).
\tag{8.1}
\]

The old predecessor token and the reverse-transport new token over a
changed target \(S_i\in\mathcal D_j\) are

\[
 e_A(S_i)=(S_i,X_{i-1}),\qquad
 e_B^{\rm rev}(S_i)=(S_i,\tau X_i).
\tag{8.2}
\]

This is genuinely different from the same-orientation transport, whose
new middle endpoint is \(\tau X_{i-1}\).

### Theorem 8.1 (exchange paths are exactly the physical intervals)

For the reverse transport (8.2), every alternating component on
\(\mathcal D_j\) is exactly one maximal consecutive
\(\mathcal D_j\)-interval in a row of \(F_A\).  It is an open path, not a
cycle.  If the interval is

\[
 I=\{a,a+1,\ldots,b\},
\]

its legal central children are precisely

\[
 \{e_A(S_i):a\le i\le r\}
 \cup
 \{e_B^{\rm rev}(S_i):r<i\le b\},
 \qquad a-1\le r\le b.
\tag{8.3}
\]

Thus every legal exchange threshold is one physical block in the
\(F_A\)-row and one physical block in its oppositely oriented
\(F_B\)-row.

#### Proof

If \(S_i,S_{i+1}\in\mathcal D_j\), then both avoid \(B\).  The coordinate
entering \(S_{i+1}\) therefore lies outside \(B\), so

\[
 \tau X_i=X_i
 \quad\hbox{and}\quad
 e_A(S_{i+1})=(S_{i+1},X_i).
\tag{8.4}
\]

Hence the new edge over \(S_i\) and the old edge over \(S_{i+1}\) meet.

Conversely, suppose a new changed edge over \(S_i\) and an old changed edge
over \(S_k\) meet:

\[
 \tau X_i=X_{k-1}.
\tag{8.5}
\]

The left side avoids \(B\), while the right side avoids \(A\).  Their
common value avoids both pairs and is fixed by \(\tau\).  Therefore
\(X_i=X_{k-1}\).  Since the length-\(m\) windows of \(F_A\) occur exactly
once, \(k=i+1\) in the same row.  Thus there are no cross-row or
nonconsecutive exchange links.

A full cyclic \(\mathcal D_j\)-interval is impossible: every row contains
the two coordinates of \(B\), and some length-\((m-1)\) windows contain
them, whereas every member of \(\mathcal D_j\) avoids \(B\).  Hence every
component is an open path.  Theorem 2.1 now gives (8.3).  Opposite
orientation reverses the order of the corresponding positions in the
\(F_B\)-row but preserves their consecutiveness.  \(\square\)

### Corollary 8.2 (two-boundary toll per path)

Let \(\mathcal I_j\) be the set of the maximal intervals above.  Every
simultaneous choice of the cuts in (8.3) is an exact central matching and

\[
 [J(X)-J(M_A)]_+\le2|\mathcal I_j|
 \le4jR_m=O(jW/m).
\tag{8.6}
\]

For \(H=\sqrt m\,\omega\), this is \(o(W/H)\) whenever
\(j\omega=o(\sqrt m)\).  Hence the reverse-transport class really does
preserve predecessor correlation \(1-o(1/H)\); the generic interlacing
example of Section 6 does not apply to it.

#### Proof

Relative to the all-\(A\) endpoint, one path cut removes one suffix interval
from an \(F_A\)-row and inserts the paired suffix interval into an
\(F_B\)-row.  Its source-position XOR therefore has at most two runs.
Apply the XOR boundary inequality and
\(|\mathcal I_j|\le2jR_m\).  \(\square\)

## 9. Exact telescoping flag profile of a reverse path

For a consecutive subinterval \(K\subseteq I\), let

\[
 E_{\pi,r}(K)=\sum_{i\in K}{\bf1}_{I_\pi(i,r)}.
\tag{9.1}
\]

Switching precisely \(K\) from its old predecessor tokens to its
reverse-transport tokens has the exact signed flag displacement

\[
 \boxed{
 \begin{aligned}
 z^-_{K,q}
 &=E_{\pi,m-q}(K)-E_{\pi,m-q}(K+q-1),\\
 z^+_{K,q}
 &=\tau E_{\pi,m+q}(K-q)-E_{\pi,m+q}(K-1).
 \end{aligned}}
\tag{9.2}
\]

The first line is the ordinary orientation coboundary.  In the second,
the shift is the orientation coboundary and \(\tau\) is the adjacent-pair
transport.

### Proposition 9.1 (collar bound)

Uniformly for \(1\le q\le m-2\),

\[
 \boxed{
 \|z^-_{K,q}\|_2^2\le2(q-1),\qquad
 \|z^+_{K,q}\|_2^2\le6q+2.}
\tag{9.3}
\]

Consequently

\[
 \|z_K\|_w^2
 \le8\sum_{q\le H}q\,w_q.
\tag{9.4}
\]

In particular the unweighted action of one arbitrarily long path block is
\(O(H^2)\), supported in its depth-\(q\) endpoint collars.

#### Proof

For proper cyclic windows, the map from a start to its window is injective.
The two equal-length start intervals in the first line of (9.2) differ by
a shift of \(q-1\), proving its bound.

For the upper line, insert and subtract
\(\tau E_{\pi,m+q}(K-1)\).  The shifted start intervals
\(K-q\) and \(K-1\) have symmetric difference at most \(2(q-1)\).
It remains to compare a window at a start in \(K-1\) with its
\(\tau\)-image.  Such a window already avoids \(A\), and it is fixed by
\(\tau\) unless it meets \(B\).  Since its associated lower window avoids
\(B\), the upper window can meet \(B\) only in its \(q+1\) added collar
positions.  Each of the two coordinates of \(B\) occurs in that collar for
at most \(q+1\) starts.  Thus at most \(2(q+1)\) starts are nonfixed, and
they contribute at most \(4(q+1)\) points to the target symmetric
difference.  Adding the two bounds gives \(6q+2\).  Equation (9.4) follows
from (9.3).  \(\square\)

The same estimate applies to every threshold child in (8.3), because its
changed suffix is itself a consecutive interval.  Thus reverse transport
simultaneously solves exact central legality, physical LONG-BLOCK
correlation, and length-independent shadow action.

## 10. Why the reverse class still does not prove contraction

The endpoint-collar estimate is only an action bound; it has no favourable
energy sign.  If \(e=\mu(M_A)-\lambda\), switching a block \(K\) changes
the raw quadratic energy by

\[
 \|\mu(M_A)+z_K-\lambda\|_w^2-\|e\|_w^2
 =2\langle e,z_K\rangle_w+\|z_K\|_w^2.
\tag{10.1}
\]

Nothing in interval alignment controls the linear term.  Nor is a fixed
cross-Gram sign implied by the present hypotheses.  Already the lower
depth-two parts are oriented endpoint differences

\[
 z^-_{K,2}={\bf1}_{I_\pi(a,m-2)}
           -{\bf1}_{I_\pi(b+1,m-2)},
\tag{10.2}
\]

whose cross inner products are signed endpoint-coincidence counts.  The
factor axioms neither exclude reversed endpoint coincidences nor turn those
counts into a nonnegative form.  The \(\tau\)-twisted upper strips have the
same unresolved sign.  This is exactly what the same-orientation pair
transport avoids with its nonnegative Gram identity; reversing the rows
gains central path alignment but loses that sign theorem.

There is one useful exception.  Rewrite the upper innovation as

\[
 z^+_{K,q}
 =(\tau-1)E_{\pi,m+q}(K-1)
  +\tau\!\left[
    E_{\pi,m+q}(K-q)-E_{\pi,m+q}(K-1)\right].
\tag{10.3}
\]

The first summand is the same-orientation pair-swap innovation and has the
nonnegative duplicate Gram.  The second is the signed orientation
coboundary.  At \(q=1\) the coboundary vanishes, as does \(z^-_{K,1}\).
Consequently the reverse atlas retains the exact favourable first-upper
identity

\[
 \left\|\sum_Iz_{I,1}\right\|_2^2-\sum_I\|z_{I,1}\|_2^2
 =2\sum_{U:\,U\cap B\ne\varnothing}\mu_1(U)(\mu_1(U)-1)
 \ge0.
\tag{10.4}
\]

The two coherent endpoints also have equal first-upper energy.  Indeed,
predecessor and successor orientation give the same \(U_1\), so the reverse
endpoint has exactly the same first-upper load as the same-orientation
pair-symmetric priority swap; that swap merely permutes the affected
target stratum by \(\tau\).  Hence independent fair whole-path coins have
the exact raw-square expectation

\[
 \mathbb E Q^{\rm raw}_1(X)
 =Q^{\rm raw}_1(M_A)
  -\frac12\sum_{U:\,U\cap B\ne\varnothing}
       \mu_1(U)(\mu_1(U)-1).
\tag{10.5}
\]

The same statement holds after subtracting the fixed integer floor.
Thus reverse transport supplies a genuine depth-one descent whenever the
displayed changed-occurrence collision sum is positive.  It does not see
collisions supported entirely on \(\tau\)-fixed targets or involving no two
changed occurrences.

The uncontrolled sign begins at depth two, where both the lower endpoint
strip and the upper orientation coboundary are present.  No current
estimate proves that the positive pair-swap part dominates those
simultaneous signed terms.

Quantitatively, summing (9.4) over the at most \(2jR_m\) paths gives only

\[
 \sum_{I\in\mathcal I_j}\|z_I\|_w^2
 =O\!\left(\frac{jW}{m}\sum_{q\le H}q\,w_q\right).
\tag{10.6}
\]

Unweighted, this is \(O(jWH^2/m)\), which becomes
\(O(jW\omega^2)\) for \(H=\sqrt m\,\omega\).  For the usual Gaussian
weights, the sum in (10.3) is of order at most \(m\), giving an
\(O(jW)\) bound but no little-oh saving.  Therefore the collar telescope
is exactly at the critical energy scale.

For binary whole-path coins \(z_I\), the gain of independent path rounding
below the coherent endpoint-pair average is

\[
 \frac14\left(
 \left\|\sum_Iz_I\right\|_w^2-\sum_I\|z_I\|_w^2
 \right)
 =\frac12\sum_{I<J}\langle z_I,z_J\rangle_w.
\tag{10.7}
\]

The right side need not be positive.  Allowing every monotone cut on a path
enlarges the integral class but does not supply a sign for (10.1).

Hence reverse transport is a genuine nontrivial factor class that removes
the exchange-order/physical-order obstruction.  Its exact remaining gate is
a signed endpoint-strip discrepancy theorem:

\[
 \boxed{\text{find path cuts with }\
 \Phi\!\left(\mu(M_A)+\sum_I z_{I,r_I}\right)=o(W).}
\tag{10.8}
\]

No such sign or discrepancy theorem follows from the \(O(H^2)\) collar
support alone.  The class is therefore strictly more promising than a
generic pair of first-avoided matchings, but it does not yet yield
constant one.
