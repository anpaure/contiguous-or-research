# Self-containment audit for `MASTER_HANDOFF.md`, Sections 1--2

**Date:** 2026-08-22  
**Scope:** the problem model, zero theorem, move-to-front model, rank-slack
lower bound, central maximizer, the asymptotic for `d(k)`, finite exact
values through `k=16`, the `k=17` upper bound, coordinate deletion, top-bit
splicing, and the unconditional `sqrt(2)` construction.  
**Verdict:** the statements retained in Sections 1--2 are mathematically
correct, but the compressed handoff is not self-contained under the strict
requirement that no cited file carry any part of their proof.  The inline
proofs below close every infinite-family gap.  The finite upper certificates
must additionally be embedded as data, as specified in Section 9.

## 1. Exact gaps in the compressed handoff

The current text omits the following logical steps.

1. The zero theorem does not state that intervals are nonempty, does not
   justify the lower direction, and leaves the `k=0` convention implicit.
2. The move-to-front paragraph does not prove the suffix-prefix
   correspondence or its converse, and its states are ordered partitions of
   the coordinates seen so far, not necessarily partitions of all `[k]`.
3. The lower-bound kernel does not prove strictness of both endpoint orders,
   the endpoint inequalities, the long-interval containment lemma, or the
   short-interval count.
4. The assertion that `s=ceil(k/2)` maximizes the bound has no proof.
5. The assertion `d(k)=sqrt(pi k/8)+O(1)` has neither the exact even/odd tail
   calculation nor an internal central-binomial estimate.
6. The exact finite table and the `k=17` upper bound depend entirely on
   external word files and a checker.  Hashes authenticate external bytes but
   are not self-contained existence proofs.
7. Coordinate deletion, its averaged inequality, and top-bit splicing are
   stated without proofs.
8. The `sqrt(2)` construction is delegated completely to another file.

The citations may remain as provenance, but the handoff should expressly say
that they are not logical dependencies.

## 2. Conventions and the zero theorem

All witnessing intervals are nonempty: `1 <= i <= j <= n`.  Put
`nu(0)=0`, witnessed by the empty word.

Suppose a word covering the empty target contains zero letters.  It must
contain at least one zero letter, since the union of a nonempty interval is
empty only when every letter in that interval is empty.  Delete every zero
position.  A witness for a nonempty target contains a nonzero letter; after
the deletion its surviving letters are consecutive and have the same union.
The result is therefore a nonzero universal word of length at most `N(k)-1`,
so `N(k) >= nu(k)+1`.

Conversely, append one zero letter to a shortest nonzero universal word.  All
old witnesses remain, and the singleton interval at the new position realizes
the empty set.  Hence

\[
                         N(k)=\nu(k)+1.
\]

This includes `k=0`, where `N(0)=1`.

## 3. Exact move-to-front state model

After positions `1,...,j`, group the coordinates having each finite
last-occurrence time, ordered from newest to oldest.  This gives an ordered
partition `(B_1,...,B_t)` of the coordinates seen so far.  A suffix whose
left endpoint lies strictly after one last-occurrence level contains exactly
the coordinates in the preceding, newer blocks.  Thus the distinct nonempty
suffix unions ending at `j` are precisely

\[
B_1,\quad B_1\cup B_2,\quad\ldots,\quad B_1\cup\cdots\cup B_t.
\]

After appending a nonempty set `X`, all coordinates in `X` acquire the newest
time and every old block loses its elements of `X`.  The new state is exactly

\[
(X,B_1\setminus X,\ldots,B_t\setminus X),
\]

after empty blocks are removed.  Conversely, a sequence of such updates
records its update sets as the letters of a word, and the prefix unions in
its states are exactly that word's suffix unions.  Therefore `nu(k)` is the
minimum number of updates required for these state-prefix unions to cover
`2^{[k]}\setminus\{\varnothing\}`.

Finally, induction on `q` gives

\[
(D^qX)_i=\bigcup_{h=0}^q X_{i+h},
\]

so the derivative triangle is exactly the catalogue of all interval unions.

## 4. Complete rank-slack lower-bound proof

