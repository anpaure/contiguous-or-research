# Audit of the odd-diamond one-to-two augmenter and its exact resolution gate

Date: 2026-08-01  
Lane: K / protected owner-slot synchronization  
Status: local augmenter independently verified; exact simultaneous cut
criterion and a sufficient class-one factorization proved.  General
class-one resolvability and global augmenter expansion remain open.

## 0. Verdict

The local theorem in
`MATH_THEOREM_ODD_DIAMOND_TIGHT_ONE_TO_TWO_AUGMENTER_20260801.md`
is correct for `m>=3`.

There is one terminology clarification.  Replacing one selected auxiliary
edge by the target edge and its rerouted auxiliary copy introduces

\[
                         R,\quad L',\quad B^p,\quad D^q.            \tag{0.1}
\]

Thus there are four new hypergraph vertices in total.  The target upper
vertex `R` is the newly discharged demand; the other **three** vertices are
the new capacity resources.  This is the sense in which the augmenter is
tight.

The exact local supply count is

\[
                   16(m+1)m(m-2)(m-1)                             \tag{0.2}
\]

per target upper colour, with no overcount.  The single-gadget physical
forest guard is also correct.  Individually safe gadgets do not compose
automatically: several gadgets can jointly close a long physical cycle.
Theorem 4.1 below gives the exact missing simultaneous graphic row.

A proper maximum-degree colouring of the complete owner-slot hypergraph
would be stronger than needed.  It is class one for `m=2,3`; no general
proof or counterexample is presently known.  The verified augmenter gives
a weaker exact route: start from one protected near-perfect matching and
solve one colourful four-resource matching together with the graphic cuts.

## 1. Model and exact class-one meaning

Let

\[
 \Omega=[2m-1],\quad
 \mathcal L={\Omega\choose m-1},\quad
 \mathcal M={\Omega\choose m},\quad
 \mathcal U={\Omega\choose m+1}.                                  \tag{1.1}
\]

Clone every \(T\in\mathcal M\) into slots \(T^0,T^1\).  A diamond
\(L\subset R\), with middle corners \(T,H\), supplies the four hyperedges

\[
                         \{R,L,T^i,H^j\},\qquad i,j\in\{0,1\}.     \tag{1.2}
\]

The host is four-uniform, but it is not literally four-partite: the two
owner slots belong to one vertex class.  Its degrees are

\[
\begin{aligned}
 d(R)&=2m(m+1)=:\Delta,\\
 d(L)&=d(T^i)=2m(m-1)=\Delta-4m.                                  \tag{1.3}
\end{aligned}
\]

Hence a proper \(\Delta\)-edge-colouring is exactly a partition into
\(\Delta\) owner-slot matchings, each saturating every upper colour.  Indeed all
\(\Delta\) colours must occur once at every maximum-degree upper vertex.
Every colour class projects to an upper-exact, lower-injective diamond
selector with physical owner degree at most two.  It does **not** imply
physical acyclicity, residence, deep-shadow coverage, or compiler
compatibility.

All scalar divisibilities pass.  Writing

\[
 W={2m-1\choose m},\qquad U={2m-1\choose m+1},qquad
 C=W-U=\operatorname {Cat}_m,                                     \tag{1.4}
\]

each class has `U` edges and leaves exactly `C` lower vertices and `2C`
owner slots unused.  Consequently a class-one obstruction, if one exists,
must be correlated.  A sharp certificate would be a family
\(A\subseteq E(\mathcal H_m)\) with

\[
                            |A|>\Delta\,\nu(A),                    \tag{1.5}
\]

because each of the \(\Delta\) matchings takes at most \(\nu(A)\) edges
from \(A\).

The two conflict projections are separately easy.  Project a slot edge to
its upper--lower pair.  This is a bipartite multigraph with four parallel
copies of every diamond and degrees `Delta` and `Delta-4m`, hence it has a
proper `Delta`-edge-colouring by König's theorem.  Project instead to its
two owner slots.  This is the simple `(Delta-4m)`-regular `K_(2,2)` blow-up
of the middle Johnson graph, hence it has chromatic index at most
`Delta-4m+1`.  The line graph of the full host is the union of these two
conflict graphs.  Therefore separate colourings of the palette rows do not
synchronize the owner row.

