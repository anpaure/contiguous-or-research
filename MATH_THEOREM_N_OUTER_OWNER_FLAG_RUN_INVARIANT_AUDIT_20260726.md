# Adversarial audit of the outer owner-flag run invariant

Date: 2026-07-26

Audited source:
MATH_THEOREM_N_OUTER_OWNER_FLAG_RUN_INVARIANT_20260726.md.

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The central results of the audited report are valid.

1. The geodesic first-swap criterion and the semigroup condition
   \(R_j=R_1^j\) are exact.
2. The \(H\)-memory circulation is equivalent to an \(H\)-safe owner
   permutation, and the Hoffman--Farkas sign in its fractional dual is
   correct.
3. The common run formulas
   \[
   B_{m-j}\mu_j^-=\frac W2\mathbf1-jR,\qquad
   B_{m+j}\mu_j^+=\frac W2\mathbf1+jR
   \]
   and \(\sum_vR_v=W\) are exact.
4. The high-quota affine line, residual arithmetic cut, the
   \(m=3,H=2\) counterexample, and the odd-prime full-depth obstruction
   rederive correctly.
5. The trace-contained central-band criterion has exactly its stated
   central-band scope; it does not assert a full SCD extension.
6. The \(sH(H+1)\) aggregate surgery toll is correct when \(s\) is the
   number of changed outgoing transitions and the modified object is again
   a permutation.

Two scope clarifications are essential.

- The vector \(R\) is common to all depths of one fixed integral successor.
  It is not invariant under every legal successor switch.
- \(R\) determines all **point margins**, not the complete target
  histograms. Run-neutral exact trades can change individual target rows.

