# Move-to-front audit of the radius-pure Bender--Knuth cubes

This note tests whether the abstract radius-pure Bender--Knuth cubes from
`TABLEAU_CRYSTAL_AUDIT.md` can be used in the weaker path-cover target of
`GLOBAL_MTF_SCD_HANDOFF.md` and `MTF_TRANSVERSAL.md`.

The answer is negative for the two natural chain assignments.

1. Two positive-radius canonical RSK/crystal chains joined by one
   Bender--Knuth edge have **no** one-step move-to-front transition in either
   direction, even after using the full ordered-partition fibers.
2. If one ignores the canonical chains and assigns to a locally geodesic
   middle path its natural consecutive-intersection/union chains, consecutive
   chains again have no MTF transition in either direction.

Thus a Bender--Knuth cube cycle decomposes into singleton MTF path components;
its component length is `1`, not `>>sqrt(m)`.  The cheap-reset theorem cannot
make this useful asymptotically.

Throughout, a saturated chain is written

\[
 C=(B; e_1,e_2,\ldots,e_h),                           \tag{0.1}
\]

meaning

\[
 B\subset B+e_1\subset B+e_1+e_2\subset\cdots.
\]

Recall the exact quotient-chain criterion from `MTF_TRANSVERSAL.md`: there is
some exposing state of `C` and one MTF update leading to an exposing state of
`D=(A;f_1,...,f_h)` with `A!=emptyset` if and only if `C-A` and `D-A` are
cross-nested.

## 1. The exact Bender--Knuth diamond on crystal chains

Let `Q,Q'=tau_iQ` be two standard tableaux of the same two-row shape, where
the elementary Bender--Knuth move is nontrivial.  Fix the unique binary
semistandard insertion tableaux of all weights in the corresponding
`sl_2` string.  Inverse RSK gives two canonical saturated chains `C_Q,C_Q'`
of the same length.

The two-letter inverse-RSK local rule has the following flag form.

### Lemma 1 (BK flag diamond)

After orienting the edge and renaming coordinates, exactly one of the
following occurs.

**Type I (direct minimum/top swap).**  For some common minimum `K`, common
increment word `E=(e_1,...,e_h)`, and distinct `x,y` outside `E`,

