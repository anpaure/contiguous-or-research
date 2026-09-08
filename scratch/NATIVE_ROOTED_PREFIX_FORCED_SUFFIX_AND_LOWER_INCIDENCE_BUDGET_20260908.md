# Forced suffix after the native rooted prefix

2026-09-08. Independent pure-proof audit. No mathematical program was run.

These are necessary conditions on an extension to length24313 covering
the complete17-cube. They do not assert that the native prefix can be
completed, or assume nu(17)=B(17).

## 1. Verified291-prefix inputs

The fixed user-supplied word is independently recorded in
USER_NATIVE35_GRAFT280_AND_ROOTED291_INDEPENDENT_CERTIFICATE_20260908.md,
with literal file native35_user_graft_20260908/native291_rooted_word.word.
Its verified data are

    n=291, D_8=D_9=288,
    number of distinct targets below rank9=836,
    b_9=3, b_8=2,
    L_9=E_9=E_8=0, L_8=1.

Here b_s counts recency prefixes of rank below s. It therefore has
836-288=548 distinct targets below rank8.
Its288 four-windows are distinct rank-nine owners, and all triple
windows except its first are distinct rank-eight targets.

## 2. Every remaining endpoint must be new at both middle ranks

The rank-eight and rank-nine layers each have24310 targets. There are
exactly24313-291=24022 positions left in a proposed length24313 extension,
and each layer is missing exactly24310-288=24022 targets.
At most one target of either fixed rank can be introduced at an endpoint.
Thus EVERY remaining endpoint must introduce a new rank-eight target
and a new rank-nine target.

An upward change in b_s cannot introduce a new rank-s target, by the
exact rank-budget lemma. Consequently both b_8 and b_9 are nonincreasing
throughout this suffix. At every new endpoint there is a rank-eight
prefix, so

    b_9=b_8+1.

Starting from (b_9,b_8)=(3,2), the only possible phases are
(3,2),(2,1),(1,0), in that order, allowing a phase to be skipped.
There can be at most two units of subsequent rank-nine potential drop.
These statements concern every hypothetical completing suffix; they
do not require a flat-middle assumption.

## 3. The initial phase really remains a flat four-window phase

Here is the local recurrence behind that assertion.
Suppose a state has exactly m prefixes below rank s, and a move leaves
that number equal to m while introducing a new rank-s target.
Write the old low prefixes as C_1,...,C_m and C_0=empty.
The m+1 candidate sets X union C_j include all new low prefixes.
A genuinely new rank-s target must also be among these candidates:
an old prefix already of rank s cannot give a new rank-s set by union.

Hence all m+1 candidates are distinct, the first m remain below rank s,
and the last is the new rank-s target. In particular the new low-prefix
vector is

    X, X union C_1, ..., X union C_(m-1),

and the new rank-s target is X union C_m.

At the end of the291 prefix, m=3 and its first three recency prefixes
are its literal suffix unions of lengths1,2,3: its rank-nine prefix is
reached by length4 and there are exactly three prefixes below it.
The displayed recurrence therefore preserves these literal identities
at every subsequent step with b_9=3. Thus each such step continues the
flat four-window middle-owner schedule, with a new rank-eight triple.

There is no inference here that an arbitrary optimal word must be flat.
Flatness is inherited from this particular prefix during its initial
constant-potential phase.

## 4. The actual census strengthens the generic block bound by34

The total number of nonempty targets below rank8 is

    sum_{j=1}^7 binom(17,j)=41225.

After the291 prefix,40677 of them remain unseen.
While b_8=2, an endpoint can introduce at most two such targets.
After its first decrease, every later endpoint has b_8<=1 and introduces
at most one.

Let a count how many of the24022 future endpoints remain in the
initial b_8=2 phase. Even allowing every available low prefix to be new,
the suffix can introduce at most

    2a+(24022-a)=24022+a

targets below rank8. Therefore

    a>=40677-24022=16655.                                  (1)

The first flat middle block must contain at least

    288+16655=16943 rank-nine owners,

or16946 physical letters including the initial three startup letters.
The first potential drop cannot occur earlier.

The generic count that ignores the actual rooted census gives16909
owners. The34-unit refinement has an exact interpretation:
the first three b_8 values are1,2,3 and every later prefix value is2,
so the291 prefix has2*291=582 low-prefix occurrences. Only548 are
distinct. Its34 repeated low occurrences are already spent and cannot
be made new by appending a suffix.

## 5. Reusable formula for a longer flat prefix

Append t steps while retaining the initial (b_9,b_8)=(3,2) phase and
introducing a new target at each of ranks8 and9 on every step.
Let g be the number of NEW distinct targets below rank8 in this extension.
Then g<=2t and the extended prefix has

    n=291+t,  D_8=D_9=288+t,  lambda=548+g.

The remaining number of positions is24022-t. Its initial flat phase
must have at least

    a_remaining>=16655+t-g

further positions. The total initial block therefore satisfies

    middle owners >=16943+(2t-g),
    physical letters >=16946+(2t-g).                         (2)

The quantity2t-g is exactly the additional number of repeated low-prefix
occurrences. Each further repeat raises the necessary total block length
by one. Producing two fresh lower targets per step preserves the current
bound; it does not reduce it.

More generally, for any prefix in this same startup/flat phase with n
letters, n-3 fresh targets at each middle rank, and lambda distinct
targets below rank8, the bound is

    total first-block owners >=16909+(2n-lambda).             (3)

Thus a certificate need only report n, lambda, and the preserved
new-middle/flat-phase conditions to update the necessary suffix budget.

## 6. The independently verified311 extension

The complete fixed-word census is recorded in
NATIVE291_TO311_OPTIMAL_SINGLETON_EXTENSION_20260908.md,
with literal word native35_user_graft_20260908/native311_all_singletons.word
and full census native35_user_graft_20260908/native311_all_interval_witness_census.json.
Its20-step extension has308 distinct targets at each of ranks8 and9,
893 targets below rank9, and every singleton. It retains b_9=3 and
exactly two below-eight prefixes at every appended endpoint. Consequently

    lambda=893-308=585,  g=585-548=37.

It adds2*20-37=3 repeated low occurrences, for37 in total.
Equations (2)-(3) then force

    first-block owners >=16946,
    first-block letters >=16949,
    further flat steps after the311 prefix >=16949-311=16638.

These are exact arithmetic deductions from the independently verified
fixed-word certificate, not an additional search or an assertion of
completion. This audit read the complete frontier record without rerunning
its mathematical programs.

## 7. Remaining construction question

The291 and311 words are real constructive progress for their named
target families. The rank budgets identify the required length and
fresh-target behavior of any successful continuation. They do not
supply the remaining24022 or24002 new middle/facet steps, all lower
targets, or the full upper layer.

The separate task of building an arbitrary-q recurrent native period
was interrupted by the new rate-proof audit before a general construction
was established. No generic reset, repeated middle target, or conditional
port diagram is being recorded as a solution to that task.
