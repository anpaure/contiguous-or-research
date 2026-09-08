# Thread A: spaced GMM dummy forests and the protected-port obstruction

Date: 2026-07-29

Status: pure theorem/obstruction.  The GMM tight-enumeration projection and
the GMM--dummy augmentation are kept distinct.  Exact lower-colour
preservation plus minimum component length is reduced to a coloured circular
cut, while the dummy route is reduced to an oriented spaced facet SDR.  A
mixed-side dummy extension is proved.  Neither GMM theorem by itself supplies
the required spacing for general depth.  More strongly, an explicit tight
enumeration at `m=3` has optimal spacing, exact lower colours, and local
depth-three freshness but misses a protected `q=2` target.  Thus component
length is not the remaining compiler-port theorem.

## 1. Attribution and notation

Let `m>=2` and

\[
 \Omega=[2m],\qquad
 \mathcal M=\binom{\Omega}{m},\qquad
 \mathcal L=\binom{\Omega}{m-1},
\]

and put

\[
 C=\operatorname {Cat}_m,qquad
 W=|\mathcal M|=(m+1)C,qquad
 N=|\mathcal L|=mC.                                 \tag{1.1}
\]

The verified GMM corollary supplies two separate existential objects:

1. a tight enumeration of the two levels `m-1,m`; and
2. a saturating incidence cycle through all rank-`m-1` sets and `N`
   distinct rank-`m` owners.

The direct-jump projection below uses the first object.  The dummy
augmentation uses the second.  No successor, spacing, or protected-window
property is transferred from one output to the other.

## 2. Exact coloured-cut theorem for a tight projection

Contract a tight enumeration to its rank-`m` owner cycle

\[
 H=(T_0,T_1,\ldots,T_{W-1},T_0).
\tag{2.1}
\]

For the cycle edge \(e_i=T_iT_{i+1}\), put

\[
 \lambda(e_i)=T_i\cap T_{i+1}\in\mathcal L.
\tag{2.2}
\]

Exactly `N` edges are mediated by the lower level, one for every colour
\(R\in\mathcal L\), and the remaining `C` edges are direct jumps.  For a
colour \(R\), let

\[
 I_R=\{e\in E(H):\lambda(e)=R\}.
\tag{2.3}
\]

Thus \(I_R\) consists of its unique mediated occurrence and any direct
occurrences of the same intersection colour.

### Theorem 2.1 (spaced lower-rainbow cut normal form)

Fix `1<=d<=m`.  A spanning subgraph \(F\subset H\) is a linear forest with
exactly `C` components, every lower colour exactly once, and every component
having at least `d+1` owner vertices if and only if its edge indicators
\(x_i=\mathbf1_{\{e_i\in F\}}\), with \(o_i=1-x_i\), satisfy

\[
 \sum_{e_i\in I_R}x_i=1
 \qquad(R\in\mathcal L),                             \tag{2.4}
\]

and, cyclically modulo `W`,

\[
 \sum_{t=0}^{d}o_{i+t}\le1
 \qquad(0\le i<W).                                  \tag{2.5}
\]

The number of omitted edges is automatically

\[
 \sum_i o_i=W-N=C.                                  \tag{2.6}
\]

#### Proof

Equation (2.4) is precisely exact lower-colour ownership.  Summing it over
the `N` colours gives \(|E(F)|=N\), hence (2.6).  Deleting `C>0` edges from
one Hamilton cycle leaves exactly `C` path components, including singleton
components when cuts are adjacent.

If consecutive omitted cycle edges have cyclic index gap `g`, the component
between them has exactly `g` owner vertices.  All gaps are at least `d+1`
exactly when no cyclic block of `d+1` edge positions contains two omissions,
which is (2.5). \(\square\)

### Corollary 2.2 (direct jumps are not optional mergers)

If every mediated edge is retained, then exact lower colours force every
direct jump to be omitted.  Consequently the canonical direct-jump deletion
has minimum component length `d+1` if and only if the direct jumps already
have cyclic separation at least `d+1` in `H`.

Retaining a direct jump of colour `R` is possible only by deleting the
mediated edge of colour `R` (and deleting all other direct occurrences of
`R`).  Thus it is a colour-preserving relocation of a cut, not a free
component merger.

#### Proof

