# Tomon's equal-chain theorem lies below the critical coefficient

Date: 2026-08-04  
Status: unconditional scope theorem and quantitative barrier. This note does
not disprove sharp Boolean chainization; it proves that the published
equal-chain theorem cannot supply it without a new, macroscopic rechainization
and then a separate endpoint-serialization theorem.

## 0. Setup and verdict

Put

\[
 r=\left\lceil {k\over2}\right\rceil,
 \qquad W=\binom{k}{r},
 \qquad
 \mathcal L_{<r}=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|\mathcal L_{<r}|,
\]

and let `d=d(k)` be the least integer satisfying

\[
 dW+\binom{d+1}{2}\ge \Lambda.
\]

The established asymptotic is

\[
 d=\sqrt{\pi k/8}+O(1),
 \qquad
 {2^k\over W}=2d+O(1).                         \tag{0.1}
\]

Tomon's equal-chain theorem says that if `c` is a positive integer and

\[
                         k>500c^2,               \tag{0.2}
\]

then the Boolean lattice `2^[k]` has a `c`-partition: all but at most one
chain have exactly `c` members, and the exceptional chain has at most `c`
members.

The coefficient in (0.2) misses both relevant OR scales by a fixed factor.

* At the strict-lower depth `c=d+O(1)`,

  \[
  {500c^2\over k}\longrightarrow {500\pi\over8}>196.
  \tag{0.3}
  \]

* At the full-lattice average-chain scale `c=2d+O(1)`,

  \[
  {500c^2\over k}\longrightarrow {500\pi\over2}>785.
  \tag{0.4}
  \]

Thus (0.2) is false in both critical regimes for every sufficiently large
`k`; this is a failure of the theorem's hypothesis, not a nonexistence
claim.

More quantitatively, every `c` certified by (0.2) satisfies

\[
 {c\over d}\le
 \sqrt{8\over500\pi}+o(1)=0.071\ldots .          \tag{0.5}
\]

Restricting such a `c`-partition to the strict lower ideal produces at least

\[
 \left(\sqrt{500\pi/8}+o(1)\right)W
 = (14.012\ldots+o(1))W                          \tag{0.6}
\]

nonempty chain fragments. A word of length `W+d+O(1)` has only
`W+d+O(1)=(1+o(1))W` right-endpoint chains. Consequently, any adaptation
of Tomon's partition must perform at least

\[
 \left(\sqrt{500\pi/8}-1-o(1)\right)W
 = (13.012\ldots-o(1))W                          \tag{0.7}
\]

genuine cross-fragment chain joins before endpoint serialization is even
possible.

This is the precise scope barrier: truncation, splitting, deleting empty
parts, or relabelling chains by owners cannot help. A successful adaptation
would need a new `Theta(W)` correlated rechainization theorem, followed by
owner containment and the physical countdown law.

## 1. The primary equal-chain input

A `c`-partition of a finite poset is a partition into chains in which all
but at most one chain have size `c`. The exceptional chain, when present,
has size at most `c`.

Tomon's theorem gives a `c`-partition of `2^[k]` under (0.2). The explicit
constant is important here: an undischarged notation such as
`k=Omega(c^2)` conceals the coefficient that decides whether the result
reaches the OR scale.

Primary source:

* I. Tomon, *Improved bounds on the partitioning of the Boolean lattice into
  chains of equal size*, Discrete Mathematics 339 (2016), 333--343,
  DOI `10.1016/j.disc.2015.08.025`.

The author's theorem summary states the explicit condition `k>500c^2`.

## 2. Critical-coefficient comparison

### Theorem 2.1 (the published range does not reach `d+O(1)`)

Fix an absolute constant `C`. For all sufficiently large `k`, Tomon's
hypothesis (0.2) does not apply with

\[
                         c=d(k)+C.                 \tag{2.1}
\]

It also does not apply with `c=2d(k)+C`.

#### Proof

By (0.1),

\[
 {500(d+C)^2\over k}
 = {500\pi\over8}+o(1)>1,
\]

so eventually `500(d+C)^2>k`. Replacing `d+C` by `2d+C` gives the limit
`500pi/2>1`. Both contradict (0.2). \(\square\)

The first substitution is the maximum size wanted for one strict-lower
owner chain. The second is the natural size of one full-lattice chain in a
minimum `W`-chain decomposition. Hence neither the one-sided nor the
complemented full-lattice route is in the theorem's certified range.

### Corollary 2.2 (largest certified chains have seven percent of the needed
lower depth)

If `c=c(k)` obeys (0.2), then (0.5) holds.

#### Proof

Condition (0.2) gives `c<sqrt(k/500)`. Divide by
`d=sqrt(pi k/8)+O(1)`. \(\square\)

For the full-lattice average `s_k=2^k/W=2d+O(1)`, the corresponding ratio is

\[
 {c\over s_k}\le
 \sqrt{2\over500\pi}+o(1)=0.035\ldots .           \tag{2.2}
\]

Thus the theorem produces many short chains, not a near-minimum chain
decomposition.

## 3. Restriction to the lower ideal

