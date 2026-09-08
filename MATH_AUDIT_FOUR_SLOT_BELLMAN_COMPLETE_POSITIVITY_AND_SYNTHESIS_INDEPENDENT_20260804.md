# Independent audit: complete four-slot Bellman positivity and synthesis rebase

**Date:** 2026-08-04  
**Audited corollary:**
`MATH_THEOREM_FOUR_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md`  
**Corollary SHA-256:**
`1624cff37c4f6b45edd16234e054d43c99ceb722d7dac4b57d058a40465b68b9`  
**Audited synthesis:**
`MATH_SYNTHESIS_SMOOTH_CONFIGURATION_RESIDENCE_AND_LOCAL_JOIN_FRONTIER_20260804.md`  
**Synthesis SHA-256:**
`37e4f7fb4196f819997fb8612981b0162757fce6a901cd009cd61927ea960b30`  
**Verdict:** **PASS after editorial rebase.**  The mathematical conclusion is exactly that every
Bellman table of grid size at most four is strictly positive.  Grid sizes
at least five remain open.  No `B+O(1)` conclusion follows.

## 1. Branch exhaustion

For a four-slot table `(0,x,y,z,T)`, internal superadditivity gives

\[
                         x\le y/2.
\]

Therefore the maximum of the four generator efficiencies is attained by
at least one of

\[
                         y/2,\qquad z/3,\qquad T/4.
\]

These three cases form an exhaustive cover, with harmless overlaps at
ties.

1. If `y/2` is maximal, the independently audited two-efficient theorem
   proves strict positivity on the complete branch.
2. If `z/3` is maximal, put `u=T-z`,
   `w=max(y,2u)`, and `v=max(y,u+x)`.  The alternatives `w=y` and `w=2u`
   exhaust the branch.  On `w=y`, first-crossing deletion removes
   `z>=A`, and period monotonicity reduces the subcritical face to exactly
   `P+u=A` or `P+u=2y`; both boundary theorems are independently audited.
   On `w=2u`, the complete adverse-pulse theorem is independently audited.
3. If `T/4` is maximal, the exact four-state Apéry theorem reduces the
   branch to the threshold face, the already closed two-efficient tie, and
   the scalar function `J(alpha)`.  The threshold theorem and independently
   audited scalar gate close all three pieces.

Thus all four-slot tables are positive, including every efficiency tie.
Together with the proved `n<=3` result, all `n<=4` tables are positive.

## 2. Hash replay

Every hash cited by the aggregate corollary matches the current file:

\[
\begin{array}{c|l}
\text{role}&\text{SHA-256}\\ \hline
\text{efficiency normal forms}&2bc644a1fdfef612ed9a0181326a5da25ce3e4952ed4f001c06875aec09dbb5d\\
\text{two-efficient closure}&47819d25abf75877b6bc723ed593354bb0e76582635996227ac9c48812b986c8\\
\text{two-efficient audit}&20dcdbb21cd71ed2bacd6c637ff59ee23ffa2dec6ed1da61cf42f05af07d2fbb\\
\text{three-efficient reduction}&0b46d0b2e073cc9eab4171198e2b4686ce08ef055887fd3f72cd0a506cdfef35\\
\text{first `w=y` boundary}&7e1a12d5cce9a16b6fd9a1b65d7d9d625d114c5b8810fa7f2d6baf95bfed722b\\
\text{first-boundary audit}&090494f7180f211752635415294b4fd5f341cded2362de9c46aaf19eb6aea1c4\\
\text{second `w=y` boundary}&6a44b458c013e3c553be3925f9439960b139262175aaf79bbb9fb50054f6c7d7\\
\text{second-boundary audit}&5db0e5ebe3b5ab3bab6fff6930fe6f7c406486a4853e0b80e7eeac5223396cd8\\
\text{`w=2u` closure}&64451d508cc73c5ac5baf04bd749695358eea7fffb3d4c93a8c5eafa8c3bfae1\\
\text{`w=2u` audit}&c86adbe63511b8102bab86576893c3da9a6fd438ef3bd2430b0714ab885490c9\\
\text{four-state Apéry theorem}&8fc1405920daea3e597a105d04b9b63e42867a4db1cf9c9515f2a73cd6584cda\\
\text{Apéry scalar gate}&2b334fc6670ec73d4eba0f9de7a211b5e64f38a77f205ee822bebc4f3a79e776\\
\text{scalar-gate audit}&4dc1f99d6626cd23130f08f56e9cc94d1458c5b253901636ee9e508d938b2bd5.
\end{array}
\]

The independently audited current Apéry normal-form theorem additionally
has audit

\[
 `MATH_AUDIT_FOUR_SLOT_APERY_EXACT_NORMAL_FORM_AND_THRESHOLD_FACE_INDEPENDENT_20260804.md`
\]

with SHA-256
`740996898d0961e09b65662de54f72bc281c49cce2b287225cddcec59654499c`.

## 3. Synthesis scope

The synthesis accurately records the new result:

\[
 \boxed{
 \text{every grid of size at most four is positive; any finite
 counterexample has grid size at least five.}
 }
\]

The earlier sentence saying that the completed `n=3` argument leaves grid
size at least four is a chronological intermediate statement and remains
true; the subsequent `n=4` section explicitly strengthens it to five.

The synthesis also correctly keeps the following statements open:

* Bellman positivity for arbitrary finite grid size, beginning at `n=5`;
* the exact smooth binomial configuration/coagulation theorem;
* integral chainization, literal containment, residence, upper occurrence,
  and common-cap correlation;
* `nu(k)<=B(k)+O(1)` and `nu(k)=B(k)`.

Thus the finite `n<=4` dual theorem is not promoted into an OR-word upper
bound.

## 4. Editorial rebase

The three requested editorial changes are present in the proof-bearing
locations:

1. the efficiency branches are now an overlapping cover at ties, not
   called a disjoint partition;
2. the theorem's consequence is stated as grid size at least five;
3. the dependency table now includes the independent Apéry normal-form
   audit hash `74099689...`.

The aggregate status paragraph and one synthesis verdict bullet retain the
informal phrase “active slots.”  In context they refer to the displayed
generator indices and do not alter the formal grid-size theorem.  Replacing
those two remaining phrases by “grid size” would be stylistically cleaner,
but no proof or scope statement depends on them.

No substantive mathematical line changed in the rebase.  Every dependency
hash in the updated aggregate table still matches its current file.

**Final independent verdict: PASS.**
