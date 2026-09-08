# K17 explicit-lift owner compression: exact opposite-choice no-go

Date: 2026-07-31  
Status: solver-free exact theorem and authenticated finite replay  
Scope: direct one-occurrence-per-first-middle-owner compression of
`answers/k17_upper25746.word`; no unrestricted K17 no-go

## 0. Outcome

The certified length-25,746 K17 lift has exactly 1,433 excess rank-nine
first-middle deliveries:

\[
\begin{array}{c|r}
\text{rank-nine targets}&24{,}310\\
\text{first-middle deliveries}&25{,}743\\
\text{terminal stalls}&3\\
\text{jumps}&0\\
\text{flat duplicate extras}&4\\
\text{ghost duplicate extras}&1{,}429.
\end{array}
\]

Thus the numerical gap

\[
25{,}746-B(17)=25{,}746-24{,}313=1{,}433
\]

is literally the duplicate-owner waste.  This does **not** mean that the
duplicates can simply be quotient out.  The strongest direct quotient—keep
one delivered occurrence of each rank-nine label and order the kept labels
by physical start—is not upper complete.

The obstruction is cardinality-minimal.  The owner

\[
                         c=\mathtt{0x00dbd}
\]

has exactly two delivered occurrences, at starts 9,801 and 9,967.  The
rank-ten target `0x00fbd` forces the late occurrence, whereas `0x04dbd`
forces the early occurrence.  No one-occurrence owner transversal can cover
both targets.

Consequently the guarded-convex or laminar common-cap theorem cannot close
K17 by applying a lower compiler after this direct owner compression.  A
successful construction must alter the first-middle occurrence deck by a
physical contraction, deletion, rethreading, or value change, or use a
different source.

## 1. Authenticated first-middle inventory

Let

\[
                   A=(A_0,\ldots,A_{25745})
\]

be `answers/k17_upper25746.word`, SHA-256

```text
f8ea81ab1f8f1280f638e7e607b32a7dd53fc541b30fe1005db8aae692be031b
```

For each start \(p\), scan rightward to the first endpoint \(q(p)\) for
which

\[
              \left|\bigcup_{i=p}^{q(p)}A_i\right|\ge9.
\]

If the first crossing has rank nine, write

\[
              D_p=\bigcup_{i=p}^{q(p)}A_i.
\]

The exact waste identity partitions every start into a stall, a jump, or a
delivery and gives

\[
 L-\binom{17}{9}=s+j+f+g,                             \tag{1.1}
\]

where \(f\) and \(g\) are flat and ghost duplicate extras.  Literal replay
of the authenticated word gives

\[
 (s,j,f,g)=(3,0,4,1429).                              \tag{1.2}
\]

The three stalls are starts 25,743, 25,744, and 25,745.  Every earlier
start delivers rank nine, and all \(\binom{17}{9}=24{,}310\) labels occur.
Their occurrence multiplicities are

\[
                   1^{22979}2^{1230}3^{100}4^1.       \tag{1.3}
\]

The first-middle spans have histogram

\[
                   2^2 3^{6388}4^{12869}5^{6484}.     \tag{1.4}
\]

Equations (1.1)--(1.4) independently authenticate the asserted 1,433
duplicate-owner count; it is not inferred merely from the upper-bound gap.

## 2. The direct owner-compression model

For a rank-nine label \(c\), let

\[
             O(c)=\{p:D_p=c\}.
\]

A **direct owner compression** chooses one \(x_c\in O(c)\) for every
rank-nine label and orders the labels by increasing \(x_c\).  This produces
a 24,310-row rank-nine chronology.  Because first-middle deadlines are
monotone, any such distinct-label subsequence has strictly increasing
deadlines and is chain aligned.  The remaining issue is its upper spectrum.

### Lemma 2.1 (rank-ten adjacency reduction)

Let \(X\) have rank ten.  A direct owner compression contains a consecutive
block with union exactly \(X\) if and only if it has two adjacent selected
labels that are distinct rank-nine subsets of \(X\).

#### Proof

Every selected label in an exact \(X\)-block is a rank-nine subset of
\(X\).  The block contains at least two distinct labels, and any two distinct
rank-nine subsets of a rank-ten set have union \(X\).  In particular, its
first two selected labels form the required adjacent pair.  Conversely, any
such adjacent pair is itself an exact \(X\)-block.  \(\square\)

### Lemma 2.2 (physical adjacency criterion)

