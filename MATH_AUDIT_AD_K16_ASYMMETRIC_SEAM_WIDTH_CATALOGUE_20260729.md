# K16 asymmetric near-carrier: exact seam-width catalogue and one-cut obstruction

Date: 2026-07-29  
Status: solver-free exact local catalogue, exact one-cut impossibility, and an
exact multi-cut/global-successor formulation.  No simultaneous repair is
claimed.

## 1. Frozen input and scope

The input is

```text
scratch/k16_asymmetric_two_rail_factor_20260729.json
SHA-256 4f5368d063bcfddfe5c2be6d7f68d5ebc38327ee3c4f40d6b00d9d05c1ace139

scratch/k16_asymmetric_two_rail_factor_20260729.audit.json
SHA-256 d7aa0e13f0e30d0d814187d6892662cc4234d7f81e901c70bac4559fe3377e23
```

It is a simple spanning two-factor of `J(16,8)` with `28` components, every
component has at least `16` vertices, and its undirected edge set is invariant
under the rotation `rho` of the first fifteen coordinates.  It has positive
residence at least four and complete lower and upper q1 palettes.  Its only
fixed-window holes are

\[
\begin{array}{c|c|c}
 &\text{orbit representatives}&\text{literal total}\\ \hline
\text{lower q2}&33337,33609,34069&3\cdot15=45,\\
\text{upper q3}&36343,36599,39791,39911,40623,46811
 &5\cdot15+3=78.
\end{array}                                                   \tag{1.1}
\]

The rank-eleven orbit represented by `46811` has size three; every other
orbit in (1.1) is free of size fifteen.  Direct rotation of the nine displayed
representatives reproduces the two literal hole lists in the frozen audit
exactly.

This note answers three different width questions, which must not be
conflated.

1. A fixed lower-q2 row means width exactly three, and a fixed upper-q3 row
   means width exactly four.
2. The set of all one-seam providers for the same rank-eleven masks can use
   longer widths.
3. Arbitrary-upper/compiler coverage is existential over all interval widths.
   The exact endpoint-minimal theorem, not a local short-window guess, gives
   the WLOG range.

## 2. Exact one-cut seam records

For a source component `Gamma`, choose a sign `epsilon_Gamma` and let

\[
                     H_\Gamma=s_\Gamma^{\epsilon_\Gamma}              \tag{2.1}
\]

be either cyclic orientation.  A directed cross-component seam record is

\[
 a=(x,y,\epsilon_\Gamma,\epsilon_\Delta),\qquad
 x\in\Gamma,\quad y\in\Delta,\quad\Gamma\ne\Delta,\quad x\sim y.      \tag{2.2}
\]

It cuts

\[
 c_L(a)=\{x,H_\Gamma x\},\qquad
 c_R(a)=\{H_\Delta^{-1}y,y\},                                  \tag{2.3}
\]

and joins the resulting tail `x` to the resulting head `y`.  For width `w`
and split `1<=j<w`, its crossing word is

\[
 Q(a;w,j)=
 (H_\Gamma^{-(j-1)}x,\ldots,H_\Gamma^{-1}x,x,
  y,H_\Delta y,\ldots,H_\Delta^{w-j-1}y).                       \tag{2.4}
\]

Write `I(a;w,j)` and `U(a;w,j)` for the intersection and union of (2.4).

### Theorem 2.1 (complete one-cut local catalogue through width eleven)

In a one-cut opening of every one of the 28 frozen components, every new
window of width `2<=w<=11` is exactly one of the words (2.4), and every
selected record (2.2) creates all `w-1` displayed splits.  No width in this
range crosses two seams.

#### Proof

The head and tail identities are precisely the decoder in
`MATH_THEOREM_AD_EVEN_COMPONENT_DECODE_OPEN_SPLICE_20260729.md`.  A window
crossing two seams contains the entire opened component between them and at
least one vertex on either side.  Every opened component has at least 16
vertices, so such a window has width at least 18.  Hence every window of
width at most 11 is either an unchanged internal source window or has the
unique form (2.4).  Conversely, each split in (2.4) is present around the
selected seam.  QED.

