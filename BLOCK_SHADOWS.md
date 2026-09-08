# Completing lower shadows inside saturating-cycle blocks

This note analyzes the block construction of `GLOBAL_RECURSION.md` exactly.
It gives:

1. an exact path-decomposition formulation of the missing lower-shadow
   condition;
2. a local linear-forest extension theorem;
3. a global necessary-and-sufficient certificate;
4. a useful two-block absorber; and
5. rigorous local and global obstructions showing why arbitrary assignment of
   the Catalan-many unused middle sets is not enough.

It does not prove that the required certificate exists for every `m`.

Throughout, put

\[
 W=\binom{2m}{m},\qquad
 K=\operatorname{Cat}_m,\qquad
 N=\binom{2m}{m+1}=W-K.
\]

Start with a saturating alternating cycle

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0, \tag{0.1}
\]

where all `U_i` are the `(m+1)`-sets, the `C_i` are distinct `m`-sets, and

\[
 C_i\subset U_i\supset C_{i+1}. \tag{0.2}
\]

Let

\[
 \mathcal C=\{C_0,\ldots,C_{N-1}\},\qquad
 \mathcal X=\binom{[2m]}m\setminus\mathcal C. \tag{0.3}
\]

Thus `|mathcal X|=K`.  The members of `mathcal X` are the unused middle sets
that Theorem 1 of `GLOBAL_RECURSION.md` inserts into the upper-colour blocks.

## 1. Exact deletion-label model

For a fixed upper set `U`, every middle set `X subset U` has a unique
**deletion label**

\[
 \delta_U(X)=U\setminus X\in U. \tag{1.1}
\]

The `m+1` middle subsets of `U` form a clique in `J(2m,m)`.  In deletion
labels, this is simply the complete graph on vertex set `U`.

If `X,Y subset U` are distinct middle sets, then

\[
 X\cap Y=U\setminus
 \{\delta_U(X),\delta_U(Y)\}. \tag{1.2}
\]

Thus an edge between deletion labels `a,b` has lower colour

\[
 U\setminus\{a,b\}. \tag{1.3}
\]

For block `U_i`, define its two terminal middle sets and terminal deletion
labels by

\[
 p_i=C_i,\quad q_i=C_{i+1},\qquad
 a_i=\delta_{U_i}(p_i),\quad b_i=\delta_{U_i}(q_i). \tag{1.4}
\]

The two terminals are distinct, so `a_i ne b_i`.

An assignment of the unused middle sets is a map

\[
 \alpha:\mathcal X\longrightarrow\{0,\ldots,N-1\}
 \quad\hbox{such that}\quad X\subset U_{\alpha(X)}. \tag{1.5}
\]

For each block put

\[
 I_i=\alpha^{-1}(i),\qquad
 V_i=\{p_i,q_i\}\cup I_i,
\]

and let

\[
 A_i=\delta_{U_i}(V_i)\subseteq U_i \tag{1.6}
\]

be its deletion-label set.  Ordering the assigned middle sets inside block
`i` is exactly the same thing as choosing a Hamilton path in the complete
graph on `A_i` from `a_i` to `b_i`.

### Proposition 1 (exact block equivalence)

Legal assignments `alpha` together with terminal Hamilton paths

\[
 Q_i:a_i\leadsto b_i\quad\hbox{in }K_{A_i} \tag{1.7}
\]

are in bijection with Hamilton middle-layer cycles whose edges of each upper
union colour `U_i` form one contiguous nonempty block and whose compressed
upper-colour cycle is (0.1).

Under this bijection the lower intersection colours in block `i` are exactly
the complements in `U_i` of the edges of `Q_i`, as in (1.3).

#### Proof

Replace every deletion label along `Q_i` by its middle set `U_i setminus
{label}`.  This gives a path from `C_i` to `C_(i+1)` through precisely the
middle sets assigned to `U_i`.  All its edges have union `U_i`.  Consecutive
block paths share exactly their common seam vertex `C_(i+1)`.  Since the seam
sets and assigned sets partition the middle layer, cyclic concatenation gives
a Hamilton cycle.

Conversely, cut any such Hamilton cycle at every change of upper colour.  Its
`U_i` block has endpoints `C_i,C_(i+1)` and all internal vertices are unused
middle subsets of `U_i`; these give (1.5), and deletion labels give (1.7).
Equation (1.2) proves the colour statement.  QED.

