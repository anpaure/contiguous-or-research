# One split pivot carries both coatom flags: exact two-ray criterion and the native-host gate

Date: 2026-08-01  
Lane: additive-constant regeneration / mixed-coatom compiler  
Status: exact conditional positive theorem, exact host obstruction for the
canonical full-ray normal form, and finite native-word replay.  A suitable
merged host is **not** present in the authenticated coatom tensor, so this is
not yet an unconditional `B(k)+1` construction.

## 0. Outcome

A split letter is strictly stronger than the previously studied inserted
one-cell star.  Replacing one actual old source letter

\[
                         X=Z\cup T
\]

by the consecutive block `Z,T` creates two independent exclusive rays: a
left ray with base `Z` and a right ray with base `T`.  Every old interval OR
is retained by contracting the block.

Consequently one split absorbs both canonical old-only mixed-coatom chains

\[
             A\cup P_q,\qquad B\cup S_q,\qquad 2\le q\le d,
\]

in a completely explicit local host.  Put

\[
 Z=A\cup\{f_1\},\qquad T=B\cup\{f_d\},\qquad X=Z\cup T,
\]

and assume the old local source already contains

\[
 \{f_{d-1}\},\ldots,\{f_2\},X,
 \{f_{d-1}\},\ldots,\{f_2\}.                         \tag{0.1}
\]

After replacing the one displayed `X` by `Z,T`, the left-exclusive ray is
the complete `A+P` flag and the right-exclusive ray is the complete `B+S`
flag.  The old local length is `2d-3`, the new local length is `2d-2`, and
the total physical cost is **exactly one position**.  The singleton filler
letters in (0.1) are old positions, not additional insertions.

The host hypothesis is load-bearing.  In the authenticated `0110` coatom
tensor, the merged letter `X` is not an actual source letter; indeed no
canonical maximal-erosion envelope contains it.  The two native flags also
occur at opposite ends rather than in the mirrored order (0.1).  Thus the
result identifies a sharp new host target, but does not claim it has already
been planted.

## 1. Universal two-ray split ledger

Write an old word locally as

\[
 \cdots,L_s,\ldots,L_1,X,R_1,\ldots,R_t,\cdots          \tag{1.1}
\]

and replace `X` by two nonempty letters `Z,T`.

### Theorem 1.1 (block contraction and the two exclusive rays)

The order-preserving contraction map preserves every old interval OR if
and only if

\[
                              X=Z\cup T.                    \tag{1.2}
\]

Under (1.2), the genuinely new intervals which meet exactly one half of the
split block include the two rays

\[
 \begin{aligned}
  \Lambda_i&=Z\cup L_1\cup\cdots\cup L_i &&(0\le i\le s),\\
  \mathrm P_j&=T\cup R_1\cup\cdots\cup R_j &&(0\le j\le t),
 \end{aligned}                                             \tag{1.3}
\]

where empty unions are omitted.  Every old named owner, lower match, and
upper witness survives with the same literal value.  An old witness
containing `X` has its deadline increased by one and every other witness
keeps its length.

#### Proof

An old interval avoiding `X` is copied.  An old interval containing `X` is
mapped to the interval containing both `Z,T`, whose union is unchanged
exactly under (1.2).  Necessity follows by applying preservation to the old
singleton cell `X`.  Intervals ending at `Z` but not containing `T`, and
intervals beginning at `T` but not containing `Z`, give (1.3).  \(\square\)

This theorem has no lost-crossing ledger: the old crossing cells are
transported to intervals one position longer.

## 2. Exact necessary and sufficient cut/label conditions

Let

\[
 C^-_0\subsetneq C^-_1\subsetneq\cdots\subsetneq C^-_s,
 \qquad
 C^+_0\subsetneq C^+_1\subsetneq\cdots\subsetneq C^+_t       \tag{2.1}
\]

be two occurrence-labelled target chains.

### Theorem 2.1 (consecutive full-ray criterion)

At the fixed old cut (1.1), the two chains occupy, in order, the consecutive
exclusive ray cells (1.3), including the two singleton bases, if and only if

