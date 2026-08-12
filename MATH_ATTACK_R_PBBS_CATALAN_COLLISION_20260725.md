# Lane R: PBBS clean-switch supply, short returns, and Catalan collision energy

Date: 2026-07-25

## Verdict

The requested all-dimensional exact factor with Catalan collision excess at
every Gaussian depth is **not** constructed here.  Two formerly open PBBS
gates are, however, settled by exact hand proofs.

1. **Clean-switch supply is positive at the Catalan scale.**  Every PBBS
   first-angle core of load one supports an explicit clean directed (C_4)
   in its residual digraph, hence an alternating (C_8) in the odd graph.
   There are at least

   \[
   \frac{m-2}{m+2}W
   \]

   distinct such (C_8)'s.  At least

   \[
   \frac{(m-2)(2m+1)}{128m(m+2)}\operatorname{Cat}_m
   =\left(\frac1{64}-o(1)\right)\operatorname{Cat}_m
   \]

   are pairwise vertex-disjoint and can be toggled simultaneously as an
   integral spanning (2)-factor.

2. **The first higher PBBS rank defect is Catalan.**  The exact short-return
   formula below shows that wrong-rank depth-two PBBS windows are precisely
   gap-three returns in the omitted-label word.  PBBS first-angle
   multiplicity then gives

   \[
   E_2(P_m)=b_2(P_m)\le \frac{2W}{m+2}<4\operatorname{Cat}_m.
   \]

The decisive unresolved gate is now centered topology and multidepth
collision cancellation, not raw clean-cycle supply.  The guaranteed clean
(C_8)'s have a nonzero three-vertex residual-path vector.  They therefore
cannot be promoted, one by one, to balanced splits merely from cleanliness.
At depths (q\ge3), the exact short-return charge, correct-target coverage,
and added-color pair congestion are also unproved in the Gaussian window.

All statements below are integral.  The PBBS object is kept explicitly
separate from an exact wreath factor.  No fractional factor, signed selector,
or independently chosen rankwise factor is used as if it were a literal
factor.

## 1. Notation and the exact constant-one target

Put

\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
B=\frac Wn=\operatorname{Cat}_m,
\]

and

\[
N_q=\binom{n}{m-q},\qquad
d_q=\left\lfloor\frac W{N_q}\right\rfloor.
\]

For an exact wreath factor (F), let (mu_q^F(S)) be its depth-(q)
cyclic-shadow load.  Use the half-normalized collision excess

\[
Q_q(F)
=\frac12\sum_{S\in\binom{[n]}{m-q}}
 (\mu_q^F(S)-d_q)(\mu_q^F(S)-d_q-1).
\tag{1.1}
\]

This is the excess number of unordered colliding occurrence pairs above the
floor/ceiling minimum.  It is nonnegative for every integral load vector of
total (W).

### Theorem 1.1 — Catalan-per-row exact-factor criterion

Assume that for every fixed positive integer (A) there is a constant
(C_A<\infty) such that, for all sufficiently large (m), one **single
exact factor** (F_{m,A}) satisfies

\[
\max_{1\le q\le \lceil A\sqrt m\rceil}Q_q(F_{m,A})
\le C_A B.
\tag{1.2}
\]

Then

