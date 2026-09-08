# Gate C: all-good orders as culminating Hamilton cycles of the carousel

**Status (2026-08-22).** Every reduction below is proved.  After a fixed
sign transform, the pair-sign array of every block order is a relabeling of
one canonical regular locally transitive tournament.  All-good orders are
exactly those relabelings in which the fixed value cycle is directed and
every alternating edge row is a two-sided culminating walk.

This isolates a sharp optional rigidity conjecture: every such labeling
may be affine.  It holds by exhaustive computation through `K=11` and by
targeted search at `K=13,15`, but no general proof is claimed.  The pivot
miss-set theorem already rules out the equal-block Gate-C route without
this classification.

Throughout, `K=2e+1>=3` and all subscripts are read modulo `K`.

## 1. Symmetric pair signs

Let `sigma` send each value to its position.  For distinct values `a,b`,
put

\[
 x_{ab}=(-1)^{((b-a)\bmod K)+((\sigma(b)-\sigma(a))\bmod K)}.       \tag{1.1}
\]

Because reversing both nonzero clockwise distances replaces their sum by
`2K` minus that sum,

\[
                              x_{ab}=x_{ba}.            \tag{1.2}
\]

The ballot word at cut `a` is

\[
                         x_{a,a+1},...,x_{a,a+K-1}.     \tag{1.3}
\]

## 2. The carousel transform

Define a skew sign array by

\[
                 y_{ab}=(-1)^{(b-a)\bmod K}x_{ab}.      \tag{2.1}
\]

Then

\[
 \boxed{y_{ab}=(-1)^{(\sigma(b)-\sigma(a))\bmod K}.}   \tag{2.2}
\]

In particular `y_{ba}=-y_{ab}`.  Orient the edge from `a` to `b` exactly
when `y_{ab}=+1`.

### Theorem 2.1 (canonical carousel)

Under the relabeling `a\mapsto\sigma(a)`, the tournament (2.1) is the
canonical tournament `C_K` on `Z_K` in which

\[
             p\longrightarrow q
             \quad\Longleftrightarrow\quad
             (q-p)\bmod K\text{ is even}.              \tag{2.3}
\]

It is regular and locally transitive.

#### Proof

Formula (2.2) is immediate from (1.1), because the value-distance exponent
occurs twice.  It gives (2.3).  From any `p`, exactly the `e` nonzero even
distances are outgoing and the `e` odd distances are incoming, proving
regularity.

List the out-neighbors as

\[
                       p+2,p+4,...,p+2e.                \tag{2.4}
\]

For two entries in this order, the forward difference is a positive even
integer smaller than `K`, so the earlier points to the later.  Thus the
out-neighborhood is transitive.  The same argument for
`p+1,p+3,...,p+2e-1` proves that the in-neighborhood is transitive.
\(\square\)

Equivalently, in linear representatives,

\[
 y_{ab}=(-1)^{\sigma(a)+\sigma(b)}
          \operatorname{sgn}(\sigma(b)-\sigma(a)),      \tag{2.5}
\]

so this carousel is a vertex switch of the transitive tournament in
position order.

## 3. Exact all-good Hamilton formulation

Call a sign word `z_1,...,z_{2e}` *culminating* when

\[
          0\le\sum_{u=1}^m z_u\le\sum_{u=1}^{2e}z_u
          \qquad(1\le m\le2e).                         \tag{3.1}
\]

By (2.1),

\[
                         x_{a,a+u}=(-1)^u y_{a,a+u}.    \tag{3.2}
\]

### Theorem 3.1 (culminating Hamilton equivalence)

An order is all-good if and only if, in its carousel labeling,

1. the value cycle
   \[
                    0\to K-1\to K-2\to\cdots\to1\to0 \tag{3.3}
   \]
   is directed; and
2. for every `a`, the alternating edge row
   \[
             \bigl((-1)^u y_{a,a+u}\bigr)_{u=1}^{K-1} \tag{3.4}
   \]
   is culminating.

The directed-cycle condition is redundant in item 2, but records the
Hamilton constraint explicitly.

#### Proof

Equations (1.3), (3.1), and (3.2) identify goodness at `a` exactly with
item 2 for that `a`.  A culminating word must start and end with `+1`.
The last sign says `x_{a,a-1}=+1`; since `K-1` is even, (2.1) gives
`y_{a,a-1}=+1`, which is precisely the edge `a->a-1` in (3.3).  Conversely
item 2 already says every row (1.3) is good. \(\square\)

The first/last-sign part alone is equivalent to all successive position
gaps

\[
                     (\sigma(a+1)-\sigma(a))\bmod K    \tag{3.5}
\]

being odd.  Thus the earlier odd-gap Hamilton condition is exactly the
directed-cycle condition (3.3).

## 4. The affine family

Let `d` be a unit modulo `K` and set

\[
                            \sigma_d(a)=da\pmod K.      \tag{4.1}
\]

Every row then has the same pair-sign word

\[
               z_d(u)=(-1)^{u+(du\bmod K)},qquad1\le u<K.            \tag{4.2}
\]

### Proposition 4.1 (exact affine criterion)

The affine order (4.1) is all-good if and only if the word (4.2) is
culminating.  In particular any such `d` is odd.

#### Proof

Substitution in (1.1) gives (4.2), independently of the root `a`.  Theorem
3.1 proves the criterion.  Its first sign is positive only when `d` is
odd. \(\square\)

## 5. The optional rigidity theorem still open

The exact structural question is now:

> Is every culminating directed Hamilton labeling of `C_K` one of the
> affine labelings (4.1)?

Normalized exhaustive results are:

\[
\begin{array}{c|c|c}
K&\text{all-good orders with }\tau(0)=0&\text{affine gaps }d\\ \hline
3&1&1\\
5&1&1\\
7&3&1,3,5\\
9&1&1\\
11&3&1,5,9.
\end{array}                                             \tag{5.1}
\]

Targeted pivot-improving searches at `K=13` and `K=15` found respectively
only the affine gaps `{1,3,9}` and `{1,7,11,13}`.  Those two search results
are evidence, not exhaustive certificates.

The companion checker
`scratch/verify_gate_c_carousel_tournament_all_good_20260822.py` proves the
finite identities directly and exhausts all normalized orders through
`K=9`.  The exact `K=11` census is independently produced by the existing
compiled spectrum checker; (5.1) labels that row computational.
