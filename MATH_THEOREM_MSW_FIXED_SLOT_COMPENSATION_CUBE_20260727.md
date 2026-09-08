# MSW fixed-slot compensation cubes and the depth-one scalar gate

Date: 2026-07-27

## 1. Exact commuting cube

Fix $m\ge3$ and one residue class $s\pmod4$.  Let

\[
J_s=\{s,s+4,s+8,\ldots\}\cap[0,2m-4]
\]

be the corresponding pairwise disjoint four-bit slots in a Dyck word of
length $2m$.  At slot $t$, pair

\[
U1100V\longleftrightarrow U1010V.                 \tag{1.1}
\]

The fixed-marked-gap context theorem and the reciprocal-$C_8$ calculation
prove that (1.1) is a boundary-fixed exact two-row factor trade.  Trades at
different slots of $J_s$ act in disjoint trace slabs and commute, even when
their root pairs overlap.  Therefore every subset of $J_s$ gives an exact
middle wreath factor.  The resulting state space is an exact Boolean cube of
dimension $|J_s|$.

The complete proof is Sections 1--5 of
`MATH_AUDIT_FIXED_SLOT_POSITIVE_HEIGHT_RECIPROCAL_C8_20260726.md`.  The new
executable reconstruction is `scratch/msw_fixed_slot_trade_cube.py`; it
independently recovers every local separated-double-swap start from the full
triple-carrier functional graph and verifies exact middle ownership at every
requested cube vertex.

## 2. Exact active-row count

For a specified set of $h$ disjoint slots, deleting the displayed blocks and
recording their two orientations is a bijection with

\[
2^h C_{m-2h}                                           \tag{2.1}
\]

MSW roots active at all $h$ slots.  Hence, for $u=|J_s|$, the number of
distinct rows changed by the full shore is

\[
\boxed{
A_{m,u}=\sum_{h=1}^{u}(-1)^{h+1}\binom uh2^hC_{m-2h}.} \tag{2.2}
\]

The unmatched count is $C_m-A_{m,u}$.  Formula (2.2) is stronger than the
elementary avoidance estimate used for the first-eligible matching.  The
implementation checks (2.2) exactly against the reconstructed row incidence.

In particular, selecting the first active slot in $J_s$ gives a row-disjoint
matching on exactly $A_{m,u}$ rows, while selecting the full shore changes
the same rows and applies all their commuting local moves.

## 3. Local depth-one change

Write one inverse-triple pair in the common local coordinates

\[
P=(a,b,X,c,d,Y),\qquad Q=(b,d,X,a,c,Y),
\]

where $|X|=m-2$ and $|Y|=m-1$.  The two separated double swaps give

\[
P'=(b,a,X,d,c,Y),\qquad Q'=(d,b,X,c,a,Y).
\]

Put $Y^-=Y\setminus\{\text{last}(Y)\}$ and
$Y^+=Y\setminus\{\text{first}(Y)\}$.  Direct cyclic-window cancellation
gives the complete depth-one signed change

\[
\boxed{
\delta_1=
 \mathbf1_{\{a\}\cup Y^-}+\mathbf1_{\{d\}\cup Y^+}
-\mathbf1_{\{d\}\cup Y^-}-\mathbf1_{\{a\}\cup Y^+}.} \tag{3.1}
\]

Thus every rectangle has local quadratic noise $2$.  For one complete fixed
slot there are $C_{m-2}$ rectangles.  The finite reconstruction through
$m=10$ additionally finds that all four targets in (3.1), over all contexts,
are globally distinct, so the full-layer noise is exactly $2C_{m-2}$.  A
general proof of this last global injectivity is still to be written; it is
not silently included in (3.1).

Let $\mu_1$ be the canonical MSW depth-one load and define the coherent
correlation

\[
\Gamma_{m,t}:=-\langle\mu_1,\delta_{m,t}\rangle.       \tag{3.2}
\]

Then the exact depth-one CPCR change of the fixed slot $t$ is

\[
\Delta\mathrm{CPCR}_1=-\Gamma_{m,t}+2C_{m-2}.          \tag{3.3}
\]

This reduces the all-$m$ sign question to one scalar common-interval count.

## 4. The first interior slot identity

