# Independent audit of `MULTISCALE_SLAB_FUSION.md`

## 1. Verdict

The main mathematics is sound.

In particular, the following claims check out exactly:

1. the nested-hook symmetric-chain count
   \[
   (h+1)(a+1)-\Psi((h+a-b)_+);
   \]
2. the physical connector length and its max-window witnesses;
3. the disjoint two-slab construction and formula (1.1);
4. the formula and superadditivity of \(\Psi\);
5. the boundary-antichain count (1.6), the layer difference (1.8), and
   the separated-word lower bound (1.9);
6. all displayed asymptotic coefficients; and
7. the complementary-line portal identity.

There are three scope qualifications, none of which invalidates the main
theorems.

* Formula (1.2) is the exact saving relative to the explicitly used uniform
  baseline \(2t(m+1)(2m+1)\).  If the two zero-coordinate slice gadgets in
  that old baseline are each trimmed by their deletable global zero, the
  comparison changes by two positions; see Section 5 below.
* The superadditivity argument proves one-piece optimality for subdivisions
  of the first rectangular slab into height bands using the same SCD
  connector.  It does not prove exact optimality among every conceivable
  partition of the entire L-shaped region.
* Theorem B is deliberately a lower bound for the **separated** architecture:
  the boundary witnesses must be wholly inside a disjoint auxiliary word.
  It is not a lower bound for words using cross-spine intervals.  That scope
  is essential and is consistent with Section 6 of the source.

Proposition 6.3 is a correct sufficient reduction, not an existence theorem:
the coverage requirement is included in the definition of a portal braid.

## 2. Audit of the connector and SCD count

### 2.1 The elementary connector

Let

\[
C=(c_0<c_1<\cdots<c_p),\qquad D=[0,q].
\]

The displayed word

\[
(c_p,0),(c_{p-1},0),\ldots,(c_0,0),(c_0,1),\ldots,(c_0,q)
\]

has exactly

\[
(p+1)+q=p+q+1=|C|+q
\]

letters.  For \(0\le i\le p\) and \(0\le j\le q\), the interval from
\((c_i,0)\) to \((c_0,j)\) has coordinatewise maximum \((c_i,j)\).
Thus it covers all of \(C\times D\).

Deleting the unique global zero is safe.  After deletion:

* \((c_i,0)\), \(i>0\), is still available as a singleton;
* \((c_0,j)\), \(j>0\), is still available as a singleton; and
* for \(i,j>0\), the interval from \((c_i,0)\) through \((c_0,j)\)
  remains contiguous and has the same maximum.

Consequently, if a finite ranked poset \(P\) is partitioned into \(r\)
symmetric chains, concatenating these connectors gives a nonzero word for
\(P\times[0,c]\) of exact length

\[
|P|+cr-1.                                                     \tag{2.1}
\]

### 2.2 Nested hooks in three coordinates

For \(0\le h\le a\le b\), the standard hook decomposition of
\([0,h]\times[0,a]\) has chains indexed by \(u=0,\ldots,h\), with edge
heights

\[
q_u=h+a-2u.
\]

The product of the \(u\)-th chain with \([0,b]\) has a hook SCD with
\(\min(q_u,b)+1\) chains.  Hence the total chain count is

\[
\begin{aligned}
r
 &=\sum_{u=0}^{h}(\min(q_u,b)+1)\\
 &=\sum_{u=0}^{h}(q_u+1)
   -\sum_{u=0}^{h}(h+a-b-2u)_+\\
 &=(h+1)(a+1)-\sum_{u\ge0}(h+a-b-2u)_+.
\end{aligned}
\]

Because \(b\ge a\), one has \((h+a-b)_+\le h\), so extending the last
sum to all \(u\ge0\) adds no terms.  For every integer \(d\ge0\),

\[
\sum_{u\ge0}(d-2u)_+
=\left\lceil\frac d2\right\rceil
 \left(\left\lfloor\frac d2\right\rfloor+1\right)
=\Psi(d).                                                       \tag{2.2}
\]

Thus

\[
r=(h+1)(a+1)-\Psi((h+a-b)_+),                                  \tag{2.3}
\]

as claimed.  The nested hooks are saturated and symmetric, so this is an
actual chain decomposition, not merely a count of the central coefficient.

### 2.3 Four-coordinate length

The first three coordinates have volume
\((h+1)(a+1)(b+1)\).  Substitution of (2.3) into (2.1) gives

\[
\begin{aligned}
&(h+1)(a+1)(b+1)
+c\big((h+1)(a+1)-\Psi((h+a-b)_+)\big)-1\\
&\qquad=(h+1)(a+1)(b+c+1)-1
-c\Psi((h+a-b)_+),
\end{aligned}
\]

