# Independent audit of the three-palette-disjoint Catalan collar bank

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, enumeration, or solver  
**Audited source:**
`MATH_THEOREM_THREE_PALETTE_DISJOINT_CATALAN_COLLAR_BANK_20260805.md`,
current input SHA-256
`3484e5074ae1a40e147a7073f307a37c683143fc0736d31068ed3a37d2c6edd6`
(the earlier 382-line draft had SHA
`805504df0360ce3cce7565ab41f04e2cc7d99e0ca057e20d7dea0a3cad9740e2`)  
**Verdict:** **GO.**  The Johnson edge-loss constants, the two endpoint
constructions, all three palette-disjointness claims, the exact-size
thinning bounds, the new two-per-small-star geometry, and both simultaneous
union bounds are valid as stated.  No mathematical correction is required.

## 1. Resource ledger

Put `s=h+1`.  One generalized collar has owner sequence

\[
                     P,M_0,M_1,\ldots,M_h,N.          \tag{1.1}
\]

It therefore uses

\[
                    h+3=s+2                           \tag{1.2}
\]

owners and has `h+2=s+1` Johnson transitions.  Its lower colours are all
different, so it uses `s+1` lower resources.  The left seam repeats the
first of the `h` internal upper colours, while the right seam supplies one
new upper colour, so it uses

\[
                    h+1=s                             \tag{1.3}
\]

distinct upper resources.  These are exactly the three coefficients used
in the deletion ledger.

For the required bank size,

\[
 {1\over r+1}{2r\choose r}=\operatorname{Cat}_r,
 \qquad
 {1\over2r-1}{2r-1\choose r}
   ={1\over r}{2r-2\choose r-1}=\operatorname{Cat}_{r-1}.             \tag{1.4}
\]

Thus `c` and `b=c-1` are integers in both parities and have the claimed
component-joining interpretation.

## 2. Johnson colour classes and edge losses

The owner degree in `J(k,r)` is

\[
                         \Delta=rq.                   \tag{2.1}
\]

A fixed lower colour has `q+1` owner extensions, and every pair of those
extensions is a Johnson edge with that intersection.  Its edge class has
size `binom(q+1,2)`.  A fixed upper colour has `r+1` owner facets, giving
`binom(r+1,2)` edges.  These counts are exact.

After `t<W/(64s)` collars, divide the three union-bound losses by the
initial edge count `W Delta/2`.  They are at most

\[
 A_O={s+2\over32s},
 \qquad
 A_L={s+1\over64s}{q+1\over r},
 \qquad
 A_U={1\over64}{r+1\over q}.                         \tag{2.2}
\]

For `s>=3`, `r>=16s`, and `q in {r,r-1}`, the worst endpoint values give

\[
 A_O+A_L+A_U<0.09<\frac12.                           \tag{2.3}
\]

For example, the individual uniform bounds at the smallest possible
`r=48,s=3` are below `0.0521`, `0.0213`, and `0.0163`.  Hence the residual
graph actually retains more than

\[
                         0.455\,W\Delta,             \tag{2.4}
\]

far stronger than the `W Delta/4` used in the proof.

The peeling step is also in the correct direction.  If deletion of every
vertex of current degree less than `Delta/4` removed all at most `W`
vertices, charge each edge at its first deleted endpoint.  Fewer than
`W Delta/4` edges would be charged, contradicting (2.4).  Thus a nonempty
subgraph of minimum degree at least `Delta/4` survives.

## 3. Dense-core collar and endpoint audit

Fix `M_0` in a residual minimum-degree core `H`.  Partition its incident
edges by the entering coordinate.  There are `q` classes, so one entering
coordinate `rho_1` has a deleted-label class `S subseteq M_0` of size at
least

\[
                       {|E_H(M_0)|\over q}\ge {r\over4}.              \tag{3.1}
\]

After `j-1` exchanges, forbidding removal of an already inserted `rho`
costs at most `(j-1)q` edges, and forbidding insertion of an already
deleted `lambda` costs at most `(j-1)r` edges.  Hence the total forbidden
degree is less than or equal to

