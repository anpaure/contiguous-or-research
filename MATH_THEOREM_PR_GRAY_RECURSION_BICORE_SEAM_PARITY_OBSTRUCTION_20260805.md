# The Proskurowski--Ruskey recursion has a sharp bi-core seam-parity obstruction

**Date:** 2026-08-05  
**Method:** pure mathematics; no enumeration, finite search, or solver  
**Status:** exact audit of the published recursive Gray order.  The result
rules out merely alternating the signs on that fixed order in almost every
semilength at Gaussian collar depth.  It does not rule out a modified
Proskurowski--Ruskey recursion or another transposition Gray path.

## 0. Outcome

Let `T(n,k)` be the Proskurowski--Ruskey list of the Dyck words of
semilength `n` whose initial ascent has length exactly `k`.  Their standard
Hamilton path is

\[
 {cal P}_n=T(n,n)\circ T(n,n-1)\circ\cdots\circ T(n,2)
                   \circ T(n,1)^R.                 \tag{0.1}
\]

Inside `T(n,k)`, `1<k<n`, there is one top recursive seam between

\[
 \operatorname {flip}(T(n,k+1)^R)
 \quad\hbox {and}\quad
 \operatorname {insert}(T(n-1,k-1)).               \tag{0.2}
\]

For `3<=k<=n-2`, put

\[
 f(2a)=a,\qquad f(2a+1)=a+3.                       \tag{0.3}
\]

The exact MSW bi-core audit of this seam is

\[
 \boxed{
 \begin{aligned}
   \hbox{the seam is plus-safe}&\iff f(k)>h,\\
   \hbox{the seam is minus-safe}&\iff n-k-1>h.
 \end{aligned}}                                    \tag{0.4}
\]

The exceptional `k=2` seam is always plus-unsafe for `h>=1` and is
minus-safe as soon as `n>=h+2`.

Thus, when `n>=3h+2`, the `h` top seams

\[
       k=n-2,n-3,\ldots,n-h-1                       \tag{0.5}
\]

are forced plus, while the `k=2` seam is forced minus.

The target position of the `k`-seam in (0.1) has parity

\[
  1+S(n,k+2)\pmod2,                                 \tag{0.6}
\]

where `S(n,m)` is the number of Dyck words whose initial ascent has
length at least `m`.  If

\[
                 t=n-m,qquad N=n+1,
\]

then

\[
 \boxed{S(n,m)\equiv {n+t+1\choose t}\pmod2,
        \qquad
        S(n,m)\text{ is odd}\iff t\mathbin{\&}N=0.} \tag{0.7}
\]

Here `&` denotes bitwise intersection.  Consequently, if

\[
                  L=2^{\nu _2(n+1)},                \tag{0.8}
\]

then the fixed PR path can admit an alternating bi-core signing only if

\[
                  \boxed{L\ge h.}                   \tag{0.9}
\]

Moreover, if `n+1` is a power of two, then the forced-plus `k=n-2`
seam and the forced-minus `k=2` seam occur at target positions of the
same parity.  Hence no alternating signing exists in that case either.

The necessary condition left by this top-level audit is therefore

\[
 \boxed{
  2^{\nu _2(n+1)}\ge h
  \quad\hbox {and}\quad n+1\text{ is not a power of two}.}             \tag{0.10}
\]

This is a density-zero exceptional set at the Gaussian deadline
`h=Theta(sqrt(n))`: in a dyadic interval there are only `O(n/h)` possible
semilengths satisfying the first condition.

The obstruction is top-level, so first-return shielding inside recursive
calls cannot repair it.  It shows that the classical transposition Gray
code cannot simply be imported and alternately signed.  A successful PR
route must alter the recursive branch order or splice its branches before
the MSW signs are imposed.

## 1. The exact PR recursion and its seam

For a Dyck word `y=1^k0x`, define

\[
 \operatorname {flip}(y)=1^{k-1}01x,
 \qquad
 \operatorname {insert}(y)=1^{k+1}00x.              \tag{1.1}
\]

The Proskurowski--Ruskey recursion is

\[
T(n,k)=
\begin{cases}
 \operatorname {flip}(T(n,2)),&k=1<n,\\
 \operatorname {flip}(T(n,k+1)^R)\circ
       \operatorname {insert}(T(n-1,k-1)),&1<k<n,\\
 1^n0^n,&k=n.
\end{cases}                                         \tag{1.2}
\]

The endpoint formulae are

\[
\begin{aligned}
 \operatorname {first}T(n,k)
   &=1^k010^k(10)^{n-k-1},&&1<k<n,\\
 \operatorname {last}T(n,k)
   &=1^k0^k(10)^{n-k}.                               \tag{1.3}
\end{aligned}
\]

