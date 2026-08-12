# Quadratic precedence obstruction for the near-orthogonal hook rechain

## 1. Outcome and exact scope

Put

\[
                         P_m=[0,m]^3
\]

and let `W_m` be its width.  The audited construction in
`THREE_BOX_NEAR_ORTHOGONAL_CHAINS.md` gives orthogonal chain partitions

\[
                 |\mathcal L|=W_m,
             \qquad |\mathcal R'|=W_m+m.                       \tag{1.1}
\]

This note proves that this particular gain in unordered orthogonality cannot
be repaired into endpoint order at lower-order cost.  If `x` gaps of the
left chains and `y` gaps of the rechained right chains are cut, and the two
resulting precedence digraphs are acyclic, then

\[
                         x+y\geq {m(m+1)\over4}.                 \tag{1.2}
\]

Consequently any physical endpoint layout obtained by splitting this seed
has length

\[
 n\geq W_m+{m^2+5m\over8},                                    \tag{1.3}
\]

up to the harmless integer ceilings.  Since

\[
                         W_m={3\over4}m^2+O(m),
\]

this is

\[
                         n\geq(7/6-o(1))W_m.                    \tag{1.4}
\]

The obstruction occurs before triangular bandwidth and before pinning.  It
therefore kills the audited hook rechain as a route to `W_m+O(m)`.

The proof also applies unchanged to any one-prefix/one-suffix rematching of
the same pieces.  In particular, reuniting some diagonal chains instead of
using the displayed inner shift does not help.  Coordinate permutations and
global complementation merely transport the certificates.

The theorem is not a no-go for every conceivable surgery of the two raw hook
SCDs.  A construction which moves the original double-separating cuts and
simultaneously performs a more complicated multi-piece rechain lies outside
the exact scope above.  Section 7 proves, however, that the most natural such
move—putting every cut at the cap seam—destroys all possible cross-half
recombinations and itself costs `Theta(W_m)`.

## 2. The pieces used by the certificate

Recall the left label of a point `(x,y,z)`:

\[
 i_L=\min(y,m-x),\qquad
 t_L=x+y-i_L,\qquad
 j_L=\min(t_L,m-z).                                             \tag{2.1}
\]

Write `L_(i,j)` for its left hook chain.  The right hook chain `R_(i,j)` has,
when `i+j<m`, the two repeated-left-label points

\[
 u_{i,j}=(j,i,i),\qquad
 v_{i,j}=(m-i,m-j,m-j).                                        \tag{2.2}
\]

Cutting after `u_(i,j)` produces the prefix `P_(i,j)` and suffix
`S_(i,j)`.  In the audited inner-shift rechain, define

\[
 C_{a,j}=\begin{cases}
 S_{0,j},&a=0,\\
 Q_{a-1,j}=P_{a-1,j}\cup S_{a,j},&a\geq1,
 \end{cases}                                                    \tag{2.3}
\]

for `a+j<m`.  Thus `C_(a,j)` is exactly the final right chain containing the
whole suffix `S_(a,j)`.

For `0<=j<m`, put

\[
                         D_j=P_{m-j,j}.                          \tag{2.4}
\]

This is the unpaired diagonal prefix.  The families `C_(a,j)` and `D_j` are
right chains of `mathcal R'`.

## 3. One explicit two-chain contradiction for every triangular cell

For every

\[
                         a\geq0,\quad j\geq0,\quad a+j<m,       \tag{3.1}
\]

consider the four points

\[
\begin{aligned}
 p_{a,j}&=(j,a,m-j),
 &q_{a,j}&=(j,a+1,m-j),\\
 r_{a,j}&=(j,a+1,a),
 &s_{a,j}&=(m-a,m-j,m-j).                                      \tag{3.2}
\end{aligned}
\]

Direct substitution in (2.1) gives

\[
\begin{array}{c|cc}
 &L_{a,j}&L_{a+1,j}\\ \hline
 D_j&p_{a,j}&q_{a,j}\\
 C_{a,j}&s_{a,j}&r_{a,j}.
\end{array}                                                     \tag{3.3}
\]

The coordinate inequalities `a+j<m` give

