# Audit of the `B+1` near-perfect Catalan path and the one-surplus source row

Date: 2026-08-01  
Lane: Thread D / protected pivot-rich `B+1` interface  
Status: exact owner-layer equivalence and scope audit.  Two qualifications
are load-bearing: cross-packet upper colours require an explicit split, and
counting gives one **surplus/unassigned occurrence**, not by itself a
rank-nonowner occurrence.  No dimension-uniform protected extension or
physical source construction is claimed.

## 0. Verdict

Let `ML_m` have lower and owner shores

\[
 \mathcal L={[2m-1]\choose m-1},\qquad
 \mathcal O={[2m-1]\choose m},
\]

of common size `W`, and put

\[
 U={2m-1\choose m+1},\qquad C=W-U=\operatorname {Cat}_m.
\]

Fix a perfect incidence matching `M_0`.  For an incidence `e=LV` outside
`M_0`, define

\[
 \operatorname {up}(e)=M_0(L)\cup V,
 \qquad
 \lambda(e):L\longrightarrow M_0^{-1}(V).              \tag{0.1}
\]

The proposed `B+1` owner certificate is exact:

\[
 \boxed{
 |Q|=W-1,\quad Q\text{ is a matching},\quad
 \operatorname {up}(Q)=\binom{[2m-1]}{m+1},\quad
 \lambda(Q)\text{ is a spanning tree}.}                \tag{0.2}
\]

It is equivalent to one alternating Hamilton path `M_0 union Q`.  Choosing
one occurrence of every immediate-upper colour gives exactly

\[
 Q=Q_0\mathbin{\dot\cup}Q_1,\qquad
 |Q_0|=U,\qquad |Q_1|=C-1,                              \tag{0.3}
\]

where `Q_0` is an upper-exact rooted Catalan forest and `Q_1` is a tree on
its `C` contracted components.  There is no residual Hall problem, no
`1 x 1` completion, and no closure edge.

For `H` resource-disjoint pivot-rich protected paths, the alternating
second-colour edges are already independent in the two endpoint partition
matroids and the rooted graphic matroid.  Their upper colours are distinct
inside each packet, but the authoritative resource-disjointness hypothesis
does not force upper-colour distinctness **between** packets.  The exact
general certificate must therefore split this bank as

\[
             P_1=A_0\mathbin{\dot\cup}A_1,\qquad
             A_0\subseteq Q_0,\quad A_1\subseteq Q_1,   \tag{0.4}
\]

with `A_0` upper-independent and `A_1` carried by the connector tree.  If
upper-resource-disjointness is added explicitly, one may take `A_0=P_1`
and `A_1=emptyset`.  The genuine missing owner theorem is the correlated
extension of (0.4), followed by a physical directed Hamilton path on the
`C` exposed ports.

The immediate-upper conclusion is exact, but the deeper conclusion is only
internal preservation: every witness interval wholly inside a protected
path survives, while arbitrary-width ambient upper completeness is not a
consequence of (0.2).

Finally, if `B(k)=W+h`, a length-`B(k)+1` source has exactly `W+1`
length-`h+1` cells.  Counting forces `W` selected owner occurrences and one
surplus occurrence.  It does **not** force the surplus value to have rank
different from the owners.  Calling it a nonowner/task cell is correct only
after that property is supplied by the intended nonflat pivot scaffold.

## 1. Near-perfect matching is exactly a Hamilton path

### Theorem 1.1

For a matching `Q subseteq ML_m-M_0`, the following are equivalent.

1. `Q` satisfies (0.2).
2. `M_0 union Q` is a spanning alternating Hamilton path, and its turns at
   internal lower vertices cover every rank-`m+1` upper colour.

#### Proof

The union spans all `2W` incidence vertices and has

\[
                         W+(W-1)=2W-1                 \tag{1.1}
\]

edges.  Because `M_0` is perfect and `Q` is a matching, its maximum degree
is two and it has exactly one degree-one vertex on each incidence shore.

Contract every edge of `M_0`.  An edge `LV` of `Q` becomes precisely the
labelled link `L M_0^{-1}(V)`.  Thus the contracted graph is
`lambda(Q)`.  Under (0.2) it has `W` vertices, `W-1` edges, and is a forest,
so it is a spanning tree.  Moreover every contracted vertex has at most one
incoming and at most one outgoing link.  Its undirected degree is therefore
at most two.  A tree of maximum degree two is a path.  Undoing the
contractions proves the Hamilton-path assertion.

