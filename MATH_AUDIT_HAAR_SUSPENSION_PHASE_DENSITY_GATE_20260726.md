# Haar suspension into first-eligible `B_4` packets: the phase-density gate

Date: 2026-07-26

Method: pure mathematics, using the already certified finite Haar and
antipodal-suspension identities as inputs.

## 0. Verdict

The `m=4` four-for-four Haar edge is a valid complete physical
`q=1`-null, lower-`q=2`-active trade.  Its rank-two signs pass the
coordinate-degree invariant; the last two terms are `-e_19+e_29`.

There is an exact all-dimensional **signed** suspension, but no known
positive exact-factor suspension.  More sharply, the proposed use inside
the first-eligible `B_4` packet factor faces two rigorous obstructions.

1. Inside one fixed pair-cube packet, a lower depth-one target uniquely
   identifies its physical edge.  Hence every packetwise `q=1`-null cycle
   trade has the same edge set and is deeper-shadow trivial.  A useful
   suspension must change coordinate frames or couple distinct packets.
2. The Gaussian fixed-block Hall cut forces
   `Omega(W/sqrt(m))` recoupled transition sites.  Since the factor has
   `W/(2h)+o(W/h)` long strips, every retained `C_(2h)` must participate in
   `Omega(h/sqrt(m))` bounded recouplings on average.  Row-disjoint copies,
   and more generally `o(h/sqrt(m))`-overlapping copies, cannot work.

For `h=m^(3/4+o(1))`, the required overlap is
`Omega(m^(1/4+o(1)))` gadgets per strip.  Thus the finite Haar edge cannot
be inserted as a sparse absorber.  It must be fused into a phase-dense,
moving-frame recursion with one common owner completion.

An exact commutator lemma below explains how a hierarchy of
`(q-1)`-null/`q`-active trades would be produced once such positive
suspensions exist.  Its support-feasible algebra is easy; the simultaneous
packing and completion conditions are precisely the missing content.

## 1. Fixed-pair-cube rigidity

Let `P_1,...,P_h` be disjoint coordinate pairs and let `R` be a fixed core
disjoint from them.  Put

\[
 \mathcal Q(R;P_1,\ldots,P_h)
 =\left\{R\cup\{x_1,\ldots,x_h\}:x_i\in P_i\right\}.
 \tag{1.1}
\]

This is the owner set of one physical `Q_h` packet.  Its Johnson edges
are precisely the pairs which differ in one coordinate pair.

### Theorem 1.1 (edge reconstruction from the lower shadow)

On the packet (1.1), the map

\[
 \{X,Y\}\longmapsto X\cap Y                         \tag{1.2}
\]

from physical Johnson edges to lower depth-one targets is injective.
Consequently, if two simple cycle factors of the same packet have equal
complete lower depth-one multisets, then they have the same physical edge
set and therefore the same cycle decomposition and every deeper
consecutive-window multiset.

#### Proof

If an edge flips pair `P_i`, its intersection contains the fixed core `R`,
contains one selected endpoint from every `P_j`, `j!=i`, and contains no
endpoint of `P_i`.  The missing pair identifies `i`, and the retained
endpoints identify the two edge endpoints uniquely.  This proves
injectivity.

Equality of the lower multisets therefore gives equality of the edge
multisets.  A simple two-regular graph is the disjoint union of its cycles
in a unique way.  Every deeper window depends only on these cyclic edge
components. \(\square\)

### Corollary 1.2 (no intrapacket Haar suspension)

No nontrivial `q=1`-null, `q=2`-active trade can have both shores entirely
inside the same fixed first-eligible `Q_h` packet.  The conclusion remains
true for a disjoint union of packets if the depth-one equality is required
packet by packet.

Thus Hamming resolution changes, direction-order changes, and tensors of
the eight-owner rectangle inside one fixed frame cannot suspend the Haar
direction.  A positive construction must let first-shadow transport cancel
between different packets or must recouple the coordinate pairs
themselves.  The `24`-owner associator is relevant precisely because it
changes the pair frame.

## 2. The phase-density lower bound for bounded copies

Let `F` be a family of physical `C_(2h)` strips with

\[
                         |F|={W\over2h}+o(W/h).       \tag{2.1}
\]

Fix the original four-block partition of the first-eligible construction.
Mark transition positions so that every window avoiding all marked
positions is native to that fixed frame.  Write

\[
                         \mathcal T(F)
 =\sum_{C\in F}|E_{\rm rec}(C)|.                    \tag{2.2}
\]

The fixed-block Hall theorem gives, for every compact
`0<a<b<infinity`,

\[
 \sum_{a\sqrt m\le q\le b\sqrt m}
       (M_q^-+M_q^+)
 \ge \Theta(W\sqrt m)-O(m\mathcal T(F)).            \tag{2.3}
\]

Therefore `o(W)` aggregate band leave forces

\[
 \boxed{
 \mathcal T(F)=\Omega(W/\sqrt m),
 \qquad
 {\mathcal T(F)\over|F|}=\Omega(h/\sqrt m).}        \tag{2.4}
\]

