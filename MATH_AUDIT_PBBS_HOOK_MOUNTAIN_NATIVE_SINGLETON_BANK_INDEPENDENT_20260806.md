# Independent audit of the native PBBS hook singleton bank

**Date:** 2026-08-06  
**Audited theorem:**
`MATH_THEOREM_PBBS_HOOK_MOUNTAIN_NATIVE_SINGLETON_BANK_20260806.md`  
**Audited theorem SHA-256:**
`450f2d130355517fac18bef105d68ccd4f6c46bd21298e910c1ca0c816f58481`  
**Method:** symbolic audit against the exact action--angle, mountain
renewal, centered-factor, mandatory-core, source-factorization, and
long-deck identities; no finite search or computation  
**Verdict:** **PASS WITH TWO REQUIRED SCOPE/PROOF CORRECTIONS.**  The
native complete singleton bank is valid.  The two corrections do not
change its conclusion: Section 2 must explicitly exclude an early winding
return on the one-pile orbit, and “q1/upper preservation” must be read as
owner-row preservation, not preservation of an independently preassigned
short-source compiler.

## 1. Authoritative dependencies checked

The audit used the following exact statements.

1. Hook action--angle matrix and full-torus cycle:
   `MATH_THEOREM_PBBS_SOLITON_GAP_FORCES_EXPONENTIALLY_MANY_SELECTED_CYCLES_20260805.md`,
   SHA-256
   `837e14d9c07abf124fa976f2d4435a7d2fba66affcce103939eb96b64aa3fb68`.
2. Literal hook angle rotation under the centered successor:
   `MATH_THEOREM_PBBS_HOOK_LEAF_PLUCKING_ADJACENT_TRANSFER_20260805.md`,
   SHA-256
   `197f4b2e447319e37a11fbfeea51d5bb9e66ed56fdce857c2605f772bdc382b1`.
3. Exact mountain predecessor itinerary and zero-terminal return:
   `MATH_THEOREM_PBBS_ST_EXACT_ADDITIVE_RENEWAL_AND_TWO_TIME_CENSUS_20260726.md`,
   SHA-256
   `00ce3982c53d9651d9614e3dd05291d03eec01a1210f1715940f8e14183a5e9b`.
4. All-winding mountain endpoint ledger:
   `MATH_THEOREM_N_ST_MOUNTAIN_POSITIVE_WINDING_RENEWAL_AND_SHORT_CYCLE_NOGO_20260726.md`,
   SHA-256
   `830344eaa282c4c88f25b156cbb6d1e388380dbbdad8d57898c99384d7562c95`.
5. Mandatory-core short-gap localization:
   `MATH_THEOREM_PBBS_SHORT_GAP_MANDATORY_CORE_LOCALIZATION_AND_BLOCK_TEMPLATE_20260805.md`,
   SHA-256
   `0816f8e85dd67a48b29dc793600fcb99ed3df95bb398d8f1af6093ee28cafcfe`.
6. Maximal-antecedent source identity:
   `MATH_THEOREM_PBBS_MAXIMAL_ANTECEDENT_INTERSECTION_SOURCE_ROW_IDENTITY_20260805.md`,
   SHA-256
   `828d5047c5f714a387e2eb30eb24ae03f5e259a3e6caa9b2d2911b5fa4928360`.
7. Long source-deck rigidity:
   `MATH_THEOREM_COMPLEMENT_PAIRED_BACKUP_AND_PAYLOAD_UPPER_BRIDGE_20260806.md`,
   SHA-256
   `23fc0e2b262dd2b3b5c55a13fa6166ec8539dd6ff6db7cd4c8e1caad1b8f7b9c`.

The theorem's own dependency list should add items 4, 6, and 7, or give
their short direct proofs.  Item 4 is essential for making the global
residence sentence proof-complete.

## 2. Action--angle and component audit

Put

\[
 n=2m+1,\qquad p=2h-1,\qquad b=m-h>0.
\]

The hook angle `eta=(0,b,0,...,0)` has exact cyclic period `p`: a nonzero
one-pile composition cannot be fixed by a proper nonidentity rotation.
Thus its symmetry parameter is `gamma=1`.

For

\[
 F=\begin{pmatrix}n-2&2\\2b&2h+1\end{pmatrix},\qquad
 v=\binom1h,\qquad s=\binom11,
\]

the exact ledgers are

\[
 \det F=(n-2)(2h+1)-4b=n(2h-1)=np,
\]

and

\[
 \det\begin{pmatrix}1&2\\h&2h+1\end{pmatrix}=1.
\]

Hence the centered PBBS translation generates the entire hook torus; it
is one centered-factor component of length `np`.  Moreover

\[
 pv-s
 =\binom{2h-2}{hp-1}
 =\binom{2h-2}{(2h+1)(h-1)}
 =F\binom0{h-1}.
\]

Therefore the torus relation is exactly

\[
                         \tau^p=\rho
\]

up to the globally chosen orientation of `rho`.  This verifies both
component membership and the exact factor-time spacing `p` of coordinate
rotations.  It is stronger than the weaker statement that the component
is merely rotation invariant.

## 3. Exact correction to the minimum-return argument

The zero-terminal theorem alone proves

\[
                         g_0=p+2=2h+1,
\]

but does not by itself justify the sentence that arbitrary positive
terminal occupancy can only delay the *first physical* return: when the
prospective nonwrapping return passes the circumference, an early winding
return must also be excluded.

