# The canonical two-step GK selector has exact primitive fibers and asymptotically half a head defect

**Date:** 2026-08-14
**Status:** unconditional structural theorem.  The exact fiber ledger was
independently replayed on H100 through `m=10`.  This note proves an exact
obstruction to one canonical selector; it does not obstruct adaptive
three-chart selectors.

## 0. Statement

Put

\[
 n=2m+1,\qquad
 \mathcal U={ [n]\choose m+2},\quad
 \mathcal M={ [n]\choose m+1},\quad
 \mathcal L={ [n]\choose m}.
\tag{0.1}
\]

Use the linear Greene--Kleitman matching with `1` as an opening symbol and
`0` as a closing symbol.  For `U in \mathcal U`, let `p(U)` and `q(U)` be
its first and second free `1`, and put

\[
 A(U)=U-p(U),\qquad
 L(U)=U-\{p(U),q(U)\},\qquad
 B(U)=U-q(U).
\tag{0.2}
\]

Write `\beta(U)=B(U)` for the head map.

Then:

1. `U -> L(U)` is injective.  It is exactly the two-step downward
   Greene--Kleitman chain map.
2. The option `(U,p,q,A,L,B)` belongs to the topology-safe leaf-right host:
   `q>p`, and `q` is a free `1` of `A`.
3. Fix `B in \mathcal M`.  In the canonical GK factorization of `B`, let
   `D(B)` be the balanced word between its last free `0` and first free
   `1`; when there is no free `0`, it is the balanced prefix before the
   unique first free `1`.
   Then

   \[
       |\beta^{-1}(B)|=
       \#\{\hbox{top-level primitive factors of }D(B)\}.
   \tag{0.3}
   \]

