# Audit of the clock-dilated common-mate `C8`: refined current, terminal halo, and host scope

**Date:** 2026-08-13  
**Audited source:** `/Users/amir.nuriyev/.codex/attachments/92d98fcf-75a1-4de4-8d0b-3216490f0909/pasted-text.txt`  
**Source SHA-256:** `d1d1432d1c31c01103a90aa21daf7f2d6d6927b497b97ddf5075772c04f3f94f`  
**Scope:** Theorem 2 and its claimed consequences only.  
**Verdict:** the displayed internal owner paths, local Johnson/palette
algebra, edge counts, and inherited odd socket action pass.  The claimed
closed resident all-width actuator and automatic all-dimensional host do
not follow as written.  They become a proof-safe conditional theorem after
adding an exact ground-set inequality, a phase-and-endpoint-refined base
current, an explicit lifted terminal closure, and the central-odd host
condition `k=2R-1`.

## 1. Internal construction which passes

Write `X` for the coordinate support of the base owners and put `|X|=a`.
Assume each base owner `U_i` has rank `rho`.  Let

\[
 Z_j=\{z_j,z_{j+1},\ldots,z_{j+q-1}\}
       \subseteq\mathbb Z_{2q}.                       \tag{1.1}
\]

The even lifted block is

\[
 F+U_i+a+Z_0,\ldots,F+U_i+a+Z_q,
 F+U_i+b+Z_q,\ldots,F+U_i+b+Z_0,                     \tag{1.2}
\]

and the odd block interchanges `a,b`.  It contains `2q+2` owners and
`2q+1` internal edges.

If

\[
                         |F|=R-\rho-q-1,              \tag{1.3}
\]

then every lifted owner has rank `R`.  A clock edge exchanges
`z_j` for `z_(j+q)`, the midpoint exchanges `a,b`, and a local matching
edge exchanges the one base coordinate of a base Johnson edge.  Hence all
displayed edges are Johnson edges.

The owner is identified by `(U_i,tag,Z_j)`, with the only repeated clock
states carrying different tags.  Thus internal owner simplicity passes.

The immediate-ticket support profiles, after removing the common `F`, are

\[
\begin{array}{c|c|c}
&\text{lower}&\text{upper}\\ \hline
\text{clock}&(\rho,1,q-1)&(\rho,1,q+1)\\
\text{tag}&(\rho,0,q)&(\rho,2,q)\\
\text{base matching}&(\rho-1,1,q)&(\rho+1,1,q).
\end{array}                                           \tag{1.4}
\]

The profiles separate edge types.  Proper cyclic clock intervals and the
base immediate-palette simplicity separate tickets within a type.  The
internal immediate palettes therefore pass.

The exact internal counts also pass:

\[
                         8(2q+2)=16q+16               \tag{1.5}
\]

owners and

\[
                         8(2q+1)+4=16q+12             \tag{1.6}
\]

edges before adding an exterior closure.

## 2. Exact ground-set conditions

The source says only “for all sufficiently large `k`.”  The actual
conditions for the displayed disjoint-coordinate lift are

\[
                    R\ge\rho+q+1,
 \qquad k-R\ge a-\rho+q+1.                            \tag{2.1}
\]

The first makes `F` nonnegative.  The second follows from

\[
 |F\sqcup X\sqcup\{a,b\}\sqcup Z|
     =R+(a-\rho)+q+1\le k.                            \tag{2.2}
\]

These inequalities are automatic only after specifying how the base
`C8` rank and support grow relative to `(k,R)`.  “Sufficiently large” by
itself is not a substitute for (2.1).

## 3. First substantive gap: the terminal closure is not constructed

Inside one block, the clock-state trace is

\[
                         Z_0,\ldots,Z_q,Z_q,\ldots,Z_0.          \tag{3.1}
\]

This gives each clock coordinate long internal positive and zero
segments.  Local matching edges join two endpoints with the same state
`Z_0` and therefore do not shorten them.

The other endpoint of every block is declared external.  The source says
that a proof closure supplies the ray

\[
                         Z_1,Z_2,\ldots,Z_{q-1}        \tag{3.2}
\]

and that inherited terminal paths replace those rays.  No lifted terminal
owners, Johnson edges, or endpoint identifications realizing this
replacement are given.  An arbitrary inherited path need not carry the
new clock labels in the order (3.2), or even keep the same clock state.
Consequently internal residence does not prove residence on the actual
closed factor component.

A proof-safe closure may instead lift every exterior base owner by the
constant set

\[
                         F\cup\{a\}\cup Z_0,           \tag{3.3}
\]

and require exterior base edges to remain Johnson edges.  The constant
clock state joins the boundary pieces: coordinates of `Z_0` stay positive
and coordinates of `Z-Z_0` stay zero along the exterior.  This is exactly
the complementary-arc halo condition in
`MATH_THEOREM_COMPLEMENTARY_CLOCK_ADJACENT_SWAP_AND_CANONICAL_APERTURE_LIFT_20260813.md`.
Any different closure must be audited coordinate by coordinate.

The guard owners and edges belong to the protected bank.  Hence (1.5)--
(1.6) are only **internal** counts.  They cannot simultaneously be the
complete host parameter `e_m` unless the closure has been included.

## 4. The all-width proof is not valid at every physical width

The sentence

> a contiguous interval either lies entirely in one block or crosses one
> local matching edge

