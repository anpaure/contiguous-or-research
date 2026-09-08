# Catalan run rigidity turns every `K17` facet exchange into a residence-transfer packet

Date: 2026-07-31

Status: dimension-free local theorem and exact specialization to the authenticated
`K17` Hamilton carrier; no completed rethread, word, or improved bound is claimed

## 0. Result

Let `I_r(Omega)` be the inclusion graph between rank-`r` owners and
rank-`r-1` lower colours on an odd ground set `|Omega|=2r-1`.  A connected
spanning two-factor of this graph is equivalently a Hamilton cycle on all
rank-`r` owners whose Johnson-edge intersections enumerate every
rank-`r-1` colour once.

There are three exact facts which any local `K17` repair must respect.

1. Every coordinate has exactly

   \[
   \operatorname{Cat}_{r-1}
   =\binom{2r-2}{r-1}-\binom{2r-2}{r-2}             \tag{0.1}
   \]

   positive owner runs.  For `r=9` this is `Cat_8=1430`, independently of
   the Hamilton cycle.  Hence an owner- and lower-`q1`-preserving exchange
   cannot merge away a short run without creating or re-partitioning another
   run of the same coordinate.
2. A legal facet-phase exchange is an alternating circuit in the
   owner/colour incidence graph.  Its connectedness is decided exactly by an
   occurrence-labelled matching on the exposed carrier ports.  The same port
   matching gives the exact post-exchange run-length delta.
3. Disjoint exchanges compose automatically only at the degree/rainbow
   level.  Hamilton connectedness, residence, and `q2` service additionally
   require either one global port test or sequential tests in the current
   state.  Laminar interval support is sufficient only for genuine
   two-terminal modules composed bottom-up; laminarity by itself is not a
   socket theorem.

Thus the `K16` picture of a one-sided facet absorber does not transfer
literally to `K17`.  The reusable `K17` object is a **residence-transfer
packet**: it lengthens targeted runs of lengths two or three by shortening or
re-partitioning donor runs, while an alternating incidence phase preserves
all owners and lower colours.

## 1. Authenticated carrier and incidence form

The input is

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

Write its owner order as

\[
                 V_0,V_1,\ldots,V_{N-1},\qquad N=24310,              \tag{1.1}
\]

and put

\[
                         F_i=V_i\cap V_{i+1}.                         \tag{1.2}
\]

All indices are cyclic.  The alternating sequence

\[
 V_0,F_0,V_1,F_1,\ldots,V_{N-1},F_{N-1}                              \tag{1.3}
\]

is one Hamilton cycle in the rank-nine/rank-eight inclusion graph.  It uses
every vertex on both shores once.  Conversely, contracting every rank-eight
vertex of any such alternating cycle gives the lower-rainbow owner cycle.

For a coordinate `x`, an `x`-run is a maximal cyclic interval of owners
containing `x`.  Since the complete owner layer contains owners both with and
without `x`, all such runs are finite.

## 2. Catalan run rigidity

### Theorem 2.1 (dimension-free run count)

Let `|Omega|=2r-1`, and let `K` be any connected spanning two-factor of
`I_r(Omega)`.  For every coordinate `x in Omega`, the contracted owner cycle
has exactly `Cat_(r-1)` positive `x`-runs.

#### Proof

There are

\[
 M_x=\binom{2r-2}{r-1}                                                \tag{2.1}
\]

rank-`r` owners containing `x`.  Their total selected incidence degree in
`K` is `2M_x`.

There are

\[
 C_x=\binom{2r-2}{r-2}                                                \tag{2.2}
\]

rank-`r-1` colours containing `x`.  Every owner incident with such a colour
also contains `x`, and the selected degree at each colour is two.  These
colours therefore account for exactly `2C_x` incidences inside the
`x`-positive shore.

The remaining

\[
 2(M_x-C_x)=2\operatorname{Cat}_{r-1}                                \tag{2.3}
\]

selected incidences join an `x`-positive owner to a colour not containing
`x`.  If `F` omits `x`, its unique rank-`r` extension containing `x` is
`F+x`.  Consequently each incidence counted in (2.3) is in bijection with
one mixed owner adjacency of the contracted cycle, and every mixed adjacency
is counted once.  Every positive cyclic run has two mixed boundary edges, so
the run count is half of (2.3).  \(\square\)

### Corollary 2.2 (the exact `K17` invariant)

For `r=9`,

\[
 \binom{16}{8}=12870,\qquad
 \binom{16}{7}=11440,\qquad
 12870-11440=1430=\operatorname{Cat}_8.                              \tag{2.4}
\]

