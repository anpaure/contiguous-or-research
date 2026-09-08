# K16 append-`0x0200` one-hole basin and its exact portal return graph

**Date:** 2026-07-30  
**Status:** exact scoped return-cycle theorem; no completion through a sharp
first portal; global length-12,874 existence remains open

## 1. The improved basin

The authenticated word

```text
scratch/k16_append0200_12874_onehole.word
SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18
```

is exactly

```text
scratch/k16_12873_repaired_partial.word | 0x0200.
```

Appending preserves all old witnesses and supplies the two former upper
holes.  Exact replay leaves the sole hole

\[
                         h=10365=0x287d.                         \tag{1.1}
\]

This is currently the softest retained length-12,874 basin.  Appending
`0x287d` gives the verified length-12,875 certificate, but the objective here
is to cover (1.1) without increasing length.

## 2. The sixteen minimum transfers at position 6440

The source value at zero-based position 6440 is `0xa069`.  Any replacement
which creates a new witness for the low target `0x287d` must itself be a
submask of `0x287d`.  Exact context replay at this position gives 128 gainful
values:

```text
collateral 1:  16 values
collateral 4: 112 values.
```

The complete arbitrary one-substitution census has `26,701` rows which
create a witness of `0x287d`, no completing row, and collateral floor one.
The sixteen minimum values are

\[
 L=\{0x2004\vee q:q\subseteq0x0069\}.                           \tag{2.1}
\]

Every \(\ell\in L\) covers `0x287d` and loses exactly

\[
                         k=43129=0xa879.                         \tag{2.2}

\]

Thus the minimum move transfers one debt rather than eliminating it.  The
all-position census proves that these are not merely the best rows at
position 6440: they are all global collateral-one service rows.

## 3. Exact successor census

Fix any \(\ell\in L\), and call the resulting one-hole state \(W_\ell\).
The complete arbitrary second-substitution census has `27,840` rows which
create a witness of `0xa879`, no completing row, and collateral floor one.
The floor is attained by exactly sixteen rows, all again at position 6440,
with new value in

\[
 U=\{0xa000\vee q:q\subseteq0x0069\}.                           \tag{3.1}
\]

Every \(u\in U\) restores `0xa879` and loses exactly `0x287d`.

There is also a separately replayed finer tail-portal ledger.  Each
\(W_\ell\) has exactly 63 untagged tail cells.  Exhausting every nonzero
submask of `0xa879` at every such cell gives a gainful-collateral histogram
independent of \(\ell\):

```text
1:16, 2:1, 3:1, 4:367, 6:16, 8:130, 9:23,
10:65, 11:173, 12:38, 13:38, 14:7, 15:6, 16:1.
```

There are no zero-collateral exits in this tail catalogue, consistently with
the complete arbitrary-substitution census.

### Theorem 3.1 (complete induced `K_16,16` return graph)

On the 32 states obtained by putting a value of \(L\cup U\) at position
6440 and freezing every other cell, join two states when one arbitrary
substitution covers the current sole hole and leaves exactly one sole hole.
The resulting induced minimum-debt exchange graph is the complete bipartite
graph

\[
                              K_{16,16}.                         \tag{3.2}
\]

The \(L\)-shore has sole hole `0xa879`; the \(U\)-shore has sole hole
`0x287d`.  Every minimum move replaces position 6440 by an arbitrary value
on the opposite shore.  Hence every cycle within this fibre only returns the
defect; no state in this fibre is universal.  No assertion is made here about
possible outgoing one-debt edges from a non-source member of the \(U\)-shore
to states outside these 32 words.

#### Proof

Exact full replay gives the asserted sole hole for each of the 32 literal
words.  A word on one shore differs from a word on the other only at position
6440, so every ordered pair of opposite-shore values is a legal replacement.
The complete `27,840`-row census from every low-side state proves that these,
and only these, are the collateral-one exits among arbitrary substitutions.
This gives all \(16\cdot16=256\) edges of (3.2). \(\square\)

