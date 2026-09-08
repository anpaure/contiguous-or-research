# Gate C: exact factor-adapted antipodal-swap coherent tours

**Status (2026-08-22).**  Every assertion below is proved.  For every odd
`b` and every `j` with `4j<=b-1`, an explicit product of `j` antipodal
coordinate transpositions turns the descending coherent tour into a
staircase-parity tour whose two phases both have exact intersection
\[
 M_j=b(b-1)-\bigl((4j+1)b-9j+2\bigr)                     \tag{0.1}
\]
with the Catalan-switched central factor.  When `4j=b-1`, the right side
of (0.1) is increased by one.  Thus
\[
                         M_j=q-O(bj).                     \tag{0.2}
\]
In particular, `j=a_b sqrt(b)` with `a_b->infinity` slowly and
`j=o(b)` gives the first explicit factor-adapted coherent tours at the
exhaustive parity-band scale, with `q-o(q)` retained flags.

This is an existence theorem for one tour in each width, not the remaining
packing theorem.  Choosing `j=o(b)` swap locations supplies only
`exp(o(b))` evident variants, far below the required
`Theta(4^b/b^(5/2))` supports.  Exponential factor-adapted entropy and
rankwise-disjoint rounding remain open.

Throughout,
\[
 n=2b,qquad b\ge5\text{ odd},qquad q=b(b-1).             \tag{0.3}
\]

## 1. The exact factor test and coherent template

Coordinates are ordered `0,1,...,2b-1`.  Begin with the ordered
Greene--Kleitman decomposition, obtained by pairing every zero with the
latest unpaired one to its left.  For every primitive Dyck word
`D=1D'0`, replace the middle `C_D=0D'1` of its crossing chain by the
alternate middle `D` of the same Boolean diamond, and exchange the
corresponding singleton middle chains.  These simultaneous switches define
the genuine Catalan-switched SCD and its central flag factor `F*`.

For a middle set `C` and `p in C`, rotate its membership word to start at
`p`.  A word is Dyck if
all prefix heights are nonnegative and its final height is zero; it is
primitive if every proper nonempty prefix has positive height.

The Catalan-switched factor `F*` has the following exact membership test
for a flag
\[
 F=(C\setminus\{p\},C,C\cup\{q\}).                       \tag{1.1}
\]
It belongs to `F*` precisely when either

* `q<p`, `(p,q)!=(2b-1,0)`, the rotation at `p` is Dyck, and its first
  return is at `q`; or
* `(p,q)=(0,2b-1)` and `C` is primitive Dyck.

To see the test, view the middle word as a balanced walk.  Its rightmost
unpaired zero is the first arrival at the final global minimum, and its
leftmost unpaired one is the up-step after the last visit to that minimum.
Rotating at this one therefore gives a Dyck word whose first return is the
unpaired zero; the converse follows by reversing the same minimum argument.
Moreover, a GK flag has arc `(2b-1)->0` exactly when its middle is
`0D'1` with `D'` Dyck: the displayed endpoints are the only unpaired
symbols, so every intervening symbol is paired internally, and conversely
that internal Dyck pairing leaves precisely those endpoints unpaired.
Thus the switches delete **all** `(2b-1)->0` flags and insert exactly the
primitive `0->(2b-1)` flags.  This proves the two bullets.

In particular, if the arc is the cyclic predecessor arc `r->r-1`, then
membership is equivalent to the rotation at `r` being primitive Dyck.
This includes `r=0`, where the second bullet applies.  Every factor arc
joins opposite coordinate parities: a Dyck first-return block has even
length, forcing `p-q` odd in the first bullet, and `2b-1` is odd in the
second.

Let `H=(h_0,...,h_{2b-1})` be a directed Hamilton listing.  For a phase
`delta in {0,1}`, stage `0<=s<b`, and `1<=t<b`, put
\[
 z=\delta+s(b+1)\pmod {2b}.                               \tag{1.2}
\]
The corresponding internal coherent flag has H-index middle and arc
\[
 J=z+([t,b+t]\setminus\{b\}),qquad
 h_{z+b+t}\longrightarrow h_{z+b+t+1}.                  \tag{1.3}
\]
These are the `q` internal flags of one coherent phase.

