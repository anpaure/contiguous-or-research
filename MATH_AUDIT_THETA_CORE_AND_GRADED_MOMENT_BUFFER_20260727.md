# The first overlapping-cycle gate and a graded moment buffer

Date: 2026-07-27

Scope: repaired promotion-ring slow-greedy hierarchy.

## 0. Outcome

The theta audit found a gap in the original cycle-by-cycle proof, but it
also led to a proof of the arbitrary mixed-diagram theorem by a different
exposure order.  Explore rows rather than cycles.  All old columns met by
one new row are charged simultaneously by the existing disjoint
path-mesh maximum; all columns first introduced from that row are charged
by the existing internal census.  The resulting exponent is identically
\(\sum_j(q_j-1)=\omega\).  Thus no subdivided-cycle theorem is needed.

The theta graph whose paths have lengths \(2,4,4\) remains useful as the
first example showing why degrees plus the first \(C_4\) estimate alone
cannot justify the old proof.

In the abstract row--column incidence notation below, its desired estimate
is

\[
 \boxed{
 \sum_{u,v}C_{uv}(C^2_{uv})^2
 \le {L^5A^5\over d}.}
 \tag{0.1}
\]

Here \(d\) is the number of rows, \(L\) and \(A\) are the two maximum
degrees, and \(A=d\alpha\).  Degree bounds plus the first \(C_4\) estimate
miss (0.1) by one factor \(\alpha\).  A precise kernel-level sufficient
replacement is the subdivided-\(K_{2,3}\) estimate (2.6), but Section 2.1
shows that direct row exploration proves the physical count without it.

There is, however, a useful dynamic simplification.  A \(q\)-th jump
moment of an excess-\(r\) core can be truncated to one incidence of the
new column in each of its \(q\) replicas.  After allowing all equality
partitions of the old core columns, its excess is at most

\[
                         q(2r+1).
\tag{0.2}
\]

Consequently the graded choice

\[
 q(r)=\min\left\{J,
          \left\lfloor{L\over2r+1}\right\rfloor\right\}
\tag{0.3}
\]

never asks the hierarchy for a diagram beyond level \(L\), regardless of
how many displayed rows the new column meets.  Thus deterministic
high-incidence truncation removes the one-column outer crossing from the
region where \(q(r)\ge2\).  The top quarter of the buffer has only a
first-moment envelope and still needs a quarantine/loose-bound argument.

The remaining dynamic task is to turn the first-moment top strip into an
incidence-weighted quarantine/loose-envelope bound.

## 1. Incidence kernel

Let \(H\) be the \(d\times |V|\) biadjacency matrix of the conflict
incidence graph, with

\[
              \max_{u}\sum_vH_{uv}\le L,
 \qquad
              \max_v\sum_uH_{uv}\le A=d\alpha.
\tag{1.1}
\]

Put

\[
                          C=HH^{\mathsf T}.
\tag{1.2}
\]

Thus \(C_{uv}\) is the number of protected columns meeting both row
options \(u,v\).  The rectangular \(K_{2,b}\) target has the form

\[
                    \sum_{u,v}C_{uv}^{\,b}
 \le d^2L^b\alpha^b
 ={L^bA^b\over d^{b-2}}.
\tag{1.3}
\]

For \(b=2\), this is the first \(C_4\) estimate.

The operator norm satisfies

\[
                         \|C\|_{\rm op}\le LA.
\tag{1.4}
\]

Consequently, if the unrestricted version of the \(C_4\) estimate is
available, every simple even cycle has the desired scale:

\[
 \operatorname {tr}(C^k)
 \le \|C\|_{\rm op}^{k-2}\operatorname {tr}(C^2)
 \le L^kA^k.
\tag{1.5}
\]

In the repaired-ring application the columns are required pairwise
resource-disjoint.  Formula (1.5) should therefore be read as a clean
kernel calculation, not as a substitute for checking the non-disjoint
terms in the physical catalogue.

## 2. The theta core

Take two endpoint rows \(u,v\), one direct length-two path between them,
and two length-four paths with internal rows \(w,z\).  Expanding its five
column choices gives

\[
\begin{aligned}
 \operatorname {hom}(\Theta_{2,4,4},H)
 &=\sum_{u,v,w,z}
   C_{uv}C_{uw}C_{wv}C_{uz}C_{zv}\\
 &=\sum_{u,v}C_{uv}(C^2_{uv})^2.
\end{aligned}
\tag{2.1}
\]

The bipartite diagram has four rows, five columns, ten incidences, hence

\[
                          \omega=10-5=5.
\tag{2.2}
\]

The mixed-diagram prediction is therefore exactly

\[
 d^4L^5\alpha^5={L^5A^5\over d},
\tag{2.3}
\]

which is (0.1).

The first \(C_4\) estimate alone cannot prove this.  Indeed, take a single
component \(K_{A,L}\) and \(d-A\) isolated rows.  It obeys the degree
bounds and saturates

\[
                         \operatorname {tr}(C^2)=L^2A^2,
\tag{2.4}
\]

but its theta count is \(A^4L^5\), larger than (2.3) by
\(d/A=\alpha^{-1}\).  This abstract example violates the higher
rectangular estimates, so it is not a repaired-ring counterexample.  It
does show that the missing factor cannot be obtained from degrees and
\(C_4\) alone.

There is an exact sufficient estimate.  Hölder gives

