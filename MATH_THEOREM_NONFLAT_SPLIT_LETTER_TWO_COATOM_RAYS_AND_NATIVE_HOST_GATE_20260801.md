# One nonflat split carries both mixed-coatom rays, but the native packet has no dominating host

Date: 2026-08-01  
Lane: split-letter / mixed-coatom compiler / exterior host gate  
Status: exact conditional one-letter theorem and exact native-host obstruction.
The theorem preserves unrestricted interval-OR witnesses by a one-unit
deadline staircase.  It does not construct the required dominating source
letter in a Pascal child and does not preserve one fixed derivative row.

## 0. Outcome

The two canonical mixed-coatom lower chains do **not** require two inserted
letters.  One added position carries both complete chains, provided the old
word already contains one actual source letter which is their joint
dominating host.

For `2<=q<=d`, write

\[
 P_q=\{f_1,\ldots,f_{d+1-q}\},\qquad
 S_q=\{f_q,\ldots,f_d\}.                                  \tag{0.1}
\]

Let `A,B` be the two canonical active bases, including the suppressed fixed
core.  The desired occurrence-labelled target bank is

\[
             A\cup P_q,\qquad B\cup S_q,
                         \qquad 2\le q\le d.                \tag{0.2}
\]

Put

\[
 Z=A\cup\{f_1\},\qquad T=B\cup\{f_d\},\qquad X=Z\cup T.   \tag{0.3}
\]

If an old source word has the local form

\[
 \ldots,\{f_{d-1}\},\{f_{d-2}\},\ldots,\{f_2\},
 X,
 \{f_{d-1}\},\{f_{d-2}\},\ldots,\{f_2\},\ldots,          \tag{0.4}
\]

where the displayed side lists are empty for `d=2`, replace the single
letter `X` by the consecutive block

\[
                              Z,T.                           \tag{0.5}
\]

Then the intervals ending at `Z` give the entire `A`-prefix chain and the
intervals beginning at `T` give the entire `B`-suffix chain.  Every old
interval value survives by contracting `Z,T` back to `X`.  Thus the exact
answer at the unrestricted OR-word level is:

\[
             \boxed{\text{one split, not two, is sufficient.}}          \tag{0.6}
\]

This is not the common-star insertion ruled out by the one-cell fan-trace
obstruction.  Here the two new rays have different singleton endpoints `Z`
and `T`.  Intervals containing both pieces are transported old intervals;
no claim is made about the new fixed-width crossing row.

The host hypothesis is load-bearing.  In the authenticated canonical
mixed-coatom maximal erosion, no source envelope in either phase contains
`X`.  The positive theorem therefore converts the two-chain problem into a
sharp exterior planting problem; it does not solve that problem inside the
native packet.

## 1. Universal two-endpoint split

Let `W=(W_0,...,W_(N-1))` be a word of nonempty sets and suppose

\[
                            W_r=X=Z\cup T                   \tag{1.1}
\]

with `Z,T` nonempty.  Replace `W_r` by the ordered pair `Z,T`, obtaining
`W tilde`.

### Lemma 1.1 (full-block contraction)

The map

\[
 [a,b]\longmapsto
 \begin{cases}
 [a,b],&b<r,\\
 [a+1,b+1],&a>r,\\
 [a,b+1],&a\le r\le b
 \end{cases}                                                \tag{1.2}
\]

is injective on old physical intervals and preserves their literal OR
values.

#### Proof

An interval avoiding `r` is unchanged up to the index shift.  An interval
containing `r` contains both new pieces in its image, whose union is the old
letter `X`.  The three image classes are disjoint, so the map is injective.
\(\square\)

Consequently every named old lower, middle, upper, screen, residence or
topology witness survives as the same set value and in the same declared
order.  A witness containing `r` grows in length by exactly one; every other
witness retains its old length.  This is an unrestricted interval statement,
not a fixed-width statement.

The new physical cells outside the full-block transport image are precisely
the two endpoint rays (their values may duplicate old values)

\[
 Z\cup\bigcup_{i=a}^{r-1}W_i,
 \qquad
 T\cup\bigcup_{i=r+1}^{b}W_i.                              \tag{1.3}
\]