At an internal lower vertex `L`, the two adjacent owners are `M_0(L)` and
the owner endpoint `V` of its `Q` edge.  Their union is exactly
`up(LV)`, proving the turn-colour assertion.

Conversely, alternately colour the edges of an incidence Hamilton path.
Because its two endpoints lie on opposite shores, one colour class has `W`
edges and is a perfect matching; call it `M_0`.  The other has `W-1` edges
and is a matching `Q`.  Contracting `M_0` gives a spanning path, and the
turn hypothesis is precisely surjectivity of `up(Q)`.  \(\square\)

Let `a` be the unique lower vertex missed by `Q`, and let `V_*` be the
unique owner missed by `Q`.  Put `b=M_0^{-1}(V_*)`.  The directed link path
is oriented

\[
                           b\longrightarrow\cdots\longrightarrow a.
                                                               \tag{1.2}
\]

The incidence endpoints are `V_*` and `a`.  In the owner projection, every
lower colour except `a` is used exactly once as a transition.  Hence `a`,
not an unspecified colour, is the unique immediate-lower boundary debt.

## 2. Exact Catalan decomposition

### Theorem 2.1

Condition (0.2) is equivalent to disjoint matchings `Q_0,Q_1` whose union
is a matching and such that

1. `up:Q_0 -> binom([2m-1],m+1)` is a bijection;
2. `lambda(Q_0)` is a forest; and
3. after contracting all components of `lambda(Q_0)`, the links of `Q_1`
   form a spanning tree.

In that case the sizes are forced by (0.3).

#### Proof

Assume (0.2).  Select one carrying edge of `Q` for every upper colour and
call the selected set `Q_0`.  It has `U` edges and its link graph is a
subforest of `lambda(Q)`.  On the fixed set of `W` link vertices it
therefore has

\[
                              W-U=C                    \tag{2.1}
\]

components, isolated vertices included.  The remainder `Q_1=Q-Q_0` has

\[
                     (W-1)-U=C-1                       \tag{2.2}
\]

edges.  Since the full link graph is a spanning tree, the contracted
`Q_1` links form a spanning tree on the `C` old components.

Conversely, a forest together with a tree on its contracted components is
a spanning tree.  Its edge count is `U+C-1=W-1`, its incidence edges form a
matching by hypothesis, and `Q_0` already witnesses every upper colour.
Thus (0.2) holds.  \(\square\)

Because each component of `lambda(Q_0)` is a directed path with one unused
tail and one unused head, endpoint matching makes the contracted tree a
directed partial permutation.  A connected acyclic partial permutation is
a directed Hamilton path on the `C` components.  Its two unused ports are
the final physical endpoints; they are not a residual matching instance.

## 3. Protected pivot-rich paths

Let one protected owner path be

\[
 V_0,V_1,\ldots,V_\ell,\qquad \ell=3h,
\]

and let `L_i=V_i\cap V_{i+1}`.  Its incidence lift alternates as

\[
 V_0,L_0,V_1,L_1,\ldots,L_{\ell-1},V_\ell.             \tag{3.1}
\]

Choose the perfect-matching phase so that `M_0(L_i)=V_i`; the reversed
phase is symmetric.  The protected second-colour incidence
`e_i=L_iV_(i+1)` then satisfies

\[
 \operatorname {up}(e_i)=V_i\cup V_{i+1},              \tag{3.2}
\]

and, for `i<\ell-1`,

\[
 \lambda(e_i)=L_i\longrightarrow L_{i+1}.              \tag{3.3}
\]

The last head is the distinct external lower preimage of `V_ell` under
`M_0`.  Thus the protected second-colour bank is a directed path.  For `H`
resource-disjoint copies these paths are vertex-disjoint.  Formula (3.2)
and the double-`q1` packet theorem make their upper labels distinct within
each path; cross-packet upper collisions are not excluded.

Consequently the whole bank is independent in:

* the lower-tail partition matroid;
* the owner-head partition matroid;
* the cycle matroid of the labelled rooted links.

Choose `A_0 subseteq P_1` upper-independent, normally one protected edge
for every upper colour occurring in `P_1`, and put `A_1=P_1-A_0`.  Then the
exact certificate requires a rooted Catalan forest `Q_0` which contains
`A_0` and avoids both incidence shores used by `A_1`, followed by a
connector tree `Q_1` containing `A_1`.  Equivalently, the four matroid rows
apply to the `Q_0` extension only after the `A_1` endpoint exclusions are
contracted/deleted.  The final directed port Hamilton path must contain the
forced arcs induced by `A_1`.

