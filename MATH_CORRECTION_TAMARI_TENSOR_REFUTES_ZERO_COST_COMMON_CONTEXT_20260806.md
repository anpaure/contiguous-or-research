# Correction: a common token suffix can create linear cyclic-order dispersion

## Status

The context-dispersion argument in Section 3 of
`CATALAN_SEAM_ABSORPTION_OBSTRUCTION.md` contains a false step.  It claims
that inserting one common ordered context into corresponding cyclic gaps
does not increase cyclic adjacent-swap distance.  A shortest old swap path
may cross the marked gap; after insertion, that crossing must pass the
entire context and is no longer a single adjacent swap.

The independently audited all-dimensional four-row Tamari tensor gives a
literal counterexample family.  Its common token suffix creates exactly
the linear dispersion which the old theorem declared impossible.

Only the context-distance Section 3 and conclusions depending on its
zero-cost claim are retracted here.  The full-orbit pointing obstruction
and fixed-hierarchy linear-independence statements in the old note are
separate arguments.

## 1. Omitted words of a tensed complement geodesic

Let

\[
             P_0,P_1,\ldots,P_r                     \tag{1.1}
\]

be a complement geodesic.  Write its successive exchanges as

\[
             d_1\to i_1,\ldots,d_r\to i_r.          \tag{1.2}
\]

The odd-wreath lift has omitted-coordinate order

\[
             (i_1,d_1,i_2,d_2,\ldots,i_r,d_r,\infty). \tag{1.3}
\]

Indeed, the edge from `P_(t-1)` to the inserted odd vertex omits `i_t`,
the next edge omits `d_t`, and the closing edge between complementary
endpoints omits `infinity`.

In the tensor construction, the first four exchanges are the base
four-row packet and the remaining `r-4` exchanges come from one common
tail geodesic

\[
             S_0,S_1,\ldots,S_{r-4}.                 \tag{1.4}
\]

Hence every extended omitted word has the form

\[
             C_R\,B\,\infty,                        \tag{1.5}
\]

where `C_R` is the eight-letter base token word of row `R` and

\[
             B=(i^E_1,d^E_1,\ldots,i^E_{r-4},d^E_{r-4}) \tag{1.6}
\]

is literally the same ordered suffix in all four rows.

## 2. The tensor rows remain a partial factor

The audited tensor theorem proves that, within either phase, all extended
rank-`r` states and all extended adjacent unions are distinct across the
four rows.  Complementing the adjacent unions and adjoining `infinity`
gives the other shore.  Thus the four tensed wreaths are pairwise
vertex-disjoint for every `r>=4`.

Let `d_circ` be the cyclic adjacent-swap distance from the old note.  Its
overlap inequality was

\[
 |W_r(C)\cap W_r(D)|\ge 2r+1-2d_{\rm circ}(C,D).     \tag{2.1}
\]

Apply (2.1) to any two distinct tensed rows.  Their wreath supports are
disjoint, so

\[
             d_{\rm circ}(C_RB\infty,C_{R'}B\infty)
                    \ge r+1.                         \tag{2.2}
\]

The corresponding base distance is an absolute constant (the old audit
reports minimum seven).  Therefore adjoining the common suffix (1.6)
increases distance by a quantity linear in `r`.

### Theorem 2.1 (zero-cost context claim is false)

There exist fixed cyclic orders `C_R,C_(R')` and arbitrarily long common
ordered suffixes `B` such that

\[
 d_{\rm circ}(C_RB\infty,C_{R'}B\infty)
   -d_{\rm circ}(C_R\infty,C_{R'}\infty)\longrightarrow\infty. \tag{2.3}
\]

In particular, the assertion `e_t=0` for a common inserted context in old
Theorem 3 is false.

#### Proof

Use two rows of either phase of the tensed Tamari packet.  Equation (2.2)
grows with `r`, while the base distance is fixed. \(\square\)

## 3. The exact error

The old proof says that a common inserted block can be held fixed while
following a shortest adjacent-swap sequence between the old orders.  This
is valid only when the chosen swap word never moves an old label across the
marked insertion cut.  If an old adjacent transposition crosses that cut,
then after inserting a block of length `L` the old label must cross `L`
new labels.  Treating the block as having zero width loses those inversions.

For fixed linear representatives, there is an exact formula.  Write

\[
 C=C_LC_R,\qquad D=D_LD_R,
\]

insert the same ordered `L`-letter block `B` at the two displayed cuts,
and let `A_C,A_D` be the sets of old labels lying to the left of the two
cuts.  Then

\[
 d_{\rm inv}(C_LBC_R,D_LBD_R)
   = d_{\rm inv}(C,D)+L\,|A_C\mathbin\triangle A_D|. \tag{3.1}
\]

Indeed, old--old inversions are exactly those already counted by
`d_inv(C,D)`, and there are no new--new inversions.  An old label `x`
reverses its order relative to every one of the `L` new labels exactly when
`x` lies on opposite sides of the two cuts.  This proves (3.1).

Cyclic distance minimizes the corresponding inversion count over choices
of linear cut and orientation.  On every alignment which keeps `B` as one
oriented block, (3.1) applies with its own cut-side symmetric difference.
An alignment reversing or cutting through `B` also pays the resulting
internal or boundary inversions of the distinct `B`-labels.  Thus cyclic
minimization may choose a different crossing pattern, but it does not make
the marked block universally free; zero extra cost requires an alignment
with zero total block-crossing contribution.

The Tamari tensor deliberately uses base rows for which every admissible
alignment pays a nonzero cut crossing.  Its common tail is therefore a
**dispersion amplifier**, not a zero-cost context.

## 4. Consequence for the host programme

The earlier claimed no-go against indefinite common-tail suspension of the
four-row Haar/Tamari packet is withdrawn.  The local tensor already gives
a support-feasible partial factor in every dimension.  Together with the
exact noncanonical base completion, the remaining question is now solely
whether these four protected wreaths extend to a complete exact factor in
every sufficiently large dimension.

No cyclic-distance obstruction currently rules out that extension.
