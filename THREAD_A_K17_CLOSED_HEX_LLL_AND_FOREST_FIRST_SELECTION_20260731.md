# K17 closed-hex expansion and the forest-first asymmetric escape

Date: 2026-07-31  
Lane: A, closed packets / probabilistic expansion / asymmetric central forest  
Status: exact minimum-packet conflict census and unconditional forest-first
partial theorem; no K17 repair, bounded-defect central theorem, or RSB
construction is claimed

## 0. Verdict

The first balanced layer above the raw `10--45` provider columns is already
available and can be tested exactly.  It consists of the `5433` marked-safe
alternating incidence hexagons which touch at least one of the `724`
immutable complement-run rows of the connected `OPTIMAL28` carrier.

For the literal row lists in this layer:

\[
  |\mathcal H|=5433,\qquad
  \sum_i|\mathcal H_i|=8403,\qquad
  2\le |\mathcal H_i|\le34.                         \tag{0.1}
\]

The six changed incidences give `24272` distinct unavoidable resources, of
load `1..7`.  The unavoidable incidence-conflict degree on physical hexes
is `0..10`.  In the
conservative row-designated transversal, in which one multi-hit hex cannot
be chosen independently for two rows, the labelled candidate conflict
degree is `0..20`; the row-interaction degree is `0..24`.

Thus the anchored LLL fails already before topology, new-run, upper-witness,
and compiler conflicts are inserted:

\[
  L^2=4
  <2e\cdot34\cdot20=1360e,                           \tag{0.2}
\]

and the footprint criterion gives

\[
  D=2<e\cdot7\cdot7\cdot(2\cdot24-1)=2303e.         \tag{0.3}
\]

The worst-case alteration theorem gives only a `1/340` row fraction, but
the exact list-weighted conflict sum is much sharper.  Uniformly choosing
one candidate in every actual row list has expected conflict count
`126.166129907...`; alteration therefore gives `598` of the `724` rows with
pairwise incidence-compatible designated hexes.  It still cannot be
iterated as a physical repair theorem: a hex which hits an old run need not
repair residence, and no hereditary protected list has been emitted.

There is also an exact singleton-service obstruction.  The `5433` active
hexes give a direct baseline-to-one-hex gain for only `154` of the `218`
static rank-ten targets; `64` lists are empty.  Even all `27933`
marked-safe minimum hexes leave target `63302` without a direct one-hex
gain.  This is not a global no-go—two interacting hexes can create a target
absent from both individual deltas—but it proves that the minimum one-packet
layer is not the required guarded expansion bank.

The correct alternative central lane is genuinely weaker.  If full
two-factor preservation is dropped, an ordered four-transversal is an
**affine-boundary forest**, not a zero-boundary circuit.  Its `Cat_m` source
and sink vacancies permit open alternating ears.  In the unrestricted
oriented-diamond catalogue, every lower list has exact size `m(m+1)` and
the exact cross-list resource-conflict degree is `3m(m-1)`.  The full LLL
still fails, but a direct alteration plus cycle breaking unconditionally
gives an acyclic partial ordered four-transversal of size at least

\[
       \left\lfloor {N(m+1)\over9(m-1)}\right\rfloor.        \tag{0.4}
\]

This is positive density, asymptotic to `N/9`, not bounded defect.  The
remaining forest-first theorem is a near-perfect matching/absorber using
the Catalan vacancy banks while preserving downstream residence, shadows,
and the compiler.

## 1. The authenticated closed minimum packet layer

Let `F` be the frozen lower-rainbow incidence factor on the `24310`
rank-nine owners and `24310` rank-eight colours.  The marked bank has
`4108` owners.  Its complement contains `724` old strict run rows in `257`
fixed macro components.

An alternating incidence hex `h` changes three selected incidences to the
opposite three incidences of one six-cycle.  Write

\[
 I^-(h),I^+(h),\qquad |I^-(h)|=|I^+(h)|=3,           \tag{1.1}
\]

for its removed and added colour--owner incidences, and put

\[
                         I(h)=I^-(h)\sqcup I^+(h).   \tag{1.2}
\]

Every such hex is owner-degree and lower-colour-degree neutral.  Let
`R(h)` be the old bad-run rows whose support contains a removed incidence.
The active catalogue is

\[
 \mathcal H=\{h:h\text{ avoids marked owners and }R(h)\ne\varnothing\}.
                                                               \tag{1.3}
\]

For one old row `i`, define its closed-hex hit list

