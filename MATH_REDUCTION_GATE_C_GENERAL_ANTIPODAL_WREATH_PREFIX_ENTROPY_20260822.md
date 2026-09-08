# Gate C: general antipodal labellings, exact prefix tests, and the block-entropy threshold

**Status (2026-08-22).**  Every general assertion below is proved.  An
arbitrary antipodal coordinate permutation applied to the descending tour
admits an exact prefix-height formula for every coherent flag and both
phases.  The formula reduces the multiplicity gate to a concrete signed
permutation problem.

Two rigorous entropy conclusions follow.

1. Factor overlap `q-L` forces the orientation/sign word to have at most
   `L/(2h)` cyclic transitions; hence signs contribute only `exp(o(b))`
   choices whenever `L=o(q)`.
2. If the residue permutation has at most `K` cyclic successor breaks and
   the parity-corrected sign word `c` has `o(b)` transitions, then this
   high-overlap-compatible signed subfamily has size `exp(o(b))` for
   `K=o(b/log b)`.  At the sharp
   scale `K=c b/log b`, its residue entropy is `exp((c+o(1))b)`.  Thus this
   descending-block route is entropy-insufficient for `c<log 4` but
   entropy-viable for `c>log 4`.

What remains open is analytic, not enumerative: prove that exponentially
many of the viable block permutations actually pass enough of the prefix
tests to have `q-O(bK)` factor overlap, or prove that high overlap forces a
smaller, low-entropy subclass.

Throughout,
\[
 n=2b,qquad b\ge3\text{ odd},qquad
 h={b-1\over2},qquad q=b(b-1).                           \tag{0.1}
\]

## 1. The full antipodal wreath action

An antipodal coordinate permutation is a permutation `pi` of
`Z_(2b)` satisfying
\[
                         \pi(x+b)=\pi(x)+b\pmod {2b}.     \tag{1.1}
\]
It is uniquely parameterized by a residue permutation
`alpha in S_b` and an orientation word `epsilon in {0,1}^b`:
\[
\begin{aligned}
 \pi(x)&=\alpha(x)+b\epsilon_x\pmod {2b},\\
 \pi(x+b)&=\pi(x)+b\pmod {2b},
 \qquad 0\le x<b.                                      \tag{1.2}
\end{aligned}
\]

Apply `pi` to the descending Hamilton listing
\[
                         H^*=(-i\pmod {2b})_{i=0}^{2b-1}. \tag{1.3}
\]
The sparse antipodal-swap construction is the special case
`alpha=id`, with a sparse orientation word.  Here no restriction is made.

For a coherent template with offset `z` and internal position `t`, put
\[
                         r=-z-b-t\pmod {2b}.              \tag{1.4}
\]
Before applying `pi`, its middle and arc are
\[
 C^0_{r,t}=r+([0,b]\setminus\{t\}),qquad r\longrightarrow r-1. \tag{1.5}
\]
After applying `pi`, write
\[
 C^\pi_{r,t}=\{\pi(r+u):0\le u\le b,\ u\ne t\},qquad
 p_r=\pi(r),\qquad q_r=\pi(r-1).                         \tag{1.6}
\]

## 2. Exact all-labelling prefix-height criterion

For `0<=ell<=2b`, define
\[
 A^\pi_{r,t}(\ell)=
 \left|\left\{u\in[0,b]\setminus\{t\}:
  (\pi(r+u)-p_r)\bmod {2b}<\ell\right\}\right|,          \tag{2.1}
\]
and
\[
                         H^\pi_{r,t}(\ell)
 =2A^\pi_{r,t}(\ell)-\ell.                              \tag{2.2}
\]
This is exactly the prefix height of the membership word of
`C^pi_(r,t)` rotated to start at its arc-start coordinate `p_r`.

### Theorem 2.1 (exact wreath membership test)

The flag indexed by `(r,t)` belongs to the Catalan-switched factor if and
only if exactly one of the following holds.

