# The `k=15 -> 16` trimmed lift: exact witnesses and the three-deletion fusion gate

Date: 2026-07-30

Status: theorem-level structural audit and lightweight exact reconstruction.
Pure three-entry deletion from the standard lift is ruled out.  More
strongly, every length-`12873` word with the fixed old copy, a distinguished
seam singleton, and an arbitrary tagged terminal block is ruled out.  No
unrestricted length-`12873` conclusion is claimed.

## 1. Frozen source and reconstructed lift

Let

\[
 A=(a_1,\ldots,a_n),\qquad n=6438,
\]

be `answers/k15.word` on the old ground set (V=[15]).  Its SHA-256 is

```text
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b.
```

Let (z\notin V).  The standard trimmed lift is

\[
 L(A)=a_1,\ldots,a_n,\{z\},
       (\{z\}\cup a_1),\ldots,(\{z\}\cup a_{n-1}).       \tag{1.1}
\]

It has length (2n=12876).  Rendering masks as decimal integers separated
by one space and terminated by a newline gives SHA-256

```text
9d0214f6c7cea45a1f26d031687ecada9ac34500e925dcfc127bdf1514b624c8.
```

The ordinary trimmed-lift proof already proves universality.  A separate
lightweight ending-OR replay also obtains all (65535) nonempty masks.  The
replay is not a search and uses at most eleven distinct ending-OR states at
any position.

## 2. Notation for interval states

For a word (X=(x_1,\ldots,x_m)), write

\[
 \mathcal I(X)=
 \left\{\bigcup_{t=i}^j x_t:1\le i\le j\le m\right\}.       \tag{2.1}
\]

Write (\operatorname{Pref}(X)) for all prefix unions, including the empty
prefix (0), and (\operatorname{Suf}^+(X)) for all nonempty suffix unions.
For families of masks, (\mathcal P\vee\mathcal Q) denotes their pairwise
unions.  Deletion from a word always means order-preserving subsequence
deletion.

## 3. Exact witness classification for the unshortened lift

### Theorem 3.1 (all interval witnesses)

Put (A^-=(a_1,\ldots,a_{n-1})).  For every nonempty (S\subseteq V):

1. the intervals of (L(A)) with union (S) are exactly the intervals
   wholly inside the first copy (A) whose old union is (S);
2. an interval with union (S\cup\{z\}) is of exactly one of the following
   three forms:

   \[
   \begin{array}{ll}
   \text{transformed:}&
      (z\cup a_i),\ldots,(z\cup a_j),\quad 1\le i\le j<n;\\
   \text{singleton-prefix:}&
      z,(z\cup a_1),\ldots,(z\cup a_j),\quad 0\le j<n;\\
   \text{seam:}&
      a_i,\ldots,a_n,z,(z\cup a_1),\ldots,(z\cup a_j),
      \quad 1\le i\le n,\ 0\le j<n.
   \end{array}                                               \tag{3.1}
   \]

Here (j=0) means that no transformed entry is used.  Consequently the
family of old projections of all (z)-containing witnesses is exactly

\[
 \{0\}\ \cup\ \mathcal I(A^-)
 \ \cup\ 
 \bigl(\operatorname{Suf}^+(A)\vee\operatorname{Pref}(A^-)\bigr). \tag{3.2}
\]

#### Proof

Every letter from the singleton onward contains (z), while no letter in
the first copy does.  This proves part 1.  A (z)-containing interval starts
either in the transformed block, at the singleton, or in the old block.
These are the three mutually exclusive lines of (3.1).  Removing (z)
from their unions gives respectively an interval of (A^-), a prefix of
(A^-), or a suffix of (A) union a prefix of (A^-).  Nonempty prefixes
already belong to (\mathcal I(A^-)); the singleton supplies (0).  This
proves (3.2).  (□)

The usual trimmed-lift injection is a subfamily of (3.1): an old witness
([i,j]) is copied into the transformed block if (j<n), and is sent to
(a_i,\ldots,a_n,z) if (j=n).  Formula (3.2) records all additional seam
and cyclic-wrap witnesses, which are essential for any shortening argument.

## 4. Rigidity and the exact deletion criterion

Let (D_0\subseteq[n]) be deleted positions in the first copy, let
(E\subseteq[n-1]) be deleted transformed positions, and put

\[
 P=A-D_0,
 \qquad
 Q=A^- -E.                                                     \tag{4.1}
\]

### Theorem 4.1 (arbitrary deletion rigidity)

