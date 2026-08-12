# Direct upper rooted shores: exact rank, cut, Rado, and path-ear forms

Date: 2026-07-31  
Status: exact characterization for a fixed direct basis; exact one-coordinate
Rado theorem; solver-free parameter-three census; deterministic decomposition
of the frozen strict chain through child parameter five.  No all-parameter
existence theorem is claimed.

## 0. Result

Fix an oriented Catalan child path forest (F) at parameter (n), and fix
a size-(C) direct common basis (Q\subseteq E(F)).  On the upper shore, a
candidate occurrence (e=(q,x)), (x\notin U_q), has labels and physical
roles

\[
 d(e)=L_q+x,\qquad v(e)=U_q+x,\qquad
 \tau(e)=t_q+x,\qquad \eta(e)=h_q+x.                 \tag{0.1}
\]

The allowed lower-colour bank and the anchor bank are

\[
 \mathcal D_Q=\binom{\Omega}{n}\setminus T(Q),\qquad
 A_Q=\{U_q:q\in Q\}\subseteq\binom{\Omega}{n+1}.    \tag{0.2}
\]

This note gives four exact forms of the missing upper-shore condition.

1. A direct basis admits an upper no-empty side precisely when a finite
   double-rainbow selector satisfies explicit degree, graphic-cycle, and
   rooted-cut inequalities.
2. In graphic-matroid language, its (P) physical edges must be independent
   before contracting the root star and spanning after contracting it.
3. Equivalently, the side splits into an (R)-edge rooted kernel with one
   anchor in each of its (C) path components, followed by exactly
   (K=\operatorname{Cat}_n) endpoint-compatible ears pairing (2K) distinct
   kernel paths.  This is the exact anchored path-ear normal form suggested
   by the finite recursion.
4. If one forgets the second rainbow coordinate and the degree/anchor caps,
   ordinary Rado gives a complete pair of graphic-rank inequalities.  The
   second palette is a genuine additional constraint, so this relaxation is
   not the missing all-(n) theorem.

For the authenticated (n=3) child, all four strict direct common bases admit
an upper no-empty shore.  Thus there is no upper rooted obstruction at that
first recursive face.  The three frozen upper shores at child parameters
(3,4,5) decompose exactly into rooted kernels plus (5,14,42) Catalan ears.
However, a different direct common basis of the recursively supplied
\(n=4\) child has contracted upper candidate rank \(12<R=14\): two
nonanchor physical vertices are isolated even in the full allowed candidate
graph.  Hence direct common-basis incidence does not imply the rooted rank
equality.

## 1. Parameters and upper occurrences

Use

\[
\begin{aligned}
 M&=\binom{2n}{n},&N&=\binom{2n}{n-1},&P&=\binom{2n}{n-2},\\
 C&=M-P,&K&=M-N=\operatorname{Cat}_n,&R&=N-C,&H&=N-P.
\end{aligned}                                             \tag{1.1}
\]

The useful identities are

\[
             R=P-K,\qquad H=C-K.                         \tag{1.2}
\]

Let

\[
                       Y=\binom{\Omega}{n+1}.             \tag{1.3}
\]

Thus (|Y|=N).  Let \(\mathscr E_Q^-\) be the upper direct occurrences
whose lower label lies in \(\mathcal D_Q\).  Parallel occurrences are retained
as distinct elements, although their physical undirected edges may be
parallel in the graphic representation.

A selector (S\subseteq\mathscr E_Q^-) is **double-rainbow** when

\[
 d:S\longrightarrow\mathcal D_Q,\qquad
 v:S\longrightarrow\binom{\Omega}{n+2}                  \tag{1.4}
\]

are bijections.  In particular, (|S|=P).  It is **degree-safe** when, for
every (y\in Y),

\[
 |\{e\in S:y\in\{\tau(e),\eta(e)\}\}|\le2,              \tag{1.5}
\]

and every anchor has total selected side degree at most one:

\[
 |\{e\in S:y\in\{\tau(e),\eta(e)\}\}|\le1
                         \qquad(y\in A_Q).               \tag{1.6}
\]

Under (1.5), an acyclic physical support is a disjoint union of undirected
paths.  Each component may then be oriented consistently; the inherited
child orientation of an occurrence is not a constraint.  Condition (1.6)
puts every anchor at a path endpoint or as an isolated vertex.

