# K16 FL0 motif 390: Farkas lock and minimal certificate expansion

Date: 2026-07-29

## 1. Exact result

Let $Q$ be the detector-zero, lower/upper-$q=1$-complete endpoint

```text
scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json
```

and let $R$ be the fixed resident PBBS endpoint.  Put

\[
\mathcal B=E(Q)\setminus E(R),\qquad
\mathcal R=E(R)\setminus E(Q).
\]

For $e\in\mathcal B$, let $b_e\ge0$ mean that $e$ is deleted from
$Q$.  For $f\in\mathcal R$, let $r_f\ge0$ mean that $f$ is inserted.
The physical model makes these variables Boolean, but the obstruction below
does not use integrality.

At every rank-eight owner $v$, degree preservation is

\[
  \sum_{f\in\mathcal R:v\in f}r_f
  -\sum_{e\in\mathcal B:v\in e}b_e=0.                 \tag{D_v}
\]

Every palette row in the guarded core has base load one and one blue
provider.  It therefore normalizes to either $b_e-r_f\le0$, when the fixed
catalogue contains one red replacement, or $b_e\le0$, when it contains
none.

The selected guarded residence obstruction is motif 390, coordinate 2,
start 8107:

```text
61994(0) -- 57902(1) -- 57998(1) -- 58250(0).
```

Write

\[
 a=b_{(57902,57998)},\qquad
 b=b_{(57902,61994)},\qquad
 c=b_{(57998,58250)}.
\]

Destroying this closed length-two run requires

\[
                         a+b+c\ge1.                   \tag{M390}
\]

**Theorem 1 (literal solver-free lock).**  The 21 guarded palette rows and
nine degree sockets in the frozen core imply

\[
                         a=b=c=0                      \tag{1}
\]

over the nonnegative reals.  Hence they contradict (M390).  Consequently no
degree-balanced switch supported by the fixed symmetric-difference catalogue
$R\triangle Q$ can simultaneously retain these 21 lower/upper-$q=1$
colours and destroy motif 390.  In particular the exact $R/Q$ overlay has no
resident both-$q=1$-complete factor.

This theorem is local to the fixed catalogue.  It does not exclude a switch
using an edge outside $Q\cup R$, a different resident endpoint, or a
different middle factor.

## 2. Explicit Farkas cancellation

Use sorted blue/red indices from the frozen overlay and put
$x=r_{11806}=r_{(57902,61990)}$.  The internal-edge branch has three exact
blocks:

\[
\begin{aligned}
T:\quad &x+r_{9710}+r_{9960}+r_{8352}\le0,\\
M:\quad &a+r_{10793}+r_{12168}-x-r_{12057}\le0,\\
E:\quad &r_{12057}+r_{5685}\le0.
\end{aligned}                                           \tag{2}
\]

The four tail pieces are

\[
\begin{aligned}
T_1={}&D_{61990}+U_{62118}+L_{61988},\\
T_2={}&D_{64036}+U_{65060}+U_{64044},\\
T_3={}&D_{47660}+U_{47676}+L_{47652},\\
T_4={}&D_{47644}+U_{47772}+U_{47645}.
\end{aligned}
\]

Their sum is $T$.  Similarly,

\[
\begin{aligned}
M_1={}&D_{59942}+U_{64038}+L_{57894},\\
M_2={}&L_{57870}+D_{59918}+U_{59950}+L_{59406},\\
E_1={}&D_{59422}+L_{51230}+U_{59486},\\
E_2={}&D_{26718}+L_{18526}+U_{27742},
\end{aligned}
\]

with $M=M_1+M_2$ and $E=E_1+E_2$.  Adding all three blocks cancels
$x,r_{12057}$ and gives

\[
\boxed{
a+r_{10793}+r_{12168}+r_{9710}+r_{9960}+r_{8352}+r_{5685}\le0.}
                                                               \tag{3}
\]

Every term is nonnegative, so $a=0$.  This certificate uses exactly 17
palette rows and eight sockets.  It explains the earlier unit-propagation
fixpoint: the missing inference is a linear implication cycle, not a parity
or Boolean obstruction.

