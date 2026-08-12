# Exact Johnson endpoint splicing and the random safe-edge calculation

## Verdict

Endpoint scarcity is not the first obstruction in the multidepth splice
problem.  Let

\[
 W=\binom{2m}{m}.
\]

Every vertex-disjoint family of nontrivial middle-level Johnson paths can be
spliced, using only Johnson-adjacent endpoints of different components, into
a linear forest with at most

\[
 \boxed{\frac{W}{2m}}
\]

components.  Reversing and concatenating paths preserves every old internal
intersection and union window.  In particular, for every `H=o(m)`, the
component charge in the endpoint-capped erosion theorem is automatically

\[
 Hc\le \frac{HW}{2m}=o(W).
\]

This does **not** settle the multidepth gate.  The remaining crossing windows
may collide, and arbitrary splices may create short coordinate runs.  The
deterministic component bound also leaves as many as order `W/m` components,
whereas a lossless depth-`H` boundary-slot ledger by itself would need
`c=o(W/H^2)`.

For independent uniform queue segments with `L_0=o(sqrt(m))`, an exact
calculation shows that almost every available endpoint adjacency is
**initially, for one splice**, short-run-safe.  The expected safe endpoint
degree is of order `m^2/L_0`, which is much larger than `log W`.  Thus generic
initial endpoints are not sparse.  Turning this density into one
pin-compatible multidepth linear forest still requires a dynamic
quasirandom/path-cover theorem not supplied by marginal coordinate symmetry.

## 1. The deterministic endpoint-splice theorem

Let `J=J(2m,m)` be the Johnson graph.  Its vertices are the `m`-subsets of
`[2m]`, and two vertices are adjacent when their symmetric difference has
size two.

### Theorem 1

Let `P` be a family of pairwise vertex-disjoint, nontrivial paths in `J`.
There is a sequence of endpoint splices, always between two different current
components, which produces a vertex-disjoint linear forest with `c`
components satisfying

\[
 \boxed{c\le \frac{W}{2m}.}
\tag{1.1}
\]

Every consecutive vertex window originally internal to one input path is
still consecutive, possibly in reverse order, in the final forest.
Consequently all of its intersection and union labels are unchanged.

### Proof

Repeatedly do the following whenever possible.  Choose endpoints `A,B` of
two different current components with `A~B` in `J`, orient the first path to
end at `A`, orient the second to begin at `B`, and concatenate them through
the Johnson edge `AB`.  This operation preserves vertex-disjointness and
produces another path.  It also preserves every old internal window; reversal
only reverses the order of the same sets.

Stop when no such cross-component endpoint edge remains.  Suppose there are
`c` components.  Their `2c` endpoints are distinct; write their set as `S`.
Every edge of `J[S]` must join the two endpoints of one component.  There is
at most one such pair per component, so

\[
 e_J(S)\le c.
\tag{1.2}
\]

The Johnson graph `J(2m,m)` is `m^2`-regular.  Its eigenvalues are

\[
 \theta_j=(m-j)^2-j,\qquad 0\le j\le m,
\]

and hence its least eigenvalue is `-m`.  Decomposing the indicator of an
arbitrary set `S` into its constant and orthogonal parts gives the exact
spectral supersaturation inequality

\[
 \begin{aligned}
 2e_J(S)
 &\ge \frac{m^2|S|^2}{W}
       -m\left(|S|-\frac{|S|^2}{W}\right)\\
 &=\frac{m(m+1)|S|^2}{W}-m|S|.
 \end{aligned}
\tag{1.3}
\]

Substituting `|S|=2c` and (1.2) yields

\[
 2c\ge \frac{4m(m+1)c^2}{W}-2mc.
\]

For `c>0`, this is equivalent to

\[
 2mc\le W,
\]

which is (1.1).  \(\square\)

### Corollary 2

At the sprinkled-erosion threshold

\[
 H=(1+o(1))\sqrt{m\log\log m},
\]

the forest from Theorem 1 satisfies

\[
 Hc=O\left(W\sqrt{\frac{\log\log m}{m}}\right)=o(W).
\tag{1.4}
\]

Thus the component condition in the multidepth splice gate is not an
independent obstruction.

If the initial queue packing has

\[
 p=(1+o(1))\frac{W}{L_0}
\]

segments with `L_0=o(m)`, the construction performs `p-c` splices and

\[
 \frac{c}{p}\le (1+o(1))\frac{L_0}{2m}=o(1).
\tag{1.5}
\]

Thus it joins almost all available segment boundaries in the literal sense
that only an `o(1)` fraction of the maximum possible `p-1` joins is lost.

## 2. What the theorem does not buy

If the original segments carry lossless radius-`d` profiles, the exact
erosion/splice ledger leaves `c d(d+1)` boundary shadow slots after the
segments have been joined into `c` paths.  Theorem 1 gives only

\[
 c d(d+1)\le \frac{W d(d+1)}{2m}.
\tag{2.1}
\]

This is `o(W)` for `d=o(sqrt(m))`, but at
`d^2~m log log m` the right side is of order `W log log m`.  More
importantly, slot counts alone do not say that the crossing labels are new.
Theorem 1 therefore settles the physical component toll, not the shadow
defect or short-run toll.

