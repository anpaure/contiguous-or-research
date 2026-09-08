# Gate C: exact gap-winding coordinates for the two-sided-ballot count

**Status (2026-08-22).** Every assertion below is proved.  A cyclic block
order is encoded by the positive clockwise gaps between the positions of
successive block values.  In these coordinates, every sign in the ballot
word is exactly the parity of two integers: the number of even gaps crossed
and the number of complete position-circle windings.

In particular, a two-sided-ballot cut forces both incident successive-value
gaps to be odd.  Hence an order with at most `R<K` failed cuts has at most
`R` even gaps, all contained in the cyclic subgraph induced by the failed
values.  This is a strict sparse-defect reduction, not yet the required
entropy bound.

Throughout, `K>=3` is odd and all subscripts are read modulo `K`.

## 1. Successive-value gaps

Let `tau in S_K` be a cyclic block order: position `i` carries value
`tau_i`.  Write

\[
 \sigma=\tau^{-1},\qquad
 d_a=(\sigma(a+1)-\sigma(a))\bmod K\in\{1,\ldots,K-1\}.
                                                               \tag{1.1}
\]

For `1<=u<=K`, put

\[
 D_a(u)=\sum_{t=0}^{u-1}d_{a+t},\qquad
 E_a(u)=|\{0\le t<u:d_{a+t}\text{ is even}\}|,
 \qquad L_a(u)=\left\lfloor{D_a(u)\over K}\right\rfloor.
                                                               \tag{1.2}
\]

The total sum is a positive multiple of `K`:

\[
                  \sum_{a\in\mathbb Z_K}d_a=hK,
                  \qquad 1\le h\le K-1.                    \tag{1.3}
\]

Indeed, the gaps telescope modulo `K`; their sum lies strictly between
zero and `K^2`.  Moreover

\[
                         h\equiv K-E_0(K)\pmod2.            \tag{1.4}
\]

This follows because `K` is odd and the parity of the sum of the gaps is
the parity of the number of odd gaps.

## 2. Exact winding formula

For the cut at position `i=sigma(a)`, the sign word from the equal-block
row theorem is

\[
 w_a(u)=+1
 \quad\Longleftrightarrow\quad
 (\sigma(a+u)-\sigma(a))\bmod K\equiv u\pmod2,
 \qquad 1\le u<K.                                      \tag{2.1}
\]

### Theorem 2.1 (gap/winding identity)

For every `a` and `1<=u<K`, one has

\[
 \boxed{w_a(u)=(-1)^{E_a(u)+L_a(u)}.}                    \tag{2.2}
\]

#### Proof

The telescoping definition of the gaps gives

\[
 R_a(u):=(\sigma(a+u)-\sigma(a))\bmod K
        =D_a(u)-K L_a(u).                                \tag{2.3}
\]

The remainder is nonzero for `u<K`, so the displayed floor is the unique
integer producing the representative in `{1,...,K-1}`.  Among the `u`
gaps in (1.2), exactly `u-E_a(u)` are odd.  Since `K` is odd,

\[
 R_a(u)\equiv D_a(u)-L_a(u)
          \equiv u-E_a(u)-L_a(u)\pmod2.                  \tag{2.4}
\]

Thus `R_a(u)` has the same parity as `u` exactly when
`E_a(u)+L_a(u)` is even.  This is (2.2).  \(\square\)

When every gap is odd, (2.2) simplifies to

\[
 \boxed{w_a(u)=(-1)^{\lfloor D_a(u)/K\rfloor}.}           \tag{2.5}
\]

Thus the signs are constant during each complete traversal of the position
circle and alternate whenever the increasing lift `D_a(u)` crosses a
multiple of `K`.

## 3. Exceptional cuts contain every even gap

Call value `a` good when its word `w_a(1),...,w_a(K-1)` is two-sided
ballot:

\[
 0\le\sum_{u=1}^m w_a(u)\le
       \sum_{u=1}^{K-1}w_a(u)\qquad(1\le m<K).            \tag{3.1}
\]

### Lemma 3.1 (both incident gaps are odd)

If `a` is good, then `d_a` and `d_(a-1)` are odd.

#### Proof

The first step in (3.1) must be `+1`; otherwise its first prefix is
negative.  Since `d_a<K`, (2.2) at `u=1` has `L_a(1)=0` and says
`w_a(1)=(-1)^{1_{d_a even}}`.  Hence `d_a` is odd.

The last step must also be `+1`: if it were `-1`, the penultimate prefix
would exceed the terminal sum by one, violating the upper inequality in
(3.1).  Directly,

\[
 (\sigma(a-1)-\sigma(a))\bmod K=K-d_{a-1}.              \tag{3.2}
\]

The index `K-1` is even, while `K-d_(a-1)` is even exactly when
`d_(a-1)` is odd.  Equation (2.1) proves the claim. \(\square\)

### Corollary 3.2 (sparse even-gap defect)

Let `B` be the set of failed cuts and suppose `|B|=R<K`.  If `d_a` is
even, then both `a` and `a+1` lie in `B`.  Consequently

\[
 \boxed{|\{a:d_a\text{ is even}\}|\le R.}               \tag{3.3}
\]

More precisely, the even gaps are edges of the cyclic graph induced by
`B`; if `B` has `c` nonempty cyclic components, their number is at most
`R-c`.

#### Proof

Apply Lemma 3.1 first at `a` and then at `a+1`.  Thus either endpoint being
good would force `d_a` odd.  The induced subgraph of a proper vertex subset
of a cycle is a union of paths, with `R-c` edges. \(\square\)

At the coefficient-one equal-block scale, the preceding ballot-rigidity
theorem gives `R=O(K^2/b)=o(K)`.  Hence (3.3) shows that all but `o(K)`
successive-value gaps are odd, while (2.5) controls every interval avoiding
the sparse even-gap set.

## 4. Exact injective encoding

The pair

\[
                         (\sigma(0),(d_a)_{a\in\mathbb Z_K})             \tag{4.1}
\]

determines `sigma`, hence `tau`, because recursively

\[
                         \sigma(a+1)=\sigma(a)+d_a\pmod K.               \tag{4.2}
\]

Conversely, a sequence `d_a in {1,...,K-1}` comes from a block order iff
its successive partial sums modulo `K` are all distinct and its total is
zero modulo `K`; choosing `sigma(0)` then gives exactly one order.  Thus the
live count is equivalently a count of Hamiltonian positive-gap sequences
satisfying (3.1) through the exact winding formula (2.2), with at most `R`
even entries.

This coordinate change by itself gives no subfactorial bound: merely
counting sequences with sparse even gaps is still too large.  The missing
step is a rigidity or entropy theorem for the simultaneous winding-ballot
conditions at the `K-R` good starting points.
