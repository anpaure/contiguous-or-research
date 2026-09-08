# Initialized recency extensions, interleaving, and the exact k18 lower bound

Date: 2026-09-08. Independent pure-proof audit by `exact_b_induction`.

This note audits the finite statements supplied by root from the newest
user submission. No mathematical execution or literal-word verification
was performed by this author. The supplied file
`/Users/amir.nuriyev/Downloads/k18_optimal48623.word` has now passed the
separate independent first-occurrence census by `exact_b_finite_frontier`.
That execution is attributed in Section 7; its contents and coverage are
not premises of the standalone lower bound below.

The initialized-extension identity and interleaving bound pass with the
definitions below. The lower bound proves nu(18)>=48623 independently of
PBBS or any supplied construction. The separately checked literal word
attains it, so nu(18)=B(18)=48623. Exact equality in all dimensions does
not follow from this single finite case.

## 1. Recency states and their literal meaning

Let X be a finite alphabet. An ordered recency state is an ordered
partition P=(P_1,...,P_q) of X into nonempty blocks, in most-recent-first
order. Its nonempty prefix unions are P_1, P_1 union P_2, and so on.
For a nonempty update S subseteq X, define T_S(P) by prepending S,
removing its coordinates from every previous block, and deleting empty
blocks. Formally, an empty update leaves the state unchanged.

For a word A whose total union is X, obtain P_A by scanning its letters
backward, recording at each step the coordinates not seen at a later
step, and deleting zero increments. Its prefix unions are exactly the
distinct nonempty suffix ORs of A. Indeed each backward scan step enlarges
the current suffix union by precisely the recorded increment.

After appending a letter S, the suffix unions are S itself and S union C
for the old suffix unions C. Deleting repetitions produces exactly the
prefix unions of T_S(P_A). Thus, after any appended sequence, every
displayed recency prefix has an actual ordinary suffix-interval witness
at that time. Conversely every nonempty suffix-interval OR is one of
those prefixes. This remains true with empty projected updates if one
also records the empty suffix OR separately.

## 2. The initialized update number

For a complete recency state P on X, define lambda_X(P) to be the minimum
number l of nonempty updates S_1,...,S_l such that the union of the
nonempty prefix decks of

    P, T_(S_1)(P), ..., T_(S_l)...T_(S_1)(P)

contains every nonempty subset of X. The initial state is included.
The minimum is finite: appending every nonempty target as its own update
is one finite candidate.

For |X|=k>=1, let W(k)=binomial(k,floor(k/2)). Each state is a chain
and therefore contains at most one target of any fixed rank. Taking a
rank of size W(k), lambda+1 states must cover W(k) targets. Hence

    lambda_X(P)>=W(k)-1.                                (2.1)

For k=0 the sole state is empty and lambda=0, so the same numerical
inequality holds trivially with W(0)=1; no rank-zero target is incorrectly
included in the nonempty target family.

## 3. Exact all-marked extension identity

Let A be a universal word on X, and let z be a new coordinate. Define
Ext_z(A) as the minimum number of letters appended to A to make a
universal word on X union {z}, under the restriction that EVERY appended
letter contains z. Write each appended letter as Q_i union {z}, where
Q_i subseteq X can be empty. This definition measures added length, not
the total length of the extended word.

**Theorem.**

    Ext_z(A)=1+lambda_X(P_A).                            (3.1)

**Lower bound.** Any universal extension has a witness for {z}. Because
A has no z and all its letters are nonempty old sets, that witness lies
entirely in the appended block. Its old projection is empty, so at least
one appended Q_i is empty. Delete all empty Q_i when forming the sequence
of projected nonempty updates. Empty updates do not change recency state.

Every target D union {z}, D nonempty, has a witnessing interval ending
at an appended position. Its old projection D is a suffix OR of the
projected word A,Q_1,...,Q_i, so it is a prefix of the current recency
state. After ignoring empty updates, that state is either the initial
P_A or the state after one of the retained nonempty updates. Thus the
initial state together with those retained updates covers every nonempty
D in the sense defining lambda. If the extension has t letters, there
are at most t-1 retained nonempty updates, so t>=lambda_X(P_A)+1.