For a source cut `c`, let `L_{c,w}^\pm(T)` count the cyclic width-`w`
occurrences of target `T` destroyed by `c`, and put

\[
 G_{a,w}^-(T)=\#\{j:I(a;w,j)=T\},\qquad
 G_{a,w}^+(T)=\#\{j:U(a;w,j)=T\}.                       \tag{2.5}
\]

If `X` is the set of 28 selected cuts and `Y` the 27 selected seams, the
literal ledger is

\[
 m_{T,w}^\pm(T_0)=\mu_w^\pm(T_0)
 -\sum_{c\in X}L_{c,w}^\pm(T_0)
 +\sum_{a\in Y}G_{a,w}^\pm(T_0).                        \tag{2.6}
\]

This is an identity, including multiplicity.  In particular, a cut which
removes the last old occurrence of a previously covered colour creates a new
demand.  It is unsound to impose only the nine positive-gain rows unless the
cut set is independently protected against all other last-occurrence losses.

### Corollary 2.2 (exact one-cut record model)

For each component `Gamma`, let

\[
 \mathcal P_\Gamma=\{(\epsilon,x):\epsilon\in\{-1,1\},\ x\in\Gamma\}.
                                                                    \tag{2.7}
\]

Choose exactly one `p in P_Gamma`.  It fixes both the cut tail and cut head.
For every compatible ordered pair `p in P_Gamma`, `q in P_Delta`, introduce
a seam bit `z_{pq}` when the tail of `p` is Johnson-adjacent to the head of
`q`.  The ordinary in/out-degree-one rows, one first record, one last record,
`sum z=27`, and strict component-order potentials make the selected records
one path.  Equation (2.6) is then linear in the record and seam bits.

The frozen instance has

\[
 \sum_\Gamma|\mathcal P_\Gamma|=2\cdot12870=25740             \tag{2.8}
\]

cut/orientation records and exactly `1,269,120` directed oriented
cross-component seam records before residence and palette filtering.  This
is a complete one-cut model; it does not assume a common orientation for
different physical components.

## 3. Fixed depth versus arbitrary upper width

### Theorem 3.1 (exact width boundary)

For the nine concrete deficit orbits:

1. every lower-q2 literal has a positive-residence-compatible local provider
   at width three;
2. every upper-q3 literal, including all three members of the `46811` orbit,
   has a positive-residence-compatible local provider at width four;
3. widths three and four are respectively minimal; and
4. for arbitrary-upper detection of a rank-eleven target, the exact WLOG
   endpoint-minimal range is

   \[
                              4\le w\le11.                 \tag{3.1}
   \]
5. on the frozen cross-component one-cut arms, the exact endpoint-minimal
   upper support is the smaller set `w in {4,5}`.

#### Proof

A Johnson step can delete at most one member from the running intersection
and add at most one member to the running union.  Starting at rank eight,
rank six therefore needs at least two transitions and rank eleven at least
three.  This proves the lower bounds three and four.  The exhaustive local
census described in Section 7 supplies positive-safe examples at those
bounds for every literal target and verifies rotation-uniform provider
counts.

For claim 4, apply Theorem 2.1 and Corollary 2.2 of
`MATH_AUDIT_AD_COMPONENT_CATALOGUE_WIDTH_COMPLETENESS_20260729.md` with
`r=8,q=3`:

\[
 B_{8,3}=\binom{8+3-2}{3-2}+2=\binom91+2=11.              \tag{3.2}
\]

Every arbitrary interval witness contains an endpoint-minimal subinterval,
and every such subinterval has width from four through eleven.

For claim 5, the independent replay listed in Section 7 tests every frozen
cross-component one-seam ribbon at every width four through eleven.  It
finds endpoint-minimal support exactly `4,5`; at widths six and seven every
raw target occurrence keeps the same union after deleting at least one
endpoint.  Repeated deletion cannot produce an old internal target
occurrence, because the six upper target orbits are absent at every old
cyclic width.  Thus the resulting same-target subinterval still crosses the
same seam and has width four or five.  QED.

The scope consequences are important.

