# Cross-audit of the rotor--SCD resolution report

Date: 2026-07-24

Source audited:
MATH_ATTACK_J_ROTOR_SCD_RESOLUTION_20260724.md.

## 1. Verdict

The central combinatorial claims survive, but one material correction is
required.

1. The no-averaging theorem is correct as an exact identity for the weighted
   run-count ledger that it defines. In fact its proof works for arbitrary
   nonnegative radius weights.
2. The pseudo-color orbit and residual-arc Eulerization are exact. The
   statewise permutation formulation of genuine SCD recoloring is also exact.
3. The whole-chain two-color overlay theorem is correct, with the important
   scope restriction that it does not describe trades which split or
   recombine chains.
4. The \(\mathrm{RSCD}_A\) reduction is a rigorous sufficient route to the
   contiguous-OR bound, and it is the exact asymptotic gate for the saturated
   rotor/SCD-resolution architecture.
5. Equation (1.10) does **not** give the exact hard-reset rotor-prefix
   extraction toll. For \(0\le d<m\), a run through \(t\) radius-\(d\)
   states has prefix-extraction length
   \[
   \boxed{t+2d,}
   \]
   not \(t+2d+1\). The residual block \(R\) is not a member of the symmetric
   chain and need not be written. Thus the exact hard-reset prefix toll is
   \[
   \boxed{\widehat\iota_d=2d\qquad(0\le d<m),}
   \]
   while \(\widehat\iota_m=2m-1\) at the formal terminal radius.

The off-by-one correction changes the finite exact ledger, including the
all-start identity, but does not change any \(o(W)\) threshold. If

\[
\widehat\Phi_H(\mathcal D)
=\sum_{d=0}^H2d\,p_d^*(\mathcal D)
\]

and \(\Phi_H\) is the report's functional with weights \(2d+1\), then, for
fixed positive Gaussian windows and all sufficiently large \(m\),

\[
\widehat\Phi_H(\mathcal D)
\le \Phi_H(\mathcal D)
\le \frac32\widehat\Phi_H(\mathcal D)+\frac{W}{m+1}.
\tag{1.1}
\]

Consequently

\[
\Phi_H=o(W)\quad\Longleftrightarrow\quad
\widehat\Phi_H=o(W).
\tag{1.2}
\]

Thus the stated \(\mathrm{RSCD}_A\) remains an equivalent asymptotic
formulation of the corrected prefix-extraction lemma. The report still does not
prove \(\mathrm{RSCD}_A\), MWB, or the contiguous-OR conjecture.

## 2. Exact hard-reset prefix-extraction toll

Let

\[
\omega=(L;z_1,\ldots,z_{2d};R),
\qquad |L|=|R|=m-d,
\qquad d<m.
\]

The \(2d+1\) nonempty masks of the corresponding symmetric chain are

\[
C_j=L\cup\{z_1,\ldots,z_j\},
\qquad 0\le j\le2d.
\tag{2.1}
\]

### Lemma 2.1 (correct rotor-run length)

In the last-occurrence-prefix realization, a directed rotor run through
\(t\) radius-\(d\) states has exact hard-reset length

\[
\boxed{(2d+1)+(t-1)=t+2d.}
\tag{2.2}
\]

### Proof

Initialize the first state with the entries

\[
\{z_{2d}\},\{z_{2d-1}\},\ldots,\{z_1\},L.
\tag{2.3}
\]

For each \(j\), the OR of the final \(j+1\) entries in (2.3) is \(C_j\).
Thus all masks in (2.1) occur as literal contiguous suffix ORs.

It is unnecessary to prepend \(R\). If earlier word history exists, its
older last-occurrence blocks are simply restricted to \(R\) and may be an
arbitrary ordered partition of \(R\). At the beginning of the whole word,
unseen coordinates may equivalently be assigned one virtual
last-occurrence time \(-\infty\). If the convention demands an actually
written complete initial partition, prepend one global universe sentinel
\([2m]\) once; this is a single global entry, not one entry per run. The OR
identities in (2.3) themselves require no sentinel. This is the
refined-prefix invariant needed for every later rotor step.

For a rotor successor determined by \(x\in L\), \(y\in R\), append

