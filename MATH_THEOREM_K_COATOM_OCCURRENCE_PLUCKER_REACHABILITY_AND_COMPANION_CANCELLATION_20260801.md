# Occurrence-labelled Pluecker reachability and cross-flag companion cancellation

Date: 2026-08-01  
Lane: K, physical lower-compiler reachability  
Status: exact restricted-support Markov theorem, exact all-depth
cross-flag cancellation lemma, and a bounded private-anchor Hall theorem.
The hypotheses have not yet been realized in a global safe carrier, so no
bounded compiler defect or additive-constant upper bound is claimed.

## 0. Outcome

The saturated catalogue lattice is now authoritative: the complete
all-depth action of one coatom packet is an antisymmetric Boolean flag, and
its depth-two projection is the Johnson-square relation

\[
 e_{H+a+x}+e_{H+b+y}-e_{H+b+x}-e_{H+a+y}.             \tag{0.1}
\]

All such squares generate the fixed-coordinate-degree lattice.  The issue is
therefore not integer span.  It is whether a prescribed **nonnegative,
occurrence-labelled** fibre is connected by the squares which are physically
available in one carrier.

This note proves three sharper statements.

1. For a fixed bipartite frame, all even occurrence circuits form an exact
   Markov basis.  Four-cycles alone form a Markov basis for every fibre if
   and only if the allowed occurrence graph is chordal bipartite, provided
   every graph four-cycle has a literal guarded coatom lift.  An induced
   \(C_6\) is the first exact obstruction.
2. For \(d\ge3\), a fixed filler flag forces every isolated \(q=2\) switch to carry a
   companion \(q=d\) square.  Swapping the first two filler positions
   cancels all intermediate depths.  Taking opposite commutators on two
   different internal filler cores cancels the deep companion as well and
   leaves an exact \(q=2\)-only core transfer.  For adjacent cores this is
   an eight-corner Boolean cube, not one quadratic square.
3. On the source-fixed private-anchor face, row/column quota shortfalls give
   an explicit compiler-defect bound.  If

   \[
     \Phi=\sum_u(\deg_D(u)-r_u)^+
          +\sum_v(\deg_D(v)-c_v)^+,                  \tag{0.2}
   \]

   then some table in the fibre misses at most \(\Phi\) demanded \(q=2\)
   targets; if \(\Phi=0\), it misses none.  Markov completeness makes that
   table reachable.  This implication fails without injective guarded
   anchors and says nothing by itself about deeper compiler rows.

The exact remaining construction is consequently a physical one: build a
square-complete or circuit-complete occurrence support, lift its moves with
common guards, and keep the companion-square and nonlinear maximal-cap
ledgers bounded.

## 1. The fixed-frame table

Fix a common Boolean core \(H\) and two disjoint label shores \(U,V\).
Write

\[
                   T_{uv}=H\cup\{u,v\},
                   \qquad (u,v)\in U\times V.          \tag{1.1}
\]

An unlabelled occurrence table is

\[
                       x=(x_{uv})\in\mathbb N^{U\times V}.       \tag{1.2}
\]

Its row and column sums are denoted \(r_u,c_v\).  A \(q=2\) coatom action
inside this frame is

\[
 \square(u,u';v,v')=
 e_{uv}+e_{u'v'}-e_{uv'}-e_{u'v}.                    \tag{1.3}
\]

For the canonical packet, take

\[
 H=K\cup\{\infty,c\}\cup\{f_2,\ldots,f_{d-1}\},quad
 U=\{a,b\},\quad V=\{f_1,f_d\};                     \tag{1.4}
\]

then its depth-two action is exactly (1.3).

Let

\[
 \partial:\mathbb Z^{U\times V}\longrightarrow
          \mathbb Z^U\oplus\mathbb Z^V,\qquad
 e_{uv}\longmapsto e_u\oplus e_v.                  \tag{1.5}
\]

The authoritative Pluecker-lattice theorem implies the corresponding
uniform-set statement globally.  In the fixed frame, its representation is
particularly transparent.  If \(I_U,I_V\) are the augmentation ideals,

\[
                   \ker_{\mathbb Z}\partial=I_U\otimes I_V.    \tag{1.6}
\]

After choosing \(u_0,v_0\), the tensors

\[
 (e_u-e_{u_0})\otimes(e_v-e_{v_0})                   \tag{1.7}
\]

