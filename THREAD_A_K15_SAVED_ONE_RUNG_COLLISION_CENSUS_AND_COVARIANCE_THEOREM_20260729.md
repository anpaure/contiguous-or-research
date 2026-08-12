# Saved `k=15` one-rung collision census and covariance theorem

Date: 2026-07-29

Status: exact theorem and independently audited linear-time census.  No saved
factor currently satisfies all hypotheses of the one-rung parent theorem.
The closest saved factors nevertheless have hundreds of locally safe square
corners.  Thus their obstruction is not collision cover: it is parent
topology and two-sided cyclic residence (and, for one connected comparison
factor, upper-palette completeness).

Subsequent closure: `THREAD_A_K15_TWO_PARENT_FLAG_STABILIZER_ORBIT_AND_COMMON_XI_NOGO_20260729.md`
proves that diagonal common-parent symmetries cannot change the old `Xi`, but
an independently relabelled B-parent flag-stabilizer orbit always supplies a
safe seam once eligible parent cycles exist.  Thus diagonal decorrelation is
no longer a remaining hypothesis under that minimal two-parent interface.

## 1. Domain of the audit

Let $X$ have size $n=15$, let $r=8$, and put

\[
 W=\binom{15}{8}=6435,\qquad D=4.
\]

The exact one-rung theorem applies to a single Hamilton cycle $F$ in
$J(15,8)$ satisfying all of the following:

1. the lower edge colours $Y \cap Y'$ are the $6435$ rank-seven sets,
   each exactly once;
2. the upper edge colours $Y \cup Y'$ cover all $5005$ rank-nine sets;
3. every cyclic one-run and every cyclic zero-run of every coordinate has
   length at least four.

On its duplicate-safe oriented square catalogue $\mathcal D$, write
$C_{\rm dup}=|\mathcal D|$.  The radius-two endpoint labels give the exact
identity

\[
 N_{\rm safe}=C_{\rm dup}-N_{11}-N_{12}-N_{21}+N_\times.       \tag{1.1}
\]

Here `safe` means safe at the unique new seam.  It becomes a valid one-rung
Hamilton-path splice only when the three parent conditions above also hold.

### Lemma 1.1 (component obstruction)

If the parent is a cyclic factor with $c>1$ components, no construction
that cuts one A edge and one complementary-B edge and adds one rung can be a
spanning path.

#### Proof

The A and B rails initially contain $2c$ cycles.  The two cuts open one A
cycle and one B cycle, and the rung joins precisely those two paths.  The
other $2c-2$ cycles are untouched.  Thus the result is disconnected when
$c>1$.  $\square$

## 2. Exact census of the saved factors

The script

```text
scratch/audit_laneA_k15_one_rung_collision_kernel_20260729.py
```

reconstructs every physical component, rechecks the middle partition,
Johnson adjacency, exact lower palette, upper support, and both cyclic run
families, and then visits each edge and square corner only constantly many
times.  It verifies both

\[
 C_{\rm dup}=C-2d_{\Gamma}(\mathcal U)+2e_{\Gamma}(\mathcal U) \tag{2.1}
\]

and (1.1) before emitting a report.  It never treats a locally safe corner
in a disconnected or non-biresident factor as a valid splice.

The following table contains every principal saved `q1`-exact,
upper-complete parent-factor candidate in the current `k=15` lanes.  The
columns $s_+,s_-$ count cyclic one-runs and zero-runs of length below four.

| saved factor | components | $s_+$ | $s_-$ | $C_{\rm dup}$ | $N_{11}$ | $N_{12}$ | $N_{21}$ | $N_\times$ | local $N_{\rm safe}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PBBS `seed0.engine` | 13 | 0 | 1995 | 480 | 75 | 45 | 45 | 0 | 315 |
| PBBS `seed1.engine` | 13 | 0 | 2145 | 450 | 30 | 30 | 45 | 0 | 345 |
| double-shadow strict `xi18` | 20 | 1425 | 1845 | 510 | 90 | 75 | 30 | 0 | 315 |
| double-shadow phase2 `xi28` | 11 | 1110 | 2220 | 570 | 60 | 75 | 45 | 0 | 390 |
| `seed0.dualresident.seed7` | 26 | 855 | 0 | 540 | 75 | 75 | 60 | 30 | 360 |
| all-depth `u2u3l3_s801` | 9 | 0 | 2040 | 780 | 105 | 75 | 30 | 0 | 570 |
| all-depth `from4` | 3 | 0 | 2010 | 810 | 105 | 75 | 30 | 0 | 600 |
| all-depth `from3` | 2 | 0 | 2010 | 810 | 105 | 75 | 30 | 0 | 600 |
| `q1ham_d93` | 1 | 1050 | 2070 | 540 | 60 | 45 | 45 | 0 | 390 |

Every displayed number is a literal physical count, not a quotient count.
In every row (1.1) holds.  In particular, every row has collision noncover;
the local safe fraction ranges from $315/510$ to $345/450$.  None is a
valid parent:

* the first eight rows are disconnected;
* none is cyclically biresident;
* the only connected row, `q1ham_d93`, has 1050 short one-runs and 2070
  short zero-runs.

