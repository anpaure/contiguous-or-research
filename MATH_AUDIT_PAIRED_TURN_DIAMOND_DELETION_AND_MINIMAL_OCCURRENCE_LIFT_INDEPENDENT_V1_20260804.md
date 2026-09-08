# Independent audit V1: paired turn-diamond deletion and minimal occurrence lift

**Date:** 2026-08-04  
**Verdict:** **GO** at the declared paired-support and occurrence-lift scope.
No computation, search, or solver output is used.

Audited theorem:
`MATH_THEOREM_PAIRED_TURN_DIAMOND_DELETION_AND_MINIMAL_OCCURRENCE_LIFT_20260804.md`,
SHA-256
`b1852de086db9846d6f4748e7200fe4757d31036e5a50673a68dac78d6262110`.

Author audit:
`MATH_AUDIT_PAIRED_TURN_DIAMOND_DELETION_AND_MINIMAL_OCCURRENCE_LIFT_20260804.md`,
SHA-256
`944f69851bfe010f09a0a745afc7bf6b3bf967e7866711e8686cf366487ed9f5`.

## 1. Exact casualty set

For one claim,

\[
 V(P_i^\epsilon)=C_i\mathbin{\dot\cup}E_i^\epsilon,
 \qquad E_i^0\cap E_i^1=\varnothing.
\]

If the deletion bank meets `C_i`, it kills both alternatives.  If it avoids
`C_i`, alternative `epsilon` survives exactly when the deletion bank avoids
`E_i^epsilon`.  Therefore a claim is dead exactly when it has a common hit,
or it has no common hit and both ordered sides are hit.  This is precisely
the displayed set `D_F`.

Every dead claim of the second kind contributes two distinct side-hit
records to `s_F`.  Different claims contribute disjoint ordered pairs, so

\[
 |D_F|\le c_F+\left\lfloor{s_F\over2}\right\rfloor.
\]

For each live claim, choose either surviving displayed path.  The total
support disjointness assumption across distinct claims makes all choices
simultaneously vertex-disjoint.

## 2. Sharpness and physical-resource form

The numerical bound is attained on an instance with nonempty declared
resource pieces: delete one common resource in each of `c` claim pairs and
one exclusive resource on each side of `t` other pairs.  Then

\[
 c_F=c,
 \qquad s_F=2t,
 \qquad |D_F|=c+t.
\]

Under physical support disjointness, one deleted common resource can witness
at most one common-hit claim and one deleted exclusive resource can witness
at most one ordered side hit.  Hence

\[
 c_F\le f_C,
 \qquad s_F\le f_E,
\]

and the corresponding resource bound follows.  If common cores are
protected, every dead claim requires two exclusive-side losses and

\[
 |D_F|\le\lfloor |F|/2\rfloor.
\]

## 3. Middle-Levels turn-diamond specialization

For one protected wedge, the two branches share the lower source and q1
terminal and have distinct owner occurrences.  Protected wedge packing
makes sources distinct across claims, all `2p` owner values distinct, and
all q1 terminal values distinct.  Definition 3.1 additionally demands the
capacity-faithful occurrence quotient and total support disjointness for
every flag, guard, and continuation.  Thus it supplies exactly the abstract
hypotheses of the paired-deletion lemma.

After frozen deletion, the theorem therefore leaves all but at most

\[
 c_F+\left\lfloor{s_F\over2}\right\rfloor
\]

claims with pairwise disjoint typed routes.

If deletions hit only the selected owner occurrences, then `c_F=0`.  Since
all owners are distinct, `r` deleted owner occurrences create at most `r`
ordered side hits, so at most `floor(r/2)` claims die.  Conversely, avoiding
every predeclared owner and terminal deletion makes both hit counts zero on
the direct face; the theorem correctly retains the warning that source,
flag, or hidden-capacity deletions must still be priced.

## 4. Fixed-bank Rado equality

After contracting each complete surviving branch, every live claim has at
least one private claim-to-sink edge and every dead claim has none.  Supports
and sink capacities are disjoint across claims.  Thus all live claims are
simultaneously serviceable and no dead claim is serviceable.  The maximum
service size is exactly `p-|D_F|`, so the factor-restricted Rado deficiency
is exactly `|D_F|`, not merely bounded by it.

## 5. Hidden global flag obstruction

Let one unit flag `g` lie on both alternatives of every claim.  Every claim
has two valid branches before deletion, but deleting `g` kills all `p`
claims with a one-resource deletion bank.  This violates total support
disjointness across claims and proves that no function of deletion-bank
cardinality alone can replace the multiplicity-aware hypotheses.

Definition 3.1(5)--(6) excludes this failure mode exactly: a shared flag
must be represented with its true common multiplicity, and then the required
cross-claim disjoint lift does not exist.  Marginal branch activation cannot
hide the obstruction.

## 6. Scope

The theorem does not construct the raw dual-branch occurrence lift or prove
that its frozen deletion intersection is bounded.  It also does not close
two-coordinate products, topology, upper decoration, residence, compiler
regeneration, or the all-dimensional OR-word theorem.

The independent V1 verdict is **GO** at the hashes listed above.