which is exactly (3.3).  Every claimed target has an explicit internal
connector witness, so this is a physical word rather than a shadow-only
enumeration.

## 3. Audit of the L-slab construction

### 3.1 The line spine

For fixed \((c,d)\), the values in (2.1) are exactly all legal solutions
of

\[
x_1+x_2=R-c-d.
\]

Different \((c,d)\) give disjoint lines, so their concatenation is a
permutation of \(L_R\) and has length \(|L_R|\).

If \(y\in L_{R+s}\) and \(y_1,y_2\ge s\), then

\[
y-se_1,\qquad y-se_2
\]

are legal rank-\(R\) points in the same complete line.  The intervening
segment has maximum \(y\).  Conversely, a segment of rank-\(R\) line
points whose maximum has excess \(s\) has endpoint separation \(s\), so
both maximized line coordinates are at least \(s\).  Thus the line
criterion used later for the central boundary is exact.

### 3.2 The disjoint partition

The regions

\[
S_1=\{x:x_1<t\},\qquad
S_2=\{x:x_1\ge t,\ x_2<t\}
\]

are disjoint and their union is precisely
\(\{x:x_1<t\text{ or }x_2<t\}\).

For \(S_1\), the sorted side lengths are

\[
t-1,m,m,m.
\]

Equation (3.3) therefore gives

\[
t(m+1)(2m+1)-1-m\Psi(t-1).                                    \tag{3.1}
\]

The omitted point is the global zero.  Every target in Theorem A has rank
at least \(R\ge1\), so omitting it loses no required witness.

For \(S_2\), translate \(x_1\) by \(-t\) and permute the first two local
coordinates.  The sorted side lengths are

\[
t-1,m-t,m,m.
\]

The condition

\[
t\le\left\lfloor\frac{m+1}{2}\right\rfloor
\]

is exactly what is needed for \(t-1\le m-t\).  The defect is zero because

\[
(t-1)+(m-t)-m=-1.
\]

The local origin translates to \((t,0,0,0)\), which is nonzero and must be
retained.  The exact length is therefore

\[
t(m-t+1)(2m+1).                                                \tag{3.2}
\]

If the line criterion fails for a target of excess \(0\le s\le t\), then
one of \(y_1,y_2\) is below \(s\), hence below \(t\).  The target lies in
exactly one of \(S_1,S_2\), and the corresponding universal connector word
represents it internally.

Adding \(|L_R|\), (3.1), and (3.2) gives

\[
|L_R|+t(2m-t+2)(2m+1)-1-m\Psi(t-1),
\]

which verifies (1.1).

### 3.3 Range and nonzero audit

The theorem has content only for \(m\ge1\), which follows from the
existence of an integer \(t\ge1\) in its stated range.  The other range
conditions have the following roles.

* \(R\ge1\) makes every line-spine letter nonzero.
* \(R+t\le4m\) keeps every target layer inside \([0,m]^4\).
* \(t\le\lfloor(m+1)/2\rfloor\) both orders the sides of \(S_2\) and later
  implies \(2t-2\le m\) in the antichain count.
* The zero in \(S_1\) is deleted; the translated origin in \(S_2\) is
  nonzero and retained.  Thus the complete concatenated word has no zero
  letters.

Corollary 3.1 should formally take integer \(q\ge1\); the case \(q=0\) is
the trivial no-extension case and can be handled separately.  Its condition
\(2q\le(m+1)/2\) is exactly the substitution \(t=2q\) into Theorem A.

## 4. The defect function and asymptotic accounting

For \(d=2v\), (2.2) is \(v(v+1)\); for \(d=2v+1\), it is \((v+1)^2\).
In particular,

\[
\Psi(t-1)=\left\lfloor\frac{t^2}{4}\right\rfloor.               \tag{4.1}
\]

For positive integers \(a,b\), each summand satisfies

\[
(a+b-1-2j)_+
\ge(a-1-2j)_+ +(b-1-2j)_+.
\]

If both right summands are positive, the difference is exactly \(1+2j\);
if only one is positive, the inequality is immediate.  Summing proves

\[
\Psi(a+b-1)\ge\Psi(a-1)+\Psi(b-1).                              \tag{4.2}
\]

Iterating (4.2) proves (4.3) for a partition of the first slab into
positive-height bands.  The unique band beginning at coordinate zero can
delete its local origin; every translated band must retain its nonzero
origin.  Hence the common single \(-1\) correction does not reverse the
inequality.

This proves optimality against exactly that class of height-band
subdivisions.  It should not be enlarged to an exact optimality claim for
arbitrary nonrectangular partitions or different assignments of the
L-shaped overlap.

