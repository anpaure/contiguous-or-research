# Odd adjacent necklaces: stabilizer-root bipartization and the exact surplus-current gate

**Date:** 2026-08-06  
**Method:** delete one complete stabilizer orbit of coordinate boundaries,
Burnside's lemma, odd-group phase-cube matching, and cotransversal basis
exchange; no computation  
**Status:** unconditional structural theorem and smaller exact reduction.
It works directly on the cyclic nearest-neighbour graph modulo the actual
odd rotational stabilizer.  It proves an exact closed formula for the
rooted quotient imbalance and absorbs every nonwrap Hall constraint into
one cotransversal surplus matroid.  It does **not** prove that the remaining
same-shore current has the required coloured matroid matching, nor does it
erase the hub-colour/receiver-extension gate.

## 1. The stabilizer-root cut

Let

\[
 {\cal T}_{n,R}
 =\{t\in\{0,1,2\}^{\mathbb Z_n}:\sum_i t_i=R\},
 \qquad n,R\text{ odd}.
\tag{1.1}
\]

Edges move one unit between cyclically adjacent coordinates.  Let
`H <= C_n` be the rotational stabilizer of the fixed background data in
one ordinary adjacent-necklace sector.  Put

\[
 |H|=h,\qquad n=h\ell.
\tag{1.2}
\]

Both `h` and `ell` are odd.  Index coordinates as

\[
 (j,p),\qquad j\in\mathbb Z_h,\quad 0\le p<\ell,
\tag{1.3}
\]

so that a generator of `H` sends `(j,p)` to `(j+1,p)`.

Delete the complete `H`-orbit of coordinate boundaries

\[
 D=\{\{(j,\ell-1),(j+1,0)\}:j\in\mathbb Z_h\}.
\tag{1.4}
\]

The coordinate cycle minus `D` is a disjoint union of `h` paths of odd
order `ell`.  Let `B_H` be the quotient by `H` of the token graph using
only transfers inside those paths, and let `W_H` be the quotient edge
set induced by transfers across `D`.  Thus the full simple sector graph is

\[
                         G_H=B_H\cup W_H.
\tag{1.5}
\]

Define

\[
 \chi_H(t)=\sum_{j\in\mathbb Z_h}\sum_{p=0}^{\ell-1}p\,t_{j,p}
             \pmod2.
\tag{1.6}
\]

### Theorem 1.1 (root-orbit bipartization)

The function `chi_H` is `H`-invariant and hence descends to necklace
orbits.  Every edge of `B_H` reverses `chi_H`, while every edge of `W_H`
preserves it.  Consequently `B_H` is genuinely bipartite on the simple
necklace quotient, and `W_H` is exactly a same-shore edge bank.

#### Proof

The group `H` permutes the index `j` and fixes `p`, so (1.6) is invariant.
An internal transfer changes the weighted sum by one.  A boundary transfer
changes it by `ell-1`, which is even because `ell` is odd.  These statements
survive orbit coalescence; a quotient loop, if one occurs, is omitted from
the simple graph. \(\square\)

This is the quotient-safe replacement for choosing one literal root.  A
single root is not invariant under a periodic background, whereas the
boundary orbit (1.4) is.

## 2. Exact Burnside formula for the quotient current

Write

\[
                         \ell=2m+1
\tag{2.1}
\]

and put

\[
 F_\ell(z)
 =\prod_{p=0}^{\ell-1}\bigl(1+(-1)^p z+z^2\bigr)
 =(1+z+z^2)(1+z^2+z^4)^m.
\tag{2.2}
\]

Let `L_H` and `R_H` be respectively the `chi_H=0` and `chi_H=1` shores
of `B_H`, and set

\[
                         \Delta_H=|L_H|-|R_H|.
\tag{2.3}
\]

### Theorem 2.1 (stabilizer-orbit imbalance)

The exact quotient shore imbalance is

\[
 \boxed{
 \Delta_H={1\over h}
   \sum_{d\mid\gcd(h,R)}
      \varphi(d)\,[z^{R/d}]F_\ell(z)^{h/d}.}
\tag{2.4}
\]

In particular `Delta_H>0` throughout the nonempty odd-mass range.

#### Proof

Apply Burnside's lemma with the sign `(-1)^{chi_H}`.  An element of order
`d` in `H` has `h/d` cycles on the path-component index `j`, every cycle
having odd length `d`.  A fixed configuration repeats each representative
digit `d` times.  It therefore exists only when `d` divides `R`; after
dividing the mass by `d`, its signed enumerator is

\[
                         F_\ell(z)^{h/d}.
\tag{2.5}
\]

