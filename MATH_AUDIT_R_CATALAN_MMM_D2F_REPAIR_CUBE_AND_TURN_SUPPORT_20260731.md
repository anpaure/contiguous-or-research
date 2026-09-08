# Audit of the raw MMM turn-support formula and the D2F repair-cube theorem

Date: 2026-07-31  
Status: independent mathematical audit; PASS with scope qualifications

## 0. Verdict

`MATH_THEOREM_R_CATALAN_MMM_D2F_REPAIR_CUBE_AND_TRANSFER_OBSTRUCTION_20260731.md`
passes independent audit after the wording corrections recorded below.

The decisive new formula is valid:

\[
 A_n=(2n+1)(\operatorname {Cat}_n-\operatorname {Cat}_{n-1}),
\]

\[
 D_n=(2n+1)\frac{(n-2)(n-3)}{(n+1)(n+2)}
                   \operatorname {Cat}_{n-1}.
\]

The circuit lower bound `sum t_i>=D_n` is also valid for every repair
starting from the raw canonical factor.  The theorem correctly does not
extend that lower bound to an already repaired recursively lifted factor.

The formula is correctly restricted to `n>=2`.  At the degenerate `n=1`
base, the all-empty three-forest triple gives `A_1=P_1=1,D_1=0` and must be
handled separately.

The `m=5` polynomial exchange is correctly scoped: every proper vertex of
the frozen cube has coefficient zero, while the full packet is positive;
three-switch global minimality is not claimed.

## 1. Independent turn-normal-form check

Use paper parameter `n`, so the middle-levels ground size is `2n+1` and the
two shores have ranks `n,n+1`.

For a lower-shore rotation orbit, the cycle lemma gives its unique
representative `D0` with `D` Dyck.  Writing `D=1u0v`, the two upper
neighbours are

\[
                         1u1v0,\qquad1u0v1,
\]

so their union is `1u1v1`.

For an upper-shore orbit, use the unique representative `1D` and write the
last-return decomposition `D=u1v0`.  Its lower neighbours are

\[
                         0u1v0,\qquad1u0v0,
\]

so their intersection is `0u0v0`.  This verifies both normal forms without
using the claimed orbit count.

## 2. Independent three-forest quotient check

The cycle lemma for a binary word of excess three gives three positive
starting positions, counted with multiplicity.  Cutting a positive word
after its last visits to heights one and two gives the unique cyclic
three-forest representation

\[
                              1a1b1c
\]

up to cyclic permutation of `(a,b,c)`.

For the upper MMM turn the triple is `(u,v,empty)`.  If `u,v` are nonempty,
the empty component fixes the cyclic origin.  If exactly one is empty, the
only collision is

\[
                    (u,\varnothing)\sim(\varnothing,u).
\]

Catalan convolution gives `Cat_n` ordered pairs of total semilength `n-1`;
the one-empty collision removes exactly `Cat_{n-1}` copies.  Hence the
number of cyclic image classes is `Cat_n-Cat_{n-1}`.

Any stabilizer order divides both `2n+1` and the upper weight `n+2`, hence
is at most three.  A threefold repetition has equal three-forest components
`(w,w,w)`, incompatible with `(u,v,empty)` for `n>=2`.  Thus every attained
upper orbit is free.  Reverse-complementation proves the lower statement.

No hidden primitive-necklace assumption is used in this argument.

## 3. Count and algebra check

Multiplying the class count by the free orbit length gives `A_n`.  The two
palette ranks are complementary and have common size

\[
                              P_n=\binom{2n+1}{n-1}.
\]

Using

\[
 \operatorname {Cat}_n=\frac{2(2n-1)}{n+1}
                         \operatorname {Cat}_{n-1}
\]

gives the stated formula for `D_n`, and direct division gives

\[
 \frac{D_n}{P_n}=\frac{(n-2)(n-3)}{2n(2n-1)}.
\]

The first audited values are

\[
                    0,0,3,22,117,550
                    \qquad(n=2,\ldots,7),
\]

agreeing with independent literal turn enumeration.  At `n=5`, ground size
11 is prime, so the 22 missing colours really are two free orbits; the
obstruction is not only stabilizer-three.

## 4. Circuit lower-bound check

An alternating circuit of length `2t` meets at most `t` vertices on either
middle-levels shore.  Only turns at met vertices can change.  Therefore it
can introduce at most `t` colours which were absent before that switch.
Taking the union over an ordered packet gives

\[
 |S^\pm(F')\setminus S^\pm(F_n)|\le\sum_i t_i.
\]

Palette completeness requires all `D_n` initially absent colours to occur
at the endpoint, proving `sum t_i>=D_n`.  Overlap, loss and later
reintroduction cannot invalidate this upper bound; they can only waste
changed occurrences.

## 5. `m=5` cube and scalar-transfer audit

The frozen signed-palette table has lower/upper deficiencies

\[
                     3,2,2,1,2,1,1,0
\]

in selector order.  Lemma 1.1 of the theorem therefore makes every proper
target coefficient zero.  At the full vertex, the literal `210/210`
matching, gap forest and off-face trace prove positivity.  The `(0,0)`
preglue endpoint with component lengths `120,132` has the same authenticated
decoration, so Hamiltonicity is not used.

The component-count cube

\[
                         1,1,1,1,2,3,2,1
\]

gives constant polynomial coefficients `2,2,2,2,4,8,4,2`; this independently
refutes context-free multiplicative switch factors.  The stronger `ML(7)`
`1728/144/72` fibre split correctly proves that even component count is not
enough: occurrence, gap and phase data are genuinely required.

## 6. Required scope qualifications

The theorem observes all of the following boundaries.

1. `D_n` is the deficit of the **raw canonical MMM factor**, not of every
   standard-glued endpoint or every recursively repaired factor.
2. The lower bound excludes bounded-total-support repair of that raw factor;
   it does not exclude a macroscopic repair or a lift which inherits an
   already repaired parent.
3. Three `C10`s are minimal in the frozen cube and the stated audited
   catalogues only.  Arbitrary adaptive or longer two-circuit repairs remain
   unexcluded.
4. The boundary-state transfer theorem is exact but not a bounded-width or
   nonempty-root theorem.
5. D2F positivity proves the central Catalan path forest only.  Residence,
   deeper shadows, seams and compiler compatibility remain downstream.

With these scopes, the theorem is valid.