are integral square generators.  Over characteristic zero this is the
standard-module tensor factor in the permutation representation of
\(S_U\times S_V\).  Equation (1.6) concerns the saturated lattice; it does
not imply nonnegative or physical reachability.

## 2. Exact nonnegative Markov basis

Let \(G=(U,V;E)\) be a bipartite allowed-support graph.  For a nonnegative
integer degree vector \(b\) on \(U\cup V\), define the fibre

\[
 \mathcal F_G(b)=\{x\in\mathbb N^E:\partial x=b\}.              \tag{2.1}
\]

An even cycle has its two alternating edge classes.  Adding one class and
subtracting the other is its circuit move.

### Theorem 2.1 (all circuits are an exact Markov basis)

For every bipartite \(G\), the even-cycle circuit moves connect every
nonempty fibre \(\mathcal F_G(b)\).

#### Proof

For \(x,y\in\mathcal F_G(b)\), color each copy in \((x-y)^+\) red and each
copy in \((y-x)^+\) blue.  At every vertex the red and blue degrees agree.
Pair them locally and follow alternating colors.  This decomposes the
discrepancy into alternating even closed walks, which split into simple even
cycles.  On each cycle subtract the red class and add the blue class.  The
move is nonnegative because every subtracted edge is a current red copy, and
it strictly reduces \(\|x-y\|_1\).  Iteration reaches \(y\). \(\square\)

Call \(G\) **chordal bipartite** if it has no induced cycle of length more
than four.

### Theorem 2.2 (sharp square criterion)

The following are equivalent.

1. Four-cycle moves connect every nonempty fibre of \(G\).
2. Every even-cycle move admits a nonnegative sequential realization by
   four-cycle moves from every table containing its subtracted edge class.
3. \(G\) is chordal bipartite.

#### Proof

Suppose \(G\) is chordal bipartite.  A cycle of length at least six has a
chord, which divides it into two smaller even cycles.  Orient the first
subcycle move so that it subtracts only old negative-class edges and creates
   one copy of the chord.  Orient the second so that it consumes that chord and
   subtracts the remaining old edges.  This is a nonnegative, feasibly ordered
   realization of the original cycle move.  The square vectors need not be
   sign-conformal as formal vectors: the transient chord is created and then
   cancelled.  Induction on cycle length proves 3 implies 2, and Theorem 2.1
   gives 1.

Conversely, let \(C_{2\ell}\), \(\ell\ge3\), be induced.  Give every cycle
vertex degree one and every exterior vertex degree zero.  The fibre consists
of the two alternating perfect matchings of the cycle.  No exterior edge can
occur, and the induced cycle contains no four-cycle.  Hence the two states
cannot be joined by square moves.  Thus 1 implies 3.  The implication 2 to 1
is immediate. \(\square\)

For complete \(G=K_{U,V}\), this gives the usual quadratic Markov basis.
More constructively, one unit alternating cycle of length \(2\ell\) can be
triangulated with \(\ell-1\) squares: the first square creates a chord, each
successive square moves that buffer chord forward, and the last consumes it.
Consequently any two tables in a complete fibre are joined by at most

\[
                              {1\over2}\|x-y\|_1                 \tag{2.2}
\]

square moves.

The induced-\(C_6\) obstruction is the cubic binomial

\[
 X_{u_1v_2}X_{u_2v_3}X_{u_3v_1}
 -X_{u_1v_3}X_{u_3v_2}X_{u_2v_1}.                    \tag{2.3}
\]

Thus a literal alternating \(C_6\) macro is not merely a larger heuristic
move: it is the first missing Markov generator whenever physical support is
not rectangle-complete.

## 3. Occurrence-labelled physical lift

Let \(\Omega\) be a set of source-fixed physical occurrences.  An occurrence
\(\omega\) has an allowed endpoint list \(L(\omega)\subseteq V\); its row
type \(u(\omega)\in U\) is fixed.  Form the labelled support graph

\[
              \widetilde G=(\Omega,V;
                    \{\omega v:v\in L(\omega)\}).                \tag{3.1}
\]

A state is a matching with degree one at every \(\omega\) and prescribed
degrees at \(V\).  A graph four-cycle exchanges the endpoint choices of two
occurrences.  Its projected target change is (1.3).

Call the bank **square-transparent** when:

1. every graph four-cycle used in Theorem 2.2 is a literal embedded coatom
   switch on those two occurrences;
2. the switch preserves the declared owner, upper, residence and trace-guard
   state; and
3. occurrences with the same projected row type are either compiler-
   indistinguishable or admit the required neutral label exchange.

