# Adjacent coatom twists close the full signed counter lattice, but not the compiler basis

Date: 2026-08-01  
Lane: A, additive-constant coatom packet / compiler linkage  
Status: unconditional integral catalogue theorem, exact one-block actuator
obstruction, and exact fixed-common-flat-compiler no-go.  Prepared physical
planting, nonnegative serial reachability, terminal U5, and regeneration remain
open.  No `B(k)+O(1)` conclusion is claimed.

## 0. Outcome

The reflection defect in the common-order coatom catalogue is not a genuine
linear obstruction.  In the endpoint-planted catalogue, subtracting a
boundary-role conjugate of one adjacent twist isolates one primitive Johnson
square at one prescribed depth.  Consequently, in the stable template range,
the enlarged signed catalogue generates exactly the product of the depthwise
point-degree kernels:

\[
 \boxed{
 \Lambda_d=
 \bigoplus_{q=2}^{d}
 \ker_{\mathbb Z}\!\left(
   \partial_1:\mathbb Z^{\binom{\Omega}{r-q}}
       \longrightarrow\mathbb Z^\Omega\right).}       \tag{0.1}
\]

Thus there is no remaining rational, integral-index, parity, or other linear
all-depth occurrence-counter invariant beyond the separately conserved point
degrees.  Sections 1--3 give an independent structural description of the
pair-current quotient and its octahedral kernel in the canonical unplanted
fibre; they are not a second proof inside the endpoint-planted catalogue.
The endpoint-planted equality uses the sharper boundary-role commutator.

Two physical qualifications are exact and load-bearing.

1. A breaker preserves its label-attached coatom order in both phases; it
   transports a prepared twist but does not create one.  The internal q1
   palette of one fixed active block recovers its omission-order Hamilton
   path, so no nontrivial one-block q1-exact order actuator exists.
2. In the raw flat phase-common individual-incidence graph, an adjacent twist
   gains no common incidence and deletes the complete common neighbourhood of
   exactly `2d` interval columns.  Hence a matching restricted to that fixed
   raw basis can never improve under the twist.  Compiler improvement must
   change cap state or use an alternating path to a previously unused physical
   cell; fixed-address Pluecker circuits alone only route alternating cycles.

The sharp remaining local theorem is therefore a **prepared, q1-compensated
multi-block order actuator plus a basis-changing return bank**, not another
counter-lattice lemma.

## 1. Incidence lattices

Let `Omega` be a `k`-element coordinate set.  For `s>=2`, put

\[
 C_s=\mathbb Z^{\binom{\Omega}{s}},\qquad
 \partial_{s,j}e_X=\sum_{Y\in\binom Xj}e_Y.          \tag{1.1}
\]

Define

\[
 L_s=\ker\partial_{s,1},\qquad
 T_s=\ker\partial_{s,2},\qquad
 K_2=\ker\partial_{2,1}.                             \tag{1.2}
\]

The pair-current map on a signed rank-`s` occurrence vector is
`D_s=partial_(s,2)`.  Since

\[
 \partial_{2,1}\partial_{s,2}=(s-1)\partial_{s,1},  \tag{1.3}
\]

it maps `L_s` into `K_2`.

### Lemma 1.1 (exact pair-current quotient)

If `3<=s<=k-2`, then

\[
 0\longrightarrow T_s\longrightarrow L_s
   \mathop{\longrightarrow}^{D_s}K_2
   \longrightarrow0                                             \tag{1.4}
\]

is an exact sequence of integer lattices.

#### Proof

If `D_s z=0`, then (1.3) and torsion-freeness give
`partial_(s,1)z=0`, so the kernel in (1.4) is exactly `T_s`.

The lattice `K_2` is generated integrally by pair squares

\[
 [ab]+[xy]-[ax]-[by].                                \tag{1.5}
\]

This is Theorem 3.1 of
`MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`
specialized to rank two; its inductive proof is integral, not only rational.

Choose an `(s-2)`-set `H` disjoint from `a,b,x,y`.  The Johnson square

\[
 e_{Hab}+e_{Hxy}-e_{Hax}-e_{Hby}                    \tag{1.6}
\]

has zero point degrees and pair current (1.5): every pair meeting `H`, and
every pair contained in `H`, cancels.  Thus `D_s` is onto over the integers.
\(\square\)