A deletion subsequence of (L(A)) is universal on (V\cup\{z\}) if and
only if all three conditions hold:

1. the singleton letter ({z}) is retained;
2. (P) is universal on (V), equivalently
   (\mathcal I(P)=2^V\setminus\{0\});
3. every old projection occurs in a retained (z)-witness:

   \[
   2^V
   =\{0\}\cup\mathcal I(Q)
    \cup\bigl(\operatorname{Suf}^+(P)
                    \vee\operatorname{Pref}(Q)\bigr).         \tag{4.2}
   \]

#### Proof

The only letter of the lift with old projection zero is the singleton
({z}), so that letter is necessary and sufficient for the target
({z}).  An interval for a target not containing (z) cannot meet the
tagged terminal part of the lift, hence it lies in (P).  This proves 2.
With the singleton retained, the proof of Theorem 3.1 applies verbatim to
the retained words (P,Q), and yields exactly (4.2).  The same classification
also proves sufficiency.  (□)

### Corollary 4.2 (all shortening deletions lie in the transformed half)

If (A) has minimum possible universal-word length on (V), then every
universal proper deletion subsequence of (L(A)) retains all of the first
copy (A).  Therefore a three-deletion reduction of the authenticated
(k=16) lift must delete exactly three entries of its transformed block,
and no other entries.

#### Proof

By Theorem 4.1, deleting even one old-copy entry would make the shorter word
(P) universal on (V), contradicting minimality of (A).  The singleton
cannot be deleted either.  (□)

For the present source, (\nu(15)=6438=n).  Hence a triple
(E\subseteq[n-1]) gives a length-(12873) word **if and only if**, for

\[
 Q=A^- -E,                                                     \tag{4.3}
\]

equation (4.2) holds with (P=A).  This is the exact pure-deletion gate;
it has no residence, compiler, or factor assumptions.

## 5. The four-block fusion theorem

Let (E=\{e_1<e_2<e_3\}) and split (Q=A^- -E) into its at most four
nonempty maximal retained blocks

\[
 C_0,C_1,\ldots,C_s,qquad s\le3.                              \tag{5.1}
\]

Write (U(C)) for the full union of a block.  For (i<j), put

\[
 M_{ij}=U(C_{i+1})\vee\cdots\vee U(C_{j-1}),                   \tag{5.2}
\]

with empty middle union equal to zero.

### Theorem 5.1 (exact three-deletion fusion formula)

The interval family of the erased transformed word is

\[
 \mathcal I(Q)
 =\bigcup_{i=0}^{s}\mathcal I(C_i)
 \ \cup\!
 \bigcup_{0\le i<j\le s}
 \left(
   \operatorname{Suf}^+(C_i)\vee\{M_{ij}\}
                     \vee\operatorname{Pref}^+(C_j)
 \right).                                                     \tag{5.3}
\]

Consequently (E) is a successful optimal deletion triple exactly when
the right-hand side of (5.3), together with

\[
 \operatorname{Suf}^+(A)\vee\operatorname{Pref}(Q)            \tag{5.4}
\]

contains every nonempty old mask.

#### Proof

An interval of (Q) either lies in one retained block or has a first and
last retained block (C_i,C_j).  In the latter case it consists of a suffix
of (C_i), every intervening block in full, and a prefix of (C_j).  This
gives (5.3) uniquely.  The second assertion is Corollary 4.2 and (4.2).
(□)

### Corollary 5.2 (rankwise fusion-capacity cut)

For every (1\le r\le15), a successful deletion triple must satisfy

\[
 \left|
 {V\choose r}\setminus\bigcup_{i=0}^{s}\mathcal I(C_i)
 \right|
 \le \left({s+1\choose2}+1\right)15
 \le105.                                                       \tag{5.5}
\]

#### Proof

After duplicate states are collapsed, every nonempty prefix or suffix OR
chain on a (15)-point ground set has at most fifteen states.  In a product
of two chains, the distinct outputs of one fixed rank form an antichain and
therefore number at most fifteen.  Each of the at most six fusion rectangles
in (5.3), and the one seam rectangle (5.4), contributes at most fifteen
rank-(r) masks.  (□)

Thus a proof-safe search need not treat all (2^{15}) old projections as an
unstructured universe.  It first checks the inherited within-block bank;
at each rank, at most 105 remaining targets can possibly be discharged by
the seven chain-product rectangles.

### Theorem 5.3 (pure three-deletion no-go for the authenticated lift)

No three entries can be deleted from the standard lift (1.1) while
preserving universality.

#### Proof