\[
X=L-x+y.
\tag{2.4}
\]

The new leading last-occurrence blocks are

\[
X,\{x\},\{z_1\},\ldots,\{z_{2d}\},
\tag{2.5}
\]

followed by blocks partitioning \(R-y\). Grouping only the tail for the
abstract annotation gives

\[
(L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d}),
\]

which is the required rotor successor. Each further state therefore costs
one appended entry.

For exactness within this hard-reset prefix-extraction model, the first
state exposes \(2d+1\) distinct suffix ORs ending at one chronological
endpoint, so at least \(2d+1\) entries are necessary. Each of the remaining
\(t-1\) chronological endpoints requires at least one new entry. Hence
(2.2) is both an upper and a lower bound. \(\square\)

The radius-zero case is an immediate regression test. A radius-zero chain
consists only of the middle mask \(L\), and the one-entry word

\[
[L]
\]

realizes it. Its overhead is zero, not one.

At \(d=m\), the empty mask is formal and needs no entry. The chain has
\(2m\) nonempty members, so its one-state word has length \(2m\) and toll
\(2m-1\).

The report's length \(t+2d+1\) is valid as a stronger canonical-reset
convention obtained by also writing \(R\). It is therefore a legitimate
upper bound and defines a legitimate abstract run ledger, but it is not the
exact hard-reset prefix-extraction toll. No claim is made that (2.2) is a
lower bound for arbitrary contiguous-OR words which share setup across runs
or leave the rotor-prefix architecture.

### Corollary 2.2 (correct prefix-extraction all-start identity)

With

\[
c_d=N_d-N_{d+1},\qquad N_{m+1}=0,
\]

the exact hard-reset prefix toll when every full-SCD state starts separately
is

\[
\boxed{
\sum_{d=0}^{m-1}2d\,c_d+(2m-1)c_m
=4^m-W-1.
}
\tag{2.6}
\]

Indeed,

\[
\begin{aligned}
\sum_{d=0}^{m-1}2d\,c_d+(2m-1)c_m
&=\sum_{d=0}^{m}2d(N_d-N_{d+1})-c_m\\
&=2\sum_{q=1}^{m}N_q-1\\
&=4^m-W-1.
\end{aligned}
\]

After adding the baseline \(W\) chain-state entries, the word length is
\(4^m-1\), exactly the number of nonempty Boolean masks. The report's
\(4^m-2\) identity is arithmetically correct for its different reset
weights; it is not the exact prefix-extraction-toll identity.

## 3. General no-averaging theorem

Put

\[
G=(2m)!,\qquad s=2m-1,\qquad Q_m=sG.
\]

At radius \(d\le H\le m-2\), let \(r=m-d\). The state and arc data are

\[
|\Omega_d|=\frac{G}{r!^2},
\qquad
\deg^+=\deg^-=r^2,
\tag{3.1}
\]

and every directed rotor arc has master multiplicity

\[
a_d=s\gamma_d(r-1)!^2.
\tag{3.2}
\]

A color means a label on transition-head occurrence slots. A genuine
clipped-SCD color contains exactly one occurrence of every chain state in
its prescribed clipped full SCD.

Let \(w_0,\ldots,w_H\ge0\) be arbitrary. Define

\[
\Phi_w(\mathcal D)
=\sum_{d=0}^H w_d p_d^*(\mathcal D),
\qquad
R_w=\sum_{c,d}w_d r_{c,d},
\tag{3.3}
\]

where \(r_{c,d}\) is the number of hard-started monochromatic runs of color
\(c\) at radius \(d\).

### Theorem 3.1 (weighted chronology elimination)

Optimizing jointly over genuine \(Q_m\)-color full-SCD resolutions of the
exact band master and over chronologies using every master-arc copy once,

\[
\boxed{
\min R_w
=Q_m\min_{\mathcal D\ {\rm full\ SCD}}\Phi_w(\mathcal D).
}
\tag{3.4}
\]

For a frozen chronology, the lower bound in (3.4) remains valid; the upper
bound constructs a chronology adapted to the chosen SCD.

### Proof: lower bound