At `s=2`, `T_2=0` and `D_2` is the identity.  The stable coatom range below
has `s>=4`, so no boundary exception is used.

## 2. The integral pair-balanced kernel is octahedral

For pairwise disjoint sets `H,{a_i,b_i}` with `|H|=s-3`, define the
three-dimensional octahedral trade

\[
 \mathcal O(H;(a_1,b_1),(a_2,b_2),(a_3,b_3))
 =\sum_{\epsilon\in\{0,1\}^3}(-1)^{|\epsilon|}
 e_{H\cup\{x_{1,\epsilon_1},x_{2,\epsilon_2},x_{3,\epsilon_3}\}},
                                                               \tag{2.1}
\]

where `x_(i,0)=a_i` and `x_(i,1)=b_i`.

### Theorem 2.1 (integral octahedral generation)

For `3<=s<=k-2`, the lattice `T_s` is generated over `Z` by the trades
(2.1).

#### Proof

Every (2.1) has zero pair current.  Indeed, requiring a fixed pair fixes at
most two of the three binary choices, and summing over a remaining free
choice cancels the signs.

We prove generation by induction on `k`.  The base is `k=s+2`.  Index an
`s`-set coefficient by its omitted pair and write it as `y_(ij)`.  Put

\[
 T=\sum_{i<j}y_{ij},\qquad r_i=\sum_{j\ne i}y_{ij}.  \tag{2.2}
\]

The pair equation for `{i,j}` says that the sum over omitted pairs disjoint
from `{i,j}` is zero, hence

\[
 y_{ij}=r_i+r_j-T.                                   \tag{2.3}
\]

Summing (2.3) over `j ne i` and using
`sum_i r_i=2T` gives `(k-3)(r_i-T)=0`, hence `r_i=T` because
`k=s+2>=5`.  Summing the `r_i` then gives both `kT` and `2T`, so
`(k-2)T=0`.  Therefore `T=0`, all `r_i=0`, and all `y_(ij)=0`.
The base kernel is zero.

Now let `k>=s+3`, choose `z in Omega`, and split `w in T_s` according to
whether its sets contain `z`.  Identify the containing coefficients with
a vector `y` on the `(s-1)`-sets of `Omega-{z}`.  The pair equations
`{z,x}` say precisely that `partial_(s-1,1)y=0`.  By the integral
uniform-degree theorem, `y` is an integer sum of Johnson squares with a
common `(s-3)`-core and two exchanged pairs.

For each such square choose a fresh coordinate `c` outside its core, four
external labels, and `z`; this is possible because `k>=s+3`.  Adding the
third pair `(z,c)` turns that square into an octahedron (2.1) whose
`z`-containing slice is the prescribed square.  Subtract these octahedra to
kill every coefficient containing `z`.  The remainder belongs to `T_s` on
`Omega-{z}` and is generated by induction.  \(\square\)

Equivalently, for a common `(s-3)`-core `R`, the generators are

\[
 Q_{R\cup\{u\}}(a,b;x,y)-Q_{R\cup\{v\}}(a,b;x,y),   \tag{2.4}
\]

where

\[
 Q_R(a,b;x,y)=e_{Rax}+e_{Rby}-e_{Ray}-e_{Rbx}.       \tag{2.5}
\]

## 3. Independent canonical-fibre octahedral factorization

This section concerns the **unplanted canonical common-order flag action**,
not the eight-term endpoint-planted baseline used in Section 4.  Use the
notation

\[
 \pi=(H,x,y,J),\qquad \pi'=(H,y,x,J),                \tag{3.1}
\]

where `|H|=t-1` and `|J|=d-t-1`.  Subtract the two packet actions.  The
only affected flag layers are `t` and `d-t`; in physical depths they are

\[
 q_-=t+1,qquad q_+=d+1-t.                           \tag{3.2}
\]

The corresponding actions are, with one consistent orientation,

\[
 Q_{G\cup J}(a,b;x,y)\quad(q_-),\qquad
 Q_{G\cup H}(a,b;x,y)\quad(q_+).                    \tag{3.3}
\]

If `d=2t`, both summands occur in the same central depth.

### Lemma 3.1 (formal canonical-fibre pure-depth cube)

