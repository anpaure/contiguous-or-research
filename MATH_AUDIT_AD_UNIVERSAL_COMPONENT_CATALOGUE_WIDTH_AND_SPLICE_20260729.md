# Independent audit: universal even component catalogue, witness widths, and literal splice

Date: 2026-07-29  
Status: solver-free adversarial proof audit; final post-correction verdict.

## 0. Audited sources

This audit concerns the following frozen versions:

1. `MATH_THEOREM_AD_UNIVERSAL_COMPONENT_CATALOGUE_WIDTH_AND_SPLICE_20260729.md`  
   SHA-256 `df6a7cdefcc218960e702d6d6dda7d8954211dd75fb067401b5ee732b6cc52d3`.
2. `MATH_THEOREM_AD_CANONICAL_SECTION_COMPONENT_CATALOGUE_20260729.md`  
   SHA-256 `3e2307354cf3915c5d4556a5a1d4d4244cd315dac43c05b8f3bec86f8514634a`.
3. `MATH_AUDIT_AD_COMPONENT_CATALOGUE_WIDTH_COMPLETENESS_20260729.md`  
   SHA-256 `54b300663d1680a62bced53bc07e7d2d0c20109999681e8975e967a814e50635`.
4. `MATH_THEOREM_AD_EVEN_COMPONENT_DECODE_OPEN_SPLICE_20260729.md`  
   SHA-256 `4f13a88272fc8ef18d02fbdeffdbca4530e20bd24727956d8d90f039cd084623`.

No SAT solver, exhaustive search, or sustained computation was used.  The
audit is a direct proof audit.

## 1. Final verdict

The corrected synthesis passes.

* The canonical undirected edge-orbit catalogue is exact for every
  `rho`-invariant spanning simple two-factor.
* For even `r`, the `Nr^2/2` literal edge-orbit catalogue is globally
  inclusion-minimal under fixed coordinate labels.
* Arbitrary successor permutations and zero, nonunit, or unit component
  voltages require no component-by-voltage selector tensor.
* The minimal-shadow-witness upper bound and the sharp simple-cycle
  constructions are correct.
* The physical lift decoder and the active-record width-`W` Waksman splice
  are exact, including independent reversal and one cut per physical lift.
* The old-minus-cuts-plus-seams ledger is exact under its component-length
  hypothesis, and the partial global successor is the exact correction for
  short components.

The result does **not** prove that the safe shadow-width catalogue is
minimal for spanning `rho`-equivariant factors, that a splice satisfying
residence exists, or that the unrestricted common compiler is feasible.

## 2. Canonical factor catalogue

Put

\[
 K=2r,\qquad n=2r-1,\qquad W={2r\choose r},\qquad N=W/n.
\]

The cyclic action on the middle layer is free.  A nonidentity power of
`rho` has old-coordinate cycles of one common length `d>1` dividing `n`.
An invariant old part has size divisible by `d`, whereas

\[
 \gcd(n,r)=\gcd(n,r-1)=1.
\]

Thus every middle mask has orbit length `n` and every physical middle mask
has a unique canonical address `rho^a U_i` after fixing the owner-orbit
section.

For

\[
 \mathcal A=\{(i,j,p):U_i\sim\rho^pU_j\},\qquad
 \overline{(i,j,p)}=(j,i,-p),
\]

reversal has no fixed dart.  Indeed, a fixed dart would have `i=j` and
`2p=0`; oddness of `n` gives `p=0`, which is not strict Johnson adjacency.
Consequently

\[
 |\mathcal A|=Nr^2,\qquad |\mathcal E|=Nr^2/2,
 \qquad \mathcal E=\mathcal A/(a\sim\bar a).
\]

### 2.1 Undirected loop coefficient

A quotient loop represented by

\[
                    U_i\;--\;\rho^pU_i,qquad p\ne0,
\]

has physical orbit

\[
 \{\{\rho^sU_i,\rho^{s+p}U_i\}:s\in\mathbb Z_n\}.
\]

At `rho^s U_i` its two incident neighbours are the phases `s+p` and
`s-p`.  They are distinct because `2p\ne0` in the odd group.  Therefore one
selected quotient loop contributes **two**, not one, to its owner degree.
The equations

\[
                   \sum_{e\in\mathcal E}m_i(e)y_e=2
\]

