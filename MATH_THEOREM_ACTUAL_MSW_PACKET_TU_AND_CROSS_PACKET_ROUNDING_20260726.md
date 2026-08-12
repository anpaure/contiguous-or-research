# Actual recursive MSW matrix: packet TU and the cross-packet rounding gate

Date: 2026-07-26

## 0. Outcome

The generic determinant-two triangle is not the right local model inside
one recursive MSW parent packet.

Fix the switch scale `r`, an aligned size-`r+1` parent context `C`, and
the `Cat_(r-1)` elementary switches indexed by
`R in D_(r-1)`.  On every tagged lower or upper depth in a range

\[
                         r\le q\le Q\le m-r,             \tag{0.1}
\]

the vertically stacked column matrix of this one packet is totally
unimodular.  The reason is exact:

* the two suffix arms are independent of `R`, so all their rows are
  signed all-one rows on the packet;
* the two prefix cores contain the complete insertion/deletion set of
  `R`, so every prefix endpoint recovers both its arm type and `R`.
  Hence each prefix row touches at most one packet column.

Thus no determinant-two minor, and in particular no triangle minor, lies
inside one parent packet.  Every obstruction in the actual stacked matrix
must use target collisions between distinct aligned parent contexts.

This yields a sharp conditional rounding theorem.  For each tagged target
row, retain the incidences from one parent packet and declare all incidences
from the other packets exceptional.  The retained matrix is TU.  If

\[
 \Lambda_{\mathcal Q}
 =\sum_{(q,S)}w_q
   \left(
    d(q,S)-\max_Cd_C(q,S)
   \right)                                               \tag{0.2}
\]

is the minimum resulting exceptional incidence, then every fractional
point of an additive MSW subcube has an integral rounding with aggregate
weighted cap-tail increase at most `2 Lambda_Q`.  Here `d_C(q,S)` is the
number of nonzero packet-`C` columns at tagged row `(q,S)`, and
`d=sum_C d_C`.

Consequently:

1. positive-density disjoint triangle obstructions force
   `Lambda_Q=Omega(W)`;
2. the actual additive rounding theorem is finished if
   `Lambda_Q=o(W)`;
3. without a cross-parent collision census, the universal bound remains

   \[
                  \Lambda_{\mathcal Q}
                  \le8M\sum_{q\in\mathcal Q}w_q         \tag{0.3}
   \]

   per tagged lower-depth family, where
   `M=T_(m,r)=Theta(W/r^(3/2))`.

Thus logarithmic windows already round at `o(W)`, while a Gaussian window
still requires a new theorem.  The exact missing theorem is not generic
TU; it is the cross-parent prefix/suffix collision bound (0.2), or a
dynamic analogue for the nonadditive full cube.

**Subsequent audit.**  The literal bound (0.2) is false for the complete
Catalan parent atlas.  The persistent marked-gap family in
`MATH_OBSTRUCTION_MSW_CROSS_PARENT_LAMBDA_GAUSSIAN_20260726.md` gives

\[
 \Lambda_{[r+1,A\sqrt m]}^{\rm MWB}
 =\Omega\left(W\sqrt m/r^{3/2}\right),                 \tag{0.4}
\]

and already gives `Omega(W)` on the first `Theta(r^(3/2))` depths.  The
packet-TU theorem below remains valid; what fails is paying every
cross-packet incidence separately.

---

## 1. Exact packet form through a depth interval

Fix an aligned size-`r+1` parent context `C`.  The elementary switches in
this context are indexed by `R in D_(r-1)`.  Rotate the omitted-label word
at the parent block.  The common tail has the embedded flip permutation of
`R` first and the exterior tail of `C` second.  Since the embedded block
has even length, the parity split has the form

\[
\begin{aligned}
 \mathsf E_{C,R}
   &=(\iota_C\mathsf A(R),\ \mathsf E_C^{\rm ext}),\\
 \mathsf O_{C,R}
   &=(\iota_C\mathsf B(R),\ \mathsf O_C^{\rm ext}),     \tag{1.1}
\end{aligned}
\]

up to a simultaneous interchange of `A,B` caused by the fixed ambient
orientation.  That interchange has no effect on the argument.  The
underlying sets of `mathsf A(R)` and `mathsf B(R)` are respectively the
down-step and up-step positions of `R`.

At lower depth `q`, put

\[
                         \ell=m-q-1.                    \tag{1.2}
\]

The exact isolated column is

\[
\begin{aligned}
 a_{q,C,R}={}&
  \partial_C\operatorname {suf}_{\ell}(\mathsf O_{C,R})
 +\partial_C\operatorname {suf}_{\ell}(\mathsf E_{C,R})\\
 &-\partial_C\operatorname {pre}_{\ell}(\mathsf E_{C,R})
 -\partial_C\operatorname {pre}_{\ell}(\mathsf O_{C,R}),
                                                               \tag{1.3}\\
 \partial_CK={}&
  \mathbf e_{K\cup\{\gamma_C\}}
 -\mathbf e_{K\cup\{\beta_C\}}.
\end{aligned}
\]

