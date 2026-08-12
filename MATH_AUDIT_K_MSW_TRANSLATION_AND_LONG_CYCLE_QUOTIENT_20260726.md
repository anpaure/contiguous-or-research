# Canonical MSW translation audit and the long-cycle quotient relaxation

Date: 2026-07-26

Method: pure mathematics only. No web search, computation, solver, or
finite search is used.

## 0. Verdict

Put

\[
 p=2m+1,\qquad W=\binom p m,\qquad
 T=W/p=\operatorname {Cat}_m,
\]

and suppose that \(p\) is prime. The requested congruence class
\(p\equiv1\pmod4\) is exactly the case \(m\) even.

The audit gives four exact conclusions.

1. The canonical MSW/Chung--Feller factor is not invariant under
   \(x\mapsto x+1\), for any \(m\ge2\). More strongly, it contains no
   translation-fixed AP row when \(p\ge5\). Thus for even \(m\) it has zero
   fixed rows, whereas an invariant shortest-cycle factor must have exactly
   two.

2. Projecting the oriented arcs of any exact physical odd-graph factor to
   translation necklaces gives a tagged \(p\)-regular bipartite
   multigraph. Every perfect matching lifts to a translation-invariant
   directed owner permutation. It is a simple undirected cycle factor only
   if the matching does not select a voltage-edge orbit together with its
   exact reverse.

3. For a reverse-free lift, every-second traversal gives a literal exact
   alternating \(X/Y\) Johnson factor. The apparent upper-interface gap
   disappears because the upper trace on one parity is exactly the
   complement of the lower trace on the other parity. The full depth-\(H\)
   contiguous-OR compiler nevertheless needs \(2H+2\) consecutive omitted
   labels to be distinct, not merely \(2H\).

4. Long cycles are accepted by the constant-one transfer only with three
   quantitative ledgers: literal cooldown defect \(o(W)\), component
   collar \(o(W)\), and aggregate one-sided target holes \(o(W)\).
   Bipartite edge-colouring supplies none of these higher-order estimates.

The long-cycle relaxation therefore genuinely bypasses the
shortest-\(p\)-cycle Catalan/two-AP-loop obstruction, but it does not by
itself prove constant one.

## 1. Canonical flip lists and coordinate translation

Let \({\cal D}_m\) be the Dyck words of semilength \(m\). For
\(w\in{\cal D}_m\), write

\[
 \rho(w)=(\rho_1(w),\ldots,\rho_{2m}(w))
\]

for its canonical MSW flip-position permutation. The cyclic omitted-label
word of the associated wreath is

\[
 \widehat\rho(w)=(\rho_1(w),\ldots,\rho_{2m}(w),p).
\tag{1.1}
\]

With

\[
 \mu(u)=\overline{\operatorname {rev}(u)},
\]

the exact recurrences are

\[
 \rho(PQ)=\rho(P)\mathbin\Vert(|P|+\rho(Q))
\tag{1.2}
\]

for concatenated Dyck words, and

\[
 \rho(1u0)=(2a,\;2a-\rho(\mu(u)),\;1)
\tag{1.3}
\]

when \(1u0\) is primitive of length \(2a\). Equivalently, for
\(w=1u0v\) and \(d=|u|+2\),

\[
 \rho(w)=(d,\;d-\rho(\mu(u)),\;1,\;d+\rho(v)).
\tag{1.4}
\]

### Lemma 1.1 (infinity-neighbour parity)

For every \(w\in{\cal D}_m\), the first entry of \(\rho(w)\) is even and
the last entry is odd. Consequently the two neighbours of \(p\) in
\(\widehat\rho(w)\) have opposite parity.

#### Proof

The first entry is the even length of the first primitive component. By
(1.3), the last flip in a primitive component is \(1\). If the final
primitive component is preceded by a Dyck prefix of even length \(2b\),
(1.2) makes the final entry \(2b+1\). \(\square\)

Let \(\tau:x\mapsto x+1\) on \(\mathbb F_p\), with \(p\) representing
zero. If \(j\) is the position of \(2m=p-1\) in \(\rho(w)\), applying
\(\tau\) to (1.1) and recutting immediately after the new occurrence of
\(p\) gives

\[
 \Theta_w=
 (\rho_{j+1}+1,\ldots,\rho_{2m}+1,\,
  1,\,
  \rho_1+1,\ldots,\rho_{j-1}+1).
\tag{1.5}
\]