are exactly physical degree two, with `m_i(e)=2` on an owner loop.  This
also proves that the Boolean quotient solution decodes to a simple physical
two-factor even when a loop voltage is nonunit: the loop orbit may split
into several physical cycles, but every physical vertex still has its two
distinct `+p` and `-p` neighbours.

For `K=16`, the stated `28` undirected quotient loops are consistent with
an analytic count.  For a fixed nonzero phase `p`, let
`g=gcd(p,15)` and `L=15/g`.  A shore mask of old size `7` or `8` differs
from its `p`-shift by one exchange precisely when one `p`-cycle carries one
nonconstant cyclic block and all other `p`-cycles are constant.  After
division by the free `15`-rotation action, the number per shore and phase is
`1,2,6` for `g=1,3,5`, respectively.  There are `8,4,2` such phases, so one
shore contributes

\[
                       8\cdot1+4\cdot2+2\cdot6=28
\]

directed loop darts.  The two shores contribute `56`, paired by reversal
into `28` undirected quotient loops.

### 2.2 Even-`r` global minimality

Counting a loop twice, the quotient pseudograph is `r^2`-regular.  When
`r` is even, write `r^2=2k`.  Orient an Euler tour in each connected
component.  Every quotient vertex then has indegree and outdegree `k`; an
oriented loop contributes one of each.  Splitting each vertex into a left
tail and right head gives a `k`-regular bipartite multigraph.  Repeated Hall
matching partitions its edges into `k` perfect matchings.

Each matching selects one incoming and one outgoing incidence at every
owner.  A selected loop supplies both incidences at that owner, exactly as
the weighted degree equation requires.  Hence every matching decodes to an
equivariant simple factor and the matchings partition all of
\(\mathcal E\).
Every edge orbit therefore occurs in some factor.  It follows that for even
`r`

\[
                     \mathcal E_{\rm fact}=\mathcal E.
\]

Thus \(\mathcal E\) is the unique inclusion-minimal subset of the literal
physical edge-orbit universe containing every invariant factor under the
fixed coordinate labels.  This is not a lower bound against a different
parametric Boolean encoding.  It also does not compute a minimum catalogue
after quotienting whole feasible factors by the additional single global
normalizer multiplier.  That multiplier acts coherently on the entire
factor and cannot be chosen independently by edge or component.

For odd `r`, the degree `r^2` is odd and the preceding edge partition is
unavailable.  The complete catalogue remains \(\mathcal E\), while its
globally inclusion-minimal support is exactly the union of supports of
feasible weighted degree-two solutions.  Equality of that union with all
of \(\mathcal E\) is not proved.

### 2.3 Oriented decoding correction

The originally displayed undirected set `E(x)` forgot the chosen component
orientations and therefore could not be an injective decoder of an
**oriented** factor.  The corrected decoder is

\[
 \mathcal D(x)=
 \{(\rho^sU_i,\rho^{s+p}U_j):x_{(i,j,p)}=1,\ s\in\mathbb Z_n\}.
\]

One-out, one-in, and

\[
                         x_a+x_{\bar a}\le1
\]

make this a directed permutation of the physical middle states whose
incoming and outgoing physical edges are distinct.  Forgetting dart order
gives the underlying simple factor.  This restores the claimed bijection.

There is also no independent oriented-support loss.  If an undirected edge
orbit `e` occurs in an invariant factor, choose the orientation of the
physical-cycle orbit containing a fixed representative edge so that it
realizes either prescribed dart above `e`, and transport by `rho`.
Stabilizers have odd order and hence cannot reverse a cycle orientation.
Therefore

\[
 \mathcal A_{\rm fact}
 =\{a\in\mathcal A:[a]\in\mathcal E_{\rm fact}\}.
\]

In particular, even `r` gives
\(\mathcal A_{\rm fact}=\mathcal A\).

## 3. Compact arbitrary-successor and voltage representation

The selected outgoing dart at owner `i` gives

\[
                 F(i,s)=(\sigma(i),s+p_i).
\]

For a `sigma`-cycle `C`, its voltage and lift data are

\[
 v_C=\sum_{i\in C}p_i\pmod n,\qquad
 g_C=\gcd(n,v_C),\qquad
 L_C=|C|n/g_C.
\]

It lifts to exactly `g_C` physical cycles of length `L_C`.  These data are
already present in the successor permutation and edge phases; no selector
over component partitions or voltage tuples is required.

A width-`N` shared-control Waksman network is therefore an exact symbolic
replacement for enumerating whole component orders.  Its
`O(N log N)`-control size is asymptotically optimal only for the declared
topology-oblivious promise of realizing all `N!` permutations.  No lower
bound of that strength is proved for the smaller family of locally legal
factor permutations.

