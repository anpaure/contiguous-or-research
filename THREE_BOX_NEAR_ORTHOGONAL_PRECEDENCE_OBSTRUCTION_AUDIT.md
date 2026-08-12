# Audit of the quadratic hook-precedence obstruction

## 1. Verdict

The four-point certificates, their gap supports, congestion two, the
quadratic cut bound, and the `7/6` endpoint-length consequence are correct
for the stated **pure-refinement** model: begin with the audited hook pair
(or any orthogonal one-prefix/one-suffix rematching of the same pieces), cut
chain gaps, and do not subsequently merge the resulting pieces across old
chains.

The extension to every orthogonal one-prefix/one-suffix matching is also
correct.  The proof does not depend on the inner-shift formula.

The cap-seam comparability calculation is correct, as is the conclusion that
no lower cap half can be joined directly to an upper cap half while the left
hook partition remains unchanged.  The source does not quite prove its
stronger `Theta(W_m)` chain-count sentence: it does not discuss lower--lower,
upper--upper, or cap-half--uncut-chain mergers.  The conclusion is repairable
by a short rank argument supplied in Section 7 below.  With that addition,
every final right chain contains at most one cap half, so the cap halves alone
force at least `m(m+1)` right chains and an asymptotic `Theta(W_m)` excess.

Two scope qualifications should remain explicit.

1. The `7/6` bound does not cover cutting and then performing an arbitrary
   new multi-piece rechain which compensates for the cuts.  The source says
   this in Section 1, but its final architectural wording is broader than
   the proved theorem.
2. The cap argument assumes the original left chains are not split to remove
   the duplicate left-label incidences.  A simultaneous cap surgery on both
   endpoint partitions lies outside that lemma.

There is also one harmless wording error: global complementation reverses
inclusion; it preserves comparability and transports directed cycles after
exchanging endpoint roles.

## 2. The four chain memberships

For a triangular right-hook label `i+j<=m`, the explicit right chain is

\[
\begin{aligned}
R_{i,j}={}&\{(j,y,i):0\le y\le m-j\}\\
 &\cup\{(x,m-j,i):j<x\le m-i\}\\
 &\cup\{(m-i,m-j,z):i<z\le m\}.                    \tag{2.1}
\end{aligned}
\]

Its cut point is `u_(i,j)=(j,i,i)`.  Hence

\[
 P_{i,j}=\{(j,y,i):0\le y\le i\},                  \tag{2.2}
\]

and `S_(i,j)` starts with `(j,i+1,i)` and contains
`v_(i,j)=(m-i,m-j,m-j)` whenever `i+j<m`.

Fix `a+j<m`.  For the diagonal label `(m-j,j)`, formula (2.2) gives

\[
 p_{a,j}=(j,a,m-j),\qquad
 q_{a,j}=(j,a+1,m-j)\in D_j=P_{m-j,j}.              \tag{2.3}
\]

They are consecutive in that prefix.  Likewise

\[
 r_{a,j}=(j,a+1,a),\qquad
 s_{a,j}=(m-a,m-j,m-j)\in S_{a,j}\subseteq C_{a,j}. \tag{2.4}
\]

Now substitute in

\[
 i_L=\min(y,m-x),\quad
 t_L=x+y-i_L,\quad
 j_L=\min(t_L,m-z).
\]

The strict inequality `a+j<m` gives

\[
\begin{array}{c|cc}
 &i_L&j_L\\ \hline
p_{a,j}&a&j\\
q_{a,j}&a+1&j\\
r_{a,j}&a+1&j\\
s_{a,j}&a&j.
\end{array}                                                   \tag{2.5}
\]

For example, at `s_(a,j)`,

\[
 i_L=\min(m-j,a)=a,qquad j_L=\min(2m-2a-j,j)=j.
\]

Thus the incidence table (3.3) in the source is exact, including the
boundary cases `a=0`, `j=0`, and `a+j=m-1`.