4. The exact number of heads having fiber size `k` is

   \[
   \boxed{
   \#\{B:|\beta^{-1}(B)|=k\}={2m-k\choose m-k}}
   \qquad(1\le k\le m).
   \tag{0.4}
   \]

Consequently

\[
 |\operatorname {im}B|={2m\choose m-1},
 \tag{0.5}
\]

and the exact duplicate/head deficit is

\[
 \boxed{
 |\mathcal U|-|\operatorname {im}B|
 ={2m\choose m-2}
 ={m-1\over2m+1}|\mathcal U|.}
\tag{0.6}
\]

Thus the most direct two-step GK selector is perfect on lower colors but
wastes asymptotically one half of the available distinct heads.  Any proof
of a full-leaf three-chart-plus-reset theorem must move a macroscopic family
away from this canonical choice.

## 1. The two downward GK steps

Repeatedly erase matched `10` pairs.  The remaining symbols of any word are
some free zeros followed by some free ones.  Since `U` has three more ones
than zeros, its first two free ones exist.  Changing the first free one to
zero is one downward step in its Greene--Kleitman chain; changing the next
free one is the second downward step.  Hence `(0.2)` is exactly the map from
rank `m+2` to rank `m` within each GK chain.

The symmetric-chain decomposition partitions the Boolean lattice.  Every
rank-`m` word has at most one rank-`m+2` word in its chain, so

\[
                         U\longmapsto L(U)
\tag{1.1}
\]

is injective.

After the first step, `q(U)` is the first free one of `A(U)`.  In
particular it is a leaf in the sense of the fixed-GK leaf catalogue.  Free
positions are ordered as free zeros followed by free ones, and `p(U)` has
just become the last free zero of `A(U)`.  Therefore `q(U)>p(U)`.  This
proves assertions 1 and 2.

## 2. The exact inverse primitive catalogue

Every `B in \mathcal M` has a unique factorization

```text
D_0 0 D_1 0 ... 0 D_a 1 D_{a+1} 1 ... 1 D_{2a+1},
```

where the displayed zeros and ones are the free symbols and every `D_i` is
a (possibly empty) Dyck word.  There are `a` free zeros and `a+1` free
ones.  Define the **central balanced factor**

\[
                              D(B):=D_a.
\tag{2.1}
\]

Write its unique top-level decomposition as

\[
                     D(B)=P_1P_2\cdots P_k,
\tag{2.2}
\]

where every `P_i` is a nonempty primitive Dyck word.  For `a=0`, the
factor `D_a=D_0` is the prefix before the unique first free `1`; for
`a>0`, it is literally between the last free `0` and first free `1`.
Let `p_i` and `q_i`
be the opening and closing symbols of `P_i`.

Changing the closing zero `q_i` to one leaves `p_i` unmatched and makes
`q_i` the next unmatched one.  All earlier and later top-level factors
remain balanced.  Thus for

\[
                              U_i=B+q_i,
\tag{2.3}
\]

the first two free ones are exactly `p_i,q_i`.  Applying `(0.2)` gives

\[
                              B(U_i)=B.
\tag{2.4}
\]

Conversely, suppose `B=B(U)` under `(0.2)`.  In `B`, the changed coordinate
`q(U)` is a zero and matches the still-present first free one `p(U)`.
There is no unmatched symbol strictly between them, so this matched block
is one top-level primitive factor of the central balanced factor `(2.1)`.
The two constructions are inverse.  This proves `(0.3)`.

## 3. Exact Catalan-triangle fiber enumeration

Let

\[
 C(x)=1+xC(x)^2
\tag{3.1}
\]

be the Catalan generating function.  A primitive Dyck word has generating
function `xC(x)`.  Fix the number `a` of free zeros.  Apart from the central
factor, the factorization in Section 2 has `2a+1` arbitrary Dyck gaps.  A
central factor with exactly `k` primitive components contributes
`(xC(x))^k`.  Since the matched part has semilength `m-a`, the required
number is

\[
 \sum_{a\ge0}[x^{m-a}](xC)^kC^{2a+1}
 =[x^{m-k}]{C^{k+1}\over1-xC^2}
 =[x^{m-k}]{C^{k+1}\over2-C}.
\tag{3.2}
\]

The standard Lagrange identity, valid for `r>=0` and `s>=1`,

\[
 [x^r]{C(x)^s\over2-C(x)}={2r+s-1\choose r}
\tag{3.3}
\]

now gives

\[
 [x^{m-k}]{C^{k+1}\over2-C}
 ={2m-k\choose m-k},
\tag{3.4}
\]

which is `(0.4)`.

Summing over the nonempty fibers and using the hockey-stick identity gives

\[
 \sum_{k=1}^m{2m-k\choose m-k}
 =\sum_{j=0}^{m-1}{m+j\choose j}
 ={2m\choose m-1}.
\tag{3.5}
\]

Finally,
`|\mathcal U|={2m+1\choose m+2}={2m+1\choose m-1}`, and Pascal's
identity gives

\[
 {2m+1\choose m-1}-{2m\choose m-1}
 ={2m\choose m-2}.
\tag{3.6}
\]

Dividing by `|\mathcal U|` proves the last equality in `(0.6)`.

## 4. Scope and repair interface

The collision count above alone is not a Hall proof about the complete
leaf host.  It concerns the single deterministic rule “take the next free
one.”  The full host also permits adjacent matched peaks and the other two
inverse head charts.  Exact simultaneous lower/head SDRs exist through
`m=6` in the frozen finite certificates.  On the other hand, the purely
leaf-right subhost has a separate exact Hall obstruction already at `m=7`:
its upper--head projection has maximum matching `4950<5005`.  Thus an
all-parameter repair must also use chart-zero left resets `q<p`; it cannot
remain entirely inside the descending-potential leaf-right host.

What `(0.4)--(0.6)` supply is an exact repair ledger.  A head with central
factor `P_1...P_k` receives `k` canonical uppers and can retain only one;
the other `k-1` labels must be rerouted.  The total rerouting demand is the
binomial quantity in `(0.6)`, not a lower-order exceptional set.  Therefore
an all-parameter proof must use the full three-chart geometry globally and
organize a necessary bank of chart-zero resets.  Bounded or sparse repairs
of the canonical selector cannot suffice.

## 5. Reproducibility

The H100-only diagnostic

`scratch/audit_gk_canonical_leaf_rules_20260814.py`

enumerates the literal rule, verifies lower injectivity, and checks the
fiber histogram `(0.4)` through `m=10`.  The structural proof above does
not depend on finite extrapolation.
