# K16 trimmed lift: fixed-base high-shore compression no-go

Date: 2026-07-30  
Lane: R  
Status: proved.  This closes every length-three rewrite confined to the
transformed high shore of the authenticated trimmed lift.  It does not close
blocks which alter the first copy or move the central singleton.

## 1. Frozen positions

Let `V={0,...,14}`, let `z` be coordinate 15, and let

```text
A = answers/k15.word,
|A| = n = 6438,
SHA-256(A) = f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b.
```

The authenticated standard lift is

\[
 Q=A\ \Vert\ [\{z\}]\ \Vert\
 [\{z\}\cup A_0,\ldots,\{z\}\cup A_{n-2}],                 \tag{1.1}
\]

with zero-based physical positions

```text
A                  Q[0:6438],
{z}                Q[6438],
transformed shore  Q[6439:12876].
```

A three-cell saving which leaves `A` and its following singleton fixed has
the form

\[
                 Q'=A\ \Vert\ [\{z\}]\ \Vert\ H,             \tag{1.2}
\]

where `H` has exactly

\[
                 12873-6438-1=6434                              \tag{1.3}
\]

nonempty letters on `V union {z}`.  No tagging assumption is imposed on the
letters of `H`.  Their old-coordinate projections may even be empty.  Thus
the theorem below is stronger than a no-go for words of the form `z|B'`.

## 2. The exact fixed-boundary obligations

For a letter `h` of `H`, write

\[
 \pi(h)=h\cap V,\qquad \epsilon(h)=1[z\in h].                  \tag{2.1}
\]

Let `Int_z(H)` be the old projections of intervals of `H` containing at
least one letter with `epsilon=1`.  Let `Pref(pi H)` include the empty prefix,
and let `Suff(A)` include the empty suffix.

### Lemma 2.1 (exact projected interface)

The word `Q'` is universal on `V union {z}` if and only if

\[
 2^V\subseteq
 \operatorname{Int}_z(H)\ \cup\
 \bigl(\operatorname{Suff}(A)\vee
                 \operatorname{Pref}(\pi H)\bigr).             \tag{2.2}
\]

### Proof

The intact first copy `A` covers every nonempty target avoiding `z`.  An
interval for `z union S` either lies wholly in `H`, in which case it must
contain a `z`-bearing letter and its old projection lies in `Int_z(H)`, or it
crosses the displayed central singleton.  In the second case its projection
is exactly a suffix union of `A` joined to a prefix union of `pi H`.  The
empty suffix and prefix include intervals starting or ending at the
singleton.  These alternatives are exhaustive and literal, proving both
directions.  QED.

Equation (2.2) is the complete boundary/compiler interface for this fixed
architecture.  There is no additional independent `COMP_3` assumption:
middle ownership and every lower/deeper contiguous-OR obligation are already
contained in (2.2).

## 3. Authenticated suffix fact

A linear replay of the source gives the complete distinct suffix profile

\[
 0,18033,20081,20083,20087,20215,24311,32503,32511,32767,      \tag{3.1}
\]

whose ranks are

\[
                         0,7,8,9,10,11,12,13,14,15.             \tag{3.2}
\]

In particular:

* there is no nonempty suffix of rank below seven;
* the unique rank-seven suffix state is

\[
                             T=18033=A_{n-1}.                   \tag{3.3}
\]

The reversed source has the same rank profile and unique rank-seven terminal
suffix `18553`.  The argument below applies verbatim in either orientation.

## 4. Forced middle ownership

There are

\[
                         {15\choose7}=6435                       \tag{4.1}
\]

targets `z union S` with `|S|=7`.

### Lemma 4.1 (all nonterminal rank-seven projections are internal)

If `Q'` is universal, then every rank-seven set `S != T` occurs as the OR of
the old projections on some interval of `H`.  This assertion concerns a
projected interval; the interval need not itself contain `z`.

### Proof

Take a witness for `z union S`.  If it lies in `H`, projecting gives the
required interval.  Otherwise it crosses the central singleton and has old
projection `U union P`, where `U` is a suffix state of `A` and `P` is a prefix
state of `pi H`.  If `U` is nonempty, (3.2) gives `|U|>=7`.  Since
`U subseteq S` and `|S|=7`, equality holds, so `U=S`; uniqueness in (3.3)
then gives `S=T`, contrary to the hypothesis.  Hence `U=0`, and the prefix
of `pi H` is itself an interval with OR `S`.  QED.

The empty-suffix case is why the statement is valid even for an all-untagged
prefix of `H`: a central witness is still a projected `H` interval.  Global
tagging is not being silently assumed.

### Lemma 4.2 (equality in the interval-antichain bound)

Let a word of length `L` have `L` distinct interval ORs of one fixed rank.
Then its `L` letters are exactly those `L` distinct masks.

### Proof

Choose one witness interval for every mask.  No chosen interval contains
another: containment of intervals implies containment of their ORs, and two
distinct sets of equal rank cannot contain one another.  Write the intervals
as `[l_i,r_i]` with increasing left endpoints.  Incomparability forces the
right endpoints to increase as well.  For `L` intervals in `[1,L]`, this
gives

\[
                         l_i\ge i,\qquad r_i\le i.               \tag{4.2}
\]

Thus every witness is `[i,i]`.  The masks are distinct, so the letters are
exactly their permutation.  QED.

### Corollary 4.3 (forced high-shore deck)