For the incoming edge, $U_{61998}$ gives $b-x\le0$; adding $T$ gives
$b\le0$.  For the outgoing edge,

\[
U_{58254}+D_{58126}+U_{62222}+L_{57614}
\]

gives $c\le0$.  This proves (1) and then contradicts (M390).  Thus the
complete 22-row core is LP-infeasible.

The sign-by-sign derivation, all 21 provider rows, and all socket equations
are independently replayed in the two audit notes and the solver-free audit
script listed in Section 8.

## 3. Certificate-aware catalogue coefficients

The Farkas proof gives a sharp way to test a proposed new edge before any
factor search.  In this section, common edges $Q\cap R$ remain fixed and a
catalogue enlargement adds only new red insertion variables; the original
blue-deletion bank is unchanged.  For a physical Johnson edge
$e=\{S,T\}\notin Q\cup R$, put

\[
\lambda(e)=S\cap T,\qquad \upsilon(e)=S\cup T.
\]

For $j\in\{A,B,C\}$, let $\mathcal D_j$ be the degree sockets and let
$\mathcal L_j,\mathcal U_j$ be the lower/upper palette rows occurring in the
corresponding Farkas sum:

\[
\begin{aligned}
\mathcal D_A={}&\{26718,47644,47660,59422,59918,59942,61990,64036\},\\
\mathcal L_A={}&\{18526,47652,51230,57870,57894,59406,61988\},\\
\mathcal U_A={}&\{27742,47645,47676,47772,59486,59950,62118,64038,64044,65060\};
\end{aligned}
\]

\[
\begin{aligned}
\mathcal D_B={}&\{47644,47660,61990,64036\},\\
\mathcal L_B={}&\{47652,61988\},\\
\mathcal U_B={}&\{47645,47676,47772,61998,62118,64044,65060\};
\end{aligned}
\]

\[
\mathcal D_C=\{58126\},\qquad
\mathcal L_C=\{57614\},\qquad
\mathcal U_C=\{58254,62222\}.
\]

If a nonnegative variable $z_e$ for the new edge is added, its exact
coefficient in certificate $j$ is

\[
\boxed{
\kappa_j(e)=|e\cap\mathcal D_j|
-\mathbf 1_{\lambda(e)\in\mathcal L_j}
-\mathbf 1_{\upsilon(e)\in\mathcal U_j}.}             \tag{4}
\]

The first term is its incidence in the summed degree equations; the two
negative terms are the lower and upper palette tokens that the edge can
restore.  Therefore:

**Lemma 2 (necessary fixed-common branch escape).**  In such a red-only,
fixed-common enlargement, if every selected new edge has
$\kappa_j(e)\ge0$, then the $j$-th Farkas certificate persists verbatim and
its motif edge still cannot be deleted.  A repair using branch $j$ must
select at least one new edge with $\kappa_j(e)<0$.

This is stronger than raw row or socket incidence.  In particular, an edge
which both supplies a protected colour and enters a positively weighted
socket can have $\kappa_j=0$, so it does not weaken the certificate.

## 4. Complete helpful-edge census

There are 21 guarded colours.  Each has exactly 36 physical Johnson
providers.  After deduplication there are 732 providers, of which 699 are
absent from $Q\cup R$.  This finite list is complete for negative
coefficients: if an edge supplies none of the guarded colours, then (4)
reduces to the nonnegative number of its certificate sockets.

For the 699 absent relevant providers, the exact coefficient histograms are

\[
\begin{array}{c|rrr}
&\kappa=-1&\kappa=0&\kappa=1\\ \hline
A&420&268&11\\
B&229&450&20\\
C&85&608&6.
\end{array}                                             \tag{5}
\]

The complete joint histogram is

