# Exact one-seam lift, relative relabeling, and endpoint caps

Date: 2026-09-08. Author: Codex subagent `exact_b_induction`.

Status: complete finite constructive equivalences proved below. This note
does not claim a new attaining word in dimension 18 or an all-dimensional
exact induction. No mathematical computation was run for this note. The
relative-relabeling precedence formulation was proposed by root and is
independently proved here. The endpoint-cap profile reduction is derived
here. Actual endpoint profiles and finite decisions belong to their
separately attributed certificates.

## 1. Relation to existing lift results

`MASTER_HANDOFF.md`, Section 2.2, already proves the standard trimmed lift
and its literal-border improvement. The standard lift of a universal word
of length m has length 2m. The earlier
`FINITE_LIFT_SLACK_THEOREMS_AUDIT_20260724.md`, Sections 2–3, proves
descending-tail, ascending-prefix, and two-ended conditional improvements;
its Section 11 gives the general tagged double-cover criterion.

The result below specializes that exact criterion to one pure new-letter
bridge, then eliminates the existential seam witnesses. For a fixed marked
tail it gives an exact finite precedence problem for a relative relabeling
of the universal unmarked word. It is stronger than merely counting seam
targets or assuming a long literal border.

The latest verified baseline is recorded in
`scratch/EXACT_B_GOAL_CHECKPOINT_20260908.md` and
`K17_OPTIMAL24313_VERIFIED_20260908.md`: nu(17)=24313 and the standard lift
has length 48626, whereas B(18)=48623. This note formulates a concrete gate
for saving the remaining three letters in this one-seam architecture.

## 2. Exact seam-deck theorem

Let X be a finite nonempty alphabet. Let A=(A_1,...,A_m) be a universal
word of nonempty subsets of X, and let B=(B_1,...,B_l) be any finite word
of subsets of X. Empty letters in B are allowed: after tagging, they become
the nonempty singleton {z}. Let z be a new coordinate and put

    L(A,B) = A || {z} || (B_1 union {z}) || ... || (B_l union {z}).

Write Cov(B) for the nonempty old targets realized by ordinary nonempty
intervals of B. Let Suf_0(A) and Pref_0(B) be the suffix-union and
prefix-union chains, each including the empty union.

**Theorem 2.1.** The projections onto X of all intervals of L(A,B) that
contain z are exactly

    {empty} union Cov(B)
      union {C union P : C in Suf_0(A), P in Pref_0(B)}.       (2.1)

Here adjoining the empty projection to Cov(B) causes no ambiguity if B
itself has an empty interval union.

**Proof.** An interval meeting the tagged tail but not the bridge is
entirely in that tail, hence has a projection in Cov(B) or is empty. An
interval containing the bridge contains a suffix of A, possibly empty,
and a prefix of B, possibly empty, and its projection is their union.
These cases exhaust all intervals containing z. Every displayed projection
has the described literal witness. The singleton bridge realizes {z}.
All targets avoiding z remain covered inside A. This proves the exact
deck statement and its universality consequence. QED.

For a nonempty old target D, define T_B(D) as follows. Take the longest
initial segment of B all of whose letters are subsets of D, and let
T_B(D) be its union. The segment can be empty or can be all of B. Thus
T_B(D) is the largest prefix-union of B contained in D. Put

    R_B(D) = D minus T_B(D),
    Def(B) = (2^X minus {empty}) minus Cov(B).

**Corollary 2.2 (fixed-tail seam criterion).** The word L(A,B) is universal
if and only if, for every D in Def(B), there is C in Suf_0(A) satisfying

    R_B(D) subseteq C subseteq D.                            (2.2)

**Proof.** If a seam realizes D=C union P, both C and P are subsets of D,
so P is contained in T_B(D), and D minus T_B(D) is contained in C.
Conversely, (2.2) implies C union T_B(D)=D, giving an actual seam witness.
Targets outside Def(B) have internal marked witnesses. QED.

For a genuine nonempty defect D, R_B(D) is nonempty: equality
T_B(D)=D would already provide an internal nonempty prefix witness in B.
Nevertheless (2.2) remains valid for an empty R, using C=empty. A full
target D=X presents no difficulty even if it is a defect: the full suffix
union of the universal word A is X and repairs it. Thus the full target
must not be discarded as an unsupported exceptional case.

One immediate necessary condition for the fixed unrelabeled A is

    A_m subseteq intersection_{D in Def(B)} D                (2.3)

when Def(B) is nonempty. Every genuine defect requires a nonempty suffix,
which contains A_m. This simple condition is necessary, not sufficient.

## 3. Exact relative-relabeling reduction

List the distinct suffix-union states of A in increasing order as

    empty = C_0 strictly contained in C_1 ... C_q = X.

Define its ordered recency blocks E_i=C_i minus C_(i-1), and their positive
sizes b_i=|E_i|. This is the most-recent-first convention. Let pi be a
permutation of X applied to every letter of A; B remains fixed.

Construct a directed graph G_B on X by adding every arc

    x -> y,  x in R_B(D), y in X minus D, D in Def(B).        (3.1)