The mediated occurrence already supplies the unique `R` required by (2.4).
Every additional retained occurrence violates (2.4).  The second statement
is the exhaustive alternative for choosing one edge from `I_R`. \(\square\)

The average component length is `W/C=m+1`; hence `d<=m` is necessary.  At
the endpoint `d=m`, equality in every average forces every gap to be exactly
`m+1`.  Put

\[
 P_a=\{e_{a+j(m+1)}:0\le j<C\}.                     \tag{2.7}
\]

Maximal residence on this fixed projected cycle exists exactly when some
phase `P_a` satisfies

\[
                         |I_R\setminus P_a|=1
                         \qquad(R\in\mathcal L).     \tag{2.8}
\]

Bare tightness controls neither the phase nor these colour quotas.  In
particular, the consecutive direct jumps in the audited `m=2` tight
enumeration are a literal deletion-only failure already at `d=1`.  Its same
projected owner cycle does admit a different tight expansion, obtained by
relocating the colour-3 and colour-4 cuts, whose two components have lengths
`3,3`.  Thus the fixed-enumeration failure is not falsely promoted to a
fixed-projection obstruction.

## 3. The dummy route is a spaced facet-SDR problem

Write a saturating cycle in the oriented form

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N-1},X_{N-1},R_0,
\tag{3.1}
\]

where \(R_i\subset X_i\supset R_{i+1}\).  Let

\[
 \mathcal E=\mathcal M\setminus\{X_0,\ldots,X_{N-1}\},
 \qquad|\mathcal E|=C,                               \tag{3.2}
\]

be the omitted owners.  The GMM--dummy proof chooses a facet SDR

\[
 \phi:\mathcal E\longrightarrow\mathcal L,
 \qquad \phi(Y)\subset Y,                            \tag{3.3}
\]

and one fixed alternating side of (3.1).  Its ordinary Hall condition is
supplied by the Boolean shadow inequality.

### Proposition 3.1 (fixed-side spacing law)

Suppose the selected facets are

\[
 \phi(\mathcal E)=\{R_{s_1},\ldots,R_{s_C}\}
\]

in cyclic order, and put

\[
 q_j=s_{j+1}-s_j\pmod N,qquad q_j\ge1,qquad
 \sum_jq_j=N=mC.                                    \tag{3.4}
\]

In the published fixed-side dummy augmentation, deleting the dummies gives
component lengths

\[
                         L_j=q_j+1.                  \tag{3.5}
\]

Hence every component has at least `d+1` vertices if and only if the facet
SDR is `d`-spaced:

\[
 q_j\ge d\quad(1\le j\le C).                        \tag{3.6}
\]

Equivalently, with binary incidence variables \(u_{Y,i}\), one needs

\[
\begin{aligned}
 &\sum_{i:R_i\subset Y}u_{Y,i}=1 &&(Y\in\mathcal E),\\
 &\sum_Yu_{Y,i}\le1 &&(0\le i<N),\\
 &\sum_{t=0}^{d-1}\sum_Yu_{Y,i+t}\le1 &&(0\le i<N),
\end{aligned}                                       \tag{3.7}
\]

with cyclic indices.

At `d=m`, every `q_j=m`, so the image of `\phi` is one positional residue
class modulo `m`.  Thus maximal fixed-side residence is equivalent to the
existence of a phase `a` for which

\[
 \left|N_{\partial}(\mathcal A)\cap
       \{R_{a+jm}:0\le j<C\}\right|\ge|\mathcal A|
 \qquad(\mathcal A\subseteq\mathcal E).             \tag{3.8}
\]

The unconditioned shadow Hall inequalities used in the GMM--dummy proof do
not imply any one of the phase-conditioned inequalities (3.8).

#### Proof

Choose the alternating side so that, at a selected facet `R_s`, its incidence
edge is replaced by

\[
 X,d_Y,Y,R_s.
\]

After deleting `d_Y`, the new owner `Y` starts the component at that cut.  If
the opposite alternating side is chosen throughout, `Y` instead ends the
preceding component; the length formula is unchanged.
Between successive selected facets there are `q_j` old selected owners and
one inserted owner, proving (3.5).  The remaining statements are the binary
and endpoint-capacity forms of the same cyclic spacing condition. \(\square\)