\[
\begin{array}{c|r@{\qquad}c|r}
(\kappa_A,\kappa_B,\kappa_C)&\#
 &(\kappa_A,\kappa_B,\kappa_C)&\#\\ \hline
(-1,-1,0)&202 &(0,-1,0)&27\\
(-1,0,0)&213 &(0,0,-1)&85\\
(-1,0,1)&5   &(0,0,0)&137\\
(0,0,1)&1    &(0,1,0)&18\\
(1,0,0)&9    &(1,1,0)&2.
\end{array}                                             \tag{6}
\]

In particular, no edge helpful to $C$ is helpful to $A$ or $B$, while
202 edges are simultaneously helpful to $A$ and $B$.

**Theorem 3 (minimum all-branch certificate transversal).**  The minimum
number of absent Johnson insertion edges whose negative-coefficient sets meet
all three Farkas certificates in the fixed-common, red-only enlargement is
exactly two.  Every minimum pair consists of one of
the 202 $A+B$-helpful edges and one of the 85 $C$-only edges.  Hence there
are exactly

\[
                         202\cdot85=17{,}170            \tag{7}
\]

such unordered pairs.  One explicit pair is

\[
 (57902,61966),\qquad (50062,57998),                    \tag{8}
\]

with coefficient vectors $(-1,-1,0)$ and $(0,0,-1)$, respectively.

The first edge provides $L_{57870}$ and $U_{61998}$.  The second provides
$U_{58254}$ without touching socket 58126.  By contrast, the tempting edges

\[
(57998,58126),\qquad(58126,61966)
\]

also provide an outgoing-branch colour but touch socket 58126, so their
$C$-coefficient is zero.  They do not weaken the outgoing certificate.

## 5. Exact two-new-edge physical gate

The certificate census can be sharpened from abstract edge eligibility to a
literal degree-balanced switch at this core.

**Theorem 4 (complete two-new-edge C4 census).**  Among all Johnson
2-switches which

1. delete one of the three motif-390 closure edges and one further edge of
   $Q$;
2. insert two Johnson edges absent from $Q\cup R$; and
3. preserve all 21 guarded $q=1$ supports,

there are exactly 11 switches.  Their motif-branch histogram is

\[
                         A:3,\qquad B:4,\qquad C:4.     \tag{9}
\]

Ten preserve the complete 21-row load vector exactly; the remaining one adds
one extra guarded occurrence and loses none.  Exactly ten use a second
deleted edge in $Q\setminus R$; one uses a common edge in $Q\cap R$.
A literal fixed-common-safe, exact-guarded-load example is

\[
\begin{aligned}
\text{delete }&\{(57902,57998),(59918,59948)\},\\
\text{insert }&\{(57902,59948),(57998,59918)\}.
\end{aligned}                                           \tag{10}
\]

The first inserted edge has coefficient vector $(-1,0,0)$ and restores
$U_{59950}$; the second is coefficient-neutral because its restoration of
$L_{57870}$ is offset by its incidence at socket 59918.  All four displayed
edges are Johnson edges, the second deleted edge lies in $Q\setminus R$,
and both inserted edges are absent from $Q\cup R$.

Within the nontrivial Johnson $C_4$ class, two cross edges are built into
the switch.  The complete replay additionally proves that every one of the
25 Johnson squares through motif 390 has both cross edges outside
$Q\cup R$.  Thus two outside edges are necessary and sufficient **within
this C4 class**.  This is not a lower bound for longer alternating circuits,
which may combine one outside edge with existing $R\setminus Q$ insertion
edges.

Before the support filter, there are exactly 25 such Johnson squares through
motif 390, with branch counts $(7,9,9)$.  All 25 happen to have both inserted
edges outside $Q\cup R$.  The 21-row filter leaves the 11 in (9).

The full physical $q=1$ audit is sharper again.

**Theorem 5 (unique full-$q=1$ portal and exact defect transport).**  Exactly
one of the eleven switches preserves *every* physical lower and upper
$q=1$ support:

\[
\begin{aligned}
\text{delete }&\{(57902,61994),(25135,29230)\},\\
\text{insert }&\{(25135,57902),(29230,61994)\}.
\end{aligned}                                           \tag{11}
\]