\[
                         \mathcal H_i=\{h:i\in R(h)\}.       \tag{1.4}
\]

These are actual balanced packet lists.  They are **not** protected repair
lists: changing one support incidence is necessary for removing the old run,
but the rethread can create another short run.

### Theorem 1.1 (exact K17 list and incidence-conflict census)

The active closed layer has

\[
 |\mathcal H|=5433,\qquad |{i\}|=724,
 \qquad\sum_i|\mathcal H_i|=8403.                   \tag{1.5}
\]

Its list-size profile has minimum two and maximum thirty-four.  Six rows
have size two and one row has size thirty-four.  The number of rows hit by
one hex has profile

\[
              1^{2947}2^{2115}3^{263}4^{103}5^5.    \tag{1.6}
\]

Among the six-incidence resources there are exactly `24272` distinct
resources, with load profile

\[
  1^{17818}2^{5087}3^{981}4^{302}5^{54}6^{25}7^5.   \tag{1.7}
\]

Join distinct physical hexes when their incidence sets meet.  The resulting
atom-conflict degrees lie in `0..10`, with profile

\[
 0^{301}1^{777}2^{1181}3^{1184}4^{934}5^{515}
 6^{304}7^{141}8^{61}9^{25}10^{10}.                 \tag{1.8}
\]

For a conservative ordinary transversal, replace `h` in every row list it
hits by a labelled copy `(i,h)`.  Copies in different lists conflict when
their physical hexes share an incidence or are the same hex.  The `8403`
copy degrees lie in `0..20`; the maximum is attained by `(152,176)`.  The
induced interaction graph on the `724` row variables has degree `0..24`.

#### Finite proof

The producer enumerates every alternating incidence hex of the frozen
factor, filters marked owners, and records its six literal incidences and
old rows.  The Lane-A audit takes that authenticated column bank as input,
reconstructs (1.4), inverts the six incidence lists, and forms exact set
unions—no pairwise quadratic search is used.  For the labelled graph it
additionally gives each physical hex one identity resource and omits
same-list edges.  The separately cited independent split-column audit
replays the producer's incidences and row memberships from the physical
factor.  Together these audits prove the census.  \(\square\)

The identity-resource convention deliberately forbids coalescing one hex
to service several rows.  A correlated set-cover packetization may exploit
such coalescence, but it is a different random object and needs its own list
and conflict census.

## 2. Exact anchored-LLL and nibble verdict

Apply the independent-transversal theorem with

\[
                       L=2,\qquad L^+=34,\qquad\Delta=20.   \tag{2.1}
\]

### Corollary 2.1 (the full active-list LLL fails)

The sufficient condition is false by (0.2).  In resource form, append the
hex identity to its six incidence resources.  Then

\[
 D=2,\quad w=7,\quad\lambda=7,\quad\sigma=24,       \tag{2.2}
\]

and (0.3) disproves the footprint sufficient inequality.

The exact bad-event graph does not rescue the elementary symmetric test.
It has `17005` events, maximum event probability `1/6`, and maximum event
dependency degree `341`, so

\[
       e\,p_{\max}(D_{\max}+1)=154.942\ldots>1.      \tag{2.2a}
\]

Even the maximum of the eventwise quantities `e p_E(d_E+1)` is
`11.5527...`.  This rules out those elementary local-symmetric criteria; it
does not refute an asymmetric or Shearer certificate.

This is a verdict on these sufficient criteria, not an infeasibility proof.
One may discard candidates before applying the LLL.  Since the resulting
minimum list size can be at most two, an equal-size truncation could pass
the symmetric criterion only with conflict degree zero.  Existence of a
two-per-row globally orthogonal subbank has not been audited.

### Theorem 2.2 (exact weighted alteration gives 598 rows)

#### Proof

Choose one hex uniformly and independently from every actual row list.  If
`E` is the `17005`-edge labelled conflict graph, the expected number of
realized conflict edges is exactly

\[
 S=\sum_{\{(i,h),(j,g)\}\in E}{1\over|\mathcal H_i||\mathcal H_j|}
 ={1415309166305224916351\over11217821830210195200}
 =126.166129907\ldots .                              \tag{2.3}
\]

Since the realized conflict count is integer, some outcome has at most
`floor(S)=126` conflicts.  Choose one endpoint of every realized conflict
edge and delete the union of those chosen endpoints.  This removes at most
126 row representatives and leaves a conflict-free partial transversal on
at least

\[
                              724-126=598             \tag{2.4}
\]