Assume `d>=3`, `r>=d+4`, and `k>=r+5`.  For every `2<=q<=d`, every
octahedron (2.4) of rank `r-q` is an integer combination of four formal
unplanted common-order packet actions which is zero at every depth other
than `q`.  This is a signed canonical-fibre identity; it neither belongs to
the endpoint-planted catalogue merely by notation nor asserts that the four
old phases occur in one carrier or have owner-disjoint simultaneous lifts.

#### Proof

For `q=t+1`, keep `G,H,x,y,a,b` fixed and compare (3.1) with

\[
 J=J_0\cup\{u\}\quad\hbox{and}\quad J=J_0\cup\{v\}.
\]

Subtract the two commutators.  Their `q_+` companions in (3.3) agree and
cancel, while their `q` difference is (2.4).  For `q=d+1-t`, keep `G,J`
fixed and vary `H=H_0+u,H_0+v`; now the `q_-` companions cancel.  In the
central case, fix one of `H,J` and vary the other; the fixed summand in the
single central row cancels.

The endpoint `q=d` has `t=1` and no variable `H`.  Write

\[
 G_u=R\cup\{u\},\quad J_u=J_0\cup\{v\},\qquad
 G_v=R\cup\{v\},\quad J_v=J_0\cup\{u\}.             \tag{3.4}
\]

Then `G_u union J_u=G_v union J_v`, so the q2 companions are identical,
whereas the qd difference is the desired octahedron.  When the fixed core
`K` is empty, the variable non-endpoint member of `G` can be the active
role `c`; no extra core coordinate is required.

The two filler frames together may use one more coordinate than one packet;
the hypothesis `k>=r+5` supplies it.  The sharper reciprocal reuse of an
action-invisible active role is available in the canonical fixed-action
menu, but it is intentionally not used here because the endpoint-planted
baseline does not inherit that menu.

Finally, arbitrary relabelling partitions the `(r-q-3)`-core of any desired
octahedron into `G` and the required part of `H` or `J`.  The stated rank
conditions make every part nonnegative.  \(\square\)

This factorization is an independent explanation of the pair-current-zero
kernel.  The sharp endpoint-planted full-span proof below instead uses a
boundary-role commutator and needs only `k>=r+4`.

## 4. Full integral all-depth span

Let `Lambda_d` be the integer span of all relabelled and reversed actions
of

1. the untwisted endpoint-planted coatom packets under every admissible
   injective assignment of their labelled roles; and
2. the same planted packets with one adjacent omission transposition in the
   label-attached `Ica` block, using the authoritative schedule
   `E={0,2,4,6,8,10}`.

### Theorem 4.1 (full coupled signed counter lattice)

If

\[
 d>=2,\qquad r>=d+4,\qquad k>=r+4,                  \tag{4.1}
\]

then (0.1) holds.  In particular

\[
 \operatorname{rank}\Lambda_d
   =\sum_{q=2}^{d}\left(\binom{k}{r-q}-k\right).     \tag{4.2}
\]

#### Proof

Let `Delta^0` be the action of the untwisted endpoint-planted packet,
`Delta^s` the action with omissions `f_s,f_(s+1)` transposed in `Ica`, and
put `C_s=Delta^s-Delta^0`.  The exact boundary formula for
`1<=s<=floor(d/2)` uses

\[
\begin{aligned}
H_s^+&=K\cup\{\infty,c,f_{s+2},\ldots,f_d\},\\
H_s^-&=K\cup\{\infty,c,f_1,\ldots,f_{s-1}\},\\
H_{s,q}&=K\cup\{\infty,f_{s-(d+1-q)},\ldots,f_{s-1}\}
             \quad(q>d+1-s),
\end{aligned}                                                   \tag{4.3}
\]

with empty filler ranges omitted, and has the following role support:

\[
\begin{array}{c|c}
q&(C_s)_q\\ \hline
s+1&Q_{H_s^+}(a,p;f_s,f_{s+1}),\\
d+1-s&Q_{H_s^-}(a,f_0;f_s,f_{s+1}),\\
q>d+1-s&Q_{H_{s,q}}(a,c;f_s,f_{s+1}).
\end{array}                                                   \tag{4.4}
\]

All other rows vanish; when `2s=d`, the first two squares occur in the
same central row and add.  Crucially, the active role `b` occurs in no row,
`p` occurs only in the first row, and `f_0` only in the second.

Let `tau_p` exchange the coordinates assigned to the packet roles `p,b`,
fixing every other role.  Since both labelled packets are catalogue
columns,