Put $r=m-2$ and let $z\in D_r$.  Let $b(z)$ be the coordinate flipped by
the first application of the MSW map $h$ after $g$, and define

\[
B(z)=\mathbf1\{b(z)=1\},\qquad
E(z)=\mathbf1\{z_2=z_3=1\}.                           \tag{4.1}
\]

The exact finite audit through $4\le m\le10$ has no exception to the local
correlation identity

\[
\boxed{g(z)=2B(z)+E(z),}                              \tag{4.2}
\]

where $g$ is the per-rectangle coherent gain minus its noise $2$.

The counting consequences of (4.2) are already rigorous.  Write the first
primitive component of $z$ as $1u0$, followed by $v$.  The MSW map
$g$ flips the closing down-step of that first component.  In the resulting
path, $h$ chooses coordinate $1$ exactly when $u$ is a nonempty primitive
Dyck path.  Catalan convolution therefore gives

\[
|B|=\sum_{j=1}^{r-1}C_{j-1}C_{r-j-1}=C_{r-1}.        \tag{4.3}
\]

The ballot/reflection count for Dyck paths whose third and fourth steps are
both up is

\[
|E|=C_r-2C_{r-1}.                                    \tag{4.4}
\]

On $B$, write $u=1p0$.  The event $E$ says that $p$ starts with two up-steps.
Summing over $p$ and the suffix $v$ gives

\[
|B\cap E|
=\sum_{k=1}^{r-2}(C_k-C_{k-1})C_{r-2-k}
=C_{r-1}-2C_{r-2}.                                   \tag{4.5}
\]

Consequently (4.2) implies the four-class histogram

\[
\begin{array}{c|c}
g&\#\text{ paired contexts}\\ \hline
0&2(C_{m-3}-C_{m-4})\\
1&C_{m-2}-3C_{m-3}+2C_{m-4}\\
2&2C_{m-4}\\
3&C_{m-3}-2C_{m-4}.
\end{array}                                             \tag{4.6}
\]

Its weighted sum is $C_{m-2}$.  Together with noise $2C_{m-2}$, it gives

\[
\boxed{\Gamma_{m,2}=3C_{m-2}},\qquad
\Delta\mathrm{CPCR}_1=-C_{m-2}.                       \tag{4.7}
\]

The rootwise refinement (4.2) was originally the missing part of this
deduction.  Lemmas 4.3--4.4 below bypass that refinement and prove the
aggregate conclusion (4.7) directly from the exact \(\Gamma\)-inverse
criterion.  Thus (4.7), unlike the stronger root-by-root histogram (4.6), is
now an all-\(m\) theorem.

There is also an explicit finite-verified injection blueprint for (4.2).
For either target pair, first cancel canonical roots which cover both the
lost and gained target.  For the first pair, every remaining gained-target
root has prefix `101101` or `111101` and maps injectively to a lost-target
root by swapping Dyck coordinates $4$ and $5$, replacing the valley `01` by
the peak `10`.  For the second pair, the remaining roots have prefix
`11010` or `11101`; the corresponding injection uses $(1,2)$ in the first
case and $(3,4)$ in the second.  These become `10110` and `11110`.
All indices and displayed words are zero-based/left-to-right in the Dyck
encoding.  The unmatched positive
roots have respective cardinalities

\[
1+B(z)+E(z),\qquad 1+B(z),                            \tag{4.8}
\]

which is exactly (4.2).  This injection has zero exceptions through $m=10$.
The swaps visibly preserve the Dyck condition: the first and third raise a
valley, while `11010 -> 10110` lowers a peak from height one and remains
nonnegative.  Injectivity and separation of the three prefix classes are
also immediate.  Section 4.1 proves their common-interval transport.
Completeness of the listed root prefixes is unnecessary for Theorem 4.5,
which instead counts the natural aligned endpoint-two family.

The independent verifier is `scratch/audit_msw_slot2_catalan_histogram.py`;
its report is `scratch/msw_slot2_catalan_histogram_m4_m10_report.json`.

### 4.1 Label-free interval transport

The common-interval part of the injection has now been separated from the
MSW dynamics.  Let \(q=(q_0,\ldots,q_{n-1})\) be the MSW flip permutation,
including the sentinel.  The recovered cyclic order satisfies

