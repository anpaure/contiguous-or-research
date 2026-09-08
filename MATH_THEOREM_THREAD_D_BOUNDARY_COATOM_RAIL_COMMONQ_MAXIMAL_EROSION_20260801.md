# Boundary coatom rails have an exact zero-length common-cap criterion

Date: 2026-08-01  
Lane: Thread D, folded-C8 boundary physicalization  
Status: exact maximal-erosion/common-cap theorem and an explicit positive
folded codimension-two rail.  The direct aligned zero-charge embedding and
every simple phase-common lower-palette rail are ruled out; non-common rail,
sidecar, upper-support, and compiler alternatives remain.

## 0. Verdict

Recutting the aligned folded comparator so its two ray corridors meet the
one global linear cut can avoid the internal split/stutter obstruction.  It
does not make source reconstruction automatic.

For any proposed pair of phase owner words `T^0,T^1`, the exact test is the
screened maximal-erosion criterion of Section 1.  In particular, assume
first that each phase's unpinned maximal erosion is nonempty and reconstructs
the complete owner word.  Then forcing a left boundary source cap `X_L` and
a right boundary cap `X_R` changes no source length and reconstructs phase
`epsilon` iff

\[
 T_0^\epsilon\setminus T_1^\epsilon\subseteq X_L,
 \qquad
 T_{W-1}^\epsilon\setminus T_{W-2}^\epsilon\subseteq X_R, \tag{0.1}
\]

together with nonempty containment in the corresponding endpoint owners.
The phase-specific maximal endpoint letters are

\[
 M_L^\epsilon=X_L\cap T_0^\epsilon,
 \qquad M_R^\epsilon=X_R\cap T_{W-1}^\epsilon.          \tag{0.2}
\]

All other source letters may be the maximal erosion letters.  Thus a genuine
rank-balanced owner link satisfying (0.1) has a phase-common source cap and
changes **zero source positions relative to that same owner path's standard
`W+d` inverse**.  This is not a claim of zero birth cost relative to a
different old macro.

This also gives a sharp obstruction.  In a simple coatom rail

\[
 T_i=X\cup(D\setminus\{x_i\}),\qquad |D|=d,             \tag{0.3}
\]

the first and last endpoint directions lie outside the common core `X`.
Consequently the bare endpoint letter/cap `X` cannot reconstruct the rail.
It must be enlarged by one edge direction on each end.  Therefore using the
folded hosts `X_L,X_R` literally as the cores of the two boundary coatom
rails is a no-go; the exact positive replacement is a direction-augmented
endpoint cap, or a different owner ordering whose endpoint directions are
already contained in the displayed hosts.

There is in fact such a different owner geometry.  Section 3.2 gives an
explicit phase-independent codimension-two missing-pair rail of `d+1`
owners whose literal endpoint source letters are exactly `X_L,X_R`.  It is
Johnson, simple, locally residence-clean, and has an exact common source of
the optimal length `2d+1`.  What remains unproved is the global zero-charge
splice: its two erosion halos must coincide with the ambient halos of the
one recut folded chronology, while palette, upper support, and compiler Hall
survive.

For the direct aligned splice, this last test is now negative: no common
right endpoint both joins the two phase exteriors and contains `X_R`.
Independently, exact phase equality of the two boundary lower colours forces
the common rail to repeat its first owner at the last endpoint.  Hence the
literal simple-common-rail implementation is a no-go despite the positive
local source rows.  The remaining escape is a non-common rail or a
phase-dependent lower-colour circuit together with a different halo splice.

The theorem distinguishes **common cap** from **literal common source**.  A
single identical source word `Q` in both phases implies
`T^0=D^dQ=T^1`; it cannot encode two different folded owner chronologies.
The positive object is one phase-common cap supporting two phase-specific
source words.

## 1. Exact common-cap criterion

Let

\[
 T^\epsilon=(T_0^\epsilon,\ldots,T_{W-1}^\epsilon),
 \qquad \epsilon\in\{0,1\},                            \tag{1.1}
\]

be two proposed rank-`r` owner paths of the same length `W>=2`.  Define their
maximal depth-`d` erosions

