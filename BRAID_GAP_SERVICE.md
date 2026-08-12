# Gap service for rotating peak braids

## 1. Outcome

Let \(a\ge3\), and let

\[
 H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,\ |x|,|y|,|z|\le a\},
 \qquad M_a=3a^2+3a+1,
\]

and put

\[
                         L=4a+2.
\]

This note attacks the gap-start problem isolated in
`ROTATING_BRAID_ANALYSIS_AUDIT.md`.  It obtains an exact global
service inequality, but it also finds a genuine obstruction to the
strongest local form of the hoped-for lemma.

Fix \(1<c<2\).  Call a directed internal peak plateau **dangerous** when
its cost satisfies

\[
                         \lambda>ca.                 \tag{1.1}
\]

Resolve the dangerous plateaux into maximal direct rotating components as
in `ROTATING_BRAID_ANALYSIS.md`.  Let

\[
 E=\sum_P\lambda(P)=\sigma a^2,\qquad
 m=\#\{P\}=sa,
\]

and let \(r\) be the number of direct components.

### Theorem 1 (global braid-plus-gap service)

There is a heterogeneous internal-threshold-run assignment with charge
congestion

\[
 C_\alpha\le4a+3,\qquad C_\beta\le4a+3,              \tag{1.2}
\]

omitting at most \(\max\{0,m-1\}\le3a+2\) shared plateau endpoints, whose
total cost is at most

\[
 \boxed{
 Q\le
 \bigl(3c+2\sigma-2cs\bigr)a^3
+(12a^2+6a)r+23a^2+15a.}                           \tag{1.3}
\]

More exactly, if \(G\) is the number of positions outside the displayed
dangerous plateaux, \(U\) is the exceptional set inside those gaps, and
\(V\) is the number of positions in the union of the terminal plateau
blocks of the direct components, and \(\omega\) is the endpoint-overlap
multiplicity, then

\[
\boxed{
 Q\le
 (2+c)aE-2ca^2m
+2am+caG+(2-c)aU+2aV,}                              \tag{1.4}
\]

with

\[
 G=M_a-E-m+\omega,\qquad
 0\le\omega\le\max\{0,m-1\},
                                                               \tag{1.5}
\]

\[
 U\le2L(r+1),\qquad V\le(2a+1)r.                   \tag{1.6}
\]

Thus every gap start outside \(U\) is serviced at cost at most \(ca\);
the only loss is \(O(a)\) gap-interface positions and one terminal block
per direct component.

### Corollary 2 (few-component near-threshold closure)

If \(r=o(a)\), then

\[
 Q\le\bigl(3c+2(\sigma-cs)\bigr)a^3+o(a^3).          \tag{1.7}
\]

Consequently, whenever

\[
 \sigma-cs<\frac{4-3c}{2}-\eta                     \tag{1.8}
\]

for some fixed \(\eta>0\), the assignment has

\[
                         Q\le(4-2\eta)a^3+o(a^3).   \tag{1.9}
\]

At a mass-feasibility endpoint, where \(\sigma=cs+o(1)\), this becomes

\[
                         Q\le3ca^3+o(a^3).           \tag{1.10}
\]

In particular, taking \(c=4/3-1/1000\) gives the strict constant
\(4-3/1000\).  This proves the desired sub-four gap service for the
few-component extremal braid.

### Obstruction

There are explicit clean rotating words with \(\Theta(a)\) one-point gaps
such that every avoiding run contained in either adjacent \(L\)-position
window at each interior gap point has cost greater than \(4a/3\).  Hence
neither of
the following is true:

* every gap start has a locally available run of cost at most \(4a/3\);
* failure of direct adjacency automatically creates a cheap peak.

The construction is in Section 7.  Its gap set has only \(O(a)\) points,
and the average of the local span-\(L\) minima over those gap starts is
strictly greater than \(4a/3\).  This does not disprove Theorem 1 or a
global result permitting \(O(a)\)
omissions.  It does prove that the remaining \(r=\Theta(a)\) case needs a
global transition-resource argument, not a pointwise seam lemma.

## 2. Cheap peaks in a dangerous-free window

We use two elementary facts.

### Lemma 3 (a nondirected peak contains a singleton peak)

Let \(P\) be a constant-coordinate peak plateau.  If its order along the
coordinate line is not directed, then \(P\) contains a singleton peak in
one of the two cross-coordinates.

#### Proof

