# Protected Delcourt--Postle reserves and the nonzero-boundary cover-down gate

Date: 2026-07-31  
Status: exact reserve-stability theorem, exact affine slot normalization,
exact structured absorber-bank bound, a dimension-uniform nonzero-boundary
`2 -> 3` actuator, and a sharp smallest edge-alignment obstruction.  This
does **not** prove exact cover-down, a perfect AGCF, or `nu=B`.

## 0. Verdict

The all-candidate AGCF absorber theorem (`2292AG`) and the arbitrary-`Q`
Delcourt--Postle side-forest theorem (`2295ROOT`) have one rigorous positive
composition:

> any closed protected reserve of `o(P)` host resources may be fixed first,
> and the Delcourt--Postle construction still supplies a `P-o(P)` physical
> linear forest outside it, uniformly for every admissible common basis `Q`.

This allows a structured absorber/anchor bank and the unavoidable unused-slot
baseline to coexist with the asymptotic side body.  It does **not** align the
last leave.  Three exact extra rows remain:

1. the capacity-slot leave is affine, with a forced unused-slot baseline;
2. after the baseline is removed, the residual must lie in the **positive
   matching semigroup** of the reserved packet boundaries, not merely in the
   AGCF flux lattice; and
3. the physical completion ears must be independent in the graphic matroid
   contracted by the retained forest.

The second row is genuinely nontrivial.  At `n=3` there is an actual AGCF
matching of size `Cat_3-1` whose leave has every exact flux and divisibility
row but contains no candidate.  Balanced `2 <-> 2` switches cannot change
that leave.  The witness is nevertheless repaired by an explicit `2 -> 3`
packet, and the packet suspends to every `n>=3`.  Thus the missing theorem is
a nonzero-boundary augmenting cover-down, not another local balanced
absorber or another marginal near-matching theorem.

## 1. The two hosts must not be identified

Let `H_n` be the `(3n+1)`-uniform AGCF resource hypergraph.  Its three
resource shores are

\[
 {\cal M}=\binom{[2n]}n,\qquad
 {\cal L}=\binom{[2n]}{n-1},\qquad
 {\cal U}=\binom{[2n]}{n+1}.
\]

An edge is a whole complement geodesic and consumes `n+1,n,n` resources on
these shores.

For a fixed admissible common basis `Q`, let `G_Q` be the four-uniform
capacity-slot hypergraph of `2295ROOT`.  Its atom consumes

\[
  \{\hbox{one punctured lower outer colour},
    \hbox{one upper outer colour},
    \hbox{two physical-owner slots}\}.                 \tag{1.1}
\]

These are different incidence systems.  No incidence-preserving map from an
arbitrary AGCF path edge to a legal fixed-`Q` side packet has been proved.
Accordingly, the results below compose them only through a stated protected
packet realization; no AGCF path is silently treated as a `G_Q` atom.

Use the side notation

\[
 N=\binom{2n}{n-1},\quad P=\binom{2n}{n-2},\quad
 K=\operatorname {Cat}_n,\quad C=\operatorname {Cat}_{n+1},
\]

and

\[
 D_0=2(n+1)(n+2).
\]

For every `Q`,

\[
 |E(G_Q)|\ge4P\binom n2-2C(n^2-1),\qquad
 \Delta(G_Q)\le D_0,\qquad \Delta_2(G_Q)\le2(n+1).   \tag{1.2}
\]

## 2. Delcourt--Postle is stable under a protected reserve

For a set `Z` of host vertices of `G_Q`, write `G_Q-Z` for the induced
subhypergraph obtained by forbidding every atom meeting `Z`.

### Theorem 2.1 (uniform protected-reserve theorem)

Fix a cycle cutoff `L>=3` and, in the Delcourt--Postle hypotheses, fix
`beta=1/4`.  There is
`alpha=alpha(L)>0` such that, for every sufficiently large `n`, every
admissible `Q`, and every host-vertex set `Z`, the hypergraph `G_Q-Z`
contains a matching whose physical projection has no simple cycle of length
at most `L` and whose size is at least

\[
 P-O\!\left({P\over n}+P D_0^{-\alpha}+|Z|\right).     \tag{2.1}
\]

