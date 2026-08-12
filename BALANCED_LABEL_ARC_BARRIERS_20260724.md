# Centered omitted-label arcs: exact criteria and sharp balance-only barriers

Date: 2026-07-24

## Verdict

Point regularity of an odd-graph component does not by itself supply a
target-dimensional centered arc.  This remains false even after imposing
the exact odd-gap condition obeyed by omitted-edge labels.

There are two precise obstructions.

1.  An infinite family of simple point-regular cycles in `O_m` has no proper
    centered path whose length is a multiple of `2m+1`.  Every length-`n`
    path in this family has integral incidence discrepancy of order `n` and
    centered-vector `L1` norm of order `n^2`.  Its `n=9` member is, up to
    rotation and relabeling, the simple 27-cycle already seen in the PBBS
    audit.
2.  In the purely label-preserving four-edge reconfiguration model, a
    proper balanced component can require linearly many directed-four-cycle
    reversals.  The lower-bound examples still have distinct adjacent
    labels and all same-label cyclic gaps odd.

The positive local statement is also exact.  For the four segments cut by
one alternating eight-cycle, a proper balanced regrouping exists only when
one segment is centered or two segment vectors are opposite.  Thus the
scalable supply target can be sharpened from arbitrary four-vector
cancellation to a supply of zero arcs or opposite arc pairs.

These results do not obstruct an all-dimensional PBBS switching theorem.
They show that such a theorem must use more than coordinate homomesy, label
balance, and the odd-gap rule; in particular, a bounded number of generic
local reversals cannot be its entire mechanism.

## 1. Prefix discrepancy and endpoint correction

Let `lambda_0,...,lambda_{rn-1}` be a cyclic word on `n` labels, each used
exactly `r` times.  Put

\[
 v_x=n e_x-\mathbf 1
\]

for a label `x`, and define the prefix-discrepancy walk

\[
 D(j)=\sum_{i=0}^{j-1}v_{\lambda_i}
 =n\,c(j)-j\mathbf 1.
 \tag{1.1}
\]

Here `c(j)` is the vector of label counts in the first `j` positions.  The
total walk closes: `D(rn)=D(0)=0`.

### Lemma 1 (exact collision criterion)

A cyclic edge-label block is balanced if and only if its two endpoint
prefix discrepancies agree.  Equivalently,

\[
 D(b)=D(a)
 \quad\Longleftrightarrow\quad
 \#_x(\lambda_a,\ldots,\lambda_{b-1})=(b-a)/n
 \quad\hbox{for every }x.
 \tag{1.2}
\]

In particular, a proper point-regular cycle cut out of a point-regular
odd-graph component is exactly a nontrivial self-intersection of `D`.

For a path `P=(A_0,...,A_{kn-1})` in `O_m`, let `t_x` count its `kn-1`
internal edge labels and put

\[
 e_x=1_{x\in A_0}+1_{x\in A_{kn-1}}.
\]

The endpoint-corrected identity from the odd-graph audit gives

\[
 2\iota_x(P)=kn-1-t_x+e_x.
 \tag{1.3}
\]

Consequently `P` is centered if and only if

\[
 \boxed{t_x=k-1+e_x\quad\hbox{for every }x.}
 \tag{1.4}
\]

In discrepancy form, its internal label block must have the exact value

\[
 n t-(kn-1)\mathbf 1
 =n e-(n-1)\mathbf 1.
 \tag{1.5}
\]

If the endpoints are adjacent and the closing edge omits `y`, then
`e=\mathbf 1-e_y`; after adjoining that closing label, (1.4) says precisely
that every label occurs `k` times.  Thus closable centered arcs reduce to
ordinary collisions of (1.1), while general centered arcs hit the
endpoint-dependent targets (1.5).

## 2. An infinite endpoint-corrected obstruction

The next construction includes the actual PBBS obstruction at `n=9` and
extends its discrepancy mechanism to infinitely many odd dimensions.

Let

\[
 n=4k+1\ge 9,
 \qquad d=(n+1)/2=2k+1,
 \qquad 3\nmid d,
 \tag{2.1}
\]

