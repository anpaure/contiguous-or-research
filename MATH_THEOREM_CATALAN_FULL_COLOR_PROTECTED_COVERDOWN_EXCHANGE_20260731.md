# Full-colour protected cover-down: exact exchange normal form, unit ears, and sharp slot obstructions

Date: 2026-07-31  
Status: exact fixed-host equivalence and exact serialization theorem; literal
Boolean obstruction at parameter three; algebraic abstract obstruction to
deducing an exact forest from a full conflict-free colouring.  No large-
parameter Boolean cover-down theorem is claimed.

## 0. Verdict

Fix an admissible common deletion bank `Q` and its four-uniform capacity-slot
hypergraph `G_Q`.  The full Delcourt--Postle colouring is useful as a
distributed candidate reservoir, but the colouring itself adds no exact
augmentability.  For a current matching `M`, every protected completion is
controlled by the single gain functional

\[
 g_M(S)=|S|-|N_M(S)|,
\tag{0.1}
\]

where `S` is an outside matching and `N_M(S)` is its complete conflict
neighbourhood in `M`.  Let `F_fix` be the frozen central/seam scaffold,
with its incidences already deducted from the available slots.  If
`F_fix union phi(M-N_M(S))` is a forest, the remaining physical condition
is exactly one graphic contraction row for the projected edges of `S`.

This yields a zero-defect equivalence, not an existence theorem.  Two
sharp obstructions explain the boundary.

1. In the authenticated literal `n=3` fixed-`Q` Boolean host, four residual
   upper targets require eight endpoint-slot incidences in a bank of total
   capacity seven.  Thus no exact matching exists, before topology or a
   downstream compiler is considered.  No colouring or alternating packet
   can cross this cut.
2. For every fixed cycle cutoff `L`, there are arbitrarily large regular
   four-resource slot hosts with `Delta_2<=2` and an *optimal* `Delta`-
   colouring whose every colour class is a matching projecting to one cycle
   longer than `L`, while no exact matching projects to a forest.  This is
   an abstract slot construction, not a Boolean containment counterexample;
   it proves that the full-colouring axioms alone cannot close coefficient
   one.

The positive surviving target is therefore a Boolean-specific theorem
which forces enough protected unit ears, or an equivalent multi-colour
packet satisfying (0.1) and the graphic row.  Repeating the largest single
colour class cannot supply that correlation.

## 1. Fixed-host notation

Let `G=G_Q` have resource vertices

\[
       \mathcal D\sqcup\mathcal V\sqcup\mathcal S,
       \qquad |\mathcal D|=|\mathcal V|=P.
\tag{1.1}
\]

An atom contains one punctured lower colour `D`, one upper colour `V`, and
one slot at each of its two physical owners.  Ordinary owners have two
slots and seam anchors have one.  Let

\[
                  \phi:E(G)\longrightarrow {X\choose2}
\tag{1.2}
\]

be physical projection, forgetting slot indices.  In the Boolean host the
owner pair determines its intersection and union, so a host matching has
no projected parallel pair.  In the abstract statements below, parallel
pairs are retained and count as a two-cycle.

For a matching `M` and an outside set `S`, define

\[
 N_M(S)=\{e\in M:\ e\cap s\ne\varnothing
                    \text{ for some }s\in S\}.
\tag{1.3}
\]

The canonical toggle is

\[
                    M\star S=(M\setminus N_M(S))\cup S.
\tag{1.4}
\]

When `S` is a matching, (1.4) is a matching.  Conversely every old atom
which can coexist with `S` is retained by (1.4).

A set `Z subseteq M` is **protected** when its atoms must survive.  This is
equivalent to

\[
                         N_M(S)\cap Z=\varnothing.
\tag{1.5}
\]

The inherited seam itself is already protected by the host definition:
an anchor has only its one residual side slot.  Condition (1.5) is for
additional literal side atoms, root atoms, or declared sockets which may
not be replaced.

Let `F_fix` denote any further protected physical scaffold already present,
including retained child fragments and seam edges.  Its incidences are
charged before the residual slots of `G_Q` are created.  Physical forest
tests below are made on `F_fix union phi(M)`, not merely on the isolated
side row.

## 2. Exact protected gain theorem

### Theorem 2.1 (protected matching gain)

