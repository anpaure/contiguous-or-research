# Gate C: the fixed-cut obstruction for the entire ordered-GK diamond class

**Status (2026-08-22).**  Every assertion below is proved.  Starting from
one ordered Greene--Kleitman symmetric-chain decomposition and performing
an arbitrary collection, or an arbitrary sequence, of legal central
Boolean-diamond switches never changes the unordered coordinate pair of a
central flag.  All resulting arcs therefore cross the single balanced cut
given by alternating positions in the chosen coordinate order.

This invariant is strong enough to rule out the proposed fixed-factor
packing: for every constant \(C\), all coherent phase supports having at
least \(q-Cb\) flags in any one factor from this construction class together
meet only \(O_C(N/\sqrt b)=o(N)\) of its flags.  The obstruction is not a
shortage of alternating Hamilton cycles; it is the much smaller collection
of middle-rank parity-split layers accessible to their FIFO windows.

The last theorem quantifies the weakest possible escape while retaining
the \(q-O(b)\) loss scale.  Any central factor admitting such a
rankwise-disjoint tour packing of positive
density must, relative to **every** balanced coordinate cut, contain
\(\Omega(N/\sqrt b)\) flags internal to each shore.  Hence a modification of
an ordered-GK diamond factor must change the unordered endpoint pair of at
least \(\Omega(N/\sqrt b)\) central flags; middle-only diamond switches can
never supply even one such change.

Throughout,
\[
 n=2b,\qquad b\ge3\text{ odd},\qquad
 h={b-1\over2},\qquad q=b(b-1),\qquad
 N={2b\choose b-1}.                                    \tag{0.1}
\]

## 1. The exact invariant of the construction class

Fix an ordered coordinate list
\[
                 x_0\prec x_1\prec\cdots\prec x_{2b-1}
\]
and its alternating balanced cut
\[
 X=\{x_i:i\text{ even}\},\qquad
 Y=\{x_i:i\text{ odd}\}.                              \tag{1.1}
\]
In the ordered Greene--Kleitman decomposition, read a middle set as a
balanced zero--one word in this order, with one denoting membership.  Pair
each zero with the latest still-unpaired one to its left.  A nonsingleton
middle word \(C\) has central flag
\[
 C-\{p(C)\}\subset C\subset C\cup\{q(C)\},             \tag{1.2}
\]
where \(q(C)\) is the rightmost unpaired zero and \(p(C)\) is the leftmost
unpaired one.  Thus \(q(C)\prec p(C)\).

### Lemma 1.1 (ordered-GK arcs cross the alternating cut)

The positions of \(p(C)\) and \(q(C)\) have opposite parity.

#### Proof

No matched pair crosses an unpaired position.  Indeed, an opener before an
unpaired zero would still be available when that zero is read, while a
closer after an unpaired one would pop that one before any earlier opener.
There is no unpaired position strictly between the rightmost unpaired zero
and the leftmost unpaired one.  Hence all positions strictly between
\(q(C)\) and \(p(C)\) are paired among themselves.  Their number is even,
so the positional difference \(p(C)-q(C)\) is odd. \(\square\)

