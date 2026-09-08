# `k=17` marker58: residence-aware factor/source fibre and deep-upper rethread gate

Date: 2026-08-02  
Lane: H3, protected upper host  
Status: exact source-fibre and rethread reduction, with new finite distance
and fixed-order staircase obstructions.  The authenticated connected factor
is rejected before source binding on both the flat `D^3` face and the complete
optimal three-particle monotone-staircase face.  No resident replacement
factor, ranks 11--17 completion, compiler, or contiguous-OR word is claimed.

## 1. Authoritative rebase

Let `F0` be the developed factor

```text
scratch/k17_marker58_upper_q1_quotient_audit_20260802/
  c68b.double_fusion.factor.tsv
```

with SHA-256

```text
7d39e3aee641521df2d441d0342a2bd060dafb05cc7f5703ef206f53b6d21e3c.
```

The central factor theorem proves that `F0` is one Hamilton cycle on all
24,310 rank-nine owners, uses every rank-eight facet once, covers every
rank-ten cap, has quotient voltage four, and retains literally all 986
first-58/open-3 marker paths.  The residence audits prove

\[
 N_2=2873,\qquad N_3=2499,\qquad N_{<4}=5372,             \tag{1.1}
\]

no legal depth-three opening cut, a best-cut residual of 5,369 short runs,
and 11,640 failures of maximal `D^3` reconstruction.  Its cyclic owner-
interval deck additionally has 1,972, 510 and 51 holes at ranks 11, 12 and
13, respectively, and no holes at ranks 14--17.

Thus `F0` closes owner/lower-q1/rank-ten/connectivity only.  It is neither a
flat source-atlas host nor an optimal three-particle variable-staircase host.
The live object is a residence-aware reselection of the factor together with
a nonempty literal source fibre.

This note extends, rather than duplicates,

```text
MATH_THEOREM_K17_MARKER58_CONNECTED_RANK10_FACTOR_AND_RESIDENCE_MASTER_GATE_20260802.md
MATH_AUDIT_K17_MARKER58_CONNECTED_HOST_RESIDENCE_NOGO_20260802.md
MATH_AUDIT_AD_K17_MARKER58_DOUBLE_C6_CONNECTED_Q1_AND_FIXED_RESIDENCE_NOGO_20260802.md.
```

### Theorem 1.1 (fixed-order three-particle staircase no-go)

Open an oriented owner cycle at any cut.  Let
`a_1<=...<=a_m` be the occurrence-labelled starts of its internal length-two
positive runs.  Repeated positions from different coordinates are retained.
For `0<=x<=W`, put

\[
 r(x)=\max\bigl(\{a_j:a_j+3\le x\}\cup\{0\}\bigr),
 \qquad G_2=\max_{0\le x\le W}(x-r(x)).                  \tag{1.2}
\]

Equivalently, when `m>=1`,

\[
 G_2=\max\!\left\{a_1+2,
        \max_{j<m}(a_{j+1}-a_j+2),W-a_m\right\};          \tag{1.2a}
\]

set `G_2=W` if `m=0`.

For every three-particle monotone staircase on this chronology, with start
defects whose two largest values are `delta_1>=delta_2>=0`, thresholds
`alpha_i=W-delta_i`, and exact length-two frontiers `R_2,R_3`, its scalar
loss satisfies

\[
 \operatorname{Loss}\ge
 \delta_1+\delta_2+R_2+R_3
 \ge 2(W-G_2).                                            \tag{1.3}
\]

For every cut of `F0`, in both orientations, the exact value is

\[
                         G_2=36.                           \tag{1.4}
\]

Consequently every such schedule has

\[
                    \operatorname{Loss}\ge
                    2(24310-36)=48548>7401.               \tag{1.5}
\]

Equivalently, loss at most 7,401 would require

\[
                         G_2\ge20610.                      \tag{1.6}
\]

#### Proof