and put `L=3n`.  Since `2d-n=1` and `3` does not divide `d`, one has
`gcd(d,3n)=1`.  On edge positions in `Z_(3n)`, define the label word by

\[
 \boxed{\lambda_{dj}=\lfloor j/3\rfloor,
 \qquad 0\le j<3n.}
 \tag{2.2}
\]

The labels are `0,...,n-1`, with the floor interpreted in the displayed
range.

Each label occurs at the three positions

\[
 d(3a),\quad d(3a+1),\quad d(3a+2)\pmod {3n}.
\]

Their cyclic gaps are

\[
 d,\quad d,\quad 3n-2d=2n-1,
 \tag{2.3}
\]

all odd.  They are all at least five, so adjacent edge labels are distinct.

### Lemma 2 (the word defines a simple point-regular odd-graph cycle)

Word (2.2) defines a simple cycle of length `3n` in

\[
 O_m=KG(n,m),\qquad m=(n-1)/2,
\]

and every ground coordinate occurs in exactly `3m` of its vertices.

### Proof

For one label `x`, declare membership to be zero at both endpoints of every
`x`-labeled edge and toggle membership across every other edge.  Between
successive `x`-labels there are an even number of non-`x` edges by (2.3), so
this prescription is consistent around the cycle.

Across an edge labeled `x`, coordinate `x` is absent at both endpoints and
each of the other `n-1` coordinates occurs at exactly one endpoint.  Thus
successive vertex sizes sum to `n-1=2m`.  The walk length `3n` is odd, so
cyclic closure forces every vertex size to be `m`.  Consecutive vertices
are disjoint and therefore form an odd-graph edge.

Finally, the cyclic label identity

\[
 2\iota_x=3n-3
\]

gives `iota_x=3m` for every coordinate.

It remains to prove simplicity.  Let `b(p)` be the membership of coordinate
zero at vertex position `p`.  The three zero-labeled edges are at
`0,d,2d`.  The label starts `3ad` for `a in Z_n` run through all multiples
of three modulo `3n`.  After relabeling the coordinates, the incidence word
of vertex `A_i` is therefore

\[
 C_s(q)=b(s-3q),
 \qquad s=i\pmod3,quad q\in\mathbb Z_n,
 \tag{2.3a}
\]

up to a cyclic shift by `(i-s)/3`.

Each `C_s` has exactly `m` ones.  It has no proper cyclic period: if a
period `p<n` divided `n`, then `n/p` would divide both its length `n` and
its number `m` of ones, contrary to `gcd(n,m)=1`.  It remains only to check
that the three necklaces `C_0,C_1,C_2` are pairwise different.

This has a short explicit gap check.  Between the three zero-labeled edges,
the membership pattern is alternating, with a repeated zero at each labeled
edge.  More explicitly, for representatives `0<=p<3n`, one has `b(p)=1`
exactly on

\[
 \begin{split}
 &2\le p\le d-1,\quad p\text{ even};\\
 &d+2\le p\le2d-1,\quad p\text{ odd};\\
 &2d+2\le p\le3n-1,\quad p\text{ even}.
 \end{split}
 \tag{2.3b}
\]

Substitution of these three arithmetic progressions in (2.3a) gives the
following cyclic gaps between the ones of `C_s`.  All unlisted gaps equal
two.

If `n=12u+1`, there is one gap of length one and two gaps of length three.
After anchoring the unique length-one gap at gap position zero, the two
length-three gap positions are

\[
 \begin{array}{c|c}
 s&\text{positions of the two 3-gaps}\\ \hline
 0&\{u,5u\}\\
 1&\{u,2u\}\\
 2&\{4u,5u\}.
 \end{array}
 \tag{2.3c}
\]

If `n=12u+9` with `u>=1`, the corresponding positions are

\[
 \begin{array}{c|c}
 s&\text{positions of the two 3-gaps}\\ \hline
 0&\{u+1,2u+1\}\\
 1&\{u+1,5u+3\}\\
 2&\{4u+3,5u+3\}.
 \end{array}
 \tag{2.3d}
\]