\[
 R_j=q_{-1-2j\pmod n},
\]

so a depth-one interval starting at (a) uses the q-index set

\[
 P(a)=\{-1-2(a+t)\pmod n:0\le t\le m-2\}.           \tag{4.9}
\]

For the first injection class, the observed flip-word coupling has an odd
left endpoint (s), an even right endpoint (e), and

\[
 q'_{[s,e]}=(q_{e-1},q_s,q_e,q_{s+1},\ldots,q_{e-2}). \tag{4.10}
\]

Writing (a=n-(s-1)/2), direct modular arithmetic gives

\[
 q'[P(a-1)]=q[P(a)\setminus\{e\}\cup\{e-1\}].       \tag{4.11}
\]

For `11010 -> 10110`,

\[
 q'_{[0,5]}=(q_3,q_5,q_0,q_1,q_2,q_4),
\]

and

\[
 q'[P(0)]=q[P(n-1)\setminus\{1\}\cup\{2\}].        \tag{4.12}
\]

For `11101 -> 11110`, with even (s) and odd (e),

\[
 q'_{[s,e]}=(q_{s+2},\ldots,q_{e-1},q_s,q_e,q_{s+1}). \tag{4.13}
\]

Whenever (P(a)\cap[s,e]=\{s,s+2,\ldots,e-1\}),

\[
 q'[P(a)]=q[P(a)\setminus\{s\}\cup\{e\}].          \tag{4.14}
\]

Equations (4.11)--(4.14) are formal identities for every odd (n=2m+1);
they do not depend on the labels in (q).  The executable symbolic checker
`scratch/msw_slot2_symbolic_compensation.py` exhausts every parity-compatible
block and occurrence start, not merely those seen in finite MSW factors.

The flip-word couplings themselves now follow from the exact MSW recursion

\[
 \rho(1u0v)=(d,d-\rho(\mu u),1,d+\rho(v)),\qquad d=|u|+2. \tag{4.15}
\]

At the root, the leaf Tamari rotation

\[
 X=10\,1B0C\longmapsto Y=110B0C
\]

has, writing (D=|B|+4),

\[
\begin{aligned}
 \rho(X)&=(2,1,D,D-\rho(\mu B),3,D+\rho(C)),\\
 \rho(Y)&=(D,D-\rho(\mu B),2,3,1,D+\rho(C)).          \tag{4.16}
\end{aligned}
\]

Thus its changed block is sent by

\[
 (x_0,\ldots,x_{\ell-1})\mapsto
 (x_2,\ldots,x_{\ell-2},x_0,x_{\ell-1},x_1).       \tag{4.17}
\]

In a right-tree context, (4.15) merely shifts the block by an even number
of flip positions.  In a left-tree context, the identity

\[
 \rho(\mu w)=|w|+1-\operatorname{rev}\rho(w)
\]

reverses the block, converting (4.17) to

\[
 (x_{\ell-2},x_0,x_{\ell-1},x_1,\ldots,x_{\ell-3}). \tag{4.18}
\]

Induction on the binary-tree address proves: use (4.17) after an even
number of left edges and (4.18) after an odd number.  The addresses of the
three forward prefix rotations are respectively `RL`, `LLL`, and `LL`;
hence `101101` and `111101` give (4.10), while `111011` gives (4.13).
For `110100 -> 101100`, concatenation and the fixed calculations

\[
 \rho(110100)=(6,4,5,2,3,1),\qquad
 \rho(101100)=(2,1,6,4,5,3)                           \tag{4.19}
\]

give (4.12) directly.  This is an all-(m) derivation because any remaining
Dyck suffix concatenates unchanged.  The executable
`verify_leaf_rotation_context_theorem` checks every leaf rotation through a
requested finite semilength as a regression of the proof.

Consequently the remaining gap is no longer a flip-word claim.  It is the
inverse-fibre completeness/alignment statement: after cancelling roots
covering both targets, the negative roots are exactly

\[
 \{101101\ldots,111101\ldots\}\quad\text{and}\quad
 \{110100\ldots,111011\ldots\},                       \tag{4.20}
\]