Likewise, the \(\varphi(n)^{c-1}\) count is a count of abstract labelled unit-
voltage tuples modulo one common multiplier.  Its information lower bound
applies to an interface promised to admit and distinguish all such tuples.
It is not an unconditional lower bound for legal spanning factors unless
realization of all those relative-voltage classes is separately proved.

## 4. Minimal literal shadow witnesses

Let `A_0,...,A_(w-1)` be distinct consecutive states in a one-pass interval
of a simple Johnson cycle.

For an upper depth-`q` target `T`, set `D_i=T\setminus A_i`; for a lower
depth-`q` target `L`, set `D_i=A_i\setminus L`.  In either case the `D_i`
are distinct `q`-sets in an `(r+q)`-set and a witness is equivalent to

\[
                          \bigcap_iD_i=\varnothing.
\]

Each Johnson step can add at most one new union coordinate, or remove at
most one intersection coordinate, so `w>=q+1`.  If the witness is
endpoint-minimal, deleting its last and first state leaves nonempty
intersections.  Choose

\[
 x\in\bigcap_{i=0}^{w-2}D_i,
 \qquad
 y\in\bigcap_{i=1}^{w-1}D_i.
\]

Then `x!=y` and every internal `D_i` contains both.  Hence, for `q>=2`,

\[
 w-2\le {r+q-2\choose q-2}.
\]

For `q=1`, two distinct singleton deletion sets already have empty
intersection, so the unique minimal width is two.  Thus

\[
 q+1\le w\le B_{r,q},\qquad
 B_{r,1}=2,\qquad
 B_{r,q}={r+q-2\choose q-2}+2.
\]

Every witness contains an endpoint-minimal subinterval.  Therefore

\[
 H_q(r)=\{q+1,\ldots,B_{r,q}\}
\]

is an unconditional complete detection list for every occurring proper
depth-`q` lower or upper shadow.  The common list over
`1<=q<=r-1` is

\[
 H_{\rm safe}(r)=
 \{2,3,\ldots,{2r-3\choose r-3}+2\}.
\]

### 4.1 Sharp constructions

For `2<=q<=r-1`, write

\[
 T=\{x,y\}\mathbin{\dot\cup}\Omega,
 \qquad |\Omega|=r+q-2.
\]

List every `(q-2)`-subset `E_i` of `Omega` in fixed-weight Gray order and
put

\[
 D_0=\{x\}\cup E_1\cup\{a\},\qquad
 D_i=\{x,y\}\cup E_i,\qquad
 D_{s+1}=\{y\}\cup E_s\cup\{b\},
\]

where `a notin E_1` and `b notin E_s`.  Consecutive deletion sets share
exactly `q-1` entries.  Every proper prefix has durable token `x`, every
proper suffix has durable token `y`, and the full intersection is empty.
Thus `A_i=T\setminus D_i` is a simple Johnson path whose unique union
witness for `T` has width

\[
                         s+2=B_{r,q}.
\]

Closing through states containing a coordinate outside `T` yields a simple
cycle and contaminates every interval using the closing path.  Complement
gives the lower construction.  The construction also works at `q=2`.

At depth three, choosing distinct `u_1,...,u_s` in an `(r+1)`-set with
`2<=s<=r+1` and using

\[
 D_0=\{x,u_1,u_2\},\quad
 D_i=\{x,y,u_i\},\quad
 D_{s+1}=\{y,u_s,u_{s-1}\}
\]

gives an exact unique-width obstruction for every width
`4<=s+2<=r+3`.

These cycles prove sharpness in the class of arbitrary simple Johnson-cycle
components.  They are not proved extendible as prescribed components of a
spanning `rho`-equivariant factor.  Hence `H_safe` is an unconditional
complete upper catalogue for equivariant factors, but its minimum possible
endpoint or minimum sublist in that narrower class remains open.  The
proved negative statement is that no dimension-independent bound is WLOG
for unrestricted simple component chronologies, and gauge or the local
factor equations alone cannot establish such a bound for the narrower
spanning-equivariant class.

## 5. Physical decoding and literal splice

For a quotient cycle

\[
 C=(i_0,\ldots,i_{\ell-1}),\qquad
 P_j=\sum_{t<j}p_{i_t},\qquad v=P_\ell,
\]