Duplicate arcs may be discarded. There are no self-arcs from an individual
defect, because R_B(D) is contained in D, although directed cycles can
arise from different defects.

**Theorem 3.1 (precedence equivalence).** A relative relabeling pi makes
L(pi(A),B) universal if and only if X admits an ordered partition
(F_1,...,F_q) such that

    |F_i|=b_i,
    block(x) < block(y) for every arc x -> y of G_B.          (3.2)

Whenever such a partition is supplied, an explicit pi and every missing
target's literal seam witness can be constructed.

**Proof.** Fix a relabeling, and use F_i=pi(E_i). For a target D, some
prefix F_1 union ... union F_j contains R_B(D) and avoids X minus D if
and only if every element of R_B(D) has strictly smaller block index than
every element of X minus D. Necessity follows from the prefix boundary j.
For sufficiency, when R_B(D) is nonempty take j to be its largest block
index. Every element outside D then lies after j. If R_B(D) is empty use
j=0. If D=X there are no excluded coordinates and the same choice works.
This proves equivalence to (2.2), including ties: a required coordinate
and an excluded coordinate cannot share a block.

Conversely, every ordered partition with these sizes is pi(E_1),...,pi(E_q)
for some coordinate permutation: choose any bijection from each E_i to
F_i and combine them. Relabeling preserves the universality of A. For
each defect D use the suffix of pi(A) whose union is F_1 union ... union
F_j, the bridge {z}, and the longest B-prefix contained in D. Their union
is D union {z}. These are actual contiguous, nonwrapping witnesses. QED.

Thus the complete graph, rather than pairwise guessed seam witnesses,
encodes every defect simultaneously. There is no independence assumption.
It is legitimate to replace G_B by its transitive closure, but not to
relax strict inequalities to non-strict ones.

Its initial minimal vertices have a particularly simple description:

    Min(G_B) = intersection_{D in Def(B)} D.                (3.3)

The empty intersection is X. A coordinate in that intersection is never
the excluded endpoint of an arc. Conversely, if y is excluded by some
defect D, then R_B(D) is nonempty, and any of its coordinates gives an
incoming arc into y. More generally, after removing a union P of already
assigned blocks, an unassigned y is minimal exactly when

    R_B(D) subseteq P for every defect D excluding y.       (3.4)

This follows directly from the complete incoming-arc set. In particular,
an empty defect intersection rules out every nonempty first block and
hence every universal left word in this architecture.

## 4. Complete finite block decision

The following finite recursion is necessary and sufficient for (3.2).

1. On the remaining induced graph, compute its vertices with no incoming
   edge from any remaining vertex.
2. Choose an arbitrary subset of exactly b_i such vertices as the next
   block F_i. Remove this whole subset simultaneously and recurse.
3. Accept only after all required blocks have been assigned.

If there are fewer than b_i current minimal vertices, that branch fails.
Every valid ordered partition follows such a branch, because neither a
later block nor the same block can have an edge into its current block.
Conversely, each selected subset has no internal arc and no incoming arc
from a later block; induction gives all strict inequalities. This proves
completeness of the decision and of a negative answer when all branches
are exhausted.

Acyclicity alone is insufficient for prescribed blocks of size greater
than one. For example, a three-vertex directed chain is acyclic but cannot
have a first block of size two. If every remaining block has size one,
ordinary topological sorting is sufficient; arbitrary choices among
current minima cannot destroy existence of a topological ordering.

For a profile (b_1,b_2,1,...,1), a complete search need enumerate only the
first two blocks: at most binomial(k,b_1) choices followed by at most
binomial(k-b_1,b_2), always restricted to current minima. The singleton
remainder is decided by topological sorting. This is a finite complete
criterion, not a probabilistic or heuristic search.

A simple positive subcase uses just the last suffix letter to repair
every defect. Let U be the union of all R_B(D), and I the intersection of
all defects. Such a common last-letter repair of size b exists exactly
when U subseteq I and |U|<=b<=|I|: choose U subseteq C subseteq I with
|C|=b. A relative relabeling placing C in a certified base's first block
then repairs every defect using that single suffix state. This is a
sufficient construction for the general problem, and an exact criterion
for this more restrictive one-state repair.

## 5. Endpoint caps give additional profiles

Let m>=2, l=A_m, and P=A_(m-1). Replace l by a nonempty C subseteq l.
The last pair union is preserved exactly when

    l minus P subseteq C subseteq l.                       (5.1)

Under (5.1), every interval of length at least two is unchanged. Only the
one-letter occurrence of l can be lost. Hence the capped word remains
universal whenever l has another ordinary interval witness. In particular,
an earlier literal occurrence of l suffices for every cap satisfying
(5.1). If C=l there is of course no change or backup requirement.

More precisely, for a proper cap C, the old target l survives if and only
if either it has a witness entirely in A_1,...,A_(m-1), or P subseteq l.
Indeed all longer intervals are unchanged; a longer witness ending at the
last position exists exactly when the last pair already has union l.
This gives an exact universality test for a pair-preserving endpoint cap,
although an earlier duplicate is the simplest sufficient certificate.