Let `mathscr P` be any `c`-partition of `2^[k]`. Because
`mathcal L_<r` is a down-set, the intersection of a chain in `mathscr P`
with `mathcal L_<r` is an initial segment of that chain, hence is itself a
chain. Delete empty intersections, and call the resulting family of lower
fragments `mathscr F`.

### Lemma 3.1 (fragment count)

\[
                         |\mathscr F|\ge
                         \left\lceil{\Lambda\over c}\right\rceil .
                                                               \tag{3.1}
\]

#### Proof

The fragments partition `mathcal L_<r`, and every fragment has at most `c`
members. \(\square\)

### Theorem 3.2 (macroscopic rechainization is necessary)

Suppose `mathscr P` is supplied by Tomon's theorem, so `k>500c^2`. Then

\[
 { |\mathscr F|\over W}
 \ge \sqrt{500\pi/8}+o(1).                         \tag{3.2}
\]

Any construction which turns all these fragments into at most
`W+d+C` chains, without losing a lower target, requires at least

\[
 |\mathscr F|-(W+d+C)
 \ge
 \left(\sqrt{500\pi/8}-1-o(1)\right)W              \tag{3.3}
\]

cross-fragment joins.

#### Proof

From `c<sqrt(k/500)`, Lemma 3.1, and
`Lambda/W=d+O(1)`,

\[
 { |\mathscr F|\over W}
 \ge {\Lambda\over cW}
 = {d+O(1)\over c}
 \ge \sqrt{500\pi/8}+o(1).
\]

A join of two current chain components can reduce their number by at most
one. To go from `|mathscr F|` components to at most `W+d+C` therefore
requires at least their difference in joins. Since `d+C=o(W)`, (3.3)
follows. \(\square\)

The count is insensitive to the exceptional chain: its lower intersection
also has size at most `c`.

## 4. Why this is an owner and chronology barrier, not just a size estimate

An anchored lower-chain factor asks for one inclusion chain under each
middle owner `T`, together with only the `d,d-1,...,1` boundary staircase in
the linear model. A word of length `W+d+C` gives at most `W+d+C`
right-endpoint chains, because all interval unions ending at a fixed
position are nested.

Tomon's lower fragments are merely abstract chains. The theorem does not
provide any of the following.

1. **Cross-fragment comparability.** Placing several fragments under the
   same owner does not make their union a chain. The `Theta(W)` joins in
   (3.3) must be actual comparable joins.
2. **Distinct owner containment.** Even after a join, the resulting chain
   must lie below a distinct rank-`r` owner. Relabelling alone does not
   prove the required containment matching.
3. **Endpoint serialization.** If `a_i(x)` is the age of coordinate `x` at
   consecutive owners, a physical OR word requires

   \[
   x\in T_i\cap T_{i+1},\quad a_i(x)>0
       \Longrightarrow a_{i+1}(x)=a_i(x)-1.         \tag{4.1}
   \]

   An abstract chain partition supplies no ordering of owners and no
   countdown-compatible flags.
4. **The second endpoint system.** A word simultaneously induces the
   fixed-right and fixed-left nested interval systems. One abstract chain
   decomposition supplies only one marginal system.

Consequently, even a hypothetical improvement of `500` sufficient to reach
`c=d` would not automatically solve the OR problem: it would first give
roughly `2W` full-lattice chains (because the average full chain length is
`2d+O(1)`), and the lower fragments would still need owner correlation and
serialization. Reaching `c=2d+O(1)` would be the relevant full-lattice
coefficient, but would still leave (4.1).

## 5. Relation to the stronger uniform-chain results

Sudakov--Tomon--Wagner construct a minimum `W`-chain decomposition in which
all but an `o(1)` proportion of chains have asymptotically average size.
Restricting their upper-half construction yields an anchored lower factor
covering all but `o(Lambda)` targets at depth `d`.

This is asymptotically much sharper than the `c`-partition theorem, but it
still leaves an exponentially large exceptional bank in absolute terms.
It does not give an all-chain `d+O(1)` maximum, an `O(1)` lower-target
defect, or the countdown law (4.1). Thus it does not remove the endpoint
serialization gate.

Primary source:

* B. Sudakov, I. Tomon and A. Z. Wagner, *Uniform chain decompositions and
  applications*, Random Structures & Algorithms 60 (2022), 261--286,
  arXiv:1911.09533.

## 6. Exact conclusion

Tomon's equal-chain theorem is not a hidden proof of
`nu(k)<=B(k)+O(1)`. Its explicit coefficient certifies chains shorter than
the needed lower depth by a factor tending to at least `14.012...`, and its
restriction leaves at least `14.012...W` lower fragments.

Therefore the shortest honest implication is

\[
\boxed{
 \text{Tomon short equal chains}
 \;\Longrightarrow\;
 \Theta(W)\text{ new cross-chain joins still required}
 \;\Longrightarrow\;
 \text{owner matching still required}
 \;\Longrightarrow\;
 \text{endpoint countdown still required}.}
\]

The result is a scope barrier, not a no-go theorem. A new global
rechainization using the Boolean geometry could perform the required joins;
proving that is essentially the sharp chainization frontier already isolated
in the repository.