distinct rows.  \(\square\)

For comparison, the degree-only theorem gives merely

\[
 {1\over2}{L^2\over L^+\Delta}={1\over340}.          \tag{2.5}
\]

The weighted theorem uses the actual row degrees and every exact conflict
edge.  It still does not assert residence repair: it selects
incidence-disjoint hexes designated to hit old supports.

The protected conflict graph can differ in both directions after filtering:
residence and witness tests may delete candidates and hence some old conflict
edges, while their collars and anchors add new conflicts.  Therefore the
numbers above neither upper- nor lower-bound the final protected LLL ratio.
They prove that the currently emitted unfiltered bank itself has no useful
full-transversal LLL margin.

## 3. Upper singleton service closes the minimum one-packet lane

### Proposition 3.1 (empty direct-service rows)

Against the `218` static rank-ten targets, only `355` of the `5433` active
hexes create a direct new baseline occurrence.  Their union contains `154`
targets, of individual degree `1..8`; hence `64` targets have empty direct
active-hex lists.

Across all `27933` marked-safe minimum hexes, including those which hit no
old run, `217/218` targets have a direct gain.  Target `63302` is the unique
empty direct one-hex row.

#### Proof

For each of a hex's three source colours the replay replaces

\[
 w^{\rm fixed}\cup w^-\quad\hbox{by}\quad
 w^{\rm fixed}\cup w^+.                            \tag{3.1}
\]

Literal comparison with the authenticated target bank gives the displayed
counts.  The independent split-hex audit reproduces every changed endpoint
from bitmasks.  \(\square\)

This is precisely scoped.  Two overlapping hexes can change both endpoints
of a colour and create an upper label which neither individual baseline
delta creates.  Proposition 3.1 therefore forces longer or compound packets;
it is not a global upper-shadow obstruction.

## 4. Forest-first selection is an affine-boundary object

Let `|Omega|=2m` and put

\[
 \mathcal L={\Omega\choose m-1},\quad
 \mathcal X={\Omega\choose m},\quad
 \mathcal U={\Omega\choose m+1},\quad
 K=\operatorname {Cat}_m,
\]

\[
               N=|\mathcal L|=|\mathcal U|=mK,
               \qquad M=|\mathcal X|=(m+1)K.        \tag{4.1}
\]

An oriented diamond atom is

\[
 \alpha=(L;a,b),\quad
 U_\alpha=L+a+b,quad T_\alpha=L+a,quad H_\alpha=L+b,       \tag{4.2}
\]

with `a,b` distinct outside `L` and physical arc
`T_alpha -> H_alpha`.

### Theorem 4.1 (exact defective forest normal form)

Let `A` be a family of `N-delta` atoms whose lower, upper, tail, and head
resources are separately injective.  Its directed trace has indegree and
outdegree at most one.  If it contains `c(A)` directed cycles, deleting one
atom from every cycle gives an acyclic family of size

\[
                         N-\delta-c(A),              \tag{4.3}
\]

which spans `X` as a linear forest with exactly

\[
                         K+\delta+c(A)               \tag{4.4}
\]

path components, allowing isolated vertices.  It omits exactly
`delta+c(A)` lower resources and the same number of upper resources.
Conversely every such defective ordered four-transversal is an atom family
of this form with no directed cycles.

#### Proof

Distinct tails and heads give the degree bounds.  Every non-path component
is therefore a vertex-disjoint directed cycle.  Deleting one edge per cycle
preserves all four injectivity conditions and leaves a forest.  Equations
(4.3)--(4.4) follow from `components=vertices-edges`.  The converse is the
definition read backwards.  \(\square\)

Define the directed middle boundary

\[
                 \partial\mathcal A
                  =\sum_{\alpha\in\mathcal A}
                         ({\bf e}_{H_\alpha}-{\bf e}_{T_\alpha}).    \tag{4.5}
\]

If `Z_T,Z_H` are the omitted tail and head resources before cycle deletion,
then

\[
 \partial\mathcal A={\bf1}_{Z_T}-{\bf1}_{Z_H},
 \qquad |Z_T|=|Z_H|=K+\delta.                       \tag{4.6}
\]

Thus even an exact (`delta=0`) Catalan forest has `K` source ports and `K`
sink ports.  Full directed two-factor preservation artificially imposes
zero boundary.  Forest-first selection permits alternating paths ending in
the vacancy banks; only the lower/upper palettes remain globally exact.