After deleting one atom from every remaining physical cycle, it contains a
physical linear forest of size

\[
 P-O\!\left({P\over n}+P D_0^{-\alpha}+|Z|+{P\over L}\right). \tag{2.2}
\]

All constants for fixed `L` are independent of `Q` and `Z`.  Consequently,
if `|Z|=o(P)`, a sufficiently slow diagonal choice `L=L(n)->infinity`
gives a `P-o(P)` physical forest avoiding `Z`.

#### Proof

Deleting `Z` removes at most

\[
                  \sum_{z\in Z}d_{G_Q}(z)\le D_0|Z|            \tag{2.3}
\]

atoms.  It cannot increase maximum degrees, pair-codegrees, short-cycle
configuration degrees, or their mixed codegrees.  Thus the same
Delcourt--Postle coloring theorem used in `2295ROOT` applies to `G_Q-Z`
with `alpha=alpha(L,1/4)` and at most
`D_0(1+D_0^{-\alpha})` colors.  Its largest color class has
size at least

\[
 { |E(G_Q)|-D_0|Z| \over D_0(1+D_0^{-\alpha})}.        \tag{2.4}
\]

The exact ratio calculation in `2295ROOT` gives

\[
 { |E(G_Q)|\over D_0}
 \ge P\left(1-{8\over n}+O(n^{-2})\right).             \tag{2.5}
\]

Equations (2.4)--(2.5) prove (2.1).  The selected physical graph is simple,
has maximum degree two, and has no cycle of length at most `L`.  Its
remaining cycles are edge-disjoint and each has at least `L+1` edges, so
deleting one atom per cycle costs at most `P/(L+1)`.  This proves (2.2).
`square`

### Corollary 2.2 (preloaded anchor forest)

Let `B` be any already chosen host matching whose physical projection is a
forest.  Form its **closed support** `cl(B)` from

* its two outer resources per atom; and
* every capacity slot at every physical owner used by an atom of `B`.

Then `|cl(B)|<=6|B|`.  Applying Theorem 2.1 with `Z=cl(B)` and adjoining
`B` afterwards produces a physical forest containing `B` and having size

\[
 P-O\!\left({P\over n}+P D_0^{-\alpha}+|B|+{P\over L}\right)    \tag{2.6}
\]

whenever `|B|=o(P)`.  In particular all cap-one seam anchors already used
by `B` remain protected.

#### Proof

An atom has two outer resources and two physical owners; each owner has at
most two slots.  Hence the size bound.  A matching in `G_Q-cl(B)` shares no
outer resource with `B` and touches no physical owner of `B`.  The two
physical forests are therefore vertex-disjoint, so their union is a
forest.  The size claim follows from Theorem 2.1. `square`

This is deliberately a strong isolation condition.  Allowing future ears
to attach to `B` requires the graphic condition in Section 6.

### Corollary 2.3 (resource reserves versus atom bans)

Let `R` be any additionally forbidden family of host atoms.  There is a
physical forest in `G_Q-Z-R` of size

\[
 P-O\!\left({P\over n}+P D_0^{-\alpha}+|Z|
                 +{|R|\over D_0}+{P\over L}\right).           \tag{2.7}
\]

#### Proof

Besides the at most `D_0|Z|` atoms incident with `Z`, deleting `R` removes
at most `|R|` further atoms.  Replace the numerator of (2.4) by
`|E(G_Q)|-D_0|Z|-|R|` and repeat the proof. `square`

Thus protecting one host resource has unit-order cost in the selected
forest bound, while merely banning one atom has `1/D_0`-order cost.  Neither
operation prescribes which resources the selected color class leaves.

## 3. Remove the forced affine slot baseline first

The slot class of `G_Q` has size `2N-C`.  Put

\[
 \sigma=(2N-C)-2P=C-2K={2(n-1)\over n+2}K={2P\over n}. \tag{3.1}
\]

### Proposition 3.1 (balanced-host normalization)

A matching of `P-t` side atoms leaves exactly

\[
                  (t,t,2t+\sigma)                            \tag{3.2}
\]