For comparison, the connected positive-resident artifact `connected409`
has

\[
$(C_{\rm dup},N_{11},N_{12},N_{21},N_\times,N_{\rm safe})$
$=(660,45,60,45,0,510)$,
\]

but it has 2130 short zero-runs and misses 360 physical upper-q1 colours.
It is therefore outside the upper-complete parent domain as well.

The exact bi-residence CEGAR artifacts have status `UNKNOWN` and contain no
accepted factor.  The Claude/Opus workspace likewise contains no
`CARRIER_PASS_CYCLIC` parent.  Consequently the set of saved factors to
which the one-rung theorem applies is empty, and no saved one-rung
`k=15 -> 16` splice exists.  This is a census conclusion, not a universal
nonexistence theorem.

### Equivariant compression

All rows in the table are \(\mathbb Z_{15}\)-equivariant.  The action on a
rank-seven lower label is free: a label fixed by a nontrivial translation
would be a union of cycles of size three or five, whereas seven is divisible
by neither.  Hence the action on oriented square corners is free.  It follows
that

\[
C_{\rm dup},N_{11},N_{12},N_{21},N_\times,N_{\rm safe}
\quad\hbox{are all multiples of }15,                 \tag{2.2}
\]

and each of the four endpoint-label histograms is uniform over the fifteen
coordinates.  The emitted audits verify these facts.  Thus only
$C_{\rm dup}/15$, between 30 and 54 in the table, quotient representatives
are needed for this particular collision audit.  Equivariance compresses
the test; it does not force collision noncover.

## 3. Exact covariance decomposition

The next theorem gives a genuine factor-level sufficient inequality and an
average route to existence.

Let $n=2r-1$, $W=\binom nr$, and let $\mathcal D$ be the duplicate-safe
oriented catalogue of an eligible parent, of size

\[
m=C_{\rm dup}>0.
\]

For $x\in X$, put

\[
\begin{aligned}
a_i(x)&=|\{s\in{\cal D}:A_i(s)=x\}|,\\
b_j(x)&=|\{s\in{\cal D}:B_j(s)=x\}|,\\
c_{ij}(x)&=|\{s\in{\cal D}:A_i(s)=B_j(s)=x\}|,
\end{aligned}                                             \tag{3.1}
\]

where $(i,j)\in\{(1,1),(1,2),(2,1)\}$.  Null labels contribute to none
of these counts.  Define

\[
 B=\frac{\langle a_1,b_1\rangle+\langle a_1,b_2\rangle+
                 \langle a_2,b_1\rangle}{m},              \tag{3.2}
\]

and the aggregate diagonal covariance

\[
 \Xi=\sum_{(i,j)}\left(
       \sum_xc_{ij}(x)-\frac{\langle a_i,b_j\rangle}{m}
       \right).                                           \tag{3.3}
\]

### Theorem 3.1 (collision covariance theorem)

One has the exact identity

\[
 \boxed{N_{\rm safe}=m-B-\Xi+N_\times.}                  \tag{3.4}
\]

Put

\[
h=\frac{2W}{n},\qquad
A_i=\sum_xa_i(x),\quad B_j=\sum_xb_j(x),                 \tag{3.5}
\]

and

\[
T=\min(A_1,B_1)+\min(A_1,B_2)+\min(A_2,B_1).             \tag{3.6}
\]

Then

\[
 B\le \frac hmT\le3h.                                   \tag{3.7}
\]

Consequently the checkable factor-level inequality

\[
 \boxed{m+N_\times>\frac hmT+\Xi}                        \tag{3.8}
\]

forces a safe one-rung corner.  In particular, if
$\Xi\le\varepsilon m$, then

\[
 \boxed{m(1-\varepsilon)+N_\times>\frac{6W}{n}}          \tag{3.9}
\]

is sufficient.  At `k=15`,

\[
h=858,\qquad \frac{6W}{n}=2574.                          \tag{3.10}
\]

#### Proof

By definition,

\[
N_{11}+N_{12}+N_{21}=B+\Xi.
\]

Substitution in (1.1) gives (3.4).

It remains to prove (3.7).  Fix a coordinate `x`.  Exact lower q1 implies
that the number of parent edges toggling `x` is

\[
2\left(\binom{n-1}{r-1}-\binom{n-1}{r-2}\right)
=\frac{2W}{n}.                                           \tag{3.11}
\]

Equivalently, the number of nonconstant positive runs is
$W/n$.  For a fixed finite endpoint age, each such run has at most two
oriented endpoints of that age, and a fixed oriented cut endpoint occurs in
at most one square-corner row.  Therefore

\[
a_i(x),b_j(x)\le\frac{2W}{n}=h.                           \tag{3.12}
\]

For any two nonnegative vectors bounded coordinatewise by `h`,

\[
\langle a,b\rangle\le h\min\left(\sum_xa(x),\sum_xb(x)\right).
\]

Applying this to the three pairs in (3.2) gives the first inequality in
(3.7).  Since every slot mass is at most $m$, $T\le3m$, giving the
second.  Finally (3.8) follows from (3.4) and the first bound in (3.7),
while (3.9) uses $\Xi\le\varepsilon m$ and the second.  $\square$