## 2. The antipodal-swap labelling

Start with the descending Hamilton listing
\[
 H^*=(0,2b-1,2b-2,\ldots,1),qquad h_i^*=-i\pmod {2b}.    \tag{2.1}
\]
For
\[
 A_j=\{1,5,9,\ldots,4j-3\},                              \tag{2.2}
\]
swap the labels at H-positions `a` and `a+b` for every `a in A_j`.
Call the resulting listing `H^(j)`.

Equivalently, define the residue set
\[
 X=\{b-1-4u:0\le u<j\}\subseteq\mathbb Z_b              \tag{2.3}
\]
and let `pi` swap the two coordinates `x` and `x+b` for every `x in X`.
Then
\[
                         H^{(j)}=\pi(H^*).                \tag{2.4}
\]
The equivalence follows because the two labels at positions `a,a+b` in
(2.1) are `2b-a` and `b-a`, with common residue `b-a` modulo `b`.

The parity word of `H^(j)` is the antipodal staircase: it is alternating
except at the flipped position pairs in (2.2), and has exactly `4j`
same-parity Hamilton edges.

## 3. Canonical interval coordinates

For a template (1.3), define
\[
                         r=-z-b-t\pmod {2b}.              \tag{3.1}
\]
Under the descending listing (2.1), its middle and arc become
\[
 C^0_{r,t}=r+([0,b]\setminus\{t\}),qquad
                         r\longrightarrow r-1.           \tag{3.2}
\]
Indeed the coordinate corresponding to H-index `z+u` is `-z-u`, whose
offset from `r` is `b+t-u`; the two pieces of (1.3) therefore give
`[t+1,b]` and `[0,t-1]`.

For `H^(j)`, the flag is exactly `pi` applied to (3.2).  For fixed `t`
and either fixed phase, (1.2) and (3.1) give
\[
                         r\equiv-\delta-s-t\pmod b.       \tag{3.3}
\]
Thus `s->r mod b` is a bijection.  It is enough to count the pairs
\[
                         (r,t)\in\mathbb Z_b\times[1,b-1], \tag{3.4}
\]
and the answer is automatically identical in the two phases.
Indeed `pi` commutes with translation by `b`, and rotating a translated
middle at its translated arc start gives the identical relative step word;
factor membership therefore depends only on `r mod b`.

If `r in X` or `r-1 in X`, exactly one endpoint of the predecessor arc is
moved to its antipode.  Its two new endpoints have the same coordinate
parity, so no such flag lies in `F*`.  Hence assume
\[
                         r,r-1\notin X.                   \tag{3.5}
\]
The arc remains `r->r-1`.  Membership is now exactly the primitive-Dyck
condition from Section 1.

## 4. The toggle-height criterion

Rotate at `r`.  Before applying `pi`, the step word of (3.2) has plus
steps at
\[
                         [0,b]\setminus\{t\}              \tag{4.1}
\]
and minus steps elsewhere.  Put
\[
 D_r=\{x-r\pmod b:x\in X\}\subseteq[0,b-1],qquad
 D=D_r\setminus\{t\}.                                   \tag{4.2}
\]
Under (3.5), neither `0` nor `b-1` belongs to `D_r`.  Each `d in D`
moves a plus step from position `d` to its antipode `d+b`.  A value
`d=t` causes no change because the corresponding coordinate pair is empty
in (3.2).

Let `H_0(ell)` be the prefix height before these moves and `H(ell)` the
height afterward.  For `1<=ell<=2b`,
\[
 H(\ell)=H_0(\ell)
 -2|\{d\in D:d<\ell\le d+b\}|,                           \tag{4.3}
\]
where
\[
 H_0(\ell)=
 \begin{cases}
 \ell,&1\le\ell\le t,\\
 \ell-2,&t<\ell\le b+1,\\
 2b-\ell,&b+1<\ell\le2b.
 \end{cases}                                             \tag{4.4}
\]