\[
 C_s-\tau_pC_s
  =\mathbf e_{s+1}\otimes
      Q_{H_s^+}(b,p;f_s,f_{s+1}).                    \tag{4.5}
\]

Likewise, exchanging `f_0,b` gives

\[
 C_s-\tau_0C_s
  =\mathbf e_{d+1-s}\otimes
      Q_{H_s^-}(b,f_0;f_s,f_{s+1}).                 \tag{4.6}
\]

The identities remain valid in the central case because the other central
summand is fixed by the relevant role swap.  They also handle `d=2,s=1`:
the q2 correction is the sum of the `p`- and `f_0`-squares, and (4.5)
isolates the former.

As `s` runs from `1` to `floor(d/2)`, (4.5)--(4.6) cover every depth
`2,...,d`.  Each isolated direction is a **primitive** Johnson square, not
twice one.  Arbitrary admissible relabelling realizes every square at that
depth.  For example, at `q=s+1` the square core has size `r-s-3`; the packet
needs `s+7` labels outside it, while

\[
 k-(r-s-3)=k-r+s+3\ge s+7.                          \tag{4.7}
\]

The reflected row has the same count.  The integral uniform-degree theorem
therefore shows that `Lambda_d` contains the complete point-degree kernel at
each depth separately.

Conversely, the endpoint-planted baseline and every adjacent-twist
derivative decompose into Johnson squares at each depth, so every catalogue
action is point balanced.  This gives the reverse inclusion in (0.1) and
proves equality over `Z`.

In the stable range, each point-incidence map has rational rank `k`, giving
(4.2).  \(\square\)

This theorem is an unlabelled signed occurrence-**counter** theorem.  The
four columns in (4.5) or (4.6) generally have different endpoints and owner
slots.  It does not say that they are simultaneously present, owner-disjoint,
or traversable through nonnegative carrier states.

## 5. A twist transports its order; it does not create it

Let one fixed active block have coatom omission order
`pi=(pi_0,...,pi_(d+1))`.  Its internal q1 colours are

\[
 K\cup V\cup\bigl(F-\{\pi_i,\pi_{i+1}\}\bigr)
 \qquad(0\le i\le d).                               \tag{5.1}
\]

### Proposition 5.1 (one-block order-actuator no-go)

With the active label, filler set, and first and last omissions fixed, a
replacement of one isolated block preserves its internal q1 colour multiset
if and only if it preserves its omission order.

#### Proof

Removing the common `K union V` from (5.1) gives the coatoms
`F-{pi_i,pi_(i+1)}`.  Complementing each inside the known filler set `F`
recovers exactly the unordered edge set

\[
 \{\{\pi_i,\pi_{i+1}\}:0\le i\le d\}               \tag{5.2}
\]

of the Hamilton path through the filler omissions.  This edge set determines
the order up to reversal.  The fixed first and last omissions select one of
the two orientations.  \(\square\)

For the adjacent change `...,u,x,y,v,... -> ...,u,y,x,v,...`, the exact
one-phase q1 defect is

\[
 \begin{aligned}
 &[KV(F-\{u,y\})]+[KV(F-\{x,v\})]\\
 &\quad-[KV(F-\{u,x\})]-[KV(F-\{y,v\})].             \tag{5.3}
 \end{aligned}
\]

The middle `{x,y}` edge cancels.  Because the active and filler alphabets are
disjoint, a block with a different active triple cannot cancel these literal
colours.  Hence a physical order actuator needs
a second occurrence of the same active label, an explicitly matching screen
bank, or a larger multi-block compensation circuit.

The breaker theorem itself is not contradicted: its source and output both
use the same twisted label-attached `Ica` order.  It is a safe edge inside a
prepared twisted fibre, not an edge from the canonical fibre into it.

## 6. Exact fixed-common-flat compiler antitonicity

Let `c(t,h)=[t,t+h)` be a flat maximal-envelope compiler column, put

\[
 u=6d+17,qquad b_X=u+1,qquad b_Y=u-d-2,             \tag{6.1}
\]

and, for `1<=s<d`, swap omissions `f_s,f_(s+1)` in the label-attached
`Ica` block.  For one phase whose block starts at `b`, only the following
`2d+2` columns can change:

