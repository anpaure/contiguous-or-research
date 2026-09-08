# Even splice excess, the fixed-shore constant gate, and the exact two-rank carrier

Date: 2026-07-31  
Lane: independent even-lift algebra  
Status: proved source-independent splice and carrier implications; exact K16
replay.  No all-\(k\) existence theorem is claimed.

## 1. Rank-slack notation

For \(k\geq1\), put

\[
 r_k=\left\lceil\frac k2\right\rceil,
 \qquad w_k={k\choose r_k},
 \qquad \Lambda_k=\sum_{j=1}^{r_k-1}{k\choose j},                 \tag{1.1}
\]

and define

\[
 d_k=\min\left\{d\geq0:
       d w_k+{d+1\choose2}\geq\Lambda_k\right\},
 \qquad B(k)=w_k+d_k.                                             \tag{1.2}
\]

Here \(B(k)\) is the proved monotone-deadline lower bound.  For a word
\(A=(a_0,\ldots,a_{L-1})\), let

\[
 (D^qA)_i=a_i\cup\cdots\cup a_{i+q}.                              \tag{1.3}
\]

All letters are nonempty sets and all intervals below are linear.

## 2. The closed splice and its exact excess

Let \(X=(x_0,\ldots,x_{n-1})\) be a word on \(V\), and let \(z\notin V\).
Define

\[
 \mathcal S_z(X)=X\,[\{z\}]\,
   (\{z\}\cup x_0,\ldots,\{z\}\cup x_{n-2}).                    \tag{2.1}
\]

### Theorem 2.1 (closed-splice equivalence)

The word \(\mathcal S_z(X)\) is universal on \(V\cup\{z\}\) if and only if
\(X\) is universal on \(V\).  Its length is \(2n\).

#### Proof

Every target omitting \(z\) must be realized in the initial \(X\), proving
necessity.  Conversely, let \(M\ne\varnothing\) have witness
\([a,c]\) in \(X\).  If \(c<n-1\), its tagged copy realizes
\(M\cup\{z\}\).  If \(c=n-1\), the original interval followed by the bare
singleton realizes \(M\cup\{z\}\).  The singleton realizes \(\{z\}\).
These and the original witnesses realize every nonempty target.  The length
is \(n+1+(n-1)=2n\).  ∎

Suppose now that \(X\) has length \(B(k-1)+e\).  If \(k=2m\) is even, then
\(w_{2m}=2w_{2m-1}\), so Theorem 2.1 has the exact excess

\[
 |\mathcal S_z(X)|-B(2m)
 =2e+2d_{2m-1}-d_{2m}.                              \tag{2.2}
\]

For comparison, if \(k=2m+1\) is odd, then

\[
 2w_{2m}-w_{2m+1}=\frac1{m+1}{2m\choose m}=\operatorname{Cat}_m,
\]

and hence

\[
 |\mathcal S_z(X)|-B(2m+1)
 =2e+\operatorname{Cat}_m+2d_{2m}-d_{2m+1}.          \tag{2.3}
\]

Thus the closed splice is naturally an even-lift construction.  Across an
odd step it pays a Catalan-width toll.

### Theorem 2.2 (even depth dichotomy)

For \(m\geq2\),

\[
 d_{2m}\leq d_{2m-1}\leq d_{2m}+1.                  \tag{2.4}
\]

Consequently an exact odd parent must shed

\[
 c_{2m}:=2d_{2m-1}-d_{2m}
 \in\{d_{2m},\ d_{2m}+2\}                           \tag{2.5}
\]

cells to reach \(B(2m)\).  The value \(d_{2m}+1\) never occurs.

#### Proof

Put \(h={2m-1\choose m}\), \(a=d_{2m-1}\), \(b=d_{2m}\), and
\(T_t={t+1\choose2}\).  Symmetry gives

