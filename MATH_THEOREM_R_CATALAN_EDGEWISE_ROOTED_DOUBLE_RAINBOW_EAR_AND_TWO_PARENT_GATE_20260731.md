# Strict edgewise Catalan recursion: rooted double-rainbow ears, the augmented lower graphic gate, and the two-parent correction

Date: 2026-07-31  
Status: exact fixed-basis characterizations; exact private-ear Rado theorem;
smallest fixed-orientation and fixed-basis counterexamples; exact
independent-filler quantifier.  No all-parameter DERF, residence, deep-shadow,
compiler, or contiguous-OR equality theorem is claimed.

## 0. Verdict

The useful strict edgewise recursion survives, but in a narrower and more
precise form than the first formulation suggested.

1. **Directness is undirected.**  A side occurrence must use the physical
   edge and the two palette labels of one child edge.  It need not preserve
   the child arrow.  The final path components are oriented only after the
   complete support is known to be a forest.
2. **The child orientation is existential state.**  The two pulled-back
   direct matroids can have rank strictly below the required
   (C=\operatorname {Cat}_{n+1}).  A fixed coherent orientation can
   therefore fail before topology, even when all physical candidate degrees
   are at least three.
3. **For a fixed direct common (C)-set (Q), the upper no-empty condition
   is exact.**  It is a double-rainbow selector that is independent in the
   physical graphic matroid and spanning after the anchor star is contracted.
   Equivalently, it is a rooted kernel of (C) one-anchor paths followed by
   (K=\operatorname {Cat}_n) endpoint-compatible matching ears.
4. **After fixing that upper shore, the complete lower topology is one
   augmented graphic matroid.**  It must be tested against
   (P_0\cup\Pi^-), not against the central partial matching (P_0) alone.
   Palette exactness and physical capacities remain separate rows.
5. **A genuine Rado theorem is available for private complete ears.**  Its
   graphic rank inequalities are necessary and sufficient under explicit
   resource privacy.  Separate one-palette Rado tests are not enough.
6. **The untouched (c)-rail is an independent parent (G).**  The
   structural parent (F) supplies (Q), the direct occurrences and the
   three-sector attachment geometry; an arbitrary Catalan forest (G) may
   supply the disjoint copied rail.  Consequently every immutable-(c)
   obstruction has only fixed-filler scope.

The corrected induction target is therefore a noncanonical, two-parent
rooted-ear construction.  One must choose a favorable orientation and
(Q), not prove that every orientation or every direct basis works.

## 1. Scope and two corrections to literal strictness

Use, for child parameter (n\ge3),

\[
 M=\binom{2n}{n},\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad K=M-N,
\]

\[
 C=M-P=\operatorname {Cat}_{n+1},\quad
 R=N-C=P-K,\quad H=N-P=C-K.                         \tag{1.1}
\]

Let an oriented child edge be

\[
 q=(L_q,U_q,t_q,h_q),\qquad
 L_q=t_q\cap h_q,\quad U_q=t_q\cup h_q.             \tag{1.2}
\]

The upper direct occurrence at (x\notin U_q) has palette labels
(L_q+x,U_q+x) and undirected physical edge

\[
                 \{t_q+x,h_q+x\}.                    \tag{1.3}
\]

The lower occurrence for (x\in L_q) is the deletion dual.  Formula
(1.3), not the inherited arrow (t_q+x\to h_q+x), is the strict physical
requirement.

### Proposition 1.1 (the saved path orientations do not certify ordered lifts)

In the authenticated child-(n=3) chained witness, child edge (q=14)
supplies the two lower projections

\[
 (L,U,t,h)=(32,37,36,33),\qquad (8,13,12,9).          \tag{1.4}
\]