If `Q'` were universal, then the 6,434 projected letters of `H` would be a
permutation of

\[
             \{S\subseteq V:|S|=7\}\setminus\{T\}.             \tag{4.3}
\]

### Proof

Lemma 4.1 supplies 6,434 distinct rank-seven interval masks in a word of
length 6,434.  Apply Lemma 4.2.  QED.

This is the exact middle-ownership law for the fixed lift boundary.  The
terminal target `z union T` may use the left boundary interval
`A_{n-1},{z}`; every other marked middle target consumes one projected high
letter in the equality case.

## 5. Lower-rank contradiction

### Theorem 5.1 (fixed-base high-shore compression no-go)

There is no universal word of the form (1.2) with `|H|=6434`.  This remains
true when the entries of `H` are arbitrary nonempty 16-bit masks.

### Proof

Assume universality.  Corollary 4.3 says every nonempty projected letter of
`H` has rank seven (indeed all 6,434 do).  Consider the required target

\[
                              \{z,0\}.                           \tag{5.1}
\]

An interval lying in `H` has old projection containing at least one
rank-seven projected letter, so it cannot project to `{0}`.  A central
interval with empty `A` suffix and nonempty `H` prefix contains the first
rank-seven projected letter; with empty prefix it projects to zero.  A
central interval with nonempty `A` suffix has projection rank at least seven
by (3.2).  These exhaust Lemma 2.1, so `{z,0}` has no witness, a
contradiction.  QED.

The same proof works for any one-element old target and for the reversed
source orientation.

### Corollary 5.2 (no bounded transformed-shore replacement)

No replacement of a contiguous block of the transformed high copy by a
block three entries shorter can produce a universal length-12,873 word while
leaving `A,{z}` fixed.  In fact, rewriting the *entire* high shore cannot do
so.

This strictly supersedes pure three-deletion and adjacent-union no-gos within
this fixed architecture.

## 6. What a hypothetical three-cell saving would have to do

Before the final contradiction, equality already forces a global change.
The original projected transformed shore `A[:-1]` has rank histogram

```text
rank 1:   15
rank 2:  105
rank 3:  455
rank 4: 1365
rank 5: 4495
rank 6:    1
rank 7:    1
```

Its sole rank-seven entry is its first entry, `18553`.  Therefore any
contiguous replacement satisfying merely the forced deck (4.3) would have to
cover every old transformed index from 1 through 6436, a block of width at
least 6,436.  A genuinely bounded local block cannot even reach the forced
middle deck.  The lower-rank contradiction then shows that this global deck
rewrite is still insufficient.

Thus a successful length-three compression cannot remain in the one-low-copy,
one-central-singleton, one-high-shore architecture.  It must alter the first
copy or the position/role of the singleton, or use an interleaved multi-sector
chronology in which marked lower targets and marked middle ownership do not
compete for this same 6,434-cell shore.

## 7. Audit and model-size consequence

The lightweight checker

```text
scratch/audit_r_k16_trimmed_lift_high_shore_compression_nogo_20260730.py
```

hash-pins `A` and verifies, in each orientation:

* the complete suffix-rank profile `0,7,...,15`;
* the unique terminal rank-seven suffix;
* the transformed-shore rank histogram;
* the single original rank-seven transformed position; and
* the minimum 6,436-wide contiguous block covering all non-rank-seven
  transformed positions.

It is a linear audit with zero SAT variables, no quadratic interval
enumeration, and negligible memory.  The exact combinatorial proof then
closes the whole fixed-boundary class, so a CNF/C++ search for bounded
high-shore replacements would be both larger and logically unnecessary.

The pre-existing
`scratch/search_k16_trimmed_lift_tail_csp_20260730.py` is safe only as a
positive search: every SAT assignment is subjected to full literal replay.
Its model does not include general nonempty-source-suffix plus nonempty-high-
prefix central witnesses, so an UNSAT result from it is not an exact no-go for
its advertised family.  Theorem 5.1 supplies the missing no-go without using
that strengthened CSP.

## 8. Exact current incumbent outside the no-go class

The current partial length-12,873 word is

```text
scratch/k16_12873_repaired_partial.word
SHA-256 0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

An independent monotone ending-OR replay gives exactly

```text
length                         12873
missing masks                  10365, 52833, 52835
maximum ending-OR states       12
literal {z} position           6437
first divergence from Q        0
tagged / untagged entries      6376 / 6497
tag runs                       121
```

Here `10365` is an unmarked rank-eight target; `52833=z|20065` and
`52835=z|20067` are marked targets of old ranks seven and eight.  This file is
not universal and is not a solution.  It is also genuinely outside Theorem
5.1: it does not retain the prefix `A,{z}`, its singleton occurs at position
6437 rather than 6438, and its tagged and untagged cells are interleaved.

Consequently a repair of this three-hole incumbent must preserve or improve
its mixed-sector escape.  Normalizing it back to one intact low copy followed
by one singleton and one shortened high shore would enter the class excluded
by Theorem 5.1.

## 9. Exact scope boundary

The theorem assumes the displayed consecutive prefix `A,{z}` remains fixed.
It does not exclude:

* a replacement block crossing from `A` through the central singleton;
* moving or recompiling the singleton source;
* interleaving low and high sectors;
* replacing the first copy by another old-universal chronology; or
* an unrelated length-12,873 word.

Those classes require a new exact interface.  They cannot be certified by a
local high-shore CSP after Theorem 5.1.