The parity lists in (1.1) have internal prefix length `r-1`.  Their
exterior suffix lengths are `m-r` and `m-r-1`.  Under (0.1),

\[
                 r-1\le\ell\le m-r-1.                  \tag{1.4}
\]

It follows that both suffixes in (1.3) lie wholly in the exterior tail
and are independent of `R`, whereas both prefixes contain the whole
internal `R` list.  Therefore there are fixed exterior cores
`A_(q,C),B_(q,C)` and variable prefix cores
`P^E_(q,C,R),P^O_(q,C,R)` such that

\[
 \boxed{
 a_{q,C,R}=f_{q,C}+g_{q,C,R},}                          \tag{1.5}
\]

where

\[
\begin{aligned}
 f_{q,C}&=\partial_C(A_{q,C}+B_{q,C}),\\
 g_{q,C,R}&=-\partial_C
       (P^E_{q,C,R}+P^O_{q,C,R}).                       \tag{1.6}
\end{aligned}
\]

At `q=r`, this is exactly the packet formula already recorded as

\[
 a_{C,R}=\partial_C(A_C+B_C)
          -\partial_C(P^E_{C,R}+P^O_{C,R}).             \tag{1.7}
\]

The point of (1.4) is that the same decomposition is valid
simultaneously throughout the whole interval (0.1), not only at the
matched depth.

---

## 2. Prefix endpoints recover the spectator

### Lemma 2.1 (packet-private prefix supports)

Fix `C,q` satisfying (0.1).  As `R` varies in `D_(r-1)`, all endpoints in

\[
 \operatorname {supp}g_{q,C,R}
\]

are mutually distinct.  They are also disjoint from
`supp f_(q,C)`.

#### Proof

By (1.4), the internal part of `P^E_(q,C,R)` is the affine image of the
complete down-step set of `R`; the internal part of
`P^O_(q,C,R)` is the affine image of its complete up-step set.  A down-step
set, or its complementary up-step set, determines the Dyck word.  Hence
each map

\[
 R\longmapsto P^E_{q,C,R},\qquad
 R\longmapsto P^O_{q,C,R}                               \tag{2.1}
\]

is injective.

The two arm types cannot collide.  If their fixed exterior portions
differ, this is immediate.  At the endpoint where those portions are
empty, the down-step set of a nonempty Dyck word contains its last
coordinate, while every up-step set omits that coordinate.  Thus