After the collar tags are installed and the ambient paths are oriented,
the first physical edge is traversed in the stored direction, while the
second is traversed opposite to its stored direction.  While retaining
these saved ambient path orientations, no orientation of the single child
edge (q=14) can make both occurrences inherit its arrow.  Thus the frozen
artifact certifies the undirected direct-edge/palette recursion, not the
stronger ordered recursion.

#### Proof

Literal replay gives ambient traversals (228\to225) for the first edge
and (201\to204) for the second; the stored second arrow is
(204\to201).  Reversing (q=14) reverses both stored projections, so it
cannot agree with both ambient traversals simultaneously. \(\square\)

The two occurrences lie in different ambient path components, so reversing
one output component removes this particular conflict.  Proposition 1.1 is
an audit-scope correction for the saved orientations, not a proof that no
ordered realization of the same undirected support exists.

### Proposition 1.2 (a coherent orientation can have direct rank (13<C))

On ([6]), consider the coherently oriented Catalan forest

```text
28->13;
26->56->49->19;
38->35->41->44->52->21->7->11->25;
37;
42->14->22->50.
```

Its lower and upper edge colours are both the complete palettes.  Its
non-tail bank is

\[
                  \{13,19,25,37,50\}.                 \tag{1.5}
\]

In the upper direct candidate graph the four vertices
({13,19,25,50}) have only the three neighbours
({31,55,59}).  Dually, the non-head bank
({26,28,37,38,42}) has only the four lower neighbours
({2,4,8,32}).  Hence both pulled-back direct restrictions have rank

\[
                 15-6+4=13<14=C.                     \tag{1.6}
\]

In particular this orientation has no direct common (C)-set.  Its two
minimum physical candidate degrees are nevertheless both three, so the
condition (\eta^\pm(F)\ge3) does not imply direct incidence rank.

#### Proof

The displayed neighbour sets violate Hall on the terminal banks.  Rank
four is attained by the upper matching

\[
 (13,31),(19,55),(25,59),(37,47)                     \tag{1.7}
\]

and the lower matching

\[
 (26,8),(28,4),(37,32),(38,2).                       \tag{1.8}
\]

If
({\cal T}) is the rank-six direct transversal matroid and (J) is the
five-element non-tail bank, then (r_{\cal T}(J)=4).  Dual rank on the
fifteen-element tail image is

\[
 15-r({\cal T})+r_{\cal T}(J)=15-6+4=13.
\]

The lower computation is identical.  Direct enumeration of (1.3) gives
physical degree histograms (3^5,4^5,5^5) on both shores. \(\square\)

The counterexample does not say that the underlying undirected forest has
no favorable orientation.  The complete (n=3) census in the cited source
finds a favorable orientation for every undirected forest.  That is a finite
fact, not an all-(n) orientation theorem.

### Proposition 1.3 (orientation is a Boolean endpoint-cut state)

For a fixed undirected Catalan forest, both direct occurrence multigraphs,
including their palette labels and undirected physical edges, are invariant
under coherent reversal of any child path.  On a nontrivial path

\[
                         v_0v_1\cdots v_s,             \tag{1.9}
\]

the tail image is all path vertices except (v_s), while the head image is
all path vertices except (v_0).  Reversing the path swaps those two
terminal choices.  Thus the orientation-dependent part of strict balanced
expansion is exactly one Boolean endpoint choice per child component; it is
not a choice of occurrence graph or of (Q).

#### Proof

For an undirected child edge, (L=t\cap h), (U=t\cup h), the conditions
(x\notin U) and (x\in L), both outer labels, and the unordered physical
edge are unchanged when (t,h) are exchanged.  Along (1.9), coherent
orientation uses (v_0,\ldots,v_{s-1}) as tails and
(v_1,\ldots,v_s) as heads; reversal exchanges the omitted endpoints.
The strict balanced-expansion weights distinguish precisely the omitted
terminal from the endpoint image. \(\square\)