The three anchored pairs are distinct in both cases.  For `n=9`, the three
anchored cyclic gap words are, directly,

\[
 (1,4,2,2),\qquad (1,3,2,3),\qquad (1,2,2,4).
 \tag{2.3e}
\]

Thus the three `C_s` are pairwise nonconjugate, while each has orbit size
`n` under cyclic shift.  The `3n` vertices are all distinct.  This completes
the proof of Lemma 2.  QED

The cycle need not be assumed to come from PBBS for the theorem below.

### Theorem 3 (uniform quadratic discrepancy)

Let `P_i` be any `n` consecutive vertices of the cycle from Lemma 2.  There
is an integer `a_i` such that its coordinate-incidence deviations from the
centered value `m` consist of

\[
 a_i\text{ entries }+1,qquad
 a_i\text{ entries }-1,qquad
 n-2a_i\text{ zeroes},
 \tag{2.4}
\]

where

\[
 \boxed{
 \left\lfloor\frac{n-1}{6}\right\rfloor
 \le a_i\le
 \left\lceil\frac{n-1}{6}\right\rceil.
 }
 \tag{2.5}
\]

Consequently no length-`n` path is centered, and

\[
 \boxed{
 \|\zeta_m(P_i)\|_1
 =2n a_i
 \ge 2n\left\lfloor\frac{n-1}{6}\right\rfloor.
 }
 \tag{2.6}
\]

No length-`2n` path is centered either.  Hence the only centered segment
whose length is a multiple of `n` is the full length-`3n` walk.

### Proof

The internal label interval of `P_i` is

\[
 J_i=[i,i+n-2]
\]

and has `n-1` edges.  A label has three occurrences with gaps (2.3), so
`J_i` contains at most two of them.  If it contains two, they are a pair
`p,p+d` with

\[
 p=i+u,qquad 0\le u\le d-3.
 \tag{2.7}
\]

Let `t_x` be the internal count and `e_x` the endpoint count for coordinate
`x`.  Equation (1.3) with `k=1` gives

\[
 \iota_x(P_i)-m=(e_x-t_x)/2.
 \tag{2.8}
\]

If `p,p+d` are the first two occurrences of their label, the preceding
occurrence is at `p-(2n-1)`; if they are the last two, it is at `p-d`.
In the two cases, the number of toggles before vertex `A_i` has parity,
respectively,

\[
 2n-2-u\equiv u\pmod2,
 \qquad
 d-u-1\equiv u\pmod2.
\]

The two path endpoints have the same membership because the number of
internal non-`x` edges is even.  Thus a coordinate has deviation `-1`
exactly when (2.7) holds with `u` even.

Write `e=d^{-1}` modulo `3n`.  The pair `p,p+d` has the same label exactly
when

\[
 ep\pmod3\in\{0,1\}.
 \tag{2.9}
\]

The even offsets in (2.7) are

\[
 u=2v,qquad 0\le v<k.
\]

As `v` increases, `e(i+2v)` advances by the nonzero residue `2e` modulo
three.  Among `k` consecutive terms of this three-cycle, the number lying
in the two-element set `{0,1}` is between `floor(2k/3)` and
`ceil(2k/3)`.  Since `2k=(n-1)/2`, these are the bounds in (2.5).

All deviations in (2.8) belong to `{-1,0,1}`.  Their sum is zero because
all `n` vertices have size `m`, so the number of `+1` deviations equals the
number of `-1` deviations.  This proves (2.4)--(2.6).

The complementary `2n` vertices have incidence vector equal to `3m`
minus that of the omitted `n` vertices.  Their deviation from `2m` is the
negative of the latter deviation from `m`, proving the last assertion.
QED

For `n=9`, (2.2) is, after a rotation and a coordinate relabeling, the
omitted-label word

```text
928139241352463574685796817
```

of the simple PBBS 27-cycle in the odd-eight context audit.  Thus the
endpoint-corrected obstruction already occurs in a genuine factor
component, not only in a closed walk.

