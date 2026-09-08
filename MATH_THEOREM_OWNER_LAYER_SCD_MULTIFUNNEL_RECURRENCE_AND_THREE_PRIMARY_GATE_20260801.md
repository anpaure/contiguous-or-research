# SCD multi-funnels: a common matching, an exact Catalan braid recurrence,
# and the first unavoidable cross-funnel obstructions

Date: 2026-08-01  
Lane: owner-layer rooted connectors after the four-row SCD socket theorem  
Status: exact positive common-matching construction, exact local braid and
count recurrences, and exact canonical/product/three-primary obstructions.
No all-`m` upper-exact rooted completion is claimed.

## 0. Outcome

Put

\[
 C=\operatorname {Cat}_m,
 \qquad c=\operatorname {Cat}_{m-1},
 \qquad D={2m-3\choose m-2}={m\over2}c.              \tag{0.1}
\]

The four-row SCD socket from the preceding note is not an isolated
matching accident.  This note proves the following exact facts.

1. For any fixed coordinate `x`, every perfect incidence matching between
   ranks `m-1` and `m` has exactly `c` edges which add `x`.  A product SCD
   on disjoint ordered coordinate pairs `(z_i,a_i)` makes every edge adding
   `a_i` retain `z_i`.  Hence one common perfect matching simultaneously
   contains three or four full capacity-`c` funnels.  Common-`M_0`
   compatibility itself is positive.

2. The same four-row matching contains a larger mixed-head port bank of
   order `D`: short central chains use head `zS`, while long central chains
   use head `azR`.  This bank is injective in tails, heads, matched owners
   and upper colours.  Its scalar connector shortage is at most six:

   \[
   (C-1-D)_+=1,3,6,5,0,0,\ldots
   \quad(m=3,4,5,6,\ m\ge7).                         \tag{0.2}
   \]

   This is only a port/colour shell.  It does not certify alternate upper
   providers or realize the bank as free endpoints of one upper-exact
   `Q_0`, so (0.2) is not a bounded-defect Hamilton theorem.

3. Every short central chain closes under the common matching to a
   monochromatic directed triangle.  Breaking the triangles coherently
   reduces the first genuine connector problem to a directed graph on the
   `c` short chains.  If that quotient has a Hamilton path, the lift is a
   literal local provider-plus-connector path with `c` upper representatives
   and `2c-1` colour-certified connector edges.  Conditional on preserving
   its declared free ports in the global `Q_0`, the residual connector mass is

   \[
   I_m=C-2c
      =\sum_{i=1}^{m-2}\operatorname {Cat}_i
                         \operatorname {Cat}_{m-1-i}. \tag{0.3}
   \]

   Thus the two extreme terms in the Catalan first-return recurrence are
   exactly the local SCD braid; the internal convolution (0.3) is the
   nonlocal recursive debt.

4. The standard Greene--Kleitman SCD does not supply that quotient path.
   Its only possible long ordering is strictly decreasing in coordinate
   sum and has Hall deficiency at least two for every `m>=4`.  The smallest
   literal failure is displayed at `m=4`.

5. Four disjoint full funnels cannot be block-private.  An exact union
   reserve cut forces at least `I_m-1` selected socket heads to lie in some
   other funnel's two-coordinate reserve for every `m>=7`.  Moreover the
   directed dependency relation `z->a` of a full funnel has no directed
   cycle of length at most `m`.  The missing recycling is therefore
   Catalan-scale, and every dependency graph on at most `m` funnel letters
   is acyclic.

6. The natural nested four-product has an additional sharp collision.
   Already two nested levels contain `Cat_(m-2)` disjoint forced tail
   conflicts.  Consequently the strong endpoint-disjoint four-product
   retains at most `4c-Cat_(m-2)` sockets, which is less than `C-1` for
   every `m>=22`.  This kills the canonical nested four-funnel recurrence,
   but not every nonnested correlated four-funnel construction.