The argument does not assume that the first appended letter was {z}.
It also does not claim that all initial prefixes were already witnessed
with z in an arbitrary candidate extension. It only uses that including
the initial state gives a valid initialized update cover.

**Upper bound.** Take an optimal initialized sequence S_1,...,S_l and
append

    {z}, S_1 union {z}, ..., S_l union {z}.               (3.2)

At the first appended letter, every prefix of P_A has its old suffix
witness followed by {z}; this covers the initial prefix deck with z.
At each later appended position, the recency-prefix interpretation from
Section 1 gives an old-projection suffix witness in A,S_1,...,S_i.
Its lifted interval ends at a tagged letter and hence contains z. If it
extends back into A, it also crosses the initial singleton bridge; that
adds no old coordinate. Thus every displayed initialized target becomes
an actual tagged target. The singleton {z} is explicit, and all z-free
targets remain inside A. This proves the upper bound and (3.1).

In particular Ext_z(A) depends only on P_A once A is known universal.
This is a statement about extensions with one contiguous appended marked
block. It does not constrain arbitrary interleaved constructions by the
same exact identity.

## 4. General interleaving bound

Let V be any word of nonempty subsets of X union {z}, of length N.
Let m_z be its number of letters containing z. Let R_z be the number of
maximal runs of letters avoiding z that occur after a letter containing z.
Equivalently, R_z is the number of adjacent marked-to-unmarked transitions.
An initial unmarked run is not counted.

Let D_(z,s) be the number of distinct rank-s targets containing z that V
realizes by ordinary intervals. For 1<=s<=|X|+1,

    D_(z,s)<=m_z+(s-1)*R_z.                              (4.1)

**Proof.** The rank-s targets having a witness ending at a marked position
number at most m_z: all suffix unions at a fixed endpoint form a chain,
which contains at most one distinct rank-s set. It remains to count
targets witnessed at unmarked endpoints. Such a witness must contain an
earlier marked letter, so its endpoint lies in one of the counted runs.

Fix such a run. Let p be the marked position immediately preceding it,
and let B_j be the union of the first j unmarked letters of this run.
All unmarked letters are nonempty, so the distinct B_j form a nonempty
increasing chain. A witness ending at its j-th position and containing z
has union

    C union B_j,

where C is a suffix union of the fixed prefix of V ending at p. All such
C contain z, since their last letter does. If the resulting target has
rank s, then |B_j|<=s-1. There are at most s-1 distinct B_j of those sizes.
For any one B_j, its unions with the fixed suffix chain C again form a
chain and give at most one distinct rank-s target. This yields at most
s-1 targets for the entire run. Summing over runs proves (4.1).

When s=1 no target {z} can have an unmarked endpoint, since that endpoint
would add a nonempty old set. Thus the same inequality holds with the
run contribution zero. Division by s-1 in the next consequence is used
only for s>=2.

## 5. Consequence for universal words and relation to earlier results

If V is universal, deleting every marked letter leaves a universal word
on X. Indeed every old-target witness originally used only unmarked
letters, so its positions remain consecutive after deletion. Thus

    N-m_z>=nu(k), where k=|X|,
    m_z<=N-nu(k).                                       (5.1)

Universality gives D_(z,s)=binomial(k,s-1). Combining (4.1) and (5.1),
for 2<=s<=k+1,

    R_z>=max(0,ceil((binomial(k,s-1)+nu(k)-N)/(s-1))).    (5.2)

Applying the same argument to the reversed word gives the identical
bound on the number of unmarked-to-marked transitions.

This is the run-form version of the earlier entrance/exit capacity
bound in
`scratch/EXACT_B_ENTRANCE_EXIT_CAPACITY_AND_INDUCTION_OBSTRUCTION_20260908.md`,
Sections 2–4, with old projection rank s-1. That note also retains the
finer boundary-dependent cut charge. The present proof is independently
valid; the structural transition inequality should not be represented as
a previously unavailable all-dimensional theorem. The earlier note's
Section 5 already lists the 18-to-19 value 541 using the lower bound
B(18)=48623. Thus neither that number nor its necessary-condition status
is new: exact nu(18) now proves attainment of the old lower bound and
reconfirms the same transition constraint.