\[
 \Lambda_{2m-1}=2^{2m-2}-1,
 \qquad \Lambda_{2m}=2\Lambda_{2m-1}-h+1,           \tag{2.6}
\]

while \(w_{2m-1}=h\) and \(w_{2m}=2h\).

The odd lower mass is a sum of \(m-1\) binomial coefficients, each at most
\(h\), so \(a\leq m-1\).  Also \(h\geq T_{m-1}+1\) for \(m\geq2\): check
\(m=2\) directly; for \(m\geq3\), unimodality gives
\(h\geq{2m-1\choose2}>T_{m-1}\).  Odd feasibility therefore gives

\[
 2ah+T_a=2(ah+T_a)-T_a
 \geq2\Lambda_{2m-1}-T_a
 \geq2\Lambda_{2m-1}-h+1=\Lambda_{2m},
\]

so \(b\leq a\).

Conversely, even feasibility says

\[
 2bh+T_b\geq2\Lambda_{2m-1}-h+1.
\]

Adding \(2h+2T_{b+1}-T_b\geq h-1\) and dividing by two shows
\((b+1)h+T_{b+1}\geq\Lambda_{2m-1}\), hence \(a\leq b+1\).
This proves (2.4), and (2.5) follows by substitution.  ∎

The central-binomial estimate gives

\[
 d_k=\sqrt{\frac{\pi k}{8}}+O(1),
 \qquad c_{2m}=\Theta(\sqrt m).                     \tag{2.7}
\]

So the word-level splice does not itself prove a constant-additive even
recurrence.

The exact finite arithmetic is

| child | \(d_{k-1}\to d_k\) | splice length | \(B(k)\) | required saving |
|---:|:---:|---:|---:|---:|
| 10 | \(2\to2\) | 256 | 254 | 2 |
| 12 | \(3\to2\) | 930 | 926 | 4 |
| 14 | \(3\to2\) | 3438 | 3434 | 4 |
| 16 | \(3\to3\) | 12876 | 12873 | 3 |

These are arithmetic identities.  The solved even words were not obtained
by one common literal-deletion rule: K10 was a direct carrier search, K12
required a repaired lift (with a later six-piece reconstruction), K14 used a
two-cut plus one-ear six-piece braid, and K16 used an endpoint-rerooted
four-filter carrier followed by one common-cap compiler.

Nevertheless, their final words share one exact derivative invariant.  In
each case the child has exactly $d_k$ omitted owner deadlines rather than the
$2d_{k-1}$ slack cells in the word-level splice.  Thus the saving
$2d_{k-1}-d_k$ is paid in one block by recompiling the two shores against one
child staircase; the construction histories do not assign one local seed
event to each shaved cell.

## 3. Why a fixed old shore still leaves \(+1\) or \(+2\)

The \(\Theta(\sqrt k)\) splice excess can be reduced algebraically to a
constant, but the last constant cannot be removed inside the most literal
architecture.

### Lemma 3.1 (equal-rank interval saturation)

For any finite sequence \(C=(c_1,\ldots,c_t)\) of sets, allowing empty sets,
at most \(t\) distinct interval unions have one prescribed rank \(s\).  If
equality holds, every entry of \(C\) is a
distinct rank-\(s\) set and these singleton intervals are all of the
rank-\(s\) unions.

#### Proof

For each left endpoint, its interval unions form an inclusion chain and
therefore contain at most one distinct rank-\(s\) set.  Equality forces a new
rank-\(s\) value at every start.  Backward induction from the final letter
then forces that value to be the singleton letter at each start.  ∎

### Theorem 3.2 (fixed-shore constant gate)

Let \(m\geq3\), let \(X\) be a universal word on \(2m-1\) coordinates, and
suppose the last letter of \(X\) has rank at least \(m-1\).  For arbitrary
old-coordinate sets \(c_1,\ldots,c_t\), if

\[
 X\,[\{z\}]\,
 (\{z\}\cup c_1,\ldots,\{z\}\cup c_t)             \tag{3.1}
\]