This split is lossless.  Given any protected solution `Q`, choose the
`Q_0` representative of each protected upper colour from one protected
occurrence when possible.  Those chosen protected edges are `A_0`; all
remaining protected edges lie in `A_1=Q_1`.  Conversely a certificate with
(0.4) contains every protected incidence.  A forced `A_1` loop or cycle
after contracting `Q_0` is therefore an exact obstruction, not a reason to
discard the split.

The small protected-factor theorem only certifies that a compatible
alternating phase `M_0` can occur in some factor when `6Hh<=m-2`.  That
auxiliary factor neither supplies the common extension nor the port
Hamilton path.

### 3.1 The upper/root-tail projection does extend

Two of the four extension rows above admit an unconditional projection.  If
`mathcal X` is a nonempty family of rank-`m+1` sets on `[2m-1]`, then its
rank-`m` lower shadow satisfies

\[
                         |\partial\mathcal X|
                           \ge |\mathcal X|+m.           \tag{3.4}
\]

This is the central one-step Kruskal--Katona surplus.  For completeness, put
`k=m+1` and `x=|mathcal X|`.  Since
`x<=binom(2k-3,k)`, write the first step of its canonical expansion as

\[
                 x={s\choose k}+b,qquad
                 k\le s\le2k-3,qquad
                 0\le b<{s\choose k-1}.                \tag{3.4a}
\]

The remainder rank-`k-1` colex family is supported on at most `s` points.
Because `s<=2k-3`, its lower shadow has size at least `b`.  Therefore the
Kruskal--Katona formula gives

\[
 \partial_k(x)-x
 \ge {s\choose k-1}-{s\choose k}.                       \tag{3.4b}
\]

The right side is at least `k-1=m`: it equals `k-1` at `s=k`, and its
increment from `s` to `s+1` is

\[
                    {s\choose k-2}-{s\choose k-1}\ge0
                    \qquad(s\le2k-3).                   \tag{3.4c}
\]

This proves (3.4), with equality at `x=1`.

Consequently, any `t<=m` prescribed distinct containment tickets

\[
       (R,T),\qquad |R|=m+1,\quad |T|=m,\quad T\subset R,              \tag{3.5}
\]

with distinct `R` and distinct `T`, extend to an injection assigning every
rank-`m+1` set `R` a distinct rank-`m` subset `T(R)`.  Indeed, delete the
`t` prescribed vertices on both shores.  For any remaining nonempty upper
family `X`, (3.4) gives

\[
              |N(X)\setminus T(\mathcal P)|
                    \ge |X|+m-t\ge |X|,                \tag{3.6}
\]

so Hall applies.

Relative to `M_0`, a ticket `T subset R=T+{b}` lifts uniquely as follows.
Write `L=M_0^{-1}(T)` and `T=L+{a}`; then the incidence

\[
                         L\ --\ (L+\{b\})              \tag{3.7}
\]

has upper colour `R`.  Distinct `T` give distinct rooted tails `L`.
However the other owners `L+{b}` need not be distinct, and the rooted links
need not form a forest.  Thus (3.4)--(3.7) solve exactly the upper-colour
and tail rows, not head injectivity or graphic connectivity.

For the protected split (0.4), reserve all `p=|P_1|=3Hh` rooted tails used
by `P_1`: the `A_0` tails are prescribed and the `A_1` tails are forbidden
to `Q_0`.  Delete from the upper shore the colours already represented by
`A_0`, and delete all `p` reserved tails from the lower shore.  The same
Hall calculation gives

\[
                         |N(X)|-p\ge |X|+m-p\ge |X|     \tag{3.8}
\]

whenever `p<=m`.  Thus `Q_0` has an upper-exact rooted-tail semimatching
which contains `A_0` and avoids every `A_1` tail.  This applies throughout
the stronger planted-factor range `6Hh<=m-2`.

It still does not avoid the **heads** used by `A_1`, nor make the newly
chosen heads distinct among themselves, nor make the rooted links a forest.
The remaining central problem is precisely to correlate this Hall
extension with those head exclusions and one spanning link path.

## 4. Upper witnesses: what is and is not automatic