\[
 \boxed{
 \begin{aligned}
  Z&=C^-_0, & T&=C^+_0, & X&=C^-_0\cup C^+_0,\\
  C^-_i-C^-_{i-1}&\subseteq L_i\subseteq C^-_i
      &&(1\le i\le s),\\
  C^+_j-C^+_{j-1}&\subseteq R_j\subseteq C^+_j
      &&(1\le j\le t).
 \end{aligned}}                                             \tag{2.2}
\]

In particular, (2.2) requires `X` to be one **actual old source letter**.
Containment of `X` in a source envelope is only a precursor; equality must
be realized in one common cap word.

#### Proof

The two singleton ray values force the first line.  Inductively, assuming
the preceding cumulative union is `C^-_(i-1)`, adjoining `L_i` gives
`C^-_i` exactly if and only if the second-line inclusions hold.  The right
shore is identical.  Theorem 1.1 supplies preservation.  \(\square\)

There is a more permissive, and still exact, fixed-cut form.  One may skip
ray addresses.  Then a split works if and only if there are nonempty
`Z,T`, with `Z union T=X`, and strictly ordered endpoint sequences such that

\[
 C^-_u=Z\cup\bigcup_{i=1}^{\ell_u}L_i,
 \qquad
 C^+_v=T\cup\bigcup_{j=1}^{r_v}R_j.                         \tag{2.3}
\]

Equation (2.3), not chain cardinality, is the complete direct-address
criterion.  It is also an `O(length * number-of-targets)` fixed-word test
after the possible split bases of `X` are enumerated.  Necessarily

\[
 X\subseteq C^-_0\cup C^+_0,
 \]

with `X` admitting a nonempty cover `X=Z union T`, `Z subseteq C^-_0`,
`T subseteq C^+_0`.

## 3. Canonical mixed-coatom specialization

Put

\[
 P_q=\{f_1,\ldots,f_{d+1-q}\},\qquad
 S_q=\{f_q,\ldots,f_d\}.                                   \tag{3.1}
\]

Reindex by `u=d-q`, so `0<=u<=d-2`, and define

\[
 C^-_u=A\cup\{f_1,\ldots,f_{u+1}\},\qquad
 C^+_u=B\cup\{f_{d-u},\ldots,f_d\}.                        \tag{3.2}
\]

### Theorem 3.1 (one conditional split carries both flags)

Assume the old local source word is exactly (0.1), with

\[
 X=(A\cup\{f_1\})\cup(B\cup\{f_d\}).                       \tag{3.3}
\]

Split `X` into

\[
                Z=A\cup\{f_1\},\qquad T=B\cup\{f_d\}.      \tag{3.4}
\]

Then, for every `2<=q<=d`, the new word contains pairwise distinct
exclusive cells of values

\[
                         A\cup P_q,qquad B\cup S_q.          \tag{3.5}
\]

Every interval value of the old word remains.  The operation changes no
old set value and adds exactly one source position.

#### Proof

The nearest left letter is `{f_2}`, the next is `{f_3}`, and so on.  Hence
the left ray is

\[
 A+f_1,\ A+f_1f_2,\ldots,A+f_1\cdots f_{d-1}.
\]

The right letters occur in the order `f_(d-1),f_(d-2),...,f_2`, giving

\[
 B+f_d,\ B+f_{d-1}f_d,\ldots,B+f_2\cdots f_d.
\]

These are (3.5).  Theorem 1.1 gives preservation and the one-position
ledger.  \(\square\)

Suppressed fixed cores may be adjoined to `A,B`; overlap between `A` and
`B` is harmless because `Z,T` are allowed to overlap.

## 4. Why this does not contradict the star-fan no-go

The inserted-star seam has one common base on both fans.  Assigning the two
coatom flags there forces all lost crossing values to contain both active
labels and the full filler flag, so they cannot repay the opposite phase.

The split operation is different in both decisive respects:

1. its two exclusive rays have independent bases `Z` and `T`; and
2. it discards no old crossing cell--each is transported through the whole
   block and its deadline rises by one.

