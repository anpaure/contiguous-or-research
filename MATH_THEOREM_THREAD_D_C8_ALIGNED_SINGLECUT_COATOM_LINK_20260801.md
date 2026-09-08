# The aligned folded-C8 caps admit a resident coatom link, but not a simple phase-common lower palette

Date: 2026-08-01  
Lane: Thread D, physical boundary of the four-block nonzero `C8` relation  
Status: exact local construction and sharp boundary-palette obstruction.  The
construction is not yet a zero-charge regenerative macro.

## 0. Verdict

The two useful members of the seven planted-host menu are

\[
 X_L=K\cup\{z,a_1,a_3,f_1\},\qquad
 X_R=K\cup\{z,a_1,a_3,f_d\}.                         \tag{0.1}
\]

They do admit a literal common owner/source rail.  For every `d>=4` there is
an explicit simple rank-`r` Johnson path on `d+1` owners which is internally
depth-`d` resident, is used unchanged in both phases, and has a nonzero exact
depth-`d` inverse whose first and last source letters are exactly `X_L,X_R`.
The small depths `d=2,3` have the explicit rows in Section 2.

This does **not** finish the planted-host macro.  The two phase-independent
upper boundary colours agree, but the two lower boundary colours do not.  In
fact, among all common codimension-two rails compatible with the two folded
phase exteriors, equality of the two phase boundary-lower palettes forces the
first and last owner to be equal.  Hence no simple common rail can preserve
the exact lower palette.

There are two further literal obstructions.

1. In the fixed folded owner fibre only one owner contains either cap.  The
   authenticated aligned path endpoints contain neither.  Merely recutting
   that cycle cannot put `X_L,X_R` at the two linear source ends.
2. The displayed inverse has `2d+1` source letters for `d+1` owner rows.  It
   is zero-charge relative to an already supplied `d+1`-owner chronology only
   when its left and right `d`-letter halos are identified with ambient
   boundary halos.  The cap letters alone do not prove this identification.

Thus the seven-host menu contains the correct two typed caps, and the owner
and residence equations are locally soluble, but **common lower palette plus
zero-charge ambient halo embedding remains open**.  One must allow either a
phase-dependent lower-colour circuit/sidecar or a genuinely different
non-common rail.

## 1. The authenticated aligned fibre cannot simply be recut

Suppress `K` only in prose and write `F[i,j]={f_i,...,f_j}`.  The common edge
cut in the aligned folded paths has endpoints

\[
 E_0=K+za_0a_2+F[1,d],\qquad
 E_1=K+za_0f_0+F[1,d].                                  \tag{1.1}
\]

Both phases have these same ordered endpoints.  The deleted lower and upper
colours are, respectively,

\[
 C_*=K+za_0+F[1,d],\qquad
 U_*=K+za_0a_2+F[0,d].                                  \tag{1.2}
\]

Neither endpoint contains `a_1` or `a_3`, hence neither contains `X_L` or
`X_R`.  More strongly, direct inspection of the eight active tensor states
and seven screens gives exactly one folded owner containing both `a_1,a_3`:

\[
                   U=K+za_1a_3+F[1,d].                  \tag{1.3}
\]

It contains both caps.  Every source letter at the first linear position is
used by the first owner window only, and every source letter at the last
linear position is used by the last owner window only.  Therefore placing
`X_L,X_R` at the two source ends requires two cap-containing owner endpoints.
A simple edge-cut path has two distinct endpoints, whereas (1.3) supplies
only one.  This proves the fixed-fibre recut obstruction.

The audit replays (1.1)--(1.3) for `2<=d<=12`; the uniqueness in (1.3) is the
constant active-octagon inspection and is dimension independent.

## 2. Explicit common coatom-link rail

Put

\[
 D=K\cup\{z,a_1,a_3\}\cup F[0,d+1].                    \tag{2.1}
\]

Since `|K|=r-d-3`, we have `|D|=r+2`.  For `d>=4`, order the filler labels as

\[
 (v_0,\ldots,v_{d+1})=
 (f_2,f_{d+1},f_1,f_3,f_4,\ldots,f_{d-2},f_d,f_{d-1},f_0).
                                                                  \tag{2.2}
\]

The middle range is empty when `d=4`.  Define omitted pairs and owners by

\[
                M_j=\{v_j,v_{j+1}\},\qquad
                T_j=D\setminus M_j\quad(0\le j\le d).   \tag{2.3}
\]

