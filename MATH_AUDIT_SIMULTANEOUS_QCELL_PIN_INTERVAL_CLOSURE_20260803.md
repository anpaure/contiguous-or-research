# Pure-mathematics audit of simultaneous q-cell interval closure

**Date:** 2026-08-03

**Audited file:**
`MATH_THEOREM_SIMULTANEOUS_QCELL_PIN_INTERVAL_CLOSURE_20260803.md`

**Audited SHA-256:**
`857c75500e4ff0a5e7b231fe739d0961f338256a3bae79eb6f76c3b9539d9b88`

## Verdict

**NO-GO as the current standalone frozen statement; GO after the exact
corrections below.**

The central mathematics is correct.  In particular, there is no
counterexample to the coordinatewise allowed-support factor, the protected
erosion endpoints, the run-local `d+1` obstruction, the integral
assignment formulation, or the bounded-defect corollary.  The current file
nevertheless omits the carrier hypothesis and transition definition on
which those proofs depend: `alpha_i` and `beta_i` are undefined, and an
arbitrary cyclic Johnson walk need not omit every coordinate.  There is also
one ambiguous protected-anchor shortcut and several exact-formulation
qualifications which should be repaired before the theorem is cited as a
standalone result.

This audit is entirely deductive.  No finite enumeration, search, solver,
or remote computation was used.

## 1. Required carrier correction

Lines 11--18 must define the complete carrier and its swap labels.  Replace
their opening by the following hypothesis:

> Let `0<r<k`, put `W=binom(k,r)`, and let
> `T_0,...,T_(W-1)` run through every rank-`r` set exactly once in a cyclic
> Johnson Hamilton carrier.  Define
>
> \[
> T_{i+1}=T_i\setminus\{\alpha_i\}\cup\{\beta_i\},
> \qquad i\in\mathbb Z_W.
> \]
>
> Assume every maximal positive coordinate run has length at least `d+1`.

Without this correction, the collar (0.2) uses undefined symbols.  More
substantively, line 130 is false for a general cyclic Johnson walk: `0<r<k`
alone does not imply that every coordinate is absent from some visited
owner.  Traversal of the complete rank layer does imply it, so every
positive run is then a proper cyclic arc and all coordinate-specific linear
lifts are legitimate.

Line 138 should accordingly say that **the standing minimum-run hypothesis**
gives `t-s+1>=d+1`; it should not appeal to an as-yet unconstructed factor.

## 2. Cyclic erosion geometry: GO after adding the missing proof

For a lifted positive `x`-run `[s,t]`,

\[
x\in E_h
\quad\Longleftrightarrow\quad
[h-d,h]\subseteq[s,t]
\quad\Longleftrightarrow\quad
h\in[s+d,t].
\]

Thus the erosion interval is exactly `R=[s+d,t]`.  If the next positive run
starts at `s'>=t+2`, then the two erosion intervals have at least

