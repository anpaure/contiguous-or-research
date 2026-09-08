# Folded-C8 addressed transport: exact forced-edge Hall and common-cap gate

Date: 2026-08-01  
Lane: R, folded-C8 ambient compiler closure  
Status: unconditional finite theorem for a typed addressed bijection and a
fixed old occurrence matching.  The canonical screened folded-C8 audit gives
the required unguarded occurrence bijection for `2<=d<=12`.  Owner legality,
the `q1` sidecars, address-specific guards, and regenerative return remain
separate hypotheses.  No all-`k` conclusion is claimed.

**Scope correction.**  For an actual split/full-block refinement, the old
matching transports injectively on full-block cells and the ray cells are
side cells outside that image.  In that preferred architecture there is no
separate ambient Hall gate.  The forced-edge Hall/linkage theorem below is
the exact fallback for a clipped or non-refinement planting, for
address-specific guard losses, or whenever mandatory packet returns occupy
cells inside the transported bank.

## 0. Result

There are three different bijections in the folded-C8 discussion, and they
must not be identified.

1. A **threshold pairing** pairs the two abstract prefix/suffix tickets in
   the terminal birail calculation.  It has no physical cell address.  In
   the folded antidiagonal, one paired ticket consists of two ray-cell
   occurrences (often lying in opposite phases); it is never licensed to
   collapse those two occurrences to one compiler cell.
2. An **address bijection** pairs an old physical interval occurrence with a
   new physical interval occurrence of the same declared type.
3. A **compiler matching** pairs each target mask with one physical interval
   occurrence which literally realizes it.

The new screened audit proves the second object globally on the canonical
finite family.  Its type is

\[
             \tau(J)=(\lvert J\rvert,\operatorname{OR}(J),
                       \operatorname{Cap}(J)).              \tag{0.1}
\]

For every type, old and new fibres have the same size; ordering each fibre
lexicographically gives a bijection `Phi` of **all** interval occurrences.
Consequently `Phi` transports every old occurrence matching without cell
collisions in the unguarded one-core graph.  On the strict
`core=target` subface this transport is already literal edge by edge.  On the general
`core subseteq target subseteq cap` face, simultaneous literal common-`Q`
still requires the cap-gluing condition below.

If specified packet-return addresses must be used, the exact additional
condition is not another ray count.  Pull those new addresses back through
`Phi`, force the resulting old target--cell edges, and ask whether they
extend to an old complete matching.  This is ordinary forced-edge Hall; relative
to a named old matching it is equivalently a vertex-disjoint alternating
linkage problem.

Source-cap compatibility is an independent outer condition.  For a fixed
row family it has the exact maximal-word intersection test in Theorem 2.1
below.  Before a complete cap state is fixed, the feasible assignment sets
need not form a matroid.  Thus the valid decomposition is

\[
 \boxed{\text{compatible cap state}}
 \quad\longrightarrow\quad
 \boxed{\text{forced packet edges}}
 \quad\longrightarrow\quad
 \boxed{\text{residual Hall / alternating linkage}}.       \tag{0.2}
\]

The lower- and upper-`q1` sidecars constrain the first box and their own
edge-occurrence capacities.  They are not compiler cells unless a literal
construction declares them to be such.  Recycling the common screen in an
existing immediate-left source occurrence gives length charge `chi=0`, but
does not remove either its source-cap rows or the matching edges whose
intervals meet that occurrence.

When the physical packet is a genuine full-block refinement, the middle
box is private from the transported background and the last box is
automatic; only the cap/owner/sidecar and reset rows remain.

## 1. Typed occurrence transport

Let `W^-` and `W^+` be two source words of the same length.  Let
`C^-`,`C^+` be their physical interval occurrences.  A type record for a
cell `J` is

\[
 \widehat\tau(J)=
  (\lvert J\rvert,\operatorname{OR}(J),
    \operatorname{Cap}(J),\gamma(J)),                       \tag{1.1}
\]

