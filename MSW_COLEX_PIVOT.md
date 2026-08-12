# The colex-leading pivot of every full `(2 3)` MSW component

## 1. Statement

Put

\[
 n=2m+1,\qquad \tau=(2\ 3),\qquad m\geq3.
\]

For `0<=j<=m-2`, put

\[
 d=2j+4,
 \qquad
 \mathcal A_j=
 \{1u0:u\in\mathcal D_{j+1}\}
 \mathbin{\dot\cup}
 \{10\,1v0:v\in\mathcal D_j\}.
\]

Fix `R in D_(m-j-2)`.  The proved full-component classification is

\[
                  K_{j,R}=\{AR:A\in\mathcal A_j\}.       \tag{1.1}
\]

Let

\[
 C_{j,R}=\sum_{A\in\mathcal A_j}B_{m-1}e_{q(AR)},
 \qquad
 \Delta_{j,R}=(\tau-1)C_{j,R}.                         \tag{1.2}
\]

We order equal-size subsets by colex, equivalently by their ordinary
binary-mask values: `S<T` when the largest member of `S triangle T`
belongs to `T`.

### Theorem 1 (full-component colex pivot)

The colex-smallest target having nonzero coefficient in
`Delta_(j,R)` is the following set, and its coefficient is `+1`:

\[
 P_{j,R}=
 \begin{cases}
 \{2\}\cup(4+\operatorname {Down}(R)),&j=0,\\[2mm]
 \{2\}\cup[4,j+3]\cup
       (2j+4+\operatorname {Up}(R)),&1\le j\le m-3,\\[2mm]
 \{2,5,7,\ldots,2m-1\},&j=m-2.
 \end{cases}                                           \tag{1.3}
\]

The pivots in (1.3) are pairwise distinct.  The `j=0` pivots contain
`2m`; the interior pivots do not, and their value of `j` is recovered from
the initial consecutive run `4,...,j+3`; the top pivot omits `4`.
For fixed `j`, the remaining shifted up- or down-set recovers `R`.
Consequently the vectors `Delta_(j,R)` are linearly independent over
every field: order their columns by their pivots (1.3) and eliminate by
increasing colex order.

The restriction `m>=3` is necessary.  For `m=2`, the relevant rank is
one, and every cyclic order contains every singleton once, so every
component effect is zero.

The component identification (1.1) is proved in
`MSW_COMPONENT_HIERARCHY_REDUCTION.md`.  Consequently the theorem below is
unconditional and uses no computation.

## 2. Turning alternating cyclic intervals into ordinary intervals

For a Dyck word `W` of semilength `s`, write

\[
 \rho(W)=(a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1}),
 \quad
 \mathsf A(W)=(a_i),\quad \mathsf B(W)=(b_i).          \tag{2.1}
\]

As unordered sets, `mathsf A(W)=Down(W)` and
`mathsf B(W)=Up(W)`.

The MSW concatenation law gives

\[
 q(AR)=(\rho(A),\ d+\rho(R),\ n).                     \tag{2.2}
\]

Starting at the final position of `q(AR)` and reading positions with
step two gives

\[
 n,\ q_1,q_3,\ldots,q_{2m-1},q_0,q_2,\ldots,q_{2m-2}.
\]

Therefore every rank-`(m-1)` alternating window which avoids `n` is an
ordinary interval of length `m-1` in

\[
 L(A,R)=
 \mathsf B(A)\ \Vert\ (d+\mathsf B(R))\ \Vert\
 \mathsf A(A)\ \Vert\ (d+\mathsf A(R)).               \tag{2.3}
\]

Every set preceding (1.3) in colex avoids `n`, since (1.3) avoids `n`
and `n` is the largest coordinate.  Hence it suffices to analyze the
ordinary intervals in (2.3).

We use the abbreviations

\[
 X_A=\mathsf B(A),\quad Y_A=\mathsf A(A),\quad
 U=d+\mathsf B(R),\quad D=d+\mathsf A(R).             \tag{2.4}
\]

## 3. Two cancellation lemmas

### Lemma 2 (the full up/down multisets are `tau`-invariant)

For every `j`, both multisets

\[
 \{\operatorname {Up}(A):A\in\mathcal A_j\},\qquad
 \{\operatorname {Down}(A):A\in\mathcal A_j\}        \tag{3.1}
\]

are invariant under `tau`.

#### Proof

In the first part of `mathcal A_j`, write `A=1u0`.  If `u` begins with
`10`, write `u=10v`, where `v in D_j`.  Then

