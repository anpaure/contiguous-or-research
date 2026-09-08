# One-cell insertion kernels and the optimal two-cell append for the `k=16` three-hole basin

Date: 2026-07-30

Status: exact theorem and light exhaustive cut audit.  The two-cell word is a
verified upper-bound construction.  The one-cell no-go is scoped to the
frozen length-`12873` three-hole word; it is not a global lower bound for
`nu(16)`.

## 1. Frozen words

Let

```text
W = scratch/k16_12873_repaired_partial.word
```

with length `12873`, SHA-256

```text
0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

and exact hole set

\[
 {cal H}=\{\mathtt{287d},\mathtt{ce61},\mathtt{ce63}\}.       \tag{1.1}
\]

The authenticated extension is

\[
                         W^+=W\Vert\mathtt{0200}\Vert\mathtt{287d}, \tag{1.2}
\]

stored as `answers/k16_upper12875.word`, of length `12875` and SHA-256

```text
d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9
```

Exact replay finds no missing nonzero mask.  Hence the current exact bracket
is

\[
                         12873\le\nu(16)\le12875.        \tag{1.3}
\]

## 2. Exact one-cell insertion criterion

For a cut `c in {0,...,n}` of a word `V=(V_0,...,V_(n-1))`, let

\[
 L_c=\{0\}\cup\left\{\bigvee_{i=a}^{c-1}V_i:0\le a<c\right\},
 \qquad
 R_c=\{0\}\cup\left\{\bigvee_{i=c}^{b}V_i:c\le b<n\right\}. \tag{2.1}
\]

Thus `L_c` is the suffix-OR chain immediately left of the cut and `R_c` is
the prefix-OR chain immediately right of it.

Let `H_c(V)` be the family of targets having no old witness wholly to one
side of cut `c`; equivalently, every old witness crosses the cut.  A target
with no old witness belongs to `H_c(V)` vacuously.

### Theorem 2.1 (insertion-kernel iff theorem)

Insert one nonempty letter `x` at cut `c`.  The resulting word is universal
if and only if

\[
 \boxed{
   \text{for every }h\in H_c(V)\text{ there exist }
   \ell\in L_c,\ r\in R_c\text{ with }\ell\vee x\vee r=h.
 }                                                            \tag{2.2}
\]

In particular,

\[
                       x\subseteq\bigcap_{h\in H_c(V)}h        \tag{2.3}
\]

is necessary.

#### Proof

Every target outside `H_c(V)` retains an old witness wholly on one side of
the cut.  Every target in `H_c(V)` must use a new interval containing `x`,
and every such interval is uniquely a left suffix, `x`, and a right prefix.
This proves necessity and sufficiency of (2.2).  Since `x` lies in every new
witness, it is a submask of every member of `H_c(V)`, proving (2.3).
\(\square\)

### Audit convention

The finite audit below tests the optimistic kernel using only the three
original holes, which are a subset of every `H_c(V)`.  Failure of this
relaxation is therefore an unconditional no-go for a true interior insertion:
adding the cut-private displaced targets can only make the condition harder.
At an exterior cut, `H_c(V)` is exactly the old hole set.

## 3. No one-cell insertion into the frozen basin

For (1.1),

\[
       \mathtt{287d}\cap\mathtt{ce61}\cap\mathtt{ce63}
       =\mathtt{0861}.                                      \tag{3.1}
\]

There are only `15` nonzero candidate literals `x`, the nonzero submasks of
`0x0861`.  The light audit forms the two chains (2.1) at all `12874` cuts and
tests every one of these candidates.

### Theorem 3.1 (frozen one-insertion no-go)

There is no cut `c` and no nonempty letter `x` for which

\[
        {cal H}\subseteq\{\ell\vee x\vee r:
                     \ell\in L_c,\ r\in R_c\}.             \tag{3.2}
\]

The maximum is two supplied holes; it is achieved by exactly `32`
cut/literal rows.  Consequently no genuine one-cell insertion can complete
the frozen word `W`, even before charging targets whose old witnesses are
split by the insertion.

#### Proof

Condition (3.1) reduces the literal list to 15.  Suffix and prefix ORs form
chains with at most 17 distinct states, so (3.2) is checked directly and
exactly for all cuts.  The authenticated audit returns zero full rows,
maximum two, and 32 maximizers.  By the audit convention after Theorem 2.1,
the relaxed failure implies the genuine insertion failure. \(\square\)

This is stronger than an append-only obstruction, but remains source-
relative: altering the `12873` basin changes its cut chains and can make
(3.2) feasible.

## 4. A general append-width lower bound

Order masks by inclusion and let `width(H)` denote the largest antichain in
`H`.

### Theorem 4.1 (append chain-cover bound)

If appending `t` cells to a word covers every mask in its old hole set `H`,
then

\[
                              t\ge\operatorname{width}(H).     \tag{4.1}
\]

#### Proof

Every new witness for an old hole ends at one of the appended cells.  For a
fixed endpoint, the ORs of intervals ending there form a chain: moving the
left endpoint left can only add coordinates.  Assign each old hole to one
new witnessing endpoint.  This covers `H` by at most `t` chains.  By the
elementary chain-cover/antichain inequality, `t` is at least the width. \(\square\)

Here `0xce61` is a proper subset of `0xce63`, while `0x287d` is incomparable
with both.  Therefore

\[
                         \operatorname{width}({\cal H})=2,     \tag{4.2}
\]

and one appended cell is impossible.

### Theorem 4.2 (the authenticated append is optimal for `W`)

The first appended cell `0x0200` supplies the nested pair

\[
 \begin{aligned}
  \mathtt{8c61}\vee\mathtt{cc41}\vee\mathtt{0200}
      &=\mathtt{ce61},\\
  \mathtt{8c62}\vee\mathtt{8c61}\vee
  \mathtt{cc41}\vee\mathtt{0200}&=\mathtt{ce63}.
 \end{aligned}                                               \tag{4.3}
\]

The second appended cell is the singleton witness `0x287d`.  Hence (1.2) is
universal; by (4.2), two is the minimum number of appended cells capable of
completing this frozen basin.  The earlier `0x0661` bridge is also valid, but
the smaller `0x0200` bridge and hash in Section 1 are the frozen canonical
certificate. \(\square\)

## 5. Consequence for a length-`12874` route

A one-cell-completable altered basin `V` of length `12873` must satisfy the
following exact, checkable condition at some cut `c`:

1. one nonzero `x` lies in the intersection of its complete cut-residual
   family `H_c(V)`;
2. every residual mask lies in the product-of-two-chains translate
   `x join L_c join R_c`; and
3. all targets outside `H_c(V)` have a witness avoiding the cut.

The two-cell upper word reveals the desired service split: one suffix chain
serves the nested pair `ce61<ce63`, while a second endpoint serves the
incomparable target `287d`.  A length-preserving balanced exchange must
internalize both services into the existing chronology, or alter the basin
so that one cut-product kernel supplies all residual targets.  The phase-pair
theorem in

```text
THREAD_A_K16_PHASE_BRAID_ACTIVATION_AND_RETHREAD_ESCAPE_20260730.md
```

explains the cost: pure retagging only moves fixed projected witnesses between
the two shores.  To merge the two append services into one cell, an exchange
must also create a second projected occurrence or change the cut chains; tag
balance alone cannot do it.

## 6. Audit artifact

The lightweight verifier is

```text
scratch/audit_threadA_k16_one_cell_insertion_20260730.py
  SHA-256 480c83a2080c0202da5219fa9d916a79463bb310ae949df025d7f74e7c257dfa