The third start defect and every remaining deadline/correction term in the
exact staircase normal form are nonnegative.  By definition,
`R_2>=r(alpha_1)`: every run whose full three-edge corridor satisfies
`a_j+3<=alpha_1` is unshielded.  Equation (1.2) gives

\[
                     R_2\ge r(\alpha_1)\ge\alpha_1-G_2,
 \qquad \delta_1+R_2\ge W-G_2.                            \tag{1.7}
\]

Similarly `R_3>=r(alpha_2)`, because a run whose full corridor ends by
`alpha_2` has at most one active shield.  Thus

\[
                     R_3\ge r(\alpha_2)\ge\alpha_2-G_2,
 \qquad \delta_2+R_3\ge W-G_2.                            \tag{1.8}
\]

Summing proves (1.3).  The exhaustive audit computes (1.4) for all 24,310
cuts in each orientation.  Equations (1.5)--(1.6) follow. \(\square\)

The exact audit additionally records 7,582 q1-safe openings in each
orientation; their maximum `G_2` is still 36.  Its best terminal-start
diagnostics have losses 48,562 and 48,566, but (1.5) is the stronger
arbitrary-start lower bound.

Frozen audit artifacts are

```text
0c85b7a1903c71eff20b0eea47c6f63d7fac4edd509875c582d5a644d0af99ef
  scratch/audit_v_k17_marker58_deadline_particles_20260802.cpp
b54ab366b43f892bac94b6b1972ddbfbee8c0407cebb7804914e43f3be23a8d8
  scratch/v_k17_marker58_deadline_particles_20260802/marker58.deadline.audit.json
57741e39226d1f62af1f0488f8515f58bb5f254c2cc6c1ceb136560bba66b726
  scratch/v_k17_marker58_deadline_particles_20260802/marker58.deadline.cuts.tsv
99c6d3525192ad0fee3f1846ef12dbb42d4206ed6b1090cd224f8ccea2254bcc
  scratch/v_k17_marker58_deadline_particles_20260802/marker58.deadline.runs.tsv
```

The no-go is exact for row-OR recovery plus the scalar lower-cell budget of
the complete three-particle monotone-staircase class.  It does not claim a
lower Hall/common-cap or ranks-11--17 verdict, and it is not a theorem about
an unrelated nonmonotone or different-particle architecture.  Such
architectures are outside the live H3 route; they are not an escape assigned
to this fixed host.

## 2. Exact flat `D^3` fibre

Use cyclic indices and the trailing convention

\[
                 T_i=(D^3S)_i
                    =S_i\cup S_{i-1}\cup S_{i-2}\cup S_{i-3}. \tag{2.1}
\]

For an owner chronology `T`, define its maximal source envelope

\[
                 K_i=T_i\cap T_{i+1}\cap T_{i+2}\cap T_{i+3}. \tag{2.2}
\]

### Theorem 2.1 (maximal erosion and the run criterion)

For an unrestricted cyclic set word `S`, the following are equivalent:

1. `D^3 S=T` for some `S`;
2. `D^3 K=T`; and
3. for every coordinate, every proper cyclic positive run in `T` has length
   at least four.

The all-zero and all-one coordinate traces are allowed.  Moreover, `K` is
the pointwise largest word satisfying `D^3 K subseteq T` and, when the three
conditions hold, the largest exact antecedent.

#### Proof

If `x in S_i`, then `x` belongs to `T_i,T_(i+1),T_(i+2),T_(i+3)`, so
`S_i subseteq K_i`.  On a proper positive run of length `L`, erosion leaves
the `L-3` possible four-consecutive-one starts when `L>=4` and leaves none
when `L<=3`.  Dilation recovers the run exactly in the first case and misses
it in the second.  Constant traces are immediate.  This also proves
maximality. \(\square\)

For binary source-incidence variables `s_(i,x)`, the complete unrestricted
fibre over fixed `T` is therefore

\[
 s_{i,x}=0\quad(x\notin K_i),\qquad
 \sum_{a=0}^3s_{i-a,x}\ge1\quad(x\in T_i).                \tag{2.3}
\]