By Corollary 4.2, the three deleted entries would all have to lie in the
transformed block.  Thus (Q=A^- -E) has length

\[
 |Q|=6437-3=6434.                                             \tag{5.6}
\]

For any fixed left endpoint in an arbitrary word, its interval unions form
an inclusion chain as the right endpoint moves right.  Hence at most one
**distinct** rank-seven mask is witnessed from each left endpoint.  The last
retained entry of (Q) must be one of

\[
 a_{6434},a_{6435},a_{6436},a_{6437},                          \tag{5.7}
\]

because only three entries were deleted.  These four masks are respectively

```text
3170, 3169, 19521, 2657,
```

and all have rank five.  Therefore no rank-seven interval starts at the last
position of (Q), and

\[
 |\mathcal I(Q)\cap {V\choose7}|\le |Q|-1=6433.                \tag{5.8}
\]

It remains to count genuinely additional seam masks.  Every member of
(\operatorname{Suf}^+(A)) contains the final letter

\[
 a_{6438}=18033,
\]

which has rank seven.  Suffix unions form an inclusion chain.  Consequently,
if

\[
 s\vee p\in {V\choose7},\qquad
 s\in\operatorname{Suf}^+(A),\quad p\in\operatorname{Pref}(Q),
\]

then necessarily (s\vee p=18033).  Thus (5.4) contributes at most one
distinct rank-seven mask beyond (\mathcal I(Q)).  Notice that the
singleton-prefix family (\operatorname{Pref}(Q)) is already contained in
(\mathcal I(Q)); counting it again would be a double count.

The shortened lift therefore covers at most

\[
 6433+1=6434<{15\choose7}=6435                              \tag{5.9}
\]

of the (z)-tagged rank-seven targets.  This contradicts universality.
(□)

The same conclusion holds after reversing the displayed lift.  Reversal
does not change any interval-union family.  Equivalently, one may use the
dual bound of at most one distinct rank-seven mask per right endpoint: the
first retained transformed letter in the reversed orientation is one of the
same four rank-five masks in (5.7).

It also holds for the other standard orientation, namely applying the
trimmed lift to (A^{\mathrm{rev}}) (and, equivalently, reversing that
lift).  Its seam anchor is (a_1=18553), again of rank seven.  The final four
letters of its transformed base word are

\[
 a_5,a_4,a_3,a_2=109,8297,10345,8249,
\]

of ranks (5,5,6,5).  Three deletions cannot remove all four, so the same
one-per-left-endpoint argument gives at most 6433 internal rank-seven masks
and at most one additional seam mask.

There is also a valid proof from the weaker seam-capacity-two ledger, once
the interval-antichain stability step is included.  If $t$ distinct masks of
one rank are assigned witness intervals in a word of length $L$, those
intervals form a containment antichain.  After sorting them by left endpoint,

\[
 \ell_i\ge i,\qquad r_i\le L-t+i,
\]

so every chosen witness has length at most $L-t+1$.  The loose seam bound
two forces $t\ge6433=L-1$, hence all 6433 internal witnesses have length at
most two.  In $A^-$ there is exactly one rank-seven singleton and two
rank-seven inherited adjacent pairs.  Three deletions create at most three
new adjacencies, so the shortened word has at most six rank-seven intervals
of length at most two, a contradiction.  The seam-adds-only-one proof above
is shorter and strengthens the architecture theorem in Section 6, but it
does not invalidate this antichain proof.

## 6. Exact bounded transformed-block replacement

The same argument treats a bounded replacement without enumerating global
intervals.  Suppose a transformed base word has the form

\[
 Q=XCY.                                                        \tag{6.1}
\]

Then, with the usual empty-block conventions,

\[
\begin{aligned}
\mathcal I(Q)={}&\mathcal I(X)\cup\mathcal I(C)\cup\mathcal I(Y)\\
&\cup(\operatorname{Suf}^+(X)\vee\operatorname{Pref}^+(C))\\
&\cup(\operatorname{Suf}^+(C)\vee\operatorname{Pref}^+(Y))\\
&\cup(\operatorname{Suf}^+(X)\vee\{U(C)\}
                              \vee\operatorname{Pref}^+(Y)),   \tag{6.2}
\end{aligned}
\]

and

\[
\begin{aligned}
\operatorname{Pref}(Q)={}&\operatorname{Pref}(X)\\
&\cup(\{U(X)\}\vee\operatorname{Pref}^+(C))\\
&\cup(\{U(X)\vee U(C)\}\vee\operatorname{Pref}^+(Y)).       \tag{6.3}
\end{aligned}
\]