### Corollary 3.1 (infinite internal-splitting obstruction)

For infinitely many odd dimensions, there is a simple point-regular
odd-graph cycle of length `3n` which has no proper centered contiguous arc.
In particular, its cyclic vertex order cannot be cut into three centered
length-`n` paths and reclosed as three wreaths.

Indeed, if a path of `ell` middle vertices is centered, its common
coordinate incidence is `m ell/n`; since `gcd(m,n)=1`, one has `n|ell`.
Theorem 3 excludes the only two proper possibilities `ell=n,2n`.

Thus even the conjunction of simplicity, point regularity, correct length
divisibility, and the exact odd-graph label parity rule does not imply
orbitwise wreath splittability.  Inter-component exchange or a genuinely
noncontiguous rebundling is necessary in any general conversion theorem.

## 3. Exact classification of a balanced one-switch split

Let an alternating eight-cycle cut four segments with centered vectors
`u_1,u_2,u_3,u_4`.  If the old touched components are point regular, then

\[
 u_1+u_2+u_3+u_4=0.
 \tag{3.1}
\]

### Lemma 4 (zero-or-opposite criterion)

A proper nonempty subset of `{u_1,u_2,u_3,u_4}` has sum zero if and only if

\[
 \boxed{
 u_i=0\text{ for some }i
 \quad\hbox{or}\quad
 u_i=-u_j\text{ for some }i\ne j.
 }
 \tag{3.2}
\]

Consequently:

* a balanced `(1,3)` split requires and is certified by a zero segment;
* a balanced `(2,2)` split requires and is certified by an opposite pair;
* a balanced `(1,1,2)` split requires two zero segments (the remaining pair
  is then opposite); and
* a balanced four-way split requires all four segments to be centered.

### Proof

A proper subset has size one, two, or three.  Size one gives a zero vector,
size two gives an opposite pair, and a size-three zero sum is equivalent by
(3.1) to the complementary singleton being zero.  The listed partition
types follow immediately.  QED

This reduces the nonlocal supply needed for balanced splitting to two
concrete objects: zero arcs and opposite arc pairs.  A generic cancellation
of four nonzero vectors with no opposite pair can support only the one-group
reconnection; it cannot increase the number of balanced components.

## 4. A linear fragmentation barrier for four-edge trades

The following result concerns the exact label-token operation induced by a
directed-four-cycle reversal.  Give every edge occurrence a token.  In one
alternating-eight switch, map each of the four new edge tokens to the unique
removed token having the same omitted label.  Uniqueness holds because the
four normal-form labels are distinct.  All tokens are thereby preserved,
although their cyclic adjacencies can change.

### Lemma 5 (fragmentation after `t` switches)

After `t` label-preserving four-edge switches, at most `8t` adjacencies of
the initial cyclic token word have disappeared.  Therefore:

1. the token set of any final whole component is a union of at most `4t`
   cyclic intervals of the initial word;
2. the token set of any contiguous arc in a final component is a union of
   at most `4t+1` cyclic intervals of the initial word.

### Proof

Replacing four edge tokens can change only the predecessor and successor
adjacency of each replaced token, hence at most eight token adjacencies.
All other path-internal adjacencies survive that switch.

If a subset is a union of `c` intervals in the initial cyclic order, it has
`2c` selected/unselected boundary adjacencies.  For a final whole component,
every such boundary adjacency must have disappeared, giving `2c<=8t`.
For a final arc, at most its two endpoint adjacencies may survive, giving
`2c-2<=8t`.  QED

Now let `n=3g` be odd, `g>=3`, and let every label occur `r>=2` times.  Split
the labels into consecutive triples and form

\[
 \boxed{
 \mathcal W_{n,r}
 =(1,2,3)^r(4,5,6)^r\cdots(n-2,n-1,n)^r.
 }
 \tag{4.1}
\]

Adjacent labels are distinct.  The cyclic gaps between successive copies
of one label are

\[
 3,\ldots,3,\quad rn-3(r-1)=r(n-3)+3,
 \tag{4.2}
\]