The two cross-coordinate values are distinct along \(P\), are integral,
and sum to a constant.  If one cross-coordinate is not monotone, it has an
interior strict local maximum or minimum.  A maximum is a singleton peak
of that coordinate; a minimum is a singleton peak of the complementary
cross-coordinate.  \(\square\)

### Lemma 4 (internal gap windows are \(ca\)-cheap)

Let \(W\) be \(L=4a+2\) consecutive positions which contain no directed
peak plateau of cost greater than \(ca\).  Then \(W\) contains an internal
threshold run of cost at most \(ca\).

#### Proof

The universal peak-mesh theorem supplies a peak plateau \(P\) contained in
\(W\).  If \(\lambda(P)\le ca\), use it.  Otherwise \(P\) is not directed,
by the hypothesis on \(W\), and Lemma 3 supplies a singleton peak inside
\(P\).  In either case the run is internal in the full word because its
two smaller boundary values lie inside \(W\).  \(\square\)

This is the key observation: long gaps do not need to know anything about
the orientations of their neighboring braid blocks.

## 3. A one-dimensional gap service lemma

Let \(I=[u,v]\) be a contiguous gap containing no dangerous plateau, and
write \(g=|I|\).  A position \(i\in I\) is **right-deep** if

\[
                         i+L\le v,
\]

and **left-deep** if

\[
                         i-L\ge u.
\]

Assign a right-deep position a run from Lemma 4 inside
\([i+1,i+L]\).  If it is not right-deep but is left-deep, use the symmetric
run inside \([i-L,i-1]\).

Let \(U(I)\) be the positions which are neither right-deep nor left-deep.
Then

\[
 |U(I)|\le \min\{g,2L\}.                             \tag{3.1}
\]

In fact the sharper value is \(\max\{0,2L-g+O(1)\}\) when
\(L\le g<2L\), but (3.1) is the useful uniform form.

For positions in \(U(I)\), use the universal peak-mesh assignment in the
whole order: forward except in the final \(L\) positions, and backward
there.  Its cost is at most \(2a\).  Consequently

\[
 Q(I)\le ca\bigl(g-|U(I)|\bigr)+2a|U(I)|
       =cag+(2-c)a|U(I)|.                            \tag{3.2}
\]

All chosen runs have one-sided span at most \(L+1\) in the convention
\(v_i+1-i\) or \(i-(u_i-1)\).  Hence an adjacent \(\alpha\)-increment is
charged by at most \(L+1\) forward starts, and an adjacent
\(\beta\)-increment by at most \(L+1\) backward starts.  Thus
\(C_\alpha,C_\beta\le L+1=4a+3\), independently of the number of gaps.

### Corollary 5 (average gap cost)

For gaps \(I_1,\ldots,I_h\), with total size \(G\), put
\(U=\sum_\nu|U(I_\nu)|\).  Then

\[
 Q_{\rm gap}\le caG+(2-c)aU,\qquad U\le2Lh.          \tag{3.3}
\]

If \(G=\Theta(a^2)\) and \(h=o(a)\), their average assigned cost is

\[
                         ca+o(a).                    \tag{3.4}
\]

This proves the endpoint average below \(4a/3\) for a sublinear number of
macroscopic gaps by taking any fixed \(c<4/3\).

## 4. Accounting for all interfaces

Dangerous plateau edge intervals are pairwise disjoint.  Plateaux of
different coordinates may share one endpoint position, but there are only
\(O(a)\) dangerous plateaux because each has \(\Theta(a)\) edges.  Put all
shared endpoint positions into an omitted set of size \(O(a)\).  For start
accounting the plateau intervals may then be treated as disjoint; the word
and the plateau runs themselves are not altered.  All double-counting and
omitted-target corrections are \(O(a^2)\).

The complement consists of at most \(r+1\) gap intervals.  Corollary 5
gives at most

\[
                         2L(r+1)                    \tag{4.1}
\]

exceptional gap positions.

Within a direct component, every position of a block \(P_j\), except in
the last block, is assigned the next plateau \(P_{j+1}\).  Let \(V\) count
the positions in the last block of every component.  Then

\[
 U\le2L(r+1),\qquad V\le(2a+1)r,                   \tag{4.2}
\]

which is (1.6).

Every position in \(U\cup V\) uses the universal cost-\(2a\) assignment.
The gap positions outside \(U\) use cost at most \(ca\), and all runs again
have one-sided span at most \(L+1\).  Therefore this entire mixed assignment
has \(O(a)\) charge congestion.

## 5. Cost of the direct components

For \(x,y\in[ca,2a]\), put \(x=ca+u\), \(y=ca+v\), where
\(0\le u,v\le(2-c)a\).  Since