The weakening is strict.  At `m=3`, a frozen pair `P,Q` of double-rainbow
Hamilton cycles has no common-transversal spanning two-factor anywhere in
`P union Q`—all `6272` such factors have rank at most fourteen—while the
same union contains an exact ordered four-transversal whose lift is five
paths.

## 5. Exact unrestricted forest conflict geometry

For a fixed lower resource `L`, let `A_L` contain every ordered pair
`(a,b)`.  Then

\[
                         D:=|\mathcal A_L|=m(m+1).    \tag{5.1}
\]

The global resource degrees and pair-codegrees are

\[
 d(L)=d(U)=m(m+1),\qquad d(T)=d(H)=m^2,             \tag{5.2}
\]

\[
\begin{array}{c|cccccc}
\text{resource pair}&LU&LT&LH&UT&UH&TH\\ \hline
\text{maximum codegree}&2&m&m&m&m&1.
\end{array}                                         \tag{5.3}
\]

### Proposition 5.1 (exact cross-list conflict degree)

Join two atom copies in different lower lists when they share an upper,
tail, or head resource.  Every atom has degree

\[
                         \Delta=3m(m-1).             \tag{5.4}
\]

#### Proof

For a fixed atom, the other-list conflicts through `U,T,H` number

\[
                  D-2,\qquad m^2-m,\qquad m^2-m.     \tag{5.5}
\]

The `U cap T` and `U cap H` overlaps each contain `m-1` atoms; there is no
other-list `T cap H` overlap.  Inclusion--exclusion gives

\[
 D-2+2(m^2-m)-2(m-1)=3m(m-1).                       \tag{5.6}
\]

Equations (5.2)--(5.3) follow by the same choices of the omitted/inserted
coordinates.  \(\square\)

Giving every atom weight `1/D` loads every lower and upper resource exactly
one and every tail and head resource by

\[
                              {m^2\over D}={m\over m+1}.    \tag{5.7}
\]

The unused tail and head mass is exactly `K` on each shore.  Hence the
fractional point has precisely the vacancy budget required by (4.6); its
failure is integral correlation, not capacity.

## 6. Direct LLL fails, but a forest nibble has positive density

The equal-list independent-transversal LLL would require

\[
                 D\ge2e\Delta.                      \tag{6.1}
\]

But

\[
                 {D\over\Delta}={m+1\over3(m-1)}\le1
                 \qquad(m\ge2),                     \tag{6.2}
\]

so (6.1) fails in every dimension.  This does not disprove a full ordered
four-transversal.

### Theorem 6.1 (unconditional forest-first positive-density nibble)

For every `m>=2`, the unrestricted oriented-diamond catalogue contains an
acyclic partial ordered four-transversal of size at least

\[
             \left\lfloor{N(m+1)\over9(m-1)}\right\rfloor. \tag{6.3}
\]

#### Proof

Activate each lower list with probability

\[
                         \theta={D\over\Delta}\le1          \tag{6.4}
\]

and choose a uniform atom in every active list.  Let `A` be the number of
active rows and `C` the number of chosen conflict pairs.  The total number
of candidate conflict pairs is at most `ND Delta/2`, so

\[
 \mathbb E(A-C)
 \ge \theta N-{\theta^2N\Delta\over2D}
 ={ND\over2\Delta}.                                  \tag{6.5}
\]

Deleting one endpoint per chosen conflict leaves a four-resource-injective
atom family of at least that size for some outcome.  Its directed cycles
have length at least three: a directed two-cycle would use both orientations
of one Johnson edge and hence the same lower and upper diamond resources.
Delete one edge from every directed cycle.  At least two thirds of the
atoms remain, giving

\[
 {2\over3}{ND\over2\Delta}
 ={ND\over3\Delta}={N(m+1)\over9(m-1)}.             \tag{6.6}
\]

Taking the integer floor proves (6.3).  \(\square\)

The limiting density is `1/9`.  A near-perfect theorem needs a
quasirandom nibble plus a vacancy-bank absorber; Theorem 6.1 by itself
leaves a linear palette defect.

## 7. Exact consequence for equality and for an additive constant

Forest-first selection removes the zero-boundary packet gate only for the
central Catalan object.  It does not turn a singleton complement exchange
column into a legal modification of the connected K17 owner cycle.

If a terminal physicalization starts from a family in Theorem 4.1, write

\[
                         h=\delta+c(\mathcal A).     \tag{7.1}
\]