and hence are all odd.  Thus (4.1) satisfies the exact local parity rule of
an odd-graph omitted-label word.

### Lemma 6 (sharp interval complexity in the clustered word)

If a proper token subset of (4.1) contains exactly `k` copies of every
label, where `1<=k<r`, then it is a union of at least

\[
 \boxed{\left\lceil n/6\right\rceil}
 \tag{4.3}
\]

cyclic intervals.  This bound is attained.

### Proof

Inside each of the `g=n/3` triple blocks, the subset contains exactly `3k`
of the `3r` tokens.  Its indicator is therefore nonconstant inside every
triple block, producing at least one selected/unselected transition on an
internal adjacency of that block.  Hence there are at least `g` transitions
in the full cyclic word.  A union of `c` intervals has exactly `2c`
transitions, so `c>=ceil(g/2)=ceil(n/6)`.

For sharpness, choose the first `3k` positions in alternating triple blocks
and the last `3k` positions in the others.  Since `g` is odd, the internal
`g` transitions and one transition at the cyclic block boundaries give
exactly `g+1` transitions, hence `(g+1)/2=ceil(g/2)` intervals.  QED

The linear order in (4.3) is best possible for arbitrary balanced words,
even without using a necklace-splitting theorem.  If every label occurs at
least twice, choose one occurrence of each label.  The resulting proper
balanced token subset is a union of at most `n` singleton intervals.  Thus,
if

\[
 \phi(\lambda)=
 \min\{\text{number of cyclic intervals in a proper balanced token subset}\},
\]

then every balanced word has `phi(lambda)<=n`, whereas the odd-gap words
(4.1) have

\[
 \phi(\mathcal W_{n,r})=\left\lceil n/6\right\rceil.
 \tag{4.4}
\]

So the worst-case label-only fragmentation scale is `Theta(n)`, including
within the class satisfying the odd-gap rule.

### Theorem 7 (linear trade lower bound)

Starting from (4.1), any label-preserving four-edge switch sequence which
creates a proper point-regular component requires at least

\[
 \boxed{
 t\ge \frac14\left\lceil\frac n6\right\rceil
 =\Omega(n)
 }
 \tag{4.5}
\]

switches.

### Proof

A point-regular component of length `kn` has exactly `k` occurrences of
every omitted edge label.  Its abstract token set is therefore a balanced
proper subset of (4.1).  Lemma 6 says it has at least `ceil(n/6)` initial
intervals, while Lemma 5 says it has at most `4t`.  QED

If `r` is odd, (4.2) constructs a point-regular closed walk in `O_m` by the
same argument as Lemma 2.  It is generally not simple.  The purpose of
Theorem 7 is exact: even label balance, distinct consecutive labels, the
odd-gap rule, and point regularity of the closed walk do not imply a
bounded-switch centered decomposition.  Simplicity or more detailed PBBS
geometry must enter any positive theorem.

## 5. Consequence for the switching program

The omitted-label problem now has three sharply separated levels.

1. **Balance only.**  Prefix discrepancy closes only after the full
   component.  It need not self-intersect earlier.
2. **Odd-graph local feasibility.**  Requiring distinct adjacent labels and
   odd same-label gaps still does not force even an endpoint-corrected
   centered arc; Theorem 3 gives quadratic centered-vector discrepancy.
3. **Balanced switching.**  One proper alternating-eight split needs a zero
   arc or an opposite pair (Lemma 4), and generic label-preserving local
   surgery can require linearly many trades (Theorem 7).

Accordingly, the next positive theorem should target one of the following
PBBS-specific statements rather than arbitrary coordinate homomesy:

* a positive density of zero prefix-discrepancy collisions;
* a positive density of opposite pairs of arc vectors compatible with one
  normal-form connector; or
* a global route using `Theta(n)` coordinated reversals while maintaining
  point-regular components throughout.

The finite `KG(9,4)` certificate demonstrates that the third mechanism can
work in one dimension.  The results above explain why a dimension-free
bounded local template is not forced by the currently known homomesy.
