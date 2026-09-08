# K17 GMM/U joint-palette interface: an exact coherent ten-cycle factor

Date: 2026-07-31  
Status: exact finite certificate for one authenticated parent/U-bank fibre;
not a K17 word and not a global recurrence theorem

## 0. Result

The owner-level gate left after the endpoint-oriented residual-forest
semantics can be coupled literally to the frozen 737-path pure-`U` bank.
For the authenticated `k=15` two-cycle parent and the frozen Y-U-X colour
catalogue, there is an exact directed rank-6-coloured forest on the 6435
rank-7 `A` bases with:

* 5005 edges, one of every rank-6 colour;
* 1430 directed paths, including 455 isolated bases;
* the prescribed 1430 free `X` labels and prescribed 1430 free `Y` labels;
  and
* one `alpha` source and one `beta` sink on every nontrivial path.

Expanding this forest through the two parent rails and adjoining the frozen
U bridges gives a literal Johnson 2-factor on all

\[
             {17\choose9}=24310
\]

middle owners.  Its edge intersections are all

\[
             {17\choose8}=24310
\]

lower colours exactly once.  It has ten connected components.  Each
component has a coherent cyclic orientation alternating

\[
 X\longrightarrow A/G\longrightarrow Y
 \quad\hbox{and}\quad
 Y\longrightarrow U\longrightarrow X
\]

(with a direct `Y -> X` identity in place of an empty U bridge).

Thus, in this fixed fibre, there is **no Hall or colour-incidence
obstruction** to pure-U insertion plus the joint untagged palette at the
2-factor level.  The exact remaining owner-topology defect is ten cycles,
not a palette deficit.  A colour-preserving component fusion/opening is not
proved here.  Tagged upper service, global residence, deeper shadows and
the common compiler also remain separate.

## 1. Immutable inputs

The replay uses only these fixed literal inputs:

```text
answers/k15.word
SHA-256 f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b

scratch/k17_pbbs_u_upper_complete_20260731.fragments
SHA-256 f7ea82ae64a396da5db80836af55c16f3ebc8b96e8e354384423b4b96df944c8

scratch/k17_pbbs_u_yux_bridge_matching_20260731.tsv
SHA-256 e602f2f3abc91909bec42bdde02422001d9c78f354207c7fd69b0288d99c4148
```

The path/socket interpretation is the one proved in Sections 1--5 of the
endpoint-oriented residual-factor note.  The present finite certificate
does not use the later macro-flow statements of that live note as an input.

## 2. Exact U-side palette census

The U bank partitions all 5005 old rank-9 owners into 737 Johnson paths.
Its 4268 internal intersections are distinct rank-8 colours.  Hence the
residual old rank-8 palette has

\[
                6435-4268=2167
\]

colours.

The frozen bridge table chooses two distinct residual colours at every U
path, for 1474 port colours in total.  The complement consists of 693
colours, each used by its literal direct seam `Y(T)-X(T)`.  Thus

\[
              4268+1474+693=6435.                 \tag{2.1}
\]

The 1474 literal U endpoints have between one and nine residual facet
options.  Exactly 32 residual colours occur at no U endpoint at all.  They
are all in the 693-colour direct bank, so this forced-direct phenomenon is
not a Hall obstruction.  It is the smallest visible local constraint on
any recurrence that tries to replace the direct bank by ports.

Writing `L` and `R` for the 737 chosen left and right bridge colours and
`D` for the 693 direct colours, the required free endpoint banks are

\[
 X_*=R\mathbin{\dot\cup}D,
 \qquad
 Y_*=L\mathbin{\dot\cup}D.                         \tag{2.2}
\]

Both have size 1430, their intersection is exactly `D`, and their union is
the complete 2167-colour residual palette.

## 3. The directed rank-6 incidence reduction

Let `T_i` be the depth-three parent middle owners in the two directed
cycles of orders 6390 and 45, and put

\[
 C_i=T_i\cap T_{\operatorname{succ}(i)}.
\]

The `C_i` enumerate all rank-7 sets once.  Cutting the X rail at `alpha_i`
frees the owner after that cut, while cutting the Y rail at `beta_i` frees
the owner before that cut.  Therefore (2.2) fixes

\[
 \alpha=\{\operatorname{pred}(i):T_i\in X_*\},
 \qquad
 \beta=\{i:T_i\in Y_*\}.                           \tag{3.1}
\]

Their exact parent-cycle counts are

\[
 \alpha:(1405,25),\qquad \beta:(1402,28),           \tag{3.2}
\]

so both endpoint classes hit both parent cycles.  Also

\[
 |alpha|=|\beta|=1430,
 \qquad |\alpha\cap\beta|=455.                     \tag{3.3}
\]

Orient every desired A-base path from alpha to beta.  A rank-7 base may be
a tail iff it is not in beta, and may be a head iff it is not in alpha.
There are exactly 5005 eligible tails and 5005 eligible heads.  For every
rank-6 colour `Z`, independently choose

\[
 C^-\supset Z\quad(C^-\notin\beta),
 \qquad
 C^+\supset Z\quad(C^+\notin\alpha),
 \qquad C^-\ne C^+.                                \tag{3.4}
\]

Each side is an ordinary bipartite inclusion matching.  In the literal
instance every colour has at least two eligible tails and at least two
eligible heads.  The deterministic certificate saturates both shores and
forbids the one possible self-pair in the second matching.  Its directed
union has no cycle.  Consequently it is exactly a 1430-path forest, with
the 455 members of `alpha intersect beta` as its isolated paths.

This is a finite positive matching certificate, not an all-r theorem that
the two inclusion matchings are always simultaneously acyclic.

## 4. Physical endpoint shift and coherence

One indexing subtlety is essential.  If a G-path starts at `alpha_i`, its
physical X arm ends at the state immediately after the **previous** alpha
cut on that parent cycle.  If it ends at `beta_j`, its physical Y arm ends
at the **next** beta cut.  Pairing `T_succ(i)` directly with `T_j` gives an
abstract cut-label permutation, not the physical path pairing.

The replay applies these two cyclic shifts and then constructs every
physical owner and edge.  Each tagged path is coherently traversed from its
free X endpoint, along an X arm, through its directed A-base path, and along
a Y arm to its free Y endpoint.  The frozen external catalogue returns Y
to X through either one oriented U path or one direct identity.  The
resulting component permutation has ten cycles, and direct vertex-level
replay gives the same ten physical components.

Only 150 of the 1430 macro endpoint pairs are Johnson-adjacent.  Thus this
certificate belongs to the unrestricted macro class; it is not evidence
for the stronger coupled pair-of-tight-enumerations subclass.

## 5. Exact scope

The certificate proves, for these fixed inputs:

1. the rank-6 A-base colour matching and path topology;
2. exact physical free-endpoint ownership;
3. complete, multiplicity-one lower palettes in all four tag sectors; and
4. coherent orientation on each of ten full owner cycles.

It does not prove:

1. a colour-preserving fusion of the ten cycles to one cycle or path;
2. preservation of every tagged upper target;
3. a global `010/0110`-safe chronology or staircase budget;
4. deeper-shadow service or a common-cap compiler; or
5. any numerical K17 bound.

The machine-readable edge and path catalogues and two independent replays
are stored beside the audit JSON in `scratch/`.