So upper-union completeness is automatic.  The entire question is whether
the paths `Q_i` can be chosen so that their edge labels (1.3) cover the full
rank-`m-1` layer.

## 2. The local path-extension theorem

Fix a block `U`, a deletion-label set `A subseteq U`, and distinct terminal
labels `a,b in A`.  Suppose a family of desired lower colours has already
been assigned to this block.  Each desired colour `S subset U`, `|S|=m-1`,
requires the unique deletion-label edge

\[
 e_U(S)=U\setminus S\in\binom A2. \tag{2.1}
\]

Let `H` be the graph on `A` formed by all these required edges.

### Theorem 2 (terminal clique-path extension)

There is a Hamilton `a`--`b` path of the complete graph `K_A` containing all
edges of `H` if and only if:

1. `H` is a linear forest: it is acyclic and has maximum degree at most two;
2. `deg_H(a)<=1` and `deg_H(b)<=1`; and
3. if `a` and `b` lie in the same nontrivial component of `H`, then that
   component contains every vertex of `A`.

#### Proof

Necessity follows because every subgraph of a Hamilton path is a linear
forest, the two prescribed endpoints have path degree one, and an `a`--`b`
path component cannot be joined to any additional vertex without increasing
the degree of `a` or `b`.

For sufficiency, orient every nontrivial component of `H` as a path.  Orient
the component containing `a`, if any, to start at `a`, and the component
containing `b`, if any, to end at `b`.  If these are the same component,
condition 3 says it already spans `A`, and it is the required Hamilton path.
Otherwise, order all path components and isolated vertices with the
`a`-component first and the `b`-component last.  Because the ambient graph is
complete, join the end of each oriented component to the start of the next.
The result is a Hamilton `a`--`b` path containing `H`.  QED.

### Corollary 3 (one designated colour)

Let `D_U(S)` be the two middle endpoints of the Boolean diamond `[S,U]`:

\[
 D_U(S)=\{S\cup\{x\}:x\in U\setminus S\}. \tag{2.2}
\]

A terminal block path through middle vertex set `V` can be chosen to contain
lower colour `S` if and only if

\[
 D_U(S)\subseteq V \tag{2.3}
\]

and either `D_U(S)` is not the pair of terminal vertices, or `V` consists of
the two terminals only.

This is Theorem 2 for one required edge.  It records an easy but important
fact: once a block receives an internal vertex, its old terminal edge can no
longer remain in the terminal-to-terminal Hamilton path.

## 3. Exact global lower-shadow certificate

Let

\[
 \mathcal S=\binom{[2m]}{m-1}
\]

be the lower colour layer, also of size `N`.

### Theorem 4 (exact representative-path formulation)

The saturating-cycle blocks can be assigned and ordered so that every lower
colour occurs if and only if there exist:

1. a legal partition

   \[
   \mathcal X=\mathop{\dot\bigcup}_{i=0}^{N-1} I_i,
   \qquad X\in I_i\Longrightarrow X\subset U_i; \tag{3.1}
   \]

2. a representative map

   \[
   \rho:\mathcal S\longrightarrow\{0,\ldots,N-1\},
   \qquad S\subset U_{\rho(S)}; \tag{3.2}
   \]

such that, for every `i`, all diamond endpoints `D_(U_i)(S)` with
`rho(S)=i` lie in

\[
 V_i=\{C_i,C_{i+1}\}\cup I_i, \tag{3.3}
\]

and the required deletion-edge graph

\[
 H_i=\{e_{U_i}(S):\rho(S)=i\} \tag{3.4}
\]

satisfies the three conditions of Theorem 2 with terminals `a_i,b_i`.

#### Proof

Suppose first that the desired block paths exist.  Assign each unused middle
vertex to its unique block.  For every lower colour choose one occurrence on
the Hamilton cycle and let `rho(S)` be its block.  The chosen edges in one
block form a subgraph of its terminal Hamilton path, so Theorem 2 gives all
the stated conditions.

Conversely, apply Theorem 2 independently in every block to extend `H_i` to a
terminal Hamilton path on `V_i`.  Proposition 1 concatenates these paths into
a Hamilton middle-layer cycle with complete upper colours.  Every lower
colour `S` occurs on its representative edge in block `rho(S)`.  QED.

This is a necessary-and-sufficient reformulation, not an existence proof.
Its advantage is that the global problem is now cleanly divided into:

* assigning each unused middle vertex to one containing upper block;
* assigning every lower colour to one containing upper block; and
* enforcing only a linear-forest constraint inside each clique.