For `3<=k<=n-2`, the two words on the top seam of (1.2) are therefore

\[
\begin{aligned}
 A_{n,k}
   &=1^k0110^{k+1}(10)^{n-k-2},\\
 B_{n,k}
   &=1^k0010^{k-1}(10)^{n-k-1}.                     \tag{1.4}
\end{aligned}
\]

They differ by exchanging

\[
                    q=k+2,qquad p=2k+3,             \tag{1.5}
\]

where `q` is an upstep of `A_(n,k)` and `p` is an upstep of
`B_(n,k)`.

Put

\[
\begin{aligned}
 A_k&=1^k0110^{k+1},\\
 B_k&=1^k0010^{k-1}.                                 \tag{1.6}
\end{aligned}
\]

Then

\[
 A_{n,k}=A_k(10)^{n-k-2},
 \qquad
 B_{n,k}=B_k(10)^{n-k-1}.                            \tag{1.7}
\]

All four ranks involved in the seam can consequently be computed in the
short prefixes `A_k,B_k` by the MSW concatenation law.

## 2. The exact MSW rank table

For a Dyck word `x`, let `D(x)` and `I(x)` be its MSW deletion and
insertion orders.  For a primitive word `w=1u0` of semilength `a`, the
first-return recursion gives

\[
 D(w)=(2a-I(\mu u),1),
 \qquad
 I(w)=(2a,2a-D(\mu u)),                              \tag{2.1}
\]

where `mu` is reverse-complement.

### Lemma 2.1 (the short-prefix rank)

Define

\[
                     f(k)=d_{A_k}(k+2).              \tag{2.2}
\]

Then, for `k>=2`,

\[
 f(k)=i_{B_k}(k+2),                                  \tag{2.3}
\]

and, for `k>=3`,

\[
                     f(k)=1+f(k-2).                  \tag{2.4}
\]

The initial values are

\[
                     f(1)=3,qquad f(2)=1.           \tag{2.5}
\]

Consequently (0.3) holds.

#### Proof

For `k>=2`, the word `A_k` is primitive and the reverse-complement of its
interior is `B_k`.  Formula (2.1) therefore identifies the deletion rank of coordinate
`k+2` in `A_k` with the insertion rank of the same coordinate in `B_k`,
which proves (2.3).

For `k>=3`, `B_k` is primitive and the reverse-complement of its interior
is `A_(k-2)`.  In its insertion order the leading coordinate `2k+2`
comes first, after which (2.1) identifies coordinate `k+2` with coordinate
`k` in `D(A_(k-2))`.  Hence

\[
 i_{B_k}(k+2)=1+d_{A_{k-2}}(k)=1+f(k-2),
\]

which is (2.4).

For `k=1`, `A_1=101100=(10)(1100)`, and concatenating the two deletion
orders gives

\[
                         D(A_1)=(1,4,3),
\]

so `f(1)=3`.  For `k=2`, one has

\[
 B_2=(1100)(10),qquad I(B_2)=(4,3,6),
\]

and hence `f(2)=i_(B_2)(4)=1`.  Solving (2.4) separately on the two
parities gives (0.3). `square`

### Theorem 2.2 (generic seam rank table)

For the seam (1.4)--(1.5), `3<=k<=n-2`, the four intrinsic ranks are

\[
\boxed{
\begin{array}{c|cc}
 &A_{n,k}&B_{n,k}\\ \hline
 \text{deletion rank}&d(q)=f(k)&d(p)=k+2\\
 \text{insertion rank}&i(p)=k+2&i(q)=f(k).
\end{array}}                                         \tag{2.6}
\]

Therefore the exact safety statement is (0.4).

#### Proof

The first entry is Lemma 2.1.  In `B_(n,k)`, coordinate `p=2k+3` is the
upstep of the first `10` factor after `B_k`.  Since `B_k` has semilength
`k+1`, the concatenation law puts it at deletion rank `k+2`.

For the third entry, (2.1) for `A_k` maps coordinate `p=2k+3` to
coordinate `1` in `D(B_k)`.  The latter is the final deletion of the
primitive word `B_k`, at rank `k+1`; the leading entry of `I(A_k)` adds
one.  Thus `i_(A_(n,k))(p)=k+2`.  The fourth entry is (2.3).

Forward clipped residence requires both deletion ranks to exceed `h`.
Since `f(k)<=k+2`, this is equivalent to `f(k)>h`.  Reverse clipped
residence requires both insertion ranks to be at most `n-h`.  Since
`f(k)<=k+2`, this is equivalent to