## 3. Comparability and the precedence 2-cycle

Coordinatewise,

\[
 p_{a,j}=(j,a,m-j)<(m-a,m-j,m-j)=s_{a,j},           \tag{3.1}
\]

because `j<m-a` and `a<m-j`.  Also

\[
 r_{a,j}=(j,a+1,a)<(j,a+1,m-j)=q_{a,j}.             \tag{3.2}
\]

Along a fixed left-endpoint chain, increasing targets require increasing
right endpoints.  Therefore (3.1), inside `L_(a,j)`, forces

\[
                              D_j<C_{a,j},            \tag{3.3}
\]

whereas (3.2), inside `L_(a+1,j)`, forces

\[
                              C_{a,j}<D_j.            \tag{3.4}
\]

This is a genuine directed 2-cycle in the right-endpoint precedence graph.
The number of index pairs is

\[
                  \sum_{j=0}^{m-1}(m-j)=\frac{m(m+1)}2.        \tag{3.5}
\]

No parity or missing-label exception occurs.

## 4. Gap supports and congestion

If neither `L_(a,j)` nor `L_(a+1,j)` is cut between its two displayed
incidences, and neither `C_(a,j)` nor `D_j` is cut between its displayed
incidences, all four incidences remain in the same four refined chain
classes.  The cycle (3.3)--(3.4) therefore survives.  Hitting one of those
four gap intervals is necessary.

The congestion calculation is exact for the audited inner-shift rechain.

* A final chain `C_(a,j)` contains only the suffix used by its one indexed
  certificate.  Its internal support gaps occur once.
* In `D_j`, the support for index `a` is the single gap
  `p_(a,j)|q_(a,j)`.  As `a` varies, these are consecutive distinct gaps.
* A left chain `L_(h,k)` can occur only in `Gamma_(h,k)` as its first left
  chain and in `Gamma_(h-1,k)` as its second left chain.

Thus a right gap has congestion one and a left gap at most two.  Since there
are `m(m+1)/2` certificates, any gap hitting set has size at least

\[
                        \left\lceil\frac{m(m+1)}4\right\rceil. \tag{4.1}
\]

The argument only asserts necessity.  It does not assert that hitting all
supports suffices to make both precedence graphs acyclic.

## 5. Arbitrary one-prefix/one-suffix rematching

Assume every original `P_(i,j)` and `S_(i,j)` remains whole, and every final
right chain contains at most one prefix and at most one suffix.  Let
`C_(a,j)` be the chain containing `S_(a,j)` and let `D_j` contain the
diagonal prefix `P_(m-j,j)`.

They cannot be the same orthogonal chain.  The suffix contains one point in
each of `L_(a,j)` and `L_(a+1,j)`, namely `s` and `r`; the diagonal prefix
contains another point in each, namely `p` and `q`.  Their union would meet
both left chains twice.

The inequalities `r<s` and `p<q` occur internally in the two whole pieces,
so the same precedence 2-cycle remains.  Distinct suffixes lie in distinct
matched chains, and every prefix/suffix piece contributes its internal gaps
to at most its own indexed role.  Even when one final chain contains both a
diagonal prefix for one certificate and a suffix for another, those support
gaps lie in disjoint whole pieces.  Congestion is therefore at most two (in
fact the right-gap bound remains one away from a junction, and no junction
gap is in a displayed support).

Hence the quadratic cut theorem extends to this whole class exactly as
claimed.  It does not extend automatically to a rechain using two prefixes,
two suffixes, or pieces cut at new locations.

## 6. Endpoint-length arithmetic

In the pure-refinement model, `x` cuts of the left family and `y` cuts of the
right family create respectively

\[
                         W_m+x,\qquad W_m+m+y          \tag{6.1}
\]

nonempty endpoint classes.  A physical word of length `n` has at most `n`
left endpoint values and `n` right endpoint values.  Therefore