where `gamma` is the complete address-dependent guard record required by
the intended compiler: deadline class, protected occurrence bits, boundary
type, and any other structural zero.  On the unguarded decoder face omit
`gamma`.  Here `Core(J)` means the actual literal OR of the source letters
on `J`.  The guard coordinate is defined extensionally: equal `gamma`
means identical permitted target neighbourhoods after every structural
deletion.  Merely giving two guards the same informal name is insufficient.

An **address isomorphism** is a bijection

\[
                         \Phi:C^-\longrightarrow C^+         \tag{1.2}
\]

preserving (1.1).  Let `L` be the target bank.  On the one-core face an
occurrence matching is an injection `m:L->C^-` such that

\[
 \operatorname{Core}(m(T))\subseteq T
       \subseteq\operatorname{Cap}(m(T))                     \tag{1.3}
\]

and every guard of `m(T)` is legal.  Call it **strict-core** when the first
inclusion is equality.  A general graph matching becomes a literal
common-`Q` matching only when its complete row family passes Theorem 2.1.

### Theorem 1.1 (global address transport)

If `Phi` is an address isomorphism, then

\[
                         \Phi m:T\longmapsto\Phi(m(T))        \tag{1.4}
\]

is an occurrence matching in the new one-core graph.  In particular, it
has the same target set, no cell collision, the same widths, and the same
complete guard types.  Strict-core matchings remain strict-core.

The last assertion is edgewise: each transported strict-core cell has
literal OR equal to its assigned target.  Simultaneous common-`Q` still
requires Theorem 2.1 unless the displayed source word itself is already the
certified joint solution.

For a general matching, the conclusion is a literal common-`Q` matching if
and only if its transported row family passes Theorem 2.1 (or lies in a
declared matching-closed cap state).

If only the first three coordinates of (1.1) are preserved, the same
conclusion holds on the unguarded width/core/cap face and for every old
matching edge whose image is independently checked to have the required
guard.  It does not hold for arbitrary address-specific guards.

#### Proof

Injectivity follows from injectivity of `m` and `Phi`.  Type preservation
gives

\[
 \operatorname{Core}(\Phi(m(T)))=
 \operatorname{Core}(m(T))\subseteq T
 \subseteq\operatorname{Cap}(m(T))=
 \operatorname{Cap}(\Phi(m(T))),
\]

and preserves the width and every recorded guard.  This proves all claims.
\(\square\)

This theorem is stronger than equality of value counters: it transports a
named matching.  It is also different from a packet-local bijection.  A
partial bijection on the changed cells says nothing about the old matching
cells outside its domain.

### Lemma 1.2 (fibre completion of a packet-local bijection)

Suppose old and new cells have the same cardinality in every complete type
fibre of (1.1).  Every injective type-preserving partial map, with
`D subseteq C^-`,

\[
                            \beta:D\longrightarrow C^+       \tag{1.5}
\]

extends to a global address isomorphism `Phi`.

#### Proof

Fix a type fibre.  The partial map uses equally many distinct old and new
members of that fibre.  Pair the unused old and new members arbitrarily.
Doing this independently in every fibre extends `beta` and preserves type.
\(\square\)

Thus the right positive object is not necessarily the canonical
lexicographic bijection.  The frozen fibre counts allow a prescribed
packet-local bijection to be completed globally, provided it preserves the
full type and is injective on both occurrence shores.

### Corollary 1.3 (canonical screened folded-C8 scope)

For the canonical aligned folded source plus opposite ray word, the frozen
audit constructs, for both tested screens and every `2<=d<=12`, a global
bijection preserving

\[
                 (\text{width},\text{literal OR core},
                   \text{interval common cap}).              \tag{1.6}
\]

It does so with a fresh screen and with a fixed immediate-left ambient
letter containing the screen.  The latter has packet length charge zero.
Therefore every old one-core compiler matching transports collision-free as
a graph matching on the unguarded (1.6)-face; every strict-core matching
transports literally edge by edge.  General common-`Q` simultaneity remains
Theorem 2.1.
Moreover every injective packet-local bijection
preserving (1.6) extends to such a global transport.  The audit does not
preserve an address-specific `gamma`, prove the owner word, or provide
either `q1` sidecar.
The payload also explicitly verifies the ray-shore semantics: an abstract
prefix/suffix antidiagonal is a paired two-cell ticket with distinct
interval occurrences, not one right-hand matching vertex.

