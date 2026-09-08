# Outer moving frames: the false rounding theorem and the minimal exact successor

Date: 2026-07-26

## 0. Verdict

The two source notes are consistent and together settle the status-cell
rounding question.

1. The full moving-frame catalogue has an exact simultaneous all-depth
   **fractional** cover.  Averaging whole legal options over `S_(2m)` gives
   uniform target load at every signed depth.
2. Disaggregating a frame into edge marginals and rounding by a network/TU
   argument is invalid: the perfect-matching degree matrix contains the
   determinant-two triangle minor and needs all odd-set blossom rows.
3. Adding blossoms, or averaging whole perfect matchings from the outset,
   does not repair the target problem.  In the complete status-cell atlas
   the owner overlap is connected, so every integral point chooses one
   global frame.  Every such point has a linear Gaussian target deficit,
   while the fractional deficit is zero.

Therefore the proposed “remaining rounding theorem” is **false**, not
merely unproved.  There is no rounding of the symmetric master point to a
status-cell integral option with `o(W)` target loss.

Scope correction (2026-07-26): the status-component theorem does not
classify arbitrary owner-disjoint subcube packets selected from several
frames.  Such packet mosaics are another integral architecture outside the
column model; the exact J(4,2) example and its valid-dimensional tensor lift
are recorded in
MATH_AUDIT_ARBITRARY_MULTIFRAME_SUBCUBE_HYPERMATCHING_ESCAPE_20260726.md.
Thus the exterior-moving strip statement below is one clean sufficient
successor, not the unique or minimal successor.  A floor-balanced multiframe
packet hypermatching is a second exact successor.

The exterior-moving formulation is an exact factor of cyclic strips whose
individual cycles may change ambient frame (or move through exterior
coordinates) and whose aggregate central target holes are o(W).  This
assertion, stated precisely below as EMSF, plus the verified local trace
compiler, implies constant one directly.  It contains no fractional mixture
and no subsequent rounding step.

Existence of `EMSF` is open.  The reduction from it to constant one is
proved here.

## 1. What the symmetric fractional theorem really proves

Let `A_stat` be the catalogue of whole legal fixed-frame status-cell
options.  A column includes one perfect matching, all connected
three-shore resolutions, one common all-depth local factor choice, and its
literal signed trace occurrences.  It is not an individual matching edge
or one associator cell.

Take one legal base option with certified occurrences on `G=W-L` middle
owners and all its coordinate conjugates.  If conjugates are normalized to
give every middle owner load one, transitivity gives every rank-`m+-q`
target load `W/N_q`.  Equivalently, after quarantined owners are retained
as zero-occurrence singleton columns, the uniform orbit of whole exact
options gives load `G/N_q`.  Since

\[
 N_q\le N_1={m\over m+1}W,
 \qquad L<{W\over m+1},                                      \tag{1.1}
\]

one has `G/N_q>1` at every positive depth.  The same orbit coefficient is
used at every sign and depth.

For arbitrary joint target weights `y`, averaging one common conjugate
therefore gives

\[
 \max_{o\in S_{2m}o_0}
 \sum_{q,\epsilon,T\in I_{o,q}^\epsilon}y_{q,T}^\epsilon
 \ge
 \sum_{q,\epsilon}{G\over N_q}\sum_Ty_{q,T}^\epsilon
 \ge\sum_{q,\epsilon,T}y_{q,T}^\epsilon.                       \tag{1.2}
\]

Thus the exact joint fractional Hall dual is zero.  This conclusion is
stronger than every fixed suffix, pair-type, or occupancy-profile
fractional check.

It says only that the desired target vector belongs to the **convex hull**
of whole global options.  It does not say that the hull contains a suitable
vertex.

## 2. Two distinct integrality failures

### 2.1 The edge-marginal relaxation is false

If a global frame is replaced by edge variables `y_e` satisfying only

\[
                         \sum_{e\ni v}y_e=1,                     \tag{2.1}
\]

then the constraint matrix contains

\[
 \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},
 \qquad |\det|=2.                                               \tag{2.2}
\]

On two disjoint triangles, weight `1/2` on every triangle edge satisfies
(2.1) but is not a convex combination of perfect matchings.  It violates

\[
                         y(E(U))\le{|U|-1\over2}
 \qquad(|U|\text{ odd}).                                      \tag{2.3}
\]

Hence no network/TU proof can round profile flow without blossom rows.