Fix `1 <= s <= k`, put `M=M_s=binom(k,s)`, and suppose a universal word has
length `n`.  Choose one witness interval for each of the `M` distinct
rank-`s` targets.  These intervals are pairwise noncontaining: containment of
intervals implies containment of their unions, while two distinct `s`-sets
cannot contain one another.  In particular `n >= M`.

Write `n=M+t`, order the witnesses by left endpoint, and denote them
`[ell_i,u_i]`, `1 <= i <= M`.  The left endpoints are distinct.  Their order
forces the right endpoints to be strictly increasing as well, because
`ell_i < ell_j` and `u_i >= u_j` would make the latter interval a subinterval
of the former.  Both endpoint sequences are therefore strictly increasing
integer sequences in `[1,M+t]`, and hence

\[
                   i\le\ell_i\le u_i\le i+t.                 \tag{4.1}
\]

Every interval `[a,b]` of length at least `t+1` satisfies `a <= M` and
`b >= a+t`; by (4.1) it contains `[ell_a,u_a]`.  Its union consequently has
rank at least `s`.  Every target of rank below `s` must therefore use an
interval of length at most `t`.  The number of such physical intervals is

\[
\sum_{h=1}^t(n-h+1)
 =tM+\binom{t+1}{2}.                                  \tag{4.2}
\]

Distinct targets require distinct witness intervals, so

\[
\Lambda_s\le tM_s+\binom{t+1}{2}.
\]

Thus `t >= tau_s` and `n >= M_s+tau_s`.  Maximizing over `s` proves the
displayed general lower bound.

## 5. Complete proof that the central rank maximizes

Put

\[
b_s=M_s+\tau_s,\qquad
H_s=\Lambda_s+\binom{M_s+1}{2}.
\]

For `n=M_s+t`, the identity

\[
tM_s+\binom{t+1}{2}
 =\binom{n+1}{2}-\binom{M_s+1}{2}                    \tag{5.1}
\]

shows that `b_s` is exactly the least integer `n` for which
`binom(n+1,2) >= H_s`.  (The constraint `n >= M_s` is automatic because
`H_s >= binom(M_s+1,2)`.)  It is therefore enough to maximize `H_s`.

Let `a=M_s` and `b=M_{s+1}`.  Since
`Lambda_{s+1}=Lambda_s+a`,

\[
H_{s+1}-H_s
 =a+\frac{b(b+1)-a(a+1)}2.                          \tag{5.2}
\]

This is positive whenever `b >= a`.  If `a>b`, write `e=a-b >= 1`.  Then

\[
e(a+b+1)-2a=(e-1)(2b+e)\ge0,
\]

so (5.2) is nonpositive.  The binomial ranks increase to the middle, with
two equal middle ranks in odd dimension, and then decrease.  Consequently
`H_s`, and hence `b_s`, attains its maximum at
`s=ceil(k/2)`.  This proves

\[
B(k)=W+d(k).
\]

The maximizer need not be unique in the smallest dimensions; the statement
only asserts that the displayed central rank is a maximizer.

## 6. An internal central-binomial estimate

Let

\[
I_n=\int_0^{\pi/2}\sin^n x\,dx.
\]

Integration by parts gives `I_n=((n-1)/n)I_{n-2}`, and hence

\[
I_{2m}=\frac\pi2\frac{\binom{2m}{m}}{4^m}.           \tag{6.1}
\]

After substituting `x=pi/2-u/sqrt(n)`,

\[
\sqrt n I_n
 =\int_0^{\pi\sqrt n/2}
       \cos^n(u/\sqrt n)\,du.                        \tag{6.2}
\]

For `0 <= y < pi/2`, `tan y >= y`, so
`log cos y <= -y^2/2`.  On `0 <= y <= 1`, Taylor's theorem also gives

\[
\log\cos y\ge-y^2/2-Cy^4                            \tag{6.3}
\]

for an absolute constant `C`; equivalently, the quotient
`(log cos y+y^2/2)/y^4` extends continuously at zero and is bounded below on
`[0,1]`.  Thus, for `0 <= u <= sqrt(n)`,

\[
e^{-u^2/2-Cu^4/n}
 \le \cos^n(u/\sqrt n)
 \le e^{-u^2/2},                                     \tag{6.4}
\]