## 4. Sharp profile form and an averaging route

Normalize $p_i=a_i/m$, $q_j=b_j/m$, let
$u_i=\sum_xp_i(x)$, $v_j=\sum_xq_j(x)$, and centre the profiles by

\[
p_i^\circ=p_i-\frac{u_i}{n}{\bf1},\qquad
q_j^\circ=q_j-\frac{v_j}{n}{\bf1}.                       \tag{4.1}
\]

Then (3.2) gives exactly

\[
\frac Bm=
\frac{u_1v_1+u_1v_2+u_2v_1}{n}
+\langle p_1^\circ,q_1^\circ+q_2^\circ\rangle
+\langle p_2^\circ,q_1^\circ\rangle.                   \tag{4.2}
\]

Thus, if $\Xi/m\le\varepsilon$, Cauchy--Schwarz and (3.4) prove the
sharper sufficient condition

\[
\frac{u_1v_1+u_1v_2+u_2v_1}{n}
+\|p_1^\circ\|_2(\|q_1^\circ\|_2+\|q_2^\circ\|_2)
+\|p_2^\circ\|_2\|q_1^\circ\|_2+\varepsilon
<1+\frac{N_\times}{m}.                                  \tag{4.3}
\]

If all four centred norms are at most `sigma`, the simpler condition

\[
\frac3n+3\sigma^2+\varepsilon
<1+\frac{N_\times}{m}                                    \tag{4.4}
\]

is sufficient.  For a translation-equivariant factor the four profiles are
exactly uniform, so the centred terms vanish.  The saved audits exhibit
positive covariance, but it is far below collision cover.  For example,
`from3` has

\[
m=810,\quad B=\frac{88245}{810},\quad
\Xi=\frac{81855}{810},\quad N_\times=0,
\]

and (3.4) gives $N_{\rm safe}=600$.

### Corollary 4.1 (legal re-pairing average)

Suppose a finite orbit of legal parent-factor switches preserves eligibility,
the size `m` of the duplicate-safe catalogue, and the four marginal profiles,
and re-pairs the A and B half-signatures one-wise uniformly, meaning

\[
\mathbb E\,c_{ij}(x)=\frac{a_i(x)b_j(x)}m
\quad\text{for every }(i,j),x.                            \tag{4.5}
\]

If $B<m$, some orbit member has a safe corner.  In particular,
$m>3h$ is a profile-free sufficient condition for such an orbit.

#### Proof

Equation (4.5) gives $\mathbb E\Xi=0$.  Averaging (3.4) gives

\[
\mathbb E N_{\rm safe}=m-B+\mathbb E N_\times\ge m-B>0.
\]

Some orbit member therefore has positive integer $N_{\rm safe}$.  The
last assertion follows from $B\le3h$.  $\square$

This is the promised average/counting route.  It is conditional on a
**legal chronology-preserving switch orbit**, not on arbitrary random
pairing.  The square graph has maximum degree two and supplies no generic
expander mixing.  Moreover, uniform marginals alone are insufficient:
one may take perfectly uniform labels with $A_1=B_1$ on every row and all
other slots null, making every row unsafe.  The minimum new structural
hypothesis is therefore diagonal decorrelation of the two half-signatures,
quantified by `Xi`, or a legal switch orbit proving it on average.

## 5. Audited boundary

The present work proves:

* the saved-candidate set contains no valid one-rung parent;
* every principal nearby saved factor has exact collision noncover, with the
  counts in Section 2;
* (3.8), (4.3), and Corollary 4.1 are rigorous sufficient existence
  theorems for a future eligible parent or legal switch orbit.

It does **not** prove that an eligible parent factor exists, that every such
factor satisfies collision noncover, or that a collision-safe one-rung child
automatically satisfies deeper shadows or `COMP_3`.

The lightweight script was independently audited line by line.  Its A/B
age-one and age-two extraction follows the unique path away from each cut;
its complement conversion on the B shore is correct; its dangerous set is
exactly $L\setminus\{v\}$; its reciprocal square and duplicate-safe
formulae are exact; and its multi-component scope is fail-closed.

Machine-readable reports are:

```text
scratch/laneA_pbbs_seed0_one_rung_collision_kernel_20260729.audit.json
scratch/laneA_pbbs_seed1_one_rung_collision_kernel_20260729.audit.json
scratch/laneA_double_shadow_strict_xi18_one_rung_collision_kernel_20260729.audit.json
scratch/laneA_double_shadow_phase2_xi28_one_rung_collision_kernel_20260729.audit.json
scratch/laneA_seed0_dualresident_seed7_one_rung_collision_kernel_20260729.audit.json
scratch/laneA_u2u3l3_s801_one_rung_collision_kernel_20260729.audit.json
scratch/laneA_from4_one_rung_collision_kernel_20260729.audit.json
scratch/laneA_from3_one_rung_collision_kernel_20260729.audit.json
scratch/laneA_q1ham_d93_one_rung_collision_kernel_20260729.audit.json
scratch/laneA_connected409_one_rung_collision_kernel_20260729.audit.json
```