### 2.2 Whole-matching target rounding is also false

Blossoms are not the real remaining gate.  In the catalogue of all
quartet-related frames, the union of the coordinate matchings is
`K_(2m)`.  By the exclusion-component theorem, the entire middle layer is
one common-owner component.  An integral component choice therefore
selects one whole global fixed-frame option.

For every such option, at `q=floor(A sqrt m)` the fixed-frame pair-type
cut gives

\[
 M_q^-\ge(\delta_A-o(1))W,
 \qquad
 M_q^+\ge(\delta_A-o(1))W,                                   \tag{2.4}
\]

where

\[
 \delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.                    \tag{2.5}
\]

Combining (1.2) and (2.4) yields the literal integrality gap

\[
 \boxed{
 \eta_H^{\rm frac}=0,
 \qquad
 \eta_H^{\rm int}\ge(2\delta_A-o(1))W.}                      \tag{2.6}
\]

### Theorem 2.1 (no status-cell rounding theorem)

There is no map which takes every feasible symmetric fractional master
point in the complete status-cell catalogue to an integral catalogue
option while increasing aggregate protected target deficit by `o(W)`.

#### Proof

Apply such a map to the point in (1.2).  Its input deficit is zero, so its
output deficit would be `o(W)`, contradicting (2.6). \(\square\)

This proof already works with whole matching columns, hence with every
blossom inequality.  The determinant-two minor diagnoses why the proposed
profile network was too weak; the linear gap proves that even the corrected
matching polytope is the wrong integral architecture.

## 3. Exterior-moving strip factors

Let

\[
                         W_m=\binom{2m}m,
 \qquad N_{m,q}=\binom{2m}{m-q}.                              \tag{3.1}
\]

A cyclic `h`-strip is a family of middle owners

\[
 X_t=K\cup I_z(t,h),qquad t\in\mathbb Z/(2h),                 \tag{3.2}
\]

where `|K|=m-h` and `z_0,...,z_(2h-1)` are distinct.  Its signed targets
are

\[
 L_t^q=K\cup I_z(t+q,h-q),qquad
 U_t^q=K\cup I_z(t,h+q).                                      \tag{3.3}
\]

The word *exterior-moving* concerns the construction certificate, not a
new target definition.  Along one strip, the local compiler may change its
ambient perfect matching, associator shore, or packet frame with `t`; the
final owner sequence (3.2) and literal targets (3.3) are what matter.  In
particular the strip is not required to lie in one status cell of one
global matching.

For a strip family `F`, define the missing signed targets

\[
\begin{aligned}
 M_q^-(F)&=\#\{T\in\tbinom{[2m]}{m-q}:
                    T\ne L_t^q(C)\ \forall C,t\},\\
 M_q^+(F)&=\#\{T\in\tbinom{[2m]}{m+q}:
                    T\ne U_t^q(C)\ \forall C,t\}.              \tag{3.4}
\end{aligned}
\]

### `EMSF` — exterior-moving strip-factor theorem (open)

There exist integers `H_m<h_m<m`, integral families of main strips
`F_m`, and residual middle-owner sets `R_m` such that

1. the main strips are owner-disjoint and, together with the singleton
   owners in `R_m`, partition the entire middle layer exactly;
2. every strip `C` has length `2h_C` with `h_C>=h_m` and is supplied by
   the verified local trace compiler, allowing certified frame changes
   inside the strip;
3. 
   \[
   {H_m\over\sqrt m}\longrightarrow\infty,
   \qquad {H_m\over h_m}\longrightarrow0,
   \qquad |R_m|=o(W_m);                                        \tag{3.5}
   \]
4. the aggregate literal central deficit satisfies
   \[
   \boxed{
   \sum_{q=1}^{H_m}\bigl(M_q^-(F_m)+M_q^+(F_m)\bigr)=o(W_m).}  \tag{3.6}
   \]

The phrase “supplied by the compiler” means that every declared frame
change is part of one integral whole-cycle certificate.  It does not mean
that different frame columns are fractionally averaged and rounded later.

Variable strip lengths and singleton residual owners remove the irrelevant
divisibility requirement `2h_m | W_m`.  The owner partition remains exact.

Condition (3.6) is the minimal quantitative conclusion needed by the
central-word endgame.  Balanced overload, quasirandomness, a prescribed
frame distribution, or a TU representation are possible sufficient tools,
not additional requirements of `EMSF`.