is universal, then

\[
 t\geq {2m-1\choose m-1}=h.                         \tag{3.2}
\]

It therefore has length at least

\[
 B(2m)+d_{2m-1}-d_{2m}+1
 \in\{B(2m)+1,\ B(2m)+2\}.                         \tag{3.3}
\]

#### Proof

Consider the tagged targets \(\{z\}\cup R\), where \(|R|=m-1\).  Tail
intervals supply at most \(t\) old projections by Lemma 3.1.  An interval
starting at the bare singleton and entering the tail has the same old
projection as a tail prefix and is already included in that count.  Every
remaining seam-crossing witness starts in \(X\) and contains its final
letter.  If that anchor has rank above \(m-1\), it supplies no such target;
if it has rank \(m-1\), it supplies only itself.

If the anchor has rank above \(m-1\), the tail must supply all \(h\) targets,
so \(t\geq h\) immediately.  If the anchor has rank \(m-1\), then
\(t\leq h-2\) is impossible.  At \(t=h-1\), the tail must attain equality in
Lemma 3.1, so all tail letters have rank \(m-1\geq2\).  Then neither a tail
interval nor a seam interval can realize a tagged target whose old part is a
singleton, again a contradiction.  Hence \(t\geq h\).  Finally the proved
lower bound gives \(|X|\geq B(2m-1)=h+d_{2m-1}\); adding the singleton and
tail proves (3.3).  ∎

In particular, a literal deletion from the closed splice would need to leave
a tagged tail of length

\[
 h+d_{2m}-d_{2m-1}-1\in\{h-1,h-2\},                \tag{3.4}
\]

which contradicts (3.2).  An exact even induction must therefore change at
least one of the following: the old shore, the bare-singleton placement, or
the uniform tagged-tail form.  This is a source-relative obstruction through
the displayed anchor hypothesis, not an unrestricted even no-go.

If a specially robust parent allowed its tagged tail to be shortened to
exactly \(h\), (3.3) would already give \(B+1\) or \(B+2\).  Such robustness
is an additional existence condition; it does not follow from universality.

## 4. The exact generalized collar identity

There is a proof-safe way to state any proposed multi-cut repair without
pretending that marginal target counts suffice.

Fix a word skeleton with a set \(P\) of free collar positions.  Let
\(\mathcal R\) be the targets not already realized by an interval avoiding
\(P\).  A physical host for \(T\in\mathcal R\) is a pair \((F_T,I_T)\), where
\(I_T\subseteq P\) is the nonempty set of free positions in one literal
interval and \(F_T\subseteq T\) is the union of its fixed cells.

### Theorem 4.1 (maximal-core collar equivalence)

The skeleton has a nonzero collar completion if and only if one can select
one physical host for every \(T\in\mathcal R\) such that

\[
 K_p:=\bigcap_{T:p\in I_T}T\ne\varnothing             \tag{4.1}
\]

for every free position \(p\) (with an unused-position intersection equal to
the full ground), and

\[
 F_T\cup\bigcup_{p\in I_T}K_p=T
 \qquad(T\in\mathcal R).                             \tag{4.2}
\]

When these conditions hold, assigning the literal collar value \(K_p\) to
position \(p\) completes the word.

#### Proof

In any completion, a free cell used by \(T\) is a nonempty subset of \(T\),
so it lies in \(K_p\); every coordinate of \(T\setminus F_T\) must survive in
one used core.  This proves necessity.  Conversely, the assignment \(K_p\)
is contained in every target using \(p\), while (4.2) supplies every demanded
coordinate, so every chosen host interval has union exactly \(T\).  ∎

Starting from an exact odd parent, an even equality collar must have net
deletion \(c_{2m}\) from (2.5): an \(s\)-out/\((s-c_{2m})\)-in replacement.
Theorem 3.2 says a successful equality collar in the middle-rank-anchor
orientation must actually be mixed: it must touch the old shore or singleton,
or cease to be a uniformly tagged tail.  Theorem 4.1 is the exact remaining
simultaneous condition.  It is an iff interface, not an all-\(m\) existence
proof.