For the two small depths use

\[
\begin{array}{c|c}
d&(M_0,\ldots,M_d)\\ \hline
2&(f_2f_3,\ f_1f_2,\ f_0f_1),\\
3&(f_2f_4,\ f_1f_2,\ f_1f_3,\ f_0f_1).
\end{array}                                               \tag{2.4}
\]

### Theorem 2.1 (owner, residence and endpoint reconstruction)

The rows `T_0,...,T_d` are distinct rank-`r` owners and consecutive rows are
Johnson adjacent.  Every coordinate's omitted positions form an interval;
therefore every positive owner run either has length `d+1` or meets a path
boundary.  In particular the rail is internally depth-`d` resident.

Moreover

\[
 X_L\subseteq T_0,\quad T_0\setminus T_1=\{f_1\}\subseteq X_L,
 \qquad
 X_R\subseteq T_d,\quad T_d\setminus T_{d-1}=\{f_d\}\subseteq X_R. \tag{2.5}
\]

Let

\[
 E_p=\bigcap_{\max(0,p-d)\le j\le\min(d,p)}T_j
                 \qquad(0\le p\le2d).                  \tag{2.6}
\]

Then the literal source row

\[
 A_0=X_L,\qquad A_p=E_p\ (1\le p\le2d-1),\qquad A_{2d}=X_R \tag{2.7}
\]

is nonzero and satisfies

\[
                    \bigcup_{p=j}^{j+d}A_p=T_j
                       \qquad(0\le j\le d).             \tag{2.8}
\]

For the order (2.2), (2.7) is completely explicit:

\[
\begin{aligned}
 A_p&=D\setminus\{v_0,\ldots,v_{p+1}\}&& (1\le p\le d),\\
 A_p&=D\setminus\{v_{p-d},\ldots,v_{d+1}\}&& (d\le p\le2d-1),
\end{aligned}                                             \tag{2.9}
\]

with `A_d=K+za_1a_3`.

#### Proof

Consecutive omitted pairs in (2.3) share one label and exchange one label,
so the complementary owners are Johnson adjacent.  In (2.2), each filler is
used by one or two consecutive omitted pairs; the same interval property is
immediate in (2.4).  Complementing the omitted traces proves residence.

At the left end, the first transition newly omits `f_1`; all other elements
of `T_0` occur in `E_1`.  Thus shrinking `E_0=T_0` to `X_L` loses nothing in
the first dilation.  The right end is the reverse statement with `f_d`.
Every interior entry remains its maximal erosion entry.  This proves
(2.5)--(2.8), and the union of consecutive omitted pairs gives (2.9).
\(\square\)

The baseline equation (2.8) is load-bearing.  Endpoint inclusions (2.5)
alone do not imply interior reconstruction for an arbitrary owner path.

## 3. Both phases join the same rail

In the common universe `D`, the folded owners immediately adjacent to the
central owner (1.3) have missing pairs

\[
\begin{array}{c|cc}
 &\text{left exterior}&\text{right exterior}\\ \hline
-&\{a_1,f_{d+1}\}&\{a_3,f_0\}\\
+&\{a_3,f_{d+1}\}&\{a_1,f_0\}.
\end{array}                                                \tag{3.1}
\]

For (2.2), `M_0={f_2,f_(d+1)}` and
`M_d={f_(d-1),f_0}`.  The small rows (2.4) have the same compulsory
`f_(d+1)` and `f_0` at the corresponding ends.  Hence each left exterior is
adjacent to `T_0`, and each right exterior is adjacent to `T_d`.  The same
internal source/owner rail therefore works in both phases.  The two joined
paths consisting of one exterior owner, the whole rail, and the other
exterior owner remain internally depth-`d` resident; this is stronger than
the clipped rail statement alone.

Its internal lower and upper colours are

\[
 L_j=D\setminus(M_j\cup M_{j+1}),\qquad
 H_j=D\setminus(M_j\cap M_{j+1})                       \tag{3.2}
\]

for `0<=j<d`.  The `L_j` are all distinct.  The `H_j` are all distinct for
`d=2` and `d>=4`; the displayed `d=3` rail has one repeated upper value.  In
every depth the complete upper counter is identical in the two phases.

Thus owner rank, Johnson adjacency, residence, literal endpoint caps and the
upper rows are not the remaining obstruction.