The algebra explains the return invariant.  An \(L\)-value contains the
required low bit `0x0004` and omits the high bit `0x8000`; a \(U\)-value does
the reverse.  The four optional bits are exactly a submask of `0x0069` and
do not change the critical debt.  The physical occurrence defect therefore
alternates

\[
                         \{0x287d\}\leftrightarrow\{0xa879\}.   \tag{3.3}
\]

The completeness of both substitution censuses follows from the exact local
identity.  If \(C_W(t)\) is the number of interval witnesses of \(t\),
\(D_p^W(t)\) counts those containing position \(p\), and
\(A_{p,x}^W(t)\) counts the new containing-\(p\) intervals after replacing
\(W_p\) by \(x\), then

\[
 C_{W[p\leftarrow x]}(t)=C_W(t)-D_p^W(t)+A_{p,x}^W(t).       \tag{3.4}
\]

For a missing target \(t\), every serving replacement is enumerated exactly:
for some left/right context OR \(c\subseteq t\), it has
\(t\setminus c\subseteq x\subseteq t\).  Hence no arbitrary replacement is
lost by the service-row generation.

## 4. The first nonreturn exits

Exclude position 6440.  For every \(W_\ell\), `27,712` service rows remain,
their collateral floor is two, and exactly 65 rows attain it:

* 64 rows at position 0 lose exactly
  \(\{0xa86d,0xac6d\}\);
* one row is

```text
p12873: 0x0200 -> 0xa879.
```

  It covers the current hole but destroys exactly

\[
                         \{0xce61,0xce63\}.                     \tag{4.1}
\]

Within the 63 untagged-tail catalogue, the terminal row is the unique
minimum nonreturn operation.  Its two destroyed witnesses are respectively
the terminal intervals `[12871,12873]` and `[12870,12873]`.  Globally, all
65 minimum nonreturn rows expand one debt to two; none is a descent.

## 5. Exact remaining gate

A two-substitution completion of the append-`0x0200` basin, if one exists,
must use at least one of:

1. a nonminimum first service row, with at least two temporary debts which
   the second edit closes simultaneously; or
2. a genuinely synergistic pair for which neither edit alone creates the
   final `0x287d` witness.

In particular, no two-substitution completion can begin with one of the
sixteen sharp portals.  Three-or-more-position edits, other length-12,874
words, and the two surviving radius-two classes above remain open.  No
global lower bound `nu(16)>12874` is claimed.

Every candidate must be replayed on the full 16-bit word.  Projected
occurrence Hall clearance remains only a necessary gate; shared top-bit
chronology is additional.

## 6. Reproducible certificate

```text
scratch/audit_l_k16_append0200_onehole_return_cycle_20260730.py
  SHA 01fccb3eff98b67de48935db44522ef367dc4796bdb450dd67c925a2a373f126

scratch/k16_append0200_onehole_return_cycle_20260730.audit.json
  SHA cbdf91496c3bd7862304f9d5b1fdd0f7084f1e35f15a6163a58fb0eb9c39dcd6
  payload 81151548ec2547addf3306b05d820cdaf4cdba9a3d8231e05a63da984219411a
```

This checker is standard-library only, uses explicit fail-closed checks,
authenticates the source bytes, reconstructs the append, recomputes every
interval multiplicity, and freezes all sixteen tail-successor histograms and
all 256 return edges.

The complete arbitrary first/second-substitution census is independently
frozen in

```text
scratch/audit_threadA_k16_append0200_one_debt_return_20260730.py
  SHA 285aef014f25b24dc58770facec6399a0753bb558569ead0590355ba61e9305d

scratch/threadA_k16_append0200_one_debt_return_20260730.audit.json
  SHA 6a39bb79a4fb8c579cd3c482978a9b4252a32ccc41a23924050db547ff10b2dd
```

That script uses Python assertions, so its frozen run is valid under the
ordinary interpreter used to produce the audit; invoking it with `python -O`
would not be a proof-safe replay.  The two independent ledgers agree on the
32 one-hole states, all 256 minimum return edges, and the unique terminal
tail exit.