and their target occurrences have the starts and one-label replacements in
(4.11)--(4.14).  Once (4.20) is proved, the Catalan decrement
(-C_{m-2}) follows without another asymptotic estimate.  The strengthened
finite audit has zero exceptions through (m=10) and records the four full
six-bit prefix histograms explicitly.

### 4.2 A stronger bypass: the marked-Γ insertion identity

The prefix-completeness statement can in fact be bypassed.  Put \(r=m-2\)
and let \(z\in D_r\).  In the zero-based flip word \(\rho(z)\), let

\[
 k(z)=\left\lfloor {\rho(z)^{-1}(1)\over2}\right\rfloor.
\]

Starting from the (k(z))-th Chung--Feller state (x_k), define the two
consecutive endpoint-two paths

\[
 y_0=g(x_k),\qquad y_1=g(h(y_0)).                     \tag{4.21}
\]

For an endpoint-two path (y), let

\[
 A(y)=y_{<2}\,1011\,y_{\ge2},\qquad
 B(y)=y_{<2}\,1101\,y_{\ge2}.                        \tag{4.22}
\]

These are endpoint-four paths of semilength (r+2=m).  Direct use of the
MSW flip recursion and the local rectangle (3.1) gives the exact upper-target
normal form

\[
 (T_{L,1},T_{G,1},T_{L,2},T_{G,2})
   =(A(y_1),B(y_1),B(y_0),A(y_0)).                    \tag{4.23}
\]

Here upper targets are complements of the lower targets; every lower target
contains the sentinel.  Consequently its canonical load is exactly the
intrinsic fibre size

\[
 c(T)=|\Gamma^{-1}(T)|.                               \tag{4.24}
\]

The exact inverse criterion for \(\Gamma\), already proved in
`MATH_THEOREM_MSW_Q1_INVERSE_AND_SQRT_BOUND_20260725.md`, now closes the
scalar calculation completely.

### Lemma 4.3 (the aligned endpoint-two family)

Let \(\mathcal Y_r\) be the endpoint-two paths of length \(2r\) which begin
with `11` and have either one or two up-steps starting at height one.  Then
the map \(z\mapsto y_0\) in (4.21) is a bijection

\[
                         D_r\longrightarrow\mathcal Y_r.              \tag{4.25}
\]

