# Independent audit of `MTF_SCD_INDUCTION_NEXT.md`

## Verdict

**PASS WITH SCOPE CORRECTIONS.**

The following substantive claims are correct.

1. The lower and upper one-coordinate MTF lift identities are exact.
2. The displayed closed-walk splice is a genuine MTF path, including the
   one-state case.
3. Closing a path by the ordered-partition reset and then applying the splice
   gives the stated state-count and reset-mass recurrence.
4. The `k=3,4,5` certificates are valid; the `k=5` initialization/update word
   has length 14 and covers every nonzero 5-bit mask.
5. For a direct SCD transversal in which **every** assigned-chain arc has one
   globally fixed orientation `d -> d-1`, the reset excess is
   `(4/sqrt(e)+o(1))W(2m)`.  With the globally reversed orientation it is
   `(4/sqrt(e)-2+o(1))W(2m)`.

Two formulations need to be kept narrower than some prose in the source.

* After reset states are inserted, the lifted defect is **at most** `2q`, not
  necessarily exactly `2q`, because reset states may incidentally expose some
  formerly missing masks.  All displayed upper bounds remain valid.
* The radius calculation does not exclude a cover mixing increasing and
  decreasing components, using same-radius arcs, skipping radii, or making
  reset states double as assigned-chain states.  It excludes the direct,
  globally oriented monotone schemes stated explicitly in Theorem 5 and its
  reversed analogue.

The bounded search program is a useful certificate finder, not an exhaustive
test of all path tours: it fixes the maximal chain as the first state.  Its
failure to return a `k=6` certificate has no negative mathematical force.

## 1. Audited artifacts

At audit time the source hashes were:

```text
c6e48e911c5091d456076e9d36b536e1aa369b1110985f702d93f74c83c5418e  MTF_SCD_INDUCTION_NEXT.md
42a32e6cb0288c56d9528c4d52c03c6862760d4c62e190c9c1a426f92bda0343  mtf_scd_small_verify.cpp
82a2fcb766be9c44d07200864a94d3669abf5db679d0cb773ea0b0fe87cd2061  mtf_scd_tour_search.cpp
```

I compiled the certificate checker independently with Clang C++20 and
optimization enabled.  Its output was:

```text
k=3 cyclic MTF-SCD certificate: PASS
k=4 MTF-SCD path certificate: PASS
k=5 MTF-SCD path certificate: PASS
k=5 induced OR word length 14: PASS
```

I also compiled the search program independently.  Its `k=3` and `k=4`
outputs reproduce the certified tours.  This execution is only corroborating
evidence; the proofs below do not trust the program.

## 2. State convention and exact update

An MTF state is an ordered partition

\[
             \Pi=(B_1,\ldots,B_s)
\]

of the coordinate set.  For a nonempty mask `X`,

\[
 M_X(\Pi)=(X,B_1\setminus X,\ldots,B_s\setminus X),
\]

with empty residual blocks deleted.  Its exposed masks are the nonempty
prefix unions.  This convention agrees with the last-occurrence state of an
OR word: appending `X` makes all coordinates of `X` most recent and leaves the
relative ages of all other coordinates unchanged.

## 3. Re-derivation of the one-coordinate lift

Let `z` be new and define

\[
\begin{aligned}
L_z(\Pi)&=(B_1,\ldots,B_s,\{z\}),\\
U_z(\Pi)&=(B_1\cup\{z\},B_2,\ldots,B_s),\\
V_z(\Pi)&=(\{z\},B_1,\ldots,B_s).
\end{aligned}
\]

For `X subseteq [k]`, `z` is disjoint from `X`.  Therefore

\[
\begin{aligned}
M_X(L_z\Pi)
 &= (X,B_1\setminus X,\ldots,B_s\setminus X,\{z\})
  = L_z(M_X\Pi),\\
M_{X\cup\{z\}}(U_z\Pi)
 &= (X\cup\{z\},B_1\setminus X,\ldots,B_s\setminus X)
  = U_z(M_X\Pi).
\end{aligned}
\]

Deleting empty residuals gives the same ordered lists on both sides.  This
also covers all boundary cases:

* `X` may contain an entire old block or may equal `[k]`;
* `Pi` may have one block;
* no empty update is needed.

The prefix chains are exactly as asserted:

* before its final block, `L_z(Pi)` has the old prefix unions;
* `U_z(Pi)` has `z` joined to every nonempty old prefix union;
* `V_z(Pi)` has `{z}` followed by `z` joined to every nonempty old prefix.

Consequently two lifted copies of `L` old states form `2p` paths with first
block-count sum

\[
             \sum_j ((s_j+1)+s_j)=2R+p.
\]