Ordinary facet Hall proves (3.7) only for `d=1`.  Therefore the verified
dummy theorem gives nontrivial paths (length at least two), but no general
depth-`d` spacing theorem.

## 4. A mixed-side dummy extension

The fixed alternating side in Proposition 3.1 is convenient, not intrinsic.
The following extension gives the exact additional freedom.

### Theorem 4.1 (oriented spaced facet-incidence augmentation)

For each `Y in E`, choose a facet `R_i subset Y` and one of its two incidence
edges on (3.1).  Require all chosen incidence edges to be vertex-disjoint.
Define

\[
 b_i=
 \begin{cases}
 1,&\text{if the chosen edge is }X_{i-1}R_i,\\
 0,&\text{if the chosen edge is }R_iX_i.
 \end{cases}                                        \tag{4.1}
\]

For the selected lower positions `s_j` and gaps `q_j` of (3.4), the dummy
construction extends verbatim and produces an exact lower-rainbow spanning
forest with `C` paths of lengths

\[
                 L_j=q_j+1+b_{s_j}-b_{s_{j+1}}.      \tag{4.2}
\]

Consequently it is depth-`d` resident in the new coordinate exactly when

\[
                 q_j+b_{s_j}-b_{s_{j+1}}\ge d
                 \qquad(1\le j\le C).               \tag{4.3}
\]

At `d=m`, all component lengths must equal `m+1`, equivalently

\[
                 q_j=m+b_{s_{j+1}}-b_{s_j}
                 \in\{m-1,m,m+1\}.                 \tag{4.4}
\]

#### Proof

Replace every selected incidence edge by the three-edge detour through its
private dummy and omitted owner.  Vertex-disjointness makes these detours
simultaneously simple.  The `C` omitted owners and the `C` chosen old owners
are distinct, so the remaining `C(m-1)` owners can again be distributed
among the dummy groups; the augmented bipartite graph is `(m+1)`-regular.
The detoured Hamilton cycle is therefore alternately two-colourable, and the
residual regular bipartite graph splits into the other perfect matchings,
exactly as in the published dummy proof.  Deleting all dummies leaves `C`
paths and every real lower vertex once, hence the exact lower deck.

If `b_{s_j}=1`, the inserted owner at the first cut belongs to the following
component; if `b_{s_{j+1}}=0`, the inserted owner at the next cut belongs to
the preceding component.  Adding these two endpoint contributions to the
`q_j` old owners gives (4.2).  Equations (4.3)--(4.4) follow, and summing
(4.2) gives `W`. \(\square\)

This is a positive extension of the dummy theorem, but not a general
oriented spaced-SDR existence theorem.  The selected cycle incidences must
simultaneously satisfy facet ownership, vertex-disjointness, and (4.3).

At `m=2`, every saturating cycle has lower order `a,b,c,d`, selected owners
`ab,bc,cd,da`, and omitted owners `ac,bd`.  A fixed-side SDR selects one
position of parity `a,c` and one of parity `b,d`; its gaps are `1,3`, giving
component lengths `2,4`.  Mixed sides remove this artificial obstruction:
choose the incidences

\[
 X_3R_0\quad\text{for }Y_0=R_0\cup R_2,
 \qquad
 R_1X_1\quad\text{for }Y_1=R_1\cup R_3.
\tag{4.5}
\]

They are vertex-disjoint, and (4.2) gives lengths `3,3`.  Thus mixed-side
selection can genuinely improve residence; what remains open is its
all-`m`, all-`d` existence.

## 5. Exact protected-window and compiler-port ledger

Fix `1<=H<=m`.  Let \(F_A\) be any spanning exact lower-rainbow path forest on
`M`, with
`C` components of owner lengths

\[
 \ell_1,\ldots,\ell_C,qquad
 \sum_j\ell_j=W.                                    \tag{5.1}
\]

Assume \(\ell_j\ge H+1\) and local residence through depth `H`: every
intersection of `q+1` consecutive owners within a path has rank `m-q`, for
`1<=q<=H`.

For \(S\in\binom{\Omega}{m-q}\), define

\[
 \omega_q(S)=
 \sum_{P}\#\left\{i:
   \bigcap_{s=0}^{q}T_{i+s}=S\right\}.              \tag{5.2}
