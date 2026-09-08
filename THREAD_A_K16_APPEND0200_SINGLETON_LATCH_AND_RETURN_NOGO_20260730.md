# The append-`0200` singleton latch and its exact one-cell return obstruction

Date: 2026-07-30

Status: exact theorem and fail-closed light audit.  This note proves a
source-relative one-substitution no-go and closes every second substitution
after the sixteen sharp one-debt portals.  It does **not** exclude an
arbitrary synergistic two-position exchange.

## 1. Frozen basin

Let

```text
W = scratch/k16_12873_repaired_partial.word
SHA-256 0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

and put

\[
                     V=W\Vert\mathtt{0200}.                 \tag{1.1}
\]

The literal word `V` is stored as

```text
scratch/k16_append0200_12874_onehole.word
SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18
```

It has length `12874`, and exact interval-OR replay gives the sole hole

\[
                         h_0=\mathtt{287d}.                  \tag{1.2}
\]

Thus a lossless one-cell substitution in `V` would prove
`nu(16)=12874`.

## 2. Exact local replacement criterion

For a word `U`, write `C_U(t)` for the total number of intervals of OR `t`.
At a position `p`, let `D_p^U(t)` count those witnesses containing `p`.
Let `L_p(U)` be the suffix-OR multiset immediately to the left of `p`, with
the empty suffix included, and define `R_p(U)` symmetrically on the right.
For a proposed replacement `x`, put

\[
 A_{p,x}^U(t)=
 \sum_{\substack{\ell\in L_p(U),\ r\in R_p(U)\\
                  \ell\vee x\vee r=t}}
       m_L(\ell)m_R(r).                                    \tag{2.1}
\]

### Lemma 2.1 (local-delta identity)

After replacing `U_p` by `x`,

\[
 C_{U[p\leftarrow x]}(t)
       =C_U(t)-D_p^U(t)+A_{p,x}^U(t).                       \tag{2.2}
\]

Consequently, when `U` has hole set `H`, the replacement is universal if
and only if

\[
 H\cup\{t:C_U(t)=D_p^U(t)>0\}
 \subseteq
 \{\ell\vee x\vee r:\ell\in L_p(U),\ r\in R_p(U)\}.      \tag{2.3}
\]

#### Proof

Intervals avoiding `p` are unchanged and contribute
`C_U(t)-D_p^U(t)`.  Every interval containing the new cell decomposes
uniquely into a left suffix, the new cell, and a right prefix, giving
(2.1)--(2.2).  A target with an avoiding witness survives automatically;
the old holes and targets without an avoiding witness give exactly (2.3).
\(\square\)

This criterion is used below with full multiplicities, so no pointwise
near-witness or unique-witness heuristic enters the census.

## 3. The sharp first portal cube

At zero-based position `6440`,

\[
 V_{6439}=\mathtt{2879},\qquad V_{6440}=\mathtt{a069}.       \tag{3.1}
\]

Define

\[
 X^-={\mathtt{2004}\vee s:s\subseteq\mathtt{0069}\}.      \tag{3.2}
\]

This is a Boolean cube of sixteen values.

### Theorem 3.1 (exact one-substitution floor)

Among all one-cell substitutions in `V` which create a witness of `h_0`,
there are `26701` service rows and no universal row.  The minimum collateral
is exactly one.  It is attained in exactly the sixteen rows

\[
                 (p,x)=(6440,x),\qquad x\in X^-.            \tag{3.3}
\]

Every word in (3.3) has the sole hole

\[
                         h_1=\mathtt{a879}.                  \tag{3.4}
\]

#### Proof

For each position, Lemma 2.1 restricts service values to the finite
suffix/prefix product at that position.  Exact evaluation over all positions
and every induced service value returns `26701` rows, zero satisfying (2.3),
minimum debt one, and precisely (3.2)--(3.4).  The audit asserts all four
figures and the exact cube before printing `PASS`. \(\square\)

The local reason for the transfer is visible in (3.1).  For every
`x in X^-`,

\[
                         \mathtt{2879}\vee x=mathtt{287d}.  \tag{3.5}
\]

Thus `[6439,6440]` becomes a low witness of `h_0`.  It was the unique
high witness of `h_1`; removing bit 15 from the cell destroys that label.
The longer interval `[6439,6441]` still retains the neighbouring high target
`0xa87d`, which is why the spill is the singleton (3.4), not the two-target
spill of the ripple basin.

## 4. Exact return-cycle obstruction

Define the opposite cube

\[
 X^+=\{\mathtt{a000}\vee s:s\subseteq\mathtt{0069}\}.      \tag{4.1}
\]

### Theorem 4.1 (all sixteen one-cell returns fail)

Fix any `x in X^-` and let `V_x=V[6440<-x]`.  Among all substitutions in
`V_x` which create a witness of its sole hole `h_1`, there are exactly
`27840` service rows and no universal row.  Their minimum collateral is one,
attained only by

\[
                 (q,y)=(6440,y),\qquad y\in X^+.            \tag{4.2}
\]

Every word in (4.2) again has sole hole `h_0`.  These conclusions, including
the complete service count, are independent of the chosen `x in X^-`.

If the return is required to use a genuinely different position
`q != 6440`, then `27712` service rows remain.  Their minimum collateral is
two, attained in exactly `65` rows:

* `64` rows at `q=0`, all losing
  `{0xa86d,0xac6d}`;
* one row `(q,y)=(12873,0xa879)`, losing
  `{0xce61,0xce63}`.

#### Proof

Apply Lemma 2.1 separately to each of the sixteen SHA-defined words `V_x`.
The fail-closed audit asserts the `27840/0/1/16` ledger, the exact cube
(4.1), the returned hole `h_0`, and the off-portal `27712/2/65` ledger with
the two stated debt classes.  No random or solver search is involved.
\(\square\)

The same local identity explains the minimum return:

\[
                         \mathtt{2879}\vee y=mathtt{a879}
                         \qquad(y\in X^+).                  \tag{4.3}
\]

But every such value omits bit 2, so it destroys the unique low witness
(3.5).  In particular, the original value `0xa069` belongs to `X^+`; literal
reversion is one of the sixteen minimum returns.

### Corollary 4.2 (singleton latch)

The audited minimum first-service and minimum-return fibres toggle

\[
               \mathtt{287d}\ \longleftrightarrow\ \mathtt{a879}          \tag{4.4}
\]

at the same physical position: overwriting once more by the chosen member of
the opposite cube literally returns to the corresponding one-hole state.
Hence no second substitution completes any of the sixteen sharp first-portal
states.  A return at another position pays at least two new debts.

## 5. Exact scope boundary

Theorem 3.1 proves that `V` itself has substitution distance at least two
from a universal word.  Theorem 4.1 proves more than a greedy-search
observation: it exhausts every possible second substitution after every
minimum-collateral first service row.

It does **not** prove that the global substitution distance is at least
three.  A two-edit completion could still occur in either of these ways:

1. the first edit services `0x287d` but creates two or more temporary debts,
   all repaired by the second edit; or
2. neither individual edit services `0x287d`, while their joint interval
   creates it.

Those are the smallest surviving balanced-exchange classes.  No completion
was found or persisted in the theorem's closed portal fibre.

## 6. Audit artifacts

```text
scratch/audit_threadA_k16_append0200_one_debt_return_20260730.py
  SHA-256 285aef014f25b24dc58770facec6399a0753bb558569ead0590355ba61e9305d

scratch/threadA_k16_append0200_one_debt_return_20260730.audit.json
  SHA-256 6a39bb79a4fb8c579cd3c482978a9b4252a32ccc41a23924050db547ff10b2dd
```

The script verifies the two source hashes, reconstructs (1.1), performs a
full interval-OR replay, asserts the complete first census, and then asserts
the complete return census for all sixteen first states.  Its state banks
have at most seventeen OR labels per endpoint; it uses no SAT/CP solver and
does not enumerate alternative words outside this fixed portal fibre.