Both deleted edges lie in $Q\setminus R$, and both inserted edges are
absent from $Q\cup R$.  The switch destroys motif 390.  Its only physical
$q=1$ load changes are

\[
\begin{array}{c|cc}
&\text{old load}&\text{new load}\\ \hline
L_{29226}&1&2\\
L_{57898}&2&1\\
U_{29231}&2&1\\
U_{57903}&1&2,
\end{array}                                             \tag{12}
\]

so both palettes remain hole-free.

This portal does not reduce the unweighted short-run count.  It removes exactly motif 390 and
creates exactly one new motif: coordinate 9, length 3, with closure

\[
\{(28782,29230),(29230,61994),(61800,62248),(61994,62248)\}.
                                                               \tag{13}
\]

Thus its exact gate vector

\[
(\text{lower holes},\text{upper holes},M390\text{ survives},
 \text{new shorts},\text{removed shorts},\text{total shorts})
=(0,0,\mathrm{false},1,1,2222).                         \tag{14}
\]

The switched factor has three physical components of lengths

\[
                         12{,}424,\quad433,\quad13.
\]

The new coordinate-9 motif lies on the 12,424-cycle.  Define

\[
 \Psi_4(F)=\sum_{M\in\operatorname{Short}(F)}(4-\ell(M))
                                                               \tag{15}
\]

where $\operatorname{Short}(F)$ is the occurrence-labelled multiset of
cyclic one-runs of lengths 1, 2, and 3.  Then this portal has

