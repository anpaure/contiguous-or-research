# Rank-isolated selector squares are never legal factor trades

Date: 2026-07-24

## 1. Result

The Petr--Turek adjacent-pair vectors give an exact linear separation of
the cyclic-interval shadow ranks.  It is tempting to use them as integral
two-wreath switches: at a chosen rank (r), exchange one diagonal of the
four-order square for the other, preserving the middle layer and every
other shadow rank.

That tempting step is impossible.  Neither diagonal can occur inside an
exact middle wreath factor.  The two cyclic orders on either diagonal share
at least (n-4) middle intervals, whereas distinct members of an exact
factor must have disjoint middle-interval families.

Thus the rank-isolated vectors prove linear surjectivity but are not
packing-compatible Markov moves.  Any integral use of the spectral
separation theorem requires a larger composite trade whose positive and
negative supports are themselves middle packings.

No claim about the Wreath Conjecture or the coefficient-one OR bound is
made here.

## 2. The selector square

Let

\[
 n=2m+1,
 \qquad 2\le r\le m-1,
\]

and let (C=(z_0,z_1,\ldots,z_{n-1})) be an oriented cyclic order.  Let
(\tau) exchange the entries in positions (0,1), and let (\sigma)
exchange the entries in positions (r,r+1).  Put

\[
 z_{C,r}=e_C-e_{\tau C}-e_{\sigma C}+e_{\tau\sigma C}.
 \tag{2.1}
\]

For the all-start cyclic-interval incidence matrices (A_s), the exact
selector identity is

\[
 A_s z_{C,r}=0\quad(s\ne r),
 \tag{2.2}
\]

while (A_rz_{C,r}) is the nonzero four-set square recorded in
`WREATH_CROSS_RANK_SPECTRAL_20260724.md`.  In particular (A_mz_{C,r}=0).
At the level of signed column sums, therefore, the two diagonals

\[
 \{C,\tau\sigma C\},
 \qquad
 \{\tau C,\sigma C\}
 \tag{2.3}
\]

have the same middle incidence and differ at no lower rank except (r).

## 3. Adjacent swaps retain almost every middle interval

### Lemma 3.1

Let (2\le s<n).  If (C') is obtained from a cyclic order (C) by one
adjacent transposition, then (C) and (C') have at least (n-2) common
cyclic (s)-intervals.

#### Proof

Write the exchanged positions as (i,i+1).  A position interval of length
(s) changes as a set only if it contains exactly one of these two
positions.  Since the positions are adjacent, this happens only for the
interval ending at (i) and the interval beginning at (i+1).  All other
(n-2) position intervals contain both exchanged entries or neither, and
therefore retain exactly the same coordinate set.  QED

### Lemma 3.2

Each pair of cyclic orders on either diagonal in (2.3) has at least

\[
 \boxed{n-4}
 \tag{3.1}
\]

common length-(m) cyclic intervals.

#### Proof

The two orders in one diagonal differ by the two adjacent transpositions
(\tau,\sigma).  By Lemma 3.1, each transposition can alter at most two of
the (n) position intervals of length (m).  Hence at least (n-4)
position intervals are unchanged by both.  The same argument applies to
both diagonals.  QED

For the present range (m\ge3), one has (n-4=2m-3>0).  The four affected
starts are distinct for (2\le r\le m-1); the displayed lower bound is all
that is needed, so no exclusion of accidental additional coincidences is
required.

## 4. Integral obstruction

### Theorem 4.1

No diagonal in (2.3) is contained in an exact middle wreath factor.
Consequently the selector vector (2.1) is never an applicable two-for-two
trade between exact factors.

#### Proof

In an exact middle wreath factor, the length-(m) interval families of two
distinct selected cyclic orders are disjoint: together all selected orders
partition the middle layer.  Lemma 3.2 says that the two orders in either
selector diagonal share at least one middle interval.  They therefore
cannot both be selected.  An exchange of one complete diagonal for the
other can never be initiated.  QED

This pinpoints the gap between the real-linear theorem

\[
 A_r(\ker A_m)=\ker U_r
\]

and an integral factor-switching theorem.  The rank-isolated squares span
the desired target space only after allowing signed combinations whose two
sides have extensive internal middle collisions.

## 5. Exact finite census at (m=4)

The read-only checker

```text
python3 scratch/analyze_rank_isolated_wreath_squares.py \
  m4_vertical_wreath_factor.txt
```

enumerates all (8!) oriented circular orders, both selector ranks
(r=2,3), and quotients the resulting orders by reversal and rotation.  It
checks the rank-isolation identity on every distinct square and audits the
two diagonals against the archived exact factor.

Its output is

```text
factor=m4_vertical_wreath_factor.txt n=9 m=4 rows=14
distinct PT squares=80640 applicable=0
rank-isolation identities checked=80640
rank=2 holes=0 energy=28 applicable=0 isolated_ok=0 delta_hist={}
  diagonal occupancy census={(0, 0): 40208, (0, 1): 56, (1, 0): 56}
rank=3 holes=0 energy=2 applicable=0 isolated_ok=0 delta_hist={}
  diagonal occupancy census={(0, 0): 40208, (0, 1): 56, (1, 0): 56}
```

No diagonal contains two selected orders, exactly as Theorem 4.1 forces.
The checker also verifies directly, square by square, that the two
diagonals agree at every rank other than the advertised selector rank.

## 6. Remaining constructive target

The useful spectral fact survives: the different shadow ranks can be
separated exactly in the signed column lattice over the reals.  What is now
needed is a packing-compatible replacement:

> Construct bounded or well-amortized signed sums of selector squares such
> that the positive columns are pairwise middle-disjoint, the negative
> columns are pairwise middle-disjoint, and the net image remains localized
> to one shadow rank (or has Gaussian-small leakage into the other ranks).

This is strictly more specific than an unspecified integral-rounding gate.
It is also compatible with the balanced (C_8) program: those switches are
packing-compatible, but not rank-isolated; selector squares are
rank-isolated, but not packing-compatible.  A successful composite trade
must combine the two properties.
