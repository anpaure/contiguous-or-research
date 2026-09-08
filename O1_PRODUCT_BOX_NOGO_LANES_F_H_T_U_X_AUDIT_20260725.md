# Audit of O(1) lanes F, H, T, U, and X

Date: 2026-07-25

This audit reads the complete current proof bodies in:

- `MATH_ATTACK_F_COMPACT_THREEBOX_NO_GO_20260725.md`;
- `MATH_ATTACK_H_MULTISCALE_THREE_FOURBOX_FUSION_20260725.md`;
- `MATH_ATTACK_T_CONTIGUOUS_CORE_CLASSIFICATION_20260725.md`;
- `MATH_ATTACK_THREE_SHELL_ENDPOINT_NO_GO_20260725.md`;
- `MATH_ATTACK_FOURBOX_ONEPIN_ABSORPTION_NOGO_20260725.md`;
- `MATH_ATTACK_U5_EQUAL_SURFACE_BRAID_20260725.md`;
- `MATH_ATTACK_U6_COMPACT_FOURBOX_COUNTEREXAMPLE_20260725.md`;
- `MATH_ATTACK_X_NONPRODUCT_PACKET_AGGREGATION_20260725.md`.

The verdicts below concern the actual proved statements and their stated
scope.  None of these reports proves the full constant-one theorem.

## Executive classification

| lane | principal result | audit verdict | active-task recommendation |
|---|---|---|---|
| F | unrestricted two-endpoint lower bound for a dominant three-box | **sound, completed no-go** | archive as an active search lane after merging the theorem into the common product-box obstruction record |
| H | literal wreath portal fusion plus ambient equal-shell sharing toll | **sound; positive construction and scoped no-go, live extraction gate conditional** | **retain** |
| T | contiguous-core, internally confined shell, and one-pin repair no-gos | **sound, architecture-scoped, largely completed/overlapping** | archive as an active lane; retain the theorem files as constraints on H/U |
| U | equal-surface common-lift braid, pin gate, and compact four-box counterexample | **sound; equal-ray PACK remains conditional/open** | **retain** |
| X | nonproduct strip packets and independent-packet chronology obstruction | **sound modulo the two explicitly imported strip-cover theorems; full-cube completion open** | **retain** |

If only sixteen live tasks are kept, the clean choice among these five is to
keep H, U, and X.  F and T have delivered durable no-go theorems but no
remaining mechanism as distinct as the three retained gates.  If a separate
obstruction/audit task is desired, F and U6 can instead be consolidated into
one endpoint-dual product-box task rather than occupying two live slots.

## F: compact three-box endpoint dual

### Verified theorem

For (r\ge p+q), with (V=(p+1)(q+1)), the plateau layers have size
(V), and every literal range-maximum word satisfies

\[
g_3(p,q,r)\ge V+\left\lceil\frac{V(r-p-q)}{2r}\right\rceil.
\]

In particular,

\[
g_3(t,t,3t)\ge (t+1)^2+\left\lceil\frac{(t+1)^2}{6}\right\rceil.
\]

### Reconstruction checks

1. A selected common-left-endpoint class and a selected
   common-right-endpoint class are target chains.  Their intersection has at
   most one target because the two physical endpoints determine one interval.
2. Across two adjacent plateau ranks, a partition into (V+\delta) endpoint
   chains contains at least (V-\delta) target covers.
3. Telescoping \(\phi=x+y\) bounds horizontal covers by
   \((p+q)\delta\).  Thus the partition contains at least
   \((r-p-q)V-r\delta\) vertical covers.
4. A vertical cover cannot occur in both endpoint partitions: otherwise the
   corresponding left and right classes would have two common targets.
5. There are exactly \(V(r-p-q)\) vertical plateau covers.  Adding the two
   ledgers gives the displayed bound with the ceiling in the correct
   direction.

The proof does not require canonical witnesses, saturation, confined letters,
or unique occurrences.  The same endpoint argument survives a translated
ambient realization after local projection; allowing projected zero letters
does not weaken the endpoint lower bound.

### Scope

This refutes a uniform compact-ratio **one-parent** theorem, including the ray
((t,t,3t)).  It does not refute a near-diagonal-only theorem and cannot be
summed over product parents when a global word shares endpoints between them.

## H: multiscale three/four-box fusion

### Verified positive construction

For an exact wreath factor on (2m+1) coordinates, the block

\[
E_0,\ldots,E_{2m},E_0,\ldots,E_{2H},
\qquad E_j=I_\pi(j,m-H),
\]

literally exposes the full flag
(I_\pi(j,m-H),\ldots,I_\pi(j,m+H+1)) at every original start.  The repeated
prefix is exactly long enough even for the start (j=2m).  Concatenating an
exact factor has length