Expanding the auxiliary term in (1.1) and using (4.1) gives

\[
\begin{aligned}
&t(2m-t+2)(2m+1)-1-m\Psi(t-1)\\
&=4tm^2+(6t-2t^2)m+(2t-t^2)-1
-m\left\lfloor\frac{t^2}{4}\right\rfloor\\
&=4tm^2-\frac94t^2m+O(tm+t^2).
\end{aligned}
\]

Thus (1.3) is correct, and throughout the allowed range this remains
\(\Theta(tm^2)\).

## 5. Exact saving: baseline qualification

Let

\[
G=(m+1)(2m+1).
\]

Relative to the explicitly declared old uniform cost \(2tG\), subtraction
of the new auxiliary length gives

\[
2tG-
\big[t(2m-t+2)(2m+1)-1-m\Psi(t-1)\big]
=t^2(2m+1)+m\Psi(t-1)+1,
\]

so (1.2) is algebraically exact for that baseline.

There is a minor comparison nuance.  In the old independent fan, the
\(x_1=0\) and \(x_2=0\) three-box gadgets can each delete their global-zero
letter.  If both obvious trims are taken, that fan has cost \(2tG-2\), and
the saving becomes

\[
t^2(2m+1)+m\Psi(t-1)-1.                          \tag{5.1}
\]

This changes only an additive constant.  It does not affect Theorem A,
the \(\Theta(tm^2)\) conclusion, or any asymptotic coefficient.  Formula
(1.2) should simply be read as comparison with the uniform old accounting
used in the predecessor construction, not with the optimally zero-trimmed
version of that fan.

## 6. Boundary antichain and separated lower bound

### 6.1 Exact boundary count

Fix \(y_1=a<t\).  Complementing the other three coordinates changes their
sum from \(2m-a\) to \(m+a\).  Since \(a<m\) in the stated range, ordinary
inclusion-exclusion gives

\[
\#\{(y_2,y_3,y_4):y_2+y_3+y_4=2m-a\}
=\binom{m+a+2}{2}-3\binom{a+1}{2}.                \tag{6.1}
\]

If also \(y_2=b<t\), then \(a+b\le2t-2\le m\).  The number of legal
\((y_3,y_4)\) with sum \(2m-a-b\) is therefore \(a+b+1\).  The overlap sum
is

\[
\sum_{a,b=0}^{t-1}(a+b+1)=t^3.
\]

Inclusion-exclusion and elementary summation yield

\[
|\mathcal B_{m,t}|
=tm^2+t(t+2)m+\frac{t(5+3t-5t^2)}3,              \tag{6.2}
\]

which verifies (1.6).

### 6.2 Antichain endpoint bound

All members of \(\mathcal B_{m,t}\) have rank \(2m\), so they form an
antichain under coordinatewise order.  If two selected witness intervals
have the same left endpoint or the same right endpoint, one interval
contains the other.  Their maxima would then be comparable.  Therefore a
word of length \(n\) contains witnesses for at most \(n\) distinct members
of any antichain.

It follows immediately that an auxiliary physical word \(V\) containing
all the distinguished witnesses internally must satisfy

\[
|V|\ge|\mathcal B_{m,t}|.
\]

This proof is independent of how the letters of \(V\) are described
logically.  It also shows why the word **occurrences**, rather than shared
recursive descriptions, are the relevant resource.

The scope is important: the proof assumes those witnesses are wholly in
the auxiliary occurrences.  It gives no such tax to a target represented
by an interval crossing a line-spine seam.

### 6.3 Rank-layer difference and total length

For \(R=2m-t\), inclusion-exclusion in the four-box gives

\[
|L_{2m-t}|
=\binom{2m-t+3}{3}-4\binom{m-t+2}{3},             \tag{6.3}
\]

with the standard convention \(\binom uv=0\) for \(u<v\).  There are no
double-bound terms because \(2m-t<2(m+1)\).  Subtracting (6.3) from the
central coefficient gives

\[
M_m-|L_{2m-t}|
=t^2m+t-\frac{t(t-1)^2}{2}.                       \tag{6.4}
\]

The total length of the separated concatenation is at least
\(|L_{2m-t}|+|\mathcal B_{m,t}|\).  Subtracting (6.4) from (6.2) therefore
gives the exact excess over width

\[
tm(m+2)-\frac{7t(t^2-1)}6,                        \tag{6.5}
\]

which is (1.9).

For \(t=o(m)\), (6.5) is

\[
(1-o(1))tm^2.
\]

For \(t=\alpha m+O(1)\),

\[
(6.5)=\left(\alpha-\frac76\alpha^3\right)m^3+O(m^2).
\]