\[
 2uv\le(2-c)a(u+v),
\]

we obtain the secant inequality

\[
 \boxed{
 xy\le\left(1+\frac c2\right)a(x+y)-2ca^2.}          \tag{5.1}
\]

For starts in \(P_j\), the next-block assignment costs

\[
                         (\lambda_j+1)\lambda_{j+1}. \tag{5.2}
\]

Add a nonnegative closing product to each direct component and sum (5.1)
cyclically.  The terms with the added \(1\) in (5.2) total at most \(2am\).
It follows that all nonterminal block starts cost at most

\[
 Q_{\rm braid}
 \le(2+c)aE-2ca^2m+2am.                             \tag{5.3}
\]

The assigned run \(P_{j+1}\) has one-sided span at most

\[
                 \lambda_j+\lambda_{j+1}+2\le4a+2=L
\]

for every start in \(P_j\).  Thus this part of the assignment has the same
\(O(a)\) congestion bound.

Finally,

\[
 G=M_a-\sum_P(\lambda(P)+1)+O(a)
  =(3-\sigma)a^2+O(a).                              \tag{5.4}
\]

Adding (5.3), the gap cost \(caG\), the excess gap-interface cost
\((2-c)aU\), and the terminal-block cost \(2aV\) proves (1.4) and hence
Theorem 1.

For the fully explicit error in (1.3), note first that

\[
 m<\frac{M_a-1}{ca}<3a+3,
 \qquad\text{so}\qquad m\le3a+2.                    \tag{5.5}
\]

Substitute \(G=M_a-E-m+\omega\) in (1.4).  After removing the leading
term in (1.3), the remainder is

\[
\begin{aligned}
 R={}&3ca^2+ca+(2-c)am+ca\omega\\
    &+(2-c)aU+2aV.                                  \tag{5.6}
\end{aligned}
\]

Using \(1<c<2\), \(\omega\le m\), (1.6), and (5.5) gives

\[
 R\le(12a^2+6a)r+23a^2+15a,                        \tag{5.7}
\]

which is exactly the displayed finite error in (1.3).

## 6. Parameter-sensitive consequences

The leading coefficient in Theorem 1 is

\[
                         3c+2\sigma-2cs
                         =3c+2(\sigma-cs).           \tag{6.1}
\]

The quantity

\[
                         e_c:=\sigma-cs
 =\frac1{a^2}\sum_P(\lambda(P)-ca)                  \tag{6.2}
\]

is the total excess length of dangerous blocks above the chosen threshold.
Thus the exact few-component condition is not merely that the gaps have
average cost below \(4a/3\); it is

\[
                         3c+2e_c<4.                 \tag{6.3}
\]

This explains the parameter warning in the audit.  A threshold
\(c=4/3-\delta\) has a raw gap saving \(3\delta\), but block-length excess
uses that saving at twice its normalized mass.

At the mass-feasibility endpoint from the direct-braid audit,
\(\sigma=cs+o(1)\), so \(e_c=o(1)\), and (6.3) has the full saving
\(3\delta\).  Away from that endpoint, a single-scale gap theorem cannot
be uniform unless it also controls \(e_c\).  The natural next refinement
is multiscale: apply (3.2) at several thresholds and charge each block only
for the layer of its excess above the preceding threshold.

## 7. Transparent separators: a local counterexample

We now show that direct-component maximality does not force an individual
gap start to be cheap.

Let

\[
                         a=12m,\qquad 1\le j\le m-1,
\]

and define

\[
                         t_j=7m+j,\qquad r_j=6m+j.
\]

Use the full high lines

\[
\begin{aligned}
 X_t&=((t,y,-t-y):-a\le y\le a-t),\\
 Y_t&=((-t-z,t,z):-a\le z\le a-t),\\
 Z_t&=((x,-t-x,t):-a\le x\le a-t),
\end{aligned}                                       \tag{7.1}
\]

in the increasing orientations displayed.  Insert the separator points

\[
\begin{aligned}
 R^z_j&=(r_j,a-r_j,-a) &&\text{between }X_{t_j},Y_{t_j},\\
 R^x_j&=(-a,r_j,a-r_j) &&\text{between }Y_{t_j},Z_{t_j},\\
 R^y_j&=(r_j,-a,a-r_j) &&\text{between }Z_{t_j},X_{t_{j+1}}.
\end{aligned}                                       \tag{7.2}
\]