\]

### Theorem 5.1 (protected-port counts and collision identity)

For every `1<=q<=H`:

1. the number of protected `q`-edge windows is

   \[
   I_q:=\sum_j(\ell_j-q)
       =W-qC=(m+1-q)C;                              \tag{5.3}
   \]

2. the target shore has size

   \[
   B_q:=\binom{2m}{m-q},                             \tag{5.4}
   \]

   and

   \[
   \frac{I_q}{B_q}
     =\prod_{j=2}^{q}\frac{m+j}{m-q+j};             \tag{5.5}
   \]

3. if `h_q` is the number of zero-load targets and

   \[
   c_q:=\sum_S(\omega_q(S)-1)^+,
   \]

   then

   \[
   c_q-h_q=I_q-B_q;                                  \tag{5.6}
   \]

4. conditionally, in any completed depth-`q`-resident odd-child generalized
   braid which retains these `A` paths, the number of structural cross ports
   is `2C`, and the `z`-containing erosion columns are exactly the windows in
   (5.2).  Hence the child target `\{z\}\cup S` has positive protected
   compiler-port degree exactly when `\omega_q(S)>0`.

#### Proof

Path `j` has exactly `ell_j-q` internal windows, giving (5.3).  Equation
(5.5) is the quotient of (5.3) and (5.4), after cancelling factorials.
Under local residence every window contributes to exactly one target in
(5.2), so

\[
 \sum_S\omega_q(S)=I_q.
\]

If the support has size `B_q-h_q`, subtracting one from every positive load
gives (5.6).  Each nontrivial A path has two endpoint slots.  Every cross
edge leaves the `z` sector, so a window containing `z` lies wholly in one A
path.  The child envelope and `\{z\}\cup S` have the same rank; containment
therefore forces equality, proving item 4. \(\square\)

For `q=2`, put

\[
 N_2=\binom{2m}{m-2}=\frac{m(m-1)}{m+2}C,
 \qquad D:=N-N_2=\frac{3m}{m+2}C,
 \qquad
 t=\frac{2(m-1)}{m+2}C.                             \tag{5.7}
\]

Then

\[
 I_2=(m-1)C=N_2+t,
 \qquad c_2-h_2=t.                                  \tag{5.8}
\]

The surplus `t` is exactly the number `D-C` of upper-forest direct jumps
restored in the cyclic two-tight-band splice.  It is also the difference
between the cyclic `BB` edge count and the number of distinct no-`z` upper
targets.  This scalar coincidence does not force `h_2=0`.

There is an exact one-rank-lower reformulation, and it does not require a
separate residence hypothesis at `q=2`.  Replace each owner path

\[
 T_0,T_1,\ldots,T_{\ell-1}
\]

by its colour path

\[
 R_i=T_i\cap T_{i+1}\qquad(0\le i<\ell-1).
\]

These paths form a spanning linear forest on the `N=mC` rank-`m-1` colour
vertices, with `C` components and `N-C=I_2` edges.  Consecutive colours
`R_i,R_{i+1}` are distinct facets of the common owner `T_{i+1}`;
therefore their intersection has rank exactly `m-2`.  Every derived edge is
coloured by

\[
 R_i\cap R_{i+1}\in\binom{\Omega}{m-2},             \tag{5.9}
\]

and its colour load is exactly `omega_2`.  For fixed `S`, the possible
colour vertices are the `m+2` supersets `S+x`; since the derived graph is a
forest,

\[
                         0\le\omega_2(S)\le m+1.     \tag{5.10}
\]

In particular,

\[
 |\operatorname{supp}\omega_2|
 \ge \left\lceil\frac{(m-1)C}{m+1}\right\rceil,
 \qquad
 h_2\le N_2-
 \left\lceil\frac{(m-1)C}{m+1}\right\rceil.        \tag{5.10a}
\]

Thus protected `q=2` is itself a coloured-forest coverage problem one rank
below q1.  Minimum component length supplies its edge count, not its colour
support.

At `m=7,d=3`, the exact ledger is

\[
\begin{array}{c|c}
\text{structural cross ports}&858\\
\text{protected q2 windows}&2574\\
\text{rank-five q2 targets}&2002\\
\text{forced q2 repeat surplus}&572\\
\text{depth-three z-compiler columns}&2145\\
\text{rank-four parent targets}&1001\\
\text{raw depth-three surplus}&1144.
\end{array}                                         \tag{5.11}
\]