\[
\begin{array}{ll}
h=1:&c(b+s-1,1),c(b+s,1),c(b+d+s+1,1),c(b+d+s+2,1),\\
2\le h\le d:&c(b+s,h),c(b+d+s+2-h,h).
\end{array}                                                   \tag{6.2}
\]

The two phase disturbance sets have one shared fringe and therefore
`4d+3` columns in their union.

Let `H_0^raw=H_X^0 \cap H_Y^0` be the intersection of the two raw flat
**individual-incidence** graphs for the untwisted phases, on the complete
bank of targets having some nonempty individual incidence, and let
`H_s^raw` be the corresponding twisted intersection on the same shores.
This is not yet a complete common-cap state or a co-selectability graph.
Define

\[
\begin{aligned}
 Z_s={}&\{c(u+s+1,h):1\le h\le d-s\}\\
 &\cup\{c(u+s-d-2,h):1\le h\le d-s-1\}\\
 &\cup\{c(u+s-h,h):1\le h\le s\}\\
 &\cup\{c(u+d+s+3-h,h):1\le h\le s+1\}.
                                                               \tag{6.3}
\end{aligned}
\]

These families are disjoint and `|Z_s|=2d`.

### Theorem 6.1 (fixed-common-flat compiler no-go)

For every column `c`,

\[
 \Gamma_{H_s^{\rm raw}}(c)=
 \begin{cases}
  \varnothing,&c\in Z_s,\\
  \Gamma_{H_0^{\rm raw}}(c),&c\notin Z_s.
 \end{cases}                                                   \tag{6.4}
\]

Consequently

\[
 H_s^{\rm raw}\subsetneq H_0^{\rm raw},\qquad
 \nu(H_s^{\rm raw})\le\nu(H_0^{\rm raw}).          \tag{6.5}
\]

The inclusion in (6.5) remains valid after restricting the target bank;
strictness is asserted only for the complete nonempty raw bank above,
because every old neighbourhood on `Z_s` is then nonempty.

#### Proof

The transposition changes only the two maximal erosions ending at the first
swapped position and beginning after the second.  A column containing either
erosion strictly internally has the same allowed/mandatory/hit signature;
the surviving boundary placements are exactly (6.2).

At the core placements, the two phase neighbourhoods are transposed by
`f_s <-> f_(s+1)`.  The exact phase-intersection case split has four rows:

\[
\begin{array}{c|c|c}
\text{column class}&\text{number}&\text{new common neighbourhood}\\ \hline
Z_s&2d&\varnothing\\
\text{shared fringe}&1&\text{old neighbourhood}\\
\text{other disturbed columns}&2d+2&\text{old neighbourhood}\\
\text{outside (6.2)}&\text{all remaining}&\text{old neighbourhood}.
\end{array}                                                   \tag{6.6}
\]

For `c in Z_s`, one phase mandates `f_s` while the other forbids it, and
conversely for `f_(s+1)`, so the common neighbourhood is empty.  At the
shared fringe the two one-sided relaxations point in opposite directions
and their conjunction is exactly the old predicate.  At each of the other
disturbed columns, either both phase intersections are already empty or the
unchanged other-phase allowed/mandatory predicate dominates the
transposition; direct substitution in the two signatures gives the old
intersection.  Outside (6.2), both individual predicates are unchanged.
This proves (6.4), and (6.5) follows.  \(\square\)

The theorem is deliberately scoped to the raw flat individual-incidence
intersection.  A fixed complete cap state and its co-selectability rows can
only delete further edges from that raw graph, but changing the cap state can
select a different surviving subgraph.  The `2d+2` one-phase disturbance
count is a column-footprint count, not the matching-loss parameter `ell` in
Section 7.  A terminal compiler may change cap state or physical cell basis;
that is the surviving route.

## 7. Exact basis-changing linkage law

Fix an old guarded graph `H^-` and a new guarded graph `H^+` on the same
target and cell shores, each arising from one legal complete cap state.  Let
`M` be a maximum matching of `H^-`, with deficiency `delta_old`.  Suppose
`ell` edges of `M` are absent from `H^+` and delete them, obtaining `M_0`.
Let `alpha` be the maximum number of pairwise vertex-disjoint
`M_0`-augmenting paths in `H^+`.

### Theorem 7.1 (compiler gain is augmenting-path boundary)

\[
 \boxed{\delta_{new}-\delta_{old}=\ell-\alpha.}       \tag{7.1}
\]