The frozen files are

```text
scratch/audit_r_folded_c8_address_bijection_and_screen_recycling_20260801.py
scratch/r_folded_c8_address_bijection_and_screen_recycling_20260801.audit.json
```

with SHA-256 values

```text
247e4aa93100dd6d7d4c282daf6e2183e4ca95c70049aa0cefc807d72bf24dcc
c7c99e1cf57ec490bd3a7136349d047a06fa6af249c1a65363cb639a26bf4cd3
```

and payload
`8ee79f497d8ae1951dd28d16b61dfa0d7a4b5fa15e9cae455dd28df5ddf21368`.
The full construction and its independent audit are
`MATH_THEOREM_R_FOLDED_C8_ADDRESSED_OCCURRENCE_BIJECTION_AND_ZERO_CHARGE_SCREEN_20260801.md`
and
`MATH_AUDIT_R_FOLDED_C8_ADDRESSED_OCCURRENCE_AND_SCREEN_RECYCLING_20260801.md`.

## 2. Exact source-cap composition

Fix one proposed target--cell assignment and every owner, `q1`, screen,
protected, and exterior row it is required to retain.  For a row `R`, write

* `S_R` for its target;
* `E_R` for its frozen exterior union;
* `J_R` for its live source positions; and
* `D_p subseteq P_p` for the required source lower bound and source cap at
  live position `p`.

The lower bound `D_p` includes every actual endpoint/base letter which is
required to remain present, as well as all fixed screen support.

Split the rows into background rows `B` and packet rows `P`; the packet rows
include every owner/source row certifying the `q1` sidecars, while
recycled-screen support enters the lower bound `D_s` (and a frozen ambient
letter also fixes its cap).  Put

\[
\begin{aligned}
 K_p^B&=P_p\cap\bigcap_{R\in B:\ p\in J_R}S_R,\\
 K_p^P&=P_p\cap\bigcap_{R\in P:\ p\in J_R}S_R,\\
 K_p&=K_p^B\cap K_p^P.                                  \tag{2.1}
\end{aligned}
\]

An empty intersection of row targets is read as the ambient cap `P_p`.

### Theorem 2.1 (necessary and sufficient cap-gluing test)

There are **nonempty** source letters
`D_p subseteq Q_p subseteq P_p` satisfying every background and packet row

\[
                   E_R\cup\bigcup_{p\in J_R}Q_p=S_R          \tag{2.2}
\]

if and only if

\[
 D_p\subseteq K_p\quad\text{and}\quad K_p\ne\varnothing
       \quad\text{for every live }p,
 \qquad
 S_R=E_R\cup\bigcup_{p\in J_R}K_p
        \quad\text{for every }R.                            \tag{2.3}
\]

When feasible, `Q_p=K_p` is the componentwise maximal solution.  Hence two
separately feasible row systems glue if and only if they use one common
upper cap, use the union of their two lower-bound systems, and the resulting
intersections in (2.1) pass all of (2.3); marginal nonemptiness is
insufficient.

#### Proof

Every solution of (2.2) is contained in every target of every row using
`p`, so `D_p subseteq Q_p subseteq K_p`.  This proves the first condition
and nonemptiness.  Equation (2.2) gives `E_R subseteq S_R`, while every
incident `K_p subseteq S_R`; hence
`E_R union union K_p subseteq S_R`.  The reverse containment follows from
`Q_p subseteq K_p` and (2.2).  Conversely, (2.3) makes `Q_p=K_p` a nonempty
cap-legal solution of every row and respects the lower bound.  \(\square\)

For screen support at an existing position `s`, put the desired screen
`S_scr` into the lower bound `D_s`.  This requires

\[
                         S_{\rm scr}\subseteq D_s
                              \subseteq K_s.                 \tag{2.4}
\]

It does **not** replace the old ambient letter by `S_scr`.  In the audited
zero-charge realization the pre-existing letter `H` is unchanged and
contains the screen; algebraically one takes `D_s=P_s=H`.  No position is
added, so `chi=0`, but every owner, compiler, protected, and `q1` row
containing `s` remains in (2.1)--(2.3).  Zero length is not zero cap
footprint.  In particular every selected target row crossing `s` must
contain the whole ambient letter `H`, not merely the smaller abstract
screen.

