# The `K17` multipath carrier forces one facet rail and a guarded socket debt

Date: 2026-07-31  
Status: exact dimension-uniform reduction and solver-free `K17` consequences;
no radius-one path CNF, `K17` word, or all-dimension construction is claimed

## 0. Result

Put

\[
             W={17\choose8}=24310,
             \qquad L=W+3=24313.
\]

The exact radius-one census closes the direct Hamilton-path route more
strongly than non-isolation.  Among the `1430` occurrence neighbours of the
six-swap state, `1411` are residence-clean and `122` have no isolated marked
component, but none is connected and none passes the Hamilton-path degree
necessity.  The minimum forced-leaf count is `21`, and the best component
shapes are `102+2+2` and `103+2+2`.

For a **three-path** carrier the correct solver-free consequence is:

\[
 \boxed{\text{every radius-one state needs at least eight
 outside-catalogue adjacency units}.}                 \tag{0.1}
\]

Thus the twelve three-component frontier states are only radius-two roots;
having three weak components does not give a three-path cover.  No one of the
`122` path CNFs should be run.

The downstream depth-two schedule has a second, independent rigidity.  In a
length-`W+1` rank-eight/rank-nine row which displays every missing rank-nine
owner in its first derivative, all rank-eight occurrences necessarily form
one contiguous **facet rail**.  If the marked owner bank consists of `p`
Johnson paths, then at least `p-1` rank-eight colours are not supplied either
by the direct facet rail or by internal marked turns.  They are compulsory
socket/palette debts.

For the authenticated three-path fallback, direct replay gives

```text
marked owner tokens                         5810
internal marked turns                       5807
distinct internal rank-eight colours        5807
complement owners                           18500
required direct facet slots                 18501
minimum socket/palette debts                    2
all residual lower targets                  47034
short-cell slack                              1591
```

Hence its marked side is optimally squarefree: exactly two additional colours
are necessary.  This does **not** construct the complementary rail.  The
remaining rail gate is an exact connected pair-column system on `18501`
facets and `18500` complement owners.

Once all sockets and the final depth-two row are fixed occurrence by
occurrence, the earlier common-cap obstruction theorem survives unchanged:
the residual clutter has rank at most three.  Before sockets are fixed this
is false in general; one atomic variable socket can already create a minimal
rank-four cap obstruction.  A connector/socket choice may therefore be
separated from the lower compiler only on a common permanent-bit/host face.

The exact live interface is consequently

\[
 \boxed{
 \begin{array}{c}
 \text{three-path connector or compensated outside adjacencies}\\
 +\ \text{one connected facet rail and two designated debt colours}\\
 +\ \text{global envelope/deep-provider replay}\\
 +\ \text{socket-conditioned port completion}\\
 +\ \text{one guarded common-cap Hall matching}.
 \end{array}}                                         \tag{0.2}
\]

An actuator may be charged to both (0.1) and the two palette debts only when
one literal signed certificate proves both services.  Geometric overlap or
scalar neutrality is not such a certificate.

## 1. A `p`-path actuator lower bound

Let `G` be the undirected projection of a standard clean connector catalogue
on `n` marked objects.  Write

* `c(G)` for its number of weak components;
* `z(G)` for its number of isolated vertices;
* `ell(G)` for its number of vertices of degree exactly one; and
* `B_G` for the tail--head bipartite projection of the directed catalogue.

An **outside adjacency unit** is one edge of a proposed path cover not
present in `G`.  A compound physical packet may export several such units,
but its literal resources and currents are then charged once as a compound
column.

### Theorem 1.1 (`p`-path actuator bound)

If a spanning union of `p` vertex-disjoint paths uses `q` outside adjacency
units, then

\[
 q\ge
 \max\left\{
 0,
 c(G)-p,
 z(G)+\left\lceil{\ell(G)\over2}\right\rceil-p,
 n-p-\nu(B_G)
 \right\}.                                           \tag{1.1}
\]

In particular, a direct `p`-path cover can exist only if

\[
 c(G)\le p,qquad
 z(G)+\left\lceil{\ell(G)\over2}\right\rceil\le p,
 \qquad \nu(B_G)\ge n-p.                             \tag{1.2}
\]

#### Proof

Delete the `q` outside edges from the proposed `p`-path forest.  The result
has at most `p+q` path components, all using edges of `G`.  Every isolate of
`G` is a singleton component.  Each remaining `G`-path contains at most two
degree-one vertices of `G`: such a vertex cannot be internal in a path made
of `G`-edges.  Therefore