The first family prevents every false positive, and the second supplies
every required owner-coordinate occurrence.

There is also an exact bounded-box specialization.  Suppose the only extra
set restrictions are

\[
                     L_i\subseteq S_i\subseteq A_i\subseteq K_i. \tag{2.4}
\]

Then the fibre is nonempty if and only if

\[
 L_i\subseteq A_i\quad\hbox{for all }i,qquad
 T_i\subseteq A_i\cup A_{i-1}\cup A_{i-2}\cup A_{i-3}
                     \quad\hbox{for all }i.               \tag{2.5}
\]

Indeed the maximal choice `S_i=A_i` proves sufficiency.  Hence a failure of
this set-only fibre has a radius-three certificate: either a forced
coordinate lies outside one envelope, or one owner-coordinate has no one of
its four possible source providers.

Ranks, occurrence identities, fixed-root equations, shared capacities,
forbidden tuples and compiler matchings are not boxes.  Once any of those
are added, (2.5) is no longer a completeness theorem.  They must remain in
the occurrence-labelled fibre below.

For a linear opening, the first and last three source windows are governed
by the chosen boundary collars.  The cyclic run criterion may be applied
only to internal runs; the seam/collar state in the central master theorem
is the exact boundary replacement.

## 3. Literal open-3 marker phase

Fix distinct `v_0,...,v_4,beta` outside `X`, put

\[
 U=X\cup\{\beta,v_0,v_1,v_2,v_3,v_4\},                  \tag{3.1}
\]

and define the five source states

\[
 S_0=X\cup\{v_0\},\qquad
 S_j=X\cup\{\beta,v_j\}\quad(1\le j\le4).              \tag{3.2}
\]

Their cyclic derivative is

\[
 T_t=\bigcup_{a=0}^3S_{t-a}=U\setminus\{v_{t+1}\}.       \tag{3.3}
\]

Opening native edge type 3 gives the exact directed correspondence

\[
 (S_2,S_3,S_4,S_0,S_1)
 \longmapsto
 (T_2,T_3,T_4,T_0,T_1).                                  \tag{3.4}
\]

Thus the source roles occur as three buffers, primitive `P`, primitive `H`;
the state indices are the safe unambiguous labels.  The four protected q1
edges leave `S_2,S_3,S_4,S_0`, whereas the packet's four labelled lower-
source demands use `S_2,S_3,S_4,S_1`.  The equality `3944=4*986` is only a
count.  It is not a physical source-occurrence binding.

Let the five pinned source states in (3.4) occupy positions `p,...,p+4`, and
write them as `R_0,...,R_4`.  Put

\[
 P_j=\bigcup_{h=1}^jS_{p-h},\qquad
 Q_j=\bigcup_{h=1}^jS_{p+4+h}.                            \tag{3.5}
\]

The complete affected owner window is

\[
\begin{aligned}
T_p&=P_3\cup R_0,\\
T_{p+1}&=P_2\cup R_0\cup R_1,\\
T_{p+2}&=P_1\cup R_0\cup R_1\cup R_2,\\
T_{p+3}&=R_0\cup R_1\cup R_2\cup R_3,\\
T_{p+4}&=R_1\cup R_2\cup R_3\cup R_4,\\
T_{p+5}&=R_2\cup R_3\cup R_4\cup Q_1,\\
T_{p+6}&=R_3\cup R_4\cup Q_2,\\
T_{p+7}&=R_4\cup Q_3.
\end{aligned}                                             \tag{3.6}
\]

In particular, with `L_j=S_(p-j)`, the incoming ordered age cells must obey

\[
\begin{aligned}
L_1\setminus S_2&=\{v_1\},\\
L_2\setminus(S_2\cup L_1)&=\{v_0\},\\
L_3\setminus(S_2\cup L_1\cup L_2)&=\{v_4\}.
\end{aligned}                                             \tag{3.7}
\]