### Corollary 3.1 (physical occurrence Markov theorem)

If \(\widetilde G\) is chordal bipartite and square-transparent, every two
physical occurrence assignments in one endpoint-degree fibre are connected
by literal \(q=2\) coatom switches.  For arbitrary \(\widetilde G\), the
same conclusion holds after supplying a literal guarded macro for every
chordless even-cycle circuit.

The hypotheses are necessary in scope.  An induced labelled \(C_6\) has two
assignments and no square move.  Even if the unlabelled projected table is
unchanged, two same-type occurrences can also remain disconnected when their
labels matter but no neutral exchange exists.

There is a second, independent invariant.  If \(M\) is a compiler matching,
write \(Q(M)\) for its set of used physical cells.  Every square replaces
two incidences on two cells by the opposite two incidences on those same
cells, and therefore

\[
                              Q(M')=Q(M).                        \tag{3.2}
\]

The symmetric difference of two matchings with the same target shore is a
union of alternating cycles and paths.  Squares can route the cycle
components, but every path has two cell-shore endpoints and changes
\(Q(M)\).  Hence square Markov completeness cannot by itself improve the
fixed-basis deficiency

\[
                         |\mathcal L|-\nu(G[\mathcal L,Q(M)]).  \tag{3.3}
\]

An exterior free cell, dummy endpoint, or other literal basis-changing
operation is indispensable.  This is exactly the endpoint resource measured
by Thread D's return-Hall graph.

The prospective ordered-pair coatom atlas has abstract support
\(K_{q,q}\) with its diagonal removed.  If that ordered-pair set is used
directly as an occurrence support, then for \(q\ge3\) it contains the
induced cycle

\[
 u_1v_2u_3v_1u_2v_3u_1.                              \tag{3.4}
\]

Hence a square-only universal Markov claim on that interpretation is false;
the cubic move (2.3) is required.  This is an architecture-specific warning,
not a claim that the current compiler must use the ordered-pair parameters
as its two occurrence shores.

Most importantly, the catalogue theorem says that every labelled square
exists somewhere.  It does not imply square-transparency at a fixed carrier
occurrence.  The fixed-incumbent coatom theorem in fact recovers its ordered
parameter pair and gives fibre one at one planted old word.  Physical
square-completeness is therefore a new reachability theorem, not a corollary
of lattice saturation.

## 4. The fixed-flag companion and its cancellation

Let

\[
 F=I\mathbin{\dot\cup}\{x,y\},\qquad |I|=d-2,                  \tag{4.1}
\]

and fix an order of \(I\).  Let \(\pi=(x,y,I)\) and
\(\pi'=(y,x,I)\).  Subtract their antisymmetric flag signatures.

### Lemma 4.1 (two-layer flag commutator, \(d\ge3\))

Assume \(d\ge3\).

The signed two-packet commutator \(A(\pi)-A(\pi')\) vanishes at every flag
layer except \(t=1,d-1\).  Under the physical target embedding, its only
lower actions are

\[
 Q_G(a,b;x,y)\quad(q=d),qquad
 Q_{G\cup I}(a,b;x,y)\quad(q=2),                    \tag{4.2}
\]

with the same orientation, where

\[
 Q_R(a,b;x,y)=
 e_{R+a+x}+e_{R+b+y}-e_{R+b+x}-e_{R+a+y}.            \tag{4.3}
\]

#### Proof

Swapping filler positions one and two changes only the rank-one prefix and
the complementary rank-\((d-1)\) suffix in the flag signature.  The
rank-one difference is \(e_x-e_y\), which embeds as \(Q_G\).  The
rank-\((d-1)\) difference is
\(e_{F-y}-e_{F-x}\), which embeds as \(Q_{G\cup I}\).  All intermediate
prefixes and complementary suffixes agree. \(\square\)

Thus a nonzero \(q=2\) action cannot be isolated inside one fixed filler
flag: the complement relation forces its deep companion.

For \(d=2\), the layers \(t=1\) and \(t=d-1\) coincide.  Their two signed
contributions add, so the sole row is \(2Q_G(a,b;x,y)\) at
\(q=2=q=d\), rather than two separately indexed companion squares.
There are no two distinct zero-dimensional internal cores to use in the
cross-flag cancellation below; \(d=2\) is a bounded base case.

### Theorem 4.2 (cross-flag q2-only transfer)

Assume \(d\ge3\).  Let \(I,J\) be two available \((d-2)\)-element internal
filler cores, disjoint from \(G,a,b,x,y\), with the same
\(G,a,b,x,y\).  Take the commutator of Lemma 4.1 on \(I\) and the oppositely
oriented commutator on \(J\).  The total lower action is

\[
               Q_{G\cup I}(a,b;x,y)
                -Q_{G\cup J}(a,b;x,y)                \tag{4.4}
\]

at \(q=2\), and zero at every other depth.

#### Proof

Each commutator has no intermediate action.  Their identical deep
\(Q_G(a,b;x,y)\) companions cancel, leaving (4.4). \(\square\)

Algebraically this uses four reversible packet actions.  Literally it needs
four serially available embeddings, or an owner-compatible simultaneous
macro, with the common upper/residence guards replayed at each step.

If \(I=H\cup\{u\}\) and \(J=H\cup\{v\}\), where \(|H|=d-3\), then (4.4)
is the pure cube

\[
       (e_a-e_b)\otimes(e_x-e_y)\otimes(e_u-e_v),              \tag{4.5}
\]

with the fixed core \(G\cup H\) adjoined.  It has eight corners and every
one- and two-factor marginal vanishes.  Thus the first all-depth-neutral
primitive obtained from adjacent flag swaps is cubic in its three binary
directions; a lone fixed-flag quadratic cannot lose its reflected deep
companion.

For a set \(\mathcal I\) of internal cores, let \(R_{\mathcal I}\) be the
graph whose edges are physically available transfers (4.4).  If
\(R_{\mathcal I}\) is connected, these transfers generate the full zero-sum
coefficient lattice

\[
 \left\{\sum_{I\in\mathcal I}z_IQ_{G\cup I}:
                         \sum_Iz_I=0\right\}.                    \tag{4.6}
\]

This is a genuine all-depth-neutral counter sublattice.  It does not
claim to be the complete kernel of the global companion map when different
deep squares satisfy further relations.

There is already a physical obstruction before U5.  For fixed
\(F=I\mathbin{\dot\cup}\{x,y\}\), the two order variants used in Lemma 4.1
share the upper-screen owner

\[
             O_F=K\cup\{\infty,c,a,b\}\cup F.                  \tag{4.7}
\]

Changing the usual private extreme filler or private active label does not
separate this owner.  Hence four pairwise-owner-disjoint canonical slots do
not realize Theorem 4.2: the two copies over \(I\) collide at \(O_{F_I}\),
and the two over \(J\) collide at \(O_{F_J}\).  A literal proof needs a
shared-owner four-arm resolver, a modified packet which privatizes (4.7),
or a serial reuse theorem whose intervening filler-order action is included
in the ledger.  None is currently available.

Whether a degree-two shared-owner reconnection can preserve the lower
palette, upper unions, residence and boundary decks simultaneously is open;
topological degree counting alone does not certify such a resolver.

## 5. A bounded private-anchor compiler theorem

Assume now the complete fixed frame \(U\times V\).  Let
\(D\subseteq U\times V\) be the demanded \(q=2\) target types, one target
per pair.  Suppose every occurrence is a distinct, source-fixed,
trace-guarded compiler cell dedicated to its assigned target.  Then a table
\(x\) has exact private-anchor Hall deficiency

\[
                    \delta_D(x)=|\{(u,v)\in D:x_{uv}=0\}|.       \tag{5.1}
\]

For prescribed margins \(r,c\), put

\[
 \alpha_u=(\deg_D(u)-r_u)^+,qquad
 \beta_v=(\deg_D(v)-c_v)^+,qquad
 \Phi=\sum_u\alpha_u+\sum_v\beta_v.                 \tag{5.2}
\]

### Theorem 5.1 (explicit bounded-defect table)

There is a table in the margin fibre with

\[
                             \delta_D(x)\le\Phi.                 \tag{5.3}
\]

In particular, if every row and column has enough quota for its demanded
targets, then \(\delta_D(x)=0\).  From any initial table in the same complete
fibre, a sequence of q2 squares reaches such a table.

#### Proof

For each row \(u\), mark \(\alpha_u\) demanded pairs in that row for
omission.  For each column \(v\), additionally mark \(\beta_v\) demanded
pairs in that column.  Let \(Z\) be the union of all marked pairs.  Then
\(|Z|\le\Phi\), and the retained demand matrix
\(b=\mathbf1_{D-Z}\) satisfies

\[
                \sum_vb_{uv}\le r_u,qquad
                \sum_ub_{uv}\le c_v.                 \tag{5.4}
\]

Subtract these retained unit demands from the margins.  The residual row
and column margins are nonnegative integers with equal total.  On the
complete bipartite frame, greedily place the minimum of the first positive
row and column residual, delete an exhausted margin, and continue.  This
gives a nonnegative residual table \(y\).  Then \(x=b+y\) has the required
margins and is positive on every pair in \(D-Z\), proving (5.3).  Theorem
2.2 connects the complete fibre by squares. \(\square\)

The bound is intentionally elementary rather than optimal.  Every omitted
pair can pay at most one row and one column shortage, so
\(\max\{\sum\alpha_u,\sum\beta_v\}\) is a lower bound; overlapping shortage
patterns can prevent equality with that lower bound.

### Scope of the Hall conclusion

The private-anchor hypothesis is essential.  If two positive target rows
have the same sole physical cell, their table counts are positive but their
Hall deficiency is one.  More generally, maximal-cap nonzeroness and
overlapping interval constraints are nonlinear and are not encoded in
row/column margins.  A valid physical application must export:

1. injective source-fixed anchors or the full guarded target--cell graph;
2. a square-transparent occurrence support;
3. the all-depth companion ledger of Section 4; and
4. a joint maximal-cap replay after the terminal matching is chosen.

For the current mixed coatom tensor, the canonical local chain cells have
disjoint phase domains, and Thread D's exact trace-guarded local return graph
is empty, although native columns exist and an exterior return bank remains
open.  Thus Theorem 5.1 presently has no literal local return-anchor bank to
act on.  It is a concrete sufficient transition theorem, not a proof of
bounded U5.

## 6. Exact remaining criterion

The authoritative saturated flag lattice removes all linear congruence
questions.  A proof of bounded terminal compiler deletion can now use the
following finite physical state.

* **Occurrence support:** a labelled bipartite graph
  \(\widetilde G\), with every required four-cycle or chordless circuit
  realized by a safe packet macro.
* **Companion state:** for every q2 move, its deep-square label; admissible
  terminal combinations have zero or bounded companion sum.  The transfers
  (4.4) give an explicit zero-companion sublibrary.
* **Compiler state:** guarded private anchors, or the exact nonlinear
  common-cap obstruction clutter.  On the private complete face, (5.2) is a
  sufficient bounded-defect potential.

An exact all-dimensional sufficient row is therefore:

> In every safe child, the occurrence support contains a circuit-complete
> source-fixed bank and either (i) the private complete occurrence frame of
> Theorem 5.1 or (ii) an explicit certificate that the retained demand
> indicator extends to the prescribed margins on the allowed support; its
> core-transfer graph is connected; its row/column shortage potential
> \(\Phi\) and uncancelled companion repair cost are bounded by one absolute
> constant; and its selected assignment passes the joint maximal-cap trace
> guards.

Under that row, Theorems 2.1, 4.2 and 5.1 give a physically reachable
terminal compiler with bounded q2 and companion defect.  Coverage at
\(q\ge3\), hard packet-cell tasks, and regeneration of the same bank remain
separate unless included in the guarded state.

Dependencies:

* `MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`;
* `MATH_THEOREM_K_ZERO_OWNER_COATOM_U5_REGENERATIVE_RECURRENCE_20260801.md`;
* `MATH_THEOREM_K_OCCURRENCE_LABELLED_PLUCKER_LIFT_AND_ENDPOINT_OBSTRUCTION_20260801.md`;
* `MATH_THEOREM_K_COATOM_Q2_PLUCKER_MARKOV_AND_COMPILER_PRESSURE_20260801.md`;
* `MATH_THEOREM_K_COATOM_JOHNSON_PLUCKER_MARKOV_AND_CHAIN_HALL_20260801.md`;
* `MATH_THEOREM_SERIAL_COATOM_SAFE_SEARCH_AND_FINAL_COMPILER_REDUCTION_20260801.md`;
* `MATH_THEOREM_THREAD_D_COATOM_TENSOR_COMPILER_PREFIX_AUGMENTED_HALL_GATE_20260801.md`;
* `MATH_THEOREM_THREAD_D_COATOM_U5_NATIVE_COLUMNS_AND_RETURN_HALL_20260801.md`; and
* `MATH_THEOREM_H2_COATOM_TENSOR_FIXED_ACTIVE_MENU_AND_HOST_QUANTIFIER_20260801.md`.