\[
                         k+2\le n-h,
\]

or `n-k-1>h`. `square`

### Lemma 2.3 (the exceptional `k=2` seam)

For `n>=4`, the `k=2` seam is

\[
\begin{aligned}
 A_{n,2}&=11011000(10)^{n-4},\\
 B_{n,2}&=11001100(10)^{n-4},                        \tag{2.7}
\end{aligned}
\]

and exchanges `q=4` with `p=6`.  Its ranks are

\[
\boxed{
\begin{array}{c|cc}
 &A_{n,2}&B_{n,2}\\ \hline
 \text{deletion rank}&d(4)=1&d(6)=3\\
 \text{insertion rank}&i(6)=2&i(4)=1.
\end{array}}                                         \tag{2.8}
\]

It is therefore plus-unsafe for every `h>=1`, and minus-safe whenever
`n>=h+2`.

#### Proof

The relevant prefix orders are

\[
\begin{aligned}
 D(11011000)&=(4,5,2,1),&
 I(11011000)&=(8,6,7,3),\\
 D(11001100)&=(2,1,6,5),&
 I(11001100)&=(4,3,8,7).                             \tag{2.9}
\end{aligned}
\]

The first row follows from (2.1) and
`110010=(1100)(10)`; the second follows by concatenating the orders of
two copies of `1100`.  Reading coordinates `4,6` gives (2.8), and the
safety conclusion follows from the intrinsic rank criterion. `square`

### Corollary 2.4 (the forced seam bands)

Assume `h>=1` and `n>=3h+2`.  Then every seam in (0.5) is plus-safe and
minus-unsafe.  The `k=2` seam is minus-safe and plus-unsafe.

#### Proof

For `k>=n-h-1`,

\[
                         k>2h,
\]

so (0.3) gives `f(k)>h`; while `n-k-1<=h`.  Apply Theorem 2.2.
Lemma 2.3 gives the last statement. `square`

## 3. Exact parity of every top recursive seam

Let

\[
                 a(n,k)=|T(n,k)|.                   \tag{3.1}
\]

Thus `a(n,k)` counts Dyck words whose initial ascent has length exactly
`k`.  Put

\[
                 S(n,m)=\sum_{j=m}^n a(n,j).         \tag{3.2}
\]

This counts Dyck words whose first `m` symbols are all upsteps.

### Lemma 3.1 (global target position)

In the Hamilton path (0.1), the target vertex immediately after the top
recursive seam of `T(n,k)` has index

\[
  J(n,k)=1+\sum_{j=k+1}^n a(n,j)+a(n,k+1).           \tag{3.3}
\]

Consequently

\[
                 J(n,k)\equiv1+S(n,k+2)\pmod2.      \tag{3.4}
\]

#### Proof

All blocks `T(n,j)` with `j>k` precede `T(n,k)` in (0.1).  The first
recursive branch of `T(n,k)` has `a(n,k+1)` vertices, and the target is
the next vertex.  This gives (3.3).  Modulo two, the two copies of
`a(n,k+1)` cancel, proving (3.4). `square`

### Lemma 3.2 (ballot and Lucas formula)

Let `m<=n` and put `t=n-m`.  Then

\[
 S(n,m)
  ={2n-m\choose n-m}-{2n-m\choose n-m-1}.           \tag{3.5}
\]

Modulo two,

\[
 S(n,m)\equiv{n+t+1\choose t}.                       \tag{3.6}
\]

In particular,

\[
 S(n,m)\text{ is odd}
       \iff t\mathbin{\&}(n+1)=0.                   \tag{3.7}
\]

#### Proof

After the first `m` upsteps, the path starts at height `m`, has `n-m`
upsteps and `n` downsteps left, and must stay nonnegative.  The reflection
principle gives (3.5).

Since subtraction and addition agree modulo two, Pascal's identity gives

\[
\begin{aligned}
S(n,m)
 &\equiv {n+t\choose t}+{n+t\choose t-1}\\
 &={n+t+1\choose t}\pmod2.
\end{aligned}
\]

Lucas's theorem says that a binary binomial coefficient `{A choose B}` is
odd exactly when adding `B` and `A-B` produces no binary carry.  Here
`A-B=n+1`, so this is exactly (3.7). `square`

## 4. The recursion obstruction

Assign alternating signs to the vertices of (0.1).  The sign at a target
position depends only on the parity of that position and on the one global
choice of initial sign.

### Theorem 4.1 (low-bit obstruction)

Assume `h>=2` and `n>=3h+2`.  If

\[
                       2^{\nu _2(n+1)}<h,             \tag{4.1}
\]