## 5. A two-rank carrier that pays the slack only once

The solved even words reveal a different exact architecture.  They do not
delete cells from two compiled parent words.  They construct \(w_k\) central
owners and then apply one depth-\(d_k\) compiler.

### Theorem 5.1 (two-rank carrier/compiler implication)

Let \(A\) be a word of length \(w_k+d_k\), put \(r=r_k\), and suppose
\(d=d_k\geq1\).  Set

\[
 E=D^dA=(E_0,\ldots,E_{w_k-1}).                     \tag{5.1}
\]

Assume:

1. every \(E_i\) has rank \(r\) or \(r+1\);
2. define
   \[
   P_i=\begin{cases}
      E_i,& |E_i|=r,\\
      (D^{d-1}A)_i,& |E_i|=r+1;
   \end{cases}                                      \tag{5.2}
   \]
   then every \(P_i\) has rank \(r\), and the \(P_i\) enumerate
   \(\binom{[k]}r\) exactly once;
3. every target of rank above \(r\) is a contiguous union of entries of
   \(E\); and
4. every target of rank below \(r\) is a contiguous union of letters of
   \(A\).

Then \(A\) is universal and has length \(B(k)\).

#### Proof

Each \(P_i\) is a physical interval of \(A\), so item 2 realizes the middle
layer.  If \(E_i\cup\cdots\cup E_j=U\), then

\[
 E_i\cup\cdots\cup E_j=A_i\cup\cdots\cup A_{j+d},  \tag{5.3}
\]

so item 3 realizes every upper target physically.  Item 4 realizes the lower
targets.  The length is \(w_k+d_k=B(k)\).  ∎

For even \(k=2m\), the central owners split into two shores of \(h\) masks
according to a distinguished coordinate.  The identity

\[
 |A|=2h+d_{2m}=B(2m)                                \tag{5.4}
\]

shows exactly where the closed splice overpays: it duplicates the parent
compiler slack, while Theorem 5.1 compiles both shores simultaneously and
pays \(d_{2m}\) only once.  Constructing such a carrier and its common lower
compiler is the substantive induction gate.

The exact derivative census of all four solved even answers is:

| $k$ | $d_k$ | ranks in $D^{d_k}A$ | projected middle owners | upper envelope cover | omitted owner deadlines |
|---:|---:|:---|:---:|:---:|:---|
| 10 | 2 | $5^{252}$ | complete | complete | `{0,2}` |
| 12 | 2 | $6^{924}$ | complete | complete | `{0,2}` |
| 14 | 2 | $7^{3432}$ | complete | complete | `{0,1}` |
| 16 | 3 | $9^{6386}8^{6484}$ | complete | complete | `{0,2,6389}` |

For K10, K12, and K14 the envelope itself is the flat middle carrier.  K16
is the first of these four fixtures requiring the rank-drop clause (5.2).
This identifies the reusable invariant more sharply than the historical
search operations: distinct child envelopes, complete projected owners,
complete upper envelope unions, and exactly $d_k$ deadline holes.

## 6. Literal K16 replay

For the authenticated optimum `answers/k16.word`, let \(A\) be its 12,873
letters, \(E=D^3A\), and define \(P\) by (5.2).  Independent literal replay
gives:

\[
 |E|=12870,
 \qquad |E_i|=\begin{cases}
 9,&0\leq i\leq6385,\\
 8,&6386\leq i\leq12869.
 \end{cases}                                        \tag{6.1}
\]

All 12,870 envelopes are distinct.  The rank histogram is

\[
             6484\text{ of rank }8,
 \qquad      6386\text{ of rank }9.                 \tag{6.2}
\]

