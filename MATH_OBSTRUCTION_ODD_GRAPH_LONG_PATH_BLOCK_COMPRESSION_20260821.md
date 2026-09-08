# The rainbow-hole gate for long odd-graph path compression

**Status (2026-08-21).**  This note gives an exact obstruction to
compressing punctured wreaths by arbitrary nonbacktracking paths in the
odd graph.  Such a path extends to a wreath if and only if its natural
edge holes are all distinct.  Nonbacktracking alone first fails at four
edges.  The hypergraph of extendible `s`-vertex paths has an exact
degree/codegree profile; when `s=Theta(r)`, which is the range needed to
make the compressed wreath rank fixed, its rank-scaled codegree is bounded
away from zero.  Thus the ordinary fixed-rank nibble can construct
fixed-length path factors, but it does not noncircularly supply the long
path factor needed for fixed-rank wreath compression.

This is not a proof that no specially colored Hamilton cycle or explicit
long rainbow-path factor exists.  It isolates that object as an additional
gate.  It also records the exact expectation identities after restriction
to a random invariant path factor; symmetry alone does not control the
survival probabilities in those identities.

## 1. The hole coloring and the exact extension criterion

Put
\[
        b=2r+1,\qquad G=KG(b,r),\qquad
        N=\binom br .                                      \tag{1.1}
\]
For an edge `XY` of `G`, write
\[
        \chi(XY)=[b]\setminus(X\cup Y)                     \tag{1.2}
\]
for its unique **hole**.  This is a proper edge coloring at every
vertex: the `r+1` edges incident with an `r`-set have the `r+1` elements
of its complement as their distinct colors.

Let
\[
        X_0,X_1,\ldots,X_\ell                              \tag{1.3}
\]
be a nonbacktracking path, and put
`h_i=chi(X_(i-1)X_i)` for `1<=i<=ell`.  Consecutive holes obey
\[
 X_{i+1}=(X_{i-1}\setminus\{h_{i+1}\})\cup\{h_i\},
 \qquad h_{i+1}\in X_{i-1}.                                \tag{1.4}
\]
Indeed, the complement of `X_i` is `X_(i-1) union {h_i}`;
nonbacktracking excludes deleting `h_i` again.

### Theorem 1.1 (rainbow-hole extension criterion)

For `1<=ell<=2r`, the path (1.3) occurs consecutively in the window
cycle of a wreath if and only if
\[
                    h_1,\ldots,h_\ell
             \quad\hbox{are pairwise distinct}.             \tag{1.5}
\]
In particular this criterion applies throughout the proposed range
`ell<=r`.

If (1.5) holds, set
\[
 a=\left\lfloor{\ell\over2}\right\rfloor,
 \qquad c=\left\lfloor{\ell-1\over2}\right\rfloor .        \tag{1.6}
\]
The number of unoriented wreaths extending the **ordered** path at a
fixed consecutive location is exactly
\[
                         (r-a)!(r-c)!.                       \tag{1.7}
\]

#### Proof

In a wreath with cyclic order `C=(c_0,...,c_(b-1))`, let
`W_i={c_i,...,c_(i+r-1)}`.  Two of these windows are disjoint exactly
when their start indices differ by `r` or `r+1`.  Hence their induced
odd-graph cycle is
\[
              V_t=W_{tr},\qquad t\in\mathbb Z_b,             \tag{1.8}
\]
and the hole of `V_(t-1)V_t` is `c_((t-1)r-1)`.  These `b`
edge holes are all distinct, proving necessity.

Conversely put `A=X_0`, `B=X_1`, and `h_1=z`.  Then
`[b]=A disjoint-union B disjoint-union {z}`.  From (1.4) and
distinctness, the even holes `h_2,h_4,...` are distinct elements of
`A`, while `h_3,h_5,...` are distinct elements of `B`.  Complete them,
in arbitrary orders, so that
\[
 \{h_2,h_4,\ldots,h_{2r}\}=A,
 \qquad
 \{h_3,h_5,\ldots,h_{2r+1}\}=B.                            \tag{1.9}
\]
There are exactly `(r-a)!(r-c)!` completions.  Starting with
`V_0=A,V_1=B`, recurrence (1.4) now gives a cycle of `b` distinct
`r`-sets and returns to `V_0`.

Define a cyclic coordinate order (with the `c`-subscript read modulo
`b`) by
\[
             c_{(t-1)r-1}=h_t\qquad(1\le t\le b).            \tag{1.10}
\]
Multiplication by `r` is invertible modulo `b`.  The even holes in
(1.9) give `W_0=A`, the odd holes other than `h_1` give `W_r=B`, and
the window cycle in (1.8) obeys the same recurrence (1.4).  It is
therefore the completed cycle.  Reversing the completed coordinate
order reverses the prescribed path, so an ordered path fixes the choice
of direction and causes no additional factor two.  This proves
(1.7).  \(\square\)