For any finite hypergraph `G`, matching `M`, and protected bank
`Z subseteq M`, the maximum size of a matching containing `Z` is

\[
 |M|+\max\left\{
 |S|-|N_M(S)|:\begin{array}{l}
 S\subseteq E(G)\setminus M\text{ is a matching},\\
 N_M(S)\cap Z=\varnothing
 \end{array}\right\}.
\tag{2.1}
\]

#### Proof

Every admissible `S` gives the matching (1.4), contains `Z`, and has the
displayed size.  Conversely let `T` be any matching containing `Z` and put
`S=T-M`.  Every member of `N_M(S)` is absent from `T`, so

\[
 |T|=|T\cap M|+|S|
 \le |M|-|N_M(S)|+|S|.
\]

Also `N_M(S)` misses `Z`.  Taking maxima proves equality. `square`

For `G_Q`, no matching has more than `P` atoms because every atom uses one
member of the `P`-set `mathcal D`.  A `P`-matching automatically saturates
both `mathcal D` and `mathcal V`.

### Theorem 2.2 (exact protected forest cover-down)

Assume `F_fix union phi(M)` is a forest and put `h=P-|M|`.  There is a
`P`-atom matching `T` containing `Z` for which
`F_fix union phi(T)` is a capped linear forest if and only if there is an
outside matching `S` such that

\[
 N_M(S)\cap Z=\varnothing,
 \qquad |S|-|N_M(S)|=h,                              \tag{2.2}
\]

and, with

\[
 F_0=F_{\rm fix}\cup\phi(M\setminus N_M(S)),         \tag{2.3}
\]

the multigraph formed by `phi(S)` after contracting every component of
`F_0` is loopless and acyclic.  Equivalently, its edges are independent in
the quotient graphic matroid.

Whenever these conditions hold,

\[
                     T=M\star S.                     \tag{2.4}
\]

#### Proof

For sufficiency, (1.4) is a matching containing `Z`, and (2.2) gives size
`P`.  Residual-slot disjointness gives total ordinary physical degree at
most two and anchor degree at most one after `F_fix` is restored.  Adding
edges to the forest `F_0` produces a forest exactly under the loopless
quotient-forest test.  Hence (2.4), together with `F_fix`, is a capped
linear forest.

For necessity, take an exact terminal `T` and put `S=T-M`.  Then
`N_M(S) subseteq M-T`.  If this containment were strict, `M star S` would
be a matching of size strictly greater than `|T|=P`, impossible.  Therefore

\[
                         N_M(S)=M-T.                  \tag{2.5}
\]

Equations (2.2)--(2.4) follow, and contracting the common subforest
`F_fix union phi(M cap T)` gives the graphic condition. `square`

If the rooted/no-empty row is required, adjoin the prescribed root-star
edges and replace the last condition by the corresponding spanning-tree
test.  This does not change the matching gain formula.

## 3. What the full colouring adds

Let

\[
                     E(G)=C_1\sqcup\cdots\sqcup C_t
\tag{3.1}
\]

be any proper conflict-free colouring; every `C_j` is a host matching and
its projection avoids the declared short cycles.  Theorem 2.2 becomes
exactly the same maximization after writing

\[
                 S=S_1\sqcup\cdots\sqcup S_t,
                 \qquad S_j\subseteq C_j,             \tag{3.2}
\]

with the load-bearing condition that the **union** in (3.2) is a matching.
The colouring makes every within-class conflict disappear.  It gives no
control of cross-class conflicts, gain, the quotient graphic rank, or a
downstream compiler relation.

For one class, the best gain is a bipartite Hall deficiency.  Delete the
members of `C_j` conflicting with `Z`, make the bipartite conflict graph
between the surviving class and `M-Z`, and call its maximum-matching size
`nu_j`.  Then

\[
 \max_{A\subseteq C_j}(|A|-|N_M(A)|)=|C_j^{Z}|-\nu_j.
\tag{3.3}
\]

These one-colour gains do **not** add.  The smallest slot pattern already
has one old atom `r` and two mutually disjoint new atoms `x,y` of different
colours, where `x` and `y` conflict with `r` through its two different
slots.  Each singleton colour has gain zero, whereas

\[
                  |\{x,y\}|-|N_M(\{x,y\})|=2-1=1.
\tag{3.4}
\]