These positive totals do not prevent a zero-load target.

## 6. Optimal spacing does not imply protected `q=2`

The independence is already exact at `m=3`.  On `[6]`, take the five paths

\[
\begin{aligned}
P_1&:146-126-124-234,\\
P_2&:345-235-236-256,\\
P_3&:356-156-135-123,\\
P_4&:136-346-134-145,\\
P_5&:125-245-456-246.
\end{aligned}                                       \tag{6.1}
\]

They partition all twenty rank-three owners.  Their fifteen internal edge
intersections are

\[
16,12,24;\quad35,23,26;\quad56,15,13;\quad
36,34,14;\quad25,45,46,                              \tag{6.2}
\]

which are every rank-two set exactly once.  Join the paths cyclically by the
five direct edges

\[
 234-345,\quad256-356,\quad123-136,\quad145-125,\quad246-146.
\tag{6.3}
\]

This gives the Hamilton owner cycle

\[
\begin{split}
146,126,124,234,345,235,236,256,356,156,135,123,\\
136,346,134,145,125,245,456,246,(146).
\end{split}                                         \tag{6.4}
\]

### Theorem 6.1 (perfect-spacing protected-window counterexample)

Mediating the fifteen internal edges of (6.4) by their distinct rank-two
intersections and leaving the five edges (6.3) direct gives a tight
enumeration of levels `2,3`.  Its direct jumps are perfectly spaced four
owner vertices apart.  Deleting them gives `C=5` paths, each of the maximal
forced length `m+1=4`, with exact lower colours and local residence through
depth three.

Nevertheless its ten protected `q=2` labels are

\[
 (1,2),\ (3,2),\ (5,1),\ (3,4),\ (5,4).             \tag{6.5}
\]

Thus labels `1,2,3,4,5` each have load two and label `6` has load zero.  In
the standard odd-child braid of Theorem 5.1(4), the protected target
`\{z,6\}` has compiler-port degree zero.

#### Proof

The owner list (6.4) is a Hamilton cycle by inspection.  The internal labels
(6.2) are the complete rank-two deck, so inserting each between its two
incident owners lists every lower vertex once.  The thirty cross-rank steps
flip one bit and the five direct Johnson steps flip two bits, for total flip
length

\[
 30+2\cdot5=40=(20+15)+(20-15),
\]

which is tight.  The direct edges occur after every fourth owner.  Every
three-owner intersection inside (6.1) is the singleton displayed in (6.5),
and every four-owner intersection is empty, proving local residence through
depth three.  Equation (6.5) is then immediate.  In that braid, equal target
and envelope ranks make the missing port irrepairable by a one-core or by the
B sector. \(\square\)

This counterexample is stronger than a short-component obstruction: the
spacing is optimal and every local rank drop is correct.  The failure is
pure protected-label chronology.

## 7. Exact remaining hypothesis

The verified GMM inputs now reduce the A side to the following simultaneous
selection theorem, which remains unproved for general `m,H`:

1. in the tight route, choose one occurrence from every colour fibre `I_R`
   so that the omitted edges satisfy (2.5); or, in the dummy route, choose a
   vertex-disjoint oriented facet-incidence SDR satisfying (4.3);
2. require local old-coordinate residence through depth `H` on every
   resulting path;
3. require the pointwise protected inequalities

   \[
   \omega_q(S)\ge1
   \qquad(1\le q\le H, S\in\binom{\Omega}{m-q});    \tag{7.1}
   \]

4. only after these A-side conditions, impose the already isolated B-jump
   colour equations, endpoint Hall inequalities, voltage/core closure, and
   common compiler Hall.

The GMM tight enumeration proves the owner cycle and exact q1 colour fibres.
The published dummy augmentation proves item 1 only at `H=1`.  The mixed-side
extension enlarges the admissible spacing family but does not prove its
existence.  Theorem 6.1 proves that even an optimal solution of item 1 plus
local residence does not imply item 3.  Therefore the minimum remaining
lemma is a **simultaneous spaced-colour/protected-window selection theorem**,
not another component-count or scalar-port estimate.