then no alternating signing of the fixed PR Hamilton path is bi-core safe.

#### Proof

Let `L=2^(nu_2(n+1))`.  In the forced-plus band (0.5), take first
`k_0=n-2`, corresponding in Lemma 3.2 to `t=0`, and then

\[
                       k_1=n-L-2,                    \tag{4.2}
\]

corresponding to `t=L`.  Since `L<h`, both belong to (0.5).

For `t=0`, (3.7) says that `S` is odd, so (3.4) makes the target position
even.  For `t=L`, the lowest set bit of `n+1` lies in both operands of the
bitwise intersection.  Thus (3.7) says that `S` is even, and (3.4) makes
the target position odd.

Both seams are forced plus by Corollary 2.4, but their target positions
have opposite parity.  No alternating signing can label both targets plus.
`square`

### Theorem 4.2 (power-of-two obstruction)

Assume `h>=1`, `n>=3h+2`, and `n+1` is a power of two.  Then no
alternating signing of the fixed PR Hamilton path is bi-core safe.

#### Proof

The forced-plus seam `k=n-2` has `t=0`, hence an even target position as
above.

For the forced-minus `k=2` seam, `m=4` and

\[
                         t=n-4=(n+1)-5.              \tag{4.3}
\]

Because `n+1` consists of one binary set bit and `0<=t<n+1`, one has

\[
                         t\mathbin{\&}(n+1)=0.
\]

Lemma 3.2 makes `S(n,4)` odd, so Lemma 3.1 places this target at an even
position as well.  The two targets have the same alternating sign, while
their seams require opposite signs. `square`

### Corollary 4.3 (density-zero surviving dimensions)

For `n>=3h+2`, a necessary condition for the published PR path to admit
an alternating bi-core signing is (0.10).

For fixed `h`, in any interval of `X` consecutive integers, the first
condition in (0.10) holds for at most

\[
                         {X\over h}+1                \tag{4.4}
\]

values.  In particular, if `h(n)=Theta(sqrt(n))`, then every dyadic
interval `[X,2X]` contains only `O(sqrt(X))` exceptional dimensions, and
the exceptional dimensions have asymptotic density zero.

#### Proof

Theorems 4.1 and 4.2 give (0.10).  If
`2^(nu_2(n+1))>=h`, then `n+1` is divisible by
`2^ceil(log_2 h)`.  Multiples of this integer have spacing at least `h`,
which proves (4.4). `square`

Reversing the entire Hamilton path does not help: it applies the same
parity translation to every seam target.  Hence opposite-parity seams
forced to the same sign remain inconsistent, and same-parity seams forced
to opposite signs remain inconsistent.

## 5. Exact scope and the corrected next target

This theorem does **not** say that the signed bi-core-safe Dyck Gray-code
lemma is false.  It proves the following narrower and useful statement:

> The standard Proskurowski--Ruskey branch order cannot simply be supplied
> with alternating MSW signs.  Its top recursive seams already contradict
> one another in all but a density-zero set of semilengths at the Gaussian
> deadline.

The obstruction is not a lack of locally safe transpositions.  The generic
seam theorem (0.4), together with Lemma 2.3, shows that, for `n>3h+1`,
every audited seam `k=2,...,n-2` is safe in at least one sign.  The failure
is a **global phase conflict**: forced seams land in the wrong parities of
the fixed recursive order.

Nor can first-return shielding repair the displayed conflict.  The seams
used in Theorems 4.1 and 4.2 occur in the top-level lists themselves, with
no external Dyck guard.

The corrected PR-based target is therefore one of the following.

1. Reorder or reverse selected recursive branches so that the forced-plus
   and forced-minus seams land on their required target parities, while
   retaining transposition adjacency at every new branch join.
2. Delete the parity-incompatible top seams and prove that the resulting
   recursively shielded pieces can be fused by a separate bi-core-safe
   bank whose size is exponentially smaller than `Cat_n`.
3. Use the Pruesse--Ruskey ideal-prism construction only after proving that
   every selected two-cover step projects to one literal Dyck
   transposition and passes the two-ended rank test.  The abstract prism
   theorem alone does not prove either condition.

The bitwise formula (3.7) supplies the exact phase oracle for the first
option.  Any proposed modification of the PR recursion can now be audited
without generating the Gray list.

## References

F. Ruskey and A. Proskurowski, *Generating binary trees by
transpositions*, Journal of Algorithms **11** (1990), 68--84.

T. R. Walsh, *Generation of well-formed parenthesis strings in constant
worst-case time*, Journal of Algorithms **29** (1998), 165--173.  Section 2
records the exact PR recursion and endpoint words used above.
