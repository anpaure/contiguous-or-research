# Every period-three exceptional palette has an explicit collision-free filter

Date: 2026-07-31  
Status: exact all-dimension partial diamond-matching theorem; removes the
three-primary phase-word obstruction when equivariance is not required; no
extension to a full Catalan linear matching is claimed

## 0. Verdict

Let

\[
 q=2m-1=3(2a+1),\qquad m=3a+2,
\]

and write the ground set as

\[
                     \Omega=\mathbb Z_q\sqcup\{\infty\}.
\]

Let `K_3` be the order-three subgroup of `Z_q` and

\[
          \pi:\mathbb Z_q\longrightarrow
          \mathbb Z_q/K_3\cong\mathbb Z_{2a+1}
\]

be the quotient.  The exceptional lower and upper colour banks are

\[
 L_A=\{\infty\}\cup\pi^{-1}(A),qquad
 U_B=\pi^{-1}(B),                                    \tag{0.1}
\]

where `|A|=a` and `B=Z_(2a+1)-A`.

There is an explicit partial perfect matching of the Boolean diamond graph
which simultaneously:

1. uses every exceptional lower colour exactly once;
2. uses every exceptional upper colour exactly once;
3. has all nonexceptional opposite-shore colours distinct;
4. has all physical middle endpoints distinct; and
5. pairs every lower-filter physical edge with its setwise-complement upper
   edge.

No assumption on `v_3(q)` is needed.  The phase-word difficulty in the
equivariant filter theorem is therefore a symmetry cost, not an intrinsic
exceptional-palette obstruction.

## 1. Construction

For every `a`-set `A` of the quotient, put

\[
 B=\mathbb Z_{2a+1}\setminus A.
\]

For (a\ge1), choose any deterministic ordered pair of distinct quotient points

\[
                         b_A,c_A\in B.                \tag{1.1}
\]

For example take the two least elements in the standard representatives.
Choose fixed representatives

\[
             x_A\in\pi^{-1}(b_A),qquad
             y_A\in\pi^{-1}(c_A).                    \tag{1.2}
\]

Define two diamonds:

\[
e_A^-=\bigl(L_A, L_A\cup\{x_A,y_A\}\bigr),        \tag{1.3}
\]

\[
e_A^+=\bigl(U_B\setminus\{x_A,y_A\}, U_B\bigr).   \tag{1.4}
\]

Their physical Johnson edges are

\[
 \psi(e_A^-)={L_A+x_A,L_A+y_A\},                   \tag{1.5}
\]

\[
 \psi(e_A^+)={U_B-x_A,U_B-y_A\}.                   \tag{1.6}
\]

The two endpoints in (1.6) are precisely the complements in `Omega` of the
two endpoints in (1.5).

When (a=0), the quotient has one point and its fibre has three finite
elements.  Choose any two distinct elements of that fibre for (x_A,y_A).
There is only one (A), and the same formulas apply.

## 2. Exact injectivity

The exceptional colours `L_A` are distinct, and complementation makes the
`U_B` distinct.  It remains to check the other two shores.

From

\[
                      L_A+x_A+y_A                    \tag{2.1}
\]

recover `A` as the quotient cosets whose three finite points are all
present.  The two additional nonfull cosets recover `{b_A,c_A}` and the
chosen representatives.  Thus the upper colours (2.1) are distinct.

From

\[
                      U_B-x_A-y_A                    \tag{2.2}
\]

recover `B` as the quotient cosets with nonempty intersection, and recover
the two deleted representatives from the two size-two cosets.  Thus the
lower colours (2.2) are distinct.  Exceptional and nonexceptional lower
colours cannot collide because only the former contain `infinity`; on the
upper shore only the nonexceptional colours contain `infinity`.

For physical endpoints containing `infinity`, the full finite quotient
cosets recover `A`; the unique additional point then distinguishes `x_A`
from `y_A`.  Hence all endpoints in (1.5) are distinct.  Their complements
in (1.6) are also distinct, and no endpoint from (1.5) equals one from
(1.6) because exactly the former contain `infinity`.

Therefore the selected diamonds are a partial matching on both colour
shores, and their physical lift is itself a matching.  In particular it has
middle degree one and is acyclic.  \(\square\)

## 3. Size and relation to the equivariant theorem

There are

\[
                     E={2a+1\choose a}
\]

exceptional colours on each shore, so the construction uses `2E` diamonds
and `4E` distinct middle vertices.  Under full rotation these colours form
`Cat_a` orbits, but the construction deliberately chooses every physical
colour separately.  It need not be invariant under any nontrivial subgroup.

When `v_3(q)=1`, orbiting one representative per quotient necklace recovers
the complement-paired clean-subgroup filters of the earlier theorem.  When
`v_3(q)>1`, the equivariant phase-word coupling remains real, but it is
irrelevant to this nonsymmetric partial matching.

## 4. Exact remaining gate

Delete the used lower and upper colours and reserve the `4E` used middle
vertices.  The remaining all-`m` central problem is to extend (1.3)--(1.4)
to a perfect diamond matching whose physical lift has degree at most two and
is acyclic.  The theorem does not prove residual Hall, rectangle-capacity
feasibility, or forest extension.  Its consequence is narrower but useful:
period-three stabilizers need no separate phase-word theorem in a direct,
symmetry-broken ordered-four-transversal proof.