For a central flag \(f=(L,C,U)\), write
\[
 p(f)=C\setminus L,\qquad q(f)=U\setminus C.            \tag{1.3}
\]
The alternate middle vertex of the same Boolean diamond is
\[
 C'=L\cup(U\setminus C).
\]
The central diamond switch replaces
\[
 (L,C,U)\longmapsto(L,C',U).                            \tag{1.4}
\]
It may be performed only as part of a collision-free system so that all
chains still partition the Boolean lattice.  Legality will not matter for
the invariant.

### Theorem 1.2 (fixed-cut and fixed-undirected-multigraph invariant)

Let \(\mathfrak A\) be the central flag factor obtained from the fixed
ordered Greene--Kleitman SCD by any finite sequence of legal switches
\((1.4)\), simultaneous or sequential.  Then:

1. every arc of \(\mathfrak A\) crosses the fixed cut \(X\mid Y\);
2. each switch merely reverses its arc;
3. the complete multiset of unordered arc pairs is identical to that of
   the original ordered-GK factor.

#### Proof

The outer sets \(L,U\) do not change in (1.4), and
\[
 U\setminus L=\{p(f),q(f)\}.
\]
The old middle selects \(p(f)\) first and \(q(f)\) second, whereas the
alternate middle selects them in the opposite order.  Thus the new arc is
\(q(f)\to p(f)\), with the same unordered endpoints.  Lemma 1.1 puts those
endpoints on opposite shores before every switch, and induction over any
sequence of switches proves all three claims. \(\square\)

There is a useful exact refinement.  Put
\(
 \operatorname{Cat}_r=(r+1)^{-1}{2r\choose r}.
\)
If the positions satisfy \(p>q\) and \(p-q=2a+1\), then the original
ordered-GK factor has exactly
\[
                 \operatorname{Cat}_a\operatorname{Cat}_{b-1-a}       \tag{1.5}
\]
flags with arc \(p\to q\); there are no other arcs.  To see this, rotate
the balanced word to start at \(p\).  The rotation is Dyck and its first
return is at \(q\), after
\(2b-p+q+1=2(b-a)\) steps.  Its primitive first excursion can be chosen in
\(\operatorname{Cat}_{b-a-1}\) ways and its remaining Dyck suffix in
\(\operatorname{Cat}_a\) ways, giving (1.5).  Conversely this decomposition
recovers exactly the required unpaired symbols.  In particular the
undirected arc multigraph is the complete \(X\)--\(Y\) bipartite graph with
positive Catalan-convolution multiplicities and is
\(\operatorname{Cat}_b\)-regular, by
\[
 \sum_{a=0}^{b-1}\operatorname{Cat}_a
                 \operatorname{Cat}_{b-1-a}=\operatorname{Cat}_b.     \tag{1.6}
\]
Thus the obstruction below is not caused by absent cross-cut coordinate
edges.

## 2. Coherent windows and cut bandwidth

Let \(H=(z_0,z_1,\ldots,z_{2b-1})\) be a directed Hamilton cycle and
\(\delta\in\{0,1\}\) one of its two coherent phases.  Indices below are
cyclic modulo \(2b\).  The \(q\) internal middle windows of its coherent
FIFO tour have index sets
\[
 J_{s,t}^{\delta}
 =\delta+s(b+1)+\bigl([t,b+t]\setminus\{b\}\bigr),
 \quad 0\le s<b,\quad1\le t<b,                          \tag{2.1}
\]
and its corresponding flag has middle
\[
 C_{s,t}^{\delta}(H)=\{z_j:j\in J_{s,t}^{\delta}\}
\]
and coordinate arc
\[
 z_{\delta+s(b+1)+b+t}\longrightarrow
 z_{\delta+s(b+1)+b+t+1}.                              \tag{2.2}
\]
Indeed, at packet zero the FIFO window is the interval of \(b+1\)
H-positions from \(t\) through \(b+t\), with the antipodal position \(b\)
deleted.  Advancing a packet translates all positions by \(b+1\), and the
packets close because \(b(b+1)\equiv0\pmod{2b}\).  Formula (2.2) also shows
that every Hamilton edge occurs in exactly \(h=(b-1)/2\) internal flags:
the start index has fixed parity for a fixed \(t\), multiplication by
\(b+1\) runs through that parity class, and each parity occurs \(h\) times
among \(1\le t<b\).

For an arbitrary balanced cut \(X\mid Y\), define
\[
 \sigma_i=\begin{cases}1,&z_i\in X,\\-1,&z_i\in Y,
             \end{cases}
 \qquad
 k_X(H)=|\{i:z_i,z_{i+1}\text{ lie on the same shore}\}|.              \tag{2.3}
\]

### Lemma 2.1 (interval-minus-point discrepancy)

Every coherent middle window satisfies
\[
 \left|2|C_{s,t}^{\delta}(H)\cap X|-b\right|\le k_X(H)+2.             \tag{2.4}
\]

#### Proof

Put \(\tau_i=(-1)^i\sigma_i\).  Across a cut-crossing Hamilton edge,
\(\tau\) stays constant; across a same-shore edge, it changes sign.
Therefore the cyclic word \(\tau\) has exactly \(k_X(H)\) sign changes.
Any cyclic interval meets at most \(k_X(H)+1\) constant-sign pieces, and
on each piece the alternating sum
\(\sum(-1)^i\tau_i=\sum\sigma_i\) has absolute value at most one.  Hence
every cyclic interval has discrepancy at most \(k_X(H)+1\).  The set
(2.1) is an interval with one point deleted, which costs at most one more.
Its discrepancy is exactly the left side of (2.4). \(\square\)

## 3. No \(q-O(b)\) fixed-factor packing in the diamond class

For \(K\ge0\), let
\[
 \mathcal B_K(X)=\left\{C\in{\Omega\choose b}:
       |2|C\cap X|-b|\le K+2\right\}.                  \tag{3.1}
\]

### Theorem 3.1 (construction-class no-go)

Let \(\mathfrak A\) be any central factor in the ordered-GK diamond class
of Theorem 1.2.  Fix \(L\ge0\), put \(K=\lfloor L/h\rfloor\), and let
\(\mathscr T\) be any collection of coherent phase supports such that
\[
                         |\mathcal T\cap\mathfrak A|\ge q-L             \tag{3.2}
\]
for every \(\mathcal T\in\mathscr T\).  Then
\[
 \left|\mathfrak A\cap\bigcup_{\mathcal T\in\mathscr T}\mathcal T\right|
 \le |\mathcal B_K(X)|
 \le (K+3){b\choose h}^{\!2}.                           \tag{3.3}
\]
Consequently
\[
 {1\over N}\left|\mathfrak A\cap
       \bigcup_{\mathcal T\in\mathscr T}\mathcal T\right|
 \le {2(K+3)\over\sqrt{\pi b}}\,(1+O(b^{-1})).         \tag{3.4}
\]
In particular, for every fixed \(C\), no collection of supports with
overlap at least \(q-Cb\) covers a fixed positive fraction of
\(\mathfrak A\).  More quantitatively, if the union in (3.3) has size at
least \(\alpha N\), then
\[
 L\ge\left({\alpha\sqrt\pi\over4}+o_\alpha(1)\right)b^{3/2}.            \tag{3.5}
\]

#### Proof

Every same-shore edge of \(H\) accounts for \(h\) distinct tour flags by
(2.2), and none can lie in \(\mathfrak A\) by Theorem 1.2.  Hence (3.2)
implies \(hk_X(H)\le L\), so \(k_X(H)\le K\).  Lemma 2.1 puts the middle
of every flag in every selected support inside \(\mathcal B_K(X)\).
A central factor uses each middle target at most once, giving the first
inequality in (3.3).

If \(a=|C\cap X|\), then there are \({b\choose a}^2\) possible middles.
Condition (3.1) permits at most \(K+3\) integer values of \(a\), and
\({b\choose a}\le {b\choose h}\), proving (3.3).  Finally,
\[
 {b\choose h}^{\!2}={2\over\pi b}4^b(1+O(b^{-1})),\qquad
 N={4^b\over\sqrt{\pi b}}(1+O(b^{-1})),
\]
which gives (3.4). \(\square\)

For (3.5), inequality (3.4) forces
\(K\ge(\alpha\sqrt{\pi b}/2)-3+o(\sqrt b)\); now use \(L\ge hK\).
Notice that \(b^{3/2}=o(q)\).  The theorem kills the one-defect-per-packet,
\(L=O(b)\), target throughout this construction class, but leaves a
genuinely different mesoscopic-loss architecture logically possible.
More generally, a loss \(L=O(bK_b)\) gives only the upper bound
\(O(K_bN/\sqrt b)\).  Once \(K_b=\Theta(\sqrt b)\), this bound no longer
vanishes; in particular the present theorem does not obstruct the live
fixed-factor wide-band route at loss \(\Theta(b^{3/2})=o(q)\).

Exactly alternating Hamilton cycles show why counting cycles alone misses
the obstruction.  Rooting at a fixed member of \(X\), their number is
\[
                         b!(b-1)!,                       \tag{3.6}
\]
because the \(b\) members of \(Y\) and the remaining \(b-1\) members of
\(X\) may be ordered independently.  This is far larger than the required
\(N/q=\Theta(4^b/b^{5/2})\) tour count.  Nevertheless (2.1) puts their two
phases in exactly the two split layers 
\(|C\cap X|=h,h+1\), containing only
\[
                         2{b\choose h}^{\!2}=O(N/\sqrt b)               \tag{3.7}
\]
middle targets.

## 4. Quantitative minimum escape from every balanced cut

For a general central factor \(\mathfrak A\) and a balanced cut
\(X\mid Y\), put
\[
 R_X(\mathfrak A)=|\{f\in\mathfrak A:p(f),q(f)\in X\}|,
 \qquad
 R_Y(\mathfrak A)=|\{f\in\mathfrak A:p(f),q(f)\in Y\}|.                \tag{4.1}
\]

### Theorem 4.1 (endpoint-changing surgery is necessary at scale
\(N/\sqrt b\))