Consequently the literal interface has radius three on both sides.  Testing
only the five central masks, or only their unordered cumulative collars, is
not complete.

There is a useful necessary endpoint row.  To avoid confusion with the
erosion envelope `K_i`, denote the omitted native facet by

\[
                         J_u=U\setminus\{v_2,v_3\}.        \tag{3.8}
\]

For the orientation in (3.4), the factor edge leaving the terminal owner
`T_1` must have lower colour `J_u`, because

\[
                    S_4\cup S_0\cup S_1=J_u.              \tag{3.9}
\]

Indeed `T_1=J_u union {v_3}` and
`T_(p+5)=J_u union S_(p+5)`.  Two consecutive owners are distinct rank-nine
masks, so their Johnson intersection has rank eight and is exactly `J_u`.
Since the q1 factor selects every lower colour once, its unique `J_u` edge
must be the exterior arc leaving the canonical terminal.  If it meets
neither endpoint, this path has no canonical atlas entry.  Meeting the
opposite endpoint gives the reflected sign; meeting both restores the
omitted five-cycle edge and is incompatible with a connected factor on more
than five owners.

### Orientation correction

A Hamilton cycle need not traverse all 986 disjoint protected paths with
the same canonical sign.  Let `sigma_u(y)` be the sign induced on path `u`
by the directed factor arcs, and let every atlas entry carry its permitted
sign.  The exact link is

\[
               z_{u,a}=1\quad\Longrightarrow\quad
               \operatorname{sign}(a)=\sigma_u(y).        \tag{3.10}
\]

Global reversal negates the entire sign vector; it does not independently
flip its coordinates.  In the convention (2.1), if `T'_i=T_(c-i)`, the
transported antecedent is

\[
                           S'_i=S_{c-i-3},                 \tag{3.11}
\]

not naive word reversal.  A common-sign condition is valid only if the
packet specification separately proves or imposes it.

## 4. Exact residence-aware factor/source master

Let `M` be the physical (or orbit-tied) factor master of the central theorem:
one selected edge per rank-eight facet, degree two at every rank-nine owner,
positive load at every rank-ten cap, all 3,944 protected edges fixed, one
directed Hamilton cycle, and one typed opening seam.  Its exact internal
residence rows forbid every selected bracket path

\[
                        0,1^\ell,0,\qquad1\le\ell\le3.    \tag{4.1}
\]

For a physical directed path `P=(w_0,...,w_(ell+1))`, the seam-aware row is

\[
 \sum_{j=0}^{\ell}y_{w_j,w_{j+1}}
 -\sum_{j=0}^{\ell}h_{w_j,w_{j+1}}\le\ell.               \tag{4.2}
\]

Here `h_a<=y_a` and `sum_a h_a=1`.  On the one-cycle face this is exact: the
motif must be broken or meet the unique opening seam.  Exact q1 already
excludes `ell=1`, but retaining that row is harmless.  In an orbit-tied
master, repeated appearances of one quotient option are deduplicated and the
strict cyclic row is

\[
       \sum_{q\in\operatorname{supp}(P)}q
             \le |\operatorname{supp}(P)|-1.             \tag{4.2a}
\]

In the connected nonzero-voltage `Z_17`-equivariant face, provided the
occurrence-labelled motif orbit is free, one seam cannot clip all 17
translates of a bad motif.  Under that hypothesis the strict cyclic
quotient-support clauses are equivalent to linear residence.

For a master state `m=(x,y,h)`, let `A_u(m)` be the set of complete
occurrence-labelled entries for marker path `u`.  An entry includes the five
states (3.4), all equations (3.6)--(3.10), fixed-root legality, every
physical occurrence and token, and every local protected clause.  With
entry variables `z_(u,a)`, a complete source fibre also needs a legal source
letter at every position.  Let `L_i(m)` be the complete occurrence-labelled
domain at position `i`, with letter mask `B_alpha`, and use

