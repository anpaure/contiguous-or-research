# The PBBS max-height q1 section is not automatically graphic

**Date:** 2026-08-05  
**Method:** exact hand calculation at `m=2`; no computation or search  
**Status:** sharp scope correction.  The max-height q1 section is q2-complete,
but its selected edges can contain a whole PBBS step-two factor cycle.  Thus
the cycle-hit hypothesis in the two-factor Pascal lift is genuinely
additional.

## 1. The two PBBS cycles on five coordinates

Work on `Z_5` and put `m=2`.  Let

\[
 A_j=\{j,j+1\},\qquad B_j=\{j,j+2\},               \tag{1.1}
\]

with indices modulo five.  These are respectively the five adjacent and
five nonadjacent two-subsets.

Direct cyclic `10` matching gives

\[
 f(A_j)=A_{j+2},\qquad f(B_j)=B_{j+1}.              \tag{1.2}
\]

For example,

\[
 01\mapsto23\mapsto04\mapsto12\mapsto34\mapsto01,
\]

and

\[
 02\mapsto13\mapsto24\mapsto03\mapsto14\mapsto02.
\]

Thus the centered `g=f^2` factor also has exactly two five-cycles, one on
the `A_j` and one on the `B_j`.

## 2. The max-height section selects the whole A-cycle

Fix the q1 target `K={j}`.  Its deficit-three word has one `1`.  The unique
nonempty Dyck block is the `10` at positions `j,j+1`; it is preceded by the
unmatched zero at `j-1`.  Therefore the max-height q1 rule selects the edge

\[
 \{j,j+1\}--\{j-1,j\}=A_j--A_{j-1}.                \tag{2.1}
\]

As `j` ranges over `Z_5`, these are exactly all five edges of the A-cycle.
Hence the selected occurrence set contains that entire factor cycle.  Its
complement consists of all five q1 occurrences on the B-cycle.

The section is nevertheless q2-complete.  There is only one q2 target, the
empty set, and every adjacent pair of selected singleton turns witnesses it.
Thus

\[
 \boxed{\text{q2-complete does not imply cycle-hit, even for the canonical
 PBBS max-height section.}}                           \tag{2.2}
\]

## 3. The obstruction is repairable but not automatic

Every singleton q1 target has one occurrence on each of the two factor
cycles (equivalently, the q1 load is two).  Moving the representative of
one singleton from its A-occurrence to its B-occurrence punctures both
cycles.  Four consecutive-cycle edges remain selected on A, so the empty
q2 target is still witnessed.

Therefore the example is not a no-go for a graphic q2-complete section.  It
is a no-go only for the claim that the canonical max-height choice already
satisfies the graphic clauses.  Any all-`m` proof must include a
cycle-breaking representative exchange or a more flexible joint selection.