\[
\begin{aligned}
n-W_m&\ge\max(x,m+y)\\
     &\ge\frac{m+x+y}{2}\\
     &\ge\frac m2+\frac{m(m+1)}8
       =\frac{m^2+5m}{8},                              \tag{6.2}
\end{aligned}
\]

with the evident ceilings.  The width formulas

\[
 W_{2t}=3t^2+3t+1,qquad W_{2t+1}=3(t+1)^2             \tag{6.3}
\]

give `W_m=(3/4)m^2+O(m)`, and hence

\[
                         n\ge(7/6-o(1))W_m.            \tag{6.4}
\]

This implication relies on not compensating for cuts by merging pieces from
different old chains.  The quadratic **cut** lower bound survives without
that counting assumption, but (6.1) need not.

## 7. Cap-seam calculation and the missing count argument

For `i+j<m`, the cap point and its predecessor are

\[
 w_{i,j}=(m-i,m-j,i),qquad
 e_{i,j}=(m-i-1,m-j,i).                              \tag{7.1}
\]

This remains correct when `i+j=m-1`: the predecessor is then the last point
of the first hook segment rather than an earlier horizontal point.

If a lower half `A_(i,j)` is followed by an upper half `B_(a,b)`, whole-piece
comparability is equivalent to `e_(i,j)<=w_(a,b)`.  Its three coordinates
give

\[
                         i\le a\le i+1,qquad b\le j.  \tag{7.2}
\]

If `a=i`, the lower half contains `u_(i,j)` of left label `(i,j)`, while the
vertical cap row of `B_(i,b)` contains its point at `z=m-j`, also of label
`(i,j)`.  If `a=i+1`, the lower half contains `(j,i+1,i)` of label
`(i+1,j)`, and the cap row of `B_(i+1,b)` contains the same label at
`z=m-j`.  Conditions `b<=j` and `a+b<m` for an actual cut half ensure these
points are present.  Thus every comparable lower--upper merge violates
orthogonality to the unchanged left partition.

This proves the source's direct no-rechain lemma.  To obtain the stated
chain-count consequence, add the following rank argument.

* Every lower cap half starts below rank `m` and ends at rank
  `2m-j-1>=m`; hence two lower halves cannot be concatenated whole in either
  order.
* Every upper cap half starts at rank `2m-b>m` and ends above rank `2m`;
  hence two upper halves cannot be concatenated whole.
* An upper half cannot precede a lower half by rank, while a lower half
  cannot precede an upper half by the orthogonality calculation above.

Therefore a final right chain contains at most one of the `2T_m=m(m+1)` cap
halves, even if uncut right chains are inserted between pieces: transitivity
would still make two cap halves comparable, and duplicate left incidences do
not disappear.  The cap halves alone force at least

\[
                              2T_m=m(m+1)              \tag{7.3}
\]

right chains.  Since `W_m=(3/4)m^2+O(m)`, this yields an asymptotic excess
`(1/4)m^2+O(m)=Theta(W_m)` over the original width.  This repairs the
unstated counting step in Section 7 of the source.

If the left chains are themselves split so that the repeated labels land in
different left endpoint classes, the lower--upper orthogonality objection
can disappear.  Such a simultaneous two-family surgery is not excluded by
the cap lemma.

## 8. Audited conclusion

The source establishes a real quadratic obstruction, not merely a collection
of overlapping perimeter cycles:

\[
 \boxed{\text{every split-only ordered repair needs at least }
        \left\lceil m(m+1)/4\right\rceil\text{ gap cuts}.}
\]

Its `7/6` consequence is valid for split-only refinements, and its
one-prefix/one-suffix extension is valid.  The cap-seam conclusion is also
valid after adding the rank/count argument above.  What remains outside the
proof is precisely a simultaneous, compensating multi-piece rechain after
the quadratic cuts, or a construction based on different initial cut
locations and a different left-chain geometry.