For the one-pile orbit this exclusion is exact.  Every component phase has
angle `rot^u eta`; hence its terminal occupancy is either `0` or `b`.  Let
`s<h` be a proposed centered-factor return duration.  In the mountain
endpoint notation write

\[
 R_s=\sum_{j=0}^{s-1}\mathfrak d(\tau^j\eta)
       -\delta(\tau^s\eta),
 \qquad \mathfrak d(\eta)=1+2\eta_0.
\]

Because `s<h<p`, the moving terminal slot meets the unique pile at most
once.  Therefore

\[
 0<\sum_{j=0}^{s-1}\mathfrak d(\tau^j\eta)
    \le s+2b\le h-1+2b<n,
\]

while `1<=delta<n`.  Consequently

\[
                         -n<R_s<n.
\]

If a physical return occurred, the exact endpoint ledger would require
`R_s` to be a multiple of `n`; it would therefore have to be zero.  Such a
return would be nonwrapping.  The exact terminal-spacing/no-overtaking
ledger puts the first possible returned-edge predecessor closure at the
`(2z+2)`-nd predecessor selection, whose centered duration is

\[
                         h+zp\ge h
\]

for terminal occupancy `z`.  Thus no return has duration below `h`.
For `z=0`, duration `h` occurs and has odd omitted-label gap `2h+1`.

This proves the theorem's intended statement:

* every positive coordinate run on this component has length at least
  `h`;
* every zero-terminal phase starts an exact length-`h` run.

The theorem should replace its two informal “can only delay” sentences by
this one-pile winding audit, or cite it as a lemma.  With that correction,
taking `h=d+1` makes the entire selected component cyclically depth-`d`
resident.

## 4. Rotation bank and occurrence distinctness

Choose a zero-terminal phase `D` with omitted coordinate `x_0`.  The
relations

\[
 \tau^{jp}D=\rho^jD,\qquad x_j=\rho^jx_0,
 \qquad 0\le j<n,
\]

retain the same one-pile angle and zero terminal occupancy.  Thus they
give an exact length-`d+1` run for every coordinate.

The `n` phases are distinct.  If a nonidentity rotation fixed a rank-`m`
owner, each rotation orbit in its support would have a common length
`ell>1`, with `ell|n` and `ell|m`.  This contradicts
`gcd(m,2m+1)=1`.  Their omitted labels are likewise all distinct, because
the `rho`-orbit of a coordinate has length `n`.

Passing from each run start to its eroded singleton-source position adds
the same offset `d`; hence these source positions still have exact cyclic
spacing

\[
                         p=2d+1>d.
\]

They are therefore pairwise distinct singleton free intervals, including
across the cyclic wrap.

## 5. Source factorization and literal singleton values

For the resident simple Johnson owner trace define

\[
 P_t=\bigcap_{a=0}^{d}T_{t-a}.
\]

An exact owner run `[u,u+d]` of coordinate `x` has eroded support
`{u+d}`.  At that position the eroded-run beginning and ending labels are
both `x`.  Simplicity of the Johnson trace prevents any second insertion
or deletion label at those same transitions.  Hence the complete
mandatory core is exactly

\[
                         F_{u+d}=\{x\}.
\]

Let `R` be the `n` selected eroded positions and replace `P_t` by `{x}`
at the position assigned to `x`, retaining `P_t` elsewhere.  The maximal
cyclic components of `R` are isolated points, each of length one at most
`d`, and every mandatory core is retained.  The short-gap localization
theorem therefore applies simultaneously and gives

\[
                         D^dA=T.
\]

Thus all `n` literal singleton cells coexist in one antecedent; this is
not merely a collection of alternative rotations.

## 6. q1, component, and upper-deck preservation

The labelled owner chronology `T` is unchanged.  It follows pointwise
that

* every owner vertex is unchanged;
* every owner Johnson edge is unchanged;
* every immediate lower colour `T_i cap T_(i+1)` is unchanged;
* every immediate upper colour `T_i cup T_(i+1)` is unchanged; and
* the directed PBBS component and its topology are unchanged.

For every proper owner interval, long-deck rigidity gives

\[
 \bigcup_{i=a}^{b}T_i
 =\bigcup_{t=a}^{b+d}A_t.
\]

Equivalently, two antecedents with the same labelled derivative have the
same corresponding source-interval OR values at every width at least
`d+1`.  Hence every arbitrary-width upper witness supplied by this owner
component survives literally.

The required semantic correction is that this does **not** preserve an
independently fixed short-source occurrence matching.  Shrinking `P_t` can
erase lower values assigned to intervals meeting the selected positions.
Accordingly, “q1 is unchanged” means the owner-edge lower/upper palettes,
not every previously chosen source-compiler occurrence.  The original
theorem's scope exclusion 4 already records this distinction and should be
kept.

## 7. Final proof-safe scope

The following conclusion passes independently:

> For `2<=d+1<m`, one untouched canonical PBBS hook component admits a
> depth-`d` antecedent with one pairwise occurrence-disjoint literal
> singleton cell for every one of the `n=2m+1` coordinates, while leaving
> its owner chronology, owner q1 palettes, component topology, and complete
> owner-derived upper OR deck unchanged.

This is a component-local native singleton bank.  It does not prove
residence on the other PBBS components, preservation of a preassigned
short-source compiler, nonsingleton low-target payloads, component gluing,
or the global `B(k)+O(1)` theorem.