\[
W+\frac{2H+1}{2m+1}W.
\]

The rank-(m) intervals are exact by the factor property, and the
rank-(m+1) intervals are exact by cyclic complementation.

The coordinate-relabeling argument is also correct: conditional on the image
of (X\in\binom{[2m+1]}m), the added point in its paired upper cover is uniform
among (m+1) choices, while a product of (b) fixed chains has at most (b)
internal upper covers.  This yields \(\rho W-o(W)\) genuine common-start
cross-parent incidences for every positive-mass selected upper-middle sector.
It does **not** identify those incidences with the sloped shoulder demands.

### Verified ambient shoulder and aggregation ledger

For the three-box band in Lemma 3.1, the audited quantities are

\[
F=\frac{k(k+1)}2,\quad
E=\frac{k(k+1)(k+2)}6,\quad
M=\frac{k(k+1)(k-1)}3.
\]

The adjacent-layer cover count, boundary-potential telescope, and
left/right orthogonality give exactly

\[
(c+2k)(C_L+C_R-2V)
\ge(c-p-q+2k)V+\frac{k(k+1)(k-6(p+q)-4)}3.
\]

At (p=q=s,c=2s,k=\lfloor s/8\rfloor), the leading quotient is
(289/3456\).  All selected witnesses may leave the child box; only their
target endpoints enter the proof.

The complementary-shell decomposition of ([0,R]^4), including the rank-one
offset of the (\mathcal B_s\) child, is correct.  The exact width identity

\[
W_R=1+\sum_{s=1}^R((s+1)^2+s^2)
\]

aligns every chosen child width layer at global rank (2R).  Double-counting
endpoint--child incidences in one ambient word legitimately yields

\[
\mathcal C_R\ge
\left(\frac{289}{3456}-o(1)\right)W_R-2D.
\]

This is a genuine global necessary sharing ledger, not an invalid sum of
independently paid local word lengths.

The laminar identity

\[
\mathcal C_R=\sum_{v,j,\sigma}(a_{v,j,\sigma}-1)_+
\]

and its consequence

\[
h_Rs_R\ge\left(\frac{289}{10368}-o(1)\right)R^2
\]

are correct under the report's explicit meaning of (s_R): the number of
**actual shared typed physical endpoint sites** at one hierarchy node.
They do not rule out a surface-scale root, a linear-depth comb, or unrestricted
baseline reuse.

### Status

The proved construction and no-go are distinct and useful.  The pointed
cyclic-flag extraction/multidepth-surjectivity assertion remains unproved.

## T: contiguous cores, shells, and one-pin completion

### Contiguous translated core

The exterior-antichain injection is correct even for witnesses crossing the
entire core: a witness not ending in the suffix and not wholly inside the
join-closed core must start in the prefix.  The rank-(R) and rank-(2R)
shoulder counts yield

\[
|P|+|S|\ge f_R(\max\{s,3k-s\}).
\]

The comparison with (W_R-W_{R-k}) is exact.  The only fixed-thickness
first-order survivor is the centered case (k) even, (s=3k/2).

The additional lower-boundary endpoint toll is also sound.  After deleting
the core, all witnesses for the down-set remain wholly in (P) or (S).
For the (M) rank-(R) antichain witnesses, strictly ordered left endpoints
force strictly ordered right endpoints.  Writing their offsets in a word of
length (M+D) bounds the lower-rank capacity by

\[
L\le(M+R-1)D.
\]

This excludes every fixed centered thickness and every centered
(k<(2/\sqrt3-o(1))\sqrt R).  The specialized two-zero-face (4R-1))
argument is consistent: common height providers for fixed (x)- and
(y)-row roots must lie between the roots, and two different heights force
opposite chronological orders.

### Internally confined shells

The exact shell antichain

\[
|([0,t]^3\setminus[0,t-k]^3)\cap\{x+y+z=2t\}|
=\frac{3k}{2}(2t+3-3k)
\]

for (t\ge3k) is correct.  Summing it over disjoint or overlapping shell
hulls gives the stated factor-two confined-module bound and the necessary
((3/4-o(1))R^2) overlap incidence.  Repeating the count directly with
selected left and right endpoints gives the architecture-free requirement of
quadratic cross-window reuse on **each** endpoint side.  It does not rule out
such reuse.

### One-pin absorption

Given the U5 endpoint toll, the inequality

\[
6e+b\ge\Gamma_r-4r-4
\]

is correct.  The zero-slope and lateral one-coordinate raises all use the
same (r)-target family, hence supply at most (2r) side-typed middle
endpoints.  A vertical raise forces a completion position outside the
third-coordinate-zero literal spine, and one such position serves at most
one left and one right incidence.  Thus pure one-pin completion pays
(289r^2/10368+O(r)).