Fix any feasible colored chronology and make every physical cut. For a
color \(c\) and radius \(d\), its state occurrences are the distinct
vertices of \((\mathcal D_c)_d\). Consecutive vertices in a monochromatic
run are joined by directed rotor arcs. Distinct runs are vertex-disjoint and
together span the radius class. Hence they form a spanning directed path
forest and

\[
r_{c,d}\ge p_d^*(\mathcal D_c).
\tag{3.5}
\]

A monochromatic cyclic circuit is not an exception: its mandatory physical
cut deletes one cyclic adjacency and produces one path. Therefore

\[
\begin{aligned}
R_w
&\ge\sum_c\Phi_w(\mathcal D_c)\\
&\ge Q_m\min_{\mathcal D}\Phi_w(\mathcal D).
\end{aligned}
\tag{3.6}
\]

### Proof: upper bound

Choose a full SCD \(\mathcal D\), and at each radius choose an optimal
forest \(F_d\) with \(p_d=p_d^*(\mathcal D)\) components. Index colors by

\[
(b,\sigma)\in[s]\times S_{2m}
\]

and let \((b,\sigma)\) carry \(\sigma\mathcal D\).

A state stabilizer has size \(r!^2\). Since \(\mathcal D_d\) contains
\(\gamma_d\) states, every state occurs in the colored orbit

\[
s\gamma_dr!^2
=a_dr^2
\tag{3.7}
\]

times, exactly its master head multiplicity.

A directed rotor arc has stabilizer \((r-1)!^2\). Since \(F_d\) has
\(\gamma_d-p_d\) arcs, its colored coordinate orbit uses each directed arc

\[
s(\gamma_d-p_d)(r-1)!^2
\tag{3.8}
\]

times. The residual multiplicity of every arc is therefore

\[
sp_d(r-1)!^2.
\tag{3.9}
\]

At each state the residual indegree and outdegree are both

\[
sp_d(r-1)!^2r^2=sp_dr!^2.
\tag{3.10}
\]

The colored forest orbit has exactly the same number \(sp_dr!^2\) of path
starts and path ends at every state: there are \(p_d\) base starts and
ends, and each state stabilizer has size \(r!^2\).

At each state, pair residual incoming arcs bijectively with colored paths
starting there. Color the head occurrence of the connector by the color of
the paired path, and prepend the connector to that path. This uses every
residual arc exactly once, because the total number of residual arcs equals
the total number \(Q_mp_d\) of colored paths.

Contract these connector-plus-path trails. At a macrovertex, the number of
macroedges beginning there is the residual outdegree, while the number
ending there is the number of colored path ends. Equation (3.10) makes the
macrograph balanced. Every nonempty weak component of a finite balanced
directed multigraph has an Euler circuit. Eulerize and expand.

Every master-arc copy is now used once, and every chosen colored forest path
is consecutive. The number of hard color runs is at most \(Q_mp_d\) at
radius \(d\). Hence

\[
R_w\le Q_m\sum_dw_dp_d=Q_m\Phi_w(\mathcal D).
\tag{3.11}
\]

Minimization and (3.6) prove (3.4). \(\square\)

This proof contains no fractional selection, probabilistic averaging, or
Birkhoff step. The only averaging corollary is the valid finite inequality

\[
\min_c\Phi_w(\mathcal D_c)
\le\frac1{Q_m}\sum_c\Phi_w(\mathcal D_c)
\le\frac{R_w}{Q_m}.
\tag{3.12}
\]

Taking \(w_d=2d+1\) recovers Theorem 2.1 exactly as a canonical-reset
run-count identity. Taking

\[
w_d=2d\qquad(0\le d\le H<m)
\]

gives the corrected exact hard-reset prefix-extraction identity

\[
\boxed{
\widehat R_H^*
=Q_m\min_{\mathcal D}\widehat\Phi_H(\mathcal D).
}
\tag{3.13}
\]

Hard-reset prefix words for all colors can be constructed with total length

\[
Q_mW+\widehat R_H^*.
\tag{3.14}
\]