Thus every coordinate of every exact `K17` owner/lower-colour Hamilton
cycle has exactly `1430` positive runs.  In the authenticated carrier the
length-two and length-three counts are:

| coordinate | length 2 | length 3 | separate-run floor deficit `2 h_2+h_3` |
|---:|---:|---:|---:|
| 0 | 53 | 93 | 199 |
| 1 | 45 | 81 | 171 |
| 2 | 49 | 101 | 199 |
| 3 | 45 | 83 | 173 |
| 4 | 48 | 93 | 189 |
| 5 | 49 | 92 | 190 |
| 6 | 42 | 95 | 179 |
| 7 | 56 | 86 | 198 |
| 8 | 54 | 91 | 199 |
| 9 | 43 | 105 | 191 |
| 10 | 58 | 96 | 212 |
| 11 | 46 | 107 | 199 |
| 12 | 55 | 94 | 204 |
| 13 | 52 | 94 | 198 |
| 14 | 48 | 88 | 184 |
| 15 | 160 | 215 | 535 |
| 16 | 160 | 215 | 535 |

The column sums are the authenticated `1063` length-two and `1829`
length-three runs.  The equality `17*1430=24310` is exact, although it is
not itself a construction of the carrier.

### Theorem 2.3 (histogram moments and conditional donor bound)

Let `h_x(ell)` and `h'_x(ell)` be the cyclic positive-run histograms of two
exact owner/lower-colour Hamilton cycles on the same Boolean layers, and put

\[
                         \delta_x(\ell)=h'_x(\ell)-h_x(\ell).          \tag{2.5}
\]

Then, for every coordinate `x`,

\[
                 \sum_{\ell\ge1}\delta_x(\ell)=0,\qquad
                 \sum_{\ell\ge1}\ell\,\delta_x(\ell)=0.             \tag{2.6}
\]

For a residence floor four define

\[
 D_x=\sum_{\ell<4}(4-\ell)h_x(\ell),\qquad
 G_x=\sum_{\ell\ge4}(\ell-4)h_x(\ell).                              \tag{2.7}
\]

In `K17`, every coordinate has positive mass `12870` and `1430` runs, so

\[
                         G_x-D_x=12870-4\cdot1430=7150.               \tag{2.8}
\]

The authenticated carrier has no length-one runs, hence

\[
                         D_x=2h_x(2)+h_x(3),\qquad G_x=7150+D_x.      \tag{2.9}
\]

In particular, the long-run excess `G_x` is abundant for every coordinate.
If every old short run is required to survive as a distinct output run, so
that short-short coalescence is forbidden, then at least `D_x` units must be
transferred into those distinct descendants and removed elsewhere.

Without that extra hypothesis, `D_x` is **not** a lower bound on transfer
from long runs.  For example, two length-two runs may coalesce to one
length-four run while a long run splits elsewhere to restore the Catalan run
count.  The unconditional facts are the two histogram moments (2.6) and the
exact excess-deficit identity (2.8), not a canonical pairing of old and new
runs.

#### Proof

The first identity in (2.6) is Theorem 2.1.  The second holds because both
cycles use the same complete owner layer, containing `M_x` owners with `x`.
Subtracting four times the first moment identity from the second gives
(2.8), and the absence of length-one runs gives (2.9).  \(\square\)

The excess-deficit identity is only a scalar feasibility check.  It neither
chooses a decomposition into transfers nor places compatible chronological
sockets.

## 3. Facet-phase exchanges and the exact port test

### Definition 3.1 (one facet-phase circuit)

Let `K` be an owner/colour Hamilton cycle in `I_r(Omega)`.  A facet-phase
circuit is a simple `K`-alternating incidence cycle

\[
 Z=(A_0,F_0,A_1,F_1,\ldots,A_{s-1},F_{s-1},A_0),                    \tag{3.1}
\]

indexed so that

\[
 A_iF_i\in K,\qquad F_iA_{i+1}\notin K.                             \tag{3.2}
\]

Necessarily

\[
                         F_i=A_i\cap A_{i+1}.                         \tag{3.3}
\]

The phase toggle is

\[
                         K'=K\triangle E(Z).                          \tag{3.4}
\]

It moves each occurrence-labelled facet `F_i` from owner port `A_i` to the
next owner port `A_(i+1)`.

### Theorem 3.2 (degree, rainbow, and coordinate flux)