This is explicitly not an unrestricted PACK lower bound: factoring the
literal spine, using multipin owners, or moving to other shared sites escapes
it.

### Status

All three no-go statements are sound but are architecture exclusions rather
than a surviving positive program.  Their live content is already absorbed
by H's high-degree-sharing gate and U's multipin PACK gate.

## U: equal surface braid and compact four-box counterexample

### Equal-surface braid

The common-lift word is literal.  Pairing decreasing/increasing hook chains
around the lift (e) covers every interface point (a_{t,v}) literally and
every (b_{t,v}=a_{t,v}\vee e) by a monotone interval.  Its exact length is

\[
N_r+\lceil r/2\rceil
=W_r-\lfloor r/2\rfloor-2.
\]

The sloped matching has

\[
M_r(k)=r(2k+1)-k(k+1),
\]

and for (k=\lfloor(r-1)/8\rfloor) its capacity exceeds the two-child toll
by (29r^2/432+O(r)).  The full-drain sums and constants
(5/64,289/5184,29/1296) follow by summing the verified quadratic
coefficients.

The common-lift optimality proof is valid: truncating at the first lift
partitions (J_r) into at most two product-order chains per lift, and
(\operatorname{width}(J_r)=r).  The middle-queue invariant

\[
4e+a\ge\Gamma_r
\]

is an exact two-child endpoint-union/intersection count.  The onion-block
(5r^2+3r) lower bound uses only literal subfamilies that remain forced after
cross-child joins; the report correctly withdrew the stronger false count.

The live equal-ray PACK theorem and pin-compatible middle absorption remain
unproved.

### Compact four-box counterexample

Origin-subbox deletion and translated ambient retraction are valid
join-preserving operations.  The four-dimensional shoulder ledger has the
correct corner quantities

\[
F_k=\binom{k+2}{3},\quad
E_k=\binom{k+3}{4},\quad
M_k=3\binom{k+2}{4},
\]

and gives, at ((t,t,t,3t)) with (k=\lfloor t/2\rfloor),

\[
g_4(t,t,t,3t)\ge\frac{561}{512}t^3-O(t^2).
\]

For ((36n,36n,36n,105n)), the middle-section width is

\[
\left(36^3-\frac98\right)n^3+O(n^2).
\]

Embedding the boundary subbox at scale (35n) gives the exact positive
gap (165579n^3/512-O(n^2)).  The full-dimensional collar is also valid:
the width upper bound by projection to the first three coordinates repairs
the zero-mass-single-ray issue and makes the independently paid SCD average
lose (Omega(W)).

This does not aggregate against a genuinely global word sharing positions
between parents and does not settle the equal four-box ray.

## X: nonproduct packet aggregation

### Verified exact packet mechanics

The reverse-block initialization formula, the two-block embedding of any
literal packet word, the full-strip MTF transition, the root-block count
(2H+2), and the exact aggregate surplus ledger all check.  The two positive
band theorems rely on their explicitly imported economical matching/cover
inputs; conditional on those previously audited theorems, the literal MTF
conversion and the (W+o(W)) band bounds are correct.

The parent-rainbow estimate is valid for a prescribed fixed finite-block SCD
partition.  Conditional on one middle target image, the deleted and added
(d)-sets are independent uniform choices, and weak displacement
compositions give a legitimate overcount.  It is not simultaneous over all
partitions.

### Verified independent-packet obstruction

At the (j)-th position of an independent packet only (j) packet suffixes
end there, and their ORs form a chain.  Double-counting omitted ranks gives

\[
\sum_{\alpha,j}(B-j)_+\le B\Gamma+D_I.
\]

The central-binomial defect estimate and the choice
(H^2\sim3\eta m/2) correctly imply that a near-width full-lattice
independent packet system puts at least ((1-\eta-o(1))W) middle mass in
packets larger than ((\sqrt{3\eta}+o(1))\sqrt{k}).  Hence retaining
((1-o(1))W) middle ownership in sub-Gaussian packets forces
(Gamma\ge(1-o(1))W).

The conclusion is restricted exactly as stated: merging/reassigning packets
or allowing decisive intervals to cross packet seams escapes it.

## Final recommendation

The strongest distinct live mathematical programs among these reports are:

1. **H:** extract globally distinct multidepth shoulder flags from the
   width-baseline wreath portal word;
2. **U:** solve equal-ray PACK by multipin, middle-queue-compatible surface
   absorption;
3. **X:** repacketize a leading middle mass into Gaussian-scale packets or
   construct a genuinely cross-seam global braid.

F, U6, and T should remain in the permanent proof ledger as verified no-go
theorems, but F and T need not consume separate live exploration tasks after
the thirty-task review is complete.