\[
 \operatorname {Up}(110v0)
   =\tau\operatorname {Up}(101v0).                    \tag{3.2}
\]

These pair exactly with the second part of `mathcal A_j`.  Every remaining
`u` begins with `11`, so `Up(1u0)` contains both `2` and `3` and is fixed
by `tau`.  This proves the first assertion.  Taking complements proves the
second.  QED.

The next lemma is the only nontrivial cancellation.

For a nonempty Dyck word `u`, let `t(u)` be the length of the prefix before
its last primitive component.  The MSW recursion gives, for `A=1u0`,

\[
 \mathsf B(A)\setminus\{\hbox{its first entry}\}
 =\{1\}\cup(1+\operatorname {Up}(u))\setminus\{t(u)+2\}.
                                                               \tag{3.3}
\]

Indeed, the first entry of `mathsf B(1u0)` is
`d-a_0(rev u)`.  Here `a_0(rev u)` is the length of the first primitive
component of `rev u`, hence the length of the last primitive component of
`u`; this is (3.3).

### Lemma 3 (first-deletion cancellation)

For fixed semilength `s>=2`, the multiset

\[
 \left\{
 \mathsf B(1u0)\setminus\{\hbox{its first entry}\}:
 u\in\mathcal D_s
 \right\}                                               \tag{3.4}
\]

is `tau`-invariant.

#### Proof

By (3.3), the set in (3.4) contains `2` unless `u` is primitive, and it
contains `3` unless `u` begins with `10`.  Thus all terms except the
primitive words and the words beginning with `10` contain both `2,3` and
are fixed by `tau`.

We give a bijection between the two exceptional families.  Write a
primitive word as

\[
                         u=1w0,qquad w\in\mathcal D_{s-1}.
\]

Delete the first symbol of `w` and append a down-step.  The resulting word
`b` has final height `-2`, has height at least `-1` before its final
position, and has a well-defined first position `c` at which its height is
`-1`.  Flip the down-step at `c` to an up-step.  The resulting word `v` is
Dyck, and `c` is the first position of its last primitive component.

This map `w -> v` is a bijection of `D_(s-1)`.  Its inverse flips the
first up-step of the last primitive component of `v` to a down-step,
deletes the final down-step, and prepends an up-step.  Moreover,

\[
 \operatorname {Up}(v)\setminus\{c\}
   =\{p-1:p\in\operatorname {Up}(w),\ p>1\}.          \tag{3.5}
\]

Formula (3.3) now gives

\[
 \begin{aligned}
 P(1w0)
   &=\{1\}\cup(2+\operatorname {Up}(w)),\\
 P(10v)
   &=\{1,2\}\cup
       \bigl(3+(\operatorname {Up}(v)\setminus\{c\})\bigr)
     =\tau P(1w0),                                    \tag{3.6}
 \end{aligned}
\]

where `P(u)` denotes the set in (3.4).  Hence all exceptional terms pair
under `tau`.  QED.

## 4. The interior components `1<=j<=m-3`

Put

\[
 a=j+2,\qquad r=m-j-2,
\]

so `a,r>=1`, the four block lengths in (2.3) are `a,r,a,r`, and the
window length is

\[
                         m-1=a+r-1.                   \tag{4.1}
\]

The `m+2` windows avoiding `n` are exactly

\[
\begin{array}{ll}
W_0(A)=X_A\cup\operatorname {pre}_{r-1}U,&\\[1mm]
W_s(A)=\operatorname {suf}_{a-s}X_A\cup U\cup
       \operatorname {pre}_{s-1}Y_A,&1\le s\le a,\\[1mm]
W_{a+u}(A)=\operatorname {suf}_{r-u}U\cup Y_A\cup
       \operatorname {pre}_{u-1}D,&1\le u\le r,\\[1mm]
W_{m+1}(A)=\operatorname {suf}_{a-1}Y_A\cup D.&
\end{array}                                             \tag{4.2}
\]

We inspect them in this order.

* The sum of the `W_0(A)` is `tau`-invariant by Lemma 2.
* In `W_1(A)`, the first-type terms `A=1u0` are `tau`-invariant by
  Lemma 3.  For a second-type term `A=10 1v0`, direct use of the MSW
  recursion gives

  \[
       W_1(A)=\{3\}\cup(3+\operatorname {Up}(v))\cup U. \tag{4.3}
  \]

  Hence its positive transposed term is

  \[
       \{2\}\cup(3+\operatorname {Up}(v))\cup U.       \tag{4.4}
  \]