\[
                         \Psi_4(F')-\Psi_4(F)=-1,              \tag{16}
\]

because it replaces one length-two motif by one length-three motif.  Thus it
is neutral for the unweighted short-run count but strictly improving for the
erosion-deficit potential.  No claim is made that every positive
$\Psi_4$-state admits another such improving portal.

In particular, a two-outside-edge $C_4$ suffices for a degree-balanced,
full-$q=1$, motif-390-destroying switch, and it is the unique such C4.  No
global minimum is proved over longer alternating circuits.  What remains is
not C4-portal existence but composing such transports so that newly created
motifs collide and annihilate, or are lengthened past the forbidden
length-three threshold, rather than merely move.

This theorem closes the *local guarded-core C4 expansion class* exactly.  It does not
say that (10), or any of the other ten squares, preserves the thousands of
palette rows outside the core, avoids every newly created short run, or
extends to the desired global endpoint.

## 6. Relation to the 147 row transversals

The earlier branch-tree audit has four row-certificate leaves
$\mathcal A,\mathcal B,\mathcal C,\mathcal D$.  If one permits only changes
to row semantics while freezing all nine degree sockets, their minimum row
transversal has size three and there are exactly

\[
                         3(9+8\cdot6-8)=147             \tag{17}
\]

minimum row triples.  Equation (7) does not contradict (17): one physical
edge can provide one lower and one upper token, and a catalogue edge also
changes the support of its two degree equations.  The coefficient census is
the sharper test for actual edge additions.

Neither count is a physical completion theorem.

## 7. Exact proved/conditional boundary

The following statements are proved.

1. The fixed $R\triangle Q$ overlay cannot hit motif 390 while preserving
   the 21 guarded $q=1$ colours; the obstruction is linear over
   nonnegative reals.
2. In the fixed-common, red-only enlargement, Equation (4) is the exact
   change in each displayed Farkas certificate caused by a new red Johnson
   edge.
3. In that same enlargement, the lists (5)--(7) are complete for all absent
   edges that can weaken those certificates.
4. Within that coefficient model, two absent edges are necessary and
   sufficient to invalidate all three *displayed certificates*
   simultaneously, and all 17,170 such pairs are enumerated.
5. Independently, exactly 11 two-outside-edge $C_4$ switches destroy motif
   390 while preserving the 21 guarded supports.  Within the C4 class, two
   outside edges are necessary and sufficient; no global lower bound for
   longer circuits is claimed.
6. Exactly one of those switches preserves both complete physical $q=1$
   palettes; it transports one short motif to one new short motif and hence
   has zero short-count drift but erosion-deficit drift $-1$.

The following statements are not proved.

1. A negative coefficient is not by itself a legal switch.  The complete
   C4 census proves that some negative edges extend legally, not that every
   one does.
2. The explicit robust pair (8) invalidates the three inequalities but is not itself
   asserted to be a completed alternating circuit.
3. An existential repair may choose one motif branch, so invalidating all
   three certificates is stronger than necessary.  Conversely even one
   weakened certificate may remain globally infeasible for other reasons.
4. The unique full-$q=1$ C4 is short-count-neutral, not residence-clean.  No
   residence-clean $k=16$ factor, no deeper-shadow carrier, and no
   compiler is constructed here.

Thus the next exact move class is sharply restricted: enumerate or construct
alternating circuits containing a selected $\kappa_j<0$ edge for the motif
branch they delete, then re-audit degree, both complete $q=1$ palettes, all
new short-run closures, deeper shadows, and only afterward the compiler.  A
generic fixed-common, red-only provider-star expansion that contains no
negative-coefficient edge cannot solve this core.  If common edges may become
deletable, their new blue variables require a separate coefficient audit.

## 8. Frozen artifacts

```text
FL0 endpoint
17bd05a0bb0da228e580d65bdec27ce04589072baecb8575e0623fc4ea4343b8
scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json

detector-zero full bank
703d44d0e949094a6bc37ed0a44b1a3caca2af74fda24cf0908c84a98246976d
scratch/k16_failedlit0_fullbank_20260729.audit.json

exact overlay no-go
4fd0b2d2a15326b9ecfa5c1b939f835814ca2d5303268268ad1ea639e33fdcf2
scratch/k16_failedlit0_exact_overlay_20260729.json

22-row guarded core
2f8031fff879faf42b80a169aee2f0a0f5a2484987c5fe625c20fc5bf945c238
scratch/k16_failedlit0_guarded_q1_motif_core_20260729.json

forced internal-edge 17-row core
ab08cc116e5aa284f0c2cce34ceb3d9bc2ebfcca0208025317d40241752677a5
scratch/k16_failedlit0_b11795_q1_core_20260729.json

solver-free branch-tree script
d545ed1abe07d3b09f3437d6791ee3badfb419451288893ede1a822fc878f8cc
scratch/audit_k16_failedlit0_motif390_branch_cores_20260729.py

solver-free branch-tree replay
70fd8101aac580b90a4add44213278920f0eb834265f4f0ad32146cacfb74033
scratch/k16_failedlit0_motif390_branch_cores_20260729.audit.json

complete guarded-colour provider catalogue
9ba223ea58e00cd2f9619c5ce7f309ff45c62b5d90beabb7cea3b30aa254df70
scratch/k16_failedlit0_complete_core_q1_provider_catalogue_20260729.json

coefficient-aware replay script
a52ea6bc15ff6a75f042b3bd36c9cd2d2cc4c20d3006be0a74e444f9bb9a5bfd
scratch/audit_k16_fl0_motif390_catalogue_expansion_20260729.py

coefficient-aware replay
370bfed7b9deee2a0d7bca6ea0e308d7cef6f91ef548431cae31607e97de079d
scratch/k16_fl0_motif390_catalogue_expansion_20260729.audit.json

two-new-edge C4/full-q1 replay script
2555ef8d94b5ea81b710742076865e309247601b76c74553d123d32645cde9df
scratch/audit_k16_fl0_motif390_two_new_c4_20260729.py

two-new-edge C4/full-q1/motif replay
34d06b1e4de36c6bc96b954bbdcea08907f1ae1105c8c3dc0dc1e74804e4de82
scratch/k16_fl0_motif390_two_new_c4_20260729.audit.json
```

Detailed independent derivations:

```text
MATH_AUDIT_K16_FAILEDLIT0_GUARDED_MOTIF390_SOLVER_FREE_CORE_20260729.md
MATH_AUDIT_K16_FL0_MOTIF390_EXPLICIT_FARKAS_CERTIFICATE_20260729.md
```