* To repair the **fixed upper-q3 row**, only width four counts.  A width-five
  or width-seven union does not repair that fixed row.
* To repair the **arbitrary upper/compiler row**, widths four through eleven
  are the exact unconditional detection catalogue.  A width-four provider
  repairs both rows, but a proof that some locally available width-four
  provider survives all endpoint, cut, loss, and chronology constraints is
  still missing.
* In the frozen one-cut cross-component catalogue, raw occurrences have
  support `4,5,6,7`, with none at widths `8,9,10,11`.  Endpoint minimization
  removes every width-six and width-seven column: the exact WLOG support is
  `4,5`, before and after the local positive-seam filter.  Thus width at most
  six does suffice here, and width at most five is already complete.  This
  frozen one-cut reduction does not change the unrestricted
  multi-cut/compiler endpoint eleven, because a minimal word may cross
  several seams.

Representative **raw** positive-safe cross-component provider counts per
literal target are:

\[
\begin{array}{c|c|rrrr}
\text{type}&\text{rep}&w=3&w=4&w=5&w=6\\ \hline
-q2&33337&90&0&0&0\\
-q2&33609&74&0&0&0\\
-q2&34069&74&0&0&0\\ \hline
+q3&36343&0&210&62&14\\
+q3&36599&0&198&86&14\\
+q3&39791&0&286&114&32\\
+q3&39911&0&282&142&40\\
+q3&40623&0&228&118&32\\
+q3&46811&0&340&140&30
\end{array}                                                   \tag{3.3}
\]

Counts in (3.3) include the orientation and split.  They are local records,
not a matching: two listed providers can demand different cuts or
orientations on the same component.

The endpoint-minimal counts for the upper representatives are:

\[
\begin{array}{c|rr|r}
\text{rep}&\text{minimal }w=4&\text{minimal }w=5&
              \text{positive-safe minimal }w=5\\ \hline
36343&1066&56&6\\
36599&868&46&12\\
39791&1220&88&20\\
39911&1066&82&30\\
40623&1028&86&18\\
46811&1310&80&30
\end{array}                                                   \tag{3.4}
\]

## 4. Nine scalar rows versus nine circulant row blocks

Let `O_j` be one of the nine target orbits.  For an arbitrary physical
splice, a quotient label by itself does not certify every phase.  The exact
deep constraint is the vector inequality

\[
 \mathbf b_j-\sum_p\mathbf L_{jp}r_p
       +\sum_a\mathbf G_{ja}z_a\ \ge\ \mathbf1_{|\mathcal O_j|},       \tag{4.1}
\]

where the coordinates are the literal rotations of the representative.
Thus (1.1) gives nine circulant/vector row blocks but

\[
                        8\cdot15+1\cdot3=123              \tag{4.2}
\]

literal scalar inequalities.  Arbitrary noninvariant cuts and seams can
load different coordinates differently.

Only when the cut and seam packets are selected in complete `rho`-orbits do
the coordinates in each block have equal load.  Then (4.1) collapses to nine
scalar inequalities.  For a seam orbit `omega`, the exact coefficient is

\[
 A_{j\omega}={1\over|\mathcal O_j|}
   \sum_{a\in\omega}\sum_{T\in\mathcal O_j}G_a(T).         \tag{4.3}
\]

It is an integer by equivariance.  A single provider slot whose label lies in
a free size-fifteen target orbit contributes one per literal target.  A slot
whose label lies in the exceptional size-three `46811` orbit contributes
`15/3=5` per literal target; multiple slots add corresponding multiples of
five.  This short-orbit coefficient does not license scalar compression for
a noninvariant physical splice.

An invariant seam packet also carries endpoint-incidence equations and cut
compatibility.  Nine satisfied scalar quota rows alone are not a factor or a
path.

## 5. Exact one-cut impossibility

### Theorem 5.1 (81-versus-123 obstruction)

No word obtained by cutting each of the 28 frozen components exactly once
and joining the opened components with 27 Johnson seams can simultaneously
fill all 45 fixed lower-q2 holes and all 78 fixed upper-q3 holes.

#### Proof