\[
 p_{a,j}<s_{a,j}\quad\hbox{in }L_{a,j},
 \qquad
 r_{a,j}<q_{a,j}\quad\hbox{in }L_{a+1,j}.                     \tag{3.4}
\]

Hence the first left chain forces the right-endpoint order

\[
                         D_j<C_{a,j},                            \tag{3.5}
\]

while the second forces

\[
                         C_{a,j}<D_j.                            \tag{3.6}
\]

This is an alternating precedence cycle of length two.  Denote it by
`Gamma_(a,j)`.  There are exactly

\[
             T_m=|\{(a,j):a+j<m\}|={m(m+1)\over2}              \tag{3.7}
\]

such certificates.

The certificate is genuinely occurrence-labelled.  It does not disappear
merely because a different right chain produces the same comparison: the
four displayed incidences must remain connected inside their respective
chain pieces.

## 4. Exact cut supports

The cut support of `Gamma_(a,j)` consists of four chain intervals:

1. the gaps of `L_(a,j)` strictly between `p_(a,j)` and `s_(a,j)`;
2. the gaps of `L_(a+1,j)` strictly between `r_(a,j)` and `q_(a,j)`;
3. the gaps of `C_(a,j)` strictly between `r_(a,j)` and `s_(a,j)`;
4. the gaps of `D_j` strictly between `p_(a,j)` and `q_(a,j)`.

The final interval in item 4 is one gap: the two points are consecutive in
the prefix `P_(m-j,j)`.

If none of these gaps is cut, all four incidences in (3.3) remain paired and
the contradictory inequalities (3.5)--(3.6) survive.  Therefore every
acyclic refinement must hit every support.

### Lemma 1 (support congestion two)

Every chain gap belongs to the supports of at most two of the certificates
`Gamma_(a,j)`.

### Proof

The right chain `C_(a,j)` is unique to its certificate, so a gap in such a
chain is used once.  In `D_j`, the certificates with varying `a` use the
successive, pairwise distinct gaps

\[
                         p_{a,j}\mid q_{a,j}.                    \tag{4.1}
\]

Thus right-chain gaps have congestion one.

A left chain `L_(h,k)` occurs only as the first left chain of
`Gamma_(h,k)` and as the second left chain of `Gamma_(h-1,k)`, when those
indices exist.  Hence a left-chain gap has congestion at most two.  \(\square\)

### Theorem 2 (quadratic split lower bound)

Every refinement of the audited pair with both precedence digraphs acyclic
uses at least

\[
                         \left\lceil {m(m+1)\over4}\right\rceil \tag{4.2}
\]

gap cuts in total.

### Proof

Every one of the `T_m` supports must be hit.  By Lemma 1, one gap cut hits at
most two supports.  Therefore at least `ceil(T_m/2)` cuts are necessary.
\(\square\)

This is the previously missing proof behind the informal claim that the
hook-pair precedence defect is quadratic.  The key is not a family of nested
perimeter cycles; those have large congestion.  It is the family of local
two-chain reversals (3.3).

## 5. Independence from the chosen whole-piece matching

The proof did not use the particular equality

\[
                         Q_{i,j}=P_{i,j}\cup S_{i+1,j}.
\]

It used only that every `P_(i,j)` and `S_(i,j)` remains uncut and is placed
whole in one final right chain.  In any one-prefix/one-suffix matching, let
`C_(a,j)` be the chain containing `S_(a,j)` and `D_j` the chain containing
`P_(m-j,j)`.  They cannot be the same orthogonal chain, since each of the two
pieces already meets both `L_(a,j)` and `L_(a+1,j)`.  Equations
(3.2)--(3.6) then remain valid verbatim.

Distinct suffixes belong to distinct matched chains and the diagonal-prefix
gaps (4.1) remain disjoint.  A matched right chain contains at most one
prefix and at most one suffix.  Consequently one of its gaps can occur in at
most one certificate through its prefix role and at most one certificate
through its suffix role.  Its congestion is therefore still at most two.
Lemma 1 and Theorem 2 continue to hold.  This includes the alternative
matching which reunites diagonal prefixes and suffixes before shifting the
strictly interior pieces.