### Proposition 2.2 (cap feasibility is not a matroid before the state is fixed)

At one live source position take cap `{a,b}` and three distinct rows

\[
\begin{array}{c|c|c}
 &E_R&S_R\\ \hline
 e_1&\{c\}&\{a,c\}\\
 e_2&\{d\}&\{a,d\}\\
 e_3&\varnothing&\{b\}.
\end{array}                                                \tag{2.5}
\]

The sets `{e_1,e_2}` and `{e_3}` are feasible, but neither `e_1` nor `e_2`
can be added to `{e_3}`.  Thus the feasible row subsets have maximal members
of sizes two and one and violate the matroid exchange axiom.

#### Proof

The first two rows use `Q_s={a}` and the third uses `Q_s={b}`.  Every mixed
choice has empty intersection in (2.1).  \(\square\)

Consequently no transversal-matroid or Hall calculation may be performed on
the union of individually legal cap options.  First fix a complete cap
state satisfying (2.3), or prove a separator which makes the cap choices
Cartesian.

## 3. Mandatory return addresses and forced-edge Hall

Let `Phi` be a global address isomorphism.  Let

\[
              F^+=\{(T_i,b_i):1\le i\le q\}                  \tag{3.1}
\]

be the mandatory packet compiler assignments in the new word: ray returns,
cut-target returns, and any sidecar which actually consumes a compiler cell.
One abstract folded antidiagonal ticket contributes its two physical ray
assignments separately to (3.1); their constant intersection/union cap does
not merge their cell capacities.
Assume `T_i in L` and that the `T_i` and `b_i` are separately distinct.
Genuinely new tasks not lying in the old target bank must instead be added
to the new residual Hall problem.  Pull the displayed returned targets back by

\[
              a_i=\Phi^{-1}(b_i),\qquad
              F^-=\{(T_i,a_i):1\le i\le q\}.                 \tag{3.2}
\]

Because `Phi` preserves cell type, `F^-` consists of legal old incidences
exactly when `F^+` consists of legal new incidences on that typed face.

Let `H^-=(L,C^-;E^-)` be the old occurrence compiler graph in one complete
matching-closed cap state.  Write `I={T_1,...,T_q}` and
`A={a_1,...,a_q}`.

### Theorem 3.1 (forced-address extension theorem)

There is a complete old graph matching containing `F^-`, and hence by `Phi`
a complete new graph matching containing `F^+`, if and only if

\[
 \lvert N_{H^- - A}(Y)\rvert\ge\lvert Y\rvert
                     \qquad(Y\subseteq L\setminus I).        \tag{3.3}
\]

The new graph matching is collision-free with every mandatory packet
address.  It is a literal common-`Q` matching exactly when its complete row
family passes Theorem 2.1.  If (3.3) fails, a violating `Y` is an exact
ambient rank-cut certificate even before that cap test.

#### Proof

After fixing `F^-`, its targets and cells cannot be used again.  Extending
it is therefore exactly the problem of matching `L\setminus I` into
`C^-\setminus A`, and Hall's theorem gives (3.3).  Apply Theorem 1.1 to the
resulting complete old matching.  Its forced edges map to (3.1), and all
other images avoid the `b_i` because `Phi` is injective.  The final
common-`Q` qualification is Theorem 2.1.  \(\square\)

This is the minimal ambient condition missing from a local return
bijection.  If no return address is prescribed, take `q=0`; every old
matching transports automatically.  If only a packet-local bijection is
known and no global `Phi` is available, apply Hall directly in the new graph
after deleting the packet targets and cells.

### Corollary 3.2 (packet-local lift)

First fix one complete compatible cap/guard state `theta` and its old/new
typed incidence graphs.  Suppose their complete type fibres are balanced
and a physical packet supplies a type-preserving partial address bijection
`beta` in that state.  Label selected domain cells `a_i` by returned targets
`T_i`, assume both `T_i-a_i` and `T_i-beta(a_i)` are legal in `theta`, and
require the latter assignments.  Then the packet-local return extends to a
collision-free ambient graph matching if and only if the forced old edges
`T_i-a_i` satisfy (3.3).  The resulting row family is literal common-`Q` if
and only if it passes Theorem 2.1.