It has `h` lower and `h` upper palette omissions after cycle breaking.  If,
in addition, a literal compiler realizes it in length `B(k)+a`, leaves
`eta` middle masks and a further target family `H'`, and incurs no other
unrecorded seam cost, terminal listing gives the conditional bound

\[
                    \nu(k)\le B(k)+a+2h+\eta+|H'|.  \tag{7.2}
\]

Thus a uniform bound on the right-hand defect is enough for `B+O(1)`.  The
physicalization and no-extra-seam hypotheses are essential: a partial
central forest alone is not a word.  If any central/palette debt is exported
recursively rather than paid terminally, it must be reset or contracted in
the bounded sidecar potential.

Within this CLMT route, equality requires the exact `h=0` central object.
The minimum missing forest-first theorem is therefore much stronger than
the positive-density nibble:

> find a four-resource matching leaving `O(1)` lower/upper rows, with only
> `O(1)` directed cycles and an absorber into the `K+O(1)` tail/head vacancy
> banks, while preserving the residence, deep-shadow, and common-compiler
> sidecar.

A fixed total order of ground coordinates cannot provide the absorber:
the resulting monotone catalogue is exact-cover UNSAT already at `m=3`.
Any common potential must depend on middle owners, or graphic independence
must be enforced by a different alteration/absorption mechanism.

## 8. Adversarial audit and exact boundary

1. The `5433` hexes are genuinely balanced; the original `10--45` raw edge
   columns are not.
2. `R(h)` means “old support hit,” not “residence repaired.”  Therefore the
   exact `2..34` lists are an outer relaxation of protected lists.
3. The copy conflict degree `20` is conservative because it forbids one
   multi-hit action from serving several rows.  The physical atom degree
   `10` is also recorded.  Neither is advertised as the final anchor degree.
4. Candidate filtering can reduce old incidence degree while new collars
   add conflicts.  Failure of (0.2) is a failure of this direct LLL test,
   not a monotone impossibility theorem for every subcatalogue.
5. The one-hex empty target row does not survive arbitrary composition:
   compound endpoint changes can create it.
6. Forest-first open boundary applies to the central ordered-four-
   transversal.  The current connected K17 chronology still requires exact
   owner/lower-palette conservation unless it is rebuilt by that different
   architecture.

Consequently this note proves two useful boundaries and no completion:
the emitted minimum closed K17 packet layer has inadequate anchored-LLL
margin, while the unrestricted forest-first atom system has an exact
positive-density integral theorem but no near-perfect absorber.

## 9. Frozen artifacts

```text
MATH_THEOREM_THREAD_D_K17_OPT28_MINIMAL_HEX_VARIANT_STATE_20260731.md
SHA-256 6d27374be992b57c6fc6b751af5ac9f39fd68fe9ab047a62bb5d8a7e38e3c49a

MATH_AUDIT_K17_OPT28_HEX_SPLIT_COLUMN_COVERAGE_INDEPENDENT_20260731.md
SHA-256 953b6c20711a10115c26c38667298fb145dd9df92dfae2c4d6ca659a1957cc6d

scratch/threadD_k17_opt28_hex_variant_catalogue_20260731.audit.json
SHA-256 9ac6416078d73676ca63d483cf30540806ef14f588f77bf8301d0ca5b919a87e
payload ba0fce17bfe13d491cbb2cf229d3f070e75def80b50de854d89af226e5d24923

scratch/audit_threadA_k17_closed_hex_packet_conflicts_20260731.py
SHA-256 128c8fe2d3eb60af85249c34331da14b76844c6608deadfacda08cca46a6ee57

scratch/threadA_k17_closed_hex_packet_conflicts_20260731.audit.json
SHA-256 81d8ccea1e8ccfeb2a44286b68b102919cb454710c740ddd5ccd9f174478923c
payload ddc73e190907c50b94358495b69bf4cf2e4aba30860c435ed6c27d6953441cba

MATH_THEOREM_CATALAN_TWO_CYCLE_HYBRID_LOCK_AND_FOREST_ESCAPE_20260731.md
SHA-256 59c2aa3cbe2e391f7ba5aed081dba56ae12928744bf6844d242a72b658f4df6e

MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md
SHA-256 aac430e2b2aaece12c42fafe3c84df4ffa57e0837814f4ff623458e08f322d1c

THREAD_A_GLOBAL_COORDINATE_POTENTIAL_M3_EXACT_NOGO_20260731.md
SHA-256 6a4d4ddda5f7f60615269912e9f9942bd3fa1fba743508738ace9209ad3d79a5
```
