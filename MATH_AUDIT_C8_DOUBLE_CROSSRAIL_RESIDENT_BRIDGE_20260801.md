# Independent audit: folded-C8 endpoint correction and double-crossrail bridge

Date: 2026-08-01  
Lane: independent symbolic referee  
Target: `MATH_THEOREM_C8_DOUBLE_CROSSRAIL_RESIDENT_BRIDGE_AND_PHASE_ENDPOINT_CORRECTION_20260801.md`  
Verdict: **GO as a local theorem, after two scope/notation corrections recorded below.**

The audit is symbolic.  I inspected the two replay programs and their frozen
JSON outputs, but did not use the finite replays as a substitute for the
all-`d` proof.

## 1. Endpoint correction

For the split endpoint word

\[
 \{z,b\},\ \{z,c\},\ \{z,c,f_d\},\ldots,
 \{z,c,f_1\},
\]

the two interval families are

\[
 I^S_j=[1,d-j+1],\qquad I^P_j=[d-j+2,d+1].
\]

Their unions are, directly,

\[
 \operatorname{OR}(I^S_j)=\{z,c\}\cup F[j+1,d],\qquad
 \operatorname{OR}(I^P_j)=\{z,c\}\cup F[1,j].
\]

They are adjacent and disjoint because
`max I^S_j + 1 = min I^P_j`.  The intervals are pairwise distinct, and a
prefix interval cannot equal a suffix interval.  Hence this gives exactly
`2(d-1)` distinct physical cells at one endpoint.

The authenticated finite statement is also correctly scoped.  In the first
seam the old phase has common base `a_3`, and in the symmetry-related seam
the new phase has common base `a_1`.  Thus the replays establish

\[
 P_0(j)\leftrightarrow S_1(j+1),\qquad
 P_1(j)\leftrightarrow S_0(j+1)
\]

respectively for every checked `2<=d<=12`.  The other phase on either one
fixed seam has unequal prefix and suffix bases and is not a cross bank.  The
theorem states this correctly.

The background claim is target-labelled, not occurrence-labelled.  The
endpoint map can identify old addresses only when their old interval unions
are equal.  Therefore it is injective on a matching whose left vertices are
distinct target masks.  After releasing the prefix-ray target masks and
assigning them to the displayed prefix cells, every remaining transported
matching edge avoids both ray families.  This does not preserve arbitrary
protected multiplicities of one target, and the theorem explicitly excludes
that stronger conclusion.

## 2. Owner path

Index the owners as

\[
 G_1,\ldots,G_d,B,A,H_1,\ldots,H_d,D,E.
\]

Since `|K|=r-d-3`, each displayed owner has rank `r`.  Every ordinary
transition consists of two different facets of `M_+` or `M_-`; `BA` and
`DE` exchange `f_0` and `f_(d+1)`.  Hence every transition is a Johnson
step.  Active-label and boundary-filler signatures separate the four owner
types, so the `2d+4` owners are distinct.

The `2d+3` intersections are exactly the list in equation (2.8).  Values in
one sweep are separated by their omitted filler pair.  Values in different
lines are separated by `a_1/a_3` and/or `f_0/f_(d+1)`.  Thus the lower
colours are all distinct.

The union support is exactly four values:

\[
 M_+,quad K\cup\{z,a_1\}\cup F,quad
 M_-,quad K\cup\{z,a_3\}\cup F.
\]

Here the two sweep values occur repeatedly; the assertion is support, not an
upper-rainbow assertion.

## 3. Residence

The internal-run calculation is exact.

* `K` and `z` persist throughout.
* `a_1` has a run of length `2d+2`.
* the non-boundary `a_3` run has length `d+2`;
* `f_0` has an internal run of length `d+2`;
* `f_(d+1)` has a safe run of length `d+1` and a clipped terminal
  occurrence;
* for `1<=s<=d`, the run of `f_s` strictly between its two omissions has
  length

\[
 (d-s)+2+(s-1)=d+1.
\]

All remaining short runs meet a path boundary.  Thus every internal
positive run has length at least `d+1`, which is precisely the depth-`d`
residence condition used by maximal erosion.

## 4. Maximal source and exact dilation

Let `E_p` be the maximal depth-`d` envelope.  At left-rail position
`p=d+s`, the covering owner window is