The strongest universal trade barrier is the following rank-one
all-depth law. If two \(H\)-safe exact factors on the same owner support
have run vectors \(R,R'\), then for every \(j\le H\),

\[
 B_{m-j}(\mu_j^{-\prime}-\mu_j^-)
 =-j(R'-R),\qquad
 B_{m+j}(\mu_j^{+\prime}-\mu_j^+)
 = j(R'-R).                                      \tag{0.1}
\]

Thus every realizable point-margin correction is linear in \(j\), uses
one common integer vector, and has opposite signs below and above. A
proposed correlated-row absorber whose point effects do not satisfy
(0.1) cannot be an exact whole-owner switch, regardless of its one-depth
Hall slack.

There is nevertheless a legal escape from **full shadow** rigidity. The
certified 24-owner pair-frame associator replaces one six-square factor by
another on the identical owner support. Its run vector is unchanged, but
it exchanges eight selective lower targets and eight selective upper
targets at depth one, and it also changes its correlated depth-two target
families. It is therefore an exact run-neutral shadow-moving atom. What
remains unproved is a packing/suspension theorem giving enough such atoms
with cap-safe multidepth signatures inside one spanning owner successor.

For an actually shadow-locked target, a single terminal seam is not enough:
one must simultaneously free an enclosing shadow target. The legal
escape architecture is consequently an alternating common-support trade
followed by a relative collar switch, not a global relabeling.

## 1. Re-audit of the main source theorems

### 1.1 Geodesicity and semigroup consistency

For a Johnson transition \(X_i\to X_{i+1}\), let \(a_i\) be its deleted
coordinate and \(b_i\) its inserted coordinate. A length-\(j\) path from
\(X_0\) is geodesic exactly when the \(a_i\) are distinct members of
\(X_0\) and the \(b_i\) are distinct members of \(X_0^c\). Reusing a
coordinate spends two transitions without increasing the endpoint
distance; conversely, distinct first swaps produce endpoint distance
\(j\). Therefore

\[
 \bigcap_{i=0}^jX_i=X_0-\{a_0,\ldots,a_{j-1}\},
\]

and

\[
 \bigcup_{i=0}^jX_i=X_0+\{b_0,\ldots,b_{j-1}\}.
\]

For prescribed nested flags, their induced middle endpoint maps must be
the powers of the first map. Conversely, if \(R_1\) is a permutation and
\(R_j=R_1^j\), consecutive nested endpoints differ by the displayed
single deletion and insertion. Hence the source's Theorem 2.1 is exact.
Independent lower and upper flags or independently bijective \(R_j\)'s
are not a legal escape from chronology.

### 1.2 Memory circulation

The root equation makes the integral \(z_\gamma\)'s binary and selects
one outgoing \(H\)-path from each root. For an \((H-1)\)-memory state,
the selected outdegree is at most one because its first owner fixes its
root. Memory conservation makes indegree equal outdegree, so the selected
memory edges are vertex-disjoint directed cycles.

If two roots tried to have the same successor owner, their selected
suffix memories would both have to equal the unique selected prefix
memory at that successor. That memory state has indegree one, a
contradiction. Thus the first-step map is a permutation and its selected
\(H\)-windows are exactly the \(z_\gamma=1\) paths. This verifies
Theorem 3.1.

For the fractional dual, write a quota throughput as \(c_j+t\),
\(0\le t\le1\). After multiplying the equations by
\(\alpha,\phi,y\), the coefficient of \(z_\gamma\) is the left side of
(3.10), while the box contribution is \(-ty\ge-\max(0,y)\). This gives
the sign in (3.11). Conversely, separation of the nonnegative
\(z\)-orthant times the \(t\)-box gives the same inequalities. Theorem
3.2 is correct.

Coordinate conjugates of one safe wreath cycle give root and memory
conservation. Transitivity on each target rank and total target mass \(W\)
give uniform fractional load \(W/N_j\). Thus Theorem 3.3 really excludes
a fractional Hall obstruction to this exact relaxation.

### 1.3 Run counts and quota arithmetic

For one coordinate \(v\), every nonconstant cyclic binary membership word
has equally many \(0\to1\) and \(1\to0\) transitions. \(H\)-safety makes
every zero-run and one-run have length at least \(H\). A one-run of length
\(\ell\) contributes \(\ell-j\) all-one windows of \(j+1\) consecutive
states. Hence

\[
 \sum_{S\ni v}\mu_j^-(S)=\frac W2-jR_v.
\]

The zero-run calculation gives

\[
 \sum_{T\ni v}\mu_j^+(T)=\frac W2+jR_v.
\]

Every owner transition deletes exactly one coordinate, so
\(\sum_vR_v=W\), with no factor two. The baseline/high-quota decomposition
then gives (0.10)--(0.11) and all congruences in Section 5.

The residual bound (5.11) follows by taking one coordinate with
\(R_v\le\lfloor W/(2m)\rfloor\), one with
\(R_w\ge\lceil W/(2m)\rceil\), and imposing
\(0\le h_{j,v}^-\le\rho_j\). Its two displayed constants are correct.

At \(m=3,j=2\), every singleton load is \(10-2R_v\), hence even; balance
would force all six loads to be four, contradicting total mass twenty.
At \(j=m-1\), all singleton loads have one common residue modulo \(m-1\);
two consecutive quotas cannot both occur, so all loads are equal and
\(2m\mid W\). For odd prime \(m=p\),
\(\binom{2p}{p}\equiv2\pmod p\). Both counterexamples are valid with the
stated scopes.

### 1.4 Promotion and surgery

The laminar variables in Theorem 7.1 select one centered saturated chain
per owner up to a variable radius. Their target equations cover every set
of the central band exactly once. Conversely, every trace-contained
central-band chain partition defines those variables. At one depth, the
owner edges must form a perfect matching, but independently selected
depthwise matchings need not obey laminarity. The source makes no improper
full-SCD inference.

If \(s\) outgoing transitions are changed, a depth-\(j\) window changes
only when one of its \(j\) transitions is among those \(s\). Thus at most
\(js\) old lower targets and \(js\) old upper targets can be lost.
Summing \(2js\) for \(1\le j\le H\) gives

\[
 2s\sum_{j=1}^Hj=sH(H+1).
\]

This proves (8.2). It is only a loss bound: a proposed rewiring must still
be checked to be a Johnson permutation and to have return-free
\(2H\)-collars at every new seam.

## 2. Exact local difference theorem

The source states the global formula. The following local form is the
useful absorber invariant.

Let \(\Omega\subseteq\binom{[2m]}m\). Let \(F\) be a factor of \(\Omega\)
into directed cycles such that every cyclic window through depth \(H\) is
geodesic. Put

\[
 n_v(\Omega)=|\{X\in\Omega:v\in X\}|,
\]

and let \(r_v(F)\) be the number of transitions of \(F\) which delete
\(v\). Let \(\mu_{j,F}^\pm\) be its signed occurrence histograms.
For a vector \(z\) on \(k\)-sets, write

\[
 (B_kz)_v=\sum_{S\ni v}z(S).
\]

### Theorem 2.1 (common-support trade law)

For every \(j\le H\),

\[
 B_{m-j}\mu_{j,F}^-=n(\Omega)-jr(F),               \tag{2.1}
\]

\[
 B_{m+j}\mu_{j,F}^+=n(\Omega)+jr(F).               \tag{2.2}
\]

Moreover,

\[
 \sum_vr_v(F)=|\Omega|,                            \tag{2.3}
\]

and

\[
 Hr_v(F)\le
 \min\{n_v(\Omega),\,|\Omega|-n_v(\Omega)\}.        \tag{2.4}
\]

#### Proof

Apply the cyclic run proof separately to every cycle in \(F\). The total
number of one-states is \(n_v(\Omega)\), and each one-run loses exactly
\(j\) admissible starts. This gives (2.1). Zero-runs give (2.2).
Every transition has one deleted coordinate, proving (2.3). There are
\(r_v(F)\) one-runs and \(r_v(F)\) zero-runs, each of length at least
\(H\), proving (2.4). \(\square\)

### Corollary 2.2 (rank-one all-depth barrier)

Let \(F,F'\) be two \(H\)-safe cycle factors on the identical owner support
\(\Omega\). Put

\[
 \Delta r=r(F')-r(F),\qquad
 \Delta\mu_j^\pm=\mu_{j,F'}^\pm-\mu_{j,F}^\pm.
\]

Then

\[
 B_{m-j}\Delta\mu_j^-=-j\Delta r,\qquad
 B_{m+j}\Delta\mu_j^+=j\Delta r.                  \tag{2.5}
\]

In particular,

\[
 \frac1jB_{m-j}\Delta\mu_j^-
 =\frac1kB_{m-k}\Delta\mu_k^-                     \tag{2.6}
\]

for all \(j,k\le H\), and

\[
 B_{m+j}\Delta\mu_j^+
 =-B_{m-j}\Delta\mu_j^-.                           \tag{2.7}
\]

Therefore a proposed exact correlated-row trade with prescribed
histogram changes \(g_j^\pm\) is impossible unless one integer vector
\(\Delta r\), of coordinate sum zero, satisfies

\[
 B_{m-j}g_j^-=-j\Delta r,\qquad
 B_{m+j}g_j^+=j\Delta r                           \tag{2.8}
\]

at every protected depth.

This is stronger than checking total mass, separate depthwise Hall
conditions, or separate lower/upper point balance. It is the strongest
universal conclusion available from the run vector alone.

### Corollary 2.3 (run-neutral kernel)

If \(r(F')=r(F)\), then all signed point margins agree at all depths:

\[
 B_{m-j}\Delta\mu_j^-=B_{m+j}\Delta\mu_j^+=0.      \tag{2.9}
\]

Equation (2.9) does **not** imply \(\Delta\mu_j^\pm=0\). It says only that
the shadow change lies in the appropriate point-incidence kernels.

For the full middle layer, (2.4) also gives

\[
 0\le R_v\le\frac{W}{2H}.                          \tag{2.10}
\]

Thus even a point-compatible correction can fail because the required new
integer run vector lies outside the run-length polytope.

## 3. Which operations preserve what

The following distinctions are exact.

### 3.1 Operations preserving \(P\), \(R\), and every shadow

Changing the written starting point of a cycle, reordering the list of
cycles, or changing auxiliary SCD labels without changing successor edges
does not change \(P\). Everything is preserved.

### 3.2 Independent reversal of whole owner cycles

One may reverse any subfamily of the directed cycles of \(P\). The result
is again a Johnson permutation and is \(H\)-safe. On each reversed cycle,
the number of deletions of \(v\) becomes the old number of additions of
\(v\), which equals the same cyclic run count. Hence \(R\) is unchanged.

Every cyclic interval of states appears once in the opposite orientation,
so its intersection and union are unchanged as sets. Therefore

\[
 \mu_{j,P'}^-=\mu_{j,P}^-,\qquad
 \mu_{j,P'}^+=\mu_{j,P}^+                         \tag{3.1}
\]

for all \(j\). Cycle reversal cannot unlock a target or repair a labelled
shadow deficit.

### 3.3 Coordinate conjugation

For \(\sigma\in\operatorname{Sym}([2m])\), put

\[
 P^\sigma=\sigma P\sigma^{-1}.
\]

Then

\[
 R_v(P^\sigma)=R_{\sigma^{-1}v}(P),                \tag{3.2}
\]

and

\[
 \mu_{j,P^\sigma}^\pm(S)
 =\mu_{j,P}^\pm(\sigma^{-1}S).                     \tag{3.3}
\]

Thus coordinate conjugation preserves the unlabelled run multiset and
relabels the shadows. It preserves the labelled run vector only when
\(R\) is \(\sigma\)-invariant. If both an absorber collar and its preload
are conjugated, every collision and every shadow-lock condition is merely
relabeled; no relative absorption has occurred.

### 3.4 Complementation

Conjugating by \(X\mapsto[2m]\setminus X\) preserves every cyclic run
count and exchanges the signed shadows:

\[
 L_j(CX)=C\,U_j(X),\qquad
 U_j(CX)=C\,L_j(X).                                \tag{3.4}
\]

It transports a lower lock to the complementary upper lock. It does not
destroy the lock.

### 3.5 Common-support factor replacement

Replacing an \(H\)-safe cycle factor \(F\) on \(\Omega\) by another such
factor \(F'\) on exactly the same \(\Omega\) is an exact legal owner
operation: the complement of \(\Omega\) is untouched, and every owner is
still used once.

- If \(r(F')=r(F)\), the operation is run-neutral and preserves every
  point margin, but it may change full shadow histograms in the kernels
  (2.9).
- If \(r(F')\ne r(F)\), it changes the labelled run vector. Its point
  effect is forced to be (2.5); it cannot prescribe different depth
  profiles independently.

This is the correct framework for an exact packet absorber.

### 3.6 Verified seam rewiring

Suppose \(P'\) differs from \(P\) at a set \(E\) of \(s\) owner tails and
is independently verified to be an \(H\)-safe Johnson permutation. If
\(d_X,d'_X\) are the old and new deleted coordinates at \(X\), then

\[
 R_v(P')-R_v(P)
 =|\{X\in E:d'_X=v\}|-|\{X\in E:d_X=v\}|.          \tag{3.5}
\]

Hence

\[
 \sum_v\Delta R_v=0,\qquad
 \|\Delta R\|_1\le2s.                              \tag{3.6}
\]

At depth \(j\), at most \(js\) occurrence rows of each sign can change.
Such a surgery can change both \(R\) and actual shadow locks, but only
through its verified seam collars. Merely drawing a Johnson cross-edge is
not enough: permutation closure and all \(2H\)-local return-free tests are
part of legality.

### 3.7 Operations which are not integral escapes

The following do not define a new exact owner successor by themselves:

1. choosing a different matching or flow independently at every depth;
2. balancing lower and upper flags separately;
3. averaging coordinate conjugates fractionally;
4. applying a global relabeling to both preload and absorber;
5. selecting associator shores independently on overlapping owner
   supports;
6. cutting cycles to open paths without recording boundary or leave terms.

The first two violate semigroup consistency, the third has only a
fractional run vector, the fourth preserves every collision, the fifth
violates exact ownership, and the sixth leaves the hypotheses of the
cyclic run theorem. Open paths and owner leaves are legitimate approximate
architectures only when their boundary and leave tolls are entered
explicitly.

## 4. Shadow-lock is a second, nonlinear obstruction

Let \(D_{q+1}^-\) be the lower targets already at cap at depth \(q+1\).
For a demanded lower target \(T\) at depth \(q\), put

\[
 \partial T=\{T-x:x\in T\}.
\]

If a return-free occurrence of \(T\) is the terminal \(q\)-subwindow of
an enclosing \((q+1)\)-window, the enclosing lower target is \(T-x\) for
some \(x\in T\). In a completed cycle every \(q\)-window has such a
one-step backward enclosure. Therefore

\[
 \partial T\subseteq D_{q+1}^-
 \quad\Longrightarrow\quad
 \text{no new cap-safe occurrence of \(T\) can be inserted}              \tag{4.1}
\]

unless the same operation also removes an occurrence from at least one
member of \(\partial T\).

For an upper target \(U\), the corresponding condition is

\[
 \nabla U=\{U+x:x\notin U\}\subseteq D_{q+1}^+.     \tag{4.2}
\]

This lock has four important properties.

1. It is not detected by \(|D_{q+1}^\pm|\) or by point margins.
2. Simultaneously conjugating \(T,D\), and the collar preserves it.
3. Whole-cycle reversal preserves it because it preserves every shadow
   histogram.
4. Changing \(R\) alone does not defeat it. The actual cap family
   \(D_{q+1}^\pm\) must move, or a cap/leave error must be paid.

Thus the common run vector and shadow-lock are independent necessary
structures: the former is a linear all-depth point constraint, while the
latter is a fibrewise nonlinear cap constraint.

## 5. Two exact legal escape atoms

### 5.1 Relative conjugate component switch

Let \(\Omega\) be invariant under a coordinate permutation \(\sigma\), and
let \(F\) be an \(H\)-safe cycle factor on \(\Omega\). Then
\(\sigma F\) is another \(H\)-safe cycle factor on the identical support,
so

\[
                         F\longleftrightarrow\sigma F           \tag{5.1}
\]

is an exact common-support switch. Its signature is

\[
 r_v(\sigma F)=r_{\sigma^{-1}v}(F),\qquad
 \mu_{j,\sigma F}^\pm(S)=\mu_{j,F}^\pm(\sigma^{-1}S).           \tag{5.2}
\]

For a transposition \(\sigma=(ab)\),

\[
\begin{aligned}
 \Delta r_a&=r_b(F)-r_a(F),\\
 \Delta r_b&=r_a(F)-r_b(F),\\
 \Delta r_v&=0\qquad(v\ne a,b).
\end{aligned}                                      \tag{5.3}
\]

This is a legal run-transfer atom. Its point-shadow action is automatically
\((-j\Delta r,+j\Delta r)\), so it changes the run vector without violating
the common-depth law. When \(r_a(F)=r_b(F)\), it is run-neutral; if the
shadow histogram is not \((ab)\)-invariant, it still changes labelled
target rows.

For absorption, the word **relative** is decisive. A global conjugation of
the entire owner system also moves the preload and changes no collision.
A useful atom requires a proper common owner support \(\Omega\), or a
certified collar shore, while the exterior preload remains fixed.

### 5.2 The certified 24-owner run-neutral shadow switch

There is a concrete nontrivial instance of (2.9). Let

\[
 A=\{a,b,c,d\},\qquad R=\{u,v,w,x\},
\]

\[
 \mathcal Y=\{uw,ux,vw,vx\},\qquad
 \Omega=\binom A2\times\mathcal Y.
\]

For

\[
 M_0=\{ab,cd\},\quad M_1=\{ac,bd\},\quad M_2=\{ad,bc\},
\]

let \(F_i\) be the certified six-square factor on the same 24 owners using
shore matching \(M_i\).

At depth one its lower and upper supports are

\[
 \operatorname{supp}\mu_{1,F_i}^-=C^-\dot\cup R_i^-,
\]

\[
 \operatorname{supp}\mu_{1,F_i}^+=C^+\dot\cup R_i^+,
\]

where \(|C^\pm|=16\), \(|R_i^\pm|=8\), and the three selective families
are pairwise disjoint.

For \(z\in A\), the lower point degree is

\[
 4\quad\text{from }C^-,
 \qquad4\quad\text{from }R_i^-,
\]

and hence eight, independently of \(i\). For \(z\in R\), it is

\[
 8\quad\text{from }C^-,
 \qquad2\quad\text{from }R_i^-,
\]

and hence ten. Since every coordinate lies in 12 of the 24 owners,
Theorem 2.1 gives the common local run vector

\[
 r_z(F_i)=
 \begin{cases}
 4,&z\in A,\\
 2,&z\in R.
 \end{cases}                                      \tag{5.4}
\]

Thus

\[
                         F_i\longleftrightarrow F_j             \tag{5.5}
\]

is an exact run-neutral switch, yet it replaces
\(R_i^-\) by \(R_j^-\) and \(R_i^+\) by \(R_j^+\).

Its correlated depth-two occurrence signature is also explicit. Every
four-cycle contributes four depth-two starts with one common trace, so

\[
 \mu_{2,F_j}^--\mu_{2,F_i}^-
 =4(\mathbf1_{M_j}-\mathbf1_{M_i}),               \tag{5.6}
\]

and, after adjoining the full reservoir \(R\),

\[
 \mu_{2,F_j}^+-\mu_{2,F_i}^+
 =4(\mathbf1_{\{Z\cup R:Z\in M_j\}}
    -\mathbf1_{\{Z\cup R:Z\in M_i\}}).             \tag{5.7}
\]

On the lower sign the common four-target family is
\(\mathcal Y\); on the upper sign it is
\(\{A\cup Y:Y\in\mathcal Y\}\). Each common family cancels in the
corresponding difference. Equations (5.6)--(5.7) have zero point
incidence, as required by (2.9).

This atom proves that the common run vector is not a full shadow-lock.
It supplies exactly the kind of correlated multirow column an absorber LP
must use.

There are two limitations.

1. A single switch moves depth-one and depth-two rows together; they cannot
   be selected independently.
2. The coefficient four in (5.6)--(5.7) can violate a cap-two preload.
   A cap-safe absorber must alternate several atoms so that a saturated
   depth-two row is freed before another occurrence is inserted.

The existing long-cycle suspension proves a legal common-support
associator seed, but not a dense packing with the required complete
multidepth cap signature. That packing theorem remains open.

## 6. Strongest barrier and the exact escape architecture

Let a proposed terminal absorber have signed histogram effect
\(g_j^\pm\).

### Necessary linear layer

It must first pass the run test:

\[
 B_{m-j}g_j^-=-j\Delta r,\qquad
 B_{m+j}g_j^+=j\Delta r
\]

for one feasible integer \(\Delta r\) with coordinate sum zero and with
both old and new run vectors satisfying the run-length bounds. Failure of
this test is an unconditional no-go for any exact \(H\)-safe whole-owner
switch.

### Necessary fibre layer

For every demanded target \(T\) or \(U\), the final trade must expose at
least one unsaturated enclosing shadow. If an entire \(\partial T\) or
\(\nabla U\) remains at cap throughout, terminal motion cannot insert the
target.

### Legal two-stage escape

An exact correlated-row absorber may therefore operate as follows.

1. Use a common-support run-neutral kernel switch, such as a packed
   pair-frame associator atom, to remove one occurrence from a saturated
   enclosing target \(S\in\partial T\) (or \(S\in\nabla U\)), while moving
   the displaced occurrence to a cap-safe row. Its total point effect is
   zero.
2. Use a **relative** return-free collar shore, with the preload fixed, to
   insert the demanded target through the newly free enclosing row.
3. Close the entire collection of switches as one exact owner factor.
   The aggregate effect must satisfy the rank-one law (2.5), even though
   its internal kernel atoms have zero point effect.

Every step is a legal operation once its two shores have the same owner
support and its seam collars pass the Johnson and \(H\)-safety tests.
What is not yet proved is the abundance theorem: one needs a
bounded-overlap family of such atoms and relative collars which routes
every correlated deficit without exceeding any target cap.

This identifies the exact constructive boundary. The source's run
invariant rules out independently tuned depth corrections, but it does not
rule out a correlated-row absorber built from run-neutral shadow switches
plus a coherent run-transfer/relative-seam layer.

An independent proof audit rederived (2.1)--(2.5), checked every operation
in Section 3, and enumerated all depth-one and depth-two targets of the
24-owner switch. It found no error in the decisive trade law or escape
atom.