Oddness of `d` is important: repeating a digit `d` times leaves its sign
`(-1)^{p t}` unchanged.  There are `phi(d)` elements of order `d` in the
cyclic group.  Summing (2.5) gives (2.4).

The factorization (2.2) has nonnegative coefficients, and the identity
term `d=1` has a positive coefficient at every attainable odd mass.
Hence (2.4) is positive. \(\square\)

For `H=1`, formula (2.4) is the single-root coefficient from the rooted
path theorem.  Thus periodic quotienting changes the amount of current by
an explicit divisor sum; it does not make the current disappear.

## 3. The nonwrap graph saturates its minority shore

Pair positions inside every path component by

\[
 (j,0)(j,1),\ (j,2)(j,3),\ldots,
 (j,\ell-3)(j,\ell-2),
\tag{3.1}
\]

leaving `(j,ell-1)` unpaired.  On one ordered coordinate pair use

\[
 01-10,\qquad02-11,\qquad12-21,
\tag{3.2}
\]

with quiet singleton states

\[
                              00,20,22.
\tag{3.3}
\]

Fix all pair sums, the two-state keys in (3.2), and all unpaired digits.
The active keys form a hypercube; the stabilizer of the fixed key data is
a subgroup of the odd group `H`.  The odd-group hypercube quotient theorem
therefore perfectly matches every fibre having at least one active key.

### Theorem 3.1 (minority saturation)

The graph `B_H` has a matching `M^-` which covers every vertex of `R_H`.
Its unmatched set `Q^-` consists exactly of the all-quiet singleton-key
orbits.  In particular

\[
                         |Q^-|=\Delta_H.
\tag{3.4}
\]

The shifted pairing

\[
 (j,1)(j,2),\ldots,(j,\ell-2)(j,\ell-1),
\tag{3.5}
\]

leaving `(j,0)` unpaired gives a second such matching `M^+` and a second
surplus set `Q^+` of the same size.

#### Proof

The phase-cube quotient matchings described above cover every nonquiet
fibre and use only internal path transfers, so they belong to `B_H`.
In an unmatched state, every pair is one of (3.3).  Its contribution to
(1.6) is even, and the unpaired position `ell-1` is even.  Hence every
unmatched orbit lies in `L_H`.  The matching therefore saturates `R_H`,
and the number left in `L_H` is the shore difference (3.4).

For (3.5), the first position of every ordered pair is odd.  The states
`20` and `22` still contribute an even amount to (1.6), and the unpaired
position zero contributes nothing.  The same argument applies. \(\square\)

This theorem is strictly stronger than the scalar identity (2.4): the
whole nonwrap Hall problem already has an explicit quotient matching.

## 4. The surplus cotransversal matroid

Regard `B_H=(L_H,R_H;E)` as a bipartite graph.  Its transversal matroid
`T_H` on `L_H` has rank `|R_H|` by Theorem 3.1.  Let

\[
                         S_H=T_H^*
\tag{4.1}
\]

be its dual, a cotransversal matroid of rank `Delta_H`.

### Lemma 4.1 (exact surplus bases)

For a set \(U\subseteq L_H\) of size \(\Delta_H\), the following are
equivalent:

1. `U` is a basis of `S_H`;
2. `B_H-U` has a perfect matching; and
3. `B_H` has a matching which covers every vertex except exactly `U`.

Moreover, for arbitrary \(X\subseteq L_H\),

\[
 r_{S_H}(X)
 =|X|-|R_H|+\nu_{B_H}(L_H\setminus X,R_H),
\tag{4.2}
\]

where the final term is the maximum size of a matching from
\(L_H\setminus X\) into \(R_H\).

#### Proof

The bases of the dual are complements of bases of `T_H`.  A
`|R_H|`-set is a basis of `T_H` exactly when it is matched bijectively to
`R_H`.  This proves the equivalences.  The standard dual-rank identity

\[
 r_{T_H^*}(X)=|X|-r(T_H)+r_{T_H}(L_H\setminus X)
\]

gives (4.2). \(\square\)

Thus all exponentially many nonwrap Hall cuts are now represented by one
ordinary cotransversal rank oracle.

## 5. Two root phases give a Boolean exchange cube of surplus bases

Take the two minority-saturating matchings `M^-` and `M^+` from Theorem
3.1.  In the multigraph union `M^- union M^+`, every vertex of `R_H` has
degree two.  Its nontrivial path components have one endpoint in
\(Q^-\setminus Q^+\) and one in \(Q^+\setminus Q^-\); vertices unmatched by
both are regarded as length-zero components.

Put

\[
 A=Q^-\setminus Q^+,
 \qquad C=Q^-\cap Q^+.
\tag{5.1}
\]

Let