## 4. Sharp lower-palette obstruction

The preceding construction is only one member of the possible common-rail
family.  The endpoint algebra classifies them all.

Let a common first owner be adjacent to both left rows in (3.1) and contain
`X_L`.  Its missing pair must be

\[
                   M_0=\{f_{d+1},x\},\qquad x\notin X_L. \tag{4.1}
\]

Similarly, a common last owner adjacent to both right rows and containing
`X_R` must have

\[
                   M_d=\{f_0,y\},\qquad y\notin X_R.     \tag{4.2}
\]

The two boundary lower colours in the minus phase are

\[
 D\setminus\{a_1,f_{d+1},x\},\qquad
 D\setminus\{a_3,f_0,y\},                               \tag{4.3}
\]

and in the plus phase they are

\[
 D\setminus\{a_3,f_{d+1},x\},\qquad
 D\setminus\{a_1,f_0,y\}.                               \tag{4.4}
\]

### Theorem 4.1 (phase-common lower palette forces an owner repeat)

The two multisets in (4.3)--(4.4) are equal if and only if

\[
                         x=f_0,qquad y=f_{d+1}.          \tag{4.5}
\]

But then `M_0=M_d={f_0,f_(d+1)}`, so `T_0=T_d`.  Therefore no simple common
rail can have a phase-common exact boundary lower palette.

#### Proof

Equality with the same active omission would require `a_1=a_3`, so the two
rows must pair crosswise.  Cancelling the common active label gives
`{f_(d+1),x}={f_0,y}`.  The endpoint exclusions in (4.1)--(4.2) leave only
(4.5).  Complementing proves the repeated-owner conclusion.  \(\square\)

For the explicit rail, the two directed lower-counter differences have size
two each.  The boundary upper colours are the phase-common values
`D\setminus{f_(d+1)}` and `D\setminus{f_0}`.  This pinpoints the exact debt:
it is a two-colour lower boundary circuit, not owner rank, residence, upper
support or common cap.

## 5. Why this is not yet zero source-length accumulation

A depth-`d` inverse of `d+1` owner rows occupies `2d+1` source positions,
including `d` left and `d` right halo positions.  Equation (2.7) proves the
correct local row, but not that those `2d` halo cells equal an existing
ambient boundary word.

If (2.7) replaces only the single central owner (1.3), it adds `d` owner and
source positions.  If it replaces an already allocated `d+1`-owner segment,
the scalar length can be neutral, but the joins must be rechecked.  In the
literal aligned segment starting at owner address `p_L`, the two possible
right exterior rows omit `{a_3,f_d}` and `{a_1,f_d}`.  A common adjacent
rank-`r` owner must either omit `f_d` or omit both `a_1,a_3`; either choice
prevents containment of `X_R`.  Hence the direct `p_L,...,p_L+d`
zero-charge replacement is impossible before any Hall calculation.

The exact remaining positive theorem would have to supply, jointly:

1. the two ambient halo identifications for (2.7);
2. a two-colour phase-dependent lower boundary circuit (or a non-common
   rail avoiding Theorem 4.1); and
3. the usual protected matching/contraction rows for every interval crossing
   the planted block.

The other five members of the seven-host menu may be used to pay item 2 or
to build the halos, but their one-sided ray identities alone prove neither.

## 6. Audit

Run

```text
python3 scratch/audit_threadD_c8_aligned_singlecut_coatom_link_20260801.py --write
```

The dependency-light replay checks `2<=d<=12`:

* the exact folded endpoints and unique cap-containing owner;
* every owner, source, residence and dilation row in Sections 2--3;
* internal and boundary lower/upper counters;
* the complete endpoint-pair exhaustion proving Theorem 4.1; and
* the direct zero-charge right-end obstruction in Section 5.

Frozen replay:

```text
scratch/audit_threadD_c8_aligned_singlecut_coatom_link_20260801.py
  SHA-256 2ebbeb5e25131831c4acc07d657adc11234af356c30fd096da63fde057295115
scratch/threadD_c8_aligned_singlecut_coatom_link_20260801.audit.json
  SHA-256 844e4cbf600a159063a060b315dacb9e50b9575e92328a436092dcc3276eeff9
  payload fd08dd345f42b5a31fa25e03ebebcdd1d2ffa6c343b74d9cf2f54a04bb134a80
```