Fix constants \(\alpha>0\) and \(C<\infty\).  Suppose a central factor
\(\mathfrak A\) contains pairwise rankwise-target-disjoint partial
coherent tours \(\mathcal P_i\), where \(\mathcal P_i\) is contained in a
phase support \(\mathcal T_i\),
\[
 |\mathcal P_i|\ge q-Cb,
 \qquad
 \sum_i|\mathcal P_i|\ge\alpha N.                       \tag{4.2}
\]
Then, uniformly for **every** balanced cut \(X\mid Y\),
\[
 R_X(\mathfrak A),R_Y(\mathfrak A)
 \ge\left({\alpha^2\sqrt\pi\over64}+o_{\alpha,C}(1)\right)
       {N\over\sqrt b}.                                 \tag{4.3}
\]

#### Proof

For \(H_i\), write \(k_i=k_X(H_i)\), and let \(e_X(H_i)\) and \(e_Y(H_i)\)
count its edges internal to the two shores.  A cyclic tour visits equally
many vertices in the two shores, so its numbers of \(X\to Y\) and
\(Y\to X\) transitions agree; consequently
\[
                         e_X(H_i)=e_Y(H_i)=k_i/2.         \tag{4.4}
\]
The full phase support has \(h e_X(H_i)\) flags on \(X\)--\(X\) edges.
Deleting at most \(Cb\) flags to obtain \(\mathcal P_i\) leaves at least
\[
                         hk_i/2-Cb                       \tag{4.5}
\]
such flags, and the same lower bound holds on \(Y\)--\(Y\) edges.

