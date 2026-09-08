# Audit R: mixed coatom screens have zero owner defect; the remaining gate is joint menu--U5 regeneration

Date: 2026-08-01  
Status: independently audited local theorem and exact global reduction  
Scope: the additive-constant regenerative-packet route; this is not by itself a proof of `nu(k)<=B(k)+O(1)`

## 0. Verdict

The four repeated owners in the all-lower-screen coatom tensor are not an
exported sidecar.  They are removed, without adding a coordinate or a word
cell, by using the opposite Johnson-diamond screen at zero-based transitions

\[
                              E=\{1,3,5,7\}.                 \tag{0.1}
\]

For every `d>=1` and `r>=d+4`, the resulting two phases are simple
rank-`r` Johnson paths of length `12d+35`, have the same *distinct* owner
set, preserve both adjacent palettes, preserve pointwise prefix and suffix
ORs, preserve the complete distinct internal interval-OR support, and have
minimum internal positive run `d+1` with the same clipped boundary state.

Thus the local rows U1--U4 are closed with **zero owner sidecar**.  The
remaining exact global rows are:

1. embedding a compatible menu choice for every exposed Pascal task;
2. choosing those menus together with one common compiler matching (U5);
3. regenerating the same bounded interface at the next lift.

In particular, no future ledger should charge `+4` owner obligations to
this packet.

## 1. Exact construction