Global complementation and coordinate permutations preserve inclusion,
chain gaps and support congestion (with the two endpoint roles exchanged
when appropriate).  Hence all isomorphic complement/orientation variants
inherit the same lower bound.

## 6. Consequence for triangular endpoint length

Suppose `x` of the cuts in Theorem 2 are made in `mathcal L` and `y` in
`mathcal R'`.  The two endpoint families then contain at least

\[
                         W_m+x,qquad W_m+m+y                         \tag{6.1}
\]

nonempty chains.  A word has only one left and one right endpoint slot per
physical position, so even a perfect triangular schedule must have

\[
\begin{aligned}
 n-W_m
 &\geq\max(x,m+y)\\
 &\geq {m+x+y\over2}\\
 &\geq {m\over2}+{m(m+1)\over8}
  ={m^2+5m\over8}.                                             \tag{6.2}
\end{aligned}
\]

This proves (1.3).  Explicitly,

\[
 W_{2t}=3t^2+3t+1,
 \qquad
 W_{2t+1}=3(t+1)^2,                                            \tag{6.3}
\]

so (1.4) follows.

Equation (6.2) addresses the triangular endpoint question at the scale that
matters here: chain count alone already consumes a positive fraction of the
width.  The one-sided bandwidth and precedence-with-deadlines conditions can
only add slots; they cannot recover those lost in (6.2).  This note does not
claim the exact bare one-sided bandwidth of the unrepaired incidence graph.

## 7. Why moving every cut to the cap seam also fails

There is one especially natural attempted evasion.  Instead of cutting
`R_(i,j)` just after `u_(i,j)`, cut it immediately before the point

\[
                         w_{i,j}=(m-i,m-j,i),                    \tag{7.1}
\]

where the final left-label row begins.  This cap cut already separates the
two repeated labels `u_(i,j),v_(i,j)` and also cuts the conspicuous backward
precedence transition.

Let `A_(i,j)` be the lower cap half and `B_(a,b)` an upper cap half.  The last
point of `A_(i,j)` and first point of `B_(a,b)` are

\[
 e_{i,j}=(m-i-1,m-j,i),
 \qquad
 w_{a,b}=(m-a,m-b,a).                                          \tag{7.2}
\]

If they are comparable in the order needed for a rechain,

\[
                         e_{i,j}\leq w_{a,b},                    \tag{7.3}
\]

then coordinatewise comparison forces

\[
                         a\in\{i,i+1\},\qquad b\leq j.          \tag{7.4}
\]

If `a=i`, both halves meet `L_(i,j)`: the lower half contains `u_(i,j)` and
the upper row contains the label `(i,j)`.  If `a=i+1`, both halves meet
`L_(i+1,j)`: the lower half contains `(j,i+1,i)` and the upper row contains
the same left label.  In either case their union is not orthogonal to
`mathcal L`.

Thus no lower cap half can be recombined with an upper cap half while
preserving both comparability and orthogonality.  In particular the same
lower-half/upper-half matching mechanism which produced the `+m` inner-shift
rechain now absorbs none of the `m(m+1)/2` cap cuts.  Within this natural
cap-cut architecture the extra cost is already `Theta(W_m)`.

This does not classify every mixed choice of cut positions, but it closes the
canonical alternative: the seam which directly removes the visible
precedence wrap is exactly the seam at which the low-cost rechain matching
vanishes.

## 8. Final architectural conclusion

The hook construction now has a complete audited diagnosis.

* Cutting immediately after the repeated lower corner permits the remarkable
  `+m` orthogonal rechain, but leaves a congestion-two packing of
  `m(m+1)/2` precedence cycles.
* Any whole-piece rematching of those same prefixes and suffixes inherits the
  packing.
* Moving every cut to the natural precedence cap seam kills the matching and
  costs `Theta(W_m)` directly.
* Complement and coordinate-orientation variants are isomorphic.

Therefore an ordered `W_m+O(m)` construction cannot be obtained by repairing
this hook seed locally.  A successful ordered-orthogonal construction must
build the endpoint order into a genuinely different chain geometry, rather
than orthogonalizing first and attempting to clean up the resulting order.