Thus the full-colour route is genuinely a correlated multi-colour
augmentation, not a sum or repetition of single-colour `P-o(P)` results.

## 4. Minimal unit ears and exact serialization

Call an outside matching `S` a **minimal augmenting ear** if

\[
 g_M(S)>0,
 \qquad g_M(A)\le0\quad(\varnothing\ne A\subsetneq S).
\tag{4.1}
\]

Protection is imposed by requiring `N_M(S) cap Z=emptyset`.

### Lemma 4.1 (every minimal ear has unit gain)

For a minimal augmenting ear,

\[
                       |S|=|N_M(S)|+1.                \tag{4.2}
\]

Moreover, in the bipartite conflict graph between
`S` and `R=N_M(S)`, there is a matching saturating `R`.

#### Proof

Put `g=|S|-|R|`.  For any `s in S`,

\[
 g_M(S-s)=|S|-1-|N_M(S-s)|\ge g-1.
\]

Minimality makes the left side nonpositive, so `g=1`.

For Hall on `R`, suppose some nonempty `X subseteq R` has
`|N_S(X)|<|X|`.  Because every member of `R` meets `S`, `N_S(X)` is
nonempty.  Put `A=S-N_S(X)`.  Then `A` is a proper nonempty subset,
`N_M(A) subseteq R-X`, and

\[
 |A|=|S|-|N_S(X)|>|R|+1-|X|=|R-X|+1.
\]

Hence `g_M(A)>0`, contradicting minimality.  Hall gives a matching
saturating `R`. `square`

Choose such a matching and write it as an injection

\[
                      \mu:R\longrightarrow S,         \tag{4.3}
\]

where `r` conflicts with `mu(r)`.  There is one unmatched root
`s_infty in S`.  Make a dependency digraph on `S`: for every conflict
`r--s`, put

\[
                         \mu(r)\longrightarrow s,     \tag{4.4}
\]

and ignore loops.

### Theorem 4.2 (SCC ear/circuit serialization)

Process the strongly connected components of (4.4) in topological order.
For a nonroot component `K`, first remove all old atoms

\[
                         \mu^{-1}(K)                  \tag{4.5}
\]

and then add all new atoms of `K`.  Finish by adding the singleton root
`s_infty`.  Every displayed state is a matching, no protected atom is
removed, and the final state is `M star S`.  Every nonroot block is
balanced; the final root supplies the unique gain.  The maximum temporary
matching deficit is the maximum size of a nonroot SCC.

If every SCC is a singleton, the ear is a sequence of one-for-one exchanges
followed by one insertion.  A nontrivial SCC is the exact irreducible
dependency block.  It need not be a simple palette-alternating circuit:
that stronger name is justified only when its signed outer-colour boundary
also vanishes.

#### Proof

The root has no outgoing arc because it is outside the image of `mu`, so
it is a singleton sink.  Consider a nonroot SCC `K`.  An old atom not yet
removed whose mate lies in a later component cannot conflict with a member
of `K`, for that would give an arc from the later component into `K`,
contradicting topological order.  Old atoms belonging to earlier components
are already absent, and the atoms (4.5) are removed before `K` is added.
The new atoms are mutually disjoint because `S` is a matching.  Thus every
step is valid.  Each nonroot block removes and adds `|K|` atoms; the root
adds one. `square`

There are two distinct notions of serialization.

* **Forest-safe with temporary palette holes.**  Delete all of `R`, then
  add the members of `S` in any order.  If the terminal quotient row in
  Theorem 2.2 passes, every prefix is a forest because graphic independence
  is hereditary.
* **Palette-transparent packet serialization.**  For a block `K`, define
  its signed outer boundary

  \[
   \partial_{D,V}(K)=
      \mathbf1_{D,V}(K)-\mathbf1_{D,V}(\mu^{-1}(K)). \tag{4.6}
  \]

  A balanced SCC preserves every currently covered lower colour and upper
  cap exactly when (4.6) is zero.  A unit ear is monotone cover-down exactly
  when its total boundary is `+1` on one previously missing lower colour
  and one previously missing upper cap and zero elsewhere.  Graphic
  transparency of the SCC order is the separate requirement that every
  SCC prefix pass Theorem 2.2's contraction row.