If the old state family misses exactly `q` nonempty masks, the two copies
miss the lower and upper copies of those masks and may additionally miss
`{z}`.  The standard path-cover word length is

\[
 2L-2p+(2R+p)+(2q+1)
 =2L-p+2R+2q+1,
\]

which verifies (3.3).

## 4. Closed-walk splice, including all seams

Suppose

\[
 \Pi_0\to\Pi_1\to\cdots\to\Pi_{\ell-1}\to\Pi_0
\]

is closed and `Pi_0=M_X(Pi_(ell-1))`.  The proposed list has `ell` lower
states, one `V` state, and `ell-1` ordinary upper states, hence `2ell` states.

The internal lower and upper arcs follow from the lift identities.  The two
new seams are exact:

\[
 M_{\{z\}}(L_z\Pi_{\ell-1})=V_z\Pi_{\ell-1},
\]

and

\[
\begin{aligned}
M_{X\cup\{z\}}(V_z\Pi_{\ell-1})
 &= (X\cup\{z\},\Pi_{\ell-1}-X)\\
 &=U_z(M_X\Pi_{\ell-1})=U_z\Pi_0.
\end{aligned}
\]

Here `Pi-X` means the ordered residual blocks after deleting empties.  The
formula remains correct if `X=[k]`.  For `ell=1`, the two-state path
`L_z(Pi_0),V_z(Pi_0)` uses only the first seam and directly has the claimed
coverage.

The one `V` state replaces the omitted `U_z(Pi_(ell-1))`: it exposes all of
that state's upper masks and also `{z}`.  Thus the splice misses exactly the
two copies of the old missed masks.  For `p` closed walks, first lower states
have block-count sum `R+p`; the path-cover construction has length

\[
        2L-p+(R+p)+2q=2L+R+2q,
\]

verifying (4.3).

## 5. Exact reset and parity propagation

For a desired state `Pi=(B_1,...,B_s)`, append

\[
                     B_s,B_{s-1},\ldots,B_1.
\]

Starting from any state, after these `s` updates the last occurrences are
ordered exactly as `(B_1,...,B_s)`.  All blocks are nonempty, so every update
is legal.  The last update returns to the already listed first state, hence a
path becomes a closed cyclic list after only `s-1` additional states.

For paths of total state count `L`, path count `p`, first-block sum `R`, and
defect `q`, the closed walks therefore have total cyclic length

\[
                     L+R-p.
\]

Splicing gives

\[
 L'=2(L+R-p),\qquad R'=R+p,\qquad q'\le 2q.          \tag{A}
\]

The weak inequality for `q'` is the only correction needed: reset states can
cover extra masks.  Since every first state has at least one block, `p<=R`.
Using

\[
 W(2m+1)=2W(2m)-\operatorname{Cat}_m,
 \qquad W(2m+2)=2W(2m+1),
\]

and `Cat_m/W(2m)=1/(m+1)`, (A) proves that

\[
 L=W+o(W),\quad R=o(W),\quad q=o(W)
\]

propagates by one dimension.  This is a parity-transfer lemma, not a way of
creating the needed family from a fixed finite base: doubling a fixed
relative error preserves a nonzero relative error.

## 6. Independent certificate verification

### `k=3`

The three chains contain respectively

```text
0,1,3,7 | 4,5 | 2,6,
```

so they partition `0,...,7`, and each is saturated and symmetric.  Direct
application of the update rule gives

```text
(1,2,4) --4--> (4,1,2) --2--> (2,4,1) --1--> (1,2,4).
```

This is a genuine cycle.

### `k=4`

The six chains collectively list each integer `0,...,15` exactly once.
Their endpoint ranks sum to four, and adjacent members add one bit.  The
updates independently evaluate to

```text
(1,2,4,8) --8--> (8,1,2,4)
            --4--> (4,8,1,2)
            --2--> (2,4,8,1)
            --8--> (8,2,4,1)
            --5--> (5,8,2).
```

### `k=5`

Sorting the members of the ten displayed chains gives each integer
`0,...,31` exactly once.  Every adjacent pair differs by one added bit and
the endpoint ranks sum to five.  Recomputing all nine updates gives exactly
the ten displayed ordered partitions; in particular the non-singleton
updates at the second seam are

```text
(8,2,1,16,4) --18--> (18,8,1,4)
                 --20--> (20,2,8,1)
                  --5--> (5,16,2,8)
                  --9--> (9,4,16,2).
```

Reverse initialization followed by the updates is

```text
8,16,1,2,4,8,16,1,2,8,18,20,5,9.
```

Independent suffix-OR enumeration covers all 31 nonzero masks.

The path cannot close directly.  The maximal first chain forces the unique
state `(4,2,1,16,8)`.  Since a move's first block is its update mask, a move
from `(9,4,16,2)` to that state would have to use `X=4`; it instead produces
`(4,9,16,2)`.

