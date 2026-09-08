# The all-hook q2-neutral chain extends to h=3 and reaches an omission

**Date:** 2026-08-05  
**Method:** exact block cancellation and one rooted PBBS update; no search  
**Status:** unconditional for b>=1 at the action/profile and one-gadget
physical level.  The terminal connector is q2-neutral and one of its donor
components contains an explicitly tie-omittable q1 occurrence.  The result
does not supply two angle-disjoint lifts of every hook connector.

## 1. Terminal specialization

Use the literal family of
MATH_THEOREM_PBBS_ALL_HOOK_Q2_NEUTRAL_CONNECTOR_CHAIN_20260805.md, but put

\[
                         h=3,\qquad m=b+4,\qquad b\ge1.
\tag{1.1}
\]

The source imposed h>=4.  Its literal proof in fact remains valid at h=3.

The three old-row nonempty block heights are

\[
                         (3,2,2),
\]

and the same is true for the three companion rows; in every deficit-three
word the other two blocks are empty.  Hence all six required occurrences
remain uniquely max-height selected.

For the common companion calculation, the three inverse-state Dyck words
have their proposed initial maxima at heights 4,3,3.  Their later
competitors have height at most two because the relevant word is
\((10)^b\).  Therefore the first post-maximum zero \(d\) remains the common
reverse survivor when h=3.  The common-deletion q2 theorem still applies
without a tie.

Thus the clean C6 is q1- and q2-neutral and its action triple is

\[
 \boxed{
 (4,1^b),\qquad(3,1^{b+1}),\qquad(3,2,1^{b-1}).}
\tag{1.2}
\]

The three profiles are distinct, so the old edges lie on three distinct
PBBS components and the switch is a genuine merger.

## 2. Explicit omittable phase in the near-hook donor

The component with soliton partition

\[
                         J_b=(3,2,1^{b-1})
\tag{2.1}
\]

contains the rooted Dyck phase

\[
                         D=1(10)^b0\,111000.
\tag{2.2}
\]

The first global maximum is the top of the final height-three mountain.
Writing \(D=P1Q\) at its final up-step gives

\[
 P=1(10)^b0\,11,\qquad Q=000.
\]

The rooted PBBS formula therefore yields

\[
\begin{aligned}
 \phi(D)
 &=\overline Q\,0\,\overline P\\
 &=11100(01)^b100\\
 &=111000\,(10)^{b-1}\,1100.
\end{aligned}
\tag{2.3}
\]

Its primitive factors have heights

\[
                         3,\underbrace{1,\ldots,1}_{b-1},2.
\tag{2.4}
\]

Apply the exact outgoing-occurrence criterion at this phase.  The current
deficit-three block has height \(3-1=2\), while the final primitive factor
also has height two.  Hence the outgoing occurrence is maximal but **not
uniquely** maximal.

Choose the later height-two block in this one q1 tie.  Then the outgoing
edge at (2.3) is omitted from the max-height section.  This tie choice does
not affect q2 completeness: the global q2-section theorem explicitly
permits arbitrary tie decisions, because every occurrence used in its
canonical q2 witnesses is uniquely tallest.

Therefore \(J_b\) is an omission-bearing terminal donor for a suitably
chosen q2-complete max-height section.

## 3. Consequence for the two-rail programme

At action-profile level, the all-hook connector chain now runs through

\[
 \{H_b,H_{b+1},J_b\},\qquad1\le b\le m-4,
\tag{3.1}
\]

and the last triple contains the omission-bearing donor (2.1).  Combined
with the exact two-rail topology theorem, this removes the terminal
profile obstruction: if two angle-disjoint physical lifts of the required
connector are available at each rail stage, both rigid output rails can be
propagated to a \(J_{m-4}\) donor and broken there.

The only missing statement in this restricted PBBS programme is now the
angle-lifting/packing theorem.  One explicit connector per action triple is
not enough; the two rails require compatible physical component choices
and disjoint occurrences through the entire chain.