An unoriented canonical row could agree with the translate only if
\(\Theta_w\) or its reverse were a canonical flip list. Formula (1.5) is
the exact action on the cycle indices; coordinate shift is not an action
on the Dyck roots.

### Theorem 1.2 (canonical non-equivariance)

For every \(m\ge2\), the canonical MSW factor is not invariant under
\(\tau\).

#### Proof

Take \(w_0=(10)^m\). By (1.2),

\[
 \rho(w_0)=(2,1,4,3,\ldots,2m,2m-1).
\tag{1.6}
\]

In \((\rho(w_0),p)\), the neighbours of label \(2m\) are \(2m-3\) and
\(2m-1\), both odd. After translation, \(2m\) becomes \(p\), while those
neighbours become \(2m-2\) and \(2m\), both even. Lemma 1.1 excludes every
canonical row in either orientation.

The exact recut is also instructive:

\[
 \Theta_{w_0}=(2m,1,3,2,5,4,\ldots,2m-1,2m-2).
\tag{1.7}
\]

It begins in \(2m\), so a corresponding root would be primitive; (1.3)
would then force the last entry to be \(1\), contrary to (1.7). Its reverse
begins in \(2m-2\), so the first primitive component would have length
\(2m-2\). The remaining suffix is necessarily \(10\), and (1.2) would
force the last two entries to be \((2m,2m-1)\), whereas the reverse of
(1.7) ends in \((1,2m)\). \(\square\)

## 2. No canonical row is an AP fixed row

A wreath fixed setwise by \(\tau\) has, after placing \(p=0\) last, an
omitted-label order

\[
 (d,2d,\ldots,(p-1)d,p)
 \quad\text{in }\mathbb F_p
\tag{2.1}
\]

for some \(d\ne0\). Conversely every such AP order is fixed.

### Theorem 2.1 (intrinsic AP obstruction)

If \(p=2m+1\ge5\) is prime, no canonical MSW row is an AP row.

#### Proof

Suppose \(\rho(w)\) has form (2.1), and put

\[
 D=\rho_1(w)\in\{1,\ldots,p-1\}.
\]

The number \(D\) is the even length of the first primitive component. The
last flip within this component is \(1\), at position \(D\). Since the AP
step is also \(D\),

\[
 1=\rho_D(w)\equiv D^2\pmod p.
\tag{2.2}
\]

Thus \(D=1\) or \(D=p-1\). Parity excludes \(1\), so \(D=p-1=2m\), the
whole root is primitive, and the putative flip list is

\[
 (2m,2m-1,\ldots,1).
\tag{2.3}
\]

Formula (1.3) would then require

\[
 \rho(\mu(u))=(1,2,\ldots,2m-2).
\]

But a nonempty Dyck flip list begins with an even primitive-component
length, never \(1\). Since \(m\ge2\), the inner word is nonempty.
\(\square\)

### Corollary 2.2 (the missing two fixed rows)

For prime \(p=2m+1\),

\[
 \operatorname {Cat}_m
 =\frac1{m+1}\binom{2m}{m}
 \equiv2(-1)^m\pmod p.
\tag{2.4}
\]

Indeed \(\binom{p-1}{m}\equiv(-1)^m\) and
\((m+1)^{-1}\equiv2\pmod p\). In an invariant shortest-cycle factor,
nonfixed rows occur in orbits of size \(p\), while fixed rows are AP rows.
Only \(m<p\) geometric AP rows exist. Hence an invariant shortest factor
has exactly two fixed AP rows for even \(m\), and cannot exist for odd
\(m\ge3\). (The exceptional \(m=1,p=3\) triangle is one AP cycle.) The
canonical factor has none for \(m\ge2\) by Theorem 2.1.

This obstruction is independent of the choice of root or orientation.

## 3. Exact shortest-cycle quotient boundary

The failed canonical shortcut does not invalidate the abstract
difference-family formulation. Let
\(c=(c_i)_{i\in\mathbb F_p}\) be a shortest wreath's cyclic omitted-label
permutation. Its middle owners are

\[
 M_i(c)=\{c_{i-2},c_{i-4},\ldots,c_{i-2m}\}.
\tag{3.1}
\]