All suffix unions of length at least two are unchanged. In the uncompressed
time-indexed recency blocks, capping moves precisely l minus C from the
first block to the second, leaving every later block unchanged. In
particular, if the old last pair strictly grows, so the second recency
block already has positive size b_2, the positive size profile changes as

    (|l|, b_2, b_3,...) -> (|C|, b_2+|l|-|C|, b_3,...).     (5.2)

If the old immediate second block was empty, use the uncompressed blocks
and then delete zero blocks; no positive-block formula should silently
skip this case.

**Profile reduction.** Once arbitrary relative relabeling is allowed,
valid endpoint caps with the same resulting block sizes are equivalent
for Theorem 3.1. There is no need to test every cap mask. One valid base
word for each possible size profile suffices, because its subsequent
coordinate permutation realizes every assignment to blocks of that shape.
Under an earlier-duplicate certificate and strict pair growth, every size

    max(1, |l minus P|) <= |C| <= |l|

is available. For a five-coordinate last letter this gives at most five
profiles, regardless of the number of cap subsets. This is an exact
reduction of the specified cap-and-relative-relabeling family.

## 6. Budget and the remaining constructive gate

The length of L(A,B) is m+1+l. Saving d letters from the standard 2m lift
therefore requires l=m-d-1. In particular, for an odd alphabet size k,
write W=binomial(k,floor(k/2)) and suppose m=W+t. A tail of length W-1
would give

    m+1+(W-1)=2W+t.                                       (6.1)

Since W(k+1)=2W(k) for odd k, this has the same additive excess t above
the next width. This arithmetic is not an assertion that B(k+1)=2W+t
in every case. For the verified k=17 word, W=24310 and t=3, so a tail
of length 24309 satisfying Theorem 3.1 yields length 48623=B(18).

For a fixed tail B and a chosen collection of certified universal base
profiles, the concrete gate is now exact:

* compute all ordinary defects of B and their maximal allowed prefixes;
* build G_B by (3.1);
* solve its prescribed-block partition problem for those profiles;
* on success, construct the coordinate permutation and the literal lift.

A proof or computation that this gate fails only rules out the specified
tail and those base profiles. It does not rule out a different tail,
opening, source word, multiple bridges, or a general attaining word.

If B is a prefix formed by deleting c final letters from a universal word
on k coordinates, then |Def(B)|<=ck. Every defect must have a witness
ending at a deleted position; the nonempty suffix unions at any fixed
endpoint form a strict inclusion chain with at most k distinct members.
Thus the four-letter deletion in the present 17-dimensional interface has
at most 68 defects. This is a general bound, not a claim about the measured
number in a particular file.

## 7. Why plain truncation of the same flat word fails

Here is a useful exact negative finding explaining why relative relabeling
or another genuine boundary change is needed.

Suppose a word A of length m>=w+1 has all (w-1)-letter interval unions of
rank less than s, and all w-letter interval unions have rank s and are
pairwise distinct. Then any rank-s target appearing in a w-window has
that unique literal interval witness. Shorter intervals extend to a
(w-1)-window and have smaller rank. Longer intervals contain two adjacent
distinct rank-s w-windows and have rank greater than s.

Let T be the penultimate w-window union, ending at m-1. If B is the
literal prefix A_1,...,A_(m-c) for any c>=2, then T is a defect of B.
Furthermore A_m is not contained in T: otherwise the final w-window union
would be contained in T, and equal ranks would force it to equal the
penultimate union, contradicting distinctness. Condition (2.3) fails.

Consequently L(A,B) cannot be universal for any such truncation. This
argument survives applying the same coordinate relabeling to both copies,
and also simultaneous reversal of both copies. It does not survive an
arbitrary relative relabeling or a separate valid endpoint cap, which are
precisely the additional freedoms in Sections 3–5.

The verified optimal17 word satisfies these hypotheses with w=4 and s=9:
every triple has rank8 and the 24310 four-letter unions are the 24310
distinct rank9 targets. Those facts were independently checked by
`exact_b_finite_frontier` in
`scratch/verify_k17_optimal24313_direct_forward_20260908.py`; they are not
new execution claims of this note. Thus simply taking its literal prefix
of length m-4 as the marked tail cannot save three letters with the same
unchanged left copy. The exact precedence criterion describes a genuine
way to escape that narrowly proved obstruction.

## 8. Status and attribution

The seam deck, precedence equivalence, complete block recursion, endpoint
cap reduction, and flat-prefix obstruction are proved above without
execution. Root proposed the precedence gate and endpoint-cap extension;
this note supplies their independent proof and boundary cases. Existing
standard, border, and endpoint-chain lifts remain attributed to the
earlier cited notes. No negative decision for a relative relabeling is
asserted here, and no new 18-dimensional word is claimed until a separate
literal certificate is supplied and checked. The all-k exact goal remains
open.

Independent internal review: team task `exact_equality_structure` read
Sections 3–5 and reported PASS on
2026-09-08, including strict block inequalities, simultaneous-minima
recursion, the last-pair-growth guard, and same-size cap equivalence.
This is an internal proof review, not external certification.