7. In the cyclic quotient when `m=3r+2`, the residual order-three theorem
   forces symmetry breaking on exactly a bank indexed by `Cat_r` necklace
   sectors.  This bank is not itself a new Latin/graphic obstruction: for
   any equivariant first matching, arbitrary cells on all fixed rows have
   injective columns and symbols and form isolated directed edges.  They can
   therefore be reserved first.  What remains is a relative free-bulk
   completion avoiding their columns and symbols.  A bounded
   Skolem/three-lift patch is still impossible, but the smaller-Catalan
   state is now a positive protected reserve rather than an opaque defect.

The tight pivot can be the distinguished source once its predecessor phase,
the product/nonproduct SCD matching, and the first free outgoing socket are
chosen jointly.  This joint matching and the upper-exact endpoint
serialization remain open.  The exact theorem proved here is that the live
object is an **acyclic cross-funnel Catalan braid**, not four independent
socket lists and not `O(1)` exceptional quotient phases.

## 1. Fixed-coordinate load and simultaneous full funnels

Let `M` be any perfect matching from rank `m-1` to rank `m` of
`[2m-1]`.  Say that a matched edge **adds** `x` when

\[
                         M(B)=B+x.                    \tag{1.1}
\]

### Lemma 1.1 (coordinate-load invariant)

For every coordinate `x`, exactly `c=Cat_(m-1)` edges of `M` add `x`.

#### Proof

Every lower set containing `x` is matched to an upper set containing `x`.
The upper sets containing `x` which are not images of such lower sets are
exactly the images of edges adding `x`.  Their number is

\[
 {2m-2\choose m-1}-{2m-2\choose m-2}
 ={1\over m}{2m-2\choose m-1}
 =\operatorname {Cat}_{m-1}.                         \tag{1.2}
\]

\(\square\)

Call an ordered coordinate pair `(z,a)` **sharp for `M`** when every edge
which adds `a` has `z` in its lower endpoint.  If

\[
 B=zS,\qquad M(B)=azS,                               \tag{1.3}
\]

put `A=aS`.  Injectivity of `M` implies

\[
 M(A)=aSx,\qquad x\notin S\cup\{a,z\},              \tag{1.4}
\]

because `M(A)=azS=M(B)` is impossible.  Thus `A subset M(B)` is an
off-matching incidence and contracts to the socket

\[
                         A\longrightarrow B.          \tag{1.5}
\]

Its physical owner endpoints are `aSx,azS`, and its upper colour is
`azSx`.  Distinct `B` give distinct tails, heads, both owner endpoints and
colours: equality of two colours would make their `z`-deleted matched
owners `M(A)` equal, and hence their tails equal.

### Theorem 1.2 (simultaneous product-SCD funnels)

Let `(z_i,a_i)`, `1<=i<=t`, be disjoint ordered coordinate pairs.  On each
two-coordinate cube use the SCD

\[
 \varnothing<z_i<z_i a_i,
 \qquad a_i,                                         \tag{1.6}
\]

and take a standard product SCD with any SCD on the remaining coordinates.
The central successor matching `M` of the product SCD makes every pair
`(z_i,a_i)` sharp.  Consequently it contains `t` simultaneous full funnels,
each of exact order `c`.

In particular, three common-`M` funnels exist for `m>=4`, and four exist
for `m>=5`, including the scalar four-funnel range `m>=6`.

#### Proof

Every cover edge of a product chain changes one factor along one of its
factor chains.  The only factor-chain edge which adds `a_i` is
`z_i<z_i a_i`; hence it already contains `z_i`.  Lemma 1.1 supplies exactly
`c` such central matching edges, and (1.3)--(1.5) construct their sockets.
\(\square\)

This theorem closes only the common-perfect-matching row.  Distinct
add-coordinate funnels cannot share a head under one perfect matching, but
their unions still have tail-tail, head-tail/cross-role, upper-provider and
graphic constraints.

## 2. A larger one-funnel mixed-head bank and its exact scalar defect

Return to the four-row matching of the preceding note.  Write

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},
 \qquad |G|=2m-3,
\]

and fix an SCD of `2^G`.  Every central chain has a segment `S<L`, with
`|S|=m-2`, `|L|=m-1`.  It is either short, or it lies in a long segment