### Corollary 1.2 (nonbacktracking is insufficient)

For every `r>=4`, choose a partition
\[
 [b]=A\mathbin{\dot\cup}B\mathbin{\dot\cup}\{z\},
 \qquad |A|=|B|=r,
\]
and elements `a in A`, `d in B`.  Then
\[
 \begin{split}
 X_0&=A,\qquad X_1=B,\\
 X_2&=A-\{a\}+\{z\},\\
 X_3&=B-\{d\}+\{a\},\\
 X_4&=A-\{a\}+\{d\}                                      \tag{1.11}
 \end{split}
\]
is a nonbacktracking odd-graph path of length `4<=r`, but its holes are
\[
                         z,a,d,z.                            \tag{1.12}
\]
It does not extend to a wreath.  Thus an ordinary Hamilton path or cycle
cannot be cut into long admissible blocks merely by invoking
nonbacktracking.

## 2. The admissible-path factor has a scaled-codegree barrier

For `2<=s<=r+1`, let `A_(r,s)` be the `s`-uniform hypergraph on
`V(G)` whose hyperedges are the vertex sets of the rainbow-hole paths
with `s` vertices.  Such a set induces a path in `G`, so its order is
unique up to reversal.  Put
\[
 \alpha=\left\lfloor{s-1\over2}\right\rfloor,
 \qquad
 \beta =\left\lfloor{s-2\over2}\right\rfloor,
 \qquad
 F_{r,s}=(r)_\alpha(r)_\beta,                               \tag{2.1}
\]
where `(r)_j=r!/(r-j)!`.

### Theorem 2.1 (exact path-factor profile)

The number of hyperedges of `A_(r,s)` is
\[
             Q_{r,s}={N(r+1)F_{r,s}\over2}.                 \tag{2.2}
\]
It is regular of degree
\[
             D^{\rm path}_{r,s}
               ={s(r+1)F_{r,s}\over2},                     \tag{2.3}
\]
and its maximum pair codegree is attained by an edge of `G` and equals
\[
             C^{\rm path}_{r,s}=(s-1)F_{r,s}.               \tag{2.4}
\]
Consequently
\[
 {C^{\rm path}_{r,s}\over D^{\rm path}_{r,s}}
      ={2(s-1)\over s(r+1)},
 \qquad
 {sC^{\rm path}_{r,s}\over D^{\rm path}_{r,s}}
      ={2(s-1)\over r+1}.                                  \tag{2.5}
\]

More explicitly, if two targets occur at distance `t` along such a
path, put
\[
 q_t=\begin{cases}
       r-t/2,&t\text{ even},\\
       (t-1)/2,&t\text{ odd}.
     \end{cases}                                            \tag{2.6}
\]
Their codegree is
\[
 L_{r,s,t}=
 { (r+1)F_{r,s}(s-t)
   \over
   \binom r{q_t}\binom{r+1}{r-q_t}},
 \qquad 1\le t\le s-1.                                    \tag{2.7}
\]
Pairs of other intersection types have codegree zero.

#### Proof

Choose the oriented first edge in `N(r+1)` ways.  After its hole, the
new distinct even holes may be chosen in `(r)_alpha` ways and the new
distinct odd holes in `(r)_beta` ways.  Reversal identifies the two
orientations, proving (2.2).  Coordinate transitivity and incidence
counting give (2.3).

At distance `t=2j`, the two targets intersect in `r-j` coordinates; at
distance `t=2j+1`, they intersect in `j` coordinates.  Since `t<=r`,
these intersection sizes determine `t`.  The number of unordered target
pairs with intersection `q_t` is
\[
 {N\over2}\binom r{q_t}\binom{r+1}{r-q_t}.                  \tag{2.8}
\]
Every path contains `s-t` pairs at distance `t`.  Double counting gives
(2.7).  At `t=1`, its denominator is `r+1`, giving (2.4).  For `t>=2`,
the denominator in (2.7) is at least `r(r+1)`, so these codegrees are
strictly smaller.  \(\square\)

For every fixed `s`, (2.5) and the standard fixed-uniformity nibble give
a matching in `A_(r,s)` covering `N-o(N)` targets.  This supplies a
near-perfect factor by fixed-length admissible paths.  It does not supply
the desired long factor.  If the compressed wreath rank
\[
                         k={2r\over s}                        \tag{2.9}
\]
is fixed, then `s=Theta(r)` and
\[
 {sC^{\rm path}_{r,s}\over D^{\rm path}_{r,s}}
                         ={4\over k}+o(1),                   \tag{2.10}
\]
not `o(1)`.  Thus the usual growing-rank low-codegree checkpoint for
constructing the factor is precisely unavailable in the range which
makes the next auxiliary rank fixed.  This does not rule out a special
Hamilton construction; it shows that the proposed hierarchy has not
removed the growing-rank gate.