## 4. `EMSF` implies constant one

### Theorem 4.1 (exact successor reduction)

Assume `EMSF`.  Then

\[
 \nu(2m)=(1+o(1))\binom{2m}m,
 \qquad
 \nu(2m+1)=(1+o(1))\binom{2m+1}m.                              \tag{4.1}
\]

#### Proof

For one main strip `C` define letters

\[
 A_t=\bigcap_{j=0}^{H_m}X_{t+j}
     =K\cup I_z(t+H_m,h_C-H_m).                                \tag{4.2}
\]

The linear block

\[
 A_0,\ldots,A_{2h_C-1},A_0,\ldots,A_{2H_m-1}                  \tag{4.3}
\]

has length `2h_C+2H_m`, and its contiguous unions realize every target
(3.3) of that strip for all `q<=H_m`.  This follows from

\[
 \bigcup_{s=0}^{r}A_{t+s}
 =K\cup I_z(t+H_m,h_C-H_m+r),\qquad0\le r\le2H_m.               \tag{4.4}
\]

Let `K_m=|F_m|`.  The main strips cover `W_m-|R_m|` owners and each has at
least `2h_m` owners, so

\[
 K_m\le {W_m-|R_m|\over2h_m}.
\]

Concatenating (4.3) over all main strips and appending every residual middle
owner as a singleton costs

\[
 \sum_C(2h_C+2H_m)+|R_m|
 =W_m+2H_mK_m
 \le W_m+{H_m\over h_m}W_m
 =W_m+o(W_m).                                                   \tag{4.5}
\]

Append every positive-depth target missing from the strip images in the
central band as one literal singleton letter.  By (3.6) this costs
`o(W_m)`.  The rank-`m` residual targets were already paid in (4.5).

The product-SCD tail word covers all ranks outside the central band with
length

\[
 O\left(W_m\exp\left[-{H_m^2\over8m}\right]\right)=o(W_m),     \tag{4.6}
\]

using `H_m/sqrt m -> infinity`.  Concatenation cannot destroy any witness.
Thus the even universal word has length `(1+o(1))W_m`.

The exact odd lift in the product-SCD endgame doubles the even construction
with only `o(W(2m+1))` additional boundary cost, giving the odd assertion.
The reverse inequalities are Sperner's bound: witnesses for distinct sets
in a largest layer require distinct right endpoints. \(\square\)

This proof uses neither (1.2) nor an integral rounding of it.  It consumes
one integral strip factor already satisfying (3.6).

## 5. Necessary mobility of any `EMSF` construction

The existing cuts give two immediate audits of a proposed construction.

### Proposition 5.1 (no asymptotically fixed frame)

Fix `A>0` and `q=floor(A sqrt m)`.  If all but `o(W)` phase occurrences of
a proposed factor remain inside status cells of one perfect matching `M`,
then

\[
                         M_q^-+M_q^+\ge(2\delta_A-o(1))W.       \tag{5.1}
\]

Hence `EMSF` must contain `Omega(W)` genuinely frame-changing occurrences
at every protected Gaussian scale.

#### Proof

Apply the fixed-frame pair-type cut to the normal occurrences.  Exceptional
occurrences can fill at most one target per sign and therefore change the
two-sign deficit by at most `2o(W)`. \(\square\)

### Proposition 5.2 (no asymptotically frozen exterior)

If a positive-density coordinate set `R` is untouched by all but `o(W)`
phase occurrences at the same depth, the suffix histogram dual gives

\[
                         M_q^-+M_q^+=\Omega_A(W).                 \tag{5.2}
\]

Thus a valid factor must also move `Omega(W)` occurrences across every
macroscopic suffix cut exposed by its packet atlas.

These are necessary conditions, not a construction.  They explain the
term exterior-moving: adding more frames to a convex catalogue is useless
unless individual integral cycles physically traverse the cuts which
separate every fixed-frame option.

## 6. Exact frontier

### Proved

* simultaneous symmetric fractional cover by whole moving-frame options;
* blossom obstruction to edge-marginal/TU rounding;
* linear target integrality gap even after whole matching/blossom legality;
* impossibility of any `o(W)`-loss status-cell rounding theorem;
* the direct implication `EMSF => constant one`.

### Open

Construct the integral exterior-moving strip factor in `EMSF`, or refute
it by a statewise invariant which applies to cycles that change frame
internally.  Fractional frame averaging cannot decide this existence
question.