Specifically, if a universal 19-coordinate word has N=B(19)=92381 and
nu(18)=48623, take s=10. Since binomial(18,9)=48620,

    48620+48623-92381=4862=9*540+2.

It must have at least 541 exits and at least 541 entrances for EACH of its
19 coordinates. In particular it has at least 1082 tag transitions per
coordinate. This is a necessary condition for exact attainment at 19,
not a proof that such a word cannot exist.

## 6. Standalone endpoint lower bound in dimension 18

The following proof requires only ordinary interval unions. Let a universal
word on 18 coordinates have length N. Write

    W=binomial(18,9)=48620,
    Lambda=sum_(j=1)^8 binomial(18,j)=106761.

The latter equality also follows from symmetry:
Lambda=(2^18-binomial(18,9))/2-1.

Choose one witnessing interval for each of the W distinct rank-nine
targets. Two chosen intervals cannot have the same left endpoint: their
unions would be comparable by inclusion and have equal cardinality,
hence be identical. They also cannot have the same right endpoint, nor
can one properly contain another, by the same equal-rank argument.
Therefore N>=W. Order them by increasing left endpoints and write

    [l_i,r_i], 1<=i<=W.

Their right endpoints are strictly increasing too, because otherwise
two intervals would be nested. If N=W+t, t>=0, both ordered endpoint
lists satisfy

    i<=l_i<=i+t,  i<=r_i<=i+t.                          (6.1)

For each a=1,...,W, the interval [a,a+t] is valid and contains
[l_a,r_a], by (6.1). Thus every (t+1)-letter interval has union of rank
at least nine. Every longer interval contains such a window, so every
target of rank at most eight must have a witness of length at most t.

For t=0 there are no such nonempty intervals, already a contradiction.
In general their number is

    sum_(j=1)^t (N-j+1)=tW+t(t+1)/2.                    (6.2)

Consequently Lambda<=tW+t(t+1)/2. If t<=2, the right side is at most

    2W+3=97243<106761=Lambda,

a contradiction. Hence every universal word has

    N>=W+3=48623.                                      (6.3)

All valid (t+1)-windows, the t=0 case, and the preliminary N<W case are
covered explicitly. This is the same endpoint mechanism as the earlier
standalone17 proof, with its 18-dimensional rank counts substituted.

## 7. Separately executed literal certificate and scope

`exact_b_finite_frontier` has independently verified that the supplied
48623-letter file covers all 262143 nonempty targets by ordinary
nonwrapping intervals. Its first-coordinate-occurrence algorithm groups
equal event positions and visits 607684 OR-change events, with no use of
the ending-suffix recurrence. The single h100 run took approximately
0.550 seconds under 30 CPU seconds, 45 wall seconds and 1 GiB limits.
The literal SHA-256 is

    6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5.

The full independently authored certificate is
`scratch/K18_OPTIMAL48623_INDEPENDENT_FIRST_OCCURRENCE_CERTIFICATE_20260908.md`,
with the report, literal word and all ordinary interval witnesses under
`scratch/k18_optimal48623_first_occurrence_20260908/`. This author read the
certificate but did not rerun that computation. Root is conducting the
separate ending-suffix and interval-replay verification.

Together with (6.3), the checked literal gives nu(18)=B(18)=48623. No PBBS
construction history or initialized-update optimality claim is needed
for that conclusion. The numerical substitution in Section 5 can now use
the proved finite optimum, but already followed from the previously
established lower bound and was explicitly recorded earlier.

The separate identity (3.1) can certify optimality of an all-marked
extension once its actual decomposition and initialized coverage are
established. This note does not infer such a decomposition merely from
the total length of an arbitrary supplied word. The exact finite upper
bound is attributed to the literal certificate above, while the general
extension and transition theorems are the pure proofs of this note.
