# Boolean endpoint rounding: a product-rounding no-go and the exact two-SCD socket ledger

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorems.  The first theorem
shows that independent rounding of the exact endpoint-triangular fractional
flag factor has a linear named-target defect with overwhelmingly high
probability.  The second theorem proves that the canonical two-SCD
collar-and-tail construction has enough sockets both in total capacity and
in raw number at the coefficient-one depth.  It reduces that construction
exactly to one typed containment/capacity Hall matching.  No integral
endpoint factor, owner containment, or countdown serialization is claimed.

## 0. Setup and outcome

Put

\[
 r=\left\lceil {k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad {cal L}=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|{cal L}|,
\]

and let `d=d(k)` be least with

\[
                         dW+{d+1\choose2}\ge\Lambda.       \tag{0.1}
\]

The exact endpoint-triangular fractional theorem supplies `n=W+d`
labelled slots of capacities

\[
             (\underbrace{d,\ldots,d}_{W+1},d-1,\ldots,1) \tag{0.2}
\]

and a probability distribution on a legal Boolean flag in every slot such
that every named target has total marginal one.

This note proves two complementary facts.

1. If the slot flags are sampled independently from the symmetric
   fractional solution, then already the rank-`r-1` row has `Omega(W)`
   uncovered named targets with probability `1-exp(-Omega(W))`.  Repairing
   such an outcome requires changing `Omega(W)` slot flags.  Thus product
   rounding plus a bounded, sublinear, or local alteration cannot prove the
   desired `O(1)` defect.
2. For even `k=2m`, take one SCD for the top `d`-rank collar and an
   independent SCD for the lower residual tail.  Keeping full collars and
   using every short collar as a socket gives exactly the right total
   capacity.  Moreover, the number of short sockets is

   \[
             (1-e^{-\pi/4}+o(1))W>0.544W,             \tag{0.3}
   \]

   while splitting all residual SCD tails into pieces of size at most `d`
   needs only

   \[
       \left(\sum_{q\ge1}e^{-\pi q^2/4}+o(1)\right)W
       <0.501W.                                       \tag{0.4}
   \]

   Hence neither total capacity nor raw socket count obstructs this
   coefficient-one construction.  Its exact missing statement is one
   matching whose edge records both containment and residual capacity.

The two results point in the same direction: coefficient-one rounding must
be globally dependent, but the most natural cross-SCD dependent face has a
strict scalar reserve.

## 1. Independent rounding leaves a linear top-row defect

Write

\[
                         a={k\choose r-1}.             \tag{1.1}
\]

In the symmetric fractional construction, let `p_j` be the probability
that slot `j` uses rank `r-1`.  Conditional on doing so, its rank-`r-1`
member is uniform on the `a` named targets of that rank.  Exact marginals
give

\[
                 0\le p_j\le1,
                 \qquad \sum_{j=1}^{n}p_j=a.          \tag{1.2}
\]

Sample the `n` slot flags independently.  Let `Z` be the number of
rank-`r-1` targets selected by no slot.

### Theorem 1.1 (product-rounding barrier)

For every `k` with `a>=2`,

\[
                         \mathbb E Z\ge {a\over4}.      \tag{1.3}
\]

Furthermore,

\[
 \Pr\left(Z<{a\over8}\right)
      \le \exp\left(-{a^2\over32n}\right).            \tag{1.4}
\]

Since `a=(1-o(1))W` and `n=(1+o(1))W`, the right side of (1.4) is
`exp(-Omega(W))`.  Any alteration which changes fewer than `a/8` slot
flags leaves at least one rank-`r-1` target uncovered on every outcome
counted by the complementary event.

### Proof

Fix a rank-`r-1` target `S`.  Slot `j` selects `S` with probability

\[
                             x_j={p_j\over a}.          \tag{1.5}
\]

Thus `0<=x_j<=1/a` and `sum_j x_j=1`.  Independence gives

\[
                         \Pr(S\text{ is missed})
                         =\prod_j(1-x_j).              \tag{1.6}
\]

Among vectors satisfying the two constraints after (1.5), the product in
(1.6) is minimized by taking exactly `a` coordinates equal to `1/a` and
the others zero.  One elementary proof is to fix the sum of two
nonextreme coordinates: since

\[
                (1-x)(1-y)=1-(x+y)+xy,
\]

pushing one coordinate toward `0` or `1/a` decreases the product.  Repeat
until an extreme point is reached.  Consequently

\[
 \Pr(S\text{ is missed})
     \ge \left(1-{1\over a}\right)^a\ge {1\over4}.    \tag{1.7}
\]

Summing (1.7) over the `a` targets proves (1.3).

The random variable `Z` is a function of the `n` independent slot choices.
Changing one slot flag changes `Z` by at most one: it can remove at most
one old rank-`r-1` occurrence and insert at most one new one, and if both
operations change emptiness their effects have opposite signs.  McDiarmid's
bounded-difference inequality therefore gives

\[
 \Pr(Z\le \mathbb EZ-t)\le\exp\left(-{2t^2\over n}\right). \tag{1.8}
\]

Use `t=a/8` and (1.3).  This proves (1.4).

Finally, one changed slot can newly cover at most one previously uncovered
rank-`r-1` target.  Therefore an outcome with `Z>=a/8` requires at least
`a/8` changed slots before it can become exact.  \(\square\)

### Scope of Theorem 1.1

The theorem applies to the natural product rounding of the exact symmetric
fractional flag factor.  It does not rule out an exceptional exact product
outcome of exponentially small probability, and it does not rule out a
globally dependent rounding.  It proves the sharper algorithmic boundary:

\[
 \boxed{\text{independent flag sampling followed by }o(W)
        \text{ slot alterations cannot be the proof.}}         \tag{1.9}
\]

The conclusion uses only one Boolean rank.  Correlations among the members
of a flag, perfectness of the incomparability graph, and all
Greene--Kleitman inequalities cannot change it.

## 2. The canonical two-SCD collar face

Now specialize to even dimension `k=2m`, so `r=m`, and fix two arbitrary
symmetric chain decompositions

\[
                         {\mathscr S}_{C},\qquad
                         {\mathscr S}_{R}              \tag{2.1}
\]

of `B_(2m)`.  They need not agree.

### Collar bank

From every chain of `mathscr S_C`, retain its members in the strict lower
ideal having ranks at least `m-d`.  A chain which reaches rank `m-d` gives
one full collar of length `d`.  A chain which starts at rank `j>m-d`
gives a short collar of length

\[
                             \ell=m-j<d               \tag{2.2}
\]

and hence a socket of residual capacity `d-ell`.  A middle singleton chain
has no strict-lower target and is an empty socket of capacity `d`.

### Residual bank

Restrict `mathscr S_R` to the nonempty ranks below `m-d`.  Every nonempty
restriction is a residual chain.  Split it consecutively into chunks of
size at most `d`.  These chunks partition every named target not already
in the collar rank band.

Add the `d` boundary sockets of capacities `1,2,...,d` from (0.2).

Make the **typed socket graph** with residual chunks on the left and short
or boundary sockets on the right.  A residual chunk `F` is adjacent to a
nonempty collar socket `D` precisely when

\[
           |F|\le d-|D|,
           \qquad \max F\subseteq\min D.              \tag{2.3}
\]

It is adjacent to an empty or boundary socket precisely when its size does
not exceed that socket's capacity.  The latter convention is static: no
owner is assigned to an empty socket in this note.

### Theorem 2.1 (exact collar-face reduction)

The two-SCD collar face yields an exact endpoint-triangular partition of
`mathcal L` if and only if its typed socket graph has a matching saturating
all residual chunks.  Equivalently,

\[
                    |N(X)|\ge |X|
                    \qquad\text{for every residual chunk family }X.  \tag{2.4}
\]

### Proof

If `F` is matched to a nonempty socket `D`, (2.3) says that every member of
the chain `F` lies below every member of the chain `D`; their concatenation
is therefore one chain of length at most `d`.  A chunk placed in an empty
or boundary socket is already a chain of admissible length.  The full
collars, the filled short sockets, and the boundary chains are target
disjoint and cover the complete strict lower ideal.

Conversely, every construction which keeps the collar bank and attaches
each residual chunk whole to at most one socket defines exactly such a
matching.  Hall's theorem gives (2.4).  \(\square\)

This is an exact theorem for the collar-preserving face, not an assertion
that every endpoint partition has that form.

## 3. The scalar socket ledger is exact

For a chain `C` of `mathscr S_C`, let

\[
                         L(C)=|C\cap{\cal L}|.         \tag{3.1}
\]

Define total socket capacity and total residual mass by

\[
 K=\sum_C(d-L(C))_+,
 \qquad
 E=\sum_C(L(C)-d)_+.                                 \tag{3.2}
\]

The value `E` is exactly the number of targets below the collar band, and
it is independent of the chosen SCD.

### Proposition 3.1 (exact capacity balance)

\[
                         K-E=dW-\Lambda.              \tag{3.3}
\]

After the triangular boundary sockets are included,

\[
                  K+{d+1\choose2}-E
                  =dW+{d+1\choose2}-\Lambda
                  =:\sigma\ge0.                     \tag{3.4}
\]

### Proof

For every integer `x`, `(d-x)_+-(x-d)_+=d-x`.  Sum this identity over the
`W` SCD chains and use

\[
                         \sum_C L(C)=\Lambda.
\]

This proves (3.3); (3.4) is (0.1).  \(\square\)

Thus the exact lower-bound slack is precisely the unused scalar capacity
of the two-SCD socket construction.  No capacity is lost merely by choosing
the collar face.

## 4. There are asymptotically more sockets than chunks

Write `B_j=binom(2m,j)`.  In any SCD the number of chains starting at rank
`j` is `B_j-B_(j-1)`.  Therefore the number `S` of short or empty collar
sockets is exactly

\[
                         S=W-B_{m-d}.                 \tag{4.1}
\]

Let `P` be the number of residual chunks obtained by splitting every
residual SCD chain into consecutive pieces of size `d`, except that the
unique deleted empty set can alter the count by at most one.  Then

\[
             P=\sum_{q\ge1}B_{m-qd-1}+O(1).          \tag{4.2}
\]

Indeed, a lower SCD segment of length `ell` contributes
`ceil((ell-d)_+/d)` chunks, and

\[
             \left\lceil{(\ell-d)_+\over d}\right\rceil
             =\sum_{q\ge1}{\bf1}_{\{\ell>qd\}}.      \tag{4.3}
\]

Summing (4.3) over the SCD length histogram telescopes to (4.2).

### Theorem 4.1 (strict socket-count reserve)

As `m` tends to infinity,

\[
 {S\over W}\longrightarrow1-e^{-\pi/4},             \tag{4.4}
\]

and

\[
 {P\over W}\longrightarrow
             \Theta_*:=\sum_{q\ge1}e^{-\pi q^2/4}.   \tag{4.5}
\]

Moreover,

\[
                         \Theta_*<0.501
                         <0.544<1-e^{-\pi/4}.          \tag{4.6}
\]

Consequently there is an absolute `eta>0` such that

\[
                         S-P\ge\eta W                 \tag{4.7}
\]

for all sufficiently large even `k`.

### Proof

The lower-bound depth satisfies

\[
                         {d^2\over m}\longrightarrow{\pi\over4}. \tag{4.8}
\]

The central-binomial local limit, with its standard Gaussian domination,
gives for fixed `q`

\[
 {B_{m-qd-1}\over W}\longrightarrow e^{-\pi q^2/4}, \tag{4.9}
\]

and permits summation over `q`.  Equations (4.1)--(4.2) now give
(4.4)--(4.5).

For a completely elementary numerical separation, use

\[
 e^{-\pi/4}<0.456,
 \qquad e^{-\pi}<0.044,
\]

and, for `q>=3`, the inequality `q^2>=9+7(q-3)`.  Hence

\[
 \sum_{q\ge3}e^{-\pi q^2/4}
 \le {e^{-9\pi/4}\over1-e^{-7\pi/4}}<0.000856.
\]

Thus `Theta_*<0.500856<0.501`, whereas
`1-e^(-pi/4)>0.544`.  This proves (4.6)--(4.7).  \(\square\)

The `d` boundary sockets were not counted in `S`, so they only strengthen
the raw count.

## 5. Exact surviving Boolean rounding theorem

The two-SCD face has now passed both scalar tests:

\[
 \boxed{
 \begin{array}{c}
 \text{total socket capacity} - \text{residual mass}=\sigma\ge0,\\
 \text{number of sockets} - \text{minimum }d\text{-chunks}=\Omega(W).
 \end{array}}                                          \tag{5.1}
\]

These inequalities do not imply (2.4).  A short socket can have the wrong
capacity, or its Boolean bottom can fail to contain the top of every
available residual chunk.  Therefore the precise remaining theorem on
this face is:

> **Two-SCD typed socket Hall lemma.**  Choose the collar SCD and residual
> SCD so that every family of residual chunks has at least as many
> capacity-compatible containing sockets.

This is a strictly more concrete target than unrestricted bounded coloring.
It has a linear reserve in vertex count and exact total capacity, but it is
still a named Boolean expansion theorem.  Proving it would establish the
integral endpoint-triangular partition on this collar face.

Even that static success would not yet provide:

1. distinct rank-`r` owner containment for the empty and boundary sockets;
2. a simultaneous left-endpoint partition;
3. countdown/suffix-OR serialization; or
4. residence, upper shadows, topology, and common-cap compatibility.

Those gates are deliberately outside this theorem.