Now let `A` be a family of embedded bounded gadgets.  Suppose one gadget
touches at most `r_0` strips and marks at most `s_0` transition positions
on each touched strip, where `r_0,s_0` are absolute constants.  Put

\[
                         d(C)=|\{A\in\mathscr A:C\text{ is touched by }A\}|.
\]

### Theorem 2.1 (overlap forced on bounded Haar copies)

If the final mixed-frame factor has `o(W)` aggregate Gaussian-band leave,
then

\[
 \boxed{
 {1\over|F|}\sum_{C\in F}d(C)
 =\Omega\!\left({h\over s_0\sqrt m}\right).}        \tag{2.5}
\]

In particular

\[
                         \max_Cd(C)
 =\Omega(h/(s_0\sqrt m)).                            \tag{2.6}
\]

#### Proof

The union of the gadget marks satisfies

\[
 \mathcal T(F)
 \le s_0\sum_Cd(C).
\]

Combine this with (2.4) and divide by (2.1). \(\square\)

### Consequences

* Row-disjoint bounded copies have `d(C)<=1` and fail whenever
  `h/sqrt(m)->infinity`.
* Any family with `max_C d(C)=o(h/sqrt(m))` fails.
* At `h=m^(3/4+o(1))`, every strip must meet
  `Omega(m^(1/4+o(1)))` gadgets on average.
* The required number of bounded gadget incidences is
  `Omega(W/sqrt(m))`.  This is compatible with the raw owner count, but
  incompatible with independent component switches: gadgets sharing a
  strip do not give independent exact-factor bits.  They must be fused
  into a larger common-support trade.

Since every gadget touches at most `r_0` strips,

\[
 |mathscr A|
 \ge {1\over r_0}\sum_Cd(C)
 =\Omega\!\left({W\over r_0s_0\sqrt m}\right).       \tag{2.7}
\]

Thus even the number of local commutator instances must be Gaussian-scale;
no Catalan-scale or one-per-strip bank is large enough when `h>>sqrt(m)`.

There is no scalar slot-count contradiction at this scale.  Giving each
strip `Theta(h/sqrt(m))` disjoint bounded phase slots supplies
`Theta(W/sqrt(m))` row-slot incidences in total, exactly the order required
by (2.4).  The obstruction is structural: the four (or more) altered row
segments of every instance must reclose into long physical cycles, and the
overlapping instances must share one exact owner partition.  Counting
alone neither proves nor refutes that fused closure.

This is a Hall/invariant obstruction, not a failure of probabilistic
packing estimates.  It applies even if every individual bounded gadget is
perfectly exact.

## 3. What the antipodal suspension proves and fails to prove

Let `w` be a signed wreath trade on `2m+1` coordinates with

\[
                         B_mw=B_{m-1}w=0.             \tag{3.1}
\]

Insert two new coordinates in gaps at distance `m` and sum over all
`2m+1` pointings; call the resulting linear operator `P_m`.  The exact
sector calculation gives

\[
 B_{m+1}P_mw=B_mP_mw=0,                              \tag{3.2}
\]

and

\[
 B_{m-1}P_mw
 =(m-1)(\iota_x+\iota_y)B_{m-2}w.                   \tag{3.3}
\]

Thus the `m=4` Haar signal has an injective signed suspension in every
dimension.

The failure is positivity.  For one old cyclic row, its `2m+1` pointed
extensions repeat each relevant new middle owner `m+1` times.  A packing
can contain at most one pointed extension of that old row.  For the
certified four-for-four seed, the exact five-state/three-state pointing
criterion has no one-point-per-row solution already at `m=4 -> 5`.
Equivariant, antipodal, and marked-cut orderwise extensions therefore do
not give a positive trade.

There is a second independent obstruction.  The two completed `m=4` Haar
factors cannot, under any relabeling, choice of infinity, rooting, or row
reversal, be made canonical port-transversal factors.  Hence their finished
rows cannot simply be installed at the boundary of a larger Dyck hole.

The linear identity is consequently not the missing theorem.  The missing
theorem must reroute owner boundaries and construct the common completion
at the same time.

### 3.1 The deeper signal must also be dispersed

Iterating the signed antipodal operator from the `m=4` seed multiplies one
old rank-two coefficient by

\[
                         \prod_{j=4}^{M-1}(j-1)
 ={(M-2)!\over2}.                                    \tag{3.4}
\]

But in dimension `M` every middle packing has the universal depth-two
target capacity

\[
 \mu_{M-2}(T)
 \le
 \left\lfloor{(M+3)(M+2)\over6}\right\rfloor .      \tag{3.5}
\]

For `M>=7`, (3.4) is larger than (3.5); the twice-suspended `M=6`
profile is already excluded by the sharper four-versus-three saturation
count.  Therefore even a hypothetical positive thinning cannot retain the
literal factorial branch amplitude.  A valid suspension must **disperse
and renormalize** the Haar signal while keeping some nonzero controlled
depth-two component.

## 4. A depth-raising commutator lemma

The following algebra isolates the proposed all-depth hierarchy.

Let

\[
                         w={\bf1}_P-{\bf1}_N          \tag{4.1}
\]