## 2. Exact rank and cut characterization

Adjoin a new root \(\rho\) and the full root star

\[
                 E_\rho=\{\rho a:a\in A_Q\}.             \tag{2.1}
\]

Let \(\widehat{\mathsf M}_Q\) be the graphic matroid of the multigraph on
\(Y\cup\{\rho\}\) whose non-root elements are the physical edges of
\(\mathscr E_Q^-\).  Then

\[
 r_{\widehat{\mathsf M}_Q}(E_\rho)=C,qquad
 r(\widehat{\mathsf M}_Q/E_\rho)\le N-C=R.              \tag{2.2}
\]

### Theorem 2.1 (fixed-basis upper rooted criterion)

The direct basis (Q) admits an upper no-anchor-free side forest if and only
if there is a double-rainbow, degree-safe selector (S\subseteq\mathscr E_Q^-)
such that

\[
 r_{\widehat{\mathsf M}_Q}(S)=P,qquad
 r_{\widehat{\mathsf M}_Q/E_\rho}(S)=R.                 \tag{2.3}
\]

The first equality says that the physical side is a forest.  The second says
that after all anchors are identified with the root, the selected support is
spanning.  Equivalently, every component before contraction contains an
anchor.

#### Proof

Since (|S|=P), the first equality is exactly acyclicity.  The contraction
rank identity gives

\[
 r_{\widehat{\mathsf M}_Q/E_\rho}(S)
 =r_{\widehat{\mathsf M}_Q}(S\cup E_\rho)-C.             \tag{2.4}
\]

Its value is (R=N-C) exactly when (S\cup E_\rho) has rank (N), or
equivalently is connected on (Y\cup\{\rho\}).  This happens exactly when
every component of (S) meets (A_Q).  Together with degree safety, this is
precisely an anchor-capped no-empty linear side forest.  Its components can
be oriented existentially after selection. \(\square\)

The contraction nullity is forced:

\[
 |S|-r_{\widehat{\mathsf M}_Q/E_\rho}(S)=P-R=K.          \tag{2.5}
\]

This is the graphic form of the Catalan side charge.

### Corollary 2.2 (exact binary cut system)

Write (x_e\in\{0,1\}) for (e\in\mathscr E_Q^-), and let
(E_S(Z)) and \(\delta_S(Z)\) denote selected physical edges internal to and
leaving (Z\subseteq Y).  The desired upper side exists exactly when the
following system is feasible:

\[
\begin{aligned}
 \sum_{e:v(e)=V}x_e&=1
       &&\left(V\in\binom{\Omega}{n+2}\right),\\
 \sum_{e:d(e)=D}x_e&=1 &&(D\in\mathcal D_Q),            \tag{2.6}\\
 \sum_{e:y\in\{\tau(e),\eta(e)\}}x_e&\le2 &&(y\in Y),\\
 \sum_{e:y\in\{\tau(e),\eta(e)\}}x_e&\le1 &&(y\in A_Q),\tag{2.7}\\
 |E_S(Z)|&\le |Z|-1 &&(\varnothing\ne Z\subseteq Y),   \tag{2.8}\\
 |\delta_S(Z)|&\ge1
       &&(\varnothing\ne Z\subseteq Y\setminus A_Q).  \tag{2.9}
\end{aligned}
\]

Indeed, (2.8) is the graphic independence system and (2.9) says that no
component is disjoint from the anchor bank.  This is an exact integer
characterization, not an assertion that its linear relaxation is integral.

## 3. Anchored Catalan path-ear normal form

### Theorem 3.1 (rooted kernel plus (K) ears)

The selector in Theorem 2.1 exists if and only if there are disjoint sets

\[
                 F_0,E\subseteq\mathscr E_Q^-,qquad
                 |F_0|=R,\qquad |E|=K,                \tag{3.1}
\]

with the following properties.

1. (F_0\cup E) is double-rainbow and degree-safe.
2. The physical support of (F_0) consists of exactly (C) undirected paths,
   each containing exactly one anchor.  Equivalently, (F_0) is an
   uncontracted forest and a basis of
   \(\widehat{\mathsf M}_Q/E_\rho\).