The phase toggle has degree two at every owner and every lower-colour
vertex.  It therefore preserves the complete owner layer and the complete
lower-`q1` palette.  It is a Hamilton carrier exactly when `K'` is connected.

Moreover, put

\[
 a_i=A_i\setminus F_i,qquad b_i=A_{i+1}\setminus F_i.               \tag{3.5}
\]

For every coordinate `x`,

\[
 \#\{i:a_i=x\}=\#\{i:b_i=x\}.                                      \tag{3.6}
\]

Thus this individual phase circuit already has zero coordinate-boundary
flux.  Whenever `K'` is connected, it may change run lengths but not the
number of runs of any coordinate.  (For a disconnected two-factor, an
all-positive component needs a separate cyclic-run convention, so no such
statement is made.)

#### Proof

At every vertex of `Z`, one selected incidence is removed and one is added,
which proves the degree assertion.  Contraction then retains every lower
colour as one Johnson edge.  Connectedness is the only remaining condition
for one Hamilton cycle.

Along the closed Johnson walk `A_0,A_1,...,A_0`, the step across `F_i`
removes `a_i` and inserts `b_i`.  The coordinate indicator of the final
owner equals that of the initial owner, so entries and exits balance
coordinatewise, proving (3.6).  More explicitly, the mixed-boundary count at
seam `i` changes by

\[
                 \mathbf1_{\{b_i=x\}}-\mathbf1_{\{a_i=x\}},          \tag{3.7a}
\]

whose sum is zero by (3.6).  \(\square\)

### Theorem 3.3 (occurrence-labelled phase/socket criterion)

For each `F_i`, let `B_i` be its other neighbour in `K`.  Before the toggle,
the contracted colour edge is

\[
                         e_i^- = A_i\mathbin{-}_{F_i}B_i,             \tag{3.7}
\]

and afterward it is

\[
                         e_i^+ = A_{i+1}\mathbin{-}_{F_i}B_i.         \tag{3.8}
\]

Delete the `s` occurrence-labelled edges `e_i^-` from the old owner cycle.
This leaves `s` paths, allowing singleton paths when two deleted edges were
adjacent.  Give every deleted edge two distinct stubs

\[
                         p_i=(A_i,e_i^-),\qquad q_i=(B_i,e_i^-).       \tag{3.9}
\]

Let `rho` be the perfect matching of the `2s` stubs which pairs the two ends
of each retained path.  The old and new seam matchings are

\[
 \mu^- =\{p_iq_i:0\le i<s\},\qquad
 \mu^+ =\{q_ip_{i+1}:0\le i<s\}.                                   \tag{3.10}
\]

Then the components of the new owner two-factor are in bijection with the
cycles of

\[
                              \rho\cup\mu^+.                          \tag{3.11}
\]

In particular, the phase toggle preserves Hamilton connectedness if and
only if (3.11) is one `2s`-cycle.

#### Proof

Suppress the interiors of all retained paths.  They become precisely the
matching `rho`; the new coloured seams become precisely `mu^+`.  Suppression
does not change the number of connected components.  Two perfect matchings
form disjoint even cycles, giving the criterion.  \(\square\)

Occurrence labels in (3.9) are essential.  If two cuts meet at the same
owner, the two degree deficits are different stubs even though their owner
set is the same.

## 4. Exact residence delta from the same ports

### Theorem 4.1 (weighted positive-strand gluing)

Keep the cut paths and stub matchings of Theorem 3.3.  Fix a coordinate
`x`.  In every retained path, decompose the `x`-positive owners into maximal
positive subpaths.  Positive subpaths meeting no cut stub are unchanged and
may be discarded from the delta ledger.  Let `B_x` be the remaining
occurrence-labelled boundary subpaths; give each `R in B_x` weight

\[
                              w(R)=|R|.                               \tag{4.1}
\]

For a seam matching `mu`, form a weighted multigraph `G_x(mu)` on `B_x`:
whenever `mu` joins two stubs whose endpoint owners both contain `x`, join
the two boundary subpaths incident with those stubs.  Loops are retained
when both stubs lie on the same positive subpath.

The positive `x`-runs which meet a cut are exactly the connected components
of `G_x(mu)`.  The length of such a run is the sum of the vertex weights in
its component.  Consequently

\[
 \delta_x(\ell)
 =\#\{C\in\operatorname{cc}G_x(\mu^+):w(C)=\ell\}
  -\#\{C\in\operatorname{cc}G_x(\mu^-):w(C)=\ell\}.                 \tag{4.2}
\]

