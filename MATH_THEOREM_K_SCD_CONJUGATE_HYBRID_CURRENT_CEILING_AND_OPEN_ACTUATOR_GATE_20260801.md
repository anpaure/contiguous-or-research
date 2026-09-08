# Conjugate SCD hybrids transport endpoint current but do not create it

Date: 2026-08-01  
Lane: K / flexible four-row SCD / external-current actuators  
Status: **exact four-shore component-switch theorem, exact directed-current
and cycle criteria, and a new ceiling for the standard GK hybrid even after
all short-provider rethreads.  Closed C6/C8 circuits have zero current and
the forward gain-one C6 has nonpositive current.  Thus the standard
`F(a,z)`--`F(z,a)` hybrid is impossible for every `m>=10`; a prospective
nonstandard or genuinely open/basis-changing packet remains live.**

## 0. Verdict

Put

\[
 c=\operatorname {Cat}_{m-1},\qquad
 I=\operatorname {Cat}_m-2c,\qquad C=\operatorname {Cat}_m=2c+I.
\tag{0.1}
\]

The raw physical symmetric difference of two owner forests is not, in
general, a union of legal alternating switches: owner degree can be four,
an upper colour can be split between different physical components, and a
component switch can create a cycle.  There is an exact repair of this
statement.  Close every directed path by a **typed dummy** carrying its
missing lower colour, terminal owner, source owner, and a private upper
label.  If these closures are rooted-legal and chosen equivariantly under
`tau=(a z)`, the red and blue augmented factors are perfect on four
resource shores.  Connected components of their four-shore incidence
graph then switch independently and preserve every palette and degree row.

For a directed path forest let

\[
 H_q=\#\{\hbox{unused lower colours containing }q\},\qquad
 S_q=\#\{\hbox{source owners containing }q\},
\]

and

\[
                         \kappa_q=1+S_q-H_q.        \tag{0.2}
\]

Every conjugate component has current change

\[
 \Delta\kappa_q=0\quad(q\notin\{a,z\}),\qquad
 \Delta\kappa_a+\Delta\kappa_z=0.                 \tag{0.3}
\]

It can transfer current from `a` to `z`, but it cannot create total
`a+z` current.  For the standard flexible SCD forest, if `D_long` is the
number of reversed-D `a`-options using long providers, then

\[
 \kappa_z=1-I,\qquad \kappa_a=c-D_{\rm long}+1.    \tag{0.4}
\]

Thus neutral conjugate switching alone is impossible for every `m>=6`.

The independent first-stage short-provider rethread `h` has the exact
positive signature

\[
                         \Delta(\kappa_a,\kappa_z)=(0,1).       \tag{0.5}
\]

After `p` such rethreads and a conjugate transfer of `r` units from `a` to
`z`, the two coordinate cuts are exactly

\[
                 I-1-p\le r\le c-D_{\rm long}+1.             \tag{0.6}
\]

This is the sharp scalar interface between the positive one-unit bank and
the neutral component cube.

The standard GK phase has a further diagonal-image loss.  With

\[
                         K={2m-4\choose m-4},                  \tag{0.7}
\]

head injectivity forces at least `K-c` reversed-long options.  Since
`p<=c`, every standard-GK hybrid therefore satisfies

\[
 \kappa_a+\kappa_z\le 3c-K-I+2<0\qquad(m\ge10).               \tag{0.8}
\]

This closes the proposed standard conjugate hybrid, even with every short
root activated, from `m=10` onward.  The statement is architecture-specific:
it does not rule out a non-GK forest, a third parent, a changed owner basis,
or an open packet with positive total current.

## 1. The exact four-shore component cube

Let `F^0` be a directed, upper-exact, lower-injective linear forest on all
rank-`m` owners.  Assume it is rooted by an incidence bijection `M_0`: each
used lower root is the tail label of its outgoing edge, and for every path
component its unused lower root `K` is paired with terminal owner `M_0(K)`.
Let `F^1=tau F^0`, rooted by `tau M_0 tau`, where `tau=(a z)`.