\[
 E_p^\epsilon=
 \bigcap_{i=\max(0,p-d)}^{\min(W-1,p)}T_i^\epsilon,
 \qquad0\le p<W+d.                                     \tag{1.2}
\]

Let `P_p` be prescribed nonempty phase-common source caps and put

\[
                         M_p^\epsilon=P_p\cap E_p^\epsilon. \tag{1.3}
\]

### Theorem 1.1 (screened maximal-erosion equivalence)

There exist nonempty phase source words `Q^epsilon`, both using the cap word
`P`, such that

\[
 Q_p^\epsilon\subseteq P_p,
 \qquad D^dQ^\epsilon=T^\epsilon                       \tag{1.4}
\]

iff, for both phases,

\[
 M_p^\epsilon\ne\varnothing\quad(0\le p<W+d),
 \qquad
 T_i^\epsilon=\bigcup_{p=i}^{i+d}M_p^\epsilon
                         \quad(0\le i<W).               \tag{1.5}
\]

When (1.5) holds, `Q^epsilon=M^epsilon` is a witness.

#### Proof

Any source letter at address `p` belongs to every owner using that address,
so it lies in `E_p^epsilon`; the cap further restricts it to
`M_p^epsilon`.  Hence any feasible word is pointwise contained in `M`, and
its owner unions imply the reconstruction equality in (1.5).  Conversely
(1.5) directly says that `M` is a nonempty source word dilating to `T`.
\(\square\)

With free caps, take

\[
                         P_p=E_p^0\cup E_p^1.            \tag{1.6}
\]

Then (1.5) reduces to nonempty maximal erosions and
`D^dE^epsilon=T^epsilon`.  Thus common-cap containment has no additional
integrality gate once the two owner paths are individually exact erosions.
The sets in (1.6) are source caps only; their ranks may exceed the owner
rank and no rank claim about the caps is intended.

## 2. Two forced boundary letters

Assume throughout this section that the baseline maximal erosions are
nonempty and exact:

\[
                         D^dE^\epsilon=T^\epsilon.       \tag{2.0}
\]

Now use the free cap (1.6) at every interior address, but prescribe boundary
caps `X_L,X_R` at addresses `0,W+d-1`.  Since

\[
 E_0^\epsilon=T_0^\epsilon,
 \qquad E_{W+d-1}^\epsilon=T_{W-1}^\epsilon,            \tag{2.1}
\]

the maximal allowed endpoint letters are exactly (0.2).  Source address `0`
occurs only in owner row `0`, and the last source address occurs only in the
last owner row.  All interior reconstruction rows are therefore unchanged.
At the left endpoint,

\[
 \bigcup_{p=1}^{d}E_p^\epsilon
      =T_0^\epsilon\cap T_1^\epsilon,                   \tag{2.2}
\]

because the prefix intersections are nested and
`E_1=T_0\cap T_1` is the
largest.  Hence

\[
 T_0^\epsilon=M_L^\epsilon
                  \cup(T_0^\epsilon\cap T_1^\epsilon)  \tag{2.3}
\]

iff the first condition in (0.1) holds.  The reversed argument gives the
right condition.  This proves:

### Corollary 2.1 (zero-length boundary-pin theorem)

Subject to the baseline exactness hypothesis (2.0), the two boundary caps
admit exact phase source words of the original length `W+d` iff, for each
phase,

\[
\begin{aligned}
 &M_L^\epsilon,M_R^\epsilon\ne\varnothing,\\
 &T_0^\epsilon\setminus T_1^\epsilon\subseteq X_L,\\
 &T_{W-1}^\epsilon\setminus T_{W-2}^\epsilon\subseteq X_R.
\end{aligned}                                           \tag{2.4}
\]

The witness is the maximal erosion with its two endpoint letters replaced
by (0.2).  No source position is inserted or deleted.

Without (2.0), the endpoint containments are only necessary.  The fully
general iff statement is Theorem 1.1: in addition, every interior erosion
letter must be nonempty and every interior owner row must equal the union
of its `d+1` maximal erosion letters.