The existing private-ear/Rado theorem is a sufficient way to force the
last condition: quarantine the off fragments, give different ears private
resources and ports, and require their suppressed links to be independent
in one fixed quotient graphic matroid.  The full colouring does not create
that privacy.

## 5. Local common caps versus the downstream compiler

The word **cap** has two different uses which must not be conflated.

1. In `G_Q`, the upper resource `V` is the local two-step common cap of
   its diamond.  A `P`-matching saturates every `V`, so it automatically
   gives a bijection `pi:mathcal D to mathcal V`.  If its physical graph is
   a linear forest, orienting the paths gives the two injective intermediate
   maps.  Thus Theorem 2.2 already includes the exact local common-cap row.
2. A preassigned SCD cap map, maximal-envelope assignment, or later word
   compiler is not encoded by the Delcourt--Postle colouring.  A fixed cap
   map may be imposed by restricting the host to its compatible atoms
   before applying Theorem 2.2.  If the compiler is chosen after the side
   forest, its literal Hall/common-cap recourse remains an additional final
   condition.

No statement here promotes local `V`-saturation to the downstream compiler.

## 6. Literal Boolean obstruction at `n=3`

Use the authenticated child forest and common basis in

```text
MATH_THEOREM_R_TWO_COORDINATE_SIDE_TURN_FOREST_AND_CAPACITY_CUT_20260731.md.
```

On the upper shore,

```text
D = {07,0b,0d,0e,13,23},
B = binom([6],4) minus {0f}.
```

Targets `3d` and `3e` force `0d` and `0e`.  The four residual targets are

```text
W={1f,2f,37,3b}.
```

Every residual candidate has both physical endpoints in

```text
S={0f,17,1b,27,2b,33}.
```

Only `0f` is not an anchor.  Hence the residual slot capacity is

\[
                         2+5=7,                      \tag{6.1}
\]

whereas four diamonds require

\[
                         2|W|=8.                     \tag{6.2}
\]

The opposite shore has an incidence-perfect matching, so this is a literal
two-sided common basis whose one upper fixed-`Q` host has no `P`-matching.
It follows immediately that no protected exchange, no collection of colour
classes, and no all-at-once circuit packet can give zero defect for this
`Q`.

This refutes an all-parameter **arbitrary-`Q`** cover-down statement.  It
does not refute selecting another common basis for the same child, and it
does not prove that a corresponding cut exists for all sufficiently large
Boolean parameters.

## 7. An optimal full-colouring obstruction

The previous obstruction is Boolean but finite.  The next construction is
dimension-scalable and isolates the logical weakness of the colouring
input itself.

Fix a prime `p>max{L,3}`.  Take four resource parts

\[
 D=\{d_i\},\quad V=\{v_i\},\quad
 S_0=\{x_i^0\},\quad S_1=\{x_i^1\},
 \qquad i\in\mathbb Z_p,                             \tag{7.1}
\]

where `x_i^0,x_i^1` are the two slots of one physical owner `x_i`.  Put

\[
 f(c)=\begin{cases}c+1,&c\ne-1,\\1,&c=-1,
 \end{cases}                                         \tag{7.2}
\]

and for `c,i in Z_p` include the atom

\[
 e_{c,i}=\{d_i,\ v_{i+c},\ x^0_{i+2c},\
                    x^1_{i+2c+f(c)}\}.               \tag{7.3}
\]

### Theorem 7.1 (tight-slot full-colour obstruction)

The host (7.3) has all of the following properties.

1. It is `p`-regular and has maximum pair codegree at most two.
2. Colouring `e_(c,i)` by `c` is a proper edge-colouring with exactly
   `p=Delta` colours.  Every colour class has `p` atoms and saturates both
   `D` and `V`.
3. The physical projection of colour `c` is the single `p`-cycle

   \[
                   \{x_jx_{j+f(c)}:j\in\mathbb Z_p\}, \tag{7.4}
   \]

   so every class avoids projected cycles of lengths `3,...,L`.
4. No `p`-atom host matching has a forest projection.

#### Proof

For fixed `c`, each coordinate in (7.3) is a translate of `i`, so the
colour class is a matching.  Every resource occurs once for every `c`,
giving degree `p`.  A cross-part resource pair determines `c` uniquely,
except for the single repeated value introduced by (7.2), so every pair
codegree is at most two.  More explicitly, the six pair equations reduce
to one of