put `g=gcd(n,v)` and `m=n/g`.  For every coset representative `h` of the
subgroup generated by `v`, the sequence

\[
 \Gamma_{C,h}=
 \bigl((i_j,h+qv+P_j):0\le q<m,\ 0\le j<\ell\bigr)
\]

is one physical cycle.  The `g` cycles are disjoint, have length `m ell`,
and exhaust the lift.  This decoder is valid for zero and nonunit voltages,
not only unit voltage.

Independently orient every physical cycle, cut one directed edge, and view
the remaining component as a path from the cut head to the cut tail.  A
one-cut linear Johnson ordering exists if and only if these opened paths
can be ordered so that every preceding tail is Johnson adjacent to the next
head.  This is merely the exact endpoint condition; it does not assert that
such an order always exists.

### 5.1 Sparse seam formulation

Canonical physical addresses require both relabelling artificial quotient
slots by their fixed owner-orbit IDs and applying the section gauge within
each owner orbit.  Section gauge alone cannot permute owner slots.

Root/order fields give exactly one cut per physical cycle provided their
domains are ordinary bounded integers, for example

\[
                         h_x,o_x\in\{0,\ldots,W-1\},
\]

with no modular overflow.  Otherwise a rootless cycle could wrap around the
order field and a directed seam cycle could wrap around the potential
field.

After contraction, seam indegree and outdegree at most one, exactly `c-1`
seams on `c` components, and a strict component potential give one directed
Hamilton path through the components.  The complete directed physical
Johnson seam catalogue has exactly

\[
                              Wr^2
\]

arcs before factor-dependent guards.  This is a complete upper catalogue,
not an inclusion-minimality theorem.

### 5.2 Active-record Waksman formulation

Attach to every physical state the inseparable record

\[
 (\text{root bit},\text{root address},\text{cut-tail address},
   \text{head set},\text{tail set}).
\]

Exactly one record per physical component is active.  A universal
permutation network can route all active records to a prefix in any desired
component order, while inactive records fill the suffix.  Consecutive
active output records satisfy the splice condition exactly when the first
tail set is Johnson adjacent to the next head set.  Conversely, any literal
splice order extends to a permutation of all `W` records.  Therefore the
active-record formulation is an **if and only if**, not merely a sufficient
ordering heuristic.

The unique last-active record is characterized by an active bit followed
by an inactive bit, or by being active at the last output; it routes
`bottom`.  Fields on inactive outputs are ignored.  Inverse-routing the
next-root field through the same switch settings and transferring it one
`H`-predecessor step produces the exact partial global successor.

With

\[
 q_R=1+2\lceil\log_2W\rceil+2K,
\]

the ordering layer has `S(W)` controls and at most `2q_R S(W)` routed mux
variables, plus guarded endpoint tests.  Its scale is

\[
                       O((K+\log W)W\log W).
\]

This is a complete topology-oblivious construction.  It is not claimed to
be circuit-minimal.

## 6. Exact cut and seam ledger

Fix `1<=w<=W`.  When every physical component has length at least `w`, a
cyclic width-`w` occurrence survives opening exactly when its `w-1`
transition edges avoid the cut.  A fixed cut destroys `w-1` occurrences.
At a seam there is one new interval for every nontrivial split of `w`
states between its two sides, hence `w-1` gains.  A width-`w` interval
cannot cross two seams because it would contain an entire intervening
component of length at least `w` and at least one state on each side.
Therefore, target by literal target and with multiplicity,

\[
 m_{T,w}^{\pm}(S)
 =\mu_w^{\pm}(S)
  -\sum_eL_{e,w}^{\pm}(S)
  +\sum_aG_{a,w}^{\pm}(S).
\]

The total number of surviving linear windows is

\[
 W-c(w-1)+(c-1)(w-1)=W-w+1.
\]

For `w=1`, the loss and gain families are empty.  If a component is shorter
than `w`, the seamwise decomposition can double count a window crossing
several seams and periodic repetition is not literal.  The exact
replacement is the partial global Hamilton successor `G`: a start is active
if and only if

\[
                        G^j x\ne\bot\qquad(0\le j<w).
\]

This gives exactly the `W-w+1` literal intervals without any minimum
component-length hypothesis.  In the conservative guarded-pass bound,
\(\mathcal E_J^\rightarrow\) is the directed physical Johnson-adjacency set and
has exactly `Wr^2` members.