* **Ordinary case.**  `q_r<p_r`, `(p_r,q_r)!=(2b-1,0)`, and, with
  \[
  \ell_r=(q_r-p_r)\bmod {2b}+1=2b-p_r+q_r+1,             \tag{2.3}
  \]
  one has
  \[
  \begin{array}{ll}
  H^\pi_{r,t}(\ell)>0,&1\le\ell<\ell_r,\\
  H^\pi_{r,t}(\ell_r)=0,&\\
  H^\pi_{r,t}(\ell)\ge0,&\ell_r<\ell\le2b.
  \end{array}                                            \tag{2.4}
  \]
* **Switched case.**  `(p_r,q_r)=(0,2b-1)` and
  \[
  H^\pi_{r,t}(\ell)>0\quad(1\le\ell<2b),
  \qquad H^\pi_{r,t}(2b)=0.                              \tag{2.5}
  \]

#### Proof

Equation (2.2) is the definition of rotated walk height.  In the ordered
Greene--Kleitman factor, the arc-end `q` is the first arrival at the final
global minimum and the arc-start `p` is the up-step after the last visit
to that minimum.  Equivalently, rotation at `p` is Dyck and first returns
at `q`, which is exactly (2.3)--(2.4).  The Catalan switch removes all
`(2b-1)->0` flags and inserts exactly the primitive-Dyck
`0->(2b-1)` flags, giving (2.5). \(\square\)

For phase `delta`, the exact overlap is therefore
\[
 M_\delta(\pi)=
 \sum_{t=1}^{b-1}\sum_{s=0}^{b-1}
 \mathbf1_{\mathfrak F^*}
 \left(r=-\delta-s(b+1)-b-t,\ t\right).                 \tag{2.6}
\]
For each fixed `t`, the two phases partition all `2b` possible values of
`r`; hence
\[
 M_0(\pi)+M_1(\pi)=
 \sum_{t=1}^{b-1}\sum_{r\in\mathbb Z_{2b}}
 \mathbf1_{\mathfrak F^*}(r,t).                         \tag{2.7}
\]
Equations (2.1)--(2.7) are an exact finite dynamic program requiring only
the signed permutation `pi`; no SCD or tour data remain implicit.

## 3. High overlap removes sign entropy

Let
\[
 P_x=\alpha(x)+\epsilon_x\pmod2,
 \qquad c_x=P_x+x\pmod2,qquad x\in\mathbb Z_b.          \tag{3.1}
\]
Because `b` is odd, `P_x` is the coordinate parity of `pi(x)`.  The two
antipodal Hamilton edges above the residue edge `x->x-1` are cross-parity
if and only if
\[
                         c_x=c_{x-1}.                    \tag{3.2}
\]
Thus the number of same-parity Hamilton edges is twice the cyclic
transition count
\[
 T(c)=|\{x:c_x\ne c_{x-1}\}|.                           \tag{3.3}
\]

Every factor arc crosses coordinate parity, and every Hamilton edge occurs
in exactly `h` flags of either coherent phase.  Consequently
\[
 \boxed{M_\delta(\pi)\le q-2hT(c).}                      \tag{3.4}
\]
In particular, `M_delta(pi)>=q-L` forces
\[
                         T(c)\le {L\over2h}.              \tag{3.5}
\]

For fixed `alpha`, equation (3.1) is a bijection between orientation words
`epsilon` and binary words `c`.  The number with `T(c)<=R` is at most
\[
                         2\sum_{i=0}^R\binom bi.          \tag{3.6}
\]
If `R=o(b)`, its logarithm is
\[
                         O\left(R\log{eb\over R}\right)=o(b). \tag{3.7}
\]
So no coefficient-one high-overlap family obtains a hidden `2^b` factor
from arbitrary antipodal orientations.

## 4. Exact descending-block entropy

For `alpha in S_b`, define its cyclic successor-break count
\[
 B(\alpha)=
 |\{x\in\mathbb Z_b:\alpha(x)\ne\alpha(x-1)+1\pmod b\}|. \tag{4.1}
\]
Thus `B(alpha)=K` says that the cyclic listing
`alpha(0),...,alpha(b-1)` is a concatenation of `K` directed intervals of
consecutive residues.

### Lemma 4.1 (block-permutation count)