\[
 c,\quad2c,\quad 2c+f(c),\quad c,\quad c+f(c),\quad f(c),
\]

and each displayed map has fibres of order at most two.

The value `f(c)` is nonzero.  Since `p` is prime, translation by `f(c)` is
one `p`-cycle, proving (7.4).

Finally, a `p`-atom matching uses `2p` distinct slot vertices.  There are
exactly `2p` slots, so it uses every slot.  Every physical owner therefore
has degree exactly two.  A nonempty finite two-regular multigraph contains
a cycle (a parallel pair counts as a two-cycle), hence cannot be a forest.
`square`

This example is stronger than a poor largest-colour estimate: the colouring
is optimal, every class already has the target cardinality and exact local
common caps, and all declared short cycles are absent.  Its obstruction is
the tight graphic cut `p` edges on `p` physical owners.

The construction is not asserted to embed in a Boolean `G_Q`.  It proves
that a positive large-`n` Boolean theorem must use additional containment
geometry or a cut-expanding protected-ear hypothesis; it cannot be a formal
corollary of the full conflict-free colouring and its degree/codegree data.

## 8. Exact surviving all-parameter target

For a fixed Boolean host, Theorem 2.2 is the weakest exact endpoint.  A
positive cover-down theorem may be stated in either equivalent language.

* Find a multi-colour outside matching `S` of gain exactly `P-|M|` whose
  protected quotient projection is graphic-independent.
* Export enough minimal unit ears from Section 4, with zero-boundary
  balanced SCCs, distinct missing-colour roots, and a private/Rado link
  system which makes their physical blocks serializable.

The first is exact but globally correlated.  The second is a stronger
constructive certificate.  Neither is supplied by the colouring theorem.
The literal `n=3` cut says the first can be empty for an arbitrary common
basis; Theorem 7.1 says no proof using only the abstract colouring rows can
exclude that outcome asymptotically.

## 9. Audits and scope locks

The literal Boolean cut is independently replayed by

```text
scratch/audit_catalan_a1_side_turn_capacity_cut_20260731.py
scratch/catalan_a1_side_turn_capacity_cut_20260731.audit.json
```

with hashes

```text
MATH_THEOREM_R_TWO_COORDINATE_SIDE_TURN_FOREST_AND_CAPACITY_CUT_20260731.md
  74dd8c45844e249f94d879469a78538dfee4b1b0b4582ea6d701c20e4cd6fe7a
scratch/audit_catalan_a1_side_turn_capacity_cut_20260731.py
  ddcad2ee21ff83d939274a79e46fc3b125977ceef119cd1219f01fe14a392ec4
scratch/catalan_a1_side_turn_capacity_cut_20260731.audit.json
  398cfbecaabec84a982dc81015a56af841b456da3838417c32cc46068f33430f
payload
  3f2ecae3c78afdd514d88fafdce8bf5dc68ccf7edaf7d9245c18daa226ecb934
```

The algebraic full-colour construction is replayed for primes
`5,7,11,...,43` by

```text
scratch/audit_catalan_full_color_protected_coverdown_exchange_20260731.py
scratch/catalan_full_color_protected_coverdown_exchange_20260731.audit.json.
```

Their hashes and retained payload are

```text
scratch/audit_catalan_full_color_protected_coverdown_exchange_20260731.py
  354f465f23015eaedf838497bb851e08818878e80ba682c7db563106263193ce
scratch/catalan_full_color_protected_coverdown_exchange_20260731.audit.json
  b57649ff49f9ca2d3de9b8b1ddf9512080c003bec900220fb5f9d6e31caf735e
payload
  c24697be51c30934f7bd7e58ac3a33365893f12b0f6e507702e31425019be1b5
```

The finite audit checks all atom incidences, degrees, pair codegrees,
colour matchings, and projected cycle connectivity.  The all-prime claims
are proved symbolically in Theorem 7.1; the finite census is calibration,
not the source of the universal quantifier.

Nothing in this note proves a large-parameter Boolean cover-down, a rooted
no-empty shore, two-shore attachment compatibility, residence/deep-shadow
rows, the downstream common-cap compiler, or `nu=B`.