Equations (4.2), (6.2), and (6.3) are a necessary-and-sufficient certificate
for replacing a transformed block by any shorter tagged block.  If the new
block has (b) entries, then outside the unchanged internal witness bank,
at most

\[
 5\cdot15+\frac{b(b+1)}2                                      \tag{6.4}
\]

new rank-(r) projections can be supplied: five chain-product rectangles
and the internal intervals of the new block.  This is a capacity bound, not
an existence assertion.

The next lemma closes the entire fixed-first-copy architecture at the target
length, so (6.2)--(6.3) are chiefly useful for longer replacements or for
diagnosing which part of the architecture must move.

### Lemma 6.1 (saturation of the fixed-rank interval bound)

Let $C=(c_1,\ldots,c_L)$ be a word of arbitrary subsets of a $k$-point
ground set; empty $c_i$ are allowed.  For $0\le r\le k$,

\[
 \left|\mathcal I(C)\cap{[k]\choose r}\right|\le L.            \tag{6.5}
\]

If equality holds, then $c_1,\ldots,c_L$ are pairwise distinct $r$-sets,
and these singleton intervals are all the rank-$r$ interval unions.

#### Proof

For a fixed left endpoint $i$, the unions of $[i,j]$, $j\ge i$, form
an inclusion chain, and hence contain at most one distinct rank-$r$ set.
Summing over the $L$ left endpoints proves (6.5).

Suppose equality holds.  Then every left endpoint must contribute one new
rank-$r$ mask, distinct from the masks contributed by all other starts.
The last start has only the singleton interval, so $c_L$ has rank $r$.
Proceed backward.  Assume $c_{i+1}$ is an $r$-set.  If an interval
$[i,j]$ with $j\ge i+1$ has rank $r$, then either $c_i\subseteq
c_{i+1}$, in which case its union is $c_{i+1}$ until an outside coordinate
appears, or $c_i\not\subseteq c_{i+1}$, in which case its union already has
rank greater than $r$.  The former mask is already witnessed by the
singleton at start $i+1$, so it cannot be the required new mask.  Hence the
new mask at start $i$ must be the singleton $c_i$, which is an $r$-set.
Backward induction proves that every letter has rank $r$; equality also
forces them to be distinct.  Two distinct $r$-sets have union of rank
greater than $r$, so there are no further rank-$r$ interval unions.
(□)

### Theorem 6.2 (fixed-first-copy tagged-tail no-go)

Let $C=(c_1,\ldots,c_{6434})$ be **any** sequence of old-coordinate
subsets, including possibly empty subsets.  The word

\[
 A,\{z\},(\{z\}\cup c_1),\ldots,(\{z\}\cup c_{6434})          \tag{6.6}
\]

is not universal on sixteen coordinates.

#### Proof

Theorem 3.1 applies with $C$ in place of $A^-$.  Among old projections
of rank seven, the internal family $\mathcal I(C)$ has at most 6434
members by Lemma 6.1.  The seam family

\[
 \operatorname{Suf}^+(A)\vee\operatorname{Pref}(C)            \tag{6.7}
\]

contains at most one distinct rank-seven mask, because every old suffix
contains $a_n=18033$, already of rank seven.  The prefix-only projections
from intervals starting at the singleton are already members of
$\mathcal I(C)$ unless the prefix is empty.

To cover all ${15\choose7}=6435$ tagged rank-seven projections, equality
must therefore hold in Lemma 6.1.  All 6434 letters $c_i$ are consequently
distinct rank-seven sets.  It follows that every nonempty interval or prefix
of $C$ has rank at least seven.  Every nonempty seam projection in (6.7)
also has rank at least seven because it contains $a_n$.  Hence no target

\[
 \{z\}\cup S,\qquad 1\le |S|\le6,                              \tag{6.8}
\]

is witnessed, a contradiction.  (□)

The theorem includes arbitrary three-entry deletion and arbitrary replacement
of the complete transformed block, provided the first copy $A$ and the
distinguished singleton at the seam are fixed.  It does not cover a rethread
that changes the old copy, moves the only singleton into the tagged tail, or
uses letters with a different tag pattern.  Applying the theorem to
$A^{\mathrm{rev}}$, whose seam anchor $a_1$ has rank seven, gives the
other standard orientation as well.

### Corollary 6.3 (dimension-uniform fixed-anchor lower bound)

Let $A$ be any old-coordinate word whose seam-anchor letter $a_n$ has
rank $r\ge2$, and let $C$ be arbitrary.  If