\[
 \sum_{\alpha\in L_i(m)}\lambda_{i,\alpha}=1,\qquad
 s_{i,x}=\sum_{\substack{\alpha\in L_i(m)\\x\in B_\alpha}}
                     \lambda_{i,\alpha}.                 \tag{4.3a}
\]

It consists of

\[
 \sum_{a\in A_u(m)}z_{u,a}=1                              \tag{4.3}
\]

for all 986 paths, the global set-incidence equations (2.3), all physical
token capacities, shared-occurrence equality constraints, and all remaining
minimal forbidden tuples.  The `z` variables are linked to the corresponding
`lambda` variables.  Two entries referring to the same already-fixed
chronology position and source occurrence must be glued by equality.  Two
entries attempting to place one movable capacity-one occurrence at different
positions conflict instead; those cases must not be conflated.

### Theorem 4.1 (factor/source Benders equivalence)

A flat protected host with the prescribed marker bank and the declared
complete source domains `L_i(m)` exists if and only if some master state `m`
satisfies the palette, rank-ten, topology and residence rows and its
occurrence-labelled fibre `A(m)` is nonempty.

For the set-box projection (2.4), every infeasible fibre has a radius-three
coordinate core given by (2.5).  For the full occurrence-labelled fibre, an
arbitrary minimal signed core `C^+ union C^-` gives the exact logic-Benders
row

\[
       \sum_{q\in C^+}(1-q)+\sum_{q\in C^-}q\ge1.         \tag{4.4}
\]

A whole-master no-good is always sound.  A uniformly bounded core after
global capacities, shared collars, fixed-`M_0` correlation or compiler
matchings is not proved.

#### Proof

Restriction of a host gives `m` and its selected literal entries.  Conversely
the factor chronology plus a fibre solution supplies every source position,
collar and protected occurrence required by the definition.  Equation
(4.4) is precisely the negation of one infeasible partial assignment.
The radius-three claim on the box face is Theorem 2.1 and (2.5). \(\square\)

The fixed `F0` is rejected by (4.2) before (4.3), and Theorem 1.1 rejects its
optimal three-particle variable-staircase fibre as well.  Running another
atlas, staircase or compiler solve over its chronology cannot change either
verdict.

Quotienting (4.3) is valid only if the complete source occurrence universe,
collars, root matching, tuple language and capacities carry the same free
`Z_17` action.  Equivariance of the factor alone is insufficient.

## 5. Exact ranks 11--17 separation

The source and owner interval decks are linked without approximation.

### Theorem 5.1 (long-source/owner interval identity)

If `D^3S=T`, then for every cyclic source interval of length at least four,

\[
             \bigcup_{j=a}^{b}S_j
               =\bigcup_{i=a+3}^{b}T_i.                  \tag{5.1}
\]

Conversely,

\[
             \bigcup_{i=c}^{d}T_i
               =\bigcup_{j=c-3}^{d}S_j.                  \tag{5.2}
\]

#### Proof

Expand each `T_i` by (2.1).  In (5.1), the owner windows from `a+3` through
`b` contain exactly the source indices `a,...,b`; (5.2) is the same union in
the other direction. \(\square\)

Hence a target `Z` occurs in the complete source interval deck if and only if

\[
 \boxed{\text{some owner interval has union }Z}
 \quad\lor\quad
 \boxed{\text{some source interval of length }1,2,3
        \text{ has union }Z}.                             \tag{5.3}
\]

For an opened linear word, intervals meeting the first or last three source
positions are boundary/exterior rows and must be replayed separately; (5.3)
does not erase cut collateral.

For fixed `T`, put

\[
                       I_Z=\{i:T_i\subseteq Z\}.           \tag{5.4}
\]

An owner-interval witness exists exactly when one maximal cyclic run `R` of
`I_Z` satisfies

\[
                           \bigcup_{i\in R}T_i=Z.          \tag{5.5}
\]

Indeed any witness lies in such a run, whose extension cannot introduce an
element outside `Z`; the converse is immediate.