\[
\nu(k)\le (1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{1.3}
\]

#### Proof

For (H_A=\lceil A\sqrt m\rceil), (d_q\ge1) gives

\[
\sum_{q\le H_A}\frac{Q_q(F_{m,A})}{d_q}
\le C_AH_AB
=O_A\!\left(\frac W{\sqrt m}\right)
=o(W).
\tag{1.4}
\]

The dependence of (C_A) on (A) is harmless.  Choose increasing integers
(M_j) so large that for every (m\ge M_j): the factor asserted for
(A=j) exists,

\[
\frac{C_j\lceil j\sqrt m\rceil}{2m+1}\le\frac1j,
\qquad m\ge j^4,
\tag{1.5}
\]

and all fixed-(j) asymptotic estimates used by the literal transfer hold.
Put

\[
j(m)=\max\{j:M_j\le m\},\qquad
H_m=\lceil j(m)\sqrt m\rceil.
\]

Then

\[
j(m)\longrightarrow\infty,\qquad
\frac{H_m}{\sqrt m}\longrightarrow\infty,\qquad
H_m=o(m),
\]

and (1.4) is (o(W)) along this diagonal.  The proved integral
contiguous-OR transfer is

\[
\nu(2m+1)\le
W+\frac{2H_m+1}{2m+1}W
+2\sum_{q\le H_m}\frac{Q_q(F_{m,j(m)})}{d_q}
+2L_m(m-H_m-1).
\tag{1.6}
\]

The seam term is (o(W)), the collision term is (o(W)), and the audited
outer SCD-product tail is (o(W)) because
(H_m/\sqrt m\to\infty) and (H_m=o(m)).  Thus (1.3) holds in odd
dimensions.  The proved trimmed one-coordinate parity lift gives the even
dimensions.  Every use of (1.6) is inside the same exact factor.  ∎

The quantifiers in Theorem 1.1 matter.  One factor must handle the whole
fixed Gaussian window.  Separate factors for separate depths do not
diagonalize.  One fixed (A) does not kill the outer tail.  On the other
hand, the constants (C_A) may grow arbitrarily quickly because the slow
diagonal absorbs them.

More generally, a bound (Q_q=O_A(Bq^\alpha)) with any fixed
(\alpha<1) also sums to (o(W)) on (q\le A\sqrt m).  The raw scale
(Q_q=O(qB)) is critical: its unweighted sum through (A\sqrt m) is only
(O_A(W)), not (o(W)).

## 2. The exact PBBS first-row theorem

Let (P_m) be the canonical parenthesis/PBBS spanning (2)-factor of
(O_m=KG(2m+1,m)).  For a middle vertex (X), let its two factor
neighbors be (Y_P(X),Z_P(X)), and define its first angle

\[
\chi_P(X)=Y_P(X)\cap Z_P(X)\in\binom{[n]}{m-1}.
\]

For a core (K\in\binom{[n]}{m-1}), write

\[
\mu_P(K)=\#\{X:\chi_P(X)=K\},\qquad
a_j=\#\{K:\mu_P(K)=j\}.
\]

The proved PBBS complete-angle theorem states

\[
1\le\mu_P(K)\le3
\tag{2.1}
\]

for every \(K\).  This fact is also reproved internally by Lemma 3.1:
split every common \(U_+(K)\cap U_-(K)\) mark into consecutive symbols
\(C,A\).  The resulting circular word has exactly three \(A\)'s and three
\(C\)'s; its cyclic \(A\to C\) transitions are exactly the digons of
\(D_K\), hence exactly the angle occurrences of \(K\).  A nonconstant
circular binary word with three symbols of each type has between one and
three such transitions.  Thus no external coverage or multiplicity
assumption is hidden in (2.1).

Since

\[
N_1=\binom{n}{m-1}=\frac m{m+2}W,
\]

conservation gives

\[
a_1+a_2+a_3=N_1,
\qquad
a_1+2a_2+3a_3=W,
\]

and hence

\[
a_2+2a_3=r:=W-N_1=\frac{2W}{m+2}.
\tag{2.2}
\]

For (m\ge3), (d_1=1).  Substitution in (1.1) yields

\[
\boxed{
Q_1(P_m)=a_3\le\frac{W}{m+2}<2B.}
\tag{2.3}
\]

This is a statement about the angle histogram of the genuine PBBS
(2)-factor.  It is not yet an exact-wreath-factor statement because a PBBS
component may have length \(\ell n\), \(\ell>1\).

### Proposition 2.1 — sharp first-row congestion gate

Let (G) be any spanning (2)-factor, put

\[
t=|E(P_m)\setminus E(G)|,
\qquad
\delta=\mu_1^G-\mu_1^{P_m}.
\]

Then

\[
\|\delta\|_1\le4t
\tag{2.4}
\]

and

\[
Q_1(G)=Q_1(P_m)
+\left\langle\delta,\mu_1^{P_m}-\frac32\mathbf1\right\rangle
+\frac12\|\delta\|_2^2.
\tag{2.5}
\]

Consequently

\[
\left|Q_1(G)-\frac12\|\delta\|_2^2\right|
\le2B+6t.
\tag{2.6}
\]

In particular, if (t=O(B)), then

\[
\boxed{
Q_1(G)=O(B)
\quad\Longleftrightarrow\quad
\|\mu_1^G-\mu_1^{P_m}\|_2^2=O(B).}
\tag{2.7}
\]

#### Proof

An angle can change only at an endpoint of a removed PBBS edge.  At most
(2t) angle occurrences change, and changing one occurrence changes its
histogram by (L^1)-distance two.  This proves (2.4).  Expanding the
quadratic (1.1) at (d_1=1) gives (2.5).  By (2.1), the absolute value of
every coordinate of (mu_1^{P_m}-3\mathbf1/2) is at most (3/2).
Equations (2.3)--(2.5) give (2.6), and (2.7) follows.  ∎

There is also a useful one-sided form.  Suppose (h) old angle occurrences
are deleted and the added-angle multiset has multiplicities (c_S).  Removing
one occurrence from a load in ({1,2,3}) increases (Q_1) by at most one.
Adding (c) occurrences to a remaining load at most three increases it by
at most (2c+\binom c2).  Therefore

\[
Q_1(G)\le Q_1(P_m)+3h+\sum_S\binom{c_S}{2}.
\tag{2.8}
\]

Thus Catalan edge distance plus Catalan added-angle pair congestion preserves
Catalan collision energy.  Centered component balance alone does not imply
the last congestion bound.

## 3. A positive-density clean PBBS (C_8) theorem

This section settles the raw clean-cycle supply question.

Fix (K\in\binom{[n]}{m-1}) and put (T=[n]\setminus K).  For
(u\in T), define

\[
\alpha_K(u)=r_+(K\cup\{u\}),\qquad
\beta_K(u)=r_-(K\cup\{u\}),
\tag{3.1}
\]

where (r_+) and (r_-) are the forward and reverse PBBS omitted labels.
The residual digraph (D_K) has the two arcs

\[
u\longrightarrow\alpha_K(u),\qquad
u\longrightarrow\beta_K(u).
\]

Let (U_+(K)) and (U_-(K)) be the three forward and reverse unmatched
zeros of the deficit-three word of (K).

### Lemma 3.1 — exact cyclic predecessor/successor law

For every (u\in T),

\[
\boxed{
\alpha_K(u)=\operatorname{prev}^{\rm strict}_{U_+(K)}(u),
\qquad
\beta_K(u)=\operatorname{next}^{\rm strict}_{U_-(K)}(u).}
\tag{3.2}
\]

#### Proof

Cut the cyclic word at its forward unmatched zeros and write

\[
0_{a_0}D_0\,0_{a_1}D_1\,0_{a_2}D_2,
\tag{3.3}
\]

where the (D_i) are Dyck words.  If the flipped zero (u) lies inside
(D_i), the two excess opens created by the flip consume the next two old
unmatched zeros and leave (a_i), the strict preceding unmatched zero.  If
(u=a_i), the new open consumes (a_{i+1}) and leaves (a_{i-1}), again
the strict predecessor.  This proves the forward identity.  Reverse the
cyclic order to obtain the second identity.  ∎

A digon (u\leftrightarrow v) in (D_K) is exactly a PBBS angle occurrence
of (K): the middle vertex (T\setminus\{u,v}) has factor neighbors
(K\cup\{u}) and (K\cup\{v}).  Lemma 3.1 says that digons are precisely
cyclic (U_+\to U_-) adjacencies.

### Theorem 3.2 — every load-one core has a clean (C_4)

If (mu_P(K)=1), then (D_K) contains a clean simple directed (C_4).

#### Proof

Put (A=U_+(K)) and (C=U_-(K)).  Compress the ground circle to the marks
in (A\cup C).  At a shared mark, replace the mark by two consecutive
symbols (C,A).  This preserves the number of cyclic (A\to C)
adjacencies, hence the number of digons.  The expanded circular word has
three (A)'s and three (C)'s.  Having exactly one (A\to C) transition
means that it has one (A)-run and one (C)-run.

If (A\cap C=\varnothing), the cyclic type is therefore

\[
a_0,a_1,a_2,c_0,c_1,c_2.
\]

Lemma 3.1 gives the directed cycle

\[
a_2\longrightarrow a_1\longrightarrow c_0
\longrightarrow c_1\longrightarrow a_2,
\tag{3.4}
\]

using respectively \(\alpha,\beta,\beta,\alpha\).  The four reverse arcs are
absent: the corresponding out-neighborhoods show that
\(a_1\not\to a_2\), \(c_0\not\to a_1\),
\(c_1\not\to c_0\), and \(a_2\not\to c_1\).

If \(A\cap C=\{x\}\), the forced \(C,A\) pair at \(x\) contracts the unique
one-run type to

\[
x,a_1,a_2,c_1,c_2.
\]

Now

\[
a_2\longrightarrow a_1\longrightarrow c_1
\longrightarrow c_2\longrightarrow a_2
\tag{3.5}
\]

is a directed \(C_4\), again of type
\(\alpha,\beta,\beta,\alpha\), and the same predecessor/successor check
excludes every reverse arc.  Two or more shared marks would give at least
two forced (C,A) boundaries, so cannot occur when there is only one
digon.  Thus (3.4) or (3.5) always supplies a clean \(C_4\).  ∎

By the clean-(C_4)/alternating-(C_8) dictionary, each cycle in Theorem
3.2 is a genuine PBBS-alternating (C_8), and its core (K) is unique.

### Corollary 3.3 — Catalan-density vertex-disjoint supply

Assume \(m\ge3\).

There are at least

\[
\boxed{
a_1\ge \frac{m-2}{m+2}W}
\tag{3.6}
\]

distinct clean PBBS-alternating (C_8)'s.  There is a pairwise
vertex-disjoint subfamily of size at least

\[
\boxed{
\left\lceil\frac{a_1}{128m}\right\rceil
\ge
\frac{(m-2)(2m+1)}{128m(m+2)}B
=\left(\frac1{64}-o(1)\right)B.}
\tag{3.7}
\]

#### Proof

From (2.2),

\[
a_1=N_1-a_2-a_3=N_1-r+a_3
\ge N_1-r=\frac{m-2}{m+2}W,
\]

which proves (3.6).  Core uniqueness prevents duplication across (K).
The audited PBBS overlap bound says that each middle vertex lies in at most
(16m) alternating-(C_8) candidates.  Selecting one eight-vertex cycle
therefore eliminates at most (8\cdot16m=128m) candidates.  Greedy
selection proves (3.7).  Vertex-disjoint alternating cycles may be toggled
simultaneously; their symmetric difference with (P_m) is an integral
spanning (2)-factor.  ∎

Corollary 3.3 proves clean supply only.  It does not say that the toggled
factor remains componentwise point-regular.

## 4. The exact centered obstruction inside the supplied cycles

The unique digon in either cyclic type in Theorem 3.2 joins the opposite
active vertices of the displayed clean (C_4).  Let these vertices be
(u,v).  The corresponding two cut endpoints (K\cup\{u}) and
(K\cup\{v}) remain joined in the PBBS factor, after the four cut edges
are deleted, through the three-vertex path

\[
P=(K\cup\{u},\ T\setminus\{u,v},\ K\cup\{v}).
\tag{4.1}
\]

Its incidence vector is

\[
\iota(P)=\mathbf1+\mathbf1_K.
\]

For the integral centered vector

\[
\zeta(P)=n\iota(P)-m|P|\mathbf1,
\]

one obtains

\[
\boxed{
\zeta(P)=n\mathbf1_K-(m-1)\mathbf1\ne0.}
\tag{4.2}
\]

Thus the explicit local supply carries a compulsory noncentered residual
path.  The balanced-switch theorem still permits a merge, a reordering, or
a cancellation with another path vector.  It does **not** permit one to
declare the switch a balanced split from cleanliness alone.

There is a useful topology dichotomy.  If the other two cut edges lie on two
distinct PBBS components, both different from the component containing
(4.1), then the old cut shape is (211).  Following the four new seams
shows that the new cut shape is (4).  The switch is then an automatically
balanced three-to-one pure merge.  Otherwise, the same clean (C_8)
certifies an additional nonlocal collision among its four cut edges on the
PBBS orbit structure.  Neither side of this dichotomy gives a balanced
positive-density splitting theorem by itself.

The obstruction is algebraically cancellable only at a nonlocal scale.
PBBS is equivariant under cyclic coordinate rotation \(\rho\).  A load-one
core \(K\) has full orbit of size \(n\): if its orbit had size \(d<n\), then
the stabilizer size \(n/d\) would divide

\[
\gcd(n,m-1)=\gcd(2m+1,m-1)\in\{1,3\}.
\]

The only nontrivial possibility is a stabilizer of order three.  It acts
freely on unordered digons, forcing \(\mu_P(K)\equiv0\pmod3\), contrary to
\(\mu_P(K)=1\).  Hence

\[
\sum_{j=0}^{n-1}\mathbf1_{\rho^jK}=(m-1)\mathbf1
\]

and therefore

\[
\boxed{
\sum_{j=0}^{n-1}
\left(n\mathbf1_{\rho^jK}-(m-1)\mathbf1\right)=0.}
\tag{4.3}
\]

Equation (4.3) gives \(a_1/n=\Theta(B)\) integral zero-sum orbits of short
path vectors.  It is not yet a factor trade: the \(n\) rotated \(C_8\)'s
need not be vertex-disjoint, and their residual paths need not be sewn into
the same new components.  Global vector cancellation cannot replace the
componentwise centered equations.

## 5. Exact short-return identity at every depth

Let

\[
C=(A_0,A_1,\ldots,A_{L-1})
\]

be a simple componentwise point-regular cycle in \(O_m\), oriented
cyclically.  Let \(\lambda_i\) be the omitted label of the edge
\(A_iA_{i+1}\).  Point regularity implies \(L=\ell n\) and every label
occurs exactly \(\ell\) times in the cyclic word \((\lambda_i)\).

For \(1\le q\le m\), define the parity-window intersection

\[
I_q(i)=\bigcap_{h=0}^{q}A_{i+2h}.
\tag{5.1}
\]

### Theorem 5.1 — gap formula

There is a nonnegative integer (eta_{i,q}) such that

\[
\boxed{|I_q(i)|=m-q+\eta_{i,q}.}
\tag{5.2}
\]

If (mathcal G_C(x)) is the multiset of cyclic gaps between consecutive
occurrences of label (x), then every (g\in\mathcal G_C(x)) is odd and at
least three, and

\[
\boxed{
\sum_i\eta_{i,q}
=\sum_{x\in[n]}\sum_{g\in\mathcal G_C(x)}
\left(q-\frac{g-1}{2}\right)_+.}
\tag{5.3}
\]

#### Proof

Since

\[
A_{i+1}=A_i^c\setminus\{\lambda_i\},
\]

one has the exact step-two recurrence

\[
\boxed{
A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.}
\tag{5.4}
\]

Consecutive labels cannot be equal, because that would give
(A_{i+2}=A_i).  Along (5.1), the transition numbered (h) inserts
(lambda_{i+2h}) and deletes (lambda_{i+2h+1}).  Each deletion reduces
the running intersection by one unless the deleted label was inserted
earlier in the same block; an inserted label was absent from an earlier
sampled vertex and hence never belonged to the full intersection.  Thus
(eta_{i,q}) is exactly the number of inserted labels whose next
same-label occurrence is a later deletion in the same (2q)-edge block.
This proves (5.2).

After an edge labelled (x), coordinate (x) is absent at two consecutive
vertices.  Until the next (x)-labelled edge, its incidence toggles at each
step.  The next occurrence is therefore at an odd gap; simplicity excludes
gap one.

Fix consecutive occurrences at positions (p,p+g).  They contribute to
(eta_{i,q}) exactly for starts (i=p-2h) satisfying

\[
0\le h\le q-1,\qquad 2h+g\le2q-1.
\]

The number of such starts is

\[
\left(q-\frac{g-1}{2}\right)_+.
\]

Summing over all ordered consecutive cyclic gaps proves (5.3).  ∎

Summing (5.2) over every component of a componentwise point-regular
(2)-factor (P), put

\[
E_q(P)=\sum_i\eta_{i,q},\qquad
b_q(P)=\#\{i:\eta_{i,q}>0\}.
\tag{5.5}
\]

### Theorem 5.2 — sharp sparse-rebundling obstruction

Let (G) be an exact wreath factor and

\[
t=|E(P)\setminus E(G)|.
\]

Then

\[
\boxed{
b_q(P)\le2qt,
\qquad
E_q(P)\le2q(q-1)t.}
\tag{5.6}
\]

If a route from (P) to (G) uses (s) alternating (C_8)'s, then
(t\le4s), so

\[
\boxed{
b_q(P)\le8qs,
\qquad
E_q(P)\le8q(q-1)s.}
\tag{5.7}
\]

#### Proof

Every exact wreath window (5.1) has rank (m-q).  A (P)-window remains
unchanged if all of its (2q) factor edges remain in (G).  Each removed
(P)-edge belongs to exactly (2q) such cyclic windows, proving the first
inequality in (5.6).  Since gaps have size at least three, a window contains
at most (q-1) inserted-then-deleted returns.  Hence
(E_q(P)\le(q-1)b_q(P)).  This proves (5.6).  Each (C_8) removes four
factor edges, giving (5.7).  ∎

Thus an (O(B))-switch PBBS rebundling requires the genuinely PBBS-specific
Gaussian-depth estimates

\[
b_q(P_m)=O(qB),\qquad E_q(P_m)=O(q^2B).
\tag{5.8}
\]

Component homomesy and the odd-gap rule do not imply (5.8).  To see the
logical obstruction, partition an odd label set into cyclic blocks of odd
sizes, all but (O(1)) of size three, and repeat the labels of each block
(r) times consecutively, with (r>1) odd.  The resulting abstract label
word uses every label (r) times and all consecutive same-label gaps are
odd, but its size-three blocks contribute

\[
E_2=(n-O(1))(r-1)=\Theta(rn).
\]

This word is not asserted to be a realizable simple PBBS orbit.  It proves
exactly that uniform label counts plus odd gaps, without the additional PBBS
bracket order, cannot yield (5.8).

## 6. The depth-two PBBS defect is Catalan

At (q=2), the only charged gap in (5.3) is (g=3), with charge one.
Moreover,

\[
\lambda_i=\lambda_{i+3}
\quad\Longleftrightarrow\quad
A_i\cap A_{i+2}=A_{i+2}\cap A_{i+4}.
\tag{6.1}
\]

Indeed, (5.4) gives

\[
A_i\cap A_{i+2}=A_i\setminus\{\lambda_{i+1}\}.
\]

If (lambda_{i+3}=lambda_i), applying (5.4) once more gives the same set
for (A_{i+2}\cap A_{i+4}); the converse follows by comparing the unique
deleted and inserted coordinates.  These are two adjacent occurrences of
the same PBBS first angle on the step-two cycle.

Every PBBS component has length a positive multiple of (n).  Its
step-two components therefore have length at least (n\ge5).  A set of
(k\le3) vertices in a disjoint union of such cycles spans at most (k-1)
adjacencies.  Applying (2.1) fiber by fiber gives

\[
\boxed{
E_2(P_m)=b_2(P_m)
\le a_2+2a_3
=\frac{2W}{m+2}<4B.}
\tag{6.2}
\]

This is stronger than the cruder all-pairs bound
\(a_2+3a_3\le3W/(m+2)\).

If \(s\) vertex-disjoint clean \(C_8\)'s from Corollary 3.3 are toggled,
the old-edge distance is \(4s\).  At depth one, the PBBS overload stability
bound gives

\[
O_1(G)\le\frac{W}{m+2}+8s.
\tag{6.3}
\]

At depth two, at most four centered four-edge windows are affected by each
removed old edge, and every depth-two rank excess is at most one.  Here
\(E_2(G)\) denotes the sum of
\(\left|\bigcap_{h=0}^2A_{i+2h}\right|-(m-2)\) over the oriented
components of \(G\); reversing a component merely reindexes this sum.
Hence

\[
E_2(G)\le E_2(P_m)+16s
\le\frac{2W}{m+2}+16s.
\tag{6.4}
\]

Thus Catalan-many toggles preserve Catalan first-overload and depth-two
rank-defect scales.  Equations (6.3)--(6.4) do not assert componentwise
balance or depth-two collision balance.

## 7. A fixed-depth PBBS fiber cap

The deficit-((2q+1)) parenthesis structure gives one more exact theorem.

### Theorem 7.1 — correct-fiber cap

For (S\in\binom{[n]}{m-q}), let (U_+(S)) and (U_-(S)) be its
(2q+1) forward and reverse unmatched zeros.  Let
(mu_{P,q}^{\rm corr}(S)) be the number of canonically oriented step-two
PBBS paths

\[
A_0\longrightarrow A_1\longrightarrow\cdots\longrightarrow A_q
\]

with

\[
\bigcap_{j=0}^{q}A_j=S.
\]

Then

\[
\boxed{
\mu_{P,q}^{\rm corr}(S)\le\binom{2q+1}{q}.}
\tag{7.1}
\]

#### Proof

If (A\supset S) is a middle set, it is obtained from the word of (S) by
flipping (q) zeros to ones.  Parenthesis monotonicity says that this can
match old unmatched zeros but cannot create a new unmatched zero.  Hence

\[
r_+(A)\in U_+(S),\qquad r_-(A)\in U_-(S).
\tag{7.2}
\]

The transition (A_{j-1}\to A_j) deletes (r_-(A_j)).  All (A_j)
contain (S), so no deleted label lies in (S).  There are (q) initial
extra labels in (A_0\setminus S) and exactly (q) deletions.  If any
deletion removed a label inserted earlier along the path, one initial extra
label would survive every (A_j), contradicting that their intersection is
exactly (S).  Therefore the deletion labels are distinct and

\[
A_0\setminus S\subset U_-(S).
\]

The \(q\)-subset \(A_0\setminus S\) determines \(A_0\), and PBBS then
determines the oriented path.  There are at most
\(\binom{2q+1}{q}\) choices.  ∎

For \(q=1\), (7.1) recovers the sharp upper bound three.  For \(q=2\), it
gives ten.

As a precise conditional consequence, fix (q) and assume that every PBBS
window has correct rank (m-q) and every rank-((m-q)) target occurs.  For
all sufficiently large (m), (d_q=1).  Since

\[
W-N_q
=\sum_{j=0}^{q-1}
\left[\binom{n}{m-j}-\binom{n}{m-j-1}\right]
\le2q(q+1)B,
\tag{7.3}
\]

and every load lies between one and
(L_q=\binom{2q+1}{q}), one gets

\[
\boxed{
Q_q(P_m)
\le (L_q-2)q(q+1)B.}
\tag{7.4}
\]

The hypotheses of (7.4) are unproved beyond depth one.  Also
(L_q\asymp4^q/\sqrt q), so (7.4) is not useful at
(q=\Theta(\sqrt m)).  The theorem is a genuine fixed-depth result, not a
Gaussian-window claim.

## 8. Why generic centered (C_8) control is at the critical scale

For a balanced exact factor-to-factor (C_8), let
(delta_q=\mu_q(F')-\mu_q(F)).  The audited universal boundary estimate is

\[
\|\delta_q\|_1\le16q,
\qquad
\|\delta_q\|_2^2\le32q.
\tag{8.1}
\]

The balanced overload, being half the (L^1)-distance to the set of
floor/ceiling vectors, satisfies

\[
|O_q(F')-O_q(F)|\le8q.
\tag{8.2}
\]

After (s) switches,

\[
|O_q(F_s)-O_q(F_0)|\le8qs.
\tag{8.3}
\]

Thus (s=O(B)) switches cannot repair a linear-overload Gaussian row: at
(q\asymp\sqrt m), their total capacity is only (O(W/\sqrt m)=o(W)).
Across (H=\lceil A\sqrt m\rceil), one switch changes the aggregate
unweighted overload by at most

\[
8\sum_{q\le H}q=4H(H+1).
\tag{8.4}
\]

Repairing an \(\varepsilon W\) aggregate defect therefore requires at least

\[
\left(\frac{\varepsilon}{2A^2}+o(1)\right)B
\]

switches.  Catalan-many switches are the correct cardinality scale.

However, combining (s=\Theta(B)) with only the triangle or bounded
congestion form of (8.1) gives the critical row bound

\[
Q_q=O(qB),
\]

whose sum through (A\sqrt m) is (O_A(W)), not (o(W)).  Positive
density, vertex disjointness, and centered component balance do not by
themselves produce the factor-(q) cancellation demanded by Theorem 1.1.

There is also a sharp limitation on one simple way of enforcing disjoint
first-shadow supports.  If a family of common cores satisfies

\[
2\le|K\cap K'|\le m-5
\]

pairwise, the known support formula makes their short-trade first-shadow
supports disjoint.  But no ((m-4))-set can lie in two such cores, so

\[
|\mathcal K|\binom{m-1}{3}\le\binom{2m+1}{m-4}.
\]

Consequently

\[
\frac{|\mathcal K|}{B}
\le
\frac{6(2m+1)m}{(m+2)(m+3)(m+4)(m+5)}
=\frac{12+o(1)}{m^2}.
\tag{8.5}
\]

This rules out the separated-core certificate as a positive-density
strategy.  It does not rule out candidate-specific disjointness or signed
cancellation among close cores.

## 9. A constant-curvature exact (C_8)-cube lemma

The generic (O(q)) curvature in (8.1) is not inevitable.  The explicit
MSW-orbit (C_8) cell has increment norms

\[
\|\delta_{i,1}\|_2^2=4,
\qquad
\|\delta_{i,q}\|_2^2=8
\quad(2\le q\le m-2).
\tag{9.1}
\]

This gives a nontrivial exact-factor composition lemma.

### Theorem 9.1 — exact cube rounding with constant row toll

Suppose one exact factor contains \(s\) row-disjoint explicit MSW \(C_8\)
cells.  Every subset of the cells may be toggled, and all \(2^s\) vertices
of the resulting cube are literal exact factors.  Let \(a_q\) be the
midpoint of their depth-\(q\) histograms and extend (1.1) to real histograms
by the same quadratic formula, denoting it by
\(\widetilde Q_q(a_q)\).  Then for independent signs \(\varepsilon_i\),

\[
\boxed{
\mathbb E Q_q
=\widetilde Q_q(a_q)
+\frac18\sum_{i=1}^{s}\|\delta_{i,q}\|_2^2.}
\tag{9.2}
\]

The rounding toll is \(s/2\) at depth one and \(s\) at every depth
\(2\le q\le m-2\).

If, for each fixed \(A\), such a cube has

\[
\widetilde Q_q(a_q)\le C_AB
\qquad(1\le q\le\lceil A\sqrt m\rceil),
\tag{9.3}
\]

then one cube vertex has

\[
\sum_{q\le\lceil A\sqrt m\rceil}\frac{Q_q}{d_q}
=O_A\!\left(\frac W{\sqrt m}\right)=o(W),
\tag{9.4}
\]

and the same slow diagonal used in the proof of Theorem 1.1 proves the
constant-one theorem.

#### Proof

Write

\[
\mu_q(\varepsilon)=a_q+\frac12\sum_i\varepsilon_i\delta_{i,q}.
\]

Independence and mean-zero signs annihilate all cross terms in the quadratic
(1.1), proving (9.2).  Formula (9.1) gives the stated tolls.  Row
disjointness uses two wreath rows per cell, so \(2s\le B\).  Sum (9.2) over
the fixed window with weights \(1/d_q\le1\).  The expected aggregate is
\(O_A(HB)=O_A(W/\sqrt m)\); at least one integral cube vertex is no larger
than its expectation.  Apply the literal transfer (1.6) and the same slow
diagonal used in Theorem 1.1.  ∎

Theorem 9.1 is a proved exact composition lemma, but (9.3) is not supplied
by PBBS rebundling.  The clean PBBS cycles in Corollary 3.3 are not shown to
be exact-factor cells, to have the telescoping norm (9.1), or to have a low
common midpoint.  These distinctions are essential.

## 10. Exact implication scope and remaining lemmas

The proved lane-R conclusions are:

1. Catalan collision excess on every row of one common fixed-window exact
   factor quantitatively implies the sharp constant-one OR theorem.
2. PBBS itself has \(Q_1<2B\).
3. Every PBBS load-one core supplies a clean alternating \(C_8\), giving
   \(\Omega(W)\) candidates and at least
   \((1/64-o(1))B\) vertex-disjoint simultaneous toggles.
4. The exact all-depth PBBS short-return charge is (5.3), and every sparse
   exact rebundling must satisfy (5.6)--(5.8).
5. PBBS satisfies the first nontrivial bound
   \(E_2=b_2<4B\).
6. Correct fixed-depth PBBS fibers have the integral cap (7.1).
7. A special exact (C_8) cube with constant multirank curvature would
   compose into constant one by Theorem 9.1.

The following statements remain **unproved**:

1. A positive-density subfamily of the clean PBBS \(C_8\)'s whose joint
   symmetric difference is componentwise point-regular and makes net
   progress from long PBBS components toward wreaths.
2. A quantitative topology/cancellation theorem pairing the compulsory
   vectors (4.2) inside each new component.  The global rotation sum (4.3)
   is not enough.
3. An exact factor at \(O(B)\), or even \(o(W)\), edge distance from PBBS.
4. Gaussian-depth estimates \(E_q=O_A(q^2B)\), correct-rank coverage, and
   Catalan collision excess for PBBS local windows.
5. Catalan added-color pair congestion under a balanced rebundling route.
6. A PBBS-derived exact \(C_8\) cube satisfying the constant-curvature and
   midpoint conditions of Theorem 9.1.

Accordingly, this report proves the missing clean-cycle density theorem and
an exact depth-two PBBS bound, but not positive-density **balanced**
rebundling, an exact low-collision wreath factor, MWB, labelled
synchronization, or the coefficient-one theorem itself.

The clean-cycle theorem and the short-return theorem were independently
audited from their definitions, including the (128m) packing constant,
the cyclic-type classification, the gap multiplicities, and the edge-distance
constants.
