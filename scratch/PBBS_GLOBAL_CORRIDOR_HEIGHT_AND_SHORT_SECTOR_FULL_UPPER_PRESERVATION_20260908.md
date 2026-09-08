# The global PBBS corridor has height at least its depth

Date: 2026-09-08. Author: Codex subagent `exact_b_induction`.

Status: new pure proof. Together with the already recorded immediate-upper
recapture and five-block q2 argument, this proves complete upper preservation
for the explicit all-r short-sector path. No new computation was used.

## 1. Height as a cyclic interval statistic

Encode membership by an up-step +1 and nonmembership by a down-step -1.
For a rank-r set on n=2r+1 cyclic coordinates, let D be its normalized
Dyck word: the rooted circular word is 0D, where D is balanced and has
nonnegative prefix sums. Then

\[
 \boxed{\operatorname{ht}(D)
   =\max_{I\text{ a cyclic interval of at most }n\text{ positions}}
       \sum_{i\in I}(2\mathbf1_A(i)-1).}                 \tag{1.1}
\]

To prove this, write H=ht(D). An interval wholly inside D has increment
equal to the difference of two prefix heights in [0,H], hence at most H.
An interval crossing the distinguished zero has increment

\[
                  -h_{\rm start}-1+h_{\rm end}\le H-1.
\]

The full-circle increment is -1. Conversely, a prefix of D ending at a
maximum attains H. This proves (1.1), including its independence of the
chosen physical coordinate origin.

## 2. Flipping consecutive reverse-unmatched zeros forces height

Let S have rank r-q, where 1<=q<=r. Its deficit is 2q+1. Perform reverse
cyclic-parenthesis matching, namely repeated cancellation of adjacent 01
pairs. Let

\[
                     C_0,C_1,\ldots,C_{2q}
\]

be its reverse-unmatched zeros in forward physical order, with any choice
of C_0. The open cyclic arc between any two consecutive C marks is balanced.
Indeed, each unmatched zero is a permanent barrier during cancellation;
a pair cannot cross it, so every symbol in each such open arc cancels with
another symbol in that same arc. Its numbers of zeros and ones are equal.

Set

\[
                     B=S\cup\{C_0,\ldots,C_{q-1}\}.
\]

The cyclic interval from C_0 through C_(q-1), inclusive, contains exactly
those q reverse-unmatched zeros and the q-1 balanced intervening arcs.
In B every displayed C mark is a one. This interval therefore has total
increment q. The other 2q+1-q marks lie outside the interval, so the arc
does not wrap more than once. Equation (1.1) proves

\[
                      \boxed{\operatorname{ht}(B)\ge q.} \tag{2.1}
\]

This statement does not require a global-maximum choice of the first mark.
That choice is needed for the canonical path in the next section.

## 3. Height-controlled canonical support at every depth

Use the actual global-maximum corridor from
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, Lemma 21.1 and Theorem 21.2.
For the given S, its selected expanded A_0,C_0 boundary numbers reverse
marks forward and forward marks backward, and supplies

\[
 B_t=S\cup\{C_0,\ldots,C_{q-t-1}\}
       \cup\{A_0,\ldots,A_{t-1}\},\qquad 0\le t\le q.
\]

That established theorem proves both

\[
             gB_t=B_{t+1}\quad(0\le t<q),\qquad
             \bigcap_{t=0}^{q}B_t=S,\qquad g=f^2.
\]

Its initial state B_0 has precisely the form of Section 2. Consequently
the corridor theorem has the following additional conclusion:

\[
 \boxed{\text{Every rank-}(r-q)\text{ set has a correct q-edge canonical
 witness whose initial root has height at least }q.}       \tag{3.1}
\]

In particular, for q>=3 the initial state cannot lie in any component of
the bad short-run sector. Every state of each such component has the
explicit height-two root

\[
              (10)^x1(10)^{y+1}0(10)^z,
              \qquad x+y+z=r-2,\quad xyz=0.
\]

This sector is invariant under f and g by its exact coordinate map, as
proved in `scratch/PBBS_EXACT_THREE_RUN_COMPONENT_SECTOR_20260908.md`.
Thus a g-path starting outside it stays in a component outside it. Every
state and every edge of the corridor witness is therefore untouched when
the bad components are replaced by the explicit short-sector path.

This argument uses the established corridor to identify actual canonical
edges. A mere large-height completion of S would not suffice.

## 4. Complete upper preservation for the explicit short-sector path

For every r>=3, take the all-r path from
`scratch/PBBS_ALL_R_SHORT_RUN_SECTOR_JOHNSON_PATH_20260908.md`, replacing
the r-2 bad canonical components by their one 3(2r+1)(r-2)-owner path.
Keep every other canonical component intact. Complement the lower owners
to obtain the upper-middle owners.

This mixed path/cycle family covers every target of rank at least r+1.

* Rank r+1: every original owner is retained exactly once.
* Rank r+2: the deleted q1 colors are recovered by the exact phase and
  backup identities in Sections 2-3 of
  `scratch/PBBS_ALL_R_SHORT_SECTOR_FIRST_UPPER_RANKS_PRESERVED_20260908.md`.
* Rank r+3: Section 4 of that same note uses the explicit five-block q2
  construction. Since |S|=r-2>=1, its central root has height H+2>=3.
  Its witness lies outside the invariant bad sector and remains intact.
* Rank r+1+q for 3<=q<=r: apply (3.1). The witness starts at height at
  least q>=3, hence lies entirely in an untouched component. Complementing
  its exact intersection produces the requested literal cyclic upper union.

These cases exhaust all ranks from r+1 through 2r+1. In particular,

\[
 \boxed{\text{The explicit all-r short-sector path preserves the entire
 canonical upper deck when all other components are left intact.}} \tag{4.1}
\]

The higher-rank conclusion is stronger than a statement about the chosen
cuts: every target of rank at least r+3 has a supplier completely outside
the bad sector. Only rank r+2 needs the explicit seam and backup analysis.

## 5. Exact scope and audit record

This proves an all-r support statement for one linear path together with
the remaining cyclic components. The untouched cycles still require
valid opening and joining before there is a single ordinary source word.
No claim about their cutting costs, the lower-rank source atlas, or
nu(k)=B(k) follows from upper support alone.

The earlier full-upper computation for r=3,...,8 was already completed
and is recorded in
`scratch/pbbs_all_r_short_sector_upper_audit_20260908.json` and the first
upper-ranks note. It was not rerun for this proof. The new argument is
Sections 1-4, which has no computational premise.

The result in this note supersedes the higher-rank open status in the
first upper-ranks note. That earlier note remains the detailed record of
the q1 recapture, q2 witness, and bounded audit.