\[
                         R<S<L<U.                    \tag{2.1}
\]

The four-row matching obeys

\[
 M(aS)=aL,\qquad
 M(zS)=azS\quad\hbox{for a short chain},\qquad
 M(azR)=azS\quad\hbox{for a long chain}.             \tag{2.2}
\]

Define

\[
 H_S=\begin{cases}
       zS,&S<L\text{ short},\\
       azR,&R<S<L<U\text{ long}.
     \end{cases}                                     \tag{2.3}
\]

### Theorem 2.1 (mixed-head port bank)

For every central chain,

\[
                         aS\longrightarrow H_S       \tag{2.4}
\]

is a legal socket of upper colour `azL`.  The `D` sockets in (2.4) have
pairwise distinct tails, heads, matched head owners and upper colours.
Their two physical owner-endpoint banks are cross-disjoint.  In particular,
the socket arcs themselves are a directed matching and hence acyclic.

#### Proof

In both cases `M(H_S)=azS`, and `aS subset azS`.  Also `M(aS)=aL`, so the
upper colour is `aL union azS=azL`.  Distinct SCD chains have distinct
`S,L` and, on long chains, distinct `R`.  Short heads contain `z` but not
`a`, long heads contain both, and all tails omit `z`; this proves all
same-role and cross-bank injectivity assertions. \(\square\)

Since `D=(m/2)c`, direct Catalan arithmetic gives

\[
 C-1-D
 ={ -m^2+7m-4\over2(m+1)}c-1.                       \tag{2.5}
\]

For `m=3,4,5,6` this equals `1,3,6,5`, and it is nonpositive for every
`m>=7`.  This proves (0.2).

The qualification is essential.  A connector edge is omitted from the
upper-exact representative forest, so its upper colour must have another
selected provider.  Theorem 2.1 gives one injective occurrence of each
colour, not an alternate provider.  Moreover, after a fixed `Q_0` is
chosen, a directed-matching socket bank induces only a partial permutation
on its free components.  Rooted Hall then holds only if that partial
permutation is already the one Hamilton path from the distinguished source.
Thus the six-unit scalar shortage does not measure the upper-provider or
endpoint-serialization defect.

## 3. The monochromatic short-core triangle

For a short chain `S<L`, put

\[
 A_S=aS,\qquad B_S=zS,\qquad C_S=L.                 \tag{3.1}
\]

The four-row matching has

\[
 M(A_S)=aL,\qquad M(B_S)=azS,\qquad M(C_S)=zL.      \tag{3.2}
\]

### Theorem 3.1 (rotational triangle)

The rooted link digraph contains

\[
                 A_S\longrightarrow B_S
                 \longrightarrow C_S
                 \longrightarrow A_S,               \tag{3.3}
\]

and all three arcs have upper colour `azL`.  The `c` triangles are
vertex-disjoint over the short chains.

#### Proof

The three containments are

\[
 aS\subset azS,\qquad zS\subset zL,\qquad L\subset aL.
\]

Their colours are respectively

\[
 aL\cup azS=azL,\quad
 azS\cup zL=azL,\quad
 zL\cup aL=azL.
\]

Distinct short chains have distinct `S,L`, while the three vertices in one
triangle have different `{a,z}` signatures. \(\square\)

Identify a subfamily of rotation row `i` with its short-chain index set
`I_i`.  The exact graphic rank (equivalently, maximum acyclic size) inside
the rotational support is

\[
 |I_0|+|I_1|+|I_2|-|I_0\cap I_1\cap I_2|.           \tag{3.4}
\]

Indeed, the only cycles are the disjoint triangles whose three rows are all
present.  In particular the union of all three full rows has maximum
acyclic size `2c`.

There are three two-edge breaks:

\[
\begin{array}{c|c|c}
\text{type}&\text{path}&(\text{source},\text{terminal})\\ \hline
\alpha&A_S\to B_S\to C_S&(A_S,C_S)\\
\beta&B_S\to C_S\to A_S&(B_S,A_S)\\
\gamma&C_S\to A_S\to B_S&(C_S,B_S).
\end{array}                                         \tag{3.5}
\]