Write the active row as

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.
```

Let `n=d+2`, let

\[
 F=\{f_0,\ldots,f_{n-1}\},\qquad C_i=F-\{f_i\},\qquad
 F^\circ=F-\{f_0,f_{n-1}\},                              \tag{1.1}
\]

and take a disjoint core `K` of size `r-d-4`.  Replace each active triple
`V` by

\[
 B(V)=\bigl(K\cup V\cup C_0,\ldots,K\cup V\cup C_{n-1}\bigr). \tag{1.2}
\]

For a transition from `V` to `W`, put `I=V cap W`.  The terminal cell of
`B(V)` and initial cell of `B(W)` have the two useful common neighbours

\[
 L(V,W)=K\cup I\cup F,
 \qquad
 U(V,W)=K\cup(V\cup W)\cup F^\circ.                        \tag{1.3}
\]

Use `U` at (0.1), and `L` at the other seven transitions.

### Lemma 1.1 (literal Johnson bridge)

Both cells in (1.3) have rank `r` and are Johnson adjacent to both boundary
block cells.

#### Proof

Write `V=I+x`, `W=I+y`.  Relative to the last cell of `B(V)`, the lower
screen exchanges `x` for `f_(n-1)`, while the upper screen exchanges `f_0`
for `y`.  Relative to the first cell of `B(W)`, the lower screen exchanges
`f_0` for `y`, while the upper screen exchanges `x` for `f_(n-1)`.  Each is
one deletion and one insertion.  Their ranks are respectively
`|K|+2+n=r` and `|K|+4+n-2=r`.  \(\square\)

## 2. Exact zero-defect theorem

### Theorem 2.1

The two expanded phases defined above satisfy, for every `d>=1` and
`r>=d+4`:

1. they are simple rank-`r` Johnson paths with common endpoints and length
   `12d+35`;
2. all owners are distinct and the two owner sets agree;
3. their adjacent-intersection sets are equal and rainbow, and their
   adjacent-union multisets agree;
4. their prefix-OR and suffix-OR signatures agree pointwise;
5. their complete distinct internal interval-OR supports agree and have size
   `12d+68`; and
6. every internal positive coordinate run has length at least `d+1`, with
   equal clipped boundary states.

#### Proof

At the four selected positions, the active edges in the two phases are the
same four undirected edges, merely permuted or reversed:

\[
 \{Ib\!-!bc,\ Cd\!-!Ic,\ Ibc\!-!Ica,\ Ia\!-!ca\}.       \tag{2.1}
\]

Their intersections are one occurrence each of the four formerly repeated
colours `eb,ec,c-infinity,ea`; replacing them removes precisely one member
of every repeated pair.  The four selected active unions form in both
phases the distinct set

\[
 \{\infty ebc,\ \infty ecd,\ \infty abc,\ \infty eac\}.   \tag{2.2}
\]

The seven retained lower colours are also common and pairwise distinct.
Block, lower-screen and upper-screen owners omit respectively one, zero and
two filler coordinates, so different types cannot collide.  Within a type,
the active label and omitted filler determine the owner.  Hence all
`12n+11` owners are distinct, and their two sets agree.  Lemma 1.1 gives
literal Johnson topology.  The same labelled edge data give equality of the
immediate palettes.

At a lower screen, a prefix remains at the active prefix through the left
endpoint; at an upper screen it advances through the right endpoint.  The
suffix statement is the reverse.  The active words have the same pointwise
prefix and suffix OR signatures, so the expanded signatures agree.

For internal OR support, first separate the seven singleton lower screens.
Their values are `K union I union F` for the common seven-colour set of
retained intersections.  A singleton lower screen must be treated
separately: its rank-two active part is not necessarily the union of an
active-vertex interval.  Any interval containing a lower screen and a block
cell has full filler `F` and contracts to a contiguous active interval.

After removing lower screens, the only nontrivial pieces are
`B(V),U(V,W),B(W)`.  The complete support is

\[
\begin{aligned}
\mathcal I={}&\{K\cup V\cup C_i\}\\
 &\cup\{K\cup I\cup F:I\text{ is one of the seven retained colours}\}\\
 &\cup\{K\cup A\cup E:A\text{ is one of (2.2)},\
                 E\in\{F^\circ,C_0,C_{n-1}\}\}\\
 &\cup\{K\cup F\cup Z:Z\text{ is a consecutive active OR}\}.
                                                               \tag{2.3}
\end{aligned}
\]

Indeed, a non-full-filler interval is exactly a singleton block, a singleton
upper screen, or an upper screen together with one adjacent boundary
coatom.  Every other nonsingleton interval contains two distinct coatoms or
a full lower screen.  The four lines in (2.3) have sizes

\[
                   12n,\quad7,\quad12,\quad25,                 \tag{2.4}
\]

and are disjoint by filler profile, giving `12n+44=12d+68`.

Active coordinates occur through a full length-`n` block.  Middle fillers
retain positive runs of length at least `n`; only `f_0,f_(n-1)` can also be
absent at an upper screen, shortening the minimum to
`n-1=d+1`.  The first and last blocks and the positional screen schedule are
common, so the clipped boundary states agree.  \(\square\)

### Scope of Theorem 2.1

The theorem asserts equality of **distinct OR support**.  It does not assert
equality of interval multiplicities or of arbitrary deeper intersection
decks.  Those stronger statements are false in general and are not used by
compressed-deck replacement.

## 3. Exact global menu--compiler reduction

The zero-owner result does not make compiler U5 automatic.  The correct
quantifier is joint across all selected packets.

Let `T` be the exposed task set.  For each `t in T`, let `M_t` be its menu of
literal embeddings of Theorem 2.1.  A selection

\[
                       s\in\prod_{t\in T}M_t                 \tag{3.1}
\]

is called *physical* when the chosen packets obey the required topology,
owner, colour and residence privacy constraints.  For a physical `s`, let
`H_(phi,rho)^s=(L,C;E_(phi,rho)^s)` be its literal trace-guarded
target--cell compiler graph in joint phase vector `phi` and reachable
frontier `rho`.  Define the edgewise common graph

\[
 H^\cap(s)=\left(L,C;
       \bigcap_{\phi,\rho}E_{\phi,\rho}^s\right),              \tag{3.2}
\]

where the intersection is over every allowed joint phase vector and every
reachable frontier.  This graph, rather than a scalar cell count, is the
exact common-cap object.

### Theorem 3.1 (joint menu--U5 criterion)

There is a physical menu selection and one literal compiler matching common
to every selected packet phase and every reachable frontier if and only if
there exists a physical `s` such that

\[
 \boxed{
 \delta\bigl(H^\cap(s)\bigr)=
   \max_{X\subseteq L}
      \bigl(|X|-|N_{H^\cap(s)}(X)|\bigr)=0.}                  \tag{3.3}
\]

#### Proof

For fixed `s`, a literal common compiler is exactly a matching saturating
`L` in the edgewise intersection (3.2).  Hall's theorem is exactly (3.3).
Taking the existential quantifier over physical selections proves the
statement.  \(\square\)

The fixed-unused-cell U5 interface is the following important specialization.
Suppose there is a reference graph `H=(L,C;E)`, a worst-frontier cell ideal
`D_0`, and a joint macro cell set `D_mac(s)` such that

\[
 E\bigl(H^\cap(s)\bigr)
   =\{(x,c)\in E:c\notin D_0\cup D_{\rm mac}(s)\}.             \tag{3.4}
\]

Then (3.3) is exactly

\[
 \delta_H(D_0\cup D_{\rm mac}(s))=
   \max_{X\subseteq L}
    \bigl(|X|-|N_H(X)\setminus(D_0\cup D_{\rm mac}(s))|\bigr)=0. \tag{3.5}
\]

If the right side of (3.4) is only a subgraph of `H^cap(s)`, (3.5) remains
sufficient but is no longer necessary.  In particular, deleting an entire
cell merely because one unrelated incidence changes can discard a usable
common incidence.

Under the exact cell factorization (3.4), define the residual Hall slack and
selected-menu load on a shore `X` by

\[
\begin{aligned}
 b_H(X)&=|N_H(X)\setminus D_0|-|X|,\\
 \ell_s(X)&=\left|N_H(X)\cap
        \left(D_{\rm mac}(s)\setminus D_0\right)\right|.
                                                               \tag{3.6}
\end{aligned}
\]

Then (3.5) is exactly the simultaneous cut system

\[
                         \ell_s(X)\le b_H(X)
                         \quad(X\subseteq L).                  \tag{3.7}
\]

This is the weakest cell-factorized common-cap condition.  Packet-local sets
`D_e` may replace `D_mac(s)` by `union_t D_(s(t))` exactly only when that
factorization is certified for every joint phase vector.  Mere containment
gives a conservative sufficient test.  Under an exact factorization,
overlaps among the `D_e` are counted only once, as required physically;
replacing the union load by a sum is sufficient but can be strictly stronger.

### Proposition 3.2 (individual U5 does not compose)

Separate per-packet cell-factorized Hall tests do not imply (3.5), even in
the smallest complete compiler graph.

#### Proof

Let `L={a}`, `C={1,2}` and `H=K_(1,2)`, with empty frontier ideal.  Two
packets have a certified factorized joint set `D_mac=D_1 union D_2`, where
`D_1={1}` and `D_2={2}`.  Deleting
either set separately leaves a matching saturating `L`, so both individual
U5 tests pass.  Deleting their union leaves no cell and the shore `{a}` has
deficiency one.  Thus only the union-cut condition (3.5), or an equivalent
joint packet/compiler selection, is sound.  \(\square\)

This criterion is stronger than checking every packet separately: a
factorized union can create a global Hall cut.  It is also stronger than
assigning one nominal unused cell per packet unless a separate theorem proves
that the joint noninvariance set is exactly covered by those deletion tokens.
In particular, equal owner sets and equal OR support do not imply that
`D_mac(s)` consists only of screen cells; short compiler incidences crossing
one or several rethreads may change throughout the macros.

### Corollary 3.3 (bounded exported debt, conditional)

If a physical selection `s` has `delta(H^cap(s))<=c` for an absolute
constant `c`, and a literal terminal module repairs the corresponding `c`
lower obligations, then the macro family exports `O(1)` compiler debt and
zero owner debt.  To yield an additive constant uniformly in dimension, the
regenerative lift must recreate the same bounded interface rather than
accumulate this debt.

## 4. Exact remaining theorem

After the mixed-screen repair, the bounded regenerative route reduces to the
following three-part statement.

> For every reachable task state, choose one embedding from each task menu
> so that the selection is physical and (3.3) holds; after executing the
> packets and the common compiler, the next Pascal lift exposes a state of
> the same bounded type.

A useful sufficient theorem would provide all three quantitative clauses:

1. each task retains an `Omega(m^2)` menu after `O(md)` local exclusions;
2. the chosen family has a trace-guarded common compiler with zero or
   absolute Hall deficiency under (3.3); and
3. the regenerated task/interface count is bounded by the same absolute
   constants.

None of these clauses follows merely from the local tensor.  This is the
precise proved/conditional boundary: the owner-repeat gate is closed, while
task availability, common-cap U5 and regeneration remain open.

## 5. Independent audit ledger

The local audit was replayed after correcting the singleton-lower-screen
case in the proof of internal OR support:

```text
scratch/audit_coatom_screen_tensor_resident_eco_packet_20260801.py
  status PASS; 96 records; payload
  17bacfee6bb6e3e402ca21f14581f57d743055bcf68cbbb05fdbb363527c144a

scratch/audit_coatom_screen_tensor_compiler_20260801.py
  status PASS_ZERO_DEFECT_COATOM_SCREEN_TENSOR; 36 records;
  perfect patterns 0110,1011,1100; payload
  9d119687e6be9affee30357fc3dc6a96f7c489b1c48edcacadf863b3de222
```

The audits support, but do not replace, the symbolic all-`d` proof.  They do
not construct the Pascal menus, compiler graph, or regenerative transition.