## 3. Exact safe-edge probability for independent queue segments

The following calculation concerns the ideal independent model.  It is not
claimed for an arbitrary ABKV matching or cover.

Let an oriented queue segment have `L_0` middle vertices and put

\[
 \ell=L_0-1.
\]

Choose its first middle set uniformly.  Choose the `ell` distinct coordinates
removed along the geodesic in a uniformly random order from that set, and
the `ell` distinct entering coordinates in a uniformly random order from its
complement.  Different segments are independent.

For a path `P`, let `I_P` be the `ell` coordinates that entered along `P`.
For a path `Q`, let `O_Q` be the `ell` coordinates that leave along `Q`.
Suppose the terminal set `B_P` and initial set `A_Q` are adjacent, say

\[
 A_Q=B_P-\{x\}+\{y\}.
\]

If `H>=2ell`, this splice creates no internal coordinate one-run of length at
most `H` precisely when

\[
 x\notin I_P,\qquad y\notin O_Q,
 \qquad I_P\cap O_Q=\varnothing.
\tag{3.1}
\]

Indeed, a newly internal run must either be the terminal run of `x`, the
initial run of `y`, or the fusion of a finite terminal run from `P` with a
finite initial run from `Q`.  For a geodesic segment, those finite boundary
runs are indexed exactly by `I_P` and `O_Q`.

The endpoint `B_P` and start `A_Q` are independent uniform middle sets, so

\[
 \Pr(B_P\sim A_Q)=\frac{m^2}{W}.
\tag{3.2}
\]

Conditional on the displayed adjacency, `I_P` is a uniform `ell`-subset of
`B_P`, `O_Q` is an independent uniform `ell`-subset of `A_Q`, and the
exchange coordinates are uniform.  Therefore the exact conditional
probability of (3.1) is

\[
 \sigma_\ell=
 \left(\frac{m-\ell}{m}\right)^2
 \frac{\binom{m-1-\ell}{\ell}}
      {\binom{m-1}{\ell}}.
\tag{3.3}
\]

For `ell=o(sqrt(m))`,

\[
 \sigma_\ell=1-O(\ell^2/m).
\tag{3.4}
\]

Hence a fixed ordered pair of independent segments admits a safe oriented
splice with probability

\[
 \boxed{\frac{m^2}{W}\sigma_\ell.}
\tag{3.5}
\]

If `p=(1+o(1))W/L_0` independent segments are sampled, the expected safe
outdegree of one segment is

\[
 (p-1)\frac{m^2}{W}\sigma_\ell
 =(1+o(1))\frac{m^2}{L_0}.
\tag{3.6}
\]

More sharply, conditional on one segment, the events of a safe outgoing
splice to the other independent segments are independent.  Thus

\[
 \Pr(\text{a fixed segment has no safe outgoing splice})
 =\left(1-\frac{m^2}{W}\sigma_\ell\right)^{p-1}.
\tag{3.7}
\]

When `ell=o(sqrt(m))`, a union bound over all segments shows that with
probability `1-o(1)` there is no isolated outgoing segment; the same holds
for incoming splices, since

\[
 \log p-(1+o(1))m^2/L_0\longrightarrow-\infty.
\tag{3.8}
\]

This proves rigorously that isolated endpoints are absent in the independent
Hall expansion and control after iterative splices are still missing.  More
generally, without `ell=o(sqrt(m))`, the exact sufficient condition for this
union bound is

\[
 \frac{m^2}{L_0}\sigma_\ell-\log(W/L_0)\longrightarrow+\infty.
\tag{3.9}
\]

The weaker hypothesis `L_0=o(m)` is not sufficient; for example,
`L_0=m^(3/4)` makes `sigma_ell=exp(-Theta(sqrt(m)))`.

The safety test (3.1) is deliberately a one-joint statement.  Static safe
edges need not compose: a coordinate may enter in one segment, persist
through an intermediate segment, and leave in a third, creating a short
internal run only after the second splice.  After a splice, the boundary-run
state of the composite is not described merely by the last original
segment's `I` or `O` set.  Any iterative theorem must update the full
depth-`H` endpoint history.

## 4. Why marginal symmetry is insufficient

The ABKV existence theorems used for the current atom matching and cover
control edge count, degree, codegree, and uncovered vertices.  Their stated
conclusions do not control the distribution of selected endpoints or the
safe-splice graph.  Coordinate transitivity gives uniform one-vertex
marginals, but the component number and all endpoint adjacencies are invariant
under a common coordinate relabelling.  Randomly relabelling a fixed selected
family therefore makes it fully coordinate-symmetric without changing its
splice graph at all.

Consequently no improvement over Theorem 1 follows from symmetry alone.  A
randomized-nibble or absorber proof must retain an explicit endpoint
quasirandomness invariant, such as a Hall-type expansion statement for the
safe directed splice graph.  The independent calculation in Section 3 shows
that the desired density is available; proving that the integral atom cover
retains it is the remaining endpoint-packing theorem.