* For `s>=2`, a first-type `W_s(A)` contains `d`, whereas (1.3) does
  not and has the same tail `U`; it is therefore later in colex.  A
  second-type `W_2(A)` contains both `2,3` and is fixed by `tau`.
  Every second-type `W_s(A)` with `s>=3` contains `d` and is later in
  colex.
* For every `u`, the sum of the `W_(a+u)(A)` is `tau`-invariant by the
  down-set half of Lemma 2.
* Finally `W_(m+1)(A)` contains all of `D`, in particular `2m`, because
  the final step of `R` is down.  The proposed pivot contains `U` and
  not `2m`, so every such window is later in colex.

It remains only to minimize (4.4).  The colex-smallest `j`-subset of
`[2j]` is `[j]`, and it is the up-set of the unique mountain Dyck word

\[
                         v=1^j0^j.
\]

Thus the unique smallest positive term in (4.4) is

\[
 \{2\}\cup[4,j+3]\cup(d+\operatorname {Up}(R)),       \tag{4.5}
\]

with coefficient `+1`.  Its untransposed partner contains `3` instead of
`2` and is later in colex.  This proves Theorem 1 in the interior range.

## 5. The bottom component `j=0`

Here `K_(0,R)` is the proved two-wreath component indexed by
`1100R,1010R`.  Its exact rank-`(m-1)` effect is

\[
 \begin{aligned}
 \Delta_{0,R}={}&
 e_{K\cup\{2,2m\}}-e_{K\cup\{3,2m\}}\\
 &-e_{K\cup\{2,n\}}+e_{K\cup\{3,n\}},               \tag{5.1}
 \end{aligned}
\]

where

\[
 K=4+(\operatorname {Down}(R)\setminus\{2m-4\}).      \tag{5.2}
\]

Since the final position of `R` is down,

\[
 K\cup\{2,2m\}=\{2\}\cup(4+\operatorname {Down}(R)). \tag{5.3}
\]

This term has coefficient `+1`.  Replacing `2` by `3` makes a set later
in colex, and either of the other terms contains the still larger
coordinate `n`.  Hence (5.3) is the unique leading term.

## 6. The top component `j=m-2`

Now `R` is empty, `a=m`, and

\[
                         L(A)=X_A\Vert Y_A.            \tag{6.1}
\]

Every window preceding the proposed pivot again avoids `n`.  Apart from
the first and last windows of the two blocks, every first-type window with
at least one entry of `Y_A` contains `2m`; every second-type such window
except the first one contains `2m`; and that exceptional first window
contains both `2,3`.  Thus all of them are either later than the proposed
pivot or individually `tau`-fixed.

The remaining boundary windows cancel as follows.

* For `A=1u0`, the first length-`(m-1)` window is

  \[
                    \operatorname {Up}(A)\setminus\{1\}
                    =1+\operatorname {Up}(u).          \tag{6.2}
  \]

  If `u` begins with `11`, it contains both `2,3`.  If `u=10v`, it is

  \[
                    \{2\}\cup(3+\operatorname {Up}(v)), \tag{6.3}
  \]

  which pairs under `tau` with the first-deleted window

  \[
                    \{3\}\cup(3+\operatorname {Up}(v)) \tag{6.4}
  \]

  of the second-type word `A=10 1v0`.
* The other first-block boundary windows from `A=1u0` cancel by Lemma 3.
  The first window from a second-type word after deleting its final `3`
  contains neither `2` nor `3`, so it is fixed.

Only the final window of a first-type word remains.  It is

\[
              \operatorname {Down}(A)\setminus\{2m\}
                    =1+\operatorname {Down}(u).        \tag{6.5}
\]

If `u` begins with `11`, (6.5) contains neither `2` nor `3` and is fixed.
If `u=10w`, its positive transposed term is

\[
                   \{2\}\cup(3+\operatorname {Down}(w)),
             \qquad w\in\mathcal D_{m-2}.             \tag{6.6}
\]

If the down positions of `w` are
`c_1<...<c_(m-2)`, the Dyck condition gives

\[
                            c_i\ge2i.                  \tag{6.7}
\]

Therefore their unique colex-minimum is

\[
              \{2,4,\ldots,2m-4\},                   \tag{6.8}
\]

attained by `w=(10)^(m-2)`.  Substitution in (6.6) gives the unique
leading target

\[
                         \{2,5,7,\ldots,2m-1\},        \tag{6.9}
\]

again with coefficient `+1`.  This completes the proof.