Then \(M_i\cap M_{i+1}=\varnothing\), and the unique omitted label is
\(c_i\). The lower depth-\(q\) trace is

\[
 \bigcap_{h=0}^{q}M_{i-2h}
 =\{c_{i-2(q+1)},c_{i-2(q+2)},\ldots,c_{i-2m}\}.
\tag{3.2}
\]

Normalize the translation phase by

\[
 \beta_i=m^{-1}\sum_{x\in M_i}x
        =-2\sum_{x\in M_i}x,\qquad
 A_i=M_i-\beta_i,\qquad
 y_i=c_i-\beta_i.
\tag{3.3}
\]

Then \(\sum_{x\in A_i}x=0\) and

\[
 \beta_{i+1}=\beta_i+2y_i,\qquad
 \sum_i y_i=0.
\tag{3.4}
\]

Thus every shortest wreath's full \(p\)-edge traversal is a closed
zero-total-voltage quotient walk. If the necklaces \([M_i]\) are distinct,
the primitive quotient object is a simple zero-voltage \(p\)-cycle. An AP
row is different: its full traversal is \(p\) repetitions of one primitive
quotient loop whose single-loop voltage is nonzero. For even \(m\), the
sought invariant shortest factor is therefore exactly two AP loops
together with

\[
 \frac{T-2}{p}
\tag{3.5}
\]

free, middle-transversal, zero-voltage \(p\)-cycle packets partitioning the
remaining middle necklaces.

There is no rankwise capacity obstruction. Quotient the containment
incidences between ranks \(r\) and \(r+1\) by translation. The two degrees
are \(p-r\) and \(r+1\). For \(r<m\), degree counting gives

\[
 |N(S)|\ge\frac{p-r}{r+1}|S|>|S|,
\]

so Hall gives a matching saturating every lower necklace. Iterating these
matchings yields disjoint nested quotient chains terminating at distinct
middle necklaces. This proves one-cover capacity only: it supplies neither
balanced loads, prescribed complete owner flags, nor the common cyclic
chronology (3.1)--(3.4).

For an invariant shortest factor, let \(k_q(O)\) be the common load of
each individual physical target in necklace \(O\), and put

\[
 \bar N_q=\frac1p\binom p{m-q},\qquad
 R_q=\sum_O(k_q(O)-1)_+,\qquad
 \bar M_q=|\{O:k_q(O)=0\}|.
\]

Since \(\sum_Ok_q(O)=T\),

\[
 \boxed{\bar M_q=R_q-(T-\bar N_q).}
\tag{3.6}
\]

At \(q=1\),

\[
 \bar N_1=\frac{m}{m+2}T,\qquad
 T-\bar N_1=\frac{2T}{m+2}.
\tag{3.7}
\]

Thus the correct one-sided rainbow target is repeat mass equal to this
forced baseline plus \(o(T)\), not zero repeats. If \(q/\sqrt m\to a\),
then \(\bar N_q/T\to e^{-a^2}\), so the forced repeat baseline is
\((1-e^{-a^2})T\). Independent rankwise Hall matchings do not encode the
required packet order.

### 3.1 Exact local \(q=1\) coordinates