At `k=17`, ranks 11--17 comprise 21,778 physical target rows.  Under a fully
equivariant factor and source fibre these reduce to

\[
             728,364,140,40,8,1,1                       \tag{5.6}
\]

rows at ranks 11 through 17, or 1,282 rows total.  Rank 17 is automatic for
a Hamilton owner cycle; the other rows must be separated.  Rethreading may
destroy an old witness, so the current completeness at ranks 14--17 is not a
hereditary certificate.

On the cyclic host, an exact, possibly exponential, extended formulation
introduces a witness variable for every directed owner path whose vertices
lie in `Z` and whose union is `Z`, plus variables for the length-at-most-three
source alternatives in (5.3).  Requiring one such witness for every `Z` is
sound and complete.  After a linear cut, merely requiring the owner path not
to cross the seam is insufficient: an owner interval beginning among the
first three owner positions expands by (5.2) into the exterior source collar.
The linear formulation is exact only after those radius-three exterior
source variables and their cross-window unions are included, or after all
witnesses touching that offset are excluded and handled by a separate
boundary ledger.  Lazy cyclic path generation or a full master no-good is
proof-safe; a scalar count of covered targets is not.

The internal five-state marker block has common total cap `U`; its proper
internal owner/source intervals supply no rank-11-or-higher target.  Thus
rank-11--17 service involving a marker path is an exterior or boundary-
crossing obligation, not an internal packet dividend.

## 6. Palette-preserving rethreads and a sharp distance obstruction

Alternating protected-avoiding incidence circuits generate the complete
owner/lower-q1 degree fibre.  For one such circuit `Q`, let `D_Q` be its
removed owner edges and `A_Q` its added owner edges.  The following screens
are exact:

1. protected avoidance preserves all 986 marker paths literally;
2. every rank-ten load changes by

   \[
          m_{F^Q}(Z)=m_F(Z)-r_Q(Z)+a_Q(Z);                 \tag{6.1}
   \]

3. the retained-path endpoint involution gives the exact component delta;
   equivalently, direct subtour and voltage replay decides the one-cycle row;
4. every destroyed short-run motif meets `D_Q`, and every newly created one
   meets `A_Q`; therefore the change in the short-run potential

   \[
                         \Phi(F)=|\mathcal R_{\le3}(F)|   \tag{6.2}
   \]

   is obtained by replaying only the four-edge neighbourhoods of the changed
   seams, with occurrence deduplication; and
5. if rejoining reverses an unchanged path atom containing protected marker
   paths, their sign links (3.10), radius-three source collars and source
   fibre must be replayed.  Edge preservation alone does not preserve source
   chronology.

There is no theorem that the factors satisfying all five screens are
connected by improving circuits.

### Theorem 6.1 (1,790-adjacency barrier from the exact cut census)

Let `F'` be any Hamilton owner factor on the same 24,310 owners, and let