Write `D={d_1<...<d_k}` and put
`a=|{d in D:d<t}|`.  Inspection of the local minima in (4.3) gives the
following exact criterion.

### Lemma 4.1 (primitive-toggle criterion)

The rotated word is primitive Dyck if and only if
\[
\begin{aligned}
 t&\ge2a+2,                                               &&\tag{4.5a}\\
 d_i&\ge2i,                 &&d_i<t,                     &&\tag{4.5b}\\
 d_i&\ge2i+2,               &&d_i>t,                     &&\tag{4.5c}\\
 d_i&\le b-2(k-i+1)-1,      &&1\le i\le k.              &&\tag{4.5d}
\end{aligned}
\]

#### Proof

In the first half, height can acquire a new minimum only immediately
after the deleted position `t` or immediately after a moved plus step
`d_i`.  Formula (4.3) gives respectively
\[
 t-1-2a,qquad d_i+1-2i\ (d_i<t),qquad
 d_i-1-2i\ (d_i>t).                                     \tag{4.6}
\]
Their strict positivity is exactly (4.5a)--(4.5c).  In the second half,
the possible new minima occur at prefix length `b+d_i`; their heights are
\[
                         b-d_i-2(k-i+1),                  \tag{4.7}
\]
whose strict positivity is (4.5d).  Between these listed locations the
height moves monotonically away from the preceding local minimum.
The final height is zero automatically.  Thus the listed inequalities are
necessary and sufficient for every proper prefix to be positive.
\(\square\)

The deletion convention in this criterion is literal.  If
`t notin D_r`, then `D=D_r`, `k=j`, and the indices `i` in (4.5) are the
ranks in the full ordered toggle list.  If `t=d_m in D_r`, that antipodal
pair is empty in the base middle and is not toggled: delete `d_m`, set
`k=j-1`, and reindex every later element down by one.  Inequality (4.5a)
is the minimum immediately after the deleted base step.  Inequalities
(4.5b) and (4.5c) are the minima immediately after a moved plus step,
according as it lies before or after the deletion.  Inequality (4.5d) is
the matching second-half minimum immediately before that plus reappears.
Thus no generic or deleted-`t` case is suppressed.

## 5. Exact case census

First suppose
\[
                         4j\le b-3,qquad c=b-4j\ge3.     \tag{5.1}
\]
Then
\[
                         X=\{c+3,c+7,\ldots,b-1\}.        \tag{5.2}
\]
Substitution of the step-four lists `(X-r) mod b` into Lemma 4.1 gives
the following complete, disjoint table.  Here all residues are modulo
`b`, and `X+u={x+u:x in X}`.

\[
\begin{array}{c|c|c}
\text{residue }r&\text{admissible }t&\text{count}\\ \hline
X\cup(X+1)&\varnothing&0\\
X-1&\varnothing&0\\
X+2&\{b-2\}&1\\
2\le r\le c-1&\{2,3,\ldots,b-1\}&b-2\\
r=c&\{3,4,\ldots,b-1\}&b-3\\
r=c+1&\{2,4,5,\ldots,b-1\}&b-3.
\end{array}                                               \tag{5.3}
\]