is false on a closed actuator.  An interval may cross an exterior return,
or traverse several lifted blocks and several switched local edges.
Equation (6.9) of the source audits only intervals meeting one local edge
with endpoints in its two adjacent blocks.

The base equality of the multisets `U_i union U_j` is likewise only the
one-edge/width-two row.  It cannot by itself lift to all physical widths.

The exact sufficient hypothesis is the refined identity used in
`MATH_THEOREM_PHASE_CLOCK_DILATION_RESIDENT_ALLWIDTH_LOCAL_AND_CENTRAL_ODD_HOST_20260813.md`:
the two base closures must have equal current after retaining

\[
 (\text{base width},\text{initial phase},
   \text{first endpoint cut},\text{last endpoint cut}).          \tag{4.1}
\]

The lifted exterior closure must use the same retained signature.  Then
every lifted interval has the form

\[
 F\cup\operatorname{OR}_X(I_{\rm base})
       \cup K_q(\text{phase and endpoint cuts}),       \tag{4.2}
\]

and equality follows by summing over signatures producing a fixed literal
target.  No injectivity of the signature-to-clock-union map is necessary.

The full-clock identity

\[
                         Z_j\cup\cdots\cup Z_{j+q}=Z   \tag{4.3}
\]

is useful shielding, but it does not repair unmatched base/exterior
unions.  Thus the source's all-width conclusion is conditional on (4.1),
not proved merely by (6.9)--(6.10).

## 5. Residence and literal aperture after repair

With a closure satisfying Section 3, every clock coordinate has positive
and zero runs at least `q`.  The tags `a,b` have phases of `q+1` owners
inside a block and join coherently across the declared endpoint types.
Each base-coordinate bit is repeated through a block of `2q+2` owners; a
base one- or zero-run therefore only lengthens.  This gives two-sided
threshold-`q` residence, provided the base closure itself has no
uncontrolled external occurrence of the added clock or tag labels.

The phrase “aperture at least `q+1`” in the source is not justified by

\[
                         \rho+q+1.                    \tag{5.1}
\]

That number is the rank contribution outside `F`, not the number of source
letters per owner.  Once a closed positive-resident Johnson owner cycle is
constructed, its literal aperture-`q` source is the canonical erosion

\[
                         A_j=\bigcap_{t=0}^{q-1}O_{j-t}.          \tag{5.2}
\]

Lemma 1.1 of the complementary-clock note proves that its `q`-window
unions are exactly the owners and that all immediate and wider owner-union
identities are literal.  This is the proof-safe aperture statement.

## 6. Odd socket action passes conditionally

Even blocks run from the external `a,Z_0` endpoint to the local `b,Z_0`
endpoint; odd blocks run from local to external.  Every base matching edge
therefore joins a local even endpoint to a local odd endpoint without
renaming its base socket.  The dilation introduces no conjugating
permutation.  Once the exterior return is explicitly lifted with the same
socket labels, the base relation survives:

\[
                         \theta_0=\kappa,qquad
                         \theta_1=\kappa\circ s.       \tag{6.1}
\]

Thus the odd four-cycle is not the flaw.  Its physical first-return claim
is conditional only on the missing exterior closure/label identification.

## 7. Host theorem: odd central dimensions only

The cited low-exposure phased-host theorem is a theorem for

\[
 { [2m-1]\choose m-1}\longleftrightarrow
 { [2m-1]\choose m}.                                  \tag{7.1}
\]

Direct use for the universal-word middle rank requires

\[
                         k=2R-1,qquad m=R.            \tag{7.2}
\]

After adding any explicit `O(q)` terminal closure, the safe exposure
bounds are simply

\[
                         \alpha_m,\beta_m\le e_m=O(q).           \tag{7.3}
\]

Together with `q=O(sqrt(k))`, this gives `e_m=2^{o(m)}` and
`alpha_m,beta_m=o(m)`, so the host theorem applies for sufficiently large
**odd** `k`, subject to (2.1) and the refined protected closure above.

For even `k=2R`, the adjacent central shores have unequal sizes:

\[
                         {2R\choose R-1}<{2R\choose R}.          \tag{7.4}
\]

There is no spanning two-factor of the full incidence graph.  A balanced
restriction or a separate even-dimensional host theorem is needed.  The
source's phrase “for all sufficiently large ambient dimensions” is
therefore false as a consequence of the cited host theorem.

## 8. Corrected theorem and implication boundary

The proof-safe conclusion is:

> **Corrected clock-`C8` theorem.**  Assume (2.1), an explicitly closed
> exterior dilation satisfying the clock/tag halo, and the
> phase-and-endpoint-refined base all-width identity (4.1).  Then the
> displayed internal blocks extend to a simple, two-sided resident,
> aperture-`q`, all-width-transparent actuator with the inherited odd
> socket action and protected size/exposure `O(q)`.  If additionally
> `k=2R-1`, the existing phased-host theorem coinstantiates it for all
> sufficiently large `k`.

Even after this repair, the actuator does not imply:

* a bounded global Euler-component count;
* simultaneous Ferrers lower flags or upper witnesses;
* private common-cap prefixes or the typed suffix cut;
* automatic planting for even `k`; or
* the final `B(k)+O(1)` theorem.

Those are later joint occurrence rows.  The local dilation remains a
useful candidate, but the attachment overstates its present unconditional
scope.
