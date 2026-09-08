# Independent audit of the phase-clock resident `C8` proposal

**Date:** 2026-08-13  
**Audited source:** `/Users/amir.nuriyev/.codex/attachments/d7e18d83-05f4-45cd-aab5-6616575a9ec5/pasted-text.txt`  
**Verdict:** local dilation **PASS after hypothesis/scope repair**; claimed general automatic host **FAIL**.

## 1. Checks which pass

The construction

\[
 C\cup V_v\cup D_t,
 \qquad D_t=\{u_t,\ldots,u_{t+h-1}\}\subset\mathbb Z_{2h},
\]

has rank `R`.  The displayed ambient inequalities are exactly equivalent
to disjoint placement of `C,X,U`.  Clock moves and lifted base moves are
literal Johnson edges.

Owner simplicity is valid after using the disjoint `X/U/C` coordinate
signatures.  Immediate lower and upper clock tickets have `U`-sizes
`h-1` and `h+1`, while lifted base-edge tickets have `U`-size `h`; this
separates the three families, and base palette simplicity handles the
last family.

The residence argument survives both seams.  The actual clock sequence is

\[
 D_0,\ldots,D_h,D_h,D_{h+1},\ldots,D_{2h},D_0,\ldots,
\]

so the antipodal anchors are repeated.  Every clock coordinate has both
binary runs at least `h` (indeed `h+1` in the paired-block period), and
every base-coordinate run is dilated by `h+1`.

The edge count

\[
                         e_h=(h+1)e_0
\]

is correct.  The estimate `d<=ceil(sqrt(k/2))` follows directly from the
central-binomial lower bound and `Lambda<=2^(k-1)`.

## 2. First exact flaw: host scope

The cited phased-host theorem is a theorem for

\[
 { [2m-1]\choose m-1}\longleftrightarrow{[2m-1]\choose m}.
\]

It cannot be applied to arbitrary `k,R` merely from the two placement
inequalities.  Direct applicability requires `k=2R-1` and `m=R`.

For even `k=2R`, the adjacent central shores have unequal sizes, so a
spanning two-factor of the full incidence graph is impossible.  Thus the
proposal's sentence asserting automatic coinstantiation for every
sufficiently large ambient dimension is false as written.  The local
actuator remains valid, but an even/general host theorem remains open.

## 3. Two proof repairs

First, the displayed exposure bounds with coefficients
`(h+1)alpha_0+8h` and `(h+1)beta_0+8h` were not derived.  The unconditional
safe estimates

\[
                         \alpha_h,\beta_h\le e_h
\]

are enough: a lower vertex cannot see more protected uppers than the
total protected upper count, and an upper cannot see more saturated
protected lowers than the total protected lower count.  For a fixed base
actuator these are `O(h)`, which suffices in the central odd host.

Second, the all-width proof must assume the base identity after retaining
the initial phase and the exact two endpoint cuts (together with base
width).  Under that explicit refined hypothesis, the lift is valid.
The proposal's claimed injectivity of

\[
       (T,\eta)\mapsto C\cup T\cup K_h(\eta)
\]

is unnecessary and need not hold.  Equality for each refined signature
can instead be summed over all signatures producing the same literal
target.

## 4. Proof-safe result

The corrected theorem is frozen in

`MATH_THEOREM_PHASE_CLOCK_DILATION_RESIDENT_ALLWIDTH_LOCAL_AND_CENTRAL_ODD_HOST_20260813.md`.

It proves:

1. local rank, Johnson adjacency, owner/palette simplicity, two-sided
   residence, all-width transparency, and socket-action preservation under
   the explicit refined base-current hypothesis;
2. protected size and exposure `O(h)`;
3. automatic phased-host completion for sufficiently large central odd
   instances `k=2R-1`; and
4. no automatic completion claim for even `k` or a general noncentral
   host.