For each path

\[
                       T_0\to T_1\to\cdots\to T_s             \tag{1.1}
\]

of `F^0`, with unused lower colour `K`, add the formal typed atom

\[
                         d=(K,\delta,T_s,T_0),                 \tag{1.2}
\]

where `delta` is a private upper label.  The four entries in (1.2) are,
in order, lower colour, dummy upper colour, typed tail owner, and typed
head owner.  Pair the dummy for the swapped path with the same label
`delta`.  This rooted/equivariant pairing is a hypothesis; an arbitrary
bijection between holes and paths is not a connector certificate.

### Lemma 1.1 (perfect augmentation)

The augmented systems `widehat F^0,widehat F^1` use every lower colour,
every typed tail owner, every typed head owner, and every true-or-dummy
upper colour exactly once.

#### Proof

The real forest uses every true upper colour once and all but `C` lower
colours.  On each directed path every owner is a tail except the terminal
and a head except the source.  The dummy (1.2) fills precisely the missing
lower, terminal-tail and source-head resources.  Coordinate conjugation
preserves the statement.  \(\square\)

Make the bipartite atom-incidence graph whose left vertices are red atoms
of `widehat F^0`, whose right vertices are blue atoms of `widehat F^1`,
and whose edges join the two atoms using the same resource on each of the
four shores.

### Theorem 1.2 (independent four-shore switches)

For every connected incidence component `Gamma`, either take all its red
atoms or all its blue atoms.  Choices on distinct components are
independent and preserve all four resource shores exactly.  Conversely,
every hybrid obtainable by whole four-shore component switches has this
form.

Each component contains equally many red and blue dummy atoms.  After
deleting the selected dummies, the real hybrid consequently has exactly
`|V|-C` edges, every true upper colour once, distinct lower colours, and
maximum directed indegree and outdegree one.

#### Proof

No resource edge leaves an incidence component.  Within one component
each resource has exactly one red and one blue incident atom, so replacing
the red shore by the blue shore preserves that resource.  The private
dummy-upper edge places the red and blue copy of each dummy in the same
component, proving equality of dummy counts componentwise.  Deleting the
chosen dummies gives the stated real support.  \(\square\)

This theorem is the correct form of the proposed alternating-component
claim.  A component of the **raw physical** overlay is not enough.

## 2. Exact endpoint-current transport

For a dummy atom define

\[
                  w_q(d)={\bf1}_{q\in\operatorname {head}(d)}
                         -{\bf1}_{q\in\operatorname {lower}(d)}.       \tag{2.1}
\]

Because the selected dummies record exactly the sources and holes,

\[
                         \kappa_q=1+\sum_{d\ \text{ selected}}w_q(d). \tag{2.2}
\]

Hence the red-to-blue current of one component is

\[
 \Delta\kappa_q(\Gamma)=
 \sum_{d\in D^1\cap\Gamma}w_q(d)
 -\sum_{d\in D^0\cap\Gamma}w_q(d).                           \tag{2.3}
\]

### Theorem 2.1 (conjugate current is a transfer)

Every four-shore component satisfies (0.3).

#### Proof

A component without a dummy has zero right side in (2.3).  If a component
contains a dummy, its private upper edge joins that red dummy to its
coordinate-swapped blue copy.  Therefore coordinate swap together with
red/blue exchange maps the connected component to itself.  It fixes every
ordinary coordinate and interchanges `a,z`.  Applying this involution to
(2.3) gives zero on the ordinary coordinates and
`Delta kappa_a=-Delta kappa_z`.  \(\square\)

Write `r_Gamma=Delta kappa_z(Gamma)`.  Starting from a base vector
`(kappa_a,kappa_z)`, a component subset `Y` passes the two singleton cuts
if and only if

\[
 -\kappa_z\le \sum_{\Gamma\in Y}r_\Gamma\le\kappa_a.          \tag{2.4}
\]