Every interval containing both `Z` and `T` is already a full-block lift.

## 2. Exact mixed-coatom construction

Index the old local positions around the host by

\[
                  -(d-2),\ldots,-1,0,1,\ldots,d-2.          \tag{2.1}
\]

Set `W_0=X` and, for `1<=s<=d-2`, put

\[
                         W_{-s}=\{f_{s+1}\},\qquad
                         W_s=\{f_{d-s}\}.                   \tag{2.2}
\]

Equation (2.2) is exactly the physical order (0.4).  Split `W_0` as in
(0.5).  For `1<=h<=d-1`, let `I_h^-` be the interval from `W_(-(h-1))`
through `Z`, and let `I_h^+` be the interval from `T` through `W_(h-1)`.
At `h=1` these are the singleton cells `Z` and `T`.

### Theorem 2.1 (one split carries both complete chains)

For every `1<=h<=d-1`,

\[
 \begin{aligned}
  \operatorname{OR}(I_h^-)
     &=A\cup\{f_1,\ldots,f_h\}
       =A\cup P_{d+1-h},\\
  \operatorname{OR}(I_h^+)
     &=B\cup\{f_{d-h+1},\ldots,f_d\}
       =B\cup S_{d+1-h}.                                  \tag{2.3}
 \end{aligned}
\]

The `2(d-1)` displayed cells are distinct.  For the canonical mixed-coatom
bases their target values are also pairwise distinct.  The source length
rises by exactly one, and every old interval target survives.

#### Proof

The left interval of height `h` contains `Z=A+f_1` and the successive
letters `f_2,...,f_h`.  The right interval contains `T=B+f_d` and the
successive letters `f_(d-1),...,f_(d-h+1)`.  This proves (2.3).  The two
families lie on opposite sides of the split boundary and have different
endpoints, so their physical cells are distinct.  Canonical `A,B` have
different private active labels, so a left target cannot equal a right
target; strict filler growth gives distinctness within each chain.  Lemma
1.1 proves preservation of the old word. \(\square\)

The construction was replayed through `d=64`; the identities themselves are
dimension-free.

### Corollary 2.2 (exact host criterion)

The singleton side letters in (2.2) are only a convenient sufficient normal
form.  For a fixed old word and a proposed decomposition `X=Z union T`, one
split realizes (0.2) if and only if, for every `1<=h<=d-1`, the actual
outward cumulative unions satisfy

\[
 \begin{aligned}
 Z\cup\bigcup_{s=1}^{h-1}W_{r-s}
    &=A\cup P_{d+1-h},\\
 T\cup\bigcup_{s=1}^{h-1}W_{r+s}
    &=B\cup S_{d+1-h}.                                    \tag{2.4}
 \end{aligned}
\]

In particular, nesting and cardinality alone are insufficient.  The common
host, its ordered split, and both literal outward traces are necessary.

## 3. Why the common-star no-go does not apply

In a common-star insertion the two fan chains share one singleton payload
`Y`.  Complementary prefix/suffix chains then force each lost crossing value
to contain both private active labels and the complete filler flag.  This is
the exact source of the constant-owner and zero-crossing-incidence
obstructions.

The split (0.5) has no common singleton fan:

\[
                  I_1^-=Z\ne T=I_1^+.                       \tag{3.1}
\]

An interval which crosses from the left of `Z` to the right of `T` contains
the complete block `Z,T` and is the full-block lift of an old interval.
Its value is protected by Lemma 1.1 and its length is allowed to increase.
The construction never asks the shortened new crossing cells to equal the
opposite packet chain and never asks the new fixed-length middle row to be
simple or flat.  Hence the common-star trace equation is not contradicted;
its hypothesis is absent.

## 4. Exact host assumptions

Theorem 2.1 may be used inside a larger construction only after all of the
following are certified.

1. **Actual-letter host.**  `X` is one literal nonempty source letter in the
   old reference word.  It is not enough that `X` lie in a carrier owner, in
   a maximal envelope union, or in a longer interval.
2. **Exact decomposition.**  The two nonempty pieces satisfy `X=Z union T`
   exactly.  Their overlap `A cap B` is allowed.
3. **Two ordered traces.**  The actual neighbouring source letters satisfy
   (2.4), with no contaminating coordinate.