\[
 \sum_{u,v}C_{uv}(C^2_{uv})^2
 \le
 \left(\sum_{u,v}C_{uv}^3\right)^{1/3}
 \left(\sum_{u,v}(C^2_{uv})^3\right)^{2/3}.
\tag{2.5}
\]

The ordinary \(K_{2,3}\) rectangle supplies the first factor at scale
\(L^3A^3/d\).  Therefore (0.1) follows exactly from

\[
 \boxed{
        \sum_{u,v}(C^2_{uv})^3\le {L^6A^6\over d}.}
\tag{2.6}
\]

Equation (2.6) is the \(K_{2,3}\) diagram with every one of its six edges
subdivided once.  It is the first concrete overlapping-cycle theorem
which the present rectangular hierarchy does not state.  In endpoint
language, it asks that two cycle closures sharing their endpoint pair pay
two independent transverse gaps.

This identifies the unsupported sentence in the former Lemma 3.1:
closing hidden witness equalities prevents double-charging, but does not
by itself prove that two distinct holonomy closures are independent.

### 2.1 Direct row-exploration resolution

The physical theta count does not require (2.6).  Start with endpoint row
\(u\), introduce its three incident columns, then expose \(w\) and its
new column, then \(z\) and its new column, and finally \(v\).  The old
column counts seen by the four rows are respectively

\[
                              0, 1, 1, 3.
\tag{2.7}
\]

The disjoint path-mesh maximum therefore contributes
\(\alpha^{0+1+1+3}=\alpha^5\), while the five columns each contribute
their one free internal-census incidence.  This is exactly (2.3).

The same argument works for every connected physical core.  When a row
is exposed, charge all incidences to old columns by the disjoint
path-mesh maximum and introduce every new column by the internal census.
Each column has one free incidence, so the total exponent is

\[
                    \sum_{i,j}q_{ij}-c=\omega.
\tag{2.8}
\]

This is the corrected Lemma 3.1 in the static mixed-diagram file.  The
subdivided-\(K_{2,3}\) inequality remains an interesting kernel statement
but is no longer a gate for the repaired-ring hierarchy.  The literal
resource-disjoint version is nevertheless proved independently in
`MATH_THEOREM_THETA_244_PHYSICAL_KERNEL_CLOSURE_20260727.md`; its
fixed-endpoint kernel is bounded by $dL^2\alpha^2$.

## 3. Excess of a replicated jump diagram

Let a core diagram \(\Gamma\) have \(c\) nonprivate columns and excess
\(r\).  Core compression gives

\[
                             c\le r.
\tag{3.1}
\]

Expand a \(q\)-th jump moment.  Before equality identifications, the
\(q\) replicas have excess \(qr\).  Identifying old columns across
replicas keeps all formal incidences and reduces the number of columns.
If \(h\) identifications occur, the excess becomes \(qr+h\).  Since at
most \((q-1)c\) old columns can disappear,

\[
                         qr+h\le qr+(q-1)c<2qr.
\tag{3.2}
\]

The selected edge \(g\) is one new shared column.  Every replica in a
nonzero jump contains at least one row hit by \(g\).  Retain canonically
one such incidence per replica and delete every other \(g\)-incidence.
Deleting constraints only enlarges the count.  The truncated shared
column has degree \(q\), hence raises excess by \(q-1\).  Combining with
(3.2),

\[
                  \omega(\text{truncated }q\text{-moment})
                  \le 2qr+q-1<q(2r+1).
\tag{3.3}
\]

This estimate is independent of the actual number \(t\) of displayed
rows met by \(g\).  It is the deterministic high-\(t\) truncation that is
missing from a constant-moment buffer.

Private degree-one columns have already been summed by the exponential
generating function.  Cross-replica coincidences among those private
columns are the usual positive-excess exponential tail and must be
included in the one-excess parameter; (3.3) concerns the compressed
physical core.

## 4. The graded moment simplex

Fix a buffer ceiling \(L\) and moment cap \(J\).  For an excess-\(r\)
observable use (0.3).  Then every truncated moment core satisfies

\[
                       q(r)(2r+1)\le L.
\tag{4.1}
\]

There are three zones.

* If \(r\le (L/J-1)/2\), the full \(J\)-th moment is available.
* If \(r\le (L-2)/4\), at least the quadratic variation is available.
* If \(r>(L-2)/4\), use only its predictable first moment as a loose
  boundary envelope.

Thus recursively taking a \(J\)-th moment of every auxiliary variable is
unnecessary.  The correct geometry is the simplex

\[
                         q(2r+1)\le L,
\tag{4.2}
\]

not a rectangle with the same moment order at every excess.

The top strip remains nontrivial: a first-moment envelope does not give a
uniform high-probability statement for every owner.  What it can give is
an incidence-weighted quarantine statement, because its static scale
contains \(\alpha^r\) with

\[
          \log(1/\alpha)=(2+o(1))\log m.
\tag{4.3}
\]

At \(r=\Theta((\log m)^2)\) this is far smaller than any inverse
polynomial.  Converting that numerical slack into a stopped dynamic
quarantine bound is the remaining boundary calculation; it is not proved
here.

## 5. Correct status

Unconditional:

1. core compression and \(\Delta\omega=t-1\);
2. the tree breadth estimate;
3. the rectangular path-mesh power estimates already in the catalogue;
4. the arbitrary static mixed-diagram bound, by row exploration;
5. the replicated-jump excess bound (3.3).

Open:

\[
 \boxed{
 \text{the first-moment top-strip quarantine estimate.}}
\]

Conditional on that statement, the graded moment simplex removes the
previous outer-flux and recursive-row-count obstructions.