On the authenticated (n=4) child, exact enumeration finds
(7600) of the (2^{14}) endpoint choices satisfying SBE on both shores;
one path flip repairs the stored choice.  At (n=3), no endpoint choice is
two-shore SBE even though direct common bases exist.  SBE is therefore a
useful sufficient orientation cut, not a necessary incidence condition.
Any SBE-based preservation argument should first solve this Boolean
endpoint system and only then invoke common-base integrality to select
(Q).

## 2. Exact upper rooted-tree and path-ear characterizations

Fix henceforth a favorable component orientation and a direct common
(C)-set (Q\subseteq E(F)).  Put

\[
 {\cal D}_Q=\binom{[2n]}n\setminus\{t_q:q\in Q\},\qquad
 A_Q=\{U_q:q\in Q\}\subseteq\binom{[2n]}{n+1}.       \tag{2.1}
\]

Let ({\cal E}_Q^-) be the allowed upper occurrences whose middle label is
in ({\cal D}_Q).  An occurrence (e=(q,x)) has the two palette colours

\[
 d(e)=L_q+x,\qquad v(e)=U_q+x                        \tag{2.2}
\]

and physical edge (\partial e=\{t_q+x,h_q+x\}) on
(Y=\binom{[2n]}{n+1}), (|Y|=N).

Adjoin a root (\rho) and all root-star edges

\[
                  E_\rho=\{\rho a:a\in A_Q\}.        \tag{2.3}
\]

Let (\widehat M_Q) be the graphic matroid of this physical multigraph.
Parallel occurrences remain parallel elements.  Always

\[
 r_{\widehat M_Q}(E_\rho)=C,\qquad
 r_{\widehat M_Q/E_\rho}({\cal E}_Q^-)\le R;          \tag{2.4}
\]

equality in the second relation is a condition, not an identity.

### Theorem 2.1 (upper rooted double-rainbow criterion)

The fixed (Q) admits an upper no-anchor-free direct side if and only if
there is a set (S^-\subseteq{\cal E}_Q^-), (|S^-|=P), such that

1. (d:S^-\to{\cal D}_Q) and
   (v:S^-\to\binom{[2n]}{n+2}) are bijections;
2. every physical vertex has degree at most two and every anchor in (A_Q)
   has degree at most one; and
3. 
   \[
   r_{\widehat M_Q}(S^-)=P,\qquad
   r_{\widehat M_Q/E_\rho}(S^-)=R.                   \tag{2.5}
   \]

#### Proof

The first rank equality says that the (P) physical edges form a forest.
The contraction identity

\[
 r_{\widehat M_Q/E_\rho}(S^-)
 =r_{\widehat M_Q}(S^-\cup E_\rho)-C                \tag{2.6}
\]

has value (R=N-C) exactly when (S^-\cup E_\rho) has rank (N), that
is, when every component of (S^-) meets the anchor star.  The degree caps
then make every component an anchor-capped path.  Conversely, root one
anchor in each of the (H=N-P) no-empty path components.  The resulting
(P+H=N) edges form a spanning tree on (Y\cup\{\rho\}), proving (2.5).
Palette exactness is precisely row 1. \(\square\)

Equivalently, if (L=\widehat M_Q\setminus E_\rho) and
(Q_0=\widehat M_Q/E_\rho), then the two rank equalities say that (S^-)
is a base of the (K)-th Higgs lift between (Q_0) and (L).  This
packages the rooted graphic row into one matroid, but the two palette bases
and the overlapping degree caps remain separate constraints.

The lift rank is explicitly

\[
                 r_{\cal H}(X)=
       \min\{r_{Q_0}(X)+K,\ r_L(X)\}.                 \tag{2.6a}
\]

### Theorem 2.2 (noncanonical rooted kernel plus Catalan ears)

The selector of Theorem 2.1 exists if and only if it has a decomposition

\[
                    S^-=F_0\sqcup E,\qquad
 |F_0|=R=P-K,\quad |E|=K,                             \tag{2.7}
\]

such that:

1. (F_0\cup E) is double-rainbow and satisfies all degree caps;
2. (F_0) is a spanning forest on all of (Y) consisting of exactly (C)
   paths, with isolated vertices counted as paths, each containing exactly
   one anchor; and
3. the (K) edges of (E) join free endpoints of (2K) distinct
   (F_0)-paths.

#### Proof

A no-empty side has (H) components and (C) anchors.  The anchor cap
allows at most two anchors per component.  If (c_i) counts components
with (i) anchors, then

\[
 c_1+c_2=H,qquad c_1+2c_2=C,qquad c_2=C-H=K.        \tag{2.8}
\]

Delete one edge separating the two anchors in every double-anchor path.
This gives (C) one-anchor paths and (K) deleted matching ears.  The
converse concatenates the indicated pairs of rooted paths and creates
neither a cycle nor a degree excess. \(\square\)

The exact one-coordinate Rado relaxation is also useful.  If
({\cal E}(V)) is the occurrence menu of the upper colour (V), then a
spanning tree using one occurrence of each (V) and (H) root-star edges
exists exactly when, for every set ({\cal U}) of upper colours,

\[
 r_{\widehat M_Q}\!\left(\bigcup_{V\in{\cal U}}{\cal E}(V)\right)
       \ge |{\cal U}|,                                \tag{2.9}
\]

\[
 r_{\widehat M_Q/E_\rho}\!\left(
       \bigcup_{V\in{\cal U}}{\cal E}(V)\right)
       \ge |{\cal U}|-K.                             \tag{2.10}
\]

These are Rado's inequalities.  They do not enforce the second palette or
the physical degree caps.

### Proposition 2.3 (a direct common basis need not be rooted)

On the recursively supplied (n=4) child, there is a direct common basis
whose retained edge set is

\[
 \{0,14,17,19,23,26,27,36,39,49,50,51,52,53\}.       \tag{2.11}
\]

Writing this displayed set as (Z), the common basis is
(Q=E(F)\setminus Z), of order (42).

Both direct incidence matchings exist, but the full allowed upper physical
graph isolates the two nonanchors (31,211).  After contracting the
(C=42) anchors, its rank is (12<R=14).  Hence no upper no-empty side
exists for this (Q).

#### Proof

The singleton cuts ({31}) and ({211}) have no selected or candidate
edge leaving them and contain no anchor, contradicting the rooted cut form
of (2.5).  The contracted graph has fifteen vertices and three components,
hence rank twelve. \(\square\)

Thus (Q) must be selected jointly with rooted topology; direct
common-basis incidence alone is insufficient.

There is a second scope limitation.  The authenticated chained child-
(n=6) lift is a valid strict direct collar with side anchor histograms

\[
 (c_0,c_1,c_2)^-=(12,141,144),\qquad
 (c_0,c_1,c_2)^+=(16,133,148).                       \tag{2.12}
\]

Hence its selected shores are not rooted/no-empty.  This does not prove
that the same child has no alternative rooted selection, but it proves that
the rooted path-ear state is a stronger certificate and is not propagated
automatically by an unconstrained successful DERF lift.

## 3. The exact lower augmented graphic gate

Use disjoint seam-label copies (Q_T,Q_H).  Contracting the retained child
segments gives the central partial matching