If the actual endpoint source letters must equal `X_L,X_R`, rather than
merely lie in those caps, add

\[
 X_L\subseteq T_0^\epsilon,
 \qquad X_R\subseteq T_{W-1}^\epsilon                  \tag{2.5}
\]

for both phases.  Under (2.5), put `M_L=X_L,M_R=X_R` in the same proof.

## 3. Explicit maximal erosion of a coatom rail

Let `X,D` be disjoint, `X` nonempty, `|D|=d`, and let

\[
 T_i=X\cup(D\setminus\{x_i\}),qquad0\le i<d,          \tag{3.1}
\]

in one simple order.  Its maximal erosion has length `2d` and is

\[
 E_p=
 \begin{cases}
 X\cup(D\setminus\{x_0,\ldots,x_p\}),&0\le p<d,\\
 X\cup(D\setminus\{x_{p-d},\ldots,x_{d-1}\}),&d\le p<2d.
 \end{cases}                                           \tag{3.2}
\]

In particular

\[
                              E_{d-1}=E_d=X,             \tag{3.3}
\]

and the endpoint directions are

\[
 T_0\setminus T_1=\{x_1\},
 \qquad T_{d-1}\setminus T_{d-2}=\{x_{d-2}\}.         \tag{3.4}

The endpoint cap `X` omits both required directions.  Replacing the maximal
endpoint letters by `X` loses the first and last owner rows.  Replacing them
by

\[
                         X\cup\{x_1\},
              \qquad    X\cup\{x_{d-2}\}               \tag{3.5}
\]

reconstructs all owners exactly.  Formula (3.2) also proves

\[
                       D^dE=T,\qquad |E|=|T|+d,         \tag{3.6}
\]

so the rail itself has optimal source length and no hidden additive charge.

For two phase orders, the phase-common endpoint caps are the unions of the
two letters in (3.5), and the interior free caps are the pointwise unions of
their maximal erosions.

### 3.1 Literal folded-host rows

In the authenticated folded notation,

\[
 X_L=K\cup\{z,a_1,a_3,f_1\},\qquad
 X_R=K\cup\{z,a_1,a_3,f_d\}.                         \tag{3.7}
\]

An exact left boundary-coatom template in phase `epsilon` is obtained by
choosing a `d`-set of directions
`D_L^epsilon={ell_0^epsilon,...,ell_(d-1)^epsilon}`
disjoint from `X_L` and putting

\[
 T_{L,i}^\epsilon
   =X_L\cup(D_L^\epsilon\setminus\{\ell_i^\epsilon\}). \tag{3.8}
\]

Its unpinned maximal source rows are (3.2) with `X=X_L`; after the endpoint
pin, the first row is replaced as below.  In particular, the two central
rows are `X_L,X_L`, while its exposed boundary row must be

\[
 Q_{L,0}^\epsilon=X_L\cup\{\ell_1^\epsilon\}.          \tag{3.9}
\]

Thus both phases fit the single literal cap

\[
 P_{L,0}=X_L\cup
       \{\ell_1^0,\ell_1^1\}.                          \tag{3.10}
\]

There is an identical right template with `X_R`, direction bank
`D_R^epsilon`, and the appropriate last direction.  Equations
(3.8)--(3.10) are explicit owner/source rows, not an existence claim for
the ambient folded chronology.  They show exactly why the bare proposed
letters `Q_{L,0}=X_L,Q_{R,last}=X_R` fail and exactly what a physical owner
link has to supply to remove that failure without adding a position.

### 3.2 A positive folded codimension-two rail

The literal folded hosts can nevertheless occur without augmentation if
they are endpoint letters of one codimension-two rail, rather than the
cores of two separate coatom rails.  Put

\[
 C=K\cup\{z,a_1,a_3\},\quad
 D=C\cup\{f_0,f_1,\ldots,f_{d+1}\},\quad
 X_L=C\cup\{f_1\},\quad X_R=C\cup\{f_d\}.              \tag{3.11}
\]

Here `|D|=r+2`.  For `d>=4`, order the filler labels as

\[
 (v_0,\ldots,v_{d+1})=
 (f_2,f_{d+1},f_1,f_3,f_4,\ldots,f_{d-2},
       f_d,f_{d-1},f_0),                               \tag{3.12}
\]

where the middle interval is empty when `d=4`.  Define

\[
 M_j=\{v_j,v_{j+1}\},\qquad T_j=D\setminus M_j,
                         \qquad0\le j\le d.            \tag{3.13}
\]

The `T_j` are distinct rank-`r` owners and consecutive rows are Johnson
adjacent.  Moreover

\[
 T_0\setminus T_1=\{f_1\}\subseteq X_L,\qquad
 T_d\setminus T_{d-1}=\{f_d\}\subseteq X_R.           \tag{3.14}
\]

Thus the endpoint criterion is met by the literal folded hosts.  An exact
source word of length `2d+1=(d+1)+d` is

\[
\begin{aligned}
 A_0&=X_L,\\
 A_p&=D\setminus\{v_0,\ldots,v_{p+1}\} &&(1\le p\le d),\\
 A_p&=D\setminus\{v_{p-d},\ldots,v_{d+1}\}
                                      &&(d\le p\le2d-1),\\
 A_{2d}&=X_R.
\end{aligned}                                           \tag{3.15}
\]

The two formulas agree at `p=d`, and direct union gives

\[
                              D^dA=(T_0,\ldots,T_d).     \tag{3.16}
\]

Indeed the unpinned rows in (3.15) are exactly the intersections of the
incident owners.  For `1<=i<=d-1`, in owner window `i`, a filler `v_t` with
`t<i` occurs in the suffix-erosion row at `p=i+d`, while one with `t>i+1`
occurs in the prefix-erosion row at `p=i`; only `v_i,v_{i+1}` are absent.
The endpoint replacements preserve rows `0,d` by (3.14) and Corollary 2.1.
This proves (3.16).

This rail is phase-independent, hence `A` itself is a literal common source
word on the rail.  It attaches by Johnson edges to both folded phases: the
two possible predecessor missing pairs are

\[
 \{a_1,f_{d+1}\},\quad\{a_3,f_{d+1}\},                \tag{3.17}
\]

and the two possible successor missing pairs are

\[
 \{a_3,f_0\},\quad\{a_1,f_0\}.                         \tag{3.18}
\]

They share `f_(d+1)` with `M_0` and `f_0` with `M_d`, respectively.
For each filler coordinate the zero positions along (3.13) are one or two
consecutive indices.  Hence every positive run created inside the rail
meets a rail endpoint.  Including either natural predecessor/successor pair,
the displayed collar has no internal positive run at all: every surviving
run meets one of its two outer cuts.  This is residence-transparent relative
to those displayed cuts, not an ambient residence certificate.  Further
owners can make an outer run internal, so the next collar inequalities must
still be checked after global attachment.

This proves a positive **local** owner/source/common-cap/residence lemma.
It does not by itself prove zero birth cost in the ambient macro.  The
isolated word (3.15) contains both `d`-cell erosion halos.  Net zero source
length follows only when the rail replaces exactly `d+1` old owner rows and
those halos are identified with the two recut ambient halos in the global
maximal erosion.  The complete cross-join reconstruction equations of
Theorem 1.1, absence of collisions with every other ambient owner and exact
owner-set replacement, lower-palette recycling, upper support, and terminal
compiler Hall remain to be checked.

The independent literal folded audit
`MATH_THEOREM_THREAD_D_C8_ALIGNED_SINGLECUT_COATOM_LINK_20260801.md`
settles two of those rows negatively for the simple common-rail class.
For any common first/last rail owners compatible with both phase exteriors,
write their omitted pairs as

\[
 M_0=\{f_{d+1},x\},\qquad M_d=\{f_0,y\}.               \tag{3.19}
\]

Equality of the two phase boundary-lower colour multisets forces
`x=f_0,y=f_(d+1)`, hence `M_0=M_d` and `T_0=T_d`.  Thus no **simple common
rail** can also preserve the exact phase boundary lower palette.  Moreover,
for the literal aligned `p_L,...,p_L+d` replacement, every common right
owner adjacent to both phase exteriors either omits `f_d` or omits both
`a_1,a_3`; none contains `X_R`.  Consequently the direct aligned
zero-charge embedding is impossible.  A positive full macro must use a
phase-dependent two-colour lower circuit/non-common rail and a different
ambient halo identification.  These no-gos do not affect the local source
equations (3.11)--(3.16).

For the displayed rail, each phase collar has `d+2` pairwise-distinct lower
colours, but the two phase counters differ by two colours in each direction.
Its `d+2` upper occurrences have `d+1` distinct values: the left boundary
upper value repeats the first internal upper value, while the right boundary
value is new.  Thus even the positive local rail should be viewed as a
controlled boundary-debt packet, not as a completed palette factor.

## 4. One global cut and ambient collars

The intended physical use places one coatom rail at each side of the one
global linear cut.  This clips the outer run of each rail, but its inner end
is attached to the ambient owner chronology.  The local formula (3.2) must
not be concatenated as a separate `2d`-letter source block: doing so would
double-count erosion halos and add length.

Instead form the complete proposed owner word `T^epsilon`—left boundary
rail, ambient middle, right boundary rail—and apply (1.2) globally.  Its
source has exactly `W+d` positions.  The construction succeeds iff (1.5)
holds.  Equivalently, all `d` source intersections crossing each rail/middle
join must be nonempty and the affected boundary owner rows must reconstruct.
This is the exact source-halo condition; common owner endpoints alone give
only one common erosion letter and are insufficient.

Residence is a separate owner-level row.  The opened simple coatom cycle has
all local positive runs boundary-clipped, but after joining its inner end to
the ambient word the collar inequalities of
`MATH_THEOREM_THREAD_D_LINK_CYCLE_RESIDENCE_CUT_AND_PALETTE_20260801.md`
must hold.  Maximal erosion cannot repair a residence defect already present
in `T`.

## 5. Folded-C8 consequence

For the current aligned folded chronology, the desired internal full hosts
are not contained in the maximal erosion at their aligned base addresses;
retaining them creates two rank-`r+1` owner rows.  Pairing the two phase bases
keeps rank but produces three equal owners.  Moving the interface to the
global cut avoids those *internal* no-gos only after a new owner-level link
is supplied.

Theorem 1.1 together with Corollary 2.1 is the complete test for that
proposed link.  If `X_L,X_R` are the common cores of literal coatom rails,
Section 3 rules them out as bare endpoint letters: each misses one required
endpoint direction.  The codimension-two rail of Section 3.2 instead has
endpoint differences `f_1,f_d` already contained in the displayed hosts,
and therefore gives an exact local positive solution.  Global zero charge
still requires its two maximal-erosion halos to be the ambient cut halos,
not separately concatenated copies.  Lower-colour boundary debt, upper
support, and terminal compiler Hall remain separate.

## 6. Audit

Run

```text
python3 scratch/audit_threadD_boundary_coatom_rail_commonq_20260801.py --write
```

The dependency-audited replay checks the coatom formulas for `3<=d<=64` and
the positive folded rail for `4<=d<=64`: exact dilation, optimal source
length, literal endpoint hosts, Johnson adjacency to both phase collars,
distinct internal lower colours, and absence of short runs internal to the
displayed predecessor--rail--successor segment.  Runs meeting that segment's
outer ends still require ambient collar inequalities after further gluing.
The replay does not identify the rail's two erosion halos with an ambient
folded macro or certify the remaining lower sidecar/upper/compiler rows.

Frozen H100 CPU replay (`prlimit --as=2 GiB`, one process):

```text
scratch/audit_threadD_boundary_coatom_rail_commonq_20260801.py
  SHA-256 3980a70ffd28cc0b42702eda3dd43fe27a1aaa2c9628c593f2b549fc67431fe6
scratch/threadD_boundary_coatom_rail_commonq_20260801.audit.json
  SHA-256 1efd103517f8053dcd08a2114657387927c29590c46eb86dd7602247b6248e84
  payload c2f7b78d44f7485e0c6f27f26007e30cf3790357f28278d3c412049a4a7483fe
```