Omit the final \(R^y\).  All displayed points are distinct.  At
\(X_{t_j}|R^z_j|Y_{t_j}\), the \(x\)-coordinate strictly decreases, the
\(y\)-coordinate strictly increases, and \(z=-a\) is a three-position
strict local minimum.  The other two joins are its cyclic coordinate
images.  At the cross-level join, the inequalities are

\[
\begin{aligned}
 a-t_j&<r_j<t_{j+1},\\
 t_j&>a-r_j>a-t_{j+1},
\end{aligned}
\]

so the same sign ledger holds.

Consequently the only internal peak plateaux in this word are the full
blocks \(X_{t_j},Y_{t_j},Z_{t_j}\).  Their costs are

\[
                         2a-t_j=17m-j\ge16m+1
                         >\frac{4a}{3}.              \tag{7.3}
\]

Every internal threshold run contains an internal peak plateau.  Therefore
every such run wholly contained in this transparent word has cost greater
than \(4a/3\).

There are \(\Theta(a)\) separator positions at distance at least \(L\)
from the two word ends.  For each of them, every avoiding run contained in
either adjacent \(L\)-position window has cost greater than \(4a/3\).
Each inserted point breaks literal plateau adjacency, so these are genuine
gap starts between maximal direct components.

To obtain a full ordering of \(H_a\), prepend all unused points in an
arbitrary order.  Keep only separators whose distance from the first
position of the displayed suffix and from the full-word endpoint is at
least \(L\).  There are still \(\Theta(a)\) of them, and both adjacent
windows remain wholly inside the clean transparent suffix.  Thus the local
counterexample is an actual full permutation, not merely an abstract
subword.

This is a rigorous obstruction to any pointwise or purely local
gap-start lemma.  It does not refute the global theorem sought in the
original problem: the number of separators is only \(O(a)\), so they may
be omitted or serviced nonlocally with \(O(a)\) congestion.

## 8. Peak-free gap geometry

The remaining many-component case has a useful exact normal form.  If a
gap interval contains no cheap peak plateau at all, each of its three
coordinate words is weakly valley-shaped.  Sorting the three valley
indices splits the gap into four monotonicity regions.  The two exterior
regions contain at most one point, and each middle region contains at most
\(2a+1\) points.  Hence

\[
                         |I|\le4a+1.                 \tag{8.1}
\]

On either middle region, choose the nonempty proper set of increasing
coordinates.  Their sum rises by at least one between distinct terms and
has range at most \(2a\).  Thus every diagonal reset region has only
\(O(a)\) edges.

Constant-coordinate edge sets, including nonpeak plateaux in the gaps, are
globally disjoint across all coordinates: two coordinates constant on one
ordering edge would force the two points to be equal.  Therefore

\[
 \sum_{\text{all constant-coordinate plateaux }P}\lambda(P)
 \le M_a-1.                                         \tag{8.2}
\]

Equations (8.1)--(8.2) explain the exact unresolved resource.  For
\(r=o(a)\), all diagonal reset edges are lower order and Theorem 1 closes
the extremal endpoint.  For \(r=\Theta(a)\), the reset budget and the
nonpeak plateau budget can both be quadratic.  One must either:

1. absorb their nonpeak plateau edges into an extension of the A-turn
   level ledger; or
2. use their upper-threshold components to replace the \(2a\) interface
   fallback in (1.4).

The transparent construction in Section 7 shows why this cannot be done
one seam at a time.  A proof must charge the shared coordinate-line
resources globally.

## 9. Theorem ledger

Proved:

* every dangerous-free internal gap window has a run of cost at most
  \(ca\);
* the exact gap cost (3.3), with \(O(a)\) congestion;
* the global braid-plus-gap inequality (1.3);
* a strict sub-four result for \(r=o(a)\) whenever (1.8) holds, including
  the mass-feasibility endpoint;
* an explicit transparent-separator family refuting pointwise seam
  cheapness; and
* the valley normal form and global constant-edge budget for peak-free
  transition gaps.

Not proved:

* a uniform sub-four inequality when \(r=\Theta(a)\);
* the parameter-sensitive budget for arbitrary \((\sigma,s)\);
* an \(O(a)\)-congestion nonlocal assignment which makes the transparent
  separators cheap on average; or
* the universal three-box obstruction and the original Boolean-array
  conjecture.

The next exact target is to replace the interface terms

\[
                  (2-c)aU+2aV=O(a^2r)               \tag{9.1}
\]

in (1.4) by a global charge to the disjoint nonpeak plateau-edge budget
(8.2), with a coefficient strictly below the secant cost already paid by
the dangerous blocks.