\[
       \ell(G)\le2\bigl(p+q-z(G)\bigr),
\]

which is the third term in (1.1).  An outside edge reduces the number of
weak components by at most one, proving the second term.

The directed `p`-path forest has `n-p` arcs with distinct tails and distinct
heads.  Its standard arcs form a matching in `B_G`, so at most `nu(B_G)` of
them can be standard.  This proves the last term.  \(\square\)

The familiar Hamilton-path bound is the case `p=1`.  The isolate-sensitive
form in (1.1) is stronger than counting all degree-at-most-one vertices as
interchangeable endpoints.

### Corollary 1.2 (the exact radius-one rebase)

Every no-isolate radius-one state has `ell(G)>=21`.  For `p=3`, (1.1) gives

\[
       q\ge\left\lceil{21\over2}\right\rceil-3=8.    \tag{1.3}
\]

For a direct cover, (1.2) gives `p>=11`.  Thus a weak-component shape
`102+2+2` is not a three-path certificate.

The displayed seventh-swap state has `z=0`, `ell=22`, and three weak
components, so its direct path-cover number is at least `11`, and a
three-path completion needs at least `8` outside units.  The frozen six-swap
graph has one isolate and `23` degree-one vertices, so its direct path-cover
number is at least `13`; a three-path completion there needs at least `10`
outside units.

Accordingly, a radius-two state should not reach a path model until it
passes all three eager cuts in (1.2) with `p=3`.  The twelve radius-one
three-component states pass only the first of those cuts a priori.

## 2. Facet-rail rigidity

Let

\[
       \mathcal V_8={ [17]\choose8},
       \qquad \mathcal V_9={ [17]\choose9}.
\]

Consider a linear row

\[
                 Z=(Z_0,\ldots,Z_W)                  \tag{2.1}
\]

whose entries have rank eight or nine.  Suppose its `a` rank-nine entries
are distinct.  Call their set `P`, and put

\[
              Q=\mathcal V_9\setminus P,
              \qquad |Q|=W-a,
              \qquad f=W+1-a.                        \tag{2.2}
\]

The row is **owner-tight** if every owner in `Q` occurs in `DZ` as the union
of two consecutive rank-eight entries.

### Theorem 2.1 (one-facet-rail theorem)

In every owner-tight row (2.1), all `f` rank-eight occurrences form one
contiguous run.  Moreover every one of its `f-1=W-a` internal adjacent pairs
has a distinct union, and those unions are exactly `Q`.

#### Proof

Suppose the rank-eight occurrences form `q` nonempty runs.  They have only
`f-q` rank-eight/rank-eight adjacencies.  A pair of distinct direct
rank-nine entries has union rank at least ten.  A rank-nine/rank-eight pair
has rank-nine union only when that union is the same direct rank-nine set;
it cannot produce an owner in `Q`.  Hence all `W-a` owners in `Q` require
rank-eight/rank-eight adjacencies.  Therefore

\[
             W-a\le f-q=W+1-a-q,
\]

so `q<=1`.  Since `f>0`, `q=1`.  Equality throughout forces every internal
facet adjacency to be used once and its owner labels to be distinct.  \(\square\)

The theorem does not by itself make the facet occurrences distinct.  Direct
palette injectivity is an additional compiler requirement.

For a linear opening the unique facet rail may meet one endpoint of (2.1),
or it may be internal.  Thus the owner entries occupy one boundary-spanning
rail in the cyclic picture, but may appear as two end blocks in the literal
linear row.  This endpoint nuance does not change the palette count below.

## 3. The invariant `p-1` palette debt

Assume the direct owner set `P` is partitioned into `p` Johnson paths.  Their
internal edge intersections give exactly `a-p` turn-colour occurrences.
Let `C` be the set of distinct such colours, let `F` be the set of distinct
direct rank-eight entries of `Z`, and write `d=|F|<=f`.

The rank-eight colours outside `F` number `W-d`.  At most `|C\setminus F|`
of them are identified by internal marked turns.  Define the remaining
socket/palette debt by

\[
       \sigma=(W-d)-|C\setminus F|.                  \tag{3.1}
\]

### Theorem 3.1 (multipath palette bound)

Every `p`-path owner skeleton satisfies

\[
       \boxed{\sigma\ge p-1+(f-d).}                  \tag{3.2}
\]

Equality holds precisely when all `a-p` internal turn occurrences have
distinct colours and none is a direct facet colour.