The projected \(P_i\) are 12,870 distinct rank-eight masks and hence are
exactly the entire middle layer.  Moreover contiguous unions of \(E\) cover
every upper target:

| rank | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| covered | 11440 | 8008 | 4368 | 1820 | 560 | 120 | 16 | 1 |

Thus this is a literal positive fixture for Theorem 5.1, with lower coverage
supplied by the authenticated common-cap compiler.

For the distinguished bit \(z=\mathtt{0x8000}\), the envelope shores are

\[
\begin{array}{c|cc}
 &\text{rank }8&\text{rank }9\\ \hline
 z\notin E_i&6435&0\\
 z\in E_i&49&6386.
\end{array}                                         \tag{6.3}
\]

The 49 tagged rank-eight envelopes occur at positions
\([6386,6389]\cup[12825,12869]\).  The owner projection itself is perfectly
balanced: 6,435 owners omit \(z\), and 6,435 contain \(z\).  Therefore

\[
 6484-6386=(6435+49)-(6435-49)=98.                  \tag{6.4}
\]

The imbalance 98 is a shore-composition statistic; it is not the payment
for \(d=3\).

The exact first-middle ledger makes the depth payment explicit.  For owner
starts \(0,\ldots,12869\), the first rank-eight witnesses have lengths

\[
 2^1,\quad3^{6386},\quad4^{6483},                   \tag{6.5}
\]

and their distinct deadlines are

\[
 \{1\}\cup[3,6388]\cup[6390,12872].                \tag{6.6}
\]

The three omitted deadlines are exactly

\[
                         \{0,2,6389\}.              \tag{6.7}
\]

The three extra starts \(12870,12871,12872\) have lengths \(3,2,1\) and all
deliver the already-owned terminal target `0xf30c` at deadline 12872.  Across
\(D^2\to D^3\), the rank transitions are

\[
 (7\to8)^{6483},\qquad(8\to9)^{6386},\qquad(8\to8)^1.             \tag{6.8}
\]

The envelope rank word has one \(9\to8\) transition.  It lies next to the
interior omitted deadline 6389; the other two omitted deadlines are left
boundary effects.  Hence neither the single transition nor the rank
imbalance pays all three units.  The exact (q=3) payment is the three-hole
deadline/tail-duplicate ledger, implemented by one common compiler.

## 7. Scope and remaining theorem

Proved here:

1. the closed-splice equivalence and its exact even/odd excess formulas;
2. the even depth dichotomy and the exact saving \(d\) or \(d+2\);
3. a fixed-middle-anchor obstruction leaving \(+1\) or \(+2\) in the
   fixed-old-shore/bare-singleton/uniform-tail architecture;
4. the exact maximal-core condition for any fixed mixed collar;
5. the solver-independent two-rank carrier/compiler implication; and
6. the complete literal K16 two-rank, owner, upper-cover, shore, transition,
   and deadline replay.

Not proved:

1. existence of exact odd parents for all odd dimensions;
2. existence of a robust \(h\)-letter tagged tail;
3. an all-\(m\) construction of the two-rank carrier or common compiler;
4. a normalization putting every optimum into either architecture; or
5. an unconditional \(B(k)+O(1)\) or exact even induction.

The weakest exact positive target exposed by this analysis is therefore:
construct, for every even dimension, a two-shore two-rank envelope satisfying
items 1--3 of Theorem 5.1 together with one simultaneous lower compiler.
The K16 rank imbalance 98 is evidence for allowable shore flexibility, not a
recurrence invariant.

## 8. Audit artifacts

The independent replay is

```text
scratch/audit_even_splice_two_rank_carrier_20260731.py
scratch/even_splice_two_rank_carrier_20260731.audit.json
```

It verifies the depth identities through \(k=256\), constructs and fully
replays the closed splices into K10/K12/K14/K16, checks the derivative
carrier invariant in all four exact answers, and performs every detailed K16
enumeration quoted above directly from `answers/k16.word`.