In particular, terminal deficiency at most `b` is possible if and only if

\[
 \alpha\ge\ell+\delta_{old}-b.                       \tag{7.2}
\]

At most `ell` of these paths can terminate at cells freed by the destroyed
matching edges.  Therefore at least

\[
                         \delta_{old}-b               \tag{7.3}
\]

paths must terminate at cells unused by `M` (read the bound as
`(delta_old-b)_+` when `b>delta_old`).

#### Proof

The matching `M_0` has size `|M|-ell`.  Berge's augmenting-path theorem
gives `nu_new=|M_0|+alpha`, proving (7.1) and (7.2).  The `ell` deleted edges
free only `ell` previously used cells.  Every further augmenting-path
endpoint lies on an old-unused cell, giving (7.3).  \(\square\)

An occurrence-labelled realization of a Johnson square, octahedral trade,
or closed `C_6` **on one fixed physical cell set** has zero matching
boundary: it routes alternating cycles and preserves that used-cell basis.
The signed counter identity alone does not imply such a fixed-cell lift, and
a realization on different cells may itself carry nonzero boundary.  Closed
fixed-cell lifts cannot supply (7.3).  A sufficient physical linkage theorem
must provide, in addition to prepared packet slots,

1. at least `delta_old-b` private unused-cell return endpoints;
2. `ell+delta_old-b` mutually co-selectable guarded augmenting paths; and
3. a literal realization of every internal alternating component.

For square-only realization the support must be chordal bipartite and every
graph four-cycle must be a certified physical Johnson square; otherwise the
corresponding longer even circuits are also required.  An induced `C_6` is
the first exact square-generation obstruction.

For the actual nonlinear compiler, first choose `M` in an old optimizing
state `theta^-`, then apply Theorem 7.1 separately to each legal new state
`theta^+`; terminal deficiency is the minimum over those new states.  If
`ell(theta^+),alpha(theta^+)` denote the corresponding rows, then

\[
 \delta_{\rm terminal}-\delta_{\rm old}
   =\min_{\theta^+}\bigl(
      \ell(\theta^+)-\alpha(\theta^+)\bigr).                   \tag{7.4}
\]

Neither the raw graph of Section 6 nor a favourable `ell-alpha` row for one
state permits exchanging the order of these quantifiers.

## 8. Proved boundary

The current status is now exact.

* **Solved:** the full integral unlabelled signed all-depth counter lattice.
* **Solved:** no isolated one-block q1-exact actuator can manufacture the
  required twist.
* **Solved:** the fixed raw phase-common individual-incidence graph, and
  hence any matching restricted to that fixed raw basis, cannot improve
  under an adjacent twist.
* **Open:** prospectively plant already twisted private slots, or build a
  q1-compensated multi-block actuator.
* **Open:** couple the resulting signed word to a nonnegative,
  occurrence-labelled, basis-changing return satisfying U5 and all cap
  guards.
* **Open:** regenerate the same prepared actuator/return interface after the
  Pascal lift.

Thus the reflection correction is genuinely positive, but its correct use
is as complete algebraic freedom behind a physical absorber.  It is not a
terminal compiler by itself.

## 9. Audit

The dependency-free audit

```text
scratch/audit_threadA_coatom_full_coupled_span_20260801.py
scratch/threadA_coatom_full_coupled_span_20260801.audit.json
```

checks:

* all 35 adjacent-flag commutator identities for `3<=d<=9`;
* both boundary-role square identities and complete depth coverage for
  `2<=d<=14`;
* zero point/pair marginals of every enumerated octahedron; and
* over two independent prime fields, equality between the octahedral span
  and the pair-incidence kernel for every `5<=k<=8`, `3<=s<=k-2`.

It reports

```text
PASS_THREAD_A_COATOM_FULL_COUPLED_SPAN
```

The compiler antitonicity was independently replayed from the raw
allowed/mandatory/minimal-hit predicates for every `2<=d<=6` and every
`1<=s<d`; the replay obtained exactly the four families (6.3), `2d` killed
columns, and no other common-neighbourhood change.  The full-span semantic
audit also caught and removed a false identification between the unplanted
four-term flag action and the endpoint-planted eight-term baseline; Theorem
4.1 now uses only the authenticated boundary-role commutators (4.5)--(4.6).