\[
                         (j-1)(r+q).                  \tag{3.2}
\]

The stated hypothesis implies the strict aperture

\[
 {rq\over4}>h(r+q).                                  \tag{3.3}
\]

Indeed it is enough to use `q>=r-1` and `r>=16(h+1)`.  Thus every one of
the `h` geodesic exchanges exists in `H`.  An allowed edge necessarily
removes a fresh original `M_0` coordinate and inserts a fresh coordinate
outside `M_0`, so the displayed geodesic form follows without an extra
assumption.

### 3.1 Left endpoint

After the geodesic is fixed, at most `h` members of `S` have been deleted.
Since `|S|>=r/4>h`, there is

\[
                         q_-\in S\cap Q.              \tag{3.4}
\]

Consequently

\[
                         P=M_0-q_-+\rho_1             \tag{3.5}
\]

is a vertex of `H`, and `PM_0` is an edge of `H` by the definition of
`S`.  It is distinct from every stem owner because it omits `q_-`, which
every stem owner contains.  Its literal predecessor letter is

\[
                         (Q-q_-)\cup\{\rho_1\},       \tag{3.6}
\]

which is nonempty and, followed by the `lambda` rail, produces `P`.

### 3.2 Right endpoint

At `M_h`, forbid removing an inserted `rho` or reinserting a deleted
`lambda`.  The same bound (3.3) leaves an edge

\[
                  M_hN,
 \qquad N=M_h-q_++z,                                 \tag{3.7}
\]

with `q_+ in Q` and

\[
                  z\notin M_0\cup\{\rho_1,\ldots,\rho_h\}.           \tag{3.8}
\]

Thus `z` is fresh, in particular `z notin M_h` and `z!=lambda_h`, exactly
the generalized right-endpoint hypotheses.  The literal successor letter
is `(Q-q_+) union {z}`, which is again nonempty and, after the `rho` rail,
produces `N`.

The endpoint `N` is distinct from every stem owner because it omits
`q_+`.  It is distinct from `P`: `P` contains the complete lambda rail,
whereas `N` contains the complete rho rail and no lambda coordinate.

### 3.3 Palette distinctness

Every internal lower colour contains all of `Q`.  The left seam lower
colour omits `q_-` and contains the complete lambda rail; the right seam
lower colour omits `q_+` and contains the complete rho rail.  Hence the
two seam colours are different from all internal colours and from each
other, even if `q_-=q_+`.

The internal upper colours are distinguished by the rho-prefix length.
The left seam repeats exactly the first internal upper colour.  The right
upper colour contains the fresh `z`; the only internal upper colour with
the full rho rail contains `lambda_h` instead.  Therefore it is new.

Finally every transition just audited is an edge of `H`.  Since `H` was
obtained after deleting every edge with a previously used lower or upper
colour, this proves cross-collar disjointness on both colour shores as well
as on the owner shore.

## 4. Large bank and exact thinning

Lemma 1.1 applies before every choice `t<M`, where

\[
                         M=\left\lfloor{W\over64s}\right\rfloor.      \tag{4.1}
\]

Thus the greedy induction genuinely produces `M` collars, not merely
`M-1`.

When `W/(64s)>=2`,

\[
                 {W\over128s}\le M\le {W\over64s}.                   \tag{4.2}
\]

Let `D_k=r+1` in the even case and `D_k=2r-1` in the odd case.  Since
`c=W/D_k`, `b=c-1>=c/2` for `c>=2`, and `t=s+2<=2s`, uniform sampling of
exactly `b` collars has

\[
 {p\over t}={b/M\over s+2}\ge {16\over D_k},
 \qquad
 p< {128s\over D_k}.                                 \tag{4.3}
\]

The asymptotic theorem is well defined because

\[
                         {M\over b}=\Theta(r/s)\to\infty.             \tag{4.4}
\]

The block weights in one owner star satisfy

