# The endpoint-corrected PBBS collar face retains forced short height-spine runs

**Date:** 2026-08-13  
**Status:** unconditional all-parameter obstruction to the current
endpoint-corrected four-incoming/one-outgoing collar architecture as a
depth-`d` resident source host.  Its graph-level protected-factor theorem
remains valid.  What fails is the first source-host condition, before
pinned erosion and before the typed cap.

## 1. The retained height spine

Put

\[
 A_t=0\,1^t0^t(10)^{r-t},
 \qquad U_t=[2r+1]\setminus A_t.
\tag{1.1}
\]

The role-zero edge installed by the height-`t` pentagon is

\[
 e_t=U_tU_{t+1},
 \qquad
 U_{t+1}=U_t-\{t+1\}+\{2t+1\}.
\tag{1.2}
\]

The endpoint-corrected collar face retains all these role-zero edges for
the high heights `4<=t<H`: it omits the *incoming role-zero collar*, not
the role-zero pentagon edge.  The edges therefore form the protected
oriented height spine

\[
 U_4-U_5-\cdots-U_H.
\tag{1.3}
\]

## 2. One exact short coordinate run

Fix `h>=4` and let

\[
                         x_h=2h+1.
\tag{2.1}
\]

Reading `(1.1)` gives the exact membership pattern

\[
 x_h\notin U_h,
 \qquad
 x_h\in U_t\quad(h+1\le t\le2h),
 \qquad
 x_h\notin U_{2h+1}.                              \tag{2.2}
\]

Indeed, `x_h` is the first one of the alternating tail of `A_h`, so it is
absent from `U_h`.  For `h+1<=t<=2h`, it lies in the zero block
`[t+1,2t]` of `A_t`, so it belongs to `U_t`.  At `t=2h+1`, it lies in the
initial one block of `A_t` and is absent from `U_t` again.

Equivalently, edge `e_h` inserts `x_h` and edge `e_(2h)` deletes it.  Thus,
whenever both edges belong to the retained protected spine, `x_h` has the
maximal positive run

\[
                  U_{h+1},U_{h+2},\ldots,U_{2h},   \tag{2.3}
\]

of length exactly

\[
                              h.                    \tag{2.4}
\]

The run is bounded by two literal protected transitions; choices on the
unprotected completion cannot extend it.

### Theorem 2.1 (resident no-go)

Let the required source aperture be

\[
                         q=d+1.
\tag{2.5}
\]

If there is an integer `h` satisfying

\[
                         4\le h\le d,
 \qquad                  2h<H,                     \tag{2.6}
\]

then the endpoint-corrected protected owner trace has a nonconstant
positive coordinate run of length below `q`.  Consequently it has no
depth-`d` source antecedent and cannot satisfy the pinned-erosion
source-host criterion.

#### Proof

The inequality `2h<H` puts both `e_h` and `e_(2h)` in the retained high
spine.  Equations `(2.2)--(2.4)` give a maximal positive run of length `h`.
Since `h<=d<d+1=q`, the necessary positive-residence condition for a
width-`q` source antecedent fails.  \(\square\)

In particular, for every

\[
                         d\ge4,
 \qquad                  H\ge9,                    \tag{2.7}
\]

one may take `h=4`.  The intended ladder range `H=Theta(d)` eventually
satisfies `(2.7)`, so this is not a bounded low-height exception.

## 3. Why the later source tools cannot repair it

The pinned-erosion equivalence begins with an owner trace whose positive
runs are long enough.  Here that preliminary condition already fails.
Changing source letters cannot change an owner membership trace.

Equivalently, for `x_h=2h+1` the safe-emission set

\[
 E_{x_h}=\{j:x_h\text{ belongs to all }q
                 \text{ owner windows containing source position }j\}
\tag{3.1}
\]

is empty on the run `(2.3)`, because that entire run has length `h<q`.
Thus the pinned-erosion coverage condition already fails with **no pins**:
for every owner `U_t` in `(2.3)`,

\[
 [t,t+q-1]\cap E_{x_h}=\varnothing.                \tag{3.2}
\]

Pins can only remove safe emissions, never create one.

The long one-tag arms and interval-Hall scheduling can absorb flags at the
free ends of fixed blocks.  They cannot alter a positive run whose
insertion and deletion edges both lie strictly inside the protected spine.
Likewise, spacing local history pins does not change `(2.2)`.

Thus the source obstruction occurs in the following order:

\[
\boxed{
\text{forced short protected owner run}
\quad\Longrightarrow\quad
\text{no resident trace}
\quad\Longrightarrow\quad
\text{pinned erosion is inapplicable}.}
\]

The typed cap is further downstream.

## 4. Surviving architectures

The graph theorem for the endpoint-corrected bank is still useful as an
owner/q1/upper-backup factor statement, but it is not a candidate literal
resident carrier in the intended height range.

Two routes survive this exact no-go.

1. **Deleted-spine, all-five-tail architecture.**  Delete every high
   role-zero edge `e_h`, put incoming collars at all five pentagon tails,
   and restore the omitted immediate lower and upper palettes using the two
   explicit isolated backup edges `f_h^-` and `f_h^+`.  This removes the
   forced runs `(2.3)` and gives an owner/q1 protected path forest.  Its
   missing theorem is the five-role source-occurrence/all-width replacement
   across the deleted role-zero sector.
2. **Fused/shared role-zero collar.**  Replace one spine incidence by a
   shared adjacent-height collar (or by an alternating lift of the minimal
   zero-seam repair ear) so that the role-zero transition is dilated rather
   than retained.  It must preserve the cumulative-union profile and the
   five-head occurrence transport.

Any successful resident PBBS ladder must alter at least one protected edge
in every short-run collar of the form `(e_h,...,e_(2h))`; an architecture
which retains the full direct height spine cannot pass the residence gate.