\[
(s'-t-1)+d\ge d+1
\]

outside positions between them.  Hence a cell interval of length `q<=d`
cannot meet two erosion intervals.  This remains true across the displayed
cyclic cut because each coordinate may be cut at one of its negative owners.

The non-distributive-looking identity in (0.1) is correct but needs this
coordinatewise proof or a direct citation.  Let

\[
I=[j,j+q-1],\qquad C=[j+q-1-d,j].
\]

For every `h in I`, one has `C subseteq [h-d,h]`.  Therefore
`x in E_h` implies that `x` is present throughout `C`.  Conversely, if `x`
is present throughout `C`, then `C` lies in one positive run `[s,t]`, with

\[
s\le j+q-1-d,qquad t\ge j.
\]

Consequently `s+d<=j+q-1` and `t>=j`, so `[s+d,t]` meets `I`.  Hence `x`
belongs to some `E_h`, `h in I`.  This proves

\[
\bigcup_{h=j}^{j+q-1}E_h
=\bigcap_{i=j+q-1-d}^{j}T_i.
\]

No wraparound exception occurs after taking the coordinate-specific lift.

## 3. Endpoint protection: GO

For a positive run `[s,t]`, the left erosion endpoint is `s+d` and

\[
x=\beta_{s-1}=\beta_{(s+d)-d-1}.
\]

The right erosion endpoint is `t` and `x=alpha_t`.  Every selected cell
containing a source position `h` has both `alpha_h` and `beta_(h-d-1)` in
its mandatory collar.  Therefore a cell whose target omits `x` can contain
neither erosion endpoint.  Lemma 1.2 is exact, including a minimum run,
where the two endpoints coincide, and a run crossing `W-1|0`.

## 4. Greatest allowed-support factor: GO

For any realizing factor define

\[
Z_x=\{h:x\in A_h\}.
\]

Owner exactness gives `Z_x subseteq R_x`; every selected cell omitting `x`
forces `Z_x` to avoid its interval.  Hence every realizer satisfies

\[
Z_x\subseteq U_x,
\]

which proves necessity of every owner and positive-cell hit and proves the
coordinatewise upper bound `A_h subseteq A_h^*`.

Conversely set

\[
A_h^*=\{x:h\in U_x\}.
\]

If `h in [i,i+d]` and `x in E_h`, then `i in [h-d,h]`, so `x in T_i`;
therefore no owner gets an extraneous coordinate.  The owner hits supply all
coordinates that do belong to `T_i`.  For a selected cell, a negative label
removes all of its positions from `U_x`, while a positive label has an
explicit hit, so its union is exactly `S_c`.

Finally `alpha_h in E_h`: its positive run ends at `h` and has length at
least `d+1`.  Any selected cell containing `h` must contain `alpha_h` by its
collar.  Thus `h in U_(alpha_h)` and every `A_h^*` is nonempty.

This proves both sufficiency and coordinatewise greatestness.  The sentence
at lines 278--280 should, however, say only that `A_h^* subseteq E_h`
prevents an **owner** from acquiring an extraneous coordinate.  Selected
cell exactness does not follow from that containment alone; it follows at
lines 286--289 from the definition of `U_x`.

## 5. Run-local owner obstruction: GO

For owner `T_i` inside a positive run `[s,t]`, its complete supplier set is

\[
D_{x,i}=[\max(i,s+d),\min(i+d,t)].
\]

If a failed supplier interval is clipped at the left or right erosion
boundary, it contains respectively `s+d` or `t`, both protected by the
previous section.  A failed supplier interval therefore cannot be clipped;
it must be the full block `[i,i+d]` of exactly `d+1` positions.  Conversely,
any forbidden full block `[h,h+d] subseteq R_x` kills owner `T_h`.

Thus Theorem 3.1 and Corollary 3.2 are exact:

\[
\text{owner failure}
\quad\Longleftrightarrow\quad
F_x\cap R\text{ contains }d+1\text{ consecutive positions}.
\]

There is no shortened boundary obstruction and no cyclic off-by-one case.

## 6. Exact zero-one formulation: GO as an existence projection

For a fixed **integral** assignment `y`, constraints (5.1) force

\[
\operatorname{supp}(z_x)\subseteq U_x(y).
\]

The owner and positive-cell inequalities are precisely the required
interval hits.  Conversely, when all hits exist, the integral greatest
completion

\[
z^*_{x,h}=\mathbf 1_{\{h\in U_x(y)\}}
\]

satisfies every row and produces `A_h^*`.  Hence eliminating `z` for fixed
integral `y` gives exactly Theorem 2.1.

Three qualifications should be made.

1. At line 453 write the cyclic sum explicitly as
   \[
   \sum_{h\in[i,i+d]_W}z_{x,h}\ge1.
   \]
2. Lines 467--469 should say **for fixed integral `y`** and call (5.1)
   projection- or existence-exact.  A nonmaximal feasible `z` can leave a
   source letter empty, although it can always be enlarged to `z^*`.
   Alternatively add the exact rows
   \[
   \sum_x z_{x,h}\ge1\qquad(h\in\mathbb Z_W).
   \]
3. No total-unimodularity or joint LP-integrality conclusion follows.  Once
   `y` is integral, `z`-integrality is actually unnecessary for feasibility,
   because a feasible continuous `z` may be replaced by the integral
   greatest completion.  The relaxed joint `y,z` polytope is not audited or
   claimed integral.

As displayed, (5.1) encodes compilation of every target in the designated
family, hence defect zero for that family.  The exact bounded-defect variant
is

\[
\sum_c y_{S,c}\le1,qquad
M=\sum_{S,c}y_{S,c}\ \text{ maximized},qquad
\delta^*=|\mathcal L|-M^*.
\]

Equivalently, defect at most `C` is the row

\[
\sum_{S,c}y_{S,c}\ge|\mathcal L|-C.
\]

The optimum identity is exact: an assignment of size `M` certifies `M`
distinct targets, while any factor realizing `M` distinct targets can
assign each target to one of its realizing cells; distinct target values
cannot use the same physical cell.

## 7. Protected anchors and bounded defect

The first assertion of Theorem 6.1, with a complete family `Z_x` satisfying
(6.2), is correct.  Its shortcut at lines 508--518 is ambiguous: a bare
owner-net witness could lie inside a negative selected interval and then
cannot be included in `Z_x`.

Replace that shortcut by:

> For every positive cell incidence `(c,x)` and every owner incidence
> `(i,x)`, choose an anchor in its corresponding required interval which
> lies in no selected cell interval whose target omits `x`.  Let `Z_x` be
> the union of all these protected anchors and the mandatory-footprint
> positions.  Anchors may be reused without limit.

Aperture compatibility keeps every mandatory-footprint position out of all
negative intervals.  The corrected anchor family therefore has exactly the
owner net and cell signature required in (6.2).

Corollary 6.2 is then **GO** with its stated conditional scope.  An injection
of `L\D` into distinct cells together with the protected sets produces one
factor realizing every retained target, so at most `|D|<=C` distinct lower
targets remain.  Appending those missing targets literally costs at most
`C` letters and cannot destroy an earlier witness.  This yields the claimed
lower-side bounded defect only inside the stated upper-complete/terminal-
repair context; it does not itself prove `B(k)+O(1)`.

For complete formality in Corollary 6.3, “supported on `B_a`” should mean
that every selected cell interval and every modified source position of the
local factor is contained in `B_a`.  Under that meaning, its separated-block
proof is valid.

## 8. Final audited status

The corrected theorem has the following proof-safe status.

- cyclic erosion identity and run separation: **GO**;
- collar protection of both erosion endpoints: **GO**;
- necessity and sufficiency of the coordinatewise greatest factor: **GO**;
- exact run-local `d+1` obstruction: **GO**;
- zero-one system: **GO for integral-assignment feasibility/projection**;
- protected-transversal bounded-defect corollary: **GO after protecting the
  owner anchors explicitly**;
- construction of the complete carrier, the protected assignment, upper
  coverage, or an unconditional `B(k)+O(1)` theorem: **not claimed**.

Accordingly the present SHA is a **NO-GO for standalone citation**, but the
mathematical interval-closure theorem is a **GO after the listed textual and
hypothesis corrections**.