vertices on the lower, upper and slot shores.  Thus its literal full-host
leave cannot be a union of `t` four-resource atoms.

Fix instead any slot set `S_0` of size `sigma` and work in

\[
                         \widehat G_Q=G_Q-S_0.                 \tag{3.3}
\]

The three host-shore sizes are then `P,P,2P`; a matching of `P-t` atoms has
leave signature `(t,t,2t)`.  It extends by `t` legal atoms exactly when its
leave is their disjoint resource union.  Theorem 2.1 applies to
`\widehat G_Q`, since `sigma=O(P/n)=o(P)`.

For `n>=4`, `S_0` may be chosen entirely among ordinary two-capacity slots,
leaving every cap-one seam-anchor slot available.

#### Proof

Equation (3.2) is the subtraction

\[
 (P,P,2N-C)-(P-t,P-t,2P-2t).
\]

The Catalan identities give (3.1).  Deleting `S_0` gives the balanced shore
sizes and the extension criterion is then literal exact cover.  Finally,
the ordinary slots number `2(N-C)=2(P-K)`, and

\[
 2(P-K)\ge\sigma\quad\Longleftrightarrow\quad2P\ge C.
\]

Since

\[
 {P\over C}={n(n-1)\over2(2n+1)},
\]

the last inequality holds for every `n>=4`. `square`

At `n=3,4,5,6`, `sigma` equals `4,14,48,165`.  The position of `S_0`, not
only its size, remains part of the degree/anchor problem.

## 4. Balanced trades cannot align a leave

Let `A_n` be the resource-incidence matrix of `H_n`.  For an AGCF matching
`M`, write

\[
                         r(M)={\bf1}-A_n{\bf1}_M.              \tag{4.1}
\]

### Lemma 4.1 (kernel versus boundary)

A replacement `P <-> Q` with

\[
                         A_n{\bf1}_P=A_n{\bf1}_Q              \tag{4.2}
\]

leaves `r(M)` unchanged.  In particular, any sequence of balanced
`2 <-> 2` switches preserves the exact leave.

For one standard absorber identity

\[
                         A+B=C+D,                              \tag{4.3}
\]

the off-to-on switch `B -> C+D` has nonzero boundary `A`.  A disjoint bank
of these absorbers finishes a leave `r` if and only if

\[
                         r=\sum_i A_i                          \tag{4.4}
\]

for its designated, pairwise resource-disjoint target candidates `A_i`.
Thus flux/lattice membership is necessary but not sufficient: (4.4) is a
positive matching-semigroup condition.

#### Proof

Equation (4.2) preserves the covered incidence vector and hence (4.1).
Equation (4.3) gives

\[
 A_n({\bf1}_C+{\bf1}_D-{\bf1}_B)=A_n{\bf1}_A.
\]

Summing disjoint switches proves necessity and sufficiency of (4.4).  Since
`r` is zero-one and the columns are nonnegative, the columns on the right
of (4.4) must be resource-disjoint. `square`

### Proposition 4.2 (what the standard trade protects)

In the explicit `2292AG` trade, the two phases have the same middle-vertex
degree profile: the same four global endpoints have degree one and every
other used middle vertex has degree two.  Thus cap-one endpoint anchors are
preserved.  Root ownership is not automatic.

Write `x` for the middle state transferred from old path `A` to new path
`D`, and `y` for the state transferred from old `B` to new `C`.  If old
paths `A,B` each contain exactly one selected root, then new paths `C,D`
each contain exactly one root if and only if

\[
                         {\bf1}_{x\ {\rm rooted}}
                           ={\bf1}_{y\ {\rm rooted}}.           \tag{4.5}
\]

Of the `(n+1)^2` possible old root pairs, exactly `n^2+1` satisfy (4.5).

#### Proof

The explicit four paths differ only by exchanging `x` and `y`; their global
endpoints and all other internal states keep their roles.  The new root
counts are

\[
 1-{\bf1}_x+{\bf1}_y,\qquad1-{\bf1}_y+{\bf1}_x,
\]

which are both one exactly under (4.5).  Either both transferred states are
roots (one choice) or neither is (n choices on each old path), giving
`n^2+1`. `square`