### Exact slack ledger

The block paths have altogether

\[
 \sum_i(|V_i|-1)=N+K=W \tag{3.5}
\]

edges.  The representative graphs `H_i` have exactly `N` edges in total, one
for each lower colour.  Therefore every completion supplied by Theorem 2 adds
exactly

\[
 W-N=K \tag{3.6}
\]

connector edges not used as the chosen representatives.  These are precisely
the Catalan-many unavoidable repeated lower-colour occurrences.  There is no
larger hidden absorber budget.

## 4. A one-private-colour absorber criterion

A useful sufficient specialization assigns one distinct lower colour to each
upper block.

For block `i`, its baseline terminal colour is

\[
 s_i=C_i\cap C_{i+1}. \tag{4.1}
\]

Let

\[
 \mu:\{U_0,\ldots,U_{N-1}\}\longrightarrow\mathcal S
\]

be a bijection with `mu(U) subset U`.  Define its internal demand by

\[
 D_i(\mu)=D_{U_i}(\mu(U_i))
       \setminus\{C_i,C_{i+1}\}. \tag{4.2}
\]

Thus `|D_i(mu)|` is zero, one, or two.

### Theorem 5 (private-colour absorber)

The bijection `mu` extends to a complete block construction if:

1. every demanded middle set in (4.2) belongs to `mathcal X`;
2. the demand sets `D_i(mu)` are pairwise disjoint;
3. if `mu(U_i)=s_i`, then no unused middle set is assigned to block `i`;
4. every unused middle set not already demanded is contained in at least one
   **open** block `U_i` with `mu(U_i) ne s_i`.

#### Proof

Assign every demand to its indicated block.  Conditions 1 and 2 make this a
legal partial assignment.  Assign each remaining unused set to any open block
containing it, using condition 4; there is no capacity restriction.  Closed
blocks are left empty by condition 3.

In a closed block the desired colour is its sole terminal edge.  In an open
block, the desired edge has both endpoints available and is not the edge
between the two terminals.  Corollary 3 extends it to a terminal Hamilton
path through all filler vertices.  Since `mu` is a bijection, these paths
cover every lower colour.  QED.

This turns the private-colour version into a perfect matching with disjoint
one- or two-vertex demands, followed by an unrestricted filler assignment.
The disjoint-demand condition is the Hall-type obstruction that a bare
matching between the two colour layers misses.

### Open-block form

Choose a set `O` of blocks to open.  Keep `mu(U_i)=s_i` outside `O`.  A direct
application of Theorem 5 shows that it is enough that:

* the closed colours `{s_i:i notin O}` are distinct;
* the missing lower colours can be bijectively assigned to the blocks in `O`
  with disjoint legal demands; and
* the open upper sets cover every remaining unused middle set.

This is the precise absorber problem hidden in the arbitrary-order statement
of Theorem 1 in `GLOBAL_RECURSION.md`.

## 5. A two-block adjacent transposition absorber

The saturating cycle supplies a canonical local switch.

Consider adjacent blocks `U_i,U_(i+1)`, which share seam

\[
 C=C_{i+1}.
\]

Let

\[
 x_i=U_i\setminus C,\qquad
 y_i=U_{i+1}\setminus C \tag{5.1}
\]

be their respective outside elements.  Define middle sets

\[
 X_i=s_{i+1}\cup\{x_i\},\qquad
 Y_i=s_i\cup\{y_i\}. \tag{5.2}
\]

### Lemma 6 (adjacent swap absorber)

Suppose `s_i ne s_(i+1)` and the two sets `X_i,Y_i` in (5.2) are distinct
members of `mathcal X`.  Assign `X_i` to block `U_i` and `Y_i` to block
`U_(i+1)`.  Then the two block paths can be ordered so that:

* block `U_i` represents lower colour `s_(i+1)`;
* block `U_(i+1)` represents lower colour `s_i`;
* arbitrary additional filler vertices may be inserted into either block.

Thus the two baseline colours are transposed while two unused middle vertices
are absorbed.

#### Proof

Since `s_(i+1) subset C subset U_i`, the Boolean diamond for
`[s_(i+1),U_i]` has middle endpoints exactly `C` and `X_i`.  Hence its desired
edge is incident with the terminal `C`.  Order block `U_i` from `C_i` through
all filler vertices, then `X_i`, then `C`.