For deciding residence at floor four, it is enough to replace every weight
by `min(4,w)` and every component sum by capped addition

\[
                              u\oplus v=\min(4,u+v).                  \tag{4.3}
\]

Thus (4.2) is an exact finite port signature for the length-one, -two, and
-three run delta.

#### Proof

Inside a retained path, positive adjacency is unchanged.  A new seam joins
two existing positive pieces exactly when both endpoint owners contain `x`.
Taking transitive closure over these joins gives exactly the post-seam
positive runs meeting the cuts, with length equal to the number of owners in
the joined pieces.  All internal pieces cancel between the two states.
Capping at four preserves exactly the predicate “length below four.”
\(\square\)

### Corollary 4.2 (exact local repair criterion)

Fix, for every coordinate, an occurrence-labelled allowed final ledger of
short runs, including their capped lengths.  A phase packet realizes that
ledger and destroys a specified collection of old short-run occurrences if
and only if:

1. every specified old occurrence meets a deleted edge; and
2. for every coordinate, the disjoint union of
   (a) the untouched internal short-run occurrences and
   (b) the components of `G_x(mu^+)` of capped weights one, two, or three
   is exactly the allowed occurrence-labelled ledger.

In particular, the desired output has no short runs if and only if there is
no untouched internal short run and every new boundary component has capped
weight four.  A scalar comparison of the numbers of short components is not
sufficient, because their coordinates, lengths, and occurrence identities
matter.

The Catalan and mass moments of Theorem 2.3 still apply.  Hence a successful
packet necessarily re-partitions donor strands even when the local guard is
described as “absorbing” a short terminal run.

## 5. The reusable `q2` flag packet and its residence ports

The preceding exchange theorem is independent of target service.  The exact
local object which couples lower and upper `q2` is the following.

### Lemma 5.1 (four-coordinate `q2` packet)

Let

\[
 L\in\binom\Omega{r-2},\qquad H\in\binom\Omega{r+2},\qquad L\subset H. \tag{5.1}
\]

Order `H-L` as `(a,b,c,d)` and put

\[
 A=L+ab,\qquad V=L+bc,\qquad B=L+cd,                                \tag{5.2}
\]

\[
 C=L+b,\qquad D=L+c.                                                  \tag{5.3}
\]

Then

\[
                         A-C-V-D-B                                   \tag{5.4}
\]

is an incidence path and

\[
 A\cap V\cap B=L,qquad A\cup V\cup B=H.                            \tag{5.5}
\]

Its two immediate upper targets are

\[
                         A\cup V=H-d,qquad V\cup B=H-a.             \tag{5.6}
\]

Conversely, every three-owner Johnson path attaining ranks `r-2` and `r+2`
in its triple intersection and union has this form.  Fixed `L,H` have
exactly `24` directed phases.

#### Proof

The forward identities are direct.  Conversely, the two Johnson steps must
remove two and insert two distinct coordinates; equality at both extreme
ranks forces all four to be distinct.  The common core is `L`, and the
ordered replacements uniquely recover `(a,b,c,d)`.  \(\square\)

### Lemma 5.2 (exact residence guard for one phase)

Place (5.2) between retained fragments `P` and `Q`.  Let `s_P(x)` be the
length of the terminal positive `x`-run in `P`, and let `p_Q(x)` be the
initial analogue in `Q`.  Assume every positive run internal to the two
fragments already has length at least four.  Also assume that every boundary
run which the packet does **not** extend is either empty or already has
length at least four.  This includes the initial `a,b` runs of `Q`, the
terminal `c,d` runs of `P`, and both boundary runs for coordinates outside
`H`.

All positive runs meeting the packet have length at least four if and only
if

\[
 s_P(a)\ge3,\quad s_P(b)\ge2,\quad
 p_Q(c)\ge2,\quad p_Q(d)\ge3,                                      \tag{5.7}
\]

and

\[
                         s_P(x)+p_Q(x)\ge1\quad(x\in L).              \tag{5.8}
\]

#### Proof

Across `A,V,B`, the phase coordinates have binary words

\[
 a:100,\qquad b:110,\qquad c:011,\qquad d:001,                       \tag{5.9}
\]

while every coordinate of `L` has word `111`.  Their complete run lengths
are respectively

\[
 s_P(a)+1,\ s_P(b)+2,\ 2+p_Q(c),\ 1+p_Q(d),\
 s_P(x)+3+p_Q(x).                                                     \tag{5.10}
\]

