# Full hook envelopes, token slides, and the three-dimer obstruction

**Date:** 2026-08-06  
**Method:** exact all-terminal hook envelope algebra, token-slide
monotonicity, and cyclic run parity; no computation or search  
**Status:** unconditional scoped no-go for the proposed native
single-hook-interval completion.  The largest-gap estimate always pays the
mass budget for parity-compatible multi-run targets, but not every low
target is parity compatible.  Beginning at rank six, some targets have
zero degree in the hook-interval Hall graph.

## 1. Parameters and notation

Put

\[
 n=2m+1,\qquad d=h-1,\qquad p=2d+1,
 \qquad b=m-d-1.
\tag{1.1}
\]

At one rooted hook phase, list all `b` free leaves by their slot numbers,
including the terminal slot:

\[
 1\le c_1\le\cdots\le c_b\le p.
\tag{1.2}
\]

If the physical root is `q`, write `P` for the maximal depth-`d` source
envelope.  All coordinates below are read modulo `n`; in monotonicity
arguments they are lifted to one interval of integers.

## 2. The full survivor-envelope formula

### Theorem 2.1 (all-terminal hook envelope)

After translating the root to zero,

\[
 \boxed{P=\{0\}\cup\{c_i+2i:1\le i\le b\}.}
\tag{2.1}
\]

Consequently the hook envelopes rooted at `q` are exactly

\[
 \boxed{
 P=\{q\}\cup(q+J),\qquad
 J\in\binom{\{3,4,\ldots,n-2\}}b,
 \quad J\text{ has no consecutive elements}.}
\tag{2.2}
\]

If the terminal occupancy is `z`, then the last `z` entries of `(1.2)`
equal `p`, and hence

\[
 \{q-2z,q-2z+2,\ldots,q-2\}\subseteq P.
\tag{2.3}
\]

The mandatory core is the first and the root ends of this terminal bank:

\[
 F=\{q,q-2z\}.
\tag{2.4}
\]

#### Proof

The `i`-th free-leaf up-step in the rooted hook word occurs after `c_i`
spine slots and `i` free peaks, hence at physical offset `c_i+2i`.
Exactly the free-leaf up-steps and the current root survive the next
`h=d+1` owners, giving `(2.1)`.

The inequalities

\[
 3\le c_1+2,
 \qquad c_b+2b\le p+2b=n-2,
\]

and

\[
 (c_{i+1}+2(i+1))-(c_i+2i)\ge2
\]

give `(2.2)`.  Conversely, `c_i=w_i-2i` recovers a unique weak
composition from every nonconsecutive `b`-set
`3<=w_1<...<w_b<=n-2`.

If exactly `z` free leaves occupy the terminal slot, their indices are
`b-z+1,...,b`; substituting `c_i=p` gives the offsets

\[
 n-2z,n-2z+2,\ldots,n-2.
\]

The first one is the exit deletion and `(2.4)` is the authenticated hook
mandatory-core formula.  \(\square\)

Every `P` is an independent set in the ordinary cycle graph: it contains
no adjacent coordinates.

### Theorem 2.2 (one-token slide)

For consecutive source phases put

\[
 y_i=q_i-2z_i,
 \qquad q_{i+1}=y_i-1.
\tag{2.5}
\]

Then

\[
 \boxed{P_{i+1}=P_i-\{y_i\}+\{y_i-1\}.}
\tag{2.6}
\]

In particular,

\[
 \boxed{
 \bigcup_{i=0}^{\ell-1}P_i
 =P_0\cup\{q_1,\ldots,q_{\ell-1}\}.}
\tag{2.7}
\]

#### Proof

Rotating the terminal hook slot deletes the first terminal free leaf
`y_i` from the common `h`-owner intersection and inserts the new physical
root `y_i-1`.  All other free-leaf labels remain common.  This is `(2.6)`;
iteration gives `(2.7)`.  \(\square\)

Thus every extra target coordinate not used as a later root must already
belong to the one independent set `P_0`.  The envelopes do not provide
independent fresh banks at every source position.

## 3. No wrap at the low deadline

For a budgeted source interval of length `ell<=d`,

\[
 \sum_{i=0}^{\ell-1}(q_i-q_{i+1})
 =\sum_i(2z_i+1)
 \le2b+d
 =2m-d-2<n.
\tag{3.1}
\]

Hence every such hook path has a unique lift

\[
 q_0>q_1>\cdots>q_\ell>q_0-n.
\tag{3.2}
\]

All target runs and all forced token slides are encountered in one cyclic
order, with exactly one cut at the terminal end of the source interval.

## 4. Every maximal dimer forces its own slide

Call

\[
 R=\{a,a-1\}
\tag{4.1}
\]

a **maximal dimer** of `S` when `a+1,a-2` are absent from `S`.

### Lemma 4.1 (forced dimer transition)

Suppose a hook interval satisfies

\[
 \bigcup_iF_i\subseteq S\subseteq\bigcup_iP_i.
\tag{4.2}
\]

Then every maximal dimer `(4.1)` forces a transition

\[
 \boxed{y_i=a,\qquad q_{i+1}=a-1}
\tag{4.3}
\]

at some nonfinal envelope step.

#### Proof

The independent set `P_0` cannot contain both `a` and `a-1`.

If `a-1` is not in `P_0`, identity `(2.7)` says it must be a later root
`q_{i+1}`.  Equation `(2.5)` then forces `y_i=a`, proving `(4.3)`.

If `a-1` is in `P_0`, then `a` is not.  It must be a later root, whose
predecessor token is `a+1`; but every predecessor token is in a mandatory
core and `(4.2)` would force `a+1 in S`, contradicting maximality.  The
initial root is also in `P_0`, so it gives no exception.  Hence the first
case is forced.