and the upper bound holds throughout (6.2).  Since `1-e^{-v} <= v`, the
integral gap between the two sides of (6.4) is at most

\[
\frac Cn\int_0^\infty u^4e^{-u^2/2}\,du=O(1/n),
\]

while the Gaussian tail beyond `sqrt(n)` is exponentially small.  Therefore

\[
I_n=\sqrt{\frac\pi{2n}}\left(1+O(1/n)\right).        \tag{6.5}
\]

For completeness, the Gaussian constant follows by squaring
`J=int_0^infinity exp(-u^2/2)du` and using polar coordinates in the first
quadrant:

\[
J^2=\int_0^{\pi/2}\int_0^\infty e^{-r^2/2}r\,dr\,d\theta
   =\pi/2.
\]

Equations (6.1)--(6.5) give

\[
\binom{2m}{m}
 =\frac{4^m}{\sqrt{\pi m}}\left(1+O(1/m)\right).
\]

Using
`binom(2m+1,m)=((2m+1)/(m+1))binom(2m,m)` then yields, uniformly in parity,

\[
W(t)=\binom t{\lfloor t/2\rfloor}
 =2^t\sqrt{\frac2{\pi t}}\left(1+O(1/t)\right).     \tag{6.6}
\]

## 7. The asymptotic for `d(k)`

At `r=ceil(k/2)`, write `W=binom(k,r)` and `Lambda=Lambda_r`.  If `k=2m`,

\[
\Lambda=2^{2m-1}-\frac W2-1,                         \tag{7.1}
\]

whereas if `k=2m+1`,

\[
\Lambda=2^{2m}-1,
\qquad
W=\frac{2m+1}{m+1}\binom{2m}{m}.                    \tag{7.2}
\]

The internal estimate (6.6) gives in both cases

\[
\frac\Lambda W=\sqrt{\frac{\pi k}{8}}+O(1).         \tag{7.3}
\]

Taking `ceil(Lambda/W)` as a feasible value in the definition of `d` shows
`d=O(sqrt(k))` and `d <= Lambda/W+1`.  Conversely,

\[
\Lambda\le dW+\binom{d+1}{2},
\]

and `binom(d+1,2)/W=O(k/W)=o(1)`, so
`d >= Lambda/W-o(1)`.  Combining this with (7.3) proves

\[
                    d(k)=\sqrt{\pi k/8}+O(1).
\]

## 8. Coordinate deletion and top-bit splicing

### Coordinate deletion

Fix `Q\subseteq[k]` and delete every letter meeting `Q`.  If
`\varnothing\ne S\subseteq[k]\setminus Q`, every letter in an interval whose
union is `S` is disjoint from `Q`; all those letters survive and remain
consecutive after the global deletion.  The retained word is universal on
`[k]\setminus Q`, so

\[
\#\{i:A_i\cap Q=\varnothing\}\ge\nu(k-|Q|).
\]

Sum over all `Q\in\binom{[k]}t` and interchange the sums.  A fixed letter
`A_i` is disjoint from exactly `binom(k-|A_i|,t)` choices of `Q`.  Therefore

\[
\sum_i\binom{k-|A_i|}{t}\ge\binom kt\nu(k-t).
\]

### Top-bit splice

For `k >= 2`, let `X=(x_1,...,x_n)` be universal on `[k-1]`, and let `b` be
the new singleton coordinate.  The word

\[
x_1,\ldots,x_n,\{b\},
x_1\cup\{b\},\ldots,x_{n-1}\cup\{b\}               \tag{8.1}
\]

has length `2n`.  Old targets occur in the first block and `{b}` occurs in
the central cell.  For `S\cup\{b\}` with nonempty old `S`, choose an
`X`-witness `[i,j]`.  If `j<n`, its marked copy in the last block is a
witness; if `j=n`, the original witness followed by the central singleton
is a witness.  Hence

\[
                         \nu(k)\le2\nu(k-1).
\]

## 9. Necessary finite-certificate appendix

The following exact data must occur in the same Markdown file if its finite
claims are to be self-contained:

1. the actual words proving the upper bounds for `1 <= k <= 16`;
2. their dimensions and lengths; and
3. an exact verifier whose correctness is proved inline.

No separate `k=17` payload is needed.  The retained length-25,746 word is
exactly (8.1) applied to the length-12,873 `k=16` word.  Thus the embedded
`k=16` certificate plus the top-bit proof supplies the `k=17` upper bound.

### Lossless compact representation

For dimension `k`, let

\[
w_k=\min\{w:36^w\ge2^k\}.
\]

Use digits `0123456789abcdefghijklmnopqrstuvwxyz`.  Encode each mask as its
base-36 expansion padded on the left to exactly `w_k` digits, concatenate the
tokens, and insert arbitrary whitespace for line wrapping.  Removing
whitespace and splitting into `w_k`-character chunks recovers the word
uniquely.  This is an explicit lossless encoding, unlike a hash.  The full
`k=1,...,16` payload occupies 91,488 non-whitespace characters (about 92.6 KB
after wrapping), so embedding it does not restore the old handoff's size.

### Exact verifier and its proof

For a decoded word `a_1,...,a_n`, define

\[
E_0=\varnothing,
\qquad
E_j=\{a_j\}\cup\{x\cup a_j:x\in E_{j-1}\}.          \tag{9.1}
\]

Induction on `j` proves that `E_j` is exactly the set of unions of nonempty
intervals ending at position `j`: an interval either starts at `j`, or is an
interval ending at `j-1` extended by `a_j`.  Hence the word is universal iff

\[
\bigcup_{j=1}^nE_j=2^{[k]}\setminus\{\varnothing\}.  \tag{9.2}
\]

The following reference code implements only (9.1)--(9.2):

```python
def check(k, n, w, payload):
    s = ''.join(payload.split())
    assert len(s) == n*w
    a = [int(s[i:i+w], 36) for i in range(0, len(s), w)]
    assert len(a) == n and all(0 < x < (1 << k) for x in a)
    ending = set()
    seen = set()
    for x in a:
        ending = {x} | {y | x for y in ending}
        seen |= ending
    assert seen == set(range(1, 1 << k))
```

The data appendix should invoke this check on every displayed payload.  With
the data embedded, the finite upper bounds are finitely checkable entirely
from the handoff.  The general lower theorem and the following arithmetic
table then prove optimality.

| `k` | `r` | `W` | `Lambda` | `d` | `B` |
|---:|---:|---:|---:|---:|---:|
| 0 | -- | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 2 | 1 | 2 | 0 | 0 | 2 |
| 3 | 2 | 3 | 3 | 1 | 4 |
| 4 | 2 | 6 | 4 | 1 | 7 |
| 5 | 3 | 10 | 15 | 2 | 12 |
| 6 | 3 | 20 | 21 | 1 | 21 |
| 7 | 4 | 35 | 63 | 2 | 37 |
| 8 | 4 | 70 | 92 | 2 | 72 |
| 9 | 5 | 126 | 255 | 2 | 128 |
| 10 | 5 | 252 | 385 | 2 | 254 |
| 11 | 6 | 462 | 1023 | 3 | 465 |
| 12 | 6 | 924 | 1585 | 2 | 926 |
| 13 | 7 | 1716 | 4095 | 3 | 1719 |
| 14 | 7 | 3432 | 6475 | 2 | 3434 |
| 15 | 8 | 6435 | 16383 | 3 | 6438 |
| 16 | 8 | 12870 | 26332 | 3 | 12873 |
| 17 | 9 | 24310 | 65535 | 3 | 24313 |

For every row with `d>0`, minimality is the directly checked pair

\[
(d-1)W+\binom d2<\Lambda
 \le dW+\binom{d+1}2;
\]

the rows with `d=0` have `Lambda=0`.

If the word payloads are not embedded, the only rigorous alternative is to
demote the finite upper statements to **externally certified** and to say
explicitly that they are not proved within the handoff.  A hash-only appendix
does not meet the strict self-containment requirement.

## 10. Self-contained `sqrt(2)` construction