Fix occurrences \(p<q\) of two distinct labels \(c,d\).  They can be made
adjacent in a direct owner compression if and only if

\[
 \boxed{
   O(e)\not\subset(p,q)
   \quad\text{for every }e\notin\{c,d\}.}             \tag{2.1}
\]

#### Proof

If some third label has every occurrence strictly between \(p\) and \(q\),
its mandatory selected occurrence separates the endpoints.  Conversely, if
(2.1) holds, choose every third label occurring between the endpoints at one
of its occurrences outside the open interval.  Occurrence choices are
independent across labels, so after choosing \(c\) at \(p\) and \(d\) at
\(q\), no selected label remains between them.  \(\square\)

Lemmas 2.1 and 2.2 give a complete solver-free enumeration: for each of the
ten rank-nine subsets of \(X\), test every pair of its at most four physical
occurrences against (2.1).

## 3. The opposite-choice core

The pivot owner has occurrence domain

\[
 O(\mathtt{0x00dbd})=\{9801,9967\},                  \tag{3.1}
\]

with first-middle deadlines 9,805 and 9,971.

Complete application of Lemmas 2.1--2.2 gives:

| rank-ten target | all viable adjacent pairs | forced pivot choice |
|---|---|---:|
| `0x00fbd` | `0x00fb9@9966 -> 0x00dbd@9967` | 9967 |
| `0x02dbd` | `0x00dbd@9967 -> 0x02d9d@9968` | 9967 |
| `0x04dbd` | `0x00dbd@9801 -> 0x04db5@9802` | 9801 |

Each row has exactly one viable pair, not merely one pair in a restricted
local atlas.

### Theorem 3.1 (direct owner-compression no-go)

No direct owner compression of the authenticated length-25,746 word is an
upper-complete rank-nine carrier.

#### Proof

By the first and third rows of the table, upper completeness requires
simultaneously

\[
 x_{\mathtt{0x00dbd}}=9967,
 \qquad
 x_{\mathtt{0x00dbd}}=9801,
\]

which contradicts the exactly-one occurrence rule.  \(\square\)

The two-target, one-binary-owner pattern is cardinality-minimal: one target
cannot demand opposite choices, and an owner with one occurrence has no
choice.  The second table row is an independent late-choice check.

## 4. Relation to interval convexity, TU, and common caps

At the level of the three displayed upper rows, every candidate-pair
neighbourhood is a singleton, hence trivially interval convex.  The failure
is the partition constraint tying two physical occurrences to one owner
label.  In Boolean form the minimal core is simply

\[
          x_{\mathtt{0x00dbd},9967},qquad
          x_{\mathtt{0x00dbd},9801},qquad
          x_{9801}+x_{9967}=1.                        \tag{4.1}
\]

Thus consecutive-ones/TU on a marginal target--candidate matrix does not
remove owner-choice coupling.  A scalable positive bank must make each
required upper witness independent of the owner occurrence choice, absorb
the partition choice inside a laminar matroid, or physically rethread the
owner deck before applying the guarded compiler.

The lower common-cap assignment only begins after a rank-nine chronology,
its schedule, envelopes, and protected upper witnesses are fixed.  Theorem
3.1 says this direct chronology family already fails its upper-carrier gate;
lower caps cannot validate the guarded-convex construction theorem without
that hypothesis.  This does not rule out extra physical upper witnesses
outside the owner-union transfer architecture.

Selecting one owner occurrence also does not itself delete a physical
letter.  Therefore even an upper-complete owner transversal would still need
a separate, exact contraction theorem to turn 25,746 physical positions into
24,313.  Theorem 3.1 closes the proposed shortcut before that second issue.

## 5. Authentication and exact scope

The independent replay is:

```text
scratch/audit_k17_upper25746_owner_compression_nogo_20260731.py
scratch/k17_upper25746_owner_compression_nogo_20260731.audit.json
```

It reconstructs all first-middle endpoints directly from the word, verifies
the complete waste ledger, enumerates all physical occurrence pairs for the
three displayed targets, and checks criterion (2.1) literally.  It uses no
SAT, CP, LP, stochastic search, or imported candidate catalogue.

The scope is exactly the direct one-occurrence-per-delivered-owner
subsequence of the authenticated explicit lift.  Physical deletions,
contractions, value-changing caps that alter the owner deck, rethreaded
orders, other parent words, and unrestricted K17 equality remain open.