## 7. Audit of the search program

The DFS correctly implements the MTF update, enumerates every symmetric
chain exposed by a visited state, rejects overlap with already assigned
sets, and accepts only after exactly `W(k)` disjoint chains cover the cube.
For `k<=6`, its 64-bit set-family representation is safe, including bit 63.

It is nevertheless a restricted search:

* the first state is fixed to the canonical singleton order;
* its first assigned chain is fixed to the maximal chain;
* a directed path cannot in general be rotated to put that chain first.

Thus a completed `NO TOUR FOUND` run would only exclude this normalized
first-state subclass.  The workspace has no complete `k=6` run certificate
or proof, and the source correctly declines to claim one.

The sort-before-`unique` operation orders successor states only by block
count, not lexicographically.  This does not affect soundness or completeness
here: distinct update masks have distinct first blocks, hence distinct
successor states.  It is merely unnecessary code.

## 8. Radius-decreasing reset constant

For `k=2m`, the number of radius-`d` chains in every SCD is

\[
c_d=\binom{2m}{m-d}-\binom{2m}{m-d-1}
   =\binom{2m}{m-d}\frac{2d+1}{m+d+1}.              \tag{B}
\]

For `d<m`, any exposing state needs a block for the nonempty minimum, `2d`
singleton increment blocks, and a block for the nonempty complement of the
top.  Hence its reset excess is at least `2d+1`.  The unique `d=m` chain has
`2m` singleton blocks, so its reset excess is `2m-1`, two below this generic
weight.

If every arc is globally oriented `d -> d-1`, at most `c_(d+1)` vertices of
radius `d` can have predecessors.  Thus at least

\[
                    (c_d-c_{d+1})_+
\]

components start there.  This proves the exact lower bound (5.2), including
the conservative subtraction of two for `d=m`.

From (B),

\[
 \frac{c_{d+1}}{c_d}
 =\frac{(2d+3)(m-d)}{(2d+1)(m+d+2)}.
\]

It crosses one at

\[
                   d_*=(1/\sqrt2+o(1))\sqrt m.
\]

For `d=x sqrt(m)` with bounded `x`, Stirling's formula gives

\[
 c_d=\frac{W(2m)}{\sqrt m}
          (2xe^{-x^2}+o(1)).                         \tag{C}
\]

The positive differences are the decreasing tail.  Summation by parts gives

\[
\begin{aligned}
\sum_{d\ge d_*}(2d+1)(c_d-c_{d+1})
 &=(2d_*+1)c_{d_*}+2\sum_{d>d_*}c_d\\
 &\sim \frac2{\sqrt e}W
    +2W\int_{1/\sqrt2}^{\infty}2xe^{-x^2}\,dx\\
 &=\frac4{\sqrt e}W.
\end{aligned}
\]

To make the passage from bounded `x` in (C) to the improper integral fully
rigorous, use the standard central-binomial Gaussian tail bound and then let
the fixed cutoff tend to infinity.  This domination step is implicit in the
source but valid.

## 9. Globally reversed constant

If every arc is instead globally oriented `d -> d+1`, the starts are bounded
below by `(c_d-c_(d-1))_+`, with `c_(-1)=0`.  On the increasing side,
summation by parts yields

\[
\begin{aligned}
\sum_{0\le d\le d_*}(2d+1)(c_d-c_{d-1})
 &=(2d_*+1)c_{d_*}-2\sum_{0\le d<d_*}c_d\\
 &\sim \frac2{\sqrt e}W
       -2W\int_0^{1/\sqrt2}2xe^{-x^2}\,dx\\
 &=\left(\frac4{\sqrt e}-2\right)W.
\end{aligned}
\]

This is positive (`0.4261... W`).  No radius-`m` correction changes the
leading term in this orientation.

## 10. Exact theorem scope after audit

What is proved is:

> A direct transversal using one chosen exposing state per SCD chain, no
> auxiliary assigned states, and arcs of one globally fixed monotone radius
> orientation has linear reset excess.  The constants are `4/sqrt(e)` for
> decreasing radius and `4/sqrt(e)-2` for increasing radius.

This does **not** prove the same bound for:

* a mixture of increasing and decreasing components;
* same-radius motion;
* components that reverse their radius direction;
* transitions that skip radii;
* schemes in which reset states simultaneously discharge additional chains;
* general MTF--SCD covers, let alone general universal OR arrays.

Accordingly the source's constructive conclusion is valid in its narrow
form: a successful version of this particular induction cannot use only one
globally oriented radius ladder.  The broader statement that all
"monotone-radius collision resolutions" are excluded should not be entered
in the theorem ledger without defining them to mean precisely this direct,
globally oriented model.