The first-shadow transition also has a useful exact quotient normal form.
Let \(A\) be a zero-sum middle representative, let \(y\) be its current
omitted-label voltage, and let \(y'\) be the next voltage. The coordinate
deleted by the every-second Johnson move is

\[
 d_A=2y+y'\in A.
\tag{3.8}
\]

The normalized lower necklace is

\[
 \kappa(A;y,y')
 =\left(A\setminus\{d_A\}\right)-\frac23d_A.
\tag{3.9}
\]

Conversely, let \(S\) be a zero-sum rank-\((m-1)\) representative and
choose \(x\notin S\). Then

\[
 A=(S+2x)\cup\{3x\},\qquad d_A=3x,
\tag{3.10}
\]

and for a chosen admissible incoming voltage \(y\),

\[
 y'=3x-2y.
\tag{3.11}
\]

Indeed \(m-1=-3/2\) in \(\mathbb F_p\), so (3.9) is exactly mean-zero
normalization, while (3.10) has total sum
\(2x(m-1)+3x=0\). Around a cyclic quotient walk, (3.11) has a unique
cyclic solution for a prescribed \(x\)-word, because its homogeneous
multiplier after \(p\) steps is \((-2)^p=-2\ne1\). Summing (3.11) gives

\[
 \sum_i y_i=\sum_i x_i.
\tag{3.12}
\]

Thus zero voltage is equivalent to \(\sum_i x_i=0\). These identities
reduce one-sided \(q=1\) coverage to a literal constrained line-digraph
problem. They do not enforce state admissibility, quotient simplicity, or
disjointness of different packets.

Deeper flags are not free choices once the ordered \(q=1\) windows are
fixed. In ordinary-window indexing, if \(S_t\) denotes the depth-one
window, then

\[
 W_t^{(q)}=\bigcap_{h=0}^{q-1}S_{t-h},\qquad
 W_t^{(q+1)}=W_t^{(q)}\cap W_{t-1}^{(q)}.
\tag{3.13}
\]

Consequently a \(q=1\) histogram without its cyclic packet grouping carries
no certified \(q>1\) chronology.

### 3.2 An affine no-go and one exact nonlinear seed

The most obvious voltage family cannot supply the free packets. If

\[
 y_i=ui+v,
\]

then integrating (3.4) gives, up to an additive constant,

\[
 c_i=ui^2+2vi+\mathrm{const}.
\tag{3.14}
\]

For \(u\ne0\), this quadratic takes equal values at
\(i\) and \(-2v/u-i\), apart from their single fixed point, and is not a
permutation. For \(u=0\), the only nonconstant possibilities are AP rows.
Thus affine voltage words yield no free simple quotient packet.

There is nevertheless an exact nonlinear closed-wreath seed. For primes
\(p\equiv5\pmod{12}\), choose \(a\ne0\) and put

\[
 y_i=a\left(i^2-\frac16\right),\qquad
 \beta_i=\frac{2a}{3}i^3-ai^2,
\tag{3.15}
\]

\[
 c_i=\beta_i+y_i=\frac{2a}{3}i^3-\frac a6.
\tag{3.16}
\]

Here \(\beta_{i+1}-\beta_i=2y_i\), and \(\sum_i y_i=0\).
Since \(p\equiv2\pmod3\), the cube map is a permutation, so \(c\) is a
literal omitted-label permutation. The phase normalization is exact:
at \(i=0\),

\[
 \sum_{r=1}^{m}r^3
 =\left(\frac{m(m+1)}2\right)^2
 =\frac1{64}\quad\text{in }\mathbb F_p,
\]

and substitution into
\(-2\sum_{r=1}^{m}c_{-2r}\) gives \(\beta_0=0\); recurrence then proves
(3.3) at every phase.

This constructs a literal closed zero-voltage wreath walk. It does not
prove that its \(p\) middle necklaces are distinct, and the polynomially
many scalar/affine variants are negligible compared with \(T\). Thus it is
a genuine seed, not a difference-family solution.

## 4. Directed arc projection and exact matching lift

Let

\[
 V=\binom{\mathbb F_p}{m},\qquad
 \overline V=V/\langle\tau\rangle.
\]

Translation acts freely on \(V\), so \(|\overline V|=T\). Orient an exact
simple odd-graph two-factor and write its successor as

\[
 s:V\longrightarrow V,\qquad A\cap s(A)=\varnothing.
\tag{4.1}
\]

Create a tagged bipartite multigraph \(B_F\) with two copies of
\(\overline V\), inserting for every physical owner \(A\) the edge

\[
 e_A:[A]_{\rm L}\longrightarrow[s(A)]_{\rm R}.
\tag{4.2}
\]

### Theorem 4.1 (regularity and invariant lift)

The graph \(B_F\) is \(p\)-regular on both shores and decomposes into
\(p\) perfect matchings. Every matching lifts to a translation-invariant
directed owner permutation supported on odd-graph edges.

#### Proof

A necklace contains \(p\) physical owners, each the tail of one arc, so
every left degree is \(p\). Since \(s\) is a permutation, each owner is
also the head of one arc, so every right degree is \(p\). Regular
bipartite edge-colouring yields \(p\) perfect matchings.

Fix one matching \(M\). For each selected tag \(e_A\), include

\[
 \{A+t\longrightarrow s(A)+t:t\in\mathbb F_p\}.
\tag{4.3}
\]

Every physical owner has a unique selected outgoing orbit because its left
necklace is matched once, and a unique incoming orbit by the right-shore
condition. Translation preserves disjointness. \(\square\)

The tags matter. Different physical tags can represent the same translated
directed arc orbit. One matching cannot select two parallel copies, but
different colour classes can, and then their physical lifts overlap.
Therefore the \(p\) lifted permutations are not a physical edge
decomposition.

### Proposition 4.2 (reverse-pair caveat)

The lift of \(M\) is a simple undirected odd-graph cycle factor if and only
if it contains no quotient two-cycle formed by a directed voltage-edge
orbit and its exact reverse.

#### Proof

A directed owner permutation has no loops. Its only possible repeated
undirected edge is a directed two-cycle \(A\to B\to A\). This projects to
an arc orbit and its exact reverse, and the converse is immediate.
\(\square\)

If \(b\) reverse pairs are selected, they lift to \(pb\) physical
backtracks and involve \(2pb\) middle owners. Their every-second map is the
identity, not a Johnson move. The support-blind literal repair overhead for
quarantining them is at most

\[
 4pHb+2pb,
\tag{4.4}
\]

where the final \(2pb\) is the net middle-shore excess after the
\(2pb\) omitted \(X\)-owners are removed from the base and both middle
shores are repaired. (There are \(4pb\) raw missing \(X/Y\) middle slots.)
Thus
\(b=o(T/H)\) is one sufficient raw leave bound, but perfect-matching
existence gives no estimate on \(b\).

## 5. Voltage and the exact component ledger

Record a voltage in \(\mathbb F_p\) on every selected quotient arc. The
matching induces a permutation of the \(T\) quotient vertices. Let a
quotient cycle \(D\) have length \(\ell_D\) and total voltage
\(a_D\).

### Lemma 5.1 (voltage lift)

The physical lift of \(D\) consists of

\[
 \begin{cases}
 p\text{ cycles of length }\ell_D,&a_D=0,\\
 1\text{ cycle of length }p\ell_D,&a_D\ne0.
 \end{cases}
\tag{5.1}
\]

#### Proof

One quotient circuit changes phase by \(a_D\). Zero voltage closes every
phase separately; nonzero voltage generates the additive group of the
prime field. \(\square\)

A physical cycle of length \(L\) produces \(\gcd(2,L)\) step-two
components. Since \(p\) is odd, the exact number of every-second Johnson
components is

\[
 \boxed{
 K(M)=\sum_D\gcd(2,\ell_D)
 \left(1+(p-1)\mathbf1_{\{a_D=0\}}\right).}
\tag{5.2}
\]

Put

\[
 Z_0(M)=\sum_{D:a_D=0}\gcd(2,\ell_D).
\tag{5.3}
\]

Since \(\sum_D\gcd(2,\ell_D)\le T\), for \(H=o(p)\),

\[
 \boxed{
 K(M)=o(W/H)\quad\Longleftrightarrow\quad
 Z_0(M)=o(T/H).}
\tag{5.4}
\]

Indeed all nonzero-voltage quotient cycles together contribute at most
\(T=o(W/H)\). Thus the total quotient cycle count need not be
\(o(T/H)\); only the parity-weighted zero-voltage count matters.

## 6. Every-second traversal and the exact upper shore

Let \(A_0,\ldots,A_{L-1}\) be a reverse-free physical odd cycle, and put

\[
 z_i=\mathbb F_p\setminus(A_i\cup A_{i+1}).
\tag{6.1}
\]

The two sets \(A_i,A_{i+2}\) are distinct \(m\)-subsets of the
\((m+1)\)-set \(\mathbb F_p\setminus A_{i+1}\). Hence they are
Johnson-adjacent and

\[
 \boxed{A_{i+2}=A_i-\{z_{i+1}\}+\{z_i\}.}
\tag{6.2}
\]

On every step-two orbit put \(X_j=A_{i+2j}\). Then

\[
 Y_j=X_j\cup X_{j+1}
    =\mathbb F_p\setminus A_{i+2j+1}.
\tag{6.3}
\]

Across all step-two components, the \(X\)-occurrences partition rank \(m\)
and the \(Y\)-occurrences partition rank \(m+1\). This is an exact
alternating \(X/Y\) factor for arbitrary physical cycle lengths.

Define the signed depth-\(q\) traces by

\[
 L^-_{i,q}=\bigcap_{r=0}^{q}A_{i+2r},\qquad
 L^+_{i,q}=\bigcup_{r=0}^{q+1}A_{i+2r}.
\tag{6.4}
\]

If \(z_i,\ldots,z_{i+2q-1}\) are distinct, then

\[
 L^-_{i,q}
 =A_i\setminus\{z_{i+1},z_{i+3},\ldots,z_{i+2q-1}\},
 \qquad |L^-_{i,q}|=m-q.
\tag{6.5}
\]

If \(z_i,\ldots,z_{i+2q+1}\) are distinct, then

\[
 L^+_{i,q}
 =A_i\cup\{z_i,z_{i+2},\ldots,z_{i+2q}\},
 \qquad |L^+_{i,q}|=m+1+q.
\tag{6.6}
\]

The union of only \(q+1\) \(X\)-owners has rank \(m+q\) and is not the
odd upper target. The needed \(q+2\)-owner union is supplied exactly by
the opposite parity.

### Lemma 6.1 (multiplicity-exact complement pairing)

For every start and depth,

\[
 \boxed{
 \mathbb F_p\setminus
 \bigcap_{r=0}^{q}A_{i+1+2r}
 =\bigcup_{r=0}^{q+1}A_{i+2r}.}
\tag{6.7}
\]

Consequently the complete histograms satisfy

\[
 \mu_q^+(U)=\mu_q^-(\mathbb F_p\setminus U).
\tag{6.8}
\]

#### Proof

By (6.3),

\[
 \mathbb F_p\setminus A_{i+1+2r}
 =A_{i+2r}\cup A_{i+2r+2}.
\]

Take the union over \(0\le r\le q\). The pairing is occurrence-by-
occurrence, so multiplicities agree. \(\square\)

If the physical cycle is odd, both parities lie in the same step-two
cycle; if it is even, they are its two step-two cycles. The complete factor
retains both, so one-sided lower coverage controls the upper side exactly.

## 7. Correct return threshold and literal compiler

A \(q\)-transition step-two window is a Johnson geodesic if and only if
its \(2q\) omitted labels are pairwise distinct. Hence

\[
 \begin{array}{c|c}
 \text{lower rank correctness through depth }H&
  \text{every }2H\text{-label block is distinct},\\[1mm]
 \text{full odd delay-}H\text{ compiler}&
  \text{every }(2H+2)\text{-label block is distinct}.
 \end{array}
\tag{7.1}
\]

The stronger line is necessary for the cited compiler because upper depth
\(H\) uses \(H+1\) Johnson transitions and \(H+2\) \(X\)-states. A repeat
between the endpoints of a \(2H+2\)-block passes every \(2H\)-test but
creates a positive coordinate run of only \(H\) states.

For a cyclic Johnson component \(X_0,\ldots,X_{\lambda-1}\), assume no
coordinate changes twice in any \(H+1\) consecutive transitions, and put

\[
 B_j=\bigcap_{s=0}^{H}X_{j-s}.
\tag{7.2}
\]

The finite delay identities are

\[
 X_i=\bigcup_{j=i}^{i+H}B_j,
\tag{7.3}
\]

\[
 L^-_{i,q}=\bigcup_{j=i+q}^{i+H}B_j,\qquad
 L^+_{i,q}=\bigcup_{j=i}^{i+q+H+1}B_j.
\tag{7.4}
\]

Therefore the cyclic word

\[
 B_0,B_1,\ldots,B_{\lambda-1},B_0,B_1,\ldots,B_{2H}
\tag{7.5}
\]

realizes every signed trace through depth \(H\) by a literal contiguous OR
and has exact length

\[
 \lambda+2H+1.
\tag{7.6}
\]

For full-collar unrolling and worst-case all-start certification, the
additional \(1\) is forced by the \(H+2\)-state upper window. This is not
a universal minimality claim for every special cycle.

## 8. Exact constant-one transfer

Let \(1\le H\le m-1\). Let \(M\) be reverse-free, let \(K(M)\) be (5.2),
and assume the \(2H+2\) cooldown in (7.1). For \(1\le q\le H\), let
\(h_q(M)\) be the number of lower rank-\((m-q)\) translation necklaces
missed by every lower trace.

Translation acts freely at these ranks. By Lemma 6.1, the physical hole
counts are exactly

\[
 M_q^-=M_q^+=p\,h_q(M).
\tag{8.1}
\]

### Theorem 8.1 (long-cycle constant-one interface)

The lifted factor gives the literal bound

\[
 \boxed{
 \nu(p)\le
 W+(2H+1)K(M)
 +2p\sum_{q=1}^{H}h_q(M)
 +2L_m(m-H-1).}
\tag{8.2}
\]

Consequently, if

\[
 \frac H{\sqrt m}\longrightarrow\infty,\qquad H=o(p),
\tag{8.3}
\]

and

\[
 \boxed{
 Z_0(M)=o(T/H),\qquad
 \sum_{q=1}^{H}h_q(M)=o(T),}
\tag{8.4}
\]

then

\[
 \nu(p)\le(1+o(1))W.
\tag{8.5}
\]

#### Proof

The \(W\) middle owners supply the base. Each of the \(K(M)\) Johnson
components costs the exact collar \(2H+1\) from (7.5). Append every actual
signed central hole and the two outer SCD tails. This proves (8.2).
Equation (5.4) makes the collar \(o(W)\), (8.4) makes the hole term
\(o(W)\), and (8.3) makes the binomial tail \(o(W)\). \(\square\)

This preserves integrality and literal contiguous-OR realizability. The
upper side is no longer an independent gate.

## 9. Exceptional windows: the necessary quantifier

The phrase “\(H\)-return-free off \(o(W)\) windows” is sufficient only if
“windows” means the complete literal defect ledger, not merely maximal
root tests.

For a cyclic omission word of length \(L\), put \(s=2H+2\le L\). If two
equal labels have forward cyclic separation \(d\), the exact number of
rooted length-\(s\) blocks containing both is

\[
 \gamma_s(d)=(s-d)_+ +(s-(L-d))_+.
\tag{9.1}
\]

For several repeats, the bad-root set is the union of these root intervals.
If \(L\ge2s-1\), a return at separation \(s-1\) spoils exactly one maximal
test. Thus \(o(W)\) bad maximal roots need not control the collar or cut
charge.

Two formulations are valid.

1. Define \({\cal E}_H\) to be the number of missing middle,
   upper-middle, and signed-depth occurrence slots after the cyclic
   \(B\)-word is formed. If \({\cal E}_H=o(W)\), append those missing sets;
   \({\cal E}_H\) simply adds to (8.2).

2. If \(b\) cuts make the resulting paths delay-\(H\) safe, their base
   toll is \(Hb\), plus one lost upper-middle edge per bare cut. A
   support-blind isolated cut loses exactly

   \[
    1+\sum_{q=1}^{H}\bigl(q+(q+1)\bigr)=(H+1)^2
   \tag{9.2}
   \]

   central slots. Thus \(b=o(W/H^2)\) is a sufficient raw cut rate. If
   post-cut holes are measured directly, the sharper sufficient
   conditions are \(Hb=o(W)\) and actual holes \(o(W)\).

Merely counting \(o(W)\) failed maximal tests proves neither condition.

## 10. Safety alone is exactly critical, not subcritical

If a zero-voltage quotient cycle has \(2H+2\) cooldown, its cyclic
omission word has length at least \(2H+2\). Therefore

\[
 Z_0(M)\le
 2\frac{T}{2H+2}=\frac{T}{H+1}.
\tag{10.1}
\]

This yields only \(K=O(W/H)\), not \(o(W/H)\). One needs average
zero-voltage cycle length \(\omega(H)\), safety at a larger scale, or the
direct weighted condition in (8.4).

Local cooldown also gives no cross-owner coverage estimate. Every canonical
MSW wreath has a permutation of all \(p\) omitted labels, so it has no
local-return defect for \(2H+2\le p\). Its step-two factor has exactly

\[
 T=W/p=o(W/H)
\]

components for \(H=o(p)\). Nevertheless its audited first-shadow defect is

\[
 M_1^-\ge(1/16-o(1))W.
\tag{10.2}
\]

The canonical factor is not invariant by Theorem 1.2, so this is not a
no-go theorem for the invariant subclass. It is a literal counterexample
to every factor-blind implication from local return-freeness plus few
components to coverage. Translation invariance only makes loads constant
on necklaces; it does not make every necklace nonempty.

## 11. Why edge-colouring does not enforce the three ledgers

Proper edge-colouring controls individual arcs. Cooldown depends on strings
of consecutive selected arcs, \(Z_0\) depends on complete subtours and
their voltage sums, and \(h_q\) depends on collisions among distant traces.
None is an edgewise colour constraint.

Regularity alone admits an exact abstract countermodel. For any \(T\)
divisible by \(r=2H+2\), partition the \(T\) quotient vertices into
directed \(r\)-cycles and replace every directed arc by \(p\) parallel
tagged copies. The bipartite arc graph is \(p\)-regular and every perfect
matching has the same quotient permutation. Give each cycle zero total
voltage and \(r\) distinct formal local omission labels. Every matching is
locally cooldown-safe, but

\[
 Z_0=\frac{2T}{r}=\frac{T}{H+1}.
\tag{11.1}
\]

Thus every lift has \(\Theta(W/H)\) zero-voltage Johnson components and
hence \(\Theta(W)\) full-collar overhead. This is an abstract
voltage-bipartite countermodel, not an assertion that every such multigraph
is an odd-graph projection. It proves that regular bipartite edge-colouring
alone cannot yield the desired conclusion. A positive theorem for the
actual projection must use additional odd-graph geometry.

The exact surviving target is one quotient perfect matching satisfying
simultaneously

\[
 \begin{array}{ll}
 \mathrm{(R)}&\text{no reverse pair, or a reverse leave of literal cost }
               o(W),\\
 \mathrm{(C)}&\text{\(2H+2\) cooldown outside a literal defect ledger }
               o(W),\\
 \mathrm{(V)}&Z_0(M)=o(T/H),\\
 \mathrm{(L1)}&\displaystyle\sum_{q=1}^{H}h_q(M)=o(T).
 \end{array}
\tag{11.2}
\]

Once such an \(M\) is found, colouring all arcs is unnecessary. The
edge-colouring theorem proves unconstrained invariant owner matchings;
(11.2) is a constrained perfect-matching/long-subtour theorem.

## 12. Exact scope of the Catalan bypass

For an invariant shortest-cycle factor, every physical component has
length \(p\). A translation-fixed component is a nonzero-voltage quotient
loop, hence an AP wreath. A zero-voltage quotient \(p\)-cycle lifts to
\(p\) physical \(p\)-cycles. This fixes the row count modulo \(p\) and
causes the two-AP-loop law.

For an arbitrary reverse-free quotient matching, a nonzero-voltage
quotient cycle of length \(\ell\) lifts to one translation-fixed physical
cycle of length \(p\ell\). It is not an AP row unless \(\ell=1\). The
total simple physical cycle count is

\[
 \sum_{D:a_D=0}p+\sum_{D:a_D\ne0}1,
\tag{12.1}
\]

and is not forced to equal the Catalan number \(T\). Without the
reverse-free condition, (12.1) instead counts directed permutation cycles
and includes the \(p\) backtracks lifted by a zero-voltage reverse
two-cycle. The only general congruence left is the tautology

\[
 C_{\rm phys}\equiv|\{D:a_D\ne0\}|\pmod p,
\]

which imposes no two-loop law. This is a genuine bypass of the
shortest-cycle obstruction on the prime \(p\equiv1\pmod4\) subsequence.

Proved here are the exact lift, complement interface, component formula,
compiler, and reduction (11.2). Not proved is a matching satisfying
(11.2) for \(H/\sqrt m\to\infty\). No coefficient-one conclusion is
claimed without that final constrained-matching theorem.

## 13. Independent audit status

Three independent proof audits were applied to disjoint parts of this
report.

* The canonical/relabeling audit verified (1.5)--(2.4), the AP obstruction,
  the Catalan congruence, and (3.6)--(3.7). It supplied the distinction
  between the zero total voltage of a full AP traversal and the nonzero
  voltage of its primitive quotient loop.

* The voltage/compiler audit verified the reverse-pair owner count, (5.2),
  the complement identity (6.7), the \(2H+2\) threshold, every index in
  (7.3)--(7.5), and the exact \(2H+1\) constructed collar.

* The exceptional-window audit verified (9.1)--(9.2) and the quantifiers in
  (11.2). It corrected the abstract countermodel normalization: (11.1)
  gives \(\Theta(W/H)\) components and therefore \(\Theta(W)\), not
  \(\Theta(W/H)\), full-collar overhead.

After those corrections, no substantive defect remains in the proved
statements. The existence of a matching satisfying (11.2) remains open.