3. Every (e\in E) joins free endpoints of two distinct (F_0)-paths.
4. On the (C) rooted (F_0)-paths, the (K) ears form a matching: no
   rooted path is incident with two ears.

Consequently (F_0\cup E) has (H=C-K) components, exactly (K) of which
contain two anchors.  The other (C-2K) components contain one anchor.

#### Proof

Let (S) satisfy Theorem 2.1.  It has (H=N-P) path components.  By the
anchor cap, every component contains at most two anchors.  If (c_j) is the
number containing (j) anchors, then no-emptiness gives (c_0=0), while

\[
 c_1+c_2=H,qquad c_1+2c_2=C.
\]

Hence

\[
                  c_2=C-H=K,qquad c_1=C-2K.            \tag{3.2}
\]

Delete one selected arc from each of the (K) double-anchor paths.  The
remaining set (F_0) has (P-K=R) edges and (C) path components, each
with exactly one anchor.  Each deleted arc reconnects the two pieces of one
former path, so the deleted edges have compatible free endpoint slots
and form a matching on the (C) rooted components.  This proves necessity.

Conversely, append the (K) endpoint-compatible matching ears to (F_0).
Each ear concatenates two distinct paths, no rooted path is used
twice, and no cycle or degree excess is created.  The result has (C-K=H)
anchored path components and the two exact palettes. \(\square\)

This is a literal noncanonical path-ear formulation.  The recursive problem
is no longer to realize an arbitrary pairing of anchors.  It is to select a
double-rainbow rooted kernel and then select the residual (K) palette pairs
as compatible ears on distinct kernel paths.

## 4. What ordinary Rado proves

There is a clean exact theorem after forgetting the lower label (d(e)) and
the degree/anchor constraints.  For each upper outer colour (V), let

\[
                  \mathscr E(V)=\{e\in\mathscr E_Q^-:v(e)=V\}. \tag{4.1}
\]

Take the (P) families \(\mathscr E(V)\) and (H) identical copies of the
root-star family (E_\rho).  Rado's theorem in
\(\widehat{\mathsf M}_Q\) gives the following.

### Proposition 4.1 (exact one-coordinate rooted Rado criterion)

There is a spanning tree consisting of one occurrence of every upper outer
colour and (H) distinct root-star edges if and only if, for every
\(\mathcal U\subseteq\binom{\Omega}{n+2}\),

\[
\begin{aligned}
 r_{\widehat{\mathsf M}_Q}\!\left(\bigcup_{V\in\mathcal U}\mathscr E(V)\right)
     &\ge |\mathcal U|,\\
 r_{\widehat{\mathsf M}_Q/E_\rho}\!\left(
          \bigcup_{V\in\mathcal U}\mathscr E(V)\right)
     &\ge |\mathcal U|-K.                              \tag{4.2}
\end{aligned}
\]

#### Proof

Rado requires the graphic rank of the union of every subfamily to be at
least the number of chosen family indices.  A subfamily containing no root
copy gives the first inequality.  Once it contains root copies, their union
is always the same set (E_\rho), so the strongest condition uses all (H)
copies:

\[
 r\!\left(\bigcup_{V\in\mathcal U}\mathscr E(V)\cup E_\rho\right)
     \ge |\mathcal U|+H.                               \tag{4.3}
\]

Use (r(E_\rho)=C), contraction, and (H=C-K) to obtain the second line of
(4.2).  There are (P+H=N) selected edges on (N+1) vertices, so a graphic
independent transversal is a spanning tree. \(\square\)

Proposition 4.1 is useful but does not enforce injectivity of the lower
labels (d(e)), the degree-two row, or the anchor cap.  Applying it
separately to the two palette coordinates also does not synchronize the
representatives.  The full problem is the simultaneous face consisting of
two partition bases, degree/anchor caps, graphic independence, and
contracted-graphic spanning.  No ordinary two-matroid intersection theorem
is asserted for that face.

## 5. Exact finite audit

### 5.1 All strict (n=3) direct common bases

The authenticated parameter-three child has four strict direct common bases,
recorded by the unique retained child edge (0,1,5,11).  Exhausting every
upper perfect occurrence matching gives