#### Proof

Lemma 1.2 extends `beta` to `Phi`; Theorem 3.1 applies.  \(\square\)

### Corollary 3.3 (exact matroid/outer-state decomposition)

For fixed compatible cap state `theta` and forced packet bank `F`, let
`M_{theta,F}` be the transversal matroid on `L\setminus I` represented by
the residual cell bank `C^-\setminus A`.  Then

\[
 \delta_{\theta,F}
   =|L\setminus I|-r_{M_{\theta,F}}(L\setminus I)
   =\max_{Y\subseteq L\setminus I}
      \bigl(|Y|-|N_{H^- -A}(Y)|\bigr)_+.                    \tag{3.4}
\]

If several packet address maps or cap states are allowed, the exact optimum
is

\[
                  \min_{(\theta,F)\ \mathrm{compatible}}
                              \delta_{\theta,F}.             \tag{3.5}
\]

The minimum in (3.5) is outside the matroid rank.  Proposition 2.2 shows why
the cap states cannot in general be unioned before taking the rank.

### Proposition 3.4 (full-block refinement makes ambient Hall automatic)

Suppose the new source word is obtained by replacing selected old letters
by consecutive nonempty blocks with the same union.  Map every old interval
to its full-block lift.  Assume every lifted old matching cell preserves all
required incidence data—literal target, permitted width/grade, deadline,
and every guard.  Let `F^+` be a legal injective literal matching of a target
set `I subseteq L` into certified side cells, each proved not to lie in the
full-block-lift image, and delete from the old matching the edges on `I`.
Then

\[
            F^+\ \cup\ \Phi_{\rm full}(M\upharpoonright(L\setminus I))
                                                                  \tag{3.6}
\]

is a collision-free complete target--cell matching.  No residual Hall test
is needed.

#### Proof

Full-block lifting is injective and preserves the literal OR of every old
interval.  By definition no side cell belongs to its image.  Thus the two
cell banks in (3.6) are disjoint; deleting the old edges on `I` also makes
their target banks disjoint.  \(\square\)

This proposition is the active positive simplification for the native
split-host construction.  A two-phase common cap and every `q1`/owner row
still have to pass Theorem 2.1 and Section 6.  Theorems 3.1 and 4.1 are
needed only when one of Proposition 3.4's transport/private-side-cell
hypotheses fails.

### Theorem 3.5 (full-block background cap decoupling)

In the setting of Proposition 3.4, regard every old source position touched
by a transported background row as a block.  A refined old letter `A_p` is,
in phase `epsilon`, a same-length block

\[
       B_p^\epsilon=(B_{p,1}^\epsilon,\ldots,
                      B_{p,\ell_p}^\epsilon),
       \qquad \bigcup_jB_{p,j}^\epsilon=A_p.                 \tag{3.7}
\]

Use phase-common piece caps

\[
              P_{p,j}=B_{p,j}^0\cup B_{p,j}^1
                        \subseteq A_p.                       \tag{3.8}
\]

An unrefined position is the one-piece case `ell_p=1`; its actual old
letter must remain fixed, or its maximal piece must separately satisfy the
same contraction equation below.

Assume every background row is transported by full-block lift.  Then the
background rows do not shrink any cap (3.8): for every such row containing
the block, its target contains `A_p`, hence contains every `P_{p,j}`.

Consequently, let `K_{p,j}^P` be the maximal piece letters imposed by the
packet/owner/`q1` rows alone.  The packet state glues to **all** transported
background rows if and only if it passes its packet rows and, for every
transported background row `R`,

\[
 E_R\cup
   \bigcup_{p\in J_R}\bigcup_{j=1}^{\ell_p}K_{p,j}^P=S_R.
                                                                  \tag{3.9}
\]

In particular the blockwise contraction equations

\[
                         \bigcup_jK_{p,j}^P=A_p              \tag{3.10}
\]

