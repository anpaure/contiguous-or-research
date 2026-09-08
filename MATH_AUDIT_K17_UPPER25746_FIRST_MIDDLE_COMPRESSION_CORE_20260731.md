# The 1,433 first-middle duplicates in the explicit K17 upper word

Date: 2026-07-31  
Status: exact inventory and solver-free scoped compression no-go  
Scope: the authenticated length-25,746 lift and phase-preserving
first-middle occurrence transversals only

## 0. Result

The gap \(25746-B(17)=1433\) is exactly the duplicate excess in the
first-rank-nine delivery ledger, but the duplicates split into two different
types:

\[
                 \boxed{1433=1429\text{ ghosts}+4\text{ flats}.}     \tag{0.1}
\]

The 1,429 ghosts are all on the pure-old, unmarked shore.  Selecting one
raw occurrence of each unmarked rank-nine target cannot preserve upper
completeness.  Two pure-old rank-ten targets force opposite occurrences of
the same repeated owner:

\[
 \begin{array}{c|c}
 \text{target}&\text{forced occurrence of }0x0bf5\\\hline
 0x1bf5&9176\\
 0x0ff5&10616.
 \end{array}                                           \tag{0.2}
\]

Thus the 1,429 choice-relevant duplicates cannot be compressed by a simple
order-preserving occurrence transversal.  The four marked extras are two
same-deadline flat groups and cannot repair either pure-old target.

This is not a no-go for a genuinely rethreaded length-24,313 word or for a
different common-cap assignment.

## 1. Exact first-middle inventory

The source is

```text
answers/k17_upper25746.word
SHA-256 f8ea81ab1f8f1280f638e7e607b32a7dd53fc541b30fe1005db8aae692be031b
```

From each left endpoint, extend right until the running OR first reaches
rank at least nine.  The exhaustive ledger is

\[
 \begin{aligned}
 L&=25746,\\
 \text{distinct delivered rank-nine targets}&=24310,\\
 \text{stalls}&=3,\\
 \text{jumps}&=0,\\
 \text{duplicate deliveries}&=1433.
 \end{aligned}                                         \tag{1.1}
\]

Hence

\[
                     25746=24310+3+1433.               \tag{1.2}
\]

The stalls are exactly the final three starts
`25743,25744,25745`.

Let \(z=2^{16}\) be the new coordinate.  The phase split is:

| shore | distinct targets | deliveries | multiplicity histogram | extras |
|---|---:|---:|---|---:|
| \(z\notin S\) | 11,440 | 12,869 | \(1^{10111}2^{1229}3^{100}\) | 1,429 ghosts |
| \(z\in S\) | 12,870 | 12,874 | \(1^{12868}2^1 4^1\) | 4 flats |

The two marked flat groups are

```text
target 0x1c3ca: right 12875, lefts 12873,12874
target 0x1f30c: right 12873, lefts 12869,12870,12871,12872
```

Within each group the left endpoints are consecutive and no other owner lies
between them.  All marked deliveries occur after every unmarked delivery.
Deleting a flat copy therefore gives no new ordering choice on the unmarked
shore.

## 2. Exact raw-interval criterion

Index the 12,869 unmarked deliveries by their left endpoint
\(p=0,\ldots,12868\), and write \(c_p\) for their rank-nine labels.  For a
label \(c\), let

\[
                         O(c)=\{p:c_p=c\}.             \tag{2.1}
\]

An occurrence transversal chooses one \(x_c\in O(c)\) for every distinct
label and reads the selected labels in increasing raw position.

### Lemma 2.1

For a fixed target \(S\), some occurrence choice makes a raw interval
\([a,b]\) a consecutive witness for \(S\) if and only if:

1. every blocker \(c\not\subseteq S\) has an occurrence outside
   \([a,b]\); and
2. the union of compatible labels having some occurrence in \([a,b]\) is
   \(S\).

#### Proof

A blocker can be kept out precisely when its occurrence domain is not
contained in the interval.  Compatible labels are independent choice
variables; selecting enough available compatible occurrences inside gives
the desired union, and every remaining compatible label may be placed
arbitrarily because it adds no bit outside \(S\).  Conversely, any selected
consecutive witness has these two properties.  \(\square\)

Multiplicity-one blockers split the raw line into short gaps.  The audit
enumerates every subinterval of every such gap and then checks all repeated
blocker domains literally.  The maximum gaps for the two core targets are
only nine and eight.

## 3. The opposite-choice core

The owner

\[
                         c=0x0bf5                     \tag{3.1}
\]

has exactly the two raw occurrences

\[
                         O(c)=\{9176,10616\}.          \tag{3.2}
\]

For \(S_1=0x1bf5\), Lemma 2.1 leaves exactly one feasible raw interval:

\[
                         [9175,9176].                  \tag{3.3}
\]

All compatible labels other than \(c\) have union `0x1bb5`, missing bit
`0x0040`; including \(c\) gives `0x1bf5`.  Thus (3.3) forces
\(x_c=9176\).

For \(S_2=0x0ff5\), the only feasible intervals are

\[
                  [10614,10616],\qquad[10615,10616].  \tag{3.4}
\]

In either interval, all compatible labels other than \(c\) have union
`0x0fe5`, missing bit `0x0010`; including \(c\) gives `0x0ff5`.  Hence every
witness forces \(x_c=10616\).

One occurrence transversal cannot satisfy both equations.  Therefore no
phase-preserving choice of one raw unmarked first-middle occurrence per
target is upper-complete.  This is a two-target, one-variable contradiction,
not a failure of a heuristic ordering.

The two pure-old targets cannot use a marked owner: any interval containing
a marked label contains \(z\), while neither target contains \(z\).
Consequently the four marked flats do not alter the core.

## 4. Relation to common-cap compilation

The result explains exactly why the numerical 1,433-owner surplus of the
explicit lift is not automatically compressible into an optimal carrier.
It is an upstream occurrence-order obstruction, before a lower common-cap
matrix is even defined.

It does **not** prove that 1,433 physical positions must remain.  Deleting
or changing letters can alter the delivery domains; rethreading can create
new upper witnesses; and a fresh length-\(B(17)\) carrier can have a different
staircase and common-cap bank.  Those operations lie outside the theorem.

## 5. Authentication

```text
scratch/audit_k17_upper25746_first_middle_compression_core_20260731.py
SHA-256 d7fdf657f965aca95d41764b803d353e9fcdee59a2b30de8ad5fc5da1dcd221f

scratch/k17_upper25746_first_middle_compression_core_20260731.audit.json
SHA-256 db82ea3203cd4866b872f4d38b9af493de15402ed6dbbe2f601f042db1b24cf3
payload 96074ba38b3c475863eaa09c0bc4484dbe8525545b9490fe840674138a0116a1
```

The audit independently reconstructs all 25,743 deliveries and all
rank-nine multiplicity domains directly from the word.  It imports neither
the earlier Pascal occurrence theorem nor a solver.