## 5. A smallest lattice-to-matching-semigroup gap and a uniform larger actuator

The exact `n=3` witness is recorded and proved in

```text
MATH_OBSTRUCTION_CATALAN_EDGE_ALIGNED_COVERDOWN_N3_SEMIGROUP_HOLE_20260731.md
```

Four resource-disjoint candidate paths are

\[
\begin{array}{c|cccc}
 E_1&012&123&234&345\\
 E_2&013&134&145&245\\
 E_3&014&024&025&235\\
 E_4&034&035&135&125.
\end{array}                                                    \tag{5.1}
\]

Their leave is

\[
\begin{aligned}
 R_M&=\{015,023,045,124\},\\
 R_L&=\{01,05,24\},\\
 R_U&=\{0125,0145,0234\}.                             \tag{5.2}
\end{aligned}
\]

It has shore sizes `(4,3,3)` and, coordinate by coordinate,

\[
                         m_x=u_x=\ell_x+1.                    \tag{5.3}
\]

Nevertheless its four middle sets contain no complementary pair, so it
contains no AGCF candidate.  This is an actual maximal matching leave, not
an artificial flux vector.  The parameter is sharp: at `n=2`, the
complement of the candidate `ab,bc,cd` is the candidate `ac,ad,bd`.

The obstruction also identifies the first useful enlargement of the packet
catalogue.  Put

\[
\begin{array}{c|cccc}
 P_1&012&123&234&345\\
 P_2&014&024&025&235,\\[1mm]
 Q_1&012&124&234&345\\
 Q_2&014&015&025&235\\
 Q_3&123&023&024&045.
\end{array}                                                    \tag{5.4}
\]

### Theorem 5.1 (dimension-uniform noncandidate-boundary actuator)

For every `n>=3`, the paths in (5.4) have complement-geodesic suspensions
`\widehat P_i,\widehat Q_j` in `H_n` such that

\[
 \bigcup_{j=1}^3 E(\widehat Q_j)
   =\left(\bigcup_{i=1}^2E(\widehat P_i)\right)\mathbin{\dot\cup}R_n, \tag{5.5}
\]

where `R_n` is a zero-one resource set with candidate shore counts

\[
                         (n+1,n,n)                             \tag{5.6}
\]

and every AGCF coordinate-flux row, but `R_n` is not a candidate.  Replacing
the two old paths by the three new paths absorbs `R_n`.  At every old middle
vertex the physical degree is not increased, and every old global endpoint
remains an endpoint.

#### Proof

Split the coordinates outside `012345` into complementary ordered sets

\[
 F=(f_1,\ldots,f_{n-3}),\qquad G=(g_1,\ldots,g_{n-3}).
\]

For an active path `S_0,S_1,S_2,S_3`, adjoin `F` to its four states and then
append the common tail which exchanges

\[
                         f_1\to g_1,\ldots,f_{n-3}\to g_{n-3}. \tag{5.7}
\]

The last active state is the complement of the first on `012345`, so the
result is a length-`n` complement geodesic.  The tails of `P_1,Q_1` cancel
because both end at `345`; the tails of `P_2,Q_2` cancel because both end at
`235`.  A direct comparison of the first three turns leaves four active
middle states

\[
 124F,\quad015F,\quad023F,\quad045F,                         \tag{5.8}
\]

plus the `n-3` new tail states following `045F`.  The three active lower
resources are

\[
                         01F,\quad05F,\quad24F,
\]

and the three active upper resources are

\[
                         0125F,\quad0145F,\quad0234F.          \tag{5.9}
\]

If `T_0=045F` and

\[
 T_j=045\cup(F\setminus\{f_1,\ldots,f_j\})
          \cup\{g_1,\ldots,g_j\},
\]

then the extra tail contributes middle states `T_j`, lower turns
`T_(j-1)-f_j`, and upper turns `T_(j-1)+g_j`, for
`1<=j<=n-3`.  Their spectator patterns separate them from (5.8)--(5.9)
and from one another.  This proves the disjoint identity (5.5).