Cut and seam accounting must remain literal.  An orbit-level provider count
is insufficient after non-equivariant physical cuts, and deleting one
provider does not create a hole when another provider survives or a seam
recreates it.

## 7. Compiler composition audit

The one-core theorem is exact only under its declared condition `DA=DP`.
The missing converse step is supplied by the corrected interval identity.
If a source interval `[a,b]` has union rank greater than `r`, then
`b-a>=d+1`; shorter intervals lie at or below the middle row.  Since
`DA=DP` and `D^dP=T`,

\[
 \bigcup_{p=a}^{b}A_p
 =(D^{b-a}A)_a
 =(D^{b-a}P)_a
 =(D^{b-a-d}T)_a
 =\bigcup_{i=a}^{b-d}T_i.
\]

Thus every upper occurrence in a one-core antecedent comes from a literal
middle-path interval, and every such middle interval lifts to the expanded
source interval.  Hall matching of the remaining lower targets is then
necessary and sufficient inside the fixed-core architecture.

Failure of this Hall system is not a lower bound against an unrestricted
antecedent satisfying only `D^dA=T`.  Likewise cyclic factor coverage,
component count, or endpoint cardinality does not imply common-compiler
feasibility.

## 8. Defects found and repaired

The adversarial audit found the following defects or missing hypotheses in
the pre-audit drafts.  All material items are repaired in the audited hashes.

1. **Oriented decoder lost orientation.**  The undirected `E(x)` could not
   decode oriented factors injectively.  It was replaced by directed
   \(\mathcal D(x)\).
2. **False oriented-support caveat.**  The claim that the extendible dart
   union might be smaller than \(\mathcal A\) even when every underlying
   edge extends was false.  The exact relation
   \(\mathcal A_{\rm fact}=\{a:[a]\in\mathcal E_{\rm fact}\}\) is now
   proved.
3. **Gauge versus owner labels.**  Section gauge was incorrectly asked to
   canonicalize owner-slot IDs.  Slot relabelling and within-orbit gauge are
   now separated.
4. **Modular order fields.**  Root and seam-potential arguments silently
   required bounded nonmodular arithmetic.  Domains and no-wrap semantics
   are now explicit.
5. **Reverse Waksman decoding.**  Last-active detection and ignored inactive
   fields are now explicit.
6. **Lower sharp closure.**  The coordinates inserted after deleting the
   durable lower token are now named before connecting through the
   token-omitting Johnson graph.
7. **Compiler converse.**  The source-interval-to-middle-interval identity
   is now proved rather than asserted as “upper-spectrum equality.”
8. **Width scope.**  Sharpness is no longer promoted from arbitrary simple
   Johnson cycles to spanning equivariant factors.  The latter minimum is
   explicitly open.
9. **Ledger endpoints.**  The range `1<=w<=W`, the trivial `w=1` case, and
   the directed meaning of \(\mathcal E_J^\rightarrow\) are now explicit.
10. **Abstract voltage lower bound.**  The \(\varphi(n)^{c-1}\) count is now
    conditioned on an interface promised to admit all abstract tuples; no
    unsupported legal-factor realization claim remains.

## 9. Exact final scope

The following are exact and WLOG within their stated objects:

1. the canonical fixed-label physical edge-orbit factor catalogue;
2. its global inclusion-minimality for even `r`;
3. arbitrary successor permutation and dart phases after an equivariant
   orientation;
4. decoding rather than selecting component lengths and voltages;
5. independent physical-lift orientations, one cut per lift, and the full
   endpoint splice criterion;
6. the safe proper-shadow width list as a complete **detection** list;
7. the literal cut/seam ledger under its length hypothesis and the partial
   global-successor replacement without that hypothesis;
8. the core-Hall compiler theorem inside `DA=DP`.

The following are only sufficient or remain open:

1. a prescribed component partition, bounded component length, or all
   component voltages one;
2. fixed small shadow lists such as `{2,3,4,6,9,13}` as all-factor claims;
3. minimum shadow-width endpoint or sublist for spanning equivariant
   factors;
4. quotient-orbit coverage after arbitrary non-equivariant physical cuts;
5. residence-safe splice existence;
6. unrestricted common-compiler feasibility;
7. circuit minimality of the physical component-order Waksman layer;
8. support-catalogue minimality modulo the one coherent global normalizer.

Accordingly, the theorem settles the component-selector question but not
literal completion: arbitrary component topology and voltage have a compact
complete symbolic catalogue, while cut-aware physical chronology and the
common compiler remain separate exact gates.