The source's separate physical master-circuit initialization estimate
remains a harmless upper bound. With the corrected prefix initialization,
one circuit at radius \(d<m\) needs at most \(2d+1\) entries. The number of
circuits is at most \(Q_mp_d\). For \(H\ge1\), one has
\(p_0\le\gamma_0=W/(m+1)\), so

\[
I_{\rm phys}
\le Q_mp_0+\sum_{d=1}^H(2d+1)Q_mp_d
\le \frac{Q_mW}{m+1}
+  \frac32Q_m\widehat\Phi_H.
\tag{3.15}
\]

The sentinel convention discussed after (2.3) adds at most one global entry.
Thus \(\widehat\Phi_H=o(W)\) still makes physical initialization
\(o(Q_mW)\). What fails is only the claimed finite exact prefix-extraction
coefficient.

## 4. Audit of the pseudo-color orbit

This section takes as an established input the exact odd middle-wreath
factor and its distinguished-coordinate cut theorem. The cut gives

\[
B=\operatorname{Cat}_m=\frac{W}{m+1}
\]

vertex-disjoint complementary Johnson paths

\[
P=(X_0,\ldots,X_m),\qquad X_m=X_0^c,
\]

partitioning the middle layer.

For completeness, the cut conclusion follows directly from exact middle
ownership. Each odd cyclic row has \(m+1\) length-\(m\) windows avoiding the
distinguished coordinate. After cutting at that coordinate, these windows
are the \(m+1\) consecutive length-\(m\) intervals of a linear order on
\([2m]\); adjacent intervals differ by one deletion and one insertion, and
the first and last intervals are complementary. Exact odd middle ownership
makes all these avoiding windows disjoint across rows and covers every
\(m\)-subset of \([2m]\). Their number of rows is
\[
\frac1{2m+1}\binom{2m+1}{m}
=\frac{1}{m+1}\binom{2m}{m}
=\operatorname{Cat}_m.
\]

### 4.1 The cut path gives genuine rotor paths

For each step put

\[
a_t=X_t\setminus X_{t+1},
\qquad
b_t=X_{t+1}\setminus X_t.
\]

Because the path has exactly \(m\) steps and changes the overlap with
\(X_0\) from \(m\) to \(0\), every step decreases that overlap by exactly
one. Thus the \(a_t\)'s are the \(m\) distinct elements of \(X_0\), and the
\(b_t\)'s are the \(m\) distinct elements of \(X_0^c\). Therefore

\[
w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1})
\tag{4.1}
\]

is a permutation of the coordinates.

All subscripts of \(w\) below must be read modulo \(2m\). One has

\[
X_t=I_w(t,m).
\tag{4.2}
\]

For a chosen radius \(d\), define

\[
\omega_d(t)=
\left(
I_w(t+d,m-d);
w_{t+d-1},\ldots,w_{t-d};
I_w(t+m,m-d)
\right).
\tag{4.3}
\]

The first \(d\) displayed singleton coordinates, together with the left
block, recover \(X_t\), so distinct centers give distinct states. Direct
cyclic-interval arithmetic gives

\[
L_{t+1}=L_t-w_{t+d}+w_{t+m},
\tag{4.4}
\]

and shifts the displayed singleton word and right block exactly as in the
rotor rule. For \(d=0\), (4.4) is the separate ordinary swap. Hence every
constant-radius segment lying inside one cut path is a genuine directed
rotor path.

### 4.2 Exact low-toll pseudo-color

Concatenate the \(B\) cut paths and assign the radius labels in blocks of
sizes \(\gamma_0,\ldots,\gamma_H\). A block of \(\gamma_d\) consecutive
centers intersects at most

\[
\frac{\gamma_d}{m+1}+2
\]

cut paths. Its states therefore form a spanning directed path forest with

\[
p_d^0\le\frac{\gamma_d}{m+1}+2.
\tag{4.5}
\]

For the corrected extraction weights,

\[
\sum_{d=0}^H2d\,\gamma_d
=2\sum_{q=1}^HN_q.
\tag{4.6}
\]

Consequently, when

\[
H=\lceil A\sqrt m\rceil,\qquad A>0\text{ fixed},
\tag{4.7}
\]