Thus `kappa_a+kappa_z>=0` is necessary, but not sufficient: the reachable
subset-sum lattice must meet the interval (2.4).

## 3. Graphic and cycle effects

The augmented hybrid uses every typed tail and head owner once, so it is a
directed permutation of the physical owners.  Deleting its dummy arcs
gives a real linear forest exactly when every directed permutation cycle
contains at least one selected dummy.

Equivalently, consider an all-real directed cycle `Q` whose arcs are
component-consistent.  For every changed component used by `Q`, let
`b_Gamma(Q)` be the red/blue phase required by that cycle.  The exact lazy
cycle clause is

\[
                  \bigvee_{\Gamma\in I(Q)}
                         [x_\Gamma\ne b_\Gamma(Q)].            \tag{3.1}
\]

Phase-common arcs are omitted from `I(Q)`.  If `I(Q)` is empty, the base
already has an all-real cycle and the state is immediately impossible.
Individual component safety does not imply that all selected components
are jointly safe; (3.1), or equivalently the complete graphic inequalities,
must be enforced on the final hybrid.

Passing (2.4) and (3.1) is **not** yet connector completion.  One still
needs the full rooted connector Hall system: legal containments, distinct
remaining lower tickets and source endpoints, all subset cuts, and a
graphic spanning tree on the contracted real components.

## 4. The standard SCD current ledger

Let `A_C` be the number of aligned-long C options, let `D_short` be the
number of short-D options, and put

\[
                         D_{\rm long}=E-A_C-D_{\rm short},     \tag{4.1}
\]

where

\[
                         E={2m-3\choose m-3}.                  \tag{4.2}
\]

The exact SCD hole/source ledger is

\[
 H_z=c+I,\quad S_z=c,qquad
 H_a=E-A_C,\quad S_a=c+D_{\rm short}.                         \tag{4.3}
\]

Therefore (0.4) holds.  In particular

\[
 \kappa_a+\kappa_z=c-D_{\rm long}-I+2
                  \le c-I+2.                                 \tag{4.4}
\]

Since

\[
                         I-c={m-5\over m+1}c,                  \tag{4.5}
\]

the right side of (4.4) is negative for every `m>=6` (at `m=6`,
`I-c=6`).  Theorem 2.1 proves that no neutral conjugate component selection
can repair both special-coordinate cuts in those dimensions.

## 5. Adding the independent short-provider rethread

For a short root `C_S=L_S`, replace a native long `zU_0` provider by

\[
                         h_{S,U_0}: C_S\longrightarrow P(U_0).          \tag{5.1}
\]

The exchanged lower roots both omit `a,z`.  The operation releases the
source owner `zL_T` and consumes the source owner `U_0`.  Hence

\[
 \Delta H_a=\Delta H_z=0,\qquad
 \Delta S_a=0,\quad\Delta S_z=1,                              \tag{5.2}
\]

which proves (0.5).  Tail capacity gives `0<=p<=c`.

After `p` such rethreads and a neutral conjugate transfer `r`, the final
currents are

\[
 \kappa_z'=1-I+p+r,\qquad
 \kappa_a'=c-D_{\rm long}+1-r.                                \tag{5.3}
\]

This proves (0.6).  Equivalently, total current requires

\[
                         p\ge I-c+D_{\rm long}-2.              \tag{5.4}
\]

The inequalities are only the two coordinate rows.  Provider/head
injectivity, the component subset lattice, (3.1), and rooted connector
Hall remain.

The finite base behaviour is consistent with the exact ledger.  At `m=4`
there is a literal 35-root Hamilton path with three independent `h`
rethreads and 13 connectors; its `z` row is tight.  At `m=5`, the exact
base-degree maximum is `p=10<I-1=13`, so that fixed grammar fails before
connectors.  These are finite statements, not an induction.

## 6. The GK diagonal-image ceiling

The aligned C auxiliary head on a long chain

\[
 R\subset S=R+\rho\subset L=S+x\subset U
\]