be a support-feasible exact-owner trade at rank `m`, and let `g` be a
coordinate permutation.  Define

\[
 [1-g]w
 =({\bf1}_P+{\bf1}_{gN})
  -({\bf1}_N+{\bf1}_{gP}).                           \tag{4.2}
\]

### Lemma 4.1 (support-feasible commutator)

Assume the two common middle supports `U` and `gU` are disjoint.  Then
(4.2) is a squarefree support-feasible trade on `U dotcup gU`.  For every
depth `j`,

\[
 B_{m-j}([1-g]w)=(1-g)B_{m-j}w.                     \tag{4.3}
\]

If

\[
 B_mw=\cdots=B_{m-q+1}w=0,
 \qquad \Delta_q:=B_{m-q}w\ne0,                    \tag{4.4}
\]

and

\[
                         g\Delta_q=\Delta_q,         \tag{4.5}
\]

then the commutator is null through depth `q`.  If additionally

\[
                         (1-g)B_{m-q-1}w\ne0,        \tag{4.6}
\]

it is depth-`(q+1)` active.

#### Proof

Each sign in (4.2) contains one packing on `U` and one on the disjoint
support `gU`, so it is a packing.  Both signs cover `U dotcup gU` exactly.
Equation (4.3) is linearity and equivariance of cyclic interval incidence.
Equations (4.4)--(4.6) then give the last assertion. \(\square\)

To make (4.2) an **applicable exact-factor move**, one further needs one
residual packing completing either sign.  Support feasibility alone does
not provide that completion.

Lemma 4.1 gives a formal recursion:

\[
 (q-1)\text{-null}/q\text{-active}
 \longrightarrow
 q\text{-null}/(q+1)\text{-active}.                 \tag{4.7}
\]

Its two nonformal inputs are exactly:

1. a selector permutation `g` satisfying (4.5)--(4.6) while
   disjointizing the two owner supports; and
2. one common exact completion of the crossed signs in (4.2).

A fixed spectator pair cannot generally supply both.  If it places `U`
and `gU` in distinguishable fixed contexts, then it also distinguishes the
leading shadow and destroys (4.5).  This is the selector/collar tension in
its shortest algebraic form.

## 5. Packable action and sequential repair

Let a trade touch `r` long strips and let `e` be the number of transition
edges changed on its negative shore.  For every depth `q`, the universal
boundary estimate is

\[
 \boxed{
 \|B_{m-q}w\|_1\le4qe.}                             \tag{5.1}
\]

Indeed one changed transition can enter or leave only `q` cyclic
`q`-windows on either shore.

If bounded gadgets are row-disjoint, then `e=O(|F|)=O(W/h)`.  At
`q=Theta(sqrt(m))`, (5.1) gives only

\[
                         O(W\sqrt m/h)=o(W)          \tag{5.2}
\]

when `h/sqrt(m)->infinity`.  This is the action version of Theorem 2.1.
To obtain linear repair at Gaussian depth one needs

\[
                         e=\Omega(W/\sqrt m),        \tag{5.3}
\]

again forcing `Omega(h/sqrt(m))` changed sites per strip.

Suppose, conditionally, that for every `q<=H` there is an applicable
`(q-1)`-null/`q`-active trade family whose leading increments span the
required balanced discrepancy lattice.  Apply the families in increasing
order of `q`.  Every later move is null at all earlier depths, so completed
depths are never disturbed.  Collateral action at depths greater than `q`
is handled at its later stage.  Thus the hierarchy would eliminate
backward leakage exactly; only the final tail beyond `H` remains, where the
factor-blind product-SCD estimate applies.

This conditional triangular procedure is mathematically sound.  What is
missing is the positive hierarchy itself and sufficient leading action at
the density (5.3).

## 6. The exact surviving suspension theorem

The strongest useful next statement is not a bounded-copy packing lemma.
Theorems 1.1 and 2.1 rule that out.  It is the following fused recursion.

> **Phase-dense moving-frame Haar suspension.**  For
> `h/sqrt(m)->infinity`, construct two exact cycle factors on one common
> retained first-eligible owner set such that:
>
> 1. every cycle has length `2h`;
> 2. their complete physical lower and upper `q=1` multisets agree;
> 3. their lower `q=2` difference is nonzero and has total useful action
>    `Omega(W)` after a compatible family is packed;
> 4. every intermediate factor is a zero-one exact owner partition;
> 5. the changed transition set has size `Omega(W/sqrt(m))`, distributed
>    as `Omega(h/sqrt(m))` sites per retained strip; and
> 6. the construction changes pair frames across first-eligible packets,
>    rather than remaining inside a fixed `Q_h`.

Given this base case, apply Lemma 4.1 with compatible moving selectors to
obtain the depth hierarchy.  Without Items 4--6, a formal tensor or signed
commutator does not address the Hall cut.

No such fused suspension is proved here.  The exact obstruction is now
localized: **complete first-shadow neutrality forces triviality inside a
fixed pair cube, while Gaussian coverage forces any mixed-frame escape to
be phase-dense and heavily overlapping.**