for every block touched by a background row, including every one-piece
unrefined block, are sufficient, and make every background equation
automatic.  Thus a contraction-exact full-block packet has neither an
ambient matching collision nor an ambient source-cap conflict.

#### Proof

A full-block lifted row either avoids the refined block or contains all its
pieces.  In the latter case its old target contains the old letter `A_p`,
so intersecting that target into (2.1) leaves every cap `P_{p,j}` unchanged.
The joint maximal piece is therefore exactly the packet maximal piece.
The maximal-word reconstruction theorem reduces the background equations
to (3.9).  Equation (3.10) restores the old contribution of every refined
or one-piece letter touched by the row and hence every old row.  \(\square\)

Failure of (3.10) is the precise way a nominal full-block source split can
still lose common-`Q` after packet rows are imposed.  Pointwise containment
of all pieces is weaker than blockwise contraction exactness.

### Corollary 3.6 (canonical two-host background closure)

Suppose the folded ray hosts are actual old letters `X_L,X_R` and the two
phases refine them in the canonical orders

\[
        X_L\longmapsto(X_L,L_\epsilon),\qquad
        X_R\longmapsto(R_\epsilon,X_R),                     \tag{3.11}
\]

where `L_epsilon subseteq X_L` and `R_epsilon subseteq X_R`.  Suppose the
local ray rows force exactly the displayed pieces and all full-block lifts
remain admissible, and every other source position used by a transported
background row is frozen at its old letter.  Then

\[
       X_L\cup L_\epsilon=X_L,qquad
       R_\epsilon\cup X_R=X_R,                              \tag{3.12}
\]

so (3.10) holds in both phases.  The old matching transports on full-block
cells, the `2d-2` ray assignments use private side cells, and all transported
background cap rows reconstruct automatically.

Thus, conditional on literal owner-legal placement of these two old host
letters, the folded ray bank has no separate ambient compiler/Hall gate.
The remaining obligations are the host-owner/residence geometry, the typed
`q1` sidecar seams, admissible deadlines, the recycled screen halo, and
regenerative contraction.

#### Proof

Equations (3.12) give blockwise contraction exactness.  Apply Proposition
3.4 and Theorem 3.5.  \(\square\)

## 4. Exact alternating-linkage form relative to the old matching

The forced-edge criterion can be tested without forgetting a named old
matching.  Start with an old complete matching `M`.  Delete from `M` every
edge incident with `I` or `A`, and call the remaining matching `M_0` in

\[
 H_0=H^-[(L\setminus I),(C^-\setminus A)].                   \tag{4.1}
\]

Let `D` be the targets of `L\setminus I` unmatched by `M_0`, and let `U`
be the cells of `C^-\setminus A` unmatched by `M_0`.  Orient every
nonmatching edge target-to-cell and every edge of `M_0` cell-to-target.
Let `lambda(D,U)` be the maximum number of pairwise vertex-disjoint directed
paths from distinct vertices of `D` to distinct vertices of `U`.

### Theorem 4.1 (old-matching linkage criterion)

The mandatory return bank is compatible with some exchange of the old
matching if and only if

\[
                             \lambda(D,U)=|D|.               \tag{4.2}
\]

More generally its exact residual matching deficiency is

\[
 \delta=|D|-\lambda(D,U)
       =\max_{Y\subseteq L\setminus I}
          \bigl(|Y|-|N_{H^- - A}(Y)|\bigr)_+.                \tag{4.3}
\]

#### Proof

If (4.2) holds, reverse the matching status along all the vertex-disjoint
paths.  Every target in `D` becomes matched, no previously matched target
becomes unmatched, and the endpoints in `U` are distinct.  This extends
`M_0` to a matching of the required size.

Conversely, take a maximum matching in `H_0` and compare it with `M_0`.
Their symmetric difference decomposes into alternating paths and cycles.
Every unit of net cardinality gain is one `M_0`-augmenting component from a
target of `D` to a cell of `U`; these components are vertex-disjoint.  A
maximum comparison may be chosen with no component having one more `M_0`
edge, since replacing the comparison edges on such a component by the
`M_0` edges would increase the comparison matching.  Conversely every
vertex-disjoint `D`--`U` path family augments simultaneously.  Thus the
maximum gain is `lambda(D,U)`.  Hall's deficiency formula gives the second
equality in (4.3).  \(\square\)