Split `[k]=P\mathbin{\dot\cup}Q`, where `|P|=p`, `|Q|=q`, `p,q\ge1`, and
fix `z\in P`.
We first prove the only lattice fact used below.  The Boolean lattice on a
`t`-set partitions into saturated symmetric chains.  Inductively, on adding
a coordinate `x`, replace

\[
C_0\subset\cdots\subset C_s
\]

by the long chain

\[
C_0\subset\cdots\subset C_s\subset C_s\cup\{x\}
\]

and, when nonempty, the short chain

\[
C_0\cup\{x\}\subset\cdots\subset C_{s-1}\cup\{x\}.
\]

The two children partition the old chain times `{0,1}` and remain saturated
and symmetric.  Every symmetric chain meets rank `floor(t/2)` exactly once,
so the number of chains is `W(t)`.

For a saturated chain `C=(C_0\subset\cdots\subset C_s)` in universe `U`, define
the bridge word

\[
\beta_U(C)=
(C_0,C_1\setminus C_0,\ldots,C_s\setminus C_{s-1},U\setminus C_s),
\]

omitting empty blocks.  Its blocks are nonempty and disjoint.  Its prefix
unions, allowing the empty prefix, include every `C_i`; its suffix unions,
allowing the empty suffix, include every `U\setminus C_i`.

Take an SCD of `2^{P\setminus\{z\}}` and append `C_s\cup\{z\}` to every
chain.  Call the resulting lifted family `\mathcal C`; it has `a=W(p-1)`
chains, and every subset of `P\setminus\{z\}` occurs in exactly one of them.
Take an SCD `\mathcal D` of `2^Q`, of size `b=W(q)`.

Form the directed complete bipartite graph on
`\mathcal C\mathbin{\dot\cup}\mathcal D`, with both directed arcs between
each pair.  It
is strongly connected and every vertex has equal indegree and outdegree, so
it has an Euler circuit

\[
v_0,v_1,\ldots,v_{2ab}=v_0.
\]

Indeed, follow unused outgoing arcs until stuck; equality of indegree and
outdegree forces the resulting trail to close at its starting vertex.  If an
arc remains, strong connectivity supplies a vertex of the current trail from
which another unused closed trail can be started; splice it into the first
trail and iterate.

Choose `v_0\in\mathcal D` and concatenate the bridge word of every visited
vertex, including both endpoint visits.

Let a nonempty target be `S=X\cup Y`, with `X\subseteq P`, `Y\subseteq Q`.
If `z\in X`, the set `P\setminus X\subseteq P\setminus\{z\}` lies on a
unique lifted chain `C`, while `Y` lies on a unique `D\in\mathcal D`.  At the
circuit's occurrence of the arc `C -> D`, a suffix of `beta_P(C)` has union
`X` and the following prefix of `beta_Q(D)` has union `Y`.  If `z\notin X`,
use the unique chains containing `Q\setminus Y` and `X` at the occurrence of
the reverse arc `D -> C`.  One half may be empty, but not both because `S` is
nonempty.  The resulting nonempty interval has union exactly `S`, proving
universality.

It remains to count.  In an SCD of `2^t`, the sum of the bridge lengths is

\[
                         2^t+W(t)-2:                  \tag{10.1}
\]

the unique chain through the empty set contributes its number of members
minus one, and every other chain contributes its number of members plus one.
The lifted left chains have total membership `2^(p-1)+a`, so their total
bridge length is `2^(p-1)+2a-2`; the right total is `2^q+b-2`.  In the first
`2ab` visits of the Euler circuit, every left vertex occurs as a tail `b`
times and every right vertex `a` times.  The repeated endpoint bridge has
length at most `q+2`.  The constructed word therefore has length at most

\[
b(2^{p-1}+2a-2)+a(2^q+b-2)+q+2.                    \tag{10.2}
\]

Choose `p=ceil(k/2)` and `q=floor(k/2)`.  From the internally proved (6.6),

\[
b2^{p-1}+a2^q=(\sqrt2+o(1))W(k),
\]

whereas

\[
ab=O(2^k/k)=o(W(k)),\qquad q=o(W(k)).
\]

Equation (10.2) consequently proves, without any external construction file,

\[
                  \nu(k)\le(\sqrt2+o(1))W(k).
\]