has underlying map

\[
                              \psi(R)=R+x.                     \tag{6.1}
\]

Head injectivity implies

\[
                         A_C\le |\operatorname {im}\psi|.      \tag{6.2}
\]

### Lemma 6.1 (exact GK image count)

\[
 |\operatorname {im}\psi|={2m-4\choose m-3}=E-K,qquad
 K={2m-4\choose m-4}.                                        \tag{6.3}
\]

#### Proof

Use the standard unmatched-symbol decomposition of a rank-`(m-2)` GK
word.  If it has `p` unmatched ones, it has `p+1` unmatched zeros and
`2p+2` intervening Dyck gaps.  The word lies in `im psi` exactly when the
distinguished central gap is nonempty.  With the Catalan series
`C(t)=1+tC(t)^2`, the number in this stratum is

\[
 A_p=[t^{m-2-p}](C(t)-1)C(t)^{2p+1}
    =[t^{m-3-p}]C(t)^{2p+3}.                                 \tag{6.4}
\]

The standard coefficient identity

\[
 [t^n]C(t)^r={r\over 2n+r}{2n+r\choose n}                    \tag{6.5}
\]

gives, with `N=2m-3`,

\[
 A_p={2p+3\over N}{N\choose m-3-p}.                           \tag{6.6}
\]

Putting `j=m-3-p` and summing,

\[
\begin{aligned}
 |\operatorname {im}\psi|
 &=\sum_{j=0}^{m-3}{N-2j\over N}{N\choose j}\\
 &=\sum_{j=0}^{m-3}left({N-1\choose j}-{N-1\choose j-1}\right)\\
 &={2m-4\choose m-3}.
\end{aligned}                                                  \tag{6.7}
\]

Pascal's identity gives the second equality in (6.3).  \(\square\)

Because there are only `c` short providers,

\[
 D_{\rm short}\le c,qquad
 D_{\rm long}=E-A_C-D_{\rm short}\ge K-c.                    \tag{6.8}
\]

Combining (5.3), `p<=c`, and (6.8) proves

\[
 \kappa_a'+\kappa_z'
 \le 3c-K-I+2.                                                \tag{6.9}
\]

### Theorem 6.2 (standard conjugate-plus-short-bank ceiling)

For every `m>=10`, the right side of (6.9) is negative.  Hence no standard
GK flexible SCD forest, no choice of at most all `c` first-stage short
rethreads, and no union of neutral `F(a,z)`--`F(z,a)` four-shore components
can make both distinguished connector currents nonnegative.

#### Proof

Direct algebra gives

\[
 K+I-3c
 =c\,{m^3-8m^2-21m+48\over2(2m-3)(m+1)}.                    \tag{6.10}
\]

At `m=10` this integer equals `494`.  The cubic numerator is positive and
strictly increasing for `m>=10`.  Also

\[
 {c_{m+1}/((2m-1)(m+2))\over c_m/((2m-3)(m+1))}
 ={2(2m-3)\over m+2}>1,                                     \tag{6.11}
\]

where `c_m=Cat_{m-1}`.  Thus the right side of (6.10) increases from
`494`, in particular it exceeds `2`; (6.9) is negative.  The current sum
is invariant under Theorem 2.1, proving the claim.  \(\square\)

## 7. Exact C6/C8 current classification

For any directed packet let `tau_q` denote used-lower-colour incidence at
`q` and let `eta_q` denote used-head-owner incidence at `q`.  A literal
switch has

\[
                         \Delta\kappa_q=\Delta\tau_q-\Delta\eta_q.       \tag{7.1}
\]

Consequently every closed four-resource C6 or C8 relation, which preserves
the lower and head shores separately, has

\[
                         \Delta\kappa_q=0\quad\hbox{for every }q.        \tag{7.2}
\]

The standard Boolean C6 forward gain replaces an off pair by an on triple.
Its resource difference is one legal ordered atom