Thus the split leaves the rigid flat-derivative ansatz.  It is legal for the
original interval-OR problem, but it still needs a physical host word.

## 5. The authenticated native packet does not contain the host

For the canonical `0110` connector, `A` and `B` are distinct adjacent
active coatoms (for example `Ibc` and `Ica`).  Their union has one more
active coordinate than either coatom.  The owner chronology contains this
union only at the isolated upper screen between the two blocks.  Every
source envelope capable of touching that screen is an intersection with a
neighboring block owner, and therefore omits one of the two exclusive
active coordinates.  Hence no canonical maximal-erosion source envelope
contains

\[
                  (A\cup B)\cup\{f_1,f_d\}.                  \tag{5.1}
\]

In particular the full-ray host (3.3) is not an actual letter of the
authenticated maximal word in either phase.  Also, its existing filler
trace is the single path

\[
 A+f_1,quad (A\cap B)+f_1f_2,quad\ldots,quad
 (A\cap B)+f_{d-1}f_d,quad B+f_d,                            \tag{5.2}
\]

not the mirrored two-sided trace (0.1).

The replay accompanying this note checks more than (5.1).  For all three
authenticated connector rows, both phases, and `3<=d<=20`, it exhausts
every split of every letter in the canonical maximal-erosion word, permits
skipped ray addresses as in (2.3), and finds no two-chain realization.  At
`d=2` there is one degenerate old-phase split; the terminal new phase still
has none.  This last statement is a finite audit, not an all-`d` theorem
over arbitrary capped or exterior antecedents.

## 6. Minimum pivot count

For a fixed host word the exact answer is now clean.

* One pivot is necessary and sufficient precisely when (2.3) holds (or
  (2.2) for the full consecutive bank).
* If no common split exists but each chain has its own one-sided dominating
  source letter and ordered side trace, two independent splits suffice--one
  per chain.  This bound `2` is independent of `d`.

For example a one-sided host equal to the minimum chain target may be split
into two equal copies; block contraction preserves the old word and one of
the exclusive rays carries the chain.  Repeating this on the other shore
uses two added positions.

This is an **absolute geometric bound conditional on host planting**.  It
is not an unconditional bound over arbitrary reference caps: a cap may have
no actual source letter, or no ordered side trace, capable of carrying even
one chain.  In the native mixed-coatom tensor the endpoint letters are
phase-exclusive, exactly as proved by the maximal-erosion domain theorem.
Therefore the present live alternatives are:

1. plant one new phase-common merged host with the mirrored trace (0.1); or
2. plant two phase-common endpoint hosts, one for each native flag.

The required number of hosts is constant; their simultaneous existence in
one protected Pascal child is the sole remaining assertion.

## 7. Audit

Run

```text
python3 scratch/audit_h1_split_pivot_two_coatom_rays_20260801.py
```

It checks the exact local construction and every contracted old interval
for `2<=d<=40`, and performs the authenticated native-word scan for
`2<=d<=20`.  It reports

```text
PASS_SPLIT_PIVOT_TWO_COATOM_RAYS
```

with canonical payload SHA-256

```text
36cc4c98321ea05523347ff5c6687ad451f5503b350fbfd59b13a7bd827a196e
```

Files:

```text
scratch/audit_h1_split_pivot_two_coatom_rays_20260801.py
scratch/h1_split_pivot_two_coatom_rays_20260801.audit.json
```

Dependencies:

* `MATH_THEOREM_H1_SPLIT_LETTER_RAY_ABSORPTION_AND_ONE_COLUMN_CRITERION_20260801.md`;
* `MATH_THEOREM_INDEPENDENT_COATOM_TWO_CHAIN_PROVIDER_SWITCH_AND_SERIAL_LAMBDA_GATE_20260801.md`;
* `MATH_THEOREM_COATOM_BOUNDARY_STAR_FAN_COMBINATION_NOGO_20260801.md`;
* `MATH_THEOREM_K_ZERO_OWNER_COATOM_U5_REGENERATIVE_RECURRENCE_20260801.md`.