Indeed, the second physical coordinate is either the `g`-pivot entering
\(y_0\), or the `h`-pivot leaving it.  In the first case the preceding
balanced path begins `10`; this is its first touching down-step, so
\(D_0=0\), the path is `10c` with \(c\) Dyck, and \(y_0=11c\) has exactly
one \(U_1\).  In the second case position two is the second touching up-step
and `h` selects it, so \(U_1(y_0)=2\).  Conversely, if \(U_1=1\), then
\(h'=g^{-1}\) selects the second touching up-step, position two; if
\(U_1=2\), then `h` itself selects position two.  Thus these and only these
endpoint-two paths are aligned.  The MSW construction uses every
endpoint-two path once, so the correspondence is bijective.

The family has the following disjoint normal forms, with \(a,b,c\) Dyck and
\(\bar b\) the bitwise complement:

\[
\begin{array}{c|c|c}
\text{type}&y&U_1(y)\\ \hline
\mathrm I&11c&1,\\
\mathrm {II}&11a0\bar b1c&2.
\end{array}                                             \tag{4.26}
\]

The decomposition in type II cuts at the first descent from height two and
the unique subsequent up-step from height one.  Consequently, with
\(\mathcal C(x)=1+x\mathcal C(x)^2\),

\[
 |\mathcal Y_r|=C_{r-1}+[x^{r-2}]\mathcal C^3=C_r.       \tag{4.27}
\]

Define \(R(y)=1\) in type II exactly when \(b\) is empty, and zero otherwise.
Define \(E(y)=1\) exactly when positions three and four of \(y\) are both
up-steps.  Then

\[
 \sum_{y\in\mathcal Y_r}R(y)=[x^{r-2}]\mathcal C^2=C_{r-1}.             \tag{4.28}
\]

If \(\mathcal A=\mathcal C-1-x\mathcal C=x^2\mathcal C^3\) is the
generating function for nonempty Dyck paths beginning `11`, the two types in
(4.26) give

\[
 \sum_{r\ge2}\!\left(\sum_{y\in\mathcal Y_r}E(y)\right)x^r
 =x\mathcal A+x^2\mathcal A\mathcal C^2
 =x\mathcal A\mathcal C=x^3\mathcal C^4.              \tag{4.29}
\]

Hence, for every \(r\ge2\),

\[
 \sum_{y\in\mathcal Y_r}E(y)=C_r-2C_{r-1}.             \tag{4.30}
\]

### Lemma 4.4 (marked-\(\Gamma\) collar)

For \(y\in\mathcal Y_r\), put \(y'=g(h(y))\).  Then

\[
\boxed{
\begin{aligned}
 c(A(y))-c(B(y))&=-1-R(y),\\
 c(A(y'))-c(B(y'))&=1+R(y)+E(y).
\end{aligned}}                                         \tag{4.31}
\]

#### Proof

Let \(c_p(T)\) count the inverse pairs in Lemma 3.1 of the inverse note whose
first pivot is the one-based position \(p\).  The two inserted words differ
only by the swap `1011`/`1101` at positions three through six.

For \(y\), both inserted paths have identical heights after position six,
and the local swap occurs at heights three and four.  It therefore changes no
prefix \(U_0\)-count.  Every inverse pair with \(p\ge7\) is identical on the
two sides.

In type I, write \(c=1u0v\).  Then

\[
 y'=011u1v.                                             \tag{4.32}
\]

This path never goes below height \(-1\), so neither insertion has a first
pivot outside the collar.  In type II, if \(a\) is empty then

\[
 y'=101\bar b1c,                                       \tag{4.33}
\]

whereas for \(a=1u0v\),

\[
 y'=101u1v0\bar b1c.                                   \tag{4.34}
\]

Any possible outside first pivot lies in \(\bar b\).  After it there is at
most the final up-step from height one, while the `1101` collar already has
two \(U_0\)-steps before it (and `1011` has three).  The equality of the
prefix \(U_0\) and suffix \(U_3\) counts in the exact inverse criterion is
therefore impossible.  Thus \(y'\) also has no outside first pivot.

It remains only to substitute the six displayed collar steps into the four
conditions of the exact inverse criterion.  Each `1` below denotes one
unique admissible second pivot; \(\eta=1\) only in the indicated \(E=0\)
subcases:

\[
\begin{array}{c|c|c}
\text{case}&c_p(A(y))-c_p(B(y))
            &c_p(A(y'))-c_p(B(y'))\\ \hline
\mathrm I,\ E=0&-\mathbf e_1
 &\mathbf e_3+\mathbf e_5-\mathbf e_6\\
\mathrm I,\ E=1&-\mathbf e_1
 &\mathbf e_3+\mathbf e_5\\
\mathrm {II},\ a=\varnothing&-\mathbf e_2-R\mathbf e_1
 &\mathbf e_3+R\mathbf e_1\\
\mathrm {II},\ a=1u0v,\ u=\varnothing
 &-\mathbf e_2-R\mathbf e_1
 &\mathbf e_3+R\mathbf e_1+\mathbf e_5-\mathbf e_6\\
\mathrm {II},\ a=1u0v,\ u\ne\varnothing
 &-\mathbf e_2-R\mathbf e_1
 &\mathbf e_3+R\mathbf e_1+\mathbf e_5.
\end{array}                                             \tag{4.35}
\]

For example, in type II the unique suffix \(U_3\)-step is preceded by a
forbidden \(D_3\)-step exactly when \(b\ne\varnothing\), which is the
\(R\mathbf e_1\) entry.  In (4.32)--(4.34), the number of suffix \(U_3\)
steps before the low bridge is one larger exactly when \(u\ne\varnothing\),
giving the \(E\mathbf e_5\) entry; when \(u=\varnothing\), the admissible
positions five and six form the cancelling pair
\(\mathbf e_5-\mathbf e_6\).  The other entries are the fixed collar pivots
at positions one, two, and three.  This proves the table directly, and
summing its coordinates gives (4.31).  \(\square\)

### Theorem 4.5 (slot-two Catalan decrement)

By (4.23), the coherent gain of the rectangle indexed by \(y\), minus its
quadratic noise two, is

\[
 \big(c(A(y'))-c(B(y'))\big)
 -\big(c(A(y))-c(B(y))\big)-2
 =2R(y)+E(y).                                          \tag{4.36}
\]

Equations (4.28) and (4.30) now give

\[
 \sum_{y\in\mathcal Y_r}(2R(y)+E(y))
 =2C_{r-1}+C_r-2C_{r-1}=C_r.                          \tag{4.37}
\]

Since there are \(C_r\) rectangles and each has noise two,

\[
 \boxed{\Gamma_{m,2}=3C_{m-2},\qquad
        \Delta\mathrm{CPCR}_1=-C_{m-2}.}              \tag{4.38}
\]

This is an all-\(m\) theorem.  `verify_marked_gamma_collar_theorem` is an
independent regression: it enumerates \(\mathcal Y_r\) directly, checks that
it equals the aligned MSW image, and verifies (4.31) from the exact inverse
criterion.  Through \(r=10\), all \(23,712\) paths pass with zero failures.
The literal factor audit separately has zero mismatches to the target normal
form (4.23) through \(m=10\).

## 5. Parity core and finite all-depth evidence

Define

\[
J_m^{\rm core}=
\begin{cases}
\{2,6,10,\ldots,2m-6\},&m\text{ even},\\
\{4,8,12,\ldots,2m-6\},&m\text{ odd}.
\end{cases}                                             \tag{5.1}
\]

For odd $m$, the reflected choice $\{2,6,\ldots,2m-8\}$ has the same
audited score.  Exhaustive search of all four fixed-slot cubes gives (5.1)
as an MWB-optimal vertex for $4\le m\le9$; the predicted offset-two cube is
also optimal internally at $m=10$.

More strongly, applying every layer in (5.1) decreases the unweighted CPCR
pair count at **each nonconstant depth** in every audited case:

\[
\begin{array}{c|l}
m&\Delta(\mathrm{CPCR}_{1},\mathrm{CPCR}_{2},\ldots)\\ \hline
4&(-2,-4)\\
5&(-5,-12,-34)\\
6&(-25,-58,-202,-688)\\
7&(-82,-225,-628,-1732,-6898)\\
8&(-372,-1018,-3007,-7903,-25994,-110492)\\
9&(-1272,-3837,-10156,-27551,-77910,-253657,-1236380)\\
10&(-5515,-16260,-45157,-119662,-342010,-1026080,
     -3821656,-19094884).
\end{array}                                             \tag{5.2}
\]

This is finite evidence, not an asymptotic theorem.  It identifies a precise
candidate factor transformation rather than an optimizer with unspecified
choices.

The exhaustive driver is `scratch/search_msw_fixed_slot_cube.py`; the
single-slot and Boolean-Moebius audit is
`scratch/audit_msw_fixed_slot_cube_compensation.py`.

For larger (m), the driver also has a `--selection-policy theory` mode.
It retains the empty/full shores, all prefixes, suffixes and singletons, and
a configurable Hamming neighborhood of the parity core.  This is only a
pruning rule: every retained state is reconstructed as a literal exact
factor and scored independently by MWB, CPCR, holes and PCap.  The general
carrier descent likewise accepts `--initial-fixed-slot-core` and now
supports `--descent-objective mwb`, so subsequent local moves are selected
using the actual weighted MWB currency rather than quadratic CPCR alone.

## 6. Exact remaining compatibility problem

All marked gaps split into four fixed-slot phases.  One phase repairs only a
quarter of the canonical marked-gap supply.  Adjacent phases cannot simply be
superposed: the local roots

\[
110010S\longleftrightarrow101010S\longleftrightarrow101100S
\]

give the known non-geodesic overlapping-slab obstruction.  Therefore the
remaining deterministic question is not the existence of many local trades;
it is a compatible four-phase compiler which routes these overlap conflicts
while preserving exact middle ownership.

Two concrete subgoals now suffice for the present lane:

1. extend the proved depth-one marked-Γ collar theorem to the all-depth
   parity core;
2. replace the forbidden adjacent-phase commutator by a bounded exact carrier
   gadget, or prove a positive-density compatible selection across the four
   phases.

Neither remaining subgoal is currently proved.  The main constant-one theorem
therefore remains open, but the depth-one slot-two decrement is no longer one
of its conditional inputs.