For `1<=K<=b`,
\[
 |\{\alpha:B(\alpha)=K\}|
 \le b\binom bK(K-1)!.                                   \tag{4.2}
\]

#### Proof

The `K` broken value-successor edges cut the directed residue cycle into
`K` consecutive intervals.  Choose those cuts, cyclically order the
resulting intervals, and choose one of the `b` positions at which to root
the resulting cyclic listing.  This gives the right side of (4.2), and
may overcount when a reordered boundary accidentally restores a successor
edge. \(\square\)

Consequently, uniformly for `K=o(b)`,
\[
 \log |\{\alpha:B(\alpha)\le K\}|
 \le K\log b+O(K+\log b).                                \tag{4.3}
\]
The scale in (4.3) is sharp in its leading exponential order.  Partition
the residue cycle into `K` fixed, nearly equal consecutive intervals and
permute those intervals arbitrarily.  This gives at least `K!` rooted
listings with at most `K` breaks, and
\[
                         \log K!=K\log K-K+O(\log K).     \tag{4.4}
\]

### Theorem 4.2 (the `b/log b` entropy threshold)

Let `K=K_b`, `R=R_b=o(b)`, and consider all signed antipodal permutations
with
\[
                         B(\alpha)\le K,qquad T(c)\le R. \tag{4.5}
\]
Then:

1. if `K=o(b/log b)`, the family has size `exp(o(b))` and is
   exponentially too small for `Theta(4^b/b^(5/2))` tours;
2. if `K=c b/log b+O(1)` for fixed `c>0`, its logarithm is at most
   \[
                         (c+o(1))b,                       \tag{4.6}
   \]
   while the block-permutation subfamily has logarithm at least
   `(c+o(1))b`;
3. therefore the descending-block family is entropy-insufficient when
   `c<log 4`, and is entropy-viable (as a candidate count) when
   `c>log 4`.

#### Proof

Multiply (3.6) by the sum of (4.2) through `K`.  Equations (3.7) and
(4.3) prove item 1.  If `K=c b/log b`, then
`K log b=cb+o(b)`, while the orientation term remains `o(b)`.
This proves the upper bound in item 2.  For every fixed-block residue
permutation, choose `c_x=0` for all `x` in (3.1); this uniquely determines
the orientation word and has `T(c)=0`.  The fixed-block construction and
Stirling in (4.4) therefore give a signed subfamily with
\[
 K\log K-K=cb+o(b),                                      \tag{4.7}
\]
proving the matching lower entropy.  Since the required supply has natural
logarithm `b log 4-O(log b)`, item 3 follows. \(\square\)

The lower bound in item 2 is purely an entropy statement.  It does not say
that arbitrary block orders satisfy the prefix inequalities (2.4)--(2.5).
That is precisely the live multiplicity gate.

## 5. Finite calibration and scope

Exhaustion of the full signed antipodal wreath family gives the following
checks on the exact criterion:

* at `b=5`, among `2^5 5!=3840` labellings, the largest two-phase overlap
  is `30`, attained by exactly the `10=2b` coordinate rotations; every
  nonrotation has overlap at most `12`;
* at `b=7`, among `2^7 7!=645120` labellings, the largest two-phase overlap
  is `70`, attained by exactly the `14=2b` rotations; every nonrotation has
  overlap at most `42`.

These finite gaps suggest rigidity but are not used as an asymptotic
theorem.  Sparse antipodal swaps prove that nonrotations can have
`q-o(q)` overlap once `b` grows, so a constant-fraction gap is false.

The exact remaining question is now narrow: among the
`exp((c+o(1))b)` block orders at `K=c b/log b` (or another comparably large
signed-permutation family), count those satisfying all but `O(bK)` of the
prefix tests.  A lower bound above `4^b/poly(b)` would supply enough local
tour candidates; a matching entropy upper bound below that scale would
close this antipodal multiplicity route.

## 6. Finite audit

The companion checker
`scratch/verify_gate_c_general_antipodal_wreath_prefix_entropy_20260822.py`
verifies the exact prefix criterion against direct factor construction,
the phase partition identity, the parity-transition formula, and the
block-count bound.  Its finite spectrum computation is confirmatory; all
general proofs are above.