The shore counts in (5.6) follow by subtracting two candidate columns from
three.  The coordinate flux follows from the same subtraction.  Every
middle state in `R_n` with active part `124,015,023` has an active complement
absent from (5.8); every remaining state has active part `045`, while its
complement has active part `123`, which is absent from `R_n`.  Hence `R_n`
contains no complementary middle pair and is not a candidate.

On old vertices, `012F,345G,014F,235G` remain the four global endpoints;
`234F,025F,024F` retain degree two, and `123F` drops from degree two to
degree one.  The intermediate active-terminal states and the common tails
are unchanged.  This proves the degree and endpoint claims. `square`

The new third path still needs a root from the absorbed boundary if the
downstream row requires one root per component; endpoint safety alone does
not supply it.

At `n=3`, this actuator is one of six exact `2 -> 3` repairs of (5.2), four
of which preserve every old cap-one endpoint.  The replay in Section 8
checks this finite statement exhaustively.

## 6. Physical acyclicity is a contracted graphic row

Let `F` be the retained physical forest after all off-state packet edges
which will be removed have been deleted.  Contract every component of `F`.
Suppose packet `i` has a menu `Sigma_i` of private physical ears; suppress
their private internal vertices so each choice is one quotient link.

### Proposition 6.1 (exact ear-selection criterion)

There is one choice from every menu whose union with `F` is acyclic if and
only if

\[
 r_{\rm gr}\!\left(\bigcup_{i\in I}\Sigma_i\right)\ge |I|
          \qquad\hbox{for every packet index set }I.           \tag{6.1}
\]

#### Proof

After contraction and suppression, the chosen ears preserve acyclicity
exactly when their quotient links form an independent set of the graphic
matroid.  Equation (6.1) is Rado's independent-transversal theorem. `square`

For a packet with several nonprivate new edges, (6.1) is only a sufficient
subclass after an explicit ear reduction; it is not silently applied to an
arbitrary path block.  Palette privacy, cap two, cap-one anchors, and root
ownership remain separate rows.

The fixed-`Q`, `n=3` fixture in

```text
MATH_THEOREM_CATALAN_DIRECT_LOWER_AUGMENTED_GRAPHIC_GATE_AND_N3_OBSTRUCTION_20260731.md
```

shows this gate is real: marginal rooted side supports exist, but the forced
contracted unions contain literal circuits (cycle ranks `1` and `4`).
Short-cycle conflicts internal to the Delcourt--Postle color class do not
imply (6.1) for future ears mixed with the retained forest.

## 7. Structured reserves work; naive sparse random reserves do not

The standard `2 <-> 2` trade support has

\[
                         w=2(3n+1)                             \tag{7.1}
\]

resource vertices.  Let its distinct `Sym(2n)` translates form an orbit
`O`.  Every resource belongs to exactly

\[
                         d={2|O|\over\operatorname {Cat}_n}    \tag{7.2}
\]

supports: on each of the three shores, a support occupies exactly
`2/Cat_n` of that shore.  The intersection graph of the supports has maximum
degree at most `w(d-1)`.  Greedy packing therefore gives at least

\[
             \left\lceil{\operatorname {Cat}_n\over4(3n+1)}\right\rceil
                                                                    \tag{7.3}
\]

pairwise resource-disjoint absorber supports.

The same argument applies to the support of Theorem 5.1.  Its support is
the union of the three new candidates, hence has `3(3n+1)` resources and
occupies the fraction `3/Cat_n` of every shore.  It therefore has a
resource-disjoint orbit bank of size at least

\[
             \left\lceil{\operatorname {Cat}_n\over9(3n+1)}\right\rceil.
                                                                    \tag{7.4}
\]

In contrast, put every resource independently into a reserve with
probability `rho`.  For a fixed resource `v`, the number `X_v` of candidates
through `v` whose other resources all lie in the reserve satisfies

\[
 {\bf E}X_v=D\rho^{3n},\qquad
 D={n+1\over2}(n!)^2.                                  \tag{7.5}
\]

If `rho=n^{-2/3-epsilon}` for fixed `epsilon>0`, Stirling gives

\[
 \log {\bf E}X_v=-3\epsilon n\log n-2n+O(\log n)\to-\infty. \tag{7.6}
\]