\[
 q_Tq'_H\in P_0
 \quad\Longleftrightarrow\quad
 [t_q]_{F-Q}=[h_{q'}]_{F-Q}.                          \tag{3.1}
\]

The fixed upper side induces a (K)-matching (\Pi^-) on (Q_T).  Put

\[
                         F_\ast=P_0\cup\Pi^-.         \tag{3.2}
\]

This is a forest: every (Q_H)-vertex has degree at most one, and all
other fixed edges form a matching on (Q_T).

For every lower anchor (b^+(q)=L_q), add a spoke from (b^+(q)) to the
component of (F_\ast) containing (q_H).  Let (A_0) denote this fixed
spoke forest.  Pull the graphic matroid of the augmented graph, contracted
by (A_0), back to the direct lower occurrence ground.

### Theorem 3.1 (lower topology is one augmented graphic row)

For every anchor-capped lower linear support (S^+),

\[
 \boxed{
 \beta(A_0\cup\partial S^+)
  =\beta(P_0\cup\Pi^-\cup\Pi^+(S^+)).}               \tag{3.3}
\]

Consequently a lower completion compatible with the fixed upper shore is
exactly a set of (P) direct occurrences satisfying:

1. bijectivity on the lower outer palette;
2. bijectivity on the punctured middle palette;
3. physical degree at most two and anchor degree at most one;
4. independence in the augmented graphic matroid.

If the lower shore is also required to have no empty component, add its
own rooted spanning-tree condition from Theorem 2.1.

#### Proof

Contract every lower path component.  An empty component becomes isolated;
a one-anchor component and its spoke become a leaf; and a two-anchor
component with its two spokes becomes a subdivision of the corresponding
edge of (\Pi^+).  Deleting isolates and leaves, suppressing subdivisions,
and contracting fixed forest edges preserve cycle rank.  The remaining
multigraph is (P_0\cup\Pi^-\cup\Pi^+), proving (3.3). \(\square\)

The words “against (P_0)” are therefore unsafe shorthand.  The lower
pairing must be graphic-independent against the whole fixed forest
(P_0\cup\Pi^-).  A parallel upper/lower pair is represented and counted as
a two-cycle, hence is forbidden by graphic independence.

## 4. A genuine augmenting-ear/Rado theorem

The original lower occurrence problem still has two palette partitions,
one graphic row and overlapping degree capacities; ordinary Rado does not
solve that four-resource intersection.  Rado becomes exact after the
recursion supplies complete private path ears.

### Theorem 4.1 (private complete-ear Rado criterion)

Fix an already installed lower scaffold whose suppressed links, together
with (P_0\cup\Pi^-), form a forest.  Let (I) be the remaining ear slots.
For every (i\in I), let ({\cal P}_i) be a nonempty menu of complete
direct lower path ears.  Assume:

1. every ear has two unused lower anchors as endpoints, no other anchor,
   and is internally palette-injective and degree-valid;
2. different slots have disjoint private physical vertices, both palette
   banks and anchor endpoints; and
3. every one-per-slot choice, together with the scaffold, covers exactly
   the prescribed remaining resources, so no installed occurrence is ever
   withdrawn.

Contract the entire augmented fixed forest: the scaffold,
(P_0\cup\Pi^-), and the fixed anchor spokes.  Map an ear (P) to the
quotient edge (\sigma(P)) joining its two contracted anchor components,
and let ({\cal G}) be the resulting graphic matroid.  Then compatible ears
(P_i\in{\cal P}_i) exist for every slot if and only if

\[
 r_{\cal G}\!\left(
      \bigcup_{i\in J}\sigma({\cal P}_i)\right)\ge |J|
                         \qquad(J\subseteq I).         \tag{4.1}
\]

Every selected family is serializable in any slot order.

#### Proof

Rado's theorem gives one independent quotient edge from each menu exactly
under (4.1).  Resource privacy makes all physical, palette and capacity
checks commute.  Every prefix of a graphic-independent set is independent,
so arbitrary installation order is legal. \(\square\)

The private-bank assumptions are essential.  In the authenticated strict
(n=3) child, retain edge (1), one of the four direct common bases.  There
are two no-empty upper pairing types and one no-empty lower pairing type,
yet the two unions have cycle ranks (1) and (4).  For the first upper
type, all (63) nonempty one-palette Rado inequalities pass separately for
each six-colour palette.  The synchronized family is nevertheless empty.
Thus separate Rado tests and marginal upper/lower existence do not imply a
collar.

## 5. The independent filler and the exact two-parent quantifier

Let (T(F,Q,S^-,S^+)) denote the complete (0,z,cz) three-sector support:
the upper side, punctured (z+(F-Q)) rail, lower side and both seam
families.  Suppose its palettes, degree caps and topology pass the preceding
theorems.  Let (G) be any Catalan forest at the same parameter and put

\[
              H(F,G)=T(F,Q,S^-,S^+)\;\sqcup\;(c+G).  \tag{5.1}
\]

The union is literal: no side or seam edge meets a (c)-rail vertex.

### Theorem 5.1 (Cartesian structural/filler completion)

If the structural data from (F) make (T(F,Q,S^-,S^+)) a linear forest
with the required non-(c) palette banks, then for every Catalan forest
(G) on the same old ground set at the same parameter (up to one fixed
coordinate relabelling):

1. (H(F,G)) has every lower and upper palette exactly once;
2. (H(F,G)) is a linear forest;
3. its component count is (\operatorname {Cat}_{n+1}); and
4. every predicate determined solely by the induced isolated (c)-rail is
   exactly the corresponding predicate of (G).

#### Proof

The translated forest (c+G) uses exactly the two banks

\[
 c+\binom{[2n]}{n-1},\qquad c+\binom{[2n]}{n+1},     \tag{5.2}
\]

which are disjoint from all three-sector palette banks.  Its physical
vertex set (c+\binom{[2n]}n) is disjoint from every other component.
Palette multiplicities, degrees, cycle ranks, component counts and trace
predicates therefore direct-sum.  The exact structural edge ledger gives

\[
 |V(T)|-|E(T)|=\operatorname {Cat}_{n+1}-\operatorname {Cat}_n, \tag{5.2a}
\]

while (G) has (\operatorname {Cat}_n) components, proving item 3.
\(\square\)

Define ({\cal S}_n) to be the set of structural tuples
((F,\omega,Q,S^-,S^+)) satisfying the strict three-sector theorem, and
let ({\cal G}_n({\cal P})) be the Catalan fillers satisfying a chosen
(c)-rail guard ({\cal P}).  The exact quantifier consequence is

\[
 \boxed{
 {\cal S}_n\ne\varnothing\ \text{ and }\
 {\cal G}_n({\cal P})\ne\varnothing
 \quad\Longrightarrow\quad
 \exists H(F,G)\text{ with the structural palettes and }c\text{-guard }{\cal P}.}
                                                               \tag{5.3}
\]

The two witnesses (F) and (G) need not coincide.  A guard involving the
(0,z,cz) sectors must still be certified on (T); Theorem 5.1 only
decouples the untouched rail.  Likewise, (5.3) does not automatically show
that the output belongs to ({\cal S}_{n+1}) or to a desired filler class.
Those are two separate right-total closure statements.

This has an exact forked-induction form.  Let (A_n) be an available,
already constructed bank of structurally eligible forests and (B_n) an
available bank of filler-eligible forests.  Let ({\cal D}_n(A_n)) be all strict structural certificates based
on members of (A_n), and define

\[
 \operatorname {Out}_n(A_n,B_n)=
 \{T_s\sqcup(c+G):s\in{\cal D}_n(A_n),\ G\in B_n\}.  \tag{5.4}
\]

### Corollary 5.2 (forked two-parent induction)

It is sufficient at every step that

\[
 A_{n+1}\cap\operatorname {Out}_n(A_n,B_n)\ne\varnothing,
 \qquad
 B_{n+1}\cap\operatorname {Out}_n(A_n,B_n)\ne\varnothing.       \tag{5.5}
\]

The two witnesses in (5.5) may be different outputs.  A one-parent
induction would require the strictly stronger triple intersection

\[
 A_{n+1}\cap B_{n+1}\cap
 \operatorname {Out}_n(A_n,B_n)\ne\varnothing.        \tag{5.6}
\]

#### Proof

The next constructor accepts an arbitrary structural parent from
(A_{n+1}) and, independently, an arbitrary filler from (B_{n+1}).
Choose the two outputs promised by (5.5) and iterate.  Requiring one output
to play both roles is exactly (5.6). \(\square\)

The reachability qualifier is load-bearing.  For a single retained ordered
pair ((F_n,G_n)), abstract nonempty intersections over larger classes do
not suffice; both next-role outputs must be reachable from that pair (or the
proof must retain the whole reachable bank used in (5.4)).

More generally, if a tag-invariant predicate (\psi) is
component-separable, then the accepted immediate fibre factors literally:

\[
 \{(s,G):\psi(T_s\sqcup(c+G))\}
 =\{s:\psi(T_s)\}\times\{G:\psi(G)\}.               \tag{5.7}
\]

Internal fixed-width residence is such a predicate.  Deep shadows and the
common compiler are not asserted to be component-separable.  Nor does
next-stage structural eligibility factor: its direct candidate graphs are
rebuilt from every output edge, including (c+G).  Finally, a finite bank
closed only under sealed filler ancestry cannot meet an unbounded residence
schedule.  With explicit indexing, an (h)-safe parameter-((n+1)) output
requires an (h)-safe structural triple and (G\in{\cal G}_n(h)).  It can
be reused as the next filler when the next requested guard is still (h);
if the guard increases to (h'>h), one needs a same-parameter member of
({\cal G}_{n+1}(h')) or a genuine rethread/promotion.  A safer structural
triple alone cannot clean the sealed copied rail.

There is one exact subface on which even next structural eligibility is
Cartesian.  For an output (H_G=T\sqcup(c+G)), call a next-step strict
certificate **filler-blind** if its deletion set (Q') and every child
edge underlying any selected direct occurrence in (S'^-\cup S'^+) belong
to (E(T)).

### Proposition 5.3 (filler-blind structural transport)

If one filler-blind next-step certificate is valid on
(H_{G_0}=T\sqcup(c+G_0)), then the identical (Q',S'^-,S'^+) is valid on
(H_G=T\sqcup(c+G)) for every Catalan filler (G) at the same parameter.

#### Proof

Every puncture and direct side occurrence used by the certificate is based
on an unchanged edge of (T).  Since (Q'\subseteq E(T)), the entire
translated (c+G) rail remains inside the next punctured central rail and
is untouched by every seam and side occurrence.  Replacing (G_0) by
(G) therefore replaces one isolated exact-palette Catalan subforest by
another and preserves all remaining palette and topology checks. \(\square\)

This robust subface has a sharp first size obstruction.  An old-parameter
(n) lift has, with (N_j=\binom{2j}{j-1}),

\[
 |E(T)|=N_{n+1}-N_n.                                  \tag{5.8}
\]

At (n=3), this is (56-15=41<\operatorname {Cat}_5=42), so a filler-blind next deletion
set cannot exist.  At (n=4), the crude count becomes
(210-56=154\ge\operatorname {Cat}_6=132); the size obstruction disappears, but the direct
palette, rooted and augmented-graphic conditions remain open.

## 6. Corrected recursive target

The strongest exact sufficient induction state isolated here is:

> **Two-parent anchored path-ear recursion.**  At parameter (n), choose
> a structural parent (F) with a favorable coherent orientation, a direct
> common (C)-set (Q), an upper rooted double-rainbow kernel plus (K)
> matching ears, and a lower double-rainbow completion independent in the
> augmented graphic matroid.  Equivalently, the lower completion may be
> supplied by a private ear bank satisfying (4.1).  Independently choose a
> filler (G) carrying the required copied-rail guard.  Require the
> non-(c) residence/deep-shadow/compiler state on the structural triple.
> Produce structural and guarded outputs for the next parameter; the two
> outputs need not be the same forest.

What is proved is the exact implication once these objects are supplied.
What remains open is their uniform supply.  In particular:

* an arbitrary fixed orientation is unsafe by Proposition 1.2; in an
  SBE-based proof the exact orientation state is the endpoint Boolean cut
  of Proposition 1.3;
* (Q) must be chosen with rooted rank by Proposition 2.3;
* two-palette correlation is necessary by the strict (n=3) coupling
  obstruction;
* private-ear Rado is sufficient but no all-(n) private ear bank is known;
* independent (G) removes fixed-(c) no-go statements, but it does not
  repair the structural triple.

The strict balanced-expansion condition from the current handoff is one
checkable sufficient source of a direct common (Q).  Its occurrence bank is
orientation-independent, and its orientation search precedes (Q) as in
Proposition 1.3.  SBE does not imply the
rooted rank (2.5), the second palette/degree intersection, or the augmented
lower row.  It therefore composes before, rather than replaces, the present
gate.

The rooted/no-empty hypothesis is deliberately stronger than bare DERF,
as (2.12) shows.  A future proof may instead carry a bounded number of empty
side components and enlarge the lower quotient state.  Nothing here rules
out that controlled-empty alternative.

For genuinely Cartesian recursion, the sharp additional lemma is now
explicit: from (n\ge4), construct and preserve a three-sector core (T)
that is pre-extendable off its filler in the sense of Proposition 5.3.
The first (n=3) transition must be exceptional by the (41<42) count.
No uniform off-filler certificate is presently known.

This is the precise proved/conditional boundary.  It is a central Catalan
forest theorem only; literal contiguous-OR equality additionally needs the
guarded residence, all-depth shadow and common compiler interfaces.

## 7. Audit ledger

The decisive finite statements are independently replayed in:

```text
scratch/catalan_direct_edgewise_n3_all_forests_20260731.audit.json
scratch/catalan_direct_edgewise_n3_two_censuses_20260731.crossaudit.json
scratch/audit_r_catalan_edgewise_orientation_and_rank_counterexamples_20260731.py
scratch/r_catalan_edgewise_orientation_and_rank_counterexamples_20260731.audit.json
scratch/audit_catalan_sbe_endpoint_orientation_independent_20260731.py
scratch/catalan_sbe_endpoint_orientation_independent_20260731.audit.json
scratch/audit_catalan_direct_upper_rooted_n3_20260731.py
scratch/catalan_direct_upper_rooted_n3_20260731.audit.json
scratch/audit_catalan_direct_n4_common_basis_upper_root_obstruction_20260731.py
scratch/catalan_direct_n4_common_basis_upper_root_obstruction_20260731.audit.json
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.audit.json
scratch/audit_catalan_direct_lower_augmented_graphic_n3_20260731.py
scratch/catalan_direct_lower_augmented_graphic_n3_20260731.audit.json
scratch/audit_catalan_independent_c_rail_filler_20260731.py
scratch/catalan_independent_c_rail_filler_20260731.audit.json
```

The all-parameter proofs used above are expanded in:

```text
MATH_THEOREM_CATALAN_DIRECT_EDGEWISE_SIDE_LIFT_RECURSION_20260731.md
MATH_THEOREM_CATALAN_DIRECT_UPPER_ROOTED_PATH_EAR_CHARACTERIZATION_20260731.md
MATH_THEOREM_CATALAN_DIRECT_LOWER_AUGMENTED_GRAPHIC_GATE_AND_N3_OBSTRUCTION_20260731.md
MATH_THEOREM_CATALAN_INDEPENDENT_C_RAIL_FILLER_20260731.md
MATH_THEOREM_CATALAN_INDEPENDENT_FILLER_GUARD_FACTORIZATION_20260731.md
MATH_THEOREM_K_DIRECT_EDGEWISE_N3_COMPLETE_CENSUS_AND_MATCHING_LOSS_RANK_20260731.md
```