The alternating paths may leave the packet collar.  Bounded rank does not
imply local linkage.

## 5. Two sharp insufficiency examples

### Example 5.1 (address collision / Hall failure)

Take targets `{x,y}` and old cells `{a^-,b^-}` with incidences

\[
 x\sim\{a^-,b^-\},\qquad y\sim\{a^-\}.                    \tag{5.1}
\]

Its unique complete matching is `x-b^-,y-a^-`.  Let the new graph be the
transported typed copy on cells `{a^+,b^+}`, with global address isomorphism
`Phi(a^-)=b^+`, `Phi(b^-)=a^+`.  Thus in the new graph
`x` sees both cells and `y` sees only `b^+`.  Suppose a packet forces the
perfectly valid one-row return

\[
                             F^+=\{x-b^+\}.                  \tag{5.2}
\]

The pulled-back forced edge is `x-a^-`.  After reserving `a^-`, the residual
Hall cut `Y={y}` has empty neighbourhood, so no complete matching contains
the forced edge.  Thus even a global type isomorphism and a legal local
return do not imply compatibility with prescribed return addresses.  The
missing condition is exactly forced-edge Hall.

This two-target example is minimal for a collision between a mandatory
packet cell and a different background target.

### Example 5.2 (source-cap conflict without a cell collision)

Use three distinct cells for the three rows (2.5).  Their target--cell
assignment is a matching and every edge is individually cap-legal.  Yet the
joint row family containing `e_3` and either of the first two has empty
source intersection.  Hence even a complete local address matching plus
ordinary Hall can fail common-`Q`.

These examples establish the necessity of both arrows in (0.2).

### Example 5.3 (nonempty piece caps do not imply contraction exactness)

Let one old source letter and one transported background target both be
`A={a,b}`.  Refine the letter into two capped positions, but let packet rows
force maximal letters

\[
                              K_1=K_2=\{a\}.                 \tag{5.3}
\]

Both positions remain nonempty and every packet containment may hold, yet
the full-block background row reconstructs only `{a}`, not `{a,b}`.  Thus
Theorem 3.5's union condition (3.9), and in particular the convenient
contraction condition (3.10), cannot be replaced by pointwise nonemptiness.

## 6. `q1` sidecars and zero-charge screen recycling

Let `E^- ,E^+` be the multisets of changed owner edges in the two phases,
and let `S^- ,S^+` be the old/even and new/odd sidecar edge multisets.  Put
`q_down(PQ)=P cap Q` and `q_up(PQ)=P union Q`.  The sidecar is exact
precisely when

\[
\begin{aligned}
 q_\downarrow(E^-\uplus S^-)&=q_\downarrow(E^+\uplus S^+),\\
 q_\uparrow(E^-\uplus S^-)&=q_\uparrow(E^+\uplus S^+),
                                                                  \tag{6.1}
\end{aligned}
\]

as occurrence multisets on a rainbow shore, or as supports when only
coverage is required.  Their physical edge occurrences must be injective
and must avoid every retained edge occurrence of the same resource sort.
All source positions used by those edges enter the packet row family in
Theorem 2.1.

For the folded upper-safe cut, (6.1) initially asks for only the lost lower
cut colour `chi`; the aligned cut also asks for its one upper casualty.  A
recycled common screen supplies `chi=0` **length charge** when it is an
already existing immediate-left source occurrence.  This notation must not
be confused with the lower cut colour, customarily also denoted `chi` in
some notes.  The recycled source occurrence remains present in:

1. every interval address which crosses it;
2. every owner and `q1` row which uses it;
3. the cap intersections (2.1); and
4. every address-specific guard record in (1.1).

The separate exact sidecar theorem
`MATH_THEOREM_R_FOLDED_C8_ADDRESSED_RETURN_AND_LOWER_C8_SIDECAR_GATE_20260801.md`
constructs an eight-owner alternating `C8` whose lower occurrence map
returns the two aligned rail casualties and whose upper occurrence counter
is unchanged.  Its explicit old-even/new-odd address maps are (3.8) and
(3.10) of that theorem.  All eight abstract owners are distinct.  Therefore
(6.1) is already closed algebraically for that aligned rail.  What remains
for this note is exactly to place all eight declared old/new edge
occurrences—especially the four new seams—with legal residence/source-cap
halos and include their rows in (2.1); distinct owners and zero signed owner
count do not make those seams physically free.