\[
 C_Q=(K+x;E),\qquad C_{Q'}=(K+y;E),                    \tag{1.1}
\]

with `x` in the top complement of `C_(Q')` and `y` in the top complement of
`C_Q`.

**Type II (one rhombus).**  For one index `t` and distinct `x,y,z`, the flags
agree outside the displayed positions and

\[
\begin{array}{c|ccc}
 &\text{minimum}&\text{increment }t&\text{top complement}\\ \hline
 C_Q    &x&y&z\\
 C_{Q'} &y&z&x.
\end{array}                                           \tag{1.2}
\]

In particular the two increment words differ in zero or one position.

### Proof

Run inverse row insertion for `(P,Q)` and `(P,Q')` simultaneously, first for
the lowest binary weight and then while applying the `sl_2` raising operator.
The deletion orders differ only by interchanging the consecutive
incomparable corners labeled `i,i+1`.  After all larger labels have been
deleted, these are the top-right and bottom-right corners of a two-row shape.

At every binary weight, the insertion tableau has bottom row identically
`2`, while its top row consists of one block of `1`s followed by one block of
`2`s.  Reverse insertion from the bottom corner changes the rightmost top-row
`1` into a `2`; reverse insertion from the top corner deletes its current
entry.  Interchanging the two corner deletions can therefore affect their
endpoints only when that moving `1|2` boundary is at the top corner.  Along
the `sl_2` string the boundary moves monotonically, so this event occurs at
most once.  If it never occurs, one minimum output and one top-complement
output are exchanged, giving (1.1).  If it occurs at chain step `t`, the
displaced endpoint is the `t`-th increment and the three affected outputs
cycle as in (1.2).  All other reverse deletions are identical in the two
orders.  This proves the lemma.

Equivalently, at every rank the two chain members are Johnson neighbours.
As the rank increases, the unique ordered pair of differing coordinates is
constant except possibly at one rhombus; monotonicity of the two saturated
chains gives exactly the two cases above.  QED.

The second paragraph is also a purely set-theoretic derivation once the
two-letter inverse-RSK fact that corresponding ranks are Johnson neighbours
and their difference pair changes at most once is recorded.

## 2. No MTF edge between the canonical chains

### Theorem 2

If the common chain length is `h>=2`, then neither directed transition

\[
 C_Q\longrightarrow C_{Q'},\qquad
 C_{Q'}\longrightarrow C_Q                              \tag{2.1}
\]

exists in the full MTF state-fiber graph.

### Proof

Use the quotient-chain criterion.

In Type I, anchor at the target minimum `A=K+y`.  The source quotient begins
with the nonempty singleton `{x}`.  The target quotient begins

\[
 \varnothing\subset\{e_1\}\subset\cdots,
\]

and `x` is not an increment of the target.  Hence `{x}` and `{e_1}` are
incomparable.  The reverse direction is identical with `x,y` interchanged.

In Type II, orient the table as in (1.2) and anchor first at the minimum of
`C_(Q')`.  The source quotient begins `{x}`, while `x` is in the target top
complement and hence is not one of its increments.  Cross-nesting fails at
the first target singleton.

For the reverse direction, the source quotient begins `{y}`.  If `t>1`, this
already crosses the target singleton `{e_1}`.  If `t=1`, the two quotients
share the first singleton `{y}`, but the next source block adds `z`, whereas
the next target block adds `e_2`.  Here `z` belongs to the target top
complement and `h>=2`, so these two size-two sets are incomparable.  Thus the
reverse direction also fails.  QED.

For the `2m`-cube every positive chain radius has `h=2d>=2`.  The only
exception is radius zero, where a chain is the singleton `{X}`.  Such chains
can be threaded arbitrarily: updating by the next middle set `Y` makes `Y`
the first block and exposes it immediately.  But there are only

\[
 \operatorname {Cat}_m=\frac1{m+1}\binom{2m}m=o(W)    \tag{2.2}
\]

radius-zero chains.

Consequently every positive-radius Bender--Knuth cube cycle has no internal
MTF edge at all.  Following its edges gives one MTF component per chain.

## 3. The natural window-chain replacement also fails

Perhaps the canonical RSK chains are the wrong chains.  The obvious
alternative is to use the chains already generated by a locally geodesic
middle path.

Let

\[
 X_{t+1}=X_t-\{a_t\}+\{b_t\},                         \tag{3.1}
\]

and suppose the exchange coordinates in every relevant window are distinct.
For a fixed `d>=1`, define the natural radius-`d` chain centered at `X_t` by
consecutive intersections and unions.  Its minimum and increment word are

\[
\begin{aligned}
 B_t&=X_t\setminus\{a_t,a_{t+1},\ldots,a_{t+d-1}\},\\
 E_t&=(a_{t+d-1},\ldots,a_t,
       b_t,b_{t+1},\ldots,b_{t+d-1}).                 \tag{3.2}
\end{aligned}
\]

### Theorem 3 (sliding-window fence)

There is no one-step MTF transition between `C_t=(B_t;E_t)` and
`C_(t+1)=(B_(t+1);E_(t+1))` in either direction.

### Proof

The next minimum is

\[
 B_{t+1}=B_t-\{a_{t+d}\}+\{b_t\}.                    \tag{3.3}
\]

Anchor the forward transition at `B_(t+1)`.  Both quotient chains initially
agree through

\[
 \{a_{t+d}\},
 \{a_{t+d},a_{t+d-1}\},\ldots,
 \{a_{t+d},\ldots,a_{t+1}\}.                         \tag{3.4}
\]

At the next step the source quotient adds the obsolete departure `a_t`,
whereas the target quotient adds the new arrival `b_(t+1)`.  These coordinates
are distinct by local geodesicity, so the two next sets cross.

In the reverse direction the source minimum quotient begins `{b_t}`.  But
`b_t` is not the first increment `a_(t+d-1)` of the target chain, so the first
nonempty quotient sets already cross.  QED.

The obstruction is exactly the MTF prefix fence: a coordinate that has just
left the sliding middle window remains trapped inside the old chain's ordered
increment list, while the next chain needs it in the tail.

## 4. Reset accounting

Let a Bender--Knuth cube contain `N` positive-radius chains.  Theorems 2 and 3
show that either natural use of its cycle yields `p=N` MTF components of
length one.  A canonical chain of radius `d` has a smallest exposing state
with at least

\[
 2d+2                                                   \tag{4.1}
\]

blocks when its minimum and top complement are nonempty.  Even granting a
uniform `O(sqrt(m))` reset for the typical radii, the path-cover bound pays

\[
 pH=\Theta(N\sqrt m),                                  \tag{4.2}
\]

not `o(N)`.  The universal `2m`-block reset is worse.

Indeed, if `V_d=binom(2m,m-d)-binom(2m,m-d-1)` is the number of radius-`d`
chains, then

\[
 \frac1W\sum_d dV_d
 =\sum_{q\ge1}\frac{\binom{2m}{m-q}}W
 =\Theta(\sqrt m),                                    \tag{4.3}
\]

by the central local limit estimate.  Thus the total minimum block count of
singleton positive-radius components is genuinely `Theta(W sqrt(m))`.

Therefore the radius-pure Bender--Knuth cubes do not advance the current
GLOBAL_MTF target.  To use tableaux in that program one needs transitions
between *different* cubes/radii whose flag diamonds satisfy the quotient
fence, or an SCD whose flags are designed for MTF dynamics from the outset.