For distinct short chains `S,T`, the literal cross-block table is

\[
\begin{array}{c|ccc}
 &\alpha_T&\beta_T&\gamma_T\\ \hline
\alpha_S&0&0&0\\
\beta_S&[S\subset L_T]&0&0\\
\gamma_S&0&0&[S\subset L_T].
\end{array}                                         \tag{3.6}
\]

For example, the nonzero entries are exactly

\[
 aS\subset aL_T,\qquad zS\subset zL_T.             \tag{3.7}
\]

All omitted equality cases are same-block closures.  Thus no external arc
enters a beta block, and an alpha block can be entered only from beta.
When there are more than two blocks, any Hamilton block ordering using only
this canonical table must therefore make every block gamma.  Its quotient
is

\[
 S\longrightarrow T
 \quad\Longleftrightarrow\quad
 S\subset L_T,\quad S\ne T.                        \tag{3.8}
\]

## 4. Exact positive implication of a short-core quotient path

### Theorem 4.1 (short-core provider/connector braid)

Suppose the short chains admit an order

\[
                         S_1,S_2,\ldots,S_c           \tag{4.1}
\]

such that

\[
                         S_i\subset L_{i+1}
                         \qquad(1\le i<c).            \tag{4.2}
\]

Then the common matching contains the directed path

\[
 C_1\to A_1\to B_1\to C_2\to A_2\to B_2
       \to\cdots\to C_c\to A_c\to B_c.              \tag{4.3}
\]

Choose `C_i->A_i` as the upper representative of colour `azL_i`.  On the
displayed `3c` vertices, retain no other representative edge.  The
remaining edges of (4.3) are `2c-1` colour-certified connector edges, and
they join the `2c` local components (the `c` representative edges and the
`c` isolated `B_i`) into one directed path starting at `C_1`.  Hence the
local distinguished-source Hall cuts hold with equality.

If a global upper-exact `Q_0` extends these `c` representatives while
leaving every declared local incoming/outgoing port free, the same
`2c-1` edges are compatible global connectors.  The theorem does not
assert that such a global extension exists.

#### Proof

The internal edges are Theorem 3.1.  Condition (4.2) and (3.6) give the
cross edge `B_i->C_(i+1)`.  Its colour is

\[
 M(B_i)\cup M(C_{i+1})
 =azS_i\cup zL_{i+1}=azL_{i+1},                     \tag{4.4}
\]

because `S_i` is a rank-`(m-2)` subset of the rank-`(m-1)` set
`L_(i+1)`.  Thus every connector colour in (4.3) is represented by the
declared internal edge of its target block (or, for `A_1->B_1`, by
`C_1->A_1`).  The full support is visibly one path. \(\square\)

The Catalan recurrence now has a literal conditional connector
interpretation.  On the port-preserving global-extension face just stated,
the braid (4.3) supplies `2c-1` of the `C-1` required connector edges.  The
exact residual is