If, in a different proposed construction, its value is changed from `A_s`
to the screen `S`, an old matched interval `J` containing it preserves its
same-address literal OR exactly when

\[
       E_J\cup A_s=E_J\cup S,                              \tag{6.2}
\]

where `E_J` is the union of the other letters of `J`.  Every failure of
(6.2) says only that this same-address interval fails OR transport; full
transport still requires its cap and guard rows.  Such a failure enters the
set `D` of Theorem 4.1 only after that old matching edge is deleted from
`M_0`; a different admissible transport may avoid it.  This replacement is
**not** the audited zero-charge mechanism.  In the frozen audit the
ambient left occurrence `H` is common and unchanged in both words, so the
global fibre bijection already incorporates it; (6.2) then holds
tautologically with `A_s=S=H`.

## 7. Exact folded-C8 closure criterion

Fix one of the audited screened folded-C8 endpoint pairs and its global
width/core/cap address bijection `Phi`.  Let `F^+` contain every mandatory
two-ray return and every compiler-cell sidecar.  Let the lower/upper edge
sidecars be typed separately.  Then the endpoint has a literal ambient
compiler extending an old occurrence matching if and only if there is one
complete phase-compatible state for which:

1. the owner and residence rows are legal;
2. the coupled lower/upper `q1` equations (6.1) hold on one pair of
   old/new sidecar edge banks, with an explicit type-preserving bijection of
   the complete old/new occurrence shores and legal physical placement of
   every declared edge;
3. the joint background/packet/screen cap equations (2.3) hold;
4. every mandatory return **and every transported residual matching edge**
   preserves the full guard type (1.1), or the complete address bijection
   preserves `gamma` fibrewise; and
5. either Proposition 3.4 applies, or the forced-edge Hall inequalities
   (3.3), equivalently the linkage equality (4.2), hold.

For a reusable two-phase endpoint, the two states must share the declared
separator, screen occurrence, and pointwise cap state.  Their residual
graphs may not be unioned.  Regeneration additionally requires that
contraction returns the same typed separator state.

If the two endpoint phases may use different compiler matchings, apply
(3.3) separately inside those two compatible cap states.  If a construction
requires one old matching to transport to both endpoints, pull both forced
banks back to the common old graph: their union must first be a partial
matching, and (3.3) is then applied once to that union.  Two separately
extendable forced banks need not have a common extension.

On the unguarded core/cap face with no prescribed return addresses, the
frozen global `Phi` makes item 5 automatic: transport any old matching.  In
the stronger full-block refinement, private side cells make it automatic
even with the prescribed ray returns.  Only a non-refinement or
nonprivate/guard-filtered planting invokes the old-graph forced-edge Hall
test.  Thus the fallback missing datum is smaller than a new global compiler
search but stronger than the two-ray antitone count:

> certify the pulled-back forced edges of the physical ray/sidecar bank,
> their exact `q1` occurrence rows, and the common cap/guard state in which
> (3.3) is evaluated.

No scalar marginal, signed deck equality, or packet-local injection can
replace these data.

## 8. Independent audit checklist

The decisive implications use the following hypotheses, each separately.

* `Phi` is global on all matching cells, not merely on the changed packet.
* Literal OR core, not only target support, is preserved.
* Any relevant address guard is preserved or checked edge by edge.
* Mandatory packet assignments are pulled back before Hall is tested.
* Cap options are fixed before their compiler graphs are optimized.
* `q1` edge occurrences and compiler interval occurrences are different
  capacity sorts unless a construction explicitly identifies them.
* Recycled-screen charge zero refers only to word length.

Dropping the fourth bullet gives Example 5.1; dropping the fifth gives
Example 5.2.  The proof of Theorem 4.1 is independently checkable by the
standard symmetric-difference decomposition and does not use any finite
search.