\[
                         e=(L,U,T,H),\qquad H=L+y.             \tag{7.3}
\]

It therefore has

\[
 \Delta\kappa_q={\bf1}_{q\in L}-{\bf1}_{q\in H}
                =-{\bf1}_{q=y}.                              \tag{7.4}
\]

Forward gain never supplies positive current in any coordinate.  The
reverse switch supplies `+1` at `y` but deletes one complete service atom.
Any hypothetical one-atom-surplus C8 has the same signature.  The audited
four-block C8 relations are closed and hence satisfy (7.2); no audited
physical C8 gain mode has a positive-total-current boundary.

Thus a genuine gain-two actuator cannot be an internal closed C6/C8
circuit.  It must be an open/dummy/basis-changing packet or an external
provider rethread with

\[
                         \Delta\tau_z-\Delta\eta_z\ge2,        \tag{7.5}
\]

after every displaced target/provider row is restored.  Raw circuit count
or gross released-head count is not evidence for (7.5).

## 8. Audit, scope, and the exact live gate

The independent finite component census is

* `scratch/analyze_scd_swapped_colored_components_20260801.cpp`, SHA-256
  `7ee3dd574974cf40ee9d90c0e33f487bf774e88c11184d8e24bfe757c9dd3200`;
* `scratch/scd_swapped_colored_components_m4_m9_20260801.audit.json`,
  SHA-256
  `f42bdb5f582d103e6e5e18c24845a198a4d718e29753da3adc9bb1a1d1817616`.

The independent lightweight arithmetic/GK-image/sign replay is

* `scratch/audit_k_scd_conjugate_hybrid_current_20260801.py`, SHA-256
  `7b028a7c0ddd8c4f81485ffbcf3ac8f57f0ee66750a84bb394fe39fe29ef3969`;
* `scratch/k_scd_conjugate_hybrid_current_20260801.audit.json`, SHA-256
  `8e4ee50cb625a5296b3feeea3b15fc508a487a6360d13c78b26f9a21c5c8a3c9`.

It independently reconstructs the GK image sizes
`1,4,15,56,210,792,3003` for `m=3,...,9`, verifies the first strict
all-short-bank ceiling at `m=10`, and checks 140 legal one-atom forward
boundaries, all with the sign (7.4).

It verifies (0.3) on every augmented component of the authenticated
`m=4,...,9` fixtures.  Their base current pairs are

\[
 (2,-3),(1,-13),(6,-47),(1,-164),(-68,-571),(-467,-2001),    \tag{8.1}
\]

all with negative sum.  This finite table is not needed for Theorem 6.2.

The first-stage finite replay is

* `scratch/threadD_scd_paired_palette_hamilton_20260801/m4.firststage.path.audit.json`,
  SHA-256
  `1ef28fe274294384435c5ee829b3116aea9aaed380a8a0913b7c2a9a151ddb2d`;
* `scratch/verify_threadD_scd_firststage_hamilton_certificate_20260801.py`,
  SHA-256
  `adb179cc179cd72e3fd5c96d4af42e88a869517fac195b6a70fb36c9cc27f205`.

The exact surviving theorem target is now sharply separated.

1. Among dimensions `m>=6`, only `m=6,7,8,9` remain outside the universal
   current ceiling, and every one still needs the component
   subset, cycle, and full rooted connector rows.  (The displayed saved
   fixtures already fail total current after all `c` possible rethreads
   for `m=7,8,9`; this does not quantify over all phase forests.)
2. For an all-dimensional construction, the new ingredient must change the
   total current: a nonstandard base with nonnegative `a+z` sum, a third
   parent, a changed rooted owner basis/closure, or a genuinely open
   positive-current packet.
3. The positive two-stratum endpoint-hole cocycle proves that an abstract
   degree fibre exists.  It does **not** prove that this fibre lies in the
   four-shore component column set, satisfies (3.1), or admits the final
   rooted connector tree.

Residence, deeper shadows, and common-cap compilation are downstream and
are not claimed here.