For \(0<\alpha\le1/2\), its coefficient is positive because

\[
1-\frac76\alpha^2\ge1-\frac7{24}>0.
\]

Thus (1.10) and (1.11) are correct.

The word "sharp" in Theorem B is justified for the isolated antichain tax:
listing the members of \(\mathcal B_{m,t}\) as singleton letters attains
\(|V|=|\mathcal B_{m,t}|\).  It does not assert that this literal list also
solves every other band target at the total lower-bound length.

## 7. Portal lemma and reduction

In Lemma 6.1, legality of the arms means

\[
v_i\ge a,\quad v_{i'}+a\le m,
\qquad v_{j'}\ge b,\quad v_j+b\le m.
\]

Because \(i,i',j,j'\) are distinct, all points in the two arms retain rank
\(R\), and all displayed portal maxima remain in \([0,m]^4\).

For the interval from \(A_u\) through \(B_w\):

* coordinate \(i\) is maximized by \(v\);
* coordinate \(i'\) is maximized by \(A_u\), at \(v_{i'}+u\);
* coordinate \(j\) is maximized by \(B_w\), at \(v_j+w\);
* coordinate \(j'\) is maximized by \(v\); and
* every other coordinate is fixed.

Hence the maximum is exactly

\[
v+ue_{i'}+we_j.
\]

The cases \(u=0\) or \(w=0\) use the single displayed occurrence of
\(v=A_0=B_0\), so there is no duplicate-origin ambiguity.  The lemma is
therefore exact.

If a portal braid satisfying Definition 6.2 exists, its defining physical
word already represents every required target.  Its length is
\(|L_R|+E\), and unimodality of the product of four chains gives
\(|L_R|\le M_m\).  Thus \(E=o(m^3)\) implies

\[
|L_R|+E\le M_m+o(m^3).
\]

Proposition 6.3 is consequently correct.  It is intentionally a reduction:
condition 4 of the definition contains the unresolved global rectangle
assignment.  The raw \(\Theta(m^4)\) capacity calculation is dimensionally
correct but does not prove disjointness, bounded overlap, or contamination
control.

## 8. Independent finite checks

I implemented the hook SCD, the connector word, the completed line spine,
the translated L-slab word, and direct enumeration of all contiguous
coordinatewise maxima.  The following checks all passed.

1. **Connector/SCD:** 200 boxes with
   \[
   0\le h\le4,\quad h\le a\le5,\quad a\le b\le c\le6.
   \]
   For each box, the chain count agreed with (2.3), the word length agreed
   with (3.3), every nonzero box point occurred as a contiguous maximum,
   and every letter was nonzero.
2. **Full slab theorem:** all 114 admissible triples \((m,t,R)\) with
   \(1\le m\le5\), all allowed \(t\), and every
   \(1\le R\le4m-t\).  Every point in
   \(L_R\cup\cdots\cup L_{R+t}\) was represented, and the exact word length
   agreed with (1.1).
3. **Counting formulas:** direct enumeration for every \(m\le30\) and every
   allowed \(t\) agreed with (1.6), (1.8), and (1.9).
4. **Defect arithmetic:** (4.1) and superadditivity were checked for
   \(d\le100\) and \(a,b\le100\).
5. **Portal identity:** exhaustive legal arms in the fixed complementary
   orientation for all \(m\le7\) agreed with (6.3) for every \((u,w)\).

These finite checks are not substitutes for the proofs above, but they
cover the boundary cases where zero deletion, translated origins, side
ordering, and binomial conventions are most likely to cause errors.

## 9. Final ledger

### Proved as stated

* The fused L-slab word and length (1.1).
* The saving (1.2) relative to the declared uniform old baseline.
* The asymptotic expansion (1.3) and \(\Theta(tm^2)\) order.
* Superadditivity of \(\Psi\) and nonimprovement under height-band
  subdivision of the first slab with the same connector.
* The exact boundary count, separated antichain tax, rank-layer difference,
  and total separated lower bound.
* The portal equation and the portal-braid sufficient reduction.

### Qualifications to preserve

* Use (5.1), rather than (1.2), when comparing with the independently
  zero-trimmed old fan.
* Do not promote the Section 4 argument to optimality over arbitrary slab
  geometries.
* Do not promote Theorem B to a lower bound for cross-spine or seam-portal
  words.
* Do not treat Proposition 6.3 or the raw rectangle capacity as a portal
  braid existence proof.

Subject to those explicit scope statements, the source is mathematically
consistent and its main architectural conclusion is valid: internal slab
fusion improves constants, while escaping the separated \(\Theta(tm^2)\)
tax requires witnesses that use the main spine, such as seam portals.