\[
                         D=E(F_0)\setminus E(F').          \tag{6.3}
\]

If some linear opening of `F'` is depth-three resident, then

\[
                              |D|\ge1790.                  \tag{6.4}
\]

If `F'` is strictly cyclically resident, then `|D|>=1791`.  If `F'` is
`Z_17`-equivariant, at least 106 old adjacency orbits must disappear.

#### Proof

Let `R_0` be the 5,372 old occurrence-labelled bracket paths.  Cutting one
old edge clips exactly the old motifs containing that edge.  The exhaustive
cut histogram says that motif degrees 3, 2, 1 and 0 occur on respectively

\[
                       272,3417,10965,9656                 \tag{6.5}
\]

old edges.  The incidence check

\[
 3(272)+2(3417)+10965
   =18615=3(2873)+4(2499)                                 \tag{6.6}
\]

shows that this is the complete bracket-edge incidence ledger.  In
particular, one old edge meets at most three old motifs.

If every edge of one old bracket path survives in `F'`, that path remains
consecutive: its internal vertices already use both of their degree-two
incidences.  Reversal preserves its `0,1^ell,0` trace.  It is therefore still
a forbidden internal motif unless the final opening seam lies on that path.
The seam can excuse at most three old motifs.  Every other old motif meets
`D`, and every edge of `D` hits at most three of them.  Thus

\[
                    5372\le3|D|+3,
\]

which gives (6.4).  Without a seam, use `5372<=3|D|` and obtain 1,791.
Orbitwise, 316 old motif orbits and degree at most three give
`ceil(316/3)=106`. \(\square\)

The 106-orbit conclusion sharpens the earlier 32-orbit locality floor: it
uses the complete all-cut motif-degree histogram (6.5), not only a coarse
support-radius estimate.

Consequently no source relabelling, cut change or single `C6`/`C8` can repair
`F0`.  Measured in physical exchanges that delete at most three or four old
adjacencies per move, pure `C6` and `C8` sequences require at least 597 and
448 moves, respectively.  On a tied
quotient face the corresponding lower bounds are 36 and 27 orbitwise moves.
These are terminal-distance lower bounds only; new short motifs can require
more changes.

The independent quotient projection supplies a complementary first CEGAR
round: 316 distinct violated support clauses, of residual widths

```text
1:37  2:15  3:149  4:115.
```

In particular 37 currently selected quotient options are individually
forbidden.  This does not prove the protected residence-aware master
infeasible; every new incumbent must be separated again.

### 6.2 Current exact rethread frontier

The residence descent has already left `F0`.  The frozen round-48 factor

```text
scratch/k17_c68b_double_fusion_residence_greedy_20260802/
  c68b.greedy48.factor.tsv
```

has SHA-256

```text
b1343737cb0e3d99dec503e526e566521504478af1c5792c9a7949b6a5796616.
```

It remains one physical cycle, retains all protected edges, uses every
rank-eight facet once and covers every rank-ten cap.  Its exact positive
short-run census is

\[
                    N_2=2312,\qquad N_3=1887,
                    \qquad\Phi=4199.                     \tag{6.7}
\]

Thus it is a genuine palette/topology-preserving descent from 5,372, but it
is not resident.  Its owner-interval holes are 2,006, 391 and 34 at ranks
11, 12 and 13; improving residence did not monotonically improve the deep
deck.

The complete endpoint-retaining one-circuit neighbourhood contains 1,888
directed `C6` circuits and 6,259 corresponding `C8` circuits.  Among candidates
which preserve every rank-ten cap and one physical component, none reduces
(6.7).  Independently, all 102 protected-disjoint, cap-safe, connected
physical star-`C8` candidates strictly worsen positive residence.  Therefore
4,199 is an exact floor only for these one-circuit faces, not a global floor.

The compound face does escape.  A complete disjoint endpoint-retaining
`C6/C8` pair census contains 7,294 final cap-safe pairs, 2,249 final connected
pairs and four residence-improving pairs.  Its materialized first escape has

\[
                         (N_2,N_3)=(2295,1870),
                         \qquad\Phi=4165.                 \tag{6.8}
\]

Regenerating the pair catalogue on that literal prefix gives 2,569 final
connected pairs and 17 improving pairs.  The second materialized escape has

\[
                         (N_2,N_3)=(2278,1870),
                         \qquad\Phi=4148.                 \tag{6.9}
\]

Both factors are independently replayed as one physical cycle with every
rank-eight facet, every rank-ten cap and all 3,944 protected edges.  The
current exact descent frontier is therefore

```text
6962d4c658a2cb91b35b4d537c0726a5a60dafea3c33595804eab1fdd8335183
  scratch/k17_c68b_double_fusion_residence_greedy_20260802/
    paired_escape002.factor.tsv
43f0f152bdb1a5b73ff481ff0b6a609f8fe7b23a9a2b83900d43e01beb452ed5
  scratch/k17_c68b_double_fusion_residence_greedy_20260802/
    paired_escape002.residence.audit.json
```

It is still nonresident.  No ranks-11--17, source-fibre or compiler replay
has been promoted for `paired_escape002`.  The two successful rounds prove
that compound, sequentially regenerated moves are genuinely stronger than
the closed one-circuit face; they do not give monotonicity to residence zero.
Marginally adding two stale circuits remains unsound.

The exact round-one quotient master contains the base resource CNF, two
incumbent component cuts and the first 316 residence blockers.  Its 37 unit
rows delete 37 incumbent options, but independent Hall/DM projections remain
perfect on both the facet--owner and missing-cap--facet graphs.  Hence those
units are not an ordinary matching obstruction.  Owner multiplicity, cap,
topology, voltage and later residence rows remain jointly correlated, and the
round-one SAT/UNSAT status is nonterminal.

For a connected `Z_17`-equivariant factor, the deadline-particle theorem
proves more than the fixed-host no-go: an optimal three-particle monotone
staircase exists if and only if there is no cyclic positive run below four.
Accordingly the orbit-tied H3 master loses nothing by enforcing the strict
cyclic support clauses (4.2a); no separate variable-staircase branch remains
inside that subclass.  Releasing orbit ties gives a larger 875,160-option
physical factor master and can in principle cluster defects near two ends,
but H3's live target remains the stronger residence-safe endpoint.

The exact current master and move-scope references are

```text
MATH_THEOREM_R2_K17_ROUND1_RESIDENCE_FACTOR_BENDERS_AND_UNIT37_DM_20260802.md
  7e7865c9ebf79d36539701f22d9eccac7a93ad6dfdee3e5a902ff90bafe071ee
MATH_THEOREM_V_K17_DEADLINE_PARTICLE_RETHREAD_AND_MARKER58_NONFLAT_NOGO_20260802.md
  2d406679c786245cbbe7b82ff942414e0917f7d6bd4d34cecfdc9612d0e5ea4b
MATH_THEOREM_L_K17_C68B_PHYSICAL_CIRCUIT_LOCALITY_AND_DEEP_CONE_GATE_20260802.md
  77473e767735a418609b18540300cde2a6c7bdcb1f15d9f52764dca54aab0d94
MATH_AUDIT_K17_GREEDY48_PHYSICAL_STAR_C8_RESIDENCE_NOGO_20260802.md
  3cb20b443f863f58ac254201dc6ff166da2b623f2e8f5a05674346d645a538d7
```

## 7. Exact surviving program and scope

The proof-safe order is now:

1. continue the quotient CEGAR with every new blocker accumulated, or enter
   a compound/long-support physical master; reselect a protected owner/
   lower-q1/rank-ten factor with exact residence active;
2. replay one-cycle topology and quotient voltage rather than inheriting
   them from `F0`;
3. solve the literal five-state occurrence fibre, including mixed path signs
   and both radius-three collars;
4. separate all 1,282 equivariant ranks-11--17 rows using (5.3), or all
   21,778 physical rows if source symmetry is absent; and only then
5. materialize the fixed-`M_0` lower/root/head/graphic compiler and its
   guarded Hall/core replay.

Closed here:

* exact flat `D^3` fibre and run criterion;
* exact open-3 marker phase, collar radius and omitted-facet endpoint row;
* the mixed-orientation/global-reversal correction;
* exact long-source/owner interval transport;
* exact protected-circuit local residence ledger; and
* the 1,790 physical / 106 quotient old-adjacency lower bound;
* the `G_2=36`, loss-at-least-48,548 fixed-order staircase no-go.

Still open:

* existence of a resident protected rank-ten-complete Hamilton factor;
* existence of a monotone cap/topology-safe rethread sequence;
* an occurrence-complete five-state atlas for any surviving factor;
* ranks 11--17 after the same reselection;
* bounded Benders cores after global capacity/compiler rows;
* exterior cut-window repayment, terminal compiler feasibility, and the
  final contiguous-OR word.

No finite search, SAT solve, compiler build or heavy local computation was
performed for this H3 theorem.