4. **Protected reference word.**  The old word already carries the target,
   owner, upper, residence and common-cap witnesses intended to survive.
   Lemma 1.1 transports them but does not create them.
5. **Deadline permission.**  Every protected witness containing the host may
   use one additional position.  A rigid compiler-width or flat-derivative
   architecture needs a separate overflow argument.
6. **New-position legality.**  If source positions have individual caps or
   recursive roles, both new positions must be certified.  The inclusions
   `Z,T subseteq X` do not by themselves manufacture the cap of the added
   physical position.

The split uses both singleton side cells as the depth-`d` chain endpoints.
It supplies no additional unpriced typed-task socket.

## 5. The canonical packet has no native host

For the authenticated `0110` mixed-coatom packet, suppress the fixed core
temporarily.  The active parts of the two bases are triples `A,B` with

\[
                     |A|=|B|=3,qquad |A\cap B|=2,qquad
                     |A\cup B|=4                                  \tag{5.1}
\]

before the fixed core is adjoined.  The required host (0.3) contains the
four active labels of `A union B` and the two filler labels `f_1,f_d`.

Let `K` be the fixed core, `|K|=r-d-4`.  Then

\[
 |Z|=|T|=|K|+4=r-d,qquad |X|=|K|+6=r-d+2.              \tag{5.2}
\]

### Theorem 5.1 (native maximal-erosion host obstruction)

No singleton source envelope in either canonical packet phase contains
`X`.  In particular, neither of the two native depth-`d` provider positions
can host the split (0.5).

#### Proof

Every coatom-block owner has one active triple.  A lower screen has only the
intersection of its adjacent active triples.  An upper screen has their
four-label union, but it is isolated between coatom blocks.  A maximal
depth-`d` source envelope is the intersection of `d+1` consecutive owners.
Since `d>=2`, every such window contains a block owner; its active part is
therefore contained in a three-label triple.  It cannot contain the
four-label set `A union B`, and hence cannot contain `X`.

At the two native `q=d` providers the obstruction is visible already from
rank: their envelopes are respectively `A+f_1` and `B+f_d` in the old phase,
with `A,B` swapped in the new phase.  Each has rank `r-d`, two below the
required host rank in (5.2). \(\square\)

Thus the one-split theorem is a genuine `+1` compression theorem, but its
application to the mixed-coatom packet requires an exterior or separately
planted dominating letter with both ordered traces.  The authenticated
native packet does not supply that letter.

## 6. Audit

Run

```text
python3 scratch/audit_nonflat_split_letter_two_coatom_rays_native_host_20260801.py
```

The replay checks:

* the complete interval-contraction injection and both ray formulas for
  every `2<=d<=64`;
* all `2(d-1)` occurrence-labelled chain cells and target distinctness; and
* every singleton maximal-erosion envelope in the padded authenticated
  tensor, for all three positive rows, both phases and every `2<=d<=32`.

It reports

```text
PASS_NONFLAT_ONE_SPLIT_TWO_COATOM_RAYS_AND_NATIVE_HOST_NOGO
```

with hashes

```text
audit script SHA-256:
08775d142ccb022a05a99ad8d04124802828b53772d10300a70f3c3659722989

audit JSON SHA-256:
5abdcd583df6a1ef02c52aff183aa88ecbe635da8ce6312168acfea34da28458

canonical payload SHA-256:
c7633558124ee97167ea52299ec210ab045458e6bb44872abc4b29189ed8fb2a

authenticated connector source SHA-256:
fcf0075ab1c591302008b0d9f31a35ac4948b85ae3fca6997157e4158c75b627
```

Dependencies:

* `MATH_THEOREM_H1_SPLIT_LETTER_RAY_ABSORPTION_AND_ONE_COLUMN_CRITERION_20260801.md`;
* `MATH_AUDIT_H2_SPLIT_LETTER_BLOCK_CONTRACTION_AND_TASK_HOSTING_20260801.md`;
* `MATH_THEOREM_INDEPENDENT_COATOM_TWO_CHAIN_PROVIDER_SWITCH_AND_SERIAL_LAMBDA_GATE_20260801.md`; and
* `MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md`.