#### Proof

We have `|C\setminus F|<=a-p`, so

\[
 \sigma\ge W-d-a+p
          =(W+1-a-d)+(p-1)
          =(f-d)+(p-1).
\]

Equality is exactly `|C\setminus F|=a-p`, which says that the internal
occurrences are injective and avoid `F`.  \(\square\)

Thus an injective facet rail has at least `p-1` additional residual
rank-eight colours.  Equivalently, lowering `p` complementary owner gaps
separately would use

\[
          \sum_{j=1}^p(|Q_j|+1)=W-a+p              \tag{3.3}
\]

facet occurrences, whereas an optimal row has only `W+1-a`; exactly `p-1`
occurrences must be coalesced or rethreaded.

This is an invariant debt, not a claim that there are literally `p-1`
independent word cells.  If the facet rail is internal, one extra
owner/facet interface can replace one owner/owner phase join.  The total
number of extra interface/palette obligations remains `p-1`.

## 4. Exact facet-rail master

Suppose now that the marked turn colours are injective.  Choose a debt set

\[
       \Gamma\subseteq\mathcal V_8\setminus C,
       \qquad |\Gamma|=p-1,                          \tag{4.1}
\]

and put

\[
       A=\mathcal V_8\setminus(C\cup\Gamma).
                                                               \tag{4.2}
\]

Then `|A|=W-a+1=|Q|+1`.  For `U in Q` and distinct `R,S in A` with
`R,S subset U`, introduce a binary pair-column `x_(U,{R,S})`; introduce an
endpoint bit `e_R` for every `R in A`.

### Theorem 4.1 (owner-labelled facet path)

There is one facet rail on vertex set `A` whose edges are labelled
bijectively by `Q` if and only if the following integral system is feasible:

\[
 \sum_{\{R,S\}\subseteq {U\choose8}\cap A}
       x_{U,\{R,S\}}=1
       \qquad(U\in Q),                               \tag{4.3}
\]

\[
 \sum_{U,\,\{R,S\}\ni R}x_{U,\{R,S\}}=2-e_R
       \qquad(R\in A),
 \qquad
 \sum_{R\in A}e_R=2,                               \tag{4.4}
\]

and, for every nonempty proper `X subset A`,

\[
 \sum_{\substack{U,\{R,S\}:\\|\{R,S\}\cap X|=1}}
       x_{U,\{R,S\}}\ge1.                          \tag{4.5}
\]

Any required endpoint containment at the one or two owner/facet interfaces
is imposed by restricting which `e_R` may equal one.

#### Proof

A rail chooses one adjacent facet pair for every complement owner, giving
(4.3).  Its internal vertices have degree two and its two ends degree one,
giving (4.4).  Connectivity gives (4.5).

Conversely, (4.3) selects `|Q|` edges on `|Q|+1` vertices.  Equations (4.4)
give maximum degree two and exactly two degree-one vertices.  The cuts (4.5)
make the selected graph connected.  It is therefore one path, and the
unique owner label on each selected edge gives the required rail.  \(\square\)

This is the exact complement gate.  Ordinary marginal port `b`-flow does
not imply (4.5), and a connected rail does not by itself prove residence,
deep-shadow coverage, or a common cap.

## 5. Calibration on the authenticated three-path fallback

The frozen clean-atom witness has `p=3` and `a=5810`.  A read-only replay of
its three literal owner paths gives

```text
internal adjacencies                 5807
distinct intersections               5807
intersection-rank set                  {8}
```

Thus its internal marked colours are exactly squarefree.  The ideal direct
rail ledger is

\[
 |Q|=W-a=18500,\qquad f=18501,\qquad |\Gamma|=2.   \tag{5.1}
\]

The two non-Johnson joins already isolated in the frozen theorem are the two
natural phase locations, but (5.1) does not prove that they realize the two
colours in `Gamma`.  A valid construction must choose `Gamma`, solve
(4.3)--(4.5), and physicalize both phase interfaces with the same palette.

If the final row has `5810` distinct rank-nine entries and `18501` distinct
rank-eight entries, then