\[
\begin{aligned}
\widehat\Phi_{\rm cut}
&:=\sum_{d=0}^H2d\,p_d^0\\
&\le
\frac{2\sum_{q=1}^HN_q}{m+1}
+2H(H+1)\\
&\le\frac{2HW}{m+1}+2H(H+1)
=o(W).
\end{aligned}
\tag{4.8}
\]

The report's old-weight estimate is also arithmetically correct and gives
the same conclusion. The fixed-\(A\) hypothesis in (4.7) should be stated
explicitly in Theorem 4.1; the displayed \(o(Q_mW)\) assertion is not proved
there for an arbitrary growing \(H\).

The constructed family has \(\gamma_d\) distinct legitimate radius-\(d\)
states for every \(d\), but it need not satisfy either shadow-injectivity
condition. Calling it a pseudo-color, rather than an SCD, is correct.

### 4.3 Orbit and Eulerization

Take \(s\) copies of the complete coordinate orbit of the pseudo-color.
There are \(Q_m=s(2m)!\) labeled pseudo-colors. A fixed state occurs

\[
s\gamma_dr!^2
\tag{4.9}
\]

times. The orbit of the selected pseudo-forest arcs uses every directed arc

\[
s(\gamma_d-p_d^0)(r-1)!^2
\tag{4.10}
\]

times, leaving \(sp_d^0(r-1)!^2\) copies per arc.

The residual connector pairing and balanced-macrograph proof of Theorem 3.1
therefore applies verbatim. It embeds all pseudo-forest paths consecutively
into an exact chronology of every master-arc occurrence. With corrected
extraction weights its toll is at most

\[
Q_m\widehat\Phi_{\rm cut}=o(Q_mW).
\tag{4.11}
\]

No SCD ownership equation is used in this Eulerization.

### 4.4 Exact statewise ownership synchronization

Fix a full SCD \(\mathcal E\), and prescribe the labeled target orbit

\[
(b,\sigma)\longmapsto\operatorname{clip}_H(\sigma\mathcal E).
\]

For a state \(\omega\), let \(P_\omega\) be its pseudo-occurrence slots and
let

\[
A_\omega=
\{(b,\sigma):
\omega\in\operatorname{clip}_H(\sigma\mathcal E)\}.
\]

Since a state stabilizer has size \(r!^2\),

\[
|A_\omega|=s\gamma_dr!^2=|P_\omega|.
\tag{4.12}
\]

Choosing a bijection

\[
\pi_\omega:P_\omega\longrightarrow A_\omega
\tag{4.13}
\]

for every state assigns each admissible target color exactly one occurrence
of that state and assigns none to an inadmissible color. Hence every target
color receives exactly the state set of its prescribed clipped full SCD.
Conversely, any recoloring into the prescribed labeled target orbit restricts
at every state to (4.13).

Thus the product of statewise bijection problems is an exact
characterization, not a fractional relaxation. What remains unproved is a
choice of these bijections preserving \(o(Q_mW)\) chronological toll.

## 5. Audit of the overlay exchange theorem

Let \(\mathcal D,\mathcal E\) be full SCDs. Their ownership overlay has the
chains of \(\mathcal D\) on the left, the chains of \(\mathcal E\) on the
right, and one edge for every Boolean mask, joining its two owner chains.

Choose chain collections \(X\subseteq\mathcal D\) and
\(Y\subseteq\mathcal E\), and form

\[
\mathcal D'=(\mathcal D\setminus X)\cup Y,
\qquad
\mathcal E'=(\mathcal E\setminus Y)\cup X.
\tag{5.1}
\]

### Theorem 5.1

Both \(\mathcal D'\) and \(\mathcal E'\) are SCDs if and only if
\(X\cup Y\) is a union of connected components of the ownership overlay.

### Proof