\[
 0\le w_i\le t,
 \qquad \sum_iw_i\le|\mathcal O(S)|,
 \qquad \sum_iw_i^2\le t|\mathcal O(S)|.            \tag{4.5}
\]

Hoeffding comparison followed by Bernstein therefore gives exactly

\[
 \Pr\{X_S>2p|\mathcal O(S)|\}
 \le
 \exp\left(-{3p|\mathcal O(S)|\over8t}\right).       \tag{4.6}
\]

The smallest tested star is

\[
                         L_*={k-r+h+1\choose h+1}.    \tag{4.7}
\]

At deadline scale, (4.3) makes the exponent at least `6L_*/D_k`, while
there are at most `2^k` tests.  Since

\[
 \log L_*=\Theta(\sqrt r\log r),
 \qquad {L_*\over D_k}\gg r,                         \tag{4.8}
\]

the union bound has superpolynomial room.  The selected exact-size bank
satisfies

\[
 |V_B\cap\mathcal O(S)|
   \le2p|\mathcal O(S)|
   <{256s\over D_k}|\mathcal O(S)|,                  \tag{4.9}
\]

which is the claimed spread constant.

## 5. Small-star extension in the current source

The expanded source adds a uniform `O(r/log r)` load bound for rank-`(r-1)`
owner stars and for lower facets inside one owner.  Its local constant two
is exact enough.

For central owners,

\[
                         |M_i\cap M_j|=r-|i-j|.       \tag{5.1}
\]

Hence a fixed rank-`(r-1)` set lies in at most two consecutive central
owners.  The left endpoint has rank-`(r-1)` intersection only with `M_0`
and `M_1`, and

\[
                         |P\cap M_0\cap M_1|=r-2.    \tag{5.2}
\]

Thus it cannot create a third owner above the same lower set.  The right
endpoint has rank-`(r-1)` intersection only with `M_h`; its intersection
with `M_(h-1)` already has rank `r-2`.  The two endpoints have no common
rank-`(r-1)` subset for `h>=2`.  This proves the first local bound two.

For internal lower colours `I_j`,

\[
                         |I_i\cup I_j|=r+j-i-1
                         \qquad(i<j).                \tag{5.3}
\]

So a rank-`r` owner contains at most two consecutive internal colours.
The left seam lower colour can coexist only with `I_1`, the right seam
only with `I_h`, and the two seam colours cannot coexist.  Therefore a
fixed owner contains at most two lower resources of one collar.

Across the large bank, owner blocks are disjoint.  A fixed lower colour
has only `q+1` containing owners, so at most `q+1` blocks can meet its
owner star.  Lower-resource blocks are also disjoint, and one owner has
only `r` lower facets, so at most `r` blocks can meet that facet star.
For either family the selected-block count `Z` has hypergeometric mean

\[
                         \mu=O(pr)=O(s)=O(\sqrt r).   \tag{5.4}
\]

At `t=K r/log r`, the standard without-replacement binomial tail gives

\[
 \Pr\{Z\ge t\}
   \le\left({e\mu\over t}\right)^t,
 \qquad
 t\log{t\over e\mu}
   =\left({K\over2}+o(1)\right)r.                   \tag{5.5}
\]

There are fewer than `2W<2*4^r` such tests.  Any fixed
`K>4 log 4` is more than sufficient for their union-bound failure
probability to tend to zero.  Since the large-star failure probability in
(4.6) also tends to zero, the two good events have a nonempty intersection
in the same exact-size sample.  Multiplying the selected-block bound by
the local contribution two proves the claimed `O(r/log r)` loads.

## 6. Exact corrections and scope

No proof correction is required.  The duplicate sentence present in the
earlier 382-line draft has already been removed in the current source.

The theorem remains prospective.  It proves a three-palette-disjoint,
low-star-spread collar bank.  It does not prove a complementary ordered
four-transversal, a resident literal trace realization, lower palettes at
depth greater than one, arbitrary-width upper witnesses, or a common-cap
compiler.