\[
 \begin{aligned}
 \text{residual rank-eight targets}&=5809,\\
 \text{all residual lower targets}&=41224+5810=47034,\\
 \text{singleton/pair cells}&=48625,\\
 \text{scalar slack}&=1591.
 \end{aligned}                                      \tag{5.2}

This positive slack does not decide the rail or the common-cap matching.

For a general clean component bank with `s` components and `tau` internal
owner tokens, a direct `p`-path cover uses `s-p` one-owner connectors.  If
physical sockets contribute a net `delta` additional rank-nine depth-two
tokens, then

\[
                    a=\tau+s-p+\delta.               \tag{5.3}

The value of `delta` is a literal socket output, not a topological constant.
For example, a direct non-Johnson concatenation has `delta=0`; a one-owner
replacement socket has `delta=1`.  Consequently neither `3903` nor `3905`
may be asserted for the seven-swap route before its physical sockets exist.
The immutable pre-join number there is `3800`.

## 6. Exact multi-socket common-cap guard

Let a final socketed row `Z` of length `W+1` be fixed.  Assume it passes the
exact maximal-envelope inversion test and

\[
               |Z_i\cup Z_{i+1}|\ge9                \tag{6.1}

for every adjacent pair.  Let `d_(<=8)` be the number of **distinct** final
rows of `Z` which are nonempty lower targets.  Suppose fixed socket prepins
reserve `c` distinct singleton/pair cells and discharge `t` distinct
residual targets.

### Theorem 6.1 (fixed-socket compiler ledger)

After the fixed prepins, the residual short-cell slack is exactly

\[
       \boxed{d_{\le8}-16910-(c-t).}                 \tag{6.2}

All residual common-cap obstructions still have rank at most three.

#### Proof

There are `65535-d_(<=8)` lower targets not displayed directly by `Z`.
Condition (6.1) implies that no such target occurs in an interval of length
at least three: a length-three interval is one row of `Z`, and a longer one
contains two adjacent rows.  After prepins the number of targets is
`65535-d_(<=8)-t`, while the number of available singleton/pair cells is
`48625-c`.  Their difference is (6.2).

Fold every fixed socket cap into the maximal position caps before selecting
the remaining target cells.  Only three short cells meet one position, a
depth-two row has three hosts, and a selected singleton/pair target has at
most two hosts.  The exact bad-pair/bad-triple proof therefore applies
unchanged.  \(\square\)

For the intended injective rank-eight/rank-nine profile,
`d_(<=8)=W+1-a`; hence (6.2) is

\[
               7401-a-(c-t).                        \tag{6.3}

A socket with `c=t` is scalar-neutral.  A duplicated direct facet or a short
cell consumed without discharging a distinct target costs one unit.

### Lemma 6.2 (exact collar influence)

If a socket changes `Z` only on a row set `I`, it can change maximal envelope
letters only on

\[
             H(I)=I+\{0,1,2\},                      \tag{6.4}

and depth-two replay equations only on

\[
             K(I)=I+\{-2,-1,0,1,2\}.                \tag{6.5}

It can change a long interval witness `[r,s]`, `s-r+1>=3`, only when its
depth-two footprint `[r,s-2]` meets `I`.

#### Proof

The envelope at position `p` is the intersection of the rows
`Z_(p-2),Z_(p-1),Z_p`, with endpoint truncation.  This proves (6.4).
A row replay uses three consecutive envelope letters, proving (6.5).
Finally, the OR of a long interval is the union of the `Z` rows in its
depth-two footprint.  \(\square\)

Supports whose replay halos `K(I)` are disjoint compose by independent local
checks; for ordered interval supports this holds when the next support
starts at least five rows after the preceding support ends.  A sharper
runwise statement is also available: if every single-collar modification is
globally invertible against the same baseline, separation by at least four
rows suffices.  Separation three is false in general: deleting one bit at
rows `1` and `4` of an all-one trace is harmless one deletion at a time but
together traps a strict internal run of length two.

For every required upper/deep target, retain one provider whose footprint
avoids all socket supports, or replay an explicit replacement provider in
the final `Z`.  Counting old providers without their footprints is not a
valid preservation argument.

## 7. When sockets may be selected before Hall

Let `Omega` be a family of physical socket configurations.  The following
is a sufficient **common guarded face**.

1. Every option has the same direct lower palette, residual target set, and
   unused short-cell bank.
2. At each position `p` there is a permanent bit `g_p` contained in every
   option's capped envelope and in every retained candidate label whose cell
   meets `p`.
3. Every bit of every depth-two row and fixed socket prepin has one common
   host which is preserved by every option and by every retained candidate
   covering that host.
4. For every retained target--cell candidate and every bit of its target,
   there is one common anchor host preserved by every compatible candidate.
5. The one common residual target--cell graph satisfies Hall.

### Theorem 7.1 (guard-neutral socket separation)

Under conditions 1--5, every target-saturating matching in the common graph
is an exact common-cap compiler for every socket option in `Omega`.

#### Proof

The permanent bits keep every letter nonempty.  The common row and prepin
hosts preserve the final depth-two row and all fixed short occurrences.  The
anchor hosts preserve every bit of every selected residual target against
all other selected caps.  Thus the maximal intersection word realizes all
declared rows.  Hall supplies a target-saturating matching.  \(\square\)

If any of these common intersections or hosts is empty, socket and compiler
columns must be selected jointly.  The rank-three statement of Theorem 6.1
does not apply to an unfixed socket treated as one atomic choice.  Indeed,
at one position with envelope `{1,2,3,4}`, take three short-cell labels

\[
 \{2,3,4\},\quad\{1,3,4\},\quad\{1,2,4\}
\]

and one socket cap `{1,2,3}`.  Every proper subfamily has nonempty
intersection, but all four intersect trivially.  This is a minimal
rank-four obstruction.  Separate local Hall tests and pairwise socket tests
are therefore insufficient.

## 8. The exact dual-service socket signature

Every physical socket packet used in a three-path construction must export
at least

\[
 \Gamma(S)=
 \left(
 I_S,
 \Delta|Z|,
 \Delta a,
 \Delta d_{\le8},
 \Delta F,
 \Delta Q,
 \partial_S,
 \mathcal P_S,
 \mathcal W_S,
 \mathcal G_S
 \right),                                            \tag{8.1}
\]

where the entries are its row support, length and rank-profile changes,
signed direct-facet and derivative-owner palettes, signed port current,
short prepins, protected long-provider changes, and common-cap guard state.

It counts as a connector actuator only for the marked adjacencies it
literally supplies.  It counts as a palette-debt repair only for a colour in
`Gamma` which it removes from the direct rail and rehosts in a distinct
short cell.  It counts as slot-preserving only after the total row length is
`W+1`.  It counts as compiler-safe only after (6.2) and Theorem 7.1, or the
joint rank-three master after the sockets are fixed.

Consequently the radius-one lower bound `8` and the fallback palette debt
`2` are neither automatically additive nor automatically identical.  A
single compound packet may discharge several adjacency units and both
palette debts, but only its literal signature (8.1) can justify that charge.

## 9. Proved and open boundary

Proved here:

* the exact `p`-path component/leaf/matching actuator bound;
* the radius-one three-path lower bound of eight outside adjacency units;
* one-facet-rail rigidity for every owner-tight rank-eight/rank-nine row;
* the invariant `p-1` socket/palette debt and the exact connected rail
  pair-column formulation;
* the fixed-socket scalar ledger and rank-three common-cap theorem;
* exact collar/deep-provider locality; and
* a sufficient common guarded face allowing socket selection before Hall.

Authenticated finite input used but not re-enumerated here:

```text
MATH_THEOREM_THREAD_D_ODD_TWO_BANK_REGENERATION_AND_K17_SIXSWAP_GATE_20260731.md
MATH_THEOREM_ODD_OCCURRENCE_EXCHANGE_HALL_LLL_AND_K17_SEVENSWAP_20260731.md
scratch/k17_sevenswap_premaster_macro_forest_20260731.flow.json
  SHA-256 56f6701224913c1b3c09cedd1483595ef627d1bc946a87af43a8e73098dda0dc
scratch/k17_sevenswap_marked_component_path_20260731.json
  SHA-256 70313f26d046ab24af053dbeb775f8d516d1faf3666e9f85bd7d13acb343dd
```

Three-path source and independent replay:

```text
MATH_THEOREM_K17_MARKED_ATOM_THREE_PATH_SOCKET_LEDGER_20260731.md
  SHA-256 eea35932f7294a58da6cf965c53acfe0f88860e151d6bb9c0790c1733f0a1498
scratch/k17_marked_atom_phase_path_frozen_20260731.json
  SHA-256 234a34703cdef66722d6df54b936361048565915f4bf9ab523e13368d828bdec
scratch/h2_independent_audit_k17_marked_atom_three_path_frozen_20260731.py
  SHA-256 805dee17d08d00a60b819f495f44a0b87c256fdfdc47ff6e0a30b3bebcc120ec
```

Still open are existence of the `18501`-facet rail, physicalization of the
two fallback sockets, socket-conditioned residual connected completion,
all upper/deep providers, and the actual common-cap matching.  This theorem
does not prove a `K17` word or an all-odd recurrence.
