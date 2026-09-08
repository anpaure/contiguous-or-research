# Involution orbit-mass floor: selective switching still needs duplicates

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let `F` be an exact middle wreath factor and let `sigma` be a coordinate
involution.  For a diagonal row replacement

\[
                  F_A=(F\setminus A)\sqcup\sigma A,
\]

the total depth-`q` load on every two-element target orbit
`{S,sigma S}` is invariant.  It follows that a target orbit of total load
zero, one, or at least two has an unavoidable minimum of respectively two,
one, or zero holes.

Consequently the number of holes which any selective diagonal switch can
remove is at most

\[
 \boxed{
 A^{(2)}_{\sigma,q}(F)
 =\#\{S:\mu_q^F(S)=0,\ \mu_q^F(\sigma S)\ge2\}.}
\tag{0.1}
\]

In particular a hole paired with a singleton-covered target can only be
moved, never eliminated.  Selective switching removes the *fair-coin
formalism* surrounding duplicate supply; it does not remove duplicate
supply itself.

For the parallel-pair involution class, class-average Johnson mixing gives
an involution with `A^(2)` essentially `h d/N`, where `h` is the number of
holes and `d` the number of targets of load at least two.  At the first
shadow, the exact wreath cap implies only `d=Omega(h/m)`.  Thus the
universally forced productive supply is of order `h^2/(mW)`, not order
`h`.  This recovers, without any fair-coin argument, the genuine
factor-`m` bottleneck.

## 1. Exact orbitwise load conservation

Fix a depth `q` and abbreviate

\[
 \mu(S)=\mu_q^F(S).
\]

For `A subseteq F`, let

\[
 a_A(S)=\#\{C\in A:S\text{ is an }(m-q)\text{-interval of }C\}.
\tag{1.1}
\]

The diagonal replacement removes those old occurrences and adds the
`sigma`-images of the occurrences in `A`.  Since `sigma^2=1`,

\[
 \boxed{
 \mu_A(S)=\mu(S)-a_A(S)+a_A(\sigma S).}
\tag{1.2}
\]

Hence for every two-element target orbit `{S,T}`, `T=sigma S`,

\[
 \boxed{\mu_A(S)+\mu_A(T)=\mu(S)+\mu(T).}
\tag{1.3}
\]

For a fixed target `S=sigma S`, equation (1.2) gives

\[
                         \mu_A(S)=\mu(S).
\tag{1.4}
\]

Thus fixed holes are absolutely frozen, while nonfixed target-orbit mass
is merely redistributed between the two members.

## 2. The orbit-mass floor

Define

\[
 b(t)=
 \begin{cases}
 2,&t=0,\\
 1,&t=1,\\
 0,&t\ge2.
 \end{cases}
\tag{2.1}
\]

### Theorem 2.1

For every diagonal replacement `F_A`,

\[
 \boxed{
 H_q(F_A)\ge
 \#\{S:S=\sigma S,\ \mu(S)=0\}
 +\sum_{\{S,\sigma S\}}b\bigl(\mu(S)+\mu(\sigma S)\bigr),}
\tag{2.2}
\]

where the sum runs over the two-element target orbits.

Moreover, if arbitrary occurrence rows could be selected independently,
the right side would be the exact minimum.  Therefore

\[
 \boxed{
 H_q(F)-H_q(F_A)
 \le A^{(2)}_{\sigma,q}(F).}
\tag{2.3}
\]

#### Proof

Equation (1.4) proves the fixed-target term.  On a two-element orbit, (1.3)
fixes the nonnegative integer total `t`.  If `t=0`, both entries vanish.  If
`t=1`, exactly one entry vanishes.  If `t>=2`, both entries can in principle
be positive.  This proves (2.2).

To see exactness in the occurrence-level relaxation, suppose initially the
orbit loads are `(0,t)` with `t>=2`.  Select any nonempty proper subset of
the `t` occurrence rows of the covered member.  Equation (1.2) changes the
loads to `(s,t-s)` with `1<=s<=t-1`, removing the hole.  Orbits already
having both entries positive need not be changed.  The cases `t=0,1` are
unavoidable.

The only initially holed two-orbits on which the floor is strictly below
the current hole count are precisely the orbits with load pattern
`(0,t)`, `t>=2`.  Counting the holed member of each such orbit gives
(2.3). \(\square\)

The packet constraint can only make the attainable improvement smaller;
it cannot invalidate the upper bound (2.3).

## 3. Duplicate supply at the first shadow

Put

\[
 N=N_1=\binom n{m-1},\qquad h=H_1(F),\qquad
 d=\#\{R:\mu_1(R)\ge2\}.
\tag{3.1}
\]

The total excess above one on the nonholes is

\[
 \sum_R(\mu_1(R)-1)_+
 =W-(N-h)=W-N+h.
\tag{3.2}
\]

In the Johnson normal form, the selected wreath `2`-factor meets each
`(m-1)`-clique in a matching.  Hence

\[
 \mu_1(R)\le M_m:=\left\lfloor{m+2\over2}\right\rfloor.
\tag{3.3}
\]

Every duplicate target contributes at most `M_m-1` to (3.2), and therefore

\[
 \boxed{
 d\ge {W-N+h\over M_m-1}.}
\tag{3.4}
\]

For `h=epsilon W` with fixed positive `epsilon`, this is

\[
                         d\ge(2\epsilon+o(1)){W\over m}.
\tag{3.5}
\]

This lower bound is sharp at the level of the cap-and-mass ledger: excess
can be concentrated on targets of maximum allowed load.

## 4. Parallel-pair class averaging

Let `I_m` be the conjugacy class of coordinate involutions of cycle type
`1 2^m`.  On every Johnson harmonic of positive degree its class-average
eigenvalue lies in `[0,1/n]`.  Let `Z` be the hole family, `|Z|=h`, and let
`D` be the duplicate family, `|D|=d`.  They are disjoint.  For uniform
`sigma in I_m`,

\[
 \mathbb E_\sigma A^{(2)}_{\sigma,1}(F)
 =\langle\mathbf1_Z,K_{\rm pp}\mathbf1_D\rangle.
\tag{4.1}
\]

Centering both indicators and using the operator norm `1/n` on the
nonconstant space gives

\[
 \boxed{
 \left|
 \mathbb E_\sigma A^{(2)}_{\sigma,1}(F)-{hd\over N}
 \right|
 \le {1\over n}
 \sqrt{h\left(1-{h\over N}\right)
       d\left(1-{d\over N}\right)}.}
\tag{4.2}
\]

In particular some parallel-pair involution satisfies the corresponding
lower bound.  When `h=epsilon W` and `d` has only the forced scale (3.5),
the main term is

\[
 {hd\over N}=\left(2\epsilon^2+o(1)\right){W\over m},
\tag{4.3}
\]

while the error in (4.2) is `O(W/m^(3/2))`.  Thus

\[
 \boxed{
 \exists\sigma\in I_m:\quad
 A^{(2)}_{\sigma,1}(F)
 \ge\left(2\epsilon^2+o(1)\right){W\over m}.}
\tag{4.4}
\]

This is enough in scale for an `Omega(m)`-round descent if one can also
split the duplicate owners legally and avoid cumulative middle cost.  It
is not a one-shot linear repair theorem.

## 5. Consequence for the current bridge programme

The parallel-pair class supplies almost complete hole-to-covered mixing,
but Theorem 2.1 shows that this is the wrong opportunity statistic.  The
productive statistic is hole-to-**duplicate** mixing, followed by an
owner-shore split of the duplicate occurrences.  The three remaining
requirements are therefore:

1. choose an involution with `A^(2)` of the scale (4.4) or better;
2. find legal owner components/cuts that split a positive fraction of
   those duplicate supports;
3. realize `Omega(m)` adaptive rounds with exactness or with cancelling
   total middle boundary.

This is the selective-switch version of the duplicate-supply gate.  It is
strictly cleaner than the fair-coin ledger, but it is not absent.

## 6. Exact involutive cut objective

The two shore orientations are actually equivalent for an involution.  If

\[
 F_A=(F\setminus A)\sqcup\sigma A,
\]

then

\[
 \boxed{F_{A^c}=\sigma F_A.}
\tag{6.1}
\]

Thus they have identical rankwise hole counts and identical designated
gains.

Fix a depth \(q\).  On every nonfixed target orbit \(\{S,T=\sigma S\}\),
put

\[
 u=\mu_q(S),\quad v=\mu_q(T),\quad
 a=a_A(S),\quad b=a_A(T).
\]

The loads in \(F_A\) are

\[
 \boxed{(u-a+b,\ v-b+a),}
\tag{6.2}
\]

while the loads in \(F_{A^c}\) are the same two numbers in the opposite
order.

Let \(P_q(A)\) be the number of exclusive orbits with initial pattern
\((0,t)\), \(t\ge2\), for which the occurrence-owner support of the
covered member meets both \(A\) and \(A^c\).  Let \(L_q(A)\) be the number
of initially covered-covered two-orbits whose two loads in (6.2) are
concentrated on one member, so that one of them is zero.

### Theorem 6.1 (exact split-minus-collapse ledger)

\[
 \boxed{H_q(F_A)-H_q(F)=L_q(A)-P_q(A).}
\tag{6.3}
\]

Consequently, for arbitrary nonnegative shadow weights \(w_q\), the exact
designated near-trade gain is

\[
 \boxed{
 \operatorname {Gain}_{w,H}(A,\sigma)
 =2\sum_{q\le H}w_q\bigl(P_q(A)-L_q(A)\bigr)
  -\partial_\sigma(A).}
\tag{6.4}
\]

### Proof

Fixed targets keep their loads.  A two-orbit of total load zero retains two
holes.  An exclusive orbit of total load one retains exactly one hole.  For
an exclusive orbit of total load at least two, (6.2) has both coordinates
positive exactly when the old occurrence owners are split by the cut; this
removes one hole and gives the contribution counted by \(P_q(A)\).

An initially covered-covered orbit starts with zero holes.  Since its total
load is at least two, it gains one hole exactly when (6.2) is concentrated
on one member; these are precisely the orbits counted by \(L_q(A)\).  No
other orbit changes its hole count, proving (6.3).  The literal ledger
charges two entries per net shadow hole and one middle boundary term,
giving (6.4). \(\square\)

Thus for parallel-pair bridges the remaining positive theorem is exactly a
low-owner-boundary hypergraph cut which splits many exclusive duplicate
supports while collapsing few common supports.  Endpoint-extension
alignment does not create an additional escape from this objective.