For reference, the full line graph is regular of degree

\[
                         8m^2-12m+3.                              \tag{1.6}
\]

At one hyperedge, inclusion--exclusion starts with
`(Delta-1)+3(Delta-4m-1)`, subtracts `8m-5` repeated pair
intersections, and restores the two nontrivial triple intersections.  The
upper star is a clique of order `Delta`, giving the lower bound used above.

## 2. Independent audit of the tight augmenter

Fix \(R\in\mathcal U\).  Choose ordered distinct \(a,b\in R\), set

\[
 L=R-\{a,b\},                                                     \tag{2.1}
\]

choose \(c\notin R\) and \(x\in L\), and define

\[
\begin{array}{lll}
 A=L+a,&B=L+b,&C=L+c,\\
 L'=L-x+c,&&D=L-x+a+c,\\
 S=L+a+c.                                                         \tag{2.2}
\end{array}
\]

For slots \(i,j,p,q\in\{0,1\}\), put

\[
\begin{aligned}
 f&=\{S,L,A^i,C^j\},\\
 e&=\{R,L,A^i,B^p\},\\
 g&=\{S,L',C^j,D^q\}.                                            \tag{2.3}
\end{aligned}
\]

The three diamonds are literal.  The first two are immediate, while

\[
                         S-L'=\{a,x\}                             \tag{2.4}
\]

shows that the middle corners of the third are `C=S-a` and `D=S-x`.
The owners `A,B,C,D` are pairwise distinct, and `R!=S`, `L!=L'`.
Therefore `e,g` are disjoint for every one of the sixteen slot choices.
Moreover

\[
                 V(e\cup g)\setminus V(f)
                    =\{R,L',B^p,D^q\}.                            \tag{2.5}
\]

If `f` belongs to a matching, `R` is missing, and the last three vertices
of (2.5) are free, then replacing `f` by `e,g` is a legal matching
augmentation.  Another slot of physical owner `B` or `D` may already be
occupied; this merely gives the allowed physical degree two.

For fixed `R`, the independent parameter counts are

\[
 (m+1)m,\qquad m-2,\qquad m-1,\qquad16,                           \tag{2.6}
\]

which multiply to (0.2).  There is no quotient by swapping `a,b`, since
that changes the auxiliary upper `S`.  More intrinsically, in the
role-labelled triple `(f,e,g)`, `A` is the common owner of `f,e` and `C`
the common owner of `f,g`; then

\[
 b=R-A,\qquad a=R-B,\qquad c=C-L,qquad x=L-L',                   \tag{2.7}
\]

and all slots are visible.  This proves injectivity of the count.

The construction needs `m>=3`.  At `m=2`, the factor `m-2` vanishes and
there is no exterior label `c`.

## 3. What is known about full class one

### Theorem 3.1 (the first two dimensions are class one)

The owner-slot hosts satisfy

\[
                         \chi'(\mathcal H_2)=12,\qquad
                         \chi'(\mathcal H_3)=24.                  \tag{3.1}
\]

#### Proof

For `m=2` there is one upper vertex and its twelve incident edges must and
can receive twelve distinct colours.

For `m=3`, identify `Omega` with `Z_5` and develop every hyperedge under
translation.  The 120 edges form 24 translation orbits of order five.
Twenty orbits are already matchings.  The only nonmatching orbits are
`B_(d,i)`, with `d in {1,2}` and `i in {0,1}`: at
`R_x=Omega-x`, take the deleted pair `{x-d,x+d}` and give both middle
owners slot `i`.  Each is a five-cycle on one owner-slot orbit.

Recolour these twenty edges by the table

\[
\begin{array}{c|ccccc}
 &0&1&2&3&4\\ \hline
B_{1,0}&0&1&0&1&2\\
B_{1,1}&1&0&1&0&3\\
B_{2,0}&2&2&3&3&0\\
B_{2,1}&3&3&2&2&1.
\end{array}                                                       \tag{3.2}
\]

Every column is a permutation.  The first two rows properly colour their
step-one five-cycles and the last two their step-two five-cycles.  The
different `(d,i)` rows have disjoint remaining resource orbits whenever
their displayed colours agree.  Thus (3.2) gives four upper-saturating
matchings, which together with the twenty good translation orbits give 24
colours.  The upper star is a 24-clique in the line graph, so equality
holds.  \(\square\)

Thus the smallest possible class-one obstruction is `m=4`.

### Theorem 3.2 (forest one-factorization is sufficient)

Let \(B_m\) be the bipartite graph on
\(\mathcal U\mathbin{\dot\cup}\mathcal L\), with one edge for every
diamond \(L\subset R\).  Its upper degree is

\[
                         q={m+1\choose2}.                           \tag{3.3}
\]

Suppose `B_m` has a proper `q`-edge-colouring such that, for every base
colour, the corresponding physical middle-owner edges form a linear
forest.  Then \(\mathcal H_m\) is class one.

#### Proof

Fix one base-colour forest.  Bipartition each path component and properly
two-colour its physical edges by a bit `epsilon(e)`.  Orient every edge
from the black endpoint to the white endpoint.  Read `i,j` in that
black-to-white endpoint order, and assign the slot hyperedge the subcolour

\[
                         (i\oplus\epsilon(e),
                          j\oplus\epsilon(e))\in\mathbb F_2^2.
                                                                        \tag{3.4}
\]

The four slot copies of one diamond receive all four subcolours.  At a
fixed owner slot, two incident physical edges have opposite `epsilon`, so
their two-element subcolour sets are disjoint.  Hence this is a proper
four-colouring over the base colour.  Doing it independently for all `q`
base colours gives \(4q=2m(m+1)=\Delta\) colours.  \(\square\)

König's theorem always supplies a proper `q`-edge-colouring of `B_m`.
The unresolved condition is the simultaneous physical linear-forest row;
Theorem 3.2 is a sufficient construction, not an assertion that an
arbitrary König factorization has that property.

## 4. Exact simultaneous augmentation theorem

Let `M` be an owner-slot matching whose physical projection `F` is a
linear forest.  Let `H` be its set of missing upper colours.  For a tight
augmenter `gamma`, write

\[
 d_\gamma=A_\gamma C_\gamma,\qquad
 N_\gamma=\{A_\gamma B_\gamma,C_\gamma D_\gamma\},                \tag{4.1}
\]

for the deleted and added physical edges.

### Theorem 4.1 (one-round matching and graphic criterion)

Choose one candidate augmenter for every `R in H`.  Replacing all of their
auxiliary edges simultaneously gives an upper-exact owner-slot matching
whose physical projection is a linear forest if and only if:

1. the chosen auxiliary edges are distinct;
2. the triples `\{L'_gamma,B_gamma^p,D_gamma^q\}` are pairwise disjoint
   and free in `M`;
3. the final physical degree is at most two; and
4. for every nonempty owner set \(Z\subseteq\mathcal M\),

\[
 \sum_\gamma
 \left(
  {\bf1}_{A_\gamma B_\gamma\subseteq Z}
 +{\bf1}_{C_\gamma D_\gamma\subseteq Z}
 -{\bf1}_{A_\gamma C_\gamma\subseteq Z}
 \right)
 \le |Z|-1-|E_F(Z)|.                                              \tag{4.2}
\]

The degree condition in item 3 is automatic from owner-slot matching
legality, but is displayed to make the physical statement explicit.

#### Proof

Items 1--2 and the distinct missing targets make all new hyperedges
disjoint.  Every old resource outside a switched auxiliary edge is
untouched, and (2.5) accounts for every new resource.  Hence the result is
an owner-slot matching saturating all uppers.

Its projected edge set is

\[
 E_F-\{d_\gamma\}_\gamma
       +\mathop{\bigcup}_\gamma N_\gamma.                          \tag{4.3}
\]

For any `Z`, its number of induced edges is the old number plus the left
side of (4.2).  The graphic inequalities `|E(Z)|<=|Z|-1` for all nonempty
`Z` are necessary and sufficient for a multigraph to be a forest; they
also catch loops and parallel two-cycles.  This proves (4.2) and the
theorem.  \(\square\)

Equivalently, delete all selected `d_gamma`, contract every component of
the remaining forest, and require the `2|H|` new physical edges to be
graphic-independent in the quotient.  Since each switch adds one net
edge, a legal round reduces the component count by exactly `|H|`.

## 5. The exact weaker absorber interface

Theorem 4.1 avoids a full \(\Delta\)-edge-colouring.  To isolate its resource
row, let

\[
 \mathcal R_M=(M\setminus P)\mathbin{\dot\cup}
   (\mathcal L\setminus V(M))\mathbin{\dot\cup}
   ((\mathcal M\times\{0,1\})\setminus V(M)),                    \tag{5.1}
\]

where `P` is the protected bank.  For every missing upper `R`, form a
four-uniform hypergraph \(\mathcal A_R\) on \(\mathcal R_M\): a candidate
contributes

\[
                         \{f,L',B^p,D^q\},                         \tag{5.2}
\]

where `f in M-P` is its auxiliary edge and the other three resources are
free.

### Proposition 5.1 (resource completion normal form)

The tight one-to-two catalogue completes all missing uppers in one round
at the owner-slot level if and only if the family
\((\mathcal A_R:R\in H)\) has a
rainbow matching.  A simple sufficient condition is

\[
             \nu(\mathcal A_R)>4(|H|-1)\qquad(R\in H).            \tag{5.3}
\]

#### Proof

A rainbow matching chooses distinct auxiliary edges and pairwise-disjoint
free triples, which are exactly items 1--2 of Theorem 4.1.  Conversely any
one-round tight completion records such a rainbow matching.

For (5.3), process the missing uppers in any order.  Fix a matching in
\(\mathcal A_R\) of
more than `4(|H|-1)` candidate resource edges for the next upper.  Each
previously chosen four-set meets at most four members of this matching, so
fewer than all candidates have been destroyed.  Greedy choice succeeds.
\(\square\)

For a sharper cutwise sufficient test one may use the standard colourful
hypergraph Hall theorem:

\[
 \nu\!\left(\bigcup_{R\in X}\mathcal A_R\right)>4(|X|-1)
                    \qquad(\varnothing\ne X\subseteq H).          \tag{5.4}
\]

Condition (5.4) supplies the rainbow matching.  It does not supply the
graphic cuts (4.2); those are the remaining physical correlation row.

## 6. Scope and remaining theorem

The local theorem is therefore load-bearing but not yet an all-dimensional
completion proof.  Its exact role is

\[
 \boxed{\text{protected near-perfect owner-slot matching}}
 \longrightarrow
 \boxed{\text{rainbow tight-augmenter matching}}
 \longrightarrow
 \boxed{\text{graphic cut oracle}}.                              \tag{6.1}
\]

Raw supply is ample: a fixed target has `Theta(m^4)` candidates and any
fixed non-target resource occurs in only `O(m^3)` of them, so an `o(m)`
protected vertex bank removes only `o(m^4)` candidates.  Current matching
occupancy can nevertheless correlate all free resources, and menu size
alone does not prove (5.3) or (5.4).

No class-one obstruction has been found.  Conversely, class one would
still leave physical acyclicity and every downstream word guard.  The
weakest useful next theorem is therefore not a full resolution: prove
(5.4), or an equivalent alternating expansion, for one protected
near-perfect matching while simultaneously satisfying (4.2).  Residence,
deep shadows, and common-cap compilation remain separate and are not
claimed here.