An internal surviving width-three or width-four window is an old cyclic
window, so it cannot equal one of the audited holes.  By Theorem 2.1 every
new fixed-depth witness crosses exactly one of the 27 seams.

For each of all `1,269,120` directed cross-component seam records, including
both independent source-component orientations and without imposing
residence or palette safety, the audit evaluated the two width-three
intersections and three width-four unions.  The exact histogram of the
number of distinct labels hit in the 123-hole set is

\[
\begin{array}{c|rrrr}
\text{hits per seam}&0&1&2&3\\ \hline
\text{records}&1,176,660&89,220&3,180&60.
\end{array}                                                   \tag{5.1}
\]

There is no record with four or five hits.  Therefore 27 seams cover at
most `27*3=81` distinct missing labels, strictly fewer than 123.  This
already allows unsafe seams and ignores all cut losses, so adding residence,
q1, component compatibility, or preservation constraints cannot evade the
obstruction.  QED.

This is a genuine one-cut impossibility, not an assertion that the frozen
factor cannot be repaired by a deeper rethread.

### Corollary 5.2 (width-five demand in arbitrary-upper one-cut repair)

In any frozen one-cut splice that covers the 45 fixed lower-q2 holes and the
78 upper target masks at arbitrary interval width, at least 42 distinct
upper masks require an endpoint-minimal width-five witness.

#### Proof

The 27 seams create at most `27*3=81` distinct labels among the width-three
lower and width-four upper hole rows.  All 45 lower labels must be supplied
at width three, leaving at most 36 of the 78 upper labels supplied at width
four.  At least `78-36=42` upper labels therefore need a longer
endpoint-minimal witness.  The frozen endpoint-minimal support is exactly
`{4,5}`, so each such witness has width five.  QED.

This does not assert that a globally compatible one-cut splice exists.

## 6. Multiple cuts: separated segments and the complete fallback

The same audit also includes same-source-component segment seams when

* the two source cut edges are distinct;
* the two depth-three source collars are vertex-disjoint; and
* neither cut removes an edge used by the opposite collar.

There are `3,189,780` such directed oriented local segment seams.  Their
fixed-hole histogram is

\[
\begin{array}{c|rrrr}
\text{hits per seam}&0&1&2&3\\ \hline
\text{records}&3,063,690&121,950&4,080&60,
\end{array}                                                   \tag{6.1}
\]

so the maximum is again three.

### Corollary 6.1 (separated-packet lower bound)

If every retained packet has at least four vertices, then a fixed-depth
literal path repair of the width-three lower and width-four upper rows needs
at least 41 seams and hence at least 42 packets/cuts.  Starting from 28
source components, it needs at least 14 cuts beyond one per source component.
A fixed-depth cyclic factor rethread, which has as many seams as packets,
needs at least 41 packets/cuts.

#### Proof

With four-vertex packets, every width-three or width-four window crosses at
most one seam.  Equations (6.1) and `ceil(123/3)=41` give the seam bound.  A
path on `p` packets has `p-1` seams, whereas a cyclic rethread has `p`.
QED.

This corollary is not valid for an architecture admitting packets shorter
than four: a width-three or width-four witness can then cross several seams
and need not occur in the single-seam catalogue.

### Theorem 6.2 (complete unrestricted multi-cut model)

Let `V` be the 12,870 middle owners and let `A(J(16,8))` be the 823,680
directed Johnson adjacencies.  Binary variables `g_{uv}` on these arcs,
one start bit and one end bit per owner, and ordinary order potentials give
an exact source-relative multi-cut path model through

\[
 \sum_u g_{uv}=1-s_v,\qquad
 \sum_v g_{uv}=1-t_u,\qquad
 \sum_v s_v=\sum_vt_v=1,                                 \tag{6.2}
\]

together with `g_uv=1 => h_v=h_u+1`.  Selected arcs belonging to the frozen
factor are retained source edges; every other selected arc is a replacement
seam.  Conversely every multi-cut rethreaded Hamilton path has exactly this
form.

Let `G` be the partial successor selected by `g`.  Propagate the next ten
owner addresses (or their 16-bit set payloads) from every valid start.  The
exact deep rows are