Hence Markov's inequality shows that, with probability tending to one, even
this fixed resource has no complete candidate in the reserve.  In
particular a naive density-`1/n` reserve cannot furnish local AGCF
extensions.  This does not obstruct the structured orbit bank (7.3) or
nonzero-boundary packets such as Theorem 5.1.

#### Proof of (7.3)--(7.4)

The group is transitive on every shore, and the inclusion ratio of a
support is `2/Cat_n` on all three shores, proving (7.2).  One support meets
at most `w(d-1)` other orbit supports.  A greedy independent set in the
intersection graph has size at least

\[
 { |O|\over1+w(d-1)}\ge {|O|\over wd}
 ={\operatorname {Cat}_n\over2w},
\]

which is (7.3). `square`

For the actuator orbit, replace `2` by `3` and `w` by `3(3n+1)` in the
same double count.  This gives `Cat_n/[9(3n+1)]` and proves (7.4).

## 8. Exact composition theorem and remaining boundary

The preceding statements give the following honest sufficient theorem.

### Theorem 8.1 (conditional protected edge-aligned completion)

Fix `Q` and a slot baseline `S_0` of size `sigma`.  Suppose there is a
family of pairwise closed-support-disjoint packet realizations in
`G_Q-S_0` such that

1. their off states and protected anchors form a physical forest `B` with
   `|cl(B)|=o(P)`;
2. a physical-forest bulk matching `M` in
   \(G_Q-(S_0\cup\operatorname {cl}(B))\) has the property that the leave
   of the combined off-state matching \(M\cup B\), measured in
   \(G_Q-S_0\), is exactly the disjoint union of the designated packet
   boundaries;
3. every choice in a packet menu has that packet's designated incidence
   boundary, is compatible with the other packet supports, and respects the
   palette, slot-capacity, protected-anchor and separately prescribed
   root-owner rows; and
4. after deleting the off-state edges which will be switched, the retained
   physical forest and the resulting private-ear menus satisfy (6.1).

Then the packet switches produce an exact outer-palette side realization
with the prescribed slot baseline, protected anchors, and physical
acyclicity.

Moreover, Theorem 2.1 guarantees a `P-o(P)` forest body outside every such
preselected bank.  Thus asymptotic coexistence of a *given* bank with a
large body is proved.  To instantiate the conditional theorem one must
still construct legal fixed-`Q` packet realizations satisfying items 1 and
3 (the AGCF packets do not supply these automatically), choose the body
with the exact nonzero-boundary leave in item 2, and prove the graphic
correlation in item 4.

#### Proof

For the bulk matching postulated in item 2, the exact leave identity and
the packet boundary identities make every nonbaseline host resource covered
exactly once after switching.  Item 3 gives the capacity, palette,
protection and root compatibility.  Proposition 6.1 applied to the retained
forest in item 4 gives acyclicity.  Separately, Theorem 2.1
proves that reserving the packet bank does not obstruct an asymptotically
complete protected bulk; it does not supply item 2's aligned bulk. `square`

The sharp next target is thus either:

* an iterative augmenting-path/tree theorem whose exposed boundaries span
  every admissible residual in the positive packet matching semigroup while
  maintaining the contracted graphic ranks; or
* a cover-down theorem choosing the Delcourt--Postle color class so its
  leave is already a union of candidate and suspended-`2 -> 3` boundary
  orbits.

The full conflict-free coloring may provide a global exchange core, but its
closed alternating components are kernel moves.  Endpoint-bearing
components with controlled boundary are essential.

## 9. Independent finite replay

Run

```text
python3 scratch/audit_catalan_agcf_edge_aligned_leave_and_augmenter_20260731.py
```

It reconstructs all `360` parameter-three candidates and verifies:

* the four-edge matching (5.1), its leave and every flux row;
* absence of any candidate or `1 -> 2` augmentation in the leave;
* all six `2 -> 3` augmentations and the four old-cap-safe ones;
* the suspended actuator and standard-trade degree ledgers through `n=6`;
* the exact root-switch criterion for the standard trade; and
* the orbit-packing constants (7.3)--(7.4).

The replay is finite corroboration.  The all-parameter claims in Sections
2--8 are proved above and do not depend on extrapolating the finite audit.