\[
 A,\{z\},(\{z\}\cup c_1),\ldots,(\{z\}\cup c_m)              \tag{6.9}
\]

is universal on $V\cup\{z\}$, then

\[
 m\ge {|V|\choose r}.                                        \tag{6.10}
\]

Indeed, the seam contributes at most one rank-$r$ projection, while
Lemma 6.1 gives at most $m$ internal projections.  Thus
$m\ge {|V|\choose r}-1$.  Equality saturates Lemma 6.1, forcing every
$c_i$ to have rank $r$, after which no tagged target of old rank
$1,\ldots,r-1$ is possible.  Hence equality is excluded.

For the authenticated $k=15$ source this architecture therefore has
length at least

\[
 6438+1+{15\choose7}=12874.                                  \tag{6.11}
\]

The verified standard lift has length 12876, so a fixed-anchor uniformly
tagged-tail construction can save at most two letters, never the three
needed for the global lower bound.

## 7. Why canonical inherited witnesses alone cannot delete a letter

The lightweight exact source census gives:

* 25,105 old masks have exactly one interval witness in (A);
* all those unique intervals have length at most seven;
* only nine old masks have any witness ending at (n);
* for every transformed index (p\in[6437]), there is a mask (S_p) whose
  unique old witness is proper (ends before (n)), contains (p), and loses
  a coordinate when (a_p) is removed.

Therefore deleting any transformed letter destroys at least one witness in
the *canonical trimmed-lift injection*.  This does **not** prove that a
single deletion is impossible: another seam or fusion witness from (4.2)
may replace it.  It proves that any successful shortening must use exactly
the noncanonical fusion structure isolated in Theorem 5.1.

The unique-witness length histogram is

```text
1:3838, 2:3632, 3:6430, 4:6433, 5:3676, 6:1066, 7:30.
```

## 8. Sequential-safe deletion is not complete

The current draft program

```text
scratch/k16_trimmed_lift_delete_search_20260730.cpp
```

contains the assertion that every universal three-deletion subsequence can
be reached through universal one-deletion intermediates.  That assertion is
false for OR-universal words in general.

### Proposition 8.1 (explicit simultaneous-only triple)

On a three-point ground set, encode masks by (1,2,4), and let

\[
 W=(1,3,4,5,2,6,1).                                          \tag{8.1}
\]

The word (W) is universal.  Deleting positions (2,4,6) gives

\[
 U=(1,4,2,1),                                                  \tag{8.2}
\]

which is also universal.  However, deleting position 2 alone loses mask 3,
deleting position 4 alone loses mask 5, and deleting position 6 alone loses
mask 6.

#### Proof

In (W), masks 1 through 6 occur as letters and (3\vee4=7), so (W) is
universal.  In (U), the letters give (1,2,4), adjacent pairs give
(5,6,3), and an interval containing (1,4,2) gives 7.  The three stated
single-deletion failures follow directly: after the relevant unique letter
is removed, its two fusion providers remain separated by another inserted
letter.  (□)

Hence a DFS that branches only through currently universal single deletions
is a valid search for **sequential-safe** triples, but is not a complete
three-deletion search.  It would become complete for the authenticated lift
only after a separate lift-specific sequentialization theorem; no such
theorem is presently proved.  Direct evaluation by the four-block formula
(5.3) does not have this gap.

## 9. Exact frontier

The verified upper bound is (\nu(16)\le12876), while the deadline lower
bound is (12873).  Theorem 6.2 closes not only pure deletion but the entire
length-`12873` fixed-(A), fixed-singleton, uniformly tagged terminal-block
architecture.  A surviving lift-local modification must alter the old-copy
chronology, move the singleton/tag boundary, or use a mixed tag pattern.
An unrelated length-`12873` word also remains outside the theorem.

## 10. Audit artifact

The reconstruction and census are recorded by

```text
scratch/audit_threadA2_k16_trimmed_lift_witness_structure_20260730.py
  SHA-256 4d6d1da9e7e710a7dd6d3bec6fcd2a7e5d6c2e3b89c3445cbfa09c70eb3bd242
scratch/threadA2_k16_trimmed_lift_witness_structure_20260730.audit.json
  SHA-256 7504a74c47234602aa7bfdfda9d885215016ab1fdfa61f2b9fb398ec29c969cd
```

The audit reads and hash-checks the canonical source, reconstructs (1.1),
checks coverage by the monotone ending-OR recurrence, and records only source
interval statistics.  It performs no deletion search.