The transition cannot be the last source transition: its new root
`a-1` would then belong only to `P_ell`, absent from `(2.7)`.  \(\square\)

## 5. Odd exits are terminal

Assume now that `S` is a disjoint union of maximal dimers.  List them in
decreasing cyclic order as

\[
 R_j=\{a_j,a_j-1\},\qquad1\le j\le r,
\tag{5.1}
\]

and define the outgoing distance

\[
 D_j=(a_j-1)-a_{j+1}\pmod n,
 \qquad1\le D_j<n,
\tag{5.2}
\]

with cyclic indices.

### Lemma 5.1 (odd-exit obstruction)

If `D_j` is odd, `R_j` must be the terminal dimer of any hook interval
satisfying `(4.2)`.

#### Proof

By Lemma 4.1, after entering `R_j` the next source root is `a_j-1`.
If the source continues, its next departing token `y` and the following
root `y-1` must both lie in `S`.  In a union of maximal dimers, `y` is
therefore the top coordinate of another dimer.

The no-wrap order `(3.2)` forces it to be the immediately following dimer:
skipping one would move below that dimer before its forced transition
from Lemma 4.1 could occur.  Thus `y=a_{j+1}`.  But the hook recurrence
requires

\[
 (a_j-1)-a_{j+1}=2z,
\]

which is even.  When `D_j` is odd no continuation is possible.  \(\square\)

There is only one terminal dimer.  Consequently any pure-dimer target
with at least two odd outgoing distances has no hook-interval ticket,
even with maximal-envelope assistance.

## 6. A rank-six zero-neighbour target

For every odd `n>=13`, take

\[
 \boxed{S=\{0,-1,-4,-5,-8,-9\}\subseteq\mathbb Z_n.}
\tag{6.1}
\]

Its three maximal dimers are

\[
 \{0,-1\},\qquad\{-4,-5\},\qquad\{-8,-9\}.
\]

Their outgoing distances are

\[
 D_1=3,\qquad D_2=3,\qquad D_3=n-9.
\tag{6.2}
\]

The first two are odd.  Lemma 5.1 would require both first dimers to be
terminal, which is impossible.

### Theorem 6.1 (native single-hook covering is false)

For every eventual parameter with `d>=6`, the rank-six target `(6.1)`
has no budgeted hook source interval satisfying

\[
 \bigcup_iF_i\subseteq S\subseteq\bigcup_iP_i.
\tag{6.3}
\]

Therefore it has degree zero in the proposed short-hook-interval Hall
graph.  All its cyclic rotations have degree zero as well.

This is a structural no-go, not a shortage of components and not a cost
failure.

## 7. The largest-gap budget is favorable when parity permits

The obstruction above isolates the correct issue.  Let `S` instead be a
union of `r` maximal cyclic runs, all of length at least two.  Let their
lengths sum to `A<=d`, and let `D_1,...,D_r` be the distances from the
last coordinate of one run to the first coordinate of the next.  Then

\[
 \sum_{j=1}^rD_j=n-A+r.
\tag{7.1}
\]

Choose one gap `D_*` as the terminal cut.  If every other `D_j` is even,
there is an exact core-only hook word:

* walk through each run with `z=0`;
* at the last coordinate of a nonterminal run use
  `z_j=D_j/2`, whose secondary core is the first coordinate of the next
  run;
* terminate in the final run.

The emitted mandatory-core set is exactly `S`.  Its length is

\[
 \ell=A-r+1\le d,
\tag{7.2}
\]

and its mass cost is

\[
 Z={n-A+r-D_*\over2}.
\tag{7.3}
\]

Thus Theorem 2.1 of the hook core-language note realizes it whenever

\[
 \boxed{D_*\ge2d+3-A+r.}
\tag{7.4}
\]

Indeed `(7.4)` is exactly `Z<=b`.

For the largest gap,

\[
 D_*\ge{n-A+r\over r}
       \ge {2(n-d)\over d},
\tag{7.5}
\]

because `r<=A/2<=d/2`.  The established asymptotic

\[
 d^2={\pi n\over8}+O(\sqrt n)
\]

implies

\[
 {2(n-d)\over d}=(16/\pi+o(1))d>2d+2.
\tag{7.6}
\]

Since `A>=2r`, the right side of `(7.4)` is at most `2d+2`.
Therefore, for all sufficiently large parameters:

### Theorem 7.1 (parity-compatible multi-run ticket)

If all non-largest outgoing run distances are even, a target consisting
of runs of length at least two has a core-only hook ticket of length at
most `d` and cost at most `b`.

More generally any chosen cut satisfying `(7.4)` works when every
remaining distance is even.

So the proposed largest-gap idea succeeds on the mass ledger with a large
margin.  Its failure on `(6.1)` is purely the forced even-distance token
slide.

## 8. Consequence for the PBBS programme

The proposed statement

> every target of rank at most `d` has a ticket on one untouched hook
> component

is false.  Hence its component-Hall theorem is false before multiplicity
is considered: some left vertices have empty neighbourhoods.

This does not obstruct PBBS or `B(k)+O(1)`.  It says that the low atlas
must add at least one of:

1. a second action partition whose envelope update is not the oriented
   one-token slide `(2.6)`;
2. a protected seam joining two short hook intervals, so two odd exits can
   be terminal locally; or
3. a bounded packet which changes the cyclic parity of one inter-run
   bridge.

Ranks one and two and every one-run target remain closed.  The next honest
low-side theorem is a mixed-component or seam atlas for the pure-dimer
parity family, not a Hall estimate inside the native single-hook graph.