\[
\begin{aligned}
 &\bigvee_x[\,x\cap Gx\cap G^2x=L\,] &&(L\text{ a lower-q2 target}),\\
 &\bigvee_x[\,x\cup Gx\cup G^2x\cup G^3x=U\,]
       &&(U\text{ a fixed upper-q3 target}),\\
 &\bigvee_{w=4}^{11}\ \bigvee_x
   [\,x\cup Gx\cup\cdots\cup G^{w-1}x=U\,]
       &&(U\text{ an arbitrary-upper rank-eleven target}).          \tag{6.3}
\end{aligned}
\]

Every bracket is guarded by validity before the final endpoint.  Equations
(6.2)--(6.3) are exact even when a witness crosses several seams.  Add the
literal q1 rows, positive-residence rows, and every old-colour preservation
row; do not optimize an outer hole count as a proxy.  Theorem 3.1 proves
that no width beyond eleven is needed for these rank-eleven arbitrary-upper
rows.

#### Proof

The degree and strict-order rows make `G` one directed Hamilton path.  Its
retained source arcs form disjoint subpaths of the frozen cycles, exactly the
packets obtained by cutting source edges; the remaining arcs join packets.
Conversely orient every packet along a given rethread and set its path arcs.
The guarded iterates enumerate every literal interval of the displayed
widths, including multi-seam intervals.  Fixed-depth correctness is by
definition, and arbitrary-upper completeness follows from (3.1).  QED.

The 823,680-arc model is a complete fallback, not a claim of practical
minimality.  A packet model can be much smaller if it proves a packet-length
lower bound; without that proof, a catalogue containing only individual
seams is incomplete.

## 7. Reproducible audit and exact boundary

The bounded, solver-free audit is

```text
scratch/audit_ad_k16_asymmetric_seam_provider_widths_20260729.py
SHA-256 94a58651826124a210a96339bcfbb8ca6f7a78d34acad0190b5aededfc5a2766

scratch/ad_k16_asymmetric_seam_provider_widths_20260729.audit.json
SHA-256 099f4e430e7264b86c09c218f755514b1bdd7477f75be50def30b01b9605c7a2

scratch/audit_ad_k16_asymmetric_endpoint_minimal_widths_20260730.py
SHA-256 6deb39221878d902c96285bdf6073e45aaaff3bf913713df38a1b3ec4023e2c8

scratch/ad_k16_asymmetric_endpoint_minimal_widths_20260730.audit.json
SHA-256 0ba51a8a68f010c6e5c974f0624b3aba585823953fea829d13f24d1a5ee415b9
```

It verifies both input hashes, reconstructs the 45 and 78 holes from the
nine orbit representatives, verifies `rho`-invariance of the source edge
set, enumerates all literal rotations, independently checks both component
orientations, applies the exact positive-run collar test, records explicit
cut heads and tails, audits the unconditional upper range `4..11` on orbit
representatives, and performs the two max-hit censuses (5.1) and (6.1).  The
second replay independently separates raw from endpoint-minimal upper
occurrences and proves frozen one-cut support `4,5`.

The proved/conditional boundary is therefore:

* **proved:** every concrete fixed hole has a positive-safe local provider at
  its minimum possible width, three or four;
* **proved:** one cut per source component can never repair all 123 fixed
  holes;
* **proved:** a separated fixed-depth multi-cut repair needs at least 42
  packets for a literal path;
* **proved:** nine scalar deep rows are exact only for invariant packet
  selection; arbitrary splicing needs nine phase-vector blocks/123 literal
  rows;
* **proved:** arbitrary rank-eleven coverage is WLOG detectable at widths
  `4..11` in an unrestricted multi-cut chronology;
* **proved:** on the frozen cross-component one-cut arms, endpoint-minimal
  upper detection uses exactly widths `4,5`, so widths `<=6` suffice and
  width `5` is already complete;
* **not proved:** a simultaneous multi-cut selection satisfying endpoint
  degree, component orientation, positive residence, q1 preservation, all
  last-occurrence preservation, and the deep rows;
* **not proved:** compiler Hall feasibility after any such carrier repair.
