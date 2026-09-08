# Independent audit of the synchronized-collar planting decision

**Date:** 2026-08-13  
**Audited file:**
`MATH_THEOREM_PBBS_SYNCHRONIZED_COLLAR_PLANTING_DECISION_AND_EXACT_SOURCE_HOST_QUANTIFIER_20260813.md`  
**Audited SHA256:**
`5624a8b95e5f380b9d18fc44099289b43c75ccd91027dab84866c1f930bf8918`  
**Verdict:** **PASS after one source-chronology scope correction incorporated
in the audited bytes.**  The all-five independent collar bank has a forced
degree-three endpoint.  The endpoint-corrected bank has a valid simple
directed graph host with its named upper backups, but retains a forced
length-four positive run and is not a growing-depth resident source host.
The pinned-erosion theorem is an exact componentwise source criterion; it
does not fuse the unprotected completion cycles into one source word.

## 1. Endpoint obstruction and corrected graph face

The literal adjacent-height identity

\[
                         P_{h,0}=Q_{h-1,1}=U_h
\]

is the unique high-height tail/head overlap.  After the head shifts, the
role-zero edges form the path `...-U_(h-1)-U_h-U_(h+1)-...`; these already
use both protected degrees at an internal `U_h`.  An independent incoming
role-zero collar has a first interior owner missing its private tag, so its
endpoint edge is distinct from both spine edges.  The degree-three no-go is
therefore literal and cannot be repaired by halo packing or Ore extension.

Omitting that incoming collar and placing one outgoing collar after the
free head `Q_(h,0)` removes the only endpoint collision.  Private
missing-tag signatures separate all collar interiors.  Enlarging the tag
reservoir before choosing deletion sets supplies one-tag endpoint whiskers;
pair-tag geodesics join all pre-oriented forced components into one path.
The rank-stratified backup paths are selected afterward as unoriented paths,
so they impose no conflicting orientation on the completed factor cycle.

The quoted size and exposure orders are preserved:

\[
 e=R^{O(1)},\qquad \alpha,\beta\le R/3.
\]

The backup-packing proof is quantifier-safe.  At rank excess `s`, a random
canonical owner path has collision probability tending uniformly to zero;
conditioning on avoidance changes star-hit probabilities by `1+o(1)`.
The exponential-moment bound at threshold `R/8`, followed by a union bound
over fewer than `2^(2R+1)` stars, yields positive probability of sub-half
exposure.  The polynomial protected-forest theorem then applies.  It gives
a simple directed two-factor, not a source antecedent.

## 2. Exact pinned-erosion equivalence

For an oriented owner trace `T`, source width `q`, and envelopes

\[
                         K_j=\bigcap_{a=0}^{q-1}T_{j-a},
\]

any source letter at position `j` is necessarily contained in `K_j`.
After exact pins `W_j` are installed, coordinate `x` is emitted at precisely
the allowed safe positions

\[
                         E_x\setminus Z_x.
\]

Thus every positive owner incidence is covered exactly when

\[
 [i,i+q-1]\cap(E_x\setminus Z_x)\ne\varnothing
 \qquad(x\in T_i).
\]

Together with pin containment and nonempty unpinned envelopes, these
conditions are both necessary and sufficient: choosing each unpinned
letter to be its full envelope introduces no forbidden coordinate and the
coverage condition supplies every required one.  The proof handles exact
pins rather than merely upper bounds on letters.

The invocation of separated-short-block freedom is also correctly scoped.
Blocks of length at most `q-1`, lying between their forced sets and maximal
envelopes and separated by an unaltered maximal position, cannot join two
erosion gaps into one gap longer than `q`.  A complete pentagon fragment has
length `q+1`; the note correctly leaves it to a decomposition or a direct
full-halo check.

One correction was required during audit.  The criterion applied to a
multi-cycle two-factor gives a componentwise antecedent.  The final source
now says exactly that the protected factor cycle carries the pins, while a
single global cyclic source chronology still requires common-history fusion
of the unprotected cycles.  No automatic global fusion remains in the
audited SHA.

## 3. Independent residence no-go

Write

\[
 A_t=0\,1^t0^t(10)^{r-t},\qquad U_t=A_t^c,
\]

and let `x_h=2h+1`.  Direct membership gives

\[
 x_h\notin U_h,qquad
 x_h\in U_t\ (h+1\le t\le2h),\qquad
 x_h\notin U_{2h+1}.
\]

Indeed `x_h` is in the alternating-one tail of `A_h`, in the zero block
`[t+1,2t]` for `h+1<=t<=2h`, and in the initial one block of `A_(2h+1)`.
Hence the protected edge `e_h` inserts `x_h`, `e_(2h)` deletes it, and its
maximal positive run is

\[
                         U_{h+1},\ldots,U_{2h}
\]

of length exactly `h`.  The range `2h<H` is exactly what retains both
boundary edges.  If `4<=h<=d`, then `h<d+1=q`, so no width-`q` antecedent
exists.  In particular `d>=4,H>=9` fails at `h=4`.  Long arms, pin spacing,
and cap routing are downstream and cannot change this protected membership
trace.

## 4. Exact boundary

The audited decision is therefore:

\[
\boxed{
\begin{array}{c}
\text{all-five independent collars: blocked by protected degree three;}\\
\text{endpoint-corrected collars: graph-hostable but nonresident;}\\
\text{pinned erosion: exact only after a resident owner trace is built.}
\end{array}}
\]

A successful resident ladder must delete or dilate the direct height-spine
edges.  Once such an owner trace exists, the pinned-erosion test remains the
correct exact source criterion, followed separately by global
common-history fusion and the occurrence-typed suffix router.

