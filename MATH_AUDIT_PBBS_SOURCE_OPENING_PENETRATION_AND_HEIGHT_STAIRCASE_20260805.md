# Self-audit: PBBS source-opening penetration and height staircase

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_PBBS_SOURCE_OPENING_PENETRATION_AND_HEIGHT_STAIRCASE_20260805.md`  
**Method:** adversarial symbolic indexing; no computation or search

## 1. Verdict

**GO at the exact prefix-copy and selected-bank scopes.**

The source/owner offset, fatal-prefix orientation, and staircase indices
are consistent.  The PBBS corollary is explicitly conditional on retaining
the phase-shifted fixed-section occurrences as consecutive intervals in one
terminal source cycle.  The current resident hybrid does not prove that
condition, so the note does not claim a bounded additive constant.

## 2. Source/owner off-by-one replay

An owner `T_i` uses source letters `A_i,...,A_(i+d)`.  The union of owners
`T_i,...,T_(i+q)` therefore uses exactly

\[
 A_i,A_{i+1},\ldots,A_{i+d+q},
\]

which is `d+q+1` letters.

Open between `-1` and `0`.  For start `i=-1-t`, the owner interval crosses
when `0<=t<q`.  Its owner suffix after the cut is

\[
 T_0,T_1,\ldots,T_{q-t-1},
\]

of size `q-t`.  A source prefix of length `d+C` creates exactly the repeated
owner starts `0,...,C-1`; hence the interval survives exactly when
`C>=q-t`.

The smallest checks are:

* `q=1,t=0`: one repeated owner `T_0` is needed, so `C=1`;
* `q=2,t=1`: only `T_0` is needed, so `C=1`;
* `q=2,t=0`: `T_0,T_1` are needed, so `C=2`.

These agree with Lemma 1.1.

## 3. Fatal-prefix direction

The internal cut at distance `a=t+1` from the witness start needs

\[
 C\ge q-a+1.
\]

It fails for a fixed `C` exactly when `a<=q-C`.  Hence the fatal edges are
the **first** `(q-C)_+` internal edges.  The final `C` internal edges are
rescued by the repeated owner prefix.  This verifies (2.1), including the
direction which is easy to reverse accidentally.

For one target, every occurrence fails exactly when the cut belongs to the
intersection of their fatal prefixes.  Therefore complementing the union of
the target cores is the exact common-cut criterion; no packing/transversal
duality is assumed.

## 4. Height collapse

At a fixed start the fatal prefixes are nested in `q`, so replacing all
selected depths there by their maximum `h_i` loses no information.  A start
`c-1-t` lies `t+1` edges before cut `c`; its maximum required repeated-owner
count is

\[
 (h_{c-1-t}-t)_+.
\]

Taking the maximum gives (3.3).  Thus zero overhead requires predecessor
heights `0,1,2,...`; one extra prefix letter requires `1,2,3,...`.  This is
the same deadline-arc orientation as the independently proved triangular
safe-cut lemma in the derivative-seam note.

If starts may be reordered arbitrarily, only the `u` starts preceding the
cut matter.  Choosing the `u` smallest heights is optimal, and matching
their sorted values `a_j` to thresholds `C+j-1` is the ordinary sorted
matching criterion.  This verifies (3.10)--(3.11).  It is a scalar theorem,
not a claim that PBBS hybrid moves realize the permutation.

For the PBBS phase-shifted bank, depth one uses all `W` starts, while every
depth at least two can use the common entrance-one start set of size

\[
 N_1={2m+1\choose m-1}=\frac{m}{m+2}W.
\]

Thus at least `2W/(m+2)` starts have height exactly one.  The displayed
product bound proves this is at least `m`; choosing `m` of them gives the
sorted list `a_1=...=a_m=1`.  Since every height is at least one, the
abstract reordered defect is exactly one.  This verifies Theorem 4.1.

The quantifier is important: the result prices the height inventory after
an arbitrary permutation of occurrence-height tokens.  It does not show
that owner-legal C6 rethreads move those tokens intact or make the selected
future intervals consecutive in the new cycle.

For the complementary rank-`(m+1)` owner row, De Morgan gives

\[
 \bigcup_{t=0}^{q}\overline{g^tX}
 =[n]\setminus L_q(X).
\]

Now every proper upper depth `q>=1` can use the entrance-one common start
set itself.  Hence all `W-N_1>=m` starts outside that set have height zero.
The maximum proper upper depth is `m-1`, because the remaining rank is the
full-ground target and the whole opened owner path supplies it.  Choosing
`m-1` zero-height tokens makes the abstract reordered defect exactly zero.
This verifies Theorem 4.2 and is the orientation relevant to an
upper-middle odd carrier.

Again, zero **scalar** defect is not yet zero physical defect: the rethread
must place those zero-height occurrence tokens consecutively without
destroying the selected future intervals.

## 5. Full-ground and long-interval edge case

The full-ground target is not charged to one fixed proper cyclic interval.
After opening, the union of the complete owner list still contains every
ground coordinate, so it remains represented by the whole linear owner
path.  The PBBS application therefore protects only proper upper targets,
whose chosen depths satisfy `q<=m<W`.

For an arbitrary target with a full-cycle witness, the complete occurrence
family contains a rotation beginning at the cut, whose internal edge span
omits that cut.  Thus the general core formula also gives an empty forced
core when all rotated full-cycle occurrences are included.

## 6. PBBS phase check

The identity

\[
 U_q(X)=[n]\setminus L_{q-1}(fX)
\]

means that an upper target of rank `m+q` has complement rank
`m-(q-1)`.  For `q=1`, its lower object is a middle root.  For `q>=2`, the
gap section at entrance depth one with extension `q-2` supplies a root `Z`
with `L_(q-1)(Z)` equal to that complement.  Taking `X=f^(-1)Z` gives the
claimed upper occurrence.  The indices are therefore consistent.

This occurrence statement lives in the canonical factor.  A later C6
rethread may preserve the target value internally without preserving this
start or its overhang.  The theorem now states the necessary terminal
consecutiveness/occurrence-map qualification explicitly.

## 7. Explicit all-unit quiet cycle replay

For the rooted all-unit state `A=0_r(10)^m`, deleting the first up-step
`p` gives

\[
 K=0_r0_p0_z(10)^{m-1}.
\]

Forward `10` cancellation removes the tail and leaves `r,p,z`.  Reverse
`01` cancellation pairs `z` to the first later one and each intervening
tail zero to the next one; it leaves `r,p,w`, with `w` the final zero.
The shared-mark convention therefore gives

\[
 C_r,A_r,C_p,A_p,A_z,C_w.
\]

Successive `C` gaps contain `1,2,0` `A` marks.  The potential values,
normalized at `C_r`, are `0,0,1`, so `C_w` is the unique maximum and its
preceding `A` is `A_z`.  The gap section selects `K+w -> K+z`.

The actual outgoing edge of `A` is `K+p -> K+r`; its boundary is
`A_r,C_p`, at potential zero.  Hence it is rejected.  The rectangular
soliton `f` update with `u=1,b=m` fixes `(10)^m` and advances the root by
one; `g=f^2` advances by two, which is a unit modulo odd `2m+1`, and hence
still visits all rotations.  Uniqueness of the potential maximum makes the
rejection rotation-stable and tie-rule independent.  This verifies
Theorem 4.3.

One middle start has only one outgoing q1 core.  Therefore rejection of its
outgoing occurrence means the start is not secretly selected for a
different core: if it were `sigma(K')`, then `K'` would equal the
intersection of that same outgoing edge.

The quiet component supplies a literal block longer than the required
`m-1` proper-upper depth.  The remaining gap is global fusion/transport,
not quiet-start existence.

## 8. Scope firewall

The exact implications are:

\[
 \text{one cyclic source with lower compiler}
 +\text{upper witness families}
 +\chi\le C
 \Longrightarrow W+d+C\text{ word},
\]

and, for a chosen bank,

\[
 \min_c\delta_h(c)\le C
 \Longrightarrow \chi\le C.
\]

The converses hold only for cyclic prefix-copy openings of the fixed source
or for retention of the selected bank, respectively.  A new collar, pivot,
or seam can create additional target occurrences and may beat `chi`.

No current theorem proves:

* terminal occurrence transport of the fixed PBBS upper bank;
* retention of the explicit zero-height staircase after global fusion;
* exterior overhang monotonicity of the resident C6 hybrid; or
* an unconditional `B(k)+O(1)` bound.