\[
                  P^E_{q,C,R}\ne P^O_{q,C,R'}           \tag{2.2}
\]

for every `R,R'`.  Appending `beta_C` or `gamma_C` creates no new
collision because neither exceptional label lies in a core, and the two
exceptional labels are distinct.

Finally, every variable prefix core contains all `r-1` coordinates of one
internal parity class.  The fixed suffix cores lie wholly in the exterior
tail.  Therefore a prefix endpoint cannot equal a suffix endpoint.
\(\square\)

Upper-depth columns are coordinate complements of the corresponding
lower-depth columns.  Complementation is a row permutation and preserves
all conclusions of Lemma 2.1.  Different depths are treated as tagged
row blocks, so no accidental equality between ranks affects the stacked
matrix.

---

## 3. Total unimodularity of one stacked parent packet

Let `A_C^all` be the matrix whose columns are indexed by
`R in D_(r-1)` and whose rows are all chosen tagged lower and upper depths
in a set `mathcal Q subseteq [r,m-r]`.

### Theorem 3.1 (stacked packet TU)

\[
                         \boxed{A_C^{\rm all}\text{ is TU}.}             \tag{3.1}
\]

#### Proof

By (1.5)--(1.6) and Lemma 2.1, every row of `A_C^all` has one of two
forms when restricted to the packet columns:

1. a signed all-one row, coming from a fixed suffix endpoint; or
2. a signed unit row, coming from one variable prefix endpoint.

Take any square submatrix `B`.  If `B` contains at least two all-one rows,
those rows are proportional and `det B=0`.  If it contains no all-one
row, every row has at most one nonzero entry, so `det B` is `0,+1`, or
`-1`.  If it contains exactly one all-one row, expand along the remaining
unit rows.  A nonzero term uses distinct columns for all unit rows and
leaves one entry of the all-one row; hence again
`det B in {0,+1,-1}`.  This is total unimodularity. \(\square\)

### Corollary 3.2 (no intrapacket triangle)

No determinant-two triangle minor can be supported by three columns from
one aligned parent packet.  More generally, every non-TU minor of the full
actual matrix uses at least one target row incident with columns from two
distinct parent contexts.

The second assertion follows because deleting all cross-parent rows makes
the full matrix a row-disjoint direct sum of the TU packet matrices.

This is stronger than triangular first-shadow independence.  It proves
all minors of a packet are unimodular, and it does so simultaneously over
the tagged depth interval (0.1).

---

## 4. The exact cross-packet excess metric

Let `A^all` be an additive stacked MSW matrix, with its columns partitioned
into parent packets `mathcal E_C`.  For a tagged target row `t=(q,S)`, put

\[
 d_C(t)=\sum_{e\in\mathcal E_C}|a_{t,e}|,
 \qquad d(t)=\sum_Cd_C(t).                              \tag{4.1}
\]

At an interior rank these are ordinary incidence counts.  Formula (4.1)
also handles boundary multiplicity without change.

Choose for each row a home packet `h(t)` attaining
`max_C d_C(t)`, and erase from that row every nonhome incidence.  Call the
retained matrix `B` and the erased matrix `E=A^all-B`.  Then

\[
 \|E\|_{1,w}:=
  \sum_t w_t\sum_e|E_{t,e}|
 =\sum_t w_t\left(d(t)-\max_Cd_C(t)\right).             \tag{4.2}
\]

Define the right side to be `Lambda_Q`.  Every row of `B` is supported in
one packet.  After grouping rows by their home packets, `B` is a direct
sum of submatrices of the packet matrices from Theorem 3.1.  Hence

\[
                              B\text{ is TU}.            \tag{4.3}
\]

The use of `d-max d_C`, rather than the full incidence on every colliding
row, is sharp for this deletion argument: all incidences belonging to one
dominant packet are retained for free.

---

## 5. A packet-core rounding theorem

Let the initial loads and caps be integral, and let `x in [0,1]^E` be a
fractional point of an additive cube.  Put

\[
 \mathcal K_w(x)=
  \sum_{q\in\mathcal Q}w_q
  \sum_S\bigl(\mu_q(S)-b_q+(A_qx)(S)\bigr)_+.           \tag{5.1}
\]

### Theorem 5.1 (cross-packet excess rounding)

There exists `X in {0,1}^E` such that

\[
 \boxed{
                 \mathcal K_w(X)
                 \le\mathcal K_w(x)+2\Lambda_{\mathcal Q}.}             \tag{5.2}
\]

In particular, `Lambda_Q=o(W)` is sufficient for coefficient-one
integral rounding of every fractionally feasible additive solution.

#### Proof

First ignore the erased matrix `E` and minimize the cap-tail objective
formed with `B`.  Its epigraph constraint matrix is `[B|-I]`, with
integral right-hand side and integral variable bounds.  By (4.3), it is
TU.  Therefore it has an integral optimum `X`, and the retained-row cost
at `X` is no larger than the retained-row cost at the given fractional
point `x`.

At an erased incidence row `t`, the scalar positive-part map is
one-Lipschitz, and

\[
 |(E(X-x))_t|
 \le\sum_e|E_{t,e}|\,|X_e-x_e|
 \le\sum_e|E_{t,e}|.                                   \tag{5.3}
\]

First compare the full objective at `X` with the retained objective at
`X`; (5.3) with `x=0` costs at most `Lambda_Q`.  The retained objective at
`X` is no larger than the retained objective at the supplied point `x`.
Comparing that retained objective back with the full objective at `x`
costs at most a second `Lambda_Q`.  This proves (5.2). \(\square\)

The theorem is deterministic and synchronized across all tagged depths.
It does not color the packets and does not lose a constant fraction of the
switch capacity.  All nonintegrality is charged only to incidences which
cross parent packets.

---

## 6. Consequence for determinant-two triangles

Consider a determinant-two triangle witnessed by three columns and three
rows, each witness row meeting the corresponding pair of columns.  It
cannot lie in one packet by Corollary 3.2.

If the three columns lie in three packets, every witness row is
cross-packet.  If two columns lie in one packet and the third in another,
the two witness rows joining the third column to the first packet are
cross-packet.  Thus every actual triangle witness uses at least two
cross-packet rows.

Consequently any family of triangle minors with disjoint witness rows has
cardinality at most one half of the number of cross-packet witness rows,
and a fortiori is `O(Lambda_Q)`.  In particular,

\[
 \text{positive-density row-disjoint triangle minors}
 \quad\Longrightarrow\quad
                         \Lambda_{\mathcal Q}=\Omega(W). \tag{6.1}
\]

This is the exact sense in which the generic triangle question reduces to
the actual cross-parent collision census.  The common suffix arms inside a
packet are stars, not odd cycles.

The converse is not asserted: large `Lambda_Q` need not organize itself
into triangle minors.  It can still obstruct the deletion-based rounding
theorem without proving an integrality gap.

---

## 7. Quantitative ledger and the surviving scale

Let

\[
 M=T_{m,r}=H_{m,r+1}\operatorname {Cat}_{r-1}
 =\left(\frac1{64\sqrt\pi}+o(1)\right)
       \frac W{r^{3/2}}.                                \tag{7.1}
\]

At one tagged interior depth every column has eight incidences, so without
using any collision structure,

\[
 \Lambda_{\mathcal Q}
 \le8M\sum_{q\in\mathcal Q}w_q.                         \tag{7.2}
\]

If lower and complementary upper blocks are both given unit weight, the
corresponding bound is doubled.  This agrees, up to the harmless constant,
with the direct independent-rounding and finite-dependence bounds in
`MATH_THEOREM_MSW_TRADE_CUBE_ROUNDING_20260726.md`.

At the fatal cutoff `r=Theta(log p)`:

* a one-depth or `O(r)`-depth aggregate has rounding cost

  \[
                  O(Mr)=O(W/\sqrt r)=o(W);              \tag{7.3}
  \]

* for a Gaussian protected window of size `p^(1/4)`, the crude bound is

  \[
                 O\left(\frac{Wp^{1/4}}{r^{3/2}}\right),\tag{7.4}
  \]

  which is not `o(W)`.

The exact Gaussian-window rounding target is therefore

\[
 \boxed{
 \sum_{(q,S)}
  \left(
    d(q,S)-\max_Cd_C(q,S)
  \right)=o(W),}                                        \tag{7.5}
\]

with lower and upper tags both included.  A weaker weighted version is
enough if the compiler charges different depths with weights.

Equation (7.5) is a concrete Catalan flag-collision statement.  It asks
that, after assigning every physical target to its dominant aligned parent
context, only `o(W)` prefix/suffix arm incidences arrive from other
contexts.  It is strictly weaker than global target injectivity and
strictly stronger than bounded boundary-conflict degree.

---

## 8. Additivity and the full cube

Theorems 3.1 and 5.1 are literal matrix theorems.  Their simultaneous-depth
application requires

\[
                 \mu_q^x=\mu_q+A_qx
                 \quad(q\in\mathcal Q).                 \tag{8.1}
\]

For one matched depth `q=r`, the fixed-scale parent switches are additive,
so the packet theorem applies directly.  At a general depth, the
boundary-conflict graph has maximum degree at most four, and an independent
class is additive at that depth.  Over a growing set of depths, coloring
the union conflict graph costs up to `4|Q|+1` colors; keeping only one color
loses an unacceptable factor.

For the full nonadditive cube, toggling one bit still has only four old and
four new targets and depends on at most four opposite-boundary bits at one
depth.  This gives the unconditional `O(M|Q|)` aggregate rounding theorem
of `MATH_THEOREM_MSW_TRADE_CUBE_ROUNDING_20260726.md`, but Theorem 5.1
cannot simply be applied to the isolated columns: after an opposite
boundary has already moved, the current target of an arm can differ from
its isolated target.

Hence the nonadditive analogue of (7.5) must be state-aware.  One exact
form is the following.

* For every toggle `e`, depth `q`, and state of its at most four boundary
  neighbors, list the at most eight current endpoint incidences.
* Partition toggles into parent packets and assign every augmented
  `(q,target,neighbor-state)` row to a home packet.
* Prove that the total nonhome incidence used by the rounding trajectory
  is `o(W)`.

This dynamic cross-packet census would reduce the full cube to packet TU
plus `o(W)` exceptional changes.  Bounded degree alone gives only the old
`O(M|Q|)` estimate.

---

## 9. Precise surviving routing gate

The actual recursive MSW matrix does avoid the generic obstruction
locally: every complete parent packet is stacked TU throughout
`r<=q<=m-r`.  The unresolved issue is entirely interpacket.

A coefficient-one proof may now close the integral step in either of two
ways.

1. **Additive route.**  First contract or retain the persistent marked-gap
   suffix fibres.  On the resulting quotient, prove the analogue of (7.5)
   for a simultaneous additive family with enough four-arm drain.  The
   uncontracted form of (7.5) is impossible for the complete atlas.
2. **Dynamic route.**  Prove the state-aware augmented version in Section
   8 while selecting all exact cube bits.  Packet TU handles the home
   incidences; nonhome incidences are paid literally.

Conversely, a sharp obstruction must exhibit `Omega(W)` cross-parent
excess and either organize it into a positive-density signed odd-cycle
minor family or give a weighted cap right-hand side on which that excess
forces `Omega(W)` integral loss.  Merely displaying the generic triangle
or the repeated common suffix arms is not enough.

Fractional four-arm capacity remains logically prior.  At the matched
depth the known fixed-scale family has only two potentially useful arms,
and Catalan overshoot can already make its raw capacity insufficient.
Packet TU removes an integer-rounding ambiguity; it does not create the
missing drain.