scratch/threadA_k16_one_cell_insertion_20260730.audit.json
  SHA-256 5fe80b3a51c711b92fa7d5c9cd47570a1a879a351b4573a2baee0a89c99899b6
```

It reconstructs both frozen words, verifies both hashes and full coverage,
checks the 15-by-12,874 relaxed insertion kernel, and verifies the literal
equalities (4.3).  It performs no optimization beyond this finite cut table
and uses no SAT/CP solver.

## 7. The ripple basin and its one-cell upper bridge

There is a second authenticated length-`12873` basin

```text
scratch/k16_12873_ripple3_partial.word
SHA-256 87f19da2994c6052caa3f9a5d87936ee340588111b29466689c10a46b3fd8b31
```

whose exact holes are

\[
                    \{\mathtt{287d},\mathtt{8ce6},\mathtt{9ce6}\}. \tag{7.1}
\]

Insert `0x0864` at zero-based cut `12870`.  The resulting length-`12874`
word is

```text
scratch/k16_ripple_insert12874_onehole.word
SHA-256 5ac147eca512b7e398c7217f1796836f454a304274c6e54fda7050fc9b4f66db
```

and has sole hole `0x287d`.

### Proposition 7.1 (why the two upper holes close)

Immediately left of the inserted cell, the relevant suffix is

\[
 \mathtt{90c6},\quad\mathtt{88c6},\quad\mathtt{8c44},
 \quad\boxed{\mathtt{0864}}.                               \tag{7.2}
\]

Consequently

\[
 \begin{aligned}
  \mathtt{88c6}\vee\mathtt{8c44}\vee\mathtt{0864}
       &=\mathtt{8ce6},\\
  \mathtt{90c6}\vee\mathtt{88c6}\vee\mathtt{8c44}
       \vee\mathtt{0864}&=\mathtt{9ce6}.
 \end{aligned}                                             \tag{7.3}
\]

These are nested suffix witnesses ending at the inserted cell.  Full replay
shows that every formerly covered mask retains another witness or is
recreated across the cut; therefore (7.3) creates no new hole.  The remaining
`0x287d` is incomparable with the upper chain and receives no witness at this
cut. \(\square\)

This is the same service geometry as the two-cell append: one cell can absorb
a nested chain of holes, but not automatically a second incomparable shore.

## 8. Exact one-cell exchange theorem

Let `V` be any word and fix a position `p`.  Write `C(t)` for the total
number of interval witnesses of target `t`, and `D_p(t)` for the number of
those witnesses containing `p`.  Let `L_p` be the suffix-OR bank ending at
`p-1` and `R_p` the prefix-OR bank starting at `p+1`, both including the empty
state.  After replacing `V_p` by `x`, put

\[
 A_{p,x}(t)=
 \sum_{\substack{\ell\in L_p, r\in R_p\\
                  \ell\vee x\vee r=t}}
      m_L(\ell)m_R(r),                                    \tag{8.1}
\]

where the multiplicities count the suffixes and prefixes giving each state.

### Theorem 8.1 (local-delta iff theorem)

For every target,

\[
                    C'(t)=C(t)-D_p(t)+A_{p,x}(t).          \tag{8.2}
\]

If `V` has sole hole `h`, the replacement is universal if and only if

\[
 A_{p,x}(h)>0                                             \tag{8.3}
\]

and

\[
 A_{p,x}(t)>0
 \quad\text{for every }t\text{ with }C(t)=D_p(t)>0.       \tag{8.4}
\]

In particular any safe service literal satisfies

\[
 x\subseteq h\cap
 \bigcap_{t:C(t)=D_p(t)>0}t.                              \tag{8.5}
\]

#### Proof

Intervals avoiding `p` are unchanged and contribute `C(t)-D_p(t)`.
Every changed interval contains `p` and decomposes uniquely as a left suffix,
the new cell, and a right prefix, giving (8.1)--(8.2).  A target with
`C(t)>D_p(t)` retains an avoiding witness automatically.  The hole and the
targets with no avoiding witness give exactly (8.3)--(8.4).  Every one of
their new witnesses contains `x`, proving (8.5). \(\square\)

### Theorem 8.2 (ripple one-substitution no-go and sharp debt floor)

For the one-hole word after Proposition 7.1, no replacement of one existing
cell by any nonzero 16-bit mask is universal.  More strongly, among all
one-cell substitutions which create a witness for `0x287d`, the minimum
number of newly missing targets is exactly two.

The exact census is:

\[
\begin{array}{r|r}
\text{service substitutions}&26889\\
\text{debt-free substitutions}&0\\
\text{minimum collateral holes}&2\\
\text{substitutions attaining the minimum}&169.
\end{array}                                                \tag{8.6}
\]

The 169 minimizers have only four debt pairs:

\[
\begin{array}{c|r|c}
\text{debt pair}&\text{number}&\text{representative }(p,x)\\ \hline
\{43117,44141\}&128&(0,2137)\\
\{10553,10557\}&8&(5921,2144)\\
\{43129,43133\}&32&(6440,8193)\\
\{52833,52835\}&1&(12873,10365).
\end{array}                                                \tag{8.7}
\]

#### Proof

For each of the `12874` positions, compute `C`, `D_p`, and the two state banks
in Theorem 8.1.  A service value must be a nonzero submask of `0x287d`.
Enumerating exactly the values induced by contexts
`ell union r subseteq 0x287d` gives `26889` position/value services.  Formula
(8.2) gives zero rows satisfying (8.4), minimum debt two, and the complete
classification (8.7).  This is a direct finite evaluation of the theorem,
not a SAT/CP search. \(\square\)

### Corollary 8.3 (scoped minimum-edit statement)

Starting from `scratch/k16_ripple_insert12874_onehole.word`, a completion
using substitutions only must change at least two positions.  One further
appended singleton `0x287d` gives the verified length-`12875` scale, but no
single substitution can give length `12874`.

This corollary does not cover moving one existing cell to a different cut,
one deletion plus one insertion, or a simultaneous two-position exchange;
nor does it assert that two substitutions suffice.  Those are the exact
surviving balanced-exchange classes.

## 9. Ripple audit artifact

The lightweight exact replay is

```text
scratch/audit_threadA_k16_ripple_one_cell_exchange_20260730.py
  SHA-256 6dd7dfe3e2c5fbae8e56e56d4dcf654e81097695ca72dc9b525566ae8a375c19

scratch/threadA_k16_ripple_one_cell_exchange_20260730.audit.json
  SHA-256 3a6c60685f0fd696d872468942a5f9cf3e89b17912c6ccb366fc317fe5dfbc52
```

It verifies both source hashes, the literal insertion, both upper witnesses,
the one-hole state, Theorem 8.1 at every position, and the census
(8.6)--(8.7).  Its largest tables are the 65,536 mask multiplicities and the
at-most-17-state suffix/prefix banks; it performs no broad word generation.