Requiring these lengths to be at least four gives (5.7)--(5.8).  \(\square\)

The local path (5.4) is only a requested packet state.  It preserves the
owner and lower-colour layers only when it is installed by a union of
alternating incidence circuits whose global port matching passes
Theorem 3.3.

### Exact `q2` coexistence ledger

For an owner cycle `J` and owner `v`, let its two owner neighbours be
`n_1(v),n_2(v)` and define the centered width-three labels

\[
 L_2^J(v)=n_1(v)\cap v\cap n_2(v),\qquad
 U_2^J(v)=n_1(v)\cup v\cup n_2(v).                                  \tag{5.11}
\]

If `J'` differs from `J` only at a cut set, let

\[
 S=\{v:\{n_1^J(v),n_2^J(v)\}\ne
          \{n_1^{J'}(v),n_2^{J'}(v)\}\}.                            \tag{5.12}
\]

The exact signed canonical `q2` deltas are

\[
 \Delta^-_2=\sum_{v\in S}
   \bigl(e_{L_2^{J'}(v)}-e_{L_2^J(v)}\bigr),\qquad
 \Delta^+_2=\sum_{v\in S}
   \bigl(e_{U_2^{J'}(v)}-e_{U_2^J(v)}\bigr).                         \tag{5.13}
\]

All other centered occurrences are unchanged.  A missing target is supplied
exactly when its coefficient becomes positive.  An old covered target is
lost exactly when its old global multiplicity plus its coefficient in
(5.13) becomes zero.  Therefore lower and upper service coexist in one
phase packet if and only if both desired holes have positive final load and
neither protected deck has a zero final load.

This criterion is coupled: the same incidence phase and the same port
matching determine both signed vectors in (5.13).  Separate lower and upper
matchings do not prove a legal packet.

For the authenticated carrier, the separately frozen finite audit proves
that the containment graph between the `910` missing rank-eleven upper
targets and the `1623` missing rank-seven lower targets has `33701` edges and
a matching saturating all `910` upper holes.  Hence there is no marginal
`L subset H` obstruction.  The unresolved obstruction is chronological:
an assigned pair and one of its 24 phases must also satisfy the residence
ports, the alternating socket, Hamilton phase, and private-witness rows.

For rank-`r+2` upper targets, the centered ledger (5.13) is already complete:
the shortening lemma in the companion hex-packet theorem proves that every
interval whose union has rank `r+2` contains a witnessing three-owner
subinterval.  For ranks above `r+2`, this shortening is false in general.  If
a deleted seam destroys every old higher-rank witness, the target must then
reappear in the new suffix/prefix crossing cone; that is a separate exact
restitution condition.

## 6. Disjoint and laminar composition

### Theorem 6.1 (disjoint exchange composition)

Let `Z_1,...,Z_t` be facet-phase circuits whose incidence-vertex supports
are pairwise disjoint.  Toggling any subfamily commutes and preserves degree
two on both Boolean shores.  Thus owner exactness and the lower-`q1` rainbow
are automatic.

The following stronger conclusions require additional hypotheses.

1. Hamilton connectedness holds if and only if the single global analogue
   of `rho union mu^+`, formed from all cut stubs, is one cycle.  It is also
   sufficient to apply the packets sequentially and pass Theorem 3.3 in the
   current carrier after every step.
2. Run-histogram deltas add independently when the occurrence-labelled
   boundary positive strands of the packets are disjoint.  Otherwise the
   global strand-gluing graph of Theorem 4.1 must be used.
3. Canonical lower/upper `q2` deltas add independently when their affected
   center sets (5.12) are disjoint.  Target-hole improvements still use final
   multiplicities, so numerical “holes filled” counts need not add when two
   packets deliver the same target.
4. Upper-`q2` ledgers are exactly the centered ledgers in item 3.  Higher
   arbitrary-width upper ledgers add locally only when the protected crossing
   cones are disjoint, or when every shared target has an explicitly retained
   witness.

In particular, two vertex-disjoint alternating circuits which each preserve
Hamilton connectedness when toggled alone need not preserve it when toggled
simultaneously: their cut-port phases may interlace.

#### Proof

Disjoint symmetric differences commute and balance degrees vertexwise.  The
global port, strand, and centered-target statements are Theorems 3.3, 4.1,
and (5.13) applied to the union of the cut sets.  Hole counts are nonlinear
thresholds of the additive occurrence loads, which explains the stated
separation requirement.  \(\square\)

### Definition 6.2 (transparent two-terminal module)

A two-terminal module consists of two incidence subgraphs `M^-` and `M^+`
on the same occurrence-labelled internal owners and colours such that:

1. each state is one spanning incidence path;
2. the two states have the same two external stubs;
3. every internal owner and colour has degree two, and the two terminal
   vertices have the prescribed degree deficits; and
4. its residence, centered-`q2`, and upper crossing-cone port records are
   evaluated relative to those same two terminals.

It is **transparent** to a parent module when the parent refers to it only
through its two fixed terminal stubs and its advertised port record.

### Theorem 6.3 (laminar bottom-up composition)

Let a family of two-terminal modules be indexed by a laminar tree of carrier
intervals.  Assume children of one node have disjoint interiors, and every
parent state treats each child transparently.  Choose a state at every node
and substitute bottom-up.  If each chosen state passes its advertised port
conditions after its children have been installed, then:

1. the final incidence graph is one path at the root, and closes to one
   Hamilton cycle when the root terminals are joined;
2. owner and lower-colour degrees are exact;
3. residence is obtained by associative capped prefix/suffix strand gluing;
4. centered `q2` occurrence deltas telescope exactly through the tree; and
5. arbitrary-width upper targets are exact under the recursively computed
   prefix/suffix crossing cones.

#### Proof

Replace the children of a leaf-to-root induction by their single terminal
paths.  Transparency leaves the parent's incidence topology unchanged, so
the chosen parent state is again one terminal path.  The residence port
operation is concatenation of positive prefixes and suffixes with addition
capped at four, which is associative.  Centered triple ledgers change only
in the one-owner collars of concatenation seams and therefore telescope.
Every interval crossing a concatenation seam is uniquely one suffix, zero or
more complete child intervals, and one prefix; this gives the recursive
upper crossing cone.  \(\square\)

### Precise laminar caveat

Laminarity of the **sets of positions** alone implies none of the conclusions
of Theorem 6.3.  If nested exchanges share an owner, colour, cut stub, `q2`
halo, or upper witness without a transparent two-terminal interface, then:

* their symmetric differences need not be degree balanced as independently
  selected atoms;
* the outer alternating circuit may cease to alternate after the inner
  toggle;
* two individually Hamilton phases may split the simultaneous output;
* a residence donor counted by both packets may be spent twice; and
* a target protected in each separate ledger may lose its last common
  witness jointly.

Such a family must be evaluated sequentially in the current state or as one
global occurrence-labelled port problem.  “Laminar” is not a substitute for
that check.

## 7. Consequence for the frozen `K17` program

The owner layer and lower `q1` layer of the authenticated carrier are already
exact and should be retained.  The correct local target is therefore:

> select a growing family of four-coordinate `q2` packets, realize them by
> alternating facet phases, and choose their occurrence-labelled socket
> matching so that the global carrier remains Hamilton; use the capped
> strand ports to eliminate the short-run ledger while obeying the two exact
> histogram moments and the excess-deficit identity, and require the signed
> `q2` and upper crossing-cone ledgers to preserve all old targets and fill
> the missing banks.

The marginal `q2` pairing exists, and the scalar donor inequality has a
large surplus.  Neither fact proves chronological compatibility.  The exact
remaining local obstruction is the simultaneous existence of:

1. an alternating incidence socket containing the requested flag paths;
2. one connected global port phase;
3. guarded donor-compatible residence strands; and
4. private lower/upper `q2` restitution and higher-rank crossing-cone upper
   restitution.

The fixed-parent residence theorem now sharpens the scope of this target.
For the present K15 parent, `165` A-shore minimum-run packets use four unique
rank-six colours and survive every occurrence transversal and every port
completion.  The exact integral optimum is stronger: every transversal
leaves at least `180` internal short runs, and an authenticated one attains
`12` per old coordinate.  Therefore a packet family confined to occurrence
choice, macro order/reversal, and port flow cannot finish.  A flat
implementation of the target above must cut inside the residual debt—hence
genuinely change the inherited chronology—or the compiler must be nonflat.
The same occurrence variables also incur exact marginal upper-unique
provider debt `505`; the residence clauses and provider rewards must be
selected jointly before any macro b-flow.  Although their formal sum gives
the valid inequality `U+R>=685`, equality and simultaneous attainment are
unknown; separate marginal minimizers cannot be inserted into the
composition state independently, and `685` is not a child-hole count.

This is a precise nonflat `K17` analogue of the `K16` facet zipper.  It is a
packet-composition theorem, not a claim that the required packet family has
already been embedded.