Let a mask \(M\) have owners \(D(M)\in\mathcal D\) and
\(E(M)\in\mathcal E\). Its multiplicity in \(\mathcal D'\) is

\[
1-\mathbf1_{\{D(M)\in X\}}
+\mathbf1_{\{E(M)\in Y\}}.
\tag{5.2}
\]

This equals one exactly when

\[
\mathbf1_{\{D(M)\in X\}}
=\mathbf1_{\{E(M)\in Y\}}.
\tag{5.3}
\]

Condition (5.3) on every overlay edge says precisely that selected
membership is constant on each connected component. Under it, every mask
occurs once in \(\mathcal D'\), and the complementary calculation gives the
same for \(\mathcal E'\). Every exchanged object is already a symmetric
chain, so exact mask coverage makes both collections SCDs. The converse is
immediate from (5.2). \(\square\)

Parallel mask edges and chains common to the two SCDs cause no problem,
provided the two side copies of a common chain remain distinct overlay
vertices.

The theorem characterizes only exchanges of whole, pre-existing chains
between two labeled colors. It does not characterize:

- a repair which cuts and recombines chains;
- a genuinely multi-color trade; or
- a trade tested only in the clipped-band overlay without preserving the
  outer portions of the full chains.

Thus connected overlays obstruct this particular exchange operation, not
all exact SCD repair mechanisms.

## 6. Corrected \(\mathrm{RSCD}_A\) reduction

For fixed \(A>0\), put \(H=\lceil A\sqrt m\rceil\). The quantifiers required
by the rotor lane are

\[
\boxed{
\forall A>0\ \exists\,(\mathcal D_{m,A})_{m\ge m_0(A)}
\quad
\frac{\widehat\Phi_H(\mathcal D_{m,A})}{W}\longrightarrow0.
}
\tag{6.1}
\]

The full SCD \(\mathcal D_{m,A}\) is chosen first. Only after that common
choice may the forests at the separate radii be optimized.

### Lemma 6.1 (old and corrected RSCD are equivalent)

For \(H\ge1\),

\[
\widehat\Phi_H(\mathcal D)
\le\Phi_H(\mathcal D)
\le\frac32\widehat\Phi_H(\mathcal D)+\frac{W}{m+1}.
\]

### Proof

The first inequality is termwise. Also,

\[
\Phi_H-\widehat\Phi_H=\sum_{d=0}^Hp_d^*.
\tag{6.2}
\]

At radius zero,

\[
p_0^*\le\gamma_0
=N_0-N_1
=\frac{W}{m+1}.
\tag{6.3}
\]

For \(d\ge1\),

\[
\sum_{d=1}^Hp_d^*
\le\frac12\sum_{d=1}^H2d\,p_d^*
=\frac12\widehat\Phi_H.
\tag{6.4}
\]

Equations (6.2)--(6.4) prove the result. \(\square\)

Therefore the report's unproved \(\mathrm{RSCD}_A\), using \(\Phi_H\), is
true if and only if the corrected extraction version (6.1) is true.

The partial-packing formulation in Proposition 6.1 is weaker than
full \(Q_m\)-color saturation as a construction format, but it is not a
weaker one-atom existence theorem. Its average immediately contains one SCD
with \(o(W)\) toll. Conversely, one such SCD and its forests fit the master
capacities with \(q_m=1\). Thus its existential content is the same corrected
\(\mathrm{RSCD}_A\) gate.

### Theorem 6.2 (conditional OR implication)

If (6.1) holds for a fixed \(A\), then there is a central-band word of length

\[
W+o(W).
\tag{6.5}
\]

### Proof

Let the optimal radius-\(d\) forest have path sizes \(t_{d,1},\ldots\).
By Lemma 2.1, direct realization of all its paths has total length

\[
\begin{aligned}
\sum_{d,j}(t_{d,j}+2d)
&=\sum_{d=0}^H\gamma_d
+  \sum_{d=0}^H2d\,p_d^*\\
&=W+\widehat\Phi_H\\
&=W+o(W).
\end{aligned}
\tag{6.6}
\]

Because all forests lie inside the radius classes of the same full SCD,
their chain states partition every mask in the central band. Independent
optimization of the forests does not lose common ownership. \(\square\)

Combining (6.5) with the separately audited outer-tail construction gives

\[
\limsup_{m\to\infty}
\frac{\nu(2m)}{\binom{2m}{m}}
\le
1+O\!\left((1+A^2)e^{-A^2}\right).
\tag{6.7}
\]

If (6.1) holds for every fixed \(A\), first take the \(m\to\infty\)
limsup for a fixed \(A\), and only then let \(A\to\infty\). This gives the
leading constant one in even dimensions. The standard trimmed one-bit lift
then gives odd dimensions.

The same conclusion can be obtained through the exact master resolution:
Theorem 3.1 with weights \(2d\) says that a saturated exact rotor/SCD
resolution has \(o(Q_mW)\) extraction toll if and only if one full integral
SCD has \(\widehat\Phi_H=o(W)\).

This equivalence is confined to the defined saturated, same-radius,
hard-reset rotor architecture. The condition is:

- sufficient, but not known necessary, for arbitrary contiguous-OR words;
- unrelated to the necessity of odd fixed-window MWB;
- not an odd exact-wreath factor or common nested-owner resolution; and
- stronger than separate depthwise SCD choices because one common full SCD
  must serve every radius.

## 7. Remaining qualifications and corrected theorem ledger

### Accepted without substantive correction

1. The master state and arc multiplicities, including the stabilizers
   \(r!^2\) and \((r-1)!^2\), are exact.
2. The no-averaging lower bound is valid for every frozen chronology.
3. The coordinate-orbit residual pairing constructs a suitable chronology;
   it does not claim to work for an arbitrarily prescribed Euler tour.
4. The pseudo-color has the exact radius histogram and distinct legitimate
   states, while correctly making no SCD claim.
5. The pseudo-occurrence-to-target-color bijections are exact integral
   ownership variables.
6. The whole-chain overlay exchange characterization is necessary and
   sufficient for that operation.
7. The mesoscopic-run argument remains valid after replacing \(2d+1\) by
   \(2d\), since on every annulus \(d\ge a\sqrt m\) the two weights are
   asymptotically identical.

### Required corrections or explicit qualifications

1. Replace (1.10) by \(t+2d\) for \(d<m\), and replace “exact extraction
   overhead \(2d+1\)” by the hard-reset prefix overhead \(2d\).
2. Recalibrate the exact prefix-extraction version of Theorem 2.1 using
   \(\widehat\Phi_H=\sum2d\,p_d^*\). The theorem with the old weights remains
   valid as an abstract canonical-reset identity.
3. Replace the extraction all-start identity (7.3a) by (2.6). Retain
   \(4^m-2\) only if it is explicitly labeled as the old reset-weight ledger.
4. State the fixed-window hypothesis \(H=\lceil A\sqrt m\rceil\), \(A\)
   fixed, in the \(o(Q_mW)\) part of Theorem 4.1.
5. State that the indices of \(w\) in (4.5)--(4.6) are modulo \(2m\).
6. Define colors formally on transition-head occurrence slots.
7. Keep the physical master-circuit initialization ledger separate. Its
   corrected estimate is (3.15), still \(o(Q_mW)\).
8. State the overlay theorem only for exchanges of whole chains in the full
   ownership overlay.
9. Preserve the quantifier order in (6.1): one common SCD is selected before
   any radiuswise forest optimization.

### Unproved statement after correction

The smallest unproved lemma in this lane remains

\[
\boxed{
\forall A>0\ \exists\,(\mathcal D_{m,A})_{m\ge m_0(A)}:
\quad
\sum_{d=0}^{\lceil A\sqrt m\rceil}
2d\,p_d^*(\mathcal D_{m,A})=o(W).
}
\tag{7.1}
\]

By Lemma 6.1 this is asymptotically equivalent to the report's
\(\mathrm{RSCD}_A\). Neither the pseudo-color orbit, the Birkhoff
factorization, nor the overlay exchange theorem proves it.

## 8. Final status

The report's structural conclusion is stable: averaging and fractional
decomposition do not bypass the need for one good integral SCD atom, and the
pseudo-orbit isolates the missing synchronization exactly.

The finite “exact run toll” is not stable as written. In the hard-reset
rotor-prefix architecture its correct value is \(2d\), not \(2d+1\), for
every nonterminal radius. Once this off-by-one is
repaired, the no-averaging theorem, pseudo-color construction, overlay
characterization, and \(\mathrm{RSCD}_A\)-to-OR implication remain rigorous,
with the same asymptotic open lemma and the same logical scope.