Similarly, the diamond `[s_i,U_(i+1)]` has middle endpoints `C` and `Y_i`.
Order the second block from `C` through `Y_i` and all remaining fillers to
`C_(i+2)`.  The two desired edges occur, and the union colour of every edge
inside its block remains unchanged.  QED.

### Corollary 7 (a proved general case)

Assume the baseline colours `s_0,...,s_(N-1)` are all distinct.  Suppose there
is a set of pairwise vertex-disjoint adjacent block pairs satisfying Lemma 6,
all their demanded sets are distinct, and every unused middle set not used by
the absorbers is contained in at least one opened block.  Then the block
construction can be ordered to cover every lower colour.

#### Proof

Swap the two private baseline colours on every selected adjacent pair and
leave every closed block with its own baseline colour.  This is still a
bijection from blocks to the lower layer.  Lemma 6 supplies the disjoint
demands, and all remaining unused vertices are legal filler in open blocks.
Apply Theorem 5.  QED.

The hypotheses are substantial; in particular, the saturating-cycle theorem
does not assert that the required `X_i,Y_i` are unused seam-complement sets.
The value of the lemma is that it identifies a concrete constant-size
absorber rather than merely requesting a favorable arbitrary ordering.

## 6. Rigorous obstructions

### 6.1 Local inaccessibility

For a lower colour `S` and an upper set `U superset S`, the only Johnson edge
with intersection `S` and union `U` has endpoints `D_U(S)` from (2.2).

Call `(S,U)` **accessible** if every endpoint in `D_U(S)` is either:

* one of the two terminals of block `U`; or
* a member of `mathcal X`, hence available for assignment to `U`.

### Proposition 8 (blocked-colour obstruction)

If some lower colour `S` has no accessible upper set `U`, then no assignment
or ordering inside the saturating-cycle blocks can cover `S`.

#### Proof

Any occurrence of `S` must be the unique diamond edge `D_U(S)` in some block
`U`.  A seam middle set that is not a terminal of that block has already been
used as a seam vertex elsewhere in the Hamilton cycle and cannot also be an
internal vertex of `U`.  Thus both diamond endpoints must satisfy the
accessibility condition.  QED.

This obstruction depends only on the seam set of the saturating cycle.  The
saturating-cycle theorem itself gives no assertion that rules it out.

### 6.2 Forced duplicate budget

If a block `U_i` contains no unused middle set at all, then it has only its two
terminals and is forced to contribute the colour `s_i`.

### Proposition 9 (forced-repeat obstruction)

Let `F` be the set of blocks containing no member of `mathcal X`.  A necessary
condition for full lower coverage is

\[
 |F|-|\{s_i:i\in F\}|\le K. \tag{6.1}
\]

#### Proof

The left side counts repeated occurrences already forced among these blocks.
Every completed Hamilton middle cycle has `W=N+K` edges and must cover `N`
lower colours.  It can therefore contain only `K` occurrences beyond the
first occurrence of each colour.  QED.

### 6.3 Hall is not enough

Even if every lower colour is accessible and the bipartite graph of accessible
pairs `(S,U)` has a perfect matching, the corresponding diamond endpoints may
demand the same unused middle set in two different blocks.  Since an unused
middle vertex can be internal to only one block, those two choices are
incompatible.  The disjoint-demand condition in Theorem 5 and the
linear-forest conditions in Theorem 4 are therefore genuine additional gates,
not technical artifacts.

## 7. Resulting research target

The exact all-`m` question is now the following terminal path-decomposition
problem.

> Given a saturating cycle (0.1), orient every unused middle set toward one
> containing upper block and assign every lower colour to one containing upper
> block so that the required deletion edges in each block form a
> terminal-compatible linear forest.

Equivalently, one must find the data in Theorem 4.  The upper union layer then
stays complete automatically, and no further central-row search is required.

There are exactly `K` nonrepresentative connector edges available globally.
Thus a plausible proof should use a system of disjoint constant-size absorbers
such as Lemma 6, plus a matching theorem for the residual colour demands.  A
proof based only on independent arbitrary assignments cannot work: it sees
neither local inaccessibility nor collisions between diamond endpoint demands.

The strongest honest conclusion is therefore:

\[
\boxed{
\text{saturating cycle}
+\text{ terminal linear-forest assignment}
\Longrightarrow
\text{complete two-sided first shadows}.}
\]

The first term is a theorem.  Existence of the second term for every `m`
remains open.

