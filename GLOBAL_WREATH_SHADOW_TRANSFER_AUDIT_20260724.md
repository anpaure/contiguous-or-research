# Audit of the global wreath-shadow transfer theorem

## Verdict

The transfer inequality in the supplied note is correct.  It is an exact
contiguous-OR construction, not merely a central-row or factor-labeling
reduction.  It does **not** prove the constant-one theorem because the required
growing-depth low-defect wreath factor remains unconstructed.

The result is essentially the explicit two-sided form of item 438 in
`MATHEMATICAL_HANDOFF.md`.  Its useful additions are the closed-form word
length and the observation that all factorability and pin constraints vanish
because the cyclic intervals are emitted as literal OR entries.

Two clarifications should be included whenever the theorem is quoted:

1. Mütze--Standke--Wiechert prove a `C_(2m+1)`-factor of the odd graph.
   One needs the elementary shortest-cycle-to-wreath lemma below to obtain
   the cyclic coordinate orders used in the OR construction.
2. The displayed depth should be read as
   `H=(1/2+epsilon)sqrt((2m+1)log(2m+1))`; without the square root it would
   contradict the required condition `H=o(m)`.

## 1. Exact middle wreath factor

Let `n=2m+1`.  Theorem 4 of Mütze--Standke--Wiechert, *A minimum-change
version of the Chung--Feller theorem for Dyck paths*, gives a factor of the
odd graph `K(n,m)` into `Cat_m` cycles of length `n`.

Every such shortest odd cycle is a wreath.  Indeed, write its vertices as
`A_0,...,A_(n-1)` and let `z_i` be the unique coordinate outside
`A_i union A_(i+1)`.  For a coordinate `z`, let `t_z` be the number of
edges labelled `z`.  Across an edge not labelled `z`, membership of `z`
toggles; across an edge labelled `z`, both endpoints omit it.  Closure around
the odd cycle gives

    n-t_z = 0 (mod 2).

Thus every `t_z` is odd.  Since `sum_z t_z=n` over the `n` coordinates,
every `t_z=1`; in particular `(z_0,...,z_(n-1))` is a permutation.  Since
successive vertices are disjoint,

    A_(i+2)=A_i union {z_i} minus {z_(i+1)}.

Solving this recurrence around the cycle gives

    A_i={z_(i+1),z_(i+3),...,z_(i+2m-1)}.

Ordering the coordinates by step two therefore makes the `A_i` exactly the
`n` cyclic intervals of length `m`.  The cycle factor consequently gives
`B=Cat_m=binom(n,m)/n` pairwise disjoint wreaths partitioning the middle
layer.

## 2. Window identity and exact length

Fix `1<=H<m`.  For one wreath `pi`, put

    E_j=I_pi(j,m-H).

Emit

    E_0,...,E_(n-1),E_0,...,E_(2H).

The repeated prefix has the exact required length: a cyclic window of at most
`2H+2` entries beginning at `E_(n-1)` needs `2H+1` entries after the wrap.
For every `1<=t<=2H+2`, because `m-H+t-1<n`,

    OR_(s=0)^(t-1) E_(j+s)=I_pi(j,m-H+t-1).

Taking `t=H-q+1` yields rank `m-q`; taking `t=H+q+2` yields rank
`m+1+q`.  The block length is `n+2H+1`, so all `B` wreaths cost

    W + ((2H+1)/n)W.

The upper depth-`q` family is the complement of the lower depth-`q` family
up to a cyclic shift.  Hence their defects are equal.  Appending every
missing mask through depth `H`, followed by both literal tails, proves

    nu(2m+1) <= W + ((2H+1)/n)W
                   + 2 sum_(q=1)^H M_q(F)
                   + 2 sum_(r=0)^(m-H-1) binom(n,r) - 1.

The final `-1` removes the empty lower-tail mask; the full mask in the upper
tail remains required.

## 3. Asymptotic threshold

Take

    H=ceil((1/2+epsilon)sqrt(n log n)).

Then `H=o(n)` and the wreath-linearization overhead is `o(W)`.  Hoeffding's
bound gives a one-sided literal tail at most

    2^n exp(-2H^2/n+o(1)).

(The factor `2^(n-1)` appearing in one draft is not the direct Hoeffding
prefactor; replacing it by `2^n` is safe and leaves the asymptotic threshold
unchanged.)

Since `W=Theta(2^n/sqrt(n))`, its ratio to `W` is
`O(n^(-2epsilon-2epsilon^2))=o(1)`.  Therefore

    sum_(q=1)^H M_q(F)=o(W)

is sufficient for `nu(2m+1)=W+o(W)`.  The established one-bit trimmed lift
then gives the even dimensions because
`W(2m+2)=2W(2m+1)`.

## 4. Exact-resolution equivalence

Let `Omega={(pi,j)}` be the `W` pointed wreath starts.  For one start
`omega=(pi,j)` and radius `d`, the sequence

    I_pi(j,m-d) subset ... subset I_pi(j,m)
      subset I_pi(j,m+1) subset ... subset I_pi(j,m+1+d)

is a saturated symmetric chain.  Consequently, nested sets

    Omega=A_0 superset A_1 superset ... superset A_m,
    |A_q|=binom(n,m-q),

whose lower and upper depth-`q` interval maps are both bijective define an
exact SCD: give `omega` radius `max{q:omega in A_q}`.  The two bijections at
each depth partition the two ranks at that depth.  Conversely, any exact SCD
made from these pointed cyclic chains has exactly these active-start sets.
Thus the equivalence stated in the prompt is exact (including `q=m`, where a
single active start supplies the empty and full sets).

This exact resolution is strictly stronger than the transfer theorem needs.
The latter uses the full domain `Omega` at every depth, tolerates collisions,
and appends only the missed masks.  Also, the literal-word construction
*bypasses* lower-meet-core and pin questions rather than proving a separate
meet-core factorization: every covered lower mask is itself the OR of the
displayed consecutive `E_j` entries, all of which are subsets of that mask.

## 5. What remains open

No known exact wreath factor is proved to have summed defect `o(W)` through
this growing depth.  Random mean-one shadows have Poisson-scale collisions;
fixed-depth or one-rank packings do not control a common exact middle factor
uniformly through `Theta(sqrt(m log m))` depths.  Signed wreath
decompositions likewise do not supply one nonnegative exact factor.

Thus the correct status is:

    exact wreath transfer and all OR/pin accounting: proved;
    growing-depth multiscale near-resolution: open;
    nu(k)=(1+o(1))W(k): not yet proved.