## 3. What an ordinary Hamilton cycle does and does not give

Assume a Hamilton path or cycle of `G` is available.  Cutting it into
consecutive `s`-vertex pieces gives a path factor leaving fewer than `s`
targets.  By Theorem 1.1, it gives the required admissible factor if and
only if the `s-1` edge holes inside every retained piece are distinct.

For `s<=4` this is automatic: `h_1` is outside `X_0 union X_1`, while
`h_2` lies in `X_0` and `h_3` lies in `X_1`.  Corollary 1.2 shows that it
is false for arbitrary nonbacktracking pieces once `s=5`.  Ordinary
Hamiltonicity therefore gives only constant-size compression for free.
For unbounded `s`, one needs an additional rainbow-block Hamilton theorem
or a separate long-path-factor construction.

## 4. The full block auxiliary and restriction identities

Now assume `s` divides `2r`, put `k=2r/s`, and take `k>=2`.  Delete one
window from a wreath.  The other `2r` windows form a path in `G`; split
it, from one endpoint, into `k` consecutive admissible `s`-vertex paths.
Let `J_(r,s)` be the `k`-uniform hypergraph whose vertices are admissible
`s`-paths and whose hyperedges are these block sets.

The construction is independent of which orientation of the punctured
wreath is used: reversal reverses both the block order and every block.
It is also simple.  Indeed, among all `b` windows of a wreath the
disjointness graph is exactly a `b`-cycle.  The union of the blocks
therefore induces the clean `2r`-vertex path.  Its two endpoints
intersect in `r-1` coordinates, and the missing window is the complement
of their union.  Thus the path order and missing window are recovered
uniquely; the edge holes then recover the cyclic coordinate order up to
reversal.

### Proposition 4.1 (full block degree and an exact adjacent codegree)

The block auxiliary is regular of degree
\[
 D^{\rm block}_{r,s}
   ={(b!/2)k\over Q_{r,s}}
   =k(r-\alpha)!(r-\beta)!.                                 \tag{4.1}
\]
Two block vertices which concatenate to an admissible `2s`-vertex path
have codegree
\[
 C^{\rm block,adj}_{r,s}
       =(k-1)((r-s+1)!)^2.                                  \tag{4.2}
\]

#### Proof

There are `b!/2` punctured wreaths, every block hyperedge has `k`
vertices, and coordinate permutations are transitive on admissible
blocks.  Equations (2.2) and `b!/N=r!(r+1)!` give (4.1).

Compatible adjacent block pairs are in bijection with admissible
`2s`-vertex paths.  The same first-edge count used for (2.2), now with
`2s<=2r`, gives
\[
       Q_{r,2s}={N(r+1)(r)_{s-1}^2\over2}.                  \tag{4.3}
\]
Every block hyperedge has `k-1` adjacent pairs.  Incidence counting and
coordinate transitivity give
\[
 { (b!/2)(k-1)\over Q_{r,2s}}
       =(k-1)((r-s+1)!)^2,                                  \tag{4.4}
\]
as claimed.  \(\square\)

The small full-auxiliary codegrees do not survive restriction by symmetry
alone.  To state the exact ledger, let `P_s` be a random matching in
`A_(r,s)` of fixed size `m_s`, with a coordinate-invariant law, and put
\[
 q_1={m_s\over Q_{r,s}},\qquad
 q_k=\Pr({\cal B}\subseteq P_s),                            \tag{4.5}
\]
where `B` is any block hyperedge.  The second probability is independent
of `B`.  For `H_(P_s)=J_(r,s)[P_s]`,
\[
 \begin{split}
 \mathbb E|E(H_{P_s})|&={b!\over2}q_k,\\
 \mathbb E[\deg_{H_{P_s}}(B)\mid B\in P_s]
   &=D^{\rm block}_{r,s}{q_k\over q_1}.                     \tag{4.6}
 \end{split}
\]

For a compatible pair orbit `tau`, let its full codegree be
`Lambda_tau` and put `q_(2,tau)=Pr(B,B' in P_s)`.  Unconditionally,
\[
 \mathbb E\!\left[
  {\bf1}_{\{B,B'\in P_s\}}\deg_{H_{P_s}}(B,B')\right]
       =\Lambda_\tau q_k.                                   \tag{4.7}
\]
If `q_(2,tau)>0`, the conditional expected codegree is
\[
       \Lambda_\tau {q_k\over q_{2,\tau}}.                 \tag{4.8}
\]

Thus neither a Hamilton factor nor the regular full auxiliary has, by
itself, proved a useful restricted degree/codegree profile.  One still
needs a factor `P_s` with the rainbow property and quantitative joint
containment ratios in (4.6)--(4.8).  For `s=Theta(r)`, constructing such
a factor is the new growing-rank gate rather than a consequence of the
fixed-rank wreath nibble.