The bank `Q_0` gives one surviving occurrence of every immediate-upper
colour.  Adding the `C-1` connector edges deletes no edge of `Q_0`, and the
result is already a path, so there is neither connector damage nor a final
opening loss at depth one.

There is an exact block-local statement at arbitrary width.  If the
oriented path components of `lambda(Q_0)` project to owner blocks
`B_1,...,B_C`, then

\[
\begin{split}
 \operatorname {Cov}(B_1\cdots B_C)
  ={}&\bigcup_i\mathcal I(B_i)\\
   &{}\cup\bigcup_{i<j}
       \left\{S\cup\bigcup_{i<t<j}\operatorname {tot}(B_t)\cup P:
         S\in\mathcal S(B_i),\ P\in\mathcal P(B_j)\right\}.
                                                               \tag{4.1}
\end{split}
\]

Here `I,P,S` are the internal-, prefix-, and suffix-union decks and `tot`
is the total union.  Formula (4.1) follows by the unique first and last
blocks met by an interval.

It follows that every interval witness wholly inside a protected packet
survives literally, possibly after reversing the packet.  The connector
tree only creates the second line of (4.1); it does not prove that those
new crossing values cover every deeper upper target.  In particular,
upper-surjectivity of `up(Q)` is exactly a rank-`m+1` statement and has no
formal implication for ranks `m+2` and above.

Thus the correct all-width conclusion is

\[
 \boxed{\text{zero protected-internal damage, but no ambient
 arbitrary-width completeness theorem}.}              \tag{4.2}
\]

## 5. The `W+1` row and the surplus-cell correction

Write `B(k)=W+h`.  A source word of length `B(k)+1` has

\[
                  (W+h+1)-(h+1)+1=W+1                 \tag{5.1}
\]

length-`h+1` windows.  Owner completeness needs at least one occurrence of
each of the `W` rank-`r` owners.  Therefore the exact scalar conclusion is

\[
             W\text{ selected owner occurrences}
             +1\text{ surplus/unassigned occurrence}. \tag{5.2}
\]

Nothing in (5.1)--(5.2) forces the surplus value to have rank different
from `r`; it may a priori be a repeated owner.  The stronger description
“one nonowner task row” is valid only under the additional physical
hypothesis that the jointly designed pivot/source scaffold assigns the
surplus occurrence that prescribed nonowner value.

For a literal use of the Hamilton-path certificate, the `W` selected owner
occurrences must form one consecutive block in the order of Theorem 1.1.
Absent an explicit bypass, placing the surplus occurrence between two of
them destroys one certified adjacency.  Hence the direct architecture is

\[
                    E,O_0,\ldots,O_{W-1}
       \quad\text{or}\quad
                    O_0,\ldots,O_{W-1},E,               \tag{5.3}
\]

where `E` is the surplus occurrence.  Reversal exchanges the two forms.

The missing lower colour `a` from (1.2) is not automatically realized by
`E`.  That requires a literal erosion/compiler identity involving `E` and
the adjacent owner endpoint.  Likewise the endpoint cap, residence state,
and deeper interval unions crossing `E` are separate physical rows.

Finally, in the sharp pivot packet the `h` pre-insertion crossing windows
have values `M_j union M_(j+1)` of rank `r+1`, whereas the `h+1`
post-insertion windows are the rank-`r` owners `M_0,...,M_h`.  Hence the
intended positive construction is necessarily a jointly designed nonflat
antecedent.  It is not obtained by inserting one letter into a frozen flat
`W`-owner row.

## 6. Exact remaining theorem

The dependency-clean `B+1` target is now:

1. choose a compatible perfect `M_0` containing the first protected colour;
2. split P1 into A0 and A1 as in (0.4), and extend `A_0` to an
   upper-exact rooted Catalan forest `Q_0` avoiding the `A_1` resources;
3. connect its `C` ports by one physical directed Hamilton path `Q_1`
   containing every forced edge of `A_1`;
4. realize the resulting `W` owner order as one consecutive block of a
   `W+1`-cell nonflat source row; and
5. assign the one surplus cell so that it pays the unique lower boundary
   colour and satisfies the endpoint residence, arbitrary-width, and
   common-cap rows.

Items 1--3 are exactly the owner/lower-`q1`/immediate-upper/topology
certificate.  Items 4--5 are not consequences of it.  In particular, no
all-`k` `B(k)+1` claim follows from the Catalan path equivalence alone.