\[
                         \phi:A\longrightarrow Q^+\setminus Q^-
\tag{5.2}
\]

pair the endpoints of the nontrivial components.  The vertices in `C`
remain fixed in every exchange.

### Theorem 5.1 (strong two-base exchange)

For every \(X\subseteq A\), the set

\[
 U_X=C\cup(A\setminus X)\cup\phi(X)
\tag{5.3}
\]

is a basis of `S_H`.  More precisely, flipping `M^-` along the pairwise
disjoint alternating components indexed by `X` gives a matching of
`B_H` whose unmatched set is exactly `U_X`.

#### Proof

Each nontrivial component is an even alternating path.  Flipping it
exchanges which of its two `L_H` endpoints is unmatched and changes no
other matching state.  The components are vertex-disjoint, so an arbitrary
collection may be flipped simultaneously.  Common unmatched vertices are
unchanged.  Lemma 4.1 then gives the basis assertion. \(\square\)

This Boolean family is a concrete, quotient-valid replacement for the
unsupported complete-transfer Gray path.  It uses only nearest-neighbour
edges of the cut-open physical sector.

It is an exchange theorem, not a current construction.  The companion
note
`MATH_OBSTRUCTION_ODD_TWO_ROOT_EXCHANGE_CUBE_EXTREME_WRAP_ONLY_20260806.md`
proves that, for trivial stabilizer and nonextreme compressed mass, the
physical boundary graph induced on the union of **all** canonical quiet
root bases is empty.  Hence the two-base cube cannot itself supply the
central current.

## 6. Exact majority-current criterion

Let `P` be a matching in the same-shore boundary graph `W_H[L_H]`.  Let
`Z` be either empty or one vertex of `L_H`, disjoint from `V(P)`.  Write

\[
                         U=V(P)\mathbin{\dot\cup}Z.
\tag{6.1}
\]

### Theorem 6.1 (cotransversal wrap-current completion)

If

\[
 |U|=\Delta_H
 \qquad\text{and}\qquad
 U\text{ is a basis of }S_H,
\tag{6.2}
\]

then `G_H` has a matching which misses exactly `Z`.  In particular it is
perfect when `Z` is empty and near-perfect when `|Z|=1`.

It is enough in (6.2) to require `U=U_X` for one of the explicit two-base
sets (5.3).

Conversely, every perfect or near-perfect matching of `G_H` which uses no
same-shore edge in `R_H` yields data (6.1)--(6.2).  Thus (6.2) is exact
for the majority-only current architecture.

#### Proof

By Lemma 4.1, choose a perfect matching of `B_H-U`.  Adjoin the edges of
`P`.  They cover `V(P)`, are disjoint from the nonwrap matching, and leave
exactly `Z` uncovered.

Conversely, remove the majority-shore same-shore edges from such a full
matching.  The remaining cross edges perfectly match `B_H-U`, so Lemma
4.1 makes `U` a surplus basis. \(\square\)

The scalar current equation is the immediate consequence

\[
                         2|P|+|Z|=\Delta_H.
\tag{6.3}
\]

Equation (6.3) is necessary but not sufficient.  The genuinely remaining
condition is that the endpoints form one surplus basis.  This is a
**cotransversal matroid matching** on the actual cyclic boundary edges,
not a complete-transfer matching and not an arbitrary Tutte family.

The two-base sufficient face is smaller still:

> retain every fixed vertex in `C`, choose one endpoint from every
> nontrivial alternating transport pair (5.2), and pair all chosen
> vertices except the optional socket by physical boundary edges.

No intermediate Hall test is left on the cut-open sector, but the cited
extreme-wrap obstruction shows that this sufficient face is empty in the
central trivial-stabilizer sectors.  A positive proof must use a genuinely
noncanonical surplus basis or the full cotransversal matroid.

## 7. Hub colours and circulation lifts

The preceding theorems are statements in one simple capacity-two necklace
sector.  To use the selected edge bank in the ambient adjacent-necklace
construction, its occurrence labels and deleted-cut hubs must still be
priced.

For a hub-rainbow occurrence lift of `P`, Theorem 6.1 and the odd
circulation-blossom packing theorem compose directly: the selected
same-shore current has distinct critical endpoints, distinct hub orbits,
and fixed-level-disjoint circulation interiors.

If a hub colour is repeated, it may **not** be silently reused.  The
paired hub-fan theorem replaces multiplicity `d` by adjacent receiver
pairs and the binary outgoing state

\[
                         \eta\equiv d-1+\epsilon\pmod2.
\tag{7.1}
\]

Likewise, the phase-cube matching used inside `B_H` is not automatically
unpointed-hub-rainbow across all background sectors.  Its repeated colours
must be passed through the same fan/receiver augmentation.  Therefore the
proof-safe global target is:

> **Coloured surplus-current theorem.**  Choose a majority-current
> matching satisfying (6.2), together with a minority-saturating nonwrap
> matching, so that after grouping all selected edges by unpointed hub
> orbit, the paired receiver rectangles satisfy the next-level augmented
> Hall/Tutte cuts and export at most the prescribed terminal socket.

This statement explicitly retains the hub partition and quotient
coalescence.  The new gain is that its odd same-shore amount and every
ordinary nonwrap Hall row have already been solved: only the coloured
surplus-basis matching and the existing receiver extension remain.

## 8. Test of the particle-pair odd-ear bypass

At central mass, write

\[
 \Sigma_q=\{t:\#\{i:t_i=0\}=\#\{i:t_i=2\}=q\}.
\tag{8.1}
\]

The shell idea starts with (\Sigma_0=\{{\bf1}\}) and tries to attach
(\Sigma_q) to (\Sigma_{q-1}) by moving one new zero--two pair through
a run of ones and annihilating it at both ends.

There is a real local ear, but the most direct fibrewise version has a
parity obstruction.  Fix (y\in\Sigma_{q-1}), fix a linear run (I) of
(L) ones in (y), and keep every coordinate outside (I) fixed.  For
one orientation of the new labels, the states obtained by replacing
positions (1\le i<j\le L) in (I) by zero and two form the triangular
grid

\[
 {cal J}_L=\{(i,j):1\le i<j\le L\},
\tag{8.2}
\]

with edges changing one of (i,j) by one while preserving their order.
The reverse orientation is a second disjoint copy.  Every boundary state
((i,i+1)) is joined to the same lower-shell vertex (y) by
(02\leftrightarrow11) or (20\leftrightarrow11).

### Proposition 8.1 (one-parent fibre parity obstruction)

If

\[
                         L\equiv2,3\pmod4,
\tag{8.3}
\]

then one oriented fibre (8.2) cannot be covered by closed odd ears whose
only old endpoint is (y).

#### Proof

The fibre has

\[
                         |{cal J}_L|={L\choose2}
\tag{8.4}
\]

vertices, which is odd exactly in the congruence classes (8.3).  A closed
odd ear based at (y) has an even number of internal vertices.  Distinct
ears in an ear decomposition have disjoint interiors, so any union of
such ears uses an even number of vertices of one oriented fibre.  It
cannot cover (8.4) when that number is odd. \(\square\)

This does **not** rule out a global shell ear decomposition.  It proves
that a successful one must couple different parents, different runs, or
the two orientations; independent one-parent fibres are insufficient.
After quotienting, it must additionally avoid orbit coalescence.  Even a
valid odd-ear decomposition of the simple quotient would still not imply
the hub-colour condition: the alternating matching selected on its ears
can reuse an unpointed deleted-cut hub, and those repetitions must still
pass through the paired fan/receiver law (7.1).

Thus the shell proposal and the surplus-current reduction point to the
same missing interaction: a cross-fibre, hub-aware ear selector rather
than independent particle-pair ears.

## 9. Exact obstruction and scope

The former odd-level gate was the full Tutte family of an augmented
nonbipartite sector.  Theorems 1.1--6.1 replace its uncoloured part by:

1. the explicit divisor-sum current `Delta_H` in (2.4);
2. one cotransversal matroid `S_H` with rank oracle (4.2); and
3. a same-shore nearest-neighbour matroid-matching problem, with the
   concrete two-base face (5.3).

This reduction respects all three structures missed by the
Ruskey--Savage shortcut:

* transfers are cyclic nearest-neighbour transfers;
* periodic backgrounds are quotiented by their actual odd stabilizer;
* hub colours remain an explicit partition/receiver constraint.

Proved here:

1. stabilizer-invariant bipartization after deleting one boundary orbit;
2. the exact Burnside current formula (2.4);
3. a quotient matching saturating the entire minority shore;
4. the exact cotransversal surplus-basis criterion;
5. a Boolean exchange cube of surplus bases from two physical root phases;
6. exact majority-only current completion once one basis is physically
   pairable.

Also proved in the companion obstruction: no canonical quiet-root basis
union contains a boundary edge at nonextreme compressed mass.

Not proved here:

1. existence of a boundary-edge matching whose endpoints form the needed
   surplus basis;
2. hub-rainbow selection, or the augmented receiver cuts when colours
   repeat;
3. cross-level circulation-interior/receiver compatibility;
4. preservation of a fixed PBBS halo or typed cap; or
5. the adjacent-necklace theorem or `nu(k)<=B(k)+O(1)`.