Put
\[
                         K=\left\lfloor{\alpha\sqrt{\pi b}\over8}
                           \right\rfloor .               \tag{4.6}
\]
By Lemma 2.1 and the count in Theorem 3.1, all partial tours with
\(k_i\le K\) together use at most
\[
 |\mathcal B_K(X)|\le(\alpha/4+o_\alpha(1))N<\alpha N/2               \tag{4.7}
\]
distinct middle targets.  Hence the tours with \(k_i>K\) contain at least
\(\alpha N/2\) of the flags in (4.2), and there are at least
\(\alpha N/(2q)\) such tours because one tour contains at most \(q\)
flags.

For every high-\(k_i\) tour, (4.5) is larger than
\[
 {hK\over2}-Cb
 =\left({\alpha\sqrt\pi\over32}+o_{\alpha,C}(1)\right)b^{3/2}.        \tag{4.8}
\]
The partial tours are target-disjoint, so these internal flags are
distinct across \(i\) and all belong to \(\mathfrak A\).  Multiplying
(4.8) by \(\alpha N/(2q)\), using \(q=b(b-1)\), proves the \(X\)-shore
bound in (4.3).  The identical argument gives the \(Y\)-shore bound.
\(\square\)

Theorem 4.1 gives the exact structural escape criterion.  A central
diamond switch keeps \(L,U\), hence keeps the unordered pair
\(U\setminus L\), and contributes zero to both quantities in (4.1) for
the distinguished alternating cut.  To reach a positive-density
\(q-O(b)\) packing, one must instead change at least one outer incidence
\(L\subset C\) or \(C\subset U\) on
\(\Omega(N/\sqrt b)\) flags of each shore type.  Equivalently, one needs a
mesoscopic upper/lower-tail rethread, a mixture of genuinely different
coordinate orders inside one integral SCD, or another operation that
changes unordered central endpoints.  No composition of middle-only
Boolean-diamond switches from one ordered GK decomposition can do so.

## 5. Finite audit

The companion checker is

`scratch/verify_gate_c_ordered_gk_diamond_fixed_cut_20260822.py`.

It verifies the fixed-cut invariant, the exact Catalan-convolution arc
multiplicities and regularity, reversal under every individual diamond,
the coherent interval discrepancy on all balanced cut words through
\(b=9\), the exact split-band count, and the alternating-phase layer
identity.  It is confirmatory; all general proofs are contained above.