\[
 G_{s+1},\ldots,G_d,B,A,H_1,\ldots,H_{s-1};
\]

at right-rail position `p=2d+2+s`, it is

\[
 H_{s+1},\ldots,H_d,D,E.
\]

These windows prove all claimed cap inclusions.  In particular the endpoint
left letters may contain `K,z,a_1,f_s`, and the endpoint right letters may
contain `K,z,a_3,f_s`.

Since every replacement lies below its cap, `D^dQ` cannot overshoot the
owner path.  The reverse inclusion can be checked owner by owner using four
unchanged anchor envelopes:

\[
\begin{array}{c|c|c}
\text{owner}&\text{rail contribution}&\text{unchanged anchor contribution}\\ \hline
G_s&F[1,s-1]&E_{s-1}=K\cup za_1a_3\cup\{f_{d+1}\}\cup F[s+1,d]\\
B&K\cup za_1\cup F^\circ&E_d=K\cup za_1\cup\{f_{d+1}\}\\
A&K\cup za_1\cup F^\circ&E_{2d+1}=K\cup za_1\cup\{f_0\}\\
H_s&F[s+1,d]\cup F[1,s-1]&E_{2d+1}\cup E_{2d+2}=K\cup za_1a_3\cup\{f_0\}\\
D&K\cup za_3\cup F^\circ&E_{2d+2}=K\cup za_3\cup\{f_0\}\\
E&K\cup za_3\cup F^\circ&E_{3d+3}=E.
\end{array}
\]

Empty filler ranges are suppressed.  The unions in the final two columns
are exactly the displayed owners.  Therefore `D^dQ=T` for every `d>=2`.
All source letters are nonempty: `z` lies in every untouched maximal
envelope, and every replacement contains either its filler alone or a
nonempty active/core endpoint.

## 5. Both cross banks in one cap state

The left rail occupies positions `d+1,...,2d`; its prefix/suffix cells have
values

\[
 K\cup za_1\cup F[1,j],\qquad
 K\cup za_1\cup F[j+1,d].
\]

The right rail occupies `2d+3,...,3d+2` and gives the analogous pair with
`a_3`.  Within each ticket the intervals are adjacent and disjoint; the two
rail position ranges are disjoint.  Hence all `4(d-1)` cells are distinct
and both zero-block cross matchings coexist in the single source word `Q`.
This is stronger than the finite endpoint correction, which places only one
complete cross bank in either authenticated phase.

## 6. Sixteen-support forest

The common core `K` must be included in equations (4.1)--(4.2).  With that
core restored, every auxiliary target has rank `r+1` and its two selected
facets have rank `r`.  Six high targets and six boundary targets remain
after removing the four bridge-supported values, so there are exactly
twelve isolated Johnson edges.

Active signatures and boundary fillers separate all 24 auxiliary owners
from one another and from the bridge.  Their intersections are likewise
distinct and avoid the bridge lower palette.  Consequently the union is a
forest with

\[
 13\text{ components},\qquad 2d+28\text{ owners},\qquad
 2d+15\text{ distinct lower colours},
\]

and upper support equal to all sixteen canonical folded values.

The auxiliary-edge residence assertion is only **componentwise**: every
positive run in a two-vertex component is boundary-clipped.  It need not
remain resident after arbitrary concatenation.  The main theorem was
corrected to require a protected completion which either extends those
runs or keeps the corresponding boundaries.

## 7. Exact scope

The following are proved:

1. the endpoint-prefix correction for the authenticated seams through
   `d=12`;
2. the all-`d` local owner/source bridge;
3. exact rank, simplicity, lower-rainbow, four-value upper support, and
   depth-`d` residence of the bridge;
4. `D^dQ=T` and both literal cross banks in one cap state;
5. a componentwise resident thirteen-component forest carrying all sixteen
   folded upper support values.

The following are not proved:

1. embedding this protected forest into a spanning owner factor;
2. preserving clipped residence under that embedding;
3. transporting an arbitrary exterior/common-cap compiler matching through
   the prospectively planted source;
4. upper occurrence/rainbow multiplicities beyond support;
5. bounded-charge regeneration in a same-parity induction.

These exclusions agree with the theorem's stated frontier.  Subject to the
two clarifications above, the local construction is proof-safe.