\[
\begin{array}{c|rrrr}
\text{retained child edge}&0&1&5&11\\ \hline
\text{perfect occurrence matchings}&8&16&8&8\\
\text{anchor-capped, no-empty linear forests}&4&16&8&8.
\end{array}                                             \tag{5.1}
\]

All forty palette matchings already satisfy the degree-two row and the two
graphic conditions: they are forests and every component contains an
anchor.  The rejected four matchings fail only the anchor-degree row.  Every
accepted shore has

\[
                    (c_0,c_1,c_2)=(0,4,5),             \tag{5.2}
\]

and has (2^5=32) choices of the root-star completion.  Thus no upper
rooted obstruction occurs among the four direct common bases at (n=3).

The solver-free exhaustive audit is

```text
scratch/audit_catalan_direct_upper_rooted_n3_20260731.py
scratch/catalan_direct_upper_rooted_n3_20260731.audit.json
```

### 5.2 The frozen strict chain

For each frozen upper no-empty shore, delete one deterministic edge from
every double-anchor path.  Literal replay gives

\[
\begin{array}{c|rrrrrr|rr}
n&M&N&P&C&K&R&|F_0|&|E|\\ \hline
3&20&15&6&14&5&1&1&5\\
4&70&56&28&42&14&14&14&14\\
5&252&210&120&132&42&78&78&42.
\end{array}                                             \tag{5.3}
\]

In every row, the kernel has exactly (C) components with one anchor each,
its anchor contraction is a spanning tree, and the deleted Catalan ears form
a matching on (2K) distinct kernel components with free endpoint slots.
Both palette coordinates split injectively as (R+K=P).  The saved upper
shore witnesses also happen to respect the inherited child orientation
inside that isolated shore.  This does not imply that the complete collar
preserves inherited arrows; the ambient chained construction is certified
only as an undirected direct-edge support.

The replay is

```text
scratch/audit_catalan_direct_upper_path_ear_chain_20260731.py
scratch/catalan_direct_upper_path_ear_chain_20260731.audit.json
```

This is exact finite evidence for the rooted path-ear state.  It does not
show that the state propagates at the next parameter.

### 5.3 First rooted obstruction on the frozen recursive chain

For the recursively supplied $n=4$ child, take the direct common basis
whose retained child-edge set is

\[
 Z=\{0,14,17,19,23,26,27,36,39,49,50,51,52,53\},
 \qquad Q=E(F)\setminus Z.                              \tag{5.4}
\]

Explicit upper and lower matchings certify both direct incidence rows for
this $Q$.  Nevertheless, after imposing the upper puncture
$\mathcal D_Q$, the full allowed upper bank has only 75 occurrences and
its physical candidate graph has two anchor-free singleton components:

\[
                         \{31\},\qquad\{211\}.           \tag{5.5}
\]

Thus each singleton violates the rooted cut (2.9) with left side zero.
After contracting all $C=42$ anchors, the candidate graph has 15 vertices,
three components, and rank

\[
                           15-3=12<R=14.                \tag{5.6}
\]

No choice of representatives can produce an upper no-empty shore for this
direct common basis.  Together with the complete $n=3$ census, this is the
first rooted obstruction on the audited recursive faces; no claim is made
over all possible parameter-three child forests.

The search witness and independent replay are

```text
scratch/search_catalan_direct_n4_upper_root_obstruction_20260731.py
scratch/catalan_direct_n4_common_basis_upper_root_obstruction_20260731.witness.json
scratch/audit_catalan_direct_n4_common_basis_upper_root_obstruction_20260731.py
scratch/catalan_direct_n4_common_basis_upper_root_obstruction_20260731.audit.json
```

## 6. Remaining all-(n) gate

For a recursively supplied child (F_n), one must choose (Q), a rooted
kernel (F_0), and (K) residual ears jointly so that

* both palette coordinates are exact;
* the kernel is a contracted-graphic basis and an uncontracted linear
  forest;
* the residual palette pairs have endpoint-compatible representatives on
  (2K) distinct rooted kernel paths; and
* after adjoining the central partial matching \(P_0\) and the induced upper
  matching \(P_L\), the lower induced matching \(P_R\) creates no alternating
  cycle in \(P_0\cup P_L\cup P_R\).

The present note closes the upper topology equivalence and the
one-coordinate Rado relaxation.  It proves neither the joint double-rainbow
selection nor its recursive propagation.