\[
 \begin{aligned}
 I_m&=(C-1)-(2c-1)=C-2c\\
    &=\sum_{i=1}^{m-2}\operatorname {Cat}_i
                         \operatorname {Cat}_{m-1-i}\\
    &={2(m-2)\over m+1}c.                            \tag{4.5}
 \end{aligned}

The first equality is topology, the second is the Catalan first-return
recurrence with its two extreme terms removed.  Any recursive completion
after (4.3) must braid this internal-convolution bank while preserving the
root `C_1` and the terminal `B_c`.

## 5. The standard SCD quotient is Hall-deficient

For the standard Greene--Kleitman SCD on `G`, the short bottoms are the
rank-`(m-2)` ballot words with one free zero.  If `x_T` is the free zero,

\[
                         L_T=T+x_T.                  \tag{5.1}
\]

Whenever `S subset L_T` is another short bottom, equal ranks give

\[
                         S=T+x_T-y                   \tag{5.2}
\]

for some `y<x_T`.  Hence the coordinate-sum potential satisfies

\[
                         \sigma(S)>\sigma(T).         \tag{5.3}
\]

The short-bottom family has only

\[
                         {m-1\choose2}+1              \tag{5.4}
\]

possible sum values, while

\[
             c>{m-1\choose2}+1\qquad(m\ge4).         \tag{5.5}
\]

Choose a repeated level `t` and put `X_t={S:sigma(S)<=t}`.  Every quotient
neighbour has sum strictly below `t`, so

\[
                         |X_t|-|N(X_t)|\ge2.          \tag{5.6}
\]

Thus the quotient (3.8) fails even unrooted one-defect Hall, and a fortiori
cannot supply (4.1).

At `m=4`, the five short bottoms and tops may be written

\[
\begin{array}{c|ccccc}
S&24&25&34&35&45\\
L&245&235&345&135&145\\
\sigma(S)&6&7&7&8&9.
\end{array}                                         \tag{5.7}
\]

For `X={24,25,34}`, every neighbour lies in `{24}`, giving deficiency at
least two.  No search is involved.

This is a no-go for the standard SCD quotient, not for a noncanonical SCD
with a Hamilton short-core quotient.

## 6. Four full funnels require Catalan-scale cross recycling

Let `P_j={z_j,a_j}`, `1<=j<=4`, be disjoint pairs.  Let `U_j` be the
rank-`m` owners containing `P_j` and `R_j` the rank-`(m-1)` lower sets
containing `P_j`.  Put

\[
                         U=\bigcup_jU_j,qquad
                         R=\bigcup_jR_j.              \tag{6.1}
\]

### Lemma 6.1 (union reserve cut)

Let `F subset U` be distinct forced matched owners with lower preimage bank
`B`.  If these rows extend to a perfect matching, then

\[
                         |F|-|B\cap R|\le |U|-|R|.    \tag{6.2}
\]

#### Proof

Every lower set in `R` must be matched into `U`.  Therefore the preimage
`M^(-1)(U)` contains `R` and has exactly `|U|-|R|` vertices outside `R`.
At most that many members of `F` can have preimages outside `R`. \(\square\)

For `t` fixed disjoint pairs, the difference between the owner and lower
intersection sizes is

\[
 \Delta_t={2t\over m}{2m-1-2t\choose m-2t}.          \tag{6.3}
\]

Here and below `binom(n,k)=0` outside `0<=k<=n`; this convention is needed
for the `t=4,m=7` term.

Hence inclusion--exclusion gives

\[
 |U|-|R|=S_4=4\Delta_1-6\Delta_2+4\Delta_3-\Delta_4,
 \qquad \Delta_1=c.                                 \tag{6.4}
\]

Direct simplification yields

\[
 2-{S_4\over c}
 ={5(m-7)(m-3)(m-2)\over
   2(2m-3)(2m-5)(2m-7)}.                            \tag{6.5}
\]

Thus `S_4<=2c` for every `m>=7`.

Consider now any compatible selection of `C-1` sockets from the four full
funnel classes.  Its head owners form `F`, and its matched lower heads form
`B`.  Lemma 6.1 forces at least

\[
 |B\cap R|\ge C-1-S_4\ge C-1-2c=I_m-1             \tag{6.6}
\]

of those heads to lie in another funnel's reserve block.  Thus the exact
internal Catalan convolution from (4.5) reappears as a cross-funnel
recycling lower bound.  Four block-private funnels cannot work.

### Lemma 6.2 (no short funnel-dependency cycle)

Draw a coordinate arc `z->a` when `(z,a)` is sharp for `M`.  This relation
has no directed cycle of length `t<=m`.

#### Proof

If `Z` is the coordinate set of such a cycle, a lower rank-`(m-1)` set
disjoint from `Z` cannot be matched by adding a member `a of Z`: sharpness
would require its predecessor `z in Z` already to be present.  Hence every
`Z`-avoiding lower set would have to map to a `Z`-avoiding upper set.  But

\[
 {2m-1-t\choose m-1}>{2m-1-t\choose m}              \tag{6.7}
\]

for `1<=t<=m`, a contradiction. \(\square\)

Equations (6.6)--(6.7) are the exact structural replacement for a cyclic
four-funnel reset: any dependency graph on at most `m` funnel letters, in
particular the scalar-minimal four-funnel graph, must be a DAG.  A larger
recursive catalogue could in principle contain a cycle longer than `m`;
the lemma does not exclude it.

## 7. The nested product is not the missing cross-funnel braid

Order two disjoint pair factors as an outer pair `(z_1,a_1)` and an inner
pair `(z_2,a_2)`, and write the remaining ground as `H`, `|H|=2m-5`.
Every short central chain

\[
                         S<L\quad\text{in }B_H       \tag{7.1}
\]

gives two outer short chains

\[
 z_2S<z_2a_2S,\qquad a_2S<a_2L.                    \tag{7.2}
\]

The inner funnel has tail and head

\[
 A_2=a_1a_2S,\qquad B_2=a_1z_2S.                   \tag{7.3}
\]

The two outer sockets in (7.2) have respective tails `B_2,A_2`.  In
particular the inner socket and the second outer socket compete for the
same lower-tail resource `A_2`.  These conflicts are disjoint over the
`Cat_(m-2)` choices of (7.1).  Therefore every endpoint-compatible
subunion of the two full banks has size at most

\[
                         2c-\operatorname {Cat}_{m-2}. \tag{7.4}
\]

For the stronger pairwise-endpoint-disjoint packet interface, the same
fixtures are `Cat_(m-2)` disjoint `K_(1,2)` stars.  Equality in (7.4) may
hold for a specified canonical product interleaving, but is not needed
below and is not asserted for every product-SCD convention.

Consequently four nested full product banks retain at most

\[
                         4c-\operatorname {Cat}_{m-2}. \tag{7.5}
\]

Already

\[
 {\operatorname {Cat}_{m-2}\over c}
 ={m\over2(2m-3)},qquad
 4c-C={6\over m+1}c.                                \tag{7.6}
\]

For every `m>=22`, (7.6) gives

\[
             4c-\operatorname {Cat}_{m-2}<C-1.       \tag{7.7}
\]

Indeed the signed ratio has numerator `m^2-23m+36`, positive from `m=22`,
and at `m=22` the strict gap already exceeds one.

Thus the natural nested four-product cannot be an all-dimensional rooted
connector construction.  The theorem is architecture-specific: a
nonnested correlated four-funnel or a larger acyclic funnel DAG is not
excluded.

For comparison, a scalar connector schedule for `m>=6` is

\[
 C=3c+r_m,\qquad
 r_m={m-5\over m+1}c,                                \tag{7.8}
\]

so nominal bank sizes `c,c,c,r_m-1` sum to `C-1`.  Equations (6.6) and
(7.7) prove that these four lists cannot simply be planted as independent
nested blocks.

## 8. The three-primary quotient exports a smaller-Catalan reserved bank

Assume `m=3r+2`.  The theorem
`MATH_THEOREM_THREE_PRIMARY_RESIDUAL_CATALAN_EXCEPTION_AND_TORSOR_RIGIDITY_20260801.md`
passes first to the maximal three-free rotation subgroup and then studies
the residual order-three action.  It proves exactly:

* the residual action fixes `Cat_r` row orbits;
* it fixes no column or symbol vertex; and
* every residual-equivariant row-saturating selector must break symmetry
  on all `Cat_r` of those sectors.

For the rest of this section put

\[
 n=2m-1=6r+3,\qquad
 s=3^{v_3(n)},\qquad
 \Gamma\le\mathbb Z_n,\quad |\Gamma|=h={n\over s},   \tag{8.0}
\]

where `Gamma` is the maximal three-free subgroup.  Let `K` be the unique
order-three coordinate subgroup and let
`R=\mathbb Z_n/\Gamma` be the residual group.

### Corollary 8.1 (no bounded-exception funnel quotient)

Assume the funnel construction is realized through a `Gamma`-equivariant
first matching and a residual-equivariant clean quotient bulk.  No such
selector can finish that bulk by an `O(1)` family of three-lifts, complete
mappings, Skolem patches or local phase exceptions.  At least

\[
                         \operatorname {Cat}_{(m-2)/3} \tag{8.1}
\]

quotient sectors must carry non-equivariant choices.

This lower bound concerns integral row/column/symbol/graphic correlation,
not raw socket count.  It therefore coexists with the six-unit scalar shell
bound (0.2): a port bank may have enough edges while its endpoint and upper
provider selector still needs exponentially many correlated phase choices.

The exceptional sectors are canonically indexed by

\[
 {\binom{\mathbb Z_{2r+1}}r}\big/\mathbb Z_{2r+1},   \tag{8.2}
\]

which has `Cat_r` members.  The next theorem shows that this required
symmetry break has an unexpectedly clean physical form.

A `K`-fixed row has the form

\[
 C=\bigcup_{j=1}^r T_j,                              \tag{8.3}
\]

where the `T_j` are complete `K`-orbits of size three.  Fix any equivariant
perfect matching `mu`, choose an arbitrary containing column

\[
                         B=C+b,                       \tag{8.4}
\]

and put

\[
                         A=C+\alpha(B).               \tag{8.5}
\]

### Theorem 8.2 (fixed-row isolated Latin forest)

Choose an arbitrary cell (8.4) for every `K`-fixed row, compatibly on each
`Gamma`-orbit.  Then:

1. all selected columns `B` are distinct;
2. all selected symbols `A` are distinct;
3. no selected column equals any selected symbol; and
4. the directed cell graph `B->A` is a matching, hence an isolated-edge
   forest.

The same assertions hold in the clean quotient and after lifting the
chosen quotient cells.

#### Proof

For any rank-`(3r+1)` set of the form `C+b`, its union of complete
order-three coordinate orbits is exactly `C`: all of `C` is a union of
full triples, while the added point contributes only one member of a new
triple.  Thus `B` uniquely recovers its full-triple core `C`.

The symbol `A=C+alpha(B)` has the same form, since `alpha(B)` is one point
outside `B` and hence outside `C`; it too uniquely recovers `C`.  Equality
of two columns, two symbols, or a column and a symbol therefore forces the
underlying fixed rows to agree.  On one row, `B=A` would give
`b=alpha(B)`, impossible because `b in B` while `alpha(B) notin B`.
This proves the physical assertions and shows that development on distinct
`Gamma` row orbits creates no collision.

It remains to exclude a quotient tail--symbol collision inside one row
orbit.  Such a collision would give

\[
                         B_C+g=A_C                   \tag{8.6}
\]

for some `g in Gamma`, and core recovery would give `C+g=C`.  The
stabilizer of `C` has order exactly three: it contains `K`, while its order
divides

\[
             \gcd(6r+3,3r)=3.                       \tag{8.7}
\]

Hence `Stab(C)=K`.  Since `Gamma` is three-free,
`\Gamma\cap K=\{0\}`, so `g=0`; (8.6) reduces to the already
excluded equality `B_C=A_C`.  This proves the quotient and lifted
assertions. \(\square\)

There are `binom(2r+1,r)=(2r+1)Cat_r` physical fixed rows,
`(s/3)Cat_r` fixed row vertices in the clean quotient, and exactly `Cat_r`
residual rotation sectors controlling their phase choices.  Theorem 8.2
allows all of them to be contracted as a protected isolated-edge bank.
Each edge exports its column `B` as a literal free incoming port and its
symbol `A` as a literal free outgoing port, so it is already in the right
form for the later cross-funnel connector braid.

### Corollary 8.3 (relative free-bulk reduction)

Put `V_fix=B_fix union A_fix`, where `B_fix,A_fix` are the reserved column
and symbol vertices.  Delete the fixed rows, and forbid every vertex of
`V_fix` in **both** residual roles.  If the remaining free quotient rows
admit a row-saturating selection with injective residual columns and
symbols whose directed graph is a forest, then its union with the reserved
fixed-row bank is a complete Latin forest.

#### Proof

The residual selection avoids every vertex of the reserved directed
matching.  The two forests are therefore vertex-disjoint; their union is a
forest and all row, column and symbol requirements are exact. \(\square\)

Thus, on the clean cyclic route, the proof-safe recursive target is sharper
than a generic smaller-Catalan absorber: reserve the canonical
`Cat_r`-sector isolated bank first, then solve one **relative free-bulk
Latin forest** around it.  Its isolated edges export literal ports for the
later connector problem, but no theorem here couples those ports to the
cross-funnel mass `I_m`.  The bank size is not `O(1)`, while its local
matching and graphic rows are automatic.

## 9. Rooted tight-pivot interface and exact remaining theorem

Let `Q_0` be upper-exact with components `K_1,...,K_C`, and let `K_1`
contain the protected tight-pivot successor path beginning at its literal
free incoming root `L_0`.  Let

\[
                         e_i:t_i\longrightarrow h_i
                         \qquad(1\le i<C)             \tag{9.1}
\]

be endpoint-compatible funnel sockets.  If

\[
 s(K_1)=L_0,\qquad
 o(K_i)=t_i,\qquad s(K_{i+1})=h_i,                  \tag{9.2}
\]

then the `e_i` are literally the consecutive arcs of a Hamilton component
path starting at `K_1`.  They are acyclic and satisfy distinguished-source
Hall after deleting the incoming copy of `K_1`.  This implication is exact
and needs no further matching theorem.

The hypotheses (9.2), not the implication, are open.  The product-SCD
theorem chooses a common matching for four funnel relations, but does not
make that matching contain the complete tight-pivot predecessor phase.
The socket theorems choose legal endpoint pairs, but do not realize them as
the free boundaries of one upper-exact `Q_0`, nor do they supply all
alternate upper providers.  The small protected matching theorem may choose
some extension of the pivot phase; it does not preserve the product-SCD
relations.

More explicitly, a joint protected extension must satisfy all of the
following literal rows.

1. The product/nonproduct `M_0` contains every predecessor incidence
   `P_0`; only then does the successor shore contract to the protected path
   `P_1`.
2. `Q_0` retains `P_1` as the designated providers of its distinct pivot
   colours, and forbids every unprotected provider entering `L_0`, so
   `s(K_1)=L_0` literally.
3. Funnel ports avoid every incidence port consumed by `P_1`, except for
   one deliberately declared attachment at the pivot terminal.  The first
   braid socket normally leaves that terminal component and enters the
   local source `C_1`; identifying `L_0=C_1` would instead consume the
   outgoing tail already used by the first pivot edge.
4. If a pivot upper colour equals some `azL_i`, exactly one of the pivot or
   SCD occurrences is the `Q_0` provider and the local component ledger is
   recomputed; two representatives of one colour are not allowed.
5. Every other upper representative avoids all incoming and outgoing ports
   reserved by the connector braid.  If a global terminal is prescribed,
   its outgoing port is reserved dually.

The protected small-matching extension and the product-SCD theorem solve
these rows only as separate marginals.

The exact all-`m` missing theorem can therefore be stated without scalar
ambiguity:

> Construct jointly a perfect `M_0` containing the tight-pivot predecessor
> phase, an upper-exact `Q_0` with the pivot component as distinguished
> source, and an acyclic cross-funnel braid on its free endpoints.  The
> braid must service the internal Catalan mass `I_m` and obey the short
> coordinate-dependency-cycle cut.  If it uses the clean
> `Gamma`-equivariant
> quotient when `m=3r+2`, it must also reserve the `Cat_r` correlated
> necklace sectors of Theorem 8.2.

The standard GK quotient, four block-private lists, a four-funnel cyclic
reset, the nested four-product, and bounded-exception repairs inside the
clean residual-equivariant quotient are all closed by the theorems above.
An arbitrarily symmetry-broken multi-funnel is not subject to the
three-primary lower bound.  A noncanonical Hamilton short-core quotient
plus a smaller-Catalan relative cross-funnel construction remains live.
Residence, deeper shadows and the common compiler cap are still outside
this owner-layer theorem.