For completeness, the arithmetic behind the last four rows is as follows.
For `2<=r<=c-1`, the ordered list is
\[
 d_i=c+4i-1-r\quad(1\le i\le j).                         \tag{5.4}
\]
It satisfies (4.5) for every `t>=2`.  At `r=c`, the list starts
`3,7,11,...`, so only `t=2` newly violates (4.5c).  At `r=c+1`, it starts
`2,6,10,...`; deleting `t=2` is allowed, `t=3` violates (4.5a), and every
`t>=4` is allowed.  If `r=x_\kappa+2` for the `\kappa`-th member of `X`,
then
\[
 D_r=\{2,6,\ldots,4(j-\kappa)-2\}
 \cup\{b-4\kappa+2,b-4\kappa+6,\ldots,b-2\}.            \tag{5.5}
\]
Lemma 4.1 permits exactly `t=b-2`.  Indeed, if `t!=b-2`, the largest
effective toggle is still `b-2`; (4.5d) would require `b-2<=b-3`, an
impossibility.  If `t=b-2`, delete that last toggle.  Every remaining
toggle precedes `t`, and (4.5a) reduces to
`b-2>=2(j-1)+2=2j`.  On the low string of (5.5), rank `i` has
`d_i=4i-2>=2i`.  On the high string, write its rank as
`i=j-\kappa+s`, where `1<=s<\kappa`; then
\[
 d_i=b-4\kappa+4s-2\ge2(j-\kappa+s)=2i                  \tag{5.5a}
\]
because `b>=4j+1`.  The upper bounds (4.5d) are respectively
\[
 4i-2\le b-2(j-i)-1,
 \qquad
 b-4\kappa+4s-2\le b-2(\kappa-s)-1,                     \tag{5.5b}
\]
which follow from `i<=j` and `s<\kappa`.  Hence `t=b-2` satisfies every
inequality and is the unique admissible value.

Finally `r in X-1` puts `1` in
`D_r`; `t=1` already makes the base word nonprimitive, and every other
`t` violates (4.5b).  The first row was disposed of by arc parity.
This proves the table without an omitted residue class.

There are `j` singleton rows, `b-4j-2` full rows, and two boundary rows.
Therefore either phase has exactly
\[
\begin{aligned}
 M_j
 &=j+(b-4j-2)(b-2)+2(b-3)\\
 &=b^2-(4j+2)b+9j-2.                                    \tag{5.6}
\end{aligned}
\]
Since `q=b(b-1)`, its loss is
\[
 \boxed{L_j=q-M_j=(4j+1)b-9j+2.}                         \tag{5.7}
\]

It remains to handle the packed endpoint case `4j=b-1`, possible when
`b=1 mod 4`.  Now
\[
                         X=\{4,8,\ldots,b-1\}.            \tag{5.8}
\]
The sets `X`, `X+1`, and `X-1` again give zero; every residue in `X+2`
gives only `t=b-2`; and the sole remaining residue `r=2` permits every
`t>=2` except `t=3`.  Thus
\[
 M_j=j+(b-3)=b+j-3,                                     \tag{5.9}
\]
which is one more than (5.6).  Equivalently,
\[
 \boxed{L_j=(4j+1)b-9j+1\qquad(4j=b-1).}                 \tag{5.10}
\]

Equations (5.7) and (5.10) prove the announced exact theorem.

## 6. Consequences and remaining gate

For every `j=o(b)`, the explicit tours retain
\[
                         q-O(bj)=(1-o(1))q               \tag{6.1}
\]
flags of the fixed genuine central factor.  Taking
`j=a_b sqrt(b)` with `a_b->infinity` and `a_b=o(sqrt(b))` reaches a parity
band containing `1-o(1)` of all middle targets, while the per-tour defect
is `O(a_b b^(3/2))=o(q)`.  At `N/q` tours this scale would create only
`o(N)` aggregate repair.

What is not supplied is multiplicity.  The displayed construction gives
one coordinate labelling for each chosen swap set.  Even allowing all
`j`-subsets of the `b` antipodal pairs yields at most
\[
                         \binom bj=\exp(o(b))             \tag{6.2}
\]
when `j=o(b)`, whereas a fixed-fraction packing needs
`Theta(4^b/b^(5/2))` distinct near-full supports.  The exact remaining
Gate-C theorem is therefore an exponential factor-adapted labelling family
with controlled codegrees and a rankwise-disjoint near-perfect matching,
or an equivalent residual coverdown construction.

## 7. Finite audit

The companion checker
`scratch/verify_gate_c_antipodal_swap_factor_adapted_tour_20260822.py`
verifies the coherent-to-canonical interval conversion, the toggle-height
criterion, every row of the case census, both phase overlaps, and the two
exact formulas.  It is confirmatory; the proof above is self-contained.
